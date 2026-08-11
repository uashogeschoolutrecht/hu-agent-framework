---
name: get-started
description: Start or continue a HU project using a risk-aware, spec-driven development workflow. Use when beginning a project, adding a feature, or asking how to work with the HU framework.
owner: Data Science Pool
last_reviewed: 2026-08-11
---

# Get Started

Start this workflow only after the user has opened the folder they want to work in. VS Code resets the Copilot Chat conversation when the user switches folders. If no workspace is open, or the current workspace is clearly not the intended project, tell the user to open the correct folder and run this skill again; do not attempt to carry the workflow across that switch. Keep the conversation concise. Announce each SDD stage in one line, plus classifications, gates, and decision records. Do not narrate file operations.

## 1. Understand intent before inspecting

Do not inspect files, run commands, or explore the workspace before this first exchange unless the user has already supplied the answers. Start with a short, focused set of questions:

> Briefly, what do you want to make or change? We will work out the specifics next.

Then ask only what is still unclear:

- What outcome would make this useful?
- Who will use it or be affected by it?
- Will it handle personal, research, or other sensitive data?
- Will it serve students, minors, patients, identifiable research subjects, or the general public?

Keep this exchange lightweight. Do not ask the user for a full specification, technical solution, or a small/big label. If the initial request already answers a question, do not ask it again.

Announce:

> SDD 1/8: Understanding the goal before examining the project context.

## 2. Form an initial scope hypothesis

From the user's brief description and answers, form a provisional view of the goal, affected parts, uncertainty, and likely session scope. Do not present this as a final classification yet. State it briefly and invite correction:

> SDD 2/8: I understand the goal as <brief summary>; initially this looks like a <focused/broad> session because <brief reason>. I’ll check the project context next and adjust that assessment if needed.

This gives the user an immediate orientation without making them wait for workspace exploration.

## 3. Locate and inspect context

Only after the initial exchange and scope hypothesis, inspect the current workspace to confirm the situation:

- For a new project, treat the open folder as the project location and inspect what is already there.
- For a change to an existing project, inspect the open folder's files, structure, configuration, tests, and version-control state.
- If the current workspace is empty, classify the work as greenfield after confirming that this is intentional.
- If the current workspace is not the project described by the user, stop and ask the user to open the target folder and run the skill again.

Announce:

> SDD 3/8: Locating the relevant project context and checking what already exists.

Do not switch folders during this workflow. Do not overwrite existing files.

## 3. Classify the work

Classify environment from the user's intent and the inspected context: greenfield or brownfield. Infer session scope rather than asking the user to label it small or big. Use the goal, number of affected parts, existing complexity, integrations, uncertainty, and expected validation effort.

Announce the classification with its reasons and invite correction:

> SDD 4/8: This is a <greenfield/brownfield> <focused/broad> session because <brief reasons>. You can correct that assessment before we continue.

Treat the scope as session-specific, not a permanent project label.

Ask these risk questions unless the answer is already clear:

1. Will it handle personal, research, or other sensitive data?
2. Will it serve students, minors, patients, identifiable research subjects, or the general public?

Classify risk as high if either answer is yes. If an answer is unclear, classify it as high. State the result and reason, for example: “This uses student data, so risk is high; I’ll add a review step before we ship.” Let the user correct a classification before continuing. Cost and external service calls are not risk gates, but each requires a decision record.

## 4. Bootstrap

If this is a new project, create these items from the templates beside this file:

- `AGENTS.md`
- `specs/`
- `decisions/`
- `.github/copilot/settings.json`

Do not overwrite existing files. If the project does not have a GitHub repository and the user asks for one, state the name, visibility, and organisation, then ask for confirmation before running `gh repo create`. Use the user's existing least-privilege authentication; never request administration or deletion capability.

The generated `AGENTS.md` is instruction-layer guidance, not a substitute for review or CI.

## 5. Specify

Announce:

> SDD 5/8: Turning the goal and project context into an agreed specification.

For greenfield work, create a new `specs/<short-name>.md`. For brownfield work, create a scoped delta in the same location and explain what existing behaviour remains unchanged. Use the spec template.

The spec must contain:

- problem and users
- scope and explicit non-goals
- environment, session scope, and risk classification with reasons
- functional requirements and acceptance criteria
- data, privacy, and external-service considerations
- infrastructure requirements and open questions
- test strategy
- prototype goal and what it should validate
- first vertical slice and the path it should trace through the system
- implementation notes, if they are already known

Do not start implementation while requirements or acceptance criteria are materially unclear. Ask focused questions instead.

## 6. Prototype and validate a vertical slice

This stage is active for every project. Keep it proportional to the inferred scope:

- For a focused project, use the smallest useful prototype: a sketch, stub, spike, example interaction, or thin proof of the riskiest assumption.
- For a broad project, prototype the uncertain or user-visible parts before committing to full implementation.
- Use the prototype to test understanding with the user and refine the spec, not merely to demonstrate generated code.

Then implement one thin vertical slice through the relevant layers, such as interface, application logic, domain/model logic, persistence, and external integration. Prefer a small traceable path over a complete horizontal module. Test the slice end to end where the architecture permits, and use the result to correct the spec or design before expanding the build.

Announce:

> SDD 6/8: Prototyping the riskiest assumption, then validating one thin path through the system.

Record important changes to the intended behaviour or architecture in the spec or a decision record. Do not treat a prototype as production-ready unless that is explicitly the goal.

## 7. Build and finish

Announce before the remaining implementation:

> SDD 7/8: Building the remaining scope against the validated specification and vertical slice.

Implement the accepted spec in small, reviewable increments. Prefer existing project conventions. Run the relevant tests after each meaningful increment and report failures plainly.

For high-risk work, pause before release for the review gate named in the spec. Check personal-data handling explicitly. Never commit secrets or data files. Before every push, inspect notebooks and clear output cells and tables derived from real records.

Ask before irreversible or destructive actions. Never delete a remote repository, branch, or release.

## Record decisions throughout

Create one `decisions/YYYY-MM-DD-<short-name>.md` for each non-obvious decision, including infrastructure choices, cost implications, and external service calls. Use the decision template:

- date
- decision
- reasoning
- alternatives rejected

Announce when a decision record is created. Do not create records for routine implementation details.

Before declaring completion, run the acceptance checks from the spec and repeat the vertical-slice test after the relevant implementation is complete.

Announce:

> SDD 8/8: Verifying acceptance criteria, the integrated slice, and recorded decisions.

Summarise what changed and what remains open, and point to the spec and decision records. For high-risk work, state whether the review gate passed, is pending, or was not applicable. Do not claim completion when verification was skipped.

Artifacts stay in English. Conversation may follow the user's language.
