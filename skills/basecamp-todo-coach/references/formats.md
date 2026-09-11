# Formats

Copied from the tracker's **Locked** sections. Do not edit here — edit the
tracker, then regenerate this file.

Source: the `buspro-skills` repo's `docs/basecamp-todo-coach/quality-system-tracker.md` (v3.9), via Gem
instruction v4.11.

---

## 1. Project Starter Context

Lives in the **Basecamp Project Description**.

Ask at most these questions:

1. What is the project / initiative name?
2. What problem are we trying to solve?
3. What output or result do we want?
4. Who is the main PIC / owner?
5. Who is the named Validation PIC, if already known?
6. What system, process, data, or document is involved?
7. Anything still unclear, out of scope, or risky?

If the user cannot answer some parts, do not block — put them under Open
Questions / Risks.

```text
[Project Starter Context]

Project / Initiative:
[Name]

Problem / Background:
[Problem being solved]

Target Output / Success:
[What should exist, improve, or become clearer]

People:
- Main PIC / Owner: [Name]
- Validation PIC: [Name, if known]
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

---

## 2. Individual Todo Format

The todo **title** uses the title rule. Everything below goes in the todo's
**description / notes** field.

```text
Todo Name / Title:
[Short title using the title rule]

Feature / Epic:
[The broader Todo List / Epic this todo belongs to]

Dependencies:
[Links to todos that must be completed before this one — title + Basecamp URL.
If none, write None.]

Updates/Changes Needed:
[Short summary of what needs to happen]

Detail:
[Specific breakdown of what to do, change, check, discuss, or produce]

Description:
[Context, problem, or reason behind the todo]

Acceptance Criteria / Done Criteria:
- [Specific, testable condition]
- [Specific, testable condition]

PIC / Owner:
[Named person responsible]

Validation PIC:
- Requirement Confirmation: [Named person, if applicable]
- Final Validation / UAT: [Named person, if applicable]
- Internal Review: [Named person, if applicable]

Open Questions / Assumptions:
- [Question, assumption, risk, or unclear point]

Tip:
[2–4 lines of practical help for whoever picks this up]
```

Rules:

- If a field is not applicable, write `N/A` or `None` and briefly say why. Do not
  delete the field. **`Tip` is the one exception — it is never `N/A`.**
- Assignee, due date, and status are **never** in this text. Assignee and due
  date are native Basecamp fields; status is the Todo Group.

### Fields removed 2026-07-29

`Todo Type` and `Module / Area` used to be fields here — both are gone (Locked
#2 amended, mentor-initiated). Both were redundant with information already
carried elsewhere:

- **Todo Type** is fully expressed by the title's `[Todo Type]` prefix (see the
  Title Rule below and `todo-types.md`'s prefix table). No separate field is
  needed to say it twice.
- **Module / Area** is fully expressed by the Epic/Todo List name, which already
  carries it — `[Module / Area] - [Outcome / Feature Name]` (see section 3). A
  todo already belongs to a Feature/Epic with that name, so repeating the module
  on every child todo added nothing.

### Dependencies field

Added 2026-07-29 (Locked #2 amended). Links to other todos that must be
completed before this one can start — predecessors only, not a general
"related work" list.

- List each blocking todo as a link (title + Basecamp URL), never a bare Work
  Breakdown number. A number describes the brief's list position, which can
  shift as items are added or reordered; a link points to the actual todo
  regardless.
- If none, write `None`.
- What this todo feeds into belongs in Description as a sentence, not here —
  there is often no todo yet to link to for that direction.
- Basecamp todo and todo-list content is sent as-is, not converted from
  Markdown, so links here must be real `<a href="...">` HTML anchors when
  written, never `[text](url)` Markdown syntax.

The format is now **11 fields**, ending in `Tip`.

### The Tip field

Added 2026-07-28 (Locked #2 amended). Short, practical help for whoever picks up
this todo — written mainly for first-time process mappers and the Business
Process team.

- **Always present.** Every todo has one.
- **Fitted to this todo, never boilerplate.** Use the per-type material in
  `todo-types.md` as raw material, then adapt it to the actual system, process,
  or risk in front of you. The same four sentences repeated across every
  Process Mapping todo in a project is a defect, not consistency.
- **Never `N/A`.** There is always something useful to say.
- **2–4 lines.** Plain language. No lecturing. Do not restate the Detail or the
  Done Criteria.
- **Never affects readiness.** A todo without a Tip is not a defect in Review
  Mode — just add one. Reviewers must not read the Tip as scope, requirement, or
  commitment.

Good:

```text
Tip:
Start from the moment Finance receives the settlement file and walk forward.
Map what really happens today, not what the SOP says. The approval step is
where this kind of flow usually breaks — check who actually signs off versus
who is supposed to. Leave exceptions for a second pass.
```

Bad (generic — would read identically on every Process Mapping todo):

```text
Tip:
Process mapping means documenting the process. Make sure you talk to
stakeholders and capture all the steps accurately.
```

---

## 3. Epic / Todo List

Use when work is broad, multi-step, needs stakeholder alignment plus
SPIKE/Development/validation, or spans several days. **Never one giant todo.**

Steps:

1. Todo List name — `[Module / Area] - [Outcome / Feature Name]`,
   e.g. `Finance Ops - Settlement View`
2. Epic Brief in the Todo List's **description** field (older epics may keep it in the first comment — still valid)
3. Proposed todo items, each following the title rule

### Module / Area examples

Billing Hub · Settlement · Finance Ops · HR Process Improvement ·
Recruitment / TA · Onboarding · Content Series · Data / Reporting ·
Stakeholder Alignment · Cross-module

Use the system/app module if the Todo List is system-related; otherwise use the
process, business, or workstream area. This only names the Todo List (Epic) —
individual todos no longer repeat it (see section 2).

Guided questions: objective? main PIC? stakeholders? who confirms requirements /
does final UAT / does internal review? major phases or first todos? dependencies
or open questions?

For discovery/process epics, also ask: expected deliverables? risks? epic-level
completion criteria?

```text
[Epic Brief]

Objective:
[What this epic/module/workstream is trying to achieve]

Main PIC:
[Name]

Stakeholders:
- [Name] — [Team / Role]

Validation PIC:
- Requirement Confirmation: [Name] — [Team / Role]
- Final UAT / Result Validation: [Name] — [Team / Role]
- Internal Review: [Name] — [Role, if needed]

Work Breakdown:
1. [First todo / phase]
2. [Second todo / phase]

Dependencies / Open Questions:
- [Dependency, blocker, or question]
```

Do **not** include "Next IPM Update" in the Epic Brief — IPM updates are separate
dated comments.

### Optional sections for larger epics

- Process Boundary / Scope (proposed start point, end point, terminology to confirm)
- Expected Deliverables (numbered list)
- Risks
- Completion Criteria (epic-level done conditions)
- Recurring Governance (recurring todos, e.g. weekly stakeholder progress update)

Rules:

- **Offer** these when the epic is discovery/process work or spans several IPMs.
  They stay optional — the user decides. Keep the Epic Brief slim otherwise.
- Keep them epic-level. Work Breakdown stays a list of todo titles; per-item
  detail belongs in the todo items.
- The Epic has exactly **one** Main PIC. Other drivers go under Stakeholders as
  co-PIC / support.

See `examples.md` Example 23 for a discovery Epic Brief using optional sections.

---

## 4. IPM Update Comment

A new dated comment on the Todo List for every IPM while the Epic is active. The
Epic Brief — in the list description — stays stable as the source of truth;
progress goes here. Comments hold nothing but the IPM timeline.

Ask first: changes since last update? status movements (from → to)? blockers or
open questions + who must respond? decisions or help needed? next steps before
the next IPM? timeline/scope risk? Confirm the update date.

```text
[IPM Update - DD Month YYYY]

Progress:
- [Completed or changed since the last update]

Status Movement:
- [Todo title]: [Previous status] → [Current status]

Blocker / Open Question:
- [Blocker or question + who must respond]

Decision / Ask:
- [Decision or support needed]

Next Step:
- [Next action + owner]

Risk / Notes:
- [Timeline, scope, dependency, or quality risk]
```

Write `None` for any section with no update.

---

## 5. Todo Groups (status)

Standard groups inside a Todo List:

Backlog · Not Started · In Progress · In Review · On Hold · Completed

Avoid:

```text
Mapping flow incentive Sales Direct & Programmatic — In Review
```

Prefer:

```text
[Process Mapping] Map Sales Incentive flow
```

…placed under the **In Review** group.
