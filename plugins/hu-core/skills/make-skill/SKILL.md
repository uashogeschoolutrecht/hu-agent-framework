---
name: make-skill
description: Create a new HU skill, or improve an existing one, so it follows the framework's structure and triggers reliably. Use when the user wants to turn a repeated prompt, workflow, or piece of know-how into a reusable skill.
owner: Data Science Pool
last_reviewed: 2026-08-18
---

# Make Skill

Use this to write a skill that other people can install and a model can route to correctly. This skill creates and edits skill files. It does not share, promote, or open a pull request; `share-contribution` does that.

Read `../../knowledge/framework/contribution-standard.md` first. It defines the frontmatter contract, description rules, content rules, and safety bar. Follow it rather than inventing a local standard, and do not restate it back to the user.

## 1. Confirm a skill is the right shape

Apply the standard's skill/agent/knowledge test. If the need is behaviour, continue here. If it is a persistent role with distinct tool permissions, stop and use `make-agent`. If it is facts, guidance, templates, or examples, stop and tell the user it belongs in the knowledge catalog instead.

State which one you concluded and why, in one line, before continuing.

## 2. Establish the trigger

The description decides whether the skill ever fires, so settle it before writing the body. Ask only what you cannot infer:

1. What task should this handle, in one sentence?
2. What would a user be saying or doing when it should fire?
3. Who owns it for review?

Then check the trigger against what already exists. Read the descriptions of the other skills in this plugin and any project skills in `.github/skills/`. If the new description could match the same request as an existing skill, say so and resolve it: narrow one description, or extend the existing skill instead of adding a second one. Report the skill you compared against.

## 3. Write the skill

Create `.github/skills/<name>/SKILL.md` in the current project, using `templates/SKILL.md` beside this file. Use the project as the first home for a new skill; promotion to a team or university plugin happens later through `share-contribution`.

Do not overwrite an existing skill. When improving one, edit it in place and keep its `name`, then update `last_reviewed` to today.

Keep the body as short as the job allows. Add a numbered stage only when the order matters. Every skill needs a stopping condition and a statement of what to report.

## 4. Check it before handing it back

Verify against the standard and report each failure rather than fixing the author's intent silently:

- `name` is kebab-case and matches the directory.
- Description says what it does and when to use it, and is distinguishable from every skill you compared it against.
- If it is only ever invoked by another skill, the description says so and says it is not a standalone entry point.
- One job, with a stated stopping condition.
- No secrets, credentials, data, or hidden Unicode.
- Nothing restates a definition that the invoking skill already establishes.

## Output

Report the file path, the trigger you settled on, the skills you compared it against, and anything that still fails the standard. Tell the user the skill works in this project now, and that `share-contribution` is the way to offer it to the team or the university. Do not claim it has been reviewed or that it is available to anyone else.

Artifacts stay in English.
