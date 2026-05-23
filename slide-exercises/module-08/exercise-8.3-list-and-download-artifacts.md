# Exercise 8.3: List and Download Artifacts

**Module 8:** Cloud Agents API and Webhooks  
**Slides:** `slides/module-08-marp.md` (Lesson 8.3)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Wait for completion, list artifacts, and download outputs.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

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



```python
def process_test_results(agent_id):
    wait_for_completion(agent_id, timeout=600)
    download_artifact(agent_id, "artifacts/junit.xml", "test_results.xml")
    # Parse XML → exit 1 if failures/errors, else exit 0
```

---

## Success criteria

- [ ] Listed artifacts · downloaded single + all · CI workflow integration

---

## Additional reference

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
