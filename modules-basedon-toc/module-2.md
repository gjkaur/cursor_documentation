# Module 2: Cursor Editor Essentials

## Cursor Training Program — Day 1

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~90 minutes |
| **Format** | Hands-on exercise |
| **Prerequisites** | Cursor installed and signed in, a Git repository (sample provided if needed) |
| **Module Goal** | Build fluency with core Cursor editor features: codebase understanding, making safe changes, Plan Mode, model selection, @mentions, checkpoints, and terminal integration |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Use the Agent to understand an unfamiliar codebase in minutes
- Get targeted explanations of specific files and functions using @mentions
- Make safe, reviewable changes and understand diffs
- Use Plan Mode to design changes before implementing them
- Compare different models and choose the right one for the task
- Use checkpoints as a safety net for experimental changes
- Let the Agent run terminal commands and react to output

---

## Lesson 2.1: Codebase Understanding

### Concept (5 minutes)

> *"One of the most important jobs of a software engineer is building a mental map of a codebase. With coding agents, you can describe what you're looking for in natural language and let the agent find it for you."*

**The Agent can:**
- Read your entire project structure
- Identify entry points and key modules
- Trace data flow through the system
- Find where specific functionality is implemented

### Hands-On Exercise (10 minutes)

**Setup:** Open any codebase (participants can use their own or download the sample provided).

**Step 1:** Open the Agent (`Ctrl+I` or `Cmd+I` on Mac)

**Step 2:** Copy and paste this prompt:

> *"Explain this codebase in 3-5 sentences. What is the main purpose? Where is the entry point (where does execution start)? List 2-3 key functions and what they do."*

**Step 3:** Press Enter and read the response

**Step 4:** Ask a follow-up:

> *"What are the main dependencies and what do they do?"*

**Expected Outcome:** The participant gets a clear mental map of the project structure.

**Success Criteria:**
- [ ] Agent responded to the prompt
- [ ] Response identified the entry point
- [ ] Response listed at least 2 key functions

---

## Lesson 2.2: Explaining a Specific File or Symbol

### Concept (5 minutes)

> *"The most precise way to get information from the agent is to point it at exactly what you want to talk about. Use @mentions to tell the agent which file or symbol to focus on."*

**Why @mentions matter:**

| Without @mention | With @mention |
|------------------|---------------|
| Agent searches entire codebase | Agent reads exact file you specify |
| May miss the right file | Always references correct file |
| Response may be about wrong code | Response is about code you care about |

### Hands-On Exercise (10 minutes)

**Step 1:** Type `@` in the Agent chat and select a file from your project (e.g., `main.c`, `app.py`, `index.js`)

**Step 2:** Complete your prompt:

> *`@filename` "Explain what this file does. List all functions and what each one does."*

**Step 3:** Compare with a question without @mention:

> *"What does the main function do?"* (without @mention)

**Discussion:** Which response was more accurate and specific?

**Success Criteria:**
- [ ] Used @mention to select a file
- [ ] Agent correctly identified the file
- [ ] Agent listed functions from the file

---

## Lesson 2.3: Making a Safe, Reviewable Change

### Concept (5 minutes)

> *"You are always in control. The Agent shows you exactly what it will change (the diff), and you decide whether to accept it. Checkpoints let you undo anything instantly."*

**Diff Review:**

| Symbol | Meaning |
|--------|---------|
| `+` (green) | Line being ADDED |
| `-` (red) | Line being REMOVED |

**Safe vs. Unsafe Changes:**

| Safe Changes ✅ | Unsafe Changes ❌ |
|-----------------|------------------|
| Adding comments | Deleting entire functions |
| Changing print messages | Modifying core logic |
| Adding whitespace/formatting | Changing function signatures |
| Adding input validation | Removing error handling |

### Hands-On Exercise (10 minutes)

**Step 1:** Ask the Agent:

> *"Add a comment at the top of the main file that says: 'Last updated: [today's date]'"*

**Step 2:** Review the diff (green = added, red = removed)

**Step 3:** Approve the change

**Step 4:** Open the file to verify

**Step 5:** Ask the Agent to make a slightly larger change:

> *"Add a welcome message at the start of the main function"*

**Step 6:** Review the diff again

**Success Criteria:**
- [ ] Agent proposed a change
- [ ] You reviewed the diff
- [ ] You approved the change
- [ ] Change appears in the file

---

## Lesson 2.4: Plan Mode

### Concept (5 minutes)

> *"Plan Mode is like measuring twice and cutting once. Use it when you want to think through a change before the agent writes any code."*

| Normal Agent Mode | Plan Mode |
|-------------------|-----------|
| Starts coding immediately | Plans first, codes second |
| You hope it's right | You approve the plan first |
| Hard to fix if wrong | Easy to edit the plan |

**When to use Plan Mode:**
- Adding a new feature
- Changes affect multiple files
- You're not 100% sure how to implement it
- Someone needs to review the approach first

### Hands-On Exercise (10 minutes)

**Step 1:** Press `Shift+Tab` to switch to Plan Mode

**Step 2:** Ask:

> *"Plan adding a simple print statement that says 'Hello from Cursor!' at the start of the main function. Don't write code yet."*

**Step 3:** Answer any clarifying questions the Agent asks

**Step 4:** Review the generated plan

**Step 5:** Type "Build it" to execute the plan

**Discussion:** How was this different from asking the agent to just "do it"?

**Success Criteria:**
- [ ] Switched to Plan Mode
- [ ] Agent asked clarifying questions
- [ ] Agent created a plan
- [ ] You approved and built the plan

---

## Lesson 2.5: Comparing Two Models

### Concept (5 minutes)

> *"Different models have different strengths. Choose based on task complexity: cheap/fast models for simple questions, expensive/smart models for complex problems."*

| Model | Best For | Cost |
|-------|----------|------|
| GPT-5 Mini | Simple questions, quick answers | $ |
| Composer 2 | Everyday coding (best value) | $$ |
| GPT-5.3 Codex | Coding specialized | $$ |
| Claude 4.6 Sonnet | Balanced daily driver | $$$ |
| Claude 4.7 Opus | Maximum quality | $$$$ |

### Hands-On Exercise (10 minutes)

**Step 1:** Switch to GPT-5 Mini: `/model gpt-5-mini`

**Step 2:** Ask: *"Explain the most complex function in this codebase"*

**Step 3:** Note the response speed and quality

**Step 4:** Switch to Claude 4.6 Sonnet: `/model claude-4.6-sonnet`

**Step 5:** Ask the **exact same question**

**Step 6:** Compare speed and quality

**Discussion:** When would you use each model?

| Model | Speed | Quality | When to Use |
|-------|-------|---------|-------------|
| GPT-5 Mini | | | |
| Claude Sonnet | | | |

**Success Criteria:**
- [ ] Switched between two models
- [ ] Noticed speed difference
- [ ] Noticed quality difference

---

## Lesson 2.6: Precise Context with @mentions

### Concept (3 minutes)

> *"@mentions are like pointing at code and saying 'Look here!' Use them whenever you want the agent to focus on specific files, functions, or folders."*

| @mention Type | Syntax | Use Case |
|---------------|--------|----------|
| File | `@filename.c` | Specific file |
| Folder | `@src/` | All files in a folder |
| Terminals | `@Terminals` | Include terminal output |
| Git commit | `@Commit` | Review uncommitted changes |
| Branch diff | `@Branch (Diff with Main)` | Compare branch changes |

### Hands-On Exercise (10 minutes)

**Step 1:** Ask without @mention:

> *"Find the error handling in this codebase"*

**Step 2:** Now use @mention with a specific file:

> *`@[safety_file]` "Find all error handling in this specific file"*

**Step 3:** Try multiple @mentions:

> *`@file1.c` `@file2.h` "How do these two files work together?"*

**Discussion:** How did the responses differ?

**Success Criteria:**
- [ ] Used @mention with a file
- [ ] Noticed difference with/without @mention
- [ ] Used multiple @mentions

---

## Lesson 2.7: Checkpoints

### Concept (3 minutes)

> *"Checkpoints are automatic snapshots taken before the agent makes significant changes. They're your 'undo' button – click any checkpoint to restore all files to that state."*

| Checkpoints | Git |
|-------------|-----|
| Automatic | Manual commits |
| Per-agent action | Per logical change |
| Temporary safety net | Permanent history |
| One-click restore | Multiple commands |

### Hands-On Exercise (10 minutes)

**Step 1:** Make a small change and note the checkpoint appears

**Step 2:** Make a second change

**Step 3:** Make a third (riskier) change

**Step 4:** Click the **first** checkpoint in the chat timeline

**Step 5:** Click "Preview" to see what the file looked like

**Step 6:** Click "Restore" to revert all files

**Verification:** All three changes are gone

**Success Criteria:**
- [ ] Observed checkpoint creation
- [ ] Previewed a previous state
- [ ] Restored to a checkpoint
- [ ] Files reverted correctly

---

## Lesson 2.8: Terminal Integration

### Concept (3 minutes)

> *"The Agent can run any terminal command you approve. This means it can compile your code, run your tests, check git status, install dependencies, and more."*

**Command Approval Flow:**

```
Agent proposes command → You see it → y/Enter to run, a to always allow, n to deny
```

### Hands-On Exercise (10 minutes)

**Step 1:** Ask the Agent:

> *"Run `ls -la` (Mac/Linux) or `dir` (Windows) and tell me what files you see"*

**Step 2:** Approve the command

**Step 3:** Review the output

**Step 4:** Ask:

> *"Run `pwd` (or `cd`) to show me the current directory path"*

**Step 5:** Ask the Agent to compile and run (if you have a code file):

> *"Compile and run the main file"*

**Success Criteria:**
- [ ] Agent proposed a command
- [ ] You approved the command
- [ ] Output appeared in chat
- [ ] Agent commented on the output

---

## Module Summary

| Lesson | Key Skill | Time |
|--------|-----------|------|
| 2.1 | Codebase Understanding | 10 min |
| 2.2 | Explaining a Specific File | 10 min |
| 2.3 | Making a Safe Change | 10 min |
| 2.4 | Plan Mode | 10 min |
| 2.5 | Comparing Two Models | 10 min |
| 2.6 | @mentions | 10 min |
| 2.7 | Checkpoints | 10 min |
| 2.8 | Terminal Integration | 10 min |

---

## Quick Reference Card

| Action | Shortcut / Command |
|--------|-------------------|
| Open Agent | `Ctrl+I` (Mac: `Cmd+I`) |
| Plan Mode | `Shift+Tab` |
| Switch model | `/model model-name` |
| @mention | `@filename` |
| Checkpoints | Click in chat timeline |
| Approve command | `y` or `Enter` |
| Deny command | `n` |

---

## Transition to Module 3

> *"Now that you're comfortable with the core editor features, let's dive deeper into the Agent's tools – the browser, terminal, and search – and understand when to use Ask Mode vs. Agent Mode."*

---

*End of Module 2*