# Coding Agents – Developing Features

## Complete Beginner's Guide

This document explains the **Developing Features** lesson from the Coding Agents course. It covers how to ship features with agents by breaking work into verifiable steps, using plans, test-driven development, design-to-code workflows, and avoiding common pitfalls.

Let me break this down for a complete beginner.

---

## The Key Insight

> *"The key to shipping features with agents is to break the work into steps the agent can verify on its own. Start every major feature with a plan, then set up the right guardrails so the agent can catch and fix its own mistakes."*

| Without Planning | With Planning |
|-----------------|---------------|
| Agent guesses what to build | Clear, verified plan |
| Wrong direction → wasted time | Editable plan before coding |
| Hard to verify progress | Verifiable steps |

---

## Start with a Plan

> *"Agents can help you think through what to build before you start writing code."*

### Plan Mode Process:

| Step | What Happens |
|------|--------------|
| 1 | Agent researches your codebase |
| 2 | Agent asks clarifying questions |
| 3 | Agent produces a step-by-step plan |
| 4 | You review and edit the plan |
| 5 | Agent builds following the plan |

### Example Clarifying Question:

```
Where should notification preferences be stored?

□ Database (UserPreferences table)
□ localStorage (client-only)
□ Database with localStorage cache
```

> *"When you submit a prompt to plan mode, the agent asks you questions to help figure out the requirements first."*

---

## The Structured Plan

```markdown
# Notification preferences

## Overview
Add a notification preferences page to user settings. Users can toggle email, push, and in-app notifications per category.

## Approach
- Follow existing settings page layout
- Use UserPreferences table with JSONB column
- Reuse existing Toggle component

## Tasks
1. Add notification_preferences column to UserPreferences table
2. Create NotificationPreferences component
3. Add API route
4. Wire up optimistic updates
5. Add tests
```

> *"Cursor makes plans useful by breaking larger requests into smaller, independently verifiable steps. At each step, the agent can measure its progress, confirm the step completed successfully, and move on."*

---

## When to Start Over

> *"Sometimes the agent builds something that misses the mark. Instead of trying to fix it through follow-up prompts, go back to the plan."*

### Wrong Way:

```
Agent builds wrong thing → Try to fix with follow-ups → More wrong → Waste time
```

### Right Way:

```
Agent builds wrong thing → Revert changes → Refine plan → Run again → Correct
```

> *"Starting over from the plan feels counterintuitive, but it's often faster than patching an approach that started with the wrong direction."*

---

## Test-Driven Development (TDD) with Agents

> *"Agents do their best work when they can tell whether their code is correct. When a test fails, the agent can see what went wrong and try again."*

### The TDD Process with Agents:

| Step | Action | Why |
|------|--------|-----|
| **1** | Write tests first | Define expected behavior |
| **2** | Confirm tests fail | Verify tests work (no code yet) |
| **3** | Commit the tests | Lock in requirements |
| **4** | Ask agent to write code | Make all tests pass |
| **5** | Commit the code | Working feature with tests |

> *"Engineers have used test-driven development for a long time, but it wasn't always the most popular way of writing code. With agents, it's much easier to write tests first."*

---

## TDD Example: Write Tests First

**Prompt:**
> *"Write tests for a discountCode() function that:*
> - *Returns the discounted price when given a valid code*
> - *Throws InvalidCodeError for expired codes*
> - *Applies fixed-amount discounts correctly (e.g., "10OFF" = $10 off)*
> - *Never returns a negative price (floor at $0)*
>
> *Follow the test patterns in src/__tests__/pricing.test.ts. Do NOT write the function yet."*

> *"Be explicit you're doing TDD, so it doesn't create mock functions for code that doesn't exist yet."*

### Then: Make the Tests Pass

**Prompt:**
> *"Make all tests in src/__tests__/discountCode.test.ts pass. Follow the service patterns in src/services/PricingService.ts. Do NOT modify the tests."*

---

## Why TDD Works So Well with Agents

> *"Why does this work so well? Because the agent can run tests, see failures, adjust its code, and try again. Each test run gives the agent concrete feedback."*

| Without Tests | With Tests |
|---------------|------------|
| Agent has no idea if code works | Agent sees pass/fail immediately |
| You must manually verify | Agent self-corrects |
| Slow iteration | Fast iteration |

> *"This approach is especially valuable for backend code where you can't verify correctness by looking at a screen."*

---

## Interactive Quiz

The course includes this quiz question:

> *"In a TDD workflow with agents, why should you commit the tests before asking the agent to write the code?"*

| Option | Correct? | Why |
|--------|----------|-----|
| To make the git history cleaner | ❌ No | Not the primary reason |
| **So the agent can't modify the tests to make them pass trivially** | ✅ **Yes** | Lock in requirements |
| Because tests need to be in a separate commit for CI | ❌ No | Not the main reason |

---

## Design to Code

> *"Agents can process and understand images. You can paste a screenshot or mockup directly into the prompt input, and the agent can match the design based on your image."*

### What This Works For:

| Use Case | Example |
|----------|---------|
| **Mockups** | Paste wireframe, ask agent to build component |
| **Visual debugging** | Screenshot unexpected UI, ask agent to investigate |
| **Iteration** | Screenshot current result, describe what needs to change |

### Figma Integration:

> *"You can also connect the Figma MCP server so the agent can pull design tokens, variables, and component specs directly from your Figma files."*

### Integrated Browser:

> *"The integrated browser lets you preview changes as the agent makes them. With this browser, the agent can navigate pages, take screenshots, and verify its own visual output."*

---

## Common Failure Pattern: Building Without Verification

> *"The biggest risk when building features quickly is skipping verification. Agents can generate a lot of code fast, but speed without correctness can create more work down the road."*

### Verification Methods:

| Method | What It Verifies |
|--------|------------------|
| **Tests** | Logic and behavior |
| **Type checking** | Structural correctness |
| **Linters** | Code style and patterns |
| **Browser tools / MCP** | UI changes |

> *"If the agent can't verify its output, you'll end up spending more time making corrections."*

---

## Feature Development Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    FEATURE DEVELOPMENT WORKFLOW                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. START WITH A PLAN                                          │
│     • Use Plan Mode                                            │
│     • Answer clarifying questions                              │
│     • Review and edit plan                                     │
│                    ↓                                           │
│  2. WRITE TESTS FIRST (TDD)                                    │
│     • Define expected behavior                                 │
│     • Confirm tests fail                                       │
│     • Commit tests                                             │
│                    ↓                                           │
│  3. LET AGENT WRITE CODE                                       │
│     • Make all tests pass                                      │
│     • Don't modify tests                                       │
│                    ↓                                           │
│  4. VERIFY                                                     │
│     • Run tests again                                          │
│     • Check type checking                                      │
│     • Lint code                                                │
│     • Preview UI (if applicable)                               │
│                    ↓                                           │
│  5. COMMIT & REPEAT                                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Takeaways

| Concept | Key Insight |
|---------|-------------|
| **Start with a plan** | Agent asks questions, creates editable plan |
| **Start over when wrong** | Revert, refine plan, run again |
| **TDD with agents** | Write tests first, lock in requirements |
| **Tests give feedback** | Agent self-corrects based on failures |
| **Design to code** | Paste images, agent builds components |
| **Verify or else** | Skipping verification creates more work |

---

## Summary for Engineers

| Question | Answer |
|----------|--------|
| **How to start a feature?** | Plan Mode – ask questions, create plan |
| **When to start over?** | Agent builds wrong thing → revert, refine plan |
| **Why TDD with agents?** | Tests give feedback, agent self-corrects |
| **What's the TDD order?** | Tests → Commit tests → Code → Commit code |
| **How to use images?** | Paste mockups, agent builds components |
| **What's the biggest risk?** | Building without verification |

---

## The Bottom Line

**Shipping features with agents is about planning first, writing tests to lock in requirements, and letting the agent verify its own work.**

**Think of it as:**
- **Without plan** = Building without blueprints 🏗️
- **With plan** = Blueprints first, then build 📐
- **Without tests** = Flying blind 🕶️
- **With tests** = GPS with constant feedback 📍

**For your engineers:**
- Start every feature with Plan Mode
- Write tests before code (TDD)
- Commit tests before agent writes code
- Let tests verify correctness
- Use images for UI work
- Never skip verification
