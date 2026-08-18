# University Knowledge

This directory contains reviewed, HU-wide knowledge for agents. It is not a general document archive and must not contain team-specific or personal information.

## Add knowledge

1. Add one Markdown document below the appropriate topic directory.
2. Start it with the metadata fields used by the existing knowledge files.
3. Add an entry to `index.json`.
4. Include an authoritative source and a review date.
5. Submit the change for review. A document is not authoritative until it is merged.

Keep documents short and task-oriented. Prefer a few focused documents over one large handbook. Put instructions for agent behaviour in a `SKILL.md`; put facts, guidance, templates, and examples here.

## Authority

University documents establish the HU-wide baseline. Team, project, and individual guidance may provide more specific choices where a document is marked `overridable: true`. Documents marked `overridable: false` are protected constraints and cannot be weakened by lower-level instructions.

## Retrieval

Agents should use `index.json` to identify relevant documents before implementation. Retrieve only documents relevant to the task, and report the document IDs used when the knowledge materially affects a decision.
