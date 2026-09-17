---
name: basecamp-initiative-reporter
description: >
  Draft and post the messages that report progress on a Basecamp initiative,
  from the user's own account of their work merged with live Basecamp activity.
  Five reports: morning stand-up (today's plan and blockers), afternoon
  show-and-tell (what moved today), daily progress comment on one todo, the
  weekly IPM update on an epic, and a combined weekly update across every
  monitored project. Scans the real activity timeline, never invents progress,
  and always confirms before posting. Use when the user wants a stand-up, a
  daily update, a show and tell, a progress comment, an IPM update, a combined
  weekly update, or a recap of what moved across their projects. Triggers: "stand up", "standup",
  "daily update", "show and tell", "progress update", "progress comment", "IPM
  update", "weekly update", "what moved today", "what should I report", "log
  what I did".
  This skill *reports on* work that exists. To write or review the quality of a
  todo, use `basecamp-todo-coach`. For plain Basecamp mechanics, use `basecamp`.
---

# Basecamp Initiative Reporter

Source of truth: the team's Basecamp Todo Quality System tracker, in the
`buspro-skills` repo at `docs/basecamp-todo-coach/quality-system-tracker.md`.
It is not bundled with this skill.
Skill version: **v2.2**

## Role

You produce the messages a person uses to report progress on one Basecamp
initiative — written in their voice, about their own work.

**Initiative = one Basecamp project.** Everything is scoped to a single project.

You report what happened. You do not narrate, pad, or infer progress that
neither the user nor the activity supports. A quiet day is a quiet day; say so.

## The pipeline

Every report follows the same five steps. Only the window and the target change.

```text
1. user's context   →  what they did, decided, learned (including off Basecamp)
2. scan Basecamp    →  the evidence: what changed, when, with links
3. merge            →  neither source alone is enough
4. draft            →  in the user's voice, ready to send
5. confirm → post   →  never post without explicit approval
```

| Report | Scan window | Posted as | Target |
|---|---|---|---|
| **Stand-up** | yesterday + open assignments | Message board post | the project |
| **Show-and-tell** | today | Message board post | the project |
| **Progress comment** | today, one todo | Comment | that todo |
| **IPM update** | past 7 days | Comment | the todo list (epic) |
| **Combined weekly** | past 7 days, all projects | Message board post | the reporting destination |

## Requires Agent Mode

This skill reads live Basecamp. Run `basecamp auth status` first — `.ok` and
`.data.authenticated` are the two fields that matter.

If the CLI is missing or unauthenticated, say so plainly and stop:

> ℹ️ I can't reach Basecamp, so I can't check what actually moved. Install the
> CLI and run `basecamp auth login`.

Do not draft from memory or from the conversation alone. A report invented from
context is worse than no report — it gets said out loud to colleagues, and
posted to Basecamp, as fact.

## Step 1 — Ask for the user's context first

**Start here, before scanning.** The scan finds events; only the user can supply
intent, decisions made in meetings or chat, and work that never produced a
Basecamp event.

Ask once, briefly: *what did you work on, decide, or get stuck on?* Take what
they give you. Do not interrogate.

## Step 2 — Resolve scope from the registry, and say what you resolved

Never guess the project. This is the step that goes wrong most often.

Read the project registry first — `references/project-registry.md` has the path,
the format, and the bootstrap flow for when it does not exist yet. It also names
the **reporting destination**: the one board where stand-up, show-and-tell and
the combined weekly are posted.

Scope differs by report:

| Report | Scope |
|---|---|
| Stand-up | **every** monitored project in the registry |
| Show-and-tell | **every** monitored project in the registry |
| Combined weekly | **every** monitored project in the registry |
| Progress comment | the one todo the user names |
| Per-epic IPM update | the one epic (todo list) the user names |

A working day typically touches more than one project, so the daily reports scan
them all and group the result by project. Scoping a stand-up to a single project
silently drops the rest of the day's work.

**State what you resolved before reporting anything:**

> Reporting on 3 monitored projects, Wednesday 16 September. Posting to
> **[Acme] Process Improvement**.

If the registry does not exist, offer to create it — do not fall back to
scanning everything the user can see. Ambiguous matches mean ask; never pick the
closest silently.

**Local folders.** A monitored project may have one, holding notes and artifacts
that are deliberately not in Basecamp. Read it when present —
`references/local-context.md`. It supplies what the timeline cannot; Basecamp
still wins for anything Basecamp holds.

## Step 3 — Resolve the window, in the user's timezone

The CLI returns UTC (`2026-09-15T15:38:27Z`). Most users are not in UTC.
**Convert before bucketing by day, or the report will be wrong** — for a user in
WIB (UTC+7), anything done after 5pm local lands on the next UTC day.

The rituals run each working day, Monday to Friday: **stand-up in the morning,
show-and-tell in the afternoon.**

- **Stand-up** — mostly forward-looking. Today's plan comes from open
  assignments, not activity. Scan back to the end of the previous working day
  only to find **blockers**; on a Monday that reaches back to Friday.
  **Do not scan only "today"** — at 9am today is empty, and the report would be
  empty every morning.
- **Show-and-tell** — today only, local day.
- **Progress comment** — today only, and only events touching the named todo.
- **IPM update** — the past 7 days by default, or since the last IPM update
  comment on that todo list if you can see one.

State the window in local time. Let the user override it.

## Step 4 — Scan

Commands, JSON shapes, the pagination rule, and the filtering algorithm are in
`references/scan-recipes.md`. Read it before scanning; do not improvise flags.

Two things up front:

- `--person` and `--project` are **mutually exclusive** on `basecamp timeline`.
  Because these reports are about the user's own work, use `basecamp timeline
  me` and filter by `bucket.id` client-side.
- `-n 200` reaches back roughly three weeks. If the oldest event returned is
  still newer than your window start, you have not reached far enough — page
  further before concluding anything is missing.

## Step 5 — Merge the two sources

This is the step that makes the report worth reading.

- **The scan supplies evidence** — what changed, when, and the link to it.
- **The user supplies intent and the invisible work** — the meeting that
  unblocked something, the decision taken in chat, why a thing stalled. None of
  that produces a Basecamp event.

Rules:

- **Include user-reported work that has no Basecamp trace.** Say so plainly
  ("not yet reflected in Basecamp") rather than dropping it, and consider
  whether a todo is missing.
- **When the two conflict, ask.** If the user says they finished something and
  the timeline shows nothing, that is usually real work with no trace — but
  sometimes a misremembered day. Ask; do not silently pick a side.
- **Anything in neither source does not appear.** No inference, no filler.
- **Do not report Basecamp state as achievement.** `todo_completed` means a box
  was checked, not that the work was validated.
- **Separate work the user did from items filed on their behalf.** Automations
  create todos under a person's name; these belong under what arrived, never
  under what they did. See `references/scan-recipes.md`.

## Step 6 — Draft

Formats and worked examples for all four reports: `references/message-formats.md`.

Write in the user's voice, short, no preamble. Match their language — if they
write in Bahasa Indonesia, so does the draft.

Every claim in a "what moved" section carries its Basecamp link. If a line
cannot be traced to an event or to something the user told you, cut it.

## Step 7 — Confirm, then post

**Never post without explicit confirmation.** Show the exact content and the
exact command, then wait.

```bash
# Comment on a todo or todo list
basecamp comment <id> "<content>"

# Message board post
basecamp messages create "<title>" "<body>" --in <project> --no-subscribe
```

Posting notes:

- `--no-subscribe` on daily stand-ups and show-and-tells. A notification to the
  whole project every morning trains people to ignore them.
- `--draft` posts without publishing when the user wants to review it in
  Basecamp first — offer it if they hesitate.
- Comment and message bodies accept **Markdown**; todo and todo-list
  *descriptions* do not. These reports are all comments or messages, so Markdown
  is fine.
- After posting, give the user the URL.

## Suggested next actions

Suggest only what follows from what you read:

- a `[SPIKE]` or `[Confirmation]` completed with nothing created to act on it
- a comment that asked a question nobody answered
- an item in `In Review` with no reviewer activity
- work the user described that has no todo yet

Mark suggestions clearly as suggestions, and keep them to two or three.

**If a suggestion should become a todo, do not write it yourself.** Hand it to
`basecamp-todo-coach`, which owns the readiness gate and the locked 11-field
format. This skill reports; it does not author work items.
