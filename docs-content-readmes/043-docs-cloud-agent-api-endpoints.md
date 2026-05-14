This is the **Cloud Agents API** documentation – it explains how to **programmatically launch and manage cloud agents** using HTTP requests.

Think of this as the **automation layer** for Cloud Agents – instead of clicking buttons in a dashboard, you can write code to create agents, send them tasks, stream their responses, and download their artifacts.

Let me break this down. (Note: This is a **developer/API** documentation for advanced users.)

---

## Overview

**Status:** Public Beta (APIs may change before general availability)

**Authentication:** Basic Authentication using an API key

**API Key Sources:**
- User API key – from Cursor Dashboard → Integrations
- Service account API key – for team/automation use

---

## Core Concept: Agent + Runs

The v1 API introduces a **durable agent** plus **per-prompt runs** (different from the flatter v0 API).

| Concept | Description |
|---------|-------------|
| **Agent** | A durable entity that maintains conversation history and workspace state across multiple runs |
| **Run** | A single execution (one prompt/response cycle) on an agent |

This means you can:
1. Create an agent once
2. Send multiple follow-up prompts (runs) to the same agent
3. The agent remembers previous context

---

## Authentication

All API requests use **Basic Authentication**:

```bash
curl -u YOUR_API_KEY: https://api.cursor.com/v1/...
```

The colon after the API key is required (empty password).

---

## Endpoints Summary

### Agent Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/v1/agents` | Create an agent and enqueue initial run |
| GET | `/v1/agents` | List agents (newest first) |
| GET | `/v1/agents/{id}` | Get agent metadata |
| POST | `/v1/agents/{id}/archive` | Soft delete (can unarchive) |
| POST | `/v1/agents/{id}/unarchive` | Restore archived agent |
| DELETE | `/v1/agents/{id}` | Permanently delete (irreversible) |

### Run Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/v1/agents/{id}/runs` | Send follow-up prompt (new run) |
| GET | `/v1/agents/{id}/runs` | List runs for an agent |
| GET | `/v1/agents/{id}/runs/{runId}` | Get run status |
| GET | `/v1/agents/{id}/runs/{runId}/stream` | Stream SSE events |
| POST | `/v1/agents/{id}/runs/{runId}/cancel` | Cancel active run |

### Artifacts

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/agents/{id}/artifacts` | List artifacts produced by agent |
| GET | `/v1/agents/{id}/artifacts/download` | Get presigned URL for artifact |

### Metadata

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/me` | Get API key info |
| GET | `/v1/models` | List available model IDs |
| GET | `/v1/repositories` | List accessible GitHub repos |

### Worker Tokens

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/v1/sub-tokens` | Create user-scoped token for My Machines |

---

## Create an Agent (POST /v1/agents)

### Request Body:

```json
{
  "prompt": {
    "text": "Add a README with setup instructions",
    "images": []  // optional, base64-encoded, max 5 images, 15MB each
  },
  "model": {
    "id": "composer-2",
    "params": [
      { "id": "thinking", "value": "high" }
    ]
  },
  "repos": [
    {
      "url": "https://github.com/your-org/your-repo",
      "startingRef": "main"
    }
  ],
  "branchName": "feature/readme",
  "autoGenerateBranch": true,
  "autoCreatePR": true,
  "skipReviewerRequest": false,
  "envVars": {
    "API_KEY": "secret-value"
  }
}
```

### Field Details:

| Field | Required | Description |
|-------|----------|-------------|
| `prompt.text` | ✅ Yes | The instruction text for the agent |
| `prompt.images` | No | Base64-encoded images (max 5, 15MB each) |
| `model.id` | No | Model ID from GET /v1/models (omit for default) |
| `model.params` | No | Per-model parameters (e.g., `thinking: high`) |
| `repos[].url` | See note | GitHub repo URL (unless `prUrl` provided) |
| `repos[].startingRef` | No | Branch/tag/commit hash to start from |
| `repos[].prUrl` | See note | PR URL (overrides `url` and `startingRef`) |
| `branchName` | No | Custom branch name |
| `autoGenerateBranch` | No | Default `true` – create new branch |
| `autoCreatePR` | No | Open PR when run completes |
| `skipReviewerRequest` | No | Skip requesting user as reviewer (if `autoCreatePR: true`) |
| `envVars` | No | Session-scoped env vars (names can't start with `cursor_`) |

**Note about `repos`:** Provide either `url` OR `prUrl` – not both.

### Response:

```json
{
  "id": "bc-00000000-0000-0000-0000-000000000001",
  "name": "Add README with setup instructions",
  "status": "ACTIVE",
  "env": { "type": "cloud" },
  "url": "https://cursor.com/agents?id=bc-...",
  "createdAt": "2026-04-13T18:30:00.000Z",
  "updatedAt": "2026-04-13T18:45:00.000Z"
}
```

---

## List Agents (GET /v1/agents)

### Query Parameters:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `limit` | 20 | Number to return (max 100) |
| `cursor` | - | Pagination cursor |
| `prUrl` | - | Filter by PR URL |
| `includeArchived` | true | Include archived agents |

### Response:

```json
{
  "items": [
    {
      "id": "bc-...",
      "name": "Add README...",
      "status": "ACTIVE",
      "env": { "type": "cloud" },
      "url": "https://cursor.com/agents?id=bc-...",
      "createdAt": "2026-04-13T18:30:00.000Z",
      "updatedAt": "2026-04-13T18:45:00.000Z"
    }
  ],
  "nextCursor": null
}
```

---

## Get an Agent (GET /v1/agents/{id})

Returns **durable metadata** for an agent (repos, branchName, autoCreatePR, etc.).

To get execution status, fetch `latestRunId` and call Get A Run.

### Response includes:

```json
{
  "id": "bc-...",
  "name": "Add README...",
  "status": "ACTIVE",
  "env": { "type": "cloud" },
  "repos": [
    {
      "url": "https://github.com/your-org/your-repo",
      "startingRef": "main"
    }
  ],
  "createdAt": "...",
  "updatedAt": "..."
}
```

---

## Create a Run (POST /v1/agents/{id}/runs)

Send a **follow-up prompt** to an existing active agent. Uses the agent's current conversation and workspace state.

**Important:** Only one run can be active per agent. If another run is in progress, you get `409 agent_busy`.

### Request Body:

```json
{
  "prompt": {
    "text": "Also add troubleshooting steps"
  }
}
```

### Response:

```json
{
  "run": {
    "id": "run-00000000-0000-0000-0000-000000000001",
    "agentId": "bc-...",
    "status": "CREATING",
    "createdAt": "2026-04-13T18:50:00.000Z"
  }
}
```

---

## List Runs (GET /v1/agents/{id}/runs)

List runs for an agent, newest first.

### Response:

```json
{
  "items": [
    {
      "id": "run-...",
      "agentId": "bc-...",
      "status": "RUNNING",
      "createdAt": "...",
      "updatedAt": "..."
    }
  ],
  "nextCursor": null
}
```

---

## Get a Run (GET /v1/agents/{id}/runs/{runId})

Get status and timestamps for a specific run.

### Run Status Values:

| Status | Meaning |
|--------|---------|
| `CREATING` | Run is being initialized |
| `RUNNING` | Agent is actively working |
| `FINISHED` | Run completed successfully |
| `CANCELLED` | Run was cancelled |
| `ERROR` | Run failed |

### Response:

```json
{
  "id": "run-...",
  "agentId": "bc-...",
  "status": "FINISHED",
  "createdAt": "2026-04-13T18:30:00.000Z",
  "updatedAt": "2026-04-13T18:45:00.000Z"
}
```

---

## Stream a Run (GET /v1/agents/{id}/runs/{runId}/stream)

Stream **Server-Sent Events (SSE)** for a run.

### Event Types:

| Event | Payload | Description |
|-------|---------|-------------|
| `status` | `{ runId, status }` | Run status update |
| `assistant` | `{ text }` | Assistant text delta |
| `thinking` | `{ text }` | Thinking text delta |
| `tool_call` | (varies) | Tool call status update |
| `heartbeat` | - | Keepalive event |
| `result` | `{ runId, status }` | Terminal run status |
| `error` | `{ code, message }` | Stream error |
| `done` | `{}` | Stream complete |

### Example Stream:

```
event: status
data: {"runId":"run-...","status":"RUNNING"}

id: 1713033500000-0
event: assistant
data: {"text":"I'll update the README now."}

event: result
data: {"runId":"run-...","status":"FINISHED"}
```

### Resuming a Stream (After Disconnect):

SSE responses include `id` values. To resume:

```
Last-Event-ID: <most_recent_event_id>
```

### Retention:

Stream responses include `X-Cursor-Stream-Retention-Seconds` header. After retention window elapses, endpoint may return `410 stream_expired` – read terminal state via Get A Run instead.

---

## Cancel a Run (POST /v1/agents/{id}/runs/{runId}/cancel)

Cancel the active run. Cancellation is **terminal** – run transitions to `CANCELLED` and cannot be resumed.

To continue the conversation, create a **new run** on the same agent.

**Returns `409 run_not_cancellable`** if run is already terminal or was never active.

---

## Artifacts

Artifacts are **agent-scoped** (workspace persists across runs).

### List Artifacts (GET /v1/agents/{id}/artifacts)

```bash
curl -u YOUR_API_KEY: https://api.cursor.com/v1/agents/bc-.../artifacts
```

Response:
```json
{
  "items": [
    {
      "path": "artifacts/screenshot.png",
      "sizeBytes": 12345,
      "updatedAt": "2026-04-13T18:45:00.000Z"
    }
  ]
}
```

### Download Artifact (GET /v1/agents/{id}/artifacts/download)

```bash
curl -u YOUR_API_KEY: 'https://api.cursor.com/v1/agents/bc-.../artifacts/download?path=artifacts/screenshot.png'
```

Response (15-minute presigned URL):
```json
{
  "url": "https://cloud-agent-artifacts.s3.us-east-1.amazonaws.com/...",
  "expiresAt": "2026-04-13T19:00:00.000Z"
}
```

**Note:** v1 paths are **relative** (e.g., `artifacts/screenshot.png`). Absolute v0 paths (`/opt/cursor/artifacts/...`) are not accepted.

---

## Agent Lifecycle

### Archive (Soft Delete):

```bash
curl -X POST -u YOUR_API_KEY: https://api.cursor.com/v1/agents/bc-.../archive
```

- Agent remains readable
- Cannot accept new runs
- Reversible via unarchive

### Unarchive:

```bash
curl -X POST -u YOUR_API_KEY: https://api.cursor.com/v1/agents/bc-.../unarchive
```

### Permanent Delete (Irreversible):

```bash
curl -X DELETE -u YOUR_API_KEY: https://api.cursor.com/v1/agents/bc-...
```

---

## Worker Tokens (My Machines)

### Create User-Scoped Worker Token (POST /v1/sub-tokens)

Create a **1-hour user-scoped token** for a My Machines worker to run as an active team member.

**Requires:** Agent-scoped **team service account API key**

**Token expires after 1 hour** – mint a new token when refreshing.

**By email:**
```bash
curl -X POST https://api.cursor.com/v1/sub-tokens \
  -H "Authorization: Bearer $CURSOR_SERVICE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"forUserEmail": "alice@company.com"}'
```

**By user ID:**
```bash
curl -X POST https://api.cursor.com/v1/sub-tokens \
  -H "Authorization: Bearer $CURSOR_SERVICE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"forUserId": 42}'
```

---

## Metadata Endpoints

### API Key Info (GET /v1/me)

```bash
curl -u YOUR_API_KEY: https://api.cursor.com/v1/me
```

Response:
```json
{
  "apiKeyName": "Production API Key",
  "createdAt": "2026-04-13T18:30:00.000Z",
  "userEmail": "developer@example.com"
}
```

### List Models (GET /v1/models)

Returns recommended model IDs for `model.id` field.

```bash
curl -u YOUR_API_KEY: https://api.cursor.com/v1/models
```

Response:
```json
{
  "items": [
    "claude-4-sonnet-thinking",
    "gpt-5.2",
    "claude-4.5-sonnet-thinking"
  ]
}
```

**To use default model:** Omit `model` from request body. Cursor resolves: user default → team default → system default.

### List GitHub Repositories (GET /v1/repositories)

List GitHub repos accessible through Cursor's GitHub App.

**⚠️ Strict rate limits:**
- 1 request per user per minute
- 30 requests per user per hour
- May take tens of seconds for users with many repos

```bash
curl -u YOUR_API_KEY: https://api.cursor.com/v1/repositories
```

Response:
```json
{
  "items": [
    { "url": "https://github.com/your-org/your-repo" }
  ]
}
```

---

## Full Example: Create and Run an Agent

### 1. Create Agent:

```bash
curl -X POST https://api.cursor.com/v1/agents \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {
      "text": "Add a README with setup instructions"
    },
    "repos": [{
      "url": "https://github.com/your-org/your-repo",
      "startingRef": "main"
    }],
    "autoCreatePR": true
  }'
```

### 2. Stream the Run:

```bash
curl -u YOUR_API_KEY: \
  -H "Accept: text/event-stream" \
  https://api.cursor.com/v1/agents/bc-.../runs/run-.../stream
```

### 3. List Artifacts:

```bash
curl -u YOUR_API_KEY: https://api.cursor.com/v1/agents/bc-.../artifacts
```

### 4. Download Artifact:

```bash
curl -u YOUR_API_KEY: 'https://api.cursor.com/v1/agents/bc-.../artifacts/download?path=artifacts/screenshot.png'
```

---

## Common Beginner Questions

### Q: Is this for beginners?
**A:** No – this is for developers building integrations and automation.

### Q: What's the difference between v0 and v1 API?
**A:** v1 splits work into **durable agent + runs** (better for follow-ups). v0 is flatter.

### Q: How do I get an API key?
**A:** Cursor Dashboard → Integrations → Generate API key.

### Q: What's a service account API key?
**A:** For team/automation use – tokens that run under team identity.

### Q: Can I resume a stream after disconnecting?
**A:** Yes – use `Last-Event-ID` header with the most recent event id.

### Q: How long do artifacts stay available?
**A:** The download URL is valid for **15 minutes**. Artifacts themselves persist with the agent.

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **Base URL** | `https://api.cursor.com/v1/` |
| **Authentication** | Basic Auth with API key |
| **Status** | Public Beta |
| **Agent** | Durable entity with conversation history |
| **Run** | Single execution on an agent |
| **Streaming** | SSE (Server-Sent Events) |
| **Artifacts** | Agent-scoped, download via presigned URL |
| **Rate limits (repos)** | 1/min, 30/hour per user |

---

## The Bottom Line

**The Cloud Agents API lets you programmatically integrate Cursor's AI capabilities into your own tools and workflows.**

**Think of it as:**
- **Dashboard** = Manual control 🖱️
- **API** = Programmatic control 💻

**Use cases:**
- Automating code reviews in CI/CD
- Building custom chatbots that can write code
- Integrating Cursor agents into internal tools
- Creating scheduled tasks that fix issues automatically

**For beginners:** You don't need this. But if you're building integrations, the API is powerful – you can create agents, stream their responses, download artifacts, and manage the full lifecycle programmatically.

