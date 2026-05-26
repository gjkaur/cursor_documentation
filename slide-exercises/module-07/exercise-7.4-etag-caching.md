# Exercise 7.4: ETag Caching

**Module 7:** Cursor API Foundations  
**Slides:** `slides/module-07-marp.md` (Lesson 7.4)  
**Time:** 18 min  
**Difficulty:** Beginner

**Objective:** Use ETags to avoid re-downloading unchanged API data.

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
def get_with_etag(url, previous_etag=None):
    headers = {'If-None-Match': previous_etag} if previous_etag else {}
    response = requests.get(url, auth=AUTH, headers=headers)

    if response.status_code == 304:
        return None, response.headers.get('ETag')  # Use cached data
    if response.status_code == 200:
        return response.json(), response.headers.get('ETag')
```

---

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

**ETagCache:** persistent pickle-based cache keyed by URL hash

**CachedCursorClient:**
- Check local cache → send `If-None-Match`
- On 304 → return cached data (Cache HIT)
- On 200 → update cache (Cache MISS)

**Batch analytics:** fetch 30 days of usage — unchanged days return 304 instantly

**Success Criteria:** Basic ETag request · persistent cache · analytics workload caching

---

## Success criteria

- [ ] Check local cache → send `If-None-Match`
- [ ] On 304 → return cached data (Cache HIT)
- [ ] On 200 → update cache (Cache MISS)
- [ ] Basic ETag request · persistent cache · analytics workload caching

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

## Prerequisites

- [ ] API key from Exercise 1 (Admin API key recommended for Analytics API)
- [ ] Python 3.8+ installed
- [ ] `curl` and `jq` installed

---

## Step-by-Step Instructions

### Step 1: Understand ETag Caching (2 minutes)

**What is ETag Caching?**

ETag (Entity Tag) is a header that uniquely identifies a version of a resource. When data doesn't change, the ETag stays the same.

**How it works:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    ETag Caching Flow                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Request 1: GET /analytics/team/dau                            │
│  Response:                                                      │
│    ETag: "abc123"                                               │
│    Body: [full data]                                            │
│                                                                 │
│  Request 2: GET /analytics/team/dau                            │
│  Headers: If-None-Match: "abc123"                              │
│                                                                 │
│  If data unchanged → 304 Not Modified (no body)                │
│  If data changed  → 200 OK with new ETag and new data          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Benefits:**
- ✅ Reduces bandwidth usage (304 responses have no body)
- ✅ Faster responses (no data processing when unchanged)
- ✅ **304 responses don't count against rate limits!**

---

### Step 2: Which APIs Support Caching?

| API | Caching Support | Cache Duration |
|-----|-----------------|----------------|
| **Analytics API** | ✅ Yes (all endpoints) | 15 minutes |
| **AI Code Tracking API** | ✅ Yes | 15 minutes |
| **Admin API** | ❌ No | N/A |
| **Cloud Agents API** | ❌ No | N/A |

**Important:** Use `YYYY-MM-DD` date format for better caching. Timestamps with times prevent cache hits.

---

### Step 3: Make Initial Request and Capture ETag (2 minutes)

**Command:**
```bash
# Make initial request and capture headers
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  -D headers.txt \
  "https://api.cursor.com/analytics/team/dau?startDate=7d&endDate=today"

# Extract ETag
ETAG=$(grep -i "etag" headers.txt | awk '{print $2}' | tr -d '\r')
echo "ETag: $ETAG"
```

**Expected output:**
```
ETag: "abc123xyz789"
```

**Save the ETag for later:**
```bash
echo "$ETAG" > etag.txt
```

---

### Step 4: Make Conditional Request (2 minutes)

Use the ETag to check if data has changed.

**Command:**
```bash
# Get stored ETag
STORED_ETAG=$(cat etag.txt)

# Make conditional request
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  -H "If-None-Match: $STORED_ETAG" \
  -w "\nHTTP Status: %{http_code}\n" \
  "https://api.cursor.com/analytics/team/dau?startDate=7d&endDate=today"
```

**Expected output (data unchanged):**
```
HTTP Status: 304
```
*(No response body – data hasn't changed)*

---

### Step 5: Wait for Cache Expiration or Data Change (1 minute)

Cache duration is 15 minutes. To test a 200 response, either:

**Option A: Wait 15 minutes** (if you have time)
```bash
# Wait 15 minutes
echo "Waiting 15 minutes for cache to expire..."
sleep 900  # 900 seconds = 15 minutes
```

**Option B: Change the date range** (immediate)
```bash
# Use a different date range – new data, new ETag
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  -D headers2.txt \
  "https://api.cursor.com/analytics/team/dau?startDate=14d&endDate=today"

NEW_ETAG=$(grep -i "etag" headers2.txt | awk '{print $2}' | tr -d '\r')
echo "New ETag: $NEW_ETAG"

# This will return 200 with new data
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  -H "If-None-Match: $STORED_ETAG" \
  -w "\nHTTP Status: %{http_code}\n" \
  "https://api.cursor.com/analytics/team/dau?startDate=14d&endDate=today"
```

---

### Step 6: Implement ETag Caching in Python (3 minutes)

Create a reusable caching client.

**Create `caching_client.py`:**
```python
#!/usr/bin/env python3
"""
ETag Caching Client for Cursor APIs
"""

import requests
import json
import os
import sys
from datetime import datetime, timedelta
from functools import wraps

API_KEY = os.environ.get("CURSOR_ADMIN_API_KEY")
if not API_KEY:
    print("❌ Error: Set CURSOR_ADMIN_API_KEY environment variable")
    sys.exit(1)

class CursorCachingClient:
    """API client with ETag caching support"""
    
    def __init__(self, api_key, cache_file="etag_cache.json"):
        self.api_key = api_key
        self.auth = (api_key, "")
        self.cache_file = cache_file
        self.cache = self._load_cache()
    
    def _load_cache(self):
        """Load ETag cache from file"""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def _save_cache(self):
        """Save ETag cache to file"""
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f, indent=2)
    
    def _get_cache_key(self, url, params=None):
        """Generate cache key from URL and params"""
        key = url
        if params:
            # Sort params for consistent keys
            sorted_params = sorted(params.items())
            key += "?" + "&".join(f"{k}={v}" for k, v in sorted_params)
        return key
    
    def get(self, endpoint, params=None):
        """
        Make GET request with ETag caching.
        
        Args:
            endpoint: API endpoint (e.g., "/analytics/team/dau")
            params: Query parameters dictionary
        
        Returns:
            Tuple of (data, from_cache, status_code)
        """
        url = f"https://api.cursor.com{endpoint}"
        cache_key = self._get_cache_key(url, params)
        headers = {"Accept": "application/json"}
        
        # Check cache for ETag
        cached_etag = self.cache.get(cache_key, {}).get("etag")
        if cached_etag:
            headers["If-None-Match"] = cached_etag
        
        # Make request
        response = requests.get(url, auth=self.auth, headers=headers, params=params)
        
        # 304 Not Modified – use cached data
        if response.status_code == 304:
            cached_data = self.cache.get(cache_key, {}).get("data")
            if cached_data:
                print(f"📦 Cache HIT (304) – using cached data from {self.cache[cache_key].get('cached_at', 'unknown')}")
                return cached_data, True, 304
        
        # 200 OK – new data, update cache
        if response.status_code == 200:
            etag = response.headers.get("ETag", "")
            data = response.json()
            
            # Update cache
            self.cache[cache_key] = {
                "etag": etag,
                "data": data,
                "cached_at": datetime.now().isoformat()
            }
            self._save_cache()
            print(f"📡 Cache MISS (200) – new data cached")
            return data, False, 200
        
        # Error – handle appropriately
        print(f"❌ Error: {response.status_code}")
        return None, False, response.status_code
    
    def clear_cache(self):
        """Clear all cached ETags"""
        self.cache = {}
        self._save_cache()
        print("🗑️ Cache cleared")

def demonstrate_caching():
    """Demonstrate ETag caching in action"""
    
    client = CursorCachingClient(API_KEY)
    
    print("🚀 ETag Caching Demo")
    print("=" * 40)
    
    # Test endpoint
    endpoint = "/analytics/team/dau"
    params = {"startDate": "7d", "endDate": "today"}
    
    # Request 1: First request (cache miss)
    print("\n1️⃣ First request (no cache):")
    data, from_cache, status = client.get(endpoint, params)
    if data:
        dau_data = data.get("data", [])
        print(f"   Status: {status}")
        print(f"   From cache: {from_cache}")
        print(f"   Days of data: {len(dau_data)}")
    
    # Request 2: Second request (should be cache hit)
    print("\n2️⃣ Second request (should use cache):")
    data, from_cache, status = client.get(endpoint, params)
    if data:
        print(f"   Status: {status}")
        print(f"   From cache: {from_cache}")
    
    # Request 3: Different date range (cache miss)
    print("\n3️⃣ Different date range (cache miss):")
    params2 = {"startDate": "14d", "endDate": "today"}
    data, from_cache, status = client.get(endpoint, params2)
    if data:
        dau_data = data.get("data", [])
        print(f"   Status: {status}")
        print(f"   From cache: {from_cache}")
        print(f"   Days of data: {len(dau_data)}")
    
    # Show cache contents
    print("\n📦 Cache contents:")
    for key, value in client.cache.items():
        print(f"   {key[:60]}...")
        print(f"      ETag: {value.get('etag', 'N/A')[:20]}...")
        print(f"      Cached at: {value.get('cached_at', 'N/A')}")
    
    # Optional: Clear cache
    # client.clear_cache()

def test_rate_limit_benefit():
    """Demonstrate that 304 responses don't count against rate limits"""
    
    print("\n📊 Rate Limit Benefit Demo")
    print("=" * 40)
    print("304 responses do NOT count against your rate limits!")
    print("ETag caching saves both bandwidth AND rate limit quota.\n")
    
    client = CursorCachingClient(API_KEY)
    endpoint = "/analytics/team/dau"
    params = {"startDate": "7d", "endDate": "today"}
    
    # First request – uses rate limit quota
    print("Request 1: Cache miss (uses 1 request quota)")
    client.get(endpoint, params)
    
    # Subsequent requests – 304 responses, NO rate limit usage
    for i in range(2, 6):
        print(f"Request {i}: Cache hit (304) – NO rate limit usage")
        client.get(endpoint, params)
    
    print("\n✅ 4 subsequent requests used 0 additional rate limit quota!")

if __name__ == "__main__":
    demonstrate_caching()
    test_rate_limit_benefit()
    print("\n✅ Demo complete")
```

**Run the script:**
```bash
export CURSOR_ADMIN_API_KEY="your_key_here"
python3 caching_client.py
```

---

### Step 7: Node.js/JavaScript Version (Optional)

**Create `caching-client.js`:**
```javascript
#!/usr/bin/env node

const https = require('https');
const fs = require('fs');

const API_KEY = process.env.CURSOR_ADMIN_API_KEY;
if (!API_KEY) {
    console.error('❌ Error: Set CURSOR_ADMIN_API_KEY environment variable');
    process.exit(1);
}

class CursorCachingClient {
    constructor(apiKey, cacheFile = 'etag_cache.json') {
        this.apiKey = apiKey;
        this.auth = Buffer.from(`${apiKey}:`).toString('base64');
        this.cacheFile = cacheFile;
        this.cache = this.loadCache();
    }

    loadCache() {
        try {
            if (fs.existsSync(this.cacheFile)) {
                return JSON.parse(fs.readFileSync(this.cacheFile, 'utf8'));
            }
        } catch (e) {}
        return {};
    }

    saveCache() {
        fs.writeFileSync(this.cacheFile, JSON.stringify(this.cache, null, 2));
    }

    getCacheKey(url, params) {
        let key = url;
        if (params) {
            const sortedParams = Object.keys(params).sort().map(k => `${k}=${params[k]}`).join('&');
            key += `?${sortedParams}`;
        }
        return key;
    }

    async get(endpoint, params = {}) {
        const url = `https://api.cursor.com${endpoint}`;
        const cacheKey = this.getCacheKey(url, params);
        const cached = this.cache[cacheKey];
        
        const urlObj = new URL(url);
        Object.keys(params).forEach(k => urlObj.searchParams.append(k, params[k]));
        
        const options = {
            headers: {
                'Authorization': `Basic ${this.auth}`,
                'Accept': 'application/json'
            }
        };
        
        if (cached && cached.etag) {
            options.headers['If-None-Match'] = cached.etag;
        }
        
        return new Promise((resolve, reject) => {
            const req = https.get(urlObj, options, (res) => {
                let data = '';
                
                res.on('data', chunk => data += chunk);
                res.on('end', () => {
                    // 304 Not Modified – use cached data
                    if (res.statusCode === 304 && cached && cached.data) {
                        console.log('📦 Cache HIT (304) – using cached data');
                        resolve({ data: cached.data, fromCache: true, status: 304 });
                        return;
                    }
                    
                    // 200 OK – new data
                    if (res.statusCode === 200) {
                        const jsonData = JSON.parse(data);
                        const etag = res.headers.etag;
                        
                        // Update cache
                        this.cache[cacheKey] = {
                            etag: etag,
                            data: jsonData,
                            cachedAt: new Date().toISOString()
                        };
                        this.saveCache();
                        
                        console.log('📡 Cache MISS (200) – new data cached');
                        resolve({ data: jsonData, fromCache: false, status: 200 });
                        return;
                    }
                    
                    // Error
                    console.error(`❌ Error: ${res.statusCode}`);
                    resolve({ data: null, fromCache: false, status: res.statusCode });
                });
            });
            
            req.on('error', reject);
            req.end();
        });
    }
}

async function main() {
    const client = new CursorCachingClient(API_KEY);
    
    console.log('🚀 ETag Caching Demo (Node.js)');
    console.log('=' .repeat(40));
    
    const endpoint = '/analytics/team/dau';
    const params = { startDate: '7d', endDate: 'today' };
    
    // Request 1: Cache miss
    console.log('\n1️⃣ First request (no cache):');
    const result1 = await client.get(endpoint, params);
    if (result1.data) {
        const dauData = result1.data.data || [];
        console.log(`   Status: ${result1.status}`);
        console.log(`   From cache: ${result1.fromCache}`);
        console.log(`   Days of data: ${dauData.length}`);
    }
    
    // Request 2: Cache hit
    console.log('\n2️⃣ Second request (should use cache):');
    const result2 = await client.get(endpoint, params);
    if (result2.data) {
        console.log(`   Status: ${result2.status}`);
        console.log(`   From cache: ${result2.fromCache}`);
    }
}

main().catch(console.error);
```

**Run the script:**
```bash
export CURSOR_ADMIN_API_KEY="your_key_here"
node caching-client.js
```

---

## Expected Output

### Step 6 Output (Python):
```
🚀 ETag Caching Demo
========================================

1️⃣ First request (no cache):
📡 Cache MISS (200) – new data cached
   Status: 200
   From cache: False
   Days of data: 7

2️⃣ Second request (should use cache):
📦 Cache HIT (304) – using cached data from 2025-01-15T10:30:45.123456
   Status: 304
   From cache: True

3️⃣ Different date range (cache miss):
📡 Cache MISS (200) – new data cached
   Status: 200
   From cache: False
   Days of data: 14

📦 Cache contents:
   /analytics/team/dau?endDate=today&startDate=7d...
      ETag: "abc123xyz789"...
      Cached at: 2025-01-15T10:30:45.123456
   /analytics/team/dau?endDate=today&startDate=14d...
      ETag: "def456uvw012"...
      Cached at: 2025-01-15T10:30:46.234567

📊 Rate Limit Benefit Demo
========================================
304 responses do NOT count against your rate limits!
ETag caching saves both bandwidth AND rate limit quota.

Request 1: Cache miss (uses 1 request quota)
📡 Cache MISS (200) – new data cached
Request 2: Cache hit (304) – NO rate limit usage
📦 Cache HIT (304) – using cached data
Request 3: Cache hit (304) – NO rate limit usage
📦 Cache HIT (304) – using cached data
Request 4: Cache hit (304) – NO rate limit usage
📦 Cache HIT (304) – using cached data
Request 5: Cache hit (304) – NO rate limit usage
📦 Cache HIT (304) – using cached data

✅ 4 subsequent requests used 0 additional rate limit quota!
```

---

## Success Criteria

- [ ] Understood ETag caching concept
- [ ] Captured ETag from initial response
- [ ] Made conditional request with `If-None-Match` header
- [ ] Received 304 response for unchanged data
- [ ] Implemented caching client in Python
- [ ] Verified that 304 responses don't count against rate limits
- [ ] Understood cache duration (15 minutes)

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No ETag in response | Some endpoints don't support caching. Use Analytics or AI Code Tracking API |
| Always getting 200, not 304 | Data may be changing frequently. Try a different endpoint or shorter time range |
| 304 but no cached data | Cache was cleared. Make initial request first |
| 400 Bad Request | Check date format. Use `YYYY-MM-DD` instead of timestamps |
| Caching not working | Verify you're using a caching-supported API (Analytics or AI Code Tracking) |

---

## Key Takeaways

| Concept | Value |
|---------|-------|
| **ETag** | Unique identifier for a resource version |
| **If-None-Match** | Header to check if resource changed |
| **304 Not Modified** | Response when ETag matches (no body) |
| **304 benefits** | No bandwidth, no processing, NO rate limit usage |
| **Cache duration** | 15 minutes (`Cache-Control: public, max-age=900`) |
| **Best practice** | Use `YYYY-MM-DD` date format for better caching |

---

## Best Practices Summary

| Practice | Why |
|----------|-----|
| **Use `YYYY-MM-DD` date format** | Better cache hits than timestamps |
| **Store ETags persistently** | Survive across script runs |
| **Handle 304 responses** | Use cached data when available |
| **Don't cache every 5 minutes** | Cache duration is 15 minutes – respect it |
| **Use 304 to save rate limits** | Each 304 saves a request quota |

---

## Bonus Challenge

Enhance the caching client with:

1. **TTL-based cache invalidation** (force refresh after 15 minutes even without 304)
2. **Parallel request handling** with shared cache
3. **Cache statistics** (hit rate, bytes saved)

```python
def get_with_ttl(self, endpoint, params=None, max_age_seconds=900):
    """Get with time-based cache invalidation"""
    cache_key = self._get_cache_key(endpoint, params)
    cached = self.cache.get(cache_key)
    
    if cached:
        cached_at = datetime.fromisoformat(cached.get("cached_at"))
        age = (datetime.now() - cached_at).total_seconds()
        
        if age < max_age_seconds:
            # Use cache without checking server
            return cached["data"], True, 304
    
    # Cache expired or missing – check server
    return self.get(endpoint, params)
```

---

## Exercise Complete ✓

Check off when done:
- [ ] Captured ETag from initial response
- [ ] Made conditional request with `If-None-Match`
- [ ] Received 304 response
- [ ] Implemented caching client
- [ ] Verified rate limit savings
- [ ] Understood 15-minute cache duration
- [ ] (Bonus) Added TTL-based cache invalidation

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
