# Basecamp Todo Examples — Bad vs Better (Workstream #5)

Status: **Draft complete — v3.9** (all types, workflows, anti-patterns, and routing boundaries covered; team review pending)

Note: all person names in this doc (Sari, Dimas, Laras, Putri, Tono, Bayu) are fictional. They only demonstrate the "named person" rule — always use the real named person for the actual project. The systems, tables, and processes named here (Cost Ledger, Revenue Share, Order ID, Content Series, and so on) are likewise illustrative placeholders, not any real system — substitute your own when writing a real todo.  
Last updated: **2026-07-29**

Purpose:
- Provide practical bad-vs-better examples per todo type.
- Help PICs and mentees understand what good Basecamp work items look like.
- Serve as Gem Knowledge / skill reference so the coach has concrete examples of how to route vague work into the correct Basecamp structure.

How to use this doc:
- For humans: read the examples before creating or reviewing todos.
- For the Gem / skill: use these as behavior references, not as rigid scripts.
- For mentors/reviewers: use the “Why it fails” and “Coaching flow” sections to explain feedback.

Core reminder:
- Neat wording is not the goal; clarity is.
- If a request is unclear, do not polish it into a Development todo.
- Route it to the right earlier step: Confirmation, Meeting / Discussion, Process Mapping, or SPIKE.
- Validation PIC must be a named person. If the name is uncertain, mark it as `(to confirm)`.

Title prefix shorthand:
- Titles use the short prefix: [Confirmation], [Meeting], [Process Mapping], [SPIKE], [Development], [UAT], [Documentation], [Follow-up], [Process Assessment], [Internal Review].
- The title prefix is the only place Todo Type appears. There is no separate Todo Type field in the body (removed 2026-07-29 — see below).

Fields removed 2026-07-29:
- `Todo Type` and `Module / Area` are no longer fields in the todo body. Todo Type is redundant with the title's `[Todo Type]` prefix; Module / Area is redundant with the Epic/Todo List name, which already carries it (`[Module / Area] - [Outcome / Feature Name]`).

Fields added 2026-07-29:
- `Dependencies`, right after `Feature / Epic`. Predecessor todos only (what must finish first), each as a real link — never a bare Work Breakdown number, since numbers describe list position and links don't go stale when items are reordered. If none, write `None`, as every example below does (none of these standalone examples has a real predecessor to link). The format is now 11 fields.

Tip field (added 2026-07-28):
- Every individual todo carries a `Tip` as its last field.
- It is written for that specific todo, never copied between todos, and never `N/A`.
- A Tip is help for whoever picks the todo up. It is never scope, requirement, or commitment, and it never affects readiness.

Index:
1. Vague request → Confirmation
2. Broad alignment → Meeting / Discussion
3. Process unclear → Process Mapping
4. Technical/data uncertainty → SPIKE
5. Requirement clear → Development
6. Output ready → UAT / Validation
7. Knowledge capture → Documentation
8. Action item → Follow-up
9. Epic in disguise → Todo List + Epic Brief
10. Unknown Validation PIC → Confirmation first
11. IPM update comment
12. Knowledge doc vs pasted Basecamp conflict → Basecamp wins
13. Hidden process uncertainty → Process Mapping first
14. Overloaded title → short title + detail in body
15. Status in title → Todo Group
16. Assignee/due date in text → native Basecamp fields
17. Project kickoff → Project Starter Context
18. Review Mode response structure
19. Bahasa Indonesia interaction style
20. Review passes → Ready verdict (when to stop coaching)
21. Mapped process needs evaluation → Process Assessment
22. Consolidated deliverable review → Internal Review
23. Discovery epic → Epic Brief with optional sections
24. Routing Boundaries — quick contrasts

---

# Example 1 — Vague request → Confirmation todo

## Bad

```text
todo: settlement finance
```

Why it fails:
- No expected output yet — what should Finance receive?
- Scope is open — which part of settlement?
- No owner named.
- No named validator yet — who will confirm this is correct?
- Implies Development, while nothing has been confirmed.

## Coaching flow

The coach does not polish this. It asks:
- What output does Finance expect?
- Who validates it?

User answers:
> A settlement recap view, requirement not confirmed yet, probably Sari from Finance checks it.

`Probably` means the validator is not confirmed → create a **Confirmation** todo and mark the validator as `(to confirm)`.

## Better

```text
Todo Name / Title:
[Confirmation] Confirm settlement recap output with Finance

Feature / Epic:
Finance Settlement View

Dependencies:
None

Updates/Changes Needed:
Confirm expected settlement recap output and validation owner with Finance.

Detail:
Walk through the draft recap columns with Finance; confirm format, data source, and cut-off rules. Confirm who the named Validation PIC will be.

Description:
Request came in vague ("settlement finance"); output and validator are unconfirmed, so Development cannot start.

Acceptance Criteria / Done Criteria:
- Finance confirms the expected recap format and columns.
- Validation PIC for the recap work is confirmed by name (currently assumed: Sari).
- Confirmation is documented; follow-up Development todo is created.

PIC / Owner:
[User's name]

Validation PIC:
- Requirement Confirmation: Sari — Finance (to confirm)
- Final Validation / UAT: N/A (belongs to the later Development/UAT todos)
- Internal Review: N/A

Open Questions / Assumptions:
- Recap cut-off assumed monthly — confirm with Finance.

Tip:
Bring a draft of the recap columns to the conversation. Finance can correct something concrete much faster than they can describe it from nothing.
Ask Sari directly whether she is the person who signs off, or whether it is someone else. This often gets passed on.
Write the answer into a Basecamp comment the same day. A verbal yes disappears.
```

After creating:
- Set assignee and due date natively in Basecamp.
- Place the todo in Backlog or Not Started.
- Create the follow-up Development todo only after this confirmation is done.

---

# Example 2 — Broad alignment need → Meeting / Discussion todo

## Bad

```text
Discuss sales incentive
```

Why it fails:
- The topic is named, but not what needs to be discussed about it.
- No expected decision — what should be settled by the end?
- No participants or stakeholder owner listed.
- Nothing says what should exist after the meeting.
- Without those, the meeting is likely to lose focus.

## Coaching flow

The coach asks:
- What decision or alignment is needed from the discussion?
- Who needs to attend?
- What should be produced after the meeting?

User answers:
> Need to align with Finance and Sales Ops on how sales incentive is calculated from billed PO/Invoice.

This is not yet a Confirmation todo because the topic is broad. Use **Meeting / Discussion**.

## Better

```text
Todo Name / Title:
[Meeting] Align sales incentive calculation flow

Feature / Epic:
Sales Incentive Calculation

Dependencies:
None

Updates/Changes Needed:
Align Finance and Sales Ops understanding of how incentive should be calculated from billed PO/Invoice.

Detail:
Prepare and discuss:
- Current sales incentive calculation flow
- Source data used for billed PO/Invoice
- Main calculation rules
- Known pain points or manual steps
- Decisions needed before process mapping or development

Description:
The sales incentive requirement involves multiple stakeholders and may affect calculation logic. A discussion is needed before creating detailed Process Mapping, SPIKE, or Development todos.

Acceptance Criteria / Done Criteria:
- Meeting is completed with Finance and Sales Ops representatives.
- Key discussion points and decisions are documented.
- Follow-up todos are created for process mapping, SPIKE, or development if needed.

PIC / Owner:
Laras

Validation PIC:
- Requirement Confirmation: Finance PIC (to confirm)
- Final Validation / UAT: N/A
- Internal Review: Bayu

Open Questions / Assumptions:
- Need to confirm who from Finance can validate the calculation rule.
- Need to confirm whether Sales Ops or Finance owns final sign-off.

Tip:
Decide before the meeting what one thing you need out of it — for example, one agreed way to read billed PO/Invoice. Without that, the talk stays general.
Invite people from Finance and Sales Ops who can actually decide, not only people who report the numbers.
Send the current calculation steps ahead of time, so the hour is spent deciding and not explaining.
Anything left open leaves the meeting as a Follow-up todo with a name on it.
```

---

# Example 3 — Process unclear → Process Mapping todo

## Bad

```text
Mapping flow incentive Sales Direct & Programmatic
```

Why it fails:
- Says “mapping”, but not what artifact should come out of it.
- Actors, inputs, outputs, and decision points are not listed yet.
- No named validator yet — who reviews the finished map?
- No done criteria, so it is hard to say when this is finished.

## Coaching flow

The coach asks:
- What process needs to be mapped?
- Who understands the real process?
- What artifact should be produced?

User answers:
> Need to map the current flow for sales incentive calculation, including Sales Direct and Programmatic, before we build it.

This should be **Process Mapping**.

## Better

```text
Todo Name / Title:
[Process Mapping] Map Sales Incentive calculation flow

Feature / Epic:
Sales Incentive Calculation

Dependencies:
None

Updates/Changes Needed:
Map the current Sales Direct and Programmatic incentive calculation flow.

Detail:
Create a process map that covers:
- Actors involved: Sales, Finance, Sales Ops, System/Admin
- Inputs: billed PO/Invoice, sales data, incentive rules
- Main calculation steps
- Decision points and exception cases
- Output needed for calculation or reporting
- Current manual steps and pain points

Description:
The current incentive process needs to be understood before deciding what should be built or automated. Process clarity is required to avoid developing the wrong calculation logic.

Acceptance Criteria / Done Criteria:
- Current process flow is documented.
- Actors, inputs, outputs, and decision points are included.
- Flow is reviewed with the named Validation PIC.
- Gaps, unclear rules, and follow-up todos are documented.

PIC / Owner:
Laras

Validation PIC:
- Requirement Confirmation: [Finance PIC name] — Finance (to confirm)
- Final Validation / UAT: N/A
- Internal Review: Bayu

Open Questions / Assumptions:
- Need to confirm whether Sales Direct and Programmatic use the same calculation rule.
- Need to identify who owns final approval of the mapped flow.

Tip:
Start from the event that triggers the process — a PO gets billed — and follow it forward one step at a time. Do not start from the system.
Talk to the person who actually runs the incentive calculation each month, not only their manager. What happens is often not what the rule says.
Finish Sales Direct first, then do Programmatic. Mapping both at once usually produces a map nobody can read.
For each step, write down where it happens: system, spreadsheet, chat, or meeting. The handoffs between those are where the time goes.
```

---

# Example 4 — Technical/data uncertainty → SPIKE todo

## Bad

```text
Create join table for settlement
```

Why it fails:
- Starts at Development, before the approach is known.
- Source tables are still unclear.
- Join key is still unclear.
- Edge cases are not defined yet.
- No recommendation or review step — who decides the approach?

## Coaching flow

The coach asks:
- Do we already know the source tables and join key?
- Are there multiple possible approaches?
- Is the expected output already confirmed?

User answers:
> We need to check which table should be used and whether join should be by Order ID or campaign actual ID.

This is a **SPIKE**, not Development.

## Better

```text
Todo Name / Title:
[SPIKE] Review settlement join strategy

Feature / Epic:
Finance Settlement View

Dependencies:
None

Updates/Changes Needed:
Investigate the recommended join strategy for settlement data before development starts.

Detail:
Review and compare:
- Possible Revenue Share source table
- Possible Cost Ledger source table
- Candidate join keys: Order ID, campaign actual ID, or other agreed key
- Handling for missing Cost Ledger records
- Handling for multiple Cost Ledger records under one campaign or order
- Recommended output fields for settlement view

Description:
The settlement view cannot be developed safely until the source tables, join key, and edge case behavior are understood. The SPIKE should produce a recommendation for review.

Acceptance Criteria / Done Criteria:
- Source table options are reviewed.
- Recommended join key is documented.
- Edge cases and risks are listed.
- Recommendation is reviewed with the internal reviewer before Development todo is created.

PIC / Owner:
Dimas

Validation PIC:
- Requirement Confirmation: N/A
- Final Validation / UAT: N/A
- Internal Review: Bayu

Open Questions / Assumptions:
- Need confirmation whether unmatched Revenue Share rows should still appear.
- Need confirmation whether multiple Cost Ledger rows should be aggregated or shown separately.

Tip:
Write the question at the top — which key reliably joins Revenue Share to Cost Ledger — and stop once you can answer it. The output is a decision, not a built table.
Try each candidate key on real data and count the rows that do not match. Numbers end this argument faster than opinions.
Record why you ruled the other key out. That note is the part people come back to.
```

---

# Example 5 — Requirement clear enough → Development todo

## Bad

```text
Build settlement view
```

Why it fails:
- The intent is clear, but there is not enough here to execute.
- Does not say what is actually being built.
- Affected system and expected behavior are not stated.
- Acceptance criteria are not testable yet.
- No named validator yet — who confirms the output is correct?

## Coaching flow

The coach checks readiness:
- Requirement confirmed? Yes.
- Expected output clear? Yes.
- Source/logic known? Yes.
- Validation PIC named? Yes.
- Acceptance criteria testable? Yes.

Only then create **Development**.

## Better

```text
Todo Name / Title:
[Development] Build Finance settlement view

Feature / Epic:
Finance Settlement View

Dependencies:
None

Updates/Changes Needed:
Build a settlement view that combines agreed Revenue Share and Cost Ledger data for Finance review.

Detail:
Implement the settlement view based on the confirmed requirement:
- Use the agreed Revenue Share source table.
- Use the agreed Cost Ledger source table.
- Join data using the confirmed join key.
- Show the agreed output fields.
- Handle missing Cost Ledger records based on confirmed behavior.
- Make the view accessible to the agreed Finance users.

Description:
Finance needs one view to review settlement data without manually checking Revenue Share and Cost Ledger sources separately. Requirement and join logic have been confirmed, so development can proceed.

Acceptance Criteria / Done Criteria:
- Settlement view is available in the agreed system.
- View shows the agreed Revenue Share and Cost Ledger fields.
- Records are displayed based on the confirmed join logic.
- Missing Cost Ledger records are handled according to the agreed rule.
- Internal review is completed.
- Named Finance Validation PIC confirms sample output is correct.

PIC / Owner:
Dimas

Validation PIC:
- Requirement Confirmation: Sari — Finance
- Final Validation / UAT: Sari — Finance
- Internal Review: Bayu

Open Questions / Assumptions:
- N/A — key requirement and join logic confirmed in prior Confirmation/SPIKE todos.

Tip:
Re-read the confirmed output fields and the join key from the SPIKE before you build. If anything has changed since then, raise it instead of deciding it alone.
Agree with Sari early how she will check the result — which campaigns she will open and what she expects to see.
If you hit a case the confirmed rule does not cover, say so the same day. Do not invent a rule quietly inside the view.
```

---

# Example 6 — Output ready for checking → UAT / Validation todo

## Bad

```text
UAT settlement
```

Why it fails:
- Does not say what will be tested.
- No sample data or scenario to test against.
- No named validator yet — who runs the UAT?
- No expected result, so there is nothing to compare the output to.

## Coaching flow

The coach asks:
- What output is ready to validate?
- Who will validate it?
- What scenarios or sample records should be tested?

User answers:
> The settlement view is ready. Finance needs to test sample campaigns with matched Cost Ledger, missing Cost Ledger, and multiple Cost Ledger rows.

This should be **UAT / Validation**.

## Better

```text
Todo Name / Title:
[UAT] Validate settlement view with Finance

Feature / Epic:
Finance Settlement View

Dependencies:
None

Updates/Changes Needed:
Validate the implemented settlement view with Finance using agreed sample records.

Detail:
Prepare and run UAT covering:
- Campaign with matching Revenue Share and Cost Ledger data
- Revenue Share record without Cost Ledger data
- Campaign with multiple Cost Ledger rows
- Expected output fields and totals
- Access and usability for Finance user

Description:
The settlement view has been implemented and needs Finance validation before the Epic can be considered complete.

Acceptance Criteria / Done Criteria:
- UAT scenario and sample records are prepared.
- Sari from Finance validates the sample output.
- Feedback is documented.
- Issues are converted into Follow-up todos.
- Validation result is recorded as approved, approved with notes, or needs revision.

PIC / Owner:
Dimas

Validation PIC:
- Requirement Confirmation: N/A
- Final Validation / UAT: Sari — Finance
- Internal Review: Bayu

Open Questions / Assumptions:
- Need to confirm if Finance wants to add one more edge case for cancelled campaigns.

Tip:
Give Sari the expected numbers for each sample campaign before she opens the view. Nobody can validate against a standard they were never told.
Run the normal matched case first, then missing Cost Ledger and multiple Cost Ledger. Starting with the odd cases hides basic problems.
Close with one written verdict, not a chat thread. Turn every issue into a Follow-up with a named owner before you mark this done.
```

---

# Example 7 — Knowledge needs to be captured → Documentation todo

## Bad

```text
Document settlement
```

Why it fails:
- Audience is not defined — who will read this?
- Does not say what should be documented.
- No storage location agreed yet.
- No reviewer named — who confirms it is clear enough?

## Coaching flow

The coach asks:
- Who is the document for?
- What should it explain?
- Where should it be stored?
- Who reviews it?

User answers:
> Need internal documentation for the settlement logic and UAT notes, stored in Drive, reviewed by Bayu.

This should be **Documentation**.

## Better

```text
Todo Name / Title:
[Documentation] Document settlement logic and UAT notes

Feature / Epic:
Finance Settlement View

Dependencies:
None

Updates/Changes Needed:
Create documentation for the agreed settlement view logic and UAT result.

Detail:
Document:
- Purpose of the settlement view
- Source tables used
- Confirmed join key
- Important output fields
- Edge case handling
- UAT scenarios and result
- Known limitations or follow-up items

Description:
Settlement logic needs to be documented so the team can maintain the view and understand the decisions behind the implementation.

Acceptance Criteria / Done Criteria:
- Documentation is created.
- Documentation explains the agreed logic and UAT result clearly.
- Documentation is stored in the agreed Drive folder.
- Internal reviewer confirms the document is understandable and complete enough.

PIC / Owner:
Dimas

Validation PIC:
- Requirement Confirmation: N/A
- Final Validation / UAT: N/A
- Internal Review: Bayu

Open Questions / Assumptions:
- Need to confirm final Drive location.

Tip:
Write for someone who joins the team in six months and has never heard of Cost Ledger. Spell the terms out.
Settle the Drive folder before you write, and paste the link into this todo. A good document in the wrong folder is lost.
When the draft is ready, ask one person who was not part of the build to read it and explain the join rule back to you. Where they hesitate is what needs rewriting.
```

---

# Example 8 — Action item from review → Follow-up todo

## Bad

```text
Fix feedback from UAT
```

Why it fails:
- Too broad for one Follow-up.
- Does not identify which feedback — UAT raised more than one item.
- No owner or validator named yet.
- No clear done condition, so it is hard to say when it is fixed.

## Coaching flow

The coach asks:
- What specific feedback needs to be resolved?
- Who raised it?
- How do we know it is fixed?

User answers:
> Finance asked to rename the “Net Amount” column to “Net Settlement Amount” and add tooltip explanation.

This should be a **Follow-up** todo.

## Better

```text
Todo Name / Title:
[Follow-up] Revise settlement amount column label

Feature / Epic:
Finance Settlement View

Dependencies:
None

Updates/Changes Needed:
Apply Finance UAT feedback by renaming the settlement amount column and adding tooltip explanation.

Detail:
Update:
- Column label from "Net Amount" to "Net Settlement Amount"
- Tooltip/help text explaining how the amount is calculated
- Related documentation if needed

Description:
This follow-up comes from Finance UAT feedback. The change is small and specific, so it should be tracked as a Follow-up todo rather than reopening the whole Development todo.

Acceptance Criteria / Done Criteria:
- Column label is updated.
- Tooltip/help text is added.
- Finance PIC confirms the wording is clear.
- Related documentation is updated if impacted.

PIC / Owner:
Dimas

Validation PIC:
- Requirement Confirmation: N/A
- Final Validation / UAT: Sari — Finance
- Internal Review: N/A

Open Questions / Assumptions:
- Assumption: calculation logic does not change, only label/help text.

Tip:
Quote or link the exact Finance UAT comment here, so a later reader knows where the new wording came from.
Search for the old label everywhere before you close: the view, the documentation, and any report that reuses the field. Renaming in one place only is the usual mistake.
Tell Sari when the change is live. Doing the work is not the same as closing the loop.
```

---

# Example 9 — Epic in disguise → Todo List + Epic Brief + breakdown

## Bad

```text
[Development] Create new settlement view for Finance
```

Why it fails:
- The outcome is clear, but it is too broad for one todo.
- It bundles several phases: confirmation, SPIKE, development, UAT, documentation.
- Requirement and technical approach may not be clear yet — has either been confirmed?
- Progress and ownership are hard to track inside one item.

## Coaching flow

The coach asks:
- Is this multi-step?
- Does it need stakeholder confirmation?
- Does it need data/technical investigation?
- Will it span several days or IPMs?

If yes, create an **Epic / Todo List**, not one giant Development todo.

## Better — Todo List

```text
Todo List Name:
Billing Hub - Finance Settlement View
```

## Better — Todo List description

```text
[Epic Brief]

Objective:
Create a Finance Settlement View so Finance can review Revenue Share and Cost Ledger settlement data in one place.

Main PIC:
Dimas

Stakeholders:
- Sari — Finance
- Bayu — Internal Reviewer

Validation PIC:
- Requirement Confirmation: Sari — Finance (to confirm)
- Final UAT / Result Validation: Sari — Finance (to confirm)
- Internal Review: Bayu

Work Breakdown:
1. [Confirmation] Confirm Finance settlement output
2. [SPIKE] Review settlement join strategy
3. [Development] Build Finance settlement view
4. [UAT] Validate settlement view with Finance
5. [Documentation] Document settlement logic and UAT notes

Dependencies / Open Questions:
- Need to confirm expected output fields.
- Need to confirm join key and edge case handling.
- Need to confirm whether Sari is the final Validation PIC.
```

## Better — Initial todo items

```text
[Confirmation] Confirm Finance settlement output
[SPIKE] Review settlement join strategy
[Development] Build Finance settlement view
[UAT] Validate settlement view with Finance
[Documentation] Document settlement logic and UAT notes
```

Note:
The Development todo should remain in Backlog / Not Started until the Confirmation and SPIKE outputs are clear.

---

# Example 10 — Unknown Validation PIC → Confirmation first

## Bad

```text
[Development] Update onboarding approval flow
```

Why it fails:
- It reads as executable, but the validator is still unknown.
- With nobody named to confirm the requirement and the result, Development carries real risk.
- “HR team” is not enough as Validation PIC — which person?

## Coaching flow

The coach asks:
- Who can confirm the approval flow requirement?
- Who will sign off the final result?

User answers:
> Not sure yet, maybe HR Ops.

Unknown named validator → **Confirmation** first.

## Better

```text
Todo Name / Title:
[Confirmation] Confirm onboarding approval validator and scope

Feature / Epic:
Onboarding Approval Flow Revision

Dependencies:
None

Updates/Changes Needed:
Confirm the named stakeholder PIC and scope for the onboarding approval flow revision.

Detail:
Confirm:
- Who owns the requirement from HR Ops
- Who validates the final flow
- Which approval steps are included
- Whether this affects only onboarding or also employee data update flow

Description:
Development should not start because the Validation PIC and exact scope are not confirmed yet.

Acceptance Criteria / Done Criteria:
- Named HR Ops Validation PIC is confirmed.
- Approval flow scope is documented.
- Follow-up Process Mapping or Development todo is created based on confirmation.

PIC / Owner:
Putri

Validation PIC:
- Requirement Confirmation: HR Ops PIC (to confirm)
- Final Validation / UAT: N/A
- Internal Review: Bayu

Open Questions / Assumptions:
- Need to confirm whether approval flow change impacts only onboarding.

Tip:
Ask for one person's name, not a team. "HR Ops" cannot approve anything; a person can.
Put a date on the answer. An open request for a name can sit for weeks and quietly block the whole epic.
Also ask who decides when HR Ops and a requesting team disagree. That single answer prevents a lot of rework later.
```

---

# Example 11 — IPM update comment

## Bad

```text
update minggu ini: masih progress, ada blocker finance belum reply
```

Why it fails:
- Says progress, but not what actually moved.
- No status movement — which todos changed, and from what to what?
- Blocker owner is vague — who exactly at Finance must reply?
- No decision or ask, so the reader cannot help.
- No next step before the next IPM.

## Coaching flow

The coach asks:
- What changed since the last update?
- Which todos moved status?
- Who exactly needs to respond?
- What help or decision is needed?
- What is the next step before next IPM?

## Better

```text
[IPM Update - 13 July 2026]

Progress:
- Process mapping completed and reviewed internally.
- Draft settlement output columns prepared for Finance confirmation.
- Source table options identified for the upcoming SPIKE.

Status Movement:
- [Process Mapping] Map current settlement flow: In Progress → In Review
- [Confirmation] Confirm Finance settlement output: Not Started → In Progress

Blocker / Open Question:
- Waiting for Sari from Finance to confirm the expected recap columns and monthly cut-off rule.

Decision / Ask:
- Need mentor input on whether the SPIKE should compare order-level and campaign-level mapping.

Next Step:
- Follow up with Sari for confirmation.
- Start SPIKE once the expected output is confirmed.

Risk / Notes:
- Development may be delayed if Finance confirmation is not received this week.
```

Note:
If a section has no update, write `None` — do not delete the section.

---

# Example 12 — Knowledge doc vs pasted Basecamp conflict

## Context

Knowledge file says:
> Final UAT PIC: Tono — Finance

Pasted Basecamp Epic Brief says:
> Final UAT / Result Validation: Sari — Finance

## Correct coach behavior

Basecamp content wins for current scope, status, PIC, Validation PIC, and recent decisions. Knowledge files may be outdated.

The coach should say:
> I found Tono in the Knowledge doc, but the pasted Basecamp Epic Brief says Sari is the current Final UAT PIC. I will use Sari as the operating source of truth and treat Tono as outdated unless you confirm otherwise.

## Better usage in todo

```text
Validation PIC:
- Requirement Confirmation: Sari — Finance
- Final Validation / UAT: Sari — Finance
- Internal Review: Bayu
```

## Open Questions / Assumptions

```text
- Knowledge doc mentions Tono as prior UAT PIC; Basecamp currently says Sari. Using Sari unless user confirms otherwise.
```

---

# Example 13 — Development request with hidden process uncertainty → Process Mapping first

## Bad

```text
[Development] Automate Content Series approval flow
```

Why it fails:
- Assumes the flow is already understood — is it?
- Approval actors and decision points may still be unclear.
- No mapped current or target flow to build against.
- Risk: Development automates the wrong process.

## Coaching flow

The coach asks:
- Is the current approval flow already mapped?
- Who approves at each step?
- Are there exceptions?
- Has stakeholder confirmed the target flow?

User answers:
> Not yet. We only know the current flow is messy and different teams have different assumptions.

This should be **Process Mapping**, not Development.

## Better

```text
Todo Name / Title:
[Process Mapping] Map Content Series approval flow

Feature / Epic:
Content Series Approval Flow

Dependencies:
None

Updates/Changes Needed:
Map the current Content Series approval flow before deciding what should be automated.

Detail:
Document:
- Current approval actors
- Inputs and outputs at each approval step
- Decision points
- Exception cases
- Pain points and manual coordination
- Draft target flow, if stakeholder can already define it

Description:
The approval process is not clear enough for Development. Process mapping is needed to align stakeholders and avoid automating the wrong workflow.

Acceptance Criteria / Done Criteria:
- Current approval flow is documented.
- Actors, inputs, outputs, and decision points are included.
- Flow is reviewed with the named business Validation PIC.
- Follow-up Confirmation, SPIKE, or Development todos are created as needed.

PIC / Owner:
[User's name]

Validation PIC:
- Requirement Confirmation: [Business PIC name] (to confirm)
- Final Validation / UAT: N/A
- Internal Review: Bayu

Open Questions / Assumptions:
- Need to confirm who owns the final approval process.
- Need to identify exception cases.

Tip:
Agree the start point and end point first — for example, from script submission to final green-light. Without that, the map keeps growing.
Teams already believe different things here. Map each team's version separately, then compare. The gaps between the versions are the real finding.
Record who can stop or send back the work at each stage. In a lifecycle this long, the veto points matter more than the steps.
Leave rare exceptions for a second pass. A clear main flow helps stakeholders more than a complete but tangled one.
```

---

# Example 14 — Too much detail in title → concise title + detail in body

## Bad

```text
[Development] Build AppSheet view to show Revenue Share and Cost Ledger data joined by campaign_actual_id with missing Cost Ledger handling and Finance validation
```

Why it fails:
- The detail is good, but the title is too long.
- Hard to scan in a Basecamp list.
- The title carries detail that belongs in the todo body.

## Better title

```text
[Development] Build settlement view
```

## Better body excerpt

```text
Updates/Changes Needed:
Build a settlement view that combines Revenue Share and Cost Ledger data for Finance review.

Detail:
- Join Revenue Share and Cost Ledger using confirmed campaign_actual_id.
- Keep Revenue Share records visible even when Cost Ledger data is missing.
- Show agreed output fields for Finance settlement review.
- Prepare sample records for validation.

Validation PIC:
- Final Validation / UAT: Sari — Finance
- Internal Review: Bayu
```

Note:
A short title is correct — Example 5's bad version failed because the todo had *only* a title and no body, not because the title was short.

Rule:
Todo title should be short and scannable. Put implementation detail in `Detail`, not in the title.

---

# Example 15 — Status in title → status belongs in Todo Group

## Bad

```text
[Process Mapping] Map incentive flow — In Review
```

Why it fails:
- Status is duplicated in the title.
- It will drift from the Todo Group the moment the status changes — which one is then correct?
- The Basecamp Todo Group is the status source of truth.

## Better

```text
Todo title:
[Process Mapping] Map incentive flow

Todo Group:
In Review
```

Rule:
Status lives in the Todo Group, never in the todo title.

---

# Example 16 — Assignee and due date in text → use native Basecamp fields

## Bad

```text
Todo Name / Title:
[UAT] Validate onboarding flow with HR

PIC / Owner:
Putri

Detail:
Assigned to Putri. Due Friday. Validate with HR.
```

Why it fails:
- Assignee and due date are duplicated in the text.
- They will drift from the native Basecamp assignee and due date fields.
- The validation details are still thin — what exactly will be checked?

## Better

```text
Todo Name / Title:
[UAT] Validate onboarding flow with HR

Feature / Epic:
Onboarding Flow Revision

Dependencies:
None

Updates/Changes Needed:
Validate the revised onboarding flow with HR Ops.

Detail:
Run validation with HR Ops covering:
- New approval step
- Notification behavior
- Error handling for missing employee data
- Expected user flow from request submission to completion

Description:
The onboarding flow revision is ready for stakeholder validation before closing the Epic.

Acceptance Criteria / Done Criteria:
- HR Ops validates the revised flow.
- Feedback is documented.
- Issues are converted into Follow-up todos.
- Validation result is recorded as approved, approved with notes, or needs revision.

PIC / Owner:
Putri

Validation PIC:
- Requirement Confirmation: N/A
- Final Validation / UAT: [HR Ops PIC name] (to confirm)
- Internal Review: Bayu

Open Questions / Assumptions:
- Need to confirm HR Ops PIC name before UAT.

Tip:
Do not start the session until you have the HR Ops person's name. Testing with "whoever is free" produces feedback that nobody owns.
Walk one real onboarding request all the way from submission to completion first, then try the missing-data case.
Ask the validator to write approved, approved with notes, or needs revision. "Looks fine" is a comment, not a verdict.
```

After creating:
- Set assignee natively in Basecamp.
- Set due date natively in Basecamp.

---

# Example 17 — Project kickoff → Project Starter Context

## Bad

```text
Help me create todos for the HR onboarding project
```

(no project context exists anywhere — no Project Description, no Epic Brief)

Why it fails:
- No problem statement or target output yet — what should the todos point at?
- No PIC and no Validation PIC named.
- Any todo written now would inherit that vagueness.

## Coaching flow

The coach does not start writing todos. It asks the starter questions (at most 7): project name? problem? expected output? main PIC? named Validation PIC if known? system/process/data involved? anything unclear, out of scope, or risky?

User answers partially:
> HR Process Improvement. Onboarding takes too long and approvals get lost. We want a revised flow. Putri drives it. Not sure yet who validates from HR Ops. Involves the onboarding form and employee master data.

Unknowns do not block — they go under Open Questions / Risks.

## Better

```text
[Project Starter Context]

Project / Initiative:
HR Process Improvement

Problem / Background:
Onboarding takes too long and approval requests get lost between HR Ops and requesting teams.

Target Output / Success:
A revised onboarding flow with clear approval steps and less manual follow-up.

People:
- Main PIC / Owner: Putri
- Validation PIC: HR Ops (to confirm)
- Key Stakeholders: HR Ops, requesting team leads

Scope:
- In Scope: onboarding request and approval flow
- Out of Scope: payroll, offboarding

System / Process / Data Involved:
- Onboarding form
- Employee master data
- Approval notification flow

Open Questions / Risks:
- Named HR Ops Validation PIC not confirmed yet.
- Unclear whether the employee data update flow is affected.

Last Updated:
14 July 2026
```

After creating:
- Place it in the Basecamp Project Description.
- First todo: `[Confirmation] Confirm onboarding approval validator and scope` (see Example 10).

---

# Example 18 — Review Mode response structure

## Input

User asks: "review this todo"

```text
[Development] Update incentive report
Description: Update the report per Finance request.
PIC: Dimas
```

## Correct coach response shape

```text
Verdict: Should become Confirmation

Key Issues:
- Expected output unclear ("update the report" — which columns, which logic?).
- "Per Finance request" — the request itself is not documented or confirmed.
- No named Validation PIC.
- Acceptance Criteria missing / not testable.

Suggested Improved Version:
[Confirmation] Confirm incentive report changes with Finance
- Updates/Changes Needed: confirm which report changes Finance expects and who validates them.
- Acceptance Criteria: Finance confirms the change list; named Validation PIC confirmed; follow-up Development todo created.
- Validation PIC — Requirement Confirmation: [Finance PIC name] (to confirm)

Questions to Confirm:
1. What exactly did Finance ask to change?
2. Who from Finance can confirm the changes and later validate the result?
3. Is there a deadline driving this?
```

Rule:
Review Mode always returns: **Verdict → Key Issues → Suggested Improved Version → Questions to Confirm**. Verdict options: Ready / Needs Revision / Should become Confirmation, Meeting / Discussion, Process Mapping, SPIKE, or Epic.

---

# Example 19 — Bahasa Indonesia interaction style

## Input

```text
tolong buatin todo: benerin laporan incentive buat finance
```

## Correct coach behavior

Reply in Bahasa Indonesia (the user's language), keep the standard terms in English, and do not polish the vague request:

```text
Sebelum saya buatkan todo-nya, requirement-nya masih belum jelas:

1. "Benerin" itu maksudnya apa — kolom yang salah, logika perhitungan, atau format laporannya?
2. Siapa dari Finance yang bisa confirm perubahannya dan jadi Validation PIC?

Kalau belum ada yang bisa confirm, saya sarankan mulai dari todo Confirmation dulu, bukan Development — supaya Acceptance Criteria-nya bisa dites dan jelas siapa yang validasi.
```

Rule:
Match the user's language; keep these terms in English: Todo, Epic, SPIKE, UAT, Validation PIC, Acceptance Criteria, Done Criteria, IPM, Basecamp.

---

# Example 20 — Review passes → Ready verdict

## Input

User asks: "review this todo" and pastes the Development todo from Example 5 (`[Development] Build Finance settlement view`), after the Confirmation and SPIKE todos were completed.

## Correct coach response shape

```text
Verdict: Ready

Why:
- Requirement and join logic were confirmed in prior Confirmation/SPIKE todos.
- Expected output and affected system are clear.
- Acceptance Criteria are specific and testable.
- Validation PIC is a named person (Sari — Finance).
- Open questions are resolved (N/A with reason).

Minor Notes (optional, not blockers):
- Consider listing 2–3 sample records now to speed up UAT preparation later.

Questions to Confirm:
- None.
```

Rule:
When a todo passes the Readiness Rule, say **Ready** and stop coaching. Do not invent issues to appear thorough. Optional suggestions go under Minor Notes and must be clearly marked as non-blocking.

---

# Example 21 — Mapped process needs evaluation → Process Assessment

## Context

Process mapping for a content-planning process is complete and validated with stakeholders. The team now needs to judge what is broken and what could be improved — before proposing any tool or redesign.

## Better

```text
Todo Name / Title:
[Process Assessment] Compile content-planning assessment findings

Feature / Epic:
Content Planning Current-State Mapping

Dependencies:
None

Updates/Changes Needed:
Compile the current-state assessment sheet from the validated maps, SIPOC, and interview findings.

Detail:
Cover: what is working; what is not working; bottlenecks; duplicate work and reporting; manual workarounds; risks and control gaps; unclear ownership or approvals; missing SOPs or governance; data quality issues; tracker and system issues; improvement opportunities; automation candidates and quick wins; downstream impact.

Description:
Mapping and validation are complete. Findings must be consolidated into one solution-neutral assessment before any future-state design starts.

Acceptance Criteria / Done Criteria:
- Assessment sheet covers all agreed categories.
- Every finding is supported by evidence from interviews, documents, or maps.
- Recommendations stay solution-neutral unless evidence clearly supports a specific tool.
- Assessment is reviewed with the Requirement Confirmation PIC before internal review.

PIC / Owner:
Laras

Validation PIC:
- Requirement Confirmation: Tono — Business PIC
- Final Validation / UAT: Tono — Business PIC (via Epic final validation)
- Internal Review: Bayu

Open Questions / Assumptions:
- Depends on completed exception mapping and validated SIPOC.

Tip:
Assess the content-planning process, not the people running it. Write "approval waits for the weekly planning meeting", not "the team is slow".
Mark clearly which findings you saw yourself and which someone told you in an interview. Tono will ask.
Put rough numbers on the problems where you can — "about two days of waiting" lands better than "slow".
List what already works too. An assessment that is only complaints is easy for stakeholders to dismiss.
```

Rule:
Process Assessment comes after Process Mapping is validated, and its output stays solution-neutral. See the Routing Boundaries section for the Mapping vs Assessment contrast.

---

# Example 22 — Consolidated deliverable review → Internal Review

## Bad

```text
[Internal Review] Review process map
[Internal Review] Review SIPOC
[Internal Review] Review assessment sheet
```

Why it fails:
- One Internal Review todo per deliverable — this doubles the todo count.
- A single-deliverable review fits better inside that todo's Done Criteria, with the Internal Review Validation PIC named there.

## Better

```text
Todo Name / Title:
[Internal Review] Review content-planning deliverables internally

Feature / Epic:
Content Planning Current-State Mapping

Dependencies:
None

Updates/Changes Needed:
One consolidated quality review of all Epic deliverables before final stakeholder validation.

Detail:
Check across the maps, SIPOC, and assessment sheet: findings supported by evidence; assumptions clearly labeled; consistent terminology; roles and handoffs understandable; open questions have owners; recommendations do not prematurely prescribe a tool.

Description:
All deliverables are drafted. One internal quality pass is needed before the final validation session.

Acceptance Criteria / Done Criteria:
- All deliverables reviewed in one pass.
- Findings are fixed or converted into Follow-up todos.
- Reviewer confirms the package is ready for final stakeholder validation.

PIC / Owner:
Laras

Validation PIC:
- Requirement Confirmation: N/A
- Final Validation / UAT: N/A (final validation is its own [UAT] todo)
- Internal Review: Bayu

Open Questions / Assumptions:
- None.

Tip:
Open the maps, the SIPOC, and the assessment sheet side by side. You are looking for places where they disagree — different step names, different owners, different numbers.
Fix small wording problems yourself while you read. Anything that needs real new work becomes a Follow-up, so this review can close.
Set a time limit before you start. Without one, a consolidated review turns into a second project.
```

Rule:
Internal Review todos exist only as a consolidated pass over several deliverables, usually near the end of an Epic.

---

# Example 23 — Discovery epic → Epic Brief with optional sections

## Context

The user asks for a new Epic: understand and assess the content-planning process, end to end. This is discovery/process work: several phases, several IPMs, no system build yet.

## Bad (coach behavior)

The coach creates a slim Epic Brief (Objective, Main PIC, Stakeholders, Validation PIC, Work Breakdown, Dependencies) and stops. It never asks about deliverables, risks, or completion criteria. Weeks later the team argues about what "done" means for the epic.

Why it fails:
- For discovery/process epics, Expected Deliverables and Completion Criteria are what IPM tracking hangs on.
- The optional sections exist for exactly this case — they were just never offered.

## Coaching flow

For a discovery/process epic, the coach asks three extra questions:
- What deliverables should exist at the end? (maps, SIPOC, assessment sheet, ...)
- What are the main risks?
- What conditions make this epic complete?

The sections stay optional — the user decides. A small, clear build epic can keep the slim brief.

## Better

```text
[Epic Brief]

Objective:
Understand and assess the current content-planning process before proposing any improvement.

Main PIC:
Laras

Stakeholders:
- Tono — Business PIC
- Bayu — Internal Reviewer

Validation PIC:
- Requirement Confirmation: Tono — Business PIC
- Final UAT / Result Validation: Tono — Business PIC
- Internal Review: Bayu

Work Breakdown:
1. [Process Mapping] Map content-planning flow
2. [Confirmation] Confirm process boundary with Tono
3. [Process Assessment] Compile content-planning assessment findings
4. [Internal Review] Review content-planning deliverables internally
5. [UAT] Validate findings with Tono

Dependencies / Open Questions:
- Interview schedule depends on team availability.

Expected Deliverables:
1. Current-state process map
2. SIPOC
3. Assessment sheet (solution-neutral)

Risks:
- Key people may not be available for interviews.
- Process may differ per content type.

Completion Criteria:
- All deliverables reviewed internally and validated by Tono.
- Open questions have named owners or follow-up todos.
```

Rule:
For discovery/process epics, the coach offers the optional sections (Process Boundary, Expected Deliverables, Risks, Completion Criteria, Recurring Governance). They stay optional — never force them on a small, clear epic.

---

# Routing Boundaries — Quick Contrasts

Use these when two todo types feel equally plausible.

## Confirmation vs Meeting / Discussion

- "Does Finance want the recap monthly or weekly?" → one decision, one named stakeholder → **Confirmation**.
- "Finance and Sales Ops disagree on how incentive should be calculated." → multiple stakeholders, no agreed direction yet → **Meeting / Discussion**.
- Rule of thumb: Confirmation = the answer already exists, someone just needs to confirm it. Meeting = the answer still has to be built together.

## SPIKE vs Process Mapping

- "We don't know which source table or join key to use." → technical/data unknown → **SPIKE**.
- "We don't know who approves what, in which order." → process/actor unknown → **Process Mapping**.
- Both unknown → **Process Mapping first** (understand the process before choosing the technical approach), then SPIKE.

## Follow-up vs new Development

- Small, specific change from feedback on delivered work (rename column, add tooltip) → **Follow-up**.
- Feedback that changes the logic or scope of the original requirement → new **Development** — or **Confirmation** first if the new expectation is unclear.
- If a Follow-up turns out bigger than expected, convert it into its own todo instead of stretching it.

## Process Mapping vs Process Assessment

- "We do not know how the process actually works." → **Process Mapping**.
- "The process is mapped and validated — now what is broken, risky, or improvable?" → **Process Assessment**.
- Normal sequence for improvement work: Process Mapping → validate with stakeholders → Process Assessment → then Confirmation / SPIKE / Development for the chosen improvements.
- Assessment output stays solution-neutral unless evidence clearly supports a specific tool.

## Internal Review todo vs Done Criteria review

- One deliverable needs an internal check → not a separate todo. Put it in that todo's Done Criteria, with the Internal Review Validation PIC.
- Several deliverables (process maps, SIPOC, assessment sheet) need one consolidated quality pass before final stakeholder validation → one **Internal Review** todo, usually near the end of the Epic.
- Never create one Internal Review todo per todo.
