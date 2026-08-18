---
id: modular-programming
title: Modular Programming As A Design Ethic
kind: guidance
scope: university
owner: HU
status: approved
last_reviewed: 2026-08-18
review_due: 2027-02-18
overridable: true
source: Framework design ethic, approved for current framework scope; pending HU-wide review
---

# Modular Programming As A Design Ethic

Prefer a small number of cohesive modules with clear, understandable interfaces and limited dependencies. Keep closely related behaviour together. Avoid both opaque monoliths and unnecessary fragmentation.

This is a design ethic, not a requirement to split every program into many files or services. For a small script or exploratory analysis, a direct implementation may be the clearest and most maintainable choice.

## When to use it

Consider explicit module boundaries when a project has multiple concerns, data sources, consumers, deployment boundaries, or parts that will change independently. For each proposed module, explain:

- Its responsibility.
- What it exposes to other modules.
- What it depends on.
- Why the boundary makes the system easier to understand, test, change, or hand over.

Prefer interfaces that are small enough for a reviewer to understand. Keep dependencies visible and avoid interfaces that merely add indirection without hiding a meaningful change boundary.

## Agent guidance

Agents should challenge their own proposed design:

- Could two proposed modules be one simpler, cohesive unit?
- Does each boundary represent a real responsibility or change boundary?
- Can a future maintainer understand a module without reading the entire system?
- Would changing one data source require changes throughout the application?

Record module boundaries in the specification when they materially affect implementation. Do not introduce generic layers, factories, abstractions, or services only to satisfy this principle.
