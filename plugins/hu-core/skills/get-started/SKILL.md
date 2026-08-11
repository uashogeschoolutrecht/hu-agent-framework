---
name: get-started
description: Start or continue a HU project using a risk-aware, spec-driven development workflow. Use when beginning a project, adding a feature, or asking how to work with the HU framework.
owner: Data Science Pool
last_reviewed: 2026-08-11
---

# Get Started

Run this workflow from the user's intent, not from an assumption that the current workspace is the relevant project. Keep the conversation concise. Announce each SDD stage in one line, plus classifications, gates, and decision records. Do not narrate file operations.

## 1. Understand intent

Begin with one short question:

> Briefly, what do you want to make or change? We will work out the specifics next.

Make clear that the answer should be brief. Do not ask the user to provide a full specification at this point.

Announce:

> SDD 1/7: Understanding the goal before examining the project context.

## 2. Locate and inspect context

Use the brief intent to determine what context is relevant:

- For a new project, ask where the user wants it created or opened if no suitable folder is open.
- For a change to an existing project, ask for its path or repository if it is not open; do not treat an unrelated empty workspace as that project.
- If a relevant workspace is open, inspect its files, structure, configuration, tests, and version-control state.
- If no relevant project exists yet, classify the work as greenfield without pretending that filesystem inspection happened.

Announce:

> SDD 2/7: Locating the relevant project context and checking what already exists.

If the user identifies an existing project that is not open, help them open or locate it before inspecting it. If they want a new project, establish its location before creating project artifacts. Do not overwrite existing files.

## 3. Classify the work

Classify environment from the user's intent and the inspected context: greenfield or brownfield. Infer session scope rather than asking the user to label it small or big. Use the goal, number of affected parts, existing complexity, integrations, uncertainty, and expected validation effort.

Announce the classification with its reasons and invite correction:

> SDD 3/7: This is a <greenfield/brownfield> <focused/broad> session because <brief reasons>. You can correct that assessment before we continue.

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

> SDD 4/7: Turning the goal and project context into an agreed specification.

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

> SDD 5/7: Prototyping the riskiest assumption, then validating one thin path through the system.

Record important changes to the intended behaviour or architecture in the spec or a decision record. Do not treat a prototype as production-ready unless that is explicitly the goal.

## 7. Build and finish

Announce before the remaining implementation:

> SDD 6/7: Building the remaining scope against the validated specification and vertical slice.

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

> SDD 7/7: Verifying acceptance criteria, the integrated slice, and recorded decisions.

Summarise what changed and what remains open, and point to the spec and decision records. For high-risk work, state whether the review gate passed, is pending, or was not applicable. Do not claim completion when verification was skipped.

Artifacts stay in English. Conversation may follow the user's language.
