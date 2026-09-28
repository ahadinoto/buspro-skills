# todo-planner

Plan clear, reviewable Basecamp work and check readiness.

```bash
npx skills add ahadinoto/buspro-skills --skill todo-planner -g
```

See the [collection guide](../../README.md) for setup, dependencies, updates,
and supported hosts. This documentation folder keeps its historical name; the
installable identifier is `todo-planner`.

[Quality decisions](quality-system-tracker.md) record the reasoning behind
the instructions. Historical design records describe their original version.

## Using it

Whichever agent you use, it is a chat. There is no command to run.

The first time you use it, the skill offers to create a project registry at
`~/.config/buspro-skills/projects.md` — the list of Basecamp projects you work
in, so it stops guessing which one you mean. It shows you the file before
writing it. See the
[reporter's readme](../progress-reporter/README.md#first-run-the-project-registry)
for the full setup; both skills share the same registry.

### Name the skill in your first message

Claude Code usually picks the skill up on its own. Other agents and other models
often do not, so say it outright:

> Use the **todo-planner** skill. I want to review a todo before I put it
> in Basecamp.

After that the conversation carries it. If the reply never mentions the
readiness gate or todo types, and never asks for the fields it needs, the skill
did not load — start a new session and name it again.

### Starter prompts

One per workflow. Paste and adapt.

For stand-ups, show-and-tells, progress comments and IPM updates, use
[`progress-reporter`](../progress-reporter/README.md)
instead — those read live Basecamp activity.

**Check the whole backlog:**

> Use the todo-planner skill. Review all the todos in this project and
> give me a backlog health summary.

You get counts and the blocking issues — how many are ready, what's waiting on
whom, which epics have gaps — rather than a full review of every todo. Ask it to
open any individual one properly from there.

**Review a draft todo** — the most common use:

> Use the todo-planner skill. Review this todo and tell me if it's ready:
> *[paste the draft]*

**Turn a vague request into properly routed todos:**

> Use the todo-planner skill. My manager asked me to "fix the reporting
> flow." Help me break this into properly routed todos.

**Write one todo from scratch:**

> Use the todo-planner skill. Help me write a todo for mapping the
> current invoice approval process.

**Plan an epic:**

> Use the todo-planner skill. Help me write an Epic Brief for a new todo
> list.

**Review discovery work:**

> Use the todo-planner skill. Review this process map against its done
> criteria: *[paste]*

### What a good review looks like

A review comes back in four parts, in this order:

1. **Verdict** — Ready / Needs Revision / Should become Confirmation, Meeting /
   Discussion, Process Mapping, SPIKE, or Epic
2. **Key Issues**
3. **Suggested Improved Version**
4. **Questions to Confirm**

If it just rewrites your todo more neatly with no verdict, that is a miss worth
reporting.

### Pushback is the skill working

If you paste something vague and get a polished `[Development]` todo back, the
skill has **failed**. A vague request is supposed to be routed to
`[Confirmation]`, `[Meeting]`, `[Process Mapping]`, or `[SPIKE]` until it is
actually ready. Being asked "who validates this?" instead of handed a tidy todo
is the point, not the tool being difficult.

### Check these on your first session

**Which mode it is in.** It should say so once, early. See [Two modes](#two-modes).

**The write gate.** Ask it to create a todo in Basecamp. It must show the exact
content, show the exact command, and *wait* for you. If it creates the todo
without asking, stop and report it — an agent with a shell can really run that,
and that is the one failure with consequences in live Basecamp data.

The rules themselves are readable at `~/.agents/skills/todo-planner/`
(or your agent's own skills directory) if you want to see what it is following.

---

## Two modes

The skill checks for the Basecamp CLI at the start of a session and says which
mode it is in.

**Agent Mode** — CLI installed and authenticated. Reads live project context,
epics, the IPM comment timeline, and the real project member list to check PIC
and Validation PIC names. Writes stay gated: it shows the exact payload and the
exact command, and waits for your confirmation.

**Paste Mode** — no CLI, not signed in, or browser chat. Coaches from what you
paste, and says plainly when an answer rests only on that.

To get Agent Mode, install the official
[Basecamp CLI](https://github.com/basecamp/basecamp-cli) and authenticate:

```bash
curl -fsSL https://basecamp.com/install-cli | bash
```

```bash
basecamp auth login --scope full
```

Check it with `basecamp auth status` — `authenticated: true` means Agent Mode is
available. `--scope full` is what enables writes; read-only auth still gets you
live context.

Mode changes how the coach gets context and whether it can write. It never
changes the standard.

---

## Found a problem? Report it

The skill is in pilot. Feedback is how it improves, so a report of "the coach
did something odd" is useful even when you are not sure it is a bug.

**Tell Adiwijaya — chat, WhatsApp, verbally, whatever is easiest.** There is no
form to fill in.

Two details help if you have them: **which setup you used** (a coding agent, or
a browser Gem / Custom GPT), and for browser chat, **whether the
end-of-instruction marker was there** (see above) — without that, a truncated
paste looks exactly like a genuine rule gap.

Worth reporting: the coach approved a todo that was not ready, routed to the
wrong type, invented a Validation PIC, wrote to Basecamp without asking, or
produced a `Tip` that was generic boilerplate.

---

---
