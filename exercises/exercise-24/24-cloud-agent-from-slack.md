# Cursor Training – Exercise 24

## Cloud Agent from Slack

**Objective:** Trigger and monitor Cloud Agents directly from Slack – allowing your team to launch AI agents without leaving their chat workspace.

**Time:** 10 minutes

**Setup:** Slack workspace with Cursor app installed, GitHub repository connected, Cloud Agents enabled

---

## Prerequisites

Before starting this exercise, ensure:

| Requirement | Status | How to check |
|-------------|--------|--------------|
| Slack workspace with Cursor app | ❓ | Cursor app installed in Slack |
| GitHub repository connected | ❓ | `cursor.com/integrations` → GitHub |
| Cloud Agents enabled | ❓ | `cursor.com/agents` accessible |
| Slack channel with Cursor bot | ❓ | Bot is a member of the channel |

---

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open your Slack workspace | Slack interface appears |
| 2 | Go to a channel with Cursor bot | Bot is present in channel |
| 3 | Type `@cursor` followed by a prompt | Bot acknowledges and starts agent |
| 4 | Receive confirmation message | Cloud Agent ID and status shown |
| 5 | Monitor progress in Slack | Updates posted to channel |
| 6 | View results when complete | PR link or summary posted |

---

## Step 1: Install Cursor Slack App (If Not Already)

If the Cursor app is not yet installed:

1. Go to `cursor.com/integrations`
2. Click "Connect" next to Slack
3. Authorize the Cursor app for your workspace
4. Select the channels where the bot should be available

**Slack permissions required:**
- Send messages
- Read channel history
- Mention bot (`@cursor`)

---

## Step 2: Invite Bot to a Channel

If bot is not already in your channel:

```slack
/invite @cursor
```

Or click on channel name → Integrations → Add apps → Cursor

---

## Step 3: Launch a Cloud Agent from Slack

In a channel with the Cursor bot, type:

```
@cursor Add a README.md file to the calculator repository explaining how to build and run the program
```

**Expected response:**

```slack
🔁 Launching Cloud Agent...

📋 Task: Add a README.md file to the calculator repository

✅ Agent started successfully
🆔 Agent ID: ca_abc123xyz
📊 Monitor: https://cursor.com/agents/ca_abc123xyz

I'll update this thread when the agent completes.
```

---

## Sample Slack Commands

### Basic Task

```
@cursor Fix the typo in the README.md file
```

### Specify Repository

```
@cursor in your-username/calculator Add input validation to the divide function
```

### Specify Branch

```
@cursor on branch feature/auth Add login functionality
```

### With Specific Model

```
@cursor with claude-4.7-opus Review the code for security issues
```

### Multiple Instructions

```
@cursor Do the following in the calculator repo:
1. Add a modulo function
2. Add unit tests for it
3. Update the README
```

---

## Step 4: Monitor Progress

The Cursor bot posts updates to the thread:

```slack
🔄 Agent progress update (ca_abc123xyz)

[10:30:45] Agent started
[10:30:47] Cloning repository...
[10:30:52] Reading calculator.c...
[10:31:05] Adding modulo function...
[10:31:20] Adding unit tests...
[10:31:35] Updating README...
[10:31:40] Creating pull request...
```

---

## Step 5: View Results

When complete:

```slack
✅ Cloud Agent completed! (ca_abc123xyz)

📊 Summary:
- Added modulo function to calculator.c
- Added 3 unit tests
- Updated README with new operation

🔗 Pull Request: https://github.com/your-username/calculator/pull/123
⏱️ Duration: 55 seconds

View full details: https://cursor.com/agents/ca_abc123xyz
```

---

## Slack-Specific Commands

| Command | Description |
|---------|-------------|
| `@cursor <prompt>` | Launch a new Cloud Agent |
| `@cursor in <repo> <prompt>` | Specify repository |
| `@cursor on <branch> <prompt>` | Specify branch |
| `@cursor with <model> <prompt>` | Specify model |
| `@cursor status` | Check status of recent agents |
| `@cursor cancel <id>` | Cancel a running agent |

---

## Success Criteria

- [ ] Cursor app installed in Slack workspace
- [ ] Bot is a member of your channel
- [ ] Successfully launched a Cloud Agent with `@cursor`
- [ ] Received confirmation and agent ID
- [ ] Monitored progress via Slack updates
- [ ] Viewed results (PR link or summary)

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `@cursor` not recognized | Invite bot to channel with `/invite @cursor` |
| No response from bot | Check Slack app permissions in integrations dashboard |
| Agent fails immediately | Check GitHub connection in `cursor.com/integrations` |
| Repository not found | Specify full repo name: `@cursor in username/repo` |
| Bot not posting updates | Ensure bot has `Send messages` permission |

---

## Key Takeaway

**Slack integration brings Cloud Agents into your team chat – no need to switch contexts.**

Use it when:
- Your team discusses a bug in Slack – launch an agent to fix it
- A code review needs changes – delegate to an agent
- Someone asks for documentation – let an agent write it
- You're away from your computer – launch an agent from mobile Slack

---

## Bonus Challenge (If Time Permits)

Create a Slack workflow that triggers a Cloud Agent based on emoji reactions:

1. Someone posts a bug report
2. Team adds 📝 emoji
3. Workflow triggers `@cursor Fix the bug described above`

Or set up channel-specific defaults:

> *"Set the default repository for #engineering channel to your-username/calculator"*

Then any `@cursor` in that channel automatically uses that repo.

---

## Exercise Complete ✓

Check off when done:
- [ ] Cursor app installed in Slack
- [ ] Bot invited to channel
- [ ] Launched Cloud Agent with `@cursor`
- [ ] Received confirmation
- [ ] Monitored progress via Slack
- [ ] Viewed results
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 25 – Cloud Agent Artifacts

---

## Quick Reference: Slack Integration Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                  SLACK INTEGRATION CHEAT SHEET                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  BASIC COMMANDS:                                                │
│  @cursor Add a README                                          │
│  @cursor in myrepo Fix the typo                                │
│  @cursor on develop Run all tests                              │
│  @cursor with opus Review security                             │
│                                                                 │
│  RESPONSES:                                                     │
│  • Confirmation with agent ID                                   │
│  • Progress updates in thread                                   │
│  • Completion with PR link                                      │
│                                                                 │
│  SETUP:                                                         │
│  1. Install from cursor.com/integrations                       │
│  2. Authorize for your workspace                               │
│  3. Invite bot to channel: /invite @cursor                     │
│                                                                 │
│  PERMISSIONS REQUIRED:                                          │
│  • Send messages                                                │
│  • Read channel history                                         │
│  • Mention bot                                                  │
│                                                                 │
│  EXAMPLE WORKFLOW:                                              │
│  Developer: "The login endpoint is returning 500"              │
│  Developer: @cursor Fix the login endpoint in main branch      │
│  Bot: 🔁 Launching Cloud Agent...                              │
│  Bot: ✅ Agent completed! PR #124 ready for review              │
│                                                                 │
│  TIPS:                                                          │
│  • Use threads to keep conversations organized                 │
│  • Set channel defaults to avoid repeating repo names          │
│  • Slack works on mobile – launch agents from anywhere         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
