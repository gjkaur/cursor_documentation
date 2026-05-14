This is the **Using Agent in CLI** documentation – it explains how to interact with Cursor's AI agent from the terminal, including modes, prompting, shortcuts, and features like MCP, rules, and non-interactive mode.

Think of this as the **user manual** for the `agent` command – everything you can do once the CLI is installed.

Let me break this down.

---

## Modes (Same as Editor)

The CLI supports the same three modes as the Cursor editor:

| Mode | Description | How to switch |
|------|-------------|---------------|
| **Agent** | Full access to all tools (files, commands, web) | Default mode |
| **Plan** | Design approach before coding – asks clarifying questions | `Shift+Tab`, `/plan`, `--plan`, `--mode=plan` |
| **Ask** | Read-only exploration – no file edits | `/ask`, `--mode=ask` |

---

## Prompting Tips

> *"Stating intent clearly is recommended for the best results."*

### Example: Prevent Code Editing

```
do not write any code
```

This is helpful when planning tasks before implementing them.

### Agent Tools Available:

- File operations (read, write, edit)
- Searching (codebase search, grep)
- Shell commands
- Web access

---

## MCP Support

> *"The CLI will automatically detect and respect your `mcp.json` configuration file, enabling the same MCP servers and tools that you've configured for the editor."*

**No extra configuration needed** – your existing MCP setup just works.

---

## ACP Support (Agent Client Protocol)

> *"Use `agent acp` to run Cursor CLI as an ACP server over stdio with JSON-RPC messaging."*

This is for custom client integrations.

---

## Rules Support

The CLI agent supports the **same rules system** as the editor.

| Rule Source | Location |
|-------------|----------|
| Project rules | `.cursor/rules/` |
| User rules | `~/.cursor/rules/` |
| AGENTS.md | Project root |
| CLAUDE.md | Project root (compatibility) |

> *"The CLI also reads AGENTS.md and CLAUDE.md at the project root (if present) and applies them as rules alongside .cursor/rules."*

---

## Working with Agent

### Navigation

| Shortcut | What it does |
|----------|--------------|
| **Arrow Up** | Cycle through previous messages |

### Input Shortcuts

| Shortcut | What it does |
|----------|--------------|
| **Shift+Tab** | Rotate between modes (Agent, Plan, Ask) |
| **Shift+Enter** | Insert newline (multi-line prompts) |
| **Ctrl+D** | Exit CLI (double press) |
| **Ctrl+J** or **Enter** | Insert newline (universal fallback) |

> *"Shift+Enter works in iTerm2, Ghostty, Kitty, Warp, and Zed. For tmux users, use `Ctrl+J` instead."*

---

## Review Mode

Press **Ctrl+R** to review changes.

### Review Shortcuts:

| Key | What it does |
|-----|--------------|
| `!` | Add follow-up instructions |
| **Arrow Up / Down** | Scroll |
| **Arrow Left / Right** | Switch files |

---

## Selecting Context

Use `@` to select files and folders to include in context.

To free up space in the context window, run:

```
/compress
```

---

## Cloud Agent Handoff ☁️

This is a **powerful feature** – push your conversation to a Cloud Agent and let it keep running while you're away.

**How to use:** Prepend `&` to any message:

```
& refactor the auth module and add comprehensive tests
```

**Then:** Pick it back up on web or mobile at `cursor.com/agents`.

---

## History / Session Management

| Command | What it does |
|---------|--------------|
| `agent ls` | List previous conversations |
| `agent resume` | Resume most recent conversation |
| `agent --continue` | Continue previous session |
| `agent --resume {thread-id}` | Resume specific conversation |
| `/resume` (slash command) | Resume most recent conversation |

---

## Command Approval

> *"Before running terminal commands, CLI will ask you to approve (`y`) or reject (`n`) execution."*

This is a **security feature** – you control what commands run.

---

## Non-Interactive Mode (For Scripts & CI)

Use `-p` or `--print` to run Agent in non-interactive mode. This prints the response to the console and exits.

### Basic Usage:

```bash
agent -p "find and fix performance issues"
```

### With Output Format:

```bash
agent -p "review these changes" --output-format json
agent -p "review these changes" --output-format text
```

### Important Warning:

> *"Cursor has full write access in non-interactive mode."*

**Be careful** – the agent can edit files without asking for approval in this mode. Use for trusted scripts and CI pipelines only.

---

## Quick Reference Card

### Modes:

| Mode | Switch | Description |
|------|--------|-------------|
| Agent | Default | Full tools |
| Plan | `Shift+Tab`, `/plan`, `--plan` | Design first, ask questions |
| Ask | `/ask`, `--mode=ask` | Read-only |

### Key Shortcuts:

| Shortcut | Action |
|----------|--------|
| `Shift+Tab` | Rotate modes |
| `Shift+Enter` | Newline |
| `Ctrl+D` | Exit (double press) |
| `Ctrl+R` | Review changes |
| `Arrow Up` | Previous messages |

### Session Management:

| Command | Action |
|---------|--------|
| `agent ls` | List conversations |
| `agent resume` | Resume latest |
| `agent --continue` | Continue previous |
| `agent --resume {id}` | Resume specific |

### Cloud Handoff:

| Command | Action |
|---------|--------|
| `& {prompt}` | Send to Cloud Agent |

### Non-Interactive:

| Flag | Action |
|------|--------|
| `-p` or `--print` | Run once, print output |
| `--output-format json` | JSON output for scripts |
| `--output-format text` | Plain text output |

---

## Common Beginner Questions

### Q: How do I write multi-line prompts?
**A:** Use `Shift+Enter` to add a newline without submitting.

### Q: How do I exit the CLI?
**A:** Press `Ctrl+D` twice.

### Q: Can the CLI use my existing MCP servers?
**A:** Yes – automatically detects `mcp.json`.

### Q: Does the CLI respect my rules?
**A:** Yes – reads `.cursor/rules/`, `AGENTS.md`, and `CLAUDE.md`.

### Q: How do I review changes before they're made?
**A:** Press `Ctrl+R` to enter review mode.

### Q: Can I use the CLI in CI pipelines?
**A:** Yes – use `-p` (non-interactive mode). Be aware the agent has full write access.

### Q: What happens if I prepend `&` to a message?
**A:** The agent continues running in the cloud – you can close your terminal.

---

## The Bottom Line

**The Cursor CLI brings the full power of Cursor's AI agent to your terminal – with modes, shortcuts, MCP, rules, and cloud handoff.**

**For terminal lovers:** This is a first-class terminal experience. Same features as the desktop app, but in your terminal.

**Key features to remember:**
1. **Modes** – Agent (full), Plan (design first), Ask (read-only)
2. **Shortcuts** – `Shift+Tab` for modes, `Ctrl+R` for review
3. **Cloud handoff** – `&` to push to cloud and walk away
4. **Non-interactive** – `-p` for scripts and CI
5. **Rules & MCP** – Your existing configs work automatically

**Pro tip:** Use Plan Mode (`Shift+Tab`) for complex tasks – it asks clarifying questions before coding. Use Ask Mode (`/ask`) when you just want to explore code without changes.

