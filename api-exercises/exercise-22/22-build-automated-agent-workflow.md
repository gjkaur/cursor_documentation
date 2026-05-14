# API Exercise 22: Build Automated Agent Workflow

**Objective:** Build a complete automated workflow that launches Cloud Agents on a schedule, monitors their progress, and sends notifications upon completion.

**Time:** 10 minutes

**Difficulty:** Advanced

**Real-World Scenario:** Your team wants to run automated code reviews every night. Instead of manually launching agents, you'll build a scheduled workflow that triggers a Cloud Agent, monitors its progress, and sends Slack notifications when complete.

---

## Prerequisites

- [ ] User API key from Exercise 1
- [ ] Python 3.8+ installed
- [ ] `schedule` library (`pip install schedule`)
- [ ] Slack webhook URL (optional, for notifications)
- [ ] Completed Exercises 5-7 (agent creation, streaming, artifacts)

---

## Step-by-Step Instructions

### Step 1: Create the Automation Script (5 minutes)

**Create `automated_workflow.py`:**

```python
#!/usr/bin/env python3
"""
Automated Agent Workflow - Schedule, monitor, and notify
"""

import requests
import time
import os
import sys
import json
import schedule
from datetime import datetime
import threading

API_KEY = os.environ.get("CURSOR_USER_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_USER_API_KEY environment variable")
    sys.exit(1)

# Slack webhook (optional)
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")

class AutomatedWorkflow:
    """Automated Cloud Agent workflow"""
    
    def __init__(self):
        self.base_url = "https://api.cursor.com/v1"
        self.auth = (API_KEY, "")
        self.runs = {}
    
    def create_agent(self, repo_url, prompt, auto_create_pr=False, webhook_url=None):
        """Create a new Cloud Agent."""
        url = f"{self.base_url}/agents"
        
        payload = {
            "prompt": {"text": prompt},
            "repos": [{"url": repo_url}],
            "autoCreatePR": auto_create_pr
        }
        
        if webhook_url:
            payload["webhookUrl"] = webhook_url
        
        response = requests.post(url, auth=self.auth, json=payload)
        
        if response.status_code != 200:
            print(f"❌ Failed to create agent: {response.status_code}")
            print(f"   {response.text}")
            return None
        
        data = response.json()
        agent_id = data.get("agent", {}).get("id")
        run_id = data.get("run", {}).get("id")
        
        self.runs[run_id] = {
            "agent_id": agent_id,
            "status": "CREATING",
            "created_at": datetime.now().isoformat(),
            "repo": repo_url,
            "prompt": prompt
        }
        
        print(f"✅ Agent created: {agent_id}")
        print(f"   Run ID: {run_id}")
        print(f"   Dashboard: https://cursor.com/agents/{agent_id}")
        
        return agent_id, run_id
    
    def check_status(self, agent_id, run_id):
        """Check agent run status."""
        url = f"{self.base_url}/agents/{agent_id}/runs/{run_id}"
        
        response = requests.get(url, auth=self.auth)
        
        if response.status_code != 200:
            return None
        
        return response.json()
    
    def wait_for_completion(self, agent_id, run_id, timeout=600, interval=5):
        """Wait for agent to complete."""
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            data = self.check_status(agent_id, run_id)
            
            if data:
                status = data.get("status", "UNKNOWN")
                self.runs[run_id]["status"] = status
                
                if status == "FINISHED":
                    print(f"✅ Agent {agent_id} completed successfully!")
                    return True
                elif status == "ERROR":
                    print(f"❌ Agent {agent_id} failed!")
                    return False
                elif status == "CANCELLED":
                    print(f"🛑 Agent {agent_id} was cancelled!")
                    return False
            
            time.sleep(interval)
        
        print(f"⏰ Agent {agent_id} timed out after {timeout}s")
        return False
    
    def get_artifacts(self, agent_id):
        """Get artifacts from completed agent."""
        url = f"{self.base_url}/agents/{agent_id}/artifacts"
        
        response = requests.get(url, auth=self.auth)
        
        if response.status_code != 200:
            return []
        
        return response.json().get("items", [])
    
    def send_slack_notification(self, message, pr_url=None):
        """Send notification to Slack."""
        if not SLACK_WEBHOOK_URL:
            return
        
        text = message
        if pr_url:
            text += f"\n<{pr_url}|View Pull Request>"
        
        payload = {"text": text}
        
        try:
            requests.post(SLACK_WEBHOOK_URL, json=payload)
            print("   📢 Slack notification sent")
        except Exception as e:
            print(f"   ⚠️ Failed to send Slack notification: {e}")
    
    def run_workflow(self, repo_url, prompt, auto_create_pr=False):
        """Run complete workflow: create, monitor, notify."""
        print(f"\n🚀 Starting workflow at {datetime.now().isoformat()}")
        print(f"   Repository: {repo_url}")
        print(f"   Prompt: {prompt[:100]}...")
        
        # Create agent
        result = self.create_agent(repo_url, prompt, auto_create_pr)
        if not result:
            return False
        
        agent_id, run_id = result
        
        # Wait for completion
        success = self.wait_for_completion(agent_id, run_id)
        
        # Get artifacts
        artifacts = self.get_artifacts(agent_id)
        if artifacts:
            print(f"\n📎 Artifacts ({len(artifacts)}):")
            for artifact in artifacts:
                print(f"   - {artifact.get('path')} ({artifact.get('sizeBytes', 0)} bytes)")
        
        # Send notification
        if success:
            message = f"✅ Agent `{agent_id}` completed successfully!"
            self.send_slack_notification(message)
        else:
            message = f"❌ Agent `{agent_id}` failed!"
            self.send_slack_notification(message)
        
        return success
    
    def run_daily_code_review(self):
        """Daily code review task."""
        repo_url = os.environ.get("REPO_URL", "https://github.com/your-org/your-repo")
        prompt = """
        Review the codebase for:
        1. Potential bugs or edge cases
        2. Security vulnerabilities
        3. Code style issues
        4. Missing error handling
        
        Create a summary report in REVIEW.md
        """
        
        self.run_workflow(repo_url, prompt, auto_create_pr=True)
    
    def run_nightly_tests(self):
        """Nightly test runner task."""
        repo_url = os.environ.get("REPO_URL", "https://github.com/your-org/your-repo")
        prompt = """
        Run all tests and:
        1. Report any failures
        2. Suggest fixes for failing tests
        3. Update test coverage report
        
        Create a test report in TEST_REPORT.md
        """
        
        self.run_workflow(repo_url, prompt, auto_create_pr=True)
    
    def run_documentation_update(self):
        """Documentation update task."""
        repo_url = os.environ.get("REPO_URL", "https://github.com/your-org/your-repo")
        prompt = """
        Update documentation:
        1. Check for outdated API references
        2. Add examples for new features
        3. Update README with latest setup instructions
        """
        
        self.run_workflow(repo_url, prompt, auto_create_pr=True)

def run_once(workflow, task_name):
    """Run a task once."""
    print(f"\n{'='*50}")
    print(f"Running: {task_name}")
    print(f"{'='*50}")
    
    if task_name == "code_review":
        workflow.run_daily_code_review()
    elif task_name == "nightly_tests":
        workflow.run_nightly_tests()
    elif task_name == "docs":
        workflow.run_documentation_update()
    else:
        print(f"Unknown task: {task_name}")

def run_scheduled(workflow):
    """Run tasks on a schedule."""
    # Schedule daily code review at 6 AM
    schedule.every().day.at("06:00").do(workflow.run_daily_code_review)
    
    # Schedule nightly tests at 10 PM
    schedule.every().day.at("22:00").do(workflow.run_nightly_tests)
    
    # Schedule weekly documentation update on Sunday at 8 AM
    schedule.every().sunday.at("08:00").do(workflow.run_documentation_update)
    
    print("\n⏰ Scheduled tasks:")
    print("   - Daily code review: 6:00 AM")
    print("   - Nightly tests: 10:00 PM")
    print("   - Weekly documentation: Sunday 8:00 AM")
    print("\nWaiting for scheduled tasks... (Ctrl+C to exit)")
    
    while True:
        schedule.run_pending()
        time.sleep(60)

def main():
    print("🚀 Automated Agent Workflow")
    print("=" * 40)
    
    workflow = AutomatedWorkflow()
    
    print("\nOptions:")
    print("1. Run code review once")
    print("2. Run nightly tests once")
    print("3. Run documentation update once")
    print("4. Start scheduler (daily/weekly tasks)")
    
    choice = input("\nSelect option (1-4): ").strip()
    
    if choice == "1":
        run_once(workflow, "code_review")
    elif choice == "2":
        run_once(workflow, "nightly_tests")
    elif choice == "3":
        run_once(workflow, "docs")
    elif choice == "4":
        run_scheduled(workflow)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
```

---

### Step 2: Install Dependencies (1 minute)

**Command:**

```bash
pip install schedule requests
```

---

### Step 3: Configure Environment Variables (1 minute)

**Create `.env` file:**

```bash
export CURSOR_USER_API_KEY="your_api_key_here"
export REPO_URL="https://github.com/your-org/your-repo"
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/xxx/yyy/zzz"  # Optional
```

**Load environment:**

```bash
source .env
```

---

### Step 4: Run a One-Time Workflow (2 minutes)

**Command:**

```bash
python automated_workflow.py
# Select option 1, 2, or 3
```

**Expected output:**

```
🚀 Automated Agent Workflow
========================================

Options:
1. Run code review once
2. Run nightly tests once
3. Run documentation update once
4. Start scheduler (daily/weekly tasks)

Select option (1-4): 1

==================================================
Running: code_review
==================================================

🚀 Starting workflow at 2025-01-15T10:30:00.123456
   Repository: https://github.com/your-org/your-repo
   Prompt: Review the codebase for:
        1. Potential bugs or edge cases
        2. Security vulnerabilities...

✅ Agent created: bc_abc123
   Run ID: run_123456
   Dashboard: https://cursor.com/agents/bc_abc123

⏳ Waiting for agent to complete...
✅ Agent bc_abc123 completed successfully!

📎 Artifacts (1):
   - artifacts/REVIEW.md (2048 bytes)

   📢 Slack notification sent
```

---

### Step 5: Run the Scheduler (2 minutes)

Start the scheduler to run tasks automatically.

**Command:**

```bash
python automated_workflow.py
# Select option 4
```

**Expected output:**

```
⏰ Scheduled tasks:
   - Daily code review: 6:00 AM
   - Nightly tests: 10:00 PM
   - Weekly documentation: Sunday 8:00 AM

Waiting for scheduled tasks... (Ctrl+C to exit)
```

---

### Step 6: Create a GitHub Actions Workflow (Optional)

For CI/CD integration, create `.github/workflows/cursor-agent.yml`:

```yaml
name: Cursor Agent - Daily Code Review

on:
  schedule:
    - cron: '0 6 * * *'  # Daily at 6 AM UTC
  workflow_dispatch:  # Manual trigger

jobs:
  code-review:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install requests
      
      - name: Run Cursor Agent
        env:
          CURSOR_USER_API_KEY: ${{ secrets.CURSOR_USER_API_KEY }}
          REPO_URL: ${{ github.repositoryUrl }}
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
        run: |
          python automated_workflow.py <<< "1"
```

---

## Expected Output

### Step 4 Output (One-Time Run):

```
🚀 Automated Agent Workflow
========================================

Options:
1. Run code review once
2. Run nightly tests once
3. Run documentation update once
4. Start scheduler (daily/weekly tasks)

Select option (1-4): 1

==================================================
Running: code_review
==================================================

🚀 Starting workflow at 2025-01-15T10:30:00.123456
   Repository: https://github.com/your-org/your-repo
   Prompt: Review the codebase for:
        1. Potential bugs or edge cases
        2. Security vulnerabilities...

✅ Agent created: bc_abc123
   Run ID: run_123456
   Dashboard: https://cursor.com/agents/bc_abc123

⏳ Waiting for agent to complete...
   (Agent is working...)
   (Agent is working...)

✅ Agent bc_abc123 completed successfully!

📎 Artifacts (1):
   - artifacts/REVIEW.md (2048 bytes)

   📢 Slack notification sent
```

---

## Success Criteria

- [ ] Created automated workflow script
- [ ] Ran one-time code review
- [ ] Ran one-time test run
- [ ] Ran one-time documentation update
- [ ] Started scheduler (optional)
- [ ] Received Slack notification (if configured)
- [ ] Created GitHub Actions workflow (optional)

---

## Configuration Options

| Environment Variable | Description | Required |
|---------------------|-------------|----------|
| `CURSOR_USER_API_KEY` | Your Cursor API key | ✅ Yes |
| `REPO_URL` | GitHub repository URL | ✅ Yes |
| `SLACK_WEBHOOK_URL` | Slack webhook for notifications | ❌ No |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Agent creation fails | Check API key and repository URL |
| Timeout | Increase timeout value for large repos |
| No artifacts | Agent may not have produced any |
| Slack not working | Verify webhook URL and channel permissions |

---

## Key Takeaways

| Concept | Value |
|---------|-------|
| **Scheduled tasks** | Run agents automatically at set times |
| **Monitored execution** | Track progress and wait for completion |
| **Artifact collection** | Save outputs for later review |
| **Notifications** | Alert team when tasks complete |
| **CI/CD integration** | Run agents from GitHub Actions |

---

## Exercise Complete ✓

Check off when done:

- [ ] Created automated workflow script
- [ ] Ran one-time code review
- [ ] Ran one-time test run
- [ ] Ran one-time documentation update
- [ ] Started scheduler (optional)
- [ ] Received Slack notification (if configured)
