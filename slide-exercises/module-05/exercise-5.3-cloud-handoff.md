# Exercise 5.3: Cloud Handoff

**Module 5:** Cursor CLI and Local Automation  
**Slides:** `slides/course-complete-marp-with-notes.md` (Module 5, Lesson 5.3)  
**Time:** 18 min  
**Difficulty:** Beginner

**Objective:** Hand off a local CLI task to a Cloud Agent with &.

---

## CLI basics (read this first)

**Demonstration (Windows):**

1. Open **PowerShell** in Cursor: ``Ctrl+` `` → select **PowerShell**.
2. Confirm the CLI is installed: `agent --version`
3. If missing, install Cursor CLI for Windows:
   ```powershell
   irm 'https://cursor.com/install?win32=true' | iex
   ```
   Or use **Command Palette** → `Shell Command: Install 'cursor' command in PATH`.
4. Run commands from your **project root** unless the exercise says otherwise.

**Note:** Bash script examples (`.sh`) in reference sections are optional on Windows — use PowerShell or ask the Agent to adapt commands.


---

## Steps from the training slides

**Environment:** Windows 10/11 · **PowerShell** in Cursor (``Ctrl+` `` → **PowerShell**)

Follow each step in order. Confirm the **Expected result** before moving on.

### Step 1 — Start CLI and hand off to Cloud

**Do this:**

```powershell
agent
```

At the `>` prompt, type (note the **`&` at the start**):

```
& Analyze the entire codebase and create a dependency graph.
```

**Expected result:** Message that a **Cloud Agent** started, plus an **Agent ID** and a `https://cursor.com/agents/...` link.

---

### Step 2 — Verify in the browser

**Do this:** Open the link in **Edge** or **Chrome**.

**Expected result:** Dashboard shows the agent **Running** (or **Completed** later). This page is the **primary** way to know when the run finishes.

---

### Step 3 — Close terminal safely

**Do this:** You may close the terminal or type `/quit`. The cloud task should keep running.

**Expected result:** Status on the web dashboard still progresses without your laptop CLI attached.

---

### Step 4 — Hand off an existing conversation

**Do this:** In a new `agent` session, after some local messages:

```
& Continue this conversation in the cloud. I need to log off.
```

**Expected result:** Handoff confirmation and cloud URL.

---

### Step 5 — One-shot cloud handoff

**Do this:**

```powershell
agent -p "& Refactor the auth module to use JWT. Update all tests and docs."
```

**Expected result:** Cloud agent launched from a single command (same `&` semantics).

---

### Step 6 — Resume later

**Do this:** Copy the agent ID from the dashboard, then:

```powershell
agent --resume YOUR_AGENT_ID_HERE
```

**Expected result:** Session resumes or shows cloud status (per your plan/features).

**Success criteria:** Handoff with `&` · dashboard link · agent continues after terminal closed
---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

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
Monitor completion at https://cursor.com/agents (status → Completed or Failed).
```

---

### Method 2: One-Shot with Cloud Handoff

```bash
agent -p "& Refactor the divide function to include division by zero checking"
```

The `&` works the same way – sends the task to the cloud.

---

## Monitoring Your Cloud Agent

### When the agent finishes (notifications)

| Channel | What to expect |
|---------|----------------|
| **Web dashboard** | Always — open your agent URL at `https://cursor.com/agents` and refresh until status is **Completed** or **Failed** |
| **Email** | Optional — only if enabled in your Cursor / cloud-agent notification settings (not guaranteed for every CLI `&` handoff) |
| **Slack** | Optional — if your workspace has the Cursor Slack app configured |
| **API / webhooks** | For automation — poll the API or configure webhooks (see Module 8) |

> **Teaching note:** Do not promise learners will always get email. Point them at the dashboard link from the handoff message first.

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
│  Check cursor.com/agents for status (email/Slack if enabled).  │
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
│  • Dashboard status (always); email/Slack if configured        │
│  • PRs created automatically                                   │
│  • Artifacts (screenshots, logs) available                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Troubleshooting (common beginner issues)

| Problem | What to try |
|---------|-------------|
| Agent panel won't open | Click inside Cursor first; try `Ctrl+Shift+P` → **Open Agent** |
| No diff appears | Switch from Ask Mode to **Agent Mode** in the panel footer |
| Agent can't see my files | **File → Open Folder** (not a single file) |
| Wrong terminal shell | ``Ctrl+` `` → **Terminal: Select Default Profile** → **PowerShell** |
| `curl` fails or behaves oddly | Use **`curl.exe`** in PowerShell, not the `curl` alias |
| `gcc` not found | Install [MinGW-w64](https://www.mingw-w64.org/) or MSVC build tools; restart terminal |
| `.sh` script won't run | On Windows use the matching `.bat` file or PowerShell commands |
| API returns 401 | Re-copy API key; check `Authorization: Bearer` header |
| API returns 429 | Wait and retry; see Exercise 7.3 for backoff |

---

## Exercise complete

- [ ] Finished all steps above
- [ ] Checked success criteria
- [ ] Noted one thing you would do differently on a real project
