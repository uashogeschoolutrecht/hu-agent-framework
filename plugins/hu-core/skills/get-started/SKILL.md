---
name: get-started
description: Start or continue a HU project using a risk-aware, spec-driven development workflow. Use when beginning a project, adding a feature, or asking how to run project work with the HU framework. For authoring or sharing a skill or agent, use make-skill, make-agent, or share-contribution instead.
owner: Data Science Pool
last_reviewed: 2026-08-13
---

# Get Started

Start this workflow only after the user has opened the folder they want to work in. VS Code resets the Copilot Chat conversation when the user switches folders. If no workspace is open, or the current workspace is clearly not the intended project, tell the user to open the correct folder and run this skill again; do not attempt to carry the workflow across that switch. Keep the conversation concise. Announce each SDD stage in one line, plus classifications, gates, decision records, and feedback loops. Do not narrate file operations.

## 1. Quick alignment before inspecting

Invoke `align-quick` as the default first step. It establishes the minimum shared understanding, performs the lightweight workspace check, and produces the initial alignment packet. Do not inspect files, run commands, or explore the workspace before quick alignment unless the user has already supplied the needed answers.

Announce:

> SDD 1/10: Understanding the goal before examining the project context.

## 2. Confirm the initial alignment

Announce:

> SDD 2/10: I understand the goal as <brief summary>. These are my working assumptions: <brief list>. Please correct anything important before I inspect the project.

The quick alignment packet is the shared baseline. Do not expand it into a full specification at this point.

## 3. Locate and inspect context

Only after the initial questioning and alignment, inspect the current workspace to confirm the situation:

- For a new project, treat the open folder as the project location and inspect what is already there.
- For a change to an existing project, inspect the open folder's files, structure, configuration, tests, and version-control state.
- If the current workspace is empty, treat it as a new project only after confirming that this is intentional.
- If the current workspace is not the project described by the user, stop and ask the user to open the target folder and run the skill again.

Announce:

> SDD 3/10: Locating the relevant project context and checking what already exists.

Do not switch folders during this workflow. Do not overwrite existing files.

Before making architecture or technology recommendations, use `hu-knowledge` when the task touches HU terminology, organizational context, standards, templates, or a recurring solution pattern. Retrieve the smallest relevant set of approved university documents, then inspect team and project guidance. Treat draft documents as unapproved context and report conflicts rather than silently resolving them.

## 4. Classify the work

Internally classify the project as new or existing from the user's intent and the inspected context. Do not expose the terms `greenfield` or `brownfield`. Infer session scope rather than asking the user to label it small or big. Use the goal, number of affected parts, existing complexity, integrations, uncertainty, and expected validation effort.

Announce the classification with its reasons and invite correction:

> SDD 4/10: This is a <new-project/existing-project> <small/big> session because <brief reasons>. You can correct that assessment before we continue.

Treat the scope as session-specific, not a permanent project label.

Classify risk as high when the work handles sensitive data, or when the intended audience or user group is sensitive: students, minors, patients, identifiable research subjects, or the general public. `align-quick` asks both questions. If either answer is yes, or either is unclear or was never answered, classify risk as high. State the result and reason, for example: “This uses student data, so risk is high; I’ll add a review step before we ship.” Let the user correct a classification before continuing. Cost and external service calls are not risk gates, but each requires a decision record.

## 4b. Escalate alignment when needed

Classify alignment uncertainty as low or high. Escalate to `align-deep` when risk is high, the work is big or spans multiple boundaries, material assumptions remain unresolved, competing interpretations are plausible, or the user explicitly requests deeper alignment. Otherwise continue with the quick alignment packet. Do not use project size alone as the trigger.

When escalating, announce:

> SDD 4b/10: This work has unresolved <risk, scope, or assumptions>, so I’m clarifying those before writing the specification.

Invoke `align-deep` before specification. It must not repeat questions already answered during quick alignment, inspection, or context retrieval.

## Bootstrap

If this is a new project, create these items from the templates beside this file:

- `AGENTS.md`
- `specs/`
- `decisions/`
- `.github/copilot/settings.json`

Do not overwrite existing files. If the project does not have a GitHub repository and the user asks for one, state the name, visibility, and organisation, then ask for confirmation before running `gh repo create`. Use the user's existing least-privilege authentication; never request administration or deletion capability.

The generated `AGENTS.md` is instruction-layer guidance, not a substitute for review or CI.

## 5. Specify

Announce:

> SDD 5/10: Turning the goal and project context into an agreed specification.

Read `principles.md` if it exists, and prefer the design and technology options its held entries support. The specification points at the file rather than restating its content.

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
- module boundaries when the work spans multiple concerns, consumers, data sources, or deployment boundaries; for a small script, state why a direct implementation is clearer
- iteration and feedback approach
- implementation notes, if they are already known

When proposing module boundaries, state each module's responsibility, interface, dependencies, and reason for the boundary. Challenge unnecessary fragmentation and generic layers. Do not create modules merely to increase file count. Keep this proportional to the work: a direct script may be the clearest design for a genuinely small or exploratory task.

Do not start implementation while requirements or acceptance criteria are materially unclear. Ask focused questions instead.

## 6. Decompose into tasks

Announce:

> SDD 6/10: Breaking the agreed specification into small, testable implementation tasks.

Invoke the reusable `plan-tasks` skill with the agreed specification. Create one `tasks/<NN>-<slug>.md` file per task at the project root. Do not overwrite existing task files; when continuing a feature, update only the task files that belong to that feature and preserve completed task history.

Every implementation task must:

- be small enough for one agent to complete and review
- have one clear outcome and explicit acceptance criteria
- include a sanity-check test for its local behavior
- declare `depends_on` task IDs, using an empty list when it has no prerequisites
- state which spec requirement it addresses

Group tasks by the path through the system rather than producing a purely horizontal list. Insert dedicated `validation` tasks after meaningful groups of implementation tasks. A validation task must depend on the tasks that establish its path and test that those elements communicate through the relevant layers. It may be the first task that proves a thin vertical slice; it is not a substitute for the final acceptance checks.

Before continuing, check that the task dependency graph has no cycles, every dependency exists, every task is reachable from a starting task, and each implementation task has a sanity test. Record the vertical-slice validation tasks explicitly in the task files. Do not implement tasks in this stage.

Create `tasks/_execution-policy.md` from the `plan-tasks` template using the defaults `use_subagents: false` and `max_workers: 2`. Do not ask the user about sub-agents. Change these values only when the user explicitly asks for sub-agent execution or a different worker count, and never write a `max_workers` value above 4. This records permission for a later execution stage; it does not start agents.

## 7. Prototype

This stage is active for every project. Keep it proportional to the inferred scope:

- For a small project, use the smallest useful prototype: a sketch, stub, spike, example interaction, or thin proof of the riskiest assumption.
- For a big project, prototype the uncertain or user-visible parts before committing to full implementation.
- Use the prototype to test understanding with the user and refine the spec, not merely to demonstrate generated code.
- Skip a separate prototype only when building the prototype is practically the same as building the whole small project. State that decision and why.

Announce:

> SDD 7/10: Prototyping the riskiest assumption so we can improve the direction before building further.

Show the prototype or a functioning thin example and proactively ask what the user would change, remove, or do differently. When the user judges a choice rather than reporting a fault, invoke `refine-principles`. If feedback materially changes the goal, users, boundaries, or assumptions, return to the alignment stage, restate the revised understanding, and update the spec's `Iterations / Feedback` section before continuing. Do not treat a prototype as production-ready unless that is explicitly the goal.

## 8. Build and gather feedback

> SDD 8/10: Building the next small improvement and gathering feedback before expanding the scope.

Implement the smallest useful next increment. After each functioning increment, proactively ask for feedback and compare it with the agreed assumptions and acceptance criteria. Repeat the prototype, feedback, and improvement loop as needed; the workflow is iterative, not a one-way march from spec to completion.

When the user's feedback judges a choice rather than reporting a fault, invoke `refine-principles`. A bug report is not a principle.

When `tasks/_execution-policy.md` enables sub-agents, invoke the reusable `coordinate-tasks` skill for implementation waves. Do not bypass that policy by launching workers directly. The coordinator must obtain approval before each wave, keep validation tasks serial, and apply the hard maximum of 4 workers.

When a user proposes a decision that appears risky or likely to undermine the goal, give a brief nudge rather than silently complying or blocking:

> One concern: <specific risk>. An alternative is <alternative>. I recommend <recommendation> unless you have a reason to prefer the original.

Ask whether the user wants to keep the original decision. Record a consequential choice in `decisions/`.

When the conflict is with a held entry in `principles.md` rather than a general risk, use `refine-principles` for the wording; it is a lighter touch for a preference and an explicit question for a constraint.

Implement the accepted spec in small, reviewable increments. Prefer existing project conventions. Run the relevant tests after each meaningful increment and report failures plainly.

For high-risk work, pause before release for the review gate named in the spec. Check personal-data handling explicitly. Never commit secrets or data files. Before every push, inspect notebooks and clear output cells and tables derived from real records.

Ask before irreversible or destructive actions. Never delete a remote repository, branch, or release.

## 9. Validate a vertical slice

> SDD 9/10: Validating one thin, functioning path through the relevant system layers.

Implement or test a small traceable path through the relevant layers, such as interface, application logic, domain/model logic, persistence, and external integration. Prefer an end-to-end slice over a complete horizontal module. Use the result and the user's feedback to correct the spec or design before expanding the build. Repeat this stage within the iteration loop whenever a new risk or layer is introduced.

## Record decisions throughout

Create one `decisions/YYYY-MM-DD-<short-name>.md` for each non-obvious decision, including infrastructure choices, cost implications, and external service calls. Use the decision template:

- date
- decision
- reasoning
- alternatives rejected
- the principle it serves, when `principles.md` has a relevant entry

Announce when a decision record is created. Do not create records for routine implementation details. If a decision contradicts a held principle, that is a signal that either the decision or the principle is wrong; raise it rather than recording both.

Before declaring completion, run the acceptance checks from the spec and repeat the vertical-slice test after the relevant implementation is complete.

Announce:

> SDD 10/10: Verifying acceptance criteria, the integrated slice, feedback, task status, and recorded decisions.

Summarise what changed and what remains open, and point to the spec and decision records. For high-risk work, state whether the review gate passed, is pending, or was not applicable. Do not claim completion when verification was skipped.

Artifacts stay in English. Conversation may follow the user's language.
