#!/usr/bin/env python3
"""Validate packages and all generated distribution inputs without writing files."""

import json
import runpy
import subprocess
import sys
from skill_catalog import REPO, CatalogError, check_package, discover


def main() -> int:
    errors = []
    try:
        skills = discover()
    except CatalogError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    for skill in skills.values():
        errors.extend(check_package(skill))
        if skill.category == "uncategorized":
            errors.append(f"{skill.name}: missing category")
        for key in ("version", "display-name", "modes"):
            if not skill.metadata.get(key):
                errors.append(f"{skill.name}: missing metadata.{key}")
        for companion in skill.values("companions"):
            if companion not in skills:
                errors.append(f"{skill.name}: unknown companion {companion}")
        optional_metadata = skill.path / "agents/openai.yaml"
        if optional_metadata.exists():
            import yaml
            config = yaml.safe_load(optional_metadata.read_text(encoding="utf-8"))
            if not isinstance(config, dict) or not isinstance(config.get("interface"), dict):
                errors.append(f"{skill.name}: invalid OpenAI metadata")
    for command in ("sync-shared.py", "build-registry.py"):
        result = subprocess.run([sys.executable, str(REPO / "tools" / command), "--check"], capture_output=True, text=True)
        if result.returncode:
            errors.append(result.stdout + result.stderr)
    try:
        module = runpy.run_path(str(REPO / "tools/build-web-prompt.py"))
        for name, config in module["BUNDLES"].items():
            bundle = module["Bundle"](name, config)
            for target_name, target in config["targets"].items():
                bundle.check_coverage(target)
                instructions = bundle.build_instructions(target_name, target)
                bundle.build_reference(target)
                bundle.build_examples()
                if target["hard_limit"] and len(instructions) > target["limit"]:
                    errors.append(f"{name}/{target_name}: instruction budget exceeded")
    except (ValueError, CatalogError, KeyError, SystemExit) as exc:
        errors.append(f"Browser bundle: {exc}")
    for path in (REPO / "adapters").rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except ValueError as exc:
            errors.append(f"{path}: {exc}")
    if errors:
        print("\n".join(f"error: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated {len(skills)} skills: metadata, references, shared copies, catalog, browser coverage and budgets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
