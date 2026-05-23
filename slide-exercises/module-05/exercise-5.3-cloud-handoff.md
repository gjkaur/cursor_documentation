# Exercise 5.3: Cloud Handoff

**Module 5:** Cursor CLI and Local Automation  
**Slides:** `slides/module-05-marp.md` (Lesson 5.3)  
**Time:** 18 min  
**Difficulty:** Beginner

**Objective:** Hand off a local CLI task to a Cloud Agent with &.

---

> **CLI basics:** Already covered in [Exercise 5.1](../module-05/exercise-5.1-interactive-cli.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)

**Step 1:** Start local session and hand off:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent
& "Analyze the entire codebase and create a dependency graph."
```

---

**Step 2:** Verify handoff:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```
🚀 Handing off to Cloud Agent...
✅ Session running at: https://cursor.com/agents/[agent-id]
```

---

**Step 3:** Check status via browser or CLI
**Where:** **Web browser** — Edge or Chrome

---

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)

**Step 4:** Push existing conversation:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```
& "Continue this conversation in the cloud. I need to log off."
```

---

**Step 5:** Long-running task:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent "& Refactor the auth module to use JWT. Update all tests and docs."
```

---

**Step 6:** Resume later:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent --resume [agent-id-from-cloud]
```

---

## Additional reference

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
