# Module 8: Cloud Agents API and Webhooks

## Cursor Training Program — Day 2

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise |
| **Prerequisites** | User API key, Python 3.8+ installed, ngrok installed |
| **Module Goal** | Programmatically create, stream, and manage Cloud Agents, and set up webhook notifications |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Create a Cloud Agent programmatically using the API
- Stream agent responses in real-time using Server-Sent Events (SSE)
- List and download artifacts from a completed agent
- Create a webhook endpoint to receive agent notifications
- Test webhooks locally using ngrok
- Build an end-to-end automated agent workflow

---

## Lesson 8.1: Creating a Cloud Agent Programmatically

### Concept (5 minutes)

> *"The Cloud Agents API lets you launch agents from your own code – perfect for CI/CD pipelines, scheduled tasks, and custom integrations."*

**Core Concept: Agent + Runs**

| Concept | Description |
|---------|-------------|
| **Agent** | A durable entity that maintains conversation history and workspace state |
| **Run** | A single execution (one prompt/response cycle) |

**Key Endpoint:** `POST /v1/agents`

**Required Fields:**

| Field | Description |
|-------|-------------|
| `prompt.text` | The instruction for the agent |
| `repos[].url` | GitHub repository URL |

### Hands-On Exercise (10 minutes)

**Step 1:** Create a simple Cloud Agent:

```bash
curl -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {
      "text": "Add a README.md file with setup instructions"
    },
    "repos": [
      {
        "url": "https://github.com/YOUR_ORG/YOUR_REPO",
        "startingRef": "main"
      }
    ],
    "autoCreatePR": true
  }' | jq '.'
```

**Step 2:** Capture the Agent ID and Run ID:

```bash
RESPONSE=$(curl -s -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {"text": "Add a README.md file"},
    "repos": [{"url": "https://github.com/YOUR_ORG/YOUR_REPO"}]
  }')

AGENT_ID=$(echo "$RESPONSE" | jq -r '.agent.id')
RUN_ID=$(echo "$RESPONSE" | jq -r '.run.id')

echo "Agent ID: $AGENT_ID"
echo "Run ID: $RUN_ID"
echo "Dashboard: https://cursor.com/agents/$AGENT_ID"
```

**Step 3:** Create an agent with a specific model:

```bash
curl -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {"text": "Review the code for security issues"},
    "model": {"id": "claude-4.7-opus"},
    "repos": [{"url": "https://github.com/YOUR_ORG/YOUR_REPO"}],
    "autoCreatePR": false
  }' | jq '{agent_id: .agent.id, model: .agent.model}'
```

**Success Criteria:**
- [ ] Agent created successfully
- [ ] Agent ID and Run ID captured
- [ ] Agent appears in `cursor.com/agents` dashboard

---

## Lesson 8.2: Streaming Agent Responses (SSE)

### Concept (5 minutes)

> *"Server-Sent Events (SSE) let you watch the agent work in real-time – seeing its thoughts, tool calls, and output as they happen."*

**Event Types:**

| Event | When It Happens | What You Get |
|-------|-----------------|--------------|
| `status` | Run status changes | `{runId, status}` |
| `assistant` | Agent speaks | `{text}` |
| `thinking` | Agent is reasoning | `{text}` |
| `tool_call` | Agent uses a tool | `{callId, name, status}` |
| `result` | Run completes | `{runId, status}` |
| `error` | Something went wrong | `{code, message}` |
| `done` | Stream ends | `{}` |

### Hands-On Exercise (10 minutes)

**Step 1:** Create an agent and capture IDs:

```bash
RESPONSE=$(curl -s -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {"text": "Read the main file and explain what it does"},
    "repos": [{"url": "https://github.com/YOUR_ORG/YOUR_REPO"}],
    "autoCreatePR": false
  }')

AGENT_ID=$(echo "$RESPONSE" | jq -r '.agent.id')
RUN_ID=$(echo "$RESPONSE" | jq -r '.run.id')
```

**Step 2:** Stream the response:

```bash
curl -N -u "$CURSOR_USER_API_KEY:" \
  -H "Accept: text/event-stream" \
  "https://api.cursor.com/v1/agents/$AGENT_ID/runs/$RUN_ID/stream"
```

**Expected output:**
```
event: status
data: {"runId":"run-...","status":"RUNNING"}

event: assistant
data: {"text":"I'll read the main file to understand the codebase."}

event: tool_call
data: {"callId":"call_123","name":"read_file","status":"started"}

event: tool_call
data: {"callId":"call_123","name":"read_file","status":"completed"}

event: result
data: {"runId":"run-...","status":"FINISHED"}
```

**Step 3:** Create a Python streaming client:

```python
#!/usr/bin/env python3
import requests
import json
import os

API_KEY = os.environ.get("CURSOR_USER_API_KEY")
AGENT_ID = "your_agent_id"
RUN_ID = "your_run_id"

url = f"https://api.cursor.com/v1/agents/{AGENT_ID}/runs/{RUN_ID}/stream"
auth = (API_KEY, "")

response = requests.get(url, auth=auth, stream=True)

for line in response.iter_lines():
    if line:
        line = line.decode('utf-8')
        if line.startswith('data:'):
            data = json.loads(line[5:])
            if 'text' in data:
                print(data['text'], end='', flush=True)
```

**Success Criteria:**
- [ ] Stream connected successfully
- [ ] Received status events
- [ ] Received assistant text
- [ ] Created Python streaming client

---

## Lesson 8.3: Listing and Downloading Artifacts

### Concept (5 minutes)

> *"Artifacts are files produced by the agent – screenshots, logs, generated code. You can list and download them programmatically."*

**Endpoints:**

| Endpoint | Purpose |
|----------|---------|
| `GET /v1/agents/{id}/artifacts` | List all artifacts |
| `GET /v1/agents/{id}/artifacts/download` | Get presigned URL for download |

**Important:** Download URLs expire after **15 minutes**.

### Hands-On Exercise (10 minutes)

**Step 1:** Wait for a Cloud Agent to complete, then list artifacts:

```bash
curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts" | jq '.'
```

**Step 2:** Download a specific artifact:

```bash
# Get download URL
DOWNLOAD_URL=$(curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts/download?path=artifacts/screenshot.png" \
  | jq -r '.url')

# Download the file
curl -L -o screenshot.png "$DOWNLOAD_URL"
```

**Step 3:** Download all artifacts:

```bash
curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts" | \
  jq -r '.items[].path' | while read path; do
    filename=$(basename "$path")
    url=$(curl -s -u "$CURSOR_USER_API_KEY:" \
      "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts/download?path=$path" \
      | jq -r '.url')
    curl -L -o "$filename" "$url"
    echo "Downloaded: $filename"
  done
```

**Success Criteria:**
- [ ] Listed artifacts from completed agent
- [ ] Downloaded a single artifact
- [ ] Downloaded all artifacts

---

## Lesson 8.4: Creating a Webhook Endpoint

### Concept (5 minutes)

> *"Webhooks let Cursor notify your server when an agent completes – no polling required."*

**Webhook Headers:**

| Header | Description |
|--------|-------------|
| `X-Webhook-Signature` | HMAC-SHA256 signature for verification |
| `X-Webhook-ID` | Unique delivery ID |
| `X-Webhook-Event` | Event type (`statusChange`) |

**Webhook Payload:**

```json
{
  "event": "statusChange",
  "timestamp": "2025-01-15T10:30:00Z",
  "id": "bc_abc123",
  "status": "FINISHED",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents?id=bc_abc123",
    "prUrl": "https://github.com/.../pull/123"
  },
  "summary": "Added README.md"
}
```

### Hands-On Exercise (10 minutes)

**Step 1:** Create a webhook server `webhook_server.py`:

```python
#!/usr/bin/env python3
from flask import Flask, request, jsonify
import hmac
import hashlib

app = Flask(__name__)
WEBHOOK_SECRET = "your-secret-here"

def verify_signature(raw_body, signature_header):
    if not signature_header or not signature_header.startswith('sha256='):
        return False
    received = signature_header[7:]
    expected = hmac.new(WEBHOOK_SECRET.encode(), raw_body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, received)

@app.route('/webhook/cursor', methods=['POST'])
def cursor_webhook():
    raw_body = request.get_data()
    signature = request.headers.get('X-Webhook-Signature', '')
    
    if not verify_signature(raw_body, signature):
        return jsonify({"error": "Invalid signature"}), 401
    
    payload = request.get_json()
    agent_id = payload.get('id')
    status = payload.get('status')
    
    print(f"✅ Agent {agent_id} status: {status}")
    
    if payload.get('target', {}).get('prUrl'):
        print(f"   PR: {payload['target']['prUrl']}")
    
    return jsonify({"status": "received"}), 200

@app.route('/webhook/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
```

**Step 2:** Install Flask and run the server:

```bash
pip install flask
python webhook_server.py
```

**Success Criteria:**
- [ ] Webhook server running
- [ ] Signature verification implemented
- [ ] Payload parsing working

---

## Lesson 8.5: Testing Webhooks Locally with ngrok

### Concept (5 minutes)

> *"ngrok exposes your local webhook server to the internet so Cursor can send webhooks to your development machine."*

### Hands-On Exercise (10 minutes)

**Step 1:** Start ngrok:

```bash
ngrok http 5000
```

**Step 2:** Copy the HTTPS URL (e.g., `https://abc123.ngrok.io`)

**Step 3:** Create an agent with the webhook URL:

```bash
WEBHOOK_URL="https://abc123.ngrok.io/webhook/cursor"

curl -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {"text": "Add a README.md file"},
    "repos": [{"url": "https://github.com/YOUR_ORG/YOUR_REPO"}],
    "webhookUrl": "'"$WEBHOOK_URL"'",
    "webhookSecret": "your-secret-here"
  }' | jq '.agent.id'
```

**Step 4:** Watch your webhook server terminal for the notification

**Step 5:** Open ngrok web interface at `http://127.0.0.1:4040` to inspect requests

**Success Criteria:**
- [ ] ngrok tunnel established
- [ ] Webhook received by local server
- [ ] Signature verified
- [ ] Payload parsed

---

## Lesson 8.6: End-to-End Automated Agent Workflow

### Concept (5 minutes)

> *"Combine everything into a complete automation script: create agent, stream response, wait for completion, download artifacts."*

### Hands-On Exercise (10 minutes)

**Create `automated_workflow.py`:**

```python
#!/usr/bin/env python3
"""
End-to-end automated agent workflow
"""

import requests
import time
import os
import json
import sys

API_KEY = os.environ.get("CURSOR_USER_API_KEY")
if not API_KEY:
    print("❌ Set CURSOR_USER_API_KEY environment variable")
    sys.exit(1)

BASE_URL = "https://api.cursor.com/v1"
AUTH = (API_KEY, "")

def create_agent(repo_url, prompt, webhook_url=None):
    """Create a Cloud Agent."""
    payload = {
        "prompt": {"text": prompt},
        "repos": [{"url": repo_url}],
        "autoCreatePR": False
    }
    if webhook_url:
        payload["webhookUrl"] = webhook_url
    
    response = requests.post(f"{BASE_URL}/agents", auth=AUTH, json=payload)
    data = response.json()
    return data["agent"]["id"], data["run"]["id"]

def wait_for_completion(agent_id, run_id, timeout=300):
    """Wait for agent to complete."""
    url = f"{BASE_URL}/agents/{agent_id}/runs/{run_id}"
    start = time.time()
    
    while time.time() - start < timeout:
        response = requests.get(url, auth=AUTH)
        status = response.json().get("status")
        print(f"Status: {status}")
        
        if status == "FINISHED":
            return True
        elif status == "ERROR":
            return False
        time.sleep(5)
    return False

def download_artifacts(agent_id):
    """Download all artifacts."""
    resp = requests.get(f"{BASE_URL}/agents/{agent_id}/artifacts", auth=AUTH)
    artifacts = resp.json().get("items", [])
    
    for artifact in artifacts:
        path = artifact["path"]
        url_resp = requests.get(
            f"{BASE_URL}/agents/{agent_id}/artifacts/download",
            auth=AUTH,
            params={"path": path}
        )
        download_url = url_resp.json().get("url")
        if download_url:
            filename = os.path.basename(path)
            r = requests.get(download_url)
            with open(filename, "wb") as f:
                f.write(r.content)
            print(f"Downloaded: {filename}")

def main():
    REPO_URL = "https://github.com/YOUR_ORG/YOUR_REPO"
    PROMPT = "Add a README.md file with setup instructions"
    
    print("🚀 Creating Cloud Agent...")
    agent_id, run_id = create_agent(REPO_URL, PROMPT)
    print(f"Agent ID: {agent_id}")
    print(f"Run ID: {run_id}")
    
    print("\n⏳ Waiting for completion...")
    if wait_for_completion(agent_id, run_id):
        print("✅ Agent completed!")
        print("\n📎 Downloading artifacts...")
        download_artifacts(agent_id)
    else:
        print("❌ Agent failed!")

if __name__ == "__main__":
    main()
```

**Run the script:**

```bash
export CURSOR_USER_API_KEY="your_key"
python3 automated_workflow.py
```

**Success Criteria:**
- [ ] Script creates agent
- [ ] Waits for completion
- [ ] Downloads artifacts
- [ ] Complete workflow runs end-to-end

---

## Module Summary

| Lesson | Topic | Time |
|--------|-------|------|
| 8.1 | Creating a Cloud Agent | 10 min |
| 8.2 | Streaming Agent Responses | 10 min |
| 8.3 | Listing and Downloading Artifacts | 10 min |
| 8.4 | Creating a Webhook Endpoint | 10 min |
| 8.5 | Testing Webhooks with ngrok | 10 min |
| 8.6 | End-to-End Workflow | 10 min |

---

## Quick Reference Card

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/v1/agents` | POST | Create agent |
| `/v1/agents/{id}/runs/{runId}/stream` | GET | Stream SSE |
| `/v1/agents/{id}/artifacts` | GET | List artifacts |
| `/v1/agents/{id}/artifacts/download` | GET | Download artifact |

| Webhook Header | Purpose |
|----------------|---------|
| `X-Webhook-Signature` | HMAC-SHA256 verification |
| `X-Webhook-ID` | Unique delivery ID |
| `X-Webhook-Event` | Event type |

---

## Transition to Module 9

> *"Now that you can programmatically launch and monitor agents, let's look at the Admin and Analytics APIs for team management and usage insights."*

---

*End of Module 8*