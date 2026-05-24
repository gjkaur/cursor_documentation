# Exercise 8.1: Create a Cloud Agent via API

**Module 8:** Cloud Agents API and Webhooks  
**Slides:** `slides/module-08-marp.md` (Lesson 8.1)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Create a Cloud Agent run using curl or Python.

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

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

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

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

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

**Success Criteria:** Agent created · IDs captured · appears in dashboard · Python function works

---

## Success criteria

- [ ] Agent created · IDs captured · appears in dashboard · Python function works

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] API key from Exercise 1 (User API key works for Cloud Agents API)
- [ ] GitHub repository connected to Cursor
- [ ] `curl` and `jq` installed

---

## Step-by-Step Instructions

### Step 1: Create a Simple Cloud Agent (3 minutes)

Create an agent that adds a README file to your repository.

**Command:**
```bash
curl -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {
      "text": "Add a README.md file with setup instructions and a brief project description"
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

**Replace:** `YOUR_ORG/YOUR_REPO` with your actual GitHub repository.

---

### Step 2: Capture Agent ID and Run ID (2 minutes)

Extract and store the IDs for later use.

**Command:**
```bash
# Create agent and capture IDs
RESPONSE=$(curl -s -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {
      "text": "Add a README.md file with setup instructions"
    },
    "repos": [{"url": "https://github.com/YOUR_ORG/YOUR_REPO"}],
    "autoCreatePR": true
  }')

AGENT_ID=$(echo "$RESPONSE" | jq -r '.agent.id')
RUN_ID=$(echo "$RESPONSE" | jq -r '.run.id')

echo "Agent ID: $AGENT_ID"
echo "Run ID: $RUN_ID"
echo "Dashboard: https://cursor.com/agents/$AGENT_ID"
```

**Expected output:**
```
Agent ID: bc-00000000-0000-0000-0000-000000000001
Run ID: run-00000000-0000-0000-0000-000000000001
Dashboard: https://cursor.com/agents/bc-00000000-0000-0000-0000-000000000001
```

---

### Step 3: Create an Agent with Custom Branch (2 minutes)

Specify a custom branch name for the agent to use.

**Command:**
```bash
curl -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {
      "text": "Add unit tests for the calculator functions"
    },
    "repos": [
      {
        "url": "https://github.com/YOUR_ORG/YOUR_REPO",
        "startingRef": "main"
      }
    ],
    "branchName": "feature/add-tests",
    "autoCreatePR": true
  }' | jq '{agent: {id: .agent.id, branchName: .agent.branchName}, run: {id: .run.id, status: .run.status}}'
```

---

### Step 4: Create an Agent with Specific Model (2 minutes)

Specify which AI model the agent should use.

**Command:**
```bash
curl -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {
      "text": "Review the codebase for potential security issues"
    },
    "model": {
      "id": "claude-4.7-opus",
      "params": [
        {"id": "thinking", "value": "high"}
      ]
    },
    "repos": [
      {
        "url": "https://github.com/YOUR_ORG/YOUR_REPO",
        "startingRef": "main"
      }
    ],
    "autoCreatePR": true
  }' | jq '{agent: {id: .agent.id, model: .agent.model}, run: {id: .run.id}}'
```

---

### Step 5: Create a Python Script for Agent Creation (1 minute)

**Create `create_agent.py`:**
```python
#!/usr/bin/env python3
"""
Create a Cloud Agent programmatically
"""

import requests
import os
import sys
import json
import time

API_KEY = os.environ.get("CURSOR_USER_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_USER_API_KEY environment variable")
    sys.exit(1)

def create_agent(repo_url, prompt, model_id=None, branch_name=None, auto_create_pr=True):
    """
    Create a Cloud Agent.
    
    Args:
        repo_url: GitHub repository URL
        prompt: Task description for the agent
        model_id: Optional model ID (default: uses team default)
        branch_name: Optional custom branch name
        auto_create_pr: Whether to auto-create a PR
    
    Returns:
        Tuple of (agent_id, run_id, dashboard_url)
    """
    url = "https://api.cursor.com/v1/agents"
    auth = (API_KEY, "")
    
    payload = {
        "prompt": {"text": prompt},
        "repos": [{"url": repo_url}],
        "autoCreatePR": auto_create_pr
    }
    
    if model_id:
        payload["model"] = {"id": model_id}
    
    if branch_name:
        payload["branchName"] = branch_name
    
    response = requests.post(url, auth=auth, json=payload)
    
    if response.status_code != 200:
        print(f"❌ Error: {response.status_code}")
        print(f"   {response.text}")
        return None, None, None
    
    data = response.json()
    agent_id = data.get("agent", {}).get("id")
    run_id = data.get("run", {}).get("id")
    dashboard_url = f"https://cursor.com/agents/{agent_id}" if agent_id else None
    
    return agent_id, run_id, dashboard_url

def main():
    print("🚀 Cloud Agent Creator")
    print("=" * 40)
    
    # Configuration
    REPO_URL = "https://github.com/YOUR_ORG/YOUR_REPO"
    PROMPT = "Add a README.md file with setup instructions"
    
    print(f"\n📦 Creating agent for: {REPO_URL}")
    print(f"📝 Prompt: {PROMPT}")
    
    agent_id, run_id, dashboard_url = create_agent(REPO_URL, PROMPT)
    
    if agent_id:
        print(f"\n✅ Agent created successfully!")
        print(f"   Agent ID: {agent_id}")
        print(f"   Run ID: {run_id}")
        print(f"   Dashboard: {dashboard_url}")
    else:
        print("\n❌ Failed to create agent")

if __name__ == "__main__":
    main()
```

**Run the script:**
```bash
export CURSOR_USER_API_KEY="your_key_here"
python3 create_agent.py
```

---

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

## Success Criteria

- [ ] Agent created successfully
- [ ] Agent ID captured
- [ ] Run ID captured
- [ ] Custom branch name specified (optional)
- [ ] Specific model selected (optional)
- [ ] Agent appears in `cursor.com/agents` dashboard
- [ ] Created Python script for agent creation

---

## Request Body Fields Reference

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| `prompt.text` | ✅ Yes | The instruction for the agent | `"Add a README file"` |
| `repos[].url` | ✅ Yes | GitHub repository URL | `"https://github.com/org/repo"` |
| `repos[].startingRef` | No | Branch/tag/commit to start from | `"main"` |
| `model.id` | No | AI model to use | `"composer-2.5"` |
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

## Exercise Complete ✓

Check off when done:
- [ ] Created a Cloud Agent via API
- [ ] Captured agent ID and run ID
- [ ] Created agent with custom branch name
- [ ] Created agent with specific model
- [ ] Verified agent appears in dashboard
- [ ] (Bonus) Added environment variables

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
