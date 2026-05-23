# Exercise 5.1: Interactive CLI

**Module 5:** Cursor CLI and Local Automation  
**Slides:** `slides/module-05-marp.md` (Lesson 5.1)  
**Time:** 20 min  
**Difficulty:** Beginner

**Objective:** Start an interactive Cursor CLI session from the terminal.

---

## CLI basics (read this first)

1. Open **PowerShell** in Cursor: ``Ctrl+` `` → select **PowerShell**.
2. Confirm the CLI is installed: `agent --version`
3. If missing, install from Cursor: **Command Palette** → `Shell Command: Install 'cursor' command in PATH` (or follow Cursor docs for `agent` CLI).
4. Run commands from your **project root** unless the exercise says otherwise.


---

## Steps

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
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

```bash
agent --mode=ask "What does this project's main function do?"
# Or inside session: /ask
```

---

**Step 5:** Plan Mode:
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

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

## Additional reference

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
│  /model <name> - Switch model (e.g., /model composer-2)        │
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
