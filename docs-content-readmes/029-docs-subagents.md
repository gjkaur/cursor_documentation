This is the **Subagents** documentation – it explains how Cursor's main agent can **delegate tasks to specialized AI assistants**. Each subagent operates in its own context window, handles specific types of work, and returns results to the parent agent.

Think of subagents as **hiring specialists** for different parts of a project – you wouldn't ask a plumber to do electrical work, and you wouldn't ask your main agent to do everything.

Let me break this down for a complete beginner.

---

## What Are Subagents? (The 10-Second Summary)

**Subagents are specialized AI assistants that Cursor's agent can delegate tasks to.** Each subagent has its own context window, handles specific work, and returns results.

| Without Subagents | With Subagents |
|-------------------|----------------|
| Main agent does everything | Delegate to specialists |
| Context gets bloated | Each subagent has isolated context |
| Sequential work only | Parallel execution possible |
| One-size-fits-all prompts | Custom prompts per domain |

> *"Use subagents to break down complex tasks, do work in parallel, and preserve context in the main conversation."*

---

## Why Use Subagents? (4 Key Benefits)

| Benefit | What it means |
|---------|---------------|
| **Context isolation** | Each subagent has its own context window. Long research tasks don't consume space in your main conversation. |
| **Parallel execution** | Launch multiple subagents simultaneously. Work on different parts of your codebase without waiting. |
| **Specialized expertise** | Configure subagents with custom prompts, tool access, and models for domain-specific tasks. |
| **Reusability** | Define custom subagents once and use them across projects. |

**You can use subagents in the editor, CLI, and Cloud Agents.**

---

## How Subagents Work

When the main Agent encounters a complex task, it can **launch a subagent automatically**. 

1. Subagent receives a prompt with necessary context
2. Works autonomously (starts with a **clean context**)
3. Returns a final message with its results

> *"Subagents start with a clean context. The parent agent includes relevant information in the prompt since subagents don't have access to prior conversation history."*

---

## Foreground vs. Background Subagents

Subagents run in one of two modes:

| Mode | Behavior | Best for |
|------|----------|----------|
| **Foreground** | Blocks until subagent completes. Returns result immediately. | Sequential tasks where you need the output |
| **Background** | Returns immediately. Subagent works independently. | Long-running tasks or parallel workstreams |

**Use `is_background: true` in your subagent configuration for background mode.**

---

## Built-in Subagents (Included with Cursor)

Cursor includes **three built-in subagents** that handle context-heavy operations automatically. These were designed based on analysis of agent conversations where context window limits were hit.

| Subagent | Purpose | Why it's a subagent |
|----------|---------|---------------------|
| **Explore** | Searches and analyzes codebases | Codebase exploration generates large intermediate output that would bloat the main context. Uses faster model to run many parallel searches. |
| **Bash** | Runs series of shell commands | Command output is often verbose. Isolating it keeps parent focused on decisions, not logs. |
| **Browser** | Controls browser via MCP tools | Browser interactions produce noisy DOM snapshots and screenshots. |

**You don't need to create these – they're already available!**

---

## Creating Custom Subagents

### Location (Where to Put Subagents)

| Location | Scope |
|----------|-------|
| `.cursor/agents/` | Project-level |
| `.claude/agents/` | Project-level (Claude compatibility) |
| `.codex/agents/` | Project-level (Codex compatibility) |
| `~/.cursor/agents/` | User-level (global) |
| `~/.claude/agents/` | User-level (Claude compatibility) |
| `~/.codex/agents/` | User-level (Codex compatibility) |

**Precedence:** Project subagents take precedence when names conflict. `.cursor/` takes precedence over `.claude/` or `.codex/`.

### Easiest Way to Create a Subagent:

Just ask Agent in chat:

> *"Create a subagent file at .cursor/agents/security-reviewer.md with YAML frontmatter containing name and description. The security-reviewer subagent should audit code for vulnerabilities."*

Agent will generate the file for you!

---

## Subagent File Format (SKILL.md-style)

Each subagent is a markdown file with **YAML frontmatter**:

```markdown
---
name: security-auditor
description: Security specialist. Use when implementing auth, payments, or handling sensitive data.
model: inherit
readonly: true
---

You are a security expert auditing code for vulnerabilities.

When invoked:
1. Identify security-sensitive code paths
2. Check for common vulnerabilities (injection, XSS, auth bypass)
3. Verify secrets are not hardcoded
4. Review input validation and sanitization

Report findings by severity:
- Critical (must fix before deploy)
- High (fix soon)
- Medium (address when possible)
```

---

## Configuration Fields

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| **name** | string | No | Derived from filename | Display name. Use lowercase letters and hyphens. |
| **description** | string | No | - | Short description. Agent reads this to decide delegation. |
| **model** | string | No | `inherit` | `inherit` or specific model ID |
| **readonly** | boolean | No | `false` | If true, no file edits or state-changing commands |
| **is_background** | boolean | No | `false` | If true, runs in background without blocking parent |

---

## Model Configuration

The `model` field controls which model a subagent uses:

| Value | Behavior |
|-------|----------|
| **`inherit`** | Uses same model as parent agent (default) |
| **Specific model ID** | Uses exact model (e.g., `composer-2`, `gpt-5.5`) |

**Choose `inherit` when:** Subagent needs same reasoning power as parent  
**Use specific model when:** You need particular capabilities regardless of parent

---

## Using Subagents (Invocation)

### Automatic Delegation

Agent proactively delegates tasks based on:
- Task complexity and scope
- Custom subagent descriptions
- Current context and available tools

> *"Include phrases like 'use proactively' or 'always use for' in your description field to encourage automatic delegation."*

### Explicit Invocation (Manual)

Request a specific subagent using `/name` syntax:

```
/verifier confirm the auth flow is complete
/debugger investigate this error
/security-auditor review the payment module
```

**Natural language also works:**

> *"Use the verifier subagent to confirm the auth flow is complete"*

---

## Parallel Execution

**Launch multiple subagents simultaneously** for maximum throughput:

> *"Review the API changes and update the documentation in parallel"*

Agent sends multiple Task tool calls in a single message, so subagents run simultaneously.

---

## Resuming Subagents

Subagents can be **resumed** to continue previous conversations. Useful for long-running tasks.

Each subagent execution returns an **agent ID**. Pass this ID to resume:

> *"Resume agent abc123 and analyze the remaining test failures"*

Background subagents write their state as they run. You can resume a subagent after it completes to continue the conversation with preserved context.

---

## Common Patterns

### 1. Verification Agent (Most Important Pattern!)

A **verification agent** independently validates whether claimed work was actually completed. This addresses a common issue where AI marks tasks as done but implementations are incomplete or broken.

```markdown
---
name: verifier
description: Validates completed work. Use after tasks are marked done to confirm quality.
---

You are a skeptical validator. Your job is to verify that work claimed as complete actually works.

When invoked:
1. Identify what was claimed to be completed
2. Check that implementation exists and is functional
3. Run relevant tests or verification steps
4. Look for edge cases that may have been missed

Be thorough and skeptical. Report:
- What was verified and passed
- What was claimed but incomplete or broken
- Specific issues that need to be addressed

Do not accept claims at face value. Test everything.
```

**This pattern is useful for:**
- Validating features work end-to-end before marking tickets complete
- Catching partially implemented functionality
- Ensuring tests actually pass (not just that test files exist)

### 2. Orchestrator Pattern (Planner → Implementer → Verifier)

| Step | Role | Responsibility |
|------|------|----------------|
| 1 | **Planner** | Analyzes requirements and creates technical plan |
| 2 | **Implementer** | Builds feature based on plan |
| 3 | **Verifier** | Confirms implementation matches requirements |

Each handoff includes structured output so the next agent has clear context.

---

## Example Subagents

### Debugger Subagent

```markdown
---
name: debugger
description: Debugging specialist for errors and test failures. Use when encountering bugs.
---

You are an expert debugger specializing in root cause analysis.

When invoked:
1. Capture error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location
4. Implement minimal fix
5. Verify solution works

For each issue, provide:
- Root cause explanation
- Evidence supporting diagnosis
- Specific code fix
- Testing approach
```

### Test Runner Subagent

```markdown
---
name: test-runner
description: Test automation expert. Use proactively to run tests and fix failures.
---

You are a test automation expert.

When you see code changes, proactively run appropriate tests.

If tests fail:
- Analyze failure output
- Identify root cause
- Fix issue while preserving test intent
- Re-run to verify

Report test results with:
- Number of tests passed/failed
- Summary of any failures
- Changes made to fix issues
```

---

## Best Practices

| Practice | Why |
|----------|-----|
| **Write focused subagents** | Each subagent should have a single, clear responsibility. Avoid generic "helper" agents. |
| **Invest in descriptions** | The description field determines when Agent delegates. Spend time refining it. |
| **Keep prompts concise** | Long, rambling prompts dilute focus. Be specific and direct. |
| **Add subagents to version control** | Check `.cursor/agents/` into your repository so the team benefits. |
| **Start with Agent-generated agents** | Let Agent help draft initial configuration, then customize. |

---

## Anti-Patterns to Avoid (What NOT to Do)

| Anti-pattern | Why it's bad |
|--------------|--------------|
| **Too many generic subagents** | Having 50+ subagents with vague instructions like "helps with coding" is ineffective. Agent won't know when to use them. |
| **Vague descriptions** | "Use for general tasks" gives Agent no signal. Be specific: "Use when implementing authentication flows with OAuth providers." |
| **Overly long prompts** | A 2,000-word prompt doesn't make a subagent smarter. It makes it slower and harder to maintain. |
| **Duplicating slash commands** | If a task is single-purpose and doesn't need context isolation, use a slash command instead. |
| **Too many subagents** | Start with 2-3 focused subagents. Add more only when you have clear, distinct use cases. |

---

## Performance and Cost Trade-offs

| Benefit | Trade-off |
|---------|-----------|
| Context isolation | Startup overhead (each subagent gathers its own context) |
| Parallel execution | Higher token usage (multiple contexts running simultaneously) |
| Specialized focus | Latency (may be slower than main agent for simple tasks) |

### Token and Cost Considerations

- **Subagents consume tokens independently** – Each has its own context window
- Running five subagents in parallel uses roughly **five times the tokens** of a single agent
- For quick, simple tasks, the main agent is often faster
- Subagents shine for **complex, long-running work**

---

## Viewing Subagents

Agent includes all custom subagents in its available tools. You can see which subagents are configured by checking the `.cursor/agents/` directory in your project.

**In Cursor Settings:** Subagents appear in the Rules section under available tools.

---

## Common Beginner Questions

### Q: What are the built-in subagents?
**A:** Explore (codebase search), Bash (shell commands), Browser (web automation). They're automatically available.

### Q: Can subagents launch other subagents?
**A:** Yes, subagents can delegate to other subagents (nested delegation).

### Q: How do I see what a subagent is doing?
**A:** Subagent activity appears in the chat/logs.

### Q: What happens if a subagent fails?
**A:** The parent agent is notified and can retry or take alternative action.

### Q: Can I use MCP tools in subagents?
**A:** Yes, subagents have access to the same tools as the main agent (configurable).

### Q: Why is my subagent using a different model?
**A:** Check the `model` field in your subagent configuration. If set to a specific model, it overrides parent.

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **What are subagents?** | Specialized AI assistants that main agent delegates to |
| **Location** | `.cursor/agents/` (project) or `~/.cursor/agents/` (user) |
| **Built-in subagents** | Explore, Bash, Browser |
| **File format** | Markdown with YAML frontmatter (name, description, model, readonly, is_background) |
| **Invocation** | Automatic (based on description) or manual (`/name`) |
| **Execution modes** | Foreground (blocks) or Background (non-blocking) |
| **Key benefit** | Context isolation + parallel execution |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What are Subagents?** | Specialized AI assistants that the main agent can delegate to |
| **Why use them?** | Keep main context clean, run tasks in parallel, specialize expertise |
| **What's built-in?** | Explore (search code), Bash (shell commands), Browser (web) |
| **How do I create one?** | Ask Agent: "Create a subagent file at .cursor/agents/..." |
| **Foreground vs background?** | Foreground = wait for result; Background = fire and forget |
| **Can they run in parallel?** | Yes! Launch multiple simultaneously |

---

## The Bottom Line

**Subagents are like hiring specialists for different tasks – each expert has their own workspace and focuses on what they do best.**

**Think of it as:**
- **Without Subagents** = One person doing everything (slower, context gets messy) 🫠
- **With Subagents** = A team of specialists working in parallel 🦸‍♂️🦸‍♀️🦸

**For beginners:** You don't need to create subagents right away. The built-in subagents (Explore, Bash, Browser) work automatically. When you notice the main agent struggling with context limits or specific domains, that's when you create a custom subagent.

**The most powerful pattern:** **Verification Agent** – have a skeptical subagent double-check work before you trust it. This catches the "AI says it's done but it's actually broken" problem.

**Start simple:** Create one subagent for a task you do repeatedly (like "audit security" or "run tests"). Add more as you identify clear, distinct use cases.

