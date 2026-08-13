---
id: "<NN>"
title: <short outcome>
type: implementation # implementation | validation
status: todo # todo | doing | blocked | done
depends_on: []
spec_requirements:
  - <requirement or acceptance criterion ID>
tests:
  sanity:
    - <command or precise local test>
  vertical_slice: []
execution:
  parallelizable: false
  allowed_paths: []
  forbidden_paths: []
  max_files_changed: 5
  worker_role: implementer # implementer | validator | reviewer
  model_tier: economical # economical | standard | advanced
---

# Task <NN>: <short outcome>

## Outcome

<What this task will make possible.>

## Scope

### In scope

- <bounded change>

### Out of scope

- <nearby work deliberately left for another task>

## Implementation Notes

<Relevant project conventions, files, interfaces, or assumptions.>

## Acceptance Criteria

- [ ] <observable criterion>

## Tests

### Sanity Check

<How this task's local behavior is checked.>

### Vertical Slice

<For implementation tasks: explain which later validation task will exercise this work, or why no slice is possible yet. For validation tasks: describe the end-to-end path and the test that proves the elements communicate.>

## Completion Log

- Started: not yet
- Completed: not yet
- Result: not yet
- Follow-up: none
