# Exercise 7.3: Rate Limits and Error Handling

**Module 7:** Cursor API Foundations  
**Slides:** `slides/module-07-marp.md` (Lesson 7.3)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Handle 429 responses with backoff and rate-limit headers.

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

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

**Monitor headers:** warn when `X-RateLimit-Remaining` < 10% of limit

**Token bucket rate limiter:** space requests evenly across the minute window

**CursorAPIClient:** combines rate limiting, retries on 429/5xx, timeout handling, and typed methods like `get_models()` and `create_agent()`

**Success Criteria:** Backoff · header monitoring · rate limiter · robust client class

---

## Success criteria

- [ ] Backoff · header monitoring · rate limiter · robust client class

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] API key from Exercise 1 (Admin API key recommended)
- [ ] Python 3.8+ installed (or Node.js)
- [ ] `curl` and `jq` installed

---

## Step-by-Step Instructions

### Step 1: Understand Rate Limits (2 minutes)

First, review the rate limits for different APIs:

| API | Endpoint Type | Rate Limit |
|-----|---------------|------------|
| **Admin API** | Most endpoints | 20 requests/minute |
| **Admin API** | `/teams/user-spend-limit` | 250 requests/minute |
| **Analytics API** | Team-level endpoints | 100 requests/minute |
| **Analytics API** | By-user endpoints | 50 requests/minute |
| **AI Code Tracking API** | All endpoints | 20 requests/minute |
| **Cloud Agents API** | All endpoints | Standard rate limiting |

**Key insight:** Rate limits are enforced **per team** and reset **every minute**.

---

### Step 2: Trigger a Rate Limit (2 minutes)

Make rapid requests to trigger a 429 response.

**Command (bash):**

```bash
# Make 25 rapid requests to trigger rate limit
for i in {1..25}; do
  echo "Request $i:"
  curl -s -u "$CURSOR_ADMIN_API_KEY:" \
    "https://api.cursor.com/teams/members" \
    -w "\nHTTP Status: %{http_code}\n"
  echo "---"
done
```

**Expected response (after hitting limit):**

```json
{
  "error": "Too Many Requests",
  "message": "Rate limit exceeded. Please try again later."
}
```

**HTTP Status:** 429

---

### Step 3: Implement Exponential Backoff (3 minutes)

Create a Python script that handles rate limits with exponential backoff.

**Create `rate_limit_demo.py`:**

```python
#!/usr/bin/env python3
"""
Rate Limit Demo with Exponential Backoff
"""

import requests
import time
import os
import sys

# Get API key from environment
API_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
if not API_KEY:
    print("Error: Set CURSOR_ADMIN_API_KEY environment variable")
    sys.exit(1)

def make_request_with_backoff(url, max_retries=5, base_delay=1):
    """
    Make an API request with exponential backoff on rate limits.

    Args:
        url: The API endpoint URL
        max_retries: Maximum number of retry attempts
        base_delay: Initial delay in seconds (doubles each retry)

    Returns:
        Response object or None if all retries failed
    """
    auth = (API_KEY, "")

    for attempt in range(max_retries):
        response = requests.get(url, auth=auth)

        # Success
        if response.status_code == 200:
            print(f"Request successful (attempt {attempt + 1})")
            return response

        # Rate limited - wait and retry
        if response.status_code == 429:
            wait_time = base_delay * (2 ** attempt)
            print(f"Rate limited. Waiting {wait_time}s before retry...")
            time.sleep(wait_time)
            continue

        # Other errors - may not be retryable
        if response.status_code == 401:
            print("Authentication failed. Check your API key.")
            return None
        if response.status_code == 403:
            print("Forbidden. Enterprise feature may be required.")
            return None
        if response.status_code == 404:
            print("Not found. Check the endpoint URL.")
            return None
        if response.status_code >= 500:
            print(f"Server error ({response.status_code}). Retrying...")
            wait_time = base_delay * (2 ** attempt)
            time.sleep(wait_time)
            continue

        # Unexpected status
        print(f"Unexpected error: {response.status_code}")
        print(f"   Response: {response.text[:200]}")
        return None

    print("Max retries exceeded. Request failed.")
    return None

def test_single_request():
    """Test a single request with backoff"""
    print("\nTesting single request...")
    url = "https://api.cursor.com/teams/members"
    response = make_request_with_backoff(url)

    if response and response.status_code == 200:
        data = response.json()
        members = data.get("teamMembers", [])
        print(f"   Found {len(members)} team members")

def test_rate_limit_handling():
    """Test multiple rapid requests to demonstrate backoff"""
    print("\nTesting rate limit handling (multiple requests)...")
    url = "https://api.cursor.com/teams/members"

    for i in range(10):
        print(f"\n   Request {i+1}:")
        response = make_request_with_backoff(url, max_retries=3)

        if response and response.status_code == 200:
            print(f"   Completed")
        else:
            print(f"   Failed")

        # Small delay between requests
        time.sleep(0.5)

if __name__ == "__main__":
    print("Rate Limit Demo")
    print("=" * 40)

    test_single_request()
    test_rate_limit_handling()

    print("\nDemo complete")
```

**Run the script:**

```bash
export CURSOR_ADMIN_API_KEY="your_key_here"
python3 rate_limit_demo.py
```

**Expected output:**

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

---

### Step 4: Handle Common Error Responses (3 minutes)

Create a comprehensive error handler that properly handles all HTTP status codes.

**Create `error_handler.py`:**

```python
#!/usr/bin/env python3
"""
Comprehensive API Error Handler
"""

import requests
import time
import os
import sys
from datetime import datetime

API_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
if not API_KEY:
    print("Error: Set CURSOR_ADMIN_API_KEY environment variable")
    sys.exit(1)

class CursorAPIError(Exception):
    """Custom exception for Cursor API errors"""
    def __init__(self, status_code, message, retryable=False):
        self.status_code = status_code
        self.message = message
        self.retryable = retryable
        super().__init__(f"[{status_code}] {message}")

def handle_api_response(response, endpoint_name=""):
    """
    Handle API response and raise appropriate exceptions.

    Args:
        response: requests.Response object
        endpoint_name: Name of the endpoint for error messages

    Returns:
        Parsed JSON response if successful

    Raises:
        CursorAPIError with appropriate status code handling
    """
    prefix = f"{endpoint_name}: " if endpoint_name else ""

    # 200 OK - Success
    if response.status_code == 200:
        return response.json()

    # 400 Bad Request - Invalid parameters
    if response.status_code == 400:
        error_msg = f"{prefix}Invalid request parameters"
        try:
            error_data = response.json()
            error_msg += f": {error_data.get('message', 'Unknown error')}"
        except:
            pass
        raise CursorAPIError(400, error_msg, retryable=False)

    # 401 Unauthorized - Invalid API key
    if response.status_code == 401:
        error_msg = f"{prefix}Authentication failed. Check your API key."
        raise CursorAPIError(401, error_msg, retryable=False)

    # 403 Forbidden - Insufficient permissions
    if response.status_code == 403:
        error_msg = f"{prefix}Forbidden. This endpoint requires Enterprise plan or higher permissions."
        raise CursorAPIError(403, error_msg, retryable=False)

    # 404 Not Found - Resource doesn't exist
    if response.status_code == 404:
        error_msg = f"{prefix}Resource not found. Check the URL."
        raise CursorAPIError(404, error_msg, retryable=False)

    # 429 Too Many Requests - Rate limited (retryable)
    if response.status_code == 429:
        error_msg = f"{prefix}Rate limit exceeded. Please wait and retry."
        raise CursorAPIError(429, error_msg, retryable=True)

    # 500 Internal Server Error (retryable)
    if 500 <= response.status_code < 600:
        error_msg = f"{prefix}Server error ({response.status_code}). Try again later."
        raise CursorAPIError(response.status_code, error_msg, retryable=True)

    # Unknown status
    raise CursorAPIError(response.status_code, f"{prefix}Unexpected error", retryable=False)

def call_api(endpoint, method="GET", data=None, max_retries=3):
    """
    Make an API call with automatic retry for retryable errors.

    Args:
        endpoint: API endpoint (e.g., "/teams/members")
        method: HTTP method (GET, POST, etc.)
        data: Request body for POST requests
        max_retries: Maximum number of retries for retryable errors

    Returns:
        API response as dictionary
    """
    url = f"https://api.cursor.com{endpoint}"
    auth = (API_KEY, "")
    headers = {"Content-Type": "application/json"}

    for attempt in range(max_retries):
        try:
            if method == "GET":
                response = requests.get(url, auth=auth, headers=headers)
            elif method == "POST":
                response = requests.post(url, auth=auth, headers=headers, json=data)
            else:
                raise ValueError(f"Unsupported method: {method}")

            # Handle response (may raise exception)
            return handle_api_response(response, endpoint)

        except CursorAPIError as e:
            print(f"   {e.message}")

            # If not retryable, raise immediately
            if not e.retryable:
                raise

            # If retryable and we have attempts left
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                print(f"   Retrying in {wait_time}s... (attempt {attempt + 2}/{max_retries})")
                time.sleep(wait_time)
            else:
                print(f"   Max retries exceeded. Giving up.")
                raise

        except requests.exceptions.RequestException as e:
            print(f"   Network error: {str(e)[:100]}")
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                print(f"   Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise

def demonstrate_error_handling():
    """Demonstrate error handling for various scenarios"""

    print("\nTesting Error Handling")
    print("=" * 40)

    # Test 1: Valid request (should succeed)
    print("\n1. Testing valid request...")
    try:
        result = call_api("/teams/members")
        members = result.get("teamMembers", [])
        print(f"   Success! Found {len(members)} team members")
    except Exception as e:
        print(f"   Failed: {e}")

    # Test 2: Invalid endpoint (should return 404)
    print("\n2. Testing invalid endpoint (404)...")
    try:
        result = call_api("/teams/invalid-endpoint")
        print(f"   Unexpected success: {result}")
    except CursorAPIError as e:
        print(f"   Correctly handled: {e.message}")

    # Test 3: Rate limit simulation (if you have a test endpoint)
    print("\n3. Rate limit handling (rapid requests)...")
    for i in range(15):
        try:
            result = call_api("/teams/members", max_retries=2)
            print(f"   Request {i+1}: Success")
        except CursorAPIError as e:
            if e.status_code == 429:
                print(f"   Request {i+1}: Rate limited (handled)")
            else:
                print(f"   Request {i+1}: {e.message}")
        time.sleep(0.3)  # Small delay between requests

if __name__ == "__main__":
    print("API Error Handler Demo")
    print("=" * 40)
    demonstrate_error_handling()
    print("\nDemo complete")
```

**Run the script:**

```bash
python3 error_handler.py
```

---

### Step 5: Understand Error Response Formats (2 minutes)

Review the common error response formats:

**400 Bad Request:**

```json
{
  "error": "Bad Request",
  "message": "Some users are not in the team"
}
```

**401 Unauthorized:**

```json
{
  "error": "Unauthorized",
  "message": "Invalid API key"
}
```

**403 Forbidden:**

```json
{
  "error": "Forbidden",
  "message": "Enterprise access required"
}
```

**404 Not Found:**

```json
{
  "error": "Not Found",
  "message": "Resource not found"
}
```

**429 Too Many Requests:**

```json
{
  "error": "Too Many Requests",
  "message": "Rate limit exceeded. Please try again later."
}
```

**500 Internal Server Error:**

```json
{
  "error": "Internal Server Error",
  "message": "An unexpected error occurred"
}
```

---

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

## Success Criteria

- [ ] Understood rate limits for different APIs
- [ ] Successfully triggered a 429 response
- [ ] Implemented exponential backoff in Python
- [ ] Handled 401, 403, 404, 429, and 500 errors appropriately
- [ ] Created reusable error handling functions
- [ ] Demonstrated retry logic for retryable errors

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

## Exercise Complete

Check off when done:

- [ ] Triggered rate limit (429) response
- [ ] Implemented exponential backoff
- [ ] Created error handler for all status codes
- [ ] Distinguished retryable vs non-retryable errors
- [ ] Tested error handling with invalid endpoints
- [ ] (Bonus) Added jitter to retry delays

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
