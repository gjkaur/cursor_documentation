Perfect! This is the documentation for **Gemini 3.1 Pro** – Google's flagship model in Cursor. This is a **unique model** because it can process **images** alongside code, making it special for frontend and UI/UX work.

Let me break this down for a complete beginner.

---

## What Is Gemini 3.1 Pro? (The 10-Second Summary)

**Gemini 3.1 Pro** is Google's most advanced coding model. Its **superpower** is that it can "see" and understand images – so you can show it a design mockup or screenshot, and it will write the code to match it.

| Aspect | Rating |
|--------|--------|
| **Speed** | Medium ⚡⚡⚡ |
| **Cost** | Medium 💰💰💰 |
| **Intelligence** | Frontier 🧠🧠🧠🧠🧠 (cutting-edge) |
| **Special ability** | **Image processing!** 🖼️ |

---

## Quick Facts Box

| Fact | Value | What it means |
|------|-------|----------------|
| **Model ID** | `gemini-3.1-pro` | What you type to select this model |
| **Default Context** | 200k tokens | ~150 pages of text normally |
| **Max Context** | 1M tokens | ~750 pages in "Max Mode" |
| **Provider** | Google | Made by Google (not Anthropic or OpenAI) |

---

## The BIG Differentiator: Image Processing 🖼️

**This is what makes Gemini special!**

Most AI models (Claude, GPT) can only read **text**. Gemini 3.1 Pro can **process images alongside code**.

### What does this mean for you?

| Without Gemini | With Gemini |
|----------------|-------------|
| You describe a design in words: *"Make a blue button with rounded corners..."* | You just **paste a screenshot** of the design |
| AI guesses what you want | AI **sees exactly** what you want |
| Takes multiple tries to get right | Gets it right the first time often |

### Real-world examples:

**Example 1: UI/UX work**
- You paste a Figma mockup of a login screen
- You say: *"Turn this into HTML/CSS"*
- Gemini writes the exact code matching the design

**Example 2: Frontend development**
- You screenshot a website you like
- You say: *"Build me a component that looks like this"*
- Gemini recreates the visual design

**Example 3: Visual bug fixing**
- You screenshot a broken layout
- You say: *"The button is misaligned. Fix it."*
- Gemini sees the issue and fixes it

**Example 4: Converting images to code**
- You have a logo or icon image
- You say: *"Create an SVG version of this logo"*
- Gemini traces the image and generates code

---

## Strengths (What Gemini Does Well)

### 1. Processes Images Alongside Code 🖼️
**The main event.** Perfect for:
- UI/UX development
- Frontend coding from design mockups
- Visual code understanding
- Converting designs to code

### 2. Huge Context (1M tokens in Max Mode)
- Can analyze your entire codebase at once
- Great for big projects

### 3. Great Value for Money
- **$2 per million input tokens** (cheaper than Claude Sonnet's $3)
- **$12 per million output tokens** (cheaper than Sonnet's $15)
- Frontier intelligence at mid-tier pricing

### 4. All Standard Tools Available
Has all the same tools as Claude models:
- Semantic search
- File reading/editing
- Web browsing
- Shell commands
- And more...

---

## Limitations (The Downsides)

### 1. No Cache Pricing Listed
The documentation shows `-` for Cache Write pricing. This means:
- Less transparent pricing for cached content
- Might not be as optimized for repeated requests

### 2. Long Context Costs More! ⚠️
**This is different from Claude models!**

| Model | Long context pricing |
|-------|---------------------|
| Claude 4.6 Sonnet | Same price (no extra charge) |
| Claude 4.7 Opus | Same price (no extra charge) |
| **Gemini 3.1 Pro** | **Higher price above 200k tokens** |

**What this means:** If your request uses more than 200k tokens (large files), you pay MORE than the base rate.

### 3. Newer Model
- Less battle-tested than Claude
- Fewer real-world coding examples
- Community support is smaller

---

## Pricing Breakdown

**Base prices (under 200k tokens):**

| Token type | Price | Compared to Claude Sonnet |
|------------|-------|--------------------------|
| **Input** (reading) | $2.00 | 33% cheaper than Sonnet ($3) |
| **Cache Write** | Not listed | ? |
| **Cache Read** | $0.20 | 33% cheaper than Sonnet ($0.30) |
| **Output** (writing) | $12.00 | 20% cheaper than Sonnet ($15) |

**LONG CONTEXT pricing (above 200k tokens):** Higher prices (specific rates not shown in this doc, but expect ~50-100% more)

---

## Real-World Cost Examples for Gemini 3.1 Pro

### Example 1: Simple UI fix (under 200k tokens)
- Input: 10,000 tokens
- Output: 2,000 tokens
- **Cost: ~$0.044 (4.4 cents)** – very cheap!

### Example 2: Building from a design mockup
- Input: 50,000 tokens + image
- Output: 20,000 tokens
- **Cost: ~$0.34 (34 cents)**

### Example 3: Large codebase analysis (over 200k tokens)
- Input: 500,000 tokens (long context pricing applies)
- Output: 100,000 tokens
- **Cost: More than base rate (check usage dashboard)**

---

## Gemini vs. Claude: The Comparison

| Feature | Gemini 3.1 Pro | Claude 4.6 Sonnet | Claude 4.7 Opus |
|---------|----------------|-------------------|-----------------|
| **Input cost** | $2.00 | $3.00 | $5.00 |
| **Output cost** | $12.00 | $15.00 | $25.00 |
| **Image processing** | ✅ YES | ❌ No | ❌ No |
| **Long context fee** | Extra charge | No extra | No extra |
| **Intelligence** | Frontier | High | Frontier |
| **Best for** | UI/UX, frontend | Daily coding | Complex tasks |

---

## When Should You Use Gemini 3.1 Pro?

### ✅ USE Gemini 3.1 Pro when:

| Situation | Why |
|-----------|-----|
| **You have a design mockup (Figma, screenshot, etc.)** | It can SEE the design and match it perfectly |
| **Building frontend/UI components** | Strong visual understanding |
| **Converting images to code** | It's the only model that can do this well |
| **You want cheaper frontier intelligence** | $2 input vs $5 for Opus |
| **Working with visual layouts** | CSS, HTML, React components with styling |

### ❌ DON'T use Gemini 3.1 Pro when:

| Situation | Better alternative |
|-----------|-------------------|
| **Working with very large codebases (>200k tokens)** | Claude (no long context penalty) |
| **You need pure backend logic** | Claude Sonnet or Opus |
| **Budget is tight AND you don't need images** | GPT-5 Mini or Claude Haiku |
| **You want maximum code quality** | Claude Opus 4.7 |
| **Your task is text-only** | Any model works, compare prices |

---

## Perfect Use Case: Frontend Development Workflow

This is where Gemini shines brightest:

```
Step 1: Open your design tool (Figma, Canva, etc.)
Step 2: Take a screenshot of the design
Step 3: In Cursor, paste the screenshot
Step 4: Type: "Turn this into responsive HTML/CSS"
Step 5: Gemini writes the exact code matching your design
Step 6: Review, tweak, deploy
```

**Time saved:** Hours of manual CSS adjustment → minutes of AI generation.

---

## Pro Tips for Using Gemini

### Tip 1: Use it for visual regression
Paste screenshots of your app before and after changes. Ask: *"Did I break anything visually?"*

### Tip 2: Combine with Claude for best results
- Use **Gemini** for the visual/frontend work (what it's best at)
- Use **Claude** for backend logic (what it's best at)
- Get the best of both worlds!

### Tip 3: Watch your token usage
Since long context costs extra, be mindful of huge requests. Break large tasks into smaller chunks.

### Tip 4: Keep images small
Large images = more tokens = higher cost. Resize screenshots before uploading.

---

## Beginner Decision Tree

```
Do you need to work with images or designs?
├─ YES → Is this frontend/UI work?
│   ├─ YES → Use Gemini 3.1 Pro! (perfect match!)
│   └─ NO → Gemini can still work, but may not be necessary
└─ NO → Do you want the cheapest frontier model?
    ├─ YES → Gemini ($2 input, good value)
    └─ NO → Use Claude Sonnet (better for pure code)
```

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is it?** | Google's top AI model with image processing |
| **What makes it special?** | Can "see" and understand images |
| **How much?** | $2 input, $12 output per 1M tokens (cheaper than Claude) |
| **Main downside?** | Extra cost for long context (>200k tokens) |
| **When to use?** | UI/UX, frontend, working with design mockups |
| **When to avoid?** | Large codebases, pure backend logic |

---

## The Bottom Line

**Gemini 3.1 Pro is the best choice for frontend and UI/UX work** because it can actually "see" what you want. For text-only coding, Claude Sonnet is often better. For pure budget, GPT-5 Mini wins.

**Think of it as:**
- **Claude Sonnet** = Backend specialist 👩‍💻 (great at logic)
- **Gemini Pro** = Frontend specialist 🎨 (great at visuals)
- **GPT-5 Mini** = Budget intern 💰 (cheapest overall)

**If you build websites, apps, or anything visual – try Gemini. You'll be amazed at how well it turns designs into code.**

