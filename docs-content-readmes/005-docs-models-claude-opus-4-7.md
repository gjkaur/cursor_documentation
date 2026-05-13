Excellent! This is the documentation for **Claude 4.7 Opus** – Anthropic's **most powerful and most expensive model**. This is the "Ferrari" of AI coding models.

Let me break this down for a complete beginner.

---

## What Is Claude 4.7 Opus? (The 10-Second Summary)

**Claude 4.7 Opus** is Anthropic's **strongest, smartest, most capable AI model**. Think of it as hiring a **senior architect** instead of a junior developer. It can handle complex, multi-step tasks without you holding its hand.

| Aspect | Rating |
|--------|--------|
| **Speed** | Medium ⚡⚡⚡ |
| **Cost** | High 💰💰💰💰💰 (most expensive!) |
| **Intelligence** | Frontier 🧠🧠🧠🧠🧠 (cutting-edge, best available) |

**"Frontier" intelligence** means it's at the absolute edge of what AI can do today.

---

## Quick Facts Box

| Fact | Value | What it means |
|------|-------|----------------|
| **Model ID** | `claude-opus-4-7` | What you type to select this model |
| **Default Context** | 200k tokens | ~150 pages of text normally |
| **Max Context** | 1M tokens | ~750 pages in "Max Mode" |
| **Provider** | Anthropic | The company that made it |

---

## What Makes Opus 4.7 Special?

The documentation highlights **four key strengths**:

### 1. Autonomous & Self-Directed 🤖
**What it means:** Opus can take a big task and complete it without you checking in constantly.

**Example:** You say *"Add user authentication to my app"* – Opus will:
- Figure out what files need to change
- Write the code
- Handle edge cases
- Fix its own mistakes
- Deliver a working solution

**Compare to cheaper models:** They might need you to say *"No, that's not what I meant"* or *"You forgot to handle passwords"*

### 2. Creative Reasoning 💡
**What it means:** It finds clever solutions you might not think of.

**Example:** Instead of a straightforward but inefficient solution, it might suggest:
- A novel algorithm
- An unexpected but better architecture
- A clever workaround for a limitation

### 3. Strong at Planning 📋
**What it means:** Before writing code, it creates a thoughtful plan.

**Example:**
```
Task: "Add dark mode to the entire website"

Opus's plan:
1. Create a theme provider component
2. Add CSS variables for colors
3. Build a toggle switch
4. Save user preference to localStorage
5. Update all 15 components to use theme vars
6. Test on all browsers
```

### 4. Reliable Tool Use 🔧
**What it means:** It uses Cursor's tools effectively and adapts when things go wrong.

**Example:** If a search doesn't find what it needs, it tries a different search strategy instead of giving up.

---

## Strengths (Detailed)

| Strength | What it means for YOU |
|----------|----------------------|
| **Drives multi-step tasks to completion** | Give it a big task, walk away, come back to working code |
| **Holds intent across long sessions** | It remembers what you wanted 2 hours and 50 messages ago |
| **Self-corrects when it hits friction** | It fixes its own mistakes without you pointing them out |
| **Writes production-ready code** | Code is clean, tested, and ready to deploy |
| **No hand-holding required** | You don't need to micromanage |
| **Explores alternative solutions** | Finds better ways than the obvious approach |
| **Catches edge cases early** | Thinks about what could go wrong before coding |
| **Chains tool results into actions** | Uses search results to decide what to edit next |

---

## Limitations (The Downsides)

### 1. Most Expensive Model 💸

| Cost comparison | Input (per 1M) | Output (per 1M) |
|----------------|---------------|-----------------|
| GPT-5 Mini | $0.25 | $2.00 |
| Claude 4.5 Haiku | $1.00 | $5.00 |
| Claude 4.6 Sonnet | $3.00 | $15.00 |
| **Claude 4.7 Opus** | **$5.00** | **$25.00** |
| GPT-5.5 | $5.00 | $30.00 |

**Opus is 5x more expensive than Haiku and 67% more than Sonnet!**

### 2. Can Over-Elaborate 🗣️
**What it means:** Sometimes it gives you a novel-length answer when a simple "yes/no" would do.

**Example:** You ask *"Should I use a class or function?"* – Opus might write 3 paragraphs explaining trade-offs, history, and philosophy when you just wanted *"Use a function."*

**When this matters:** In long coding sessions where you want quick, concise answers.

---

## Cost Comparison (Real Numbers)

Let me show you how quickly Opus adds up:

| Task type | Claude 4.6 Sonnet | Claude 4.7 Opus | Difference |
|-----------|-------------------|-----------------|------------|
| Fix a typo | $0.006 | $0.011 | +83% |
| Small feature | $0.14 | $0.23 | +64% |
| Refactor a file | $0.75 | $1.25 | +67% |
| New feature (full) | $2.10 | $3.50 | +67% |
| 50 tasks/month | $35 | $58 | +$23 |

**For a heavy user (200+ tasks/month):**
- Sonnet: ~$140/month
- Opus: ~$230/month
- **Difference: $90/month extra**

---

## Tools Available (Same as Sonnet)

Opus 4.7 has access to **ALL Cursor tools** (same as Sonnet 4.6):

- ✅ Semantic search
- ✅ Search files and folders
- ✅ Web browsing
- ✅ Read files
- ✅ Edit files
- ✅ Run shell commands
- ✅ Browser automation
- ✅ Image generation
- ✅ Ask questions
- ✅ Fetch rules

**No difference in tools – only difference is HOW WELL it uses them.**

---

## Pricing Breakdown

**All prices are per 1 million tokens** (≈750 pages of text)

| Token type | Price | Compared to Sonnet |
|------------|-------|-------------------|
| **Input** (reading) | $5.00 | +67% more than Sonnet ($3) |
| **Cache Write** (saving) | $6.25 | +67% more |
| **Cache Read** (retrieving) | $0.50 | +67% more |
| **Output** (writing) | $25.00 | +67% more |

**Same pattern:** Everything costs exactly 67% more than Sonnet 4.6.

---

## Important Pricing Detail

> "All Opus 4.7 prompts bill at the base per-token rates ... including when you use Max Mode ... up to 1M tokens at the same rates."

**What this means:** Like Sonnet, Opus does NOT charge extra for long context. You pay the same rate whether it reads 10,000 tokens or 1,000,000 tokens.

**This is actually a good deal for large projects** – other providers sometimes charge 2-5x more for long context.

---

## Thinking Variant (Crucial for Opus!)

The documentation specifically says:

> *"We recommend using the high thinking variant for the strongest results."*

**What is "thinking variant"?** A mode where the AI takes extra time to reason before answering.

**For Opus specifically:** The "high thinking variant" is where Opus truly shines. Without it, you're not getting the full value.

**Think of it like:**
- **No thinking** = Fast but surface-level (wasting Opus's potential)
- **Low thinking** = Better but not amazing
- **High thinking** = The full Opus experience (recommended!)

**Trade-off:** More thinking = slower responses + slightly higher cost

---

## When Should You Use Claude 4.7 Opus?

### ✅ USE Opus 4.7 when:

| Situation | Why |
|-----------|-----|
| **Complex, multi-file changes** | It plans across many files without losing track |
| **You're not sure how to solve a problem** | Its creative reasoning finds clever solutions |
| **You want to set it and forget it** | It self-corrects and needs less hand-holding |
| **Production-critical code** | Writes cleaner, more robust code |
| **Architecture design** | Great at planning system structure |
| **You're stuck on a tricky bug** | Its reasoning can find non-obvious issues |
| **Budget is not a concern** | If you have the credits, use the best |

### ❌ DON'T use Opus 4.7 when:

| Situation | Better alternative |
|-----------|-------------------|
| **Simple typo fixes** | GPT-5 Mini or Haiku (pennies vs. dollars) |
| **Adding basic UI text** | Sonnet or Haiku |
| **You're on a tight budget** | Sonnet gives 80% of the quality for 60% of the price |
| **Speed is critical** | Flash models are faster |
| **You need concise answers** | Opus can over-explain |
| **Your task is trivial** | Don't pay Ferrari prices for a grocery run |

---

## Model Comparison (The Full Picture)

| Feature | Claude 4.5 Haiku | Claude 4.6 Sonnet | Claude 4.7 Opus |
|---------|------------------|-------------------|-----------------|
| **Input cost** | $1.00 | $3.00 | $5.00 |
| **Output cost** | $5.00 | $15.00 | $25.00 |
| **Speed** | Fast | Medium | Medium |
| **Intelligence** | Medium | High | Frontier |
| **Auto-correction** | Basic | Good | Excellent |
| **Planning ability** | Basic | Good | Excellent |
| **Best for** | Quick tasks | Daily coding | Complex, critical work |

---

## Real-World Example Comparison

**Task:** *"Add a shopping cart to an e-commerce site"*

| Model | How it works | Result |
|-------|--------------|--------|
| **Haiku** | Adds basic cart. Might miss edge cases. Needs guidance. | 70% solution, needs polishing |
| **Sonnet** | Adds full cart with quantities, remove buttons. Handles most cases. | 90% solution, minor tweaks needed |
| **Opus** | Adds cart, persistence, coupons, inventory checks, unit tests. Self-fixes errors. | 99% solution, ready to deploy |

---

## Beginner Decision Guide

### Step 1: Ask yourself these questions

```
Is this task simple? (typo, text change, one-line fix)
├─ YES → Use Haiku or Mini (save your money)
└─ NO → Continue to next question

Is this task moderately complex? (new feature, bug fix, refactor)
├─ YES → Use Sonnet (best value)
└─ NO → Continue to next question

Is this task very complex? (multi-file, architecture, critical system)
├─ YES → Consider Opus
└─ NO → You probably don't need Opus
```

### Step 2: Try before you commit

1. Start with **Sonnet** for most tasks
2. When Sonnet struggles or gives mediocre results
3. **Switch to Opus** for just that task
4. Compare the quality difference
5. Decide if it's worth the extra cost for YOUR use case

---

## Pro Tips for Using Opus Effectively

### Tip 1: Always use high thinking variant
Without it, you're paying Opus prices for Sonnet-level quality.

### Tip 2: Use Opus for planning, not execution
Ask Opus to create a detailed plan, then use Sonnet to execute it. Best of both worlds!

**Example:**
- Opus: *"Create a 10-step plan for adding payment processing"*
- Sonnet: *"Execute step 1 of that plan"*

### Tip 3: Set a budget
In Cursor settings, you can set monthly spending limits. Opus can burn through credits fast if you're not careful.

### Tip 4: Use Max Mode with Opus
Since Max Mode doesn't cost extra with Opus, take advantage of the full 1M context for huge codebases.

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is it?** | Anthropic's most powerful, most expensive AI model |
| **Who is it for?** | Complex projects, critical code, users with budget |
| **How much?** | $5 input, $25 output per 1M tokens |
| **How smart?** | "Frontier" – best available today |
| **Main downside?** | Very expensive, can over-explain |
| **Should I use it?** | Only for complex tasks. Use Sonnet for daily work. |
| **Special feature?** | "High thinking variant" recommended |

---

## The Bottom Line

**Claude 4.7 Opus is like hiring a top-tier senior developer.** Amazing results, but expensive. Use it when you need the best, but don't waste it on simple tasks.

**For 90% of your daily coding:** Stick with Claude 4.6 Sonnet or GPT-5.  
**For that 10% of really tough problems:** Bring out Opus.

**Think of it as:**
- **GPT-5 Mini** = Intern 🧑‍🎓 (cheap, needs guidance)
- **Claude 4.6 Sonnet** = Staff Developer 👩‍💻 (balanced, reliable)
- **Claude 4.7 Opus** = Principal Architect 👨‍🏫 (expensive, exceptional)

Would you like me to compare Opus with another specific model, or explain anything else about the Claude family of models?