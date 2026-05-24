# Cursor Docs Readme Summary

This folder contains beginner-friendly explanations of Cursor documentation topics. The readmes are organized as short teaching notes that explain what each feature is, why it matters, how to use it, and what a beginner should remember.

## What This Collection Covers

The readmes cover the full Cursor product surface:

- **Getting started:** Cursor overview, quickstart workflow, and changelog context.
- **Models and pricing:** model selection, pricing behavior, Composer, Claude, GPT, Gemini, Grok, and Codex model notes.
- **Agent workflows:** Agent overview, Plan mode, Debug mode, Agent review, tools, prompting, checkpoints, security, and worktrees.
- **Customization:** plugins, rules, skills, subagents, hooks, and MCP.
- **Cloud Agent:** setup, capabilities, automations, machines, settings, networking, API endpoints, and best practices.
- **Developer tooling:** Cursor CLI, headless mode, shell mode, ACP, CLI references, TypeScript SDK, and deeplinks.
- **Integrations:** Slack, Microsoft Teams, Jira, Linear, GitHub, GitLab, JetBrains, Xcode, and Cursor Blame.
- **Teams and account management:** team setup, pricing, members, SSO, dashboard, analytics, SCIM, and enterprise billing groups.
- **Enterprise:** identity, privacy, governance, network configuration, LLM safety, pooled usage, compliance, deployment, service accounts, and BAA guidance.

## Recommended Reading Paths

### Beginner Path

Start here if you are new to Cursor:

1. [001-docs.md](001-docs.md) - high-level overview of Cursor.
2. [002-docs-get-started-quickstart.md](002-docs-get-started-quickstart.md) - first practical workflow.
3. [012-docs-agent-overview.md](012-docs-agent-overview.md) - how Cursor Agent works.
4. [017-docs-agent-prompting.md](017-docs-agent-prompting.md) - how to ask better questions.
5. [026-docs-rules.md](026-docs-rules.md) - how to make Cursor follow project guidance.

### Agent Power User Path

Use this path to learn how to run real coding workflows with Agent:

1. [012-docs-agent-overview.md](012-docs-agent-overview.md)
2. [016-docs-agent-plan-mode.md](016-docs-agent-plan-mode.md)
3. [018-docs-agent-debug-mode.md](018-docs-agent-debug-mode.md)
4. [015-docs-agent-agent-review.md](015-docs-agent-agent-review.md)
5. [019-docs-agent-tools-terminal.md](019-docs-agent-tools-terminal.md)
6. [021-docs-agent-tools-search.md](021-docs-agent-tools-search.md)
7. [024-docs-agent-security.md](024-docs-agent-security.md)

### Automation and CLI Path

Use this path if you want Cursor outside the editor:

1. [052-docs-cli-overview.md](052-docs-cli-overview.md)
2. [053-docs-cli-installation.md](053-docs-cli-installation.md)
3. [054-docs-cli-using.md](054-docs-cli-using.md)
4. [057-docs-cli-headless.md](057-docs-cli-headless.md)
5. [059-docs-cli-reference-parameters.md](059-docs-cli-reference-parameters.md)
6. [060-docs-cli-reference-authentication.md](060-docs-cli-reference-authentication.md)
7. [051-docs-sdk-typescript.md](051-docs-sdk-typescript.md)

### Admin and Enterprise Path

Use this path for team rollout, compliance, and governance:

1. [063-docs-account-teams-setup.md](063-docs-account-teams-setup.md)
2. [065-docs-account-teams-members.md](065-docs-account-teams-members.md)
3. [066-docs-account-teams-sso.md](066-docs-account-teams-sso.md)
4. [069-docs-enterprise.md](069-docs-enterprise.md)
5. [070-docs-enterprise-identity-and-access-management.md](070-docs-enterprise-identity-and-access-management.md)
6. [072-docs-enterprise-privacy-and-data-governance.md](072-docs-enterprise-privacy-and-data-governance.md)
7. [073-docs-enterprise-network-configuration.md](073-docs-enterprise-network-configuration.md)
8. [077-docs-enterprise-compliance-and-monitoring.md](077-docs-enterprise-compliance-and-monitoring.md)

## Topic Summary

### Core Cursor Concepts

These files introduce Cursor as an AI-powered code editor, explain how beginners should start, and provide release/change context.

- [001-docs.md](001-docs.md) - explains what Cursor is, what it can do, and how its main documentation areas fit together.
- [002-docs-get-started-quickstart.md](002-docs-get-started-quickstart.md) - walks through installing Cursor, opening a project, asking Agent to explain code, making a change, and reviewing results.
- [011-changelog.md](011-changelog.md) - summarizes product changes and release notes.

### Models and Pricing

These files explain Cursor model choices, usage costs, and the strengths of specific model families.

- [003-docs-models-and-pricing.md](003-docs-models-and-pricing.md) - explains available models, pricing concepts, usage, and selection tradeoffs.
- [004-docs-models-claude-4-6-sonnet.md](004-docs-models-claude-4-6-sonnet.md) - covers Claude 4.6 Sonnet.
- [005-docs-models-claude-opus-4-7.md](005-docs-models-claude-opus-4-7.md) - covers Claude Opus 4.7.
- [006-docs-models-gemini-3-1-pro.md](006-docs-models-gemini-3-1-pro.md) - covers Gemini 3.1 Pro.
- [007-docs-models-gpt-5-5.md](007-docs-models-gpt-5-5.md) - covers GPT-5.5.
- [008-docs-models-gpt-5-3-codex.md](008-docs-models-gpt-5-3-codex.md) - covers GPT-5.3 Codex.
- [009-docs-models-grok-4-3.md](009-docs-models-grok-4-3.md) - covers Grok 4.3.
- [010-docs-models-cursor-composer-2-5.md](010-docs-models-cursor-composer-2-5.md) - explains Cursor Composer 2.5.

### Agent, Tools, and Security

These files explain Cursor Agent as the main autonomous coding workflow, including modes, tools, review, prompting, and safety controls.

- [012-docs-agent-overview.md](012-docs-agent-overview.md) - introduces Agent, its tools, checkpoints, queued messages, shortcuts, and beginner best practices.
- [013-docs-agent-agents-window.md](013-docs-agent-agents-window.md) - explains the Agents window for tracking and managing Agent work.
- [014-docs-agent-overview-duplicate-capture.md](014-docs-agent-overview-duplicate-capture.md) - alternate captured version of the Agent overview.
- [015-docs-agent-agent-review.md](015-docs-agent-agent-review.md) - explains Agent Review for checking changes and catching issues.
- [016-docs-agent-plan-mode.md](016-docs-agent-plan-mode.md) - explains Plan mode for designing changes before implementation.
- [017-docs-agent-prompting.md](017-docs-agent-prompting.md) - teaches effective prompting patterns for Agent.
- [018-docs-agent-debug-mode.md](018-docs-agent-debug-mode.md) - explains Debug mode for systematic troubleshooting.
- [019-docs-agent-tools-terminal.md](019-docs-agent-tools-terminal.md) - explains how Agent uses the terminal.
- [020-docs-agent-tools-browser.md](020-docs-agent-tools-browser.md) - explains browser tooling for web-based inspection and workflows.
- [021-docs-agent-tools-search.md](021-docs-agent-tools-search.md) - explains search tools for understanding a codebase.
- [022-docs-agent-tools-canvas.md](022-docs-agent-tools-canvas.md) - explains Canvas as a visual companion for richer artifacts.
- [023-docs-configuration-worktrees.md](023-docs-configuration-worktrees.md) - explains worktree configuration for isolated work.
- [024-docs-agent-security.md](024-docs-agent-security.md) - explains Agent security controls, permissions, and safe operation.

### Customization and Extensibility

These files explain how to tailor Cursor to a team, repository, or repeated workflow.

- [025-docs-plugins.md](025-docs-plugins.md) - explains plugins and how they extend Cursor.
- [026-docs-rules.md](026-docs-rules.md) - explains Cursor rules for project-specific instructions.
- [027-docs-rules.md](027-docs-rules.md) - additional rules documentation capture.
- [028-docs-skills.md](028-docs-skills.md) - explains skills as reusable task instructions.
- [029-docs-subagents.md](029-docs-subagents.md) - explains subagents for delegating specialized work.
- [030-docs-hooks.md](030-docs-hooks.md) - explains hooks for automating behavior around Agent events.
- [031-docs-mcp.md](031-docs-mcp.md) - explains MCP servers and external tool integrations.

### Cloud Agent, Bugbot, and Security Review

These files explain remote Agent execution, Cloud Agent setup, automation, and review/security workflows.

- [032-docs-cloud-agent.md](032-docs-cloud-agent.md) - introduces Cloud Agent.
- [033-docs-cloud-agent-setup.md](033-docs-cloud-agent-setup.md) - explains Cloud Agent setup.
- [034-docs-cloud-agent-capabilities.md](034-docs-cloud-agent-capabilities.md) - summarizes Cloud Agent capabilities.
- [035-docs-cloud-agent-my-machines.md](035-docs-cloud-agent-my-machines.md) - explains machine management.
- [036-docs-cloud-agent-self-hosted-pool.md](036-docs-cloud-agent-self-hosted-pool.md) - explains self-hosted Cloud Agent pools.
- [037-docs-bugbot.md](037-docs-bugbot.md) - explains Bugbot for automated bug detection and triage.
- [038-docs-security-review.md](038-docs-security-review.md) - explains security review workflows.
- [039-docs-cloud-agent-automations.md](039-docs-cloud-agent-automations.md) - explains automations for Cloud Agent.
- [040-docs-cloud-agent-best-practices.md](040-docs-cloud-agent-best-practices.md) - collects best practices for Cloud Agent use.
- [041-docs-cloud-agent-security-network.md](041-docs-cloud-agent-security-network.md) - explains security and network considerations.
- [042-docs-cloud-agent-settings.md](042-docs-cloud-agent-settings.md) - explains Cloud Agent settings.
- [043-docs-cloud-agent-api-endpoints.md](043-docs-cloud-agent-api-endpoints.md) - documents API endpoints for Cloud Agent workflows.

### Integrations, SDK, and CLI

These files explain how Cursor connects to external developer tools and how to use Cursor from the command line or code.

- [044-docs-integrations-slack.md](044-docs-integrations-slack.md) - explains Slack integration.
- [045-docs-integrations-linear.md](045-docs-integrations-linear.md) - explains Linear integration.
- [046-docs-integrations-github.md](046-docs-integrations-github.md) - explains GitHub integration.
- [047-docs-integrations-gitlab.md](047-docs-integrations-gitlab.md) - explains GitLab integration.
- [048-docs-integrations-jetbrains.md](048-docs-integrations-jetbrains.md) - explains JetBrains integration.
- [049-docs-integrations-xcode.md](049-docs-integrations-xcode.md) - explains Xcode integration.
- [050-docs-reference-deeplinks.md](050-docs-reference-deeplinks.md) - explains Cursor deeplinks.
- [051-docs-sdk-typescript.md](051-docs-sdk-typescript.md) - explains the Cursor TypeScript SDK.
- [052-docs-cli-overview.md](052-docs-cli-overview.md) - introduces Cursor CLI.
- [053-docs-cli-installation.md](053-docs-cli-installation.md) - explains CLI installation.
- [054-docs-cli-using.md](054-docs-cli-using.md) - explains everyday CLI usage.
- [055-docs-cli-shell-mode.md](055-docs-cli-shell-mode.md) - explains CLI shell mode.
- [056-docs-cli-acp.md](056-docs-cli-acp.md) - explains ACP usage with the CLI.
- [057-docs-cli-headless.md](057-docs-cli-headless.md) - explains headless CLI workflows for scripts and CI.
- [058-docs-cli-reference-slash-commands.md](058-docs-cli-reference-slash-commands.md) - lists CLI slash commands.
- [059-docs-cli-reference-parameters.md](059-docs-cli-reference-parameters.md) - lists CLI parameters, flags, and commands.
- [060-docs-cli-reference-authentication.md](060-docs-cli-reference-authentication.md) - explains CLI authentication.
- [061-docs-cli-reference-permissions.md](061-docs-cli-reference-permissions.md) - explains CLI permissions.
- [062-docs-cli-reference-configuration.md](062-docs-cli-reference-configuration.md) - explains CLI configuration files and environment variables.
- [082-docs-integrations-cursor-blame.md](082-docs-integrations-cursor-blame.md) - explains Cursor Blame for understanding AI-generated code attribution.

### Teams and Account Administration

These files explain team setup, billing, membership, access control, and analytics.

- [063-docs-account-teams-setup.md](063-docs-account-teams-setup.md) - explains creating and setting up a team.
- [064-docs-account-teams-pricing.md](064-docs-account-teams-pricing.md) - explains team pricing, included usage, and spend controls.
- [065-docs-account-teams-members.md](065-docs-account-teams-members.md) - explains members, roles, invitations, billing rules, and deletion.
- [066-docs-account-teams-sso.md](066-docs-account-teams-sso.md) - explains SSO setup and troubleshooting.
- [067-docs-account-teams-dashboard.md](067-docs-account-teams-dashboard.md) - explains the team dashboard.
- [068-docs-account-teams-analytics.md](068-docs-account-teams-analytics.md) - explains team analytics, exports, filters, and metrics.
- [071-docs-account-teams-scim.md](071-docs-account-teams-scim.md) - explains SCIM provisioning and group management.
- [081-docs-account-enterprise-billing-groups.md](081-docs-account-enterprise-billing-groups.md) - explains enterprise billing groups.

### Enterprise, Governance, and Compliance

These files explain Cursor deployment and governance for larger organizations.

- [069-docs-enterprise.md](069-docs-enterprise.md) - introduces enterprise features and documentation topics.
- [070-docs-enterprise-identity-and-access-management.md](070-docs-enterprise-identity-and-access-management.md) - explains SSO, SCIM, RBAC, MDM, workspace trust, and allowed extensions.
- [072-docs-enterprise-privacy-and-data-governance.md](072-docs-enterprise-privacy-and-data-governance.md) - explains indexing, LLM requests, Cloud Agent data flows, privacy mode, contracts, and encryption.
- [073-docs-enterprise-network-configuration.md](073-docs-enterprise-network-configuration.md) - explains proxies, SSL inspection, DLP, IP allowlisting, VPC peering, encryption, LLM gateways, and networking.
- [074-docs-enterprise-llm-safety-and-controls.md](074-docs-enterprise-llm-safety-and-controls.md) - explains deterministic controls, LLM steering, and safety policy examples.
- [075-docs-enterprise-model-and-integration-management.md](075-docs-enterprise-model-and-integration-management.md) - explains model access, BYOK controls, MCP trust, allowlists, repository blocklists, and integrations.
- [076-docs-enterprise-pooled-usage.md](076-docs-enterprise-pooled-usage.md) - explains pooled usage and spend controls.
- [077-docs-enterprise-compliance-and-monitoring.md](077-docs-enterprise-compliance-and-monitoring.md) - explains audit logs, streaming logs, hooks, certifications, and disclosure.
- [078-docs-enterprise-baa.md](078-docs-enterprise-baa.md) - explains BAAs and use of Cursor with PHI.
- [079-docs-enterprise-deployment-patterns.md](079-docs-enterprise-deployment-patterns.md) - explains MDM, Windows Group Policy, installers, macOS profiles, Linux policy files, updates, CLI deployment, and troubleshooting.
- [080-docs-account-enterprise-service-accounts.md](080-docs-account-enterprise-service-accounts.md) - explains service accounts, API keys, CLI usage, rotation, and best practices.

## Complete Index by Number

- [001-docs.md](001-docs.md)
- [002-docs-get-started-quickstart.md](002-docs-get-started-quickstart.md)
- [003-docs-models-and-pricing.md](003-docs-models-and-pricing.md)
- [004-docs-models-claude-4-6-sonnet.md](004-docs-models-claude-4-6-sonnet.md)
- [005-docs-models-claude-opus-4-7.md](005-docs-models-claude-opus-4-7.md)
- [006-docs-models-gemini-3-1-pro.md](006-docs-models-gemini-3-1-pro.md)
- [007-docs-models-gpt-5-5.md](007-docs-models-gpt-5-5.md)
- [008-docs-models-gpt-5-3-codex.md](008-docs-models-gpt-5-3-codex.md)
- [009-docs-models-grok-4-3.md](009-docs-models-grok-4-3.md)
- [010-docs-models-cursor-composer-2-5.md](010-docs-models-cursor-composer-2-5.md)
- [011-changelog.md](011-changelog.md)
- [012-docs-agent-overview.md](012-docs-agent-overview.md)
- [013-docs-agent-agents-window.md](013-docs-agent-agents-window.md)
- [014-docs-agent-overview-duplicate-capture.md](014-docs-agent-overview-duplicate-capture.md)
- [015-docs-agent-agent-review.md](015-docs-agent-agent-review.md)
- [016-docs-agent-plan-mode.md](016-docs-agent-plan-mode.md)
- [017-docs-agent-prompting.md](017-docs-agent-prompting.md)
- [018-docs-agent-debug-mode.md](018-docs-agent-debug-mode.md)
- [019-docs-agent-tools-terminal.md](019-docs-agent-tools-terminal.md)
- [020-docs-agent-tools-browser.md](020-docs-agent-tools-browser.md)
- [021-docs-agent-tools-search.md](021-docs-agent-tools-search.md)
- [022-docs-agent-tools-canvas.md](022-docs-agent-tools-canvas.md)
- [023-docs-configuration-worktrees.md](023-docs-configuration-worktrees.md)
- [024-docs-agent-security.md](024-docs-agent-security.md)
- [025-docs-plugins.md](025-docs-plugins.md)
- [026-docs-rules.md](026-docs-rules.md)
- [027-docs-rules.md](027-docs-rules.md)
- [028-docs-skills.md](028-docs-skills.md)
- [029-docs-subagents.md](029-docs-subagents.md)
- [030-docs-hooks.md](030-docs-hooks.md)
- [031-docs-mcp.md](031-docs-mcp.md)
- [032-docs-cloud-agent.md](032-docs-cloud-agent.md)
- [033-docs-cloud-agent-setup.md](033-docs-cloud-agent-setup.md)
- [034-docs-cloud-agent-capabilities.md](034-docs-cloud-agent-capabilities.md)
- [035-docs-cloud-agent-my-machines.md](035-docs-cloud-agent-my-machines.md)
- [036-docs-cloud-agent-self-hosted-pool.md](036-docs-cloud-agent-self-hosted-pool.md)
- [037-docs-bugbot.md](037-docs-bugbot.md)
- [038-docs-security-review.md](038-docs-security-review.md)
- [039-docs-cloud-agent-automations.md](039-docs-cloud-agent-automations.md)
- [040-docs-cloud-agent-best-practices.md](040-docs-cloud-agent-best-practices.md)
- [041-docs-cloud-agent-security-network.md](041-docs-cloud-agent-security-network.md)
- [042-docs-cloud-agent-settings.md](042-docs-cloud-agent-settings.md)
- [043-docs-cloud-agent-api-endpoints.md](043-docs-cloud-agent-api-endpoints.md)
- [044-docs-integrations-slack.md](044-docs-integrations-slack.md)
- [045-docs-integrations-linear.md](045-docs-integrations-linear.md)
- [046-docs-integrations-github.md](046-docs-integrations-github.md)
- [047-docs-integrations-gitlab.md](047-docs-integrations-gitlab.md)
- [048-docs-integrations-jetbrains.md](048-docs-integrations-jetbrains.md)
- [049-docs-integrations-xcode.md](049-docs-integrations-xcode.md)
- [050-docs-reference-deeplinks.md](050-docs-reference-deeplinks.md)
- [051-docs-sdk-typescript.md](051-docs-sdk-typescript.md)
- [052-docs-cli-overview.md](052-docs-cli-overview.md)
- [053-docs-cli-installation.md](053-docs-cli-installation.md)
- [054-docs-cli-using.md](054-docs-cli-using.md)
- [055-docs-cli-shell-mode.md](055-docs-cli-shell-mode.md)
- [056-docs-cli-acp.md](056-docs-cli-acp.md)
- [057-docs-cli-headless.md](057-docs-cli-headless.md)
- [058-docs-cli-reference-slash-commands.md](058-docs-cli-reference-slash-commands.md)
- [059-docs-cli-reference-parameters.md](059-docs-cli-reference-parameters.md)
- [060-docs-cli-reference-authentication.md](060-docs-cli-reference-authentication.md)
- [061-docs-cli-reference-permissions.md](061-docs-cli-reference-permissions.md)
- [062-docs-cli-reference-configuration.md](062-docs-cli-reference-configuration.md)
- [063-docs-account-teams-setup.md](063-docs-account-teams-setup.md)
- [064-docs-account-teams-pricing.md](064-docs-account-teams-pricing.md)
- [065-docs-account-teams-members.md](065-docs-account-teams-members.md)
- [066-docs-account-teams-sso.md](066-docs-account-teams-sso.md)
- [067-docs-account-teams-dashboard.md](067-docs-account-teams-dashboard.md)
- [068-docs-account-teams-analytics.md](068-docs-account-teams-analytics.md)
- [069-docs-enterprise.md](069-docs-enterprise.md)
- [070-docs-enterprise-identity-and-access-management.md](070-docs-enterprise-identity-and-access-management.md)
- [071-docs-account-teams-scim.md](071-docs-account-teams-scim.md)
- [072-docs-enterprise-privacy-and-data-governance.md](072-docs-enterprise-privacy-and-data-governance.md)
- [073-docs-enterprise-network-configuration.md](073-docs-enterprise-network-configuration.md)
- [074-docs-enterprise-llm-safety-and-controls.md](074-docs-enterprise-llm-safety-and-controls.md)
- [075-docs-enterprise-model-and-integration-management.md](075-docs-enterprise-model-and-integration-management.md)
- [076-docs-enterprise-pooled-usage.md](076-docs-enterprise-pooled-usage.md)
- [077-docs-enterprise-compliance-and-monitoring.md](077-docs-enterprise-compliance-and-monitoring.md)
- [078-docs-enterprise-baa.md](078-docs-enterprise-baa.md)
- [079-docs-enterprise-deployment-patterns.md](079-docs-enterprise-deployment-patterns.md)
- [080-docs-account-enterprise-service-accounts.md](080-docs-account-enterprise-service-accounts.md)
- [081-docs-account-enterprise-billing-groups.md](081-docs-account-enterprise-billing-groups.md)
- [082-docs-integrations-cursor-blame.md](082-docs-integrations-cursor-blame.md)

## Bottom Line

Use this folder as a guided learning library for Cursor. Start with the beginner path, then move into Agent, CLI, Cloud Agent, or enterprise topics based on what you need to teach, automate, deploy, or govern.
