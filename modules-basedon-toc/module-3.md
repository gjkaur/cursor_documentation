# Module 3: Agent Modes and Tools

## Cursor Training Program — Day 1 (Hands-On + Concept)

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise + concept |
| **Prerequisites** | Module 2 completed, live web app available (or sample provided) |
| **Module Goal** | Master different agent modes and the core tools that make agents powerful |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Choose between Ask Mode and Agent Mode based on task and safety needs
- Use the Browser Tool to inspect live pages and read console output
- Run terminal commands through the agent and diagnose failures
- Write effective, constrained prompts that avoid scope creep

---

## Lesson 3.1: Ask Mode vs. Agent Mode

### Concept (10 minutes)

> *"When each is appropriate and the safety implications. Not every AI interaction needs full agent capabilities – sometimes you just want to ask a question."*

### The Core Distinction

| Aspect | Ask Mode | Agent Mode |
|--------|----------|------------|
| **Can read files** | ✅ Yes (with @mentions) | ✅ Yes |
| **Can edit files** | ❌ No | ✅ Yes |
| **Can run terminal** | ❌ No | ✅ Yes |
| **Can browse web** | ❌ No (limited) | ✅ Yes (with tool) |
| **Can call tools** | ❌ No | ✅ Yes |
| **Safety level** | Very high (read-only) | Moderate (needs oversight) |
| **Best for** | Questions, learning, code review | Implementation, debugging, automation |

### When to Use Each Mode

```
┌─────────────────────────────────────────────────────────────┐
│                    MODE SELECTION GUIDE                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  USE ASK MODE when:                                         │
│  • You have a question about code                           │
│  • You want to understand something                         │
│  • You're exploring a codebase                              │
│  • You want a second opinion on design                      │
│  • You're not ready to make changes                         │
│  • You're in a production environment                       │
│                                                              │
│  USE AGENT MODE when:                                       │
│  • You want the AI to write/change code                     │
│  • You need to run and react to commands                    │
│  • You want to browse and extract from web pages            │
│  • You're doing a multi-step task                           │
│  • You're in a development environment                      │
│  • You're prepared to review changes                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Safety Implications

| Risk | Ask Mode | Agent Mode |
|------|----------|------------|
| Unintended code changes | None | Moderate (requires review) |
| File deletion | None | Possible (needs approval) |
| Malicious commands | None | Possible (needs approval) |
| Data leakage | Low | Medium (can read files) |
| API cost | Low (no tool calls) | Higher (multiple tool calls) |

### The Ask Mode → Agent Mode Continuum

```
READ-ONLY ←─────────────────────────────────────→ FULL ACTION
     │                                              │
     ▼                                              ▼
Ask Mode                                      Agent Mode
     │                                              │
     └──────────→ Chat (middle ground) ←───────────┘
               (Can read, can't write)
```

### Hands-On Exercise (8 minutes)

**Step 1:** Start in Ask Mode (default for new chats)

```bash
# Open Agent panel (Cmd+I or Ctrl+I)
# Look at the mode indicator at the bottom of the input
```

**Step 2:** Try to make a change in Ask Mode

```
Change the variable name 'temp' to 'temperature' in the current file.
```

**Expected response:**
```
I'm in Ask Mode, which means I can read code and answer questions,
but I cannot make changes. To make this change, please:

1. Switch to Agent Mode using the dropdown
2. Or make the change manually
3. Or ask me to provide the exact change as a code block you can copy

Would you like me to show you the exact change?
```

**Step 3:** Ask a question that Ask Mode handles well

```
Explain the purpose of the main() function in this file.
What edge cases does it handle?
```

**Step 4:** Switch to Agent Mode

```bash
# Click the mode dropdown at the bottom of the Agent input
# Select "Agent"
# Notice the mode indicator changes color/border
```

**Step 5:** Make the same change request in Agent Mode

```
Change the variable name 'temp' to 'temperature' in the current file.
Show me the diff before I accept.
```

**Expected response (Agent Mode):**
```
I'll change 'temp' to 'temperature'.

📝 Proposed change to script.py:
  def calculate(temp):     → def calculate(temperature):
      return temp * 1.8    →     return temperature * 1.8

Accept? [Yes] [No] [Edit]
```

**Step 6:** Practice mode-switching mid-conversation

```
# Start in Ask Mode
What does this function return?

# Then: "Switch to Agent Mode and fix the off-by-one error"
```

**Success Criteria:**
- [ ] Used Ask Mode for questions
- [ ] Observed Ask Mode cannot make changes
- [ ] Switched to Agent Mode
- [ ] Made a change in Agent Mode
- [ ] Understood when to use each mode

---

## Lesson 3.2: Browser Tool

### Concept (8 minutes)

> *"Inspecting a live page and reading the console. The Browser Tool lets the agent see what your app actually looks like in a browser – not just the source code."*

**What the Browser Tool Can Do:**
- Navigate to URLs
- Read page content and DOM structure
- See console logs and errors
- Take screenshots (depending on model)
- Click elements and interact with pages
- Extract data from live pages

**When to Use Browser Tool:**

| Scenario | Without Browser | With Browser |
|----------|----------------|--------------|
| "Why is the button not showing?" | Guesses from CSS | Sees the actual rendered page |
| "Is the API returning data?" | Checks code | Sees network tab |
| "What console errors?" | Asks you | Reads console directly |
| "Does the responsive layout work?" | Trusts CSS | Actually views at different sizes |

### Hands-On Exercise (10 minutes)

**Step 1:** Start a local web app (or use a public test page)

```bash
# If you have a simple web app
python -m http.server 8000

# Or use a public test page (Cursor can browse external URLs)
```

**Step 2:** In Agent Mode, ask the agent to inspect your page

```
Use the browser tool to open http://localhost:8000
Tell me what you see on the page.
```

**Step 3:** Ask the agent to find specific elements

```
On that same page, find:
1. The main heading text
2. The number of buttons
3. Any error messages visible
```

**Step 4:** Ask the agent to check the console

```
Now open the browser developer console.
Are there any errors or warnings?
If so, what are they?
```

**Expected agent actions:**
```
Agent: I'll use the browser tool to inspect the page.

→ Tool: browser_navigate(url="http://localhost:8000")
→ Result: Page loaded successfully

→ Tool: browser_snapshot()
→ Result: Page structure captured

→ Tool: browser_console_messages()
→ Result: 
   [WARNING] Deprecated API used on line 42
   [ERROR] Failed to load resource: /api/data 404

Agent: I found two issues:
1. A console warning about a deprecated API
2. A 404 error when fetching /api/data
```

**Step 5:** Ask the agent to diagnose a layout issue

```
The login button is partially hidden on mobile sizes.
Use the browser tool to check what's happening.
```

**Step 6:** Ask the agent to extract data from a page

```
Go to https://example.com/pricing
Extract all pricing plan names and their monthly costs into a table.
```

**Browser Tool Limitations:**

| Limitation | Workaround |
|------------|------------|
| Cannot log in to sites | Provide login instructions or session cookies |
| JavaScript-heavy sites may load slowly | Add wait instructions |
| Rate limits on some sites | Space out requests |
| Cannot upload files | Not supported yet |

**Success Criteria:**
- [ ] Agent opened a URL using browser tool
- [ ] Agent read page content
- [ ] Agent checked console for errors
- [ ] Agent extracted structured data from page

---

## Lesson 3.3: Terminal Tool

### Concept (8 minutes)

> *"Running tests and diagnosing real failures. The Terminal Tool lets the agent execute commands, see output, and use that output to make decisions and fix problems."*

**What the Terminal Tool Can Do:**
- Run any shell command (with approval)
- See stdout, stderr, exit codes
- Read command output as context for next actions
- Chain commands based on previous results

**Terminal Tool Architecture:**

```
┌─────────────────────────────────────────────────────────────┐
│                    TERMINAL TOOL FLOW                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User: "Run the tests and fix any failures"                 │
│                    ↓                                         │
│  Agent: I'll run pytest                                      │
│                    ↓                                         │
│  Tool: Execute "pytest tests/"                              │
│                    ↓                                         │
│  Tool returns: Exit code 1, "2 failed, 5 passed"            │
│                    ↓                                         │
│  Agent: Two tests failed. Let me read them.                 │
│                    ↓                                         │
│  Agent: Fixes the code                                      │
│                    ↓                                         │
│  Agent: Rerunning tests...                                  │
│                    ↓                                         │
│  Agent: All tests passed.                                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Hands-On Exercise (12 minutes)

**Step 1:** Ask the agent to check your environment

```
Run these commands and tell me what versions we're using:
- python --version
- node --version (if applicable)
- git --version
```

**Step 2:** Ask the agent to run tests

```
Run the test suite. Show me which tests pass and which fail.
```

**Step 3:** If tests fail, ask the agent to diagnose

```
One or more tests failed. Here's the output:

[Paste actual test output or let agent run it]

What's causing these failures? Look at the specific error messages.
```

**Step 4:** Ask the agent to fix the failures

```
Based on your diagnosis, fix the failing tests.
Show me what you're changing before you run again.
```

**Step 5:** Watch the agent execute a debug workflow

```
I found a bug where the app crashes when input is empty.

1. First, run the app to reproduce the crash
2. Then, add logging to understand why
3. Finally, fix the bug and verify it works
```

**Expected agent behavior:**
```
Agent: I'll reproduce the crash first.

→ Terminal: python app.py
→ Output: Traceback (most recent call last):
         File "app.py", line 23, in process_input
           return data[0]
         IndexError: list index out of range

Agent: The crash happens at line 23 when data is empty.
I'll add a guard condition.

→ Editing: app.py (line 23)

Agent: Now I'll test the fix.

→ Terminal: python app.py --test-empty-input
→ Output: "No data provided" (graceful message)

Agent: Bug fixed. The app now handles empty input gracefully.
```

**Step 6:** Practice reacting to terminal output

```
Run a long-running command (like npm install or pip install).
Watch the output. If there's a warning about deprecated packages,
note it and suggest fixes.
```

**Terminal Safety Rules (Review):**

```
┌─────────────────────────────────────────────────────────────┐
│              TERMINAL TOOL SAFETY RULES                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  APPROVAL REQUIRED (Cursor will prompt):                    │
│  • Any command that writes files (git commit, rm, mv)       │
│  • Commands that change system state (npm install -g)       │
│  • Commands with sudo                                        │
│  • git push (especially --force)                            │
│  • Commands that start servers/daemons                      │
│                                                              │
│  NO APPROVAL NEEDED (configure as safe):                    │
│  • Version checks (python --version)                        │
│  • Read-only commands (cat, ls, head)                       │
│  • Running tests (pytest, npm test)                         │
│  • Git status, git diff                                     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Success Criteria:**
- [ ] Agent ran version check commands
- [ ] Agent ran test suite
- [ ] Agent diagnosed failure from output
- [ ] Agent fixed code based on terminal feedback
- [ ] Agent verified fix by rerunning

---

## Lesson 3.4: Effective Prompting in Practice

### Concept (10 minutes)

> *"Constrained prompts and avoiding scope creep. The best prompts are specific, bounded, and tell the agent what NOT to do as much as what TO do."*

### The Anatomy of an Effective Prompt

```
┌─────────────────────────────────────────────────────────────┐
│                    EFFECTIVE PROMPT STRUCTURE                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. ROLE / CONTEXT (optional but helpful)                   │
│     "You are a senior Python developer..."                  │
│                                                              │
│  2. TASK (specific, actionable)                             │
│     "Fix the bug in calculate_total()..."                   │
│                                                              │
│  3. CONSTRAINTS (what NOT to do)                            │
│     "Do not change the function signature..."               │
│                                                              │
│  4. OUTPUT FORMAT (how to respond)                          │
│     "Show me the diff and explain your change..."           │
│                                                              │
│  5. SUCCESS CRITERIA (how to know it's done)                │
│     "The function should return 0 for empty input..."       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Bad Prompts vs. Good Prompts

| Bad Prompt | Good Prompt | Why It Works |
|------------|-------------|--------------|
| "Fix this code" | "Fix the IndexError in process_list() when the list is empty. Do not change the return type." | Specific error, bound constraints |
| "Add logging" | "Add Python logging to calculate() that logs at INFO level when calculation starts and finishes. Use the existing logger config." | Concrete, uses existing patterns |
| "Make it faster" | "Optimize the search loop in find_user(). Current O(n²). Aim for O(n) or O(n log n). Don't change the function signature." | Measurable goal, preserves interface |
| "Review my code" | "Review auth.py for: 1) Security vulnerabilities (SQL injection, XSS) 2) Password handling issues 3) Session management problems. Ignore style issues." | Focused, specific concerns |

### Constraining Scope: The "Boundaries" Technique

Always tell the agent what NOT to touch:

```markdown
BOUNDARIES:
- Do NOT change: function signatures, return types, existing tests
- Do NOT touch: config files, database schemas, other modules
- Do NOT delete: comments, logging statements, error handling
- Do NOT add: new dependencies, external APIs, global state

Change ONLY: the function body of calculate_total()
```

### Avoiding Scope Creep

**Scope creep example:**
```
User: "Fix the login bug."

Agent: "I fixed the login bug. Also I refactored the authentication module,
added password reset, implemented OAuth, and reorganized your entire codebase."

User: "Wait, I just wanted the login bug fixed!"
```

**How to prevent scope creep:**

| Technique | Example |
|-----------|---------|
| **Explicit boundaries** | "Change ONLY login.js lines 42-56" |
| **One thing at a time** | "First, just identify the issue. Don't fix yet." |
| **Ask for plan first** | "Plan Mode: Show me what you'll change before doing it" |
| **Use checkpoints** | Create checkpoint before complex requests |
| **Prefer diffs over full rewrites** | "Show me the diff, don't replace the whole file" |

### Hands-On Exercise (12 minutes)

**Step 1:** Write a constrained prompt for a specific bug

```
Task: Fix the bug where `get_user_email(user_id)` returns None for valid users.

Constraints:
- Do NOT change the function signature
- Do NOT add new imports
- Do NOT modify other functions
- Do NOT add print statements (use the existing logger)

Output format: Show me the exact diff and explain the root cause.

Success criteria: Function returns the email string for valid user IDs.
```

**Step 2:** Compare response to unconstrained version

First, ask without constraints:
```
Fix get_user_email - it's returning None sometimes.
```

Then compare scope of the response.

**Step 3:** Use the "plan first" technique

```
Before making any changes, answer these questions:

1. What files would need to change?
2. What is the root cause you suspect?
3. What are the risks of your change?
4. Are there alternative approaches?

I will review your answers before approving any code changes.
```

**Step 4:** Practice "negative constraints" (telling what NOT to do)

```
Add error handling to the file parser.

But DO NOT:
- Change the return type (must remain dict)
- Add external dependencies
- Swallow exceptions silently (always log them)
- Change the existing test file
```

**Step 5:** Use the "one change at a time" pattern

```
First, add input validation to the function.
Just show me what you'd add - don't modify the file yet.

[Review]

Now, add the validation. Show the diff before I accept.
```

**Step 6:** Create a reusable prompt template

Save this as `.cursor/prompt-templates.md`:

```markdown
# My Prompt Templates

## Bug Fix Template
Task: [Describe bug]
File: [File path]
Lines: [Range if known]

Constraints:
- Do NOT change: [signatures, imports, other files]
- Do NOT add: [dependencies, global state]

Success criteria: [How to verify fix]

## Feature Addition Template
Task: [Describe feature]
Affected files: [List files]

Plan first: Yes / No

Constraints:
- Do NOT break: [existing functionality]
- Do NOT change: [API contracts]

Testing: [How to test]

## Code Review Template
Files to review: [List files]

Focus areas:
- [Security]
- [Performance]
- [Edge cases]

Ignore:
- [Style, formatting]
- [Non-critical issues]
```

**Success Criteria:**
- [ ] Wrote constrained prompt with boundaries
- [ ] Compared constrained vs unconstrained responses
- [ ] Used "plan first" technique
- [ ] Applied negative constraints ("Do NOT...")
- [ ] Created reusable prompt template

---

## Module Summary

| Lesson | Topic | Time | Key Takeaway |
|--------|-------|------|--------------|
| 3.1 | Ask vs Agent Mode | 10 min | Use Ask for questions, Agent for action |
| 3.2 | Browser Tool | 10 min | Agent can see live pages and console |
| 3.3 | Terminal Tool | 12 min | Agent can run commands and react |
| 3.4 | Effective Prompting | 12 min | Boundaries prevent scope creep |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│              AGENT MODES & TOOLS REFERENCE                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  MODES:                                                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ ASK MODE    | Read-only | Questions, learning       │   │
│  │ AGENT MODE  | Full tools | Implementation, debugging│   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  TOOLS:                                                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ BROWSER     | Navigate, read, console, screenshot   │   │
│  │ TERMINAL    | Execute commands, read output         │   │
│  │ FILE        | Read, edit, create, delete            │   │
│  │ SEARCH      | Code search, symbol lookup            │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  PROMPTING BEST PRACTICES:                                  │
│  • Be specific about the task                               │
│  • Define boundaries (what NOT to change)                   │
│  • Request plan before execution for complex tasks          │
│  • Specify output format (diff, explanation, etc.)          │
│  • Define success criteria                                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Transition to Module 4

> *"Now that you understand agent modes and core tools, Module 4 will cover Multi-Model Configuration – using different models for different tasks, managing API keys, and optimizing cost vs. quality."*

---

*End of Module 3*