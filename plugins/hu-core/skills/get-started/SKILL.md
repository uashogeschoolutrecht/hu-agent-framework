---
name: get-started
description: Start or continue a HU project using a risk-aware, spec-driven development workflow. Use when beginning a project, adding a feature, or asking how to work with the HU framework.
owner: Data Science Pool
last_reviewed: 2026-08-11
---

# Get Started

Start this workflow only after the user has opened the folder they want to work in. VS Code resets the Copilot Chat conversation when the user switches folders. If no workspace is open, or the current workspace is clearly not the intended project, tell the user to open the correct folder and run this skill again; do not attempt to carry the workflow across that switch. Keep the conversation concise. Announce each SDD stage in one line, plus classifications, gates, decision records, and feedback loops. Do not narrate file operations.

## 1. Understand intent before inspecting

Do not inspect files, run commands, or explore the workspace before this exchange unless the user has already supplied the answers. Ask exactly one question per response. Never show the user a list of upcoming questions. Keep each question short and wait for the answer before asking the next one.

The first response must contain only the stage announcement and this question:

> Briefly, what do you want to make or change? We will work out the specifics next.

After the user answers, ask only the next unanswered question, in this order:

1. What outcome would make this useful?
2. Who will use it or be affected by it?
3. Will it handle sensitive data? Use `#vscode/askQuestions` with the single-choice options `No`, `Yes`, and `Not sure`.
4. Is the intended audience or user group sensitive? Use `#vscode/askQuestions` with the single-choice options `No`, `Yes`, and `Not sure`. Explain only if needed that this includes students, minors, patients, identifiable research subjects, or the general public.
5. Is this a new project or a change to an existing project? Use `#vscode/askQuestions` with the single-choice options `New project`, `Existing project`, and `Not sure`.

For every choice question, invoke the built-in `#vscode/askQuestions` tool rather than writing the choices into the chat response. Make one tool call for one question and wait for the user's selection. Do not emulate the tool with bullets, numbered options, or a sentence listing the choices. If the tool is unavailable, ask one plain-text question without listing choices and accept the user's answer. If the user's initial message already answers a question, skip it. Do not use the terms `greenfield` or `brownfield` in user-facing questions or explanations.

Keep this exchange lightweight. Do not ask the user for a full specification, technical solution, or a small/big label.

Announce:

> SDD 1/9: Understanding the goal before examining the project context.

## 2. Align on assumptions

Draft the goal, desired outcome, users, likely affected parts, and important assumptions from the user's answers. Do not make the user write a complete plan. Ask only about assumptions that are unclear or load-bearing, one question per response, and give a recommended answer for each question. The user should be able to confirm or correct the draft rather than construct it from scratch.

> SDD 2/9: I understand the goal as <brief summary>. These are my working assumptions: <brief list>. Please correct anything important before I inspect the project.

Ask one final lightweight alignment question:

> What would make this unusable or a clear failure for you?

If the intent is vague, the assumptions conflict, or the work appears broad or high risk, continue with another short round of targeted questions. Announce why the deeper round is needed. Do not turn this into a fixed questionnaire. The alignment stage is complete when the goal, intended outcome, boundaries, and material assumptions are shared enough to inspect and specify.

## 3. Locate and inspect context

Only after the initial questioning and alignment, inspect the current workspace to confirm the situation:

- For a new project, treat the open folder as the project location and inspect what is already there.
- For a change to an existing project, inspect the open folder's files, structure, configuration, tests, and version-control state.
- If the current workspace is empty, treat it as a new project only after confirming that this is intentional.
- If the current workspace is not the project described by the user, stop and ask the user to open the target folder and run the skill again.

Announce:

> SDD 3/9: Locating the relevant project context and checking what already exists.

Do not switch folders during this workflow. Do not overwrite existing files.

## 4. Classify the work

Internally classify the project as new or existing from the user's intent and the inspected context. Do not expose the terms `greenfield` or `brownfield`. Infer session scope rather than asking the user to label it small or big. Use the goal, number of affected parts, existing complexity, integrations, uncertainty, and expected validation effort.

Announce the classification with its reasons and invite correction:

> SDD 4/9: This is a <new-project/existing-project> <focused/broad> session because <brief reasons>. You can correct that assessment before we continue.

Treat the scope as session-specific, not a permanent project label.

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

> SDD 5/9: Turning the goal and project context into an agreed specification.

For a new project, create a new `specs/<short-name>.md`. For an existing project, create a scoped delta in the same location and explain what existing behaviour remains unchanged. Use the spec template.

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
- confirmed assumptions and boundaries
- iteration and feedback approach
- implementation notes, if they are already known

Do not start implementation while requirements or acceptance criteria are materially unclear. Ask focused questions instead.

## 6. Prototype

This stage is active for every project. Keep it proportional to the inferred scope:

- For a focused project, use the smallest useful prototype: a sketch, stub, spike, example interaction, or thin proof of the riskiest assumption.
- For a broad project, prototype the uncertain or user-visible parts before committing to full implementation.
- Use the prototype to test understanding with the user and refine the spec, not merely to demonstrate generated code.
- Skip a separate prototype only when building the prototype is practically the same as building the whole small project. State that decision and why.

Announce:

> SDD 6/9: Prototyping the riskiest assumption so we can improve the direction before building further.

Show the prototype or a functioning thin example and proactively ask what the user would change, remove, or do differently. If feedback materially changes the goal, users, boundaries, or assumptions, return to the alignment stage, restate the revised understanding, and update the spec's `Iterations / Feedback` section before continuing. Do not treat a prototype as production-ready unless that is explicitly the goal.

## 7. Build and gather feedback

> SDD 7/9: Building the next small improvement and gathering feedback before expanding the scope.

Implement the smallest useful next increment. After each functioning increment, proactively ask for feedback and compare it with the agreed assumptions and acceptance criteria. Repeat the prototype, feedback, and improvement loop as needed; the workflow is iterative, not a one-way march from spec to completion.

When a user proposes a decision that appears risky or likely to undermine the goal, give a brief nudge rather than silently complying or blocking:

> One concern: <specific risk>. An alternative is <alternative>. I recommend <recommendation> unless you have a reason to prefer the original.

Ask whether the user wants to keep the original decision. Record a consequential choice in `decisions/`.

Implement the accepted spec in small, reviewable increments. Prefer existing project conventions. Run the relevant tests after each meaningful increment and report failures plainly.

For high-risk work, pause before release for the review gate named in the spec. Check personal-data handling explicitly. Never commit secrets or data files. Before every push, inspect notebooks and clear output cells and tables derived from real records.

Ask before irreversible or destructive actions. Never delete a remote repository, branch, or release.

## 8. Validate a vertical slice

> SDD 8/9: Validating one thin, functioning path through the relevant system layers.

Implement or test a small traceable path through the relevant layers, such as interface, application logic, domain/model logic, persistence, and external integration. Prefer an end-to-end slice over a complete horizontal module. Use the result and the user's feedback to correct the spec or design before expanding the build. Repeat this stage within the iteration loop whenever a new risk or layer is introduced.

## Record decisions throughout

Create one `decisions/YYYY-MM-DD-<short-name>.md` for each non-obvious decision, including infrastructure choices, cost implications, and external service calls. Use the decision template:

- date
- decision
- reasoning
- alternatives rejected

Announce when a decision record is created. Do not create records for routine implementation details.

Before declaring completion, run the acceptance checks from the spec and repeat the vertical-slice test after the relevant implementation is complete.

Announce:

> SDD 9/9: Verifying acceptance criteria, the integrated slice, feedback, and recorded decisions.

Summarise what changed and what remains open, and point to the spec and decision records. For high-risk work, state whether the review gate passed, is pending, or was not applicable. Do not claim completion when verification was skipped.

Artifacts stay in English. Conversation may follow the user's language.
