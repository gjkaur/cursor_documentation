# Coding Agents – Customizing Agents

## Complete Beginner's Guide

This document explains the **Customizing Agents** lesson from the Coding Agents course. It covers how to modify agents using Rules (static context) and Skills (dynamic context), MCP for external tools, CLI tools, and reusable workflows.

Let me break this down for a complete beginner.

---

## Why Customize Agents?

> *"Coding agents are extremely intelligent without any customization. They have a great understanding of software engineering proven approaches and generally make correct decisions. However, they don't know how your team likes to write software, your preferred tools, or the context of your business."*

| Without Customization | With Customization |
|----------------------|-------------------|
| Agent uses common patterns (Jest, CSS modules) | Agent follows your team's patterns (Vitest, Tailwind) |
| Agent guesses where to put files | Agent knows your conventions |
| Agent repeats same mistakes | Agent learns from rules |

> *"Cursor provides two layers of customization that map to how you'd onboard a new teammate: rules for things they should always know, and skills for specialized knowledge they can pull in when relevant."*

---

## Layer 1: Rules (Static Context)

> *"Rules are markdown files stored in .cursor/rules/ that the agent sees at the start of every conversation. You can think of them as always-included instructions that shape how the agent works with your code."*

### Good Rule Example:

```markdown
# Commands
- `npm run build`: Build the project
- `npm run typecheck`: Run the typechecker
- `npm run test`: Run tests (prefer single test files for speed)

# Code style
- Use ES modules (import/export), not CommonJS (require)
- Destructure imports: `import { foo } from 'bar'`
- See `components/Button.tsx` for canonical component structure

# Workflow
- Always typecheck after making a series of code changes
- API routes go in `app/api/` following existing patterns
```

> *"A good rule file is short, specific, and points to examples rather than copying them."*

### Rules Work Best For:

| Use Case | Example |
|----------|---------|
| **Build/test commands** | "Use `npm run test` for tests" |
| **Code conventions** | "Use ES modules, not CommonJS" |
| **Canonical examples** | "See `Button.tsx` for component structure" |
| **Guardrails** | "Don't modify files in `dist/`" |

---

## What to Avoid in Rules

| Don't | Why |
|-------|-----|
| **Copy entire style guides** | Use a linter instead – rules complement tooling, don't replace it |
| **Document every command** | Agent already knows common tools; add only project-specific ones |
| **Over-engineer** | Rules are included in every conversation – keep them short |
| **Ignore team sharing** | Check rules into git so everyone benefits |

> *"Start simple. Add rules only when you notice the agent making the same mistake repeatedly, and keep them short."*

---

## Layer 2: Skills (Dynamic Context)

> *"Skills extend what your agents can do with specialized knowledge and workflows. Unlike rules, skills are loaded dynamically. The agent decides when to use them based on the task at hand."*

### Skill Example:

```markdown
---
description: Deploy to staging. Use when the user asks to deploy, ship, or push to staging.
---
# Deploy to staging

## Steps
1. Run `npm run build` and confirm it succeeds
2. Run `npm run test` and confirm all tests pass
3. Run `npm run deploy:staging`
4. Verify the deployment by checking https://staging.example.com/health
5. Report the deployment status and URL
```

---

## Rules vs. Skills

| Aspect | Rules | Skills |
|--------|-------|--------|
| **When loaded** | Every conversation | Only when relevant |
| **Purpose** | Always-on conventions | Specialized workflows |
| **Context cost** | Always uses context space | Only uses full context when invoked |
| **Best for** | What the agent should always know | What the agent can do when asked |

> *"A good rule file is short, specific, and points to examples rather than copying them."*

---

## Interactive Quiz

The course includes this quiz question:

> *"You notice the agent keeps using CommonJS require() instead of ES module imports. What's the best fix?"*

| Option | Correct? | Why |
|--------|----------|-----|
| Correct it in each conversation when it happens | ❌ No | Wastes time, doesn't scale |
| **Add a rule: 'Use ES modules (import/export), not CommonJS (require).'** | ✅ **Yes** | Agent learns permanently |
| Create a skill that converts require() to import statements | ❌ No | Overkill for simple convention |

---

## MCP: Connecting to External Tools

> *"MCP (Model Context Protocol) lets the agent connect to external tools and pull in relevant context. MCP servers expose this context and actions the agent can use on demand."*

### Examples of MCP Connections:

| Tool | What Agent Can Do |
|------|-------------------|
| **Slack** | Read messages, post updates |
| **Datadog** | Investigate production logs |
| **Sentry** | Look up error details, stack traces |
| **Databases** | Query data directly |
| **Figma** | Pull design tokens, component specs |

> *"Browse the Marketplace to find servers for the tools you use."*

---

## CLI Tools as Agent Capabilities

> *"Beyond MCP, the agent can run any CLI tool installed in your terminal. Tools like gh, aws, kubectl, and docker work without extra configuration."*

### Rule Example for CLI Tools:

```markdown
- Use `gh` for all GitHub operations (issues, PRs, CI checks)
- Use `aws s3` for file storage operations
```

### Use Case:

> *"Instead of switching to a browser to check CI status or look up an issue, you can ask the agent: 'Check why CI failed on this PR using gh.' It runs the commands, reads the output, and takes action based on it."*

---

## Saving Reusable Workflows (Skills)

> *"You can also invoke skills on demand using / in the agent input. This turns skills into reusable workflows you can trigger by name."*

### Example: `/pr` Skill

```markdown
---
description: Create a pull request for the current changes.
---
1. Look at the staged and unstaged changes with `git diff`
2. Write a clear commit message based on what changed
3. Commit and push to the current branch
4. Use `gh pr create` to open a pull request with title/description
5. Return the PR URL when done
```

### Other Workflows That Work Well as Skills:

| Skill | What It Does |
|-------|---------------|
| `/fix-issue [number]` | Fetch issue details, find code, fix bug, open PR |
| `/review` | Run linters, check common issues, summarize |
| `/update-deps` | Check outdated dependencies, update one by one, run tests after each |

> *"Check these into git so your whole team can run them."*

---

## The Before and After

### Before Rules (Default Agent Behavior):

| Issue | What Agent Does |
|-------|-----------------|
| Testing | Uses Jest (more common in training data) |
| Styling | Creates CSS modules |
| API routes | Puts in random locations |

### After Adding Three Rules:

```markdown
- Tests use Vitest, not Jest. See `src/__tests__/example.test.ts` for patterns.
- Style with Tailwind utility classes. No CSS modules or styled-components.
- API routes go in `app/api/[resource]/route.ts` following existing patterns.
```

### After Rules:

> *"The agent now follows the team's conventions by default. No more correcting the same mistakes in every conversation."*

---

## Common Failure Pattern: Over-Engineering Rules

> *"You might be tempted to write rules for everything. Resist this. Too many rules consume unnecessary context and may confuse the agent."*

| Bad Practice | Good Practice |
|--------------|---------------|
| Rules for everything | Minimal, high-quality rules |
| Static rules that never change | Shared artifact team constantly updates |
| Rules for rare tasks | Use skills for occasional needs |

> *"Keep your rules minimal and high quality. They should be a shared artifact your team is constantly updating. If you only need something occasionally, put it in a skill instead."*

---

## Customization Decision Tree

```
┌─────────────────────────────────────────────────────────────────┐
│                    CUSTOMIZATION DECISION TREE                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  What do you need to customize?                                 │
│                    ↓                                           │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ Does the agent need to ALWAYS know this?                │    │
│  │                    ↓                                    │    │
│  │ YES → Use RULE                                          │    │
│  │       • Coding conventions                              │    │
│  │       • Build/test commands                             │    │
│  │       • Guardrails                                      │    │
│  │                                                         │    │
│  │ NO → Use SKILL                                          │    │
│  │       • Deployment workflows                            │    │
│  │       • Specialized tasks                               │    │
│  │       • Rare but complex procedures                     │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│  Does it need to access external tools?                         │
│  → Use MCP (Slack, Sentry, Datadog, Databases, Figma)          │
│                                                                 │
│  Is it a CLI tool?                                              │
│  → Agent can run directly (gh, aws, kubectl, docker)           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Takeaways

| Concept | Key Insight |
|---------|-------------|
| **Rules** | Always-on instructions in every conversation |
| **Skills** | Dynamically loaded for specialized workflows |
| **MCP** | Connect to external tools (Slack, Sentry, etc.) |
| **CLI tools** | Agent can run any installed CLI tool |
| **Reusable workflows** | Skills invoked with /command |
| **Don't over-engineer** | Minimal rules, use skills for rare tasks |

---

## Summary for Engineers

| Question | Answer |
|----------|--------|
| **What are Rules?** | Always-included instructions (`.cursor/rules/`) |
| **What are Skills?** | Dynamically loaded specialized workflows |
| **When to use Rules?** | What agent should always know |
| **When to use Skills?** | What agent can do when asked |
| **What is MCP?** | Connect to external tools |
| **Can agent run CLI tools?** | Yes – gh, aws, kubectl, docker |
| **How to invoke skills?** | `/skill-name` in agent input |
| **What to avoid?** | Over-engineering rules |

---

## The Bottom Line

**Customizing agents with Rules (always-on) and Skills (on-demand) makes them follow your team's conventions and workflows.**

**Think of it as:**
- **Rules** = Employee handbook (always reference) 📘
- **Skills** = Specialized training modules (learn when needed) 🎓
- **MCP** = Company tools and systems (Slack, Sentry) 🔧
- **CLI tools** = Standard equipment (gh, aws) 🖥️

**For your engineers:**
- Start with minimal rules – add when you see repeated mistakes
- Keep rules short and specific
- Use skills for complex workflows
- Check rules and skills into git
- Connect MCP for external tools
- Create reusable slash commands for common tasks
