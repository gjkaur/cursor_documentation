# Module 4: Customizing Cursor for Your Team

## Cursor Training Program — Day 1

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise + walkthrough |
| **Prerequisites** | Completion of Modules 1-3, Cursor installed |
| **Module Goal** | Learn to customize Cursor for team workflows using Rules, Skills, MCP, Hooks, and Subagents |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Create Rules to encode team coding standards and guardrails
- Use AGENTS.md for lightweight project instructions
- Build reusable Skills for specialized workflows
- Understand MCP, Hooks, and Slash workflows for team automation
- Explain how Subagents can delegate specialized work

---

## Lesson 4.1: Creating a Rule

### Concept (10 minutes)

> *"Rules are markdown files stored in `.cursor/rules/` that the agent sees at the start of every conversation. Think of them as always-included instructions that shape how the agent works with your code."*

**What Rules Are Good For:**

| Use Case | Example |
|----------|---------|
| Build/test commands | "Use `npm run test` for tests" |
| Code conventions | "Use ES modules, not CommonJS" |
| Pointers to examples | "See `Button.tsx` for component structure" |
| Guardrails | "Don't modify files in `dist/`" |

**What to Avoid in Rules:**

| Don't | Why |
|-------|-----|
| Copy entire style guides | Use a linter instead |
| Document every command | Agent already knows common tools |
| Over-engineer | Rules are included in every conversation |
| Ignore team sharing | Check rules into git |

> *"A good rule file is short, specific, and points to examples rather than copying them."*

### Rule File Structure

```yaml
---
description: "Brief description of what this rule does"
globs: "**/*.c"  # Optional: only apply to certain files
alwaysApply: true  # Apply to every conversation
---

Your rule content goes here.
Write instructions for the Agent in plain English.
```

### Hands-On Exercise (10 minutes)

**Step 1:** Create the rules directory:

```bash
mkdir -p .cursor/rules
```

**Step 2:** Create `.cursor/rules/coding-standards.mdc`:

```yaml
---
description: "Basic coding standards for C programming"
globs: "**/*.c"
alwaysApply: true
---

## Coding Standards

Follow these standards when writing or modifying C code:

1. Use 4 spaces for indentation (not tabs)
2. Add comments before every function explaining what it does
3. Use descriptive variable names (not single letters except loop counters)
4. Always check for NULL pointers before dereferencing
5. Keep functions under 30 lines when possible
```

**Step 3:** Save the file

**Step 4:** Ask the Agent:

> *"Write a function that calculates the average of an array of integers"*

**Step 5:** Verify the Agent followed the rule (comments before function, 4 spaces, descriptive names)

**Success Criteria:**
- [ ] Created `.cursor/rules/` directory
- [ ] Created a rule file with frontmatter
- [ ] Agent followed the rule when writing code

---

## Lesson 4.2: Repository Instructions (AGENTS.md)

### Concept (5 minutes)

> *"AGENTS.md is a simple markdown file that provides project-level instructions. No YAML, no special formatting – just plain markdown. The Agent reads it automatically."*

**AGENTS.md vs. Rules (.mdc):**

| Feature | AGENTS.md | Rules (.mdc) |
|---------|-----------|--------------|
| Format | Plain markdown | YAML frontmatter + markdown |
| Complexity | Simple | More powerful |
| File location | Project root | `.cursor/rules/` |
| Glob patterns | ❌ No | ✅ Yes |
| Best for | Simple project instructions | Complex, file-specific rules |

### Hands-On Exercise (5 minutes)

**Step 1:** Create `AGENTS.md` in your project root:

```markdown
# Project Instructions

## Coding Standards
- Use snake_case for variable names
- Add comments to all functions
- Keep functions under 20 lines

## Build Instructions
- Run `make` to build
- Run `make test` to test
```

**Step 2:** Ask the Agent:

> *"Create a variable to store the user's age"*

**Step 3:** Verify the Agent used snake_case (`user_age` not `userAge`)

**Success Criteria:**
- [ ] Created `AGENTS.md` in project root
- [ ] Agent followed at least one instruction

---

## Lesson 4.3: Creating and Invoking a Skill

### Concept (10 minutes)

> *"Skills are reusable workflows that teach the agent how to perform specific tasks. Unlike rules, skills are loaded dynamically – the agent decides when to use them based on the task at hand."*

**Rules vs. Skills:**

| Aspect | Rules | Skills |
|--------|-------|--------|
| When loaded | Every conversation | Only when relevant |
| Purpose | Always-on conventions | Specialized workflows |
| Context cost | Always uses space | Only uses full context when invoked |
| Best for | What the agent should always know | What the agent can do when asked |

### Skill File Structure

```
.cursor/skills/
└── skill-name/
    └── SKILL.md
```

**SKILL.md format:**

```yaml
---
name: skill-name
description: What this skill does and when to use it
---

# Skill Title

Step-by-step instructions for the agent...
```

### Hands-On Exercise (10 minutes)

**Step 1:** Create the skills directory:

```bash
mkdir -p .cursor/skills/code-reviewer
```

**Step 2:** Create `.cursor/skills/code-reviewer/SKILL.md`:

```yaml
---
name: code-reviewer
description: Reviews code for quality, bugs, and style issues. Use after writing or modifying code.
---

# Code Reviewer Skill

## Step 1: Understand the Code
- Read the file(s) being reviewed
- Identify the purpose of each function

## Step 2: Check for Issues
- Missing error handling
- Off-by-one errors
- NULL pointer dereferences
- Magic numbers (use constants instead)

## Step 3: Style and Readability
- Are variable names descriptive?
- Is there appropriate comments?
- Is the indentation consistent?

## Step 4: Provide Feedback

### Critical Issues (Must Fix)
- [Issue description with location]

### Suggestions (Should Consider)
- [Suggestion with explanation]

### Nice to Have (Optional)
- [Minor improvement idea]
```

**Step 3:** Invoke the skill:

> *"Use the code-reviewer skill to review the main function"*

**Success Criteria:**
- [ ] Created skill directory and `SKILL.md`
- [ ] Skill has name and description in frontmatter
- [ ] Successfully invoked the skill

---

## Lesson 4.4: MCP, Hooks, and Slash Workflows (Walkthrough)

### Concept (10 minutes)

> *"MCP (Model Context Protocol) lets the agent connect to external tools. Hooks let you run custom scripts before/after agent actions. Slash workflows are reusable commands your team can run."*

### MCP (Model Context Protocol)

**What MCP does:** Universal standard for connecting tools to AI models.

| Integration | What Agent Can Do |
|-------------|-------------------|
| GitHub | List repos, create PRs, read issues |
| Slack | Read messages, post updates |
| Sentry | Look up error details |
| Databases | Query data directly |
| Figma | Pull design tokens |

**MCP Configuration (`~/.cursor/mcp.json`):**

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${env:GITHUB_TOKEN}"
      }
    }
  }
}
```

### Hooks

> *"Hooks let you run custom scripts before or after agent actions – like a security guard checking each action."*

| Hook Point | Purpose |
|------------|---------|
| Before prompt submission | Scan for sensitive data |
| Before file reading | Block access to secrets |
| After code generation | Check for vulnerabilities |
| Before terminal execution | Block dangerous commands |

### Slash Workflows

> *"Slash commands are reusable workflows your team can run with `/command-name`."*

**Example `/pr` skill:**

```yaml
---
description: Create a pull request for the current changes.
---
1. Look at staged and unstaged changes with `git diff`
2. Write a clear commit message
3. Commit and push to current branch
4. Use `gh pr create` to open a pull request
5. Return the PR URL
```

### Demonstration (5 minutes)

**Instructor demonstrates:**

1. Opening MCP settings in Cursor
2. Showing an example `mcp.json` configuration
3. Showing where hooks are configured
4. Creating a simple slash command

**Discussion:** How could your team use these features?

| Feature | Team Use Case |
|---------|---------------|
| MCP | Connect to internal tools |
| Hooks | Security scanning, compliance |
| Slash commands | Standardize team workflows |

---

## Lesson 4.5: Subagents (Walkthrough)

### Concept (5 minutes)

> *"Subagents are specialized AI assistants that the main agent can delegate to. Each subagent has its own context window, so long-running tasks don't clutter the main conversation."*

### Built-in Subagents

| Subagent | Purpose |
|----------|---------|
| **Explore** | Searches and analyzes codebases |
| **Bash** | Runs series of shell commands |
| **Browser** | Controls browser via MCP |

### Custom Subagent Example

**File:** `.cursor/agents/verifier.md`

```yaml
---
name: verifier
description: Validates completed work. Use after tasks are marked done.
readonly: true
---

You are a skeptical validator. Your job is to verify that work claimed as complete actually works.

When invoked:
1. Identify what was claimed to be completed
2. Check that implementation exists and is functional
3. Look for edge cases that may have been missed
4. Report what was verified and what was incomplete
```

### When to Use Subagents

| Use Case | Why |
|----------|-----|
| Long research tasks | Don't bloat main context |
| Parallel exploration | Run multiple searches simultaneously |
| Verification | Double-check work independently |
| Specialized expertise | Custom prompts per domain |

### Demonstration (5 minutes)

**Instructor demonstrates:**

1. Creating a simple subagent
2. Invoking it from the main agent
3. Showing how results return to main conversation

---

## Module Summary

| Lesson | Topic | Format |
|--------|-------|--------|
| 4.1 | Creating a Rule | Hands-on |
| 4.2 | AGENTS.md | Hands-on |
| 4.3 | Creating and Invoking a Skill | Hands-on |
| 4.4 | MCP, Hooks, and Slash Workflows | Walkthrough |
| 4.5 | Subagents | Walkthrough |

---

## Quick Reference Card

| Concept | Location | Purpose |
|---------|----------|---------|
| Rules | `.cursor/rules/` | Always-on instructions |
| AGENTS.md | Project root | Simple project instructions |
| Skills | `.cursor/skills/` | Reusable workflows |
| MCP config | `.cursor/mcp.json` | External tool connections |
| Hooks | `.cursor/hooks.json` | Scripts before/after actions |
| Subagents | `.cursor/agents/` | Specialized assistants |

---

## Best Practices Summary

| Practice | Why |
|----------|-----|
| Start with minimal rules | Add only when you see repeated mistakes |
| Keep rules short and specific | Rules are included in every conversation |
| Check rules into git | Whole team benefits |
| Use skills for complex workflows | Loaded only when needed |
| Use subagents for parallel work | Keep main context clean |

---

## Transition to Day 2

> *"You've now mastered the Cursor editor, Agent tools, and customization. Tomorrow, we'll move to automation and integration – CLI, Cloud Agents, and the Cursor APIs."*

---

*End of Module 4*
*End of Day 1*