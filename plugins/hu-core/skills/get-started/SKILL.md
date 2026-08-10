---
name: get-started
description: Start or continue a HU project using a risk-aware, spec-driven development workflow. Use when beginning a project, adding a feature, or asking how to work with the HU framework.
owner: Data Science Pool
last_reviewed: 2026-08-10
---

# Get Started

Run this workflow in the current project. Keep the conversation concise and announce classifications, gates, and records. Do not narrate every file operation.

## 1. Orient

Ask these questions unless the answer is already clear:

1. Is this a greenfield project or a brownfield change to an existing project?
2. Is the work small or big for this session? Reassess this per session; do not permanently label the project.
3. Will it handle personal, research, or other sensitive data?
4. Will it serve students, minors, patients, identifiable research subjects, or the general public?

Classify risk as high if either of the last two answers is yes. If the answer is unclear, classify it as high. Cost and external service calls are not risk gates, but each requires a decision record.

State every classification and its reason. Example: “This uses student data, so risk is high; I’ll add a review step before we ship.” Let the user correct a classification before continuing.

## 2. Bootstrap

If this is a new project, create these items from the templates beside this file:

- `AGENTS.md`
- `specs/`
- `decisions/`
- `.github/copilot/settings.json`

Do not overwrite existing files. If the project does not have a GitHub repository and the user asks for one, state the name, visibility, and organisation, then ask for confirmation before running `gh repo create`. Use the user's existing least-privilege authentication; never request administration or deletion capability.

The generated `AGENTS.md` is instruction-layer guidance, not a substitute for review or CI.

## 3. Specify

For greenfield work, create a new `specs/<short-name>.md`. For brownfield work, create a scoped delta in the same location and explain what existing behaviour remains unchanged. Use the spec template.

The spec must contain:

- problem and users
- scope and explicit non-goals
- environment, session scope, and risk classification with reasons
- functional requirements and acceptance criteria
- data, privacy, and external-service considerations
- infrastructure requirements and open questions
- test strategy
- implementation notes, if they are already known

Do not start implementation while requirements or acceptance criteria are materially unclear. Ask focused questions instead.

## 4. Build

Implement the accepted spec in small, reviewable increments. Prefer existing project conventions. Run the relevant tests after each meaningful increment and report failures plainly.

For high-risk work, pause before release for the review gate named in the spec. Check personal-data handling explicitly. Never commit secrets or data files. Before every push, inspect notebooks and clear output cells and tables derived from real records.

Ask before irreversible or destructive actions. Never delete a remote repository, branch, or release.

## 5. Record decisions

Create one `decisions/YYYY-MM-DD-<short-name>.md` for each non-obvious decision, including infrastructure choices, cost implications, and external service calls. Use the decision template:

- date
- decision
- reasoning
- alternatives rejected

Announce when a decision record is created. Do not create records for routine implementation details.

## 6. Finish

Run the acceptance checks from the spec, summarise what changed and what remains open, and point to the spec and decision records. For high-risk work, state whether the review gate passed, is pending, or was not applicable. Do not claim completion when verification was skipped.

Artifacts stay in English. Conversation may follow the user's language.
