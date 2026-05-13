This is the **TypeScript SDK** documentation – it explains how to call Cursor's agent **programmatically from your own TypeScript/JavaScript code**.

Think of this as the **developer API** for Cursor – instead of using the Cursor app, you can integrate Cursor's AI agent directly into your own scripts, CI pipelines, or applications.

Let me break this down. (Note: This is an **advanced developer** feature.)

---

## What Is the TypeScript SDK? (The 10-Second Summary)

**The `@cursor/sdk` package lets you call Cursor's agent from your own code.** The same agent that runs in the Cursor IDE, CLI, and web app is now scriptable from TypeScript.

| Without SDK | With SDK |
|-------------|----------|
| Use Cursor app only | Script agents programmatically |
| Manual interaction | Automated workflows |
| One-off tasks | Integrated into your own tools |

> *"The SDK wraps local and cloud runtimes behind one interface. You write the same code regardless of where the agent runs."*

**Status:** Public Beta (APIs may change before general availability)

---

## Overview: Three Runtimes

The SDK supports **three runtimes** behind the same interface:

| Runtime | What it does | When to use |
|---------|--------------|-------------|
| **Local** | Runs agent inline in your Node process. Files come from disk. | Dev scripts, CI checks against a working tree |
| **Cloud (Cursor-hosted)** | Runs in isolated VM with your repo cloned in. | Caller doesn't have the repo, need many parallel agents, or runs need to survive disconnection |
| **Cloud (self-hosted)** | Same shape, but you run the VMs via self-hosted pool. | Code, secrets, and artifacts must stay in your environment |

> *"Runtime is picked by which key you pass to `Agent.create()` (local or cloud). Use the same `CURSOR_API_KEY` for either."*

---

## Authentication

Set `CURSOR_API_KEY` (or pass `apiKey`) before creating an agent.

```bash
export CURSOR_API_KEY="your-key"
```

**Supported API keys:**
- User API keys (from Cursor Dashboard → Integrations)
- Service account API keys (from Team settings)
- ❌ Team Admin API keys (not yet supported)

---

## Usage and Billing

> *"SDK runs follow the same pricing, request pools, and Privacy Mode rules as runs from the IDE and Cloud Agents."*

Spend shows up in your team's usage dashboard under the **SDK** tag.

---

## Quick Start: One-Shot Prompt

The easiest way to get started:

```typescript
import { Agent } from "@cursor/sdk";

const result = await Agent.prompt(
  "What does the auth middleware do?",
  {
    apiKey: process.env.CURSOR_API_KEY!,
    model: { id: "composer-2" },
    local: { cwd: process.cwd() }
  }
);

console.log(result.result); // agent's response
```

`Agent.prompt()` is a one-shot convenience: creates an agent, sends a single prompt, waits for the run to finish, and disposes.

---

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Agent** | A durable entity that maintains conversation history and workspace state across multiple runs |
| **Run** | A single execution (one prompt/response cycle) on an agent |
| **Stream** | Real-time events from a run (assistant text, thinking, tool calls) |

---

## Creating an Agent (Local)

```typescript
import { Agent } from "@cursor/sdk";

const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2" },
  local: {
    cwd: process.cwd()  // working directory
  }
});
```

### Creating an Agent (Cloud)

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2" },
  cloud: {
    repos: [{
      url: "https://github.com/your-org/your-repo",
      startingRef: "main"
    }]
  }
});
```

### Cloud with PR:

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  cloud: {
    repos: [{
      prUrl: "https://github.com/your-org/your-repo/pull/123"
    }],
    autoCreatePR: true
  }
});
```

---

## Sending Messages (Runs)

Each `agent.send()` returns a `Run`. The agent retains conversation context across runs.

```typescript
// Send a message
const run = await agent.send("Find the bug in src/auth.ts");

// Stream the response in real-time
for await (const event of run.stream()) {
  switch (event.type) {
    case "assistant":
      for (const block of event.message.content) {
        if (block.type === "text") {
          process.stdout.write(block.text);
        }
      }
      break;
    case "thinking":
      process.stdout.write(event.text);
      break;
    case "tool_call":
      console.log(`[tool] ${event.name}: ${event.status}`);
      break;
    case "status":
      console.log(`[status] ${event.status}`);
      break;
  }
}

// Follow-up (retains context)
const run2 = await agent.send("Fix it and add a regression test");
await run2.wait();

console.log(run2.status); // "finished" | "error" | "cancelled"
console.log(run2.result);  // final assistant text
```

### Sending Images:

```typescript
const run = await agent.send({
  text: "What's in this screenshot?",
  images: [{
    data: base64Png,
    mimeType: "image/png"
  }]
});
```

---

## Run Operations

| Method | Description |
|--------|-------------|
| `run.stream()` | AsyncGenerator of real-time events |
| `run.wait()` | Promise that resolves when run finishes |
| `run.cancel()` | Cancel the run |
| `run.conversation()` | Get structured per-turn view of the run |
| `run.supports(operation)` | Check if operation is available |
| `run.onDidChangeStatus(callback)` | Listen to status changes |

### Run Status Values:

```typescript
type RunStatus = "running" | "finished" | "error" | "cancelled";
```

---

## Listing Agents

```typescript
// List local agents
const result = await Agent.list({
  runtime: "local",
  cwd: process.cwd(),
  limit: 20
});

// List cloud agents
const result = await Agent.list({
  runtime: "cloud",
  prUrl: "https://github.com/your-org/your-repo/pull/123",
  includeArchived: true,
  limit: 20
});

for (const agentInfo of result.items) {
  console.log(agentInfo.agentId, agentInfo.name, agentInfo.status);
}
```

---

## Agent Lifecycle Management

| Method | Description |
|--------|-------------|
| `Agent.archive(agentId)` | Soft delete (can unarchive) |
| `Agent.unarchive(agentId)` | Restore archived agent |
| `Agent.delete(agentId)` | Permanent deletion (irreversible) |

```typescript
await Agent.archive(agentId);      // soft-delete
await Agent.unarchive(agentId);    // restore
await Agent.delete(agentId);       // permanent (returns 404 after)
```

---

## Resource Management (Important!)

Always dispose agents when done. The cleanest pattern is **`await using`** (TypeScript 5.2+):

```typescript
await using agent = await Agent.create({ /* ... */ });
// agent automatically disposed when block exits
```

To dispose explicitly:

```typescript
await agent[Symbol.asyncDispose]();  // full cleanup
agent.close();                       // fire-and-forget
agent.reload();                      // reload config without disposing
```

---

## Streaming Event Types

| Event Type | Description |
|------------|-------------|
| `system` | Init metadata (model, tools) |
| `user` | Echo of user prompt |
| `assistant` | Model text output |
| `thinking` | Reasoning content |
| `tool_call` | Tool invocation lifecycle (start, completion) |
| `status` | Cloud run lifecycle transitions |
| `task` | Task-level milestones |
| `request` | Awaiting user input or approval |

### Update Types (Finer Granularity):

| Update Type | Description |
|-------------|-------------|
| `text-delta` | Streaming text chunks |
| `thinking-delta` | Streaming thinking chunks |
| `thinking-completed` | Thinking block finished |
| `tool-call-started` | Tool invocation began |
| `tool-call-completed` | Tool invocation finished |
| `step-started/completed` | Step boundaries |
| `turn-ended` | End of turn with token usage |
| `shell-output-delta` | Terminal output chunks |

---

## MCP Servers (Bring Your Own Tools)

You can attach MCP servers to agents:

### Local MCP:

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "auto" },
  local: { cwd: process.cwd() },
  mcpServers: {
    docs: {
      type: "http",
      url: "https://example.com/mcp",
      auth: {
        CLIENT_ID: "client-id",
        scopes: ["read", "write"]
      }
    },
    filesystem: {
      type: "stdio",
      command: "npx",
      args: ["-y", "@modelcontextprotocol/server-filesystem", process.cwd()]
    }
  }
});
```

### Cloud MCP:

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2" },
  cloud: {
    repos: [{ url: "https://github.com/your-org/your-repo" }],
    mcpServers: {
      linear: {
        type: "http",
        url: "https://mcp.linear.app/",
        headers: {
          Authorization: `Bearer ${process.env.LINEAR_API_KEY}`
        }
      },
      figma: {
        type: "http",
        url: "https://api.figma.com/mcp",
        auth: {
          CLIENT_ID: process.env.FIGMA_CLIENT_ID,
          CLIENT_SECRET: process.env.FIGMA_CLIENT_SECRET,
          scopes: ["file_content:read"]
        }
      }
    }
  }
});
```

### MCP Configuration Load Order (Local)

1. Inline `mcpServers` on `agent.send()` (overrides)
2. Inline `mcpServers` on `Agent.create()`
3. Plugin servers (if `local.settingsources` includes "plugins")
4. Project servers (`.cursor/mcp.json`)
5. User servers (`~/.cursor/mcp.json`)

> *"Without `local.settingsources`, only inline servers are loaded."*

---

## Subagents

Define named subagents that the main agent can spawn:

```typescript
const agent = await Agent.create({
  model: { id: "composer-2" },
  apiKey: process.env.CURSOR_API_KEY,
  local: { cwd: process.cwd() },
  agents: {
    "code-reviewer": {
      description: "Expert code reviewer for quality and security.",
      prompt: "Review code for bugs, security issues, and proven approaches.",
      model: "inherit"
    },
    "test-writer": {
      description: "Writes tests for code changes.",
      prompt: "Write comprehensive tests for the given code."
    }
  }
});
```

Subagents committed to the repo at `.cursor/agents/*.md` are also picked up. Inline definitions override file-based ones with the same name.

---

## Hooks

Hooks are **file-based only** – no programmatic callback.

- **Local:** Add `.cursor/hooks.json` to the repo passed as `local.cwd`, or add `~/.cursor/hooks.json` for user-level hooks.
- **Cloud:** Commit `.cursor/hooks.json` and its scripts to the repo passed in `cloud.repos`. SDK-created cloud agents load project hooks automatically. On Enterprise plans, they also run team hooks and enterprise-managed hooks.

---

## Artifacts (Cloud Only)

List and download files from the agent's workspace:

```typescript
const artifacts: SDKArtifact[] = await agent.listArtifacts();

for (const artifact of artifacts) {
  console.log(artifact.path, artifact.sizeBytes);
  const buffer = await agent.downloadArtifact(artifact.path);
  // save buffer to disk or process
}
```

> *"Artifact support is runtime-dependent. Local SDK agents currently return no artifacts and throw for `downloadArtifact`."*

---

## Account-Level Methods (`Cursor` namespace)

### Get API Key Info:

```typescript
const me = await Cursor.me({ apiKey: process.env.CURSOR_API_KEY });
console.log(me.apiKeyName, me.userEmail, me.createdAt);
```

### List Available Models:

```typescript
const models = await Cursor.models.list();
for (const model of models.items) {
  console.log(model.id, model.displayName);
}
```

---

## Error Handling

All SDK errors extend `CursorAgentError`:

| Error Type | When |
|------------|------|
| `AuthenticationError` | Invalid API key, not logged in, insufficient permissions |
| `RateLimitError` | Too many requests or usage limits exceeded |
| `ConfigurationError` | Invalid model, bad request parameters |
| `IntegrationNotConnectedError` | SCM provider not connected (includes `helpUrl` to reconnect) |
| `NetworkError` | Service unavailable, timeout |
| `UnknownAgentError` | Catch-all for unclassified errors |

**Use `isRetryable` to drive retry logic:**

```typescript
try {
  await agent.send("Do something");
} catch (err) {
  if (err.isRetryable) {
    // retry with backoff
  }
}
```

### IntegrationNotConnectedError:

```typescript
class IntegrationNotConnectedError extends ConfigurationError {
  readonly provider: string;  // "github", "gitlab", "azuredevops"
  readonly helpUrl: string;   // dashboard link to reconnect
}
```

Use `helpUrl` to point the user at the right reconnect flow.

### UnsupportedRunOperationError:

Thrown when a Run operation is not available on the current runtime. Use `run.supports(operation)` to check before calling.

---

## Configuration Reference

### `AgentOptions` (Partial)

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `model` | `ModelSelection` | Required for local | Model to use |
| `apiKey` | `string` | `CURSOR_API_KEY` env | User or service account key |
| `name` | `string` | Auto-generated | Human-readable agent name |
| `local.cwd` | `string` | - | Working directory (local runtime) |
| `cloud.repos` | `array` | - | Repositories to work on (cloud runtime) |
| `cloud.autoCreatePR` | `boolean` | false | Auto-create PR when run completes |
| `mcpServers` | `object` | - | MCP server configurations |
| `agents` | `object` | - | Subagent definitions |

### `ModelSelection`

```typescript
interface ModelSelection {
  id: string;                    // "composer-2", "gpt-5.2", etc.
  params?: ModelParameterValue[];  // [{ id: "thinking", value: "high" }]
}
```

Use `Cursor.models.list()` to discover valid IDs, parameter definitions, and preset variants.

### `McpServerConfig`

```typescript
type McpServerConfig =
  | {  // stdio
      type?: "stdio";
      command: string;
      args?: string[];
      env?: Record<string, string>;
      cwd?: string;  // local only
    }
  | {  // HTTP / SSE
      type?: "http" | "sse";
      url: string;
      headers?: Record<string, string>;
      auth?: {
        CLIENT_ID: string;
        CLIENT_SECRET?: string;
        scopes?: string[];
      };
    };
```

---

## Known Limitations

| Limitation | Description |
|------------|-------------|
| **Inline MCP servers** | Not persisted across `Agent.resume()` – pass them again |
| **Artifact download** | Not implemented for local agents (returns empty list, throws on download) |
| **`local.settingsSources`** | Does not apply to cloud agents (cloud always loads project/team/plugins) |
| **Hooks** | File-based only (`.cursor/hooks.json`). No programmatic callbacks |

---

## Complete Example

```typescript
import { Agent, Cursor } from "@cursor/sdk";

async function main() {
  // List available models
  const models = await Cursor.models.list();
  console.log("Available models:", models.items.map(m => m.id));

  // Create a cloud agent
  await using agent = await Agent.create({
    apiKey: process.env.CURSOR_API_KEY!,
    model: { id: "composer-2" },
    cloud: {
      repos: [{ url: "https://github.com/your-org/your-repo" }],
      autoCreatePR: true
    },
    name: "My SDK Agent"
  });

  // Send a prompt and stream the response
  const run = await agent.send("Add a README with setup instructions");
  
  for await (const event of run.stream()) {
    if (event.type === "assistant") {
      for (const block of event.message.content) {
        if (block.type === "text") {
          console.log(block.text);
        }
      }
    }
  }

  // Wait for completion
  const result = await run.wait();
  console.log(`Status: ${result.status}`);
  console.log(`Duration: ${result.durationMs}ms`);

  // List artifacts
  const artifacts = await agent.listArtifacts();
  for (const artifact of artifacts) {
    console.log(`Artifact: ${artifact.path} (${artifact.sizeBytes} bytes)`);
  }
}

main().catch(console.error);
```

---

## Common Beginner Questions

### Q: Is this for me as a beginner?
**A:** No – this is an advanced developer feature for building integrations and automations.

### Q: Do I need a paid Cursor plan?
**A:** Yes – SDK runs follow the same pricing as Cloud Agents.

### Q: Can I use the SDK with CI/CD pipelines?
**A:** Yes – local runtime works great for CI checks. Cloud runtime for more complex workflows.

### Q: What's the difference between local and cloud runtime?
**A:** Local runs on your machine (files from disk). Cloud runs in isolated VMs (repos cloned fresh).

### Q: Can I cancel a running agent?
**A:** Yes – `await run.cancel()`.

### Q: Can I attach MCP servers to SDK agents?
**A:** Yes – both local stdio and remote HTTP MCP servers are supported.

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **Package** | `@cursor/sdk` |
| **Status** | Public Beta |
| **Authentication** | `CURSOR_API_KEY` env or `apiKey` parameter |
| **Runtimes** | Local, Cloud (Cursor-hosted), Cloud (self-hosted) |
| **Key classes** | `Agent`, `Run`, `Cursor` |
| **Resource cleanup** | Use `await using` or explicit `dispose()` |
| **Streaming** | SSE events via `run.stream()` |
| **Artifacts** | Cloud only via `listArtifacts()` / `downloadArtifact()` |
| **MCP** | Supported (stdio + HTTP) |
| **Hooks** | File-based only (`.cursor/hooks.json`) |

---

## The Bottom Line

**The TypeScript SDK lets you integrate Cursor's AI agent directly into your own code, scripts, and applications.**

**Think of it as:**
- **Cursor app** = Manual use 🖱️
- **SDK** = Programmatic use 💻

**Use cases:**
- CI/CD pipelines that automatically fix test failures
- Automated code review bots
- Integration with internal developer tools
- Batch processing of code changes
- Building custom AI-powered developer tools

**For developers:** The SDK is powerful. You can run agents locally for fast iteration or in the cloud for scalability. The same code works across both runtimes. MCP support lets you connect your own tools. Streaming gives you real-time visibility.

**Key APIs to remember:**
- `Agent.create()` – create a new agent
- `Agent.prompt()` – one-shot convenience
- `agent.send()` – send a message (returns Run)
- `run.stream()` – real-time events
- `run.wait()` – wait for completion
- `Agent.list()` – list existing agents
- `Cursor.models.list()` – get available models