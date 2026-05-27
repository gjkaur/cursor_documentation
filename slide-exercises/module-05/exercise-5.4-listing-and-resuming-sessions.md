# Exercise 5.4: Listing and Resuming Sessions

**Module 5:** Cursor CLI and Local Automation  
**Slides:** `slides/course-complete-marp-with-notes.md` (Module 5, Lesson 5.4)  
**Time:** 20 min  
**Difficulty:** Beginner

**Objective:** List, name, resume, and compress CLI Agent sessions.

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

**Demonstration (Windows):** Follow steps in **PowerShell** unless a step says otherwise. Agent panel: ``Ctrl+I`` · Terminal: ``Ctrl+` ``.

Follow these steps in order. Copy prompts exactly unless the exercise tells you to adapt them.

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)

**Step 1:** Create multiple named sessions:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent "Just say one word: frontend-cleanup"   # do work, exit
agent "Just say one word: db-optimization"  # do work, exit
agent "Just say one word: docs-update"
```

---

**Step 2:** List all sessions:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```
/resume
# 1. frontend-cleanup Agent (2 hours ago)
# 2. db-optimization Agent (1 hour ago)
# 3. docs-update Agent (30 minutes ago)
```

---

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)

**Step 3:** Resume by ID:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent --resume abc123-def456-ghi789
```

---

**Step 4:** Concurrent sessions in different terminals:
**Where:** **Agent panel** — ``Ctrl+I``

```bash
# Terminal 1: agent --resume frontend-cleanup
# Terminal 2: agent --resume db-optimization
```

---

**Step 5:** Context management:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```
/compress   # Summarize conversation, free context window
```

---

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

**Step 6:** Export session summary as markdown
**Where:** **Agent panel** — ``Ctrl+I``

**Step 7:** Create `scripts/cursor-sessions.ps1` to list and manage sessions (optional `.sh` on Mac/Linux)
**Where:** **Agent panel** — ``Ctrl+I``

**Naming:** Use `[area]-[task]` format (e.g., `api-auth-fix`)

**Context:** Use `/compress` on long sessions · cloud handoff for very long tasks

**Cleanup:** Sessions persist indefinitely — manually complete or discard finished ones

**Success Criteria:** Created named sessions · listed with `/resume` · resumed · used `/compress`

---

## Success criteria

- [ ] Created named sessions · listed with `/resume` · resumed · used `/compress`

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open your terminal | Command prompt appears |
| 2 | Run `agent ls` to list previous sessions | List of past conversations appears |
| 3 | Pick a session ID from the list | Session identified |
| 4 | Run `agent --resume <session-id>` | Conversation continues from where it left off |
| 5 | Run `agent --continue` to resume most recent | Latest conversation resumes |

---

## What are CLI Sessions?

| Aspect | Description |
|--------|-------------|
| **Session** | A complete conversation with the Agent |
| **Saved automatically** | Every interactive session is saved |
| **Contains** | Full conversation history, context, file state |
| **Session ID** | Unique identifier (timestamp or hash) |
| **Resume** | Pick up exactly where you left off |

---

## List Previous Sessions

### Command

```bash
agent ls
```

**Expected output:**

```
┌─────────────────────────────────────────────────────────────────┐
│  CURSOR CLI SESSIONS                                            │
├─────────────────────────────────────────────────────────────────┤
│  ID                  | DATE          | STATUS   | MESSAGES      │
│  2025-01-15-10-30-45 | Jan 15 10:30  | Complete | 12            │
│  2025-01-14-16-20-12 | Jan 14 16:20  | Complete | 8             │
│  2025-01-13-09-15-30 | Jan 13 09:15  | Complete | 5             │
│  2025-01-12-14-45-00 | Jan 12 14:45  | Complete | 23            │
└─────────────────────────────────────────────────────────────────┘

Run: agent --resume <id> to continue a session
```

### With Cloud Agents

```bash
agent ls --cloud
```

**Expected output:**

```
┌─────────────────────────────────────────────────────────────────┐
│  CLOUD AGENT SESSIONS                                           │
├─────────────────────────────────────────────────────────────────┤
│  AGENT ID            | STATUS    | CREATED      | OUTPUT        │
│  ca_abc123xyz        | Completed | Jan 15 10:30 | PR #123       │
│  ca_def456uvw        | Running   | Jan 15 11:00 | In progress   │
│  ca_ghi789rst        | Failed    | Jan 14 16:20 | Error: build  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Resume a Session

### Resume Most Recent Session

```bash
agent --continue
```

or

```bash
agent resume
```

**Expected behavior:** Continues your most recent conversation as if you never left.

### Resume Specific Session by ID

```bash
agent --resume 2025-01-15-10-30-45
```

**Expected behavior:** Loads that exact conversation, including all previous messages and context.

---

## Complete Example Workflow

### Session 1 (Morning)

```bash
$ agent

> Explain the main function in calculator.c

[Agent explains]

> Add error handling to the divide function

[Agent makes changes]

> /quit

Goodbye!
```

### Later That Day (After Lunch)

```bash
$ agent ls

ID: 2025-01-15-10-30-45 | Date: Jan 15 10:30 | Messages: 4

$ agent --resume 2025-01-15-10-30-45

Resuming session from Jan 15 10:30
Continuing conversation...

> Now also add error handling to the other functions

[Agent continues where you left off]
```

---

## Session Management Commands

| Command | Description |
|---------|-------------|
| `agent ls` | List all local sessions |
| `agent ls --cloud` | List cloud agent sessions |
| `agent --continue` | Resume most recent session |
| `agent resume` | Same as `--continue` |
| `agent --resume <id>` | Resume specific session by ID |
| `agent --clear` | Clear conversation history (start fresh) |
| `/clear` | Clear current conversation (in interactive mode) |

---

## Why Resume Sessions?

| Benefit | Description |
|---------|-------------|
| **Context preservation** | Agent remembers everything discussed |
| **Time savings** | No need to re-explain the problem |
| **Multi-session workflows** | Complex tasks across multiple days |
| **Experiment tracking** | Return to previous attempts |
| **Team collaboration** | Share session IDs (coming soon) |

---

## Success Criteria

- [ ] Ran `agent ls` and saw previous sessions
- [ ] Identified a session to resume
- [ ] Used `agent --continue` to resume most recent
- [ ] Agent remembered previous conversation
- [ ] Used `agent --resume <id>` for a specific session
- [ ] (Optional) Used `agent ls --cloud` to see cloud agents

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `agent ls` shows no sessions | You need at least one previous conversation. Start and quit a session first |
| Session not found | Check the ID exactly as shown. Use `agent ls` to verify |
| Resumed session doesn't remember context | Make sure you're using the correct session ID |
| Can't resume cloud agent | Cloud agents are resumed via `--resume` with agent ID, not session ID |
| Session corrupted | Start a new session with `/new-chat` in interactive mode |

---

## Key Takeaway

**Session management lets you pause and resume conversations – just like saving your game progress.**

Use it when:
- You need to step away from a complex task
- You want to continue a conversation the next day
- You're experimenting with different approaches
- You need to share context across multiple terminal sessions

---

## Bonus Challenge (If Time Permits)

Create a session, add some context, then resume it in a different terminal:

**Terminal 1:**

```bash
$ agent
> Remember that the divide function needs division by zero checking
> /quit
```

**Terminal 2:**

```bash
$ agent ls
$ agent --continue
> What did we discuss about the divide function?
```

The Agent should remember the previous discussion.

Or script session management:

```bash
#!/bin/bash
# resume-latest.sh
LATEST=$(agent ls | tail -1 | awk '{print $1}')
agent --resume "$LATEST"
```

---

## Exercise Complete ✓

Check off when done:
- [ ] Ran `agent ls` and saw sessions
- [ ] Used `agent --continue` to resume most recent
- [ ] Agent remembered previous conversation
- [ ] Used `agent --resume <id>` for specific session
- [ ] (Optional) Ran `agent ls --cloud`
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 23 – Launch Cloud Agent (Web Dashboard)

---

## Quick Reference: Session Management Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                 SESSION MANAGEMENT CHEAT SHEET                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  LIST SESSIONS:                                                 │
│  agent ls                 # Local sessions                      │
│  agent ls --cloud         # Cloud agent sessions                │
│                                                                 │
│  RESUME SESSIONS:                                               │
│  agent --continue         # Most recent session                 │
│  agent resume             # Same as above                       │
│  agent --resume <id>      # Specific session by ID              │
│                                                                 │
│  SESSION ID FORMATS:                                            │
│  Local: 2025-01-15-10-30-45 (timestamp)                         │
│  Cloud: ca_abc123xyz (agent ID)                                 │
│                                                                 │
│  INTERACTIVE COMMANDS:                                          │
│  /clear      - Clear current conversation                       │
│  /new-chat   - Start a brand new session                        │
│  /quit       - Save and exit                                    │
│                                                                 │
│  TYPICAL WORKFLOW:                                              │
│  Morning:                                                       │
│  $ agent                                                        │
│  > Work on feature X...                                         │
│  > /quit                                                        │
│                                                                 │
│  After lunch:                                                   │
│  $ agent --continue                                             │
│  > Continue with feature X...                                   │
│                                                                 │
│  SESSION BENEFITS:                                              │
│  • No need to re-explain context                                │
│  • Complex tasks across multiple sessions                       │
│  • Experiment without losing progress                           │
│  • Resume after computer restart                                │
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
