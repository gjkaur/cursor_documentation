This is the **Plan Mode** documentation – one of the most important features for beginners! Plan Mode is like having an **architect draw blueprints** before a construction crew starts building.

Instead of the Agent immediately writing code (which can go wrong), Plan Mode makes the Agent **plan first, then ask for your approval, then build.**

Let me break this down for a complete beginner.

---

## What Is Plan Mode? (The 10-Second Summary)

**Plan Mode creates detailed implementation plans before writing any code.**

Instead of the Agent guessing what you want and potentially messing up, it:
1. Asks you clarifying questions
2. Researches your codebase
3. Creates a detailed plan
4. Shows you the plan for review
5. **Only then** writes code (when you say "go")

| Normal Agent Mode | Plan Mode |
|-------------------|-----------|
| Starts coding immediately | Plans first, codes second |
| You hope it's right | You approve the plan first |
| Hard to fix if wrong | Easy to edit the plan |
| Good for simple tasks | **Essential for complex tasks** |

**Toggle Plan Mode:** Press `Shift + Tab` in the chat input

---

## Why Plan Mode Exists

The documentation puts it perfectly:

> *"Sometimes Agent builds something that doesn't match what you wanted. Instead of trying to fix it through follow-up prompts, go back to the plan."*

**The problem with normal Agent mode:**

You say: *"Add a shopping cart"*

Agent guesses and starts coding. 5 minutes later, it built something completely wrong. Now you have to:
- Figure out what it did wrong
- Give follow-up instructions to fix it
- Hope it doesn't break more things

**With Plan Mode:**

You say: *"Add a shopping cart"*

Agent says: *"Before I code, here's my plan..."*

You review the plan, see it missed something important, edit the plan, then say "OK now build it."

**Result:** The code is right the first time.

---

## How Plan Mode Works (5 Steps)

| Step | What happens | Your role |
|------|--------------|-----------|
| **1** | Agent asks clarifying questions | Answer them |
| **2** | Agent researches your codebase | Wait (or keep working) |
| **3** | Agent creates a comprehensive plan | Read the plan |
| **4** | You review and edit the plan | Approve, edit, or reject |
| **5** | Click "Build" when ready | Say "Go!" |

### Step 1: Clarifying Questions

Agent might ask:
- *"Should the cart save items if the user closes the browser?"*
- *"Do you need quantity buttons or just add/remove?"*
- *"Should there be a maximum item limit?"*

**Why this matters:** The Agent wants to get it right. These questions prevent misunderstandings.

### Step 2: Research

Agent reads your codebase to understand:
- What files exist
- How things are currently structured
- What patterns you use

### Step 3: Create Plan

Agent produces something like:

```markdown
# Shopping Cart Implementation Plan

## Files to create:
1. `src/components/Cart.js` - Main cart component
2. `src/context/CartContext.js` - State management

## Files to modify:
1. `src/App.js` - Add CartProvider wrapper
2. `src/components/Header.js` - Add cart icon with count

## Implementation steps:
1. Create CartContext with add/remove/update functions
2. Build Cart component with item list and total
3. Integrate into Header
4. Add localStorage persistence

## Estimated changes: ~150 lines of code
```

### Step 4: Review & Edit

You can:
- **Approve** – "Looks good, build it"
- **Edit** – "Actually, also add a checkout button"
- **Reject** – "This isn't what I meant, let's start over"

### Step 5: Build

Click "Build" and Agent executes the plan exactly as described.

---

## Where Plans Are Saved

| Default location | Workspace location |
|------------------|---------------------|
| Your home directory | Your project folder |

**Click "Save to workspace"** to move the plan to your project for:
- Future reference
- Team sharing
- Documentation

**Pro tip:** Save important plans to your workspace. They become documentation for what you built and why.

---

## When to Use Plan Mode (vs. Normal Agent)

### ✅ USE Plan Mode for:

| Situation | Why |
|-----------|-----|
| **Complex features** | Multiple valid approaches to choose from |
| **Tasks touching many files** | Need to coordinate changes across the codebase |
| **Unclear requirements** | You need to explore before knowing full scope |
| **Architectural decisions** | You want to review the approach before committing |
| **First time doing something** | You're not sure how it should work |
| **Large changes** | Mistakes would be costly to fix |

### ❌ SKIP Plan Mode (use normal Agent) for:

| Situation | Why |
|-----------|-----|
| **Quick changes** | Fixing a typo, changing a color |
| **Tasks you've done many times** | You know exactly what you want |
| **Simple, obvious fixes** | Plan Mode would be overkill |
| **Exploratory coding** | Just trying things out |

---

## The "Start Over" Strategy (Important!)

The documentation shares a **powerful insight**:

> *"Sometimes Agent builds something that doesn't match what you wanted. Instead of trying to fix it through follow-up prompts, go back to the plan."*

### Wrong way (fixing through prompts):

```
You: "Add a cart"
Agent: *builds wrong cart*
You: "No, I meant with quantity buttons"
Agent: *adds quantity buttons but breaks something else*
You: "Also it needs to save items"
Agent: *adds save but now total is wrong*
You: "Just start over..."
```

**Time wasted:** 20+ minutes of back-and-forth

### Right way (go back to plan):

```
You: "Add a cart"
Agent: *builds wrong cart*
You: Revert changes (checkpoints!)
You: Refine the plan to be more specific
Agent: *builds correct cart*
```

**Time saved:** 5 minutes

> *"For larger changes, spend extra time creating a precise, well-scoped plan. The hard part is often figuring out what change should be made. With the right instructions, delegate implementation to Agent."*

**This is the key insight:** Planning is the hard part. Once you have a good plan, the Agent can execute it easily.

---

## How to Switch Modes

| Method | How to do it |
|--------|--------------|
| **Keyboard shortcut** | Press `Shift + Tab` (rotate through modes) |
| **Dropdown menu** | Click the mode picker in Agent window |

**Auto-suggestion:** Cursor also suggests Plan Mode automatically when you type keywords that indicate complex tasks (like "refactor", "redesign", "implement", "add feature").

---

## Real-World Example

### Without Plan Mode (Normal Agent):

**You:** "Add user authentication to my app"

**Agent:** Starts coding immediately. Creates a login form, but uses the wrong database structure. Adds password reset but it doesn't work. You spend 30 minutes fixing it.

### With Plan Mode:

**Step 1:** You type "Add user authentication to my app" with Plan Mode on

**Step 2:** Agent asks:
- *"Do you want email/password or social login?"*
- *"Should I use JWT tokens or sessions?"*
- *"Do you need password reset functionality?"*

**Step 3:** You answer: "Email/password, JWT tokens, yes to password reset"

**Step 4:** Agent researches and creates a plan:

```markdown
# Authentication Implementation Plan

## New files:
- auth/auth.js - JWT helper functions
- auth/login.js - Login page component
- auth/signup.js - Signup component
- auth/reset.js - Password reset flow

## Changes to existing files:
- package.json - Add bcrypt, jsonwebtoken
- app.js - Add auth routes
- database.js - Add users table schema

## Security considerations:
- Passwords hashed with bcrypt
- Tokens expire in 24 hours
- Rate limiting on login attempts

## Estimated changes: 8 files, ~400 lines of code
```

**Step 5:** You review, approve, and Agent builds it perfectly the first time.

---

## Pro Tips for Great Plans

### Tip 1: Be specific in your request
**Bad:** "Add a search feature"
**Good:** "Add a search feature that filters products by name and category, with debounced input"

### Tip 2: Answer clarifying questions thoroughly
Each question you answer makes the plan better.

### Tip 3: Review plans carefully
Look for:
- Missed edge cases
- Wrong approaches
- Missing files or steps

### Tip 4: Save plans to workspace
They become documentation for future developers (including future you).

### Tip 5: Refine, don't fix
If the first build is wrong, revert and refine the plan. Don't try to fix through follow-ups.

---

## Common Beginner Questions

### Q: Does Plan Mode cost more?
**A:** Yes, slightly. The research and planning steps use tokens. But it saves money by preventing wrong code that wastes tokens.

### Q: Can I edit a plan after building starts?
**A:** Not easily. That's why you review carefully before clicking Build.

### Q: How long does planning take?
**A:** Usually 10-30 seconds for research, plus time for you to answer questions.

### Q: Can I use Plan Mode for any task?
**A:** Yes, but it's overkill for simple tasks. Use judgment.

### Q: What if I don't like the plan?
**A:** Edit it, reject it, or ask Agent to revise it.

### Q: Are plans saved automatically?
**A:** Yes, in your home directory. Move them to workspace for sharing.

---

## Quick Reference Card

| Feature | Details |
|---------|---------|
| **What it does** | Creates a plan before writing code |
| **Toggle shortcut** | `Shift + Tab` |
| **When to use** | Complex tasks, many files, unclear requirements |
| **When to skip** | Simple fixes, familiar tasks |
| **The 5 steps** | Clarify → Research → Plan → Review → Build |
| **If it goes wrong** | Revert, refine the plan, run again |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is Plan Mode?** | Makes Agent plan before coding |
| **Why use it?** | Prevents wrong code, saves time |
| **How to turn on?** | `Shift + Tab` |
| **Best for?** | Complex features, many files, unclear requirements |
| **Not needed for?** | Typo fixes, simple changes |

---

## The Bottom Line

**Plan Mode is like measuring twice and cutting once.**

**Think of it as:**
- **Normal Agent** = Start building without blueprints 🏗️ (risky)
- **Plan Mode** = Draw blueprints first, then build 📐 (safe)

**For beginners:** Use Plan Mode for ANY task that feels even slightly complex. The extra minute of planning will save you 10+ minutes of fixing mistakes.

**The golden rule from the docs:**
> *"The hard part is often figuring out what change should be made. With the right instructions, delegate implementation to Agent."*

**Get the plan right, and the code will be right.**

