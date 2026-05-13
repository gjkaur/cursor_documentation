This is the **Linear Integration** documentation – it explains how to use Cursor's Cloud Agents directly from **Linear**, the issue tracking tool.

Think of this as **connecting your issue tracker to AI** – you can assign issues to Cursor, and an agent will automatically work on them, create PRs, and update the issue status.

Let me break this down for a beginner.

---

## What Is the Linear Integration? (The 10-Second Summary)

**Use Cloud Agents directly from Linear by delegating issues to Cursor or mentioning @Cursor in comments.**

| Without Linear Integration | With Linear Integration |
|---------------------------|------------------------|
| Manually pick up issues | Assign issue to "Cursor" |
| Write code, create PR manually | Agent works automatically |
| Update issue status manually | Real-time status updates |

> *"Cursor analyzes issues and filters out non-development work automatically."*

---

## Setup (Installation)

### Prerequisites:

> *"You must be a Cursor admin to connect the Linear Integration. Other team settings are available to non-admin members."*

### Installation Steps:

| Step | What to do |
|------|------------|
| **1** | Go to **Cursor Integrations** |
| **2** | Click **Connect** next to Linear |
| **3** | Connect your Linear workspace and select team |
| **4** | Click **Authorize** |
| **5** | Complete Cloud Agent setup in Cursor: |
| | - Connect GitHub and select default repository |
| | - Enable usage-based pricing |
| | - Confirm privacy settings |

### Account Linking:

> *"First use prompts account linking between Cursor and Linear. GitHub connection required for PR creation."*

---

## How to Use (Two Ways)

### Method 1: Delegating Issues (Assign to Cursor)

| Step | Action |
|------|--------|
| 1 | Open Linear issue |
| 2 | Click the **assignee field** |
| 3 | Select **"Cursor"** |

The issue is now delegated to Cursor. A Cloud Agent will pick it up and work on it automatically.

### Method 2: Mentioning @Cursor in Comments

Mention `@Cursor` in a comment to assign a new agent or provide additional instructions:

```
@Cursor fix the authentication bug described above
```

---

## Workflow

### Real-time Status:

Cloud Agents show **real-time status** in Linear. You can see what the agent is doing directly in the issue.

### Automatic PR Creation:

When the agent completes its work, it **creates a PR automatically**.

### Track Progress:

You can also track progress in the **Cursor dashboard**.

---

## Follow-up Instructions

> *"You can respond in the agent session and it'll get sent as a follow-up to the agent. Simply mention @Cursor in a Linear comment to provide additional guidance to a running Cloud Agent."*

**Example:** An agent is working on an issue. You realize it needs more context:
```
@Cursor also make sure to handle the edge case when the user is not logged in
```

The agent receives this as a follow-up instruction.

---

## Configuration

Configure Cloud Agent settings from **Dashboard → Cloud Agents**:

| Setting | Location | Description |
|---------|----------|-------------|
| **Default Repository** | Cursor Dashboard | Primary repository when no project repository configured |
| **Default Model** | Cursor Dashboard | AI model for Cloud Agents |
| **Base Branch** | Cursor Dashboard | Branch to create PRs from (typically `main` or `develop`) |

---

## Configuration Options (Multiple Ways)

You can configure Cloud Agent behavior using several methods:

### 1. Issue Description or Comments (`[key=value]` syntax)

```
@cursor please fix [repo=anysphere/everysphere]
@cursor implement feature [model=claude-3.5-sonnet] [branch=feature-branch]
```

### 2. Issue Labels (Parent-Child Structure)

Use a parent-child label structure where:
- **Parent label** = configuration key
- **Child label** = value

### 3. Project Labels

Same parent-child structure as issue labels, applied at the project level.

### Supported Configuration Keys:

| Key | Description | Example |
|-----|-------------|---------|
| `repo` | Target repository | `owner/repository` |
| `branch` | Base branch for PR creation | `main`, `develop` |
| `model` | AI model to use | `claude-4-sonnet`, `gpt-5.2` |

---

## Repository Selection (Priority Order)

Cursor determines which repository to work on using this **priority order**:

| Priority | Source | Example |
|----------|--------|---------|
| **1** | Issue description/comments | `[repo=owner/repository]` syntax |
| **2** | Issue labels | Repository labels attached to the specific issue |
| **3** | Project labels | Repository labels attached to the Linear project |
| **4** | Default repository | Repository specified in Cursor dashboard settings |

---

## Setting Up Repository Labels in Linear

To create repository labels in Linear:

| Step | Action |
|------|--------|
| 1 | Go to **Settings** in your Linear workspace |
| 2 | Click **Labels** |
| 3 | Click **New group** |
| 4 | Name the group **"repo"** (case insensitive – must be exactly "repo", not "Repository" or other variations) |
| 5 | Within that group, create labels for each repository using the format `owner/repo` |

**Example:**
- Group name: `repo`
- Labels: `acme/web-app`, `acme/mobile-app`, `acme/backend-services`

These labels can then be assigned to issues or projects to specify which repository the Cloud Agent should work on.

---

## Automating with Triage Rules (Advanced)

You can set up **triage rules** in Linear to automatically:

| Action | Description |
|--------|-------------|
| Add specific labels | Auto-label issues based on conditions |
| Assign issues to Cursor | Automatically delegate certain issues |
| Trigger Cloud Agents | Start agents based on conditions |

### How to Set Up:

1. Go to **Linear project settings**
2. Navigate to **triage rules**
3. Create rules with your conditions

### Current Limitation:

> *"Linear requires a human assignee for rules to fire, though this requirement may be removed in future updates."*

---

## Complete Workflow Example

| Step | What happens |
|------|--------------|
| 1 | Team creates Linear issue: "Fix login bug in backend-api" |
| 2 | Assign issue to **Cursor** (or use triage rule to auto-assign) |
| 3 | Cloud Agent picks up issue automatically |
| 4 | Agent analyzes code, makes changes, runs tests |
| 5 | Agent creates PR on GitHub |
| 6 | Agent updates Linear issue with status and PR link |
| 7 | Team reviews PR and merges |
| 8 | Issue can be closed automatically or manually |

---

## Getting Help

> *"Check agent activity and include request IDs when contacting support."*

When troubleshooting, include the request ID from the agent activity.

---

## Feedback

Share feedback through:
- Linear comments
- Your Cursor dashboard support channels

---

## Quick Reference Card

| Feature | Details |
|---------|---------|
| **Two ways to use** | Assign issue to "Cursor" OR mention `@Cursor` in comments |
| **Configuration options** | Issue text (`[key=value]`), issue labels, project labels |
| **Repo selection priority** | Issue text → Issue labels → Project labels → Dashboard default |
| **Label group name** | `repo` (exact, case insensitive) |
| **Label format** | `owner/repository` |
| **Supported keys** | `repo`, `branch`, `model` |
| **Auto PR** | Yes – creates PR automatically |
| **Follow-up instructions** | `@Cursor` in comments |

---

## Common Beginner Questions

### Q: Do I need admin permissions to set up the integration?
**A:** Yes – you must be a Cursor admin to connect the Linear Integration.

### Q: Can I use the integration without GitHub?
**A:** No – GitHub connection is required for PR creation.

### Q: How does Cursor know which repository to work on?
**A:** Priority order: issue text → issue labels → project labels → dashboard default.

### Q: Can I specify which model to use?
**A:** Yes – use `[model=model-name]` in issue text or comments.

### Q: Can I send follow-up instructions to a running agent?
**A:** Yes – mention `@Cursor` in a Linear comment.

### Q: Can I automate which issues go to Cursor?
**A:** Yes – use Linear triage rules to auto-assign issues to Cursor based on conditions.

---

## The Bottom Line

**The Linear integration turns your issue tracker into an AI task runner.**

**Think of it as:**
- **Without Linear** = Issues wait for a human 👤
- **With Linear** = Issues can go to Cursor automatically 🤖

**For teams:** This is transformative. You can:
1. Assign issues to Cursor like you would assign to a teammate
2. Agents work autonomously and create PRs
3. Status updates happen automatically in Linear
4. Use triage rules to auto-delegate certain types of issues

**The workflow:**
```
Issue created → Assigned to Cursor → Agent works → PR created → Issue updated
```

**Key features:**
1. **Delegate issues** – Assign to "Cursor" just like any teammate
2. **Natural language config** – Use `[repo=...]` in comments
3. **Label-based routing** – Set `repo` labels in Linear
4. **Follow-up instructions** – `@Cursor` in comments to guide running agents
5. **Triage rules** – Automate assignment based on conditions

Would you like me to explain any specific Linear integration feature in more detail?