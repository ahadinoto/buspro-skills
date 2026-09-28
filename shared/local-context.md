# The project's local folder

A registered project may have a local folder. It holds **what Basecamp cannot**
— nothing else.

## What belongs there

- **Private notes** — thinking, decisions taken in chat or a meeting, context
  the user does not want on a company board.
- **Supporting artifacts** — exported schemas, CSV dumps, data structures.
  Files too large or too raw for Basecamp.
- **Digests** — generated summaries of those artifacts (below).

## What must never go there

**A copy of anything Basecamp holds.** Not the Project Starter Context, not the
Epic Brief, not todo bodies, not status.

Two independently edited copies of one fact cannot be reconciled: when they
disagree there is no way to know which is right, and the agent reads the stale
one with full confidence. Basecamp remains the source of truth for everything it
holds — read it live; it costs about a second.

If the user asks for a local copy of Basecamp content, say plainly why not, and
offer the alternative: notes *about* it, which is what the folder is for.

## Reading the folder

When a project has a local folder, read it for context the same way you would
read attached documents — then let Basecamp override it for anything Basecamp
knows (scope, status, PIC, decisions).

### The read rule, by file kind

**Prose** — `.md`, `.txt`, notes, specs: read in full.

**Structured data** — `.csv`, `.tsv`, `.json`, schema dumps: **never read
whole.** Read structure only:

- column names and apparent types
- row count
- value ranges or distinct values for key columns
- roughly 20 sample rows

That answers essentially every question worth asking of a table, and it behaves
identically whether the export has 200 rows or two million. Reading a large
export in full will exhaust the context window and fail the task outright — on a
smaller-context model it may derail the session rather than fail cleanly.

## Digests

Reading a large artifact is expensive, so record the result and reuse it.

Write `<filename>.digest.md` beside the artifact:

```markdown
<!-- GENERATED digest — do not edit. Regenerated when the source changes. -->
Source: appsheet-orders-export.csv
Size: 48293014 bytes
Modified: 2026-09-16T04:12:33Z

## What this is
One row per order line from the AppSheet orders table.

## Structure
| Column | Type | Notes |
|---|---|---|
| order_id | string | primary key, format ORD-00000 |
...

## Sample rows
...
```

**The fingerprint is what makes this safe.** Before trusting a digest, compare
the source's current size and modified time with the recorded values. If they
differ, the export has been refreshed — regenerate the digest and say so.

This is a cache, not a mirror. It is derived one-way from a single source, so
staleness is always detectable. That is the difference between this and copying
Basecamp content locally, which has no such check.

## Writing to the folder

Two classes of file, two rules.

**Generated (agent-owned)** — digests, and anything else carrying a `GENERATED`
header. Rewrite freely; that is what they are for.

**Authored (user-owned)** — notes, `projects.md`, anything the user wrote.
**Never overwrite silently.** Show exactly what you intend to add or change and
wait for confirmation. Create a new file only after confirming its path.

When in doubt about which class a file is, treat it as user-owned. Regenerating
a digest costs a few seconds; destroying someone's notes is unrecoverable.
