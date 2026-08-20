---
name: refine-principles
description: Capture and sharpen the constraints and preferences underneath a user's stated goal into project principles, and apply them to design and implementation choices. Use during deep alignment, when the user gives evaluative feedback on a decision or design, or when they ask what the project stands for.
owner: Data Science Pool
last_reviewed: 2026-08-19
---

# Refine Principles

This skill owns `principles.md`: what belongs in it, how an entry earns its place, and how the agent applies it. Other skills decide when to invoke this one; they do not restate the method.

Principles are the reasons underneath the goal. They are hard to state on request, so they are inferred from what the user says, reacts to, and rejects, then tested rather than assumed.

## What is a principle

Two kinds, both of which rule something out:

- **Constraint** — something the project must never or always do. "Never surface raw student identifiers, even internally."
- **Preference** — a standing choice between competing goods. "Prefer something the team can modify themselves over something faster that only I can maintain."

Two things that are not principles:

- **An assumption** is a factual belief that could turn out false. It belongs in the specification's Assumptions section.
- **A goal** is what the work should achieve. It belongs in the specification. Do not restate goals here or `principles.md` becomes a second specification that drifts from the first.

If an entry could appear unchanged in an unrelated project, it is not a principle. Delete it.

## The file

`principles.md` at the project root, from `templates/principles.md` beside this file. Create it only when there is a first real entry; a task that produces none does not get an empty file.

Each entry states the principle as a heading, then:

- **Rules out** — what this forbids or rejects. An entry that cannot fill this line is not falsifiable. Delete it.
- **From** — the concrete moment it came from, with a date. A principle you cannot trace to something the user said, chose, or reacted to is one you invented. Do not write it.
- **Test** — for proposed entries only, a forward-looking prediction the user can disagree with.

Entries are `Held` or `Proposed`. A proposed entry becomes held when the user states it directly, or when its test correctly predicts a choice the user then endorses. Move it; do not silently promote it.

## Mode A: eliciting during alignment

Used when deep alignment is running. Work from what the user has already said rather than opening a new interview.

Ladder from a stated specific to the reason underneath it: take an attribute the user has asked for and ask why it matters, then why that matters, until you reach something that would still be true if the technology changed. Stop there. Two or three steps is usually enough; a fourth is usually you pushing.

Offer what you infer as a tentative hypothesis, stated specifically enough to be wrong: "I think you care more about the team being able to change this than about how quickly it ships — is that wrong?" A specific wrong guess produces a sharper correction than an open question, so prefer being precise and mistaken over being safe and vague.

When two things the user wants pull against each other, say so directly and ask which gives. That tension is usually where the real principle is.

## Mode B: reflecting on feedback

Used when the user reacts to something concrete. Only evaluative feedback carries a principle:

- **Evaluative** — a judgement about a choice. "I don't like that you split this into three files." "Good, that's the right level of abstraction." Reflect on this.
- **Corrective** — a report of a fact. "This crashes on empty input." "The column is named differently." There is no principle in this. Do not reflect; fix it.

For evaluative feedback, name the choice, state what you think it reveals about what the user wants in general, and give a test. Record it as proposed.

## Testing an inference

Do not ask whether a principle is right. People agree with plausible descriptions of themselves, and a confirmed invention is worse than no principle at all, because it then steers every later decision.

Ask a forward question instead: "If that holds, then when we add the next data source we should keep it in the same module rather than adding a layer. Is that what you'd want?" The user can disagree with a prediction in a way they cannot disagree with a flattering summary.

## Boundaries

Infer about the work, never about the person. Do not describe the user's feelings, motives, confidence, or competence, and do not offer interpretations of them. The subject is always what the system should do.

Principles sit at the project and individual level of the knowledge hierarchy. They may refine university guidance marked `overridable: true`. They can never weaken a protected university constraint on privacy, security, safety, legal, or governance grounds, regardless of what the user prefers. A user constraint is the user's to change; a protected university constraint is not.

## Applying principles to choices

Read `principles.md` before proposing architecture, module boundaries, technology, or an implementation approach, and prefer the option the held principles support.

When a choice conflicts with a held entry, surface it rather than complying silently:

- **Preference** — one line, then proceed with the user's answer. "This adds a build step only you can run, which cuts against preferring team-modifiable. Say if that is fine here."
- **Constraint** — stop and ask explicitly: "You recorded that as a constraint. Has that changed?" Wait for the answer. If they confirm the constraint, take the other route. If they set it aside, update or remove the entry with today's date and the reason, then continue.

Respect the user's answer either way. The file records what they decided, not what you would prefer.

## Stopping condition

Elicitation stops when the remaining unknowns are about facts rather than preferences. Reflection stops after the feedback in front of you has produced at most one new entry; do not mine one comment for several principles.

## Output

Report which entries were added, promoted, changed, or removed, and the test attached to anything proposed. Do not claim a proposed entry is settled, and do not report principles the user has not seen.

Artifacts stay in English.
