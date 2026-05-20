# Module 5: Cursor CLI and Local Automation

## Cursor Training Program — Day 2

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise |
| **Prerequisites** | Cursor CLI installed, API key generated |
| **Module Goal** | Master the Cursor CLI for interactive sessions, scripting, and CI/CD automation |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Use the Cursor CLI in interactive mode for terminal-based conversations
- Run one-shot commands for scripting and automation
- Hand off local sessions to Cloud Agents using `&`
- List and resume previous sessions
- Use headless mode for CI/CD pipelines

---

## Lesson 5.1: Interactive CLI

### Concept (5 minutes)

> *"The Cursor CLI gives you the same Agent power – right from your terminal. Perfect for quick questions, remote development (SSH into a server), and terminal-first workflows."*

**Installation (if not already done):**

| Platform | Command |
|----------|---------|
| macOS, Linux, WSL | `curl https://cursor.com/install -fsS \| bash` |
| Windows PowerShell | `irm 'https://cursor.com/install?win32=true' \| iex` |

**Verify installation:**
```bash
agent --version
```

**Authentication:**
```bash
agent login
# Or set API key
export CURSOR_API_KEY=your_api_key_here
```

### Hands-On Exercise (10 minutes)

**Step 1:** Start interactive mode:

```bash
agent
```

**Step 2:** Ask a question:

```
> What files are in this directory?
```

**Step 3:** Ask a follow-up (Agent remembers context):

```
> Explain what the main file does
```

**Step 4:** Try CLI commands:

```
> /help
```

**Step 5:** Exit:

```
> /quit
```

**Expected Outcome:** The Agent responds to both questions, maintaining context between them.

**Success Criteria:**
- [ ] CLI started successfully
- [ ] Asked a question and got response
- [ ] Asked follow-up (context maintained)
- [ ] Used `/help` to see commands
- [ ] Exited with `/quit`

---

## Lesson 5.2: One-Shot CLI (Non-Interactive)

### Concept (5 minutes)

> *"One-shot mode (`-p` or `--print`) runs a single prompt and exits – perfect for scripts, CI/CD pipelines, and automation."*

| Interactive Mode | One-Shot Mode |
|------------------|---------------|
| Multiple turns | Single turn |
| Human at keyboard | Scriptable |
| Manual approval | Auto-approve with `--force` |
| Best for exploration | Best for automation |

**Basic syntax:**
```bash
agent -p "your prompt here"
```

### Hands-On Exercise (10 minutes)

**Step 1:** Run a simple one-shot command:

```bash
agent -p "What is the purpose of a main function in C?"
```

**Step 2:** With file modification (use `--force` to actually write):

```bash
agent -p --force "Add a comment at the top of the main file"
```

**Step 3:** With JSON output for parsing:

```bash
agent -p "What is 2+2?" --output-format json
```

**Step 4:** With a specific model:

```bash
agent -p --model gpt-5-mini "Explain this codebase briefly"
```

**Step 5:** Create a simple script:

```bash
#!/bin/bash
# review.sh
agent -p --force "Review the code in src/ for security issues" --output-format text
```

**Success Criteria:**
- [ ] Ran `agent -p` successfully
- [ ] Used `--force` to modify a file
- [ ] Used `--output-format json`
- [ ] Created a simple automation script

---

## Lesson 5.3: Cloud Handoff

### Concept (5 minutes)

> *"Prepend `&` to any message to send the task to a Cloud Agent. Close your laptop – it keeps running."*

| Local Agent | Cloud Agent |
|-------------|-------------|
| Runs on your machine | Runs in Cursor's cloud |
| Stops when you close terminal | Continues 24/7 |
| One at a time | Many in parallel |

**Syntax:**
```
& your prompt here
```

### Hands-On Exercise (10 minutes)

**Step 1:** Start interactive CLI:

```bash
agent
```

**Step 2:** Hand off a task:

```
& Add a README.md file to the repository
```

**Expected response:**
```
🔄 Handing off to Cloud Agent...
✅ Agent started: ca_abc123
📊 Monitor: https://cursor.com/agents/ca_abc123
```

**Step 3:** Check the dashboard at `cursor.com/agents`

**Step 4:** (Optional) Check status from CLI:

```bash
agent --resume ca_abc123
```

**Success Criteria:**
- [ ] Handed off task with `&` prefix
- [ ] Received Agent ID
- [ ] Verified agent appears in dashboard

---

## Lesson 5.4: Listing and Resuming Sessions

### Concept (5 minutes)

> *"Every conversation is saved as a session. You can list, resume, and continue sessions – perfect for picking up where you left off."*

| Command | Purpose |
|---------|---------|
| `agent ls` | List all sessions |
| `agent --continue` | Resume most recent session |
| `agent resume` | Same as `--continue` |
| `agent --resume <id>` | Resume specific session |
| `/resume` (in interactive) | Resume most recent |

### Hands-On Exercise (10 minutes)

**Step 1:** Create a session (if not already):

```bash
agent
> Remember that we need to add error handling to the main function
> /quit
```

**Step 2:** List sessions:

```bash
agent ls
```

**Expected output:**
```
ID                  | DATE           | MESSAGES
2025-01-15-10-30-45 | Jan 15 10:30   | 4
```

**Step 3:** Resume most recent:

```bash
agent --continue
```

**Step 4:** Verify the Agent remembers the previous conversation:

```
> What did we discuss about the main function?
```

**Step 5:** Resume specific session (replace with actual ID):

```bash
agent --resume 2025-01-15-10-30-45
```

**Success Criteria:**
- [ ] Ran `agent ls` successfully
- [ ] Used `agent --continue` to resume
- [ ] Agent remembered previous context
- [ ] Used `agent --resume` with specific ID

---

## Lesson 5.5: Headless Mode for CI/CD

### Concept (5 minutes)

> *"Headless mode (`-p` with `--force`) is designed for CI/CD pipelines – no prompts, full automation."*

**Important Warning:**
> *"Cursor has full write access in non-interactive mode."*

**Use Cases:**
- Automated code reviews in CI
- Batch refactoring across many files
- Generating documentation
- Running security scans

### Hands-On Exercise (10 minutes)

**Step 1:** Create a CI script `ci-review.sh`:

```bash
#!/bin/bash
# ci-review.sh - Run automated code review in CI

export CURSOR_API_KEY=${CURSOR_API_KEY}

echo "🔍 Running automated code review..."

agent -p --force --output-format json \
  "Review all changed files for security issues. Output findings as JSON." \
  > review_results.json

if [ $? -eq 0 ]; then
  echo "✅ Review completed"
  cat review_results.json | jq '.'
else
  echo "❌ Review failed"
  exit 1
fi
```

**Step 2:** Run the script:

```bash
chmod +x ci-review.sh
./ci-review.sh
```

**Step 3:** Create a batch processing script:

```bash
#!/bin/bash
# batch-process.sh - Process multiple files

for file in src/*.c; do
  echo "Processing $file..."
  agent -p --force "Add header comment to $file"
done
```

**Step 4:** (Optional) GitHub Actions example:

```yaml
name: AI Code Review
on: [pull_request]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Cursor review
        env:
          CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
        run: |
          agent -p --force "Review PR changes for security issues" --output-format json
```

**Success Criteria:**
- [ ] Created CI script
- [ ] Script ran successfully
- [ ] JSON output parsed correctly
- [ ] (Optional) Created GitHub Actions workflow

---

## Module Summary

| Lesson | Key Skill | Time |
|--------|-----------|------|
| 5.1 | Interactive CLI | 10 min |
| 5.2 | One-Shot CLI | 10 min |
| 5.3 | Cloud Handoff | 10 min |
| 5.4 | Listing and Resuming Sessions | 10 min |
| 5.5 | Headless Mode for CI/CD | 10 min |

---

## Quick Reference Card

| Command | Purpose |
|---------|---------|
| `agent` | Start interactive session |
| `agent -p "prompt"` | One-shot command |
| `agent --force` | Actually modify files |
| `agent --output-format json` | JSON output for scripts |
| `& prompt` | Cloud handoff (in interactive) |
| `agent ls` | List sessions |
| `agent --continue` | Resume most recent |
| `agent --resume <id>` | Resume specific session |
| `agent --model <model>` | Specify model |

---

## Common Pitfalls to Avoid

| Pitfall | Solution |
|---------|----------|
| Forgetting `--force` | Changes won't be written without it |
| No API key in CI | Set `CURSOR_API_KEY` environment variable |
| Interactive mode in script | Use `-p` for non-interactive |
| Losing session context | Use `agent --continue` to resume |

---

## Transition to Module 6

> *"Now that you can automate Cursor from the CLI, let's look at Cloud Agents – running agents in the cloud that work even when your laptop is off."*

---

*End of Module 5*