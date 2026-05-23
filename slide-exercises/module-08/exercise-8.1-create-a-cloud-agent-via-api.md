# Exercise 8.1: Create a Cloud Agent via API

**Module 8:** Cloud Agents API and Webhooks  
**Slides:** `slides/module-08-marp.md` (Lesson 8.1)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Create a Cloud Agent run using curl or Python.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

**Step 1 — set API key · Terminal:** **PowerShell**

```powershell
$env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx"
```

**Step 2 — create agent · Terminal:** **PowerShell**

```powershell
curl.exe -X POST https://api.cursor.com/v1/agents `
  -u "$($env:CURSOR_USER_API_KEY):" `
  -H "Content-Type: application/json" `
  -d '{"prompt":{"text":"Add a README.md file with setup instructions"},"repos":[{"url":"https://github.com/YOUR_ORG/YOUR_REPO","startingRef":"main"}],"autoCreatePR":true}' `
  | ConvertFrom-Json
```

**Terminal (alternative):** **Git Bash** / **WSL** — bash block below.

```bash
export CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx"
curl -X POST https://api.cursor.com/v1/agents   -u "$CURSOR_USER_API_KEY:"   -H "Content-Type: application/json"   -d '{"prompt":{"text":"Add a README.md file with setup instructions"},"repos":[{"url":"https://github.com/YOUR_ORG/YOUR_REPO","startingRef":"main"}],"autoCreatePR":true}' | jq '.'
```

---



**Step 1:** Save the JSON from the create-agent call — **Terminal:** **PowerShell**

```powershell
$response = curl.exe ... | ConvertFrom-Json   # reuse create-agent command
$env:AGENT_ID = $response.agent.id
$env:RUN_ID = $response.run.id
Write-Host "Agent ID: $($env:AGENT_ID)"
Write-Host "Dashboard: https://cursor.com/agents/$($env:AGENT_ID)"
```

---

**Step 2:** Optional model override in create payload — **Where:** edit JSON before POST (any terminal)

Create with specific model: `"model": {"id": "claude-4.7-opus"}`

---



```python
def create_agent(prompt, repo_url, auto_create_pr=False, model=None):
    payload = {
        "prompt": {"text": prompt},
        "repos": [{"url": repo_url}],
        "autoCreatePR": auto_create_pr
    }
    if model:
        payload["model"] = {"id": model}
    response = requests.post(f"{BASE_URL}/agents", auth=AUTH, json=payload)
    data = response.json()
    return data["agent"]["id"], data["run"]["id"]
```

---

## Success criteria

- [ ] Agent created · IDs captured · appears in dashboard · Python function works

---

## Additional reference

## Expected Response

### Step 1 Response:
```json
{
  "agent": {
    "id": "bc-00000000-0000-0000-0000-000000000001",
    "name": "Add a README.md file with setup instructions...",
    "status": "ACTIVE",
    "env": {
      "type": "cloud"
    },
    "repos": [
      {
        "url": "https://github.com/YOUR_ORG/YOUR_REPO",
        "startingRef": "main"
      }
    ],
    "branchName": "cursor/add-readme-1234567890",
    "autoGenerateBranch": true,
    "autoCreatePR": true,
    "url": "https://cursor.com/agents/bc-00000000-0000-0000-0000-000000000001",
    "createdAt": "2025-01-15T10:30:00.000Z",
    "updatedAt": "2025-01-15T10:30:00.000Z",
    "latestRunId": "run-00000000-0000-0000-0000-000000000001"
  },
  "run": {
    "id": "run-00000000-0000-0000-0000-000000000001",
    "agentId": "bc-00000000-0000-0000-0000-000000000001",
    "status": "CREATING",
    "createdAt": "2025-01-15T10:30:00.000Z",
    "updatedAt": "2025-01-15T10:30:00.000Z"
  }
}
```

### Step 2 Output:
```
Agent ID: bc-00000000-0000-0000-0000-000000000001
Run ID: run-00000000-0000-0000-0000-000000000001
Dashboard: https://cursor.com/agents/bc-00000000-0000-0000-0000-000000000001
```

---

## Request Body Fields Reference

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| `prompt.text` | ✅ Yes | The instruction for the agent | `"Add a README file"` |
| `repos[].url` | ✅ Yes | GitHub repository URL | `"https://github.com/org/repo"` |
| `repos[].startingRef` | No | Branch/tag/commit to start from | `"main"` |
| `model.id` | No | AI model to use | `"composer-2"` |
| `model.params` | No | Model parameters | `[{"id":"thinking","value":"high"}]` |
| `branchName` | No | Custom branch name | `"feature/my-task"` |
| `autoGenerateBranch` | No | Create new branch (default: true) | `true` |
| `autoCreatePR` | No | Open PR when done | `true` |
| `skipReviewerRequest` | No | Skip requesting reviewer | `false` |
| `envVars` | No | Environment variables | `{"API_KEY":"secret"}` |

---

## Common Status Values

| Status | Meaning |
|--------|---------|
| `CREATING` | Agent is being initialized |
| `ACTIVE` | Agent ready to accept runs |
| `RUNNING` | Agent is actively working |
| `FINISHED` | Agent completed successfully |
| `ERROR` | Agent encountered an error |
| `CANCELLED` | Agent was cancelled |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 401 Unauthorized | Check API key is set correctly |
| 404 Not Found | Repository URL may be incorrect or GitHub not connected |
| 400 Bad Request | Check JSON syntax. Missing quotes or commas |
| Agent stuck in CREATING | Wait a few seconds; check dashboard for errors |
| No PR created | Ensure `autoCreatePR: true` and agent had changes to commit |

---

## Key Takeaways

| Concept | Value |
|---------|-------|
| **Endpoint** | `POST /v1/agents` |
| **Authentication** | User API key (or service account) |
| **Response** | Returns both `agent` and `run` objects |
| **Agent ID** | Use for future operations (streaming, artifacts) |
| **Run ID** | Use for monitoring this specific execution |
| **Dashboard URL** | View agent in web UI |

---

## Bonus Challenge

Create an agent with environment variables for sensitive data:

```bash
curl -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {
      "text": "Run the deployment script using the API key from environment"
    },
    "repos": [{"url": "https://github.com/YOUR_ORG/YOUR_REPO"}],
    "envVars": {
      "DEPLOY_API_KEY": "secret-value-here",
      "ENVIRONMENT": "staging"
    },
    "autoCreatePR": false
  }' | jq '.agent.id'
```

---
