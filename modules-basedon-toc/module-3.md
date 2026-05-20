# Module 3: Agent Modes and Tools

## Cursor Training Program — Day 1

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise + concept |
| **Prerequisites** | Completion of Module 2, Cursor installed |
| **Module Goal** | Master the Agent's tools (browser, terminal, search) and understand when to use Ask Mode vs. Agent Mode |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Switch fluidly between Ask Mode and Agent Mode based on task requirements
- Use the Browser Tool to inspect web pages and debug frontend issues
- Use the Terminal Tool to run tests and diagnose failures
- Understand how semantic search differs from grep and when to use each
- Write effective prompts that produce reliable results

---

## Lesson 3.1: Ask Mode vs. Agent Mode

### Concept (10 minutes)

> *"Ask Mode = 'Tell me what you would do' (read-only). Agent Mode = 'Do it' (full access)."*

| Feature | Ask Mode | Agent Mode |
|---------|----------|------------|
| Read files | ✅ Yes | ✅ Yes |
| Search codebase | ✅ Yes | ✅ Yes |
| Explain code | ✅ Yes | ✅ Yes |
| Edit files | ❌ No | ✅ Yes |
| Create files | ❌ No | ✅ Yes |
| Run terminal commands | ❌ No | ✅ Yes |
| **Risk level** | None | Low to medium |
| **Best for** | Exploration, learning, code review | Building, debugging, refactoring |

### How to Switch Modes

| Method | Action |
|--------|--------|
| **Slash command** | Type `/ask`, `/agent`, or `/plan` |
| **Keyboard shortcut** | Press `Shift+Tab` to rotate through modes |
| **Dropdown** | Click the mode selector in the chat input |

### Hands-On Exercise (10 minutes)

**Step 1:** Switch to Ask Mode: `/ask`

**Step 2:** Ask for a change:

> *"Add a comment at the top of the main file"*

**Observe:** The Agent explains what it would do but does NOT modify files.

**Step 3:** Switch to Agent Mode: `/agent`

**Step 4:** Ask the same question:

> *"Add a comment at the top of the main file"*

**Observe:** The Agent actually makes the change.

**Discussion:** When would you use each mode?

| Scenario | Mode | Why |
|----------|------|-----|
| Exploring unfamiliar code | Ask | No risk of unwanted changes |
| Planning a refactor | Ask | Get approach before committing |
| Fixing a known bug | Agent | Need to make changes |
| Adding a new feature | Agent | Need to write code |

**Success Criteria:**
- [ ] Switched to Ask Mode
- [ ] Ask Mode explained without changing files
- [ ] Switched to Agent Mode
- [ ] Agent Mode made the change

---

## Lesson 3.2: Browser Tool

### Concept (10 minutes)

> *"The Browser Tool gives the Agent 'eyes' – it can see and interact with web pages just like a human. This is invaluable for testing web applications and debugging frontend issues."*

**What the Browser Tool Can Do:**

| Capability | Use Case |
|------------|----------|
| Navigate | Go to URLs (localhost or internet) |
| Take screenshots | Capture visual state |
| Read console logs | Debug JavaScript errors |
| Monitor network | See API calls |
| Click elements | Test interactions |
| Type into forms | Automate testing |

### Hands-On Exercise (10 minutes)

**Step 1:** Ask the Agent:

> *"Open the browser and go to https://example.com"*

**Step 2:** Ask:

> *"Take a screenshot of the current page"*

**Step 3:** Ask:

> *"What is the title of this page? What is the main heading?"*

**Step 4 (if you have a local dev server):**

> *"Open the browser to http://localhost:3000"*

> *"Check the console for any errors"*

**Discussion:** How could the Browser Tool help with your daily work?

| Use Case | Benefit |
|----------|---------|
| Testing UI changes | See visual results without manual checking |
| Debugging errors | Agent reads console logs automatically |
| API testing | Agent monitors network traffic |

**Success Criteria:**
- [ ] Agent opened the browser
- [ ] Agent took a screenshot
- [ ] Agent described the page content

---

## Lesson 3.3: Terminal Tool

### Concept (10 minutes)

> *"The Terminal Tool lets the Agent run shell commands – compile code, run tests, install dependencies, check git status. You approve every command before it runs."*

**Command Approval Options:**

| Option | Meaning |
|--------|---------|
| `y` or `Enter` | Run once |
| `a` | Always allow (add to allowlist) |
| `n` | Deny this time |
| `e` | Edit before running |

### Hands-On Exercise (10 minutes)

**Step 1:** Ask the Agent:

> *"Run `ls -la` (Mac/Linux) or `dir` (Windows) and tell me what files you see"*

**Step 2:** Approve the command

**Step 3:** Ask the Agent to run tests (if you have a test suite):

> *"Run the tests and tell me if any fail"*

**Step 4:** Ask the Agent to diagnose a failure (if a test fails):

> *"The test failed. Look at the output and figure out why."*

**Step 5 (if you have a code file):**

> *"Compile and run the main file"*

**Success Criteria:**
- [ ] Agent ran a command
- [ ] You approved the command
- [ ] Output appeared in chat
- [ ] Agent analyzed the output

---

## Lesson 3.4: Effective Prompting in Practice

### Concept (10 minutes)

> *"The way you phrase questions affects which search tools the agent uses and how effective the results are."*

**The Specificity Spectrum:**

```
Specific ←————————————————————————→ Broad
(Exact match)                          (Concepts)
     ↓                                      ↓
"Find function X"              "How does payment work?"
```

| Approach | When to Use | Example |
|----------|-------------|---------|
| **Start specific** | You know what you're looking for | "Find files that import PaymentService" |
| **Go broad** | Exploring unfamiliar territory | "How does our app handle failed payments?" |

### Constrained Prompts vs. Vague Prompts

**Vague Prompt (Avoid):**
> *"Add a user settings page"*

**Problems:** Agent has to guess layout, components, styling, patterns.

**Constrained Prompt (Use):**
> *"Add a user settings page. Look at the existing profile page for our layout pattern. Use the same form components from our UI library. Settings should include: display name (text input), email notifications (toggle), theme preference (dropdown)."*

**Why it works:** References existing files, points to established patterns, defines clear scope.

### The "Explore First" Pattern

> *"A common mistake is asking the agent to change code without first understanding what exists."*

**Bad approach:**
> *"Add form validation to the login page"*

**Good approach:**
> *"Before making any changes, show me how our existing form validation works. What patterns do we use, and where are the shared validators?"*

### Hands-On Exercise (10 minutes)

**Step 1:** Write a vague prompt and observe the response:

> *"Add error handling to this codebase"*

**Step 2:** Write a constrained prompt for the same task:

> *"Look at the existing error handling pattern in `src/utils/errors.ts`. Add similar error handling to the main function. Include logging and user-friendly messages."*

**Step 3:** Compare the responses.

**Discussion:** What made the second prompt more effective?

| Element | Why It Helps |
|---------|--------------|
| Reference to existing file | Agent sees the pattern |
| Specific location | Agent knows where to work |
| Clear requirements | Agent knows what "done" looks like |

**Success Criteria:**
- [ ] Wrote a constrained prompt
- [ ] Agent followed the constraints
- [ ] Understood why constrained prompts work better

---

## Module Summary

| Lesson | Key Skill | Time |
|--------|-----------|------|
| 3.1 | Ask Mode vs. Agent Mode | 10 min |
| 3.2 | Browser Tool | 10 min |
| 3.3 | Terminal Tool | 10 min |
| 3.4 | Effective Prompting | 10 min |

---

## Quick Reference Card

| Action | Method |
|--------|--------|
| Switch to Ask Mode | `/ask` |
| Switch to Agent Mode | `/agent` |
| Switch to Plan Mode | `/plan` or `Shift+Tab` |
| Rotate through modes | `Shift+Tab` |
| Browser navigation | "Open browser to [url]" |
| Take screenshot | "Take a screenshot" |
| Run command | "Run `command`" |
| Approve command | `y` or `Enter` |
| Always allow command | `a` |

---

## Common Pitfalls to Avoid

| Pitfall | Solution |
|---------|----------|
| Using Agent Mode for exploration | Use Ask Mode for read-only questions |
| Vague prompts | Reference specific files and patterns |
| Changing before understanding | "Explore first, then change" |
| Approving commands without review | Always review the command before approving |

---

## Transition to Module 4

> *"Now that you're comfortable with the Agent's core tools and modes, let's look at how to customize Cursor for your team – rules, skills, and more."*

---

*End of Module 3*