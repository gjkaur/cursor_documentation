# Module 8: Cloud Agents API and Webhooks

## Cursor Training Program — Day 2 (Hands-On)

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise |
| **Prerequisites** | User API key (Module 7), Python 3.8+, ngrok installed, GitHub repository |
| **Module Goal** | Programmatically create, stream, and manage Cloud Agents, and set up webhook notifications |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Create a Cloud Agent programmatically using the API
- Stream agent responses in real-time using Server-Sent Events (SSE) with resume support
- List and download artifacts from a completed agent
- Create a webhook endpoint with HMAC verification
- Test webhooks locally using ngrok
- Build an end-to-end automated agent workflow

---

## Lesson 8.1: Creating a Cloud Agent Programmatically

### Concept (5 minutes)

> *"The Cloud Agents API lets you launch agents from your own code – perfect for CI/CD pipelines, scheduled tasks, and custom integrations."*

### Core Concept: Agent + Runs

| Concept | Description |
|---------|-------------|
| **Agent** | A durable entity that maintains conversation history and workspace state |
| **Run** | A single execution (one prompt/response cycle) |

### Key Endpoint: `POST /v1/agents`

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| `prompt.text` | The instruction for the agent | "Add a README.md file" |
| `repos[].url` | GitHub repository URL | "https://github.com/org/repo" |

**Optional Fields:**

| Field | Description |
|-------|-------------|
| `autoCreatePR` | Automatically create PR on completion |
| `model.id` | Specific model to use |
| `webhookUrl` | URL for completion notifications |
| `webhookSecret` | Secret for HMAC verification |

### Hands-On Exercise (10 minutes)

**Step 1:** Set up environment

```bash
# Set your API key
export CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx"

# Test it works
curl -s -u "$CURSOR_USER_API_KEY:" \
  https://api.cursor.com/v1/models | jq '.data[0].id'
```

**Step 2:** Create a simple Cloud Agent

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

**Step 3:** Capture Agent ID and Run ID

```bash
RESPONSE=$(curl -s -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {"text": "Add a README.md file with setup instructions"},
    "repos": [{"url": "https://github.com/YOUR_ORG/YOUR_REPO"}],
    "autoCreatePR": true
  }')

AGENT_ID=$(echo "$RESPONSE" | jq -r '.agent.id')
RUN_ID=$(echo "$RESPONSE" | jq -r '.run.id')

echo "Agent ID: $AGENT_ID"
echo "Run ID: $RUN_ID"
echo "Dashboard: https://cursor.com/agents/$AGENT_ID"
```

**Step 4:** Create agent with specific model

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

**Step 5:** Python function to create agent

```python
#!/usr/bin/env python3
import requests
import os
import json

API_KEY = os.environ.get("CURSOR_USER_API_KEY")
AUTH = (API_KEY, "")
BASE_URL = "https://api.cursor.com/v1"

def create_agent(prompt: str, repo_url: str, auto_create_pr: bool = False, model: str = None):
    """Create a Cloud Agent programmatically."""
    
    payload = {
        "prompt": {"text": prompt},
        "repos": [{"url": repo_url}],
        "autoCreatePR": auto_create_pr
    }
    
    if model:
        payload["model"] = {"id": model}
    
    response = requests.post(f"{BASE_URL}/agents", auth=AUTH, json=payload)
    response.raise_for_status()
    
    data = response.json()
    return {
        "agent_id": data["agent"]["id"],
        "run_id": data["run"]["id"],
        "status": data["run"]["status"],
        "dashboard_url": f"https://cursor.com/agents/{data['agent']['id']}"
    }

# Usage
result = create_agent(
    prompt="Add comprehensive docstrings to all functions in src/",
    repo_url="https://github.com/YOUR_ORG/YOUR_REPO",
    auto_create_pr=True,
    model="claude-4.6-sonnet"
)

print(f"✅ Agent created: {result['agent_id']}")
print(f"📊 Status: {result['status']}")
print(f"🔗 {result['dashboard_url']}")
```

**Step 6:** Check agent status

```python
def get_agent_status(agent_id: str):
    """Get current status of an agent."""
    response = requests.get(f"{BASE_URL}/agents/{agent_id}", auth=AUTH)
    response.raise_for_status()
    return response.json()

# Check status of your agent
status = get_agent_status(result['agent_id'])
print(f"Status: {status.get('status')}")
print(f"Created: {status.get('createdAt')}")
```

**Success Criteria:**
- [ ] Agent created successfully
- [ ] Agent ID and Run ID captured
- [ ] Agent appears in dashboard
- [ ] Python function works

---

## Lesson 8.2: Streaming Agent Responses (SSE)

### Concept (5 minutes)

> *"Server-Sent Events (SSE) let you watch the agent work in real-time – seeing its thoughts, tool calls, and output as they happen, with resume support for interrupted connections."*

### Event Types

| Event | When It Happens | Data Example |
|-------|-----------------|--------------|
| `status` | Run status changes | `{"runId":"...","status":"RUNNING"}` |
| `assistant` | Agent speaks | `{"text":"I'll read the file..."}` |
| `thinking` | Agent is reasoning | `{"text":"Let me consider..."}` |
| `tool_call` | Agent uses a tool | `{"callId":"...","name":"read_file","status":"started"}` |
| `result` | Run completes | `{"runId":"...","status":"FINISHED"}` |
| `error` | Something went wrong | `{"code":"...","message":"..."}` |
| `done` | Stream ends | `{}` |

### Resume Support

SSE streams support the `Last-Event-ID` header – if your connection drops, you can resume from the last received event.

### Hands-On Exercise (10 minutes)

**Step 1:** Create an agent and stream with curl

```bash
# Create agent
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

# Stream the response
curl -N -u "$CURSOR_USER_API_KEY:" \
  -H "Accept: text/event-stream" \
  "https://api.cursor.com/v1/agents/$AGENT_ID/runs/$RUN_ID/stream"
```

**Step 2:** Parse SSE events in Python

```python
#!/usr/bin/env python3
import requests
import json
import os
import time

API_KEY = os.environ.get("CURSOR_USER_API_KEY")
AUTH = (API_KEY, "")
BASE_URL = "https://api.cursor.com/v1"

def stream_agent_response(agent_id: str, run_id: str, on_event=None):
    """Stream agent response with SSE."""
    
    url = f"{BASE_URL}/agents/{agent_id}/runs/{run_id}/stream"
    
    response = requests.get(url, auth=AUTH, stream=True)
    response.raise_for_status()
    
    current_event = None
    
    for line in response.iter_lines():
        if not line:
            continue
        
        line = line.decode('utf-8')
        
        if line.startswith('event:'):
            current_event = line[6:].strip()
        elif line.startswith('data:'):
            data_str = line[5:].strip()
            if data_str:
                data = json.loads(data_str)
                if on_event:
                    on_event(current_event, data)
                
                # Handle specific events
                if current_event == 'assistant':
                    print(data.get('text', ''), end='', flush=True)
                elif current_event == 'tool_call':
                    tool_name = data.get('name', 'unknown')
                    status = data.get('status', '')
                    print(f"\n🔧 Tool: {tool_name} ({status})")
                elif current_event == 'result':
                    print(f"\n✅ Run {data.get('status')}")
                elif current_event == 'error':
                    print(f"\n❌ Error: {data.get('message')}")

# Use it
def print_event(event_type, data):
    print(f"[{event_type}] {json.dumps(data)[:100]}")

# Create agent first
response = requests.post(
    f"{BASE_URL}/agents",
    auth=AUTH,
    json={
        "prompt": {"text": "List all Python files in the repository"},
        "repos": [{"url": "https://github.com/YOUR_ORG/YOUR_REPO"}]
    }
)
data = response.json()
agent_id = data['agent']['id']
run_id = data['run']['id']

print(f"Streaming agent {agent_id}...")
stream_agent_response(agent_id, run_id, on_event=print_event)
```

**Step 3:** Implement resume support

```python
class ResumableSSEClient:
    """SSE client with resume support using Last-Event-ID."""
    
    def __init__(self, api_key: str):
        self.auth = (api_key, "")
        self.base_url = "https://api.cursor.com/v1"
        self.last_event_id = None
    
    def stream(self, agent_id: str, run_id: str, on_event=None):
        """Stream with resume capability."""
        
        url = f"{self.base_url}/agents/{agent_id}/runs/{run_id}/stream"
        headers = {}
        
        if self.last_event_id:
            headers['Last-Event-ID'] = self.last_event_id
        
        response = requests.get(url, auth=self.auth, headers=headers, stream=True)
        response.raise_for_status()
        
        current_event = None
        
        for line in response.iter_lines():
            if not line:
                continue
            
            line = line.decode('utf-8')
            
            if line.startswith('event:'):
                current_event = line[6:].strip()
            elif line.startswith('id:'):
                self.last_event_id = line[3:].strip()
            elif line.startswith('data:'):
                data_str = line[5:].strip()
                if data_str:
                    data = json.loads(data_str)
                    if on_event:
                        on_event(current_event, data)
    
    def resume_from_last(self, agent_id: str, run_id: str):
        """Resume stream from last received event."""
        if not self.last_event_id:
            print("No last event ID to resume from")
            return
        
        print(f"Resuming from event: {self.last_event_id}")
        self.stream(agent_id, run_id)

# Usage
client = ResumableSSEClient(API_KEY)

# First stream (may be interrupted)
try:
    client.stream(agent_id, run_id)
except KeyboardInterrupt:
    print("\nStream interrupted. Resuming...")
    client.resume_from_last(agent_id, run_id)
```

**Step 4:** Save stream to file for later review

```python
def stream_to_file(agent_id: str, run_id: str, output_file: str):
    """Save SSE stream to file."""
    
    url = f"{BASE_URL}/agents/{agent_id}/runs/{run_id}/stream"
    
    with open(output_file, 'w') as f:
        response = requests.get(url, auth=AUTH, stream=True)
        
        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                f.write(line + '\n')
                print(line)  # Also print to console

# Usage
stream_to_file(agent_id, run_id, "agent_stream.log")
```

**Success Criteria:**
- [ ] Stream connected successfully
- [ ] Received status and assistant events
- [ ] Python streaming client works
- [ ] Resume support implemented

---

## Lesson 8.3: Listing and Downloading Artifacts

### Concept (5 minutes)

> *"Artifacts are files produced by the agent – screenshots, logs, generated code, test results. You can list and download them programmatically to integrate into CI pipelines."*

### Key Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/v1/agents/{id}/artifacts` | GET | List all artifacts |
| `/v1/agents/{id}/artifacts/download` | GET | Get presigned URL for download |

**Important:** Download URLs expire after **15 minutes**.

### Hands-On Exercise (10 minutes)

**Step 1:** Wait for agent completion and list artifacts

```python
def wait_for_completion(agent_id: str, timeout: int = 300, poll_interval: int = 5):
    """Wait for agent to complete."""
    
    start = time.time()
    
    while time.time() - start < timeout:
        response = requests.get(f"{BASE_URL}/agents/{agent_id}", auth=AUTH)
        data = response.json()
        status = data.get('status')
        
        print(f"Status: {status}")
        
        if status == 'FINISHED':
            return True
        elif status == 'ERROR':
            return False
        
        time.sleep(poll_interval)
    
    return False

def list_artifacts(agent_id: str):
    """List all artifacts for a completed agent."""
    
    response = requests.get(f"{BASE_URL}/agents/{agent_id}/artifacts", auth=AUTH)
    response.raise_for_status()
    
    artifacts = response.json().get('items', [])
    
    print(f"\n📎 Artifacts ({len(artifacts)}):")
    for artifact in artifacts:
        size_kb = artifact.get('size', 0) / 1024
        print(f"  📄 {artifact['path']} ({size_kb:.1f} KB)")
    
    return artifacts

# Usage
agent_id = "your_agent_id_here"

if wait_for_completion(agent_id):
    artifacts = list_artifacts(agent_id)
```

**Step 2:** Download a specific artifact

```python
def download_artifact(agent_id: str, artifact_path: str, output_path: str = None):
    """Download a specific artifact."""
    
    # Get presigned URL
    response = requests.get(
        f"{BASE_URL}/agents/{agent_id}/artifacts/download",
        auth=AUTH,
        params={"path": artifact_path}
    )
    response.raise_for_status()
    
    download_url = response.json().get('url')
    if not download_url:
        print(f"No download URL for {artifact_path}")
        return False
    
    # Download file
    if not output_path:
        output_path = os.path.basename(artifact_path)
    
    file_response = requests.get(download_url)
    file_response.raise_for_status()
    
    with open(output_path, 'wb') as f:
        f.write(file_response.content)
    
    print(f"✅ Downloaded: {output_path}")
    return True

# Download a specific artifact
download_artifact(agent_id, "artifacts/report.md", "report.md")
```

**Step 3:** Download all artifacts

```python
def download_all_artifacts(agent_id: str, output_dir: str = "artifacts"):
    """Download all artifacts from an agent."""
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # List artifacts
    response = requests.get(f"{BASE_URL}/agents/{agent_id}/artifacts", auth=AUTH)
    artifacts = response.json().get('items', [])
    
    for artifact in artifacts:
        path = artifact['path']
        
        # Get download URL
        url_response = requests.get(
            f"{BASE_URL}/agents/{agent_id}/artifacts/download",
            auth=AUTH,
            params={"path": path}
        )
        download_url = url_response.json().get('url')
        
        if download_url:
            # Create subdirectories if needed
            local_path = os.path.join(output_dir, path)
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            
            # Download
            file_response = requests.get(download_url)
            with open(local_path, 'wb') as f:
                f.write(file_response.content)
            
            print(f"✅ Downloaded: {local_path}")
        else:
            print(f"⚠️ No URL for: {path}")
    
    return len(artifacts)

# Download all
count = download_all_artifacts(agent_id, "agent_outputs")
print(f"Downloaded {count} artifacts to ./agent_outputs/")
```

**Step 4:** Integrate artifacts into CI pipeline

```python
# Example: Use in GitHub Actions or similar
def process_test_results(agent_id: str):
    """Download test results and exit with appropriate code."""
    
    # Wait for completion
    if not wait_for_completion(agent_id, timeout=600):
        print("❌ Agent failed")
        sys.exit(1)
    
    # Download test results
    download_artifact(agent_id, "artifacts/junit.xml", "test_results.xml")
    
    # Parse and return exit code
    import xml.etree.ElementTree as ET
    
    try:
        tree = ET.parse("test_results.xml")
        root = tree.getroot()
        
        failures = int(root.attrib.get('failures', 0))
        errors = int(root.attrib.get('errors', 0))
        
        if failures > 0 or errors > 0:
            print(f"❌ Tests failed: {failures} failures, {errors} errors")
            sys.exit(1)
        else:
            print("✅ All tests passed")
            sys.exit(0)
    except FileNotFoundError:
        print("No test results found")
        sys.exit(0)

# Usage in CI
# process_test_results(agent_id)
```

**Success Criteria:**
- [ ] Listed artifacts from completed agent
- [ ] Downloaded single artifact
- [ ] Downloaded all artifacts
- [ ] Integrated artifacts into CI workflow

---

## Lesson 8.4: Creating a Webhook Endpoint

### Concept (5 minutes)

> *"Webhooks let Cursor notify your server when an agent completes – no polling required. HMAC verification ensures the request is genuinely from Cursor."*

### Webhook Headers

| Header | Description |
|--------|-------------|
| `X-Webhook-Signature` | HMAC-SHA256 signature for verification |
| `X-Webhook-ID` | Unique delivery ID |
| `X-Webhook-Event` | Event type (`statusChange`) |

### Webhook Payload

```json
{
  "event": "statusChange",
  "timestamp": "2025-01-15T10:30:00Z",
  "id": "agent_abc123",
  "status": "FINISHED",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents/agent_abc123",
    "prUrl": "https://github.com/.../pull/123"
  },
  "summary": "Added README.md and fixed tests"
}
```

### Hands-On Exercise (10 minutes)

**Step 1:** Create webhook server with HMAC verification

```python
#!/usr/bin/env python3
# webhook_server.py

from flask import Flask, request, jsonify
import hmac
import hashlib
import json
import os

app = Flask(__name__)

# Set your webhook secret (same as when creating agent)
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "your-secret-here")

def verify_signature(raw_body: bytes, signature_header: str) -> bool:
    """Verify HMAC-SHA256 signature."""
    
    if not signature_header or not signature_header.startswith('sha256='):
        return False
    
    # Extract the actual signature
    received_signature = signature_header[7:]
    
    # Compute expected signature
    expected_signature = hmac.new(
        WEBHOOK_SECRET.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()
    
    # Use constant-time comparison to prevent timing attacks
    return hmac.compare_digest(expected_signature, received_signature)

@app.route('/webhook/cursor', methods=['POST'])
def cursor_webhook():
    """Handle Cursor webhook notifications."""
    
    raw_body = request.get_data()
    signature = request.headers.get('X-Webhook-Signature', '')
    webhook_id = request.headers.get('X-Webhook-ID', '')
    event_type = request.headers.get('X-Webhook-Event', '')
    
    # Verify signature
    if not verify_signature(raw_body, signature):
        print(f"❌ Invalid signature for webhook {webhook_id}")
        return jsonify({"error": "Invalid signature"}), 401
    
    # Parse payload
    payload = request.get_json()
    agent_id = payload.get('id')
    status = payload.get('status')
    pr_url = payload.get('target', {}).get('prUrl')
    summary = payload.get('summary', '')
    
    print(f"\n📨 Webhook received:")
    print(f"   ID: {webhook_id}")
    print(f"   Event: {event_type}")
    print(f"   Agent: {agent_id}")
    print(f"   Status: {status}")
    
    if pr_url:
        print(f"   PR: {pr_url}")
    if summary:
        print(f"   Summary: {summary[:100]}...")
    
    # Process based on status
    if status == 'FINISHED':
        # Agent completed successfully
        # Could trigger next steps, send notifications, etc.
        print(f"✅ Agent {agent_id} completed!")
        
        # Example: Send to Slack (if configured)
        # send_slack_notification(f"Agent {agent_id} finished: {summary}")
        
    elif status == 'ERROR':
        print(f"❌ Agent {agent_id} failed!")
        # Could alert on-call, create ticket, etc.
    
    return jsonify({"status": "received"}), 200

@app.route('/webhook/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "timestamp": request.args.get('_t', '')}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
```

**Step 2:** Run the webhook server

```bash
# Install Flask if needed
pip install flask

# Set webhook secret
export WEBHOOK_SECRET="your-secret-here"

# Run server
python webhook_server.py
```

**Step 3:** Create agent with webhook configuration

```bash
curl -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {"text": "Add a CONTRIBUTING.md file"},
    "repos": [{"url": "https://github.com/YOUR_ORG/YOUR_REPO"}],
    "webhookUrl": "https://your-domain.com/webhook/cursor",
    "webhookSecret": "your-secret-here",
    "autoCreatePR": true
  }' | jq '.'
```

**Success Criteria:**
- [ ] Webhook server running
- [ ] Signature verification implemented
- [ ] Payload parsing working
- [ ] Agent configured with webhook

---

## Lesson 8.5: Testing Webhooks Locally with ngrok

### Concept (5 minutes)

> *"ngrok exposes your local webhook server to the internet so Cursor can send webhooks to your development machine during testing."*

### What is ngrok?

ngrok creates a secure tunnel from a public URL to your local server. Perfect for:
- Testing webhooks without deploying
- Debugging locally
- Demo-ing to stakeholders

### Hands-On Exercise (8 minutes)

**Step 1:** Install and start ngrok

```bash
# Download from https://ngrok.com/download
# Or use package manager
brew install ngrok  # macOS
# or
# choco install ngrok  # Windows
# or download directly

# Start tunnel to port 5000 (your Flask server)
ngrok http 5000
```

**Step 2:** Copy the HTTPS URL

```
ngrok by @inconshreveable

Session Status                online
Account                       Your Name (Plan: Free)
Version                       3.x
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://abc123.ngrok.io -> http://localhost:5000
```

**Step 3:** Create agent with ngrok URL

```bash
WEBHOOK_URL="https://abc123.ngrok.io/webhook/cursor"

curl -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {"text": "Run a quick test: create a hello.txt file"},
    "repos": [{"url": "https://github.com/YOUR_ORG/YOUR_REPO"}],
    "webhookUrl": "'"$WEBHOOK_URL"'",
    "webhookSecret": "your-secret-here"
  }' | jq '.agent.id'
```

**Step 4:** Inspect webhook requests

```bash
# Open ngrok web interface
open http://127.0.0.1:4040

# Or use curl to see last request
curl http://127.0.0.1:4040/api/tunnels
```

**Step 5:** Replay failed webhooks (ngrok premium feature)

```bash
# In ngrok web interface, you can:
# - Inspect each request/response
# - Replay failed requests
# - See raw body and headers
```

**Success Criteria:**
- [ ] ngrok tunnel established
- [ ] Webhook received by local server
- [ ] Signature verified
- [ ] Payload inspected in ngrok interface

---

## Lesson 8.6: End-to-End Automated Agent Workflow

### Concept (5 minutes)

> *"Combine everything into a complete automation script: create agent, wait for completion, download artifacts, and process results."*

### The Capstone Integration Exercise

This script ties together:
- Agent creation
- Status polling (or webhook)
- Artifact download
- Result processing
- CI/CD integration

### Hands-On Exercise (12 minutes)

**Create `automated_workflow.py`:**

```python
#!/usr/bin/env python3
"""
End-to-end automated agent workflow with webhook support
"""

import requests
import time
import os
import json
import sys
import signal
import threading
from flask import Flask, request, jsonify
from typing import Optional

# ============ Configuration ============
API_KEY = os.environ.get("CURSOR_USER_API_KEY")
if not API_KEY:
    print("❌ Set CURSOR_USER_API_KEY environment variable")
    sys.exit(1)

BASE_URL = "https://api.cursor.com/v1"
AUTH = (API_KEY, "")

# Webhook configuration
WEBHOOK_PORT = 5000
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "workflow-secret-2024")

# Global flag for webhook completion
completion_event = threading.Event()
completion_result = {}

# ============ Agent Management ============
def create_agent(repo_url: str, prompt: str, webhook_url: str = None, auto_create_pr: bool = False):
    """Create a Cloud Agent."""
    
    payload = {
        "prompt": {"text": prompt},
        "repos": [{"url": repo_url}],
        "autoCreatePR": auto_create_pr
    }
    
    if webhook_url:
        payload["webhookUrl"] = webhook_url
        payload["webhookSecret"] = WEBHOOK_SECRET
    
    response = requests.post(f"{BASE_URL}/agents", auth=AUTH, json=payload)
    response.raise_for_status()
    
    data = response.json()
    return data["agent"]["id"], data["run"]["id"]

def get_agent_status(agent_id: str):
    """Get current agent status."""
    response = requests.get(f"{BASE_URL}/agents/{agent_id}", auth=AUTH)
    response.raise_for_status()
    return response.json()

def wait_for_completion_polling(agent_id: str, timeout: int = 600, poll_interval: int = 10):
    """Wait for agent completion using polling."""
    
    start = time.time()
    
    while time.time() - start < timeout:
        status = get_agent_status(agent_id)
        current_status = status.get('status')
        
        print(f"  Status: {current_status}")
        
        if current_status == 'FINISHED':
            return True, status
        elif current_status == 'ERROR':
            return False, status
        
        time.sleep(poll_interval)
    
    return False, {"status": "TIMEOUT"}

# ============ Webhook Server ============
app = Flask(__name__)

def verify_signature(raw_body: bytes, signature_header: str) -> bool:
    """Verify HMAC-SHA256 signature."""
    if not signature_header or not signature_header.startswith('sha256='):
        return False
    
    received = signature_header[7:]
    expected = hmac.new(
        WEBHOOK_SECRET.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(expected, received)

@app.route('/webhook/cursor', methods=['POST'])
def webhook_handler():
    """Handle completion webhook."""
    global completion_result
    
    raw_body = request.get_data()
    signature = request.headers.get('X-Webhook-Signature', '')
    
    if not verify_signature(raw_body, signature):
        return jsonify({"error": "Invalid signature"}), 401
    
    payload = request.get_json()
    completion_result = payload
    completion_event.set()
    
    print(f"\n✅ Webhook received: Agent {payload.get('id')} completed")
    
    return jsonify({"status": "ok"}), 200

@app.route('/webhook/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

def start_webhook_server():
    """Start the webhook server in a background thread."""
    
    def run_server():
        app.run(port=WEBHOOK_PORT, debug=False, use_reloader=False)
    
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    # Wait for server to start
    time.sleep(1)
    print(f"📡 Webhook server running on port {WEBHOOK_PORT}")

def wait_for_completion_webhook(agent_id: str, timeout: int = 600):
    """Wait for agent completion via webhook."""
    
    print(f"  Waiting for webhook notification...")
    
    if completion_event.wait(timeout):
        return True, completion_result
    else:
        return False, {"status": "TIMEOUT"}

# ============ Artifact Management ============
def download_artifacts(agent_id: str, output_dir: str = "artifacts"):
    """Download all artifacts from an agent."""
    
    # List artifacts
    resp = requests.get(f"{BASE_URL}/agents/{agent_id}/artifacts", auth=AUTH)
    artifacts = resp.json().get("items", [])
    
    if not artifacts:
        print("  No artifacts found")
        return 0
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    for artifact in artifacts:
        path = artifact["path"]
        
        # Get download URL
        url_resp = requests.get(
            f"{BASE_URL}/agents/{agent_id}/artifacts/download",
            auth=AUTH,
            params={"path": path}
        )
        download_url = url_resp.json().get("url")
        
        if download_url:
            local_path = os.path.join(output_dir, os.path.basename(path))
            r = requests.get(download_url)
            with open(local_path, "wb") as f:
                f.write(r.content)
            print(f"  ✅ Downloaded: {local_path}")
    
    return len(artifacts)

# ============ Main Workflow ============
def run_workflow(
    repo_url: str,
    prompt: str,
    auto_create_pr: bool = False,
    use_webhook: bool = True,
    output_dir: str = "agent_outputs"
):
    """Run complete automated agent workflow."""
    
    print("=" * 60)
    print("🚀 CLOUD AGENT AUTOMATED WORKFLOW")
    print("=" * 60)
    
    # Start webhook server if needed
    webhook_url = None
    if use_webhook:
        start_webhook_server()
        # Get ngrok URL or use localhost for demo
        webhook_url = f"http://localhost:{WEBHOOK_PORT}/webhook/cursor"
        print(f"📡 Webhook URL: {webhook_url}")
        print("   (For external access, use ngrok: ngrok http 5000)")
    
    # Step 1: Create agent
    print(f"\n📝 Creating agent...")
    agent_id, run_id = create_agent(repo_url, prompt, webhook_url, auto_create_pr)
    print(f"   Agent ID: {agent_id}")
    print(f"   Run ID: {run_id}")
    print(f"   Dashboard: https://cursor.com/agents/{agent_id}")
    
    # Step 2: Wait for completion
    print(f"\n⏳ Waiting for completion...")
    
    if use_webhook and webhook_url:
        success, result = wait_for_completion_webhook(agent_id)
    else:
        success, result = wait_for_completion_polling(agent_id)
    
    if not success:
        print(f"❌ Agent failed or timed out")
        return False
    
    status = result.get('status')
    pr_url = result.get('target', {}).get('prUrl')
    summary = result.get('summary', '')
    
    print(f"\n✅ Agent completed with status: {status}")
    if pr_url:
        print(f"   PR created: {pr_url}")
    if summary:
        print(f"   Summary: {summary[:200]}...")
    
    # Step 3: Download artifacts
    print(f"\n📎 Downloading artifacts...")
    artifact_count = download_artifacts(agent_id, output_dir)
    print(f"   Downloaded {artifact_count} artifacts to {output_dir}/")
    
    print("\n" + "=" * 60)
    print("✅ WORKFLOW COMPLETE")
    print("=" * 60)
    
    return True

# ============ Main Entry Point ============
if __name__ == "__main__":
    # Parse command line arguments
    import argparse
    
    parser = argparse.ArgumentParser(description="Run automated Cursor agent workflow")
    parser.add_argument("--repo", required=True, help="GitHub repository URL")
    parser.add_argument("--prompt", required=True, help="Agent prompt")
    parser.add_argument("--pr", action="store_true", help="Auto-create PR")
    parser.add_argument("--no-webhook", action="store_true", help="Use polling instead of webhook")
    parser.add_argument("--output", default="agent_outputs", help="Output directory")
    
    args = parser.parse_args()
    
    success = run_workflow(
        repo_url=args.repo,
        prompt=args.prompt,
        auto_create_pr=args.pr,
        use_webhook=not args.no_webhook,
        output_dir=args.output
    )
    
    sys.exit(0 if success else 1)
```

**Run the workflow:**

```bash
# Set your API key
export CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx"

# Run with webhook (local server)
python automated_workflow.py \
  --repo "https://github.com/YOUR_ORG/YOUR_REPO" \
  --prompt "Add a comprehensive README.md with setup, usage, and API documentation" \
  --output "./outputs"

# Or with polling only
python automated_workflow.py \
  --repo "https://github.com/YOUR_ORG/YOUR_REPO" \
  --prompt "Run all tests and report failures" \
  --no-webhook
```

**Success Criteria:**
- [ ] Script creates agent
- [ ] Waits for completion (webhook or polling)
- [ ] Downloads artifacts
- [ ] Complete workflow runs end-to-end

---

## Module Summary

| Lesson | Topic | Time | Key Skill |
|--------|-------|------|-----------|
| 8.1 | Creating a Cloud Agent | 10 min | Programmatic agent launch |
| 8.2 | Streaming Agent Responses | 10 min | SSE with resume support |
| 8.3 | Listing and Downloading Artifacts | 10 min | CI pipeline integration |
| 8.4 | Creating a Webhook Endpoint | 10 min | HMAC verification |
| 8.5 | Testing Webhooks with ngrok | 8 min | Local tunnel debugging |
| 8.6 | End-to-End Workflow | 12 min | Complete automation |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│              CLOUD AGENTS API QUICK REFERENCE                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ENDPOINTS:                                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ POST   /v1/agents                    Create agent    │   │
│  │ GET    /v1/agents/{id}               Get status     │   │
│  │ GET    /v1/agents/{id}/runs/{id}/stream  SSE stream │   │
│  │ GET    /v1/agents/{id}/artifacts     List artifacts │   │
│  │ GET    /v1/agents/{id}/artifacts/download  Download │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  WEBHOOK HEADERS:                                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ X-Webhook-Signature   HMAC-SHA256 signature         │   │
│  │ X-Webhook-ID          Unique delivery ID            │   │
│  │ X-Webhook-Event       Event type (statusChange)     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  SSE EVENT TYPES:                                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ status        Run status changed                    │   │
│  │ assistant     Agent speaking                        │   │
│  │ thinking      Agent reasoning                       │   │
│  │ tool_call     Tool invocation                       │   │
│  │ result        Run complete                          │   │
│  │ error         Something went wrong                  │   │
│  │ done          Stream ends                           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  NGORK TUNNEL:                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ ngrok http 5000          Expose local webhook       │   │
│  │ http://127.0.0.1:4040    Inspect requests           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Transition to Module 9

> *"Now that you can programmatically launch and monitor agents, Module 9 will cover Admin and Analytics APIs for team management and usage insights."*

---

*End of Module 8*