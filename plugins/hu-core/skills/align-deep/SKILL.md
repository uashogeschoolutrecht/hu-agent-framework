---
name: align-deep
description: Reduce material uncertainty before specification when a HU project is big, risky, ambiguous, or likely to cause substantial rework. Invoked by get-started after quick alignment; not a standalone entry point.
owner: Data Science Pool
last_reviewed: 2026-08-18
---

# Deep Alignment

Use this after quick alignment when `get-started` identifies high risk, substantial uncertainty, a big session scope, multiple boundaries, or an explicit user request. It may also be used later when inspection or feedback reveals a material change in assumptions.

This is not a standalone entry point. If quick alignment has not run, run `align-quick` first; if the user has not started `get-started`, start there.

Deep alignment is not a fixed questionnaire. Ask only questions whose answers could change the problem, scope, risk, architecture, acceptance criteria, governance route, or delivery strategy. Ask one text-input question per response and give a recommended answer where useful.

## Explore as relevant

- The underlying problem and desired outcome.
- Primary and secondary users.
- Stakeholders and decision authority.
- Current situation and existing workarounds.
- Scope, non-goals, and boundaries.
- Constraints and dependencies.
- Data, privacy, security, and accessibility implications.
- Candidate alternatives and competing interpretations.
- Acceptance criteria and evidence of success.
- Failure modes and unresolved decisions.

Do not demand detailed technology choices before the problem and boundaries are understood. Do not repeat questions already answered during quick alignment or project inspection.

## Deep alignment packet

Maintain and present a concise packet containing:

- Goal and underlying problem.
- Desired and measurable outcomes.
- Users, stakeholders, and decision authority.
- Scope and explicit non-goals.
- Constraints and dependencies.
- Risk classification with reasons.
- Confirmed assumptions.
- Open questions and competing interpretations.
- Acceptance criteria or evidence still needed.
- Failure conditions.
- Decisions that must be recorded.

Ask the user to correct the packet before specification. Alignment is complete when the remaining uncertainty can safely be handled in the specification, implementation, or later feedback loop.

## Avoiding friction

Do not continue questioning to achieve a target number of questions. Stop when the material uncertainties are resolved. A small project may need only one or two deeper questions; a big project may need several rounds.

If the user explicitly requests quick alignment, respect that for low-risk work. Do not use it to bypass required privacy, security, safety, or governance clarification for high-risk work.
