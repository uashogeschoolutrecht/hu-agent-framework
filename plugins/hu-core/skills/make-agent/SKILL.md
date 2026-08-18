---
name: make-agent
description: Create a custom HU agent with a narrow role and an explicit tool allowlist. Use when a reusable role needs its own tool permissions or its own context, and a skill cannot express it.
owner: Data Science Pool
last_reviewed: 2026-08-18
---

# Make Agent

Use this to define an agent: a persistent role with its own tool permissions. This skill creates and edits agent files. It does not share or promote them; `share-contribution` does that.

Read `../../knowledge/framework/contribution-standard.md` first. It defines the frontmatter contract, description rules, content rules, and safety bar. Follow it rather than inventing a local standard, and do not restate it back to the user.

## 1. Establish that an agent is warranted

Most needs are skills. An agent is justified only when at least one of these holds, and you can say which:

- The work needs a different tool set than the user's normal session, usually narrower.
- The work needs its own context so it does not inherit or pollute the main conversation.
- The role coordinates other work across a whole session rather than handling one task.

If none holds, stop and use `make-skill`. State the reason you concluded either way in one line. Do not create an agent to make a skill feel more important.

## 2. Define the role and its limits

Ask only what you cannot infer:

1. What is this agent responsible for, and what is explicitly not its job?
2. Which tools does it genuinely need?
3. Who owns it for review?

Give the narrowest tool set that does the job. A reviewing or inspecting agent is read-only by default. Never grant destructive capability that the role does not need, and never grant an agent the ability to create further agents.

Use tool names exactly as they appear in agent files that already work, such as `read`, `search`, `search/codebase`, `execute`, and `editFiles`. Do not invent tool names; an unrecognised entry silently narrows or breaks the agent. If you need a tool you have not seen used, say so rather than guessing at its identifier.

## 3. Write the agent

Create `.github/agents/<name>.agent.md` in the current project, using `templates/AGENT.md` beside this file.

The `.agent.md` suffix is required. A plain `.md` file in that directory is not loaded as an agent. The `name` in frontmatter must match the filename without the `.agent.md` suffix.

Use the project as the first home; promotion into a team or university plugin happens later through `share-contribution`, which places the same file in `agents/` at the plugin root.

Set `description` to what the role is and when to select it, in one field. Set `argument-hint` when the agent expects a particular kind of opening request. Omit `model` unless the role genuinely needs a specific one, so the agent follows the user's own model choice.

Do not overwrite an existing agent. When improving one, edit it in place, keep its `name`, and update `last_reviewed` to today.

After writing, tell the user to open Copilot Chat and confirm the agent is selectable before relying on it. Writing the file is not evidence that it loaded.

## 4. Check it before handing it back

Verify against the standard and report each failure rather than repairing the author's intent silently:

- The filename ends in `.agent.md` and `name` matches the filename without that suffix.
- `name` is kebab-case with no namespace prefix.
- The description says what the role is and when to select it, and does not collide with an existing agent or skill.
- Responsibilities and non-responsibilities are both stated.
- Every tool in the list is one you have seen in use, is needed, and any destructive capability is justified in the file.
- No secrets, credentials, data, or hidden Unicode.

## Output

Report the file path, the role boundary, the tool allowlist with a reason for each entry, and the confirmation step the user still has to perform. Do not claim the agent is loaded, available, or reviewed.

Artifacts stay in English.
