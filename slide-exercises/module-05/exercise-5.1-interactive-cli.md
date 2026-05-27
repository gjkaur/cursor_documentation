# Exercise 5.1: Interactive CLI

**Module 5:** Cursor CLI and Local Automation  
**Slides:** `slides/course-complete-marp-with-notes.md` (Module 5, Lesson 5.1)  
**Time:** 20 min  
**Difficulty:** Beginner

**Objective:** Start an interactive Cursor CLI session from the terminal.

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

**Step 1:** Start an interactive session
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent
agent "Help me understand the current codebase structure"
```

---

**Step 2:** Navigate the session (inside the running `agent` session — same terminal window) — unless step notes Git Bash or WSL
- Type prompts naturally
- `Shift+Enter` — new line without submitting
- `Enter` — submit prompt
- `Ctrl+D` twice — exit

---

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)

**Step 3:** Switch models:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```
/model
# Or list models outside session:
agent --list-models
```

---

**Step 4:** Ask Mode (read-only):
**Where:** **Agent panel** — ``Ctrl+I``

```bash
agent --mode=ask "What does this project's main function do?"
# Or inside session: /ask
```

---

**Step 5:** Plan Mode:
**Where:** **Agent panel** — ``Ctrl+I``

```bash
agent --mode=plan "Add user authentication to this API"
```

---

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)

**Step 6:** Configure status line:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
npx -y cursor-statusline
# Shows: [model: claude-4.5-sonnet] [~/project] [main] [ctx: 45k/200k]
```

---

**Step 7:** Terminal key bindings:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent /setup-terminal
```

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open your terminal | Command prompt appears |
| 2 | Type `agent` and press Enter | CLI starts in interactive mode |
| 3 | Type a prompt and press Enter | Agent responds in the terminal |
| 4 | Continue the conversation | Agent remembers context |
| 5 | Type `/quit` to exit | CLI session ends |

---

## What is the Cursor CLI?

| Aspect | Description |
|--------|-------------|
| **What it is** | Command-line interface to Cursor's Agent |
| **How to start** | Type `agent` in your terminal |
| **Interactive mode** | Chat with Agent directly in terminal |
| **Non-interactive mode** | One-shot commands for scripts (`agent -p "prompt"`) |
| **Same capabilities** | Read/write files, run commands, search code |

---

## Installation Check

Before starting, verify the CLI is installed:

```bash
agent --version
```

**Expected output:**
```
Cursor Agent version x.x.x
```

If not installed:

```bash
# macOS / Linux / WSL
curl https://cursor.com/install -fsS | bash

# Windows PowerShell
irm 'https://cursor.com/install?win32=true' | iex
```

---

## Start Interactive Mode

### Step 1: Launch the CLI

```bash
agent
```

**Expected output:**
```
Welcome to Cursor Agent. Type your questions or requests.
Working directory: /path/to/your/project
Type /help for commands, /quit to exit.

>
```

The `>` prompt indicates the CLI is ready for your input.

---

### Step 2: Ask a Question

Type a prompt and press Enter:

```
> What files are in this directory?
```

**Expected response:**
```
I'll list the files in the current directory.

Running: ls -la

[Output of ls command]

You have 5 files: calculator.c, math_utils.c, math_utils.h, README.md, and test_calculator.c.
```

---

### Step 3: Continue the Conversation

Ask a follow-up question (Agent remembers context):

```
> Explain what calculator.c does
```

**Expected response:**
```
Based on the file I saw earlier, calculator.c implements a simple calculator...

[Detailed explanation of the code]
```

---

### Step 4: Use CLI Commands

Type `/help` to see available commands:

```
> /help
```

**Expected output:**
```
Available commands:
  /help          - Show this help
  /quit          - Exit the CLI
  /model <name>  - Switch AI model
  /plan          - Switch to Plan mode
  /ask           - Switch to Ask mode
  /agent         - Switch to Agent mode
  /clear         - Clear conversation history
  /compress      - Summarize conversation to save context
```

---

### Step 5: Exit the CLI

```
> /quit
```

Or press `Ctrl+C` twice.

---

## Sample Interactive Session

```bash
$ agent

> What is the main function in calculator.c?

The main function is the entry point of the program. It:
1. Displays a menu of operations
2. Reads user input for choice and numbers
3. Calls the appropriate arithmetic function
4. Prints the result

> Add a comment at the top of the file

I'll add a comment at the top of calculator.c.

[Shows diff and asks for approval]

> y

Comment added successfully.

> /quit

Goodbye!
```

---

## CLI vs. Cursor Editor

| Feature | CLI | Editor |
|---------|-----|--------|
| **Interface** | Terminal | Graphical |
| **File viewing** | Command-line | Full editor |
| **Diff viewing** | Text-based | Visual diff |
| **Best for** | Quick tasks, automation, remote access | Full development |
| **Same Agent capabilities** | Yes | Yes |

---

## Success Criteria

- [ ] CLI is installed (`agent --version` works)
- [ ] Started interactive mode (`agent`)
- [ ] Asked a question and received response
- [ ] Asked a follow-up question (context maintained)
- [ ] Used `/help` to see commands
- [ ] Exited with `/quit`

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `agent: command not found` | Install CLI or add `~/.local/bin` to PATH |
| Authentication error | Run `agent login` in terminal first |
| CLI not responding | Check internet connection |
| Can't see output | Try a simpler prompt first |
| `/quit` doesn't work | Press `Ctrl+C` twice |

---

## Key Takeaway

**The CLI gives you the same Agent power – right from your terminal.**

This is perfect for:
- Quick questions without opening the editor
- Remote development (SSH into a server)
- Automation and scripting
- Terminal-first workflows

---

## Bonus Challenge (If Time Permits)

Try switching modes in interactive CLI:

```
> /plan
> Plan adding a modulo operation to the calculator

> /ask
> What does the divide function do?

> /agent
> Now implement the modulo operation
```

Or use the CLI to edit a file:

```
> Add a new function called square that returns n*n
```

---

## Exercise Complete

Check off when done:
- [ ] CLI installed and verified
- [ ] Started interactive mode
- [ ] Asked a question and got response
- [ ] Used follow-up question (context maintained)
- [ ] Used `/help` command
- [ ] Exited with `/quit`
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 20 – CLI – One-Shot Mode

---

## Quick Reference: CLI Interactive Mode Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                 CLI INTERACTIVE MODE CHEAT SHEET                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  START CLI:                                                     │
│  $ agent                                                        │
│                                                                 │
│  COMMANDS (type at > prompt):                                   │
│  /help        - Show all commands                              │
│  /quit        - Exit CLI                                       │
│  /model <name> - Switch model (e.g., /model composer-2.5)        │
│  /plan        - Switch to Plan mode                            │
│  /ask         - Switch to Ask mode                             │
│  /agent       - Switch to Agent mode                           │
│  /clear       - Clear conversation history                     │
│  /compress    - Summarize conversation to save context         │
│                                                                 │
│  EXAMPLE SESSION:                                              │
│  $ agent                                                       │
│  > What does this code do?                                     │
│  > Add a comment at the top                                    │
│  > Run the tests                                               │
│  > /quit                                                       │
│                                                                 │
│  TIPS:                                                         │
│  • Use arrow keys to navigate command history                  │
│  • Press Tab for autocomplete                                  │
│  • Agent remembers entire conversation                         │
│  • Same models available as in editor                          │
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
