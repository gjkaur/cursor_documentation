# Exercise 8.3: List and Download Artifacts

**Module 8:** Cloud Agents API and Webhooks  
**Slides:** `slides/module-08-marp.md` (Lesson 8.3)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Wait for completion, list artifacts, and download outputs.

---

## API basics (read this first)

**Demonstration (Windows):** Use **PowerShell** in Cursor's terminal (``Ctrl+` ``).

1. Store keys in environment variables — never commit them:

```powershell
$env:CURSOR_ADMIN_API_KEY = "crsr_your_key_here"
$env:CURSOR_USER_API_KEY = "cursor_user_your_key_here"
```

2. Use **`curl.exe`** (not the `curl` alias) or Python `requests`.
3. Install **jq** for JSON parsing: `winget install jqlang.jq` or use Python instead.
4. Bash `curl` examples below each have a **PowerShell** equivalent — use those on Windows.
5. Run scripts from a dedicated folder inside this repo or your own sandbox project.


---

## Steps from the training slides

**Demonstration (Windows):** Follow steps in **PowerShell** unless a step says otherwise. Agent panel: ``Ctrl+I`` · Terminal: ``Ctrl+` ``.

Follow these steps in order. Copy prompts exactly unless the exercise tells you to adapt them.

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```python
def wait_for_completion(agent_id, timeout=300, poll_interval=5):
    while time.time() - start < timeout:
        status = get_agent_status(agent_id).get('status')
        if status == 'FINISHED': return True
        elif status == 'ERROR': return False
        time.sleep(poll_interval)

def list_artifacts(agent_id):
    response = requests.get(f"{BASE_URL}/agents/{agent_id}/artifacts", auth=AUTH)
    return response.json().get('items', [])
```

---

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

**Single artifact:**

```python
response = requests.get(
    f"{BASE_URL}/agents/{agent_id}/artifacts/download",
    auth=AUTH, params={"path": artifact_path}
)
download_url = response.json().get('url')
# curl download_url → save to disk
```

**All artifacts:** loop items, create subdirs, download each via presigned URL

---

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```python
def process_test_results(agent_id):
    wait_for_completion(agent_id, timeout=600)
    download_artifact(agent_id, "artifacts/junit.xml", "test_results.xml")
    # Parse XML → exit 1 if failures/errors, else exit 0
```

**Success Criteria:** Listed artifacts · downloaded single + all · CI workflow integration

---

## Success criteria

- [ ] Listed artifacts · downloaded single + all · CI workflow integration

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] API key from Exercise 1 (User API key works)
- [ ] Completed Exercise 5 (have an agent ID with completed run)
- [ ] Python 3.8+ installed

---

## Step-by-Step Instructions

### Step 1: Create an Agent That Produces Artifacts (3 minutes)

First, create an agent that will produce artifacts (screenshots, logs).

**Command:**
```bash
RESPONSE=$(curl -s -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {
      "text": "Take a screenshot of the repository structure and create a log of files found"
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
echo "Agent ID: $AGENT_ID"
echo "Wait for agent to complete (check dashboard)..."
```

**Wait for completion:** Check `cursor.com/agents` until status shows "FINISHED".

---

### Step 2: List Artifacts (3 minutes)

Once the agent is complete, list all artifacts it produced.

**Command:**
```bash
curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts" | jq '.'
```

**Expected response:**
```json
{
  "items": [
    {
      "path": "artifacts/screenshot.png",
      "sizeBytes": 12345,
      "updatedAt": "2025-01-15T10:35:00.000Z"
    },
    {
      "path": "artifacts/scan_log.txt",
      "sizeBytes": 4096,
      "updatedAt": "2025-01-15T10:35:00.000Z"
    },
    {
      "path": "artifacts/file_list.json",
      "sizeBytes": 2048,
      "updatedAt": "2025-01-15T10:35:00.000Z"
    }
  ]
}
```

---

### Step 3: Download a Single Artifact (2 minutes)

Get a presigned URL and download an artifact.

**Command:**
```bash
# Get download URL for screenshot
DOWNLOAD_URL=$(curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts/download?path=artifacts/screenshot.png" \
  | jq -r '.url')

echo "Download URL: $DOWNLOAD_URL"

# Download the file
curl -L -o screenshot.png "$DOWNLOAD_URL"
echo "Downloaded: screenshot.png"
```

**Expected response:**
```json
{
  "url": "https://cloud-agent-artifacts.s3.us-east-1.amazonaws.com/...",
  "expiresAt": "2025-01-15T11:00:00.000Z"
}
```

---

### Step 4: Download All Artifacts (3 minutes)

Loop through all artifacts and download them.

**Command:**
```bash
# Get all artifact paths
ARTIFACT_PATHS=$(curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts" \
  | jq -r '.items[].path')

# Create output directory
mkdir -p agent_artifacts

# Download each artifact
for path in $ARTIFACT_PATHS; do
  filename=$(basename "$path")
  echo "Downloading: $filename"
  
  DOWNLOAD_URL=$(curl -s -u "$CURSOR_USER_API_KEY:" \
    "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts/download?path=$path" \
    | jq -r '.url')
  
  curl -L -s -o "agent_artifacts/$filename" "$DOWNLOAD_URL"
  echo "  Saved to: agent_artifacts/$filename"
done

echo "✅ All artifacts downloaded to agent_artifacts/"
ls -la agent_artifacts/
```

---

### Step 5: Create a Python Script for Artifact Management (4 minutes)

**Create `artifact_manager.py`:**
```python
#!/usr/bin/env python3
"""
Download and manage Cloud Agent artifacts
"""

import requests
import os
import sys
import json
import time
from pathlib import Path

API_KEY = os.environ.get("CURSOR_USER_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_USER_API_KEY environment variable")
    sys.exit(1)

class ArtifactManager:
    """Manage Cloud Agent artifacts"""
    
    def __init__(self, agent_id, output_dir="artifacts"):
        self.agent_id = agent_id
        self.base_url = "https://api.cursor.com/v1"
        self.auth = (API_KEY, "")
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def list_artifacts(self):
        """List all artifacts for the agent."""
        url = f"{self.base_url}/agents/{self.agent_id}/artifacts"
        
        response = requests.get(url, auth=self.auth)
        
        if response.status_code != 200:
            print(f"❌ Error listing artifacts: {response.status_code}")
            return []
        
        return response.json().get("items", [])
    
    def get_download_url(self, artifact_path):
        """Get presigned download URL for an artifact."""
        url = f"{self.base_url}/agents/{self.agent_id}/artifacts/download"
        params = {"path": artifact_path}
        
        response = requests.get(url, auth=self.auth, params=params)
        
        if response.status_code != 200:
            print(f"❌ Error getting URL for {artifact_path}: {response.status_code}")
            return None
        
        return response.json().get("url")
    
    def download_artifact(self, artifact_path):
        """Download a single artifact."""
        download_url = self.get_download_url(artifact_path)
        
        if not download_url:
            return None
        
        # Extract filename from path
        filename = Path(artifact_path).name
        output_path = self.output_dir / filename
        
        # Download file
        response = requests.get(download_url, stream=True)
        
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return output_path
        
        return None
    
    def download_all_artifacts(self):
        """Download all artifacts for the agent."""
        artifacts = self.list_artifacts()
        
        if not artifacts:
            print("No artifacts found.")
            return []
        
        print(f"Found {len(artifacts)} artifact(s)")
        print("-" * 40)
        
        downloaded = []
        for artifact in artifacts:
            path = artifact.get("path")
            size = artifact.get("sizeBytes", 0)
            size_kb = size / 1024
            
            print(f"📎 {path} ({size_kb:.1f} KB)")
            
            output_path = self.download_artifact(path)
            if output_path:
                downloaded.append(output_path)
                print(f"   ✅ Downloaded to: {output_path}")
            else:
                print(f"   ❌ Download failed")
        
        return downloaded
    
    def get_artifact_summary(self):
        """Get summary of artifacts (sizes, types)."""
        artifacts = self.list_artifacts()
        
        if not artifacts:
            return
        
        total_size = 0
        types = {}
        
        for artifact in artifacts:
            path = artifact.get("path")
            size = artifact.get("sizeBytes", 0)
            total_size += size
            
            # Get file extension
            ext = Path(path).suffix or "no_extension"
            types[ext] = types.get(ext, 0) + 1
        
        print("\n📊 Artifact Summary")
        print("=" * 40)
        print(f"Total artifacts: {len(artifacts)}")
        print(f"Total size: {total_size / 1024:.1f} KB")
        print(f"File types:")
        for ext, count in types.items():
            print(f"  • {ext}: {count} file(s)")

def wait_for_agent_completion(agent_id, timeout=300, interval=5):
    """Wait for an agent to complete."""
    url = f"https://api.cursor.com/v1/agents/{agent_id}"
    auth = (API_KEY, "")
    
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        response = requests.get(url, auth=auth)
        
        if response.status_code == 200:
            data = response.json()
            status = data.get("status")
            print(f"⏳ Agent status: {status}")
            
            if status == "FINISHED":
                print("✅ Agent completed!")
                return True
            elif status == "ERROR":
                print("❌ Agent failed!")
                return False
        
        time.sleep(interval)
    
    print("⏰ Timeout waiting for agent completion")
    return False

def create_agent_with_artifacts(repo_url, prompt):
    """Create an agent that will produce artifacts."""
    url = "https://api.cursor.com/v1/agents"
    auth = (API_KEY, "")
    
    payload = {
        "prompt": {"text": prompt},
        "repos": [{"url": repo_url}],
        "autoCreatePR": False
    }
    
    response = requests.post(url, auth=auth, json=payload)
    
    if response.status_code != 200:
        print(f"❌ Failed to create agent: {response.status_code}")
        return None
    
    data = response.json()
    agent_id = data.get("agent", {}).get("id")
    print(f"✅ Agent created: {agent_id}")
    print(f"   Dashboard: https://cursor.com/agents/{agent_id}")
    
    return agent_id

def main():
    print("🚀 Cloud Agent Artifact Manager")
    print("=" * 40)
    
    # Option 1: Use existing agent
    agent_id = input("\n📝 Enter Agent ID (or press Enter to create new): ").strip()
    
    if not agent_id:
        repo_url = input("📝 Enter GitHub repository URL: ").strip()
        prompt = input("📝 Enter task prompt: ").strip()
        
        if not repo_url or not prompt:
            print("❌ Repository URL and prompt are required")
            return
        
        agent_id = create_agent_with_artifacts(repo_url, prompt)
        
        if not agent_id:
            return
        
        print("\n⏳ Waiting for agent to complete...")
        if not wait_for_agent_completion(agent_id):
            print("Agent did not complete successfully")
            return
    
    # Manage artifacts
    manager = ArtifactManager(agent_id)
    
    # Show summary
    manager.get_artifact_summary()
    
    # Download all artifacts
    print("\n📥 Downloading artifacts...")
    downloaded = manager.download_all_artifacts()
    
    print(f"\n✅ Downloaded {len(downloaded)} files to {manager.output_dir}/")

if __name__ == "__main__":
    main()
```

**Run the script:**
```bash
export CURSOR_USER_API_KEY="your_key_here"
python3 artifact_manager.py
```

---

### Step 6: Download Artifacts from Completed Agent (2 minutes)

If you already have a completed agent ID, use this one-liner:

```bash
# Replace with your agent ID
AGENT_ID="bc-00000000-0000-0000-0000-000000000001"

# Download all artifacts
curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts" | \
  jq -r '.items[].path' | while read path; do
    filename=$(basename "$path")
    url=$(curl -s -u "$CURSOR_USER_API_KEY:" \
      "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts/download?path=$path" \
      | jq -r '.url')
    curl -L -o "$filename" "$url"
    echo "Downloaded: $filename"
done
```

---

## Expected Output

### Step 2 Output (List Artifacts):
```json
{
  "items": [
    {
      "path": "artifacts/screenshot.png",
      "sizeBytes": 12345,
      "updatedAt": "2025-01-15T10:35:00.000Z"
    },
    {
      "path": "artifacts/build_log.txt",
      "sizeBytes": 4096,
      "updatedAt": "2025-01-15T10:35:00.000Z"
    }
  ]
}
```

### Step 5 Output (Python Script):
```
🚀 Cloud Agent Artifact Manager
========================================

📝 Enter Agent ID (or press Enter to create new): bc-00000000-0000-0000-0000-000000000001

📊 Artifact Summary
========================================
Total artifacts: 3
Total size: 18.5 KB
File types:
  • .png: 1 file(s)
  • .txt: 1 file(s)
  • .json: 1 file(s)

📥 Downloading artifacts...
Found 3 artifact(s)
----------------------------------------
📎 artifacts/screenshot.png (12.1 KB)
   ✅ Downloaded to: artifacts/screenshot.png
📎 artifacts/build_log.txt (4.0 KB)
   ✅ Downloaded to: artifacts/build_log.txt
📎 artifacts/file_list.json (2.0 KB)
   ✅ Downloaded to: artifacts/file_list.json

✅ Downloaded 3 files to artifacts/
```

---

## Success Criteria

- [ ] Listed artifacts from a completed agent
- [ ] Retrieved presigned download URL
- [ ] Downloaded individual artifact
- [ ] Downloaded all artifacts in a loop
- [ ] Created Python artifact manager
- [ ] Saved artifacts to local directory

---

## Artifact Types Reference

| Artifact Type | File Extension | Description |
|---------------|----------------|-------------|
| Screenshot | `.png` | Visual capture of browser state |
| Log file | `.txt`, `.log` | Agent execution logs |
| Generated code | `.c`, `.py`, `.js`, etc. | Files created by agent |
| Configuration | `.json`, `.yaml`, `.toml` | Config files generated |
| Test results | `.xml`, `.json` | Test output |
| Build artifacts | `.bin`, `.hex`, `.elf` | Compiled outputs |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No artifacts found | Agent may not have produced any. Run agent with browser or file operations |
| Download URL expired | URLs expire after 15 minutes. Generate new URL |
| 404 Not Found | Agent ID may be incorrect or agent may be archived |
| Permission denied | Check file write permissions in output directory |
| Empty artifact list | Agent may still be running. Wait for completion |

---

## Key Takeaways

| Concept | Value |
|---------|-------|
| **List endpoint** | `GET /v1/agents/{id}/artifacts` |
| **Download endpoint** | `GET /v1/agents/{id}/artifacts/download?path=...` |
| **URL expiration** | 15 minutes (presigned S3 URL) |
| **Path format** | Relative (e.g., `artifacts/screenshot.png`) |
| **Artifact scope** | Agent-scoped (persists across runs) |

---

## Bonus Challenge

Create a script that:

1. **Downloads artifacts and uploads to S3** for permanent storage
2. **Generates a report** of all artifacts with previews
3. **Compares artifacts** between two agents

```python
def compare_artifacts(agent_id_1, agent_id_2):
    """Compare artifacts between two agents"""
    manager1 = ArtifactManager(agent_id_1)
    manager2 = ArtifactManager(agent_id_2)
    
    artifacts1 = {a['path']: a['sizeBytes'] for a in manager1.list_artifacts()}
    artifacts2 = {a['path']: a['sizeBytes'] for a in manager2.list_artifacts()}
    
    only_in_1 = set(artifacts1.keys()) - set(artifacts2.keys())
    only_in_2 = set(artifacts2.keys()) - set(artifacts1.keys())
    common = set(artifacts1.keys()) & set(artifacts2.keys())
    
    print(f"Common artifacts: {len(common)}")
    print(f"Only in agent 1: {len(only_in_1)}")
    print(f"Only in agent 2: {len(only_in_2)}")
```

---

## Exercise Complete ✓

Check off when done:
- [ ] Listed artifacts from completed agent
- [ ] Downloaded single artifact
- [ ] Downloaded all artifacts
- [ ] Created Python artifact manager
- [ ] Understood 15-minute URL expiration
- [ ] (Bonus) Compared artifacts between agents

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
