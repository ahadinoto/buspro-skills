# buspro-skills

Agent skills for a Business Process team. Each skill teaches an AI assistant to
coach a specific kind of work to the team's standard, and installs into
whichever coding agent you already use.

The examples and system names throughout are illustrative placeholders, not any
real system.

## Skills

| Skill | What it does | Docs |
|---|---|---|
| `basecamp-todo-coach` | Coaches clear, reviewable, executable Basecamp work — Starter Context, Epic Briefs, the locked 11-field todo format, the readiness gate, discovery reviews, IPM updates | [readme](docs/basecamp-todo-coach/README.md) |

## Install one skill

Install only what you need — `--skill` takes exactly the skill you name:

```bash
npx skills add ahadinoto/buspro-skills --skill basecamp-todo-coach -g
```

`npx skills` detects which agents you have (Claude Code, Antigravity, Cursor,
Codex, Windsurf, …) and installs globally. Private repo is fine — it uses the
git auth you already have.

See a skill's own readme for what it does, how to drive it, and browser-chat
setup (Gemini Gem / ChatGPT Custom GPT) if you don't use a coding agent.

Useful variations:

```bash
npx skills add ahadinoto/buspro-skills --list         # see what's available
npx skills update -g                                  # pull the latest
npx skills remove --global basecamp-todo-coach        # uninstall one
```

## Layout

```text
buspro-skills/
├── AGENTS.md                         # repo conventions (CLAUDE.md symlinks here)
├── skills/                           # installable units — what npx skills reads
│   └── basecamp-todo-coach/
│       ├── SKILL.md
│       └── references/
├── docs/                             # human documents, not installed
│   └── basecamp-todo-coach/
│       ├── README.md                 # this skill's usage guide
│       ├── quality-system-tracker.md # canonical decision log
│       ├── design-record.md          # why the skill is built this way
│       └── gem-instruction-legacy.md # superseded hand-written Gem prompt
├── tools/
│   ├── build-web-prompt.py           # browser-chat bundler (--skill)
│   └── install-global.sh             # maintainer dev helper
└── dist/                             # generated, gitignored
```

Two things about this layout are load-bearing:

**Skills live directly under `skills/`.** `npx skills` scans known containers at
the repo root and only falls back to searching the whole tree when that finds
nothing. A skill nested deeper rides that fallback and silently stops being
discovered as soon as another skill is placed correctly.

**Each skill is self-contained.** `npx skills` installs only
`skills/<skill>/`, so nothing in a skill may point at a file outside its own
directory as though the reader has it — including anything in `docs/`.

## Working on these skills

Read [AGENTS.md](AGENTS.md). Short version: record a decision in the skill's
tracker first, then update the skill, then rebuild the bundles.

```bash
tools/install-global.sh --dry-run              # symlink the working tree, safely
python3 tools/build-web-prompt.py --list       # skills and their web targets
```
