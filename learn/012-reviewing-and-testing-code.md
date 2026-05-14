# Coding Agents – Reviewing and Testing Code

## Complete Beginner's Guide

This document explains the **Reviewing and Testing Code** lesson from the Coding Agents course. It covers self-review techniques, preparing for peer review, using Agent Review, Bugbot for PRs, verifiable goals, and testing strategies.

Let me break this down for a complete beginner.

---

## The Core Challenge

> *"Coding agents can produce a lot of code, and that also means they can produce tech debt. Moving fast is great, but you want to keep your quality bar high. Your standards for what gets merged should be the same whether the code was written by hand or by an agent."*

| Human-Written Code | AI-Generated Code |
|--------------------|-------------------|
| Can have bugs | Can have bugs |
| Can miss edge cases | Can miss edge cases |
| Reviewed by humans | Reviewed by humans |
| Same quality standards | Same quality standards |

> *"AI-generated code can look correct but be subtly wrong. It might follow existing patterns, compile, and pass tests you wrote, but still miss edge cases, have security issues, or duplicate logic that exists somewhere else in your codebase."*

---

## Self-Review Techniques

Before asking others to review, review your own code.

### Technique 1: Watch the Agent Work

> *"The diff view shows changes as they happen. If you see the agent heading in the wrong direction, click Stop or press Ctrl+Shift+Backspace to cancel and redirect."*

| Action | When to Use |
|--------|-------------|
| **Stop** | Agent heading wrong direction |
| **Revert & refine plan** | Larger course correction needed |

> *"You don't have to wait until it finishes."*

### Technique 2: Ask Agent to Review All Changes

> *"Tag @Branch in your prompt to give the agent the full diff of your current branch."*

**Prompt Example:**
> *"Review the changes I've made on this branch"*

or

> *"What am I working on right now?"*

> *"This gives the agent rich context and catches issues across many different files."*

### Self-Review Prompt Examples:

**For bugs and issues:**
> *"Review the changes I've made to the discount code feature. Look for bugs, missing error handling, and anything that doesn't match our patterns in src/services/PricingService.ts"*

**For PR preparation:**
> *"What questions will reviewers have about these changes? What context should I include in the PR description?"*

---

## Prepare for Peer Review

> *"Agents can produce many code changes at once. This can result in one large commit with hundreds of changed lines. That's hard for anyone to review."*

### The Problem:

| Bad Commit Hygiene | Good Commit Hygiene |
|--------------------|---------------------|
| One giant commit | Small, semantic commits |
| Hundreds of changed lines | Each commit = one logical change |
| Hard to review | Easy to review step by step |

### The Solution: Use Agents for Commit Housekeeping

> *"This kind of commit housekeeping is tedious by hand, but agents handle it well."*

### Workflow:

| Step | Action |
|------|--------|
| 1 | Build the feature freely (don't worry about commit hygiene) |
| 2 | Once everything works, ask agent to rework commit history |
| 3 | Agent resets to main, reads all changes, plans logical sequence |
| 4 | Agent creates clean commits with descriptive messages |
| 5 | Agent validates final diff matches original (no changes lost) |

### Create a Skill for This:

Create a skill file at `.cursor/skills/rework-commits/SKILL.md` with detailed instructions for the agent to split a branch into reviewable commits.

> *"Use this prompt to create a skill so anyone on your team can run /rework-commits after finishing a feature."*

---

## Agent Review

> *"After the agent finishes a task, click Review then Find Issues to run a dedicated code review. The agent analyzes proposed edits line by line and flags potential problems."*

### How to Use:

| Method | What It Does |
|--------|--------------|
| **After a task** | Click Review → Find Issues |
| **All local changes** | Source Control tab → Agent Review (compares against main branch) |

> *"This is similar to manually prompting the agent to review your changes. We've carefully structured a prompt to make this effective for you."*

---

## Bugbot for Pull Requests

> *"Bugbot integrates with your source control provider to review pull requests automatically."*

### What Bugbot Does:

| Capability | Description |
|------------|-------------|
| **Reviews PRs** | When you push changes |
| **Reads full context** | How modified code connects to codebase |
| **Finds logic errors** | Null pointer exceptions, race conditions, missing error handling, security issues |
| **Proposes fixes** | Autofix – commit directly from PR comment |

> *"Unlike linters, which catch formatting issues, Bugbot finds logic errors."*

### Customization:

> *"You can also customize Bugbot by providing additional rules, which we'll talk more about in the next section on customizing agents."*

---

## Verifiable Goals

> *"To help ensure the correctness of your code, you want to give the agent clear signals to validate its own work."*

### The Three Checks:

| Check | What It Catches |
|-------|-----------------|
| **Tests** | Behavioral regressions |
| **Type checking** | Structural errors |
| **Linting** | Style and pattern violations |

> *"The more of these checks you have in place, the more confidently you can delegate work to agents. We recommend using typed languages with test coverage and linting rules alongside your agent."*

---

## Interactive Quiz

The course includes this quiz question:

> *"Which combination provides the strongest safety net for AI-generated code?"*

| Option | Correct? | Why |
|--------|----------|-----|
| Manual code review only | ❌ No | Misses many issues |
| Automated linting only | ❌ No | Only catches style issues |
| **Tests, type checking, linting, and Bugbot together with human review** | ✅ **Yes** | Multiple layers of verification |

---

## Let Agents Write Your Tests

> *"In the past, building thorough test coverage took significant effort. Most teams would only add tests after something broke. Agents make writing tests much more approachable."*

### Example Prompt:

> *"Write integration tests for the discount code API endpoint and e2e tests for the checkout discount flow. Look at our existing test patterns and match them."*

### Good Prompts for Generating Tests:

| Prompt Type | Example |
|-------------|---------|
| **Plan coverage** | "Plan how to get e2e coverage for our checkout flow. What scenarios should we test?" |
| **Set up tests** | "Set up integration tests for the payments API. Use our existing test infrastructure." |
| **Find gaps** | "What edge cases aren't covered by our current tests for the discount feature?" |
| **Regression tests** | "Write regression tests for the bug we fixed in PaymentService.ts." |

> *"The agent can also help you set up testing infrastructure from scratch. If you don't have Playwright configured for a web application, you can ask the agent to set up the project, write the configuration, and create your first test."*

---

## Cloud Agents

> *"Cloud agents run in remote sandboxes, which means you can close your laptop and check results later."*

### How They Work:

| Step | What Happens |
|------|--------------|
| 1 | Describe the task and provide context |
| 2 | Agent clones your repo and creates a branch |
| 3 | Agent works autonomously |
| 4 | Opens PR when finished |
| 5 | You get notified (Slack, email, web) |
| 6 | Review and merge |

### When to Use Cloud Agents:

| Task Type | Example |
|-----------|---------|
| **Bug fixes** | While working on something else |
| **Test coverage** | For existing code |
| **Documentation updates** | Automate docs |
| **Refactors** | Large, safe changes |

---

## Testing at Scale with Cloud Agents

> *"One powerful pattern is using cloud agents to test many variations in parallel."*

### Example: Testing Discount Code Feature

| Agent | Tests |
|-------|-------|
| Agent 1 | Every discount type |
| Agent 2 | Invalid inputs |
| Agent 3 | Stacking discounts |
| Agent 4 | Edge case boundary values |

> *"Each cloud agent creates a branch with its test cases and results. You can then aggregate the failures into reproducible local test cases and fix them before merging."*

---

## Speed Up Your Feedback Loops

> *"As you start working with more coding agents, the bottleneck moves to the slowest part of your system. That's often waiting for your test suite to finish."*

### The Math:

| Scenario | Time |
|----------|------|
| Tests take 10 minutes | |
| Launch 10 agents in parallel | ~2 hours of waiting |
| Make tests 50% faster | Save almost an hour every time |

> *"These improvements pay off repeatedly across every session, every branch, and every agent."*

### High-Leverage Changes:

| Improvement | Benefit |
|-------------|---------|
| Speeding up test suite | Every agent run faster |
| Trimming dependency tree | Faster installs, builds |
| Optimizing CI pipeline | Less waiting |
| Making type checking faster | Quicker feedback |
| Reducing build times | Faster iterations |

> *"The best part is agents can do this work for you. You can ask an agent to profile your tests and find the slowest ones to fix."*

---

## Common Failure Pattern

> *"Passing tests don't guarantee the code works correctly. It's possible the tests are checking the wrong behavior. The agent might have written code that works for the happy path but doesn't consider all of the edge cases."*

### The Risk:

```
Tests pass → BUT
↓
Tests check wrong behavior
↓
Code has edge case bugs
↓
Production issues
```

### The Solution:

> *"It's important for you to understand the code changes. If the change is too large to review comfortably, consider breaking it into smaller pieces that are easier to review, both for you and for agents."*

---

## Review and Testing Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                 REVIEW & TESTING WORKFLOW                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. SELF-REVIEW                                                │
│     • Watch agent work (diff view)                             │
│     • Tag @Branch for full diff review                         │
│     • Ask agent to review its own work                         │
│                    ↓                                           │
│  2. PREPARE FOR PEER REVIEW                                    │
│     • Use agent to split into small commits                    │
│     • Each commit = one logical change                         │
│                    ↓                                           │
│  3. AUTOMATED CHECKS                                           │
│     • Tests (behavioral)                                       │
│     • Type checking (structural)                               │
│     • Linting (style)                                          │
│     • Bugbot (PR review)                                       │
│                    ↓                                           │
│  4. HUMAN REVIEW                                               │
│     • Understand all changes                                   │
│     • Verify edge cases                                        │
│     • Approve or request changes                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Takeaways

| Concept | Key Insight |
|---------|-------------|
| **Same quality standards** | AI code needs same review as human code |
| **Self-review** | Watch diffs, tag @Branch, ask agent to review |
| **Commit hygiene** | Small, semantic commits for easy review |
| **Agent Review** | Dedicated code review tool |
| **Bugbot** | Automated PR reviews |
| **Verifiable goals** | Tests + type checking + linting |
| **Let agents write tests** | Make testing approachable |
| **Cloud agents** | Test many variations in parallel |
| **Speed feedback loops** | Faster tests = faster agents |

---

## Summary for Engineers

| Question | Answer |
|----------|--------|
| **How to self-review?** | Watch diff, tag @Branch, ask agent |
| **Why small commits?** | Easier for humans to review |
| **What is Agent Review?** | Dedicated code review tool in Cursor |
| **What is Bugbot?** | Automated PR review for logic errors |
| **What three checks?** | Tests, type checking, linting |
| **Why let agents write tests?** | Makes testing approachable |
| **What are cloud agents good for?** | Testing many variations in parallel |
| **What's the common failure?** | Passing tests that check wrong behavior |

---

## The Bottom Line

**Reviewing and testing code is essential for AI-generated code – the same quality standards apply, but agents can help with both writing tests and reviewing changes.**

**Think of it as:**
- **Watch agent work** = Catch mistakes early 👁️
- **Small commits** = Make review manageable 📦
- **Agent Review** = Dedicated code reviewer 🤖
- **Bugbot** = Automated PR reviewer 🔍
- **Tests + types + lints** = Safety net 🛡️

**For your engineers:**
- Review AI-generated code like human code
- Use agents to split into small commits
- Run Agent Review after tasks
- Set up Bugbot for PRs
- Let agents write tests
- Use cloud agents for parallel testing
- Always understand the fix before accepting
