"""Regression checks for discovery, self-contained installs, and adapter coverage."""

import contextlib
import copy
import importlib.util
import io
from pathlib import Path
import runpy
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from skill_catalog import CatalogError, check_package, discover

spec = importlib.util.spec_from_file_location("install_global", ROOT / "tools/install-global.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)

    def skill(self, relative="hiring/interview-prep", extra=""):
        folder = self.repo / "skills" / relative
        folder.mkdir(parents=True)
        name = folder.name
        (folder / "SKILL.md").write_text(f"---\nname: {name}\ndescription: Test interview preparation.\nmetadata:\n  renamed-from: candidate-interview-coach\n---\n\n{extra}", encoding="utf-8")
        return folder

    def symlink(self, path, target):
        try:
            path.symlink_to(target, target_is_directory=True)
        except OSError as exc:
            self.skipTest(f"Symlinks unavailable on this runner: {exc}")

    def test_mixed_layout_keeps_nested_skill(self):
        self.skill()
        flat = self.skill("todo-planner")
        text = (flat / "SKILL.md").read_text().replace("candidate-interview-coach", "basecamp-todo-coach")
        (flat / "SKILL.md").write_text(text)
        self.assertEqual(set(discover(self.repo)), {"interview-prep", "todo-planner"})

    def test_duplicate_name_fails_instead_of_silently_shadowing(self):
        self.skill()
        self.skill("project-management/interview-prep")
        with self.assertRaisesRegex(CatalogError, "Duplicate"):
            discover(self.repo)

    def test_empty_discovery_fails(self):
        with self.assertRaisesRegex(CatalogError, "No skills"):
            discover(self.repo)

    def test_duplicate_yaml_key_fails(self):
        folder = self.skill()
        path = folder / "SKILL.md"
        path.write_text(path.read_text().replace("description:", "name: conflicting-name\ndescription:"))
        with self.assertRaisesRegex(CatalogError, "duplicate YAML"):
            discover(self.repo)

    def test_missing_and_escaping_resources_fail(self):
        self.skill(extra="Read [missing](references/missing.md) and [outside](../../outside.md).")
        self.assertEqual(len(check_package(discover(self.repo)["interview-prep"])), 2)

    def test_owned_old_link_is_replaced_after_new_link_succeeds(self):
        folder = self.skill()
        root = self.repo / "installed"; root.mkdir()
        old = root / "candidate-interview-coach"
        self.symlink(old, self.repo / "skills/candidate-interview-coach")
        skill = discover(self.repo)["interview-prep"]
        with contextlib.redirect_stdout(io.StringIO()):
            installer.link_skill(root, skill, repo=self.repo)
        self.assertFalse(old.is_symlink())
        self.assertEqual((root / skill.name).resolve(), folder.resolve())

    def test_foreign_symlink_is_not_unlinked_or_replaced(self):
        self.skill()
        root = self.repo / "installed"; root.mkdir()
        target = root / "interview-prep"
        elsewhere = self.repo / "unrelated"; elsewhere.mkdir()
        self.symlink(target, elsewhere)
        skill = discover(self.repo)["interview-prep"]
        with contextlib.redirect_stdout(io.StringIO()):
            result = installer.link_skill(root, skill, repo=self.repo)
            installer.link_skill(root, skill, repo=self.repo, unlink=True)
        self.assertEqual(result["skipped"], 1)
        self.assertEqual(target.resolve(), elsewhere.resolve())

    def test_real_directory_survives_explicit_link_replacement(self):
        self.skill()
        root = self.repo / "installed"; root.mkdir()
        target = root / "interview-prep"; target.mkdir()
        (target / "notes.txt").write_text("local edits")
        with contextlib.redirect_stdout(io.StringIO()):
            installer.link_skill(root, discover(self.repo)["interview-prep"], repo=self.repo, replace_link=True)
        self.assertEqual((target / "notes.txt").read_text(), "local edits")

    def test_dry_run_makes_no_changes(self):
        self.skill()
        target = self.repo / "not-created"
        with contextlib.redirect_stdout(io.StringIO()):
            installer.link_skill(target, discover(self.repo)["interview-prep"], repo=self.repo, dry_run=True)
        self.assertFalse(target.exists())

    def test_bundle_fails_if_workflow_router_is_omitted(self):
        module = runpy.run_path(str(ROOT / "tools/build-web-prompt.py"))
        config = copy.deepcopy(module["BUNDLES"]["todo-planner"])
        target = config["targets"]["gpt"]
        target["reference"] = [row for row in target["reference"] if row[0] != "SKILL.md"]
        with self.assertRaisesRegex(ValueError, "Workflows"):
            module["Bundle"]("todo-planner", config).check_coverage(target)

    def test_real_packages_are_self_contained(self):
        for skill in discover(ROOT).values():
            self.assertEqual(check_package(skill), [], skill.name)


if __name__ == "__main__":
    unittest.main()
