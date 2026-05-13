This is the **Cursor CLI** documentation – it explains how to interact with AI agents **directly from your terminal**. Whether you want an interactive chat or scriptable automation for CI pipelines, the CLI brings Cursor's AI capabilities right to your command line.

Think of this as **Cursor for the terminal** – no GUI needed, just type `agent` and start coding with AI.

Let me break this down.

---

## What Is the Cursor CLI? (The 10-Second Summary)

**Cursor CLI lets you interact with AI agents directly from your terminal to write, review, and modify code.**

| Without CLI | With CLI |
|-------------|----------|
| Use Cursor desktop app only | Use from any terminal |
| Manual interaction | Scriptable automation |
| Can't integrate with CI | Run in CI pipelines |

> *"Whether you prefer an interactive terminal interface or print automation for scripts and CI pipelines, the CLI provides powerful coding assistance right where you work."*

---

## Installation

### macOS, Linux, WSL:

```bash
curl https://cursor.com/install -fsS | bash
```

### Windows PowerShell:

```powershell
irm 'https://cursor.com/install?win32=true' | iex
```

### Verify Installation:

```bash
agent --version
```

---

## Interactive Mode (Chat in Terminal)

Start a conversational session with the agent:

```bash
# Start interactive session
agent

# Start with an initial prompt
agent "refactor the auth module to use JWT tokens"
```

Once in interactive mode, you can have a back-and-forth conversation with the agent, review proposed changes, and approve commands.

---

## Modes (Same as Editor)

The CLI supports the same modes as the editor:

| Mode | Description | How to use |
|------|-------------|------------|
| **Agent** | Full access to all tools for complex coding tasks | Default (no flag needed) |
| **Plan** | Design approach before coding (clarifying questions) | `--plan`, `--mode=plan`, or `/plan` in chat |
| **Ask** | Read-only exploration without making changes | `--mode=ask` or `/ask` in chat |

### Switch modes in interactive chat using slash commands:

```
/plan    # Switch to Plan Mode
/ask     # Switch to Ask Mode
/agent   # Switch back to Agent Mode
```

### Keyboard shortcut in interactive mode:

`Shift+Tab` – rotate between modes

---

## Non-Interactive Mode (For Scripts & CI)

Use print mode for non-interactive scenarios like scripts, CI pipelines, or automation:

```bash
# Run with specific prompt and model
agent -p "find and fix performance issues" --model "gpt-5.2"

# Use with git changes included for review
agent -p "review these changes for security issues" --output-format text
```

**Perfect for:** CI pipelines, automation scripts, headless environments.

---

## Cloud Agent Handoff

Push your conversation to a Cloud Agent to continue running while you're away. Prepend `&` to any message:

```
& Refactor the auth module and add comprehensive tests
```

The agent continues running in the cloud – even after you close your terminal.

---

## Sessions (Resume Conversations)

Resume previous conversations to maintain context across multiple interactions:

```bash
# List all previous chats
agent ls

# Resume latest conversation
agent resume

# Continue the previous session
agent --continue

# Resume specific conversation by ID
agent --resume "chat-id-here"
```

---

## Sandbox Controls

Configure command execution settings:

```bash
# Toggle sandbox mode
/sandbox

# Or with flag
agent --sandbox enabled
agent --sandbox disabled
```

Toggle sandbox mode on/off and control network access through an interactive menu. **Settings persist across sessions.**

---

## Max Mode

Toggle Max Mode on models that support it:

```
/max-mode on
/max-mode off
```

Max Mode extends the context window to the maximum the model supports.

---

## Sudo Password Prompting

> *"Run commands requiring elevated privileges without leaving the CLI. When a command needs sudo, Cursor displays a secure, masked password prompt. Your password flows directly to sudo via a secure IPC channel; the AI model never sees it."*

**Security:** Your password never goes to the AI model – it goes directly to sudo via a secure channel.

---

## CLI Commands Summary

| Command | Description |
|---------|-------------|
| `agent` | Start interactive session |
| `agent "prompt"` | Start with initial prompt |
| `agent -p "prompt"` | Non-interactive mode (print) |
| `agent --model "model-id"` | Specify model |
| `agent ls` | List previous chats |
| `agent resume` | Resume latest conversation |
| `agent --continue` | Continue previous session |
| `agent --resume "id"` | Resume specific conversation |
| `agent --plan` | Start in Plan Mode |
| `agent --mode ask` | Start in Ask Mode |
| `agent --sandbox enabled/disabled` | Set sandbox mode |

### Interactive Slash Commands:

| Command | Description |
|---------|-------------|
| `/plan` | Switch to Plan Mode |
| `/ask` | Switch to Ask Mode |
| `/agent` | Switch to Agent Mode |
| `/max-mode on/off` | Toggle Max Mode |
| `/sandbox` | Configure sandbox settings |

---

## Real-World Examples

### Example 1: Quick Code Review

```bash
agent -p "review the changes in this PR for security issues"
```

### Example 2: Refactor with Cloud Handoff

```bash
agent
> & refactor the database layer to use connection pooling
```

Agent continues in the cloud – close your laptop, it keeps working.

### Example 3: CI Pipeline Integration

```bash
# In GitHub Actions, run a security review
agent -p "scan for hardcoded secrets" --output-format text
```

### Example 4: Resume a Complex Session

```bash
agent ls
# Chat 1: abc123 - yesterday - "fix login bug"
agent --resume "abc123"
```

Continue exactly where you left off.

---

## Common Beginner Questions

### Q: Do I need to install anything besides the CLI?
**A:** No – the CLI is standalone. It uses your Cursor account and API key.

### Q: Does the CLI cost extra?
**A:** No – uses your existing Cursor subscription (same usage-based pricing).

### Q: Can I use the CLI without an internet connection?
**A:** No – it needs to connect to Cursor's cloud.

### Q: What's the difference between `agent` and `agent -p`?
**A:** `agent` starts interactive mode (chat). `agent -p` runs once and exits (script mode).

### Q: Can I use the CLI in CI/CD pipelines?
**A:** Yes – non-interactive mode (`-p`) is designed for scripts and automation.

### Q: Is my sudo password safe?
**A:** Yes – it goes directly to sudo via secure IPC. The AI model never sees it.

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **Install (Mac/Linux/WSL)** | `curl https://cursor.com/install -fsS \| bash` |
| **Install (Windows)** | `irm 'https://cursor.com/install?win32=true' \| iex` |
| **Start interactive** | `agent` |
| **Non-interactive** | `agent -p "prompt"` |
| **Cloud handoff** | Prepend `&` to message |
| **List chats** | `agent ls` |
| **Resume** | `agent resume` or `agent --continue` |
| **Plan Mode** | `--plan` or `/plan` |
| **Ask Mode** | `--mode ask` or `/ask` |
| **Max Mode** | `/max-mode on/off` |
| **Sandbox** | `/sandbox` or `--sandbox enabled/disabled` |

---

## The Bottom Line

**The Cursor CLI brings AI coding assistance to your terminal – no GUI required.**

**Think of it as:**
- **Cursor Desktop** = Full-featured GUI app 🖥️
- **Cursor CLI** = Terminal-based power tool ⌨️

**For developers:** The CLI is perfect for:
1. **Quick tasks** – Just `agent "fix this bug"` without opening the full app
2. **CI/CD pipelines** – Automated code reviews, security scans, fixes
3. **Headless environments** – Servers, containers, remote SSH sessions
4. **Terminal-first workflows** – For developers who live in the terminal

**The coolest features:**
1. **Cloud Agent handoff** – `&` to push work to the cloud and walk away
2. **Session management** – `agent ls` and `agent resume` to continue conversations
3. **Sudo password protection** – AI never sees your password
4. **Sandbox controls** – Control command execution security

**The CLI + desktop app share the same account, models, and billing – use whichever fits your workflow.**

Would you like me to explain any specific CLI command or feature in more detail?