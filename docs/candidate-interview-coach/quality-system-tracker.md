# Candidate Interview Coach — decision record

## 2026-09-28 — Interview Prep and public availability

User-approved decisions, recorded before implementation:

- Rename the skill to `interview-prep`, under `skills/hiring/`; keep this human
  documentation path stable. Publish the reviewed package for mentee installation.
- Preserve the candidate-specific workflow, interviewer defaults, language rules,
  and nine behavioral scenarios. No generic question bank or new hiring rubric.
- Remove the incidental organization name from the reusable profile, and remove
  personal filesystem/conversation identifiers from distributed usage notes.
- Keep host-specific metadata outside the canonical body. Record version and
  capability requirements as portable metadata; retain optional file-tool fallback.
- Verify the published install source, not only local symlinks. Record package,
  discovery, and behavioral evidence separately.


## 2026-09-25 — freeze v1.1 and install one canonical source

Source: the accepted design and two de-identified candidate dry-run refinements.
This design evidence informed the bundled scenarios;
candidate claims reported there are not independently verified CV facts.

Decisions recorded before implementation:

1. Keep the installable unit at `skills/candidate-interview-coach/` in this
   existing collection. Ship the four requested files: `SKILL.md`,
   `references/interviewer-profile.md`, `references/quality-bar.md`, and
   `evals/test-scenarios.md`. Keep installation notes outside the skill.
2. Read the entire available CV and form a candidate fingerprint before intake
   or question selection. If the CV cannot be read, disclose the gap; never
   claim to have read it or manufacture anchors.
3. Ask only missing context that changes the interview. Reuse established
   role, duration, and preferences, but never carry one candidate's facts to
   another. Offer candidate-specific, numbered focus choices.
4. Let the candidate and interviewer determine the question mix. Remove the
   earlier fixed Behavioral / Technical / Management template. Prefer 2–3
   main questions for a short interview, with selective probes for ownership,
   reasoning, trade-offs, or business communication.
5. Match the interviewer's language. Use conversational Bahasa Indonesia when
   requested or established, retaining natural business/technical English.
   Use numbered lists for questions, choices, and options so `#2` is usable.
6. Place substantive experience and judgment questions first. Put motivation
   or career-transition questions near the end unless that is explicitly the
   primary screening concern. It is optional when time or chosen focus excludes it.
7. Gate each main question on Candidate → CV → Role → Interviewer →
   Conversation. A company-name substitution does not count as personalization.
8. Support live follow-ups with one next question based on the actual answer.
   Ownership gaps are reasons to explore, not evidence of dishonesty.
9. Turn the two dry runs into de-identified regression fixtures, supplemented
   by sparse-CV, intake, urgency, language, and live-answer cases. Do not bundle
   private CVs, contact information, or a supposedly verified original resume.
10. Use directory symlinks into supported local skill roots. Current official
    Antigravity roots are `~/.gemini/config/skills` and
    `~/.gemini/antigravity-cli/skills`; these differ from Gemini CLI's roots.
    Correct the shared install helper's directory inventory without changing
    its existing-directory-only behavior or adding a per-skill installer.
11. This release targets local agents. Browser ChatGPT/Gemini distribution
    needs a separate import/plugin setup; no browser-chat bundle is requested.

The original design was longer and iterative. The packaged instructions
consolidate the accepted behavior and omit superseded templates. Future
changes should address an observed weakness rather than adding generic rules.
