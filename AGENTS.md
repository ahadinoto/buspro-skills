# Working in this repo

- Canonical installable packages live at `skills/<category>/<skill>/`.
- Keep every package self-contained: references must resolve inside its leaf.
- Record behavior decisions in the skill's `docs/` quality-system-tracker before
  changing instructions. Existing documentation folder names are stable history.
- Keep canonical content agent-neutral. Host paths belong in `adapters/hosts.json`;
  browser transforms belong in `adapters/web-chat/`.
- Category directories and the repository root must not contain `SKILL.md`.
- Use short capability names, lowercase with hyphens; name must match the folder.
- Shared text is canonical in `shared/`. Declare `metadata.shared-references`,
  then run `tools/sync-shared.py`; never hand-edit generated copies.
- Regenerate inventory using `tools/build-registry.py` after metadata changes.
- Run `tools/validate-skills.py`, the unittest suite, and affected browser builds.
  The validator rejects lost browser sections and instruction-budget overflow.
- Never edit generated `dist/` files. Do not add `package.json`; discovery uses
  skill metadata, not npm packaging. Shared tooling belongs in `tools/`.
- Maintainer Python dependencies are in `requirements-dev.txt`.
- Publication exports a committed tree; keep the working tree clean and use the
  publisher's dry run before publishing. Never replace its lease with blind force.
