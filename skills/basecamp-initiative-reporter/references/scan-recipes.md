# Scanning Basecamp for a report

Exact commands, output shapes, and the two algorithms that are easy to get
wrong. Everything here was run against a live Basecamp account; the flags and
JSON keys are verified, not assumed.

Project names and IDs in the examples below are illustrative placeholders,
not real projects.

All commands take `--json`. Every response is
`{"ok": bool, "data": ..., "summary": str, "notice": str}` — check `ok` before
reading `data`.

---

## 1. Preflight

```bash
basecamp auth status --json     # .ok and .data.authenticated
```

Unauthenticated means stop, not improvise. See SKILL.md.

## 2. Resolve the project

```bash
basecamp projects list --json   # data[] of {id, name, ...}
```

Note the subcommand: `basecamp projects list`, not `basecamp projects`. The bare
form prints help, and its JSON is the *command description*, not your projects —
an easy and confusing mistake.

Match on `name`. Ambiguous match means ask.

## 3. Scan the user's activity

**`--person` and `--project` are mutually exclusive.** This fails:

```bash
basecamp timeline --in <project> --person me      # error: mutually exclusive
```

Because both workflows report the user's own work, scope by person and filter by
project:

```bash
basecamp timeline me -n 200 --json
```

Each event:

```json
{
  "action": "Sari W. checked off a to-do",
  "kind": "todo_completed",
  "created_at": "2026-09-15T15:38:27.302Z",
  "creator": { "id": 0, "name": "...", "email_address": "..." },
  "bucket":  { "id": 12345678, "name": "[Acme] Process Improvement", "type": "Project" },
  "title": "...", "summary_excerpt": "...",
  "url": "...", "app_url": "https://3.basecamp.com/...",
  "target": "...", "parent_recording_id": 0, "id": 0
}
```

Use `app_url` for links you show a human. Use `bucket.id` for filtering — never
`bucket.name`, which changes when a project is renamed.

### Pagination rule

`-n 200` reached about three weeks of history on a moderately active account.
That is not a guarantee.

**After fetching, check the oldest event returned.** If
`data[-1].created_at` is still *newer* than your window start, the window is not
fully covered — page further with `--page`, or raise `-n`, before drawing any
conclusion. Reporting "nothing moved on Monday" because you only fetched back to
Tuesday is the worst failure this skill can have.

If the window is genuinely covered and there are no events, that is a real
result: say nothing moved.

## 4. Filter

Two filters, in this order:

1. **Project**: `event.bucket.id == <project id>`
2. **Window**: `event.created_at >= window_start`

### Timezone — convert before bucketing by day

`created_at` is UTC with a `Z` suffix. Convert to the user's local zone *before*
deciding which day an event belongs to.

Worked example, user in WIB (UTC+7):

| `created_at` (UTC) | Local (WIB) | Belongs to |
|---|---|---|
| `2026-09-15T15:38Z` | Sep 15, 22:38 | Monday |
| `2026-09-15T18:00Z` | Sep 16, 01:00 | **Tuesday**, not Monday |

Comparing raw UTC strings against a local day boundary silently drops evening
work from the report and moves it to the next day. Ask the user's timezone if
you cannot determine it; do not assume UTC.

## 5. Event kinds

Observed on a real account, most frequent first:

| `kind` | Means | Report as |
|---|---|---|
| `kanban_step_created` | A step added to a card | Card work |
| `todo_created` | A todo was created | Work queued — **not** work done |
| `todo_completed` | A todo was checked off | Completed |
| `comment_created` | A comment was posted | Discussion / decision |
| `question_answer_created` | A check-in question answered | Check-in |
| `kanban_card_completed` | A card finished | Completed |
| `document_created` | A document added | Document added |
| `dock_created` | A tool was enabled on the project | **Noise — omit** |
| `project_access_changed` | Membership changed | **Noise — omit** |

Two rules for this table:

- **Omit the noise kinds.** "I changed project access" is not stand-up content.
- **Unknown kinds are not dropped.** The list is what one account happened to
  produce, not the full Basecamp vocabulary. Report an unrecognised kind using
  its `action` string, which is already human-readable ("Eri added a card").
  Silently discarding an unfamiliar kind loses real work.

`todo_created` deserves care: creating a todo is queuing work, not doing it.
Group it under what was *picked up* or *planned*, never under what was
completed.

## 6. Spotting items filed by automation

Tools that write into Basecamp do so under a person's name, so their events are
indistinguishable from real work by `creator` alone. A stand-up that lists them
as accomplishments reads as padding.

Heuristics, in order of reliability:

1. **A machine marker in the body** — a trailing identifier, a tool name, or a
   `Source:` URL in `summary_excerpt` is the strongest signal.
2. **Created and completed within seconds** — compare timestamps for the same
   `parent_recording_id`.
3. **Batch timestamps** — many items created in the same second.

When in doubt, do not silently drop it. List it under what *arrived* rather than
what the user *did*, or ask. Dropping real work is worse than over-reporting it.

## 7. Open assignments

```bash
basecamp assignments list --json
basecamp assignments due --json        # by due date
```

`data` is an **object, not an array**:

```json
{ "priorities": [...], "non_priorities": [...] }
```

Read both keys; a missing key means none of that kind, not an error. Items carry
`{id, content, bucket, parent, assignees, app_url, type}` — filter by
`bucket.id`, and use `parent` to name the epic (todo list) an item belongs to.

## 8. Detail on one item

```bash
basecamp events <id|url> --json
```

The audit trail for a single item: `created`, `completed` / `uncompleted`,
`assignment_changed`, `content_changed`, `archived` / `unarchived`,
`commented_on`.

Use it sparingly — when you need to answer "when did this stall?" or "who
reassigned this?" for one item. Do not call it for every event in the window;
the timeline already carries what a report needs.

## 9. What this scan cannot see

State these as limits rather than reporting around them:

- **Others' activity on the user's items.** `timeline me` is the user's own
  actions. If a teammate comments on their todo, it will not appear. For
  blockers, lean on open assignments and recent comment threads on those items.
- **Why something stalled.** The timeline shows absence of events, not reasons.
  "No movement since Thursday" is reportable; "blocked on Finance" is not,
  unless a comment says so.
- **Work done outside Basecamp.** Plenty of real work never becomes an event.
  If the user says they did something the timeline does not show, believe them
  and include it — note that it has no Basecamp trace yet, and that a todo may
  be worth creating.

## 10. Posting the report

Never run these without explicit confirmation. Show the exact content and the
exact command first, then wait.

### Comment on a todo or a todo list

```bash
basecamp comment <id|url> "<content>"
```

Same command for both targets — a progress comment on a todo, an IPM update on
a todo list. Comment bodies accept **Markdown** and `@Name` mentions, so the
labelled structure in `message-formats.md` renders as written.

### Message board post

```bash
basecamp messages create "<title>" "<body>" --in <project> --no-subscribe
```

- `--no-subscribe` for daily stand-ups and show-and-tells. Notifying the whole
  project every morning trains people to ignore the board.
- `--draft` creates it without publishing, for a user who wants to review it in
  Basecamp before it goes out. Offer this if they hesitate.
- `--message-board <id>` is required only when a project has more than one
  board.

Both commands return JSON with `--json`. **Give the user the resulting URL**
after posting, so they can check it rendered correctly.

### Window per report

| Report | Window | Target |
|---|---|---|
| Stand-up | end of previous working day → now, plus open assignments | message board |
| Show-and-tell | today, local | message board |
| Progress comment | today, local; events touching the named todo only | that todo |
| IPM update | past 7 days, or since the last IPM comment on that list | the todo list |
| Combined weekly | past 7 days across every monitored project | the reporting destination |

For the IPM window, look for the previous `[IPM Update - …]` comment on the todo
list and scan from its date. Fall back to 7 days when there is none.
