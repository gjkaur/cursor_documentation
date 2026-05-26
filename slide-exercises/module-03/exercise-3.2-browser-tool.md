# Exercise 3.2: Browser Tool

**Module 3:** Agent Modes and Tools  
**Slides:** `slides/module-03-marp.md` (Lesson 3.2)  
**Time:** 18 min  
**Difficulty:** Beginner

**Objective:** Use the Browser tool so the Agent can inspect live web pages.

---

## Cursor basics (read this first)

**Demonstration environment:** These exercises assume **Windows 10/11**. Open the integrated terminal with ``Ctrl+` `` and select **PowerShell** as the default profile.

| Task | Windows (demo) | Mac (optional) | Where in Cursor |
|------|----------------|----------------|-----------------|
| Open a project folder | `Ctrl+K Ctrl+O` or **File → Open Folder** | `Cmd+O` | Title bar / Explorer |
| Open **Agent** panel | `Ctrl+I` | `Cmd+I` | Right side panel |
| Open **Chat** panel | `Ctrl+L` | `Cmd+L` | Side panel (Ask/Chat) |
| Integrated terminal | ``Ctrl+` `` → **PowerShell** | ``Ctrl+` `` | Bottom panel |
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` | Search any command |
| Accept Agent diff | Click **Accept** / **Accept All** | Same | Inline diff in editor |
| Reject Agent diff | Click **Reject** | Same | Inline diff in editor |
| Switch Agent mode | Mode dropdown at bottom of Agent panel | Same | Agent panel footer |
| Toggle Plan Mode | `Shift+Tab` in Agent | Same | Agent panel |

**Windows terminal commands (common in exercises):**

| Task | PowerShell command |
|------|-------------------|
| List files | `dir` or `Get-ChildItem` |
| Show file contents | `Get-Content .\file.txt` or `type file.txt` |
| Run a local `.bat` script | `.\run_tests.bat` |
| Run compiled program | `.\calculator.exe` or `calculator.exe` |
| Set env var (session) | `$env:MY_VAR = "value"` |
| Open HTML in browser | `start index.html` |

**Tip for beginners:** Keep the **Explorer** (left), **editor** (center), and **Agent** (right) visible. Send prompts in the Agent panel; review every diff before accepting.


---

## Steps from the training slides

**Demonstration (Windows):** Follow steps in **PowerShell** unless a step says otherwise. Agent panel: ``Ctrl+I`` · Terminal: ``Ctrl+` ``.

Follow these steps in order. Copy prompts exactly unless the exercise tells you to adapt them.

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent ``Ctrl+I``

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

**Demonstration (Windows):** Agent ``Ctrl+I`` · **PowerShell** · Browser for dashboards

**Step 3:** Find specific elements:
**Where:** **Agent panel** — ``Ctrl+I``

```
On that same page, find:
1. The main heading text
2. The number of buttons
3. Any error messages visible
```

---

**Step 4:** Check the console:
**Where:** **Agent panel** — ``Ctrl+I``

```
Now open the browser developer console.
Are there any errors or warnings? If so, what are they?
```

---

**Demonstration (Windows):** Agent ``Ctrl+I`` · **PowerShell** · Browser for dashboards

**Step 5:** Diagnose a layout issue:
**Where:** **Agent panel** — ``Ctrl+I``

```
The login button is partially hidden on mobile sizes.
Use the browser tool to check what's happening.
```

---

**Step 6:** Extract data from a page:
**Where:** **Agent panel** — ``Ctrl+I``

```
Go to https://example.com/pricing
Extract all pricing plan names and their monthly costs into a table.
```

---

## Detailed reference (expanded instructions)

The section below adds troubleshooting, examples, and extra detail beyond the slides.

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

For a longer hands-on browser lab (telemetry dashboard, network, console), see [Exercise 10 – Browser Tool (Read Console)](../../core-exercises/exercise-10/10-browser-tool-read-console.md).

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
