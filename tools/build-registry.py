#!/usr/bin/env python3
"""Generate the Toolkit inventory from canonical skill metadata."""

import argparse
import json
from skill_catalog import CATEGORIES, REPO, CatalogError, discover


def render() -> str:
    skills = discover()
    data = {
        "schemaVersion": 1,
        "generatedBy": "tools/build-registry.py",
        "categories": [
            {"id": key, "label": label, "status": "available" if any(s.category == key for s in skills.values()) else "planned"}
            for key, label in CATEGORIES.items()
        ],
        "skills": [
            {
                "id": skill.name,
                "name": skill.metadata["display-name"],
                "description": skill.description,
                "version": skill.metadata["version"],
                "category": skill.category,
                "tags": skill.values("tags"),
                "path": skill.path.relative_to(REPO).as_posix(),
                "modes": skill.values("modes"),
                "requires": skill.values("requires"),
                "optional": skill.values("optional"),
                "companions": skill.values("companions"),
                "renamedFrom": skill.values("renamed-from"),
            }
            for skill in sorted(skills.values(), key=lambda s: (s.category, s.name))
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    path = REPO / "registry/skills.json"
    try:
        text = render()
    except (CatalogError, KeyError) as exc:
        parser.exit(1, f"error: {exc}\n")
    if args.check:
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            parser.exit(1, "Registry is stale; run python tools/build-registry.py\n")
        print("Registry is current.")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print("Generated registry/skills.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
