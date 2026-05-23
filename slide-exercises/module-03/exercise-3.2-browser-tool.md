# Exercise 3.2: Browser Tool

**Module 3:** Agent Modes and Tools  
**Slides:** `slides/module-03-marp.md` (Lesson 3.2)  
**Time:** 18 min  
**Difficulty:** Beginner

**Objective:** Use the Browser tool so the Agent can inspect live web pages.

---

> **Cursor basics:** Already covered in [Exercise 2.1](../module-02/exercise-2.1-codebase-understanding.md). Skip if you completed that setup.


---

## Steps

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)

**Step 1:** Start a local web app (or use a public test page)
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
python -m http.server 8000
# Or use a public test page
```

---

**Step 2:** In Agent Mode:
**Terminal:** **PowerShell** — ``Ctrl+` `` in Cursor

```
Use the browser tool to open http://localhost:8000
Tell me what you see on the page.
```

---

**Platform:** Windows 10/11 · Agent → ``Ctrl+L`` · Shell → **PowerShell** · Browser for dashboards

**Step 3:** Find specific elements:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
On that same page, find:
1. The main heading text
2. The number of buttons
3. Any error messages visible
```

---

**Step 4:** Check the console:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Now open the browser developer console.
Are there any errors or warnings? If so, what are they?
```

---

**Platform:** Windows 10/11 · Agent → ``Ctrl+L`` · Shell → **PowerShell** · Browser for dashboards

**Step 5:** Diagnose a layout issue:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
The login button is partially hidden on mobile sizes.
Use the browser tool to check what's happening.
```

---

**Step 6:** Extract data from a page:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Go to https://example.com/pricing
Extract all pricing plan names and their monthly costs into a table.
```

---

## Additional reference

## Understanding the Browser Tool

| Feature | What it does |
|---------|--------------|
| **Navigate** | Go to any URL (local or internet) |
| **Screenshot** | Capture image of current page |
| **Click** | Click buttons, links, or elements |
| **Type** | Enter text into form fields |
| **Read console** | View JavaScript console output |
| **Monitor network** | See API calls and network traffic |
| **Scroll** | Move up/down on the page |

---

## Try These Public Websites

| Website | What to Ask |
|---------|-------------|
| `https://example.com` | *"What is this page about?"* |
| `https://cursor.com` | *"What is the main product described on this page?"* |
| `https://github.com` | *"What is the search box placeholder text?"* |
| Any documentation site | *"Find the installation instructions on this page"* |

---

## Expected Agent Response (Example)

Using Option A with `https://example.com`:

```
I'll open the browser and navigate to `https://example.com`.

**Browser opened** – navigating to example.com...

**Page loaded successfully.**

**Screenshot taken** (see attached)

**Observations:**
- Page title: "Example Domain"
- Main heading: "Example Domain"
- Content: This domain is for use in illustrative examples in documents.
- Links: One link to "More information..." (goes to iana.org)

The page is a simple informational page with minimal styling.
```

---

## Browser Pane Location

The browser appears as a pane within Cursor, typically:

| Location | How to find it |
|----------|----------------|
| **Right sidebar** | Next to chat panel |
| **Bottom panel** | Below the code editor |
| **Pop-out window** | Can be detached |

**Tip:** Look for a mini browser window with URL bar and navigation buttons.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Browser pane doesn't appear | Ask: *"Show me the browser window"* or check Cursor Settings → Features → Browser |
| Page won't load | Check internet connection. Try a different URL |
| Screenshot not showing | Ask: *"Take another screenshot and describe what you see"* |
| Agent can't see page content | Make sure page is fully loaded – ask: *"Wait for page to load, then describe it"* |
| Browser is slow | Some sites are heavy. Try simpler sites like `example.com` |

---

## Key Takeaway

**The browser tool gives the Agent "eyes" – it can see and interact with web pages just like a human.**

This is useful for:

- Testing your own web applications
- Debugging UI issues
- Reading documentation online
- Verifying deployed websites
- Checking API response pages

---

## Bonus Challenge (If Time Permits)

Open a local development server:

1. Start a local web server (e.g., `python -m http.server 8080`)
2. Ask: *"Open browser to `http://localhost:8080`"*
3. Ask: *"Take a screenshot of my local project"*

---

## Quick Reference: Browser Tool Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                     BROWSER TOOL CHEAT SHEET                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  NAVIGATE:                                                      │
│  "Open browser to https://example.com"                         │
│                                                                 │
│  SCREENSHOT:                                                    │
│  "Take a screenshot"                                           │
│  "Take a screenshot and describe what you see"                 │
│                                                                 │
│  READ CONTENT:                                                  │
│  "What is the title of this page?"                             │
│  "What are the main headings?"                                 │
│  "Find all links on this page"                                 │
│  "Count how many images are on this page"                      │
│                                                                 │
│  INTERACT:                                                      │
│  "Click the first link"                                        │
│  "Scroll to the bottom of the page"                            │
│  "Type 'cursor' into the search box"                           │
│                                                                 │
│  DEBUG:                                                         │
│  "Show me the console logs"                                    │
│  "What network requests are being made?"                       │
│                                                                 │
│  USEFUL FOR:                                                    │
│  • Testing your web apps                                       │
│  • Reading documentation                                       │
│  • Debugging UI issues                                         │
│  • Verifying deployed sites                                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Related in this repo

For a longer hands-on browser lab (telemetry dashboard, network, console), see [Exercise 8 – Browser Tool (extended lab)](../08-browser-tool/08-browser-tool.md).
