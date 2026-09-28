# Progress Reporter — decision record

## 2026-09-28 — Toolkit packaging and consistent report scope

User-approved decisions, recorded before implementation:

- Rename the skill to `progress-reporter`, under `skills/project-management/`,
  tagged communication. Preserve its five report types and live-data requirement.
- Daily and combined weekly reports cover all monitored projects unless the user
  explicitly narrows scope. Per-todo and per-epic reports stay local to that item.
  Daily/combined reports go to the configured reporting destination.
- Keep one shared scope table in the package. Correct WIB conversion and calendar
  examples; use half-open local-day boundaries converted to UTC.
- Attribute Basecamp evidence with links and user-reported off-platform work
  explicitly as user-reported. Neither source is invented.
- Posting needs authorization for the concrete target and content; preserve
  already-provided authorization. Read-only credentials can support drafting,
  but posting requires write permission.
- An absent todo-planner is an optional companion, not an assumed installed skill.
- Add synthetic evaluation scenarios for scope, timezone, empty windows, missing
  access, evidence, and posting boundaries. Record executed results separately.

Earlier shared decisions remain in ../basecamp-todo-coach/quality-system-tracker.md.
