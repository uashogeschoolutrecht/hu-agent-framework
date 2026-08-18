---
name: share-contribution
description: Check a skill or agent against the HU framework standard and prepare a reviewed pull request to share it with the team or university. Use when the user asks to share, contribute, publish, or promote a skill or an agent.
owner: Data Science Pool
last_reviewed: 2026-08-18
---

# Share Contribution

Use this to offer a skill or an agent to a wider audience. It checks the contribution against the framework standard and prepares a pull request. It never merges, and it never claims approval.

Read `../../knowledge/framework/contribution-standard.md` first. It is the bar this skill checks against. Do not invent additional requirements, and do not restate the standard back to the user.

## 1. Identify what is being shared

Establish whether it is a skill folder containing `SKILL.md`, or an agent file. Confirm the path with the user if more than one candidate exists. Share one contribution at a time.

## 2. Check it against the standard

Work through the standard and record a pass or fail for each point, including frontmatter, description quality and distinguishability, single job and stopping condition, absence of restated definitions, safety, and evidence of real use.

Two checks need active work rather than reading:

- **Routing collision.** Read the descriptions of the skills and agents already in the target repository. If the contribution could match the same request as something already there, that is a fail: it either narrows its description or extends the existing contribution instead.
- **Real use.** Ask what real work it was used on. "Written but not yet used" is a fail, not a caveat.

Report every failure with the specific point it fails. Do not repair the author's intent silently; small mechanical fixes such as a missing `last_reviewed` may be made, and must be reported.

If anything fails, stop and tell the user what to fix. Do not open a pull request for a contribution that does not meet the bar.

## 3. Choose the target

Ask whether the target is the team repository (`hu-agent-framework-dsp`) or the university repository (`hu-agent-framework`). University-wide promotion should normally follow successful team use; say so if the user goes straight to university without it, then respect their answer.

Place a skill in `plugins/<plugin>/skills/<name>/` and an agent in `plugins/<plugin>/agents/<name>.md`. Do not rename the contribution to add a namespace prefix; the plugin name becomes the command prefix automatically.

## 4. Prepare the pull request

Create a branch. Copy only the contribution's own files. Do not carry across project data, fixtures, or unrelated changes. Fill in the pull request template from the target repository.

Confirm the branch name, target repository, and the files being copied with the user before running `gh`. Then open the pull request with `gh pr create`. Do not merge it, and do not approve it. A human review is required.

## Output

Report the target repository, the branch, the files copied, the pull request URL, and the result of every standard check including anything you fixed. State plainly that the contribution is proposed and not yet approved or available to anyone else.

Artifacts stay in English.
