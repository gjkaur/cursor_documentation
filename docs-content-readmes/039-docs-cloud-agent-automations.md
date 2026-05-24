This is the **Cursor Automations** documentation – it explains how to run Cloud Agents **automatically** on a schedule or in response to events from GitHub, Slack, Sentry, and more.

Think of Automations as **setting up a robot that works for you** – it triggers when something happens (a PR is opened, a Slack message is sent, a Sentry error occurs) and does tasks automatically.

Let me break this down for a beginner.

---

## What Are Cursor Automations? (The 10-Second Summary)

**Cursor Automations run cloud agents in the background, either on a schedule or in response to events from GitHub, Slack, Sentry, and more.**

| Without Automations | With Automations |
|--------------------|------------------|
| You manually run agents | Agents run automatically |
| You check for issues manually | Agents monitor events 24/7 |
| Repetitive tasks done by hand | Tedious tasks automated |

> *"Automations can be used to automate tasks like tedious code maintenance, performing deep review for vulnerabilities, triaging bugs in Slack, and investigating Sentry issues."*

---

## Getting Started

Create a new automation in the **Agents Window** (recommended) or at `cursor.com/automations`, or start from a template in the marketplace.

| Step | What to do |
|------|------------|
| **1** | Choose a trigger (e.g., every hour, when a pull request is opened, new Slack message) |
| **2** | Attach zero, one, or **multiple repositories** (multi-repo automations) |
| **3** | Write a prompt with instructions for the automation |
| **4** | Choose tools (Send to Slack, Comment on PR, MCP tools) |
| **5** | Create and watch it run! |

### Automation Types (May 2026)

| Type | When to use |
|------|-------------|
| **Single-repo** | Classic code maintenance tied to one repository |
| **Multi-repo** | Tasks spanning frontend, backend, shared libraries, or services |
| **No-repo** | Tool-only workflows (Slack digests, analytics, finance, customer health) with no attached code |

> *As of May 20, 2026, automations can be created and managed directly in the Agents Window. Newly created automations may qualify for launch promotions (check the changelog for current offers).*

---

## Billing

Automations create Cloud Agents and are billed based on Cloud Agent usage.

### Permission Scopes & Billing:

| Scope | Billing |
|-------|---------|
| **Team Owned** | Billed to team's usage pool (shared service account, no individual impact) |
| **Private** | Billed to the user who created the automation |
| **Team Visible** | Billed to the user who created the automation |

---

## Triggers (What Starts an Automation)

Triggers decide when an automation runs. An automation can have **more than one trigger** and runs when ANY trigger fires.

> *"For certain triggers like schedules or Slack, you also choose a repository and branch. Cursor cannot infer them from a pull request."*

---

### Scheduled Triggers (Cron)

Run on a recurring schedule:

| Option | Description |
|--------|-------------|
| **Preset options** | Every hour, every day, etc. |
| **Cron expression** | Precise control (e.g., `0 2 * * *` for 2 AM daily) |

> *"Scheduled triggers may run with a delay but will not start before the indicated time."*

---

### GitHub Triggers

Respond to GitHub events:

| Trigger | When it fires |
|---------|---------------|
| **Draft opened** | Draft PR created |
| **Pull request opened** | Non-draft PR created or draft marked ready |
| **Pull request pushed** | New commits pushed to existing PR |
| **Pull request label changed** | Label added/removed from PR |
| **Pull request merged** | PR merged |
| **Pull request commented** | Someone comments on a PR |
| **Push to branch** | Commits pushed to branch (outside PR) |
| **CI completed** | GitHub Check finishes on PR/branch |

---

### Slack Triggers

Respond to events from the Cursor Slack integration.

> *"Only public Slack channels are visible to Slack triggers at this time."*

| Trigger | When it fires |
|---------|---------------|
| **New message in channel** | Message sent to connected Slack channel |
| **Channel created** | New public Slack channel created |

**Message filter:** Without filter, triggers only on top-level messages. Add keyword/regex filter for threaded replies.

---

### Webhook Triggers

Create a **private HTTP endpoint** for your automation. POST to the endpoint to start a run.

| Use case | Examples |
|----------|----------|
| Internal systems | Connect to CI pipelines |
| Monitoring tools | Trigger from alerts |
| Custom integrations | Any system that can make HTTP requests |

> *"To retrieve the webhook URL, you must save the automation first, which will then generate a webhook URL to call and an API key for authentication."*

---

### Linear Triggers

Respond to events from the Cursor Linear integration:

| Trigger | When it fires |
|---------|---------------|
| **Issue created** | New issue created |
| **Status changed** | Issue status changes |
| **End of cycle** | Linear cycle completes |

---

### Sentry Triggers

Run when error and issue events occur in your Sentry project.

| Use case | Description |
|----------|-------------|
| **Investigate errors** | Automatically identify root causes |
| **Propose fixes** | Suggest resolutions |

| Trigger | When it fires |
|---------|---------------|
| **Issue created** | New issue created in Sentry |
| **Issue updated** | Existing issue changes (status, assignment) |
| **Any issue event** | Matches all issue event types |

> *"See the 'Investigate Sentry issues' marketplace template for a ready-made example."*

---

### PagerDuty Triggers

Run on incident events:

| Trigger | When it fires |
|---------|---------------|
| **Incident triggered** | New incident created |
| **Incident acknowledged** | Incident acknowledged |
| **Incident resolved** | Incident resolved |
| **Any incident event** | Matches all incident event types |

> *"Useful to automatically triage or even resolve incidents."*

---

## Tools (What the Automation Can Do)

Automations can have tools enabled for richer capabilities.

### Open Pull Request

Lets the agent create a new pull request on GitHub.

| Capability | Description |
|------------|-------------|
| **Write code** | Agent can write code |
| **Create branch** | Creates branch for changes |
| **Open PR** | Opens pull request |

> *"The pull request is opened against the repository from the GitHub trigger. For non-GitHub triggers, it uses the repository selected in the trigger settings."*

### Comment on Pull Request

Posts comments on the triggering pull request.

| Support | Details |
|---------|---------|
| **Top-level review comments** | ✅ Yes |
| **Inline code comments** | ✅ Yes |
| **Approvals** | If enabled, agent can approve, request changes, dismiss reviews |

> *"This action requires a pull request trigger."*

### Request Reviewers

Requests reviewers on the triggering pull request.

> *"The agent can use git, memory, and other tools to identify domain experts."*
> *"This action requires a pull request trigger."*

### Send to Slack

Sends messages to a Slack channel.

| Option | Description |
|--------|-------------|
| **Target specific channel** | Fixed channel |
| **Agent chooses channel** | Dynamically any channel |

> *"When you allow any channel, Cursor also includes the read access needed for the agent to discover available public channels."*

### Read Slack Channels

Gives the agent **read-only access** to list and read messages from public Slack channels.

> *"Use this when the agent needs more context before it replies or opens a pull request."*

### MCP Server

Connects an MCP server so the agent can use external tools and data sources.

> *"Connecting an MCP server gives the agent access to every tool exposed by that server. Only connect servers you trust with the permissions your automation needs."*

### Memories

Let the agent **read and write persistent notes** across runs for the same automation.

| Feature | Description |
|---------|-------------|
| **Purpose** | Build agents that remember and improve over time |
| **Storage** | Each memory stored as named entry (MEMORIES.md by default) |
| **Enabled by default** | Can be disabled |
| **View/Edit** | From tool configuration UI |

> *"Memories persist across runs and should be used with caution if your automation handles untrusted input. Inputs may lead to misleading or malicious memories that unintentionally impact future automation runs."*

---

## Automation Settings

### Model

Choose which model the agent uses. Same models as Cloud Agents, tailored for autonomous use cases. Cursor chooses a default model when you create the automation.

### Environment

| Setting | What it does |
|---------|--------------|
| **Enabled** | Agent installs dependencies before running. Use when automation needs to build, test, or execute code. |
| **Disabled** | Agent skips dependency installation. Use when it only needs to read or review code. |

> *"Configure environment settings and secrets in the Cloud Agents dashboard. The automation uses the same settings for the selected repository."*

### Permissions (Who Can Manage)

| Scope | Who can manage | Billing | Runs as |
|-------|----------------|---------|---------|
| **Private** | Only you (admins can view/disable) | Your usage | Your auth |
| **Team Visible** | Only you (admins can disable) | Your usage | Your auth |
| **Team Owned** | Only team admins | Team pool | Team service account |

> *"Promoting an automation from Private or Team Visible to Team Owned changes the identity it runs as. It stops using your auth and starts using the team's shared automations service account."*

### Identity (How Actions Appear)

| Action | Identity |
|--------|----------|
| **GitHub comments, approvals, reviewer requests** | `cursor` |
| **Team-scoped automations (open PRs)** | `cursor` |
| **Private automations (open PRs)** | Your GitHub account |
| **Slack messages** | Cursor bot |

---

## Writing Prompts (Instructions)

Prompts define what the agent should do. Write them the same way you would write instructions for a cloud agent run.

### Tips:

| Tip | Example |
|-----|---------|
| **Be specific** | "Check for hardcoded API keys in new code" |
| **Reference enabled actions** | At-mention tools or informally mention names |
| **Include decision rules** | "If vulnerability found, comment on PR. If critical, request changes." |
| **Set quality bar** | "Only open PR if tests pass" |
| **Describe output format** | "Output findings as bullet points with severity" |

---

## Example Automation Use Cases

| Use Case | Trigger | Actions |
|----------|---------|---------|
| **Nightly vulnerability scan** | Scheduled (cron) | Scan code, open PR with fixes |
| **PR security review** | Pull request opened | Comment on PR, request reviewers |
| **Slack bug triage** | New message in Slack | Investigate, reply with fix |
| **Sentry error investigation** | Issue created in Sentry | Analyze root cause, propose fix |
| **PagerDuty incident response** | Incident triggered | Triage, attempt automated resolution |

---

## Common Beginner Questions

### Q: Do I need Automations as a beginner?
**A:** No – this is for advanced users and teams who want to automate repetitive tasks.

### Q: What triggers are available?
**A:** Scheduled (cron), GitHub, Slack, Webhook, Linear, Sentry, PagerDuty.

### Q: Can an automation have multiple triggers?
**A:** Yes – runs when ANY trigger fires.

### Q: How is billing handled?
**A:** Team Owned = team pool; Private/Team Visible = your usage.

### Q: Can the agent remember things across runs?
**A:** Yes – use Memories tool for persistent notes.

### Q: Can I trigger automations from internal systems?
**A:** Yes – use Webhook triggers (private HTTP endpoint).

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **What it does** | Run Cloud Agents automatically on triggers |
| **Setup** | Agents Window (recommended) or `cursor.com/automations` |
| **Triggers** | Scheduled, GitHub, Slack, Webhook, Linear, Sentry, PagerDuty |
| **Tools** | Open PR, Comment on PR, Request reviewers, Send to Slack, Read Slack, MCP, Memories |
| **Billing** | Team pool or individual (depends on scope) |
| **Permissions** | Private, Team Visible, Team Owned |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What are Automations?** | Cloud Agents that run automatically on triggers |
| **Do I need them?** | Only for automating repetitive tasks |
| **What can trigger them?** | Schedules, GitHub, Slack, webhooks, Linear, Sentry, PagerDuty |
| **What can they do?** | Open PRs, comment, send Slack messages, use MCPs, remember things |
| **How much do they cost?** | Cloud Agent usage (team pool or individual) |
| **Can they learn over time?** | Yes – Memories tool persists across runs |

---

## The Bottom Line

**Cursor Automations let you set up "robots" that work for you 24/7 – monitoring events and taking action automatically.**

**Think of it as:**
- **Without Automations** = You check for issues manually 👀
- **With Automations** = Robots watch everything and act automatically 🤖

**For teams:** Automations are incredibly powerful. You can:
- Automatically review PRs for security issues
- Investigate Sentry errors as they happen
- Triage PagerDuty incidents
- Run scheduled code maintenance
- Respond to Slack messages with automated fixes

**The most powerful features:**
1. **Multiple triggers** – One automation can respond to many events
2. **Memories** – Agents remember and improve over time
3. **Team Owned** – Runs under team service account, no individual impact
4. **Webhook triggers** – Connect to any internal system

