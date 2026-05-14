# Cursor Training – Exercise 21

## CLI – Cloud Handoff

**Objective:** Use the Cursor CLI to hand off a task to a Cloud Agent – allowing the Agent to continue working even after you close your terminal or laptop.

**Time:** 10 minutes

**Setup:** Cursor CLI installed (from Exercise 19), Cloud Agents enabled on your account

---

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open your terminal | Command prompt appears |
| 2 | Start an interactive CLI session | `agent` prompt appears |
| 3 | Type `&` followed by your prompt | Agent confirms handoff to cloud |
| 4 | Close your terminal | Agent continues running |
| 5 | Check progress on web dashboard | See agent status and results |

---

## What is Cloud Handoff?

| Aspect | Description |
|--------|-------------|
| **What it does** | Sends a task to run in the cloud instead of your local machine |
| **Symbol** | Prefix your prompt with `&` |
| **Persistence** | Agent keeps running even after you close terminal |
| **Access** | Monitor from `cursor.com/agents` web dashboard |
| **Results** | PRs, artifacts, logs available when complete |

---

## Why Use Cloud Handoff?

| Scenario | Benefit |
|----------|---------|
| **Long-running tasks** | Agent can run for hours without your laptop on |
| **Leaving for the day** | Start a task, go home, agent finishes overnight |
| **Parallel work** | Run multiple agents simultaneously |
| **Limited local resources** | Cloud has more compute power |
| **Unstable connection** | Agent continues even if your internet drops |

---

## Basic Cloud Handoff

### Method 1: In Interactive CLI Session

Start an interactive session:

```bash
agent
```

Then prefix your prompt with `&`:

```
> & Add comprehensive error handling to calculator.c and run tests
```

**Expected response:**
```
🔄 Handing off to Cloud Agent...

Cloud Agent started successfully.
Agent ID: ca_abc123xyz
You can monitor progress at: https://cursor.com/agents/ca_abc123xyz

The agent will continue running even after you close this terminal.
You will be notified when it completes.
```

---

### Method 2: One-Shot with Cloud Handoff

```bash
agent -p "& Refactor the divide function to include division by zero checking"
```

The `&` works the same way – sends the task to the cloud.

---

## Monitoring Your Cloud Agent

### Web Dashboard

After handoff, visit: `https://cursor.com/agents`

You will see:
- Agent status (Running / Completed / Failed)
- Start time and duration
- Logs and output
- Created PRs (if any)
- Artifacts (screenshots, videos)

### CLI Status Check

```bash
agent --resume <agent-id>
```

Or check status from CLI:

```bash
agent ls --cloud
```

---

## Cloud Handoff Examples

### Example 1: Long Build and Test

```
> & Run the full test suite, compile all targets, and generate a coverage report
```

### Example 2: Multi-File Refactoring

```
> & Rename all instances of 'calculate' to 'compute' across the entire project
```

### Example 3: Documentation Generation

```
> & Generate API documentation for all C files and create a README.md
```

### Example 4: Security Audit

```
> & Scan the entire codebase for potential security vulnerabilities and create a report
```

### Example 5: Dependency Update

```
> & Check for outdated dependencies, update them, and run tests to verify
```

---

## Expected Cloud Handoff Response

```
┌─────────────────────────────────────────────────────────────────┐
│  ☁️  CLOUD AGENT HANDOFF                                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Task: Add comprehensive error handling to calculator.c        │
│                                                                 │
│  ✅ Cloud Agent launched successfully                          │
│  📍 Agent ID: ca_abc123xyz                                     │
│  🔗 Monitor: https://cursor.com/agents/ca_abc123xyz            │
│                                                                 │
│  The agent will:                                               │
│  • Read calculator.c                                           │
│  • Add error handling to all functions                         │
│  • Run tests to verify                                         │
│  • Create a PR with changes                                    │
│                                                                 │
│  You can close this terminal. The agent will continue running. │
│  You'll be notified via email/dashboard when complete.         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Success Criteria

- [ ] Started interactive CLI session
- [ ] Successfully handed off a task with `&` prefix
- [ ] Received Cloud Agent ID and dashboard link
- [ ] Verified agent appears in `cursor.com/agents`
- [ ] (Optional) Waited for agent to complete
- [ ] (Optional) Reviewed results on dashboard

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Cloud handoff not available | Ensure Cloud Agents are enabled for your account (may require Team/Enterprise plan) |
| `&` not working | Make sure there's a space after `&` before your prompt |
| Agent not appearing in dashboard | Wait a few seconds and refresh. Check correct agent ID. |
| Agent failed | Check logs in dashboard for error messages |
| Can't find results | Completed agents show PRs and artifacts in dashboard |

---

## Key Takeaway

**Cloud handoff (`&`) turns your terminal into a launchpad for persistent, cloud-based AI agents.**

Use it for:
- Long-running tasks that would tie up your laptop
- Tasks you want to run while you're away
- Parallel execution of multiple agents
- Resource-intensive operations

---

## Bonus Challenge (If Time Permits)

Start multiple cloud agents in parallel:

```
> & Run all unit tests for the backend module
```

Then immediately (without waiting):

```
> & Generate documentation for the frontend module
```

Check `cursor.com/agents` – both should be running simultaneously.

Or create a script that hands off tasks based on conditions:

```bash
#!/bin/bash
# auto-handoff.sh

if [ "$1" == "long" ]; then
    agent -p "& $2"  # Hand off to cloud for long tasks
else
    agent -p "$2"    # Run locally for short tasks
fi
```

---

## Exercise Complete ✓

Check off when done:
- [ ] Handed off task with `&` prefix
- [ ] Received Cloud Agent ID
- [ ] Verified agent in web dashboard
- [ ] (Optional) Waited for completion
- [ ] (Optional) Reviewed results
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 22 – CLI – List & Resume

---

## Quick Reference: Cloud Handoff Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                   CLOUD HANDOFF CHEAT SHEET                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  HOW TO HANDOFF:                                                │
│  In interactive CLI: > & your prompt here                       │
│  In one-shot mode:  agent -p "& your prompt here"              │
│                                                                 │
│  EXAMPLE:                                                       │
│  > & Refactor the authentication module and run all tests      │
│                                                                 │
│  MONITORING:                                                    │
│  Web dashboard: https://cursor.com/agents                      │
│  CLI status:    agent ls --cloud                               │
│  Resume:        agent --resume <agent-id>                      │
│                                                                 │
│  WHEN TO USE CLOUD HANDOFF:                                     │
│  ✅ Long-running tasks (>10 minutes)                           │
│  ✅ Tasks that should continue after you close terminal        │
│  ✅ Multiple parallel tasks                                     │
│  ✅ Resource-intensive operations                              │
│  ❌ Quick questions (use local agent)                          │
│  ❌ Interactive debugging                                       │
│                                                                 │
│  WHAT YOU GET:                                                  │
│  • Agent runs in cloud VM                                       │
│  • Persists after terminal close                               │
│  • Email/dashboard notifications                               │
│  • PRs created automatically                                   │
│  • Artifacts (screenshots, logs) available                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
