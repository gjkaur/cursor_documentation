# Exercise 7.3: Rate Limits and Error Handling

**Module 7:** Cursor API Foundations  
**Slides:** `slides/module-07-marp.md` (Lesson 7.3)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Handle 429 responses with backoff and rate-limit headers.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```python
def call_with_retry(url, max_retries=5, base_delay=1.0):
    for attempt in range(max_retries):
        response = requests.get(url, auth=AUTH)
        if response.status_code == 200:
            return response.json()
        if 400 <= response.status_code < 500:
            return None  # Don't retry client errors
        if response.status_code in [429, 500, 502, 503, 504]:
            delay = int(response.headers.get('Retry-After',
                      min(base_delay * (2 ** attempt), 60)))
            time.sleep(delay)
    return None
```

---

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**Monitor headers:** warn when `X-RateLimit-Remaining` < 10% of limit

**Token bucket rate limiter:** space requests evenly across the minute window

**CursorAPIClient:** combines rate limiting, retries on 429/5xx, timeout handling, and typed methods like `get_models()` and `create_agent()`

---

## Success criteria

- [ ] Backoff · header monitoring · rate limiter · robust client class

---

## Additional reference

## Expected Output

### Step 3 Output (Exponential Backoff):

```
Rate Limit Demo
========================================

Testing single request...
Request successful (attempt 1)
   Found 15 team members

Testing rate limit handling (multiple requests)...

   Request 1:
Request successful (attempt 1)
   Completed

   Request 2:
Request successful (attempt 1)
   Completed

   Request 3:
Rate limited. Waiting 1s before retry...
Request successful (attempt 2)
   Completed
```

### Step 4 Output (Error Handler):

```
API Error Handler Demo
========================================

Testing Error Handling
========================================

1. Testing valid request...
   Success! Found 15 team members

2. Testing invalid endpoint (404)...
   /teams/invalid-endpoint: Resource not found. Check the URL.
   Correctly handled: /teams/invalid-endpoint: Resource not found. Check the URL.

3. Rate limit handling (rapid requests)...
   Request 1: Success
   Request 2: Success
   Request 3: Rate limited (handled)
   Request 4: Success
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| 401 Unauthorized | Check API key is correct and includes the colon in Basic Auth |
| 403 Forbidden | Some endpoints require Enterprise plan. Use a different endpoint or upgrade |
| 404 Not Found | Verify the endpoint URL is correct |
| 429 Too Many Requests | Implement exponential backoff as shown |
| Script hangs | Check network connection; add timeout to requests |

---

## Key Takeaways

| Error Code | Meaning | Retryable? | Action |
|------------|---------|------------|--------|
| **400** | Bad Request | No | Fix parameters |
| **401** | Unauthorized | No | Check API key |
| **403** | Forbidden | No | Check permissions/plan |
| **404** | Not Found | No | Fix URL |
| **429** | Rate Limited | Yes | Exponential backoff |
| **500+** | Server Error | Yes | Retry with backoff |

**Best Practices:**

1. Always implement **exponential backoff** for retries
2. **Don't retry** 4xx errors (client errors) - fix the issue first
3. **Do retry** 429 and 5xx errors (server/rate issues)
4. Use **jitter** (random delay) to avoid thundering herd problems
5. Set **reasonable timeouts** (5-30 seconds depending on endpoint)

---

## Bonus Challenge

Enhance the error handler with jitter to prevent thundering herd:

```python
import random

def get_jittered_delay(base_delay, attempt, jitter_factor=0.1):
    """Add random jitter to prevent synchronized retries"""
    delay = base_delay * (2 ** attempt)
    jitter = delay * jitter_factor * random.random()
    return delay + jitter

# Usage
wait_time = get_jittered_delay(1, attempt)  # e.g., 1.0-1.5s, 2.0-3.0s, etc.
```

---
