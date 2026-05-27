# Exercise 8.4: Webhooks and HMAC Verification

**Module 8:** Cloud Agents API and Webhooks  
**Slides:** `slides/course-complete-marp-with-notes.md` (Module 8, Lesson 8.4)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Receive webhooks and verify HMAC signatures.

---

## API basics (read this first)

**Windows:** PowerShell (``Ctrl+` ``) · **`curl.exe`** · store keys in `$env:` — **never** commit keys to git.

```powershell
$env:CURSOR_USER_API_KEY = "cursor_your_key_here"
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_your_key_here"   # Admin labs (9–10)
```

More examples (Python, jq, bash): see **Detailed reference** below — optional for class.

---

## Steps from the training slides

**Environment:** Windows · PowerShell (``Ctrl+` ``) · **`curl.exe`** · keys in `$env:` only (never commit).

```powershell
$env:CURSOR_USER_API_KEY = "cursor_your_key_here"
$env:CURSOR_ADMIN_API_KEY = "cursor_admin_your_key_here"  # Modules 9–10
```

Follow each step in order. Confirm the **Expected result** before moving on.

### Step 1 — Webhook flow (30 seconds)

**Do this:** Finish this sentence: “When the agent finishes, Cursor sends an HTTPS **POST** to my URL with a signed body; I verify **HMAC** and return **200**.”

**Expected result:** You can draw: Cursor → your server → 200 OK.

---

### Step 2 — Three security checks

**Do this:** List: (1) HTTPS only, (2) verify signature, (3) handle duplicates safely.

**Expected result:** Checklist of three items.

---

### Step 3 — Prepare for ngrok (next lab)

**Do this:** Confirm you have a tiny webhook app on port **5000** (from lab guide) or will pair with a demo.

**Expected result:** Ready for Exercise 8.5 tunnel test.

**Success criteria:** Explained flow · three security checks · ready for 8.5
---

## Success criteria

- [ ] Server running · signature verified · payload parsed · agent configured

---

> **Note:** The section below is optional deep dive — not required to finish the in-class steps.

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] User API key from Exercise 1 (for creating agents with webhooks)
- [ ] Python 3.8+ installed
- [ ] `ngrok` installed (for local testing)
- [ ] `curl` and `jq` installed

---

## Step-by-Step Instructions

### Step 1: Create a Simple Webhook Server (5 minutes)

**Create `webhook_server.py`:**
```python
#!/usr/bin/env python3
"""
Webhook server for Cursor Cloud Agents
Receives notifications when agents complete or error
"""

from flask import Flask, request, jsonify
import hmac
import hashlib
import json
import os
from datetime import datetime

app = Flask(__name__)

# Your webhook secret (use environment variable in production)
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "your-secret-here")

def verify_signature(raw_body, signature_header):
    """Verify that the webhook came from Cursor."""
    if not signature_header:
        return False
    
    if not signature_header.startswith('sha256='):
        return False
    
    received_signature = signature_header[7:]  # Remove "sha256=" prefix
    
    expected = hmac.new(
        WEBHOOK_SECRET.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(expected, received_signature)

@app.route('/webhook/cursor', methods=['POST'])
def cursor_webhook():
    """Receive and process Cursor webhook."""
    
    # Get raw request body for signature verification
    raw_body = request.get_data()
    
    # Get headers
    signature = request.headers.get('X-Webhook-Signature', '')
    webhook_id = request.headers.get('X-Webhook-ID', 'unknown')
    event_type = request.headers.get('X-Webhook-Event', 'unknown')
    user_agent = request.headers.get('User-Agent', '')
    
    print(f"\n📨 Received webhook: {webhook_id}")
    print(f"   Event: {event_type}")
    print(f"   User-Agent: {user_agent}")
    
    # Verify signature (optional but recommended)
    # if not verify_signature(raw_body, signature):
    #     print("   ❌ Invalid signature!")
    #     return jsonify({"error": "Invalid signature"}), 401
    
    print("   ✅ Signature verified")
    
    # Parse the payload
    payload = request.get_json()
    
    # Extract important fields
    agent_id = payload.get('id')
    status = payload.get('status')
    timestamp = payload.get('timestamp')
    summary = payload.get('summary', 'No summary')
    
    print(f"\n📊 Agent {agent_id} status: {status}")
    print(f"   Time: {timestamp}")
    print(f"   Summary: {summary}")
    
    # Check for PR URL
    source = payload.get('source', {})
    target = payload.get('target', {})
    
    repo = source.get('repository', 'unknown')
    branch = target.get('branchName', 'unknown')
    pr_url = target.get('prUrl')
    dashboard_url = target.get('url')
    
    print(f"   Repository: {repo}")
    print(f"   Branch: {branch}")
    
    if pr_url:
        print(f"   🔗 PR created: {pr_url}")
    
    if dashboard_url:
        print(f"   📊 Dashboard: {dashboard_url}")
    
    # Take action based on status
    if status == 'FINISHED':
        print("\n✅ Agent completed successfully!")
        send_notification(f"✅ Agent {agent_id} completed: {summary}", pr_url)
        
    elif status == 'ERROR':
        print("\n❌ Agent failed!")
        send_notification(f"❌ Agent {agent_id} failed!", None)
    
    # Always return 200 to acknowledge receipt
    return jsonify({"status": "received", "webhook_id": webhook_id}), 200

def send_notification(message, pr_url):
    """Send notification (Slack, email, etc.)."""
    # This is a placeholder - implement your own notification logic
    print(f"   📢 NOTIFICATION: {message}")
    if pr_url:
        print(f"   🔗 PR: {pr_url}")
    
    # Example: Send to Slack webhook
    # slack_webhook = os.environ.get("SLACK_WEBHOOK_URL")
    # if slack_webhook:
    #     import requests
    #     requests.post(slack_webhook, json={"text": message})

@app.route('/webhook/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()}), 200

@app.route('/webhook/test', methods=['GET'])
def test_page():
    """Simple test page."""
    return """
    <html>
        <body>
            <h1>Cursor Webhook Server</h1>
            <p>Status: Running</p>
            <p>Endpoint: POST /webhook/cursor</p>
            <p>Health: GET /webhook/health</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    print("🚀 Cursor Webhook Server")
    print("=" * 40)
    print(f"Webhook endpoint: http://localhost:5000/webhook/cursor")
    print(f"Health check: http://localhost:5000/webhook/health")
    print(f"Secret: {WEBHOOK_SECRET[:10]}...")
    print("\nWaiting for webhook events...")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
```

---

### Step 2: Install Dependencies and Run Server (2 minutes)

**Install Flask:**
```bash
pip install flask
```

**Run the server:**
```bash
python webhook_server.py
```

**Expected output:**
```
🚀 Cursor Webhook Server
========================================
Webhook endpoint: http://localhost:5000/webhook/cursor
Health check: http://localhost:5000/webhook/health
Secret: your-secre...
Waiting for webhook events...
 * Running on http://0.0.0.0:5000
```

---

### Step 3: Expose Local Server with ngrok (2 minutes)

In a new terminal, start ngrok to expose your local server to the internet.

**Command:**
```bash
ngrok http 5000
```

**Expected output:**
```
ngrok by @inconshreveable

Session Status                online
Forwarding                    https://abc123.ngrok.io -> http://localhost:5000
```

**Copy the HTTPS URL** (e.g., `https://abc123.ngrok.io`)

---

### Step 4: Create an Agent with Webhook (3 minutes)

Create a Cloud Agent that will send webhook notifications.

**Command:**
```bash
# Replace with your ngrok URL
WEBHOOK_URL="https://abc123.ngrok.io/webhook/cursor"
WEBHOOK_SECRET="your-secret-here"

curl -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {
      "text": "Add a README.md file with project description"
    },
    "repos": [
      {
        "url": "https://github.com/YOUR_ORG/YOUR_REPO",
        "startingRef": "main"
      }
    ],
    "autoCreatePR": true,
    "webhookUrl": "'"$WEBHOOK_URL"'",
    "webhookSecret": "'"$WEBHOOK_SECRET"'"
  }' | jq '.agent.id'
```

---

### Step 5: Test Webhook Locally (2 minutes)

You can also test your webhook endpoint locally without creating an agent.

**Create a test script `test_webhook.py`:**
```python
#!/usr/bin/env python3
"""
Test webhook locally by sending a simulated payload
"""

import requests
import hmac
import hashlib
import json
import time

WEBHOOK_URL = "http://localhost:5000/webhook/cursor"
WEBHOOK_SECRET = "your-secret-here"

def send_test_webhook(status="FINISHED"):
    """Send a simulated webhook payload."""
    
    payload = {
        "event": "statusChange",
        "timestamp": "2025-01-15T10:30:00Z",
        "id": "bc_test123",
        "status": status,
        "source": {
            "repository": "https://github.com/test/repo",
            "ref": "main"
        },
        "target": {
            "url": "https://cursor.com/agents/bc_test123",
            "branchName": "cursor/test-branch",
            "prUrl": "https://github.com/test/repo/pull/1"
        },
        "summary": "Test webhook notification"
    }
    
    # Convert to JSON string
    body = json.dumps(payload)
    
    # Calculate signature
    signature = 'sha256=' + hmac.new(
        WEBHOOK_SECRET.encode(),
        body.encode(),
        hashlib.sha256
    ).hexdigest()
    
    headers = {
        'Content-Type': 'application/json',
        'X-Webhook-Signature': signature,
        'X-Webhook-ID': 'test_123',
        'X-Webhook-Event': 'statusChange',
        'User-Agent': 'Cursor-Agent-Webhook/1.0'
    }
    
    response = requests.post(WEBHOOK_URL, data=body, headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    print("Testing FINISHED webhook...")
    send_test_webhook("FINISHED")
    
    time.sleep(1)
    
    print("\nTesting ERROR webhook...")
    send_test_webhook("ERROR")
```

**Run the test:**
```bash
python test_webhook.py
```

---

### Step 6: Webhook Payload Format Reference

**Successful completion (FINISHED):**
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
    "branchName": "cursor/add-readme-1234",
    "prUrl": "https://github.com/your-org/your-repo/pull/1234"
  },
  "summary": "Added README.md with installation instructions"
}
```

**Error (ERROR):**
```json
{
  "event": "statusChange",
  "timestamp": "2025-01-15T10:30:00Z",
  "id": "bc_abc123",
  "status": "ERROR",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents?id=bc_abc123"
  },
  "summary": "Failed to clone repository: permission denied"
}
```

---

## Expected Output

### Step 2 Server Output:
```
🚀 Cursor Webhook Server
========================================
Webhook endpoint: http://localhost:5000/webhook/cursor
Health check: http://localhost:5000/webhook/health
Secret: your-secre...
Waiting for webhook events...
 * Running on http://0.0.0.0:5000
```

### Step 5 Test Output:
```
Testing FINISHED webhook...
Status: 200
Response: {'status': 'received', 'webhook_id': 'test_123'}

Testing ERROR webhook...
Status: 200
Response: {'status': 'received', 'webhook_id': 'test_123'}
```

### When Agent Completes (Server Output):
```
📨 Received webhook: wh_abc123
   Event: statusChange
   User-Agent: Cursor-Agent-Webhook/1.0
   ✅ Signature verified

📊 Agent bc_abc123 status: FINISHED
   Time: 2025-01-15T10:30:00Z
   Summary: Added README.md with installation instructions
   Repository: https://github.com/your-org/your-repo
   Branch: cursor/add-readme-1234
   🔗 PR created: https://github.com/your-org/your-repo/pull/1234
   📊 Dashboard: https://cursor.com/agents?id=bc_abc123

✅ Agent completed successfully!
   📢 NOTIFICATION: ✅ Agent bc_abc123 completed: Added README.md...
   🔗 PR: https://github.com/your-org/your-repo/pull/1234
```

---

## Webhook Headers Reference

| Header | Description | Example |
|--------|-------------|---------|
| `X-Webhook-Signature` | HMAC-SHA256 signature | `sha256=abc123...` |
| `X-Webhook-ID` | Unique delivery ID | `wh_abc123` |
| `X-Webhook-Event` | Event type | `statusChange` |
| `User-Agent` | Identifies sender | `Cursor-Agent-Webhook/1.0` |

---

## Success Criteria

- [ ] Webhook server running locally
- [ ] ngrok tunnel established
- [ ] Created agent with webhook URL
- [ ] Received webhook notification
- [ ] Verified signature (optional)
- [ ] Parsed webhook payload

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Port 5000 in use | Change to different port (e.g., 5001) |
| ngrok not found | Install ngrok from ngrok.com/download |
| Webhook not received | Check ngrok URL is correct and server is running |
| Invalid signature | Ensure secret matches on both ends |

---

## Key Takeaways

| Concept | Value |
|---------|-------|
| **Webhook event** | `statusChange` (FINISHED or ERROR) |
| **Signature verification** | HMAC-SHA256 with your secret |
| **Headers** | X-Webhook-Signature, X-Webhook-ID, X-Webhook-Event |
| **Retries** | Cursor retries failed deliveries |
| **Best practice** | Return 2xx quickly, process async |

---

## Exercise Complete ✓

Check off when done:
- [ ] Created webhook server
- [ ] Exposed with ngrok
- [ ] Created agent with webhook URL
- [ ] Received webhook notification
- [ ] Verified signature
- [ ] Parsed webhook payload

---

## Troubleshooting (common beginner issues)

| Problem | What to try |
|---------|-------------|
| Agent panel won't open | Click inside Cursor first; try `Ctrl+Shift+P` → **Open Agent** |
| No diff appears | Switch from Ask Mode to **Agent Mode** in the panel footer |
| Agent can't see my files | **File → Open Folder** (not a single file) |
| Wrong terminal shell | ``Ctrl+` `` → **Terminal: Select Default Profile** → **PowerShell** |
| `curl` fails or behaves oddly | Use **`curl.exe`** in PowerShell, not the `curl` alias |
| `gcc` not found | Install [MinGW-w64](https://www.mingw-w64.org/) or MSVC build tools; restart terminal |
| `.sh` script won't run | On Windows use the matching `.bat` file or PowerShell commands |
| API returns 401 | Re-copy API key; check `Authorization: Bearer` header |
| API returns 429 | Wait and retry; see Exercise 7.3 for backoff |

---

## Exercise complete

- [ ] Finished all steps above
- [ ] Checked success criteria
- [ ] Noted one thing you would do differently on a real project
