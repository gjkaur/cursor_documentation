# Exercise 8.4: Webhooks and HMAC Verification

**Module 8:** Cloud Agents API and Webhooks  
**Slides:** `slides/module-08-marp.md` (Lesson 8.4)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Receive webhooks and verify HMAC signatures.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```python
def verify_signature(raw_body, signature_header):
    received = signature_header[7:]  # strip "sha256="
    expected = hmac.new(
        WEBHOOK_SECRET.encode(), raw_body, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, received)
```

Flask route: verify signature → parse payload → handle FINISHED/ERROR

---



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
  }'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

---

## Success criteria

- [ ] Server running · signature verified · payload parsed · agent configured

---

## Additional reference

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
