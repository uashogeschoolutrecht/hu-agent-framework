---
name: share-skill
description: Prepare a reviewed pull request to share a useful skill with the DSP team or HU-wide core marketplace. Use when the user asks to share or promote a skill.
owner: Data Science Pool
last_reviewed: 2026-08-10
---

# Share Skill

1. Confirm the skill folder contains `SKILL.md` with `name`, `description`, `owner`, and `last_reviewed` frontmatter.
2. Ask whether the target is the DSP team repository (`hu-agent-framework-dsp`) or the university core repository (`hu-agent-framework`).
3. Check that the skill was used on real work, does not contain secrets or data, and answers the sensitive-data question.
4. Create a branch, copy only the skill folder to the target repository, and fill in the pull request template.
5. Open a pull request with `gh pr create`. Do not merge it. A human review is required.

University-wide promotion should normally follow successful team use. Never claim that a pull request is approved.
