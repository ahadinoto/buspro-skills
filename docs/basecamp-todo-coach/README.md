# Basecamp Todo & IPM Coach

*A skill in the [`buspro-skills`](../../README.md) repo.*

A coaching skill for writing clear, reviewable, executable Basecamp work. It
holds the Business Process team's todo quality system: Project Starter Context,
Epic Briefs, individual todos in the locked 11-field format, the readiness gate,
discovery-deliverable reviews, and IPM update comments.

The point of the skill is the **readiness gate**, not polish. A vague request
does not become a neatly worded `[Development]` todo — it gets routed to
`[Confirmation]`, `[Meeting]`, `[Process Mapping]`, or `[SPIKE]` until it is
actually ready.

---

## Install

### Coding agents — Claude Code, Cline, Antigravity, Cursor, Codex, Windsurf

One command. `npx skills` detects which agents you have installed and puts the
skill in each one's global directory.

```bash
npx skills add ahadinoto/buspro-skills --skill basecamp-todo-coach -g
```

Add `-a <agent>` to target one (e.g. `-a cline`, `-a claude-code`). Then start a
new session — see [Using it](#using-it) for what to actually say.

**Private repo?** Same command. `npx skills` uses whatever git auth you already
have — GitHub CLI, a credential helper, or SSH. If HTTPS gives you trouble, use
the SSH form:

```bash
npx skills add git@github.com:ahadinoto/buspro-skills.git --skill basecamp-todo-coach -g
```

Useful variations:

```bash
npx skills add ahadinoto/buspro-skills --list                    # look before installing
npx skills add ahadinoto/buspro-skills -g -a claude-code -y      # one agent, no prompts
npx skills update -g                                        # pull the latest version
npx skills remove --global basecamp-todo-coach              # uninstall
```

### Browser chat — Gemini Gem, ChatGPT Custom GPT, Claude Project

Browser chat has no Basecamp CLI, so the skill runs in **Paste Mode**: it coaches
normally and asks you to paste the Basecamp content it needs. The rules and the
readiness gate are identical.

Build the paste-ready bundles:

```bash
python3 tools/build-web-prompt.py --skill basecamp-todo-coach
```

Then set up your assistant from `dist/basecamp-todo-coach/<target>/`:

| Assistant | Target | What to do |
|---|---|---|
| Gemini Gem, Claude Project | `dist/basecamp-todo-coach/gem/` | Paste `system_instructions.md` into the instruction box; upload both `knowledge_*.md` files |
| Gemini Gem (if the full bundle is rejected) | `dist/basecamp-todo-coach/gem-compact/` | Same, smaller instruction tier |
| ChatGPT Custom GPT | `dist/basecamp-todo-coach/gpt/` | Paste `system_instructions.md` into Instructions; upload both `knowledge_*.md` under Knowledge |

Upload **both** knowledge files. They are not optional extras — the format
templates and the 23 worked examples live there, and the instructions tell the
agent to go read them.

### After pasting, check the last line

Some instruction boxes truncate a long paste **without saying so**. Every bundle
therefore ends with a marker line:

> `(End of instruction — if this line is missing after pasting, the text was truncated. …)`

Scroll to the bottom of the box and confirm that line is there. If it is
missing, the paste was cut: use `dist/basecamp-todo-coach/gem-compact/` instead and check again.

This takes five seconds and is worth doing every time, because a truncated paste
does not look broken — it looks like a coach that has stopped enforcing some of
the rules. Reported as "it missed my Validation PIC", that sends everyone
hunting a rule bug that does not exist.

---

## Using it

Whichever agent you use, it is a chat. There is no command to run.

### Name the skill in your first message

Claude Code usually picks the skill up on its own. Other agents and other models
often do not, so say it outright:

> Use the **basecamp-todo-coach** skill. I want to review a todo before I put it
> in Basecamp.

After that the conversation carries it. If the reply never mentions the
readiness gate or todo types, and never asks for the fields it needs, the skill
did not load — start a new session and name it again.

### Starter prompts

One per workflow. Paste and adapt.

**Review a draft todo** — the most common use:

> Use the basecamp-todo-coach skill. Review this todo and tell me if it's ready:
> *[paste the draft]*

**Turn a vague request into properly routed todos:**

> Use the basecamp-todo-coach skill. My manager asked me to "fix the reporting
> flow." Help me break this into properly routed todos.

**Write one todo from scratch:**

> Use the basecamp-todo-coach skill. Help me write a todo for mapping the
> current invoice approval process.

**Plan an epic:**

> Use the basecamp-todo-coach skill. Help me write an Epic Brief for a new todo
> list.

**Draft an IPM update:**

> Use the basecamp-todo-coach skill. Help me write this week's IPM update
> comment.

**Review discovery work:**

> Use the basecamp-todo-coach skill. Review this process map against its done
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

The rules themselves are readable at `~/.agents/skills/basecamp-todo-coach/`
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

## Editing the skill

Single source of truth: this repo. The tracker
(`docs/basecamp-todo-coach/quality-system-tracker.md`) is the canonical
decision log — record what changed and why there, then update the skill. Repo
conventions for every skill live in `AGENTS.md` at the root.

Everything under `dist/` is **generated** — do not hand-edit it; rebuild
instead. Every other file is edited directly, including
`skills/basecamp-todo-coach/references/examples.md`, which is now the canonical
home of the 23 examples (it used to be a hand-copied duplicate of a root-level
doc, so the same 49 KB lived in the repo twice).

For live editing across your own agents, symlink the working tree instead of
installing a pinned clone:

```bash
tools/install-global.sh --dry-run   # see what it would change
tools/install-global.sh             # link
tools/install-global.sh --unlink    # undo
```

It only touches global skills directories that already exist, and refuses to
overwrite a real directory (an `npx skills` install, or a copy with edits in it).

### When you change a heading in SKILL.md

The web bundler selects content by `##` heading name. Rename a heading and the
build fails loudly, naming the section — update `TARGETS` in
`tools/build-web-prompt.py`. It will not silently drop a section.

### Instruction budgets

`build-web-prompt.py` reports every tier against its target's budget:

| Target | Budget | Kind |
|---|---|---|
| `gem` | 25,000 | soft — **unverified**, see below |
| `gem-compact` | 15,000 | hard — build fails if exceeded |
| `gpt` | 8,000 | hard — documented Custom GPT cap |

The `gem` budget is an assumption, not a documented limit. What we know is that
the team's hand-written Gem instruction has run at ~14.6 KB, which proves that
much is accepted and nothing about the ceiling. If a real Gem rejects the `gem`
bundle, use `gem-compact` — do not trim the rules to fit.

Full skill content is ~93 KB, so no single bundle can hold everything. That is
why the browser path is tiered rather than one pasted file.
