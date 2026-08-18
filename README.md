# HU Agent Framework

The HU Agent Framework distributes reviewed Copilot skills and establishes a lightweight, spec-driven way of working with agents.

## Install

1. Enable `chat.plugins.enabled` in VS Code.
2. Add `uashogeschoolutrecht/hu-agent-framework` to `chat.plugins.marketplaces`.
3. Install the `hu-core` plugin.
4. Open the project folder you want to work in.
5. Run `/hu-core:get-started`.

**Important:** start `get-started` only after opening the target project folder. VS Code resets the Copilot Chat conversation when you switch to another folder, so do not start the skill first and open the project during the same conversation. If the wrong folder is open, open the correct one and start the skill again.

The plugin is in preview in VS Code. The first installation and workspace-recommendation path must be checked manually in a clean profile; see `setup/manual-verification.md`.

## Knowledge and tiers

- `hu-core`: university-wide reviewed skills in this repository.
- `hu-dsp`: Data Science Pool skills in `hu-agent-framework-dsp`.
- University knowledge: reviewed, HU-wide reference material shipped with `hu-core` in [`plugins/hu-core/knowledge/`](plugins/hu-core/knowledge/).
- Project skills: `.github/skills/` in the project repository.
- Project agents: `.github/agents/<name>.agent.md` in the project repository.

Agents retrieve relevant university knowledge first, then apply team, project, and individual context. Lower levels may refine or override university guidance marked `overridable: true`; protected university constraints remain authoritative. Plugins compose in VS Code, so the bootstrap `AGENTS.md` states this rule explicitly.

The catalog is intentionally Git-backed and small. Add a focused Markdown document, register it in `plugins/hu-core/knowledge/index.json`, and submit it for review. Do not add team-specific or personal information to this repository.

## Repository status

This is v1. The framework focuses on the get-started SDD workflow, reviewed knowledge, project guardrails, authoring and sharing skills and agents, and the plugin distribution pipe. Visualisation, analytics, richer decision records, and MCP servers are deferred.

The get-started workflow is iterative: it aligns assumptions up front, decomposes agreed specifications into dependency-aware task files, then uses small prototypes, functioning vertical slices, and user feedback to improve the direction before expanding the build. Optional parallel execution uses human-approved, bounded waves with intermediate vertical-slice validation gates.

Alignment is proportional: `align-quick` establishes the minimum shared understanding by default, while `align-deep` is used when risk, scope, uncertainty, or an explicit user request justifies more questioning.

Authoring is standardised: `make-skill` and `make-agent` write new contributions from shared templates, and `share-contribution` checks one against the contribution standard before preparing a pull request. The standard lives in [`plugins/hu-core/knowledge/framework/contribution-standard.md`](plugins/hu-core/knowledge/framework/contribution-standard.md) so the three skills do not each restate the bar.

Future directions and open ideas are collected in [`docs/ideas.md`](docs/ideas.md).
