# Module 6: Cloud Agents in the UI

## Cursor Training Program — Day 2

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~90 minutes |
| **Format** | Hands-on exercise + demonstration |
| **Prerequisites** | GitHub repository connected to Cursor, Cloud Agents enabled |
| **Module Goal** | Launch and manage Cloud Agents from the web dashboard, collect artifacts, and trigger agents from messaging platforms |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Launch and monitor Cloud Agents from the web dashboard
- Collect and review artifacts (screenshots, logs, videos)
- Trigger Cloud Agents from Slack and Microsoft Teams
- Understand when to use Cloud Agents vs. local agents

---

## Lesson 6.1: Launching a Cloud Agent

### Concept (10 minutes)

> *"Cloud agents run in isolated cloud VMs instead of your local machine. You can run as many as you want in parallel, and they don't require your laptop to be connected to the internet."*

**Local vs. Cloud Agents:**

| Local Agent | Cloud Agent |
|-------------|-------------|
| Runs on YOUR computer | Runs on Cursor's cloud computers |
| Stops when you close laptop | Runs 24/7 |
| One at a time (typically) | Run as many as you want in parallel |
| Can't work while you sleep | Work while you're offline |

**When to Use Cloud Agents:**

| Use Case | Why |
|----------|-----|
| Long-running tasks | Agent can run for hours without your laptop |
| Parallel work | Run many agents simultaneously |
| Leave and come back | Start a task, go home, agent finishes overnight |
| CI/CD integration | Automate code reviews, testing, deployments |

### Access Methods

| Method | How |
|--------|-----|
| **Web Dashboard** | `cursor.com/agents` |
| **Cursor Desktop** | Select "Cloud" in agent dropdown |
| **Slack** | `@cursor` command |
| **Microsoft Teams** | `@Cursor` command |
| **GitHub** | Comment `@cursor` on PR/issue |
| **Linear** | Assign issue to "Cursor" |
| **API** | Programmatic launch |

### Hands-On Exercise (20 minutes)

**Step 1:** Open the Cloud Agents dashboard

Navigate to `cursor.com/agents`

**Step 2:** Click "New Agent"

**Step 3:** Fill out the form:

| Field | Value |
|-------|-------|
| Repository | Select your GitHub repo |
| Branch | `main` (or your default branch) |
| Prompt | *"Add a README.md file with setup instructions and a badges section"* |
| Model | `composer-2` (or default) |

**Step 4:** Click "Start"

**Step 5:** Monitor progress in the dashboard:

```
┌─────────────────────────────────────────────────────────────────┐
│  ☁️  CLOUD AGENT RUNNING                                        │
├─────────────────────────────────────────────────────────────────┤
│  Agent ID: ca_abc123                                            │
│  Status: 🔄 Running                                             │
│  Started: 2025-01-15 10:30:45                                  │
│                                                                 │
│  📋 Activity Log:                                               │
│  [10:30:45] Agent started                                       │
│  [10:30:47] Cloning repository...                              │
│  [10:30:52] Reading files...                                    │
│  [10:31:05] Adding README.md...                                 │
│  [10:31:30] Creating commit...                                  │
│  [10:31:35] Opening pull request...                             │
└─────────────────────────────────────────────────────────────────┘
```

**Step 6:** When complete, review the PR on GitHub

**Success Criteria:**
- [ ] Cloud Agent launched successfully
- [ ] Agent appeared in dashboard
- [ ] Agent completed successfully
- [ ] PR created on GitHub

---

## Lesson 6.2: Cloud Agent Artifacts

### Concept (10 minutes)

> *"Artifacts are files produced by a Cloud Agent – screenshots, videos, logs, generated code. They show you exactly what the agent did."*

**Types of Artifacts:**

| Artifact Type | Description | When Produced |
|---------------|-------------|---------------|
| **Screenshots** | Images of browser/UI state | When agent uses browser tool |
| **Videos** | Recording of agent's actions | For complex UI interactions |
| **Logs** | Terminal output, build logs | Always |
| **Generated files** | Code, documentation, configs | Always |
| **Test reports** | Pass/fail results | After running tests |

### Hands-On Exercise (15 minutes)

**Step 1:** From the completed agent in the dashboard, click the **"Artifacts"** tab

**Step 2:** Review the artifacts:

```
┌─────────────────────────────────────────────────────────────────┐
│  ARTIFACTS                                                      │
├─────────────────────────────────────────────────────────────────┤
│  📸 Screenshots (1)                                             │
│     └── screenshot_before.png (845 KB) - View                  │
│                                                                 │
│  📋 Logs (2)                                                    │
│     ├── agent_log.txt (124 KB) - Download                      │
│     └── build_log.txt (45 KB) - Download                       │
│                                                                 │
│  📄 Generated Files (1)                                         │
│     └── README.md (2 KB) - Download                            │
└─────────────────────────────────────────────────────────────────┘
```

**Step 3:** Click to view a screenshot

**Step 4:** Download a log file and examine its contents

**Step 5:** Download the generated README.md

**Step 6:** (Optional) Run another Cloud Agent with a prompt that uses the browser:

> *"Open the browser to example.com and take a screenshot"*

Then review the screenshot artifact.

**Success Criteria:**
- [ ] Viewed at least one screenshot
- [ ] Examined log file
- [ ] Downloaded a generated file
- [ ] Understood what each artifact type shows

---

## Lesson 6.3: Cloud Agents from Messaging Platforms (Demonstration)

### Concept (10 minutes)

> *"You can trigger Cloud Agents directly from Slack and Microsoft Teams – no need to open the dashboard. Just mention @Cursor or @Cursor and give your prompt."*

**Slack Integration:**

| Command | Example |
|---------|---------|
| Basic | `@cursor Add a README file` |
| Specify repo | `@cursor in my-repo Fix the typo` |
| Specify branch | `@cursor on develop Run all tests` |
| Specify model | `@cursor with opus Review security` |

**Microsoft Teams Integration:**

| Command | Example |
|---------|---------|
| Basic | `@Cursor Add a README file` |
| Specify repo | `@Cursor in my-repo Fix the typo` |

### Demonstration (15 minutes)

**Instructor demonstrates:**

**Step 1:** In a Slack channel with the Cursor app installed:

```
@cursor Add a README.md file to the calculator repository
```

**Step 2:** Observe the response:

```
🔁 Launching Cloud Agent...

📋 Task: Add a README.md file to the calculator repository

✅ Agent started successfully
🆔 Agent ID: ca_abc123
📊 Monitor: https://cursor.com/agents/ca_abc123

I'll update this thread when the agent completes.
```

**Step 3:** Monitor progress in the thread

**Step 4:** When complete:

```
✅ Cloud Agent completed!

📊 Summary:
- Added README.md with setup instructions

🔗 Pull Request: https://github.com/.../pull/123
⏱️ Duration: 45 seconds

View full details: https://cursor.com/agents/ca_abc123
```

**Step 5:** (If using Teams) Demonstrate similar workflow in Microsoft Teams

### Discussion (10 minutes)

**How could your team use this?**

| Use Case | Benefit |
|----------|---------|
| Bug reported in chat | Launch agent to fix it immediately |
| Documentation request | Agent writes docs on demand |
| Code review | Agent reviews PR from Slack |
| On-call rotation | Agent investigates issues from phone |

**Success Criteria:**
- [ ] (For demo) Agent triggered from Slack/Teams
- [ ] Received confirmation and agent ID
- [ ] Agent completed successfully
- [ ] PR created (if applicable)

---

## Lesson 6.4: Automations (Optional / Time Permitting)

### Concept (5 minutes)

> *"Automations let you run Cloud Agents on a schedule or in response to events – GitHub PRs, Slack messages, Sentry errors, and more."*

**Trigger Types:**

| Trigger | When It Fires |
|---------|---------------|
| **Scheduled (cron)** | Daily, weekly, custom schedule |
| **GitHub PR opened** | When PR is created |
| **GitHub PR merged** | When PR is merged |
| **Slack message** | When message sent to channel |
| **Sentry error** | When new error occurs |
| **Linear issue** | When issue is created |

**Example Use Cases:**

| Automation | Trigger | Action |
|------------|---------|--------|
| Nightly code review | Schedule (6 AM daily) | Agent reviews code, opens PR |
| PR security scan | GitHub PR opened | Agent scans for vulnerabilities |
| Error investigation | Sentry error | Agent creates PR with fix |
| Documentation refresh | Schedule (weekly) | Agent updates docs |

### Demonstration (5 minutes)

**Instructor demonstrates creating a simple automation:**

1. Navigate to `cursor.com/automations`
2. Click "New Automation"
3. Select trigger (e.g., "Schedule")
4. Set schedule (e.g., daily at 6 AM)
5. Write prompt
6. Enable "Auto-create PR"
7. Save and activate

---

## Module Summary

| Lesson | Topic | Format |
|--------|-------|--------|
| 6.1 | Launching a Cloud Agent | Hands-on |
| 6.2 | Cloud Agent Artifacts | Hands-on |
| 6.3 | Cloud Agents from Messaging Platforms | Demonstration |
| 6.4 | Automations | Optional demo |

---

## Quick Reference Card

| Action | Method |
|--------|--------|
| Launch Cloud Agent | `cursor.com/agents` → New Agent |
| View artifacts | Agent details → Artifacts tab |
| Trigger from Slack | `@cursor prompt` |
| Trigger from Teams | `@Cursor prompt` |
| Monitor progress | Dashboard or Slack/Teams thread |
| Create automation | `cursor.com/automations` |

---

## When to Use Cloud Agents vs. Local Agents

| Use Local Agent When... | Use Cloud Agent When... |
|------------------------|------------------------|
| Quick questions | Long-running tasks |
| Interactive debugging | Tasks that run while you're away |
| Exploring code | Parallel work across many files |
| Small changes | Automated workflows (CI/CD) |
| You need immediate feedback | You don't need immediate results |

---

## Transition to Module 7

> *"Now that you can launch Cloud Agents from the UI, let's look at how to do this programmatically using the Cursor APIs."*

---

*End of Module 6*