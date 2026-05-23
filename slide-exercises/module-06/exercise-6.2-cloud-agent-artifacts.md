# Exercise 6.2: Cloud Agent Artifacts

**Module 6:** Cloud Agents in the UI  
**Slides:** `slides/module-06-marp.md` (Lesson 6.2)  
**Time:** 25 min  
**Difficulty:** Beginner

**Objective:** Collect and download artifacts produced by Cloud Agents.

---

> **Cloud Agents setup:** Already covered in [Exercise 6.1](../module-06/exercise-6.1-launching-a-cloud-agent.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**Step 1:** Launch agent that generates artifacts:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Generate:
1. api_documentation.md — OpenAPI-style docs for all endpoints
2. test_report.json — test suite summary
3. screenshot.png — main UI screenshot (if applicable)
4. dependencies.txt — all packages and versions

Place all in artifacts/ directory.
```

---

**Step 2:** After completion, view artifact list in UI with Download buttons and **Download All (zip)**
**Where:** **Cursor Agent panel** — ``Ctrl+L``

---

**Platform:** Windows 10/11 · Agent → ``Ctrl+L`` · Shell → **PowerShell** · Browser for dashboards

**Step 3:** Download individual artifacts
**Where:** **Cursor Agent panel** — ``Ctrl+L``

**Step 4:** Download all as zip
**Where:** **Cursor Agent panel** — ``Ctrl+L``

---

**Step 5:** Preview in browser:
**Where:** **Web browser** — Edge or Chrome
- Markdown → rendered HTML
- Images → inline preview
- JSON → formatted tree view

---

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
# List artifacts
curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts" | jq '.'

# Download specific artifact
DOWNLOAD_URL=$(curl -s -u "$CURSOR_USER_API_KEY:" \
  ".../artifacts/download?path=artifacts/report.md" | jq -r '.url')
curl -L -o report.md "$DOWNLOAD_URL"
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

Create `bin/process-artifacts.sh` to batch-download all artifacts for an agent ID.

---



```yaml
# GitHub Actions — download test results from completed agent
- name: Download Cloud Agent artifacts
  run: |
    curl -s -u "${{ secrets.CURSOR_API_KEY }}:" \
      ".../artifacts/download?path=test_results.xml" > test_results.xml
```

---

## Success criteria

- [ ] name: Download Cloud Agent artifacts
- [ ] Generated artifacts · downloaded single + zip · accessed via API

---

## Additional reference

## What are Artifacts?

| Aspect | Description |
|--------|-------------|
| **Definition** | Files produced by a Cloud Agent during its run |
| **Purpose** | Show what the agent did, verify results, debug failures |
| **Types** | Screenshots, videos, logs, output files, test results |
| **Storage** | Cloud storage, accessible via dashboard |
| **Retention** | Available for the life of the agent |

---

## Types of Artifacts

| Artifact Type | Description | When Produced |
|---------------|-------------|---------------|
| **Screenshots** | Images of browser/UI state | When agent uses browser tool |
| **Videos** | Recording of agent's actions | For complex UI interactions |
| **Logs** | Terminal output, build logs | Always |
| **Build artifacts** | Compiled binaries, packages | After compilation |
| **Test reports** | Pass/fail results | After running tests |
| **Generated files** | Code, documentation, configs | Always |
| **PR summary** | Link and description of changes | Always |

---

## Step 1: Access Artifacts from Dashboard

1. Go to `cursor.com/agents`
2. Click on a completed Cloud Agent
3. Look for the **"Artifacts"** tab or section

**Expected view:**
```
┌─────────────────────────────────────────────────────────────────┐
│  Agent: ca_abc123xyz - Completed                                │
├─────────────────────────────────────────────────────────────────┤
│  Status: ✅ Completed                      Duration: 2m 34s     │
│  Started: 2025-01-15 10:30:45            PR: #123               │
├─────────────────────────────────────────────────────────────────┤
│  ARTIFACTS                                                      │
│                                                                 │
│  📸 Screenshots (3)                                             │
│     ├── screenshot_before.png (845 KB) - View                  │
│     ├── screenshot_during.png (923 KB) - View                  │
│     └── screenshot_after.png (891 KB) - View                   │
│                                                                 │
│  📋 Logs (2)                                                    │
│     ├── agent_log.txt (124 KB) - Download                      │
│     └── build_log.txt (45 KB) - Download                       │
│                                                                 │
│  📄 Generated Files (1)                                         │
│     └── README.md (2 KB) - Download                            │
│                                                                 │
│  📊 Test Results (1)                                            │
│     └── test_report.json (4 KB) - View                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step 2: View Screenshots

Click on a screenshot artifact.

**What you see:**
- Full-size image of what the agent saw
- Often shows browser state, UI, or terminal output
- Can be downloaded for documentation

**Useful for:**
- Verifying UI changes
- Debugging visual issues
- Documenting agent's work

---

## Step 3: Examine Logs

Click or download a log artifact.

**What you see:**
```
[10:30:45] Agent started
[10:30:47] Cloning repository https://github.com/your-username/calculator
[10:30:52] Repository cloned successfully
[10:30:53] Reading calculator.c
[10:31:05] Reading calculator.c: found 8 functions
[10:31:10] Adding modulo function to calculator.c
[10:31:25] Added modulo function (lines 45-52)
[10:31:30] Running tests...
[10:31:35] Tests: 4 passed, 0 failed
[10:31:40] Creating pull request...
[10:31:45] PR created: https://github.com/your-username/calculator/pull/123
[10:31:50] Agent completed successfully
```

**Useful for:**
- Understanding agent's decision process
- Debugging agent failures
- Auditing agent actions

---

## Step 4: Review Generated Files

Download generated files (code, documentation, configs).

**Example: Generated README.md**
```markdown
# Calculator

A simple command-line calculator program written in C.

## Features
- Addition, subtraction, multiplication, division
- Error handling for division by zero
- Modulo operation (added by Cursor Agent)

## Building
```bash
gcc -o calculator calculator.c
```

## Usage
```bash
./calculator
```
```

**Useful for:**
- Reviewing changes before merging
- Understanding what was added/modified
- Quality control

---

## Artifacts in GitHub PRs

If your Cloud Agent created a PR, artifacts may be embedded:

```
┌─────────────────────────────────────────────────────────────────┐
│  cursor[bot] commented 5 minutes ago                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  I've completed the requested changes.                         │
│                                                                 │
│  📸 Screenshot of change:                                       │
│  [Image: calculator_menu_with_modulo.png]                      │
│                                                                 │
│  📋 Test results:                                               │
│  All 5 tests passed.                                           │
│                                                                 │
│  📄 Files changed:                                              │
│  • calculator.c (+12 lines)                                    │
│  • README.md (+5 lines)                                        │
│                                                                 │
│  View full details: https://cursor.com/agents/ca_abc123xyz     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Artifact Inspection Checklist

| Item | What to Check |
|------|---------------|
| **Screenshots** | Does the UI look correct? Any unexpected changes? |
| **Logs** | Any errors or warnings? Did all steps complete? |
| **Generated code** | Does it follow project style? Is it correct? |
| **Test results** | All tests passing? Coverage improved? |
| **Build artifacts** | Size, performance, dependencies? |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No artifacts shown | Not all agents produce artifacts. Try a task that uses browser or generates files |
| Artifacts won't load | Check internet connection; try refreshing page |
| Screenshot blank | Agent may have opened empty page. Check logs for URL used |
| Can't download artifact | Click the download icon or right-click → Save As |
| Artifacts not embedding in PR | Check dashboard settings for "Allow posting artifacts to GitHub" |

---

## Key Takeaway

**Artifacts are proof of the agent's work – screenshots, logs, and files that show exactly what happened.**

Always review artifacts before merging a Cloud Agent's PR to ensure:
- The agent did what you asked
- No unexpected changes were made
- All tests passed
- Quality meets your standards

---

## Bonus Challenge (If Time Permits)

Use artifacts to debug a failed agent:

1. Run a Cloud Agent with a prompt that might fail (e.g., "Fix the nonexistent function")
2. When it fails, examine the logs
3. Identify the error from the log
4. Fix the issue and re-run the agent

Or create a report from artifacts:

> *"Download all artifacts from the last 5 Cloud Agents and create a summary of what each one accomplished"*

---

## Congratulations! Training Complete ✓

You have completed all 25 exercises:

| Track | Exercises |
|-------|-----------|
| Track 1: Fundamentals | 1-8 |
| Track 2: Agent Tools | 9-13 |
| Track 3: Customization | 14-18 |
| Track 4: CLI & Automation | 19-22 |
| Track 5: Cloud Agents | 23-25 |

**What you can now do:**
- ✅ Use Agent to understand and modify code
- ✅ Create rules, skills, and subagents
- ✅ Use CLI for automation
- ✅ Launch and monitor Cloud Agents
- ✅ Integrate with Slack

---

## Quick Reference: Artifacts Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                    ARTIFACTS CHEAT SHEET                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ACCESS ARTIFACTS:                                              │
│  cursor.com/agents → Select agent → Artifacts tab              │
│                                                                 │
│  ARTIFACT TYPES:                                                │
│  📸 Screenshots - What agent saw in browser                     │
│  📋 Logs - Agent actions and decisions                          │
│  📄 Generated Files - Code, docs, configs                       │
│  📊 Test Results - Pass/fail, coverage                          │
│  🎥 Videos - Recording of agent actions                         │
│  📦 Build Artifacts - Binaries, packages                        │
│                                                                 │
│  WHAT TO CHECK:                                                 │
│  □ Screenshots: Visual correctness                              │
│  □ Logs: No errors or warnings                                  │
│  □ Generated code: Style, correctness, tests                    │
│  □ Test results: All passing                                    │
│                                                                 │
│  ARTIFACTS IN PRs:                                              │
│  Cloud Agent comments on PR with:                               │
│  • Screenshots of changes                                       │
│  • Test results                                                │
│  • Summary of what was done                                     │
│                                                                 │
│  TROUBLESHOOTING:                                               │
│  • No artifacts → Agent may not have produced any               │
│  • Blank screenshots → Check URL in logs                        │
│  • Can't download → Try different browser                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
