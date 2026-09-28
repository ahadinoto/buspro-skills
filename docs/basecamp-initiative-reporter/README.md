# progress-reporter

Draft progress updates from live Basecamp evidence.

```bash
npx skills add ahadinoto/buspro-skills --skill progress-reporter -g
```

See the [collection guide](../../README.md) for setup, dependencies, updates,
and supported hosts. This documentation folder keeps its historical name; the
installable identifier is `progress-reporter`.

[Quality decisions](quality-system-tracker.md) record the reasoning behind
the instructions. Historical design records describe their original version.

## Using it

Name the skill in your first message — most agents will not pick it up on their
own:

> Use the **progress-reporter** skill. Draft my stand-up for
> [Acme] Process Improvement.

> Use the progress-reporter skill. Show and tell for today.

It will state the project and window it locked onto before reporting:

> Reporting on **[Acme] Process Improvement** (`12345678`), Wednesday 16 September.

If that is the wrong project, say so — it should never pick silently between
similar names.

Overriding the window works in plain language: *"show and tell for this whole
week"*, *"stand-up covering since Friday"*.

### Getting the most out of show-and-tell

Share your morning stand-up when you run the afternoon show-and-tell. It can then
report **planned versus actual**, which is the most useful line in the report.
Without it, you get what moved — still useful, just less pointed.

---

## What to expect

**A stand-up leads with today's plan**, not a recap of yesterday. Yesterday only
appears when it explains a blocker. That is deliberate: at 9am you have not done
today's work yet, so a report built from today's activity would be empty every
morning.

**An empty report is a real answer.** "No movement on this initiative today" is
what the skill will say when nothing moved. It will not pad the message with
todos that were merely created — creating a todo is queuing work, not doing it.

**Basecamp claims link to evidence.** Work supplied by the user is labelled
user-reported when no Basecamp trace exists. The skill must not invent progress.

**Suggestions stay suggestions.** If one should become a todo, the skill hands
off to `todo-planner` rather than writing it — a todo drafted here would
skip the readiness gate.

---

## Known limits

Stated up front so you do not plan around things it cannot see:

- **Other people's activity on your items.** The scan is your own activity feed,
  so a teammate commenting on your todo will not appear. Blockers are found from
  your open assignments and recent comments on them.
- **Why something stalled.** The timeline shows the absence of events, not
  reasons. "No movement since Thursday" is reportable; "blocked on Finance" is
  not, unless a comment says so.
- **Work done outside Basecamp.** Plenty of real work never becomes an event. If
  you did something the timeline cannot see, tell the skill — it will include it
  and note there is no Basecamp trace yet.
- **No browser-chat version.** This skill needs live data, so there is no Gemini
  Gem or Custom GPT bundle for it.

---

## Found a problem? Report it

Tell Adiwijaya — chat, WhatsApp, verbally, whatever is easiest.

Two things worth reporting specifically, because they are the failures that
matter most here:

1. **A line you cannot verify.** Basecamp claims should link to real events;
   user-reported work must be labelled. Invented progress is a defect.
2. **A wrong day.** Basecamp returns UTC. In WIB, activity before 7am
   belongs to the previous UTC date, so filtering must use the local day boundary.
   Report an item assigned to the wrong local day.
