# AI Foundations – Agents

## Complete Beginner's Guide

This document explains the **Agents** lesson from Cursor Learn. It covers how AI models can call multiple tools, make decisions, and work autonomously – transforming from simple question-answerers into task-completing assistants.

Let me break this down for a complete beginner.

---

## What Is an Agent? (The 10-Second Summary)

**At its core, an agent is simply tools in a loop.** Instead of you telling the AI what to do step by step, you give it a goal and let it figure out the steps itself.

| Without Agent | With Agent |
|---------------|------------|
| You give turn-by-turn directions | You give the destination |
| You plan each step | Agent figures out the plan |
| You execute each action | Agent executes autonomously |
| You handle errors | Agent self-corrects |

> *"It's the difference between giving someone turn-by-turn directions versus just telling them the destination and letting them use GPS."*

---

## How an Agent Works (Real Example)

**Your request:** *"Add a dark mode toggle to my settings page."*

### What the Agent does:

| Step | Action | Tool Used |
|------|--------|-----------|
| 1 | Search codebase for settings page | Semantic search |
| 2 | Read relevant files to understand structure | Read files |
| 3 | Create a plan for implementation | Planning |
| 4 | Add state variable | Edit file |
| 5 | Create new CSS classes | Edit file |
| 6 | Implement toggle component | Edit file |
| 7 | Update UI | Edit file |
| 8 | Run tests to verify | Run command |
| 9 | Fix any errors that appear | Self-correct |

> *"This entire process happens through a series of tool calls, with the agent deciding what to do next based on the results of each action. It's like watching someone think out loud, except they're actually doing the work as they go."*

---

## Interactive Quiz (Part 1)

The course includes this quiz question:

> *"Which tasks are typically safe to delegate to agents?"*

| Option | Safe to Delegate? | Why |
|--------|-------------------|-----|
| **Patterned refactors across many files** | ✅ Yes | Clear pattern, well-understood |
| **Adding tests for a failing, well-scoped error** | ✅ Yes | Clear objective, established patterns |
| Pixel-perfect redesign from complex Figma mocks | ❌ No | Requires visual precision, subjective |
| Integrations with brand-new, undocumented libraries | ❌ No | No training data, uncertain patterns |

---

## Agents Change Your Role

### Before Agents (Traditional Development):

```
You: "What files are in the components folder?"
AI: "Here are the files..."
You: "Can you read the Button component?"
AI: "Here's the content..."
You: "Now update it to add a dark mode variant"
AI: "Here's the change..."
```

### After Agents:

```
You: "Add a dark mode toggle to the settings page"
Agent: (Figures everything out and does it)
```

> *"This is a large shift because it turns you into a task manager instead of a task doer."*

---

## Parallel Agents (Multiple at Once)

| Agent 1 | Agent 2 | Agent 3 |
|---------|---------|---------|
| Adds tests to authentication flow | Updates documentation | Refactors messy utility file |

> *"You can have multiple agents working on different parts of your codebase simultaneously."*

---

## What Agents Are Good At (Strengths)

| Task Type | Example |
|-----------|---------|
| **Clear objectives** | "Add a login button" |
| **Established patterns** | Refactoring with consistent style |
| **Adding tests** | Write tests for existing code |
| **Updating documentation** | Generate API docs |
| **Fixing bugs with clear errors** | "Fix the null pointer exception" |

---

## What Agents Struggle With (Limitations)

| Task Type | Why It's Hard |
|-----------|---------------|
| **Complex debugging** | Requires deep system understanding |
| **Pixel-perfect designs** | Visual precision, subjective |
| **New libraries** | Not in training data |
| **Undocumented APIs** | No pattern to follow |

---

## The Reality of Working with Agents

> *"Think of agents like fast junior developers who need clear direction, who also can easily forget things, so they require oversight."*

### Common Agent Behaviors:

| Behavior | Description |
|----------|-------------|
| **Get stuck in loops** | Repeat same failing approach |
| **Forget context** | Need reminders of constraints |
| **Make unintended changes** | May be too enthusiastic |
| **Need verification** | You're still responsible |

---

## Agent Costs and Risks

| Consideration | Implication |
|---------------|-------------|
| **Token usage** | Agents use significantly more tokens due to tool calls and iterations |
| **Unbounded changes** | Without constraints, may change things you didn't intend |
| **Verification needed** | You're still responsible for code quality |

> *"Without good constraints, they might enthusiastically make changes you didn't intend. And crucially, you're still responsible for verifying the code works correctly and meets your standards."*

---

## Interactive Quiz (Part 2)

The course includes this quiz question:

> *"Which guardrail helps prevent unbounded agent changes?"*

| Option | Correct? | Why |
|--------|----------|-----|
| Disable all tools to keep the agent safe | ❌ No | Agents need tools to work |
| **Require passing tests before merging changes** | ✅ **Yes** | Verification step prevents bad changes |
| Ask the agent to "be careful" | ❌ No | Not enforceable |

---

## The Art of Delegation

> *"Working effectively with agents is about learning what to delegate and when."*

### Progression:

```
Start small → Build confidence → Delegate larger chunks → Always have checkpoints
```

| Stage | Approach |
|-------|----------|
| **Beginner** | Small, well-defined tasks |
| **Intermediate** | Larger chunks with checkpoints |
| **Advanced** | Complex workflows with verification |

---

## Your New Role

| Old Role | New Role |
|----------|----------|
| Task doer | Task manager |
| Implementer | Architect and reviewer |
| Writes all code | Delegates and verifies |

> *"The goal isn't to eliminate human involvement but to amplify what you can accomplish. You become the architect and reviewer while agents handle the implementation details."*

---

## Agent Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                       AGENT WORKFLOW                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  User gives goal → Agent creates plan                          │
│         ↓                                                       │
│  Agent calls tool → Gets result → Evaluates                    │
│         ↓                                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ Decision Loop:                                          │    │
│  │   Is task complete?                                     │    │
│  │   ├─ Yes → Return result                                │    │
│  │   └─ No → Call next tool → Continue loop                │    │
│  └─────────────────────────────────────────────────────────┘    │
│         ↓                                                       │
│  Agent returns final result                                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Practical Tips for Working with Agents

| Tip | Why |
|-----|-----|
| **Start with small tasks** | Build confidence |
| **Use checkpoints** | Save progress, enable rollback |
| **Set clear objectives** | Reduce ambiguity |
| **Verify results** | Never trust blindly |
| **Add constraints** | Prevent unbounded changes |
| **Review tool calls** | Understand what agent is doing |

---

## What's Coming Next

The course will cover practical examples:

| Topic | What You'll Learn |
|-------|-------------------|
| **Prompt structuring** | Get better results |
| **Context management** | Avoid hitting limits |
| **Effective delegation** | Work with agents efficiently |
| **Verification workflows** | Ensure quality |
| **Debugging agents** | Fix when things go sideways |

> *"Working with AI is a skill that improves with practice. The mental models we've built in these foundation lessons will help you understand why certain approaches work better than others."*

---

## Summary for Engineers

| Question | Answer |
|----------|--------|
| **What is an agent?** | Tools in a loop that work autonomously |
| **How is it different?** | You give goals, not step-by-step instructions |
| **What are agents good at?** | Clear objectives, established patterns |
| **What do agents struggle with?** | Complex debugging, pixel-perfect designs |
| **What are the risks?** | Token costs, unbounded changes, need verification |
| **How to delegate effectively?** | Start small, use checkpoints, verify results |

---

## The Bottom Line

**Agents transform you from a task doer into a task manager – you set the goal, they figure out the path.**

**Think of it as:**
- **Without agents** = Giving turn-by-turn directions 🗺️
- **With agents** = Saying "Get me there" and letting GPS figure it out 📍

**For your engineers:**
- Agents are powerful but not magic – they need clear direction
- Start with small, well-defined tasks
- Use checkpoints and verification steps
- You're still the architect and reviewer
- The skill is learning what to delegate and when

**The mental models you've built:**
- Tokens → How models are priced and measured
- Context → What models can "see"
- Tool calling → How models take actions
- Agents → Tools in a loop, working autonomously
