# Exercise 7.4: ETag Caching

**Module 7:** Cursor API Foundations  
**Slides:** `slides/module-07-marp.md` (Lesson 7.4)  
**Time:** 15 min  
**Difficulty:** Beginner

**Objective:** Use ETags to avoid re-downloading unchanged API data.

---

> **API setup:** Already covered in [Exercise 7.2](../module-07/exercise-7.2-generate-and-test-api-keys.md). Skip if you completed that setup.


---

## Steps

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

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**ETagCache:** persistent pickle-based cache keyed by URL hash

**CachedCursorClient:**
- Check local cache → send `If-None-Match`
- On 304 → return cached data (Cache HIT)
- On 200 → update cache (Cache MISS)

**Batch analytics:** fetch 30 days of usage — unchanged days return 304 instantly

---

## Success criteria

- [ ] Check local cache → send `If-None-Match`
- [ ] On 304 → return cached data (Cache HIT)
- [ ] On 200 → update cache (Cache MISS)
- [ ] Basic ETag request · persistent cache · analytics workload caching

---

## Additional reference

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
