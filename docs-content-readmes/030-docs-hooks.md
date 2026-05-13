This is the **Hooks** documentation – one of the most powerful and advanced features in Cursor. Hooks let you **observe, control, and extend the agent loop using custom scripts**.

Think of hooks as **automated checkpoints** where you can run your own code before or after the Agent does something – like a security guard checking each action, or an auditor logging everything that happens.

Let me break this down for a beginner (note: this is an **advanced** feature).

---

## What Are Hooks? (The 10-Second Summary)

**Hooks let you run custom scripts before or after defined stages of the agent loop.** They can observe, block, or modify behavior.

| Without Hooks | With Hooks |
|---------------|------------|
| Agent does whatever it wants | Your scripts run before/after actions |
| No visibility into agent behavior | Full audit trail of everything |
| Cannot block risky actions | Can block dangerous commands |

> *"With hooks, you can: Run formatters after edits, Add analytics for events, Scan for PII or secrets, Gate risky operations (e.g., SQL writes), Control subagent execution, Inject context at session start"*

---

## What Can You Do with Hooks?

| Use Case | Example |
|----------|---------|
| **Run formatters after edits** | Auto-format code whenever Agent writes to a file |
| **Add analytics for events** | Log every tool call for auditing |
| **Scan for PII or secrets** | Block API keys from being sent to AI |
| **Gate risky operations** | Require approval for SQL writes or network calls |
| **Control subagent execution** | Prevent certain types of subagents from running |
| **Inject context at session start** | Add custom instructions automatically |

---

## Hook Locations (Where to Put Them)

| Location | Scope |
|----------|-------|
| `<project>/.cursor/hooks.json` | Project-level (specific to one project) |
| `~/.cursor/hooks.json` | User-level (global, applies to all projects) |

**Project hooks** live in your repository (can be shared with team).  
**User hooks** are personal (apply everywhere).

---

## Quickstart: Your First Hook

### Step 1: Create `~/.cursor/hooks.json`

```json
{
  "version": 1,
  "hooks": {
    "afterFileEdit": [
      {
        "command": "./hooks/format.sh"
      }
    ]
  }
}
```

### Step 2: Create the script at `~/.cursor/hooks/format.sh`

```bash
#!/bin/bash
# Read input, do something, exit 0
cat > /dev/null
exit 0
```

### Step 3: Make it executable

```bash
chmod +x ~/.cursor/hooks/format.sh
```

**That's it!** Your hook runs after every file edit. Cursor watches the config file and reloads automatically.

---

## Hook Execution Types

### 1. Command-Based Hooks (Default)

Run shell scripts or executables.

```json
{
  "hooks": {
    "beforeShellExecution": [
      {
        "command": "./scripts/approve-network.sh",
        "timeout": 30,
        "matcher": "curl|wget|nc"
      }
    ]
  }
}
```

### 2. Prompt-Based Hooks (LLM-Evaluated)

Use an LLM to evaluate a natural language condition.

```json
{
  "hooks": {
    "beforeShellExecution": [
      {
        "type": "prompt",
        "prompt": "Does this command look safe to execute? Only allow read-only operations.",
        "timeout": 10
      }
    ]
  }
}
```

**Features:**
- Returns structured `{ ok: boolean, reason?: string }` response
- Uses a fast model for quick evaluation
- `$ARGUMENTS` placeholder auto-replaced with hook input JSON

---

## Exit Code Behavior (Command Hooks)

| Exit Code | Meaning |
|-----------|---------|
| **0** | Hook succeeded – continue with action |
| **2** | **Block the action** (equivalent to `permission: "deny"`) |
| **Other** | Hook failed – action proceeds (fail-open) |

---

## All Hook Events (When Hooks Can Run)

### Session Lifecycle

| Event | When it runs |
|-------|--------------|
| `sessionStart` | New composer conversation created (fire-and-forget) |
| `sessionEnd` | Composer conversation ends (fire-and-forget) |

### Tool Execution

| Event | When it runs |
|-------|--------------|
| `preToolUse` | Before ANY tool executes |
| `postToolUse` | After ANY tool executes |
| `postToolUseFailure` | When a tool fails, times out, or is denied |

### Subagent Lifecycle

| Event | When it runs |
|-------|--------------|
| `subagentStart` | Before a subagent starts |
| `subagentStop` | After a subagent completes, errors, or is aborted |

### Shell & MCP

| Event | When it runs |
|-------|--------------|
| `beforeShellExecution` | Before shell command runs |
| `afterShellExecution` | After shell command runs |
| `beforeMCPExecution` | Before MCP tool executes |
| `afterMCPExecution` | After MCP tool executes |

### File Operations

| Event | When it runs |
|-------|--------------|
| `beforeReadFile` | Before Agent reads a file |
| `afterFileEdit` | After Agent edits a file |

### Tab (Inline Completions)

| Event | When it runs |
|-------|--------------|
| `beforeTabFileRead` | Before Tab reads a file |
| `afterTabFileEdit` | After Tab edits a file |

### Agent Loop

| Event | When it runs |
|-------|--------------|
| `beforeSubmitPrompt` | After user hits send, before backend request |
| `afterAgentResponse` | After agent completes an assistant message |
| `afterAgentThought` | After agent completes a thinking block |
| `stop` | When the agent loop ends |
| `preCompact` | Before context window compaction |

---

## Important Hook Details

### preToolUse (Generic Tool Hook)

Called before any tool execution. Fires for ALL tool types (Shell, Read, Write, MCP, Task, etc.).

**Input example:**
```json
{
  "tool_name": "Shell",
  "tool_input": {"command": "npm install", "working_directory": "/project"},
  "tool_use_id": "abc123",
  "cwd": "/project",
  "model": "claude-sonnet-4-20250514",
  "agent_message": "Installing dependencies..."
}
```

**Output:**
```json
{
  "permission": "allow",  // or "deny" to block
  "user_message": "Message shown to user when denied",
  "agent_message": "Message sent to agent when denied",
  "updated_input": {"command": "npm ci"}  // optionally modify the command
}
```

### subagentStart

Called before a subagent starts. Can block subagent execution.

**Input example:**
```json
{
  "subagent_id": "abc-123",
  "subagent_type": "generalPurpose",
  "task": "Explore the authentication flow",
  "parent_conversation_id": "conv-456"
}
```

**Output:**
```json
{
  "permission": "allow",  // or "deny" to block
  "user_message": "Message shown when denied"
}
```

### beforeSubmitPrompt

Called right after user hits send. Can prevent submission.

**Input:**
```json
{
  "prompt": "delete all files",
  "attachments": [...]
}
```

**Output:**
```json
{
  "continue": false,  // false = block the prompt
  "user_message": "This prompt was blocked by security policy"
}
```

### stop (Auto-Continue)

Called when agent loop ends. Can optionally auto-submit a follow-up message.

**Output:**
```json
{
  "followup_message": "auto-continue with this message"
}
```

**Loop limit:** Default 5 iterations (configurable via `loop_limit`)

---

## Matchers (Filter Which Hooks Run)

Use `matcher` to run hooks only when specific conditions are met.

| Hook | What matcher runs against |
|------|---------------------------|
| `preToolUse` / `postToolUse` | Tool type (Shell, Read, Write, Task, MCP:tool_name) |
| `subagentStart` / `subagentStop` | Subagent type (generalPurpose, explore, shell) |
| `beforeShellExecution` | Shell command string |
| `beforeReadFile` | Tool type (TabRead, Read) |
| `afterFileEdit` | Tool type (TabWrite, Write) |

**Example (beforeShellExecution with matcher):**
```json
{
  "hooks": {
    "beforeShellExecution": [
      {
        "command": "./scripts/approve-network.sh",
        "matcher": "curl|wget|nc"
      }
    ]
  }
}
```
This hook only runs when the command contains `curl`, `wget`, or `nc`.

---

## Environment Variables for Hooks

All hook scripts receive these environment variables:

| Variable | Description |
|----------|-------------|
| `CURSOR_PROJECT_DIR` | Workspace root directory (always present) |
| `CURSOR_VERSION` | Cursor version string (always present) |
| `CURSOR_USER_EMAIL` | Authenticated user email (if logged in) |
| `CURSOR_TRANSCRIPT_PATH` | Path to conversation transcript (if enabled) |
| `CURSOR_CODE_REMOTE` | "true" when running in remote workspace |
| `CLAUDE_PROJECT_DIR` | Alias for project dir (Claude compatibility) |

**Session-scoped environment variables** from `sessionStart` hooks are passed to all subsequent hook executions within that session.

---

## Security: failClosed vs failOpen

| Setting | Behavior |
|---------|----------|
| **fail-open (default)** | Hook failures (crash, timeout, invalid JSON) allow the action through |
| **failClosed: true** | Hook failures BLOCK the action (recommended for security-critical hooks) |

> *"Set `failClosed: true` on the hook definition to block the action on failure instead. This is recommended for security-critical `beforeMCPExecution` hooks."*

---

## Partner Integrations (Ready-to-Use)

Cursor partners with ecosystem vendors who have built hooks support:

| Partner | Purpose |
|---------|---------|
| **Mint** | Build inventory of MCP servers, monitor usage, scan for sensitive data |
| **Oasis Security** | Enforce least-privilege policies, maintain audit trails |
| **Runlayer** | Centralized control over agent-to-tool interactions |

---

## Troubleshooting

### How to confirm hooks are active

There is a **Hooks tab in Cursor Settings** to debug configured and executed hooks, as well as a **Hooks output channel** to see errors.

### If hooks are not working

1. Cursor watches `hooks.json` files and reloads on save
2. If hooks still don't load, **restart Cursor**
3. Check that relative paths are correct:
   - For project hooks: paths relative to project root (e.g., `.cursor/hooks/script.sh`)
   - For user hooks: paths relative to `~/.cursor/` (e.g., `./hooks/script.sh`)

---

## Common Beginner Questions

### Q: Do I need hooks as a beginner?
**A:** Almost certainly not. Hooks are an **advanced feature** for security, compliance, and automation.

### Q: Can hooks break my Cursor?
**A:** Badly written hooks can cause errors or delays. Test hooks thoroughly.

### Q: Can hooks block dangerous commands?
**A:** Yes! That's a primary use case – block `rm -rf /` or SQL writes.

### Q: Are hooks free?
**A:** Hooks run scripts on your computer. No additional cost from Cursor.

### Q: Can I use hooks from Claude Code?
**A:** Yes! Cursor supports loading hooks from third-party tools like Claude Code (compatibility mode).

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **What are hooks?** | Custom scripts that run before/after agent actions |
| **Location** | `<project>/.cursor/hooks.json` or `~/.cursor/hooks.json` |
| **Hook types** | Command-based (script) or Prompt-based (LLM) |
| **Exit code 0** | Success, continue |
| **Exit code 2** | Block the action |
| **failClosed** | Block on hook failure (security-critical) |
| **matcher** | Filter which hooks run based on command/tool type |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What are Hooks?** | Custom scripts that run before/after agent actions |
| **Should I use them?** | Only if you need security, auditing, or automation |
| **What can they do?** | Block commands, log actions, format code, scan for secrets |
| **Where do I put them?** | `.cursor/hooks.json` in your project or home directory |
| **How do I test them?** | Hooks tab in Cursor Settings |
| **Can they break things?** | Yes – test thoroughly |

---

## The Bottom Line

**Hooks are the "power user" feature for controlling Cursor programmatically.**

**Think of it as:**
- **Without Hooks** = Giving someone keys to your house 🏠🔑
- **With Hooks** = Having security cameras, locks, and an alarm system 🏠🔒📹

**For beginners:** You don't need hooks. Focus on learning the Agent, Rules, and Skills first.

**For security teams:** Hooks are essential. Use `beforeShellExecution` to block dangerous commands, `beforeSubmitPrompt` to prevent sensitive data from being sent, and `sessionStart`/`sessionEnd` for audit logging.

**The most important hooks to know about:**
1. `beforeShellExecution` – Block dangerous shell commands (exit code 2)
2. `beforeSubmitPrompt` – Prevent sensitive prompts from being sent
3. `sessionStart` – Inject context automatically at session start
4. `afterFileEdit` – Run formatters after Agent writes code

Would you like me to explain a specific hook event in more detail, or help you write a hook script for a specific use case?