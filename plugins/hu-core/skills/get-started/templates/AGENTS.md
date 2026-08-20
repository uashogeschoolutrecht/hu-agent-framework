# HU Project Instructions

Use the HU Agent Framework's spec-driven workflow. Start new work by orienting on environment, session scope, and risk, then write or update a spec before building.

Use reviewed university knowledge first, then applicable team knowledge, project instructions, and individual preferences. More specific guidance may refine or override university guidance marked `overridable: true`; it must not weaken protected university constraints.

Read `principles.md` at the project root, when it exists, before design and implementation choices. It records what this project stands for underneath the specification, and it is refined as the work proceeds rather than written once.

Project skills in `.github/skills/` are specific to this repository. Use the `hu-knowledge` skill to retrieve only relevant university context before making development decisions. The university knowledge catalog ships with the `hu-core` plugin; it is not stored in this repository.

## Guardrails

- Never commit secrets.
- Never commit data files.
- Before every push, clear notebook output cells and remove tables or plots derived from real records.
- Flag personal-data handling for review.
- Ask before irreversible or destructive actions.
- Never delete a remote repository, branch, or release.

Artifacts such as specs, decision records, and instruction files are written in English unless the user explicitly requests another language.
