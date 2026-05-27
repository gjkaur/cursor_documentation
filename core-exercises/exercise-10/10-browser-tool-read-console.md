# Cursor Training – Exercise 10

## Browser Tool – Read Console

**Objective:** Use Cursor's browser tool to read JavaScript console logs, debug errors, and monitor network traffic – essential for web application testing and debugging.

**Time:** 10 minutes

**Setup:** No code files needed. Cursor open, internet connection required.

**This folder:** Open `core-exercises/exercise-10/` in Cursor. This directory only contains this guide; no `calculator.c` is required.

---

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Cursor and press `Ctrl+I` (or `Cmd+I` on Mac) | Agent panel opens |
| 2 | Ask Agent to open a web page with console activity | Browser opens the page |
| 3 | Ask Agent to read console logs | Agent shows console messages |
| 4 | Ask Agent to check for errors | Agent identifies any errors |
| 5 | Ask Agent to monitor network traffic | Agent shows API calls |

---

## Test Pages with Console Activity

Use these pages to see different console behaviors:

### Page 1: Simple Console Message

**URL:** `https://example.com`

> *"Open example.com and show me the console logs"*

*(May have minimal console activity)*

### Page 2: Console Test Page

**URL:** `data:text/html,<script>console.log("Hello from console!");console.warn("This is a warning");console.error("This is an error");</script><h1>Console Test Page</h1><p>Check the console for messages.</p>`

> *"Open this test page and show me all console messages"*

### Page 3: Interactive Demo

**URL:** `https://developer.mozilla.org/en-US/docs/Web/API/Console`

> *"Open the MDN Console documentation and check for any console errors"*

---

## Sample Prompts (Copy-Paste)

### Option A: Read Console Logs

> *"Open the browser to the test page and show me all console messages – log, warn, and error"*

### Option B: Check for Errors

> *"Are there any errors in the console? If yes, what do they say?"*

### Option C: Monitor Network Traffic

> *"Open the browser to cursor.com and show me what network requests are made when the page loads"*

### Option D: Find Specific Console Output

> *"Is there a message that says 'Hello from console!' in the logs?"*

### Option E: Watch for New Messages

> *"Click the button on the page (if any) and tell me what new console messages appear"*

---

## Expected Agent Response (Example)

Using the Console Test Page:

```
I'll open the browser to the console test page.

**Page loaded successfully.**

**Console Logs:**

✅ LOG: "Hello from console!"
⚠️ WARN: "This is a warning"
❌ ERROR: "This is an error"

**Summary:**
- 1 informational log message
- 1 warning (not critical, but should be reviewed)
- 1 error (needs attention)

**No network requests detected on this simple page.**
```

---

## Console Message Types

| Type | Icon | Meaning |
|------|------|---------|
| **Log** | ✅ | Informational message |
| **Info** | ℹ️ | General information |
| **Warn** | ⚠️ | Potential issue, not critical |
| **Error** | ❌ | Something is broken |
| **Debug** | 🔧 | Debugging information |

---

## Network Traffic Information

When monitoring network traffic, Agent can show:

| Information | What it means |
|-------------|---------------|
| **Request URL** | What endpoint was called |
| **Method** | GET, POST, PUT, DELETE |
| **Status Code** | 200 (OK), 404 (Not Found), 500 (Server Error) |
| **Size** | How much data was transferred |
| **Time** | How long the request took |

---

## Debugging a Real Issue (Example)

**Scenario:** A website shows an error but you don't know why.

**Prompt:**

> *"Open browser to `https://httpbin.org/status/404` and check the console. What error do you see? What does it mean?"*

**Expected Agent Response:**

```
I opened httpbin.org/status/404.

**Console Logs:**
No JavaScript console errors – this page intentionally returns a 404 HTTP status.

**Network Traffic:**
- Request to /status/404 returned HTTP 404 Not Found
- This is a server-level error, not a JavaScript error

**Explanation:**
HTTP 404 means the requested resource was not found on the server. The page loaded successfully, but the server responded with a 404 status code.

**To fix:** Check if the URL is correct or if the resource exists on the server.
```

---

## Success Criteria

- [ ] Agent opened a web page in browser
- [ ] Agent read and displayed console logs
- [ ] Agent identified different message types (log, warn, error)
- [ ] Agent checked for errors
- [ ] Agent monitored network traffic (if applicable)
- [ ] You understand what console messages mean

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No console messages shown | Some pages have no console activity. Use the test page with intentional console messages |
| Agent says "cannot access console" | Make sure browser tool is fully loaded. Ask: *"Wait for page to load, then read console"* |
| Network traffic empty | Some pages make no network requests. Try a dynamic site like cursor.com |
| Console shows "CORS error" | That's normal for cross-origin requests – Agent will report it |
| Can't see browser pane | Ask: *"Show me the browser window"* or check Cursor Settings → Features → Browser |

---

## Key Takeaway

**The browser tool can read console logs and network traffic – just like opening DevTools.**

This means the Agent can:

- Debug JavaScript errors automatically
- Check if APIs are responding correctly
- Find warnings that might affect functionality
- Monitor network requests for debugging

**Real-world use case:** *"My web app shows a blank page. Open it and tell me what errors are in the console."*

---

## Bonus Challenge (If Time Permits)

Find a website with intentional console errors:

> *"Find a website that has console errors, open it, and explain what the errors mean"*

Or simulate an error:

> *"Create a simple HTML page with a JavaScript error, open it in browser, and have the Agent diagnose the error"*

---

## Exercise Complete ✓

Check off when done:

- [ ] Agent opened a web page
- [ ] Agent read console logs
- [ ] Agent identified different message types
- [ ] Agent checked for errors
- [ ] Agent monitored network traffic (if applicable)
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 11 – Terminal Tool (Run Tests)

---

## Quick Reference: Console Reading Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                 BROWSER CONSOLE READING CHEAT SHEET             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  READ CONSOLE:                                                  │
│  "Show me the console logs"                                     │
│  "Are there any console errors?"                                │
│  "What warnings are in the console?"                            │
│                                                                 │
│  MONITOR NETWORK:                                               │
│  "Show me network requests"                                     │
│  "What API calls were made?"                                    │
│  "Find the request that returned 404"                           │
│                                                                 │
│  CONSOLE MESSAGE TYPES:                                         │
│  ✅ LOG   - General information                                 │
│  ℹ️ INFO  - Informational                                       │
│  ⚠️ WARN  - Potential issue                                     │
│  ❌ ERROR - Something broke                                     │
│                                                                 │
│  NETWORK STATUS CODES:                                          │
│  200 OK              - Success                                  │
│  301 / 302           - Redirect                                 │
│  400 Bad Request     - Client error                             │
│  401 Unauthorized    - Login needed                             │
│  403 Forbidden       - Access denied                            │
│  404 Not Found       - Page missing                             │
│  500 Server Error    - Server problem                           │
│                                                                 │
│  DEBUGGING WORKFLOW:                                            │
│  1. Open page:     "Open browser to mysite.com"                 │
│  2. Check console: "Show me console errors"                     │
│  3. Check network: "Show me failed requests"                    │
│  4. Agent reports findings                                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Related in this repo

For the earlier browser-tool basics (open a page, screenshot, read content), see [Exercise 9 – Browser Tool (View Page)](../exercise-9/09-browser-tool-view-page.md).
