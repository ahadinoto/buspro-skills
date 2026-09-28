# Agent compatibility

Checked against upstream documentation and skills CLI 1.7.0 on 2026-09-28.
Packaging support is separate from host discovery and model behavior.

| Host | Model route | Installation |
|---|---|---|
| Codex | Configured Codex model | `-a codex`; shared `.agents/skills` |
| Claude Code | Configured Claude model | `-a claude-code`; `.claude/skills` |
| Antigravity | Gemini | `-a antigravity`; CLI uses legacy `.gemini/antigravity/skills` globally |
| Cline / VS Code | GLM via configured provider | `-a cline`; CLI uses `.agents/skills` |

Antigravity desktop also documents `.gemini/config/skills`; its separate CLI
uses `.gemini/antigravity-cli/skills`. The maintainer adapter knows these paths.
Cline documentation describes `.cline/skills`, while current Cline source also
supports the shared directory selected by the installer. Check your installed
host version if a package does not appear; restart a session when needed.

Skills do not configure GLM credentials, Gemini accounts, Basecamp authentication,
or PDF/OCR tools. Test the actual host with a representative task after installing.
Native file reads, command execution, and connected documents depend on that host.

Validation covers metadata, isolated references, category discovery, shared-copy
drift, browser coverage/budgets and installer link ownership. Automated packaging
tests do not certify output quality across models. The independent behavioral
check was unavailable due to a usage limit; no cross-model pass is claimed.
Interview scenarios are bundled under `evals/` for later behavioral testing.

Sources:
- [skills CLI source, pinned release](https://github.com/vercel-labs/skills/tree/v1.7.0)
- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude skills](https://code.claude.com/docs/en/skills)
- [Antigravity skills](https://antigravity.google/docs/skills)
- [Cline skills](https://docs.cline.bot/customization/skills)
- [Cline directory discovery](https://github.com/cline/cline/blob/main/apps/vscode/src/core/storage/skill-directories.ts)
- [GLM through Cline](https://docs.z.ai/devpack/tool/cline)

On macOS, disposable project installs passed for copy and symlink modes,
reinstall after moving packages into categories, and complete removal. Codex,
Antigravity, and Cline share the CLI project target `.agents/skills`; Claude
uses `.claude/skills`. Generic local Git URL updates failed in the upstream
updater, so the offline smoke test exercises refresh through `add` instead.
A fresh public GitHub installation of `interview-prep` and hosted project
`update` both passed; installed content matched the canonical package.
