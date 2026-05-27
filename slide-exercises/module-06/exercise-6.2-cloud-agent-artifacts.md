# Exercise 6.2: Cloud Agent Artifacts

**Module 6:** Cloud Agents in the UI  
**Slides:** `slides/course-complete-marp-with-notes.md` (Module 6, Lesson 6.2)  
**Time:** 25 min  
**Difficulty:** Beginner

**Objective:** Collect and download artifacts produced by Cloud Agents.

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
**Environment:** Windows 10/11 · **PowerShell** · use **`curl.exe`** (not the `curl` alias)

**Before API calls:** set your key (replace with your real key):

```powershell
$env:CURSOR_USER_API_KEY = "cursor_your_key_here"
# Admin exercises use:
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_your_key_here"
```

Follow each step in order. Confirm the **Expected result** before moving on.

### Step 1 — Launch an agent that creates artifacts

**Do this:** New Cloud Agent with this prompt:

```
Generate:
1. api_documentation.md — API-style docs for main endpoints
2. test_report.json — test summary (real or plausible for demo)
3. dependencies.txt — packages and versions

Place all files in an artifacts/ folder in the repo.
```

**Expected result:** Run completes; **Artifacts** tab or section lists files.

---

### Step 2 — Download from the UI

**Do this:** On the completed run: download **one file**, then try **Download All (zip)** if shown.

**Expected result:** Files save to your **Downloads** folder; zip opens in File Explorer.

---

### Step 3 — Preview in browser

**Do this:** Open `.md` / `.json` from the UI preview if available.

**Expected result:** Markdown renders; JSON is readable.

---

### Step 4 — List artifacts via API (PowerShell)

**Do this:** Set IDs from the dashboard, then:

```powershell
$env:AGENT_ID = "your_agent_id_here"
curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" `
  "https://api.cursor.com/v1/agents/$($env:AGENT_ID)/artifacts"
```

**Expected result:** JSON listing artifact paths (use `ConvertFrom-Json` if helpful).

---

### Step 5 — Download one artifact via API (optional)

**Do this:** Follow the lab guide’s presigned-URL pattern with `curl.exe -L -o filename ...`.

**Expected result:** File saved locally; matches UI download.

**Success criteria:** Artifacts created · downloaded in UI · listed via API
---

## Success criteria

- [ ] name: Download Cloud Agent artifacts
- [ ] Generated artifacts · downloaded single + zip · accessed via API

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open `cursor.com/agents` dashboard | List of Cloud Agents appears |
| 2 | Select a completed Cloud Agent | Agent details page opens |
| 3 | Navigate to "Artifacts" section | List of produced artifacts |
| 4 | Click on different artifact types | View screenshots, logs, outputs |
| 5 | Download artifacts (if needed) | Files saved to your computer |

---

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
`gcc -o calculator calculator.c`

## Usage
`./calculator`
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

## Success Criteria

- [ ] Accessed artifacts from a completed Cloud Agent
- [ ] Viewed at least one screenshot
- [ ] Examined log file
- [ ] Downloaded a generated file
- [ ] Understood what each artifact type shows

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

## Exercise Complete ✓

Check off when done:
- [ ] Viewed screenshots from Cloud Agent
- [ ] Examined log files
- [ ] Downloaded generated files
- [ ] Understood artifact types and their purposes
- [ ] (Optional) Completed bonus challenge

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
