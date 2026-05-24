# Exercise 7.5: List Available Models

**Module 7:** Cursor API Foundations  
**Slides:** `slides/module-07-marp.md` (Lesson 7.5)  
**Time:** 10 min  
**Difficulty:** Beginner

**Objective:** Query available models and pick the right one programmatically.

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

**Step 1:** List with curl:
**Terminal:** **PowerShell** — ``Ctrl+` `` in Cursor

```bash
curl -s -u "$CURSOR_USER_API_KEY:" \
  https://api.cursor.com/v1/models \
  | jq '.data[] | {id: .id, context: .context_window, input_price: .pricing.input}'
```

---

**Step 2:** Format with Python tabulate — Model ID, Context, Input/Output Price, Vision support
**Terminal:** **PowerShell** — `python script.py`

---

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

**Step 3:** Filter models:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```python
# Models with 100k+ context
large_context = [m for m in models if m.get('context_window', 0) >= 100000]

# Cheapest by input price
cheapest = sorted(models, key=lambda x: x['pricing']['input'])[:5]
```

---

**Step 4:** Model selection helper:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```python
select_model("code_review", "balanced")  # → claude-4.6-sonnet
select_model("simple_fix", "low")        # → gpt-5-mini
select_model("frontend_ui", "high")      # → gemini-3.1-pro
```

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] API key from Exercise 1 (User API key works for Cloud Agents API)
- [ ] `curl` and `jq` installed

---

## Step-by-Step Instructions

### Step 1: List All Available Models (2 minutes)

**Command:**
```bash
curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/models" | jq '.'
```

**Expected response:**
```json
{
  "items": [
    "claude-4-sonnet-thinking",
    "gpt-5.2",
    "claude-4.5-sonnet-thinking",
    "composer-2.5",
    "gpt-5-mini",
    "claude-4.5-haiku",
    "gpt-5.3-codex",
    "claude-4.7-opus",
    "gemini-3.1-pro",
    "grok-4.3"
  ]
}
```

---

### Step 2: Format Output for Readability (1 minute)

**Count the models:**
```bash
curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/models" | jq '.items | length'
```

**List with line numbers:**
```bash
curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/models" | jq -r '.items[]' | nl
```

**Expected output:**
```
     1  claude-4-sonnet-thinking
     2  gpt-5.2
     3  claude-4.5-sonnet-thinking
     4  composer-2.5
     5  gpt-5-mini
     6  claude-4.5-haiku
     7  gpt-5.3-codex
     8  claude-4.7-opus
     9  gemini-3.1-pro
    10  grok-4.3
```

---

### Step 3: Filter Models by Pattern (1 minute)

**Find all Claude models:**
```bash
curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/models" | jq -r '.items[] | select(contains("claude"))'
```

**Expected output:**
```
claude-4-sonnet-thinking
claude-4.5-sonnet-thinking
claude-4.5-haiku
claude-4.7-opus
```

**Find all GPT models:**
```bash
curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/models" | jq -r '.items[] | select(contains("gpt"))'
```

**Expected output:**
```
gpt-5.2
gpt-5-mini
gpt-5.3-codex
```

---

### Step 4: Save Models to a File (1 minute)

```bash
curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/models" | jq -r '.items[]' > available_models.txt

cat available_models.txt
```

---

### Step 5: Create a Python Script to List Models (Optional)

**Create `list_models.py`:**
```python
#!/usr/bin/env python3
"""
List available Cursor AI models
"""

import requests
import os
import sys
from tabulate import tabulate

API_KEY = os.environ.get("CURSOR_USER_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_USER_API_KEY environment variable")
    sys.exit(1)

def get_models():
    """Fetch available models from Cloud Agents API"""
    url = "https://api.cursor.com/v1/models"
    auth = (API_KEY, "")
    
    response = requests.get(url, auth=auth)
    
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"❌ Error: {response.status_code}")
        return []

def categorize_models(models):
    """Categorize models by provider"""
    categories = {
        "Anthropic (Claude)": [],
        "OpenAI (GPT)": [],
        "Google (Gemini)": [],
        "xAI (Grok)": [],
        "Cursor (Composer)": [],
        "Other": []
    }
    
    for model in models:
        if "claude" in model.lower():
            categories["Anthropic (Claude)"].append(model)
        elif "gpt" in model.lower():
            categories["OpenAI (GPT)"].append(model)
        elif "gemini" in model.lower():
            categories["Google (Gemini)"].append(model)
        elif "grok" in model.lower():
            categories["xAI (Grok)"].append(model)
        elif "composer" in model.lower():
            categories["Cursor (Composer)"].append(model)
        else:
            categories["Other"].append(model)
    
    return categories

def main():
    print("🚀 Available Cursor AI Models")
    print("=" * 40)
    
    models = get_models()
    
    if not models:
        print("No models found or error occurred.")
        return
    
    print(f"\n📊 Total models: {len(models)}\n")
    
    # Categorize models
    categories = categorize_models(models)
    
    # Display by category
    for category, model_list in categories.items():
        if model_list:
            print(f"\n📁 {category}:")
            for model in model_list:
                print(f"   • {model}")
    
    # Display as table
    print("\n" + "=" * 40)
    print("📋 Model List (Table Format):")
    table_data = [[i+1, model] for i, model in enumerate(models)]
    print(tabulate(table_data, headers=["#", "Model ID"], tablefmt="simple"))

if __name__ == "__main__":
    main()
```

**Run the script:**
```bash
export CURSOR_USER_API_KEY="your_key_here"
pip install tabulate  # if needed
python3 list_models.py
```

---

## Expected Output

### Step 1 Output:
```json
{
  "items": [
    "claude-4-sonnet-thinking",
    "gpt-5.2",
    "claude-4.5-sonnet-thinking",
    "composer-2.5",
    "gpt-5-mini",
    "claude-4.5-haiku",
    "gpt-5.3-codex",
    "claude-4.7-opus",
    "gemini-3.1-pro",
    "grok-4.3"
  ]
}
```

### Step 2 Output:
```
     1  claude-4-sonnet-thinking
     2  gpt-5.2
     3  claude-4.5-sonnet-thinking
     4  composer-2.5
     5  gpt-5-mini
     6  claude-4.5-haiku
     7  gpt-5.3-codex
     8  claude-4.7-opus
     9  gemini-3.1-pro
    10  grok-4.3
```

---

## Success Criteria

- [ ] Successfully retrieved models list
- [ ] Counted total number of models
- [ ] Filtered models by provider (Claude, GPT, etc.)
- [ ] Saved models to file
- [ ] (Optional) Created Python script to display categorized models

---

## Model Reference

| Model ID | Provider | Best For |
|----------|----------|----------|
| `composer-2.5` | Cursor | Everyday coding (best value) |
| `gpt-5-mini` | OpenAI | Simple tasks, fast responses |
| `gpt-5.3-codex` | OpenAI | Coding specialized |
| `gpt-5.2` | OpenAI | General coding |
| `claude-4.5-haiku` | Anthropic | Fast, balanced |
| `claude-4.5-sonnet-thinking` | Anthropic | Balanced daily driver |
| `claude-4.7-opus` | Anthropic | Maximum quality |
| `gemini-3.1-pro` | Google | Image processing, frontend |
| `grok-4.3` | xAI | Fastest responses |

---

## Key Takeaways

| Concept | Value |
|---------|-------|
| **Endpoint** | `GET /v1/models` |
| **Authentication** | User API key (or any API key) |
| **Response format** | `{ "items": ["model1", "model2", ...] }` |
| **Use in agent creation** | Pass `model.id` in request body |
| **Default model** | Omit `model` field to use configured default |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 401 Unauthorized | Check API key is set correctly |
| Empty models list | Your plan may have limited models. Check subscription |
| `jq: command not found` | Install jq: `brew install jq` (Mac) or `apt-get install jq` (Linux) |
| Model not found when creating agent | Verify model ID exactly matches from this list |

---

## Bonus Challenge

Create a script that tests each model's response time:

```python
import requests
import time
import os

API_KEY = os.environ.get("CURSOR_USER_API_KEY")

def test_model_speed(model_id, prompt="Say 'Hello'"):
    """Test response speed of a model"""
    url = "https://api.cursor.com/v1/agents"
    auth = (API_KEY, "")
    
    payload = {
        "prompt": {"text": prompt},
        "model": {"id": model_id},
        "repos": [{"url": "https://github.com/your-org/your-repo"}]
    }
    
    start = time.time()
    response = requests.post(url, auth=auth, json=payload)
    elapsed = time.time() - start
    
    return elapsed

# Test a few models
models = ["gpt-5-mini", "composer-2.5", "grok-4.3"]
for model in models:
    try:
        duration = test_model_speed(model)
        print(f"{model}: {duration:.2f} seconds")
    except:
        print(f"{model}: Error")
```

---

## Exercise Complete ✓

Check off when done:
- [ ] Retrieved models list from API
- [ ] Counted total number of models
- [ ] Filtered models by provider
- [ ] Saved models to file
- [ ] (Bonus) Created categorized display script

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
