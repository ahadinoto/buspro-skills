---
name: progress-reporter
description: "Draft stand-ups, show-and-tells, progress comments, IPM updates, and weekly reports from live Basecamp activity plus the user’s account. Use to report existing work, not to plan or author todos. Posting requires user authorization."
metadata:
  version: "2.3.0"
  display-name: "Progress Reporter"
  renamed-from: "basecamp-initiative-reporter"
  modes: "live"
  requires: "Basecamp CLI, authenticated read access"
  optional: "Basecamp write scope for posting"
  companions: "todo-planner"
  tags: "project-management, communication, Basecamp"
  shared-references: "project-registry.md, local-context.md"
---

# Progress Reporter

Report the user's work from live Basecamp evidence and their own account. Do not
infer progress from a checkbox or invent work to fill a quiet day. Match the
user's voice and language, including Bahasa Indonesia.

## Check live access

Run `basecamp auth status --json`; check `.ok` and `.data.authenticated`.
If the CLI is absent or unauthenticated, explain what is missing and stop the
scan-backed report. Ask the user to install the CLI and run `basecamp auth login`.
Never substitute remembered activity for live evidence. Read access supports
scanning and drafting; posting also requires write scope.

## Get the user's context

Use context already supplied. If material context is missing, ask once what the
user worked on, decided, learned, or got stuck on. They supply meeting decisions
and work that produced no Basecamp event. Do not interrogate or ask again for
information already in the conversation.

## Resolve scope and destination

Read `references/project-registry.md` and apply the report table in
`references/report-scope.md`. Daily and combined reports cover every monitored
project unless the user explicitly narrows the scope. Per-todo progress and
per-epic IPM updates concern the named item. Report scope and posting destination
are separate: daily and combined reports use the registry's reporting board.

If the registry is missing, offer its bootstrap flow. Never scan every visible
project by default. Resolve IDs, ask about ambiguous matches, and state the
projects, local-time window, and intended destination before drafting.

Read a registered local folder when relevant, following
`references/local-context.md`. Basecamp wins for its current recorded state;
local notes supply the work and decisions Basecamp does not hold.

## Resolve the time window

Use the user's timezone and the defaults in `references/report-scope.md`.
Represent a local day as [local midnight, next local midnight), then convert
both boundaries to UTC before comparing timestamps. WIB is UTC+7: 01:00 WIB is
18:00 UTC on the previous date. A local evening remains on that UTC date.
Use timezone-aware boundaries for regions with daylight-saving changes.

A Monday stand-up reaches back to the previous working day, usually Friday, for
blockers and continuity; its plan comes from open assignments. Honor the user's
window and working-calendar overrides. Do not use an empty morning timeline as
proof that there is no work planned.

## Scan and merge evidence

Read `references/scan-recipes.md` before scanning. Use `timeline me` and filter
by project IDs: `--person` and `--project` are mutually exclusive. Check pagination
until the window is covered; an incomplete scan cannot establish no activity.

For a combined weekly report, use this week's per-epic IPM updates where available
and scan directly for uncovered projects. Reconcile duplicated events so an IPM
update and its underlying activity are not counted as two achievements.

Merge the user's context with the live evidence:

- Link each Basecamp-derived claim to its event or item. A completion event is
  recorded state, not independent validation of the deliverable.
- Include off-platform work the user reports, labeled “user-reported; not yet
  reflected in Basecamp.” Do not invent a link for it.
- Absence from the timeline is not a contradiction of off-platform work. Ask
  only when sources actually disagree about a relevant fact, date, or status.
- Separate work performed from items filed on the user's behalf by automation.
  Unknown provenance stays explicit; do not silently discard uncertain items.
- Do not infer a blocker’s cause from lack of activity, or another person's
  activity from the user's feed. Read relevant comment threads when needed.
- Anything in neither source does not appear. A quiet window is a valid result.

## Draft the selected report

Use `references/message-formats.md` for the five report formats. Daily reports
covering several projects group items by project. Keep them concise and in the
user's voice. Compare planned and actual work only when the real morning plan
is available. Trace each claim to Basecamp or explicitly to the user.

## Post when authorized

Show the exact content and destination. Proceed if the conversation already
explicitly authorizes that concrete post; otherwise ask once. Approval to draft
is not approval to publish. Explain the action plainly; expose a shell command
only when useful. If credentials lack write scope, return the reviewed draft
and explain the missing capability instead of claiming success.

Posting commands and rendering details are in `references/scan-recipes.md`.
Use `--no-subscribe` for daily stand-ups and show-and-tells. Use a Basecamp draft
when the user requests that destination. Comment/message bodies accept Markdown;
todo descriptions do not follow the same rule. Give the resulting URL after a
successful post, and report errors without pretending the write happened.

## Suggested next actions

Offer at most two or three actions supported by the evidence: unresolved
questions, discovery without a follow-up, review without reviewer activity,
or user-reported work without a todo. Label suggestions as suggestions.

If the user wants a suggestion turned into a todo, use `todo-planner`, which
owns readiness and the 11-field format. If absent, preserve the suggestion and
offer `npx skills add ahadinoto/buspro-skills --skill todo-planner -g`.
Do not assume a companion is installed or author a todo without its quality gate.
