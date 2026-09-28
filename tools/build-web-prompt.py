#!/usr/bin/env python3
"""Bundle a skill into paste-ready prompts for browser chat agents.

Coding agents install a skill directly with `npx skills` and load references on demand.
Browser chat does, and the budgets differ enough that one bundle cannot serve
every destination, so each skill declares manifests in adapters/web-chat/.

Each target emits an instruction tier to paste into the assistant's instruction
box, plus knowledge files to upload as attachments. Whole files are never
concatenated blindly — a target names the `##` sections it takes, so a budget
overrun is fixed by moving a named section between tiers rather than truncating
prose, and a renamed heading fails the build loudly instead of silently
dropping a section.

Output goes to dist/<skill>/<target>/.

Usage:
    python3 tools/build-web-prompt.py
    python3 tools/build-web-prompt.py --skill todo-planner
    python3 tools/build-web-prompt.py --skill todo-planner --target gem
    python3 tools/build-web-prompt.py --list

Adding a skill: add adapters/web-chat/<skill>.json. A skill with no manifest is simply
not bundled for browser chat, which is fine — not every skill needs to be.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from skill_catalog import REPO, discover, resolve

DIST = REPO / "dist"

ALL_SECTIONS = "*"

# Carried over from the hand-written Gem instruction, which has been silently
# truncated on paste before. Kept as the last line of every instruction tier so
# a truncated paste is detectable rather than mysterious.
def end_marker(target_name: str, fallback: str | None) -> str:
    fix = (
        f" Use the {fallback} bundle instead."
        if fallback and target_name != fallback
        else " Re-paste; if it truncates again, report it."
    )
    return (
        "\n(End of instruction — if this line is missing after pasting, the text "
        f"was truncated.{fix})\n"
    )


def load_bundles() -> dict:
    return {path.stem: json.loads(path.read_text(encoding="utf-8"))
            for path in sorted((REPO / "adapters/web-chat").glob("*.json"))}


BUNDLES = load_bundles()


class Bundle:
    """One skill's bundling config, with paths resolved against its directory."""

    def __init__(self, name: str, config: dict):
        self.name = name
        self.config = config
        self.dir = resolve(name).path

    def path(self, relative: str) -> Path:
        return self.dir / relative

    @property
    def targets(self) -> dict:
        return self.config["targets"]

    def placement(self, target: dict) -> dict[str, str]:
        """Which tier each referenced file landed in, for this target.

        A file can be split across both tiers, so the wording has to
        distinguish all three cases — otherwise the bundle tells the agent to
        open an upload for content sitting in its own instructions.
        """
        tiers: dict[str, set[str]] = {}
        for tier in ("instructions", "reference"):
            for rel, _, _ in target[tier]:
                tiers.setdefault(rel, set()).add(tier)
        return {
            rel: ("both" if len(where) > 1 else next(iter(where)))
            for rel, where in tiers.items()
        }

    def reference_holds(self, target: dict) -> str:
        """Name what actually landed in the reference upload, for this target."""
        where = self.placement(target)
        parts = [
            label
            for rel, label in self.config["ref_labels"].items()
            if where.get(rel) in ("reference", "both")
        ]
        if not parts:
            return "supporting reference material"
        if len(parts) == 1:
            return parts[0]
        return ", ".join(parts[:-1]) + f", and {parts[-1]}"

    def rewrite(self, text: str, where: dict[str, str] | None = None) -> str:
        """Retarget cross-references at the bundle, not at files that aren't there.

        In the installed skill these are files the agent can open. In browser
        chat they are either sections of the pasted instructions or uploaded
        attachments, so the wording must match where the content actually went.
        """
        where = where or {}
        for token, replacement in self.config["always_replace"].items():
            text = text.replace(token, replacement)
        for token, (rel, wording) in self.config["tokens"].items():
            text = text.replace(token, wording[where.get(rel, "reference")])
        return text

    def select(
        self, relative: str, wanted: object, excluded: list[str], where: dict[str, str]
    ) -> str:
        """Pull the requested `##` sections out of one source file."""
        path = self.path(relative)
        if not path.exists():
            sys.exit(f"error: missing source {path.relative_to(REPO)}")

        text = self.rewrite(
            strip_generated_header(strip_frontmatter(path.read_text(encoding="utf-8"))), where
        )
        preamble, sections = split_sections(text)
        available = {title for title, _ in sections}

        def missing(name: str, what: str) -> None:
            sys.exit(
                f"error: {self.name}/{relative} has no section '{name}'{what}. "
                f"A heading was renamed — update the adapter manifest."
            )

        if wanted == ALL_SECTIONS:
            for name in excluded:
                if name not in available:
                    missing(name, " to exclude")
            chosen = [body for title, body in sections if title not in excluded]
            head = preamble.strip()  # keep the file's intro only when taking it whole
            return "\n\n".join(([head] if head else []) + [b.strip() for b in chosen])

        for name in wanted:  # type: ignore[union-attr]
            if name not in available:
                missing(name, "")
        by_title = dict(sections)
        return "\n\n".join(by_title[name].strip() for name in wanted)  # type: ignore[union-attr]

    def check_coverage(self, target: dict) -> None:
        """Every source section must be emitted once or intentionally excluded."""
        for relative in self.config["coverage_files"]:
            _, sections = split_sections(strip_frontmatter(self.path(relative).read_text(encoding="utf-8")))
            titles = [title for title, _ in sections]
            if len(titles) != len(set(titles)):
                raise ValueError(f"{relative}: duplicate section headings")
            emitted = []
            for tier in ("instructions", "reference"):
                for rel, wanted, excluded in target[tier]:
                    if rel != relative:
                        continue
                    emitted.extend([title for title in titles if title not in excluded]
                                   if wanted == ALL_SECTIONS else wanted)
            exclusions = target.get("exclude", {}).get(relative, {})
            if any(not reason.strip() for reason in exclusions.values()):
                raise ValueError(f"{relative}: exclusions need a reason")
            missing = set(titles) - set(emitted) - set(exclusions)
            unknown = (set(emitted) | set(exclusions)) - set(titles)
            duplicate = {title for title in emitted if emitted.count(title) > 1}
            overlap = set(emitted) & set(exclusions)
            if missing or unknown or duplicate or overlap:
                raise ValueError(f"{relative}: coverage error; missing={sorted(missing)}, "
                                 f"unknown={sorted(unknown)}, duplicate={sorted(duplicate)}, "
                                 f"emitted-and-excluded={sorted(overlap)}")

    def build_instructions(self, target_name: str, target: dict) -> str:
        where = self.placement(target)
        chunks = [
            f"# {self.config['title']} — Web Chat Instructions\n\n",
            "<!-- GENERATED by tools/build-web-prompt.py — do not edit. "
            f"Edit {self.dir.relative_to(REPO).as_posix()}/, then rebuild. -->\n\n",
            self.config["paste_header"].format(
                reference_holds=self.reference_holds(target)
            ),
        ]
        for rel, wanted, excluded in target["instructions"]:
            chunks.append(f"\n\n---\n\n{self.select(rel, wanted, excluded, where)}\n")
        chunks.append(end_marker(target_name, self.config.get("fallback_target")))
        return "".join(chunks)

    def build_reference(self, target: dict) -> str:
        where = self.placement(target)
        chunks = [
            "<!-- GENERATED by tools/build-web-prompt.py — do not edit. -->\n",
            "<!-- Upload as a knowledge / attached file, not as system instructions. -->\n\n",
            f"# {self.config['title']} — Reference\n",
        ]
        for rel, wanted, excluded in target["reference"]:
            chunks.append(f"\n\n---\n\n{self.select(rel, wanted, excluded, where)}\n")
        return "".join(chunks)

    def build_examples(self) -> str | None:
        rel = self.config.get("examples")
        if not rel:
            return None
        path = self.path(rel)
        if not path.exists():
            sys.exit(f"error: missing {path.relative_to(REPO)}")
        return (
            "<!-- GENERATED by tools/build-web-prompt.py from "
            f"{self.dir.relative_to(REPO).as_posix()}/{rel} — do not edit. -->\n"
            "<!-- Upload as a knowledge / attached file, not as system instructions. -->\n\n"
            + self.rewrite(path.read_text(encoding="utf-8"))
        )


def strip_frontmatter(text: str) -> str:
    """Drop a leading YAML frontmatter block. Web agents have no use for it."""
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    return text[end + 5 :] if end != -1 else text


def strip_generated_header(text: str) -> str:
    lines = text.splitlines(keepends=True)
    if lines and lines[0].lstrip().startswith("<!-- GENERATED"):
        return "".join(lines[1:]).lstrip("\n")
    return text


def split_sections(text: str) -> tuple[str, list[tuple[str, str]]]:
    """Split on `##` headings into (preamble, [(heading_title, body)])."""
    parts = re.split(r"^(## .*)$", text, flags=re.M)
    sections = [
        (parts[i][3:].strip(), parts[i] + parts[i + 1]) for i in range(1, len(parts), 2)
    ]
    return parts[0], sections


def installed_skills() -> list[str]:
    """Every skill directory present, bundled or not."""
    return sorted(discover())


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--skill",
        action="append",
        help="build only this skill (repeatable); default is every bundled skill",
    )
    parser.add_argument(
        "--target",
        action="append",
        help="build only this target (repeatable); default is every target",
    )
    parser.add_argument(
        "--list", action="store_true", help="list skills and their bundle targets"
    )
    args = parser.parse_args()

    present = installed_skills()
    unbundled = [s for s in present if s not in BUNDLES]

    if args.list:
        print("Skills in skills/:")
        for name in present:
            targets = (
                ", ".join(sorted(BUNDLES[name]["targets"])) if name in BUNDLES else "—"
            )
            print(f"  {name:<28} web targets: {targets}")
        if unbundled:
            print(
                "\nNot bundled for browser chat (no BUNDLES entry): "
                + ", ".join(unbundled)
            )
        return 0

    skill_names = [resolve(name).name for name in args.skill] if args.skill else sorted(BUNDLES)
    for name in skill_names:
        if name not in BUNDLES:
            hint = (
                f" It exists in skills/ but has no BUNDLES entry."
                if name in present
                else ""
            )
            print(f"error: no bundle config for skill '{name}'.{hint}", file=sys.stderr)
            return 2

    over_hard_limit: list[str] = []

    for name in skill_names:
        bundle = Bundle(name, BUNDLES[name])
        examples = bundle.build_examples()
        target_names = args.target or sorted(bundle.targets)
        for tname in target_names:
            if tname not in bundle.targets:
                print(
                    f"error: skill '{name}' has no target '{tname}'. "
                    f"Available: {', '.join(sorted(bundle.targets))}",
                    file=sys.stderr,
                )
                return 2

        print(f"\n{name}")
        for tname in target_names:
            target = bundle.targets[tname]
            out = DIST / name / tname
            out.mkdir(parents=True, exist_ok=True)

            bundle.check_coverage(target)
            instructions = bundle.build_instructions(tname, target)
            reference = bundle.build_reference(target)
            (out / "system_instructions.md").write_text(instructions, encoding="utf-8")
            (out / "knowledge_reference.md").write_text(reference, encoding="utf-8")
            if examples is not None:
                (out / "knowledge_examples.md").write_text(examples, encoding="utf-8")

            limit, size = target["limit"], len(instructions)
            fits = size <= limit
            cap = "hard cap" if target["hard_limit"] else "budget"
            print(f"  {tname} — {target['label']}")
            print(
                f"    system_instructions.md  {size:>7,} chars  "
                f"[{cap} {limit:,}: {'fits' if fits else 'OVER'}]"
            )
            print(f"    knowledge_reference.md  {len(reference):>7,} chars  [upload as file]")
            if examples is not None:
                print(f"    knowledge_examples.md   {len(examples):>7,} chars  [upload as file]")
            if not fits:
                print(
                    f"    → over by {size - limit:,} chars. Move a named section "
                    f"from 'instructions' to 'reference' in BUNDLES; "
                    f"do not truncate prose."
                )
                if target["hard_limit"]:
                    over_hard_limit.append(f"{name}/{tname}")

    if unbundled and not args.skill:
        print(
            "\nNote: no browser-chat bundle for "
            + ", ".join(unbundled)
            + " (no BUNDLES entry). Coding-agent installs are unaffected."
        )

    if over_hard_limit:
        print(
            f"\nerror: {', '.join(over_hard_limit)} exceeded a hard cap — "
            "the bundle will not paste.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
