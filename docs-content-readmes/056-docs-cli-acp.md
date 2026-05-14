This is the **ACP (Agent Client Protocol)** documentation – it explains how to run Cursor CLI as an ACP server for building **custom integrations**. This allows you to connect Cursor's AI agent to other editors, tools, or custom clients.

Think of ACP as the **plumbing** that lets you plug Cursor's agent into any editor or application that supports the protocol.

Let me break this down. (Note: This is an **advanced developer** feature.)

---

## What Is ACP? (The 10-Second Summary)

**Cursor CLI supports ACP (Agent Client Protocol) for advanced integrations. You can run `agent acp` and connect a custom client over stdio using JSON-RPC.**

| Without ACP | With ACP |
|-------------|----------|
| Use Cursor CLI only | Embed Cursor agent in any editor |
| Standard terminal workflow | Custom integrations (Neovim, Zed, etc.) |
| One interface | Build your own client |

> *"ACP is intended for building custom clients and integrations. For normal terminal workflows, use the interactive CLI with `agent`."*

---

## Start ACP Server

Start Cursor CLI in ACP mode:

```bash
agent acp
```

This starts a JSON-RPC server over stdio that speaks the ACP protocol.

---

## Transport and Message Format

| Aspect | Specification |
|--------|---------------|
| **Transport** | stdio (standard input/output) |
| **Protocol envelope** | JSON-RPC 2.0 |
| **Framing** | Newline-delimited JSON (one message per line) |
| **Client → Server** | Writes requests/notifications to stdin |
| **Server → Client** | Writes responses/notifications to stdout |
| **Logs** | May be written to stderr |

---

## Request Flow (Typical ACP Session)

| Step | Action |
|------|--------|
| 1 | `initialize` – handshake |
| 2 | `authenticate` with methodId: `"cursor_login"` |
| 3 | `session/new` (or `session/load` to resume) |
| 4 | `session/prompt` – send user prompt |
| 5 | Handle `session/update` notifications while model streams output |
| 6 | Handle `session/request_permission` by returning a decision |
| 7 | Optionally send `session/cancel` |

---

## Authentication

Cursor CLI advertises `cursor_login` as the ACP auth method. Pre-authenticate before startup using existing CLI auth paths:

```bash
# Login first
agent login

# Or use API key
agent --api-key "$CURSOR_API_KEY" acp

# Or specify endpoint
agent --endpoint https://api2.cursor.sh acp

# Or use key flag
agent -k acp
```

---

## Sessions, Modes, and Permissions

### Sessions

| Method | Purpose |
|--------|---------|
| `session/new` | Create a new session |
| `session/load` | Resume an existing conversation |

### Modes

ACP sessions support the same core modes as CLI:

| Mode | Description |
|------|-------------|
| `agent` | Full tool access |
| `plan` | Planning, read-only behavior |
| `ask` | Q&A/read-only behavior |

### Permissions

When tools need approval, Cursor sends `session/request_permission`. Clients should return one of:

| Response | Meaning |
|----------|---------|
| `allow-once` | Approve this one time |
| `allow-always` | Approve and remember |
| `reject-once` | Reject this time |

> *"If your client does not answer permission requests, tool execution can block."*

---

## MCP Servers in ACP Mode

ACP supports MCP servers defined in:
- Project-level `.cursor/mcp.json`
- User-level `.cursor/mcp.json`

> *"Launch agent from your project directory and approve the servers you want to use."*

### Not Supported:

> *"Team-level MCP servers configured through the Cursor dashboard are not supported in ACP mode."*

---

## Cursor Extension Methods

Cursor sends ACP **extension methods** for richer client UX. There are two types:

### Blocking Methods (Must Respond)

The agent waits for a response. Your client must reply with a JSON-RPC response.

### Notification Methods (Fire-and-Forget)

The agent sends these as notifications. Your client can display them but doesn't need to respond.

---

## Extension Methods Reference

### `cursor/ask_question` (Blocking)

Ask users multiple-choice questions.

**Request:**
```typescript
interface CursorAskQuestionRequest {
  toolCallId: string;
  title?: string;
  questions: Array<{
    id: string;
    prompt: string;
    options: Array<{ id: string; label: string }>;
    allowMultiple?: boolean;
  }>;
}
```

**Response:**
```typescript
interface CursorAskQuestionResponse {
  outcome:
    | { outcome: "answered"; answers: Array<{ questionId: string; selectedOptionIds: string[] }> }
    | { outcome: "skipped"; reason?: string }
    | { outcome: "cancelled" };
}
```

**Example:**
```json
{
  "toolCallId": "call_123",
  "title": "Need input",
  "questions": [{
    "id": "q1",
    "prompt": "Which mode should I use?",
    "options": [
      { "id": "agent", "label": "Agent" },
      { "id": "plan", "label": "Plan" }
    ],
    "allowMultiple": false
  }]
}
```

---

### `cursor/create_plan` (Blocking)

Request explicit plan approval from the user.

**Request:**
```typescript
interface CursorCreatePlanRequest {
  toolCallId: string;
  name?: string;
  overview?: string;
  plan: string;           // Markdown description
  todos: Array<{
    id: string;
    content: string;
    status: "pending" | "in_progress" | "completed" | "cancelled";
  }>;
  isProject?: boolean;
  phases?: Array<{
    name: string;
    todos: Array<{ id: string; content: string; status: string }>;
  }>;
}
```

**Response:**
```typescript
interface CursorCreatePlanResponse {
  outcome:
    | { outcome: "accepted"; planUri?: string }
    | { outcome: "rejected"; reason?: string }
    | { outcome: "cancelled" };
}
```

---

### `cursor/update_todos` (Notification)

Update the client's todo list. Sent as a notification; no response required.

**Request:**
```typescript
interface CursorUpdateTodosRequest {
  toolCallId: string;
  todos: Array<{
    id: string;
    content: string;
    status: "pending" | "in_progress" | "completed" | "cancelled";
  }>;
  merge: boolean;  // true = merge with existing, false = replace
}
```

---

### `cursor/task` (Notification)

Notify the client about a subagent task.

**Request:**
```typescript
interface CursorTaskRequest {
  toolCallId: string;
  description: string;
  prompt: string;
  subagentType:
    | "unspecified"
    | "computer_use"
    | "explore"
    | "video_review"
    | "browser_use"
    | "shell"
    | "vm_setup_helper"
    | { custom: string };
  model?: string;
  agentId?: string;      // Resume previous subagent
  durationMs?: number;
}
```

---

### `cursor/generate_image` (Notification)

Notify the client about a generated image.

**Request:**
```typescript
interface CursorGenerateImageRequest {
  toolCallId: string;
  description: string;
  filePath?: string;
  referenceImagePaths?: string[];
}
```

---

## Minimal Node.js Client Example

```javascript
import { spawn } from "node:child_process";
import readline from "node:readline";

const agent = spawn("agent", ["acp"], {
  stdio: ["pipe", "pipe", "inherit"]
});

let nextId = 1;
const pending = new Map();

function send(method, params) {
  const id = nextId++;
  const message = JSON.stringify({ jsonrpc: "2.0", id, method, params });
  agent.stdin.write(message + "\n");
  return new Promise((resolve, reject) => {
    pending.set(id, { resolve, reject });
  });
}

// Read responses from agent
const rl = readline.createInterface({ input: agent.stdout });
rl.on("line", (line) => {
  if (!line.trim()) return;
  const response = JSON.parse(line);
  if (response.id && pending.has(response.id)) {
    const { resolve } = pending.get(response.id);
    pending.delete(response.id);
    resolve(response);
  }
});

// Example: Initialize session
async function main() {
  // Initialize
  const init = await send("initialize", {
    protocolVersion: "0.1.0",
    clientInfo: { name: "my-client", version: "1.0.0" }
  });
  console.log("Initialized:", init.result);

  // Authenticate
  const auth = await send("authenticate", { methodId: "cursor_login" });
  console.log("Authenticated:", auth.result);

  // Create session
  const session = await send("session/new", {});
  console.log("Session created:", session.result);

  // Send prompt
  const prompt = await send("session/prompt", {
    sessionId: session.result.sessionId,
    message: "What files are in this directory?"
  });
  console.log("Prompt sent:", prompt.result);
}

main().catch(console.error);
```

---

## Integrations

### Neovim (avante.nvim)

avante.nvim is a Neovim plugin that provides an AI-powered coding assistant. It supports ACP, so you can connect it to Cursor's agent.

**Configuration example (lazy.nvim):**

```lua
return {
  {
    "yetone/avante.nvim",
    event = "VeryLazy",
    version = false,
    build = "make",
    opts = {
      provider = "cursor",
      mode = "agentic",
      acp_providers = {
        cursor = {
          command = os.getenv("HOME") .. "/.local/bin/agent",
          args = { "acp" },
          auth_method = "cursor_login",
          env = {
            HOME = os.getenv("HOME"),
            PATH = os.getenv("PATH"),
          },
        },
      },
    },
    dependencies = {
      "nvim-lua/plenary.nvim",
      "MunifTanjim/nui.nvim",
      "nvim-tree/nvim-web-devicons",
      {
        "MeanderingProgrammer/render-markdown.nvim",
        opts = { file_types = { "markdown", "Avante" } },
      },
    },
  },
}
```

**Key settings:**

| Setting | Value | Description |
|---------|-------|-------------|
| `provider` | `"cursor"` | Route requests through Cursor's agent |
| `mode` | `"agentic"` | Full tool access (file edits, terminal). Use `"normal"` for chat-only |
| `command` | `~/.local/bin/agent` | Path to agent binary |
| `auth_method` | `"cursor_login"` | Run `agent login` first to authenticate |

### Zed Editor

Integrate with Zed's modern editor by spawning `agent acp` and communicating over stdio. Zed extensions can implement the ACP client protocol to route AI requests to Cursor.

### Custom Editors

Any editor with extension support can implement an ACP client:
1. Spawn the agent process
2. Send JSON-RPC messages over stdio
3. Handle responses in your editor's UI

---

## Building an Integration (Checklist)

| Step | Action |
|------|--------|
| 1 | Spawn `agent acp` as a child process |
| 2 | Communicate over stdin/stdout using JSON-RPC |
| 3 | Handle `session/update` notifications to display streaming responses |
| 4 | Respond to `session/request_permission` when tools need approval |
| 5 | Optionally implement Cursor extension methods for richer UX |

> *"See the minimal Node.js client above for a working reference implementation."*

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **Start server** | `agent acp` |
| **Transport** | stdio |
| **Protocol** | JSON-RPC 2.0 |
| **Framing** | Newline-delimited JSON |
| **Auth method** | `cursor_login` |
| **Modes** | agent, plan, ask |
| **MCP support** | Project/user level only (not team) |
| **Extension methods** | `cursor/ask_question`, `cursor/create_plan`, `cursor/update_todos`, `cursor/task`, `cursor/generate_image` |

---

## Common Beginner Questions

### Q: Is ACP for me as a beginner?
**A:** No – this is for developers building custom integrations.

### Q: What's the difference between ACP and normal CLI?
**A:** Normal CLI is interactive for humans. ACP is a protocol for programs to talk to the agent.

### Q: Can I use ACP with Neovim?
**A:** Yes – avante.nvim supports ACP with Cursor.

### Q: Can I use ACP with Zed?
**A:** Yes – Zed extensions can implement the ACP client protocol.

### Q: Do MCP servers work in ACP mode?
**A:** Project and user-level MCP servers work. Team-level MCP servers are not supported.

### Q: How do I handle permission requests?
**A:** Your client must respond to `session/request_permission` with `allow-once`, `allow-always`, or `reject-once`.

---

## The Bottom Line

**ACP (Agent Client Protocol) lets you embed Cursor's AI agent into any editor or application that can speak JSON-RPC over stdio.**

**Think of it as:**
- **Normal CLI** = Terminal chat for humans 💬
- **ACP mode** = API for programs 💻

**For developers:** This is how you integrate Cursor with:
- Neovim (via avante.nvim)
- Zed editor
- Custom editors
- Your own tools

**The protocol is JSON-RPC 2.0** – simple to implement. The extension methods give you rich features like multi-choice questions, plan approval, and todo tracking.

**Neovim users:** The avante.nvim configuration example shows exactly how to set it up. Run `agent login` once, then configure the plugin.

