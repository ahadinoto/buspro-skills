# The 10 Todo Types

Copied from the tracker's **Locked** section #3. Do not edit here — edit the
tracker, then regenerate this file.

Epic / Module is **not** a todo type — it is a Todo List.

---

## Type reference

### 1. Confirmation

Use when a requirement, scope, output format, decision, assumption, or
Validation PIC needs confirmation.

Done = documented confirmation from a named stakeholder.

### 2. Meeting / Discussion

Use when broader alignment, discovery, or stakeholder discussion is needed.

Done = decisions documented + follow-up todos created.

### 3. Process Mapping

Use when the current or target process is unclear.

Done = flow / process map reviewed with the Validation PIC.

### 4. SPIKE

Use when the technical, data, or solution approach is unclear.

Done = options + trade-offs + recommendation reviewed. **The output is a
decision, not code.**

### 5. Development

Use when the requirement is clear enough to execute. Gated by the Readiness Rule.

Done = implemented per agreed logic, edge cases handled, confirmed by the named
Validation PIC.

### 6. UAT / Validation

Use when output is ready for stakeholder / reviewer validation.

Done = approved / approved with notes / needs revision. Issues become Follow-ups.

### 7. Documentation

Use when logic, process, a guide, SOP, or handover needs to be documented.

Done = stored in the agreed location, confirmed clear by the reviewer.

### 8. Follow-up

Use when an action item comes out of a meeting, UAT, review, blocker, or
feedback.

Done = completed, and the person who raised it has been updated.

### 9. Process Assessment

Use when a **mapped** process needs evaluation for issues and opportunities.

Done = what works / what does not, bottlenecks, risks, controls, and improvement
opportunities documented and reviewed. **Recommendations stay solution-neutral.**

### 10. Internal Review

Use when several deliverables need one consolidated quality review before final
validation — usually near the end of an Epic.

Done = findings fixed or turned into Follow-ups.

**Guardrail:** never one Internal Review per todo. Review of a single deliverable
belongs in that todo's Done Criteria and Validation PIC.

---

## Summary table

| Todo Type | Use When | Expected Output |
|---|---|---|
| Confirmation | Requirement, scope, decision, assumption, or Validation PIC needs confirmation | Confirmed decision / requirement |
| Meeting / Discussion | Broader alignment, discovery, or stakeholder discussion is needed | Notes, decision, follow-up items |
| Process Mapping | Current or target process is unclear | Flow diagram / process map |
| SPIKE | Technical, data, or solution approach is unclear | Recommendation and decision |
| Development | Requirement is clear enough to execute | Implemented change / output |
| UAT / Validation | Output is ready for stakeholder/reviewer validation | Approval / feedback / revision decision |
| Documentation | Logic, process, guide, SOP, or handover needs documenting | Document / guide / summary |
| Follow-up | Action item from meeting, UAT, review, blocker, or feedback | Resolved action item |
| Process Assessment | A mapped process needs evaluation for issues and opportunities | Assessment: strengths, issues, risks, controls, improvement opportunities (solution-neutral) |
| Internal Review | Several deliverables need one consolidated quality review | Reviewed/updated deliverables; findings fixed or converted to Follow-ups |

---

## Shared rules for all individual todos

1. Title uses `[Todo Type] Action + Object / Output`.
2. Validation PIC must be a named person, not only a team.
3. If the Validation PIC is unknown, create a Confirmation todo before Development.
4. A Development todo should only exist when the requirement is clear enough.
5. If stakeholder expectation is unclear → Confirmation or Meeting / Discussion first.
6. If the process is unclear → Process Mapping first.
7. If the technical, data, or solution approach is unclear → SPIKE first.
8. Open Questions / Assumptions should **expose** uncertainty, not hide it inside vague wording.
9. If a field is not applicable, fill it with `N/A` or `None` — do not delete the field.
10. Assignee and due date are set natively in Basecamp, not in the todo text.
11. Internal Review is only for consolidated multi-deliverable review — never one per todo.
12. Every todo carries a `Tip` fitted to that todo. Tip depth is calibrated by audience: the four types the Business Process team lives in — Process Mapping, Process Assessment, Confirmation, Meeting / Discussion — get scaffolded guidance for first-timers; the other six get lighter guidance. See "Tip material per type" below.

---

## Tip material per type

Every todo carries a `Tip` (Locked #2, amended 2026-07-28). What follows is **raw
material, not text to copy**. Pick the one or two points that actually apply to
the todo in front of you and rewrite them around its real system, process, or
risk. If your Tip would read identically on another todo of the same type, it is
not finished.

Depth is calibrated by audience. The first four are where the Business Process
team spends most of its time and where first-timers get stuck, so they carry
more scaffolding.

### Process Mapping — deep

- Start from the event that triggers the process and walk forward one step at a
  time. Do not start from the system.
- Map what really happens today, not what the SOP says should happen. These
  differ more often than people expect.
- Talk to the person who does the work, not only the person who owns it.
- Leave exceptions and edge cases for a second pass. A clear main flow helps more
  than a complete but tangled one.
- Name where each step happens (system, spreadsheet, chat, meeting) — handoffs
  between tools are where time is usually lost.
- Agree the start point and end point before mapping, or the map will keep
  growing.

### Process Assessment — deep

- Assess the mapped process, not the people running it.
- Separate what you observed from what you were told; label which is which.
- Look specifically at: waiting time between steps, rework loops, manual
  re-keying, steps with no clear owner, and controls that exist on paper but not
  in practice.
- Stay solution-neutral. "Approval takes 4 days because it waits for a weekly
  meeting" is an assessment; "we should build an approval tool" is not.
- Quantify where you can, even roughly — "about 2 days" beats "slow".
- Note what already works well. An assessment that only lists problems is easy
  to dismiss.

### Confirmation — deep

- Write the question so it can be answered yes or no, or with one concrete
  choice. Open questions come back as open answers.
- Say what you will do with each possible answer. That is what makes people
  reply.
- Confirm with the person who actually decides, not only the person who told you
  about it.
- Put the confirmation in writing — Basecamp comment, email, or chat. A verbal
  yes disappears.
- If you are confirming an assumption, state the assumption plainly first so the
  other person can correct it.

### Meeting / Discussion — deep

- Write the decision you need before the meeting, not the agenda. If you cannot
  name a decision, you may not need a meeting.
- Invite the people who can decide. Anyone else can read the notes.
- Send context ahead so the meeting is spent deciding, not explaining.
- Capture decisions and owners during the meeting; memory fades within a day.
- Every unresolved item leaves as a Follow-up todo with a named person, or it did
  not happen.

### SPIKE — lighter

- The output is a decision, not code and not a build. Timebox it.
- Write the question you are trying to answer at the top, and stop when it is
  answered.
- Compare at least two options, and say plainly what each costs.
- Record what you ruled out and why — that is often the most reused part.

### Development — lighter

- Re-read the confirmed requirement before starting. If it has changed, raise it
  rather than absorbing it quietly.
- Check the Done Criteria are still testable. If you cannot test one, it is not
  a criterion yet.
- Flag scope growth as it happens, not at the end.
- Agree with the Validation PIC how they will check it, before you finish.

### UAT / Validation — lighter

- Give the validator the criteria, not just the output. People cannot validate
  against an unstated standard.
- Test the realistic case first, then the edge case.
- Record the verdict as approved, approved with notes, or needs revision — not
  as a conversation.
- Turn every issue into a Follow-up with a named owner before closing.

### Documentation — lighter

- Write for the person who will read this in six months without context.
- Agree where it lives before writing. A good document in the wrong place is
  lost.
- Say what the reader should be able to do after reading it.
- Have one person who is not you read it and try to follow it.

### Follow-up — lighter

- Say where this came from — which meeting, review, or feedback — so the reason
  survives.
- One action per Follow-up. Bundled follow-ups stall.
- Close the loop with whoever raised it. Doing the work is not the same as
  reporting it done.

### Internal Review — lighter

- Review the set of deliverables together, looking for gaps and contradictions
  between them. Reviewing one at a time is what the individual todos are for.
- Check consistency first: do the deliverables agree on scope, names, and
  numbers?
- Fix small findings directly; convert anything larger into a Follow-up rather
  than holding the review open.
- Timebox it, or the review becomes another project.

## Title prefix shorthand

Titles use the short prefix. There is no separate Todo Type field in the todo
body (removed 2026-07-29 — redundant with this prefix); this table is the
reference for the full name behind each prefix.

| Title prefix | Full type name |
|---|---|
| `[Confirmation]` | Confirmation |
| `[Meeting]` | Meeting / Discussion |
| `[Process Mapping]` | Process Mapping |
| `[SPIKE]` | SPIKE |
| `[Development]` | Development |
| `[UAT]` | UAT / Validation |
| `[Documentation]` | Documentation |
| `[Follow-up]` | Follow-up |
| `[Process Assessment]` | Process Assessment |
| `[Internal Review]` | Internal Review |
