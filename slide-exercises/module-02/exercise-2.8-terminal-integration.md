# Exercise 2.8: Terminal Integration

**Module 2:** Cursor Editor Essentials  
**Slides:** `slides/module-02-marp.md` (Lesson 2.8)  
**Time:** 13 min  
**Difficulty:** Beginner

**Objective:** Let the Agent run terminal commands and react to command output.

---

> **Cursor basics:** Already covered in [Exercise 2.1](../module-02/exercise-2.1-codebase-understanding.md). Skip if you completed that setup.


---

## Steps

**Step 1:** Check the environment:

```
Run `python --version` and tell me what Python version we're using.
```

**Step 2:** Approve the command when prompted

**Step 3:** Run tests and fix failures:

```
Run the test suite. If any tests fail, fix them.
Show me what you're changing.
```

---

<img src="assets/module-02/exercise-2-8-agent-terminal-loop.svg" alt="Exercise 2.8 — Agent Terminal Loop" />

---

**Step 5:** Install a dependency:

```
Install the 'requests' library if it's not already installed.
```

---

**Step 6:** Multi-step workflow:

```
Run these commands in order:
1. git checkout main  2. git pull
3. git checkout -b feature/analytics
4. Create analytics.py  5. Run flake8  6. Fix style issues

Confirm before each command that might affect the repo.
```

---

## Additional reference

## Sample Terminal Commands to Run

### Command 1: List Files (Safest)

> *"Run `ls -la` (Mac/Linux) or `dir` (Windows) to show me all files in this directory"*

**What it does:** Lists all files and folders in the current directory

---

### Command 2: Show Current Path

> *"Run `pwd` (Mac/Linux) or `cd` (Windows) to show me the current directory path"*

**What it does:** Displays the full path of your current working directory

---

### Command 3: Compile the Code

> *"Compile `calculator.c` using `gcc -o calculator calculator.c`"*

**What it does:** Compiles the calculator program (requires GCC installed)

---

### Command 4: Run the Compiled Program

> *"Run `./calculator` (Mac/Linux) or `calculator.exe` (Windows) to test the program"*

**What it does:** Executes the compiled calculator program

*Note: This will wait for user input. Use with caution.*

---

### Command 5: Check File Contents

> *"Run `cat calculator.c` (Mac/Linux) or `type calculator.c` (Windows) to show me the file content"*

**What it does:** Displays the entire content of the file

---

## Expected Agent Response (Example)

Using Option A (List files):

```
I'll run `ls -la` to list the files in this directory.

**Command:** `ls -la`

**Output:**
```
total 32
drwxr-xr-x  5 user  staff   160 Dec 10 10:00 .
drwxr-xr-x  4 user  staff   128 Dec 10 09:30 ..
-rw-r--r--  1 user  staff  1452 Dec 10 10:00 calculator.c
-rw-r--r--  1 user  staff   512 Dec 10 09:45 math_utils.c
-rw-r--r--  1 user  staff   385 Dec 10 09:45 math_utils.h
-rwxr-xr-x  1 user  staff  9872 Dec 10 10:00 calculator
```

**Analysis:**
- `calculator.c` is the main program file
- `math_utils.c` and `math_utils.h` are helper files
- `calculator` is the compiled executable (likely from a previous build)
```

---

## Command Approval Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    COMMAND APPROVAL FLOW                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  You: "Run `ls -la`"                                           │
│                    ↓                                           │
│  Agent: "I'll run `ls -la`. Approve? (y/n)"                    │
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
│  🔧 Running: ls -la                                             │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ total 32                                                 │    │
│  │ drwxr-xr-x  5 user  staff   160 Dec 10 10:00 .          │    │
│  │ -rw-r--r--  1 user  staff  1452 Dec 10 10:00 calculator.c│    │
│  └─────────────────────────────────────────────────────────┘    │
│  ✅ Command completed (exit code 0)                             │
│                                                                 │
│  Based on the output, I can see that calculator.c is 1452      │
│  bytes and was last modified today at 10:00 AM.                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Platform-Specific Commands

| Task | Mac/Linux | Windows |
|------|-----------|---------|
| List files | `ls -la` | `dir` |
| Show current path | `pwd` | `cd` |
| Show file content | `cat filename` | `type filename` |
| Compile C | `gcc -o out file.c` | `gcc -o out.exe file.c` |
| Show disk space | `df -h` | `wmic logicaldisk get size,freespace,caption` |
| Show running processes | `ps aux` | `tasklist` |
| Git status | `git status` | `git status` |
| Make directory | `mkdir folder` | `mkdir folder` |

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

> *"Run `gcc -o calculator calculator.c`, then if that succeeds, run `ls -la calculator` to show the compiled file, then run `./calculator` to test it"*

Or create a reusable command:

> *"Create a terminal command called `build-and-test` that compiles calculator.c and runs it with test inputs 5, 3, and 1"*

---

## Quick Reference: Terminal Tool Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                    TERMINAL TOOL CHEAT SHEET                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  BASIC COMMANDS:                                                │
│  "Run `ls -la`" - List files                                    │
│  "Run `pwd`" - Show current directory                           │
│  "Run `cat calculator.c`" - Show file contents                  │
│  "Run `gcc -o calc calculator.c`" - Compile                     │
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
│      "ls -la",                                                  │
│      "git status",                                              │
│      "gcc -o calculator calculator.c"                          │
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
