"""Discover and validate canonical packages; shared by maintenance commands."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

try:
    import yaml
except ImportError:
    raise SystemExit("Install maintenance dependencies: python -m pip install -r requirements-dev.txt")

REPO = Path(__file__).resolve().parent.parent
CATEGORIES = {
    "hiring": "Hiring",
    "process-analysis": "Process analysis",
    "project-management": "Project management",
    "appsheet": "AppSheet",
    "communication": "Communication",
}
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


class CatalogError(ValueError):
    pass


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str) or key in result:
            raise CatalogError(f"Invalid or duplicate YAML key: {key!r}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise CatalogError(f"{path}: missing YAML frontmatter")
    try:
        data = yaml.load(match[1], Loader=UniqueLoader)
    except yaml.YAMLError as exc:
        raise CatalogError(f"{path}: invalid YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise CatalogError(f"{path}: frontmatter must be a mapping")
    return data


@dataclass(frozen=True)
class Skill:
    path: Path
    name: str
    description: str
    category: str
    metadata: dict[str, str]

    def values(self, key: str) -> list[str]:
        return [part.strip() for part in self.metadata.get(key, "").split(",") if part.strip()]


def discover(repo: Path = REPO) -> dict[str, Skill]:
    container = repo / "skills"
    paths = sorted(container.rglob("SKILL.md")) if container.is_dir() else []
    if not paths:
        raise CatalogError(f"No skills found in {container}")
    if (repo / "SKILL.md").exists() or (container / "SKILL.md").exists():
        raise CatalogError("A root SKILL.md would shadow the skill catalog")
    skills: dict[str, Skill] = {}
    package_roots = {path.parent for path in paths}
    for path in paths:
        relative = path.parent.relative_to(container)
        if len(relative.parts) not in (1, 2):
            raise CatalogError(f"{path}: use skills/<category>/<name>/SKILL.md")
        if any(parent in package_roots for parent in path.parent.parents):
            raise CatalogError(f"{path}: nested inside another skill")
        data = frontmatter(path)
        name, description = data.get("name"), data.get("description")
        if not isinstance(name, str) or not SLUG.fullmatch(name) or len(name) > 64:
            raise CatalogError(f"{path}: invalid skill name")
        if name != path.parent.name:
            raise CatalogError(f"{path}: folder and frontmatter name differ")
        if name in skills:
            raise CatalogError(f"Duplicate skill name: {name}")
        if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
            raise CatalogError(f"{path}: description must contain 1–1024 characters")
        metadata = data.get("metadata", {})
        if not isinstance(metadata, dict) or any(not isinstance(v, str) for v in metadata.values()):
            raise CatalogError(f"{path}: metadata values must be strings")
        category = relative.parts[0] if len(relative.parts) == 2 else "uncategorized"
        if category != "uncategorized" and category not in CATEGORIES:
            raise CatalogError(f"{path}: unknown category {category}")
        skills[name] = Skill(path.parent, name, description.strip(), category, metadata)
    aliases = {}
    for skill in skills.values():
        for alias in skill.values("renamed-from"):
            if not SLUG.fullmatch(alias) or alias in skills or alias in aliases:
                raise CatalogError(f"Ambiguous rename alias: {alias}")
            aliases[alias] = skill.name
    return skills


def resolve(name: str, repo: Path = REPO) -> Skill:
    skills = discover(repo)
    if name in skills:
        return skills[name]
    for skill in skills.values():
        if name in skill.values("renamed-from"):
            return skill
    raise CatalogError(f"Unknown skill {name!r}; available: {', '.join(skills)}")


def contained(path: Path, root: Path) -> bool:
    return path.resolve().is_relative_to(root.resolve())


def check_package(skill: Skill) -> list[str]:
    """Check executable links and explicit bundled-resource references, not prose citations."""
    errors = []
    for file in skill.path.rglob("*"):
        if not contained(file, skill.path):
            errors.append(f"{file}: symlink escapes package")
            continue
        if not file.is_file() or file.suffix != ".md":
            continue
        text = file.read_text(encoding="utf-8")
        prose = re.sub(r"(?ms)^```[^\n]*\n.*?^```[ \t]*$", "", text)
        prose = re.sub(r"`[^`\n]+`", "", prose)
        references = re.findall(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)", prose)
        references += re.findall(r"`((?:references|evals|assets|scripts)/[^`\n]+\.[a-zA-Z0-9]+)`", text)
        for reference in set(references):
            if re.match(r"[a-z][a-z0-9+.-]*:", reference) or reference.startswith("#"):
                continue
            reference = reference.split("#", 1)[0]
            # SKILL.md paths are package-relative; references may use sibling links.
            candidates = [file.parent / reference, skill.path / reference]
            if not any(contained(p, skill.path) and p.exists() for p in candidates):
                errors.append(f"{file}: missing or escaping reference {reference}")
    return errors
