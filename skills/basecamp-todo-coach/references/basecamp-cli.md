# Reading and writing Basecamp via the official CLI

This skill does **not** implement Basecamp access. It relies on the official
Basecamp CLI (`basecamp`), which ships its own agent skill covering all 155 API
endpoints.

- Repo: https://github.com/basecamp/basecamp-cli
- Install: `curl -fsSL https://basecamp.com/install-cli | bash`
- Claude Code plugin: `basecamp setup claude`
- Auth: `basecamp auth login` (add `--scope full` for write access)

For any mechanic not covered below, use `basecamp <cmd> --agent --help` — it
returns structured JSON with flags, subcommands, and gotchas. Do not guess flags.

---

## Preflight

```bash
basecamp doctor --json          # CLI health, auth, connectivity
basecamp auth status            # auth only
cat .basecamp/config.json       # project scope for this repo, if any
```

If `basecamp` is not on PATH or auth fails, tell the user plainly and fall back
to paste mode. Do not silently proceed on assumptions.

---

## Concept map

| Quality-system concept | Basecamp object | Command |
|---|---|---|
| Project / Initiative | Project | `basecamp projects list --json` |
| Project Starter Context | Project **description** | `basecamp projects show <id> --json` |
| Epic / Module / Workstream | Todo List | `basecamp todolists list --in <project> --json` |
| Epic Brief | Todo List **description** | `basecamp todolists show <todolist_id> --in <project> --json` |
| IPM updates | Dated comments on the Todo List | `basecamp comments list <todolist_id> --in <project> --json` |
| Todo Group (status) | Todo list group | `basecamp todolistgroups list --in <project> --json` |
| Todo Item | Todo | `basecamp todos list --list <todolist_id> --in <project> --json` |
| 11-field todo body | Todo **description** | `basecamp todos show <id> --json` |
| PIC / Validation PIC (name check) | Person on the project | `basecamp people list --project <id> --json` |
| Assignee / due date | Native todo fields | `basecamp assign <id> --to <person>` / `--due` |

---

## Standard read sequence

Given a project URL or ID, gather context in this order and stop as soon as you
have what the workflow needs.

```bash
# 0. If given a URL, parse it first — always.
basecamp url parse "<url>" --json

# 1. Starter Context (project description)
basecamp projects show <project_id> --json

# 2. Epics
basecamp todolists list --in <project_id> --json

# 3a. Epic Brief — lives in the Todo List description
basecamp todolists show <todolist_id> --in <project_id> --json

# 3b. IPM history — dated comments on the same Todo List
basecamp comments list <todolist_id> --in <project_id> --json

# 4. Todos in the epic
basecamp todos list --list <todolist_id> --in <project_id> --json

# 5. Status layer
basecamp todolistgroups list --in <project_id> --json

# 6. Full detail on one todo (includes comments)
basecamp todos show <todo_id> --json

# 7. People, to validate that a named PIC actually exists
basecamp people list --project <project_id> --json
```

Use `--jq` to keep responses small, e.g.:

```bash
basecamp todos list --list <id> --in <project> \
  --jq '[.data[] | {id, title, completed}]'
```

Never pipe to external `jq` — the CLI has `--jq` built in.

---

## Write operations

Read-only by default. Confirm with the user before every write.

```bash
# Create the epic
basecamp todolists create "Finance Ops - Settlement View" --in <project> --json

# Write the Epic Brief into the Todo List description.
# --name is REQUIRED even when only the description changes; sending
# --description alone returns 422 Unprocessable Entity (verified 2026-07-29).
basecamp todolists update <todolist_id> --name "<existing name>" \
  --description "<p>...</p>" --in <project> --json

# Post an IPM update (later comment on the same todolist)
basecamp comment <todolist_id> "[IPM Update - 27 July 2026] ..." --in <project> --json

# Create a todo
basecamp todo "[Confirmation] Confirm settlement output" \
  --in <project> --list <todolist_id> --json

# Native fields — never in the todo text
basecamp assign <todo_id> --to "First.Last" --in <project> --json
```

**Mentions.** For comments, prefer the deterministic form. Resolve the person
first, then embed the SGID:

```bash
basecamp people pingable --jq '.data[] | select(.name == "Jane Smith")'
basecamp comment <id> "[@Jane Smith](mention:<SGID>) please confirm" --in <project>
```

**Markdown vs plain text.** Comment and message bodies accept Markdown and are
converted to HTML. **Todo, todo list, document, and card content is sent as-is**
— so the 11-field todo body and the Epic Brief should be plain text or explicit
HTML, not Markdown. Since 2026-07-29 the brief lives in the todo list
description, so brief and todos now follow the same as-is rule; only IPM
comments convert from Markdown.

**Overwrite warning.** `todolists update --description` replaces the whole
description. To amend an Epic Brief, read the current description first, edit
the full text, and write it back — never send a fragment.

**Dependencies links.** The `Dependencies` field (added 2026-07-29) holds links
to predecessor todos. Since todo content is sent as-is, write these as real
`<a href="https://app.basecamp.com/.../todos/<id>">Title</a>` anchors, not
`[Title](url)` Markdown — Markdown syntax will show up as literal brackets and
parentheses instead of rendering as a link. When drafting a sequential chain of
todos (like Work Breakdown items that each depend on the one before), create
them in order so each one's predecessor already has a real ID to link to,
rather than creating all of them first and patching links in afterward.

---

## Verify before first real use

The mappings above are drawn from the CLI's published skill and API coverage
matrix. Confirm these five locally — they carry the quality system's weight:

1. **Todo description on create.** The 11-field format lives in the todo's
   description. Check the flag name:
   `basecamp todos --agent --help` and `basecamp todo --agent --help`.
   If create does not accept a description, the pattern becomes create → then
   `basecamp todos update <id> --description "..."`.
2. **Project description write-back.** Whether Starter Context can be written:
   `basecamp projects update --agent --help`.
3. **Todo list groups.** Naming and create/move semantics, so status changes move
   a todo between groups rather than editing its title:
   `basecamp todolistgroups --agent --help`.
4. **Todo list description read/write.** The Epic Brief lives there.
   **Verified 2026-07-29:** `basecamp todolists show <id> --in <project>`
   returns `description`, and `basecamp todolists update <id> --description`
   writes it. For IPM comments, confirm `comments list` returns oldest-first so
   the timeline reads in order; if not, sort by `created_at`.
5. **Content rendering.** Confirm that todo and todo list descriptions are sent
   as-is while comment bodies are converted from Markdown — this governs how the
   locked 11-field format and the Epic Brief render in Basecamp. Post one test
   todo and one test comment and look at them in the UI.

---

## Skill-only capabilities (enabled by live access)

Dispositions agreed 2026-07-27. Tracker #8 is the record.

### Core — the write gate

**Readiness is checked during the conversation, and creation is the reward for
passing it.** The skill never writes a todo that is not ready. See SKILL.md
"Writing to Basecamp". This is the primary behavior; everything below supports it.

### Always on when reading

- **Named-person validation** — check PIC and Validation PIC against
  `basecamp people list --project`. An unmatched name is a signal to confirm, not
  a reason to refuse. This operationalises the "Validation PIC must be a named
  person" rule instead of trusting a name found in a doc.

### Offer, do not perform unprompted

- **IPM update pre-fill** — diff todo group membership and completions since the
  date of the last IPM comment, and offer the result as a *starting draft* of
  Progress and Status Movement only. The guided questions still run. The context
  belongs to the PIC; the skill only tidies the update into the agreed format so
  it is structured and easy to read. Blockers, decisions, next steps, and risks
  are never inferred from Basecamp state.

- **Epic Brief precondition** — when the user starts epic-level work in a Todo
  List, check whether it has an Epic Brief. Read the list **description** first
  (`todolists show`); if that is empty, fall back to the first comment, where
  epics created before 2026-07-29 keep theirs. A brief in either place counts —
  do not report a missing brief without checking both. If there is genuinely
  none, the epic has no objective, Main PIC, Validation PICs, or work breakdown
  to coach against — say so once and offer to draft the brief first.
  **Not every Todo List is an epic.** Do not scan a project for missing briefs,
  do not raise this in ad-hoc or misc lists, and accept "this list is not an
  epic" as a final answer.

- **Hygiene sweep** — on request, find todos with status words in the title,
  missing or wrong type prefixes, or assignee / due date written into the body.
  Report and offer fixes; do not auto-correct.

- **Batch readiness review** (nice-to-have) — read every todo in a Todo List and
  return a Ready / Needs Revision verdict per todo. Useful for cleaning up an
  existing list. The write gate above is the real control; this is retrospective.
