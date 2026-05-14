This is the **CLI Parameters** reference documentation – it lists all the command-line options, flags, and subcommands available in the Cursor CLI.

Think of this as the **complete reference manual** for everything you can do with the `agent` command.

Let me break this down.

---

## Global Options (Can Be Used with Any Command)

| Option | Description |
|--------|-------------|
| `-v, --version` | Output the version number |
| `--api-key <key>` | API key for authentication (or use `CURSOR_API_KEY` env var) |
| `-H, --header <header>` | Add custom header to agent requests (format: `Name: Value`, can be used multiple times) |
| `-p, --print` | Print responses to console (for scripts or non-interactive use). Has access to all tools, including write and shell. |
| `--output-format <format>` | Output format (only with `--print`): `text`, `json`, or `stream-json` (default: `text`) |
| `--stream-partial-output` | Stream partial output as individual text deltas (only with `--print` and `stream-json` format) |
| `--resume [chatId]` | Resume a chat session |
| `--continue` | Continue the previous session (alias for `--resume -1`) |
| `--model <model>` | Model to use |
| `--mode <mode>` | Set agent mode: `plan` or `ask` (agent is default) |
| `--plan` | Start in plan mode (shorthand for `--mode=plan`) |
| `--list-models` | List all available models |
| `--force` | Force allow commands unless explicitly denied |
| `--yolo` | Alias for `--force` |
| `--sandbox <mode>` | Set sandbox mode: `enabled` or `disabled` |
| `--approve-mcps` | Automatically approve all MCP servers |
| `--trust` | Trust the workspace without prompting (headless mode only) |
| `--workspace <path>` | Workspace directory to use |
| `--plugin-dir <path>` | Load a local plugin directory (can be specified multiple times) |
| `--worktree` | Run in a new Git worktree under `~/.cursor/worktrees` (see CI workflows) |
| `-h, --help` | Display help for command |

---

## Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `agent` | Start in agent mode (the default) | `agent agent` |
| `login` | Authenticate with Cursor | `agent login` |
| `logout` | Log out and clear stored authentication | `agent logout` |
| `status` | Check authentication status | `agent status` |
| `about` | Display version, system, and account info | `agent about` |
| `models` | List all available models | `agent models` |
| `mcp` | Manage MCP servers | `agent mcp` |
| `acp` | Start ACP server mode (advanced, hidden command) | `agent acp` |
| `update` | Update Cursor Agent to the latest version | `agent update` |
| `ls` | List previous chat sessions | `agent ls` |
| `resume` | Resume the latest chat session | `agent resume` |
| `create-chat` | Create a new empty chat and return its ID | `agent create-chat` |
| `generate-rules` | Generate a new Cursor rule interactively | `agent generate-rules` |
| `install-shell-integration` | Install shell integration to `~/.zshrc` | `agent install-shell-integration` |
| `uninstall-shell-integration` | Remove shell integration from `~/.zshrc` | `agent uninstall-shell-integration` |
| `help [command]` | Display help for command | `agent help [command]` |

> *"When no command is specified, Cursor Agent starts in interactive agent mode by default."*

---

## MCP Subcommands

Manage MCP servers configured for Cursor Agent.

| Subcommand | Description | Usage |
|------------|-------------|-------|
| `login <identifier>` | Authenticate with an MCP server configured in `.cursor/mcp.json` | `agent mcp login` |
| `list` | List configured MCP servers and their status | `agent mcp list` |
| `list-tools <identifier>` | List available tools and their argument names for a specific MCP | `agent mcp list-tools` |
| `enable <identifier>` | Enable an MCP server | `agent mcp enable` |
| `disable <identifier>` | Disable an MCP server | `agent mcp disable` |

> *"All MCP commands support `-h, --help` for command-specific help."*

---

## Arguments

When starting in chat mode (default behavior), you can provide an initial prompt:

```
agent "fix the login bug in src/auth.ts"
```

| Argument | Description |
|----------|-------------|
| `prompt` | Initial prompt for the agent |

---

## Getting Help

All commands support the global `-h, --help` option to display command-specific help:

```bash
agent --help
agent mcp --help
agent mcp list --help
```

---

## Example Usage

### Basic Interactive Session

```bash
# Start interactive session (default)
agent

# Start with initial prompt
agent "refactor the auth module"
```

### Authentication

```bash
# Login (interactive)
agent login

# Check status
agent status

# Logout
agent logout
```

### Non-Interactive (Scripts/CI)

```bash
# Run once and print output
agent -p "What does this codebase do?"

# With API key
agent --api-key $CURSOR_API_KEY -p "Review this code"

# JSON output for parsing
agent -p --output-format json "List all functions"

# Stream JSON for real-time progress
agent -p --output-format stream-json --stream-partial-output "Analyze project"
```

### Session Management

```bash
# List previous chats
agent ls

# Resume latest chat
agent resume

# Resume specific chat
agent --resume "chat-id-here"

# Continue previous session
agent --continue
```

### Model Selection

```bash
# List available models
agent --list-models
agent models

# Use specific model
agent --model gpt-5.2 "Explain this code"

# Start in Plan mode
agent --plan "Add authentication"

# Start in Ask mode
agent --mode ask "What does this function do?"
```

### MCP Management

```bash
# List MCP servers
agent mcp list

# List tools for a server
agent mcp list-tools my-server

# Enable/disable
agent mcp enable my-server
agent mcp disable my-server

# Authenticate with MCP server
agent mcp login my-server
```

### Force Mode (Write Access)

```bash
# Without --force: only proposes changes
agent -p "Add JSDoc comments"

# With --force: actually writes files
agent -p --force "Add JSDoc comments to all functions"

# yolo alias
agent -p --yolo "Refactor this code"
```

### Utilities

```bash
# Get version and system info
agent about

# Update CLI
agent update

# Generate rules interactively
agent generate-rules

# Install shell integration (zsh)
agent install-shell-integration

# Run in worktree (CI workflows)
agent --worktree "Run tests"
```

---

## Parameter Categories Summary

| Category | Parameters |
|----------|------------|
| **Authentication** | `--api-key`, `login`, `logout`, `status` |
| **Session** | `--resume`, `--continue`, `ls`, `resume`, `create-chat` |
| **Mode** | `--mode`, `--plan`, `--print`, `acp` |
| **Model** | `--model`, `--list-models`, `models` |
| **Output** | `--output-format`, `--stream-partial-output` |
| **Security** | `--sandbox`, `--force`, `--yolo`, `--trust`, `--approve-mcps` |
| **Paths** | `--workspace`, `--plugin-dir`, `--worktree` |
| **MCP** | `mcp login`, `mcp list`, `mcp list-tools`, `mcp enable`, `mcp disable` |
| **Info** | `--version`, `--help`, `about`, `status` |
| **Other** | `--header`, `update`, `generate-rules`, `install-shell-integration`, `uninstall-shell-integration` |

---

## Common Beginner Questions

### Q: What's the difference between `agent` and `agent -p`?
**A:** `agent` starts interactive chat. `agent -p` runs once and exits (print mode).

### Q: What's the difference between `--force` and `--yolo`?
**A:** They are aliases – same behavior. `--yolo` is just for fun.

### Q: How do I see all available models?
**A:** `agent --list-models` or `agent models`

### Q: How do I resume a previous chat?
**A:** `agent ls` to see chats, then `agent --resume <chat-id>` or `agent resume` for latest.

### Q: Can I use the CLI without a Cursor account?
**A:** No – you need to `agent login` first or provide an API key.

### Q: What does `--worktree` do?
**A:** Runs the agent in a new Git worktree – useful for CI workflows to avoid messing with your main checkout.

---

## The Bottom Line

**The Cursor CLI parameters give you complete control over how the agent runs – from interactive chats to scriptable automation.**

**For most users:** Just `agent` to start interactive chat. Add `--plan` for complex tasks, `--mode ask` for read-only exploration.

**For scripting:** Use `-p --force --output-format json` with `CURSOR_API_KEY` environment variable.

**Pro tip:** Always check `agent --help` or `agent <command> --help` for the most up-to-date options.

