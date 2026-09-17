# Basecamp Todo & IPM Coach — Universal Agent Skill Design v3.0

**This is the design and decision record for the skill, not the skill itself.**
The skill is the directory below; this doc explains why it looks the way it does.

Status: **Built (v3.0) — tracking Gem instruction v4.12.** Re-sync required when
workstream #4 locks.

Built artifact: `skills/basecamp-todo-coach/` (own repo, installed via `npx skills`)

Last updated: **2026-09-11**

**v2.7 (2026-09-11)** — restructured from a Claude-only skill into a universal
agent skill. No coaching rule changed; this is packaging and distribution.

*Why one skill instead of three.* The coaching logic had drifted across three
formats — this skill, the hand-written Gem instruction, and ad-hoc custom
instructions for other agents. Every change to the tracker meant editing
several disconnected files, and a divergent hand-made Codex copy was found
during the restructure — reworded rules, a compressed CLI reference, no unique
substance, and no way to tell it had drifted. It was deleted on 2026-09-11 and
that agent now reads the canonical skill like every other. The skill is now the single source; browser-chat
prompts are generated from it.

*Repo shape follows the installer's discovery order.* `npx skills` (the
`skills.sh` ecosystem — npm `skills`, `vercel-labs/skills`) scans documented
containers at the repository root: `skills/`, `.claude/skills/`,
`.agents/skills/` and similar, each walked at most three levels deep. Only if
that scan finds **nothing at all** does it fall back to an unbounded search of
the tree.

That fallback is why the old nested `buspro/bc-coach/skill/` layout worked, and
why it could not be relied on. Verified against skills@1.5.25 with a probe
repo: a skill at `<repo>/sub/skill/<name>/` was listed while it was the only
skill present, and vanished from the listing as soon as a correctly located
`skills/<name>/` skill was added alongside it. buspro is a multi-purpose repo,
so the coach's discoverability was one unrelated skill away from silently
breaking. Hence two changes: `bc-coach` became its own repo, and `skill/` became
`skills/`. A side benefit — mentees no longer need read access to the rest of
buspro to install. (The repo was renamed `buspro-skills` the same day, to hold
more than one skill; each skill stays a self-contained directory under
`skills/`.)

*Dual-mode is now explicit.* `SKILL.md` opens with `Operating Modes —
Preflight`: run `basecamp auth status`, read `ok` and `data.authenticated`, and
declare Agent Mode or Paste Mode. Paste Mode also covers browser chat, where no
shell exists. The gate, the format, and every rule are identical in both modes —
mode governs only how context arrives and whether writing is possible. No
connection-check script was added: `basecamp auth status` already emits JSON
with exactly those fields, so a wrapper script would add a failure point and no
information.

*Browser chat is tiered, not truncated.* Full skill content is ~93 KB, with
`references/examples.md` alone at 49 KB. No instruction box takes that: a
ChatGPT Custom GPT caps instructions at 8,000 characters, and the Gem
instruction proven to paste without truncation (#4, v4.1) is ~14.6 KB. So
`tools/build-web-prompt.py` emits, per target, an instruction tier to paste and
knowledge files to upload. Content is selected by `##` heading name rather than
by concatenating files, which gives three properties worth having: a renamed
heading fails the build loudly instead of silently dropping a section; a budget
overrun is fixed by moving a *named* section between tiers rather than trimming
prose; and cross-references are rewritten per target, so a bundle never tells
the agent to open an upload for content already in its own instructions.

*What was rejected.* A `curl | bash` installer — it needs an unauthenticated
raw URL, which a private pilot repo does not have, and piping a token-bearing
URL into a shell is worse than the `npx skills` path that already handles
private auth. A `package.json` — `npx skills` resolves skills by directory
layout and `SKILL.md` frontmatter, never npm metadata, so it would imply an npm
publish that is not happening.

*Repo cleanup, same pass.* Two root files went. `basecamp_todo_example_todos_v3.md`
was a byte-identical duplicate of `references/examples.md` — 49 KB twice, plus a
manual sync rule — so the skill's copy became canonical and the bundler now
reads it directly. `universal_skill_refactoring_plan.md` had no inbound
references and its substance is this entry. The hand-written Gem instruction
stays for now: it carries no unique substance (its headings are renamed
equivalents of skill sections, and its `Example Behavior` is a pointer to
Example 1), but workstream #4 still declares it the source of truth and the
generated Gem bundle is unproven in a real Gem. Retire it once mentee testing
confirms the bundle.

*Pilot feedback is the verification plan.* Rather than pre-verifying every
surface locally, the packaging exists so mentees can install in one command and
report what breaks. That only works if reports are diagnosable, which needed two
additions: the end-of-instruction truncation check promoted from a comment to a
setup step in `README.md`, and a documented feedback channel. Both address the
same failure — a silently truncated instruction paste presents as a coach that
has stopped enforcing rules, and would otherwise be reported as a rule bug that
does not exist.

*Distribution.* GitHub, installed with `npx skills add`. A move to the company
GitLab was briefly planned and dropped — GitHub is the home for now, and
possibly permanently. Nothing in the repo is host-specific, so if that ever
changes it is one argument in the install command; there was no value in
carrying migration guidance for a move that may never happen.

**v2.6 (2026-09-03)** — synced to instruction v4.12: added a dedicated
discovery-deliverable review mode. It separates a quality verdict from Basecamp
state, accepts user-confirmed verbal validation unless written proof is required,
and checks evidence, coverage, clarity, and scope. The detailed checklist lives
in `references/deliverable-review.md` to keep `SKILL.md` concise.

**v2.2 (2026-07-28)** — synced to instruction v4.8: 12-field todo format with the
always-present `Tip` in `references/formats.md`, per-type tip material for all 10
types in `references/todo-types.md`, and a warmer Output Style in `SKILL.md` with
the readiness gate and verdict labels explicitly unchanged.

**v2.3 (2026-07-29)** — synced to instruction v4.9: Epic Brief reads from and
writes to the Todo List description (not the first comment) across `SKILL.md`
and the reference files; pre-2026-07-29 epics with a brief in the first comment
still count as having one.

**v2.4 (2026-07-29)** — synced to instruction v4.10: `Todo Type` and `Module /
Area` removed from the individual todo format (now 10 fields) across `SKILL.md`,
`references/formats.md`, `references/todo-types.md`, `references/basecamp-cli.md`,
and `references/examples.md`. Both were redundant — Todo Type with the title's
`[Todo Type]` prefix, Module / Area with the Epic/Todo List name.

**v2.5 (2026-07-29)** — synced to instruction v4.11: `Dependencies` added (now
11 fields) across `SKILL.md`, `references/formats.md`, and
`references/examples.md`. `references/basecamp-cli.md` gained a gotcha:
Dependencies links must be real `<a href>` HTML anchors on write, since todo
content is sent as-is, not converted from Markdown. Found and applied while
drafting a real five-todo sequential chain for a live epic (each todo blocked
on the one before it).

## Why a skill (vs the Gem)

Same coaching logic, four upgrades:

1. **No instruction size limit.** Skills lazy-load reference files, so SKILL.md
   stays a lean router while formats, type guidance, and examples live in
   separate files. The Gem's ~11k character size watch disappears.
2. **Real Basecamp access.** With the official Basecamp CLI available, "Agent
   Mode" becomes real: the skill reads Project Description, Todo Lists, Epic
   Briefs, todos, groups, and IPM comments directly instead of asking the user to
   paste them.
3. **No copy-per-person distribution.** The Gem needs per-person copies plus a
   shared per-initiative NotebookLM notebook (a shared Gem does not carry its
   notebook connection). One skill serves everyone; project context is read live
   per project.
4. **New capabilities the Gem cannot have** — batch readiness review across a
   Todo List, IPM updates drafted from real status movement, and named-person
   validation of PIC / Validation PIC against the project's people list.

## Decision (2026-07-27): build on the official Basecamp CLI

Basecamp shipped an **official CLI plus its own agent skill** (v0.7.2, March
2026): `github.com/basecamp/basecamp-cli`. It covers 155 endpoints — 100% of the
in-scope BC3/4/5 API — with OAuth, JSON envelopes, a built-in `--jq`, and a
`--agent --help` introspection contract. It also ships a Claude Code plugin
(`basecamp setup claude`).

Consequences:

- The Coach skill **does not implement Basecamp access**. It layers the team's
  quality conventions on top of the official skill and treats the CLI as the
  transport. This resolves the "which Basecamp integration" open decision — no
  community MCP, no custom API wrapper.
- Mechanics questions ("list my todos", "complete this") route to the official
  `basecamp` skill. The Coach skill triggers on quality and structure intent.
- Prerequisite for each user: install the CLI and run `basecamp auth login`.

## Built structure

```text
skill/basecamp-todo-coach/
├── SKILL.md                     # role, context priority, workflows, readiness rule, write policy
└── references/
    ├── formats.md               # Starter Context, Individual Todo, Epic Brief, IPM, Todo Groups
    ├── todo-types.md            # 10 types, done criteria, summary table, shared rules, prefix map
    ├── basecamp-cli.md          # concept→command map, read sequence, write policy, gotchas
    ├── deliverable-review.md    # evidence-based review of discovery work
    └── examples.md              # generated copy of examples v3.9 (workstream #5)
```

Single source of truth: `references/` content is copied from the **tracker**
(Locked sections) and the examples doc. When the tracker changes, regenerate.
The repo is the build source.

## Design choices made

- **Read-only by default.** Every write is preceded by showing the exact content
  and the exact command, then asking for confirmation. A Development todo that
  fails the Readiness Rule is never written, even on request.
- **Truth priority preserved, inverted in mechanism.** In the Gem the user pastes
  Basecamp content and it beats Knowledge docs. In the skill the CLI read *is*
  tier 1 — so decision #3 becomes automatic rather than a paste-discipline rule.
  Background Drive docs stay tier 2.
- **Explicit no-access fallback.** If the CLI is missing or unauthenticated, the
  skill says so plainly and falls back to paste mode. This is the skill analogue
  of the v4.6 retrieval self-report guardrail (decision #13) — and unlike a Gem,
  the skill *can* actually detect the failure.
- **Description field discipline.** Comment bodies accept Markdown; todo and
  document content is sent as-is. The 11-field todo body must therefore be plain
  text or explicit HTML (including Dependencies links, written as `<a href>`
  anchors, not Markdown).

## Verify before first real use

Four CLI details carry the quality system's weight and need local confirmation
(listed with the exact introspection command in `references/basecamp-cli.md`):

1. Todo **description** flag on create — the 11-field format lives there.
2. Project **description** write-back — whether Starter Context can be written.
3. `todolistgroups` create/move semantics — so status moves a todo between
   groups rather than editing its title.
4. Todo list description read/write — the Epic Brief lives there (verified 2026-07-29). Comment ordering still matters for the IPM timeline.

## Open decisions

- **Distribution.** Personal skill, shared plugin, or an internal marketplace for
  mentees? A plugin bundling the Coach skill + the official Basecamp plugin is
  the cleanest install story, but needs a hosting decision.
- **Write scope.** Read-only is the current default. Decide whether mentees get
  write access at all, or whether the skill always hands back text to paste.
- **Google Workspace CLI for background docs.** Tier 2 (initiative Drive
  folders) is currently unimplemented in the skill. Add once the Basecamp path
  is proven — the notebook sources stay mirrored from the same Drive folders so
  the Gem and the skill read the same docs.
- **Re-sync trigger.** This skill tracks instruction v4.11. Define whether #4
  findings regenerate `references/` automatically or by hand.
