# Exercise 7.5: List Available Models

**Module 7:** Cursor API Foundations  
**Slides:** `slides/module-07-marp.md` (Lesson 7.5)  
**Time:** 10 min  
**Difficulty:** Beginner

**Objective:** Query available models and pick the right one programmatically.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

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

## Additional reference

## Expected Output

### Step 1 Output:
```json
{
  "items": [
    "claude-4-sonnet-thinking",
    "gpt-5.2",
    "claude-4.5-sonnet-thinking",
    "composer-2",
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
     4  composer-2
     5  gpt-5-mini
     6  claude-4.5-haiku
     7  gpt-5.3-codex
     8  claude-4.7-opus
     9  gemini-3.1-pro
    10  grok-4.3
```

---

## Model Reference

| Model ID | Provider | Best For |
|----------|----------|----------|
| `composer-2` | Cursor | Everyday coding (best value) |
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
models = ["gpt-5-mini", "composer-2", "grok-4.3"]
for model in models:
    try:
        duration = test_model_speed(model)
        print(f"{model}: {duration:.2f} seconds")
    except:
        print(f"{model}: Error")
```

---
