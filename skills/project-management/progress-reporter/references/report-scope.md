# Report scope, time, and destination

This is the canonical scope table for all five reports. Resolve projects by ID
from the user's registry. Explicit user scope/window choices override defaults.

| Report | Default scope | Default local-time window | Posting destination |
|---|---|---|---|
| Stand-up | Every monitored project | Previous working day's close to now for blockers/continuity; today's plan from open assignments | Registry reporting board |
| Show-and-tell | Every monitored project | Today, up to now | Registry reporting board |
| Progress comment | Named todo | Today, up to now; that todo's events | Named todo |
| IPM update | Named epic/todo list | Since last IPM update if available; otherwise past seven days | Named todo list |
| Combined weekly | Every monitored project | Past seven days | Registry reporting board |

State the resolved project set, time window, timezone, and destination before
drafting. A narrowed scope does not silently change the posting board. Ask if
the requested target is ambiguous. A local day uses a half-open interval from
midnight to next midnight, bounded by now for an in-progress day.

Monitored projects and reporting destination are different concepts. A quiet
project can be omitted from the body of a combined weekly report after its
window was actually checked. Do not silently omit it from the scan.
