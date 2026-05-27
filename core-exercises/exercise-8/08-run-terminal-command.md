# Cursor Training – Exercise 8

## Run a Terminal Command

**Objective:** Let the Agent run terminal commands – from simple file listings to builds and tests – and see the output directly in the chat.

**Time:** 10 minutes

**Setup:** Open `core-exercises/exercise-8/` in Cursor with **PowerShell** as your terminal. A matching [`calculator.c`](calculator.c) is included in this folder.

---

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

Continue with `calculator.c` in **this** folder (same directory as this doc). If you already split helpers in earlier exercises, you can copy `math_utils.h` / `math_utils.c` here too.

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
