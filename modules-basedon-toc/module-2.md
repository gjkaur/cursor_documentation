# Module 2: Cursor Editor Essentials

## Cursor Training Program — Day 1 (Hands-On)

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~90 minutes |
| **Format** | Hands-on exercise |
| **Prerequisites** | Module 1 completed, Cursor installed, Git repository access |
| **Module Goal** | Master the core workflows of AI-assisted coding in Cursor |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Orient an AI agent to an unfamiliar codebase
- Get targeted explanations of specific files or symbols
- Make safe, reviewable changes using diff review
- Design complex changes with Plan Mode
- Compare models to choose the right one for each task
- Use @mentions for precise context control
- Navigate checkpoints as a safety net
- Let agents run terminal commands and react to output

---

## Lesson 2.1: Codebase Understanding

### Concept (8 minutes)

> *"Orient an agent to an unfamiliar repository. The single most powerful feature: dropping an agent into a codebase you've never seen and getting a coherent explanation of how it works."*

**The Problem:** Opening a new codebase is overwhelming. Where do you start? What's the entry point? How do things connect?

**The Cursor Solution:** Ask the agent to explain the codebase. It reads files, traces connections, and returns a roadmap.

### Hands-On Exercise (12 minutes)

**Step 1:** Open an unfamiliar repository in Cursor

```bash
# Clone a sample project if you don't have one
git clone https://github.com/facebookresearch/detectron2
cd detectron2
cursor .
```

**Step 2:** Open the Agent (`Cmd+I` or `Ctrl+I`)

**Step 3:** Ask for codebase orientation:

```
Explain this codebase to me as if I'm a new team member.

Specifically tell me:
1. What is the main purpose of this project?
2. What are the entry points (main scripts, CLI, API)?
3. What are the key modules and how do they relate?
4. What are the main dependencies?
5. What files should I read first to understand the architecture?
```

**Step 4:** Ask follow-up questions based on the response:

```
Based on what you just told me, trace the flow of data from input
to output. What functions get called in order?
```

**Step 5:** Ask for a visual overview (the agent can create diagrams):

```
Create an ASCII diagram showing the module relationships in this codebase.
```

**Expected Agent Output:**
```
📁 PROJECT: detectron2 (Facebook AI Research)

PURPOSE:
Object detection and segmentation library built on PyTorch.

ENTRY POINTS:
• train_net.py - Main training script
• demo.py - Inference demo
• Tools/*.py - Various utility scripts

KEY MODULES:
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  config/    │ ←→  │  model_zoo  │ ←→  │  engine/    │
│ (configs)   │     │ (pretrained)│     │ (training)  │
└─────────────┘     └─────────────┘     └─────────────┘
      ↓                    ↓                    ↓
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  structures │     │  modeling/  │     │  data/      │
│ (boxes,masks)│ ←→ │ (architectures)│ ←→ │ (datasets) │
└─────────────┘     └─────────────┘     └─────────────┘

FIRST FILES TO READ:
1. README.md - Project overview
2. detectron2/config/defaults.py - Configuration structure
3. detectron2/engine/defaults.py - Training loop
4. tools/train_net.py - Entry point example

DATA FLOW:
Config → build_model() → DataLoader → Training Loop → Loss → Backprop
```

**Pro Tip:** Save the agent's explanation as a project note:

```
Save this explanation as .cursor/project-overview.md so future
team members can read it.
```

**Success Criteria:**
- [ ] Agent described project purpose
- [ ] Agent identified entry points
- [ ] Agent listed key modules
- [ ] Agent suggested first files to read

---

## Lesson 2.2: Explaining a Specific File or Symbol

### Concept (5 minutes)

> *"Targeted code explanations using precise context. Don't make the agent read the whole codebase when you just need to understand one function."*

### Hands-On Exercise (8 minutes)

**Step 1:** Open a specific file in your project

**Step 2:** Select a function or class you want explained

**Step 3:** Use the Agent with precise context:

```
Explain the function I have selected. For each major section,
tell me:
- What it does
- Why it's designed that way (trade-offs)
- Potential edge cases or bugs
- How it could be improved
```

**Step 4:** Ask for a concrete example:

```
Give me a concrete example of inputs and outputs for this function.
Show me what happens in the normal case and one edge case.
```

**Step 5:** Ask about dependencies:

```
What other functions does this call? What calls this function?
Trace the call chain two levels in each direction.
```

**Alternative: Inline explanation with CMD+L**

```bash
# Shortcut: Select code, press Cmd+L (or Ctrl+L)
# The agent will explain the selected code in the chat panel
```

**Success Criteria:**
- [ ] Selected specific code
- [ ] Agent explained the selection
- [ ] Agent provided input/output examples
- [ ] Agent traced call dependencies

---

## Lesson 2.3: Making a Safe, Reviewable Change

### Concept (5 minutes)

> *"Diff review and approval workflow. Before AI changes your code, you need to see exactly what will change and approve it."*

**The Workflow:**
1. Ask agent to propose a change
2. Review the diff (what's added/removed)
3. Accept or reject changes
4. Test after acceptance

### Hands-On Exercise (8 minutes)

**Step 1:** Ask the agent to make a small, safe change:

```
Change the welcome message in index.html from "Hello World"
to "Welcome to My App"
```

**Step 2:** Watch the agent generate the diff:

```
The agent shows:
📝 Changes to index.html:

  <h1>- Hello World</h1>
  <h1>+ Welcome to My App</h1>

Accept? [Yes] [No] [Edit]
```

**Step 3:** Review the diff carefully

**Key questions to ask yourself:**
- Are the changes only what I asked for?
- Are there unexpected additions or deletions?
- Does the syntax look correct?
- Will this break anything else?

**Step 4:** Accept the change

**Step 5:** Test the change manually

```bash
# For web changes: open in browser
open index.html

# For Python: run the script
python script.py

# For React: check dev server
npm start
```

**Step 6:** If something is wrong, reject and ask for correction:

```
That change didn't work. The button disappeared.
Please explain what happened and suggest a fix.
```

**Success Criteria:**
- [ ] Agent proposed a change
- [ ] Reviewed diff before accepting
- [ ] Accepted only after verification
- [ ] Tested the change

---

## Lesson 2.4: Plan Mode

### Concept (5 minutes)

> *"Designing complex changes before implementation. Plan Mode makes the agent create a detailed plan BEFORE writing any code – perfect for multi-file changes, refactoring, or when you're unsure of the approach."*

**When to use Plan Mode:**
- Changing multiple files
- Adding a new feature
- Refactoring existing code
- You're not 100% sure of the best approach
- The change is risky or hard to undo

### Hands-On Exercise (8 minutes)

**Step 1:** Enable Plan Mode

```bash
# Press Shift+Tab in the Agent input
# The input border changes color to indicate Plan Mode
```

**Step 2:** Describe a complex change:

```
Add user authentication to this web app.

Requirements:
- Email/password login
- Session management
- Protected routes (dashboard, settings)
- Logout functionality
- "Remember me" option

Don't write code yet – just give me a plan.
```

**Step 3:** Review the agent's plan

**A good plan includes:**
```
📋 IMPLEMENTATION PLAN

Step 1: Create User Model
- File: models/user.js
- Fields: email (unique), passwordHash, createdAt, lastLoginAt

Step 2: Set up Authentication Routes
- File: routes/auth.js
- Endpoints: POST /login, POST /logout, POST /register, GET /me

Step 3: Create Session Management
- File: middleware/session.js
- Using: express-session with Redis store

Step 4: Add Protected Route Middleware
- File: middleware/auth.js
- Function: requireAuth

Step 5: Update Frontend
- Files: pages/login.html, pages/dashboard.html
- Add: login form, logout button, redirect logic

Step 6: Environment Variables
- Add to .env: SESSION_SECRET, REDIS_URL

Questions for you:
1. Should I use JWT or server-side sessions?
2. Do you have an existing user database?
3. Should I include email verification?

Ready to proceed? [Yes] [No] [Modify Plan]
```

**Step 4:** Answer questions and approve the plan

```
Use JWT for simplicity. No existing database yet – use SQLite for now.
Skip email verification for this version. Proceed.
```

**Step 5:** Watch the agent execute the plan step by step

**Success Criteria:**
- [ ] Enabled Plan Mode (Shift+Tab)
- [ ] Agent created structured plan
- [ ] Agent asked clarifying questions
- [ ] Approved plan before code was written

---

## Lesson 2.5: Comparing Two Models

### Concept (5 minutes)

> *"Choosing the right model for the task. Different models have different strengths, costs, and speeds. Learn to pick the right tool for the job."*

**Model Selection Guide:**

| Task Type | Recommended Model | Why |
|-----------|-------------------|-----|
| Typo fixes, simple edits | GPT-5 Mini | Cheap, fast, good enough |
| Daily coding, bug fixes | GPT-5.3 Codex or Claude Sonnet | Best value, high quality |
| Complex logic, architecture | Claude Opus or GPT-5.5 | Smartest, but expensive |
| Frontend/visual work | Gemini 3.1 Pro | Can see images |
| Fast, simple questions | Claude Haiku | Fastest responses |

### Hands-On Exercise (8 minutes)

**Step 1:** Ask the same question to two different models

First, set the model selector to Claude Sonnet:

```
Explain what a closure is in JavaScript with a practical example.
```

**Step 2:** Copy the response

**Step 3:** Switch the model to GPT-5 Mini

```
Explain what a closure is in JavaScript with a practical example.
```

**Step 4:** Compare the responses

| Comparison Point | Claude Sonnet | GPT-5 Mini |
|-----------------|---------------|------------|
| Length of response | | |
| Code example quality | | |
| Explanation clarity | | |
| Speed | | |

**Step 5:** Run a cost comparison

```bash
# Check token usage after each request
# Cursor shows token count at bottom of chat
```

**Step 6:** Create a personal decision matrix

```
┌─────────────────────────────────────────────────────────────┐
│              MY MODEL DECISION MATRIX                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  If task is...                    Use model...              │
│                                                              │
│  Typos / text changes            → GPT-5 Mini               │
│  Quick question                  → Claude Haiku             │
│  Daily coding (me)               → GPT-5.3 Codex            │
│  Complex debugging               → Claude Sonnet            │
│  Architecture design             → Claude Opus              │
│  UI/frontend from image          → Gemini Pro               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Success Criteria:**
- [ ] Asked same question to two models
- [ ] Compared response quality and speed
- [ ] Created personal model selection guide

---

## Lesson 2.6: Precise Context with @mentions

### Concept (5 minutes)

> *"Pointing the agent at exact files, symbols, branches, and past chats. @mentions are the precision tool for context – like laser-targeting instead of spraying the whole codebase."*

**What You Can @mention:**

| @mention | What It Does | Example |
|----------|--------------|---------|
| `@filename` | Include specific file | `@auth.py` |
| `@symbol` | Include function/class | `@UserModel` |
| `@branch` | Reference git branch | `@main` |
| `@chat` | Reference past conversation | `@previous-chat` |
| `@folder` | Reference entire directory | `@/src/utils` |
| `@web` | Search the web | `@web pandas DataFrame` |

### Hands-On Exercise (8 minutes)

**Step 1:** Use `@filename` to point at specific file

```
@database.py What are the security vulnerabilities in this database connection?
```

**Step 2:** Use `@symbol` to reference a specific function

```
@calculate_total This function is returning NaN sometimes. Why?
```

**Step 3:** Use multiple @mentions

```
@auth.py @UserModel @login_handler Review the authentication flow.
Are there any race conditions or timing attacks?
```

**Step 4:** Use `@branch` to reference different branch

```
Compare @main and @feature/payment branches.
What are the key differences in the payment handling code?
```

**Step 5:** Use `@chat` to refer to previous conversation

```
@chat(authentication-discussion) Based on that discussion,
implement the fix we agreed on.
```

**Step 6:** Use `@folder` for directory-level context

```
@src/components Find all components that don't have loading states.
```

**Step 7:** Use `@web` for external documentation

```
@web React 19 useTransition hook How do I use it?
```

**Pro Tips:**
- Start typing `@` and Cursor will auto-suggest available mentions
- You can @mention multiple items in one message
- @mentions work in both Agent and Chat modes

**Success Criteria:**
- [ ] Used `@filename` to target specific file
- [ ] Used `@symbol` to target function/class
- [ ] Used multiple @mentions together
- [ ] Used `@web` for external search

---

## Lesson 2.7: Checkpoints

### Concept (4 minutes)

> *"A safety net for experimental changes. Checkpoints let you save the state of your conversation and code changes, then revert if something goes wrong."*

**What Checkpoints Save:**
- Code changes made by the agent
- Conversation history
- File states

**When to Create Checkpoints:**
- Before starting a complex change
- At natural milestones (e.g., after Step 2 of 5)
- When you're about to try something risky
- Before letting the agent run terminal commands

### Hands-On Exercise (4 minutes)

**Step 1:** Before making a change, create a checkpoint

```bash
# Click the checkpoint icon in the Agent panel
# Or use keyboard shortcut (Cmd+Shift+S or Ctrl+Shift+S)
```

**Step 2:** Name your checkpoint descriptively

```
Checkpoint name: "Before auth refactor - safe point"
```

**Step 3:** Let the agent make changes

```
Add input validation to all form handlers.
```

**Step 4:** If something goes wrong, revert to checkpoint

```bash
# Click the checkpoint icon again
# Select "Restore to checkpoint"
# Choose which checkpoint to restore
```

**Step 5:** View checkpoint history

```bash
# In Agent panel, click the clock icon
# Shows all checkpoints with timestamps and names
```

**Checkpoint Best Practices:**
- Create checkpoints every 5-10 minutes during complex work
- Use descriptive names, not "checkpoint1"
- Test the restored state before continuing
- Clean up old checkpoints periodically

**Success Criteria:**
- [ ] Created a checkpoint
- [ ] Made changes after checkpoint
- [ ] Restored to checkpoint
- [ ] Verified restoration worked

---

## Lesson 2.8: Terminal Integration

### Concept (5 minutes)

> *"Letting the agent run and react to terminal commands. The agent can execute commands, see output, and use that output to make decisions."*

**What the Agent Can Do:**
- Run shell commands
- See stdout, stderr, exit codes
- React to command output
- Install dependencies
- Run tests
- Start/stop services

**Safety Features:**
- You approve each command before execution
- Commands appear in terminal for you to see
- You can reject dangerous commands

### Hands-On Exercise (8 minutes)

**Step 1:** Ask the agent to check the environment

```
Run `python --version` and tell me what Python version we're using.
```

**Step 2:** Approve the command when prompted

**Step 3:** Ask the agent to run tests and fix failures

```
Run the test suite. If any tests fail, fix them.
Show me what you're changing.
```

**Step 4:** Watch the agent execute sequentially:

```
Agent: I'll run the tests first.
→ Executing: pytest tests/
→ Output: 7 passed, 2 failed

Agent: Two tests failed. Let me look at them.

→ Reading: tests/test_auth.py

Agent: The login test is failing because the timeout is too short.
I'll increase it from 5 to 10 seconds.

→ Editing: tests/test_auth.py

Agent: Now I'll rerun the tests.
→ Executing: pytest tests/test_auth.py
→ Output: All tests passed

Agent: All tests are now passing.
```

**Step 5:** Ask the agent to install a dependency

```
Install the 'requests' library if it's not already installed.
```

**Step 6:** Ask for a complex terminal workflow

```
Run these commands in order:
1. git checkout main
2. git pull
3. git checkout -b feature/analytics
4. Create a new file called analytics.py
5. Run flake8 to check for style issues
6. Fix any style issues found

Confirm before each command that might affect the repo.
```

**Important Terminal Safety Rules:**

```
┌─────────────────────────────────────────────────────────────┐
│              TERMINAL COMMAND SAFETY RULES                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ALWAYS approve before running:                             │
│  • rm, delete, unlink (file deletion)                       │
│  • sudo, su (privilege escalation)                          │
│  • git push --force (destructive git)                       │
│  • Any command touching production                          │
│                                                              │
│  REVIEW carefully before approving:                         │
│  • npm install / pip install (new dependencies)             │
│  • git commands (branch changes)                            │
│  • docker commands (container management)                   │
│                                                              │
│  SAFE to auto-approve (configure in settings):              │
│  • python --version, node -v (version checks)               │
│  • ls, pwd, cat (read-only commands)                        │
│  • pytest, npm test (running tests)                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Success Criteria:**
- [ ] Agent ran version check command
- [ ] Agent ran tests and reacted to output
- [ ] Agent installed dependency
- [ ] Agent executed multi-step terminal workflow
- [ ] Understood safety rules for terminal commands

---

## Module Summary

| Lesson | Topic | Time | Key Skill |
|--------|-------|------|-----------|
| 2.1 | Codebase Understanding | 12 min | Orient to new repo |
| 2.2 | Explaining Files/Symbols | 8 min | Targeted explanations |
| 2.3 | Safe Reviewable Changes | 8 min | Diff review workflow |
| 2.4 | Plan Mode | 8 min | Design before code |
| 2.5 | Comparing Models | 8 min | Model selection |
| 2.6 | @mentions | 8 min | Precise context |
| 2.7 | Checkpoints | 4 min | Safety net |
| 2.8 | Terminal Integration | 8 min | Command execution |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│              CURSOR EDITOR QUICK REFERENCE                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  SHORTCUTS:                                                 │
│  Cmd/Ctrl + I     → Open Agent                              │
│  Cmd/Ctrl + L     → Explain selected code                   │
│  Shift + Tab      → Toggle Plan Mode                        │
│  Cmd/Ctrl + Shift + S → Create checkpoint                   │
│                                                              │
│  @MENTIONS:                                                 │
│  @filename        → Include specific file                   │
│  @symbol          → Include function/class                  │
│  @branch          → Reference git branch                    │
│  @chat            → Reference past conversation             │
│  @web             → Search the web                          │
│                                                              │
│  SAFE CHANGE WORKFLOW:                                      │
│  1. Ask for change                                          │
│  2. Review diff                                             │
│  3. Accept or reject                                        │
│  4. Test                                                    │
│                                                              │
│  PLAN MODE WORKFLOW:                                        │
│  1. Shift+Tab to enable                                     │
│  2. Describe complex change                                 │
│  3. Review plan                                             │
│  4. Answer questions                                        │
│  5. Approve → Agent executes                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Transition to Module 3

> *"Now that you've mastered the essential Cursor workflows, Module 3 will cover Multi-Model Configuration – using different models for different tasks, managing API keys, and optimizing cost vs. quality."*

---

*End of Module 2*