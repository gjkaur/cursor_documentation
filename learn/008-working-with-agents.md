# Coding Agents – Working with Agents

## Complete Beginner's Guide

This document explains the **Working with Agents** lesson from the Coding Agents course. It covers how to effectively use coding agents, write effective prompts, manage context, and avoid common failure patterns.

Let me break this down for a complete beginner.

---

## The Big Shift

> *"Developers are now writing a lot of code with agents. Instead of typing every line by hand, they talk to an agent and have it write the code for them."*

| Traditional Coding | Agent-Assisted Coding |
|-------------------|----------------------|
| Type every line manually | Describe what you want |
| Search for solutions | Agent finds patterns |
| Implement step by step | Agent executes autonomously |
| Debug manually | Agent self-corrects |

---

## What Is an Agent Harness?

The agent runs inside a "harness" made of three components:

| Component | What It Is | Who Controls |
|-----------|------------|--------------|
| **Instructions** | System prompt and rules that guide behavior | Cursor + You |
| **Tools** | File editing, codebase search, terminal execution | Built into Cursor |
| **Model** | The AI model you pick for the task | You choose |

> *"Coding agents help you accomplish tasks based on the goals you give them."*

### Model Differences:

| Model Type | Behavior |
|------------|----------|
| Some models | Trained to call shell commands more often |
| Other models | Need more explicit instructions |

> *"With Cursor, our goal is to support every frontier model and optimize the harness as much as possible."*

---

## Writing Effective Prompts

Your first entry point into working with agents is the **prompt** you give them.

### Bad Example: Vague Prompt

```
Add a user settings page
```

**Problems:**
- Agent has to guess the layout
- Doesn't know which components to use
- Unclear styling approach
- No reference to existing patterns

> *"The agent had to guess at everything: what layout you wanted, the components, the styling approach, and more."*

---

### Good Example: Constrained Prompt

```
Add a user settings page.
Look at the existing profile page in src/app/profile/page.tsx for our layout pattern.
Use the same form components from src/components/ui/Form.tsx.

Settings should include:
• Display name (text input)
• Email notifications (toggle)
• Theme preference (dropdown: light, dark, system)

Store settings using our existing useUserPreferences hook.
Follow the same API route pattern as src/app/api/user/profile/route.ts.
```

**Why this works:**
- References specific existing files
- Points to established patterns
- Defines clear scope
- Grounded in your codebase

> *"The second prompt is much better because it gives the agent specific instructions grounded in your codebase: existing files, components, and clear scope. The agent follows your patterns instead of inventing new ones."*

---

## Interactive Quiz

The course includes this quiz question:

> *"Which approach gives agents the best results?"*

| Option | Correct? | Why |
|--------|----------|-----|
| Describe what you want in general terms and let the agent figure it out | ❌ No | Too much guessing |
| **Reference specific files, existing patterns, and define clear scope boundaries** | ✅ **Yes** | Grounded in your codebase |
| Include every file in the project to give maximum context | ❌ No | Wastes tokens, confuses agent |
| Write pseudocode for the agent to translate into real code | ❌ No | Extra work, not necessary |

---

## Managing Your Context

As you work with an agent, your conversation builds up context:

| Context Includes |
|------------------|
| Messages |
| Tool calls |
| File contents |
| And more... |

> *"This context is the agent's working memory, and it has limitations."*

### When to Start Fresh:

| Situation | Action |
|-----------|--------|
| Switching to a new task | Start new conversation |
| Agent making mistakes | Start fresh |
| Agent going in circles | Start fresh (even mid-feature) |

### When to Continue:

| Situation | Action |
|-----------|--------|
| Same feature, useful context | Continue conversation |
| Agent has relevant history | Keep going |

> *"If the agent keeps going in circles, start fresh even if you're mid-feature. You can reference the old conversation to allow the agent to read the chat transcript."*

---

## Referencing Past Conversations

```
Continue the auth refactor from [past chat name]. 
I've addressed the review feedback on the JWT expiry handling. 
Now update the refresh token rotation to invalidate old tokens on use.
```

> *"The latest models are getting very good at finding context for you."*

---

## Let the Agent Find Context

| If you know the exact file | If you don't |
|---------------------------|--------------|
| Tag it with @mention | Give general description |
| "Update @auth.ts" | "Find the authentication files" |

> *"When given tools like semantic search, the agent can pull in relevant files as needed."*

---

## Common Failure Pattern: Scope Creep

> *"One of the most common mistakes is asking for too large of a change without planning."*

### Signs of Scope Creep:

| Sign | What's Happening |
|------|------------------|
| Agent making unrelated changes | Lost focus |
| Editing files you didn't want | Over-reaching |
| Losing focus | Task too large |

### How to Fix:

| Action | Why |
|--------|-----|
| Stop and assess | Recognize the problem |
| Break task into smaller pieces | Manageable chunks |
| Create a plan first | Clear scope |

> *"If you're planning an ambitious feature, we'll cover how to create solid plans and specifications in creating features."*

---

## Iteration Strategy

```
Plan feature → Kick off first conversation → Iterate in smaller follow-up conversations
```

> *"Once you have that plan and kick off the first conversation, it's often faster to iterate in smaller follow-up conversations after that."*

---

## Key Takeaways

| Concept | Key Insight |
|---------|-------------|
| **Agent harness** | Instructions + Tools + Model |
| **Effective prompts** | Reference existing files and patterns |
| **Context management** | Start fresh when agent struggles |
| **Scope creep** | Break large tasks into smaller pieces |
| **Delegation** | Let agent find context when possible |

---

## Prompt Comparison Table

| Aspect | Vague Prompt | Constrained Prompt |
|--------|--------------|-------------------|
| **Layout** | Agent guesses | References existing page |
| **Components** | Unknown | Points to specific form components |
| **Scope** | Open-ended | Clear list of settings |
| **Patterns** | Invents new ones | Follows existing hooks and routes |
| **Result** | Inconsistent | Follows your codebase patterns |

---

## Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    WORKING WITH AGENTS                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Write effective prompt                                     │
│     • Reference specific files                                 │
│     • Point to existing patterns                               │
│     • Define clear scope                                       │
│                    ↓                                           │
│  2. Agent executes with tools                                  │
│                    ↓                                           │
│  3. Monitor for scope creep                                   │
│     • Unrelated changes?                                       │
│     • Losing focus?                                            │
│     • Going in circles?                                        │
│                    ↓                                           │
│  4. Either continue or start fresh                            │
│     • Same feature → Continue                                 │
│     • Stuck/confused → Start fresh                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## What's Next

The course will cover:

| Topic | What You'll Learn |
|-------|-------------------|
| **Codebase understanding** | How agents search through your code |
| **Creating features** | Planning larger changes |
| **Debugging** | Finding and fixing issues |
| **Reviewing changes** | Verifying agent work |

---

## Summary for Engineers

| Question | Answer |
|----------|--------|
| **What is an agent harness?** | Instructions + Tools + Model |
| **How to write effective prompts?** | Reference existing files and patterns |
| **When to start fresh?** | Agent struggling, going in circles, new task |
| **What is scope creep?** | Task too large, agent loses focus |
| **How to fix scope creep?** | Break into smaller pieces, plan first |

---

## The Bottom Line

**Working with agents is a skill – you need to learn what to delegate, how to prompt, and when to intervene.**

**Think of it as:**
- **Vague prompt** = "Build me a house" 🏠 (too vague)
- **Constrained prompt** = "Build a 3-bedroom house using these blueprints" 📐 (perfect)

**For your engineers:**
- Start with specific, well-scoped prompts
- Reference existing files and patterns
- Monitor for scope creep
- Start fresh when agent struggles
- Plan before ambitious features
