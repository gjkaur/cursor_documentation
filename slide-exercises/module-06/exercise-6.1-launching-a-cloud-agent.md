# Exercise 6.1: Launching a Cloud Agent

**Module 6:** Cloud Agents in the UI  
**Slides:** `slides/course-complete-marp-with-notes.md` (Module 6, Lesson 6.1)  
**Time:** 25 min  
**Difficulty:** Beginner

**Objective:** Launch a Cloud Agent from the Cursor UI and track its run.

---

## Cloud Agents in the UI (read this first)

**Demonstration (Windows):**

1. Sign in to Cursor with a plan that includes **Cloud Agents**.
2. Open the **Cloud Agents** view from the Cursor sidebar (or **Command Palette** → "Cloud Agents").
3. Keep the web dashboard open in your browser: [cursor.com/agents](https://cursor.com/agents).
4. Use the **Agent panel** (`Ctrl+I`) for local prompts; use the Cloud UI for remote runs.
5. API steps in related modules use **PowerShell** with `$env:VAR` and `curl.exe`.


---

## Steps from the training slides

**Environment:** Windows · **Cursor app** + web browser (Edge or Chrome)

Follow each step in order. Confirm the **Expected result** before moving on.

| Where | What |
|-------|------|
| Cursor sidebar | **Cloud** / cloud icon, or **Command Palette** (`Ctrl+Shift+P`) → **Cloud Agents** |
| Browser | [https://cursor.com/agents](https://cursor.com/agents) |

### Step 1 — Open Cloud Agents

**Do this:** In Cursor, open **Cloud Agents**. Also open [cursor.com/agents](https://cursor.com/agents) in your browser.

**Expected result:** Empty list or previous runs; **+ New** (or **New Agent**) is visible.

---

### Step 2 — Create a new agent

**Do this:** Click **+ New** and fill in:

| Field | Example |
|-------|---------|
| Repository | `https://github.com/YOUR_ORG/YOUR_REPO` |
| Branch | `main` |
| Prompt | See below |
| Model | `claude-4.6-sonnet` (or course default) |
| Auto-create PR | Off for first try |

**Prompt to paste:**

```
Read README and main source files. Summarize:
- What this project does
- Key dependencies
- How to run locally
- Common issues
```

**Expected result:** Agent status **Running**; log lines appear (clone repo, read files, etc.).

---

### Step 3 — Watch the live log

**Do this:** Keep the run page open 2–5 minutes.

**Expected result:** Timestamped log lines; eventual **Completed** (or clear error).

---

### Step 4 — Review settings (gear icon)

**Do this:** Open settings and note: default model, auto-PR, notifications, webhook URL, max runtime.

**Expected result:** You know where to change defaults for the next run.

---

### Step 5 — Optional: run with auto-PR

**Do this:** New agent with **Auto-create PR** on and prompt:

```
Add CONTRIBUTING.md with dev setup, tests, PR process, and code style
```

**Expected result:** Completed run may show a PR link on the dashboard.

---

### Step 6 — Share the run URL

**Do this:** Copy the agent URL from the browser address bar for a teammate.

**Expected result:** URL format like `https://cursor.com/agents/agt_...` opens the same run when signed in.

**Success criteria:** Launched agent · watched log · understand settings · optional PR run
---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open browser to `cursor.com/agents` | Cloud Agents dashboard loads |
| 2 | Click "New Agent" button | Agent creation form opens |
| 3 | Select your repository | Repository connected to Cursor |
| 4 | Enter a prompt describing the task | Prompt saved |
| 5 | Click "Start" | Cloud Agent begins running |
| 6 | Monitor progress | Status updates in real-time |

---

## What is the Cloud Agents Dashboard?

| Aspect | Description |
|--------|-------------|
| **URL** | `cursor.com/agents` |
| **Purpose** | Launch and monitor Cloud Agents from any browser |
| **No local setup** | Works on any device with internet |
| **Real-time status** | See agent progress, logs, and results |
| **Results** | PRs, artifacts, logs available when complete |

---

## Step 1: Access the Dashboard

Open your browser and navigate to:

```
https://cursor.com/agents
```

**Expected view:**
- List of existing Cloud Agents (if any)
- "New Agent" button
- Status indicators for running agents

---

## Step 2: Create a New Cloud Agent

Click the **"New Agent"** button.

**Fill out the form:**

| Field | What to Enter |
|-------|---------------|
| **Repository** | Select your GitHub repo (e.g., `your-username/calculator`) |
| **Branch** | Select branch (e.g., `main`) |
| **Prompt** | Describe the task (see examples below) |
| **Model** | Select model (**Composer 2.5** recommended) |

---

## Sample Prompts to Try

### Option A: Documentation

> *"Add a comprehensive README.md file explaining how to build and run the calculator program. Include usage examples."*

### Option B: Feature Addition

> *"Add a new 'power' function that calculates exponentiation. Add it to the menu as option 5. Update the README."*

### Option C: Code Improvement

> *"Review all functions in calculator.c. Add input validation, error handling for division by zero, and comments for each function."*

### Option D: Testing

> *"Create unit tests for all arithmetic functions. Run the tests and fix any failures."*

### Option E: Refactoring

> *"Split calculator.c into multiple files: main.c, operations.c, and input.c. Update the build instructions."*

---

## Step 3: Monitor Progress

After clicking "Start", the dashboard shows:

```
┌─────────────────────────────────────────────────────────────────┐
│  ☁️  CLOUD AGENT RUNNING                                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Agent ID: ca_abc123xyz                                         │
│  Status: 🔄 Running                                             │
│  Started: 2025-01-15 10:30:45                                  │
│  Repository: your-username/calculator                          │
│  Branch: feature/cursor-agent-123                              │
│                                                                 │
│  📋 Activity Log:                                               │
│  [10:30:45] Agent started                                       │
│  [10:30:47] Cloning repository...                              │
│  [10:30:52] Reading calculator.c...                            │
│  [10:31:05] Adding README.md...                                 │
│  [10:31:30] Creating commit...                                  │
│  [10:31:35] Opening pull request...                             │
│                                                                 │
│  📎 Artifacts:                                                  │
│  • Screenshot_1.png (click to view)                            │
│  • build_log.txt (click to view)                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step 4: View Results

When the agent completes, you will see:

| Result Type | Description |
|-------------|-------------|
| **Pull Request** | Link to GitHub PR with changes |
| **Artifacts** | Screenshots, logs, output files |
| **Status** | Completed / Failed |
| **Duration** | Total run time |

---

## Dashboard Features

| Feature | Description |
|---------|-------------|
| **Real-time logs** | See agent activity as it happens |
| **Cancel button** | Stop a running agent |
| **View PR** | Direct link to GitHub pull request |
| **Download artifacts** | Save logs and outputs |
| **Re-run** | Run the same agent again |
| **Fork** | Create a new agent based on this one |

---

## Success Criteria

- [ ] Accessed `cursor.com/agents` dashboard
- [ ] Created a new Cloud Agent
- [ ] Selected repository and branch
- [ ] Entered a prompt and started the agent
- [ ] Monitored progress in real-time
- [ ] Viewed results (PR or artifacts)

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No repositories shown | Connect GitHub in dashboard Integrations first |
| Agent fails immediately | Check logs for error messages |
| Agent takes too long | Some tasks need time; check back later |
| No PR created | Agent may not have made changes or `autoCreatePR` not set |
| Can't find dashboard | Go to `cursor.com/agents` while logged in |

---

## Key Takeaway

**The Cloud Agents dashboard lets you launch AI agents from anywhere – no terminal, no local editor, no installation required.**

Use it when:
- You're away from your development machine
- You want to run a task without opening Cursor
- You need to monitor multiple agents
- You want to share agent results with teammates

---

## Bonus Challenge (If Time Permits)

Launch two Cloud Agents simultaneously on different tasks:

**Agent 1:**
> *"Add comments to all functions in calculator.c"*

**Agent 2 (after Agent 1 starts):**
> *"Create unit tests for calculator.c"*

Watch them run in parallel in the dashboard.

Or schedule a recurring task (if available in your plan):

> *"Set up a weekly Cloud Agent to run tests and report results"*

---

## Exercise Complete ✓

Check off when done:
- [ ] Accessed Cloud Agents dashboard
- [ ] Created and launched a Cloud Agent
- [ ] Monitored progress in real-time
- [ ] Viewed results (PR or artifacts)
- [ ] (Optional) Ran parallel agents
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 24 – Cloud Agent from Slack

---

## Quick Reference: Cloud Agents Dashboard Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                CLOUD AGENTS DASHBOARD CHEAT SHEET               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  DASHBOARD URL:                                                 │
│  https://cursor.com/agents                                      │
│                                                                 │
│  CREATE AN AGENT:                                               │
│  1. Click "New Agent"                                          │
│  2. Select repository and branch                               │
│  3. Enter prompt                                               │
│  4. Click "Start"                                              │
│                                                                 │
│  MONITORING:                                                    │
│  • Real-time logs                                              │
│  • Status indicators (running/completed/failed)                │
│  • Duration timer                                              │
│  • Cancel button                                               │
│                                                                 │
│  RESULTS:                                                      │
│  • Pull Request link (if created)                              │
│  • Artifacts (screenshots, logs)                               │
│  • Exit code and summary                                       │
│                                                                 │
│  SAMPLE PROMPTS:                                                │
│  • "Add error handling to all functions"                       │
│  • "Generate API documentation"                                │
│  • "Run tests and fix failures"                                │
│  • "Refactor the main function"                                │
│  • "Add a new feature: modulo operation"                       │
│                                                                 │
│  BENEFITS:                                                      │
│  • Works from any device                                       │
│  • No local installation required                              │
│  • Run multiple agents in parallel                             │
│  • Agents persist after browser closes                         │
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
