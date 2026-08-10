# HU Agent Framework

The HU Agent Framework distributes reviewed Copilot skills and establishes a lightweight, spec-driven way of working with agents.

## Install

1. Enable `chat.plugins.enabled` in VS Code.
2. Add `uashogeschoolutrecht/hu-agent-framework` to `chat.plugins.marketplaces`.
3. Install the `hu-core` plugin.
4. Open a project and run `/hu-core:get-started`.

The plugin is in preview in VS Code. The first installation and workspace-recommendation path must be checked manually in a clean profile; see `setup/manual-verification.md`.

## Tiers

- `hu-core`: university-wide reviewed skills in this repository.
- `hu-dsp`: Data Science Pool skills in `hu-agent-framework-dsp`.
- Project skills: `.github/skills/` in the project repository.

Lower tiers take precedence when their instructions overlap. Plugins compose in VS Code, so the bootstrap `AGENTS.md` states this rule explicitly.

## Repository status

This is v1. The framework focuses on the get-started SDD workflow, project guardrails, skill sharing, and the plugin distribution pipe. Visualisation, analytics, richer decision records, and MCP servers are deferred.
