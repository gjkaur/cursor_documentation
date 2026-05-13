# Cursor Training – Exercise 9

## Browser Tool – View Page

**Objective:** Use Cursor's built-in browser tool to open, view, and interact with web pages – allowing the Agent to see and test web interfaces.

**Time:** 10 minutes

**Setup:** No code files needed for this exercise. Just Cursor open.

**This folder:** Open `exercises/exercise-9/` in Cursor. This directory only contains this guide; no `calculator.c` is required.

---

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Cursor (any project or empty workspace) | Cursor window opens |
| 2 | Press `Ctrl+I` (or `Cmd+I` on Mac) to open Agent | Agent panel opens |
| 3 | Ask the Agent to open a web page | Agent opens browser pane |
| 4 | Ask the Agent to take a screenshot | Agent captures and shows the page |
| 5 | Ask questions about the page content | Agent answers based on what it sees |

---

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

## Sample Prompts (Copy-Paste)

### Option A: Open a Web Page

> *"Open the browser and go to `https://example.com`"*

### Option B: Take a Screenshot

> *"Take a screenshot of the current page"*

### Option C: Describe the Page

> *"What is the title of this page? What is the main heading?"*

### Option D: Count Elements

> *"How many paragraphs (`<p>` tags) are on this page?"*

### Option E: Check Links

> *"List all the links on this page"*

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

## Success Criteria

- [ ] Agent opened the browser tool
- [ ] Agent navigated to a URL
- [ ] Page loaded successfully
- [ ] Agent took a screenshot
- [ ] Agent described the page content
- [ ] You saw the browser pane in Cursor

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

## Exercise Complete ✓

Check off when done:

- [ ] Agent opened browser tool
- [ ] Agent navigated to a URL
- [ ] Agent took a screenshot
- [ ] Agent described page content
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 10 – Browser Tool (Read Console)

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
