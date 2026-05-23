# Exercise 5.2: One-Shot CLI

**Module 5:** Cursor CLI and Local Automation  
**Slides:** `slides/module-05-marp.md` (Lesson 5.2)  
**Time:** 20 min  
**Difficulty:** Beginner

**Objective:** Run single-shot Agent commands from scripts and CI.

---

> **CLI basics:** Already covered in [Exercise 5.1](../module-05/exercise-5.1-interactive-cli.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)

**Step 1:** Basic one-shot commands:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent "What is the difference between let and const in JavaScript?"
agent "Write a bash function that checks if a port is in use"
agent --mode=ask "Explain the git rebase command with examples"
```

---

**Step 2:** Specify models:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent --model gpt-5-mini "What does this command do: ls -la | grep .txt"
agent --model claude-4.5-opus "Design a database schema for a task management system"
```

---

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

Create `bin/ai-review.sh`:

```bash
#!/bin/bash
STAGED_FILES=$(git diff --cached --name-only | tr '\n' ', ')

agent --mode=ask "Review these staged files for common issues:
Files: $STAGED_FILES
Check for: debugging statements, unused imports,
security issues, missing error handling. Be concise."
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

---



**Step 4:** Batch process files:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
for file in src/**/*.py; do
    agent --mode=ask --non-interactive \
      "Summarize this Python file in one sentence: $(head -50 $file)"
done
```

---

**Step 5:** Pre-commit hook — review staged diff for secrets, debug statements, merge markers
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

**Step 6:** CI/CD — analyze test output and suggest fixes for failures
**Terminal:** **PowerShell** — clone/open repo, then continue in Agent panel

---

## Success criteria

- [ ] Ran one-shots · specified models · created reviewer script · understood CI/CD use

---

## Additional reference

## What is One-Shot Mode?

| Aspect | Description |
|--------|-------------|
| **Flag** | `-p` or `--print` |
| **Behavior** | Runs one prompt, prints response, exits |
| **Compared to interactive** | No conversation, no waiting for input |
| **Best for** | Scripts, CI/CD pipelines, automation |
| **File access** | Can read and write files (use `--force` to write) |

---

## Basic One-Shot Commands

### Command 1: Simple Question

```bash
agent -p "What is the purpose of a watchdog timer in embedded systems?"
```

**Expected output:** Agent answers the question and exits.

---

### Command 2: Code Analysis

```bash
agent -p "List all functions in calculator.c and describe what each does"
```

**Expected output:** List of functions with descriptions.

---

### Command 3: Code Generation (Print Only)

```bash
agent -p "Write a function that checks if a number is prime"
```

**Expected output:** The function code printed to terminal (files not modified).

---

### Command 4: With File Modification

```bash
agent -p --force "Add a comment at the top of calculator.c saying 'Updated via CLI'"
```

**Expected output:** Confirmation and the file is actually modified.

**Note:** `--force` is required to actually write files. Without it, Agent only shows what it would do.

---

## Output Formats

### Plain Text (Default)

```bash
agent -p "What is 2+2?" --output-format text
```

**Output:**

```
2+2 equals 4.
```

### JSON (For Scripting)

```bash
agent -p "What is 2+2?" --output-format json
```

**Output:**

```json
{
  "result": "2+2 equals 4.",
  "model": "composer-2",
  "duration_ms": 1234
}
```

### Stream JSON (Real-time)

```bash
agent -p "Explain this code" --output-format stream-json --stream-partial-output
```

**Output:** Multiple JSON objects streaming in real-time as the Agent generates the response.

---

## Using in Scripts

### Bash Script Example

Create `ask-agent.sh`:

```bash
#!/bin/bash
# Simple script to ask Cursor Agent a question

QUESTION="What is the main function of calculator.c?"

echo "Asking: $QUESTION"
agent -p "$QUESTION" --output-format text
```

Run it:

```bash
chmod +x ask-agent.sh
./ask-agent.sh
```

### CI/CD Pipeline Example

```bash
#!/bin/bash
# Run in GitHub Actions, GitLab CI, etc.

# Set API key (use secrets in CI)
export CURSOR_API_KEY=$CURSOR_API_KEY

# Review code changes
agent -p --force "Review the changes in this PR for security issues" --output-format json
```

### Batch Processing Example

```bash
# Process multiple files
for file in *.c; do
    echo "Processing $file..."
    agent -p "Add a comment at the top of $file indicating it's part of the calculator project" --force
done
```

---

## One-Shot vs. Interactive Mode

| Feature | Interactive | One-Shot (-p) |
|---------|-------------|---------------|
| **Conversation** | Yes (multiple turns) | No (single turn) |
| **Exits automatically** | No (requires /quit) | Yes |
| **Scriptable** | Difficult | Easy |
| **File modification** | Requires approval | Requires `--force` |
| **Best for** | Exploration, debugging | Automation, CI/CD |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `agent: command not found` | Install CLI first (Exercise 19) |
| Authentication error | Run `agent login` once, or set `CURSOR_API_KEY` |
| Files not modified | Add `--force` flag |
| JSON output not parsing | Make sure you have `jq` installed for parsing |
| Prompt too long | Use single quotes for prompts with spaces |

---

## Key Takeaway

**One-shot mode (`-p`) turns Cursor Agent into a command-line tool – perfect for scripts, CI/CD, and automation.**

Use it when you need:

- Quick answers without an interactive session
- Automated code reviews in CI pipelines
- Batch processing of files
- Integration with other tools

---

## Bonus Challenge (If Time Permits)

Create a script that:

1. Reads a list of functions from a file
2. Asks the Agent to generate tests for each function
3. Saves the tests to a new file

```bash
#!/bin/bash
# generate-tests.sh

functions=("add" "subtract" "multiply" "divide")

for func in "${functions[@]}"; do
    echo "Generating test for $func..."
    agent -p "Write a unit test for the $func function in calculator.c" >> tests.c
done
```

Or parse JSON output with `jq`:

```bash
agent -p "List all functions in calculator.c" --output-format json | jq '.result'
```

---

## Quick Reference: One-Shot Mode Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                  ONE-SHOT MODE CHEAT SHEET                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  BASIC SYNTAX:                                                  │
│  agent -p "your prompt here"                                    │
│  agent --print "your prompt here"                               │
│                                                                 │
│  WITH FILE MODIFICATION:                                        │
│  agent -p --force "make this change"                            │
│                                                                 │
│  OUTPUT FORMATS:                                                │
│  --output-format text        # Plain text (default)             │
│  --output-format json        # JSON for scripting               │
│  --output-format stream-json # Real-time streaming              │
│                                                                 │
│  WITH SPECIFIC MODEL:                                           │
│  agent -p --model gpt-5-mini "question"                         │
│                                                                 │
│  WITH API KEY (for CI):                                         │
│  export CURSOR_API_KEY=your_key                                 │
│  agent -p "question"                                            │
│                                                                 │
│  SCRIPT EXAMPLES:                                               │
│  # Review a file                                                │
│  agent -p "Review calculator.c for bugs"                        │
│                                                                 │
│  # Generate documentation                                       │
│  agent -p "Add comments to all functions" --force               │
│                                                                 │
│  # Batch processing                                             │
│  for f in *.c; do                                               │
│    agent -p "Add header comment to $f" --force                  │
│  done                                                           │
│                                                                 │
│  NOTE: Without --force, Agent only shows what it WOULD do       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
