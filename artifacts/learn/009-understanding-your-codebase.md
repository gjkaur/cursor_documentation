# Coding Agents – Understanding Your Codebase

## Complete Beginner's Guide

This document explains the **Understanding Your Codebase** lesson from the Coding Agents course. It covers how agents search through code using different tools, how to ask effective questions, and common failure patterns to avoid.

Let me break this down for a complete beginner.

---

## The Core Problem

> *"One of the most important jobs of a software engineer is building a mental map of a codebase and deeply understanding how the system works. As a project grows, it gets harder and harder to find the right code."*

| Traditional Approach | Agent-Assisted Approach |
|---------------------|------------------------|
| Memorize regex patterns | Describe in natural language |
| Learn specialized tools | Agent uses tools for you |
| Manual searching | Agent finds it automatically |

> *"With coding agents, you can describe what you're looking for in natural language and let the agent use tools to find it for you."*

---

## Two Search Tools

Cursor gives agents two powerful search tools:

| Tool | What It Does | Best For |
|------|--------------|----------|
| **Grep (Instant Grep)** | Exact text matching | Known function names, variables, strings |
| **Semantic Search** | Search by meaning | Unknown exact names, exploring concepts |

---

## 1. Grep / Instant Grep (Exact Matching)

### What It Does:

Finds exact strings in your codebase – function names, variable names, error messages, or regex patterns.

| Tool | Description |
|------|-------------|
| **grep** | Traditional exact string search |
| **ripgrep** | Improved, recursive searching |
| **Instant Grep** | Cursor's custom engine, faster on large codebases |

> *"The most precise way to find a piece of code is to look for an exact match, whether that's the name of a function, a variable, or other parts of code."*

### Example Pattern:

```
import .*PaymentService
```

This finds every file that imports from PaymentService.

> *"You don't need to configure anything or change your behavior to use these tools. Cursor provides them automatically."*

---

## 2. Semantic Search (Search by Meaning)

### What It Does:

Finds code by meaning, even when the exact words aren't in the file.

| Question | Semantic Search Finds |
|----------|----------------------|
| "Where do we handle authentication?" | `middleware/session.ts` (even though "authentication" isn't in the file) |

> *"This is possible because Cursor transforms your codebase into searchable vectors with a custom embedding model. That's a fancy way of saying Cursor builds an understanding of your code symbols mapped back to natural language."*

### The Research:

> *"Research on Cursor's semantic search shows that combining this tool with grep produces 12.5% higher accuracy in answering codebase questions compared to grep alone. The improvement is largest on codebases with 1,000+ files."*

> *"You don't need to configure anything to use this. Cursor automatically indexes your codebase in the background."*

---

## Interactive Quiz

The course includes this quiz question:

> *"Why does Cursor give agents both grep and semantic search?"*

| Option | Correct? | Why |
|--------|----------|-----|
| It doesn't matter; semantic search can handle everything on its own | ❌ No | Semantic search struggles with exact matches |
| **Each tool has strengths: grep finds exact text, semantic search finds concepts. Together they cover more ground** | ✅ **Yes** | Complementary tools |
| So you can manually choose which search tool to run | ❌ No | Agent chooses automatically |

---

## Asking Good Questions (The Spectrum)

The way you phrase questions affects which search tools the agent uses.

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

---

## Example 1: Targeted Search (Specific)

**Prompt:**
> *"Find all files that import from our PaymentService and show me how they handle the PaymentFailedError."*

**What happens:**
- Agent starts with **grep** (exact match)
- Searches for `import.*PaymentService`
- Finds every file referencing the service

> *"The agent starts with grep because the prompt asks for something specific."*

---

## Example 2: Broad Exploration (General)

**Prompt:**
> *"How does our application handle failed payments? Walk me through the error flow from the checkout form to the error message the user sees."*

**What happens:**
- First tool call is **"Search codebase"** (semantic search)
- Finds relevant files by meaning
- Follows up with **grep** to fill in details

> *"Notice how the first tool call is 'Search codebase.' That's the agent using semantic search to find relevant files, then following up with grep to fill in the details."*

---

## The Explore Subagent

> *"The agent can also spawn subagents to complete tasks more efficiently. There's a built-in Explore subagent that helps you search through your codebase."*

### Why Use Explore Subagent?

| Feature | Benefit |
|---------|---------|
| **Own context window** | Doesn't bloat main conversation |
| **Faster model** | Executes many parallel searches |
| **Automatic** | Agent decides when to use it |

> *"You don't have to invoke this manually. The agent will use it when it decides it's relevant."*

### Context Management:

> *"If you're searching through many files in your codebase, this will generate a lot of context. Subagents can significantly improve your context management by only returning their findings and keeping the main conversation focused."*

---

## Architectural Diagrams

> *"For large or unfamiliar codebases, you can ask the agent to generate architectural diagrams, like Mermaid diagrams, to help you visualize your codebase."*

### Prompt Example:

> *"Create a Mermaid diagram showing the data flow for our payment system, including the checkout form, API routes, payment service, and Stripe integration."*

### Benefits of Diagrams:

| Benefit | Why It Matters |
|---------|----------------|
| **Onboarding** | New team members understand faster |
| **Documentation** | Visual reference for the team |
| **Design reviews** | Identify architectural issues |
| **Reveal problems** | Services with too many dependencies, unexpected data flows |

---

## Common Failure Pattern: Changing Before Understanding

> *"A common mistake is asking the agent to change code without first understanding what exists."*

### What Can Go Wrong:

| Problem | Example |
|---------|---------|
| **Duplicates existing code** | Creates new utility when one exists |
| **Wrong patterns** | Uses different pattern than codebase |
| **Breaks conventions** | Doesn't follow established style |

> *"The agent might create a new utility function when one already exists, or use a different pattern than the rest of your codebase."*

---

## The Solution: Explore First

### Bad Approach:

```
"Add form validation to the login page"
```

### Good Approach:

```
"Before making any changes, show me how our existing form validation works. 
What patterns do we use, and where are the shared validators?"
```

> *"Coding agents take your requests literally. Where you don't provide intent, they use their best judgment. Sometimes that works well. But for changes that need to follow existing patterns, you'll get better results when you understand the codebase first and know specifically what to ask for."*

---

## Search Strategy Decision Tree

```
┌─────────────────────────────────────────────────────────────────┐
│                    SEARCH STRATEGY                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Do you know exactly what you're looking for?                  │
│                    ↓                                           │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ YES → Be specific                                       │    │
│  │       "Find files that import PaymentService"           │    │
│  │       Agent uses grep (exact matching)                  │    │
│  └─────────────────────────────────────────────────────────┘    │
│                    ↓                                           │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ NO → Go broad                                          │    │
│  │       "How does payment error handling work?"          │    │
│  │       Agent uses semantic search (by meaning)          │    │
│  └─────────────────────────────────────────────────────────┘    │
│                    ↓                                           │
│  BEFORE MAKING CHANGES: Explore first                         │
│  "Show me existing patterns before changing anything"         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Takeaways

| Concept | Key Insight |
|---------|-------------|
| **Grep** | Exact text matching (function names, variables) |
| **Semantic search** | Find by meaning (concepts, behaviors) |
| **Combine both** | 12.5% higher accuracy |
| **Explore subagent** | Parallel searches, isolated context |
| **Diagrams** | Visualize architecture |
| **Explore before changing** | Understand patterns first |

---

## Summary for Engineers

| Question | Answer |
|----------|--------|
| **What is grep?** | Exact text matching |
| **What is semantic search?** | Find code by meaning |
| **Why combine both?** | 12.5% higher accuracy |
| **What is Explore subagent?** | Parallel search, isolated context |
| **When to be specific?** | When you know exact names |
| **When to go broad?** | Exploring unfamiliar code |
| **What's the common failure?** | Changing before understanding |

---

## The Bottom Line

**Understanding your codebase with agents is about asking the right questions – specific when you know, broad when you're exploring.**

**Think of it as:**
- **Grep** = Ctrl+F on steroids (find exact text) 🔍
- **Semantic search** = "I know what it does, not what it's called" 🧠
- **Explore subagent** = Send a scout to search while you stay focused 🎯

**For your engineers:**
- Start specific when you know what you're looking for
- Go broad when exploring unfamiliar territory
- Always explore before making changes
- Use diagrams to visualize architecture
- Let agents search – you focus on understanding
