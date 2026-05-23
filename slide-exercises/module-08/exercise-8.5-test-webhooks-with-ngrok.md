# Exercise 8.5: Test Webhooks with ngrok

**Module 8:** Cloud Agents API and Webhooks  
**Slides:** `slides/module-08-marp.md` (Lesson 8.5)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Expose a local server with ngrok and inspect webhook payloads.

---

## API basics (read this first)

1. Use **PowerShell** or **Git Bash** in Cursor's terminal (``Ctrl+` ``).
2. Store keys in environment variables — never commit them:

```powershell
$env:CURSOR_ADMIN_API_KEY = "crsr_your_key_here"
$env:CURSOR_USER_API_KEY = "cursor_user_your_key_here"
```

3. Prefer `curl.exe` on Windows (not the `curl` alias) or Python `requests`.
4. Run scripts from a dedicated folder inside this repo or your own sandbox project.


---

## Steps from the training slides

Follow these steps in order. Copy prompts exactly unless the exercise tells you to adapt them.

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

**Step 1:** Start tunnel:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
ngrok http 5000
# Forwarding: https://abc123.ngrok.io -> http://localhost:5000
```

---

**Step 2:** Copy HTTPS URL
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

---

**Step 3:** Create agent with ngrok URL:
**Terminal:** **PowerShell** — ``Ctrl+` `` in Cursor

```bash
curl -X POST https://api.cursor.com/v1/agents ... \
  -d '{"webhookUrl": "https://abc123.ngrok.io/webhook/cursor", ...}'
```

---

**Platform:** Windows 10/11 · Agent → ``Ctrl+L`` · Shell → **PowerShell** · Browser for dashboards

**Step 4:** Inspect requests at `http://127.0.0.1:4040`
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

**Step 5:** Replay failed webhooks (ngrok premium) — inspect raw body and headers
**Terminal:** **Git Bash** or **Ubuntu (WSL)** — bash syntax required

**Success Criteria:** Tunnel established · webhook received · signature verified · inspected in ngrok UI

---

## Success criteria

- [ ] Tunnel established · webhook received · signature verified · inspected in ngrok UI

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] User API key from Exercise 1
- [ ] Webhook server from Exercise 20 (running)
- [ ] ngrok installed (https://ngrok.com/download)
- [ ] `curl` and `jq` installed

---

## Step-by-Step Instructions

### Step 1: Start Your Webhook Server (1 minute)

Make sure your webhook server from Exercise 20 is running.

**Command:**
```bash
python webhook_server.py
```

**Expected output:**
```
🚀 Cursor Webhook Server
========================================
Webhook endpoint: http://localhost:5000/webhook/cursor
Health check: http://localhost:5000/webhook/health
Waiting for webhook events...
```

---

### Step 2: Start ngrok (2 minutes)

In a new terminal, start ngrok to expose your local server.

**Command:**
```bash
ngrok http 5000
```

**Expected output:**
```
ngrok by @inconshreveable

Session Status                online
Account                       your-email@company.com
Version                       3.x.x
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://abc123.ngrok.io -> http://localhost:5000
Forwarding                    http://abc123.ngrok.io -> http://localhost:5000
```

**Copy the HTTPS URL** (e.g., `https://abc123.ngrok.io`) - you'll need this for webhook configuration.

---

### Step 3: Test Webhook Endpoint Accessibility (1 minute)

Verify that ngrok is working by accessing the health endpoint.

**Command:**
```bash
curl https://abc123.ngrok.io/webhook/health
```

**Expected response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-01-15T10:30:00.000Z"
}
```

---

### Step 4: Create an Agent with Webhook (2 minutes)

Create a Cloud Agent that sends webhooks to your ngrok URL.

**Command:**
```bash
# Replace with your ngrok URL
WEBHOOK_URL="https://abc123.ngrok.io/webhook/cursor"

RESPONSE=$(curl -s -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {
      "text": "Create a simple hello world program"
    },
    "repos": [
      {
        "url": "https://github.com/YOUR_ORG/YOUR_REPO",
        "startingRef": "main"
      }
    ],
    "autoCreatePR": false,
    "webhookUrl": "'"$WEBHOOK_URL"'",
    "webhookSecret": "your-secret-here"
  }')

AGENT_ID=$(echo "$RESPONSE" | jq -r '.agent.id')
echo "Agent ID: $AGENT_ID"
echo "Dashboard: https://cursor.com/agents/$AGENT_ID"
```

---

### Step 5: Monitor Webhook Delivery (2 minutes)

Watch both terminals for webhook delivery.

**Terminal 1 (webhook server) will show:**
```
📨 Received webhook: wh_abc123
   Event: statusChange
   ✅ Signature verified

📊 Agent bc_xxx status: FINISHED
   Summary: Created hello world program
   🔗 PR created: https://github.com/.../pull/123
```

**Terminal 2 (ngrok) will show request details:**
```
POST /webhook/cursor           200 OK
Duration: 45ms                  Content-Length: 1.2KB
```

---

### Step 6: Test Webhook Retry Behavior (2 minutes)

Stop your webhook server temporarily to simulate a failure, then restart to see retry behavior.

**Step A: Stop webhook server (Ctrl+C in terminal 1)**

**Step B: Create another agent:**
```bash
# Replace with your ngrok URL
WEBHOOK_URL="https://abc123.ngrok.io/webhook/cursor"

curl -s -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {"text": "Add a comment to the main file"},
    "repos": [{"url": "https://github.com/YOUR_ORG/YOUR_REPO"}],
    "webhookUrl": "'"$WEBHOOK_URL"'"
  }' | jq '.agent.id'
```

**Step C: Wait 30 seconds, then restart webhook server**

**Step D: Watch for retried delivery - Cursor will retry failed webhooks**

---

### Step 7: Inspect ngrok Web Interface (1 minute)

ngrok provides a web interface to inspect all requests.

**Open in browser:**
```
http://127.0.0.1:4040
```

**You can see:**
- All webhook requests
- Request/response headers
- Payload content
- Response status codes
- Timing information

---

## Webhook Testing Script

**Create `test_webhook_delivery.py`:**
```python
#!/usr/bin/env python3
"""
Test webhook delivery and retry behavior
"""

import requests
import time
import os
import sys
import json

API_KEY = os.environ.get("CURSOR_USER_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_USER_API_KEY environment variable")
    sys.exit(1)

def test_webhook_delivery(webhook_url, repo_url):
    """Test webhook delivery by creating an agent."""
    
    print("🚀 Testing Webhook Delivery")
    print("=" * 50)
    
    # Create agent with webhook
    print(f"\n📡 Creating agent with webhook: {webhook_url}")
    
    response = requests.post(
        "https://api.cursor.com/v1/agents",
        auth=(API_KEY, ""),
        json={
            "prompt": {"text": "Add a README.md file"},
            "repos": [{"url": repo_url}],
            "autoCreatePR": False,
            "webhookUrl": webhook_url,
            "webhookSecret": "test-secret"
        }
    )
    
    if response.status_code != 200:
        print(f"❌ Failed to create agent: {response.status_code}")
        print(f"   {response.text}")
        return
    
    data = response.json()
    agent_id = data.get("agent", {}).get("id")
    print(f"✅ Agent created: {agent_id}")
    print(f"   Dashboard: https://cursor.com/agents/{agent_id}")
    
    # Monitor for webhook
    print("\n⏳ Waiting for webhook delivery...")
    print("   (Check your webhook server logs)")
    
    return agent_id

def test_retry_behavior(webhook_url, repo_url):
    """Test webhook retry by temporarily stopping server."""
    
    print("\n🔄 Testing Webhook Retry Behavior")
    print("=" * 50)
    print("This test requires you to:")
    print("1. Keep ngrok running")
    print("2. STOP your webhook server (Ctrl+C)")
    print("3. Run this script to create an agent")
    print("4. RESTART your webhook server within 60 seconds")
    print("5. Watch for retried delivery\n")
    
    input("Press Enter when your webhook server is STOPPED...")
    
    response = requests.post(
        "https://api.cursor.com/v1/agents",
        auth=(API_KEY, ""),
        json={
            "prompt": {"text": "Add a test comment"},
            "repos": [{"url": repo_url}],
            "autoCreatePR": False,
            "webhookUrl": webhook_url
        }
    )
    
    if response.status_code == 200:
        agent_id = response.json().get("agent", {}).get("id")
        print(f"✅ Agent created: {agent_id}")
        print("\n⏳ Now RESTART your webhook server")
        print("   Cursor will retry the webhook delivery")
    else:
        print(f"❌ Failed: {response.status_code}")

def check_ngrok_status():
    """Check if ngrok is running."""
    try:
        response = requests.get("http://127.0.0.1:4040/api/tunnels", timeout=2)
        if response.status_code == 200:
            tunnels = response.json().get("tunnels", [])
            for tunnel in tunnels:
                if tunnel.get("proto") == "https":
                    print(f"✅ ngrok running: {tunnel.get('public_url')}")
                    return tunnel.get('public_url')
    except:
        pass
    
    print("❌ ngrok not running. Start with: ngrok http 5000")
    return None

if __name__ == "__main__":
    print("Webhook Testing Tool")
    print("=" * 40)
    
    # Check ngrok
    webhook_url = check_ngrok_status()
    
    if not webhook_url:
        sys.exit(1)
    
    webhook_url = f"{webhook_url}/webhook/cursor"
    
    print("\n1. Test normal delivery")
    print("2. Test retry behavior")
    
    choice = input("\nSelect test (1 or 2): ").strip()
    
    repo_url = input("Enter repository URL: ").strip()
    
    if choice == "1":
        test_webhook_delivery(webhook_url, repo_url)
    elif choice == "2":
        test_retry_behavior(webhook_url, repo_url)
    else:
        print("Invalid choice")
```

---

## Ngrok Web Interface Features

| Feature | Description |
|---------|-------------|
| **Inspector** | View all requests and responses |
| **Replay** | Resend any webhook for testing |
| **Copy as curl** | Get curl command for any request |
| **Request/Response body** | View full payloads |
| **Headers** | View all headers including signatures |

---

## Expected ngrok Web Interface View

```
┌─────────────────────────────────────────────────────────────────┐
│  ngrok Request Inspector                                        │
├─────────────────────────────────────────────────────────────────┤
│  GET /webhook/health        200 OK    2025-01-15 10:30:00       │
│  POST /webhook/cursor       200 OK    2025-01-15 10:31:00       │
│                                                                 │
│  ┌─ Request Details ─────────────────────────────────────────┐  │
│  │ POST /webhook/cursor                                      │  │
│  │ Headers:                                                  │  │
│  │   X-Webhook-Signature: sha256=abc123...                  │  │
│  │   X-Webhook-ID: wh_abc123                                 │  │
│  │   Content-Type: application/json                          │  │
│  │                                                           │  │
│  │ Body:                                                     │  │
│  │ {                                                         │  │
│  │   "event": "statusChange",                                │  │
│  │   "id": "bc_abc123",                                      │  │
│  │   "status": "FINISHED",                                   │  │
│  │   ...                                                     │  │
│  │ }                                                         │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Success Criteria

- [ ] Webhook server running
- [ ] ngrok tunnel established
- [ ] Health endpoint accessible via ngrok
- [ ] Agent created with webhook URL
- [ ] Webhook received and processed
- [ ] Inspected ngrok web interface
- [ ] Tested retry behavior (optional)

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| ngrok connection refused | Start ngrok before creating agent |
| Webhook not received | Check ngrok URL is correct (use HTTPS, not HTTP) |
| 404 on webhook | Ensure endpoint path matches (`/webhook/cursor`) |
| Signature mismatch | Verify secret is same on both ends |
| ngrok URL changes | Each ngrok session has a new URL; update agent creation |

---

## Key Takeaways

| Concept | Value |
|---------|-------|
| **ngrok** | Exposes local server to internet |
| **Web interface** | `http://127.0.0.1:4040` for inspection |
| **Retry behavior** | Cursor retries failed deliveries |
| **Testing** | Use ngrok to test without deploying |

---

## Exercise Complete ✓

Check off when done:
- [ ] Webhook server running
- [ ] ngrok tunnel established
- [ ] Health endpoint accessible
- [ ] Agent created with webhook URL
- [ ] Webhook received and processed
- [ ] Inspected ngrok web interface
- [ ] Tested retry behavior (optional)

---

## Troubleshooting (common beginner issues)

| Problem | What to try |
|---------|-------------|
| Agent panel won't open | Click inside Cursor first; try `Ctrl+Shift+P` → **Open Agent** |
| No diff appears | Switch from Ask Mode to **Agent Mode** in the panel footer |
| Agent can't see my files | **File → Open Folder** (not a single file) |
| Terminal command fails on Windows | Use **PowerShell**; use `curl.exe` instead of `curl` |
| API returns 401 | Re-copy API key; check `Authorization: Bearer` header |
| API returns 429 | Wait and retry; see Exercise 7.3 for backoff |

---

## Exercise complete

- [ ] Finished all steps above
- [ ] Checked success criteria
- [ ] Noted one thing you would do differently on a real project
