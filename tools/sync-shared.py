#!/usr/bin/env python3
"""Copy canonical shared references into the skills that declare them.

`npx skills` installs one skill directory and nothing else, so a skill cannot
reference a file belonging to another skill — a mentee simply will not have it.
Anything two skills both need therefore has to exist in both directories.

The obvious way to do that is to copy it by hand, and this repo has already been
burned three times by exactly that: a 49 KB duplicated examples doc, a divergent
hand-made Codex skill, and a hand-maintained Gemini prompt. Each was two copies
of one truth kept in sync by a human, and each drifted.

So the copies are generated. `shared/` holds the canonical text; this script
writes it into each skill's `references/` with a GENERATED header. Edit the
canonical file and re-run; never edit the copies.

Usage:
    python3 tools/sync-shared.py            # write the copies
    python3 tools/sync-shared.py --check    # verify they are current (CI/pre-publish)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SHARED = REPO / "shared"
SKILLS = REPO / "skills"

# Which skills receive which shared references.
SHARED_REFS: dict[str, list[str]] = {
    "project-registry.md": [
        "basecamp-todo-coach",
        "basecamp-initiative-reporter",
    ],
    "local-context.md": [
        "basecamp-todo-coach",
        "basecamp-initiative-reporter",
    ],
}

HEADER = (
    "<!-- GENERATED from shared/{name} by tools/sync-shared.py — do not edit.\n"
    "     Edit the canonical file and re-run the script. Both skills carry a copy\n"
    "     because npx skills installs one skill directory and nothing else. -->\n\n"
)


def rendered(name: str) -> str:
    source = SHARED / name
    if not source.exists():
        sys.exit(f"error: missing canonical source shared/{name}")
    return HEADER.format(name=name) + source.read_text()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit non-zero if any copy is missing or out of date; write nothing",
    )
    args = parser.parse_args()

    stale: list[str] = []
    written = 0

    for name, skills in SHARED_REFS.items():
        body = rendered(name)
        for skill in skills:
            target = SKILLS / skill / "references" / name
            if not target.parent.is_dir():
                sys.exit(f"error: no such skill directory: skills/{skill}/references/")

            current = target.read_text() if target.exists() else None
            rel = target.relative_to(REPO)

            if current == body:
                print(f"  ok      {rel}")
                continue

            if args.check:
                stale.append(str(rel))
                print(f"  STALE   {rel}")
                continue

            target.write_text(body)
            written += 1
            print(f"  {'updated' if current is not None else 'created'} {rel}")

    if args.check and stale:
        print(
            f"\nerror: {len(stale)} generated copy/copies out of date. "
            "Run: python3 tools/sync-shared.py",
            file=sys.stderr,
        )
        return 1

    if args.check:
        print("\nAll shared references are current.")
    else:
        print(f"\nDone. {written} file(s) written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
