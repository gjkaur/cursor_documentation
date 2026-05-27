This is the **Slash Commands** reference documentation – it lists all the slash commands available in the Cursor CLI interactive session.

Think of these as **shortcuts** you type starting with `/` to control the agent, change modes, manage settings, and more – without leaving your chat.

Let me break this down.

---

## What Are Slash Commands? (10-Second Summary)

**Slash commands are shortcuts you type in the Cursor CLI interactive session to control the agent, switch modes, manage settings, and more.**

Instead of using flags or menu options, you just type `/command` in the chat.

---

## Complete Slash Command Reference

### Mode Switching

| Command | Description |
|---------|-------------|
| `/plan` | Switch to Plan mode – design approach before coding |
| `/ask` | Switch to Ask mode – read-only exploration |
| `/agent` | Switch to Agent mode – full tool access (default) |

*Note: `/agent` is implied but not listed – it's the default mode.*

---

### Model Control

| Command | Description |
|---------|-------------|
| `/model <model>` | Set or list models (e.g., `/model gpt-5.2`) |
| `/max-mode [on\|off]` | Toggle max mode on models that support it |

---

### Session Management

| Command | Description |
|---------|-------------|
| `/new-chat` | Start a new chat session |
| `/resume <chat>` | Resume a previous chat by folder name |
| `/quit` | Exit the CLI |
| `/logout` | Sign out from Cursor |

---

### Information & Debugging

| Command | Description |
|---------|-------------|
| `/help [command]` | Show help (`/help` or `/help /model`) |
| `/usage` | View Cursor streaks and usage stats |
| `/about` | Show environment and CLI setup details |
| `/copy-request-id` | Copy last request ID to clipboard |
| `/copy-conversation-id` | Copy conversation ID to clipboard |
| `/feedback <message>` | Share feedback with the team |

---

### Configuration

| Command | Description |
|---------|-------------|
| `/auto-run [state]` | Toggle auto-run (default) or set `[on\|off\|status]` |
| `/sandbox` | Configure sandbox mode and network access settings |
| `/vim` | Toggle Vim keys (for modal editing) |
| `/setup-terminal` | Auto-configure terminal keybindings (see Terminal Setup) |

---

### MCP (Model Context Protocol)

| Command | Description |
|---------|-------------|
| `/mcp list` | Browse, enable, and configure MCP servers |
| `/mcp enable <name>` | Enable an MCP server |
| `/mcp disable <name>` | Disable an MCP server |

---

### Rules & Commands

| Command | Description |
|---------|-------------|
| `/rules` | Create new rules or edit existing rules |
| `/commands` | Create new commands or edit existing commands |

---

### Context Management

| Command | Description |
|---------|-------------|
| `/compress` | Summarize conversation to free context space |

---

## Slash Commands by Category

| Category | Commands |
|----------|----------|
| **Modes** | `/plan`, `/ask` |
| **Model** | `/model`, `/max-mode` |
| **Session** | `/new-chat`, `/resume`, `/quit`, `/logout` |
| **Info** | `/help`, `/usage`, `/about`, `/copy-request-id`, `/copy-conversation-id`, `/feedback` |
| **Config** | `/auto-run`, `/sandbox`, `/vim`, `/setup-terminal` |
| **MCP** | `/mcp list`, `/mcp enable`, `/mcp disable` |
| **Rules/Commands** | `/rules`, `/commands` |
| **Context** | `/compress` |

---

## Most Useful Commands for Beginners

| Command | Why use it |
|---------|------------|
| `/help` | Always know what commands are available |
| `/plan` | Switch to Plan mode before complex tasks |
| `/ask` | Explore code without making changes |
| `/model gpt-5.2` | Switch to a different model |
| `/new-chat` | Start fresh when conversation gets messy |
| `/quit` | Exit the CLI cleanly |
| `/compress` | Free up context space when agent seems confused |

---

## Example Usage

```bash
# Start interactive session
agent

# Switch to Plan mode to design first
> /plan

# Switch to Ask mode for read-only exploration
> /ask

# List available models
> /model

# Use a specific model
> /model gpt-5.2

# Toggle Max Mode
> /max-mode on

# See your usage stats
> /usage

# See environment info
> /about

# Copy request ID for support
> /copy-request-id

# List MCP servers
> /mcp list

# Enable an MCP server
> /mcp enable my-server

# Create a new rule
> /rules

# Compress conversation to free context
> /compress

# Start fresh
> /new-chat

# Exit
> /quit
```

---

## Quick Reference Card

| Command | Quick Description |
|---------|-------------------|
| `/plan` | Plan mode |
| `/ask` | Ask mode (read-only) |
| `/model [name]` | Set/list models |
| `/max-mode on/off` | Toggle max context |
| `/new-chat` | Fresh session |
| `/resume [chat]` | Resume previous chat |
| `/help` | Show help |
| `/usage` | Usage stats |
| `/about` | CLI info |
| `/copy-request-id` | Copy ID for support |
| `/feedback` | Send feedback |
| `/auto-run` | Toggle auto-approval |
| `/sandbox` | Configure sandbox |
| `/vim` | Toggle Vim keys |
| `/setup-terminal` | Fix terminal keybindings |
| `/mcp list/enable/disable` | Manage MCP servers |
| `/rules` | Manage rules |
| `/commands` | Manage commands |
| `/compress` | Free context space |
| `/quit` | Exit |
| `/logout` | Sign out |

---

## Common Beginner Questions

### Q: How do I see all available slash commands?
**A:** Type `/help` in the CLI.

### Q: How do I switch back to Agent mode from Plan/Ask mode?
**A:** Type `/agent` (not listed but works) or just start typing normally.

### Q: What does `/compress` do?
**A:** Summarizes the conversation to free up context window space. Useful when the agent seems to be forgetting things.

### Q: What does `/auto-run` do?
**A:** Controls whether the agent automatically runs tools (like terminal commands) without asking for approval.

### Q: How do I get my request ID for support?
**A:** Type `/copy-request-id` – it copies to clipboard.

### Q: Can I use slash commands in non-interactive mode (`-p`)?
**A:** No – slash commands only work in interactive mode.

---

## The Bottom Line

**Slash commands are your control panel inside the Cursor CLI – type `/` followed by a command to change modes, manage settings, or get information.**

**Most useful for daily use:**
- `/plan` – Think before coding
- `/ask` – Explore without changing anything
- `/model` – Switch AI models on the fly
- `/compress` – Fix context issues
- `/help` – Remember commands

**Pro tip:** Type `/help <command>` for detailed help on a specific command (e.g., `/help /model`).

