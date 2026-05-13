Perfect! This is the **Models & Pricing** page – the most technical of the three documents. It tells you:

1. **What AI models you can use** (Claude, GPT, Gemini, etc.)
2. **How much each one costs** (per million tokens)
3. **What subscription plan to choose** ($20, $60, or $200 per month)

Let me break this down for a complete beginner in plain English.

---

## The Big Picture (Read This First)

**Think of Cursor like a phone plan:**

| Concept | Phone analogy | Cursor analogy |
|---------|---------------|----------------|
| **Monthly fee** | $20/month for service | Pro plan = $20/month |
| **Included minutes** | 500 free minutes | $20 worth of AI usage |
| **Overage charges** | Pay per extra minute | Pay-as-you-go beyond limit |
| **Different models** | Local vs. international calls | Different AI models cost different amounts |

**Key point:** You don't pay per model directly. You pay a monthly subscription, which includes some "AI usage credits." Different models just use up those credits at different rates.

---

## Two Types of Usage (This is important!)

Cursor separates your AI usage into **two pools**:

| Pool | What it's for | How it's priced |
|------|---------------|-----------------|
| **Auto + Composer** | Everyday coding tasks (Agent mode, Composer) | Cheaper rate |
| **API** | Advanced usage, specific model selection | Standard API rates |

**For a beginner:** You'll almost always use the **Auto + Composer** pool. Ignore the API pool until you're advanced.

---

## Understanding the Pricing Table (The Numbers)

Let me decode what each column means:

| Column | What it means | Simple explanation |
|--------|---------------|-------------------|
| **Input** | Cost for AI to READ your code/prompt | How much it "listens" |
| **Cache Write** | Cost to temporarily save information for reuse | Storing info for later |
| **Cache Read** | Cost to retrieve saved information | Accessing stored info |
| **Output** | Cost for AI to GENERATE code/response | How much it "talks" |
| **Price per 1M tokens** | Cost per ~750,000 English words | The unit of measurement |

**Real-world example:** If you ask Cursor to write a 100-line function (~500 words), you might use ~5,000 tokens. At $3 per 1M tokens for input, that costs about $0.015 (1.5 cents).

---

## Model Prices Simplified (Cheapest to Most Expensive)

Here are the most common models ranked by **input cost** (what you'll pay most often):

| Model | Input cost (per 1M tokens) | Best for | Speed |
|-------|---------------------------|----------|-------|
| **GPT-5 Mini** | $0.25 | Quick answers, simple fixes | Fast ⚡ |
| **Claude 4.5 Haiku** | $1.00 | Balanced performance | Fast ⚡ |
| **GPT-5** | $1.25 | General coding | Medium |
| **Gemini 3 Flash** | $0.50 | Fast responses | Fast ⚡ |
| **Claude 4.6 Sonnet** | $3.00 | Complex coding (sweet spot) | Medium |
| **Claude 4.5 Sonnet** | $3.00 | Complex coding | Medium |
| **Claude 4.6 Opus** | $5.00 | Very complex tasks | Slow 🐢 |
| **GPT-5.5** | $5.00 | State-of-the-art | Slow 🐢 |
| **Claude 4.6 Opus (Fast mode)** | $30.00 | Emergency speed (expensive!) | Very Fast ⚡⚡ |

**Beginner recommendation:** Start with **Claude 4.6 Sonnet** ($3) or **GPT-5** ($1.25). They're the best balance of cost and quality.

---

## Subscription Plans (What You Actually Pay)

| Plan | Monthly price | Included API usage | Good for |
|------|--------------|-------------------|----------|
| **Pro** | $20/month | $20 worth | Occasional AI users (1-2 hours/day) |
| **Pro Plus** | $60/month | $70 worth | Daily users (3-5 hours/day) |
| **Ultra** | $200/month | $400 worth | Power users (all day, multiple projects) |

**What "included API usage" means:**
- Pro plan: You get $20 of AI usage included
- If you use $25 worth → you pay $5 extra (on-demand)
- If you use $15 worth → you pay nothing extra

---

## How Much Usage Will You Actually Need?

The documentation gives rough estimates:

| User type | Monthly usage | Recommended plan |
|-----------|---------------|------------------|
| **Light user** (tab completions only) | < $20 | Pro |
| **Occasional Agent user** | $20-40 | Pro (pay overages) |
| **Daily Agent user** | $60-100 | Pro Plus |
| **Power user** (multiple agents, automation) | $200+ | Ultra |

**For a beginner starting out:** Get the **Pro plan ($20)**. You probably won't exceed the included $20 in your first month.

---

## Key Features Included in ALL Plans

No matter which plan you choose, you get:
- ✅ Unlimited tab completions (suggestions as you type)
- ✅ Extended agent usage limits
- ✅ Access to Bugbot (automatic bug finder)
- ✅ Access to Cloud Agents (run tasks in the cloud)

---

## What is "Max Mode"?

**Max Mode** = Gives the AI more context (more code to look at)

| Normal mode | Max Mode |
|-------------|----------|
| AI sees ~200,000 tokens (~150 pages of code) | AI sees up to 1M tokens (~750 pages) |
| Standard pricing | Uses 2-5x more tokens (costs more) |

**When to use Max Mode:** Your task involves many files or a massive codebase. For small changes, skip it.

---

## Premium Routing (Advanced)

**What it is:** Cursor automatically picks the best model for your task

**When to use:** Complex tasks where you're not sure which model to pick

**Cost:** Whatever model it picks × usage

**Beginner advice:** Let Cursor use Premium Routing if you're unsure. It's like "automatic mode."

---

## Teams Plans (For Companies)

If you're working with a team:

| Plan | Price | Best for |
|------|-------|----------|
| **Teams** | $40/user/month | Small to medium teams |
| **Enterprise** | Custom | Large companies with special needs |

**Features for teams:**
- Admin dashboard (see who's using how much)
- Centralized billing (one bill for everyone)
- SSO (single sign-on with Google/Okta)
- Privacy mode enforcement

---

## Real-World Cost Examples

Let me show you what typical tasks cost:

### Example 1: Fix a small bug
- You ask: "Fix this typo in the welcome message"
- Input tokens: 2,000
- Output tokens: 500
- Using Claude 4.6 Sonnet ($3 input, $15 output per 1M)
- **Cost: ~$0.0135 (1.3 cents)**

### Example 2: Add a new feature
- You ask: "Add a dark mode toggle"
- Input tokens: 50,000 (AI reads your codebase)
- Output tokens: 10,000 (AI writes code)
- Using GPT-5 ($1.25 input, $10 output per 1M)
- **Cost: ~$0.16 (16 cents)**

### Example 3: Large refactor
- You ask: "Convert this React class component to hooks"
- Input tokens: 200,000 (AI reads many files)
- Output tokens: 50,000 (AI rewrites code)
- Using Claude 4.6 Sonnet ($3 input, $15 output)
- **Cost: ~$1.35**

**Conclusion:** Most tasks cost pennies. You'd need to do hundreds of tasks to hit $20.

---

## What Happens When You Hit Your Limit?

Two options:

1. **Pay-as-you-go** – Continue using AI, billed extra at end of month
2. **Upgrade plan** – Move to Pro Plus or Ultra for more included usage

**Important:** Your AI never gets slower or worse when you hit the limit. You just keep using it and pay a little extra.

---

## Beginner Decision Guide

### Step 1: Choose your plan

```
Are you a beginner just learning?
├─ YES → Start with Pro ($20/month)
└─ NO → Are you coding daily for work?
    ├─ YES → Get Pro Plus ($60/month)
    └─ NO → Get Pro ($20/month)
```

### Step 2: Choose your default model

```
What are you doing?
├─ Simple fixes, learning → GPT-5 Mini (cheapest)
├─ Everyday coding → GPT-5 or Claude 4.5 Haiku (balanced)
├─ Complex features → Claude 4.6 Sonnet (best value)
└─ I have no idea → Use Premium Routing (auto-pilot)
```

### Step 3: Monitor your usage

- Check your usage dashboard in Cursor settings
- If you're consistently under $20 → stay on Pro
- If you're consistently over $40 → upgrade to Pro Plus

---

## Common Beginner Questions

**Q: Do I need to buy API access separately?**  
A: No. Your subscription includes API usage credits.

**Q: What's the cheapest way to use Cursor?**  
A: Pro plan ($20) + use GPT-5 Mini for simple tasks.

**Q: What if I go over my limit by a lot?**  
A: You can set spending limits in settings to avoid surprise bills.

**Q: Can I use my own OpenAI/Anthropic API key?**  
A: Yes (BYOK = Bring Your Own Key). This is separate from Cursor's pricing.

**Q: Are there free options?**  
A: Cursor has a free trial. After that, you need a paid plan.

**Q: What's "Cache" and why does it matter?**  
A: Cache saves money. If the AI reuses information from a previous request, you pay less. It happens automatically.

---

## Summary Table for Beginners

| Your situation | Best plan | Best model | Monthly cost (estimated) |
|----------------|-----------|------------|--------------------------|
| Learning to code, occasional use | Pro ($20) | GPT-5 Mini | $20 (won't exceed) |
| Freelance developer, daily use | Pro Plus ($60) | Claude 4.6 Sonnet | $60-80 |
| Full-time developer, heavy use | Ultra ($200) | Claude 4.6 Opus | $200-250 |
| Working on a team | Teams ($40/user) | Varies | $40/user + usage |

---

## Your Action Plan

1. **Start with Pro plan ($20)**
2. **Set your default model to GPT-5** (good balance)
3. **Use Cursor normally for 2 weeks**
4. **Check your usage dashboard**
5. **Adjust plan if needed**

**Remember:** You can always upgrade or downgrade. Start small and scale up.

Would you like me to explain any specific pricing detail, or help you calculate estimated costs for your specific use case?