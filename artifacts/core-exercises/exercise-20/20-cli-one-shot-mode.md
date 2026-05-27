# Cursor Training – Exercise 20

## CLI – One-Shot Mode

**Objective:** Use the Cursor CLI in one-shot (non-interactive) mode – running a single prompt and getting a response, perfect for scripts and automation.

**Time:** 10 minutes

**Setup:** Cursor CLI installed (from Exercise 19)

---

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open your terminal | Command prompt appears |
| 2 | Type `agent -p "your prompt here"` | Agent runs once and exits |
| 3 | View the output | Response printed to terminal |
| 4 | Try with different output formats | JSON or plain text output |
| 5 | Use in a script | Automation works |

---

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
  "model": "composer-2.5",
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

## Success Criteria

- [ ] Ran `agent -p "simple question"` and got response
- [ ] Ran `agent -p --force` to modify a file
- [ ] Used `--output-format json` and saw JSON output
- [ ] Created a simple bash script using `agent -p`
- [ ] Script executed successfully

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

## Exercise Complete

Check off when done:

- [ ] Ran `agent -p` with a simple question
- [ ] Used `--force` to modify a file
- [ ] Used `--output-format json`
- [ ] Created a script with `agent -p`
- [ ] Script ran successfully
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 21 – CLI – Cloud Handoff

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
