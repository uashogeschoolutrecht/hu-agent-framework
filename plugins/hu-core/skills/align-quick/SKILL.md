---
name: align-quick
description: Establish the minimum shared understanding needed to start a HU project safely without creating unnecessary questioning friction. Invoked by get-started; not a standalone entry point.
owner: Data Science Pool
last_reviewed: 2026-08-18
---

# Quick Alignment

Use this as the default alignment mode at the start of `get-started`. If the user has not started `get-started`, start there instead of running this skill on its own. Do not inspect files, run commands, or explore the workspace before this alignment unless the user has already supplied the needed information.

## Questions

Ask one short text-input question per response and wait for the answer. Never show the user a list of upcoming questions. Skip questions the user has already answered.

1. What do you want to make or change?
2. What outcome would make this useful?
3. Who will use it or be affected by it?
4. What would make this unusable or a clear failure for you?

Then perform only a lightweight workspace check for clear project markers such as `.git`, source files, `AGENTS.md`, `specs/`, or `decisions/`. Do not perform a full inspection yet. If the folder already holds a project, say so before asking the structured questions.

Use the interactive question tool built into VS Code and the GitHub Copilot Chat plugin, `#vscode/askQuestions`, and invoke it once with these single-choice questions in one carousel:

- Will it handle sensitive data? Options: `No`, `Yes`, `Not sure`.
- Is the intended audience or user group sensitive? Options: `No`, `Yes`, `Not sure`. Explain only if needed that this includes students, minors, patients, identifiable research subjects, or the general public.
- If the workspace check found project markers: `I see this folder already holds a project — is this the project you want to work on?` Options: `Yes, this project`, `No, wrong folder`. Otherwise: `Is this a new project or a change to an existing project?` Options: `New project`, `Existing project`, `Not sure`.

Do not write these choices into the chat response or emulate the carousel with bullets. If the tool is unavailable, ask the same questions as separate plain-text questions, one per response, without listing the options. If the user's initial message already answers a question, skip it.

If the user answers `No, wrong folder`, stop the workflow and ask them to open the intended folder and start `get-started` again. Do not inspect or modify the current folder further.

Keep the exchange lightweight. Do not ask for a full specification, technical solution, architecture, or project-size label. Do not ask about sub-agents, workers, or execution policy; those defaults are set later without a question.

## Alignment packet

Summarise the following before continuing:

- Goal.
- Desired outcome.
- Users or affected people.
- Initial scope and obvious non-goals.
- Initial risk classification and reason.
- Load-bearing assumptions.
- One failure condition.
- Whether deep alignment is currently indicated.

Quick alignment is complete when the next inspection step is safe and no unresolved assumption is likely to invalidate it. Do not force deep alignment merely because the task is unfamiliar.

## Language and interaction

Use plain language such as “new project” and “existing project”. Do not use “greenfield” or “brownfield” in user-facing text. Announce the stage briefly and do not narrate file operations.
