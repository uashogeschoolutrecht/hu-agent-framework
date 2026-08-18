---
name: coordinate-tasks
description: Execute dependency-aware HU task files in human-approved, bounded waves using tightly scoped VS Code sub-agents. Use only when task files and an execution policy already exist; get-started invokes this when the policy enables sub-agents.
owner: Data Science Pool
last_reviewed: 2026-08-13
---

# Coordinate Tasks

Use this skill only after `plan-tasks` has created and validated the task files and `tasks/_execution-policy.md` exists. This skill is the only approved path for executing multiple task agents. It does not create new tasks, rewrite the specification, or silently increase concurrency.

## 1. Load the policy and graph

Read `tasks/_execution-policy.md` and every task file. Validate that:

- every dependency exists
- the graph has no cycles
- task statuses are consistent
- no task is marked `done` without a recorded test result
- `hard_max_workers` is exactly 4 or lower
- `max_workers` is between 1 and 4

If the policy is missing, malformed, or asks for more than 4 workers, stop and ask the user to resolve it.

If `use_subagents` is `false`, execute eligible tasks serially in dependency order. If it is `true`, continue with bounded waves.

## 2. Select a safe wave

A task is eligible only when every task in `depends_on` has `status: done`. Build a candidate wave from eligible `implementation` tasks, then remove tasks that:

- modify overlapping allowed paths
- modify the same public interface, schema, dependency file, configuration, fixture, or infrastructure
- require a shared mutable service
- have unclear or missing execution scope
- exceed the task's declared file-change limit

Never run `validation` tasks in parallel. Treat each validation task as a barrier that unlocks downstream work only after its test passes.

Set the actual worker count to the lowest of:

- the policy's `max_workers`
- the hard maximum of 4
- the number of safe candidate tasks

Report all four values before starting a wave: configured maximum, unblocked tasks, conflict-free tasks, and workers starting.

## 3. Ask for wave approval

Before starting every wave, show the user:

- task IDs and outcomes
- dependencies already satisfied
- files or paths each worker may change
- planned worker count and model tier
- tests each worker must run
- the validation gate that follows

Ask for approval. Do not start agents when approval is absent.

## 4. Run workers with bounded scope

Use VS Code's sub-agent capability only when it is available and the coordinator is allowed to invoke the named worker agent. Prefer isolated sessions or worktrees for parallel workers. If isolation is unavailable, execute the candidate tasks serially.

Each worker receives exactly one task file and must:

- inspect only the context needed for that task
- make the smallest correct change
- reuse existing patterns before adding abstractions or dependencies
- change only declared paths
- avoid unrelated refactors, documentation, upgrades, and cleanup
- run the task's sanity test
- stop when the acceptance criteria are met
- return a concise report containing files changed, tests run, result, and blocker

Workers may not create sub-agents, change task dependencies, alter the execution policy, or mark another task complete.

## 5. Close the wave

After workers finish:

- inspect every diff, including untracked files
- compare changed files with each task's allowed paths and file limit
- run the declared sanity tests again when practical
- mark a task `done` only when its acceptance criteria and tests pass
- mark failures `blocked` and record the reason
- stop all descendants of a failed task

Run the next eligible `validation` task serially. It must test the intended vertical slice and serve as the integration gate. Do not unlock downstream tasks until it passes.

Report the wave's worker count, changed-file count, tests, failures, retries, and unresolved work. Keep the report concise.

## 6. Cost and complexity controls

- Never exceed 4 workers.
- Never enable nested sub-agents.
- Never retry autonomously; a retry requires user approval.
- Stop after one failed retry of the same task or repeated identical failure.
- Prefer `economical` workers for narrow implementation tasks.
- Reserve `standard` or `advanced` work for coordination, integration failures, and review.
- Do not start a worker when the task is too small to justify a separate context.
- Require user approval before using external services or expensive tools.
- Do not use Autopilot or Bypass Approvals as part of this workflow.
- If the graph produces more than four safe candidates, process them in later waves.
- If review effort or conflicts grow beyond the value of parallelism, reduce the next wave to serial execution.

The coordinator must prefer less work over more work. Passing tests does not justify unrelated abstractions, broad refactors, or generated code outside the task scope.

## Output

Report the current wave, task statuses, validation result, changed files, tests, retries, and unresolved blockers. Do not claim completion while any required task or validation gate remains unfinished.

Artifacts stay in English.
