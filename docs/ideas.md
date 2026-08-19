# Future Ideas

This document is an idea register for the HU Agent Framework. The items below are possibilities for future exploration, not commitments or part of the current release scope. An idea should become a specification, decision record, and task breakdown before implementation.

## Principles For Future Work

- Keep the framework easier than ad-hoc prompting.
- Make agent behavior visible and reviewable.
- Prefer local storage for personal, sensitive, or project-specific information.
- Keep user control over consequential actions, external services, and cost.
- Prefer a small number of dependable capabilities over a large collection of specialised agents.
- Prototype ideas with real HU work before making them framework-wide defaults.

## Local Memory For People

### Idea

Help people create and maintain agent memory on their own devices, or help them configure an existing local memory system through a dedicated setup skill or agent.

The memory could hold useful project context, preferences, recurring decisions, and working conventions without making that information part of a central HU service.

### Possible shape

- A `memory-setup` skill that detects the operating system, project location, and available local storage options.
- A guided setup that explains what will be stored, where it will be stored, and how to remove or export it.
- Project-scoped and personal-scoped memory kept separate.
- A visible local file or database rather than hidden agent state.
- Explicit commands for inspect, edit, export, reset, and delete.
- Optional adapters for local Markdown, SQLite, or an approved local memory tool.
- A policy that prevents sensitive project data from being uploaded to external endpoints by default.

### Benefits

- Gives people continuity between agent sessions.
- Keeps control of personal and project context on the person's device.
- Makes memory reviewable, portable, and easier to delete.
- Can reduce repeated orientation prompts and duplicated project explanations.

### Risks and open questions

- Local memory can still contain personal data, secrets, or confidential project information.
- Different operating systems and storage providers have different security and backup behavior.
- Memory can become stale and cause agents to make incorrect assumptions.
- The framework needs clear boundaries between user preferences, project facts, and temporary conversation context.
- Should memory be encrypted, and which encryption responsibility belongs to the framework versus the operating system?
- How should consent, retention, deletion, and sharing work when a project has multiple contributors?

## Testing Agents

### Idea

Create a small, controlled set of testing agents that validate agent-produced work from different perspectives without turning every task into a large review swarm.

### Possible roles

- **Sanity tester:** runs the narrow local checks belonging to one task.
- **Vertical-slice validator:** tests that the relevant layers communicate through one functioning path.
- **Acceptance tester:** checks the specification's acceptance criteria.
- **Scope reviewer:** checks changed files, unnecessary abstractions, and unrelated refactors.
- **Data and privacy reviewer:** checks sensitive-data handling and external service use.
- **Test-design reviewer:** identifies missing or weak tests without changing implementation code.

### Guardrails

- Use a fixed allowlist of testing agents rather than allowing arbitrary agent creation.
- Give read-only access to reviewers by default.
- Require an executable test command or a clearly recorded reason why a test cannot run.
- Keep testing agents focused on the assigned task or validation gate.
- Return concise findings with severity, evidence, and recommended next action.
- Do not allow testing agents to rewrite the specification or silently broaden scope.
- Run the smallest relevant test set before an expensive full-suite run.
- Use one primary validation agent first; add another perspective only when risk justifies it.

### Risks and open questions

- Multiple testing agents may duplicate findings and increase cost without increasing confidence.
- Agents may overfit to the tests they were asked to run and miss untested behavior.
- A reviewer that is allowed to edit code can blur the boundary between validation and implementation.
- Which checks should be mandatory for high-risk work, and which should remain optional?
- Should testing agents produce persistent reports, comments on task files, or both?

## Specialist Review Sub-Agents

### Idea

Develop a small, reviewed library of specialist sub-agents for tasks that benefit from a distinct perspective. These agents should primarily inspect, test, and advise; they should not become an automatic swarm that rewrites every result.

### Possible roles

- **Aesthetic and UX reviewer:** assesses visual hierarchy, interaction flow, accessibility, consistency, and whether a design choice supports the intended user task. It should distinguish structural UX problems from subjective visual preference and should not optimise for polish before the underlying flow works.
- **Code quality and readability reviewer:** checks naming, cohesion, duplication, unnecessary abstractions, complexity, error handling, and alignment with existing project conventions.
- **Security and privacy reviewer:** checks data exposure, authentication boundaries, secrets, unsafe dependencies, and external service usage.
- **Performance reviewer:** checks likely bottlenecks, unnecessary work, resource use, and whether performance claims are backed by measurements.
- **Documentation reviewer:** checks whether setup, behavior, assumptions, and operational constraints are clear without generating documentation that was not needed.
- **Accessibility reviewer:** checks keyboard use, semantics, contrast, screen-reader behavior, and inclusive interaction patterns where relevant.

### Operating model

- The coordinator selects a specialist only when the task, risk classification, or acceptance criteria justify it.
- Specialist reviewers receive the relevant task, specification, changed files, and explicit review questions rather than the whole project by default.
- Reviewers are read-only by default and return concise findings with severity, evidence, and recommended action.
- A primary reviewer runs first; additional perspectives are added only when their concerns are materially different.
- A specialist may recommend changes but must not silently expand scope, rewrite the task, or start another agent.
- Findings are classified as blocking defect, acceptance gap, important improvement, optional polish, or future idea.
- UX and aesthetic feedback is tied to the intended user outcome and agreed design criteria, not personal preference alone.
- Code-quality feedback must distinguish necessary simplification from broad refactoring.

### Guardrails

- Keep a fixed allowlist of reviewed specialist agents.
- Do not permit nested specialist agents.
- Run no more than one or two specialist reviews per wave unless a user approves more.
- Use economical models for narrow reviews where quality is sufficient.
- Do not run a specialist review when the task is too small to justify the context and cost.
- Require human review before a specialist finding changes scope or acceptance criteria.
- Keep specialist agents separate from implementation agents so recommendations remain independently reviewable.

### Risks and open questions

- Aesthetic reviewers may present subjective preferences as objective UX findings.
- Code-quality reviewers may encourage needless abstraction or refactoring.
- Multiple reviewers may produce conflicting advice and increase decision overhead.
- What evidence or design principles should the UX reviewer use for HU-specific contexts?
- Which specialist reviews should be mandatory for high-risk or public-facing work?
- Should review findings be stored in task files, a review report, or decision records?

## Convert Get Started Into An Agent

### Idea

Convert the current `get-started` skill into a custom VS Code agent, or provide an agent wrapper around the skill, so it can own the full workflow and coordinate the specialised skills more reliably.

### Possible shape

- Keep the current skill as the portable workflow definition.
- Add a user-invocable `HU Project Guide` agent that follows the workflow and invokes `plan-tasks` and `coordinate-tasks` when appropriate.
- Give the agent an explicit tool allowlist and a restricted sub-agent allowlist.
- Keep planning and inspection tools available before implementation tools.
- Require user confirmation at workspace, risk, execution-policy, wave, and release gates.
- Make the agent hand off to narrower worker or reviewer agents rather than implementing every task itself.
- Retain a skill-only fallback for environments where custom agents are unavailable.

### Benefits

- Gives the workflow a stable coordinator identity and clearer tool permissions.
- Makes sub-agent restrictions and worker roles easier to configure.
- Can reduce the chance that a model skips a workflow stage.
- Provides a natural place to manage session handoff and wave execution.

### Risks and open questions

- An agent wrapper may duplicate instructions already present in the skill.
- Custom-agent behavior can vary by VS Code and Copilot version.
- A more capable coordinator may become overbearing or ask too many questions.
- The framework must define which decisions belong to the agent and which always require the user.
- Should the agent be visible in the normal agent picker, or only be invoked by the HU command?
- What is the compatibility strategy when Agent Host or sub-agent tools are unavailable?

## Dependency Graph Visualisation

### Idea

Generate a readable dependency chart from the Markdown task files so people can see task waves, validation barriers, blocked descendants, and the critical path.

### Possible shape

- A generated `tasks/_graph.md` with Mermaid or plain-text diagrams.
- A summary of ready tasks, blocked tasks, validation gates, and dependency roots.
- A graph check that rejects missing dependencies and cycles.
- Regeneration after task planning and after status changes.

The chart should be a view of the task files, not a second source of truth.

## Deterministic Task Scheduler

### Idea

Replace or supplement model-led wave selection with a small deterministic scheduler that reads task metadata, computes ready waves, enforces concurrency, tracks retries, and records run history.

This should be considered only after the bounded coordinator has been used on real projects. It may be more reliable for repeated or larger workloads, but it would add maintenance and integration complexity.

## Execution Cost And Quality Reports

### Idea

Record lightweight execution metrics for each task and wave:

- worker count
- model tier
- elapsed time
- files changed
- tests run and results
- retries
- blocked descendants
- estimated or observed Copilot usage where available

Reports could identify whether parallel execution saves time or merely creates more review work. Exact token or credit accounting should only be reported when the hosting environment exposes reliable values.

## Richer Decision Records

### Idea

Extend decision records for consequential agent-workflow choices, including:

- execution policy changes
- model and worker-role choices
- external service calls
- local memory configuration
- data-retention decisions
- rejected implementation alternatives

Keep this proportional. Rich schemas and automated governance are useful only when they reduce uncertainty rather than turning every small task into administrative work.

## Evaluation And Manual Verification

### Idea

Create a repeatable evaluation pack for the framework itself, covering:

- empty-folder and existing-project classification
- sensitive-data and sensitive-user-group handling
- task decomposition quality
- dependency-cycle detection
- vertical-slice task placement
- worker-limit enforcement
- scope and unnecessary-code guardrails
- serial fallback when sub-agent or worktree support is unavailable

The evaluation pack should use representative toy projects and sanitized HU scenarios. It should test both artifact quality and observed agent behavior, especially with different Copilot models.
