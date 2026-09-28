<!-- GENERATED from shared/project-registry.md by tools/sync-shared.py — do not edit.
     Edit the canonical file and re-run the script. Both skills carry a copy
     because npx skills installs one skill directory and nothing else. -->

# The project registry

Both skills read this before doing anything else. It is what stops the agent
guessing which project you mean — the single most common failure reported so far.

## Where it lives

```text
~/.config/buspro-skills/projects.md
```

Fixed path, one per user. It sits next to the Basecamp CLI's own config
(`~/.config/basecamp/`), survives skill reinstalls, and is found identically by
Claude Code, Cline, Codex and Gemini CLI.

**If it does not exist, do not invent one and do not guess a project.** Offer to
create it, walk the user through the questions below, show the file you intend
to write, and wait for confirmation. See *Bootstrap* below.

## Format

Markdown, so a person can edit it by hand without tooling.

```markdown
# Basecamp projects

## Reporting destination

Stand-up, show-and-tell, and the combined weekly update are posted here.

- Project: [Acme] Process Improvement
- Project ID: 12345678

## Monitored projects

| Project | ID | Local folder |
|---|---|---|
| [Acme] Process Improvement | 12345678 | ~/work/acme-process |
| [Acme] Billing Hub | 12345679 | ~/work/billing-hub |
| [Acme] Onboarding | 12345680 | — |
```

Rules:

- **Project ID is authoritative**, not the name. Names get edited in Basecamp;
  IDs do not. Always resolve by ID, and refresh a stale name rather than
  failing.
- **Local folder is optional.** `—` means this project has no local folder yet.
  That is normal and not an error — the project is still monitored.
- **One reporting destination.** Stand-ups span several projects (1–4 on a
  typical day), so the ritual reports go to one board rather than fragmenting
  across every project touched. Per-epic IPM comments are unaffected; they stay
  on their own todo list.
- Paths may use `~`. Expand it when reading.

## Reading it

1. Read `~/.config/buspro-skills/projects.md`.
2. Missing → *Bootstrap*.
3. Present but the project the user named is absent → offer to add it; do not
   silently fall back to a project that is listed.
4. **State what you resolved before acting:**
   > Working in **[Acme] Process Improvement** (`12345678`), local folder
   > `~/work/acme-process`.

Never proceed on an ambiguous match. Two projects with similar names means ask.

## Bootstrap

When the registry is missing, or the user asks to add a project:

1. **Find the projects.** `basecamp projects list --json` returns everything
   they can see. Show the list rather than asking them to recall IDs.
2. **Ask which to monitor.** Not all of them — only what they actively work on.
3. **Ask for a local folder per project**, and say what it is for: private
   notes and supporting files that do not belong in Basecamp. `—` is a fine
   answer; it can be added later.
4. **Ask which project is the reporting destination** — where stand-up,
   show-and-tell and the combined weekly get posted.
5. **Show the complete file, then write it only after they confirm.** Create
   `~/.config/buspro-skills/` if needed.

Do not create the file as a side effect of some other task. The user should
always know it now exists and where.

## Keeping it current

- A project the user works in that is not listed → offer to add it, once. Do not
  nag every session.
- A name that no longer matches Basecamp → update the name, keep the ID.
- Removing a project is the user's call. Never remove one on your own; a project
  with no recent activity is not necessarily finished.

`projects.md` is **authored by the user**, so the write rules for user-owned
files apply: show exactly what will change and wait. Never rewrite it wholesale
to add one row.
