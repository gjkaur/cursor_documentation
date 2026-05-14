# Cloud Agents API – Complete Beginner's Guide

This document explains the **Cloud Agents API** in detail – how to programmatically create, manage, and monitor Cloud Agents using HTTP requests. This is the API version of launching agents from the web dashboard or CLI.

Let me break this down for a complete beginner.

---

## What Is the Cloud Agents API? (The 10-Second Summary)

**The Cloud Agents API lets you programmatically launch and manage cloud agents that work on your repositories.**

| Without API | With API |
|-------------|----------|
| Click buttons in dashboard | Automate agent launches from scripts |
| Manual monitoring | Programmatically check status |
| One-off tasks | Scheduled, repeatable workflows |

> *"Public beta – The Cloud Agents API v1 is in public beta. APIs may change before general availability."*

**Important:** This is a beta feature. APIs might change, so don't build critical systems that depend on exact behavior yet.

---

## Core Concept: Agent + Runs

The v1 API introduces a **durable agent** plus **per-prompt runs**. This is different from older versions.

| Concept | Description | Analogy |
|---------|-------------|---------|
| **Agent** | A durable entity that maintains conversation history and workspace state | A dedicated workspace |
| **Run** | A single execution (one prompt/response cycle) | One conversation thread |

**Example workflow:**
1. Create an agent called "Feature Builder"
2. Send first run: "Add login button" → Agent works
3. Send second run: "Add logout button" → Agent remembers context and continues

**Key benefit:** The agent remembers everything between runs. You don't need to re-explain the project.

---

## Authentication

All API requests use **Basic Authentication** with an API key.

```bash
curl -u YOUR_API_KEY: https://api.cursor.com/v1/...
```

**Note:** The colon after the API key is required (empty password).

### Where to Get an API Key:

| API Key Type | Where to Get | Best For |
|--------------|--------------|----------|
| **User API key** | Dashboard → Integrations | Individual developers |
| **Service account API key** | Team settings → Service Accounts | Automation, CI/CD |

---

## Complete API Endpoints Reference

### Agent Management

| Method | Endpoint | What it does |
|--------|----------|--------------|
| POST | `/v1/agents` | Create a new agent and start its first run |
| GET | `/v1/agents` | List all your agents |
| GET | `/v1/agents/{id}` | Get details about a specific agent |
| POST | `/v1/agents/{id}/archive` | Soft delete (can restore later) |
| POST | `/v1/agents/{id}/unarchive` | Restore an archived agent |
| DELETE | `/v1/agents/{id}` | Permanently delete (cannot undo) |

### Run Management

| Method | Endpoint | What it does |
|--------|----------|--------------|
| POST | `/v1/agents/{id}/runs` | Send a follow-up prompt to an agent |
| GET | `/v1/agents/{id}/runs` | List all runs for an agent |
| GET | `/v1/agents/{id}/runs/{runId}` | Get status of a specific run |
| GET | `/v1/agents/{id}/runs/{runId}/stream` | Watch the agent work in real-time |
| POST | `/v1/agents/{id}/runs/{runId}/cancel` | Stop a running agent |

### Artifacts (Outputs)

| Method | Endpoint | What it does |
|--------|----------|--------------|
| GET | `/v1/agents/{id}/artifacts` | List files the agent created |
| GET | `/v1/agents/{id}/artifacts/download` | Get a download link for an artifact |

### Metadata

| Method | Endpoint | What it does |
|--------|----------|--------------|
| GET | `/v1/me` | Get info about your API key |
| GET | `/v1/models` | List available AI models |
| GET | `/v1/repositories` | List your GitHub repos |

### Worker Tokens (Advanced)

| Method | Endpoint | What it does |
|--------|----------|--------------|
| POST | `/v1/sub-tokens` | Create a token for My Machines worker |

---

## 1. Create an Agent (POST /v1/agents)

This is the most important endpoint. It creates a Cloud Agent and starts its first run.

### Request Body Fields

| Field | Required? | What it does | Example |
|-------|-----------|--------------|---------|
| `prompt.text` | ✅ Yes | The instruction for the agent | "Add a README file" |
| `prompt.images` | No | Base64-encoded images (max 5, 15MB each) | `"data:image/png;base64,..."` |
| `model.id` | No | Which AI model to use (omit for default) | `"composer-2"` |
| `model.params` | No | Model settings (thinking effort, etc.) | `[{"id":"thinking","value":"high"}]` |
| `repos[].url` | See note | GitHub repo URL | `"https://github.com/your-org/repo"` |
| `repos[].startingRef` | No | Branch/tag/commit to start from | `"main"` |
| `repos[].prUrl` | See note | Work on an existing PR instead | `"https://github.com/.../pull/123"` |
| `branchName` | No | Custom branch name | `"feature/add-readme"` |
| `autoGenerateBranch` | No | Create new branch? (default: true) | `true` |
| `autoCreatePR` | No | Open a PR when done? | `true` |
| `skipReviewerRequest` | No | Skip requesting reviewer? | `false` |
| `envVars` | No | Environment variables for the agent | `{"API_KEY":"secret"}` |

**Note about `repos`:** Provide either `url` OR `prUrl` – not both.

### Complete Example

```bash
curl -X POST https://api.cursor.com/v1/agents \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {
      "text": "Add a README.md file with setup instructions and a badges section"
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
    "branchName": "feature/add-readme",
    "autoCreatePR": true
  }'
```

### Response Explained

```json
{
  "agent": {
    "id": "bc-00000000-0000-0000-0000-000000000001",
    "name": "Add README with setup instructions",
    "status": "ACTIVE",
    "env": { "type": "cloud" },
    "url": "https://cursor.com/agents?id=bc-...",
    "createdAt": "2026-04-13T18:30:00.000Z",
    "latestRunId": "run-00000000-0000-0000-0000-000000000001"
  },
  "run": {
    "id": "run-00000000-0000-0000-0000-000000000001",
    "status": "CREATING"
  }
}
```

| Field | What it means |
|-------|---------------|
| `agent.id` | Unique identifier for the agent (keep this!) |
| `agent.status` | `ACTIVE` means ready to accept runs |
| `agent.url` | Link to view agent in web dashboard |
| `run.id` | Identifier for this specific run |
| `run.status` | `CREATING` → `RUNNING` → `FINISHED` |

---

## 2. List Agents (GET /v1/agents)

Get a list of all your agents, newest first.

### Query Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `limit` | 20 | Number of agents to return (max 100) |
| `cursor` | - | For pagination (use `nextCursor` from response) |
| `prUrl` | - | Filter by PR URL |
| `includeArchived` | true | Include archived agents? |

### Example

```bash
curl -u YOUR_API_KEY: "https://api.cursor.com/v1/agents?limit=20"
```

### Response

```json
{
  "items": [
    {
      "id": "bc-00000000-0000-0000-0000-000000000001",
      "name": "Add README...",
      "status": "ACTIVE",
      "url": "https://cursor.com/agents?id=bc-...",
      "createdAt": "2026-04-13T18:30:00.000Z",
      "latestRunId": "run-00000000-0000-0000-0000-000000000001"
    }
  ],
  "nextCursor": "bc-00000000-0000-0000-0000-000000000002"
}
```

**Note:** Use `nextCursor` to get the next page of results.

---

## 3. Get an Agent (GET /v1/agents/{id})

Get detailed information about a specific agent.

### Example

```bash
curl -u YOUR_API_KEY: \
  https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001
```

### Response (More Detailed)

```json
{
  "id": "bc-00000000-0000-0000-0000-000000000001",
  "name": "Add README...",
  "status": "ACTIVE",
  "repos": [
    {
      "url": "https://github.com/your-org/your-repo",
      "startingRef": "main"
    }
  ],
  "branchName": "feature/add-readme",
  "autoCreatePR": true,
  "url": "https://cursor.com/agents?id=bc-...",
  "createdAt": "2026-04-13T18:30:00.000Z",
  "latestRunId": "run-00000000-0000-0000-0000-000000000001"
}
```

**Note:** This endpoint returns full metadata. The list endpoint only returns basic info.

---

## 4. Create a Run (POST /v1/agents/{id}/runs)

Send a **follow-up prompt** to an existing agent. The agent remembers previous conversation.

### Important Rules

> *"Only one run can be active per agent. Calling this while another run is `CREATING` or `RUNNING` returns `409 agent_busy`."*

### Example

```bash
curl -X POST https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/runs \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {
      "text": "Also add troubleshooting steps to the README"
    }
  }'
```

### Response

```json
{
  "run": {
    "id": "run-00000000-0000-0000-0000-000000000002",
    "agentId": "bc-00000000-0000-0000-0000-000000000001",
    "status": "CREATING",
    "createdAt": "2026-04-13T18:50:00.000Z"
  }
}
```

---

## 5. Stream a Run (GET /v1/agents/{id}/runs/{runId}/stream)

**This is the most exciting endpoint!** Watch the agent work in real-time, like watching someone type.

### Event Types

| Event | When it happens | What you see |
|-------|-----------------|--------------|
| `status` | Run status changes | "RUNNING", "FINISHED" |
| `assistant` | Agent speaks | The agent's response text |
| `thinking` | Agent is reasoning | Internal thought process |
| `tool_call` | Agent uses a tool | "Reading file X", "Running command Y" |
| `heartbeat` | Keep-alive | Connection still alive |
| `result` | Run completes | Final status |
| `error` | Something went wrong | Error message |
| `done` | Stream ends | End of stream |

### Example

```bash
curl -N -u YOUR_API_KEY: \
  -H "Accept: text/event-stream" \
  "https://api.cursor.com/v1/agents/bc-.../runs/run-.../stream"
```

### What the Stream Looks Like

```
event: status
data: {"runId":"run-...","status":"RUNNING"}

id: 1713033000000-0
event: assistant
data: {"text":"I'll update the README"}

id: 1713033010000-0
event: tool_call
data: {"callId":"call_123","name":"read_file","status":"started"}

id: 1713033020000-0
event: result
data: {"runId":"run-...","status":"FINISHED"}

id: 1713033020000-0
event: done
data: {}
```

### Resuming After Disconnect

If your connection drops, you can resume from where you left off:

```
Last-Event-ID: 1713033010000-0
```

### Retention

Stream responses include `X-Cursor-Stream-Retention-Seconds` header. After that time, you'll get `410 stream_expired` – check the run status via Get A Run instead.

---

## 6. Cancel a Run (POST /v1/agents/{id}/runs/{runId}/cancel)

Stop a running agent. Cancellation is **terminal** – cannot be resumed.

### Example

```bash
curl -X POST https://api.cursor.com/v1/agents/bc-.../runs/run-.../cancel \
  -u YOUR_API_KEY:
```

### Response

```json
{
  "id": "run-00000000-0000-0000-0000-000000000001"
}
```

**Note:** Returns `409 run_not_cancellable` if the run is already finished or never started.

---

## 7. List Artifacts (GET /v1/agents/{id}/artifacts)

Artifacts are files the agent produced – screenshots, logs, generated code, etc.

### Example

```bash
curl -u YOUR_API_KEY: \
  https://api.cursor.com/v1/agents/bc-.../artifacts
```

### Response

```json
{
  "items": [
    {
      "path": "artifacts/screenshot.png",
      "sizeBytes": 12345,
      "updatedAt": "2026-04-13T18:45:00.000Z"
    },
    {
      "path": "artifacts/README.md",
      "sizeBytes": 2048,
      "updatedAt": "2026-04-13T18:45:00.000Z"
    }
  ]
}
```

---

## 8. Download an Artifact (GET /v1/agents/{id}/artifacts/download)

Get a temporary download link for an artifact (valid for 15 minutes).

### Example

```bash
curl -u YOUR_API_KEY: \
  'https://api.cursor.com/v1/agents/bc-.../artifacts/download?path=artifacts/screenshot.png'
```

### Response

```json
{
  "url": "https://cloud-agent-artifacts.s3.us-east-1.amazonaws.com/...",
  "expiresAt": "2026-04-13T19:00:00.000Z"
}
```

Then download the file:

```bash
curl -L -o screenshot.png "https://cloud-agent-artifacts.s3.us-east-1.amazonaws.com/..."
```

---

## 9. Agent Lifecycle Management

### Archive (Soft Delete)

Reversible – agent stays readable but cannot accept new runs.

```bash
curl -X POST https://api.cursor.com/v1/agents/bc-.../archive -u YOUR_API_KEY:
```

### Unarchive

Restore an archived agent.

```bash
curl -X POST https://api.cursor.com/v1/agents/bc-.../unarchive -u YOUR_API_KEY:
```

### Permanent Delete (Irreversible)

```bash
curl -X DELETE https://api.cursor.com/v1/agents/bc-... -u YOUR_API_KEY:
```

**Use with caution!** This cannot be undone.

---

## 10. Worker Tokens (For My Machines)

Create a **1-hour token** for a My Machines worker to run as a team member.

**Requires:** Service account API key

### By Email

```bash
curl -X POST https://api.cursor.com/v1/sub-tokens \
  -H "Authorization: Bearer $CURSOR_SERVICE_ACCOUNT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"forUserEmail": "alice@company.com"}'
```

### By User ID

```bash
curl -X POST https://api.cursor.com/v1/sub-tokens \
  -H "Authorization: Bearer $CURSOR_SERVICE_ACCOUNT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"forUserId": 42}'
```

### Response

```json
{
  "accessToken": "eyJ...",
  "expiresAt": "2026-04-24T19:00:00.000Z",
  "userId": 42,
  "teamId": 456
}
```

**Note:** Tokens expire after 1 hour. Mint a new one when needed.

---

## 11. Metadata Endpoints

### API Key Info (GET /v1/me)

Get information about your API key.

```bash
curl -u YOUR_API_KEY: https://api.cursor.com/v1/me
```

**Response:**
```json
{
  "apiKeyName": "Production API Key",
  "createdAt": "2026-04-13T18:30:00.000Z",
  "userEmail": "developer@example.com"
}
```

### List Models (GET /v1/models)

Get available model IDs for the `model.id` field.

```bash
curl -u YOUR_API_KEY: https://api.cursor.com/v1/models
```

**Response:**
```json
{
  "items": [
    "claude-4-sonnet-thinking",
    "gpt-5.2",
    "claude-4.5-sonnet-thinking",
    "composer-2",
    "gpt-5-mini"
  ]
}
```

### List GitHub Repositories (GET /v1/repositories)

⚠️ **Very strict rate limits:** 1 request per minute, 30 per hour.

```bash
curl -u YOUR_API_KEY: https://api.cursor.com/v1/repositories
```

**Response:**
```json
{
  "items": [
    { "url": "https://github.com/your-org/your-repo" }
  ]
}
```

---

## Complete Example: Python Script

```python
#!/usr/bin/env python3
"""
Complete Cloud Agents API example
"""

import requests
import json
import time
import sys

API_KEY = "your_api_key_here"
BASE_URL = "https://api.cursor.com/v1"

def create_agent(repo_url, prompt_text):
    """Create a new Cloud Agent"""
    url = f"{BASE_URL}/agents"
    auth = (API_KEY, "")
    payload = {
        "prompt": {"text": prompt_text},
        "repos": [{"url": repo_url}],
        "autoCreatePR": True
    }
    
    response = requests.post(url, auth=auth, json=payload)
    response.raise_for_status()
    return response.json()

def stream_run(agent_id, run_id):
    """Stream agent output in real-time"""
    url = f"{BASE_URL}/agents/{agent_id}/runs/{run_id}/stream"
    auth = (API_KEY, "")
    
    response = requests.get(url, auth=auth, stream=True)
    
    print("📡 Streaming agent output...\n")
    
    for line in response.iter_lines():
        if line:
            line = line.decode('utf-8')
            if line.startswith('event:'):
                event_type = line[6:].strip()
            elif line.startswith('data:'):
                data = json.loads(line[5:])
                if event_type == 'assistant':
                    print(f"🤖: {data.get('text', '')}")
                elif event_type == 'tool_call':
                    print(f"🔧: {data.get('name', 'unknown')} - {data.get('status')}")
                elif event_type == 'result':
                    print(f"✅: {data.get('status')}")
                elif event_type == 'done':
                    print("🏁 Stream complete")

def list_artifacts(agent_id):
    """List all artifacts from an agent"""
    url = f"{BASE_URL}/agents/{agent_id}/artifacts"
    auth = (API_KEY, "")
    
    response = requests.get(url, auth=auth)
    response.raise_for_status()
    return response.json().get('items', [])

def main():
    REPO_URL = "https://github.com/your-org/your-repo"
    PROMPT = "Add a README.md file with setup instructions"
    
    print("🚀 Creating Cloud Agent...")
    result = create_agent(REPO_URL, PROMPT)
    
    agent_id = result['agent']['id']
    run_id = result['run']['id']
    
    print(f"✅ Agent ID: {agent_id}")
    print(f"✅ Run ID: {run_id}")
    print(f"🔗 Dashboard: https://cursor.com/agents/{agent_id}")
    
    print("\n⏳ Waiting 5 seconds for agent to start...")
    time.sleep(5)
    
    # Stream the run (optional - comment out for long runs)
    # stream_run(agent_id, run_id)
    
    # Check status
    status_url = f"{BASE_URL}/agents/{agent_id}/runs/{run_id}"
    status_response = requests.get(status_url, auth=(API_KEY, ""))
    status_data = status_response.json()
    
    print(f"\n📊 Current status: {status_data.get('status')}")
    
    # List artifacts when complete
    if status_data.get('status') == 'FINISHED':
        print("\n📎 Checking for artifacts...")
        artifacts = list_artifacts(agent_id)
        for artifact in artifacts:
            print(f"  - {artifact['path']} ({artifact['sizeBytes']} bytes)")

if __name__ == "__main__":
    main()
```

---

## Complete Example: Bash Script

```bash
#!/bin/bash

API_KEY="your_api_key_here"
BASE_URL="https://api.cursor.com/v1"

# Create an agent
echo "Creating agent..."
RESPONSE=$(curl -s -X POST "$BASE_URL/agents" \
  -u "$API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {"text": "Add a README.md file"},
    "repos": [{"url": "https://github.com/your-org/your-repo"}],
    "autoCreatePR": true
  }')

AGENT_ID=$(echo "$RESPONSE" | jq -r '.agent.id')
RUN_ID=$(echo "$RESPONSE" | jq -r '.run.id')

echo "Agent ID: $AGENT_ID"
echo "Run ID: $RUN_ID"

# Check status
sleep 5
STATUS=$(curl -s -u "$API_KEY:" \
  "$BASE_URL/agents/$AGENT_ID/runs/$RUN_ID" | jq -r '.status')

echo "Status: $STATUS"

# List artifacts when complete
if [ "$STATUS" = "FINISHED" ]; then
  echo "Artifacts:"
  curl -s -u "$API_KEY:" \
    "$BASE_URL/agents/$AGENT_ID/artifacts" | jq '.items[]'
fi
```

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **Base URL** | `https://api.cursor.com/v1/` |
| **Authentication** | Basic Auth with API key |
| **Status** | Public Beta |
| **Agent** | Durable entity with conversation history |
| **Run** | Single execution on an agent |
| **Artifacts** | Files produced by agent (screenshots, logs) |
| **Streaming** | SSE (Server-Sent Events) |

### Run Status Values

| Status | Meaning |
|--------|---------|
| `CREATING` | Run is being initialized |
| `RUNNING` | Agent is actively working |
| `FINISHED` | Run completed successfully |
| `CANCELLED` | Run was cancelled |
| `ERROR` | Run failed |

### Agent Status Values

| Status | Meaning |
|--------|---------|
| `ACTIVE` | Agent can accept runs |
| `ARCHIVED` | Soft-deleted |

---

## Common Beginner Questions

### Q: What's the difference between an Agent and a Run?
**A:** Agent = durable workspace (keeps memory across runs). Run = one conversation.

### Q: Can I have multiple runs at the same time?
**A:** No – only one active run per agent. Wait or cancel the current run first.

### Q: How do I get the agent's final output?
**A:** Stream the run or check the run status when `FINISHED`.

### Q: How long do artifacts stay available?
**A:** The download URL expires in 15 minutes. The artifacts themselves persist.

### Q: What's the difference between v0 and v1 API?
**A:** v1 has "durable agent + runs" (better for follow-ups). v0 is flatter.

### Q: Can I resume a stream after disconnect?
**A:** Yes – use `Last-Event-ID` header with the last event ID.

### Q: What does `409 agent_busy` mean?
**A:** Another run is already active on this agent. Wait or cancel it.

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is the Cloud Agents API?** | Programmatic way to launch and manage Cloud Agents |
| **Do I need it?** | Only if you're building automations or integrations |
| **How do I authenticate?** | API key with Basic Auth |
| **What's an Agent vs Run?** | Agent = durable workspace; Run = single execution |
| **Can I stream responses?** | Yes – SSE events in real-time |
| **Where are artifacts?** | Listed via `/artifacts`, downloaded via presigned URL |
| **Is this production-ready?** | Public beta – APIs may change |

---

## The Bottom Line

**The Cloud Agents API lets you programmatically launch, monitor, and manage Cloud Agents – integrating Cursor's AI capabilities into your own tools and workflows.**

**Think of it as:**
- **Web Dashboard** = Manual control 🖱️
- **API** = Programmatic control 💻

**For beginners:** Start with creating an agent (`POST /v1/agents`) and streaming the response (`GET .../stream`). Then try listing artifacts. The Python example above gives you a complete working script.

**Key workflow:**
1. Create agent → get `agent_id` and `run_id`
2. Stream the run (watch in real-time)
3. Check status when done
4. Download artifacts

**Remember:** This is a **beta** API. Build accordingly – don't assume stability for critical systems.

# Webhooks – Complete Beginner's Guide

This document explains Cursor's **Webhooks** – how to receive automatic notifications when your Cloud Agents complete or encounter errors.

Think of webhooks as **automated phone calls** that Cursor makes to your server when something important happens.

Let me break this down for a complete beginner.

---

## What Are Webhooks? (The 10-Second Summary)

**When you create an agent with a webhook URL, Cursor will send HTTP POST requests to notify you about status changes.**

| Without Webhooks | With Webhooks |
|------------------|---------------|
| You manually check agent status | Cursor tells you when it's done |
| Poll the API repeatedly | Receive instant notifications |
| Wait and wonder | Get automatic updates |

> *"Currently, only `statusChange` events are supported, specifically when an agent encounters an `ERROR` or `FINISHED` state."*

---

## How Webhooks Work

```
┌─────────────────────────────────────────────────────────────────┐
│                    HOW WEBHOOKS WORK                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. You create an agent with a webhook URL                      │
│     ↓                                                           │
│  2. Agent starts working                                        │
│     ↓                                                           │
│  3. Agent finishes (or fails)                                   │
│     ↓                                                           │
│  4. Cursor sends an HTTP POST to your webhook URL               │
│     ↓                                                           │
│  5. Your server receives the notification                       │
│     ↓                                                           │
│  6. You can trigger actions (send Slack message, update DB, etc)│
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Analogy:** Webhooks are like leaving your phone number when you order food. Instead of you calling repeatedly to ask "Is it ready?", they call you when it's done.

---

## When Do Webhooks Trigger?

Currently, webhooks trigger for **status changes** when an agent reaches a terminal state:

| Event | When it happens |
|-------|-----------------|
| `FINISHED` | Agent completed successfully |
| `ERROR` | Agent encountered an error |

**Note:** Only these two events are supported currently. More events may be added in the future.

---

## Webhook Headers (What Cursor Sends)

Every webhook request includes these headers:

| Header | What it contains | Example |
|--------|------------------|---------|
| `X-Webhook-Signature` | Digital signature to verify it's from Cursor | `sha256=abc123def456...` |
| `X-Webhook-ID` | Unique identifier for this delivery | `wh_abc123` |
| `X-Webhook-Event` | The type of event | `statusChange` |
| `User-Agent` | Identifies Cursor as the sender | `Cursor-Agent-Webhook/1.0` |

### Why These Headers Matter

| Header | Purpose |
|--------|---------|
| **Signature** | Proves the request really came from Cursor (not a hacker) |
| **Webhook ID** | Helps you track and debug individual webhook deliveries |
| **Event Type** | Tells you what happened (currently always `statusChange`) |
| **User-Agent** | Helps identify the sender in your logs |

---

## Webhook Signature Verification (Important Security!)

**This is critical.** Anyone could send fake webhooks to your endpoint. Signature verification ensures requests actually came from Cursor.

### How It Works

1. Cursor creates a **secret key** (you provide it)
2. Cursor calculates a signature using that secret
3. Cursor sends the signature in the `X-Webhook-Signature` header
4. Your server recalculates the signature using the same secret
5. If they match → request is genuine
6. If they don't match → request is fake (ignore it)

### Python Example

```python
import hmac
import hashlib

def verify_webhook(secret, raw_body, signature):
    """
    Verify that a webhook request actually came from Cursor.
    
    Args:
        secret: Your webhook secret (keep this safe!)
        raw_body: The raw request body (as bytes, not parsed JSON)
        signature: The signature from X-Webhook-Signature header
    
    Returns:
        True if signature is valid, False otherwise
    """
    # Calculate expected signature
    expected = 'sha256=' + hmac.new(
        secret.encode(),     # Your secret as bytes
        raw_body,            # Raw request body as bytes
        hashlib.sha256       # SHA256 algorithm
    ).hexdigest()
    
    # Compare with received signature
    return hmac.compare_digest(expected, signature)
```

### Node.js (JavaScript) Example

```javascript
const crypto = require('crypto');

function verifyWebhook(secret, rawBody, signature) {
    // Calculate expected signature
    const expected = 'sha256=' + 
        crypto.createHmac('sha256', secret)
            .update(rawBody)
            .digest('hex');
    
    // Compare with received signature
    return signature === expected;
}
```

### Important Note

> *"Always use the raw request body (before any parsing) when computing the signature."*

**Why?** JSON parsing can change the formatting (spaces, line breaks). The signature is calculated on the exact raw bytes sent by Cursor.

**Wrong way:**
```python
# DON'T do this
body = request.get_json()  # Parsed JSON
signature = request.headers.get('X-Webhook-Signature')
verify_webhook(secret, json.dumps(body), signature)  # May fail!
```

**Right way:**
```python
# DO this
raw_body = request.get_data()  # Raw bytes
signature = request.headers.get('X-Webhook-Signature')
verify_webhook(secret, raw_body, signature)  # Works correctly
```

---

## Webhook Payload Format (What Cursor Sends)

The webhook sends a JSON object with this structure:

```json
{
  "event": "statusChange",
  "timestamp": "2024-01-15T10:30:00Z",
  "id": "bc_abc123",
  "status": "FINISHED",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents?id=bc_abc123",
    "branchName": "cursor/add-readme-1234",
    "prUrl": "https://github.com/your-org/your-repo/pull/1234"
  },
  "summary": "Added README.md with installation instructions"
}
```

### Fields Explained

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `event` | string | Type of event | `"statusChange"` |
| `timestamp` | string | When the event occurred (ISO format) | `"2024-01-15T10:30:00Z"` |
| `id` | string | Agent ID that triggered the webhook | `"bc_abc123"` |
| `status` | string | Final status of the agent | `"FINISHED"` or `"ERROR"` |
| `source.repository` | string (optional) | Repository the agent worked on | `"https://github.com/..."` |
| `source.ref` | string (optional) | Branch/tag/commit reference | `"main"` |
| `target.url` | string (optional) | Link to view agent in dashboard | `"https://cursor.com/..."` |
| `target.branchName` | string (optional) | Branch name created by agent | `"cursor/add-readme-1234"` |
| `target.prUrl` | string (optional) | Pull Request URL (if created) | `"https://github.com/.../pull/1234"` |
| `summary` | string (optional) | Summary of what the agent did | `"Added README.md..."` |

**Note:** Some fields are optional and only included when available (e.g., `prUrl` only appears if `autoCreatePR` was true).

---

## Complete Example: Python Webhook Server

Here's a complete Flask server that receives and verifies webhooks:

```python
#!/usr/bin/env python3
"""
Webhook receiver for Cursor Cloud Agents
Run with: python webhook_server.py
"""

from flask import Flask, request, jsonify
import hmac
import hashlib
import json
import os

app = Flask(__name__)

# Your webhook secret – store securely! (use environment variable)
WEBHOOK_SECRET = os.environ.get('WEBHOOK_SECRET', 'your-secret-here')

def verify_signature(raw_body, signature_header):
    """Verify that the webhook came from Cursor"""
    if not signature_header:
        return False
    
    # Expected format: "sha256=abc123..."
    if not signature_header.startswith('sha256='):
        return False
    
    # Extract the actual signature
    received_signature = signature_header[7:]  # Remove "sha256=" prefix
    
    # Calculate expected signature
    expected = hmac.new(
        WEBHOOK_SECRET.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()
    
    # Compare securely (prevents timing attacks)
    return hmac.compare_digest(expected, received_signature)

@app.route('/webhook/cursor', methods=['POST'])
def cursor_webhook():
    """Receive and process Cursor webhooks"""
    
    # Get raw request body (before parsing)
    raw_body = request.get_data()
    
    # Get signature header
    signature = request.headers.get('X-Webhook-Signature', '')
    webhook_id = request.headers.get('X-Webhook-ID', 'unknown')
    event_type = request.headers.get('X-Webhook-Event', 'unknown')
    
    print(f"\n📨 Received webhook: {webhook_id}")
    print(f"   Event: {event_type}")
    
    # Verify signature
    if not verify_signature(raw_body, signature):
        print("   ❌ Invalid signature! Ignoring request.")
        return jsonify({"error": "Invalid signature"}), 401
    
    print("   ✅ Signature verified")
    
    # Parse the payload
    payload = request.get_json()
    
    # Extract important fields
    agent_id = payload.get('id')
    status = payload.get('status')
    summary = payload.get('summary', 'No summary')
    
    print(f"\n📊 Agent {agent_id} status: {status}")
    print(f"   Summary: {summary}")
    
    # Check for PR URL
    pr_url = payload.get('target', {}).get('prUrl')
    if pr_url:
        print(f"   🔗 PR created: {pr_url}")
    
    # Take action based on status
    if status == 'FINISHED':
        print("✅ Agent completed successfully!")
        # Here you could:
        # - Send a Slack notification
        # - Update a database
        # - Trigger a deployment
        # - Send an email
        send_slack_notification(f"Agent {agent_id} completed: {summary}")
        
    elif status == 'ERROR':
        print("❌ Agent failed!")
        send_slack_notification(f"⚠️ Agent {agent_id} failed!")
    
    # Always return 200 to acknowledge receipt
    return jsonify({"status": "received"}), 200

def send_slack_notification(message):
    """Example: Send a notification to Slack"""
    # This is just an example – implement your own
    print(f"   📢 Slack notification: {message}")
    
    # Real implementation would use requests.post() to Slack webhook
    # import requests
    # requests.post(SLACK_WEBHOOK_URL, json={"text": message})

@app.route('/webhook/health', methods=['GET'])
def health():
    """Health check endpoint for monitoring"""
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    print("🚀 Starting webhook server on port 5000")
    print(f"📋 Webhook secret configured: {'*' * 10}")
    print("📍 Endpoint: http://localhost:5000/webhook/cursor")
    print("🔒 Verify signatures: ON")
    
    # Run the server
    app.run(host='0.0.0.0', port=5000, debug=True)
```

---

## Complete Example: Node.js Webhook Server

```javascript
// webhook-server.js
// Run with: node webhook-server.js

const express = require('express');
const crypto = require('crypto');

const app = express();
const PORT = 5000;

// Your webhook secret – use environment variable in production
const WEBHOOK_SECRET = process.env.WEBHOOK_SECRET || 'your-secret-here';

// Disable body parsing for raw access
app.use(express.json({ verify: (req, res, buf) => {
    req.rawBody = buf;
} }));

function verifySignature(rawBody, signatureHeader) {
    if (!signatureHeader) return false;
    if (!signatureHeader.startsWith('sha256=')) return false;
    
    const receivedSignature = signatureHeader.substring(7);
    
    const expected = crypto.createHmac('sha256', WEBHOOK_SECRET)
        .update(rawBody)
        .digest('hex');
    
    return crypto.timingSafeEqual(
        Buffer.from(receivedSignature),
        Buffer.from(expected)
    );
}

app.post('/webhook/cursor', (req, res) => {
    const rawBody = req.rawBody;
    const signature = req.headers['x-webhook-signature'];
    const webhookId = req.headers['x-webhook-id'] || 'unknown';
    const eventType = req.headers['x-webhook-event'] || 'unknown';
    
    console.log(`\n📨 Received webhook: ${webhookId}`);
    console.log(`   Event: ${eventType}`);
    
    // Verify signature
    if (!verifySignature(rawBody, signature)) {
        console.log('   ❌ Invalid signature!');
        return res.status(401).json({ error: 'Invalid signature' });
    }
    
    console.log('   ✅ Signature verified');
    
    const payload = req.body;
    const agentId = payload.id;
    const status = payload.status;
    const summary = payload.summary || 'No summary';
    
    console.log(`\n📊 Agent ${agentId} status: ${status}`);
    console.log(`   Summary: ${summary}`);
    
    // Check for PR URL
    const prUrl = payload.target?.prUrl;
    if (prUrl) {
        console.log(`   🔗 PR created: ${prUrl}`);
    }
    
    // Take action based on status
    if (status === 'FINISHED') {
        console.log('✅ Agent completed successfully!');
        // Send Slack notification, update database, etc.
    } else if (status === 'ERROR') {
        console.log('❌ Agent failed!');
    }
    
    res.json({ status: 'received' });
});

app.get('/webhook/health', (req, res) => {
    res.json({ status: 'healthy' });
});

app.listen(PORT, () => {
    console.log(`🚀 Webhook server running on port ${PORT}`);
    console.log(`📍 Endpoint: http://localhost:${PORT}/webhook/cursor`);
});
```

---

## Setting Up a Webhook

### When Creating an Agent via API

Include the `webhookUrl` field in your request:

```bash
curl -X POST https://api.cursor.com/v1/agents \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {"text": "Add a README file"},
    "repos": [{"url": "https://github.com/your-org/your-repo"}],
    "webhookUrl": "https://your-server.com/webhook/cursor",
    "webhookSecret": "your-secret-here"
  }'
```

### From the Dashboard

When creating a Cloud Agent from the web dashboard, there is a field to enter your webhook URL and secret.

---

## Best Practices

| Practice | Why | How |
|----------|-----|-----|
| **Verify signatures** | Prevents fake webhooks | Always verify `X-Webhook-Signature` |
| **Use HTTPS** | Encrypts data in transit | Use `https://` URLs in production |
| **Return quickly** | Prevents timeouts | Return 2xx immediately, process async |
| **Handle retries** | Cursor retries failed deliveries | Design your endpoint to be idempotent |
| **Store raw payloads** | Helps with debugging | Log raw body for troubleshooting |
| **Use environment variables** | Keeps secrets safe | Never hardcode secrets in code |

### What "Idempotent" Means

Webhooks may be retried if your endpoint returns an error. Your handler should handle the same webhook multiple times without causing issues.

**Bad (not idempotent):**
```python
# This would create duplicate records!
process_agent_result(payload)  # Creates a new record each time
```

**Good (idempotent):**
```python
# Check if already processed
if not already_processed(payload['id']):
    process_agent_result(payload)
```

---

## Testing Webhooks Locally

### Using ngrok (Expose local server to internet)

```bash
# Install ngrok
brew install ngrok  # on macOS

# Run your webhook server
python webhook_server.py

# In another terminal, expose it
ngrok http 5000

# ngrok gives you a public URL like:
# https://abc123.ngrok.io
```

Use that URL as your webhook endpoint while testing.

### Using a Test Endpoint

You can also use a service like **webhook.site** to test without running a server:

1. Go to webhook.site
2. Copy your unique URL
3. Use it as your webhook endpoint
4. See all webhook deliveries in the browser

---

## Common Beginner Questions

### Q: What happens if my server goes down?
**A:** Cursor will retry failed deliveries. Implement idempotent handlers to handle duplicates.

### Q: How can I test webhooks without a public server?
**A:** Use ngrok (exposes localhost) or webhook.site (test endpoint).

### Q: Do I need to verify signatures?
**A:** YES! Without verification, anyone could send fake webhooks to your endpoint.

### Q: What if I lose my webhook secret?
**A:** Generate a new one when creating the agent. Keep it secure.

### Q: Can I have multiple webhook endpoints?
**A:** Currently, one webhook URL per agent.

### Q: What information does the webhook send?
**A:** Agent ID, status, summary, PR URL (if created), and dashboard link.

### Q: How quickly are webhooks sent?
**A:** Immediately upon status change (FINISHED or ERROR).

---

## Summary Table

| Concept | Description |
|---------|-------------|
| **What it does** | Sends HTTP POST when agent completes or errors |
| **Events** | `statusChange` (FINISHED, ERROR) |
| **Headers** | `X-Webhook-Signature`, `X-Webhook-ID`, `X-Webhook-Event` |
| **Security** | HMAC-SHA256 signature verification |
| **Payload** | JSON with agent info, status, summary, PR URL |
| **Retries** | Yes, if your endpoint returns an error |
| **Best practice** | Verify signatures, return quickly, use HTTPS |

---

## Quick Reference: Webhook Headers

| Header | Format | Purpose |
|--------|--------|---------|
| `X-Webhook-Signature` | `sha256=<hex>` | Verify authenticity |
| `X-Webhook-ID` | `wh_xxx` | Unique delivery ID |
| `X-Webhook-Event` | `statusChange` | Event type |
| `User-Agent` | `Cursor-Agent-Webhook/1.0` | Identify sender |

---

## The Bottom Line

**Webhooks are automated notifications that tell your server when a Cloud Agent finishes or fails.**

**Think of it as:**
- **Polling** = Calling a restaurant every 5 minutes to ask if your order is ready 📞
- **Webhooks** = The restaurant calls you when your order is ready 📱

**For developers:** Webhooks enable powerful automation:
- Send Slack notifications when agents complete
- Update databases with agent results
- Trigger CI/CD pipelines
- Log agent activity for audit purposes
- Auto-merge PRs when checks pass

**The most important rule:** **Always verify the signature!** Never trust a webhook without verification.
