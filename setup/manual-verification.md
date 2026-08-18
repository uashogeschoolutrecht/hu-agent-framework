# Manual Verification

Run these checks in a clean VS Code profile after the first push. They cannot be validated reliably from repository CI.

1. Enable `chat.plugins.enabled`.
2. Add `uashogeschoolutrecht/hu-agent-framework` to `chat.plugins.marketplaces`.
3. Install `hu-core` from the Extensions view.
4. Start Copilot Chat and confirm `/hu-core:get-started` appears and responds.
5. Open a throwaway project containing `.github/copilot/settings.json` from the template and confirm VS Code recommends the marketplace/plugin on the first chat message.
6. Install `hu-dsp` from the same marketplace and confirm both plugins are available.

7. Create an agent with `/hu-core:make-agent` in a throwaway project and confirm it appears as a selectable agent in Copilot Chat. The agent file location and extension are not yet confirmed against the current VS Code build. If the agent does not appear, check the VS Code agent documentation for the current path, then record the working location here and in `make-agent`.

If a marketplace entry does not appear, check the VS Code Agent Plugins output/log and verify whether the current build expects `.github/plugin/marketplace.json` or `.claude-plugin/marketplace.json`. Record the result in an issue before changing the manifest.
