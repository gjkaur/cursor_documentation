This is the **Slack Integration** documentation – it explains how to use Cursor's Cloud Agents directly from **Slack** by mentioning `@cursor`.

Think of this as **bringing AI coding assistance into your team chat** – you can ask for fixes, create PRs, and manage agents without leaving Slack.

Let me break this down for a beginner.

---

## What Is the Slack Integration? (The 10-Second Summary)

**You can start Cloud Agents directly from Slack by mentioning `@cursor`.** The agent works on your code and posts updates back to the Slack thread.

| Without Slack Integration | With Slack Integration |
|--------------------------|----------------------|
| Open Cursor dashboard | Stay in Slack |
| Type prompts in web UI | Type `@cursor fix the login bug` |
| Manually check status | Get notifications when agent completes |

> *"Mention @cursor and give your prompt. Cursor automatically picks the right repository and model based on your message and your recent agent activity."*

---

## Setup (4 Steps)

| Step | What to do |
|------|------------|
| **1** | Go to **Cursor Integrations** → Click **Connect** next to Slack |
| **2** | Install the Cursor app for Slack in your workspace |
| **3** | Finalize setup in Cursor (redirects back after Slack install) |
| **4** | Start using Cloud Agents by mentioning `@cursor` |

### Prerequisites:

Before using Cloud Agents in Slack, you need:

| Requirement | Status |
|-------------|--------|
| Connect GitHub (if not already) and pick default repository | ✅ Required |
| Enable usage-based pricing | ✅ Required |
| Confirm privacy settings | ✅ Required |

---

## How to Use (Basic Commands)

### Start a Cloud Agent:

```
@cursor fix the login bug in backend-api
```

### Specify a Repository:

```
@cursor in cursor-app, fix the login bug
@cursor fix the auth issue in backend-api
```

### Specify a Model:

```
@cursor with opus, fix the login bug
@cursor with gpt-5.2, refactor the auth module
```

### Combine in Natural Language:

```
@cursor with opus, fix the login bug in backend-api
```

---

## Advanced Syntax (Inline Options)

You can also use **inline options** for explicit control:

```
@cursor branch=dev autopr=false Fix the login bug in backend-api
```

### Available Options:

| Option | Description | Example |
|--------|-------------|---------|
| `branch=` | Specify branch name | `branch=feature/auth` |
| `autopr=` | Auto-create PR (`true`/`false`) | `autopr=true` |

### Option Precedence:

| Rule | Example |
|------|---------|
| Explicit values override defaults | `branch=dev` overrides default branch |
| Later values override earlier if duplicated | Last one wins |
| Intuitive options take precedence over settings | Natural language `in repo-name` beats dashboard default |

---

## Commands Summary

| Command | What it does |
|---------|--------------|
| `@cursor [prompt]` | Start a Cloud Agent |
| `@cursor settings` | Configure defaults and channel default repository |
| `@cursor [options] [prompt]` | Use advanced options (branch, autopr) |
| `@cursor agent [prompt]` | Force create a new agent (not follow-up) |
| `@cursor list my agents` | Show your running agents |

---

## Understanding Thread Context

### In Threads with Existing Agents:

| Command | Behavior |
|---------|----------|
| `@cursor [prompt]` | **Adds follow-up instructions** (only works if you own the agent) |
| `@cursor agent [prompt]` | Forces a **new separate agent** |

### Example:

If you have an agent already working, and you type `@cursor also add error handling`, it will add that as a follow-up to the existing agent.

### Use Context Menu for Follow-ups:

When multiple agents exist in a thread, use the context menu (`↔`) on an agent's response to specify which agent to follow up on.

### Thread Context (Agent Reads the Conversation):

> *"Cloud Agents understand and use context from existing thread discussions. Useful when your team discusses an issue and you want the agent to implement the solution based on that conversation."*

**Example:** Your team debates a bug in Slack. At the end, you type `@cursor implement the fix we discussed` – the agent reads the whole conversation and implements the agreed solution.

---

## Status Updates & Handoff

### When Agent Starts:

You get a message:

> *"A Background Agent was launched. I'll update this thread when ready."*
> 
> [Open in Cursor] button

### When Agent Completes:

You get a notification and a **View PR** button (if a PR was created).

---

## Managing Agents

### List Running Agents:

```
@cursor list my agents
```

### Context Menu Options (three dots on any agent message):

| Option | What it does |
|--------|--------------|
| **Add follow-up** | Add instructions to an existing agent |
| **Delete** | Stop and archive the Cloud Agent |
| **View request ID** | Get unique ID for troubleshooting (include when contacting support) |
| **Give feedback** | Provide feedback about agent performance |

---

## Configuration

### Default Model

Set the default model used when no model is specified in your message (via Dashboard → Cloud Agents).

### Repository Selection (How Cursor Picks the Repo)

Cursor evaluates in this order:

| Priority | Source |
|----------|--------|
| 1 | **Your message content** – Repo names or keywords in prompt |
| 2 | **Recent agent activity** – Repos you've used recently |
| 3 | **Routing rules** – Custom keyword-to-repo mappings (see below) |
| 4 | **Channel default** – Repository set for this channel |
| 5 | **Default repository** – Fallback when no match found |

**To use a specific repository:** Include its name in your message:
```
@cursor in mobile-app, fix the login bug
```

### Base Branch

Starting branch for Cloud Agent. Leave blank to use the repository's default branch (often `main`).

---

## Channel Settings

Configure default settings at the **channel level** using:

```
@cursor settings
```

**Channel settings are per team** and override your personal defaults for that channel.

### When to Use:

| Scenario | Benefit |
|----------|---------|
| Different channels work on different repositories | Each channel can have its own default repo |
| Teams want consistent settings across all members | Everyone in channel uses same defaults |

### Precedence:

Channel settings take precedence over personal defaults but can be overridden by mentioning a specific repo in your message.

> *"Channel settings only apply to public channels."*

---

## Routing Rules (Keyword → Repository Mapping)

Set up **routing rules** in Dashboard → Cloud Agents to automatically map keywords to specific repositories.

### Example Rules:

| Keyword | Repository |
|---------|------------|
| `frontend` | `acme/web-app` |
| `mobile` | `acme/mobile-app` |
| `api` | `acme/backend-services` |
| `docs` | `acme/documentation` |

### How It Works:

| Message | Routes to |
|---------|-----------|
| `@cursor fix the frontend nav bug` | `acme/web-app` |
| `@cursor update the mobile onboarding flow` | `acme/mobile-app` |
| `@cursor add rate limiting to the api` | `acme/backend-services` |

---

## Privacy & Display Settings

### Privacy Mode

Cloud Agents support Privacy Mode.

> *"Privacy Mode (Legacy) is not supported. Cloud Agents require temporary code storage while running."*

### Display Agent Summary

Control whether agent summaries and diff images (may contain file paths or code snippets) are displayed. Can be turned **On/Off**.

### Display Agent Summary in External Channels

For **Slack Connect** with other workspaces or channels with external members (Guests), choose to display agent summaries in external channels.

---

## Permissions (What the Slack App Needs)

Cursor requests these Slack permissions:

| Permission | Why it's needed |
|------------|-----------------|
| `app_mentions:read` | Detects `@cursor` mentions to start agents |
| `channels:history` | Reads previous messages for context |
| `channels:join` | Automatically joins public channels when invited |
| `channels:read` | Accesses channel metadata to post replies |
| `chat:write` | Sends status updates, completions, PR links |
| `files:read` | Downloads shared files (logs, screenshots, code) |
| `files:write` | Uploads visual summaries of agent changes |
| `groups:history` | Reads private channel history for context |
| `groups:read` | Accesses private channel metadata |
| `im:history` | Reads DM history for context |
| `im:read` | Reads DM metadata |
| `im:write` | Initiates DMs for private notifications |
| `mpim:history` | Reads group DM history |
| `mpim:read` | Reads group DM metadata |
| `reactions:read` | Observes emoji reactions for feedback |
| `reactions:write` | Adds emoji reactions (✅ for running, ✅ for completed, ❌ for failed) |
| `team:read` | Identifies workspace details |
| `users:read` | Matches Slack users with Cursor accounts |

---

## Quick Reference Card

| Command | Purpose |
|---------|---------|
| `@cursor [prompt]` | Start a Cloud Agent |
| `@cursor agent [prompt]` | Force new agent (not follow-up) |
| `@cursor settings` | Configure defaults |
| `@cursor list my agents` | List running agents |
| `@cursor with [model] [prompt]` | Specify model |
| `@cursor in [repo] [prompt]` | Specify repository |

| Option | Example |
|--------|---------|
| `branch=` | `branch=feature/auth` |
| `autopr=` | `autopr=false` |

---

## Common Beginner Questions

### Q: Do I need a paid plan to use Slack integration?
**A:** Cloud Agents require usage-based pricing enabled. See billing documentation.

### Q: Can the agent read my Slack messages for context?
**A:** Yes, if you're in a thread, the agent reads the conversation history to understand context.

### Q: How do I know which repo the agent will use?
**A:** Cursor evaluates: message keywords → recent activity → routing rules → channel default → your default.

### Q: Can I use the Slack integration in private channels?
**A:** Yes, but the app needs appropriate permissions (`groups:read`, `groups:history`).

### Q: What happens if multiple agents are in the same thread?
**A:** Use the context menu (`↔`) on the specific agent's response to add follow-up instructions.

### Q: Can I see agent summaries in external Slack channels (guests)?
**A:** Yes, but you need to enable "Display Agent Summary in External Channels" in settings.

---

## The Bottom Line

**The Slack integration brings Cursor's AI coding agents directly into your team chat.**

**Think of it as:**
- **Without Slack** = Switch between Cursor and Slack 🤹
- **With Slack** = Agents work where your team already talks 💬

**For teams:** This is incredibly powerful. Your team can discuss issues in Slack, and at the end, just type `@cursor implement the fix` – the agent reads the whole conversation and does the work.

**Key features:**
1. **Natural language** – `@cursor with opus, fix the login bug in backend-api`
2. **Thread context** – Agent reads previous discussion
3. **Routing rules** – Map keywords to repos automatically
4. **Channel settings** – Different defaults per channel
5. **PR creation** – Agent can open PRs directly

**Disclaimer:** *"Cursor can make mistakes. Please double-check code and responses."*

