#!/usr/bin/env python3
"""Maintainer links only; mentees use npx skills add. Never replace real directories."""

from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
from skill_catalog import REPO, CatalogError, Skill, discover, resolve


def owned_link(path: Path, skill: Skill, repo: Path = REPO) -> bool:
    if not path.is_symlink():
        return False
    expected = {skill.path.resolve()}
    expected.update((repo / "skills" / old).resolve() for old in skill.values("renamed-from"))
    # Resolve the link payload explicitly: Windows may leave a dangling link
    # unresolved and readlink may return an extended-length path prefix.
    raw = str(path.readlink())
    if raw.startswith("\\\\?\\"):
        raw = raw[4:]
    return (path.parent / raw).resolve() in expected


def link_skill(root: Path, skill: Skill, *, repo: Path = REPO, dry_run=False,
               unlink=False, replace_link=False) -> Counter:
    counts = Counter()
    target = root / skill.name

    def remove(path):
        print(f"  {'would remove' if dry_run else 'remove'} {path}")
        if not dry_run:
            path.unlink()
        counts["removed"] += 1

    if unlink:
        for name in [skill.name, *skill.values("renamed-from")]:
            path = root / name
            if owned_link(path, skill, repo):
                remove(path)
            elif path.exists() or path.is_symlink():
                print(f"  skip {path} (not owned by this checkout)")
                counts["skipped"] += 1
        return counts
    if target.is_symlink():
        if target.resolve() == skill.path.resolve():
            counts["unchanged"] += 1
        elif owned_link(target, skill, repo) or replace_link:
            remove(target)
        else:
            print(f"  skip {target} (foreign symlink; --replace-link is explicit opt-in)")
            counts["skipped"] += 1
            return counts
    elif target.exists():
        print(f"  skip {target} (real file or directory)")
        counts["skipped"] += 1
        return counts
    if not counts["unchanged"]:
        print(f"  {'would link' if dry_run else 'link'} {target} -> {skill.path}")
        if not dry_run:
            root.mkdir(parents=True, exist_ok=True)
            target.symlink_to(skill.path, target_is_directory=True)
        counts["linked"] += 1
    for old in skill.values("renamed-from"):
        path = root / old
        if owned_link(path, skill, repo):
            remove(path)
        elif path.exists() or path.is_symlink():
            print(f"  retain {path} (old install is not owned by this checkout)")
            counts["skipped"] += 1
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skills", nargs="*")
    parser.add_argument("--skill", action="append", default=[])
    parser.add_argument("--agent", action="append", default=[])
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--unlink", action="store_true")
    parser.add_argument("--replace-link", action="store_true")
    parser.add_argument("--repair-renames", action="store_true", help="only repair existing checkout-owned installs")
    args = parser.parse_args()
    try:
        available = discover()
        requested = args.skills + args.skill
        skills = list({resolve(name).name: resolve(name) for name in requested}.values()) if requested else list(available.values())
        hosts = json.loads((REPO / "adapters/hosts.json").read_text(encoding="utf-8"))
        if any(name not in hosts for name in args.agent):
            raise CatalogError(f"Unknown agent; choose from {', '.join(hosts)}")
    except CatalogError as exc:
        parser.exit(2, f"error: {exc}\n")
    if args.list:
        for skill in skills:
            print(f"{skill.name} ({skill.category})")
        return 0
    if args.repair_renames and (args.unlink or args.replace_link):
        parser.error("--repair-renames cannot be combined with --unlink or --replace-link")
    user_dir = Path.home()
    selected = args.agent or list(hosts)
    plans = {}
    for name in selected:
        roots = [user_dir / rel for rel in hosts[name]["roots"]]
        preferred = roots[0] if args.agent else next((p for p in roots if p.is_dir()), None)
        if preferred:
            plans.setdefault(preferred, set()).update(roots)
    if not plans:
        parser.exit(1, "No existing skill roots; use --agent to choose a destination explicitly.\n")
    total = Counter()
    for skill in skills:
        for root, alternatives in plans.items():
            names = [skill.name, *skill.values("renamed-from")]
            if args.repair_renames and not any(owned_link(p / n, skill) for p in alternatives for n in names):
                continue
            print(skill.name)
            counts = link_skill(root, skill, dry_run=args.dry_run, unlink=args.unlink, replace_link=args.replace_link)
            total.update(counts)
            if counts["skipped"]:
                continue
            for alternative in sorted(alternatives):
                if alternative != root:
                    total.update(link_skill(alternative, skill, dry_run=args.dry_run, unlink=True))
    print(("Dry run: " if args.dry_run else "Done: ") + ", ".join(f"{key}={total[key]}" for key in ["linked", "unchanged", "removed", "skipped"]))
    return 1 if total["skipped"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
