# Exercise 8.2: Stream Agent Responses (SSE)

**Module 8:** Cloud Agents API and Webhooks  
**Slides:** `slides/module-08-marp.md` (Lesson 8.2)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Stream Cloud Agent events with Server-Sent Events.

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

**Terminal:** **PowerShell**

```powershell
curl.exe -N -u "$($env:CURSOR_USER_API_KEY):" `
  -H "Accept: text/event-stream" `
  "https://api.cursor.com/v1/agents/$env:AGENT_ID/runs/$env:RUN_ID/stream"
```

Set IDs first: `$env:AGENT_ID = "..."` · `$env:RUN_ID = "..."`

**Terminal (alternative):** **Git Bash** / **WSL** — bash `curl -N` block above.

Parse lines starting with `event:` and `data:` — print assistant text, tool calls, and result status.

---

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```python
def stream_agent_response(agent_id, run_id, on_event=None):
    url = f"{BASE_URL}/agents/{agent_id}/runs/{run_id}/stream"
    response = requests.get(url, auth=AUTH, stream=True)
    for line in response.iter_lines():
        if line.startswith(b'event:'):
            current_event = line[6:].strip().decode()
        elif line.startswith(b'data:'):
            data = json.loads(line[5:].strip())
            if on_event:
                on_event(current_event, data)
```

---

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

Track `last_event_id` from `id:` lines → send as `Last-Event-ID` header on reconnect

**Also:** `stream_to_file()` saves full SSE log for later review

**Success Criteria:** Stream connected · received events · Python client works · resume implemented

---

## Success criteria

- [ ] Stream connected · received events · Python client works · resume implemented

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] API key from Exercise 1 (User API key works)
- [ ] Completed Exercise 5 (have an agent ID and run ID)
- [ ] Python 3.8+ installed

---

## Step-by-Step Instructions

### Step 1: Create an Agent and Capture IDs (2 minutes)

First, create an agent that will do something observable (like reading files).

**Command:**
```bash
RESPONSE=$(curl -s -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {
      "text": "Read the main source file and explain what it does"
    },
    "repos": [
      {
        "url": "https://github.com/YOUR_ORG/YOUR_REPO",
        "startingRef": "main"
      }
    ],
    "autoCreatePR": false
  }')

AGENT_ID=$(echo "$RESPONSE" | jq -r '.agent.id')
RUN_ID=$(echo "$RESPONSE" | jq -r '.run.id')

echo "Agent ID: $AGENT_ID"
echo "Run ID: $RUN_ID"
```

---

### Step 2: Stream Using curl (3 minutes)

Stream the agent's output directly in your terminal.

**Command:**
```bash
curl -N -u "$CURSOR_USER_API_KEY:" \
  -H "Accept: text/event-stream" \
  "https://api.cursor.com/v1/agents/$AGENT_ID/runs/$RUN_ID/stream"
```

**Expected output (SSE format):**
```
event: status
data: {"runId":"run-...","status":"RUNNING"}

id: 1713033000000-0
event: assistant
data: {"text":"I'll read the main source file to understand the codebase."}

id: 1713033010000-0
event: tool_call
data: {"callId":"call_123","name":"read_file","status":"started","args":{"path":"src/main.c"}}

id: 1713033020000-0
event: tool_call
data: {"callId":"call_123","name":"read_file","status":"completed","result":{"content":"#include <stdio.h>..."}}

id: 1713033030000-0
event: assistant
data: {"text":"The main file contains a calculator program with functions for add, subtract, multiply, and divide."}

id: 1713033040000-0
event: result
data: {"runId":"run-...","status":"FINISHED"}

id: 1713033040000-0
event: done
data: {}
```

---

### Step 3: Parse Different Event Types (3 minutes)

Understanding the event types helps you build better monitoring.

| Event Type | When It Happens | What You Get |
|------------|-----------------|--------------|
| `status` | Run status changes | `{runId, status}` (CREATING, RUNNING, FINISHED, ERROR) |
| `assistant` | Agent speaks | `{text}` – the agent's response |
| `thinking` | Agent is reasoning | `{text}` – internal thought process |
| `tool_call` | Agent uses a tool | `{callId, name, status, args, result}` |
| `heartbeat` | Keep-alive | Empty (connection still alive) |
| `result` | Run completes | `{runId, status}` (FINISHED or ERROR) |
| `error` | Something went wrong | `{code, message}` |
| `done` | Stream ends | `{}` |

---

### Step 4: Create a Python Streaming Client (5 minutes)

**Create `stream_agent.py`:**
```python
#!/usr/bin/env python3
"""
Stream Cloud Agent responses in real-time
"""

import requests
import json
import os
import sys
import time

API_KEY = os.environ.get("CURSOR_USER_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_USER_API_KEY environment variable")
    sys.exit(1)

def stream_agent_run(agent_id, run_id):
    """
    Stream a Cloud Agent run in real-time.
    
    Args:
        agent_id: The agent ID (e.g., bc-xxx)
        run_id: The run ID (e.g., run-xxx)
    """
    url = f"https://api.cursor.com/v1/agents/{agent_id}/runs/{run_id}/stream"
    auth = (API_KEY, "")
    headers = {"Accept": "text/event-stream"}
    
    print(f"\n📡 Streaming agent: {agent_id}")
    print(f"🔗 Dashboard: https://cursor.com/agents/{agent_id}")
    print("-" * 50)
    
    response = requests.get(url, auth=auth, headers=headers, stream=True)
    
    current_event = None
    
    for line in response.iter_lines():
        if not line:
            continue
        
        line = line.decode('utf-8')
        
        if line.startswith('event:'):
            current_event = line[6:].strip()
        
        elif line.startswith('data:'):
            try:
                data = json.loads(line[5:])
                
                if current_event == 'status':
                    print(f"\n📊 STATUS: {data.get('status', 'unknown')}")
                
                elif current_event == 'assistant':
                    text = data.get('text', '')
                    if text:
                        print(f"\n🤖 ASSISTANT: {text}")
                
                elif current_event == 'thinking':
                    text = data.get('text', '')
                    if text:
                        print(f"\n💭 THINKING: {text}")
                
                elif current_event == 'tool_call':
                    tool_name = data.get('name', 'unknown')
                    tool_status = data.get('status', 'unknown')
                    
                    if tool_status == 'started':
                        print(f"\n🔧 TOOL STARTED: {tool_name}")
                        # Show arguments if present
                        args = data.get('args', {})
                        if args:
                            print(f"   Args: {json.dumps(args, indent=2)[:200]}")
                    
                    elif tool_status == 'completed':
                        print(f"\n✅ TOOL COMPLETED: {tool_name}")
                        # Show result summary
                        result = data.get('result', {})
                        if result and 'content' in result:
                            content = result['content'][:200]
                            print(f"   Result: {content}...")
                    
                    elif tool_status == 'failed':
                        print(f"\n❌ TOOL FAILED: {tool_name}")
                        error = data.get('error', 'Unknown error')
                        print(f"   Error: {error}")
                
                elif current_event == 'result':
                    print(f"\n🏁 RESULT: {data.get('status', 'unknown')}")
                    print("-" * 50)
                
                elif current_event == 'error':
                    print(f"\n💥 ERROR: {data.get('code', 'unknown')} - {data.get('message', '')}")
                
                elif current_event == 'done':
                    print("\n✅ Stream complete")
                
                elif current_event == 'heartbeat':
                    # Silent – just keep connection alive
                    pass
                
                else:
                    print(f"\n⚠️ Unknown event: {current_event}")
                    print(f"   Data: {json.dumps(data, indent=2)[:200]}")
            
            except json.JSONDecodeError:
                print(f"\n⚠️ Could not parse: {line[5:][:100]}")

def stream_with_resume(agent_id, run_id):
    """
    Stream with resume capability (handles disconnections).
    """
    url = f"https://api.cursor.com/v1/agents/{agent_id}/runs/{run_id}/stream"
    auth = (API_KEY, "")
    headers = {"Accept": "text/event-stream"}
    
    last_event_id = None
    
    while True:
        # Add Last-Event-ID header if we have one
        if last_event_id:
            headers["Last-Event-ID"] = last_event_id
        
        response = requests.get(url, auth=auth, headers=headers, stream=True)
        
        for line in response.iter_lines():
            if not line:
                continue
            
            line = line.decode('utf-8')
            
            # Capture event ID for resume
            if line.startswith('id:'):
                last_event_id = line[3:].strip()
                print(f"📌 Checkpoint: {last_event_id}")
            
            elif line.startswith('event:'):
                current_event = line[6:].strip()
            
            elif line.startswith('data:'):
                data = json.loads(line[5:])
                
                if current_event == 'result':
                    print(f"\n🏁 Final status: {data.get('status')}")
                    return  # Exit after completion
                
                elif current_event == 'error':
                    print(f"\n💥 Error: {data.get('message')}")
                    return
                
                elif current_event == 'done':
                    print("\n✅ Stream complete")
                    return
                
                # Process other events normally
                elif current_event == 'assistant':
                    text = data.get('text', '')
                    if text:
                        print(f"🤖 {text}")

def main():
    print("🚀 Cloud Agent Stream Viewer")
    print("=" * 40)
    
    # Get agent and run IDs from user or environment
    agent_id = input("\n📝 Enter Agent ID (or press Enter for demo): ").strip()
    run_id = input("📝 Enter Run ID: ").strip()
    
    if not agent_id or not run_id:
        print("\n❌ Please provide both Agent ID and Run ID")
        print("   Run Exercise 5 first to get these IDs")
        return
    
    print("\n🎬 Starting stream...\n")
    stream_agent_run(agent_id, run_id)

if __name__ == "__main__":
    main()
```

**Run the script:**
```bash
export CURSOR_USER_API_KEY="your_key_here"
python3 stream_agent.py
```

---

### Step 5: Handle Stream Disconnections with Resume (2 minutes)

The `stream_with_resume` function in the script above shows how to resume a stream after disconnection using the `Last-Event-ID` header.

**Key concept:** SSE events include an `id` field. If your connection drops, you can resume from the last received event ID.

**Example resume header:**
```bash
curl -N -u "$CURSOR_USER_API_KEY:" \
  -H "Accept: text/event-stream" \
  -H "Last-Event-ID: 1713033020000-0" \
  "https://api.cursor.com/v1/agents/$AGENT_ID/runs/$RUN_ID/stream"
```

---

## Expected Output

### Step 2 Output (Raw SSE):
```
event: status
data: {"runId":"run-...","status":"RUNNING"}

id: 1713033000000-0
event: assistant
data: {"text":"I'll read the main source file to understand the codebase."}

id: 1713033010000-0
event: tool_call
data: {"callId":"call_123","name":"read_file","status":"started","args":{"path":"src/main.c"}}

id: 1713033020000-0
event: tool_call
data: {"callId":"call_123","name":"read_file","status":"completed","result":{"content":"..."}}

id: 1713033040000-0
event: result
data: {"runId":"run-...","status":"FINISHED"}

id: 1713033040000-0
event: done
data: {}
```

### Step 4 Output (Python Formatted):
```
🚀 Cloud Agent Stream Viewer
========================================

📝 Enter Agent ID: bc-00000000-0000-0000-0000-000000000001
📝 Enter Run ID: run-00000000-0000-0000-0000-000000000001

🎬 Starting stream...

📊 STATUS: RUNNING

🤖 ASSISTANT: I'll read the main source file to understand the codebase.

🔧 TOOL STARTED: read_file
   Args: {"path": "src/main.c"}

✅ TOOL COMPLETED: read_file
   Result: #include <stdio.h>...

🤖 ASSISTANT: The main file contains a calculator program with functions for add, subtract, multiply, and divide.

🏁 RESULT: FINISHED
--------------------------------------------------

✅ Stream complete
```

---

## Success Criteria

- [ ] Created an agent and captured agent ID/run ID
- [ ] Streamed agent output using curl
- [ ] Identified different event types (status, assistant, tool_call, result)
- [ ] Created Python streaming client
- [ ] Handled tool call started/completed events
- [ ] (Optional) Implemented resume with Last-Event-ID

---

## Event Processing Cheat Sheet

| Event | When | Action |
|-------|------|--------|
| `status` | Run state changes | Update UI status indicator |
| `assistant` | Agent speaks | Display response text |
| `thinking` | Agent reasons | Show thinking process (optional) |
| `tool_call` (started) | Tool begins | Show "Reading file..." |
| `tool_call` (completed) | Tool finishes | Show result summary |
| `result` | Run ends | Show final status |
| `error` | Error occurs | Log error, notify user |
| `done` | Stream ends | Close connection |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No output from curl | Use `-N` flag to disable buffering |
| Connection drops | Implement resume with `Last-Event-ID` |
| Events not parsing | Check JSON format; some events have different structures |
| Tool call without result | Tool may be long-running; wait for completed event |
| `heartbeat` events | Normal – keep connection alive, can ignore |

---

## Key Takeaways

| Concept | Value |
|---------|-------|
| **Endpoint** | `GET /v1/agents/{id}/runs/{runId}/stream` |
| **Format** | Server-Sent Events (SSE) |
| **Event types** | status, assistant, thinking, tool_call, result, error, done |
| **Resume** | Use `Last-Event-ID` header |
| **Retention** | Check `X-Cursor-Stream-Retention-Seconds` header |
| **Buffer** | Use `-N` flag with curl to disable buffering |

---

## Bonus Challenge

Create a real-time dashboard that shows agent progress:

```python
import tkinter as tk
from tkinter import scrolledtext
import threading
import requests
import json

API_KEY = os.environ.get("CURSOR_USER_API_KEY")

class AgentMonitor:
    def __init__(self, agent_id, run_id):
        self.agent_id = agent_id
        self.run_id = run_id
        self.root = tk.Tk()
        self.root.title(f"Agent Monitor - {agent_id}")
        
        self.text_area = scrolledtext.ScrolledText(self.root, width=80, height=30)
        self.text_area.pack()
        
        self.status_label = tk.Label(self.root, text="Connecting...")
        self.status_label.pack()
        
    def log(self, message, color="black"):
        self.text_area.insert(tk.END, message + "\n", color)
        self.text_area.see(tk.END)
        self.text_area.tag_config("error", foreground="red")
        self.text_area.tag_config("success", foreground="green")
        self.text_area.tag_config("info", foreground="blue")
    
    def stream(self):
        url = f"https://api.cursor.com/v1/agents/{self.agent_id}/runs/{self.run_id}/stream"
        auth = (API_KEY, "")
        
        response = requests.get(url, auth=auth, stream=True)
        
        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if 'assistant' in line:
                    self.log(f"🤖 {line}", "info")
                elif 'error' in line:
                    self.log(f"❌ {line}", "error")
                elif 'result' in line and 'FINISHED' in line:
                    self.log(f"✅ Agent completed!", "success")
    
    def run(self):
        thread = threading.Thread(target=self.stream)
        thread.daemon = True
        thread.start()
        self.root.mainloop()
```

---

## Exercise Complete ✓

Check off when done:
- [ ] Streamed agent output using curl
- [ ] Identified all event types
- [ ] Created Python streaming client
- [ ] Parsed tool call arguments and results
- [ ] Handled stream completion
- [ ] (Bonus) Implemented resume capability
- [ ] (Bonus) Created real-time dashboard

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
