# Basecamp Initiative Reporter

*A skill in the [`buspro-skills`](../../README.md) repo.*

Drafts the two daily messages for one Basecamp initiative, from what actually
happened in Basecamp:

| Report | When | Answers | Posted to |
|---|---|---|---|
| **Stand-up** | Morning | What I plan to work on today, what is blocking me | Message board |
| **Show and tell** | Afternoon | What actually moved today, what is next | Message board |
| **Progress comment** | Any time | What happened to one todo today | That todo |
| **IPM update** | Weekly | What moved on one epic in the past 7 days | That todo list |
| **Combined weekly** | Weekly | What moved across all your projects | Message board |

All four are about **your own work** on **one Basecamp project**, and all four
follow the same pipeline:

```text
you give context → it scans Basecamp → merges both → drafts → you confirm → it posts
```

Neither half is enough on its own. The scan knows what changed and when; only
you know the decision taken in a meeting, or why something stalled. It never
posts without your say-so.

The companion to [`basecamp-todo-coach`](../basecamp-todo-coach/README.md): the
coach helps you *write* good work items, this reports on the ones that exist.

---

## Install

```bash
npx skills add ahadinoto/buspro-skills --skill basecamp-initiative-reporter -g
```

Add `-a <agent>` to target one (e.g. `-a cline`, `-a claude-code`).

### It needs the Basecamp CLI

Unlike the todo coach, this skill **cannot work from pasted content** — it has to
read your live activity timeline. Without the CLI it will tell you so and stop,
rather than inventing a plausible stand-up.

```bash
curl -fsSL https://basecamp.com/install-cli | bash
```

```bash
basecamp auth login
```

Read-only access is enough. Check with `basecamp auth status`.

---

## First run: the project registry

The first time you use either skill, it will offer to create a registry at:

```text
~/.config/buspro-skills/projects.md
```

It lists the Basecamp projects you actually work in, and it is how the skill
knows which project you mean. Without it, the agent has to guess — which was the
first thing mentees reported going wrong.

It will show you the file before writing it. You'll be asked:

1. **Which projects to monitor** — it lists what you can see in Basecamp; pick
   the ones you actively work on, not all of them.
2. **A local folder for each** (optional) — see below. `—` is fine.
3. **Which project is your reporting destination** — the one board where
   stand-up, show-and-tell and the combined weekly get posted. Per-epic IPM
   updates are unaffected; they stay on their own todo list.

Edit it by hand any time; it's plain Markdown.

## The local folder (optional)

A project can have a local folder for things that **don't belong in Basecamp**:

- your private notes and thinking
- decisions taken in chat or a meeting
- supporting artifacts — AppSheet schema exports, CSV dumps, data structures

**It is not a copy of Basecamp.** The skill will decline to mirror your Project
Starter Context or Epic Briefs there, and that's deliberate: two copies of the
same fact drift, and the agent can't tell which is right. Basecamp stays the
source of truth for anything Basecamp holds — reading it live costs about a
second.

Large exports are handled without drowning the session: structured data is read
as schema, row counts and a sample rather than in full, and the result is cached
in a `.digest.md` file beside it. If you refresh the export, the digest
invalidates itself automatically.

---

## Using it

Name the skill in your first message — most agents will not pick it up on their
own:

> Use the **basecamp-initiative-reporter** skill. Draft my stand-up for
> [Acme] Process Improvement.

> Use the basecamp-initiative-reporter skill. Show and tell for today.

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

**Every line traces to something clickable.** If a claim cannot be linked to a
real Basecamp event, it should not be in the report. If you see a line you cannot
verify, that is a bug worth reporting.

**Suggestions stay suggestions.** If one should become a todo, the skill hands
off to `basecamp-todo-coach` rather than writing it — a todo drafted here would
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

1. **A line you cannot verify.** Every claim should link to a real event. An
   unsupported line means the skill invented progress, which is the one thing it
   must never do — these get said out loud to colleagues as fact.
2. **A wrong day.** Basecamp returns UTC and you are in WIB, so evening work can
   land on the wrong day if the conversion is missed. If your 8pm work shows up
   in tomorrow's report, say so.
