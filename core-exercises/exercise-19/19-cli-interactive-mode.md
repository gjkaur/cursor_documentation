# Cursor Training – Exercise 19

## CLI – Interactive Mode

**Objective:** Use the Cursor CLI in interactive mode – starting a conversation with the Agent directly from your terminal.

**Time:** 10 minutes

**Setup:** Cursor CLI installed (run `curl https://cursor.com/install -fsS | bash` if not already installed)

---

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
