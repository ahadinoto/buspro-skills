# Message formats

Two rituals, every working day, on one initiative:

| | When | Answers |
|---|---|---|
| **Stand-up** | Morning | What I plan to do today, what is blocking me |
| **Show and tell** | Afternoon | What actually moved today, what is next |

Both are written in the user's voice, about their own work, ready to paste or
read aloud. No preamble, no "Here is your stand-up draft" — start at the first
line of the message itself.

Keep them short. A stand-up that takes ninety seconds to read is not a stand-up.

---

## 1. Stand-up (message board)

```text
*[Initiative name]* — [day, date]

Today
- [Item] — [what I'm actually doing to it] ([epic])
- [Item] — [what I'm actually doing to it] ([epic])

Blocked / need help
- [Item]: [what is needed, from whom]
```

Rules:

- **Two to four items under Today.** A plan listing nine things is not a plan.
  If the user has more open work than that, lead with due-today and overdue, and
  say how many others are open.
- **Say what you will do to the item, not just its title.** "Settlement view —
  finishing the join logic" beats "Settlement view".
- **Name the epic** in parentheses so the plan reads as initiative work.
- **Blockers name a person and an ask.** "Waiting on Finance" is not actionable;
  "needs Tono to confirm the settlement amount" is.
- **Drop the section if it is empty.** No blockers means no Blocked section, not
  "Blocked: none".
- One optional line of continuity above Today, only when it sets up the plan:
  `Finished the SLA mapping yesterday.`

### Worked example

```text
*[Acme] Process Improvement* — Wednesday, 16 September

Today
- Intake Form — reviewing the invitation and confirming scope (Ad hoc)
- Settlement join strategy — writing up the SPIKE answer (Finance Settlement)

Blocked / need help
- Settlement view: needs Tono to confirm whether unmatched rows still appear —
  asked in a comment Monday, no reply yet
```

---

## 2. Show and tell (message board)

```text
*[Initiative name]* — [day, date]

Moved today
- [What changed] → [link]
- [What changed] → [link]

Still open
- [Item from this morning's plan that did not move]

Next
- [Suggestion] (suggestion)
```

Rules:

- **Moved today is evidence.** Every line traces to a real event and carries its
  `app_url`. If it cannot be linked, it does not belong in this section.
- **Group by what a person recognises** — completed, decided, documented,
  advanced — not by raw `kind`.
- **Created ≠ done.** A todo created today is queued work. Put it under Next or
  a short "picked up" line, never under Moved today.
- **Mark suggestions as suggestions.** Two or three at most. This is a report,
  not a plan.
- **Empty is a valid report.** "No movement today — spent the day in the
  all-day onboarding session" is honest and useful. Never pad.

### With the morning plan available

If the user shares their stand-up, lead with the comparison — it is the most
useful line in the report:

```text
*[Acme] Process Improvement* — Wednesday, 16 September

Planned 2, moved 1.

Moved today
- Confirmed Intake Form scope, closed the review todo → [link]

Still open
- Settlement join strategy — no movement, still blocked on Tono's confirmation

Next
- Turn the Intake Form scope confirmation into a Development todo (suggestion)
```

Do not produce the "Planned N, moved M" line without the actual stand-up. Guessing
what was planned makes the whole report untrustworthy.

---

---

## 3. Progress comment (one todo)

Added 2026-09-16. A dated comment on an **individual todo**, recording what
happened to that todo on a given day.

This is the only defined use of comments on a todo item. Comments on the **Todo
List** remain the IPM timeline (section 4 below) — the two never mix. An IPM update
summarises an epic for a meeting; a progress comment records one todo's day.

**Written to be read later by a person *and* by an AI agent.** That second
audience is the reason for the fixed structure: an agent reading this todo in
three weeks has no memory of the conversation that produced it and cannot ask a
follow-up question. Anything implied is lost.

Unlike todo bodies, **comment bodies accept Markdown** and are converted to HTML
(see `scan-recipes.md`), so the labels below render as written.

```text
[Progress Update - DD Month YYYY]

**Done:**
- [What actually changed today, stated as a completed fact]

**Current state:**
[Where the todo stands now, in one or two sentences]

**Status:** [Backlog | Not Started | In Progress | In Review | On Hold | Completed]

**Blocked / waiting on:**
- [What is needed] — [Named person], asked [DD Month YYYY]

**Open questions / assumptions:**
- [Question, or an assumption being worked under]

**Next step:**
- [Next concrete action] — [Named owner]

**References:**
- [Title](https://…)
```

Write `None` for any section with nothing to record. Do not delete sections —
a fixed shape is what makes the comment parseable.

### Rules that make it agent-readable

These are not style preferences. Each one closes a way a later reader gets it
wrong:

- **Absolute dates only.** `16 September 2026`, never "today", "yesterday", or
  "last week". The comment is read on an unknown future date.
- **Named people, never pronouns or roles alone.** "Waiting on Tono" is
  resolvable; "waiting on Finance" or "he hasn't replied" is not.
- **Status uses the exact Todo Group vocabulary** listed above. A free-text
  status like "almost done" cannot be reconciled with the board.
- **Separate fact from assumption.** `Done` is what demonstrably happened.
  Anything believed-but-unconfirmed belongs under Open questions / assumptions.
  A later agent that cannot tell these apart will report assumptions as progress.
- **No implied context.** The comment must stand alone. "Fixed the thing we
  discussed" is unreadable to anyone who was not in the conversation.
- **Links are real URLs**, with the title as link text.
- **One comment per day per todo.** Amend the day's comment rather than posting
  a second one; a single dated entry per day keeps the thread ordered and
  unambiguous.

### Do not invent progress

Write only what the user reported. If their account is vague about whether
something finished, **ask** — do not resolve it into `Done`.

This is the same discipline as the readiness gate: a tidy progress comment
covering work that did not happen is worse than a rough one, because it is
read later as fact by both people and agents.

---

## 4. IPM update

A new dated comment on the Todo List for every IPM while the Epic is active. The
Epic Brief — in the list description — stays stable as the source of truth;
progress goes here. Comments hold nothing but the IPM timeline.

The **scan supplies Status Movement** — 7 days of `todo_completed`,
`todo_created` and card events give the from → to transitions without the user
reconstructing them from memory. Ask the user for what the scan cannot see:
decisions taken outside Basecamp, blockers and who must respond, help needed,
next steps before the next IPM, and timeline or scope risk. Confirm the date.

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

---

## 5. Combined weekly update (message board)

Once a week, across **every monitored project** in the registry. Posted to the
reporting destination, alongside the daily reports.

This is not a replacement for the per-epic IPM update — both exist, and they
answer different questions. The per-epic comment tells that epic's readers what
happened to *that epic*. This tells your stakeholders what happened to *your
week*, across everything.

**Build it from the per-epic IPM updates where they exist.** If you wrote them
this week, they are already the evidence — synthesise rather than re-deriving
everything from the timeline, and the two stay consistent by construction. Scan
directly only for projects with no IPM update this week.

```text
Weekly update — DD Month YYYY

This week
- [Project]: [what moved, one or two lines] → [link]
- [Project]: [what moved] → [link]

Still open
- [Project]: [what did not move, and why if known]

Blocked / need a decision
- [What is needed] — [Named person]

Next week
- [The two or three things that actually matter]
```

Rules:

- **Group by project**, in the order they matter this week — not registry order,
  and not alphabetically.
- **A project with no activity is omitted**, not listed as "no activity". Five
  empty lines bury the two that matter. Say "no movement on the other three"
  once at the end if it is worth saying at all.
- **Next week is a commitment, not a wish list.** Two or three items.
- Same evidence rule as every other report: if a line cannot be traced to an
  event, a per-epic update, or something the user told you, cut it.

---

## Message board titles

Stand-up and show-and-tell are posted to the project message board, so they need
a title. Keep it mechanical and greppable — people and agents both scan these:

```text
Stand-up — 16 September 2026 — Adiwijaya
Show and tell — 16 September 2026 — Adiwijaya
Weekly update — week ending 19 September 2026 — Adiwijaya
```

Absolute date, and the person's name, because a board carries everyone's. Do not
put the summary in the title; it belongs in the body.

Post daily reports with `--no-subscribe`. A notification to the whole project
every morning trains people to ignore the board.

---

## Todo Group vocabulary

Progress comments state status using the exact group names:

Backlog · Not Started · In Progress · In Review · On Hold · Completed

Restated here so this skill stands alone when installed — you will not have the
coach's files on disk. The canonical definition lives in the separate
`basecamp-todo-coach` skill; if the two ever disagree, the coach wins. Do not
try to open it from here.

---

## Turning a suggestion into a todo

Suggestions stay suggestions here. If the user wants one to become a real todo,
hand off to **`basecamp-todo-coach`** — it owns the readiness gate and the
locked 11-field format.

Say so plainly rather than writing the todo yourself:

> Want me to turn that into a todo? I'll run it through the todo coach so it
> gets routed and formatted properly.

A todo drafted here would skip the gate, which is exactly the unowned,
AI-polished work item the quality system exists to prevent.

---

## Language

Match the user. If they write in Bahasa Indonesia, the draft is in Bahasa
Indonesia — including the section headers (`Hari ini`, `Blocked / butuh bantuan`,
`Yang bergerak hari ini`). Keep Basecamp's own nouns (todo, epic, Basecamp) and
the todo-type prefixes (`[Confirmation]`, `[SPIKE]`) untranslated, since those
are the team's shared vocabulary.
