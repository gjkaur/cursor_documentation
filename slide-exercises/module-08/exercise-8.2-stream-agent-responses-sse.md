# Exercise 8.2: Stream Agent Responses (SSE)

**Module 8:** Cloud Agents API and Webhooks  
**Slides:** `slides/module-08-marp.md` (Lesson 8.2)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Stream Cloud Agent events with Server-Sent Events.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

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

---

## Success criteria

- [ ] Stream connected · received events · Python client works · resume implemented

---

## Additional reference

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
