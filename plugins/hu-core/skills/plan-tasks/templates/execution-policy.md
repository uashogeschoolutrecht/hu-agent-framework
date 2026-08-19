---
use_subagents: false
max_workers: 2
hard_max_workers: 4
approval_required_per_wave: true
allow_nested_subagents: false
allow_autonomous_retries: false
validation_tasks_parallel: false
---

# Task Execution Policy

This policy controls the optional bounded-wave execution of the task graph. It does not change task dependencies or permit work outside a task's declared scope.

## Defaults And Limits

- Sub-agents are disabled by default and are not asked about; they are enabled only when the user explicitly requests them.
- The default maximum is 2 workers.
- The hard maximum is 4 workers and cannot be overridden.
- The user must approve each execution wave.
- Nested sub-agents are disabled.
- Autonomous retries are disabled.
- Validation tasks run serially as dependency gates.

## User Decision

- Sub-agents: no (default; enabled only on an explicit user request)
- Worker limit: 2 (default; up to 4 on an explicit user request)
- Decision date: <YYYY-MM-DD>

## Notes

<Record only relevant constraints, such as shared infrastructure or a reason to keep execution serial.>
