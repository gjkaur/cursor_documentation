# Module 5: Cursor CLI and Local Automation

## Cursor Training Program — Day 1 (Hands-On)

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise |
| **Prerequisites** | Cursor CLI installed, terminal access, Modules 1-4 completed |
| **Module Goal** | Master the Cursor CLI for terminal-based AI workflows and automation |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Use the Cursor CLI in interactive mode for real-time AI collaboration
- Run one-shot CLI commands for scripting and CI/CD integration
- Hand off local sessions to Cloud Agents for remote execution
- List, resume, and manage concurrent sessions effectively

---

## Lesson 5.1: Interactive CLI

### Concept (8 minutes)

> *"Using Cursor from the terminal. The Cursor CLI brings AI-powered coding directly to your command line, eliminating the need to switch between terminal and editor."* 

### What Is the Cursor CLI?

The Cursor CLI is a terminal-based interface to Cursor's AI agent. It allows you to:

- Start AI sessions directly from your terminal
- Get code assistance without leaving your workflow
- Automate coding tasks with scripts
- Integrate AI into existing CLI tools

**Primary Command:** `agent` (formerly `cursor-agent`, now the main entry point) 

### Interactive Mode Commands

Once in an interactive session, these slash commands are available: 

| Command | Purpose |
|---------|---------|
| `/model` | Switch between AI models interactively |
| `/compress` | Summarize conversation, free up context window |
| `/rules` | Create and edit rules directly from CLI |
| `/commands` | Create and modify custom commands |
| `/mcp enable/disable` | Manage MCP servers |
| `/usage` | View Cursor usage stats |
| `/about` | View environment and CLI configuration |
| `/resume` | View and resume previous sessions |

### Hands-On Exercise (12 minutes)

**Step 1:** Start an interactive session

```bash
# Basic interactive mode
agent

# Start with an initial prompt
agent "Help me understand the current codebase structure"
```

**Step 2:** Navigate the interactive session

Once inside the session:
- Type your prompts naturally
- Use `Shift+Enter` to insert a new line without submitting 
- Press `Enter` to submit your prompt
- Use `Ctrl+D` twice to exit 

**Step 3:** Switch models during a session

```
# Inside the interactive session
/model

# Or list all available models
agent --list-models
```

**Step 4:** Use Ask Mode (read-only) from CLI

```bash
# Ask Mode - explores code without making changes
agent --mode=ask "What does this project's main function do?"

# Or using slash command inside session
/ask
```

**Step 5:** Use Plan Mode from CLI

```bash
# Plan Mode - design before implementation
agent --mode=plan "Add user authentication to this API"

# The agent will ask clarifying questions before writing code
```

**Step 6:** Configure your CLI status line

The status line shows useful information like current model, directory, git branch, and context usage. 

```bash
# Interactive setup for status line
npx -y cursor-statusline

# After setup, your terminal prompt shows:
# [model: claude-4.5-sonnet] [~/project] [main] [ctx: 45k/200k]
```

**Step 7:** Set up terminal key bindings

```bash
# For better Shift+Enter support in your terminal
agent /setup-terminal
```

**Success Criteria:**
- [ ] Started interactive `agent` session
- [ ] Switched models using `/model`
- [ ] Used Ask Mode and Plan Mode from CLI
- [ ] Configured status line display
- [ ] Exited session gracefully

---

## Lesson 5.2: One-Shot CLI

### Concept (8 minutes)

> *"Scripting and CI-friendly invocation. One-shot commands let you run a single AI task and exit – perfect for automation, CI/CD pipelines, and batch operations."* 

### One-Shot Command Structure

```bash
# Basic one-shot
agent "your prompt here"

# With mode specified
agent --mode=ask "question about code"

# With specific model
agent --model claude-4.5-sonnet "task description"

# Non-interactive (no prompts, just output)
agent --non-interactive "run this task"
```

### Use Cases for One-Shot CLI

| Use Case | Example |
|----------|---------|
| **Code generation** | `agent "Create a React component for a login form"` |
| **Documentation** | `agent "Generate JSDoc comments for src/api.js"` |
| **CI/CD tasks** | `agent "Review this PR diff for security issues"` |
| **Batch processing** | Loop through files with `agent` commands |
| **Pre-commit hooks** | `agent --mode=ask "Check for console.log statements"` |

### Hands-On Exercise (12 minutes)

**Step 1:** Run basic one-shot commands

```bash
# Simple question
agent "What is the difference between let and const in JavaScript?"

# Code generation
agent "Write a bash function that checks if a port is in use"

# Code explanation
agent --mode=ask "Explain the git rebase command with examples"
```

**Step 2:** Specify models in one-shot mode

```bash
# Use a cheaper model for simple tasks
agent --model gpt-5-mini "What does this command do: `ls -la | grep .txt`"

# Use a more powerful model for complex tasks
agent --model claude-4.5-opus "Design a database schema for a task management system"
```

**Step 3:** Create a scriptable code reviewer

Create `bin/ai-review.sh`:

```bash
#!/bin/bash
# AI code review for staged files

STAGED_FILES=$(git diff --cached --name-only | tr '\n' ', ')

agent --mode=ask "Review these staged files for common issues:
Files: $STAGED_FILES

Check for:
1. Debugging statements (console.log, print, debugger)
2. Unused variables or imports
3. Potential security issues
4. Missing error handling

Report only issues found, be concise."
```

**Step 4:** Batch process multiple files

```bash
# Generate summaries for all Python files
for file in src/**/*.py; do
    echo "=== $file ==="
    agent --mode=ask --non-interactive "Summarize what this Python file does in one sentence: $(cat $file | head -50)"
    echo ""
done
```

**Step 5:** Integrate with git hooks

Create `.git/hooks/pre-commit`:

```bash
#!/bin/bash
# Pre-commit hook that checks for common issues

echo "🔍 Running AI pre-commit check..."

# Get the diff of staged changes
DIFF=$(git diff --cached)

# Ask agent to review
agent --mode=ask --non-interactive "Review this git diff for issues:
$DIFF

Check for:
- Debugging statements
- Secret keys or passwords
- Merge conflict markers
- TODO comments (should be tracked as issues)

If issues found, start response with '❌ ISSUES FOUND'. Otherwise '✅ OK'."

# If issues found, exit with error
if [ $? -eq 1 ]; then
    echo "Commit blocked. Fix issues or commit with --no-verify"
    exit 1
fi
```

**Step 6:** Create a CI/CD task script

```bash
# Run in GitHub Actions or similar
agent --non-interactive "Examine the test output below and identify which tests failed and why:

$(cat test-output.log)

Provide a brief summary and suggest fixes for the first 3 failures."
```

**Success Criteria:**
- [ ] Ran basic one-shot commands
- [ ] Specified different models for different tasks
- [ ] Created a scriptable code reviewer
- [ ] Integrated CLI into pre-commit hook (optional)
- [ ] Understood CI/CD use cases

---

## Lesson 5.3: Cloud Handoff

### Concept (8 minutes)

> *"Moving a local session to the cloud. Cloud Handoff lets you push a local agent session to run remotely, freeing up your machine while the agent continues working."* 

### What Is Cloud Handoff?

Cloud Handoff allows you to:
- Send a local conversation to a Cloud Agent
- Continue the session from web or mobile (`cursor.com/agents`)
- Let the agent run long tasks while you're away
- Resume the session later from any device 

### How to Use Cloud Handoff

```
┌─────────────────────────────────────────────────────────────┐
│                    CLOUD HANDOFF FLOW                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Local Terminal                    Cloud                     │
│  ┌─────────────┐                  ┌─────────────┐           │
│  │ agent       │  ──& prompt──→   │ Cloud Agent │           │
│  │ (interactive│                  │ (runs async)│           │
│  │ session)    │  ←──result────   │             │           │
│  └─────────────┘                  └─────────────┘           │
│                                          │                   │
│                                          ↓                   │
│                                   cursor.com/agents         │
│                                   (web/mobile access)       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**The `&` Prefix:** Prepend any message with `&` to send it to the cloud. 

### Hands-On Exercise (10 minutes)

**Step 1:** Start a local session and hand off to cloud

```bash
# Start a local interactive session
agent

# Inside the session, prefix your message with &
& "Analyze the entire codebase and create a dependency graph. This will take a while - run it in the cloud."
```

**Step 2:** Verify the handoff

After sending with `&`, you'll see:
```
🚀 Handing off to Cloud Agent...
✅ Session running at: https://cursor.com/agents/[agent-id]
```

**Step 3:** Check cloud agent status

```bash
# Access via browser
open https://cursor.com/agents

# Or continue from CLI (but cloud runs independently)
```

**Step 4:** Push an existing local conversation

```bash
# If you have an ongoing local session and need to leave
# Prefix your next message with & to transfer the whole context
& "Continue this conversation in the cloud. I need to log off."
```

**Step 5:** Use cloud handoff for long-running tasks

```bash
# Example: Large refactoring task
agent "& Refactor the entire authentication module to use JWT instead of sessions. Update all tests and documentation."

# The cloud agent will continue running after you close terminal
```

**Step 6:** Resume cloud session later

```bash
# List cloud agents you have running
# Then resume by ID
agent --resume [agent-id-from-cloud]
```

**Best Practices for Cloud Handoff:**

| When to Use | When Not to Use |
|-------------|-----------------|
| Long-running tasks (>5 min) | Quick questions |
| When you need to close laptop | Interactive debugging |
| Overnight batch processing | Tasks needing terminal access |
| Parallel work streams | Security-sensitive code (local only) |

**Success Criteria:**
- [ ] Sent message with `&` prefix
- [ ] Verified cloud agent started
- [ ] Accessed cloud agent via web
- [ ] Understood when to use cloud handoff

---

## Lesson 5.4: Listing and Resuming Sessions

### Concept (8 minutes)

> *"Managing concurrent work. The Cursor CLI allows you to have multiple simultaneous sessions, list them, and resume any previous session."* 

### Session Management Commands

| Command | Purpose |
|---------|---------|
| `/resume` | List all previous sessions and resume one |
| `agent --resume [id]` | Resume a specific session by ID |
| `agent --list` | List available sessions (alternative) |

**Note:** `/list` has been replaced by `/resume` in newer versions. 

### Session Identification

By default, sessions are identified by UUID. To make sessions recognizable: 

```bash
# Name your session with the first message
agent "Just say one word: auth-refactor"

# The session will be named "auth-refactor Agent" or similar
```

### Hands-On Exercise (12 minutes)

**Step 1:** Create multiple named sessions

```bash
# Session 1: Frontend work
agent "Just say one word: frontend-cleanup"

# In the session, start your real work
# Then exit with Ctrl+D twice

# Session 2: Database optimization
agent "Just say one word: db-optimization"

# Do database work
# Exit

# Session 3: Documentation
agent "Just say one word: docs-update"
```

**Step 2:** List all sessions

```bash
# Inside any agent session
/resume

# This shows:
# 1. frontend-cleanup Agent (2 hours ago)
# 2. db-optimization Agent (1 hour ago)
# 3. docs-update Agent (30 minutes ago)
```

**Step 3:** Resume a specific session

```bash
# Using the UUID (from /resume list)
agent --resume abc123-def456-ghi789

# Or use the interactive selector from /resume
```

**Step 4:** Work with multiple concurrent sessions

```bash
# Terminal 1
agent --resume frontend-cleanup

# Terminal 2 (different tab/window)
agent --resume db-optimization

# Each session maintains its own context independently
```

**Step 5:** Session context management

```bash
# Check current context usage in session
/compress

# This summarizes the conversation and frees up context window
# Useful for long sessions approaching token limits
```

**Step 6:** Export and share session output

```bash
# Inside session, you can request export
agent --mode=ask "Summarize everything we've discussed in this session and format as markdown"
```

**Step 7:** Script to list and manage sessions

Create `bin/cursor-sessions.sh`:

```bash
#!/bin/bash
# List and manage Cursor CLI sessions

echo "📋 Active Cursor Sessions"
echo "========================"

# Method 1: Use agent's built-in resume list
# (This requires entering agent - can be automated with expect)

# Method 2: Manual tracking
SESSION_DIR="$HOME/.cursor/sessions"

if [ -d "$SESSION_DIR" ]; then
    for session in "$SESSION_DIR"/*; do
        if [ -f "$session/metadata" ]; then
            NAME=$(grep "name" "$session/metadata" | cut -d= -f2)
            ID=$(basename "$session")
            echo "  $NAME: $ID"
        fi
    done
fi

echo ""
echo "Resume with: agent --resume <id>"
```

**Session Management Best Practices:**

```
┌─────────────────────────────────────────────────────────────┐
│              SESSION MANAGEMENT TIPS                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  NAMING CONVENTIONS:                                        │
│  • Use descriptive first messages: "Just say one word: X"   │
│  • Format: [area]-[task] (e.g., "api-auth-fix")            │
│  • Include date for long-running sessions                   │
│                                                              │
│  CONTEXT MANAGEMENT:                                        │
│  • Use /compress on long sessions                           │
│  • Consider cloud handoff for very long tasks               │
│  • Export summaries periodically                            │
│                                                              │
│  CLEANUP:                                                   │
│  • Sessions persist indefinitely                            │
│  • No automatic cleanup                                     │
│  • Manually complete or discard finished sessions           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Success Criteria:**
- [ ] Created multiple named sessions
- [ ] Listed sessions using `/resume`
- [ ] Resumed a previous session
- [ ] Used `/compress` for context management
- [ ] Understood session persistence behavior

---

## Module Summary

| Lesson | Topic | Time | Key Skill |
|--------|-------|------|-----------|
| 5.1 | Interactive CLI | 12 min | Real-time terminal AI |
| 5.2 | One-Shot CLI | 12 min | Scripting & automation |
| 5.3 | Cloud Handoff | 10 min | Remote/long-running tasks |
| 5.4 | Session Management | 12 min | Concurrent work handling |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│                 CURSOR CLI QUICK REFERENCE                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  BASIC COMMANDS:                                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ agent                    Start interactive session   │   │
│  │ agent "prompt"           One-shot command            │   │
│  │ agent --mode=ask         Read-only mode              │   │
│  │ agent --mode=plan        Plan before code            │   │
│  │ agent --model <name>     Specify model               │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  SESSION COMMANDS (inside interactive):                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ /model                  Switch AI model              │   │
│  │ /compress               Summarize, free context      │   │
│  │ /rules                  Edit rules                   │   │
│  │ /commands               Edit custom commands         │   │
│  │ /mcp enable/disable     Manage MCP servers           │   │
│  │ /resume                 List/resume sessions         │   │
│  │ /usage                  View usage stats             │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  CLOUD HANDOFF:                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ & "message"              Send to cloud               │   │
│  │ cursor.com/agents        Web access                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  KEYBOARD SHORTCUTS:                                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Shift+Enter             New line (not submit)        │   │
│  │ Ctrl+D (twice)          Exit session                 │   │
│  │ Ctrl+J                  Alternative line break       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Transition to Module 6

> *"Now that you've mastered terminal-based AI workflows, Module 6 will cover Custom Prompts and Commands – creating reusable prompts, command templates, and team workflows."*

---

*End of Module 5*