---
name: plan-tasks
description: Turn an agreed HU specification into small, dependency-aware task files with local tests and intermediate vertical-slice validation tasks.
owner: Data Science Pool
last_reviewed: 2026-08-13
---

# Plan Tasks

Use this skill after a specification has been agreed. This skill plans and records work; it does not implement tasks, start parallel agents, create worktrees, or modify source code.

## 1. Read the specification

Identify the requirements, acceptance criteria, first vertical slice, relevant system layers, existing project conventions, and explicit non-goals. For an existing project, preserve behavior that the specification says is unchanged.

If requirements, boundaries, or acceptance criteria are materially unclear, ask focused questions before creating task files. Do not invent technical decisions that belong in a decision record.

## 2. Choose task boundaries

Break the work into the smallest useful units that one agent can implement and review. A task should have one outcome, touch a limited set of files or responsibilities, and be verifiable without completing unrelated work.

Organize tasks around a traceable path through the system rather than only by technical layer. Typical groups may cover interface, application logic, domain or model logic, persistence, and external integration.

After a group establishes enough of a path to test communication between elements, add a dedicated `validation` task. A validation task is an intermediate gate: it tests a functioning vertical slice through the relevant layers and identifies integration problems before more work builds on top of them. Do not force every leaf task to own a full end-to-end test when the required layers do not exist yet.

## 3. Create task files

Create `tasks/` at the project root when it does not exist. Create one file per task using `templates/task.md` as the structure. Create `tasks/_execution-policy.md` using `templates/execution-policy.md` with the defaults `use_subagents: false` and `max_workers: 2`. Do not ask the user about sub-agents; change the defaults only on an explicit user request.

`tasks/<NN>-<slug>.md`

Use stable numeric IDs within the feature or project task set. Do not overwrite an existing task file. When extending existing work, use the next available IDs and preserve completed task history.

Each implementation task must include:

- a single outcome and a bounded scope
- the specification requirement it addresses
- explicit acceptance criteria
- one or more sanity-check tests for local behavior
- `depends_on`, with an empty list when it has no prerequisites
- a status of `todo` when first created
- execution scope, including whether it is safe to run in parallel, allowed paths, and a maximum file-change count

Each `validation` task must include:

- `type: validation`
- the tasks that establish its path in `depends_on`
- the layers and user or system path it checks
- an executable vertical-slice test, or a precise test plan when implementation is required before the test can run
- the failure boundary: what must be fixed before downstream tasks continue

Use `status: todo`, `status: doing`, `status: blocked`, or `status: done` as the task log. Only the agent or user executing a task may change its status from `todo`.

## 4. Check the dependency graph

Before reporting the plan as ready, inspect all task files and verify:

- every dependency ID exists
- no task depends on itself
- the graph has no dependency cycles
- every task is reachable from at least one task with no prerequisites
- validation tasks depend on the implementation tasks needed for their slice
- no task is needlessly blocked by an unrelated task
- every implementation task has a sanity-check test
- every validation task has a vertical-slice test or an explicitly recorded prerequisite for creating it
- the final acceptance checks are represented by one or more tasks

Report any unresolved dependency or test gap instead of silently repairing the specification.

Do not generate a parallel execution schedule yet. The dependency metadata is a future input to an orchestrator; this skill only records the graph in task files.

The execution policy is opt-in and is written from the defaults `use_subagents: false` and `max_workers: 2` without asking the user. It may enable sub-agents or request more than two workers only after an explicit user request, and the maximum value is always 4. Do not put cost estimates in the task files unless they are known; record actual usage in the execution report.

## Output

Report the task directory, the number and types of tasks created, the dependency roots and final validation tasks, and any unresolved questions. Do not claim that implementation or testing is complete.

Artifacts stay in English.
