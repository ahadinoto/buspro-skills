# BusPro Toolkit

Practical skills for interview preparation and project work. Each skill is a
self-contained, agent-neutral package. Host setup and browser-chat adaptations
live separately under `adapters/`.

## Install

```bash
npx skills add ahadinoto/buspro-skills --skill interview-prep -g
```

Choose your agent when prompted, or add `-a codex`, `-a claude-code`,
`-a antigravity`, or `-a cline`. Omit `-g` for a project installation.
Node.js 22.20 or newer is required by the tested installer, skills 1.7.0.
Use `npx skills@1.7.0` to reproduce the tested version.

| Category | Skill | Purpose |
|---|---|---|
| hiring | `interview-prep` | CV-specific interview questions and follow-up probes |
| project-management | `todo-planner` | Clear todos, readiness checks, and deliverable review |
| project-management | `progress-reporter` | Evidence-based updates from live Basecamp activity |

```bash
npx skills add ahadinoto/buspro-skills --list
npx skills add ahadinoto/buspro-skills --skill todo-planner progress-reporter -g
npx skills update -g
npx skills remove interview-prep -g
```

`interview-prep` works with supplied CV text; PDF extraction depends on the host.
`todo-planner` supports pasted material; live Basecamp operations need the
Basecamp CLI and authentication. `progress-reporter` requires live Basecamp read
access, with write access only when posting is requested. Installation does not
install these tools or grant account access.

For Codex, select the skill or use `$interview-prep`; for Claude Code use
`/interview-prep`. On other hosts, ask to use the named skill and check the host's
skill list. Gemini is the model used through Antigravity; GLM can be configured
through Cline in VS Code. Model choice does not change the canonical package.
See [agent compatibility](docs/agent-compatibility.md).

## Existing users

The new names replace `candidate-interview-coach`, `basecamp-todo-coach`, and
`basecamp-initiative-reporter`, respectively. Install the new names first, verify
they appear in your agent, then remove the old names from the same install scope.
The old names are not aliases in the public installer. Updating an old install
alone does not select a differently named skill.

## Organization and contribution

```text
skills/
  hiring/interview-prep/
  project-management/todo-planner/
  project-management/progress-reporter/
adapters/                 # host paths and browser-chat manifests
registry/skills.json       # generated inventory
shared/                    # source for shared bundled references
tools/                     # maintainer tools
```

`process-analysis`, `appsheet`, and `communication` are reserved categories for
future substantive skills; they have no placeholder packages. A skill has one
home category and can have multiple tags. The Toolkit can grow with reusable
references and integrations without duplicating instructions per model.
See [architecture and authoring](docs/toolkit-architecture.md).

## Maintainers

Python 3.10+ and the development requirements are needed only for repository
tools. Mentees do not need Python.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python tools/validate-skills.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python tools/build-web-prompt.py --skill todo-planner
.venv/bin/python tools/install-global.py --repair-renames --dry-run
```

Remove `--dry-run` to repair checkout-owned links. The installer preserves real
folders and foreign links. Use `--agent codex --skill interview-prep` to create an
explicit host installation. See `--help` for unlinking and other options.

Browser-chat bundles for Todo Planner are generated under `dist/todo-planner/`.
They use pasted context and cannot run live Basecamp operations. Build and use
the generated instruction and knowledge files together. Other skills currently
have no browser-chat bundle.
