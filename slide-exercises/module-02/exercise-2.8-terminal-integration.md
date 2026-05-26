# Exercise 2.8: Terminal Integration

**Module 2:** Cursor Editor Essentials  
**Slides:** `slides/module-02-marp.md` (Lesson 2.8)  
**Time:** 13 min  
**Difficulty:** Beginner

**Objective:** Let the Agent run terminal commands and react to command output.

---

## Cursor basics (read this first)

**Demonstration environment:** These exercises assume **Windows 10/11**. Open the integrated terminal with ``Ctrl+` `` and select **PowerShell** as the default profile.

| Task | Windows (demo) | Mac (optional) | Where in Cursor |
|------|----------------|----------------|-----------------|
| Open a project folder | `Ctrl+K Ctrl+O` or **File → Open Folder** | `Cmd+O` | Title bar / Explorer |
| Open **Agent** panel | `Ctrl+I` | `Cmd+I` | Right side panel |
| Open **Chat** panel | `Ctrl+L` | `Cmd+L` | Side panel (Ask/Chat) |
| Integrated terminal | ``Ctrl+` `` → **PowerShell** | ``Ctrl+` `` | Bottom panel |
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` | Search any command |
| Accept Agent diff | Click **Accept** / **Accept All** | Same | Inline diff in editor |
| Reject Agent diff | Click **Reject** | Same | Inline diff in editor |
| Switch Agent mode | Mode dropdown at bottom of Agent panel | Same | Agent panel footer |
| Toggle Plan Mode | `Shift+Tab` in Agent | Same | Agent panel |

**Windows terminal commands (common in exercises):**

| Task | PowerShell command |
|------|-------------------|
| List files | `dir` or `Get-ChildItem` |
| Show file contents | `Get-Content .\file.txt` or `type file.txt` |
| Run a local `.bat` script | `.\run_tests.bat` |
| Run compiled program | `.\calculator.exe` or `calculator.exe` |
| Set env var (session) | `$env:MY_VAR = "value"` |
| Open HTML in browser | `start index.html` |

**Tip for beginners:** Keep the **Explorer** (left), **editor** (center), and **Agent** (right) visible. Send prompts in the Agent panel; review every diff before accepting.


---

## Steps from the training slides

**Demonstration (Windows):** Follow steps in **PowerShell** unless a step says otherwise. Agent panel: ``Ctrl+I`` · Terminal: ``Ctrl+` ``.

Follow these steps in order. Copy prompts exactly unless the exercise tells you to adapt them.

**Demonstration (Windows):** **PowerShell** · Agent ``Ctrl+I``

**Step 1:** Check the environment:

```
Run `python --version` and `gcc --version` in PowerShell.
Tell me what versions we're using.
```

**Step 2:** Approve the command when prompted

**Step 3:** List project files:

```
Run `dir` and tell me which file looks like the main program.
```

---

<img src="../../slides/assets/module-02/exercise-2-8-agent-terminal-loop.svg" alt="Exercise 2.8 — Agent Terminal Loop" />

---

**Step 5:** Install a dependency (Windows):

```
Install the requests library with pip if it's not already installed.
Use: py -m pip install requests
Show me the command output.
```

---

**Step 6:** Multi-step workflow (Windows PowerShell):

```
Run these commands in order:
1. git status
2. git branch
3. dir

Summarize what you see after each command.
Confirm before each command that might affect the repo.
```

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | **File → Open Folder** → `core-exercises/exercise-8/` | Files appear in Explorer |
| 2 | Press **`Ctrl+I`** to open Agent | Agent panel opens |
| 3 | Ask the Agent to run `dir` | Agent proposes the command |
| 4 | Review and approve the command | Command executes in PowerShell |
| 5 | View the output in the chat | Output appears in conversation |

---

## Code Example to Use

Open `core-exercises/exercise-8/` in Cursor and continue with [`calculator.c`](../../core-exercises/exercise-8/calculator.c). If you already split helpers in earlier exercises, you can copy [`math_utils.h`](../../core-exercises/exercise-6/math_utils.h) / [`math_utils.c`](../../core-exercises/exercise-6/math_utils.c) from `core-exercises/exercise-6/`.

**Current directory should have at least:**

```
calculator.c
math_utils.h (if created)
math_utils.c (if created)
```

---

## Sample Terminal Commands to Run

**Demonstration (Windows):** Use these PowerShell prompts in the Agent panel.

### Command 1: List Files (Safest)

> *"Run `dir` to show me all files in this directory"*

**What it does:** Lists all files and folders in the current directory

---

### Command 2: Show Current Path

> *"Run `Get-Location` to show me the current directory path"*

**What it does:** Displays the full path of your current working directory

---

### Command 3: Compile the Code

> *"Compile `calculator.c` using `gcc -o calculator.exe calculator.c`"*

**What it does:** Compiles the calculator program (requires GCC installed)

---

### Command 4: Run the Compiled Program

> *"Run `.\\calculator.exe` to test the program"*

**What it does:** Executes the compiled calculator program

*Note: This will wait for user input. Use with caution.*

---

### Command 5: Check File Contents

> *"Run `Get-Content calculator.c` to show me the file content"*

**What it does:** Displays the entire content of the file

---

## Sample Prompts (Copy-Paste)

### Option A: List Files

> *"Run `dir` and tell me what files you see. Which one looks like the main program file?"*

### Option B: Check Disk Space

> *"Run `Get-PSDrive -PSProvider FileSystem` to show available disk space on Windows"*

### Option C: Compile and Check for Errors

> *"Compile `calculator.c` with `gcc -o calculator.exe calculator.c`. If there are errors, explain what they mean."*

### Option D: Run Tests (if you have tests)

> *"Run `npm test` or `pytest` and show me the results"*

### Option E: Show Git Status

> *"Run `git status` to show me what files have changed"*

---

## Expected Agent Response (Example)

Using Option A (List files):

I'll run `dir` to list the files in this directory.

**Command:** `dir`

**Output:**

```text
 Directory of D:\...\exercise-8

calculator.c
math_utils.c
math_utils.h
calculator.exe
```

**Analysis:**
- `calculator.c` is the main program file
- `math_utils.c` and `math_utils.h` are helper files
- `calculator` is the compiled executable (likely from a previous build)

---

## Command Approval Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    COMMAND APPROVAL FLOW                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  You: "Run `dir`"                                              │
│                    ↓                                           │
│  Agent: "I'll run `dir`. Approve? (y/n)"                       │
│                    ↓                                           │
│  You: "y" (or press Enter)                                     │
│                    ↓                                           │
│  Agent runs command → Displays output                         │
│                    ↓                                           │
│  Agent: "Here's what the output means..."                      │
│                                                                 │
│  OTHER APPROVAL OPTIONS:                                       │
│  • "a" = Always allow (add to allowlist)                       │
│  • "n" = Deny this time                                        │
│  • "e" = Edit command before running                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Command Output in Chat

When the Agent runs a command, you'll see:

```
┌─────────────────────────────────────────────────────────────────┐
│  🔧 Running: dir                                                │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ calculator.c    math_utils.c    calculator.exe          │    │
│  └─────────────────────────────────────────────────────────┘    │
│  ✅ Command completed (exit code 0)                             │
│                                                                 │
│  Based on the output, I can see that calculator.c is 1452      │
│  bytes and was last modified today at 10:00 AM.                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Success Criteria

- [ ] Agent proposed a terminal command
- [ ] You approved the command
- [ ] Command executed successfully
- [ ] Output appeared in the chat
- [ ] Agent explained or analyzed the output
- [ ] (Optional) Added a safe command to allowlist

---

## Platform-Specific Commands

**Windows demo (PowerShell):**

| Task | Windows (demo) | Mac/Linux (optional) |
|------|----------------|----------------------|
| List files | `dir` | `ls` |
| Show current path | `Get-Location` | `pwd` |
| Show file content | `Get-Content file` | `cat file` |
| Compile C | `gcc -o out.exe file.c` | `gcc -o out file.c` |
| Show disk space | `Get-PSDrive -PSProvider FileSystem` | `df -h` |
| Git status | `git status` | `git status` |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Command not found | Ask: *"The command `xxx` is not found. How do I install it?"* |
| Permission denied | You may need to approve with `sudo` (be careful!) |
| Command takes too long | Ask Agent to add timeout: *"Run with 10 second timeout"* |
| Agent won't run command | Check that you approved it – type `y` or press Enter |
| Wrong directory | Ask: *"First, cd to the correct directory, then run the command"* |

---

## Key Takeaway

**The Agent can run any terminal command you approve.** This means it can:

- Compile your code
- Run your tests  
- Check file contents
- Show git status
- Install dependencies
- And much more...

**Remember:** You control what runs. Always review the command before approving.

---

## Bonus Challenge (If Time Permits)

Ask the Agent to chain multiple commands:

> *"Compile `calculator.c` with `gcc -o calculator.exe calculator.c`, then run `dir calculator.exe`, then run `.\\calculator.exe` to test it"*

Or create a reusable command:

> *"Create a terminal command called `build-and-test` that compiles calculator.c and runs it with test inputs 5, 3, and 1"*

---

## Exercise Complete ✓

Check off when done:

- [ ] Agent ran a simple command (e.g., `ls` or `dir`)
- [ ] You approved the command
- [ ] Output was displayed in chat
- [ ] Agent commented on the output
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 9 – Browser Tool (View Page)

---

## Quick Reference: Terminal Tool Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                    TERMINAL TOOL CHEAT SHEET                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  BASIC COMMANDS (Windows PowerShell demo):                      │
│  "Run `dir`" - List files                                       │
│  "Run `Get-Location`" - Show current directory                  │
│  "Run `Get-Content calculator.c`" - Show file contents          │
│  "Run `gcc -o calculator.exe calculator.c`" - Compile           │
│  "Run `git status`" - Check git status                          │
│                                                                 │
│  APPROVAL OPTIONS:                                              │
│  y / Enter = Run once                                           │
│  a = Always allow (add to allowlist)                           │
│  n = Deny this time                                             │
│  e = Edit before running                                        │
│                                                                 │
│  ALLOWLIST FILE: .cursor/permissions.json                       │
│  {                                                              │
│    "terminalAllowlist": [                                       │
│      "dir",                                                     │
│      "git status",                                              │
│      "gcc -o calculator.exe calculator.c"                       │
│    ]                                                            │
│  }                                                              │
│                                                                 │
│  SAFETY TIPS:                                                   │
│  • Always review commands before approving                     │
│  • Be careful with `rm`, `sudo`, `git push --force`           │
│  • Use allowlist for trusted, safe commands                    │
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
