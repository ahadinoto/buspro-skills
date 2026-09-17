# Basecamp Todo Quality System — Working Tracker

_Last updated: 2026-07-29 (v3.9)_

## Overall Goal

Create a repeatable system that helps people write clear, reviewable, and executable Basecamp todos, even when they use AI/Gemini.

The final Basecamp structure should help:
- PIC understand what they are working on
- Mentor / reviewer quickly validate the intent and scope
- Stakeholder understand what will be delivered
- Future AI Agent summarize the work clearly

Terminology: **IPM = Iteration Planning Meeting** — the recurring checkpoint where the PIC presents progress, blockers, decisions needed, and next steps.

> **Canonical source note:** the formats and rules in this tracker are the single source of truth. The Gem instruction (#4) and the future Claude skill (#8) copy from here — when a Locked section changes, sync those artifacts.

> **Versioning note (2026-07-17):** the doc set (tracker, Gem instruction, examples doc, skill) is versioned together in the `buspro-skills` repo (live 2026-07-17 as `bc-coach/` inside the buspro repo; split into its own repo 2026-09-11 so the skill sits in `skills/` at a repository root, where `npx skills` discovers it reliably; renamed `buspro-skills` 2026-09-11 to hold more than one skill); each version bump is one commit whose message mirrors the changelog entry. The tracker stays the canonical decision log — the repo tracks text diffs. Mentee feedback goes directly to the mentor by whatever channel is easiest — chat, WhatsApp, verbal. A findings Google Sheet with a fixed column schema was planned here in July and never created; dropped 2026-09-11 in favour of the informal route, on the grounds that a form is friction during a small pilot. Changelog entries cite what a report said rather than a finding ID. The repo holds the installable skill under `skills/basecamp-todo-coach/` and the human documents under `docs/basecamp-todo-coach/`. The skill's `references/` follow this tracker rather than being hand-edited against it; `references/examples.md` became the canonical home of the worked examples in v2.7, when the duplicate root-level copy was deleted.

---

## Work Plan

| # | Workstream | Status | Notes |
|---|---|---|---|
| 1 | Define principles of a good todo | Locked | Decision doc already created |
| 2 | Agree on Basecamp todo format | Locked | Individual todo format agreed (2026-07-28: amended to 12 fields — `Tip` added; 2026-07-29: amended to 10 fields — `Todo Type` and `Module / Area` removed as redundant with the title prefix and the Epic/Todo List name; 2026-07-29: amended to 11 fields — `Dependencies` added, found useful while drafting real todos for a live epic) |
| 3 | Define todo types and required fields per type | Locked | 10 todo types (2026-07-14: + Process Assessment, Internal Review) |
| 4 | Create Gemini Gem instruction | In Progress | v4.12 — discovery-deliverable review added (2026-09-03); superseded for distribution by the generated bundles in #8, kept as fallback until a mentee validates them |
| 5 | Create example todos | In Review | v3.9 — 23 examples + routing cheat sheet; fitted Tips added 2026-07-28, Epic Brief placement updated 2026-07-29, `Todo Type`/`Module / Area` removed 2026-07-29, `Dependencies: None` retrofitted into all 13 full examples 2026-07-29, needs another review pass |
| 6 | Create How-To guide for mentees | In Review | Written as `docs/basecamp-todo-coach/README.md` (install, the six starter prompts, what a good review looks like, reporting); pending mentee feedback |
| 7 | Create presentation slides | Optional / Not started | Can be created after guidance is stable |
| 8 | Create universal agent skill (Agent/CLI + Paste mode) | In Progress | v3.2 built under `skills/basecamp-todo-coach/` in the `buspro-skills` repo, tracking instruction v4.12; own repo, installed via `npx skills`; browser-chat bundles generated from the same source; re-sync when #4 locks |
| 9 | Create initiative reporter skill (stand-up, show-and-tell, progress comment, IPM update, combined weekly) | In Progress | v2.2 built under `skills/basecamp-initiative-reporter/`; reads the live activity timeline, Agent Mode only; pilot pending |

---

## Basecamp Operating Model

Status: **Locked**

The Basecamp setup should follow a 3-layer structure:

```text
Project Space = Project / Initiative level
Todo List = Epic / Module / Workstream level
Todo Item = Executable task level
Todo Group = Status level
Todo List description = Epic Brief
Todo List comments = IPM update timeline
```

### 1. Project Space = Project / Initiative

A Basecamp Project Space represents one broader initiative or program.

Examples:
- EmDig Process Improvement
- HR Process Improvement
- Content Series Life Cycle

The **Project Starter Context** should live at this level, ideally in the **Basecamp Project Description**.

Purpose:
- Give stable project context
- Help human readers understand the initiative
- Help future AI Agent / CLI read the project context directly from Basecamp
- Avoid repeating the same context every week

### 2. Todo List = Epic / Module / Workstream

A Todo List represents one larger deliverable, module, or workstream inside the project.

Examples:
- Billing Hub - Sales Incentive
- Billing Hub - Finance Settlement View
- Content Series - Lifecycle Mapping
- HR Process - Onboarding Flow Revision

Naming format: `[Module / Area] - [Outcome / Feature Name]`

The **description** of each Todo List should hold the **Epic Brief**.

### 3. Todo Item = Executable Task

A Todo Item is the smallest executable work unit.

Examples:
- `[Confirmation] Confirm Finance settlement output`
- `[SPIKE] Review settlement join strategy`
- `[Development] Build Finance settlement view`
- `[UAT] Validate settlement view with Finance`

### 4. Todo Group = Status

Todo Groups are used to track status.

Example groups:
- Backlog
- Not Started
- In Progress
- In Review
- On Hold
- Completed

Rules:
- Status should live in the Todo Group, not inside the todo title.
- New todos default to **Backlog** or **Not Started**.
- **Assignee and due date are set natively in Basecamp**, not inside the todo text. The Gem/skill should remind the user when a todo is created.

Avoid:
```text
Mapping flow incentive Sales Direct & Programmatic — In Review
```

Prefer:
```text
[Process Mapping] Map Sales Incentive flow
```

Then place the todo under the **In Review** group.

---

## Project Starter Context

Status: **Locked**

The Project Starter Context should live in the **Basecamp Project Description**.

This is intentionally lightweight. It should provide enough context for a human or AI Agent to kick off the project, while allowing details to be clarified on-the-fly through Epic Briefs, todos, comments, meetings, SPIKEs, or IPM updates.

### Project Starter Context Format

```text
[Project Starter Context]

Project / Initiative:
[Name]

Problem / Background:
[What problem are we trying to solve?]

Target Output / Success:
[What should exist, improve, or become clearer after this project?]

People:
- Main PIC / Owner: [Name]
- Validation PIC: [Name, if already known]
- Key Stakeholders: [Name/team, if known]

Scope:
- In Scope: [Short list]
- Out of Scope: [Short list, or N/A]

System / Process / Data Involved:
- [System, tool, table, document, process, or artifact]

Open Questions / Risks:
- [Unknown, risk, dependency, or assumption]

Last Updated:
[Date]
```

### Starter Questions

When creating the Project Starter Context, the Gem should ask a small number of questions only:

```text
1. What is the project / initiative name?
2. What problem are we trying to solve?
3. What output or result do we want?
4. Who is the main PIC / owner?
5. Who is the named Validation PIC, if already known?
6. What system, process, data, or document is involved?
7. Anything still unclear, out of scope, or risky?
```

If the user cannot answer some parts, do not block the process. Put them under **Open Questions / Risks**.

How the Gem (Knowledge files/notebook + paste-based) and the future Claude skill (direct Basecamp access) consume this context is defined in workstreams #4 and #8.

---

## #1 — Principles of a Good Todo

Status: **Locked**

Decision doc created separately:

`basecamp_todo_principles_decision.md`

Key decisions:
- A good todo is a mini task brief, not just a reminder.
- Todo should explain what needs to be done, why it is needed, expected output, scope, validation owner, validation method, and open questions.
- User may use AI, but still owns the clarity.
- If requirement is unclear, create Confirmation, Meeting / Discussion, Process Mapping, or SPIKE before Development.
- Validation PIC must be a named person, not just a team.
- Broad work should become a Todo List / Epic / Module, not one giant todo.
- Epic / Module should have one main PIC.
- Epic PIC should present objective, breakdown, blocker, and validation plan during IPM.

---

## #2 — Basecamp Individual Todo Format

Status: **Locked**

### Locked Field Format

```text
Todo Name / Title
Feature / Epic
Dependencies
Updates/Changes Needed
Detail
Description
Acceptance Criteria / Done Criteria
PIC / Owner
Validation PIC
Open Questions / Assumptions
Tip
```

Amended 2026-07-28: `Tip` added as the 12th field (mentor-initiated, not from a mentee finding).

Amended 2026-07-29: `Todo Type` and `Module / Area` removed (mentor-initiated, not from a mentee finding). Both were redundant with information already carried elsewhere:
- **Todo Type** is fully expressed by the title's `[Todo Type]` prefix (see Todo Name / Title below, and #3's title-prefix table). Restating it as a separate field said the same thing twice.
- **Module / Area** is fully expressed by the Epic/Todo List name, which already carries it — `[Module / Area] - [Outcome / Feature Name]` (see the Basecamp Operating Model, Todo List section). A todo belongs to a Feature/Epic with that name already, so repeating the module on every child todo added nothing.

Amended 2026-07-29: `Dependencies` added (mentor-initiated, not from a mentee finding). Found useful while drafting a real sequential chain of todos for a live epic (Work Breakdown #13–17, each blocked on the one before it) — "assumes #10, #11, #12 are finished" buried inside Open Questions was easy to skim past; a dedicated field of links is not.

The format is now **11 fields**, ending in `Tip`.

### Todo Name / Title

Short, scannable Basecamp title.

Recommended format:

```text
[Todo Type] Action + Object / Output
```

Examples:
```text
[Confirmation] Confirm Finance settlement output
[SPIKE] Review settlement join strategy
[Development] Build Finance settlement view
[UAT] Validate settlement view with Finance
[Process Mapping] Map current settlement flow
```

### Todo Type

No longer a field here (removed 2026-07-29 — see above). Still a real concept:
it drives the title prefix, routing, and the per-type Tip material. Full
definition lives in #3 below, which already carried the complete list and
summary table; this section stopped duplicating it.

### Module / Area

No longer a field here (removed 2026-07-29 — see above). Still used to *name*
the Epic / Todo List (`[Module / Area] - [Outcome / Feature Name]` — see the
Basecamp Operating Model, Todo List section), just not repeated on every child
todo. Example values: Billing Hub, Settlement, Finance Ops, HR Process
Improvement, Recruitment / TA, Onboarding, Content Series, Data / Reporting,
Stakeholder Alignment, Cross-module.

### Feature / Epic

The bigger Todo List / Epic / Module this todo belongs to.

Examples:
- Finance Settlement View
- Order Mutation Tracking
- Cost Ledger Settlement
- HR Onboarding Flow

### Dependencies

Added 2026-07-29. Links to other todos that must be completed before this one can start. Predecessors only — not a general "related work" list.

Rules:
- List each blocking todo as a link (title + Basecamp URL), never a bare Work Breakdown number. A number describes the brief's list position, which can shift as items are added or reordered; a link points to the actual todo regardless.
- If none, write `None`.
- Only what blocks this todo. What this todo feeds into belongs in Description as a sentence, not here — there is often no todo yet to link to for that direction.
- Basecamp todo and todo-list content is sent as-is, not converted from Markdown, so links here must be real `<a href="...">` HTML anchors when written, never `[text](url)` Markdown syntax.

### Updates/Changes Needed

Short summary of what needs to happen.

### Detail

Specific breakdown of what needs to be done, changed, checked, discussed, or produced.

### Description

Context, problem, or reason behind the todo.

### Acceptance Criteria / Done Criteria

Specific, testable conditions that prove the todo is done correctly.

### PIC / Owner

Named person responsible for driving the todo.

### Validation PIC

Named person who confirms the requirement and/or validates the result.

Rule:
If Validation PIC is unknown, the task is not ready for Development. Create a Confirmation todo first.

### Open Questions / Assumptions

Anything that is still unclear, risky, or assumed.

### Tip

Added 2026-07-28. Short, practical guidance for whoever picks up this todo —
written mainly for first-time process mappers and the Business Process team, so
that someone new to this kind of work knows how to start.

Rules:

- **Always present.** Unlike the Epic Brief's optional sections, `Tip` is part of
  the individual todo format every time.
- **Fitted to this todo, never boilerplate.** The per-type tip guidance (see #3)
  is raw material. The Coach adapts it to the actual work — the system, the
  process, the known risk. A tip reproduced verbatim across every todo of the
  same type is a defect, not consistency.
- **Never `N/A`.** There is always something useful to say; type guidance
  guarantees a floor. This field is the one exception to shared rule #9.
- **2–4 lines**, plain language, practical. No lecturing, no restating the
  Detail or Done Criteria.
- **Never affects readiness.** A todo missing a Tip is not a defect in Review
  Mode and never blocks Development — the Coach simply adds one. Reviewers must
  not treat the Tip as scope, requirement, or commitment.

### Out of the text format (by decision)

Assignee and due date are managed through Basecamp's native fields, not duplicated in the todo text. Status is managed through the Todo Group.

---

## #3 — Todo Types and Required Field Expectations

Status: **Locked**

The 10 individual todo types (updated 2026-07-14 — Process Assessment and Internal Review added after Slate epic testing):

```text
Confirmation
Meeting / Discussion
Process Mapping
SPIKE
Development
UAT / Validation
Documentation
Follow-up
Process Assessment
Internal Review
```

### Shared Rules for All Individual Todos

1. Todo title should use `[Todo Type] Action + Object / Output`.
2. Validation PIC must be a named person, not only a team.
3. If Validation PIC is unknown, create a Confirmation todo before Development.
4. Development todo should only exist when the requirement is clear enough.
5. If stakeholder expectation is unclear, create Confirmation or Meeting / Discussion first.
6. If process is unclear, create Process Mapping first.
7. If technical, data, or solution approach is unclear, create SPIKE first.
8. Open Questions / Assumptions should expose uncertainty instead of hiding it inside vague wording.
9. If a field is not applicable, fill it with `N/A` or `None` instead of deleting the field.
10. Assignee and due date are set natively in Basecamp, not in the todo text.
11. Internal Review todos are only for a consolidated review of several deliverables (usually near the end of an Epic). Review of a single deliverable stays inside that todo's Done Criteria and Validation PIC — do not create one Internal Review todo per todo.
12. Every todo carries a `Tip` fitted to that todo (see #2). Tip depth is calibrated by audience: the four types the Business Process team lives in — Process Mapping, Process Assessment, Confirmation, Meeting / Discussion — get scaffolded guidance for first-timers; the other six get lighter guidance. Per-type tip material lives in the examples doc (#5) and the skill's `references/todo-types.md` (#8), never in the Gem instruction, which is at its size limit.

### Todo Type Summary

| Todo Type | Use When | Expected Output |
|---|---|---|
| Confirmation | Requirement, scope, decision, assumption, or Validation PIC needs confirmation | Confirmed decision / requirement |
| Meeting / Discussion | Broader alignment, discovery, or stakeholder discussion is needed | Notes, decision, follow-up items |
| Process Mapping | Current or target process is unclear | Flow diagram / process map |
| SPIKE | Technical, data, or solution approach is unclear | Recommendation and decision |
| Development | Requirement is clear enough to execute | Implemented change / output |
| UAT / Validation | Output is ready for stakeholder/reviewer validation | Approval / feedback / revision decision |
| Documentation | Logic, process, guide, SOP, or handover needs to be documented | Document / guide / summary |
| Follow-up | Action item comes from meeting, UAT, review, blocker, or feedback | Resolved action item |
| Process Assessment | A mapped process needs evaluation for issues and opportunities | Assessment sheet: strengths, issues, risks, controls, improvement opportunities (solution-neutral) |
| Internal Review | Several deliverables need one consolidated quality review before final validation | Reviewed/updated deliverables; findings fixed or converted to Follow-ups |

### Development Readiness Rule

Development todo is allowed only when:
- Requirement has been confirmed
- Expected output is clear
- Affected system/table/view/process/workflow/artifact is known
- Main logic or expected behavior is clear
- Validation PIC is a named person
- Acceptance Criteria can be tested

If these are missing, suggest:
- Confirmation
- Meeting / Discussion
- Process Mapping
- SPIKE

---

## Epic Brief Convention

Status: **Locked**

The Epic detail should be added to the Todo List's **description** field.

This description becomes the source of truth for the Epic / Module / Workstream. Comments on the Todo List are reserved for the IPM update timeline.

**Amended 2026-07-29 (was: first comment).** The original rule said "Since Basecamp Todo Lists do not have a dedicated structured description field, the Epic detail should be added as the first comment." That premise was wrong — Todo Lists do have a description field, exposed in the Basecamp UI and readable and writable via the API (`basecamp todolists show` / `todolists update --description`, verified 2026-07-29). With the premise gone, the description is the better home:

- It stays pinned under the list name instead of scrolling away beneath accumulating IPM comments.
- The brief is required to stay stable as the source of truth (see the IPM Update Comment Convention). A description is edited in place; an edited comment changes silently with no signal to readers.
- It keeps comments as a clean, chronological IPM timeline with nothing else mixed in.
- It renders by the same as-is rule as todo descriptions, so brief and todos no longer follow different rendering rules (comment bodies convert from Markdown).

**Backward compatibility.** Epics whose brief sits in the first comment remain valid — do not treat them as missing a brief. When reading, check the description first and fall back to the first comment. Migrate on the next substantive edit rather than as a sweep.

### Epic Brief Format

```text
[Epic Brief]

Objective:
[What this epic/module/workstream is trying to achieve]

Main PIC:
[Name of the person who owns the overall delivery]

Stakeholders:
- [Name] — [Team / Role]
- [Name] — [Team / Role]

Validation PIC:
- Requirement Confirmation: [Name] — [Team / Role]
- Final UAT / Result Validation: [Name] — [Team / Role]
- Internal Review: [Name] — [Role, if needed]

Work Breakdown:
1. [First todo / phase]
2. [Second todo / phase]
3. [Third todo / phase]

Dependencies / Open Questions:
- [Dependency, blocker, or question]
- [Dependency, blocker, or question]
```

Important:
Do not include `Next IPM Update` in the Epic Brief. IPM updates should be added as separate dated comments.

### Optional Sections for Larger Epics (added 2026-07-14)

For discovery/process epics, the brief may add these epic-level sections:
- Process Boundary / Scope (proposed start point, end point, terminology to confirm)
- Expected Deliverables (numbered list)
- Risks
- Completion Criteria (epic-level done conditions)
- Recurring Governance (recurring todos, e.g. weekly stakeholder progress update)

Rules:
- Keep optional sections epic-level. Work Breakdown remains a list of todo titles; per-item detail belongs in the todo items.
- The Epic still has exactly one Main PIC (per #1 principles). Other drivers go under Stakeholders as co-PIC / support.

---

## IPM Update Comment Convention

Status: **Locked**

The Epic Brief should remain stable as the source of truth for objective, ownership, stakeholders, validation PIC, work breakdown, and open questions.

For ongoing progress, the PIC should add a new dated comment to the Todo List for every IPM while the Epic is active.

### IPM Update Comment Format

```text
[IPM Update - DD Month YYYY]

Progress:
- [What has been completed or changed since the last update]
- [Relevant progress on child todos]

Status Movement:
- [Todo title]: [Previous status] → [Current status]
- [Todo title]: [Previous status] → [Current status]

Blocker / Open Question:
- [Blocker, question, or dependency]
- [Name of person who needs to respond, if applicable]

Decision / Ask:
- [Decision needed from mentor/team/stakeholder]
- [Support needed, if any]

Next Step:
- [Next action before the next IPM]
- [Owner, if not obvious]

Risk / Notes:
- [Timeline, scope, dependency, or quality risk, if any]
```

If a section has no update, write `None`.

---

## #4 — Gemini Gem Instruction

Status: **In Progress**

Gem name: `Basecamp Todo & IPM Coach`

Source of truth for the instruction text: **`docs/basecamp-todo-coach/gem-instruction-legacy.md`** — filename stays stable; the version (v4.x) lives in the doc header and in the changelog below. Do not restate its content here; sync it when Locked sections above change.

v4 changes vs v3:
- Deduplicated the readiness/routing logic (was repeated ~5×) and merged Review Mode with the Ready-to-Work Check.
- Reduced significantly from v3 and confirmed to paste without truncation on 2026-07-14.
- Added guided questions for the Epic / Todo List workflow (parity with Starter Context and IPM workflows).
- Defined IPM once at the top.
- Reworded Agent/CLI mode into a single paste-first "Getting Context" section (a Gem cannot call Basecamp directly).
- Added: new todos default to Backlog / Not Started; assignee and due date set natively in Basecamp.

v4.1 changes:
- Role section deduplicated against the Gem's Name and Description fields (identity/scope now live there; instructions keep a one-line role anchor because the Description field is UI metadata and may not reach the model).
- Freed space used for a full worked example: vague request → clarifying questions → Confirmation todo in the locked format.
- End-of-instruction marker added to detect paste truncation.

v4.2 changes:
- Getting Context rewritten as a priority order: (1) Gem Knowledge files (Drive initiative docs) for background, (2) pasted Basecamp content for scope + live status, (3) targeted questions for gaps.
- Guardrails added: cite which Knowledge file was used; confirm time-sensitive info; names found in documents are suggestions — confirm before filling PIC / Validation PIC.

v4.3 changes:
- Truth priority made explicit: pasted Basecamp content overrides Knowledge files for current scope, status, PIC, Validation PIC, and recent decisions.
- Full worked example moved to the #5 Examples doc; the Gem keeps only a short behavior example. Unconfirmed validators are marked `(to confirm)`.
- Todo Types compressed to one-liners; further prose trims (~11.6k → ~9.5k characters) while keeping Readiness Rule, Getting Context, and all format blocks intact.
- File renamed to `basecamp_todo_ipm_coach_gem_instruction_current.md` for stable referencing.

v4.4 changes (from Gem testing feedback, 2026-07-14):
- Output Style: simple, plain English for non-native speakers (short sentences, common words, no idioms).
- Todo types extended to 10: added Process Assessment and Internal Review (with anti-proliferation guardrail).
- Epic Brief: optional epic-level sections (Process Boundary, Expected Deliverables, Risks, Completion Criteria, Recurring Governance); Work Breakdown stays a title list.

v4.5 changes (consistency fixes, 2026-07-17):
- Individual Todo Format: Todo Type placeholder fixed from "one of the 8 todo types" to "one of the 10 todo types" (leftover missed in the v4.4 type extension).
- Tracker synced: Work Plan row #4 and "Remaining before Locked" updated from v4.3 to the current version; v4.3/v4.4 changelog entries reordered chronologically.

v4.6 changes (2026-07-17):
- Getting Context: Knowledge tier now covers direct files and the initiative's NotebookLM notebook.
- New guardrail (negative case of v4.2's "say which file"): if no Knowledge content is found for a project-specific question, the Gem says so plainly and asks for context or a Basecamp paste instead of guessing. Phrased as retrieval self-report — a Gem cannot detect whether a notebook is attached.

v4.7 changes (2026-07-17, from mentee finding #1 in `basecamp_todo_findings.md`):
- Epic workflow: for discovery/process epics the guided questions now also ask about expected deliverables, risks, and epic-level completion criteria, and the Gem offers the optional Epic Brief sections. Sections stay optional per Locked decision #6 — "make all sections mandatory" was rejected.
- Examples doc → v3.5: Example 23 added (discovery Epic Brief with optional sections) — growth rule satisfied (observed feedback, not speculative).

v4.8 changes (2026-07-28, mentor-initiated — not from a mentee finding):
- **Individual Todo Format → 12 fields.** `Tip` added as the last field, always present, fitted to the specific todo. Amends Locked #2; full rules recorded there.
- **Output Style → warmer delivery, unchanged verdict.** The Gem now names what the person already got right, frames gaps as questions rather than mistakes, and treats "unclear" as normal at the start of work rather than the author's fault. Explicitly *tone only*: `Ready` / `Needs Revision` labels are unchanged, the Readiness Rule is unchanged, and the Gem still refuses to polish a vague request into a Development todo. Softening the verdict was considered and rejected — the gate is what keeps unclear work out of Development.
- Trim pass to absorb the additions and hold the instruction near its size line.

v4.9 changes (2026-07-29, mentor-initiated — found in real use, not from a mentee finding):
- **Epic Brief moves from the first comment to the Todo List description.** Amends the Epic Brief Convention; full rationale and the backward-compatibility rule are recorded there. The original rule rested on a factually wrong premise — that Todo Lists have no description field. They do, and it is readable and writable via the API (`todolists show` / `todolists update --description`, verified 2026-07-29). The description keeps the brief pinned above the IPM comment stream, makes edits visible rather than silent, leaves comments as a clean IPM timeline, and puts the brief under the same as-is rendering rule as todo descriptions.
- **Backward compatible by design.** Briefs already sitting in the first comment stay valid; readers check the description first and fall back to the comment. No migration sweep — move a brief on its next substantive edit. Rewriting history was considered and rejected as churn with no reader benefit.
- Surfaced while drafting real todos for a live epic: the skill's Epic Brief precondition reported a missing brief on an epic that had a complete one in the description. Recorded as a reminder that a Locked rule can carry a false premise for months when nothing exercises it against live data.

v4.10 changes (2026-07-29, mentor-initiated — not from a mentee finding):
- **Individual Todo Format → 10 fields.** `Todo Type` and `Module / Area` removed. Amends Locked #2; full rationale recorded there — both were redundant with information already carried elsewhere (the title's `[Todo Type]` prefix, and the Epic/Todo List name's `[Module / Area] - [Outcome / Feature Name]`).
- Review Mode & Readiness Check: dropped "Module/Area + Feature/Epic clear?" down to just "Feature/Epic clear?" since there is no longer a Module/Area field to check.

v4.11 changes (2026-07-29, mentor-initiated — found while drafting real todos for a live epic, not from a mentee finding):
- **Individual Todo Format → 11 fields.** `Dependencies` added, right after `Feature / Epic`. Amends Locked #2; full field rules recorded there. Surfaced drafting a real sequential chain (Work Breakdown #13–17, each blocked on the one before it) — a dependency note buried in Open Questions prose was easy to skim past.
- Dependencies links to other todos, never bare Work Breakdown numbers — numbers describe list position, which shifts; links point to the object regardless.

v4.12 changes (2026-09-03, mentor-initiated — found while reviewing a live Process Mapping deliverable):
- **Discovery Deliverable Review added.** Completion reviews now distinguish the quality verdict from the Basecamp state and compare each Done Criterion with the actual artifact, comments, and attachments. A completed checkbox is not evidence by itself.
- **Traceable discovery standard.** Current-state mapping is kept separate from improvement ideas; reviewers check coverage across all named systems/sheets, input/output traceability, field ownership, terms, and supporting evidence. User-confirmed verbal validation is accepted unless written approval is explicitly required, but should be recorded in Basecamp.

### Gem Configuration (decided; distribution model added 2026-07-17)

- **Name:** Basecamp Todo & IPM Coach (base). Initiative copies: `Basecamp Coach — [Initiative]`.
- **Description:** "A project-agnostic assistant that helps users create clear, reviewable, and executable Basecamp structures: Project Starter Context, Epic Briefs, individual todos, todo reviews, and IPM update comments."
- **Default tool:** None — coaching runs in plain chat; a default Canvas/Deep Research would hijack the Q&A flow.
- **Knowledge citations:** leave enabled.

Distribution model (2026-07-17 — verified: a shared Gem does not carry its NotebookLM connection; notebooks are shareable directly and auto-sync new sources; Gem file limits are plan-dependent — verify in the UI):

- **Base Gem** — instruction + #5 examples doc as direct Knowledge files, no notebook. Shared to the Business Process group (buspro@) as Viewer for ad-hoc coaching. Add the #6 How-To guide here once ready.
- **Per-person copies for initiative work** — duplicated from the base (forced by the sharing restriction), thin shells: identical instruction + the initiative notebook + the examples doc.
- **One shared NotebookLM notebook per initiative** — owned by that initiative's Main PIC, shared to mentor + team; holds the initiative docs end-to-end (mapping, assessment, requirements, specs, meeting notes). The notebook is the single source of project knowledge, so copies cannot drift on content. Keep notebook sources mirrored from the initiative Drive folder(s) so the future skill (#8) reads the same docs.
- **Copies differ in name + Knowledge only** — instruction text stays byte-identical to `_current`. Any behavior tweak routes through this tracker → new base version → re-paste all copies.
- **Governance** — version self-check (ask a copy "what instruction version are you running?"); announce version bumps to buspro@; NDA rule applies at notebook membership (members see all sources; no confidential folders in the base Gem's viewer-visible Knowledge).
- **Fallback if the notebook proves unreliable in testing** — system docs stay direct Knowledge files; the notebook holds only the project long tail.

Remaining before Locked (reopened 2026-07-28 by v4.8, still open through v4.12):
- Re-paste v4.12 from the current file (check the end marker survives) and set up one pilot initiative per the distribution model (base copy + shared initiative notebook).
- Test the v4.8/v4.10/v4.11 changes specifically: (a) the Tip is fitted to the todo rather than repeated boilerplate across todos of the same type; (b) warmer tone has not softened the readiness gate — a vague request must still be refused, not polished; (c) the Gem no longer asks for or restates Todo Type / Module / Area as separate fields; (d) Dependencies are written as links to specific todos, not as bare Work Breakdown numbers.
- Test the v4.12 review path with a completed discovery deliverable: it should distinguish evidence from status, keep improvement ideas out of the current-state map, and accept user-confirmed verbal validation without inventing written proof.
- Test against real todo requests — including one answered from Knowledge and one where a notebook source conflicts with pasted Basecamp content (Basecamp must win).
- Notebook checks: (1) attachment persists after save/reopen and after re-pasting the instruction; (2) canary question answerable only from a notebook source; (3) replies name the specific source doc and citations render; (4) truth priority holds via notebook (test above); (5) a newly added notebook source is visible on the next prompt (auto-sync).

---

## Remaining Workstreams

### #5 — Create Example Todos

Status: **In Review** — `skills/basecamp-todo-coach/references/examples.md` (was the root-level `basecamp_todo_example_todos_v3.md` until 2026-09-11; see #8 v2.7)

Purpose:
Prepare practical examples showing bad vs better todos for each major todo type.

All person names in the examples are fictional (real names live only in project-specific briefs).

Coverage (unchanged since v3.5 — 23 examples + cheat sheet, now including Process Assessment (21) and Internal Review (22) so all 10 types have a full example): bad-vs-better per todo type (1–8), Epic in disguise (9), unknown Validation PIC (10), IPM update (11), Knowledge-vs-Basecamp conflict (12), hidden process uncertainty (13), title/status/native-field hygiene (14–16), Project Starter Context kickoff (17), Review Mode response structure (18), Bahasa Indonesia interaction style (19), Ready verdict / when to stop coaching (20), and Routing Boundaries quick contrasts (Confirmation vs Meeting, SPIKE vs Process Mapping, Follow-up vs new Development). Includes title-prefix shorthand convention and an index. Example 23 (discovery Epic Brief with optional sections) added 2026-07-17 from mentee finding #1.

Growth rule: add new examples only from observed misrouting or real mentee questions during Gem testing — not speculatively.

v3.6 (2026-07-28, mentor-initiated): no new examples — the growth rule is untouched. Every example showing a full todo body gained a fitted `Tip` per the amended Locked #2, and the "Why it fails" wording was softened to the v4.8 tone (warmer delivery, same substance). This doc now also carries the per-type tip material the Gem instruction is too small to hold. Needs another review pass before #5 can Lock.

v3.7 (2026-07-29, mentor-initiated): no new examples — the growth rule is untouched. Example 9's "Better" heading changed from "First comment in Todo List" to "Todo List description", following the amended Epic Brief Convention.

v3.8 (2026-07-29, mentor-initiated): no new examples — the growth rule is untouched. `Todo Type` and `Module / Area` field blocks removed from all 13 "Better" examples that had them, following the amended Locked #2 (now 10 fields). The title-prefix shorthand note was reworded — there is no separate Todo Type field to describe, so it now just points to the field's removal.

v3.9 (2026-07-29, mentor-initiated): no new examples — the growth rule is untouched. `Dependencies: None` added to all 13 "Better" examples that have a full todo body, following the amended Locked #2 (now 11 fields). None of the existing examples have a real predecessor to link, so all read `None` — a worked example with a real Dependencies link belongs in a future addition once one surfaces from real use, per the growth rule.

Next: team review, then attach as Gem Knowledge and reuse as the skill's `references/examples.md`.

### #6 — Create How-To Guide for Mentees

Status: **Not started**

Purpose:
Create a simple onboarding guide that explains how mentees should use the Gem, write Basecamp todos, prepare IPM updates, and validate readiness before work starts.

### #7 — Create Presentation Slides

Status: **Optional / Not started**

Purpose:
Create slides for presenting the todo quality system to the team after the format, Gem instruction, examples, and guidance are stable.

### #8 — Create Claude Skill (Agent/CLI Mode)

Status: **In Progress** — design record `docs/basecamp-todo-coach/design-record.md` (v2.8; filename now stable, version lives in the header); built artifact `skills/basecamp-todo-coach/` (v3.2)

2026-09-03 (v2.6): synced to instruction v4.12 — added the discovery-deliverable review mode and `references/deliverable-review.md`. The review separates evidence-based quality from Basecamp state, accepts user-confirmed verbal validation when written proof is not required, and keeps current-state discovery distinct from later improvement ideas.

2026-07-28 (v2.2): synced to instruction v4.8 — 12-field todo format with `Tip` in `references/formats.md`, per-type tip material for all 10 types in `references/todo-types.md`, warmer Output Style in `SKILL.md` with the readiness gate explicitly unchanged.

2026-07-29 (v2.3): synced to instruction v4.9 — Epic Brief reads from and writes to the Todo List description across `SKILL.md`, `references/formats.md`, `references/basecamp-cli.md`, and `references/examples.md`. The Epic Brief precondition now checks the description first and falls back to the first comment, so pre-2026-07-29 epics are not reported as missing a brief — this was a live false positive, which is how the wrong premise was caught. `references/basecamp-cli.md` also gained two write gotchas found while applying this to a live epic: `todolists update --description` replaces the whole field, so amending a brief means read → edit full text → write back; and `--name` must be sent alongside `--description` or the API returns 422 Unprocessable Entity.

2026-07-29 (v2.4): synced to instruction v4.10 — `Todo Type` and `Module / Area` removed from the individual todo format across `SKILL.md`, `references/formats.md`, `references/todo-types.md`, `references/basecamp-cli.md`, and `references/examples.md` (10-field format). Review Mode's readiness checklist dropped its "Module/Area" clause. The title-prefix table in `references/todo-types.md` was reworded from "Todo Type field" to "Full type name" since no such field remains.

2026-07-29 (v2.5): synced to instruction v4.11 — `Dependencies` field added across `SKILL.md`, `references/formats.md`, and `references/examples.md` (11-field format). `references/basecamp-cli.md` gained a gotcha: Dependencies links must be real `<a href>` HTML anchors on write, since todo content is sent as-is and not converted from Markdown. Found and applied while drafting a real five-todo sequential chain (Work Breakdown #13–17) for a live epic.

2026-09-17 (v3.1 coach / v2.1 reporter, mentor-initiated, grilled): **project registry and local context**, resolving ten decisions taken in a structured grilling session. Phases 1–2 of 5.

The starting proposal was a local mirror of Basecamp content — `project_starter_context.md` and epic briefs written to disk alongside Basecamp, with "any changes must update both". That was rejected, and the reasoning is the point:

- **Dual-write cannot be reconciled.** Two independently authored copies of one fact give no way to know which is right when they disagree, and the agent reads the stale one with full confidence. This repo has already removed three instances of exactly that failure — a 49 KB duplicated examples doc, a divergent hand-made Codex skill, a hand-maintained Gemini prompt. It also contradicted the Locked truth-priority rule ("docs go stale; Basecamp is the operating source of truth").
- **The stated motive did not survive measurement.** "So the agent won't need to hit BC" was the reason for mirroring. Reading full project context measured ~1.09 seconds and ~3.6 KB — cheaper than reading two local files, and never stale.

What was built instead, one source per fact:

- **`~/.config/buspro-skills/projects.md`** — a fixed-path registry of monitored projects (ID authoritative, not name), each with an optional local folder, plus one reporting destination for the ritual reports. Missing → the agent asks, shows the file, and writes only on confirmation. This is the direct fix for the one piece of mentee feedback received so far, that the agent could not find the context.
- **Local folders hold only what Basecamp cannot** — private notes, and supporting artifacts such as AppSheet schema and CSV exports. Never a copy of Basecamp content. The truth-priority rule gained a clause saying so.
- **Digests, not summaries.** A large artifact is digested once into `<file>.digest.md` recording the source's size and modified time. The fingerprint is compared before the digest is trusted, so a refreshed export invalidates it automatically. Derived one-way from a single source, staleness always detectable — a cache, not a mirror.
- **Read rule by file kind**, not by size: prose read whole, structured data never — headers, types, row count, value ranges, ~20 sample rows. Behaves the same on a 200-row export and a two-million-row one.
- **Write safety by ownership**: generated files carry a `GENERATED` header and are rewritten freely; user-authored files are never overwritten without showing the change first. Same split the repo already uses for `dist/`.

Mechanism: **`shared/` plus `tools/sync-shared.py`.** `npx skills` installs one skill directory and nothing else, so anything two skills both need must exist in both. Copying by hand is what produced the three failures above, so the copies are generated from a canonical source, marked `GENERATED`, and `--check` verifies they are current. `publish-public.sh` now refuses to publish stale copies, alongside its existing denylist guard.

Caught while building, both the same bug class: the new references appeared in the browser-chat bundles as file paths, telling a Gem to open files it can never have; and excluding the filesystem section pushed `gem-compact` over its hard cap until the section was dropped from both Gem targets, with the one instruction that mattered ("ask which project") relocated into the paste header.

Phases 3–5, same day:

- **Backlog Health Summary** (`formats.md` section 5) is the coach's bulk review mode. The readiness gate runs underneath unchanged; the output is framed for a stakeholder asking "where does this initiative stand?" — counts first, one line per todo naming its single biggest gap, epic-level gaps ranked above item-level ones, and at most two suggested focus items. Measured against real projects (1, 17 and 7 todos), so a per-todo four-part review of a whole project would have been thousands of words nobody reads. It reports state and deliberately does not create or rewrite todos — gaps become work through the individual todo workflow, where the gate applies.
- **Combined weekly update** is the reporter's fifth report, across every monitored project, posted to the reporting destination. It is built from the per-epic IPM updates where those exist rather than re-deriving everything from the timeline, so the two stay consistent by construction. Projects with no activity are omitted rather than listed as empty.
- Both skill descriptions were updated, since a workflow the description does not advertise cannot be triggered.
- `AGENTS.md` gained the shared-text convention so the next skill does not hand-copy.

Same trap caught twice more while building, and worth stating as a rule: **`gem-compact` selects format sections by name, so any new section is silently dropped unless its manifest lists it.** Adding `5. Backlog Health Summary` required a manifest edit; forgetting it would have shipped a compact bundle missing the new mode with no error.

2026-09-16 (v3.0 coach / v2.0 reporter, mentor-initiated): **the two comment workflows moved to the reporter**, and all four reports became scan-backed.

- **The split now follows one rule**: the coach authors and gates work items; the reporter reports on activity. `IPM Update Comment` and `Todo Progress Comment` moved out of the coach's `formats.md` into the reporter's `message-formats.md`, and the coach's remaining format sections were renumbered 1–4.
- **Why the earlier reasoning was wrong.** The two comment workflows had been kept in the coach because they worked from user input alone and therefore survived Paste Mode. The intent is that they scan Basecamp too — an IPM update should read a week of timeline rather than have the PIC reconstruct status movements from memory. Once they scan, they cannot work in browser chat at all, so there was no Paste Mode capability left to protect.
- **All four reports share one pipeline**: user's context → scan Basecamp → merge → draft → confirm → post. They differ only in window and target. The merge step is the point: the scan knows what changed and when, the user knows the decision taken in a meeting and why something stalled. Work the user reports with no Basecamp trace is included and labelled as such rather than dropped; where the two conflict, the skill asks instead of picking a side.
- **Posting targets decided**: stand-up and show-and-tell go to the project message board (with `--no-subscribe`, since a daily notification to the whole project trains people to ignore it); progress comments go on the todo they describe; IPM updates stay on the todo list. Nothing posts without explicit confirmation.
- The `Todo Group` status vocabulary is restated in the reporter so the skill stands alone when installed, with the coach named as canonical — a deliberate 300-character duplication rather than a cross-skill file reference, which `npx skills` cannot deliver.

2026-09-16 (v2.9, mentor-initiated): **Todo Progress Comment** added as format section 6, with a seventh workflow to produce it.

- **Defines a convention the operating model was missing.** Comments on the Todo List have always been the IPM timeline; comments on an *individual todo* had no defined meaning. They now hold dated progress entries, one per day per todo. The two never mix: an IPM update summarises an epic for a meeting, a progress comment records one todo's day.
- **Written for two audiences, and the second one drove the design.** The request was a comment "an AI agent can read". An agent reading the todo weeks later has no memory of the conversation that produced the comment and cannot ask a follow-up, so anything implied is lost. Hence: absolute dates only, named people rather than pronouns or roles, status in the exact Todo Group vocabulary, fact separated from assumption, no implied context, real URLs.
- **Input is the user's own account, not a scan.** The user says what they did; the skill arranges it. It does not read Basecamp to discover progress — that is `basecamp-initiative-reporter`'s job — and it does not invent progress. Where the account is vague about whether something finished, it asks rather than resolving it into `Done`. Same discipline as the readiness gate: a tidy comment covering work that did not happen is worse than a rough one, because it is later read as fact.
- **Markdown is fine here.** Comment bodies convert from Markdown while todo and todo list bodies are sent as-is, so this format uses real labels and lists — unlike the 11-field todo body.
- Placement was reconsidered mid-design. Progress *reporting* belongs to the reporter skill; this is progress *formatting* from user-supplied words, which is the coach's existing competence and the same shape as the IPM update workflow.

2026-09-11 (v2.8, multi-skill repo): repo restructured to hold more than one skill. No coaching rule changed and the skill's behaviour is untouched — only its citation of this tracker's path.

- **Renamed `bc-coach` → `buspro-skills`.** Done before any remote existed, so it cost a `mv`; after mentees install it would change everyone's install URL. Naming it plain `skills` was rejected: the discovery container must literally be `skills/` inside the repo, which would have produced `skills/skills/<name>/`.
- **Human docs moved to `docs/basecamp-todo-coach/`** and renamed — `quality-system-tracker.md`, `design-record.md`, `gem-instruction-legacy.md`, plus a per-skill `README.md`. Drops the `_clean_v3` / `_current` suffixes, consistent with the existing convention that filenames stay stable and the version lives in the header. `docs/` rather than `reference/`, since each skill already has its own `references/`.
- **A per-skill layout (`<skill>/skill/`, `<skill>/tools/`, …) was considered and rejected.** Tested against skills@1.5.25: two skills nested that way were both discovered, then **both vanished from the listing** the moment a third skill was added conventionally at `skills/<name>/`. It also would have duplicated the ~400-line bundler per skill, recreating the duplication removed in v2.7. The motivating goal — mentees installing one skill rather than all — needed no restructure: `--skill <name>` already installs exactly one, and `npx skills` installs only that skill's directory, so self-containment is enforced by the installer regardless of layout.
- **Both tools parameterized by skill.** `build-web-prompt.py` gains `--skill` / `--target` / `--list`, moves per-skill manifests into a `BUNDLES` table keyed by skill name with paths relative to each skill directory, and writes to `dist/<skill>/<target>/`. A skill with no `BUNDLES` entry is simply not bundled for browser chat, and says so. `install-global.sh` takes an optional skill name, defaults to linking all, and validates names before touching anything.
- **Divergent Codex copy deleted.** A hand-made variant had been living in `~/.codex/skills/basecamp-todo-coach/` — reworded section headings, a CLI reference compressed from 9.5 KB to 1.9 KB, and 109 bytes of Codex display metadata. Checked before deleting: same 23 examples, neither copy carried the fields removed in v2.4, and every "unique" heading was a rename of an existing one (`Start with the right evidence` for `Evidence first`, `5. Status and workflow state` for `5. Todo Groups (status)`). No unique substance, so it went. All four agent directories on the maintainer's machine now symlink to the one canonical skill — the drift this workstream exists to prevent.
- **GitLab migration guidance dropped.** Both readmes carried a note about moving to the company GitLab. Speculative and possibly never happening, so it is gone from anything a mentee reads; the decision and its reversal stay recorded here. Nothing in the repo is host-specific, so a move would only change the source argument in the install command.
- **`AGENTS.md` added, with `CLAUDE.md` symlinked to it.** Repo conventions in one place that Claude Code, Codex, and Cursor all read. Deliberately *not* a symlink to this tracker: `CLAUDE.md` is auto-loaded every session, so pointing it at a 48 KB decision log would burn context on history instead of telling an agent what to do. It states the self-containment rule, the tracker-first rule, and that renaming a skill heading breaks the bundler on purpose.

2026-09-11 (v2.7, mentee-distribution): restructured into a universal agent skill. No coaching rule changed — the readiness gate, the locked 11-field format, the 10 types, and all 23 examples are untouched. What changed:

- **Own repo.** `bc-coach` split out of the buspro repo. `npx skills` scans documented containers at the repository root (`skills/`, `.claude/skills/`, `.agents/skills/`, … each walked at most three levels) and only falls back to an unbounded scan **when that finds nothing at all**. Verified against skills@1.5.25: a skill nested at `<repo>/sub/skill/<name>/` was found while it was the repo's only skill, and disappeared from the listing the moment a correctly located `skills/<name>/` skill was added. So the old nested layout worked by accident, and would have broken silently the first time any properly placed skill landed anywhere in buspro. Splitting also means mentees no longer need read access to the rest of buspro.
- **`skill/` → `skills/`.** Required by the same discovery rule.
- **Dual-mode preflight in `SKILL.md`.** A new `Operating Modes — Preflight` section makes the two modes explicit: Agent Mode when `basecamp auth status` reports `authenticated: true`, Paste Mode otherwise (CLI missing, not signed in, or browser chat with no shell). The old informal fallback paragraph now points at it instead of restating it. No separate connection-check script was written: `basecamp auth status` already returns JSON with `ok` and `data.authenticated`, so a wrapper would only add a moving part.
- **Web bundler.** `tools/build-web-prompt.py` generates browser-chat prompts from this same source, replacing hand-maintained Gem instruction text. Two tiers per target — instructions to paste, knowledge files to upload — because full skill content is ~93 KB and no instruction box holds that. Targets: `gem` (20.5 KB), `gem-compact` (14.1 KB, sized to the ~14.6 KB instruction already proven to paste without truncation per #4 v4.1), `gpt` (6.9 KB, under the 8,000-character Custom GPT cap). Content is selected by `##` heading name, so a renamed heading fails the build loudly rather than silently dropping a section. The end-of-instruction truncation marker from #4 v4.1 is carried into every bundle.
- **Examples de-duplicated.** `references/examples.md` was a byte-identical hand-copied duplicate of the root `basecamp_todo_example_todos_v3.md`, so the same 49 KB lived in the repo twice with a manual "edit the source, then re-copy" rule between them. The skill's copy is now canonical, the root duplicate is deleted, and the web bundler reads the skill's copy directly. All 23 examples verified intact.
- **Dangling references fixed.** `npx skills` installs only `skills/basecamp-todo-coach/`, so `SKILL.md` and `references/formats.md` pointing at a bare `basecamp_todo_quality_system_tracker_clean_v3.md` named a file no mentee receives. Both now say the tracker lives in the `bc-coach` repo and is not bundled.
- **Truncation check promoted to a setup step.** `README.md` now tells whoever sets up a Gem or Custom GPT to confirm the end-of-instruction marker survived the paste. A silently truncated paste does not look broken — it looks like a coach that has quietly stopped enforcing some rules, and gets reported as a rule bug that does not exist.
- **Feedback channel documented.** The skill's readme gained a reporting section asking reporters to say which setup they used and whether the truncation marker was present — the two details that make a report diagnosable. Reports go straight to the mentor; no form, no sheet.
- **`universal_skill_refactoring_plan.md` deleted.** An executed one-off with no inbound references; its substance, including what the plan got wrong, is recorded in the design record's v2.7 entry.

Distribution: **GitHub.** Mentees install with `npx skills add <repo> --skill basecamp-todo-coach -g`, which detects their installed agents and works with existing git auth, public or private. A move to the company GitLab was briefly planned and then dropped (2026-09-11) — GitHub is the home for now, and possibly for good. Nothing in the repo is host-specific, so a move would change only the source argument in the install command; there is no reason to plan for it in advance. Two rejected options: a root `install.sh` piped from `curl` (needs an unauthenticated raw URL, which a private repo does not have) and a `package.json` (`npx skills` resolves by directory layout and `SKILL.md` frontmatter, never npm metadata).

Purpose:
Port the coach to a Claude skill with real Basecamp access, so the agent reads Project Description, Epic Briefs, todos, groups, and IPM comments directly instead of asking the user to paste them.

2026-07-17 (draft v1.1): distribution-model implications recorded — one skill serves everyone (no per-person copies; context is read live); initiative notebook sources stay mirrored from Drive folders so Gem and skill read the same docs; the repo (versioning note at top) is the build source for `references/`.

2026-07-27 (v2.0 built): skill built ahead of #4 locking, explicitly tracking instruction v4.7 — re-sync `references/` when #4 findings change the instruction.

- **Integration decided: the official Basecamp CLI** (`github.com/basecamp/basecamp-cli`, v0.7.2, March 2026) — 155 endpoints, 100% of the in-scope API, OAuth, JSON envelopes, built-in `--jq`, `--agent --help` introspection, and its own agent skill + Claude Code plugin. The Coach skill does **not** implement Basecamp access; it layers this quality system on top and treats the CLI as transport. This closes the "which Basecamp integration" open decision — no community MCP, no custom API wrapper.
- **Structure:** `SKILL.md` (router) + `references/formats.md`, `references/todo-types.md`, `references/basecamp-cli.md`, `references/examples.md` (generated copy of examples v3.9). Reference files are generated from this tracker's Locked sections — regenerate on change, do not hand-edit.
- **Read-only by default.** Every write shows the exact content and the exact command, then asks for confirmation. A Development todo failing the Readiness Rule is never written, even on request.
- **Truth priority becomes automatic.** In the Gem, pasted Basecamp beats Knowledge docs by discipline; in the skill, the live CLI read *is* tier 1. Background Drive docs stay tier 2 (not yet implemented — Google Workspace CLI is a later addition).
- **No-access fallback:** if the CLI is missing or unauthenticated, the skill says so plainly and falls back to paste mode — the skill analogue of the v4.6 guardrail, except a skill can actually detect the failure.

- **Two-skill split:** plain Basecamp mechanics (list projects, complete a todo, post a message) route to the official `basecamp` skill. The Coach skill triggers only on quality/structure intent. Prerequisite per user: install the CLI and run `basecamp auth login`.
- **Named-person validation:** PIC / Validation PIC names are checked against `basecamp people list --project`. An unmatched name is a signal to confirm, not a reason to refuse — this operationalises Locked decision #4 rather than changing it.
- **Skill-only capabilities — dispositions agreed 2026-07-27:**
  - *Write gate (core).* Readiness is confirmed during the conversation, and creation is only allowed once it passes. This is the skill's primary control and applies to every todo type, not only Development. The batch review below is retrospective cleanup, explicitly nice-to-have.
  - *Named-person validation (always on).* PIC / Validation PIC checked against `basecamp people list --project`. An unmatched name prompts confirmation, never refusal. Operationalises Locked decision #4.
  - *IPM update pre-fill (offer-only).* Status diff since the last IPM comment seeds Progress and Status Movement as a starting draft; the guided questions still run. The context belongs to the PIC — the skill only tidies the update into the agreed format. Blockers, decisions, next steps, and risks are never inferred from Basecamp state.
  - *Epic Brief precondition (offer-only).* Fires only when the user starts epic-level work in a Todo List that has no Epic Brief — without one there is no objective, Main PIC, Validation PIC, or work breakdown to coach against. Check the Todo List **description** first, then fall back to the first comment (pre-2026-07-29 placement); a brief in either location counts. Raised once, never as a project-wide scan, and "this list is not an epic" is accepted as final. Not every Todo List is an epic.
  - *Hygiene sweep (offer-only).* On request: status words in titles, missing/wrong type prefixes, assignee or due date written into the body. Report and offer fixes; never auto-correct.

Remaining before Locked:
- Install the CLI (`basecamp auth login`) and verify five details locally: todo **description** flag on create (the 11-field format lives there); project description write-back; `todolistgroups` create/move semantics; todo list description read/write (the Epic Brief lives there — **verified 2026-07-29**: `todolists show` returns it, `todolists update --description` writes it); content rendering (todo and todo list descriptions are sent as-is while comment bodies convert from Markdown — this governs how the locked format renders, and why Dependencies links must be HTML anchors, not Markdown).
- Decide distribution (personal skill vs shared plugin vs internal marketplace) and whether mentees get write access at all.
- Re-sync `references/` after #4 locks.
