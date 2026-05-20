# Module 7: Cursor API Foundations

## Cursor Training Program — Day 2 (Concept + Hands-On)

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Concept + hands-on exercise |
| **Prerequisites** | Cursor account, basic API familiarity, Python 3.8+ installed |
| **Module Goal** | Understand the Cursor API ecosystem, authenticate securely, handle errors, and optimize requests |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Identify the five Cursor APIs and their use cases
- Generate and securely manage API keys
- Implement rate limit handling and error recovery
- Use ETag caching for efficient repeat queries
- Test authentication by listing available models

---

## Lesson 7.1: The Cursor API Landscape

### Concept (10 minutes)

> *"The five Cursor APIs at a glance and when to use each. Cursor provides multiple API surfaces for different use cases – from chat completion to team management."*

### The Five APIs

```
┌─────────────────────────────────────────────────────────────┐
│                  CURSOR API LANDSCAPE                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. CHAT COMPLETIONS API                                     │
│     • Endpoint: /v1/chat/completions                        │
│     • Purpose: OpenAI-compatible chat interface             │
│     • Use when: Integrating Cursor models into apps         │
│                                                              │
│  2. AGENTS API                                               │
│     • Endpoint: /v1/agents                                  │
│     • Purpose: Create and manage Cloud Agents               │
│     • Use when: Running autonomous agent tasks              │
│                                                              │
│  3. FILES API                                                │
│     • Endpoint: /v1/files                                   │
│     • Purpose: Upload/download files for agents             │
│     • Use when: Providing context files to agents           │
│                                                              │
│  4. ADMIN API                                                │
│     • Endpoint: /v1/admin/*                                 │
│     • Purpose: Team management, analytics, policies         │
│     • Use when: Administering organization                  │
│                                                              │
│  5. WEBHOOKS API                                             │
│     • Endpoint: /v1/webhooks                                │
│     • Purpose: Register and manage webhook endpoints        │
│     • Use when: Receiving async notifications               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### API Comparison Matrix

| API | Auth Type | Rate Limit | Cost | Primary Use |
|-----|-----------|------------|------|-------------|
| **Chat Completions** | User or API key | Per-minute token | Pay-per-token | Direct model access |
| **Agents** | User API key | Per-minute requests | Per-run | Long-running tasks |
| **Files** | User API key | Per-minute | Storage | Context upload |
| **Admin** | Admin API key | Higher limits | Included in plan | Team management |
| **Webhooks** | User API key | Per-minute | Free | Notifications |

### When to Use Which API

```
┌─────────────────────────────────────────────────────────────┐
│                    API SELECTION FLOW                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Start here: What do you need?                              │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ "I want to call a model directly"                   │   │
│  │ → Chat Completions API (OpenAI-compatible)          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ "I want to run a long task that writes code"        │   │
│  │ → Agents API                                        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ "I want to manage my team's usage and limits"       │   │
│  │ → Admin API                                         │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ "I want to be notified when agents complete"        │   │
│  │ → Webhooks API                                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### OpenAI Compatibility

The Chat Completions API is **OpenAI-compatible**, meaning:

```python
# You can use the OpenAI Python SDK with Cursor
from openai import OpenAI

client = OpenAI(
    base_url="https://api.cursor.com/v1",
    api_key="your-cursor-api-key"
)

response = client.chat.completions.create(
    model="claude-4.6-sonnet",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**Success Criteria:**
- [ ] Understands five API categories
- [ ] Can select correct API for use case
- [ ] Understands OpenAI compatibility

---

## Lesson 7.2: Authentication

### Concept (8 minutes)

> *"Generating and testing API keys. Cursor uses HTTP Basic Authentication with API keys – simple but requires careful handling."*

### Authentication Methods

| Method | Format | When to Use |
|--------|--------|-------------|
| **HTTP Basic** | `-u "api_key:"` | CLI, curl, most SDKs |
| **Bearer Token** | `Authorization: Bearer <key>` | OAuth-style clients |
| **User API Key** | Regular key | Agents, Chat, Files APIs |
| **Admin API Key** | `admin_` prefixed | Admin API only |

### API Key Types

```
┌─────────────────────────────────────────────────────────────┐
│                    API KEY TYPES                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  USER API KEY                                                │
│  • Generated in: Cursor Settings → API Keys                 │
│  • Format: cursor_xxxxxxxxxxxx                               │
│  • Scopes: Your user permissions                             │
│  • Can access: Agents, Chat, Files, Webhooks                │
│                                                              │
│  ADMIN API KEY                                               │
│  • Generated in: Organization Settings → API Keys           │
│  • Format: cursor_admin_xxxxxxxxxxxx                        │
│  • Scopes: Full organization admin                          │
│  • Can access: Admin API + everything User can              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Security Best Practices

```
┌─────────────────────────────────────────────────────────────┐
│              API KEY SECURITY CHECKLIST                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ☐ Never commit API keys to git                             │
│  ☐ Use environment variables or secret managers             │
│  ☐ Rotate keys periodically (every 90 days)                 │
│  ☐ Use different keys for development and production        │
│  ☐ Revoke unused keys immediately                           │
│  ☐ Use Admin API keys only when necessary                   │
│  ☐ Monitor key usage in dashboard                           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Hands-On Exercise (12 minutes)

**Step 1:** Generate a User API Key

```bash
# Via Cursor UI
# 1. Open Cursor → Settings (Cmd+, or Ctrl+,)
# 2. Click "API Keys" in left sidebar
# 3. Click "Generate New Key"
# 4. Name it "training-day2"
# 5. Copy the key immediately (only shown once)
```

**Step 2:** Set up environment variables

```bash
# Add to ~/.zshrc or ~/.bashrc
export CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx"

# Or for current session only
export CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx"

# Verify
echo $CURSOR_USER_API_KEY
```

**Step 3:** Test authentication with curl

```bash
# Basic authentication format: -u "api_key:"
# Note the colon after the key (empty password)

curl -s -u "$CURSOR_USER_API_KEY:" \
  https://api.cursor.com/v1/models \
  | head -20
```

**Step 4:** Test with Python

```python
#!/usr/bin/env python3
import requests
import os

API_KEY = os.environ.get("CURSOR_USER_API_KEY")
AUTH = (API_KEY, "")  # Empty password

response = requests.get(
    "https://api.cursor.com/v1/models",
    auth=AUTH
)

if response.status_code == 200:
    print("✅ Authentication successful!")
    models = response.json()
    print(f"Available models: {len(models.get('data', []))}")
else:
    print(f"❌ Authentication failed: {response.status_code}")
    print(response.text)
```

**Step 5:** Test with OpenAI SDK

```python
#!/usr/bin/env python3
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://api.cursor.com/v1",
    api_key=os.environ.get("CURSOR_USER_API_KEY")
)

try:
    response = client.chat.completions.create(
        model="gpt-5-mini",  # Fast, cheap model for testing
        messages=[{"role": "user", "content": "Say 'API works!'"}],
        max_tokens=10
    )
    print(f"✅ OpenAI SDK works: {response.choices[0].message.content}")
except Exception as e:
    print(f"❌ Error: {e}")
```

**Step 6:** Generate and test Admin API Key

```bash
# Via Cursor web
# 1. Go to cursor.com → Organization Settings
# 2. Click "API Keys"
# 3. Click "Generate Admin Key"
# 4. Copy and save

export CURSOR_ADMIN_API_KEY="cursor_admin_xxxxxxxxxxxx"

# Test admin access
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  https://api.cursor.com/v1/admin/organization \
  | jq '.'
```

**Step 7:** Revoke a key (when compromised or unused)

```bash
# Via API (requires admin key)
curl -X DELETE https://api.cursor.com/v1/api-keys/key_123456 \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{"reason": "key_compromised"}'

# Or via UI: Settings → API Keys → Revoke
```

**Success Criteria:**
- [ ] Generated User API key
- [ ] Set up environment variable
- [ ] Tested authentication with curl
- [ ] Tested with Python requests
- [ ] Tested with OpenAI SDK
- [ ] Generated and tested Admin API key

---

## Lesson 7.3: Rate Limits and Error Handling

### Concept (10 minutes)

> *"Production-grade reliability patterns. APIs have limits – understanding and handling errors gracefully is essential for robust applications."*

### Rate Limits by API

| API | Limit | Window | Burst |
|-----|-------|--------|-------|
| Chat Completions | 1000 requests | per minute | 2000 |
| Chat Completions (tokens) | 500k tokens | per minute | - |
| Agents (create) | 100 requests | per minute | 150 |
| Admin API | 500 requests | per minute | 1000 |
| Webhooks | 2000 requests | per minute | 5000 |

### HTTP Status Codes to Handle

| Code | Meaning | Action |
|------|---------|--------|
| **200** | Success | Process response |
| **400** | Bad Request | Fix request parameters |
| **401** | Unauthorized | Check API key |
| **403** | Forbidden | Check permissions |
| **404** | Not Found | Verify endpoint/ID |
| **429** | Too Many Requests | Implement backoff |
| **500** | Internal Error | Retry with backoff |
| **503** | Service Unavailable | Retry with backoff |

### Rate Limit Headers

Every response includes these headers:

| Header | Description | Example |
|--------|-------------|---------|
| `X-RateLimit-Limit` | Max requests per window | `1000` |
| `X-RateLimit-Remaining` | Requests left in window | `942` |
| `X-RateLimit-Reset` | Time when window resets (Unix timestamp) | `1700000000` |
| `Retry-After` | Seconds to wait (on 429) | `60` |

### Hands-On Exercise (10 minutes)

**Step 1:** Implement exponential backoff

```python
#!/usr/bin/env python3
import time
import requests
import os
from typing import Optional

API_KEY = os.environ.get("CURSOR_USER_API_KEY")
AUTH = (API_KEY, "")

def call_with_retry(
    url: str,
    max_retries: int = 5,
    base_delay: float = 1.0,
    max_delay: float = 60.0
) -> Optional[dict]:
    """Make API call with exponential backoff retry."""
    
    for attempt in range(max_retries):
        response = requests.get(url, auth=AUTH)
        
        # Success
        if response.status_code == 200:
            return response.json()
        
        # Client error (don't retry)
        if 400 <= response.status_code < 500:
            print(f"❌ Client error {response.status_code}: {response.text}")
            return None
        
        # Server error or rate limit (retry)
        if response.status_code in [429, 500, 502, 503, 504]:
            # Get retry delay from header or calculate
            if 'Retry-After' in response.headers:
                delay = int(response.headers['Retry-After'])
            else:
                delay = min(base_delay * (2 ** attempt), max_delay)
            
            print(f"⚠️ Rate limited (attempt {attempt + 1}/{max_retries}). "
                  f"Waiting {delay}s...")
            time.sleep(delay)
            continue
        
        # Unknown error
        print(f"❌ Unexpected error {response.status_code}")
        return None
    
    print(f"❌ Max retries ({max_retries}) exceeded")
    return None

# Test with rate limit simulation
result = call_with_retry("https://api.cursor.com/v1/models")
if result:
    print(f"✅ Success: {len(result.get('data', []))} models")
```

**Step 2:** Monitor rate limits from response

```python
def api_call_with_monitoring(url: str):
    """Make API call and track rate limit headers."""
    response = requests.get(url, auth=AUTH)
    
    # Extract rate limit headers
    remaining = response.headers.get('X-RateLimit-Remaining')
    limit = response.headers.get('X-RateLimit-Limit')
    reset = response.headers.get('X-RateLimit-Reset')
    
    if remaining and limit:
        print(f"📊 Rate limit: {remaining}/{limit} remaining")
        
        # Warning if low on quota
        if int(remaining) < int(limit) * 0.1:
            print(f"⚠️ Low on rate limit! Reset at {reset}")
    
    return response

# Test
response = api_call_with_monitoring("https://api.cursor.com/v1/models")
```

**Step 3:** Implement request queuing with rate limiting

```python
import time
from collections import deque
from threading import Lock

class RateLimiter:
    """Simple token bucket rate limiter."""
    
    def __init__(self, requests_per_minute: int):
        self.requests_per_minute = requests_per_minute
        self.interval = 60.0 / requests_per_minute
        self.last_request_time = 0
        self.lock = Lock()
    
    def acquire(self):
        """Wait until a request can be made."""
        with self.lock:
            now = time.time()
            elapsed = now - self.last_request_time
            if elapsed < self.interval:
                wait_time = self.interval - elapsed
                time.sleep(wait_time)
            self.last_request_time = time.time()

# Usage
limiter = RateLimiter(requests_per_minute=50)  # 50 requests per minute

for i in range(100):
    limiter.acquire()
    response = requests.get("https://api.cursor.com/v1/models", auth=AUTH)
    print(f"Request {i+1}: {response.status_code}")
```

**Step 4:** Complete error handling class

```python
class CursorAPIClient:
    """Robust Cursor API client with error handling."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.auth = (api_key, "")
        self.base_url = "https://api.cursor.com/v1"
        self.rate_limiter = RateLimiter(requests_per_minute=100)
    
    def _request(self, method: str, endpoint: str, **kwargs) -> dict:
        """Make authenticated request with retries."""
        url = f"{self.base_url}{endpoint}"
        self.rate_limiter.acquire()
        
        for attempt in range(3):
            try:
                response = requests.request(
                    method, url, auth=self.auth, 
                    timeout=30, **kwargs
                )
                
                # Track rate limits
                remaining = response.headers.get('X-RateLimit-Remaining')
                if remaining and int(remaining) < 10:
                    print(f"⚠️ Low rate limit: {remaining} remaining")
                
                if response.status_code == 200:
                    return response.json()
                
                if response.status_code == 429:
                    retry_after = int(response.headers.get('Retry-After', 5))
                    print(f"Rate limited. Waiting {retry_after}s...")
                    time.sleep(retry_after)
                    continue
                
                if 500 <= response.status_code < 600:
                    wait = 2 ** attempt
                    print(f"Server error. Retrying in {wait}s...")
                    time.sleep(wait)
                    continue
                
                # Client error - don't retry
                response.raise_for_status()
                
            except requests.exceptions.Timeout:
                print(f"Timeout on attempt {attempt + 1}")
                if attempt == 2:
                    raise
                time.sleep(2 ** attempt)
            
            except requests.exceptions.ConnectionError:
                print(f"Connection error on attempt {attempt + 1}")
                if attempt == 2:
                    raise
                time.sleep(2 ** attempt)
        
        raise Exception(f"Failed after 3 attempts: {response.status_code}")
    
    def get_models(self):
        return self._request("GET", "/models")
    
    def create_agent(self, prompt: str, repo_url: str):
        return self._request("POST", "/agents", json={
            "prompt": {"text": prompt},
            "repos": [{"url": repo_url}]
        })

# Test the client
client = CursorAPIClient(os.environ.get("CURSOR_USER_API_KEY"))
models = client.get_models()
print(f"✅ Client works! {len(models.get('data', []))} models")
```

**Success Criteria:**
- [ ] Implemented exponential backoff
- [ ] Monitored rate limit headers
- [ ] Created rate limiter for request queuing
- [ ] Built robust API client with error handling

---

## Lesson 7.4: ETag Caching

### Concept (8 minutes)

> *"Efficient repeat queries for analytics workloads. ETags (entity tags) let you cache responses and avoid downloading data that hasn't changed."*

### What Are ETags?

ETags are unique identifiers for API response versions. When you request the same resource again:

1. Send `If-None-Match` header with previous ETag
2. Server returns `304 Not Modified` if unchanged
3. No data transfer, no rate limit consumption

### ETag Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    ETAG CACHING FLOW                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Request 1: GET /v1/analytics/usage                         │
│  Response 1:                                                │
│    Status: 200 OK                                           │
│    Headers: ETag: "abc123"                                  │
│    Body: { ... usage data ... }                             │
│                                                              │
│  [Client caches response with ETag "abc123"]                │
│                                                              │
│  Request 2: GET /v1/analytics/usage                         │
│    Headers: If-None-Match: "abc123"                         │
│                                                              │
│  If data unchanged:                                         │
│    Response 2: Status: 304 Not Modified                     │
│    Body: (empty)                                            │
│                                                              │
│  If data changed:                                           │
│    Response 2: Status: 200 OK                               │
│    Headers: ETag: "def456" (new)                            │
│    Body: { ... updated data ... }                           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Which Endpoints Support ETags

| Endpoint | ETag Support | Cache Freshness |
|----------|--------------|-----------------|
| `/v1/models` | ✅ Yes | Changes rarely |
| `/v1/admin/members` | ✅ Yes | Changes occasionally |
| `/v1/agents/{id}` | ✅ Yes | Changes during run |
| `/v1/analytics/usage` | ✅ Yes | Daily changes |
| `/v1/agents` (list) | ⚠️ Partial | Changes frequently |

### Hands-On Exercise (10 minutes)

**Step 1:** Basic ETag usage

```python
import requests
import os
import hashlib

API_KEY = os.environ.get("CURSOR_USER_API_KEY")
AUTH = (API_KEY, "")

def get_with_etag(url: str, previous_etag: str = None):
    """Make request with ETag caching."""
    headers = {}
    if previous_etag:
        headers['If-None-Match'] = previous_etag
    
    response = requests.get(url, auth=AUTH, headers=headers)
    
    if response.status_code == 304:
        print(f"🟡 Not modified (cached response still valid)")
        return None, response.headers.get('ETag')
    
    if response.status_code == 200:
        new_etag = response.headers.get('ETag')
        print(f"✅ Data changed, new ETag: {new_etag}")
        return response.json(), new_etag
    
    response.raise_for_status()

# Test with models endpoint (rarely changes)
url = "https://api.cursor.com/v1/models"

# First request
data1, etag1 = get_with_etag(url)
print(f"Initial ETag: {etag1}")

# Second request (should be 304)
data2, etag2 = get_with_etag(url, etag1)
if data2 is None:
    print("Using cached data (no changes)")
    data2 = data1  # Use cached version
```

**Step 2:** Cache manager for analytics workloads

```python
import json
import os
import pickle
from datetime import datetime, timedelta

class ETagCache:
    """Persistent ETag cache for API responses."""
    
    def __init__(self, cache_dir: str = ".cursor_api_cache"):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
    
    def _get_cache_path(self, url: str) -> str:
        """Generate cache file path from URL."""
        url_hash = hashlib.md5(url.encode()).hexdigest()
        return os.path.join(self.cache_dir, f"{url_hash}.pkl")
    
    def get(self, url: str) -> tuple:
        """Get cached response and ETag."""
        cache_path = self._get_cache_path(url)
        if os.path.exists(cache_path):
            with open(cache_path, 'rb') as f:
                cached = pickle.load(f)
            return cached.get('data'), cached.get('etag')
        return None, None
    
    def set(self, url: str, data: dict, etag: str):
        """Cache response with ETag."""
        cache_path = self._get_cache_path(url)
        with open(cache_path, 'wb') as f:
            pickle.dump({
                'data': data,
                'etag': etag,
                'timestamp': datetime.now()
            }, f)
    
    def is_fresh(self, url: str, max_age_minutes: int = 60) -> bool:
        """Check if cached entry is still fresh."""
        cache_path = self._get_cache_path(url)
        if not os.path.exists(cache_path):
            return False
        
        with open(cache_path, 'rb') as f:
            cached = pickle.load(f)
        
        age = datetime.now() - cached['timestamp']
        return age < timedelta(minutes=max_age_minutes)

class CachedCursorClient:
    """Cursor API client with ETag caching."""
    
    def __init__(self, api_key: str):
        self.auth = (api_key, "")
        self.cache = ETagCache()
    
    def get(self, endpoint: str, force_refresh: bool = False) -> dict:
        url = f"https://api.cursor.com/v1{endpoint}"
        
        # Check cache if not forcing refresh
        if not force_refresh:
            cached_data, cached_etag = self.cache.get(url)
            if cached_data and cached_etag:
                # Verify with server
                headers = {'If-None-Match': cached_etag}
                response = requests.get(url, auth=self.auth, headers=headers)
                
                if response.status_code == 304:
                    print(f"📦 Cache HIT: {endpoint}")
                    return cached_data
                
                if response.status_code == 200:
                    print(f"🔄 Cache MISS (data changed): {endpoint}")
                    new_data = response.json()
                    new_etag = response.headers.get('ETag')
                    self.cache.set(url, new_data, new_etag)
                    return new_data
        
        # Force refresh or no cache
        print(f"🌐 API CALL: {endpoint}")
        response = requests.get(url, auth=self.auth)
        response.raise_for_status()
        
        data = response.json()
        etag = response.headers.get('ETag')
        if etag:
            self.cache.set(url, data, etag)
        
        return data

# Usage example
client = CachedCursorClient(os.environ.get("CURSOR_USER_API_KEY"))

# First call - hits API
models1 = client.get("/models")
print(f"Call 1: Got {len(models1.get('data', []))} models")

# Second call - uses cache (304)
models2 = client.get("/models")
print(f"Call 2: Using cache")
```

**Step 3:** Batch analytics with caching

```python
# Efficient daily analytics fetch with ETag caching
def fetch_daily_analytics(client: CachedCursorClient, date: str):
    """Fetch analytics for a specific date with caching."""
    endpoint = f"/admin/analytics/usage/daily?date={date}"
    
    try:
        data = client.get(endpoint)
        return data
    except Exception as e:
        print(f"Failed to fetch {date}: {e}")
        return None

# Fetch last 30 days efficiently (uses cache for unchanged days)
from datetime import datetime, timedelta

client = CachedCursorClient(os.environ.get("CURSOR_ADMIN_API_KEY"))

end_date = datetime.now()
for i in range(30):
    date = (end_date - timedelta(days=i)).strftime("%Y-%m-%d")
    data = fetch_daily_analytics(client, date)
    if data:
        print(f"{date}: {'cached' if 'Cache HIT' in str(data) else 'fresh'}")
```

**Success Criteria:**
- [ ] Understood ETag concept
- [ ] Implemented basic ETag request
- [ ] Built persistent ETag cache
- [ ] Applied caching to analytics workloads

---

## Lesson 7.5: Listing Available Models

### Concept (4 minutes)

> *"A quick authentication smoke-test. Listing models is the simplest API call – perfect for verifying your API key works and seeing what models are available."*

### The Models Endpoint

```bash
GET /v1/models
```

**Response includes:**
- Model ID (used in API calls)
- Display name
- Context window size
- Pricing information (input/output per 1M tokens)
- Capabilities (vision, tool calling, etc.)

### Hands-On Exercise (6 minutes)

**Step 1:** List models with curl

```bash
curl -s -u "$CURSOR_USER_API_KEY:" \
  https://api.cursor.com/v1/models \
  | jq '.data[] | {id: .id, context: .context_window, input_price: .pricing.input}'
```

**Step 2:** List models with Python

```python
#!/usr/bin/env python3
import requests
import os
from tabulate import tabulate

API_KEY = os.environ.get("CURSOR_USER_API_KEY")
AUTH = (API_KEY, "")

response = requests.get("https://api.cursor.com/v1/models", auth=AUTH)
models = response.json().get("data", [])

# Format for display
table = []
for model in models:
    table.append([
        model.get('id', 'unknown'),
        model.get('context_window', 'N/A'),
        f"${model.get('pricing', {}).get('input', 0):.2f}",
        f"${model.get('pricing', {}).get('output', 0):.2f}",
        "✅" if model.get('capabilities', {}).get('vision') else "❌"
    ])

print(tabulate(table, 
    headers=["Model ID", "Context (tokens)", "Input Price (1M)", "Output Price (1M)", "Vision"],
    tablefmt="grid"))

# Count models by provider
providers = {}
for model in models:
    provider = model.get('provider', 'unknown')
    providers[provider] = providers.get(provider, 0) + 1

print("\n📊 Models by Provider:")
for provider, count in providers.items():
    print(f"  {provider}: {count}")
```

**Step 3:** Filter models by capability

```python
# Find models with large context windows
large_context = [m for m in models if m.get('context_window', 0) >= 100000]
print(f"\n🔍 Models with 100k+ context: {len(large_context)}")
for m in large_context:
    print(f"  {m['id']}: {m['context_window']:,} tokens")

# Find cheapest models
cheapest = sorted(models, key=lambda x: x.get('pricing', {}).get('input', 999))[:5]
print(f"\n💰 Cheapest models by input price:")
for m in cheapest:
    price = m.get('pricing', {}).get('input', 0)
    print(f"  {m['id']}: ${price:.2f}/1M tokens")
```

**Step 4:** Create a model selection helper

```python
def select_model(task_type: str, budget: str = "balanced"):
    """Recommend a model based on task and budget."""
    
    models_config = {
        "simple_fix": {
            "low": "gpt-5-mini",
            "balanced": "claude-4.5-haiku",
            "high": "claude-4.6-sonnet"
        },
        "complex_task": {
            "low": "claude-4.6-sonnet",
            "balanced": "claude-4.7-opus",
            "high": "gpt-5.5"
        },
        "frontend_ui": {
            "low": "gemini-3.1-pro",
            "balanced": "gemini-3.1-pro",
            "high": "gemini-3.1-pro"
        },
        "code_review": {
            "low": "gpt-5.3-codex",
            "balanced": "claude-4.6-sonnet",
            "high": "claude-4.7-opus"
        }
    }
    
    return models_config.get(task_type, models_config["simple_fix"]).get(budget, "claude-4.6-sonnet")

# Test the helper
print(f"For code review with balanced budget: {select_model('code_review', 'balanced')}")
```

**Success Criteria:**
- [ ] Listed models with curl
- [ ] Formatted model list with Python
- [ ] Filtered models by capability
- [ ] Created model selection helper

---

## Module Summary

| Lesson | Topic | Time | Key Skill |
|--------|-------|------|-----------|
| 7.1 | API Landscape | 10 min | API selection |
| 7.2 | Authentication | 12 min | Key management |
| 7.3 | Rate Limits & Errors | 10 min | Robust clients |
| 7.4 | ETag Caching | 10 min | Efficient queries |
| 7.5 | Listing Models | 6 min | Auth smoke-test |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│                 CURSOR API QUICK REFERENCE                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  BASE URL: https://api.cursor.com/v1                        │
│                                                              │
│  AUTHENTICATION:                                            │
│  • Header: Authorization: Bearer <key>                      │
│  • Basic: -u "api_key:" (curl)                              │
│  • OpenAI SDK: base_url="https://api.cursor.com/v1"         │
│                                                              │
│  KEY ENDPOINTS:                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ GET  /models                    List available models│   │
│  │ POST /agents                    Create cloud agent   │   │
│  │ GET  /agents/{id}               Get agent status     │   │
│  │ GET  /admin/members             List team members    │   │
│  │ GET  /admin/analytics/usage     Get usage data       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ERROR HANDLING:                                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 429 → Wait, then retry (exponential backoff)       │   │
│  │ 5xx → Retry (server errors)                        │   │
│  │ 4xx → Fix request, don't retry                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  CACHING:                                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • Use ETag for models, members, analytics          │   │
│  │ • Send If-None-Match with previous ETag            │   │
│  │ • Handle 304 Not Modified responses                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Transition to Module 8

> *"Now that you understand the API foundations, Module 8 will cover Cloud Agents API and Webhooks – programmatically creating agents, streaming responses, and setting up notifications."*

---

*End of Module 7*