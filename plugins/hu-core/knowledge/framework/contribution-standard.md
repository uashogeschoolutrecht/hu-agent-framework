---
id: contribution-standard
title: HU Skill And Agent Contribution Standard
kind: policy
scope: university
owner: Data Science Pool
status: approved
last_reviewed: 2026-08-18
review_due: 2027-02-18
overridable: true
source: Framework contribution bar, approved for current framework scope
---

# HU Skill And Agent Contribution Standard

This is the single definition of what a good HU skill or agent looks like. `make-skill`, `make-agent`, and `share-contribution` all read this document instead of restating the bar. Change it here, not in a skill.

Teams may apply a lower bar to their own team-tier contributions. This bar applies to anything promoted into `hu-core`.

## Skill, agent, or knowledge

Choose one before writing anything:

- **Skill** — instructions for how an agent should behave during a task. Most contributions are skills.
- **Agent** — a persistent role with its own tool permissions that coordinates or performs a distinct kind of work across a whole session. Choose this only when a skill cannot express the need, usually because the work needs different tool access or a separate context.
- **Knowledge** — facts, guidance, templates, or examples that agents read. Never behaviour.

If a skill would do, write a skill. Do not create an agent to make a skill feel more important.

## Required frontmatter

Both skills and agents require `name`, `description`, `owner`, and `last_reviewed`. CI rejects anything missing these.

- `name` is plain kebab-case and matches its directory name for a skill, or its filename stem for an agent. Never add a namespace prefix; the plugin name becomes the command prefix automatically, and a manual prefix fails to load silently.
- `owner` is a team or role that can act on a review issue, not a placeholder.
- `last_reviewed` is `YYYY-MM-DD` and is the date a human actually read it.

## Description quality

The description is the only thing a model sees when deciding whether to invoke. It decides routing, so write it for that job:

- Say what it does, then when to use it.
- Make it distinguishable from every other skill in the plugin. If two descriptions could match the same request, one of them is wrong.
- A skill invoked only by another skill must say so and must state that it is not a standalone entry point. Otherwise it will fire on its own and skip everything its parent does first.
- Do not describe aspirations, tone, or quality. Describe the trigger.

## Content

- One job. A skill that does three unrelated things is three skills, or one skill that should not exist.
- A clear stopping condition. State when the work is done and what to report.
- Enough operational detail that a weaker model can follow it. Prefer checkable conditions over intentions.
- Define a concept once, in the skill that owns it. A skill invoked by another skill inherits its parent's context and must not restate definitions, limits, or vocabulary the parent has already established. Duplicated rules drift apart.
- Use the framework's existing vocabulary. Session scope is `small` or `big`. Risk is `low` or `high`. Do not use `greenfield` or `brownfield` in user-facing text.
- Artifacts stay in English. Conversation may follow the user's language.

## Safety and review

- No secrets, credentials, tokens, or data files.
- No hidden Unicode. Instructions must be visible and understandable to a human reviewer, because a skill runs in everyone's context.
- Answer the sensitive-data question honestly.
- An agent declares the narrowest tool set that does its job, and never requests destructive capability it does not need.
- It has been used on real work. An untested skill is a proposal, not a contribution.

## Review outcome

A contribution meets the bar when every point above holds. Report which points fail rather than repairing the author's intent silently. A human review and merge is always required; no automated check replaces it.
