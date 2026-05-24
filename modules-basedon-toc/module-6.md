# Module 6: Cloud Agents in the UI

## Cursor Training Program — Day 2 (Hands-On + Demonstration)

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~90 minutes |
| **Format** | Hands-on exercise + demonstration |
| **Prerequisites** | Cursor account, GitHub repository access, Modules 1-5 completed |
| **Module Goal** | Master the Cloud Agents UI for remote execution, artifact collection, and messaging integrations |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Launch and monitor Cloud Agents from the Cursor UI
- Collect and download artifacts from completed cloud runs
- Trigger Cloud Agents from messaging platforms (Slack, Discord)
- Manage cloud agent history and settings

---

## Lesson 6.1: Launching a Cloud Agent

### Concept (10 minutes)

> *"The core remote execution capability. Cloud Agents run in Cursor's infrastructure, not on your machine – perfect for long-running tasks, scheduled jobs, or when you need to close your laptop."*

### Cloud Agents vs. Local Agent

| Aspect | Local Agent | Cloud Agent |
|--------|-------------|-------------|
| **Runs on** | Your machine | Cursor's infrastructure |
| **Persistence** | Ends when you quit | Continues indefinitely |
| **Access** | Local only | Web, mobile, API |
| **Terminal access** | Your terminal | Simulated/scripted |
| **File access** | Local files | GitHub repos only |
| **Cost** | Included in subscription | Per-run (see pricing) |
| **Best for** | Interactive work | Batch, scheduled, hands-off |

### When to Use Cloud Agents

```
┌─────────────────────────────────────────────────────────────┐
│              CLOUD AGENT USE CASES                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ✅ GOOD FOR CLOUD AGENTS:                                  │
│  • Long-running tasks (>10 minutes)                         │
│  • Scheduled jobs (daily reports, weekly maintenance)       │
│  • Tasks you want to run while offline                      │
│  • Parallel execution of multiple agents                    │
│  • Team-accessible results (share agent URL)                │
│                                                              │
│  ❌ BAD FOR CLOUD AGENTS:                                   │
│  • Interactive debugging                                    │
│  • Tasks needing local files (not in GitHub)                │
│  • Security-sensitive code (must stay local)                │
│  • Quick questions (faster locally)                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Accessing Cloud Agents UI

**Navigation Paths:**

| Method | Steps |
|--------|-------|
| **From Cursor Editor** | View → Cloud Agents (or click cloud icon in sidebar) |
| **From Web** | https://cursor.com/agents |
| **From Mobile** | cursor.com/agents (responsive web) |

### Cloud Agent Dashboard Overview

```
┌─────────────────────────────────────────────────────────────┐
│  🤖 Cloud Agents                                    [+ New]  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Active (2)                                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 🔄 security-audit-2024    running • 12 min elapsed  │   │
│  │    Started: 10:32 AM • repo: company/app            │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │ 🔄 doc-generator           running • 3 min elapsed  │   │
│  │    Started: 10:41 AM • repo: company/docs           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  Completed (4)                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ ✅ pr-review-42            FINISHED • 2 artifacts   │   │
│  │    Completed: 9:15 AM • PR #42                      │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │ ✅ test-suite              FINISHED • 1 artifact    │   │
│  │    Completed: 8:45 AM • All tests passed           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  Failed (1)                                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ ❌ deploy-staging          ERROR • see logs         │   │
│  │    Failed: 7:30 AM • Auth token expired            │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Hands-On Exercise (15 minutes)

**Step 1:** Navigate to Cloud Agents

```bash
# Option A: From Cursor Editor
# Click the cloud icon in the left sidebar or go to View → Cloud Agents

# Option B: From browser
open https://cursor.com/agents
```

**Step 2:** Create your first Cloud Agent

Click **"+ New"** button and fill out the form:

```
┌─────────────────────────────────────────────────────────────┐
│  New Cloud Agent                                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Repository: https://github.com/YOUR_ORG/YOUR_REPO         │
│                                                              │
│  Branch: main                                               │
│                                                              │
│  Prompt:                                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Read the README.md and the main source files.       │   │
│  │ Create a summary of:                                │   │
│  │ - What this project does                            │   │
│  │ - Key dependencies                                  │   │
│  │ - How to run it locally                            │   │
│  │ - Common issues and solutions                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  Model: claude-4.6-sonnet        [Change]                   │
│                                                              │
│  Auto-create PR: ☐                                          │
│                                                              │
│                              [Cancel]  [Launch Agent]       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Step 3:** Monitor the agent in real-time

After launching, you'll see the live log:

```
┌─────────────────────────────────────────────────────────────┐
│  Agent: project-summary-2024                    [Running]  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  📡 Live Log                                                 │
│                                                              │
│  [10:45:01] Agent starting...                               │
│  [10:45:02] Cloning repository...                           │
│  [10:45:15] Repository cloned                               │
│  [10:45:16] Reading README.md                               │
│  [10:45:18] Reading package.json/setup.py                   │
│  [10:45:25] Analyzing dependencies                          │
│  [10:45:40] Generating summary...                           │
│  [10:45:55] Agent thinking...                               │
│                                                              │
│  ─────────────────────────────────────────────────────────  │
│  Agent: I've analyzed the repository. Here's what I found:  │
│                                                              │
│  ## Project Summary                                          │
│                                                              │
│  This is a FastAPI-based task management API...             │
│                                                              │
│  (continuing)                                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Step 4:** Configure agent settings

Click **Settings** (gear icon) to configure:

| Setting | Options | Purpose |
|---------|---------|---------|
| **Default Model** | List of available models | Set preferred model for new agents |
| **Auto-create PR** | On/Off | Automatically create PRs on completion |
| **Notification Email** | Email address | Receive completion notifications |
| **Webhook URL** | HTTPS endpoint | POST completion events |
| **Max Run Time** | 5min - 24hrs | Prevent runaway agents |

**Step 5:** Launch an agent with PR creation

Create a new agent with:

```
Prompt: "Add a CONTRIBUTING.md file with guidelines for:
- How to set up the dev environment
- How to run tests
- PR submission process
- Code style requirements"

Auto-create PR: ✅ Yes

Branch prefix: docs/contributing
```

**Step 6:** Share an agent with team members

```bash
# Each agent has a unique URL
# Click "Share" button to copy
https://cursor.com/agents/agt_abc123def456

# Team members can view logs and artifacts without login
# (if agent is set to public)
```

**Success Criteria:**
- [ ] Accessed Cloud Agents UI
- [ ] Launched a Cloud Agent from UI
- [ ] Monitored live agent logs
- [ ] Configured agent settings
- [ ] Launched agent with PR creation
- [ ] Shared agent URL

---

## Lesson 6.2: Cloud Agent Artifacts

### Concept (8 minutes)

> *"Collecting outputs from a cloud run. Artifacts are files produced by the agent – screenshots, generated code, logs, reports – that you can download or view in the UI."*

### Types of Artifacts

| Artifact Type | Description | Examples |
|---------------|-------------|----------|
| **Log files** | Agent execution logs | `agent.log`, `debug.log` |
| **Code files** | Generated/modified code | `*.py`, `*.js`, `*.html` |
| **Documents** | Markdown, text reports | `*.md`, `*.txt`, `*.json` |
| **Images** | Screenshots, diagrams | `*.png`, `*.jpg`, `*.svg` |
| **Archives** | Multiple files bundled | `*.zip`, `*.tar.gz` |
| **Test results** | Test outputs | `junit.xml`, `coverage.json` |

### Artifact Storage

```
┌─────────────────────────────────────────────────────────────┐
│                    ARTIFACT STORAGE                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  • Artifacts are stored for 30 days                         │
│  • Each agent can have multiple artifacts                   │
│  • Download URLs expire after 15 minutes                    │
│  • Max artifact size: 100MB per file                        │
│  • Total artifacts per agent: 1GB limit                     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Hands-On Exercise (15 minutes)

**Step 1:** Create an agent that generates artifacts

Launch a Cloud Agent with this prompt:

```
Generate the following artifacts:

1. A file called `api_documentation.md` with OpenAPI-style docs for all endpoints
2. A file called `test_report.json` summarizing the test suite
3. A screenshot of the main UI (if applicable) as `screenshot.png`
4. A file called `dependencies.txt` listing all packages and versions

Place all artifacts in an `artifacts/` directory.
```

**Step 2:** Wait for completion and view artifacts

After the agent finishes, you'll see:

```
┌─────────────────────────────────────────────────────────────┐
│  Agent: doc-generator-2024                     [FINISHED]   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  📎 Artifacts (4)                                            │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 📄 api_documentation.md    15.2 KB    [Download]    │   │
│  │ 📄 test_report.json        8.4 KB     [Download]    │   │
│  │ 🖼️ screenshot.png          245 KB     [Download]    │   │
│  │ 📄 dependencies.txt        1.2 KB     [Download]    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  📦 Download All (zip)                                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Step 3:** Download individual artifacts

Click **Download** next to any artifact to save it locally.

**Step 4:** Download all artifacts as zip

Click **"Download All (zip)"** to get a single archive containing all artifacts.

**Step 5:** Preview artifacts in browser

Some artifacts can be previewed directly:
- Markdown files: Rendered HTML preview
- Images: Inline preview
- JSON: Formatted tree view
- Text files: Raw view with line numbers

**Step 6:** Access artifacts via API

```bash
# List artifacts for an agent
curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts" | jq '.'

# Download a specific artifact
DOWNLOAD_URL=$(curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts/download?path=artifacts/report.md" \
  | jq -r '.url')

curl -L -o report.md "$DOWNLOAD_URL"
```

**Step 7:** Create an artifact processing script

Create `bin/process-artifacts.sh`:

```bash
#!/bin/bash
# Download and process artifacts from a completed Cloud Agent

AGENT_ID=$1
if [ -z "$AGENT_ID" ]; then
    echo "Usage: $0 <agent-id>"
    exit 1
fi

API_KEY="${CURSOR_USER_API_KEY}"

echo "📦 Fetching artifacts for agent: $AGENT_ID"

# Get artifact list
ARTIFACTS=$(curl -s -u "$API_KEY:" \
    "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts")

# Create output directory
mkdir -p "./artifacts_$AGENT_ID"

# Download each artifact
echo "$ARTIFACTS" | jq -r '.items[] | "\(.path) \(.size)"' | while read path size; do
    echo "  Downloading: $path ($size bytes)"
    
    DOWNLOAD_URL=$(curl -s -u "$API_KEY:" \
        "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts/download?path=$path" \
        | jq -r '.url')
    
    # Create subdirectory if needed
    mkdir -p "./artifacts_$AGENT_ID/$(dirname "$path")"
    
    curl -s -L -o "./artifacts_$AGENT_ID/$path" "$DOWNLOAD_URL"
done

echo "✅ Downloaded to ./artifacts_$AGENT_ID/"
```

**Step 8:** Use artifacts in CI/CD

```yaml
# GitHub Actions example
- name: Download Cloud Agent artifacts
  run: |
    # After agent completes, download test results
    curl -s -u "${{ secrets.CURSOR_API_KEY }}:" \
      "https://api.cursor.com/v1/agents/${{ steps.agent.outputs.agent_id }}/artifacts/download?path=test_results.xml" \
      > test_results.xml

- name: Publish Test Results
  uses: dorny/test-reporter@v1
  with:
    name: Cloud Agent Tests
    path: test_results.xml
    reporter: java-junit
```

**Success Criteria:**
- [ ] Created agent that generates artifacts
- [ ] Viewed artifact list in UI
- [ ] Downloaded single artifact
- [ ] Downloaded all artifacts as zip
- [ ] Accessed artifacts via API
- [ ] Created artifact processing script

---

## Lesson 6.3: Cloud Agents from Messaging Platforms

### Concept (10 minutes)

> *"Triggering work from chat. This demonstration shows how to integrate Cloud Agents with Slack, Microsoft Teams, Jira, Discord, and other messaging platforms – turning chat commands and ticket assignments into autonomous agents."*

### Supported Integrations

| Platform | Capabilities | Setup Complexity |
|----------|--------------|------------------|
| **Slack** | `@Cursor` mentions, command triggering, notifications | Medium (Slack app) |
| **Microsoft Teams** | `@Cursor` in channels, delegate tasks to cloud agents | Medium (Teams integration) |
| **Jira** | Assign issues to Cursor, `@Cursor` in comments, PR updates in Jira | Medium (requires Rovo) |
| **Discord** | Command triggering, webhook responses | Medium (Bot token) |
| **Generic Webhook** | POST-triggered agents | Low (any platform) |

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│              MESSAGING INTEGRATION ARCHITECTURE              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Slack/Discord/Teams                                         │
│       │                                                      │
│       │ "/cursor review PR #42"                              │
│       ↓                                                      │
│  Webhook Receiver (your server or Cursor hosted)            │
│       │                                                      │
│       │ POST /v1/agents with webhookUrl                     │
│       ↓                                                      │
│  Cursor Cloud Agent                                          │
│       │                                                      │
│       │ POST to webhookUrl when complete                    │
│       ↓                                                      │
│  Webhook Receiver → Post response to Slack                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Demonstration: Slack Integration

**Demo Setup (Instructor-led):**

**Step 1:** Create a Slack App

```bash
# Navigate to https://api.slack.com/apps
# Click "Create New App" → "From Scratch"
# Name: "Cursor Agent"
# Select your workspace
```

**Step 2:** Configure Slash Command

```
Command: /cursor
Request URL: https://your-server.com/webhook/slack-cursor
Short Description: Run a Cursor Cloud Agent
Usage Hint: [prompt or command]
```

**Step 3:** Deploy webhook receiver

```python
# webhook_slack.py - Deploy to a server (Render, Railway, AWS Lambda)
from flask import Flask, request, jsonify
import requests
import os
import json

app = Flask(__name__)

SLACK_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
CURSOR_API_KEY = os.environ.get("CURSOR_USER_API_KEY")

@app.route('/webhook/slack-cursor', methods=['POST'])
def slack_cursor():
    # Parse Slack command
    data = request.form
    user = data.get('user_name')
    command_text = data.get('text')
    response_url = data.get('response_url')
    
    # Acknowledge immediately
    # (later send actual response to response_url)
    
    # Launch Cloud Agent
    agent_response = requests.post(
        "https://api.cursor.com/v1/agents",
        auth=(CURSOR_API_KEY, ""),
        json={
            "prompt": {"text": command_text},
            "repos": [{"url": "https://github.com/your-org/your-repo"}],
            "webhookUrl": "https://your-server.com/webhook/agent-complete",
            "webhookSecret": "your-secret"
        }
    )
    
    agent_data = agent_response.json()
    agent_id = agent_data['agent']['id']
    
    # Send acknowledgment to Slack
    requests.post(response_url, json={
        "text": f"🤖 Launching Cloud Agent `{agent_id}`\n"
                f"Prompt: {command_text}\n"
                f"Watch progress: https://cursor.com/agents/{agent_id}"
    })
    
    return jsonify({"text": "Processing..."}), 200

@app.route('/webhook/agent-complete', methods=['POST'])
def agent_complete():
    # Verify signature
    payload = request.get_json()
    
    agent_id = payload.get('id')
    status = payload.get('status')
    summary = payload.get('summary')
    pr_url = payload.get('target', {}).get('prUrl')
    
    # Find which Slack channel to post to (store in DB)
    # Send completion message to Slack
    
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(port=5000)
```

**Step 4:** Test the Slack command

In Slack, type:

```
/cursor Review the recent commits and summarize what changed
```

**Expected Slack Response:**

```
🤖 Launching Cloud Agent `agt_abc123`
Prompt: Review the recent commits and summarize what changed
Watch progress: https://cursor.com/agents/agt_abc123

[5 minutes later, agent completes]

✅ Cloud Agent Complete!
Agent: agt_abc123
Summary: Found 3 commits since yesterday. Main changes: fixed login bug, added tests, updated README.
PR: https://github.com/your-org/your-repo/pull/43
```

### Demonstration: Discord Integration

**Step 1:** Create Discord Bot

```bash
# Go to Discord Developer Portal
# Create Application → Bot
# Copy Bot Token
# Enable Message Content Intent
```

**Step 2:** Discord bot code

```python
# discord_bot.py
import discord
from discord.ext import commands
import requests
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

CURSOR_API_KEY = os.environ.get("CURSOR_USER_API_KEY")
WEBHOOK_URL = "https://your-server.com/webhook/discord-cursor"

@bot.command(name='cursor')
async def cursor_command(ctx, *, prompt):
    await ctx.send(f"🤖 Launching Cloud Agent...")
    
    response = requests.post(
        "https://api.cursor.com/v1/agents",
        auth=(CURSOR_API_KEY, ""),
        json={
            "prompt": {"text": prompt},
            "repos": [{"url": "https://github.com/your-org/your-repo"}],
            "webhookUrl": WEBHOOK_URL
        }
    )
    
    agent_data = response.json()
    agent_id = agent_data['agent']['id']
    
    await ctx.send(f"✅ Agent launched: https://cursor.com/agents/{agent_id}")

bot.run(os.environ.get("DISCORD_TOKEN"))
```

**Step 3:** Usage in Discord

```
!cursor Add error handling to all API endpoints
```

### Demonstration: Generic Webhook Trigger

Any system that can send HTTP POST requests can trigger Cloud Agents:

```bash
# Trigger from any webhook sender
curl -X POST https://your-server.com/trigger-agent \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Run the weekly security scan",
    "repo": "https://github.com/company/app"
  }'
```

**Use Cases:**
- GitHub webhook → trigger on PR creation
- Cron job → scheduled agents (daily reports)
- CI/CD pipeline → post-deploy validation
- Internal dashboard → one-click agent launch

### Demonstration: Agent Status Notifications

Configure your agent to send status updates to messaging platforms:

```json
{
  "prompt": "Deploy the staging environment",
  "repos": [{"url": "https://github.com/company/app"}],
  "webhookUrl": "https://your-server.com/webhook/slack-status",
  "webhookConfig": {
    "notifyOnStart": true,
    "notifyOnComplete": true,
    "notifyOnError": true,
    "slackChannel": "#deployments"
  }
}
```

**Success Criteria (Demonstration):**
- [ ] Understood messaging integration architecture
- [ ] Saw Slack slash command demonstration
- [ ] Saw Discord bot demonstration
- [ ] Understood generic webhook triggering
- [ ] Learned about status notifications

---

## Module Summary

| Lesson | Topic | Time | Key Skill |
|--------|-------|------|-----------|
| 6.1 | Launching Cloud Agents | 15 min | Remote execution |
| 6.2 | Cloud Agent Artifacts | 15 min | Output collection |
| 6.3 | Messaging Integrations | 10 min | Chat-triggered agents |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│              CLOUD AGENTS QUICK REFERENCE                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  UI ACCESS:                                                 │
│  • Cursor Editor: View → Cloud Agents                       │
│  • Web: https://cursor.com/agents                           │
│                                                              │
│  LAUNCHING:                                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 1. Click "+ New"                                    │   │
│  │ 2. Select repo and branch                           │   │
│  │ 3. Write prompt                                     │   │
│  │ 4. Choose model                                     │   │
│  │ 5. Enable/disable auto-create PR                    │   │
│  │ 6. Click "Launch Agent"                             │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ARTIFACTS:                                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • View in agent detail page                         │   │
│  │ • Download single or all as zip                     │   │
│  │ • Access via API (expiring URLs)                    │   │
│  │ • Stored for 30 days                                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  MESSAGING INTEGRATIONS:                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ /cursor [prompt] in Slack                           │   │
│  │ !cursor [prompt] in Discord                         │   │
│  │ Webhook POST to trigger endpoint                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Transition to Module 7

> *"Now that you've mastered Cloud Agents in the UI, Module 7 will cover Model Configuration – selecting the right models, managing API keys, and optimizing cost vs. quality."*

---

*End of Module 6*