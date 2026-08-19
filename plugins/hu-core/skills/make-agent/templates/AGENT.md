---
name: <kebab-case-name-matching-the-filename-without-.agent.md>
description: '<What this role is and when to select it. Distinguish it from every other agent and skill.>'
argument-hint: <What a useful opening request looks like. Delete this line when the agent does not expect one.>
tools: ['read', 'search']
owner: <team or role that can act on a review issue>
last_reviewed: <YYYY-MM-DD>
---

# <Title Case Role>

<What this agent is responsible for, in one or two sentences.>

## Not this agent's job

<What it must hand back rather than do. An agent without stated limits absorbs neighbouring work.>

## How it works

<The role's approach. Prefer checkable conditions over intentions. Keep it short enough that a reviewer can hold the whole role in mind.>

## Limits

- <Why each granted tool is needed, especially any that changes or deletes something. Read-only roles keep to `read` and `search`.>
- Does not create other agents.
- Does not change scope, acceptance criteria, or another task's status.
- Asks before irreversible or destructive actions.

## Output

<What it reports back, and what it must not claim.>

Artifacts stay in English.
