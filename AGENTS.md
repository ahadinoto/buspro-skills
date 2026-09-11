# Working in this repo

This repo holds the Business Process team's agent skills. Each skill under
`skills/` is an installable unit; `docs/<skill>/` holds the human documents
behind it.

## Layout

- `skills/<skill>/` — the skill itself. **Must stay directly under `skills/`**:
  `npx skills` scans known containers at the repo root and only falls back to
  searching the tree when that finds nothing, so a skill moved deeper stops
  being discovered the moment another skill is placed correctly.
- `docs/<skill>/` — that skill's tracker, design record, and readme. Not
  installed with the skill.
- `tools/` — shared, skill-parameterized. `--skill <name>`.
- `dist/` — generated output, gitignored. Never edit; rebuild.

## The rule that matters

**A skill must be self-contained.** `npx skills` installs only
`skills/<skill>/`, so nothing inside a skill may reference a file outside its
own directory as though the reader has it. Cite the repo by name instead, and
say the file is not bundled.

This is easy to get wrong: a line like ``see `../../docs/foo.md` `` works on
this machine and is broken for every mentee.

## Changing a rule

Record the decision in `docs/<skill>/quality-system-tracker.md` **first**, with
the reasoning, then update the skill to match. The tracker is the canonical
decision log and the audit trail for why a rule exists — not a changelog
written after the fact.

Then rebuild the browser-chat bundles:

```bash
python3 tools/build-web-prompt.py --skill <name>
```

The bundler selects content by `##` heading name. **Renaming a heading in a
skill breaks the build on purpose** — it exits non-zero and names the section.
Fix `BUNDLES` in `tools/build-web-prompt.py`; do not work around it.

## Adding a skill

1. `skills/<new-skill>/SKILL.md` plus `references/` as needed.
2. `docs/<new-skill>/` for its human docs.
3. Add it to the root `README.md` index.
4. Only if it needs browser-chat support: add a `BUNDLES` entry. A skill with
   no entry is simply not bundled, which is fine.

Do not copy `tools/` per skill. If one skill needs bespoke tooling, add
`tools/<skill>-thing.py` rather than forking the directory.

## Local development

```bash
tools/install-global.sh --dry-run   # see what would change
tools/install-global.sh             # symlink every skill into your agent dirs
```

Symlinks mean your edits are live with no reinstall. That is the maintainer
path; mentees use `npx skills add`, which pins a clone.

## Don't

- Don't hand-edit anything under `dist/`.
- Don't add a `package.json`. `npx skills` resolves skills by directory layout
  and `SKILL.md` frontmatter, never npm metadata.
- Don't trim rules to fit a browser-chat budget. Move a named section to the
  knowledge tier instead.
