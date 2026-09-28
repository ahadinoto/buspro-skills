# Toolkit architecture and authoring

The installable unit is a leaf skill folder, not a category or the entire toolkit.
Keep knowledge and behavior in that leaf, optional model UI metadata under
`agents/`, and installation mechanics outside the canonical instructions.

Add a package under hiring, process-analysis, project-management, appsheet, or
communication. Choose one home category; use metadata tags for other subjects.
Supply name, description and string-valued metadata for display-name, version,
modes, dependencies, and optional companions. Keep dependencies honest: a tool
required for one mode should not block a pasted-context mode.

Record decisions before changing behavior. Add references only when useful,
keep relative links internal, and document missing-companion fallbacks. Shared
references are copied from `shared/` by the sync tool so individual installations
remain complete. The generated registry describes what is actually present.

A browser-chat manifest explicitly selects every covered section or records an
exclusion reason. Validate coverage when changing headings. Live actions must
be replaced with pasted-context instructions in browser-chat output.

Short names are public identifiers. Renaming is a deliberate compatibility
change: announce the replacement, install it first, and retire the old identifier.
Maintenance aliases help local tools repair links; they do not make old names
installable through the external CLI.

The future Toolkit can add useful process-analysis, AppSheet, and communication
skills plus optional integrations as concrete needs emerge. Keep one canonical
instruction set and add adapters only where host capabilities differ.
