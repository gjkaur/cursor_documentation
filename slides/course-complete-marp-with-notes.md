---
marp: true
theme: flat-gaia
paginate: true
header: 'Cursor Training Program — Complete Course'
---



<!-- _class: lead -->

# Cursor Training Program

## AI-Assisted Development with Cursor

Springpeople · 2-day instructor-led course · Modules 1–10

<!--
Good morning, and welcome to the Cursor Training Program — AI-Assisted Development with Cursor. Thank you for being here. Over the next two days we will move from mental models to daily editor workflows, then into automation, Cloud Agents, and the Cursor APIs.

Springpeople · 2-day instructor-led course · Modules 1–10. Before we start, please confirm three things: Cursor is installed, you are signed in, and you have a Git repository you can experiment in — sample repos are fine if you do not want to use production code.

This course is roughly seventy percent hands-on and thirty percent concept and discussion. You will see slide numbers in the footer; match them to this speaker script or to Marp presenter view. Questions are welcome — short ones during a slide, longer ones at breaks or module transitions.
-->

---


## Course Agenda

| Module | Title | Day | Duration |
|--------|-------|-----|----------|
| **1** | Mental Models for AI-Assisted Development | Day 1 | ~60 min |
| **2** | Cursor Editor Essentials | Day 1 | ~90 min |
| **3** | Agent Modes and Tools | Day 1 | ~60 min |
| **4** | Customizing Cursor for Your Team | Day 1 | ~60 min |
| **5** | Cursor CLI and Local Automation | Day 1 | ~60 min |
| **6** | Cloud Agents in the UI | Day 2 | ~90 min |
| **7** | Cursor API Foundations | Day 2 | ~60 min |
| **8** | Cloud Agents API and Webhooks | Day 2 | ~60 min |
| **9** | Admin and Analytics APIs | Day 2 | ~75 min |
| **10** | AI Code Tracking and Reporting | Day 2 | ~20 min |

**Total:** ~11.5 hours across 2 days (hands-on labs + demonstrations)

<!--
Let me orient you to the full two-day arc shown on this agenda slide.

Day one builds editor fluency: Module one gives shared mental models for how AI assistants actually work. Modules two through four are hands-on in the Cursor editor — understanding codebases, safe changes, agent modes, rules, and skills. Module five introduces the CLI for terminal and scripting workflows.

Day two shifts to automation and integration: Cloud Agents in the UI, API authentication and reliability, programmatic Cloud Agent launches and webhooks, admin and analytics reporting, and AI code tracking.

The total scheduled time is about eleven and a half hours across both days, plus breaks. I will adjust pacing based on your experience — raise your hand if you have never opened Cursor before so I can spend a little extra time on setup in the first hands-on module.
-->

---


## Day 1 — Foundations & Editor Workflows

| Module | Title | Focus | Duration |
|--------|-------|-------|----------|
| **1** | Mental Models for AI-Assisted Development | Foundations | ~60 min |
| **2** | Cursor Editor Essentials | Hands-On | ~90 min |
| **3** | Agent Modes and Tools | Hands-On + Concept | ~60 min |
| **4** | Customizing Cursor for Your Team | Hands-On + Walkthrough | ~60 min |
| **5** | Cursor CLI and Local Automation | Hands-On | ~60 min |

Concept blocks, hands-on exercises, team customization, and CLI automation.

<!--
This slide previews Day 1 — Foundations & Editor Workflows. Walk the module table row by row: name the module number, what participants will do there, and whether it is mostly concept, hands-on, or demonstration. Emphasize that day one is about building confidence in the editor before we ask anyone to call an API.
-->

---


## Day 2 — Cloud Agents, APIs & Analytics

| Module | Title | Focus | Duration |
|--------|-------|-------|----------|
| **6** | Cloud Agents in the UI | Hands-On + Demonstration | ~90 min |
| **7** | Cursor API Foundations | Concept + Hands-On | ~60 min |
| **8** | Cloud Agents API and Webhooks | Hands-On | ~60 min |
| **9** | Admin and Analytics APIs | Hands-On + Demonstrations | ~75 min |
| **10** | AI Code Tracking and Reporting | Hands-On + Take-Home | ~20 min |

Cloud agents, programmatic APIs, admin analytics, and AI code tracking.

<!--
This slide previews Day 2 — Cloud Agents, APIs & Analytics. Explain that day two assumes day-one mental models and editor habits are in place. Modules seven through ten require API keys; enterprise features are needed for modules nine and ten. If anyone lacks admin access, pair them with someone who has keys for those exercises.
-->

---


<!-- _header: 'Module 1 — Mental Models for AI-Assisted Development' -->

<!-- _class: lead -->

# Mental Models for AI-Assisted Development

## Module 1 · Day 1 (Foundations)

Cursor Training Program · Concept block · ~60 min

<!--
We are starting Module 1: Mental Models for AI-Assisted Development. Cursor Training Program · Concept block · ~60 min State the module goal in plain language: what participants will be able to do when we finish — not just what topics we will mention.

Preview whether this module is lecture, hands-on, or mixed. If it is hands-on, tell people when to open their laptops and which folder or repo to use. If it is concept-only, ask them to listen for one idea they can use on Monday morning.
-->

---


## Module Overview

| Aspect            | Details                                                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Duration**      | ~60 minutes                                                                                                       |
| **Format**        | Concept block (foundational theory)                                                                               |
| **Prerequisites** | None – this is the starting point                                                                                 |
| **Module Goal**   | Build accurate mental models of how AI coding assistants work, their limitations, and how to use them effectively |

<!--
This module overview slide sets expectations. In your own words, cover: Duration is ~60 minutes. Format is Concept block (foundational theory). Prerequisites is None – this is the starting point. Module Goal is Build accurate mental models of how AI coding assistants work, their limitations, and how to use them effectively.  Call out prerequisites explicitly and pause until anyone blocked by missing tools has help. Do not read the table word-for-word — translate it into what the room will experience in the next hour.
-->

---


## Learning Objectives

By the end of this module, participants will be able to:

- Explain why AI outputs are probabilistic, not deterministic
- Identify and mitigate hallucinations in coding contexts
- Understand token-based pricing and cost optimization
- Master context as the single most valuable AI skill
- Distinguish between tool calling, MCP, and autonomous agents
- Define the developer's evolving role with AI agents

<!--
These learning objectives describe outcomes, not topics. Paraphrase them: Explain why AI outputs are probabilistic, not deterministic. Identify and mitigate hallucinations in coding contexts. Understand token-based pricing and cost optimization. Master context as the single most valuable AI skill. Distinguish between tool calling, MCP, and autonomous agents. Define the developer's evolving role with AI agents.

Ask the room: which of these would help your team most this quarter? Note one or two answers — you can refer back at the module summary.

Tell participants they are not expected to memorize this list; they should recognize each outcome when they have done it during an exercise or demo.
-->

---


<!-- _class: lead -->

# Lesson 1.1

## How AI Models Work

_Concept · 12 minutes_

<!--
[Timing: Concept · 12 minutes. Adjust depth if the room is fast or slow — do not rush hands-on blocks.]

We now begin Lesson 1.1: How AI Models Work. Concept · 12 minutes. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Why Outputs Are Probabilistic

> Unlike traditional software that gives the same output for the same input, AI models generate responses based on **probability distributions**.

At its simplest, an LLM is a **next-token prediction engine**.

Given a sequence of tokens, it predicts what comes next — then samples, appends, repeats.

<!--
Read or closely paraphrase the quote on screen: "Unlike traditional software that gives the same output for the same input, AI models generate responses based on probability distributions."

At its simplest, an LLM is a next-token prediction engine. Given a sequence of tokens, it predicts what comes next — then samples, appends, repeats.

Pause two beats after the quote so it lands. Then ask whether anyone has seen the opposite problem in real projects.
-->

---


## Next-Token Prediction

<img src="assets/module-01/next-token-prediction.svg" alt="Next-token prediction probabilities" />

<!--
This slide is visual: Next-token prediction probabilities. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Traditional Code vs. AI Model

| Traditional Code                         | AI Model                                   |
| ---------------------------------------- | ------------------------------------------ |
| Deterministic (same input → same output) | Probabilistic (different outputs possible) |
| You control the logic                    | You influence, but don't control           |
| Errors are bugs                          | Errors are features of probability         |
| Predictable behavior                     | Needs management via parameters            |

<!--
Walk this table conversationally: Traditional Code — AI Model. Deterministic (same input → same output) — Probabilistic (different outputs possible). You control the logic — You influence, but don't control. Errors are bugs — Errors are features of probability. Predictable behavior — Needs management via parameters. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Traditional vs. AI — Implication

**Implication:** Never trust a single run as ground truth.

<!--
For slide 12, Traditional vs. AI — Implication: Implication: Never trust a single run as ground truth.

Check for questions before you advance. If the room is silent, ask a specific question tied to the slide content.
-->

---


## What Determines AI Output?

<img src="assets/module-01/factors-output.svg" alt="Factors that shape AI output" />

<!--
This slide is visual: Factors that shape AI output. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Key Parameters You Control

| Parameter       | What It Does                                 | Best For                              |
| --------------- | -------------------------------------------- | ------------------------------------- |
| **Temperature** | Randomness (0 = deterministic, 1 = creative) | Bug fixes (low), brainstorming (high) |
| **Top-p**       | Nucleus sampling – limits token pool         | Balanced responses                    |
| **Max Tokens**  | Limits response length                       | Controlling cost                      |

<!--
Walk this table conversationally: Parameter — What It Does, Best For. Temperature — Randomness (0 = deterministic, 1 = creative), Bug fixes (low), brainstorming (high). Top-p — Nucleus sampling – limits token pool, Balanced responses. Max Tokens — Limits response length, Controlling cost. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Key Parameters — Example Values

```python
temperature: 0.2   # focused
top_p: 0.9         # balanced
max_tokens: 4000   # cap length
```

<!--
temperature: 0.2   # focused top_p: 0.9         # balanced max_tokens: 4000   # cap length Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "temperature: 0.2   # focused" and explain why it matters.
-->

---


## Temperature Impact

Same prompt: _"Write a function to reverse a string"_

```python
# Temperature 0.1 — very deterministic
def reverse_string(s):
    return s[::-1]

# Temperature 0.7 — balanced (adds edge cases)
def reverse_string(s):
    if not s: return s
    return s[::-1]

# Temperature 1.2 — creative, potentially unstable
def flip_the_text(text): ...
```

<!--
Same prompt: _"Write a function to reverse a string"_ def reverse_string(s): return s[::-1] Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "# Temperature 0.1 — very deterministic" and explain why it matters.
-->

---


## The Training Gap

Models are frozen at their training cutoff date. They don't know:

- Code written after their training date
- Your company's internal APIs
- Your specific architecture decisions
- Recent library updates (unless in context)

**Implication:** You must provide this information in the prompt or context.

<!--
On this slide, The Training Gap, cover these points in order: F i r s t ,   C o d e   w r i t t e n   a f t e r   t h e i r   t r a i n i n g   d a t e . Next, Your company's internal APIs. Next, Your specific architecture decisions. Next, Recent library updates (unless in context).
-->

---


<!-- _class: lead -->

# Lesson 1.2

## Hallucinations

_Concept · 10 minutes_

<!--
[Timing: Concept · 10 minutes. Adjust depth if the room is fast or slow — do not rush hands-on blocks.]

We now begin Lesson 1.2: Hallucinations. Concept · 10 minutes. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What Are Hallucinations?

> Confident-sounding outputs that are **factually wrong**, made up, or don't exist.

Most dangerous form: the model sounds **completely confident** while being **completely wrong**.

<!--
Read or closely paraphrase the quote on screen: "Confident-sounding outputs that are factually wrong, made up, or don't exist."

Most dangerous form: the model sounds completely confident while being completely wrong.

Pause two beats after the quote so it lands. Then ask whether anyone has seen the opposite problem in real projects.
-->

---


## Hallucinations in Code

| Type                   | Example                        | How to Spot               |
| ---------------------- | ------------------------------ | ------------------------- |
| **Fake APIs**          | `import nonexistent_library`   | Check docs; import fails  |
| **Wrong parameters**   | Incorrect function signature   | Type checking             |
| **Invented methods**   | `list.reverse_in_place()`      | Know the standard library |
| **Confident nonsense** | "This is the standard way to…" | Cross-reference           |
| **Outdated syntax**    | Old Python 2 style             | Know version differences  |

<!--
Walk this table conversationally: Type — Example, How to Spot. Fake APIs — import nonexistent_library, Check docs; import fails. Wrong parameters — Incorrect function signature, Type checking. Invented methods — list.reverse_in_place(), Know the standard library. Confident nonsense — "This is the standard way to…", Cross-reference. Outdated syntax — Old Python 2 style, Know version differences. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Why Models Hallucinate

<img src="assets/module-01/hallucination-causes.svg" alt="Root causes of hallucination" />

<!--
This slide is visual: Root causes of hallucination. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Example: Confident Wrong

```python
User: "How do I use requests for async calls?"

# Hallucinated (confident, wrong)
import requests.async as async_requests
response = await async_requests.get('https://api.example.com')

# Reality: requests does NOT have async support.
# Correct answer: Use httpx or aiohttp
```

<!--
User: "How do I use requests for async calls?" import requests.async as async_requests response = await async_requests.get('https://api.example.com') Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "User: "How do I use requests for async calls?"" and explain why it matters.
-->

---


## Hallucination Mitigation Strategies

| Strategy                 | How It Works                | Example                              |
| ------------------------ | --------------------------- | ------------------------------------ |
| **Grounding**            | Provide source material     | Paste library docs into context      |
| **Verification**         | Ask for citations           | "Which line of the docs shows this?" |
| **Constrained decoding** | Limit possible outputs      | JSON mode, regex patterns            |
| **Self-consistency**     | Ask multiple times, compare | Run same prompt 3×, take majority    |
| **Low temperature**      | Reduce randomness           | `temperature: 0.1`                   |
| **Tool use**             | Let model search/lookup     | Enable web search for docs           |

<!--
Walk this table conversationally: Strategy — How It Works, Example. Grounding — Provide source material, Paste library docs into context. Verification — Ask for citations, "Which line of the docs shows this?". Constrained decoding — Limit possible outputs, JSON mode, regex patterns. Self-consistency — Ask multiple times, compare, Run same prompt 3×, take majority. Low temperature — Reduce randomness, temperature: 0.1. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Hallucination Detection Checklist

Before accepting AI-generated code, verify:

- Do the imported libraries exist?
- Are function signatures correct?
- Does the syntax match my language version?
- Are there obvious logic errors?
- Would this code actually run?
- Does the model cite sources you can verify?

<!--
On this slide, Hallucination Detection Checklist, cover these points in order: F i r s t ,   D o   t h e   i m p o r t e d   l i b r a r i e s   e x i s t ? . Next, Are function signatures correct?. Next, Does the syntax match my language version?. Next, Are there obvious logic errors?. The remaining bullets are detail you can skip if time is short: Would this code actually run?, Does the model cite sources you can verify?.
-->

---


## The Developer's Mindset

> _"Trust, but verify – especially when the AI sounds most confident."_

- Hallucinations decrease with better prompts and context
- They never fully disappear
- You are the human-in-the-loop responsible for verification
- Experience helps you "smell" potential hallucinations

<!--
Read or closely paraphrase the quote on screen: "_"Trust, but verify – especially when the AI sounds most confident."_"

- Hallucinations decrease with better prompts and context - They never fully disappear - You are the human-in-the-loop responsible for verification - Experience helps you "smell" potential hallucinations

Pause two beats after the quote so it lands. Then ask whether anyone has seen the opposite problem in real projects.
-->

---


<!-- _class: lead -->

# Lesson 1.3

## Tokens and Pricing

_Concept · 10 minutes_

<!--
[Timing: Concept · 10 minutes. Adjust depth if the room is fast or slow — do not rush hands-on blocks.]

We now begin Lesson 1.3: Tokens and Pricing. Concept · 10 minutes. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What Is a Token?

| Language | Example                     | Token Count                  |
| -------- | --------------------------- | ---------------------------- |
| English  | "Hello world"               | 2 tokens (~0.75 words/token) |
| English  | "Congratulations"           | 1 token                      |
| Code     | `function calculateTotal()` | ~5 tokens (~2–4 chars/token) |
| Chinese  | "你好世界"                  | 4–8 tokens                   |

<!--
Walk this table conversationally: Language — Example, Token Count. English — "Hello world", 2 tokens (~0.75 words/token). English — "Congratulations", 1 token. Code — function calculateTotal(), ~5 tokens (~2–4 chars/token). Chinese — "你好世界", 4–8 tokens. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Why Tokens Matter

A token is the atomic unit of processing for LLMs — not a word, not a character.

You pay per token · Context windows are measured in tokens · Token limits determine how much code the AI can "see"

<!--
For slide 28, Why Tokens Matter: A token is the atomic unit of processing for LLMs — not a word, not a character. You pay per token · Context windows are measured in tokens · Token limits determine how much code the AI can "see"

Check for questions before you advance. If the room is silent, ask a specific question tied to the slide content.
-->

---


## Input vs. Output Pricing

**Input tokens** (prompt, code context, retrieved docs) cost **less** than **output tokens** (generated code and explanations).

Output is often **5–8× more expensive** — generation is more compute-intensive than reading.

<!--
For slide 29, Input vs. Output Pricing: Input tokens (prompt, code context, retrieved docs) cost less than output tokens (generated code and explanations). Output is often 5–8× more expensive — generation is more compute-intensive than reading.

Check for questions before you advance. If the room is silent, ask a specific question tied to the slide content.
-->

---


## Model Pricing Examples

| Model             | Input (per 1M) | Output (per 1M) | Output/Input |
| ----------------- | -------------: | --------------: | -----------: |
| GPT-5 Mini        |          $0.25 |           $2.00 |           8× |
| Claude 4.5 Haiku  |          $1.00 |           $5.00 |           5× |
| GPT-5.3 Codex     |          $1.75 |          $14.00 |           8× |
| Gemini 3.1 Pro    |          $2.00 |          $12.00 |           6× |
| Claude 4.6 Sonnet |          $3.00 |          $15.00 |           5× |
| Claude 4.7 Opus   |          $5.00 |          $25.00 |           5× |
| GPT-5.5           |          $5.00 |          $30.00 |           6× |

<!--
Walk this table conversationally: Model — Input (per 1M), Output (per 1M). GPT-5 Mini — $0.25, $2.00. Claude 4.5 Haiku — $1.00, $5.00. GPT-5.3 Codex — $1.75, $14.00. Gemini 3.1 Pro — $2.00, $12.00. Claude 4.6 Sonnet — $3.00, $15.00. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## What 1 Million Tokens Looks Like

| Content Type         | Approximate Amount            |
| -------------------- | ----------------------------- |
| Plain English text   | ~750,000 words (~1,500 pages) |
| Python code          | ~250,000–500,000 lines        |
| Average conversation | 5–10 sessions                 |
| Full codebase        | Small to medium project       |

<!--
Walk this table conversationally: Content Type — Approximate Amount. Plain English text — ~750,000 words (~1,500 pages). Python code — ~250,000–500,000 lines. Average conversation — 5–10 sessions. Full codebase — Small to medium project. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Cost Calculation Example

```python
prompt_tokens = 5000    # instructions + context
output_tokens = 2000    # AI response

model = "claude-4.6-sonnet"
input_price  = 3.00     # per 1M tokens
output_price = 15.00    # per 1M tokens

input_cost  = (5000 / 1_000_000) * 3.00
output_cost = (2000 / 1_000_000) * 15.00
total_cost  = input_cost + output_cost   # ~$0.045 (4.5 cents)
```

<!--
prompt_tokens = 5000    # instructions + context output_tokens = 2000    # AI response model = "claude-4.6-sonnet" Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "prompt_tokens = 5000    # instructions + context" and explain why it matters.
-->

---


## Cost Optimization Strategies

| Strategy               | How It Works                | Impact             |
| ---------------------- | --------------------------- | ------------------ |
| **Use cheaper models** | Mini/Haiku for simple tasks | 5–20× reduction    |
| **Reduce context**     | Only send relevant code     | 2–5× reduction     |
| **Cache responses**    | Reuse common answers        | Variable           |
| **Batch operations**   | Combine multiple tasks      | 30–50% reduction   |
| **Monitor usage**      | Track spending per user     | Prevents surprises |
| **Set limits**         | Monthly spending caps       | Budget protection  |

<!--
Walk this table conversationally: Strategy — How It Works, Impact. Use cheaper models — Mini/Haiku for simple tasks, 5–20× reduction. Reduce context — Only send relevant code, 2–5× reduction. Cache responses — Reuse common answers, Variable. Batch operations — Combine multiple tasks, 30–50% reduction. Monitor usage — Track spending per user, Prevents surprises. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Real-World Cost Bounds

| Usage Level | Monthly Cost | What You Can Do                          |
| ----------- | ------------ | ---------------------------------------- |
| Light       | $10–20       | Occasional questions, small fixes        |
| Medium      | $50–100      | Daily coding, regular agent use          |
| Heavy       | $200–500     | Full-time AI assistance, multiple agents |
| Enterprise  | $1000+       | Team usage, automation, CI/CD            |

<!--
Walk this table conversationally: Usage Level — Monthly Cost, What You Can Do. Light — $10–20, Occasional questions, small fixes. Medium — $50–100, Daily coding, regular agent use. Heavy — $200–500, Full-time AI assistance, multiple agents. Enterprise — $1000+, Team usage, automation, CI/CD. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## The Cache Effect

Models can cache frequently used content:

- **Cache Write:** Cost to initially store
- **Cache Read:** **Much cheaper** than fresh input (80–95% savings)

```python
# First request  → pays full input price
# Second request → same context → pays cache read price
```

Context discipline = cost discipline.

<!--
Models can cache frequently used content: - Cache Write: Cost to initially store - Cache Read: Much cheaper than fresh input (80–95% savings) Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "# First request  → pays full input price" and explain why it matters.
-->

---


<!-- _class: lead -->

# Lesson 1.4

## Context

_Concept · 12 minutes · The single most valuable AI skill_

<!--
[Timing: Concept · 12 minutes · The single most valuable AI skill. Adjust depth if the room is fast or slow — do not rush hands-on blocks.]

We now begin Lesson 1.4: Context. Concept · 12 minutes · The single most valuable AI skill. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What Is Context?

Context = all the information the model has access to when generating a response.

<img src="assets/module-01/context-inputs.svg" alt="What goes into context" />

<!--
This slide is visual: What goes into context. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## The Context Window Limit

| Model                            | Context Window | Pages of Text | Lines of Code |
| -------------------------------- | -------------: | ------------: | ------------: |
| Claude 4 (Haiku / Sonnet / Opus) |           200k |          ~150 |       ~50,000 |
| GPT-5 Mini / GPT-5.3 Codex       |           272k |          ~200 |       ~70,000 |

<!--
Walk this table conversationally: Model — Context Window, Pages of Text. Claude 4 (Haiku / Sonnet / Opus) — 200k, ~150. GPT-5 Mini / GPT-5.3 Codex — 272k, ~200. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Context Window — What Happens When Full

**When you exceed context:** Oldest content gets truncated · Critical information may be dropped

**Context engineering** = knowing what to put in, what to leave out, and how to structure it.

<!--
For slide 39, Context Window — What Happens When Full: When you exceed context: Oldest content gets truncated · Critical information may be dropped Context engineering = knowing what to put in, what to leave out, and how to structure it.

Check for questions before you advance. If the room is silent, ask a specific question tied to the slide content.
-->

---


## Context Checklist

Before every AI interaction, ask:

- What problem am I trying to solve?
- What files/code does the model need to see?
- What would a human need to know to help me?
- What information can I safely leave out?
- Is my context under the token limit?
- Have I included relevant error messages?
- Have I specified constraints (libraries, version, style)?

<!--
On this slide, Context Checklist, cover these points in order: F i r s t ,   W h a t   p r o b l e m   a m   I   t r y i n g   t o   s o l v e ? . Next, What files/code does the model need to see?. Next, What would a human need to know to help me?. Next, What information can I safely leave out?. The remaining bullets are detail you can skip if time is short: Is my context under the token limit?, Have I included relevant error messages?, Have I specified constraints (libraries, version, style)?.
-->

---


## Good vs. Bad Context — Bad Example

**BAD (vague):**

```
"Fix this bug: my code doesn't work"
```

<!--
BAD (vague): "Fix this bug: my code doesn't work" Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: ""Fix this bug: my code doesn't work"" and explain why it matters.
-->

---


## Good vs. Bad Context — Good Example

**GOOD (specific):**

```
Python function sorts dicts by key but raises KeyError.
Code: def sort_by_key(data, key): ...
Input: [{'name': 'Alice'}, {'age': 30}]
Using Python 3.11. Expected: skip dicts without the key.
```

<!--
GOOD (specific): Python function sorts dicts by key but raises KeyError. Code: def sort_by_key(data, key): ... Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "Python function sorts dicts by key but raises KeyError." and explain why it matters.
-->

---


## Context Prioritization Pyramid

<img src="assets/module-01/context-pyramid.svg" alt="Context prioritization pyramid" />

<!--
This slide is visual: Context prioritization pyramid. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Context Window Management

| Strategy                | How It Works                         | When to Use          |
| ----------------------- | ------------------------------------ | -------------------- |
| **Summarization**       | Compress earlier conversation        | Long sessions        |
| **Selective inclusion** | Only relevant files                  | Large codebases      |
| **Chunking**            | Split across multiple calls          | Exceeding limit      |
| **Hierarchical**        | Summaries + details on demand        | Complex projects     |
| **Vector retrieval**    | Semantic search for relevant context | Very large codebases |

<!--
Walk this table conversationally: Strategy — How It Works, When to Use. Summarization — Compress earlier conversation, Long sessions. Selective inclusion — Only relevant files, Large codebases. Chunking — Split across multiple calls, Exceeding limit. Hierarchical — Summaries + details on demand, Complex projects. Vector retrieval — Semantic search for relevant context, Very large codebases. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## The "Lost in the Middle" Problem

Models pay **most attention to the beginning and end** of context, and **less to the middle**.

<img src="assets/module-01/lost-in-middle.svg" alt="Lost in the middle attention chart" />

**Implication:** Put critical information at the beginning OR end, not the middle.

<!--
This slide is visual: Lost in the middle attention chart. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


<!-- _class: lead -->

# Lesson 1.5

## Tool Calling and MCP

_Concept · 8 minutes_

<!--
[Timing: Concept · 8 minutes. Adjust depth if the room is fast or slow — do not rush hands-on blocks.]

We now begin Lesson 1.5: Tool Calling and MCP. Concept · 8 minutes. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What Is Tool Calling?

Tool calling (function calling) lets the AI request execution of external functions.

The AI **doesn't execute code** — it outputs a structured request that **your system** executes.

<img src="assets/module-01/tool-calling-flow.svg" alt="Tool calling flow" />

<!--
This slide is visual: Tool calling flow. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Common Tool Types in Development

| Tool             | Purpose            | Example                          |
| ---------------- | ------------------ | -------------------------------- |
| **read_file**    | Read code files    | "Show me the auth module"        |
| **edit_file**    | Modify code        | "Add error handling to line 42"  |
| **search_code**  | Find patterns      | "Find all uses of this function" |
| **run_terminal** | Execute commands   | "Run the tests"                  |
| **web_search**   | Find documentation | "Look up pandas DataFrame API"   |
| **browser**      | Browse web pages   | "Open the PR and review it"      |
| **git**          | Version control    | "Create a branch and commit"     |

<!--
Walk this table conversationally: Tool — Purpose, Example. read_file — Read code files, "Show me the auth module". edit_file — Modify code, "Add error handling to line 42". search_code — Find patterns, "Find all uses of this function". run_terminal — Execute commands, "Run the tests". web_search — Find documentation, "Look up pandas DataFrame API". Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## MCP (Model Context Protocol)

> _"USB-C for AI — one protocol that works across different tools."_

**Without MCP:** Each tool needs custom integration

**With MCP:** Tools advertise their capabilities; AI discovers them dynamically

<img src="assets/module-01/mcp-architecture.svg" alt="MCP architecture" />

<!--
This slide is visual: MCP architecture. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.

Tie the diagram to this idea: "_"USB-C for AI — one protocol that works across different tools."_"
-->

---


## Why MCP Matters

| Benefit              | Explanation                                |
| -------------------- | ------------------------------------------ |
| **Interoperability** | Same tools work across different AI models |
| **Discoverability**  | AI can learn what tools are available      |
| **Standardization**  | One protocol, not dozens of custom APIs    |
| **Extensibility**    | Add new tools without changing AI logic    |

<!--
Walk this table conversationally: Benefit — Explanation. Interoperability — Same tools work across different AI models. Discoverability — AI can learn what tools are available. Standardization — One protocol, not dozens of custom APIs. Extensibility — Add new tools without changing AI logic. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Tool Calling Best Practices

1. **Define clear tool schemas** — name, description, parameters
2. **Validate tool calls** before execution — allowlist + parameter checks
3. **Set timeouts** — e.g., 30 seconds max per tool
4. **Log all tool calls** — audit trail for debugging
5. **Require human approval** for destructive actions — never auto-run writes/deletes

<!--
For slide 51, Tool Calling Best Practices: 1. Define clear tool schemas — name, description, parameters 2. Validate tool calls before execution — allowlist + parameter checks 3. Set timeouts — e.g., 30 seconds max per tool 4. Log all tool calls — audit trail for debugging 5. Require human approval for destructive actions — never auto-run writes/deletes

Check for questions before you advance. If the room is silent, ask a specific question tied to the slide content.
-->

---


<!-- _class: lead -->

# Lesson 1.6

## Agents

_Concept · 8 minutes_

<!--
[Timing: Concept · 8 minutes. Adjust depth if the room is fast or slow — do not rush hands-on blocks.]

We now begin Lesson 1.6: Agents. Concept · 8 minutes. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Agent vs. Chatbot

| Aspect          | Chatbot                              | Agent                             |
| --------------- | ------------------------------------ | --------------------------------- |
| **Interaction** | Single turn or simple back-and-forth | Multi-step, goal-oriented         |
| **Control**     | User drives each step                | Agent plans and executes          |
| **Memory**      | Limited to conversation              | Can maintain state across steps   |
| **Actions**     | None (text only)                     | Can call tools, modify files      |
| **Autonomy**    | None                                 | Goal-directed autonomy            |
| **Example**     | "Explain this code"                  | "Fix all bugs in this repository" |

<!--
Walk this table conversationally: Aspect — Chatbot, Agent. Interaction — Single turn or simple back-and-forth, Multi-step, goal-oriented. Control — User drives each step, Agent plans and executes. Memory — Limited to conversation, Can maintain state across steps. Actions — None (text only), Can call tools, modify files. Autonomy — None, Goal-directed autonomy. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## The Agent Loop

<!--
For slide 54, The Agent Loop: The Agent Loop

Check for questions before you advance. If the room is silent, ask a specific question tied to the slide content.
-->

---


## The Agent Loop — Diagram

<img src="assets/module-01/agent-loop.svg" alt="Agent loop diagram" />

<!--
This slide is visual: Agent loop diagram. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Levels of Agent Autonomy

| Level  | Name        | Description                            | Example                    |
| ------ | ----------- | -------------------------------------- | -------------------------- |
| **L1** | Assistant   | Responds, needs step-by-step guidance  | Basic chatbot              |
| **L2** | Tool-caller | Can request tools, human approves      | Cursor Agent with approval |
| **L3** | Planner     | Makes plans, executes with supervision | Auto-code review           |
| **L4** | Autonomous  | Self-directed, minimal supervision     | CI/CD agent                |
| **L5** | Full Agent  | Complete task ownership                | Enterprise automation      |

<!--
Walk this table conversationally: Level — Name, Description. L1 — Assistant, Responds, needs step-by-step guidance. L2 — Tool-caller, Can request tools, human approves. L3 — Planner, Makes plans, executes with supervision. L4 — Autonomous, Self-directed, minimal supervision. L5 — Full Agent, Complete task ownership. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## How Agents Change Your Role

**Traditional:**

<img src="assets/module-01/role-flow-traditional.svg" alt="Traditional developer workflow" />

**Agent-Assisted:**

<img src="assets/module-01/role-flow-agent-assisted.svg" alt="Agent-assisted developer workflow" />

<!--
This slide is visual: Traditional developer workflow. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Developer Role Shift

| Old Role       | New Role           |
| -------------- | ------------------ |
| Code writer    | Intent specifier   |
| Debugger       | Quality reviewer   |
| Implementation | Orchestration      |
| Manual testing | Acceptance testing |
| Problem solver | Problem framer     |

<!--
Walk this table conversationally: Old Role — New Role. Code writer — Intent specifier. Debugger — Quality reviewer. Implementation — Orchestration. Manual testing — Acceptance testing. Problem solver — Problem framer. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## When to Use Agents

**Good for agents:**

- Large, multi-step tasks · Repetitive patterns
- Well-defined with clear success criteria
- Low-risk changes · Documentation updates

**Bad for agents:**

- Security-critical systems · Unrecoverable actions
- Poorly defined goals · Real-time requirements
- High cost of failure

<!--
On this slide, When to Use Agents, cover these points in order: F i r s t ,   L a r g e ,   m u l t i - s t e p   t a s k s   ·   R e p e t i t i v e   p a t t e r n s . Next, Well-defined with clear success criteria. Next, Low-risk changes · Documentation updates. Next, Security-critical systems · Unrecoverable actions. The remaining bullets are detail you can skip if time is short: Poorly defined goals · Real-time requirements, High cost of failure.
-->

---


## Module Summary

| Lesson | Topic              | Key Insight                                                |
| ------ | ------------------ | ---------------------------------------------------------- |
| 1.1    | How AI Models Work | Probabilistic, not deterministic – manage with temperature |
| 1.2    | Hallucinations     | Models invent confidently – always verify                  |
| 1.3    | Tokens and Pricing | Output costs more – optimize context, use cheaper models   |
| 1.4    | Context            | Single most valuable skill – quality in = quality out      |
| 1.5    | Tool Calling & MCP | AI requests actions, you control execution                 |
| 1.6    | Agents             | Goal-directed action – changes developer role              |

<!--
Module 1 summary. In sixty seconds, walk the lesson table and restate one key insight per row.

Ask the closing question: what will you do differently on Monday? Take two or three answers.

Announce the break or introduce the next module with one connecting sentence.
-->

---


<!-- _header: 'Module 2 — Cursor Editor Essentials' -->

<!-- _class: lead -->

# Cursor Editor Essentials

## Module 2 · Day 1 (Hands-On)

Cursor Training Program · Hands-on exercise · ~90 min

<!--
We are starting Module 2: Cursor Editor Essentials. Cursor Training Program · Hands-on exercise · ~90 min State the module goal in plain language: what participants will be able to do when we finish — not just what topics we will mention.

Preview whether this module is lecture, hands-on, or mixed. If it is hands-on, tell people when to open their laptops and which folder or repo to use. If it is concept-only, ask them to listen for one idea they can use on Monday morning.
-->

---


## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~90 minutes |
| **Format** | Hands-on exercise |
| **Prerequisites** | Module 1 completed, Cursor installed, Git repository access |
| **Module Goal** | Master the core workflows of AI-assisted coding in Cursor |

<!--
This module overview slide sets expectations. In your own words, cover: Duration is ~90 minutes. Format is Hands-on exercise. Prerequisites is Module 1 completed, Cursor installed, Git repository access. Module Goal is Master the core workflows of AI-assisted coding in Cursor.  Call out prerequisites explicitly and pause until anyone blocked by missing tools has help. Do not read the table word-for-word — translate it into what the room will experience in the next hour.
-->

---


## Learning Objectives

By the end of this module, participants will be able to:

- Orient an AI agent to an unfamiliar codebase
- Get targeted explanations of specific files or symbols
- Make safe, reviewable changes using diff review
- Design complex changes with Plan Mode
- Compare models to choose the right one for each task
- Use @mentions for precise context control
- Navigate checkpoints as a safety net
- Let agents run terminal commands and react to output

<!--
These learning objectives describe outcomes, not topics. Paraphrase them: Orient an AI agent to an unfamiliar codebase. Get targeted explanations of specific files or symbols. Make safe, reviewable changes using diff review. Design complex changes with Plan Mode. Compare models to choose the right one for each task. Use @mentions for precise context control. Navigate checkpoints as a safety net. Let agents run terminal commands and react to output.

Ask the room: which of these would help your team most this quarter? Note one or two answers — you can refer back at the module summary.

Tell participants they are not expected to memorize this list; they should recognize each outcome when they have done it during an exercise or demo.
-->

---


## Agenda

| Lesson | Topic | Time |
|--------|-------|------|
| 2.1 | Codebase Understanding | 20 min |
| 2.2 | Explaining Files/Symbols | 13 min |
| 2.3 | Safe Reviewable Changes | 13 min |
| 2.4 | Plan Mode | 13 min |
| 2.5 | Comparing Models | 13 min |
| 2.6 | @mentions | 13 min |
| 2.7 | Checkpoints | 8 min |
| 2.8 | Terminal Integration | 13 min |

<!--
Use this agenda as your pacing map for the module. You will cover: Lesson 2.1, Codebase Understanding, about 20 min; Lesson 2.2, Explaining Files/Symbols, about 13 min; Lesson 2.3, Safe Reviewable Changes, about 13 min; Lesson 2.4, Plan Mode, about 13 min; Lesson 2.5, Comparing Models, about 13 min; Lesson 2.6, @mentions, about 13 min. Announce when the next hands-on block starts so people can close email and open Cursor. If you fall behind, shorten concept repetition before cutting exercise time.
-->

---


<!-- _class: lead -->

# Lesson 2.1

## Codebase Understanding

*Concept · 8 min · Exercise · 12 min*

<!--
We now begin Lesson 2.1: Codebase Understanding. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Use the Cursor Agent to orient yourself in an unfamiliar repository. Open the lab guide at slide-exercises/module-02/exercise-2.1-codebase-understanding.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## The Problem & The Solution

**The Problem:** Opening a new codebase is overwhelming. Where do you start? What's the entry point?

**The Cursor Solution:** Ask the agent to explain the codebase. It reads files, traces connections, and returns a roadmap.

> *"Drop an agent into a codebase you've never seen and get a coherent explanation of how it works."*

<!--
Read or closely paraphrase the quote on screen: "Drop an agent into a codebase you've never seen and get a coherent explanation of how it works."

The Problem: Opening a new codebase is overwhelming. Where do you start? What's the entry point? The Cursor Solution: Ask the agent to explain the codebase. It reads files, traces connections, and returns a roadmap.

Pause two beats after the quote so it lands. Then ask whether anyone has seen the opposite problem in real projects.
-->

---


## Exercise 2.1 — Steps 1–2

**Step 1:** Open an unfamiliar repository in Cursor

Use **PowerShell**, **Git Bash**, or **CMD** in Cursor's integrated terminal (Ctrl+`):

```bash
git clone https://github.com/facebookresearch/detectron2
cd detectron2
cursor .
```

**Step 2:** Open the Agent (Ctrl+I on Windows/Linux · Cmd+I on Mac)

<!--
Hands-on time for Exercise 2.1 — Steps 1–2. This exercise is Codebase Understanding. Goal: Use the Cursor Agent to orient yourself in an unfamiliar repository.. Follow the detailed steps in slide-exercises/module-02/exercise-2.1-codebase-understanding.md. 

Step 1: Open an unfamiliar repository in Cursor Use PowerShell, Git Bash, or CMD in Cursor's integrated terminal (Ctrl+`): git clone https://github.com/facebookresearch/detectron2 cd detectron2 cursor . Step 2: Open the Agent (Ctrl+I on Windows/Linux · Cmd+I on Mac)

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.1 — Step 3: Orientation Prompt

```
Explain this codebase to me as if I'm a new team member.

Specifically tell me:
1. What is the main purpose of this project?
2. What are the entry points (main scripts, CLI, API)?
3. What are the key modules and how do they relate?
4. What are the main dependencies?
5. What files should I read first to understand the architecture?
```

<!--
Hands-on time for Exercise 2.1 — Step 3: Orientation Prompt. This exercise is Codebase Understanding. Goal: Use the Cursor Agent to orient yourself in an unfamiliar repository.. Follow the detailed steps in slide-exercises/module-02/exercise-2.1-codebase-understanding.md. 

Explain this codebase to me as if I'm a new team member. Specifically tell me: 1. What is the main purpose of this project? 2. What are the entry points (main scripts, CLI, API)? 3. What are the key modules and how do they relate? 4. What are the main dependencies? 5. What files should I read first to understand the architecture?

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Explain this codebase to me as if I'm a new team member.  Specifically tell me: 1. What is the main purpose of this project? 2. What are the entry points (main scripts, CLI, API)? 3. What are the key modules and how do they relate? 4. What are the main dependencies? 5. What files should I read first to understand the architecture?"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.1 — Step 4: Trace Data Flow

**Step 4:** Follow up — trace data flow:

```
Based on what you just told me, trace the flow of data from input
to output. What functions get called in order?
```

<!--
Hands-on time for Exercise 2.1 — Step 4: Trace Data Flow. This exercise is Codebase Understanding. Goal: Use the Cursor Agent to orient yourself in an unfamiliar repository.. Follow the detailed steps in slide-exercises/module-02/exercise-2.1-codebase-understanding.md. 

Step 4: Follow up — trace data flow: Based on what you just told me, trace the flow of data from input to output. What functions get called in order?

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Based on what you just told me, trace the flow of data from input to output. What functions get called in order?"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.1 — Step 5: Visual Overview

**Step 5:** Ask for a visual overview:

```
Create an ASCII diagram showing the module relationships in this codebase.
```

<!--
Hands-on time for Exercise 2.1 — Step 5: Visual Overview. This exercise is Codebase Understanding. Goal: Use the Cursor Agent to orient yourself in an unfamiliar repository.. Follow the detailed steps in slide-exercises/module-02/exercise-2.1-codebase-understanding.md. 

Step 5: Ask for a visual overview: Create an ASCII diagram showing the module relationships in this codebase.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Create an ASCII diagram showing the module relationships in this codebase."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Expected Agent Output (Sample)

<img src="assets/module-02/expected-agent-output-sample.svg" alt="Expected Agent Output (Sample)" />

<!--
This slide is visual: Expected Agent Output (Sample). Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Pro Tip — Save the Overview

**Pro Tip:** Save the agent's explanation as a project note:

```
Save this explanation as .cursor/project-overview.md so future
team members can read it.
```

<!--
Pro Tip: Save the agent's explanation as a project note: Save this explanation as .cursor/project-overview.md so future team members can read it. Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "Save this explanation as .cursor/project-overview.md so future" and explain why it matters.
-->

---


## Exercise 2.1 — Success Criteria

**Success Criteria:**
- Agent described project purpose
- Agent identified entry points and key modules
- Agent suggested first files to read

<!--
We are closing Exercise 2.1 — Codebase Understanding. Read each success criterion on the slide and ask the room to mentally check what they completed.

Expected outcome: Use the Cursor Agent to orient yourself in an unfamiliar repository.. Invite one or two volunteers to share what surprised them or what the Agent got wrong.

If many groups are behind, offer five more minutes or demonstrate the last step on your machine. Do not leave the exercise without a shared definition of done.
-->

---


<!-- _class: lead -->

# Lesson 2.2

## Explaining a Specific File or Symbol

*Concept · 5 min · Exercise · 8 min*

<!--
We now begin Lesson 2.2: Explaining a Specific File or Symbol. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Get targeted explanations of one file or symbol without reading the whole repo. Open the lab guide at slide-exercises/module-02/exercise-2.2-explaining-a-specific-file-or-symbol.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Targeted Explanations

> *"Don't make the agent read the whole codebase when you just need to understand one function."*

Use **precise context** — select a function or class, then ask focused questions.

<!--
Read or closely paraphrase the quote on screen: "Don't make the agent read the whole codebase when you just need to understand one function."

Use precise context — select a function or class, then ask focused questions.

Pause two beats after the quote so it lands. Then ask whether anyone has seen the opposite problem in real projects.
-->

---


## Exercise 2.2 — Steps 1–3

**Step 1:** Open a specific file in your project

**Step 2:** Select a function or class you want explained

**Step 3:** Use the Agent with precise context:

```
Explain the function I have selected. For each major section, tell me:
- What it does
- Why it's designed that way (trade-offs)
- Potential edge cases or bugs
- How it could be improved
```

<!--
Hands-on time for Exercise 2.2 — Steps 1–3. This exercise is Explaining a Specific File or Symbol. Goal: Get targeted explanations of one file or symbol without reading the whole repo.. Follow the detailed steps in slide-exercises/module-02/exercise-2.2-explaining-a-specific-file-or-symbol.md. 

Step 1: Open a specific file in your project Step 2: Select a function or class you want explained Step 3: Use the Agent with precise context: Explain the function I have selected. For each major section, tell me: - What it does - Why it's designed that way (trade-offs) - Potential edge cases or bugs - How it could be improved

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Explain the function I have selected. For each major section, tell me: - What it does - Why it's designed that way (trade-offs) - Potential edge cases or bugs - How it could be improved"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.2 — Step 4: Example I/O

**Step 4:** Ask for a concrete example:

```
Give me a concrete example of inputs and outputs for this function.
Show me what happens in the normal case and one edge case.
```

<!--
Hands-on time for Exercise 2.2 — Step 4: Example I/O. This exercise is Explaining a Specific File or Symbol. Goal: Get targeted explanations of one file or symbol without reading the whole repo.. Follow the detailed steps in slide-exercises/module-02/exercise-2.2-explaining-a-specific-file-or-symbol.md. 

Step 4: Ask for a concrete example: Give me a concrete example of inputs and outputs for this function. Show me what happens in the normal case and one edge case.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Give me a concrete example of inputs and outputs for this function. Show me what happens in the normal case and one edge case."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.2 — Step 5: Dependencies

**Step 5:** Ask about dependencies:

```
What other functions does this call? What calls this function?
Trace the call chain two levels in each direction.
```

<!--
Hands-on time for Exercise 2.2 — Step 5: Dependencies. This exercise is Explaining a Specific File or Symbol. Goal: Get targeted explanations of one file or symbol without reading the whole repo.. Follow the detailed steps in slide-exercises/module-02/exercise-2.2-explaining-a-specific-file-or-symbol.md. 

Step 5: Ask about dependencies: What other functions does this call? What calls this function? Trace the call chain two levels in each direction.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "What other functions does this call? What calls this function? Trace the call chain two levels in each direction."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Inline Explanation Shortcut

```bash
# Select code, press Cmd+L (or Ctrl+L)
# The agent explains the selected code in the chat panel
```

**Success Criteria:**
- Selected specific code · Agent explained the selection
- Agent provided input/output examples · Agent traced call dependencies

<!--
Success Criteria: - Selected specific code · Agent explained the selection - Agent provided input/output examples · Agent traced call dependencies Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "# Select code, press Cmd+L (or Ctrl+L)" and explain why it matters.
-->

---


<!-- _class: lead -->

# Lesson 2.3

## Making a Safe, Reviewable Change

*Concept · 5 min · Exercise · 8 min*

<!--
We now begin Lesson 2.3: Making a Safe, Reviewable Change. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Let the Agent propose a small change and review the diff before accepting. Open the lab guide at slide-exercises/module-02/exercise-2.3-making-a-safe-reviewable-change.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## The Diff Review Workflow

1. Ask agent to propose a change
2. Review the diff (what's added/removed)
3. Accept or reject changes
4. Test after acceptance

> *"Before AI changes your code, see exactly what will change and approve it."*

<!--
Read or closely paraphrase the quote on screen: "Before AI changes your code, see exactly what will change and approve it."

1. Ask agent to propose a change 2. Review the diff (what's added/removed) 3. Accept or reject changes 4. Test after acceptance

Pause two beats after the quote so it lands. Then ask whether anyone has seen the opposite problem in real projects.
-->

---


## Exercise 2.3 — Steps 1–2

**Step 1:** Ask for a small, safe change:

```
Change the welcome message in index.html from "Hello World"
to "Welcome to My App"
```

**Step 2:** Watch the agent generate the diff:

```
📝 Changes to index.html:

  <h1>- Hello World</h1>
  <h1>+ Welcome to My App</h1>

Accept? [Yes] [No] [Edit]
```

<!--
Hands-on time for Exercise 2.3 — Steps 1–2. This exercise is Making a Safe, Reviewable Change. Goal: Let the Agent propose a small change and review the diff before accepting.. Follow the detailed steps in slide-exercises/module-02/exercise-2.3-making-a-safe-reviewable-change.md. 

Step 1: Ask for a small, safe change: Change the welcome message in index.html from "Hello World" to "Welcome to My App" Step 2: Watch the agent generate the diff: 📝 Changes to index.html: <h1>- Hello World</h1> <h1>+ Welcome to My App</h1> Accept? [Yes] [No] [Edit]

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Change the welcome message in index.html from "Hello World" to "Welcome to My App""

Tell them to paste this prompt into the Agent (or read it aloud while they type): "📝 Changes to index.html:    <h1>- Hello World</h1>   <h1>+ Welcome to My App</h1>  Accept? [Yes] [No] [Edit]"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.3 — Review Questions

Before accepting, ask yourself:

- Are the changes **only** what I asked for?
- Are there unexpected additions or deletions?
- Does the syntax look correct?
- Will this break anything else?

**Step 4:** Accept · **Step 5:** Test manually

<!--
Hands-on time for Exercise 2.3 — Review Questions. This exercise is Making a Safe, Reviewable Change. Goal: Let the Agent propose a small change and review the diff before accepting.. Follow the detailed steps in slide-exercises/module-02/exercise-2.3-making-a-safe-reviewable-change.md. 

Before accepting, ask yourself: - Are the changes only what I asked for? - Are there unexpected additions or deletions? - Does the syntax look correct? - Will this break anything else? Step 4: Accept · Step 5: Test manually

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.3 — Test After Accept

```bash
# Windows (PowerShell)
start index.html          # web
python script.py          # Python
npm start                 # React

# Mac
open index.html
python script.py
npm start
```

<!--
Hands-on time for Exercise 2.3 — Test After Accept. This exercise is Making a Safe, Reviewable Change. Goal: Let the Agent propose a small change and review the diff before accepting.. Follow the detailed steps in slide-exercises/module-02/exercise-2.3-making-a-safe-reviewable-change.md. 

start index.html          # web python script.py          # Python npm start                 # React open index.html python script.py npm start

Tell them to paste this prompt into the Agent (or read it aloud while they type): "# Windows (PowerShell) start index.html          # web python script.py          # Python npm start                 # React  # Mac open index.html python script.py npm start"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.3 — If Something Goes Wrong

```
That change didn't work. The button disappeared.
Please explain what happened and suggest a fix.
```

**Success Criteria:**
- Agent proposed a change · Reviewed diff before accepting
- Accepted only after verification · Tested the change

<!--
Hands-on time for Exercise 2.3 — If Something Goes Wrong. This exercise is Making a Safe, Reviewable Change. Goal: Let the Agent propose a small change and review the diff before accepting.. Follow the detailed steps in slide-exercises/module-02/exercise-2.3-making-a-safe-reviewable-change.md. 

That change didn't work. The button disappeared. Please explain what happened and suggest a fix. Success Criteria: - Agent proposed a change · Reviewed diff before accepting - Accepted only after verification · Tested the change

Tell them to paste this prompt into the Agent (or read it aloud while they type): "That change didn't work. The button disappeared. Please explain what happened and suggest a fix."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 2.4

## Plan Mode

*Concept · 5 min · Exercise · 8 min*

<!--
We now begin Lesson 2.4: Plan Mode. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Use Plan Mode to design a change before the Agent edits files. Open the lab guide at slide-exercises/module-02/exercise-2.4-plan-mode.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Design Before You Code

Plan Mode makes the agent create a **detailed plan BEFORE writing any code**.

**When to use Plan Mode:**
- Changing multiple files · Adding a new feature
- Refactoring existing code
- You're not 100% sure of the best approach
- The change is risky or hard to undo

<!--
On this slide, Design Before You Code, cover these points in order: F i r s t ,   C h a n g i n g   m u l t i p l e   f i l e s   ·   A d d i n g   a   n e w   f e a t u r e . Next, Refactoring existing code. Next, You're not 100% sure of the best approach. Next, The change is risky or hard to undo.
-->

---


## Exercise 2.4 — Step 1: Enable Plan Mode

**Step 1:** Enable Plan Mode (Shift+Tab in the Agent input):

```bash
# Press Shift+Tab in the Agent input
# The input border changes color to indicate Plan Mode
```

<!--
Hands-on time for Exercise 2.4 — Step 1: Enable Plan Mode. This exercise is Plan Mode. Goal: Use Plan Mode to design a change before the Agent edits files.. Follow the detailed steps in slide-exercises/module-02/exercise-2.4-plan-mode.md. 

Step 1: Enable Plan Mode (Shift+Tab in the Agent input):

Tell them to paste this prompt into the Agent (or read it aloud while they type): "# Press Shift+Tab in the Agent input # The input border changes color to indicate Plan Mode"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.4 — Step 2: Describe Change

**Step 2:** Describe a complex change:

```
Add user authentication to this web app.

Requirements:
- Email/password login · Session management
- Protected routes (dashboard, settings)
- Logout functionality · "Remember me" option

Don't write code yet – just give me a plan.
```

<!--
Hands-on time for Exercise 2.4 — Step 2: Describe Change. This exercise is Plan Mode. Goal: Use Plan Mode to design a change before the Agent edits files.. Follow the detailed steps in slide-exercises/module-02/exercise-2.4-plan-mode.md. 

Step 2: Describe a complex change: Add user authentication to this web app. Requirements: - Email/password login · Session management - Protected routes (dashboard, settings) - Logout functionality · "Remember me" option Don't write code yet – just give me a plan.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Add user authentication to this web app.  Requirements: - Email/password login · Session management - Protected routes (dashboard, settings) - Logout functionality · "Remember me" option  Don't write code yet – just give me a plan."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.4 — Step 3: Review the Plan

**Step 3:** Review the agent's plan — a good plan includes:

```
📋 IMPLEMENTATION PLAN

Step 1: Create User Model — models/user.js
Step 2: Auth Routes — routes/auth.js (login, logout, register)
Step 3: Session Management — middleware/session.js
Step 4: Protected Route Middleware — middleware/auth.js
Step 5: Update Frontend — pages/login.html, dashboard.html
Step 6: Environment Variables — .env (SESSION_SECRET, REDIS_URL)

Questions for you:
1. JWT or server-side sessions?
2. Existing user database?
3. Include email verification?

Ready to proceed? [Yes] [No] [Modify Plan]
```

<!--
Hands-on time for Exercise 2.4 — Step 3: Review the Plan. This exercise is Plan Mode. Goal: Use Plan Mode to design a change before the Agent edits files.. Follow the detailed steps in slide-exercises/module-02/exercise-2.4-plan-mode.md. 

Step 3: Review the agent's plan — a good plan includes: 📋 IMPLEMENTATION PLAN Step 1: Create User Model — models/user.js Step 2: Auth Routes — routes/auth.js (login, logout, register) Step 3: Session Management — middleware/session.js Step 4: Protected Route Middleware — middleware/auth.js Step 5: Update Frontend — pages/login.html, dashboard.html Step 6: Environment Variables — .env (SESSION_SECRET, REDIS_URL) Questions for you: 1. JWT or server-side sessions? 2. Existing user database? 3. Include email verification? Ready to proceed? [Yes] [No] [Modify Plan]

Tell them to paste this prompt into the Agent (or read it aloud while they type): "📋 IMPLEMENTATION PLAN  Step 1: Create User Model — models/user.js Step 2: Auth Routes — routes/auth.js (login, logout, register) Step 3: Session Management — middleware/session.js Step 4: Protected Route Middleware — middleware/auth.js Step 5: Update Frontend — pages/login.html, dashboard.html Step 6: Environment Variables — .env (SESSION_SECRET, REDIS_URL)  Questions for you: 1. JWT or server-side sessions? 2. Existing user database? 3. Include email verification?  Ready to proceed? [Yes] [No] [Modify Plan]"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.4 — Approve & Execute

**Step 4:** Answer questions and approve:

```
Use JWT for simplicity. No existing database yet – use SQLite for now.
Skip email verification for this version. Proceed.
```

**Step 5:** Watch the agent execute the plan step by step

<!--
Hands-on time for Exercise 2.4 — Approve & Execute. This exercise is Plan Mode. Goal: Use Plan Mode to design a change before the Agent edits files.. Follow the detailed steps in slide-exercises/module-02/exercise-2.4-plan-mode.md. 

Step 4: Answer questions and approve: Use JWT for simplicity. No existing database yet – use SQLite for now. Skip email verification for this version. Proceed. Step 5: Watch the agent execute the plan step by step

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Use JWT for simplicity. No existing database yet – use SQLite for now. Skip email verification for this version. Proceed."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.4 — Success Criteria

**Success Criteria:**
- Enabled Plan Mode (Shift+Tab)
- Agent created structured plan
- Agent asked clarifying questions
- Approved plan before code was written

<!--
We are closing Exercise 2.4 — Plan Mode. Read each success criterion on the slide and ask the room to mentally check what they completed.

Expected outcome: Use Plan Mode to design a change before the Agent edits files.. Invite one or two volunteers to share what surprised them or what the Agent got wrong.

If many groups are behind, offer five more minutes or demonstrate the last step on your machine. Do not leave the exercise without a shared definition of done.
-->

---


<!-- _class: lead -->

# Lesson 2.5

## Comparing Two Models

*Concept · 5 min · Exercise · 8 min*

<!--
We now begin Lesson 2.5: Comparing Two Models. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Run the same prompt on two models and compare quality, speed, and cost. Open the lab guide at slide-exercises/module-02/exercise-2.5-comparing-two-models.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Model Selection Guide

| Task Type | Recommended Model | Why |
|-----------|-------------------|-----|
| Typo fixes, simple edits | GPT-5 Mini | Cheap, fast, good enough |
| Daily coding, bug fixes | GPT-5.3 Codex or Claude Sonnet | Best value, high quality |
| Complex logic, architecture | Claude Opus or GPT-5.5 | Smartest, but expensive |
| Frontend/visual work | Gemini 3.1 Pro | Can see images |
| Fast, simple questions | Claude Haiku | Fastest responses |

<!--
Walk this table conversationally: Task Type — Recommended Model, Why. Typo fixes, simple edits — GPT-5 Mini, Cheap, fast, good enough. Daily coding, bug fixes — GPT-5.3 Codex or Claude Sonnet, Best value, high quality. Complex logic, architecture — Claude Opus or GPT-5.5, Smartest, but expensive. Frontend/visual work — Gemini 3.1 Pro, Can see images. Fast, simple questions — Claude Haiku, Fastest responses. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Exercise 2.5 — Compare Two Models

**Step 1:** Set model to Claude Sonnet, ask:

```
Explain what a closure is in JavaScript with a practical example.
```

**Step 2:** Copy the response

**Step 3:** Switch to GPT-5 Mini — ask the **same question**

**Step 4:** Compare responses side by side

<!--
Hands-on time for Exercise 2.5 — Compare Two Models. This exercise is Comparing Two Models. Goal: Run the same prompt on two models and compare quality, speed, and cost.. Follow the detailed steps in slide-exercises/module-02/exercise-2.5-comparing-two-models.md. 

Step 1: Set model to Claude Sonnet, ask: Explain what a closure is in JavaScript with a practical example. Step 2: Copy the response Step 3: Switch to GPT-5 Mini — ask the same question Step 4: Compare responses side by side

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Explain what a closure is in JavaScript with a practical example."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.5 — Comparison Table

| Comparison Point | Claude Sonnet | GPT-5 Mini |
|-----------------|---------------|------------|
| Length | | |
| Code example quality | | |
| Explanation clarity | | |
| Speed | | |

<!--
Hands-on time for Exercise 2.5 — Comparison Table. This exercise is Comparing Two Models. Goal: Run the same prompt on two models and compare quality, speed, and cost.. Follow the detailed steps in slide-exercises/module-02/exercise-2.5-comparing-two-models.md. 

Direct participants to reproduce exactly what appears on this slide.

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.5 — Cost & Decision Matrix

**Step 5:** Check token usage at bottom of chat after each request

**Step 6:** Create a personal decision matrix:

<img src="assets/module-02/exercise-2-5-cost-decision-matrix.svg" alt="Exercise 2.5 — Cost & Decision Matrix" />

<!--
Hands-on time for Exercise 2.5 — Cost & Decision Matrix. This exercise is Comparing Two Models. Goal: Run the same prompt on two models and compare quality, speed, and cost.. Follow the detailed steps in slide-exercises/module-02/exercise-2.5-comparing-two-models.md. 

Step 5: Check token usage at bottom of chat after each request Step 6: Create a personal decision matrix: <img src="assets/module-02/exercise-2-5-cost-decision-matrix.svg" alt="Exercise 2.5 — Cost & Decision Matrix" />

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.5 — Success Criteria

**Success Criteria:**
- Same question to two models
- Compared quality and speed
- Created personal model-selection guide

<!--
We are closing Exercise 2.5 — Comparing Two Models. Read each success criterion on the slide and ask the room to mentally check what they completed.

Expected outcome: Run the same prompt on two models and compare quality, speed, and cost.. Invite one or two volunteers to share what surprised them or what the Agent got wrong.

If many groups are behind, offer five more minutes or demonstrate the last step on your machine. Do not leave the exercise without a shared definition of done.
-->

---


<!-- _class: lead -->

# Lesson 2.6

## Precise Context with @mentions

*Concept · 5 min · Exercise · 8 min*

<!--
We now begin Lesson 2.6: Precise Context with @mentions. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Use @mentions to point the Agent at exact files, symbols, and context. Open the lab guide at slide-exercises/module-02/exercise-2.6-precise-context-with-mentions.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## @mention Types

| @mention | What It Does | Example |
|----------|--------------|---------|
| `@filename` | Include specific file | `@auth.py` |
| `@symbol` | Include function/class | `@UserModel` |
| `@branch` | Reference git branch | `@main` |
| `@chat` | Reference past conversation | `@previous-chat` |
| `@folder` | Reference entire directory | `@/src/utils` |
| `@web` | Search the web | `@web pandas DataFrame` |

> *"Laser-targeting instead of spraying the whole codebase."*

<!--
Walk this table conversationally: @mention — What It Does, Example. @filename — Include specific file, @auth.py. @symbol — Include function/class, @UserModel. @branch — Reference git branch, @main. @chat — Reference past conversation, @previous-chat. @folder — Reference entire directory, @/src/utils. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Exercise 2.6 — Steps 1–2

**Step 1:** Use @filename to point at a specific file:

```
@database.py What are the security vulnerabilities in this database connection?
```

**Step 2:** Use @symbol to reference a specific function:

```
@calculate_total This function is returning NaN sometimes. Why?
```

<!--
Hands-on time for Exercise 2.6 — Steps 1–2. This exercise is Precise Context with @mentions. Goal: Use @mentions to point the Agent at exact files, symbols, and context.. Follow the detailed steps in slide-exercises/module-02/exercise-2.6-precise-context-with-mentions.md. 

Step 1: Use @filename to point at a specific file: @database.py What are the security vulnerabilities in this database connection? Step 2: Use @symbol to reference a specific function: @calculate_total This function is returning NaN sometimes. Why?

Tell them to paste this prompt into the Agent (or read it aloud while they type): "@database.py What are the security vulnerabilities in this database connection?"

Tell them to paste this prompt into the Agent (or read it aloud while they type): "@calculate_total This function is returning NaN sometimes. Why?"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.6 — Step 3: Multiple @mentions

**Step 3:** Combine multiple @mentions:

```
@auth.py @UserModel @login_handler Review the authentication flow.
Are there any race conditions or timing attacks?
```

<!--
Hands-on time for Exercise 2.6 — Step 3: Multiple @mentions. This exercise is Precise Context with @mentions. Goal: Use @mentions to point the Agent at exact files, symbols, and context.. Follow the detailed steps in slide-exercises/module-02/exercise-2.6-precise-context-with-mentions.md. 

Step 3: Combine multiple @mentions: @auth.py @UserModel @login_handler Review the authentication flow. Are there any race conditions or timing attacks?

Tell them to paste this prompt into the Agent (or read it aloud while they type): "@auth.py @UserModel @login_handler Review the authentication flow. Are there any race conditions or timing attacks?"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.6 — Step 4: @branch

**Step 4:** Use @branch to reference a different branch:

```
Compare @main and @feature/payment branches.
What are the key differences in the payment handling code?
```

<!--
Hands-on time for Exercise 2.6 — Step 4: @branch. This exercise is Precise Context with @mentions. Goal: Use @mentions to point the Agent at exact files, symbols, and context.. Follow the detailed steps in slide-exercises/module-02/exercise-2.6-precise-context-with-mentions.md. 

Step 4: Use @branch to reference a different branch: Compare @main and @feature/payment branches. What are the key differences in the payment handling code?

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Compare @main and @feature/payment branches. What are the key differences in the payment handling code?"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.6 — Step 5: @chat

**Step 5:** Use @chat to refer to a previous conversation:

```
@chat(authentication-discussion) Based on that discussion,
implement the fix we agreed on.
```

<!--
Hands-on time for Exercise 2.6 — Step 5: @chat. This exercise is Precise Context with @mentions. Goal: Use @mentions to point the Agent at exact files, symbols, and context.. Follow the detailed steps in slide-exercises/module-02/exercise-2.6-precise-context-with-mentions.md. 

Step 5: Use @chat to refer to a previous conversation: @chat(authentication-discussion) Based on that discussion, implement the fix we agreed on.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "@chat(authentication-discussion) Based on that discussion, implement the fix we agreed on."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.6 — Steps 6–7: @folder & @web

**Step 6:** Use @folder for directory-level context:

```
@src/components Find all components that don't have loading states.
```

**Step 7:** Use @web for external documentation:

```
@web React 19 useTransition hook How do I use it?
```

<!--
Hands-on time for Exercise 2.6 — Steps 6–7: @folder & @web. This exercise is Precise Context with @mentions. Goal: Use @mentions to point the Agent at exact files, symbols, and context.. Follow the detailed steps in slide-exercises/module-02/exercise-2.6-precise-context-with-mentions.md. 

Step 6: Use @folder for directory-level context: @src/components Find all components that don't have loading states. Step 7: Use @web for external documentation: @web React 19 useTransition hook How do I use it?

Tell them to paste this prompt into the Agent (or read it aloud while they type): "@src/components Find all components that don't have loading states."

Tell them to paste this prompt into the Agent (or read it aloud while they type): "@web React 19 useTransition hook How do I use it?"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## @mention Pro Tips

- Start typing **@** — Cursor auto-suggests available mentions
- You can @mention **multiple items** in one message
- @mentions work in both **Agent** and **Chat** modes

<!--
On this slide, @mention Pro Tips, cover these points in order: F i r s t ,   S t a r t   t y p i n g   @   —   C u r s o r   a u t o - s u g g e s t s   a v a i l a b l e   m e n t i o n s . Next, You can @mention multiple items in one message. Next, @mentions work in both Agent and Chat modes.
-->

---


## Exercise 2.6 — Success Criteria

**Success Criteria:**
- Used @filename to target a specific file
- Used @symbol to target a function or class
- Used multiple @mentions together
- Used @web for external search

<!--
We are closing Exercise 2.6 — Precise Context with @mentions. Read each success criterion on the slide and ask the room to mentally check what they completed.

Expected outcome: Use @mentions to point the Agent at exact files, symbols, and context.. Invite one or two volunteers to share what surprised them or what the Agent got wrong.

If many groups are behind, offer five more minutes or demonstrate the last step on your machine. Do not leave the exercise without a shared definition of done.
-->

---


<!-- _class: lead -->

# Lesson 2.7

## Checkpoints

*Concept · 4 min · Exercise · 4 min*

<!--
We now begin Lesson 2.7: Checkpoints. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Create and restore checkpoints before risky Agent experiments. Open the lab guide at slide-exercises/module-02/exercise-2.7-checkpoints.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## A Safety Net for Experiments

**What Checkpoints Save:**
- Code changes made by the agent
- Conversation history · File states

**When to Create Checkpoints:**
- Before complex changes · At milestones (Step 2 of 5)
- Before risky experiments · Before terminal commands

<!--
On this slide, A Safety Net for Experiments, cover these points in order: F i r s t ,   C o d e   c h a n g e s   m a d e   b y   t h e   a g e n t . Next, Conversation history · File states. Next, Before complex changes · At milestones (Step 2 of 5). Next, Before risky experiments · Before terminal commands.
-->

---


## Exercise 2.7 — Create & Restore

**Step 1:** Create a checkpoint before making a change

```bash
# Click checkpoint icon in Agent panel
# Windows/Linux: Ctrl+Shift+S · Mac: Cmd+Shift+S
```

<!--
Hands-on time for Exercise 2.7 — Create & Restore. This exercise is Checkpoints. Goal: Create and restore checkpoints before risky Agent experiments.. Follow the detailed steps in slide-exercises/module-02/exercise-2.7-checkpoints.md. 

Step 1: Create a checkpoint before making a change

Tell them to paste this prompt into the Agent (or read it aloud while they type): "# Click checkpoint icon in Agent panel # Windows/Linux: Ctrl+Shift+S · Mac: Cmd+Shift+S"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.7 — Steps 2–3

**Step 2:** Name it descriptively: `"Before auth refactor - safe point"`

**Step 3:** Let the agent make changes:

```
Add input validation to all form handlers.
```

<!--
Hands-on time for Exercise 2.7 — Steps 2–3. This exercise is Checkpoints. Goal: Create and restore checkpoints before risky Agent experiments.. Follow the detailed steps in slide-exercises/module-02/exercise-2.7-checkpoints.md. 

Step 2: Name it descriptively: "Before auth refactor - safe point" Step 3: Let the agent make changes: Add input validation to all form handlers.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Add input validation to all form handlers."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.7 — Steps 4–5

**Step 4:** If something goes wrong → **Restore to checkpoint**

**Step 5:** View history via the clock icon in Agent panel

<!--
Hands-on time for Exercise 2.7 — Steps 4–5. This exercise is Checkpoints. Goal: Create and restore checkpoints before risky Agent experiments.. Follow the detailed steps in slide-exercises/module-02/exercise-2.7-checkpoints.md. 

Step 4: If something goes wrong → Restore to checkpoint Step 5: View history via the clock icon in Agent panel

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Checkpoint Best Practices

- Create checkpoints every 5–10 minutes during complex work
- Use **descriptive names**, not "checkpoint1"
- Test the restored state before continuing
- Clean up old checkpoints periodically

**Success Criteria:**
- Created checkpoint · Made changes · Restored · Verified restoration

<!--
On this slide, Checkpoint Best Practices, cover these points in order: F i r s t ,   C r e a t e   c h e c k p o i n t s   e v e r y   5 – 1 0   m i n u t e s   d u r i n g   c o m p l e x   w o r k . Next, Use descriptive names, not "checkpoint1". Next, Test the restored state before continuing. Next, Clean up old checkpoints periodically. The remaining bullets are detail you can skip if time is short: Created checkpoint · Made changes · Restored · Verified restoration.
-->

---


<!-- _class: lead -->

# Lesson 2.8

## Terminal Integration

*Concept · 5 min · Exercise · 8 min*

<!--
We now begin Lesson 2.8: Terminal Integration. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Let the Agent run terminal commands and react to command output. Open the lab guide at slide-exercises/module-02/exercise-2.8-terminal-integration.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What the Agent Can Do

- Run shell commands · See stdout, stderr, exit codes
- React to command output · Install dependencies
- Run tests · Start/stop services

**Safety Features:**
- You approve each command before execution
- Commands appear in terminal for you to see
- You can reject dangerous commands

<!--
On this slide, What the Agent Can Do, cover these points in order: F i r s t ,   R u n   s h e l l   c o m m a n d s   ·   S e e   s t d o u t ,   s t d e r r ,   e x i t   c o d e s . Next, React to command output · Install dependencies. Next, Run tests · Start/stop services. Next, You approve each command before execution. The remaining bullets are detail you can skip if time is short: Commands appear in terminal for you to see, You can reject dangerous commands.
-->

---


## Exercise 2.8 — Steps 1–3

**Step 1:** Check the environment:

```
Run `python --version` and tell me what Python version we're using.
```

**Step 2:** Approve the command when prompted

**Step 3:** Run tests and fix failures:

```
Run the test suite. If any tests fail, fix them.
Show me what you're changing.
```

<!--
Hands-on time for Exercise 2.8 — Steps 1–3. This exercise is Terminal Integration. Goal: Let the Agent run terminal commands and react to command output.. Follow the detailed steps in slide-exercises/module-02/exercise-2.8-terminal-integration.md. 

Step 1: Check the environment: Run python --version and tell me what Python version we're using. Step 2: Approve the command when prompted Step 3: Run tests and fix failures: Run the test suite. If any tests fail, fix them. Show me what you're changing.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Run `python --version` and tell me what Python version we're using."

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Run the test suite. If any tests fail, fix them. Show me what you're changing."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.8 — Agent Terminal Loop

<img src="assets/module-02/exercise-2-8-agent-terminal-loop.svg" alt="Exercise 2.8 — Agent Terminal Loop" />

<!--
Hands-on time for Exercise 2.8 — Agent Terminal Loop. This exercise is Terminal Integration. Goal: Let the Agent run terminal commands and react to command output.. Follow the detailed steps in slide-exercises/module-02/exercise-2.8-terminal-integration.md. 

<img src="assets/module-02/exercise-2-8-agent-terminal-loop.svg" alt="Exercise 2.8 — Agent Terminal Loop" />

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.8 — Step 5: Install Dependency

**Step 5:** Install a dependency:

```
Install the 'requests' library if it's not already installed.
```

<!--
Hands-on time for Exercise 2.8 — Step 5: Install Dependency. This exercise is Terminal Integration. Goal: Let the Agent run terminal commands and react to command output.. Follow the detailed steps in slide-exercises/module-02/exercise-2.8-terminal-integration.md. 

Step 5: Install a dependency: Install the 'requests' library if it's not already installed.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Install the 'requests' library if it's not already installed."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 2.8 — Step 6: Multi-Step Workflow

**Step 6:** Multi-step workflow:

```
Run these commands in order:
1. git checkout main  2. git pull
3. git checkout -b feature/analytics
4. Create analytics.py  5. Run flake8  6. Fix style issues

Confirm before each command that might affect the repo.
```

<!--
Hands-on time for Exercise 2.8 — Step 6: Multi-Step Workflow. This exercise is Terminal Integration. Goal: Let the Agent run terminal commands and react to command output.. Follow the detailed steps in slide-exercises/module-02/exercise-2.8-terminal-integration.md. 

Step 6: Multi-step workflow: Run these commands in order: 1. git checkout main  2. git pull 3. git checkout -b feature/analytics 4. Create analytics.py  5. Run flake8  6. Fix style issues Confirm before each command that might affect the repo.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Run these commands in order: 1. git checkout main  2. git pull 3. git checkout -b feature/analytics 4. Create analytics.py  5. Run flake8  6. Fix style issues  Confirm before each command that might affect the repo."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Terminal Command Safety Rules

| Category | Commands |
|----------|----------|
| **Always approve first** | `rm`, `sudo`, `git push --force`, production changes |
| **Review carefully** | `npm install`, `pip install`, git branch changes, docker |
| **Safe to auto-approve** | `python --version`, `ls`, `pwd`, `cat`, `pytest`, `npm test` |

**Success Criteria:**
- Ran version check · Ran tests and reacted to output
- Installed dependency · Executed multi-step workflow

<!--
Walk this table conversationally: Category — Commands. Always approve first — rm, sudo, git push --force, production changes. Review carefully — npm install, pip install, git branch changes, docker. Safe to auto-approve — python --version, ls, pwd, cat, pytest, npm test. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Module Summary

| Lesson | Topic | Key Skill |
|--------|-------|-----------|
| 2.1 | Codebase Understanding | Orient to new repo |
| 2.2 | Explaining Files/Symbols | Targeted explanations |
| 2.3 | Safe Reviewable Changes | Diff review workflow |
| 2.4 | Plan Mode | Design before code |
| 2.5 | Comparing Models | Model selection |
| 2.6 | @mentions | Precise context |
| 2.7 | Checkpoints | Safety net |
| 2.8 | Terminal Integration | Command execution |

<!--
Module 2 summary. In sixty seconds, walk the lesson table and restate one key insight per row.

Ask the closing question: what will you do differently on Monday? Take two or three answers.

Announce the break or introduce the next module with one connecting sentence.
-->

---


## Quick Reference Card

<img src="assets/module-02/quick-reference-card.svg" alt="Quick Reference Card" />

<!--
This quick reference slide is meant for post-course use. Tell participants to screenshot it or copy the commands into their team wiki.

Offer two minutes for questions on this module only, then move on.
-->

---


<!-- _header: 'Module 3 — Agent Modes and Tools' -->

<!-- _class: lead -->

# Agent Modes and Tools

## Module 3 · Day 1 (Hands-On + Concept)

Cursor Training Program · ~60 min

<!--
We are starting Module 3: Agent Modes and Tools. Cursor Training Program · ~60 min State the module goal in plain language: what participants will be able to do when we finish — not just what topics we will mention.

Preview whether this module is lecture, hands-on, or mixed. If it is hands-on, tell people when to open their laptops and which folder or repo to use. If it is concept-only, ask them to listen for one idea they can use on Monday morning.
-->

---


## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise + concept |
| **Prerequisites** | Module 2 completed, live web app available (or sample provided) |
| **Module Goal** | Master different agent modes and the core tools that make agents powerful |

<!--
This module overview slide sets expectations. In your own words, cover: Duration is ~60 minutes. Format is Hands-on exercise + concept. Prerequisites is Module 2 completed, live web app available (or sample provided). Module Goal is Master different agent modes and the core tools that make agents powerful.  Call out prerequisites explicitly and pause until anyone blocked by missing tools has help. Do not read the table word-for-word — translate it into what the room will experience in the next hour.
-->

---


## Learning Objectives

By the end of this module, participants will be able to:

- Choose between Ask Mode and Agent Mode based on task and safety needs
- Use the Browser Tool to inspect live pages and read console output
- Run terminal commands through the agent and diagnose failures
- Write effective, constrained prompts that avoid scope creep

<!--
These learning objectives describe outcomes, not topics. Paraphrase them: Choose between Ask Mode and Agent Mode based on task and safety needs. Use the Browser Tool to inspect live pages and read console output. Run terminal commands through the agent and diagnose failures. Write effective, constrained prompts that avoid scope creep.

Ask the room: which of these would help your team most this quarter? Note one or two answers — you can refer back at the module summary.

Tell participants they are not expected to memorize this list; they should recognize each outcome when they have done it during an exercise or demo.
-->

---


## Agenda

| Lesson | Topic | Time |
|--------|-------|------|
| 3.1 | Ask Mode vs. Agent Mode | 18 min |
| 3.2 | Browser Tool | 18 min |
| 3.3 | Terminal Tool | 20 min |
| 3.4 | Effective Prompting in Practice | 22 min |

<!--
Use this agenda as your pacing map for the module. You will cover: Lesson 3.1, Ask Mode vs. Agent Mode, about 18 min; Lesson 3.2, Browser Tool, about 18 min; Lesson 3.3, Terminal Tool, about 20 min; Lesson 3.4, Effective Prompting in Practice, about 22 min. Announce when the next hands-on block starts so people can close email and open Cursor. If you fall behind, shorten concept repetition before cutting exercise time.
-->

---


<!-- _class: lead -->

# Lesson 3.1

## Ask Mode vs. Agent Mode

*Concept · 10 min · Exercise · 8 min*

<!--
We now begin Lesson 3.1: Ask Mode vs. Agent Mode. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Learn when Ask Mode is read-only and when Agent Mode can edit files. Open the lab guide at slide-exercises/module-03/exercise-3.1-ask-mode-vs-agent-mode.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## The Core Distinction

| Aspect | Ask Mode | Agent Mode |
|--------|----------|------------|
| **Can read files** | ✅ Yes (with @mentions) | ✅ Yes |
| **Can edit files** | ❌ No | ✅ Yes |
| **Can run terminal** | ❌ No | ✅ Yes |
| **Can browse web** | ❌ No (limited) | ✅ Yes (with tool) |
| **Can call tools** | ❌ No | ✅ Yes |
| **Safety level** | Very high (read-only) | Moderate (needs oversight) |
| **Best for** | Questions, learning, code review | Implementation, debugging, automation |

<!--
Walk this table conversationally: Aspect — Ask Mode, Agent Mode. Can read files — ✅ Yes (with @mentions), ✅ Yes. Can edit files — ❌ No, ✅ Yes. Can run terminal — ❌ No, ✅ Yes. Can browse web — ❌ No (limited), ✅ Yes (with tool). Can call tools — ❌ No, ✅ Yes. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## When to Use Each Mode

**USE ASK MODE when:**
- You have a question about code · Exploring a codebase
- You want a second opinion on design
- You're not ready to make changes · Production environment

**USE AGENT MODE when:**
- You want the AI to write/change code
- You need to run and react to commands
- Multi-step tasks · Development environment
- You're prepared to review changes

<!--
On this slide, When to Use Each Mode, cover these points in order: F i r s t ,   Y o u   h a v e   a   q u e s t i o n   a b o u t   c o d e   ·   E x p l o r i n g   a   c o d e b a s e . Next, You want a second opinion on design. Next, You're not ready to make changes · Production environment. Next, You want the AI to write/change code. The remaining bullets are detail you can skip if time is short: You need to run and react to commands, Multi-step tasks · Development environment, You're prepared to review changes.
-->

---


## Safety Implications

| Risk | Ask Mode | Agent Mode |
|------|----------|------------|
| Unintended code changes | None | Moderate (requires review) |
| File deletion | None | Possible (needs approval) |
| Malicious commands | None | Possible (needs approval) |
| Data leakage | Low | Medium (can read files) |
| API cost | Low (no tool calls) | Higher (multiple tool calls) |

<!--
Walk this table conversationally: Risk — Ask Mode, Agent Mode. Unintended code changes — None, Moderate (requires review). File deletion — None, Possible (needs approval). Malicious commands — None, Possible (needs approval). Data leakage — Low, Medium (can read files). API cost — Low (no tool calls), Higher (multiple tool calls). Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## The Mode Continuum

<img src="assets/module-03/the-mode-continuum.svg" alt="The Mode Continuum" />

> *"Not every AI interaction needs full agent capabilities."*

<!--
This slide is visual: The Mode Continuum. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.

Tie the diagram to this idea: ""Not every AI interaction needs full agent capabilities.""
-->

---


## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Cursor Agent panel** (`Ctrl+L`) is for natural-language prompts — not a shell.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Pause the slide deck for environment setup. Everyone should open PowerShell or Git Bash in Cursor's integrated terminal.

For API exercises: set keys with `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY` — never commit keys to git. On Windows, use `curl.exe` rather than the PowerShell curl alias when the lab shows curl commands.

Walk the room for two to three minutes. Common blockers: wrong key type, missing curl, wrong working directory. Do not advance until most pairs show a successful test call or are paired with someone who has.
-->

---


## Exercise 3.1 — Steps 1–2

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**


**Step 1:** Open Agent panel (`Cmd+I` / `Ctrl+I`) — note mode indicator at bottom
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

<!--
Hands-on time for Exercise 3.1 — Steps 1–2. This exercise is Ask Mode vs. Agent Mode. Goal: Learn when Ask Mode is read-only and when Agent Mode can edit files.. Follow the detailed steps in slide-exercises/module-03/exercise-3.1-ask-mode-vs-agent-mode.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Step 1: Open Agent panel (Cmd+I / Ctrl+I) — note mode indicator at bottom Where: Cursor Agent panel — `Ctrl+L (or Ctrl+I` for inline Agent)

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.1 — Steps 1–2 (Part 2)

**Step 2:** Try to make a change in **Ask Mode**:
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

```
Change the variable name 'temp' to 'temperature' in the current file.
```

<!--
Hands-on time for Exercise 3.1 — Steps 1–2 (Part 2). This exercise is Ask Mode vs. Agent Mode. Goal: Learn when Ask Mode is read-only and when Agent Mode can edit files.. Follow the detailed steps in slide-exercises/module-03/exercise-3.1-ask-mode-vs-agent-mode.md. 

Step 2: Try to make a change in Ask Mode: Where: Cursor Agent panel — `Ctrl+L (or Ctrl+I` for inline Agent) Change the variable name 'temp' to 'temperature' in the current file.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Change the variable name 'temp' to 'temperature' in the current file."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.1 — Steps 3–5

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**


**Step 3:** Ask a question Ask Mode handles well:
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

```
Explain the purpose of the main() function in this file.
What edge cases does it handle?
```

<!--
Hands-on time for Exercise 3.1 — Steps 3–5. This exercise is Ask Mode vs. Agent Mode. Goal: Learn when Ask Mode is read-only and when Agent Mode can edit files.. Follow the detailed steps in slide-exercises/module-03/exercise-3.1-ask-mode-vs-agent-mode.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Step 3: Ask a question Ask Mode handles well: Where: Cursor Agent panel — `Ctrl+L (or Ctrl+I` for inline Agent) Explain the purpose of the main() function in this file. What edge cases does it handle?

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Explain the purpose of the main() function in this file. What edge cases does it handle?"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.1 — Steps 3–5 (Part 2)

**Step 4:** Switch to **Agent Mode** via the dropdown
**Where:** **Cursor Agent panel** — ``Ctrl+L``

**Step 5:** Repeat the rename request — agent shows diff for approval
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

<!--
Hands-on time for Exercise 3.1 — Steps 3–5 (Part 2). This exercise is Ask Mode vs. Agent Mode. Goal: Learn when Ask Mode is read-only and when Agent Mode can edit files.. Follow the detailed steps in slide-exercises/module-03/exercise-3.1-ask-mode-vs-agent-mode.md. 

Step 4: Switch to Agent Mode via the dropdown Where: Cursor Agent panel — `Ctrl+L` Step 5: Repeat the rename request — agent shows diff for approval Where: Cursor Agent panel — `Ctrl+L (or Ctrl+I` for inline Agent)

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.1 — Step 6 & Success Criteria

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**Step 6:** Practice mode-switching mid-conversation:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
# Start in Ask Mode: What does this function return?
# Then: "Switch to Agent Mode and fix the off-by-one error"
```

**Success Criteria:**
- Used Ask Mode for questions · Observed Ask Mode cannot make changes
- Switched to Agent Mode · Made a change with diff review

<!--
We are closing Exercise 3.1 — Ask Mode vs. Agent Mode. Read each success criterion on the slide and ask the room to mentally check what they completed.

Expected outcome: Learn when Ask Mode is read-only and when Agent Mode can edit files.. Invite one or two volunteers to share what surprised them or what the Agent got wrong.

If many groups are behind, offer five more minutes or demonstrate the last step on your machine. Do not leave the exercise without a shared definition of done.
-->

---


<!-- _class: lead -->

# Lesson 3.2

## Browser Tool

*Concept · 8 min · Exercise · 10 min*

<!--
We now begin Lesson 3.2: Browser Tool. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Use the Browser tool so the Agent can inspect live web pages. Open the lab guide at slide-exercises/module-03/exercise-3.2-browser-tool.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What the Browser Tool Can Do

- Navigate to URLs · Read page content and DOM structure
- See console logs and errors · Take screenshots (depending on model)
- Click elements and interact with pages
- Extract data from live pages

> *"See what your app actually looks like in a browser — not just the source code."*

<!--
Read or closely paraphrase the quote on screen: "See what your app actually looks like in a browser — not just the source code."

- Navigate to URLs · Read page content and DOM structure - See console logs and errors · Take screenshots (depending on model) - Click elements and interact with pages - Extract data from live pages

Pause two beats after the quote so it lands. Then ask whether anyone has seen the opposite problem in real projects.
-->

---


## Browser Tool: With vs. Without

| Scenario | Without Browser | With Browser |
|----------|----------------|--------------|
| "Why is the button not showing?" | Guesses from CSS | Sees the rendered page |
| "Is the API returning data?" | Checks code | Sees network tab |
| "What console errors?" | Asks you | Reads console directly |
| "Does responsive layout work?" | Trusts CSS | Views at different sizes |

<!--
Walk this table conversationally: Scenario — Without Browser, With Browser. "Why is the button not showing?" — Guesses from CSS, Sees the rendered page. "Is the API returning data?" — Checks code, Sees network tab. "What console errors?" — Asks you, Reads console directly. "Does responsive layout work?" — Trusts CSS, Views at different sizes. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Exercise 3.2 — Steps 1–2

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)


**Step 1:** Start a local web app (or use a public test page)
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
python -m http.server 8000
# Or use a public test page
```

<!--
Hands-on time for Exercise 3.2 — Steps 1–2. This exercise is Browser Tool. Goal: Use the Browser tool so the Agent can inspect live web pages.. Follow the detailed steps in slide-exercises/module-03/exercise-3.2-browser-tool.md. 

Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts) Step 1: Start a local web app (or use a public test page) Terminal: PowerShell — unless step notes Git Bash or WSL python -m http.server 8000

Tell them to paste this prompt into the Agent (or read it aloud while they type): "python -m http.server 8000 # Or use a public test page"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.2 — Steps 1–2 (Part 2)

**Step 2:** In Agent Mode:
**Terminal:** **PowerShell** — ``Ctrl+` `` in Cursor

```
Use the browser tool to open http://localhost:8000
Tell me what you see on the page.
```

<!--
Hands-on time for Exercise 3.2 — Steps 1–2 (Part 2). This exercise is Browser Tool. Goal: Use the Browser tool so the Agent can inspect live web pages.. Follow the detailed steps in slide-exercises/module-03/exercise-3.2-browser-tool.md. 

Step 2: In Agent Mode: Terminal: PowerShell — `Ctrl+ `` in Cursor Use the browser tool to open http://localhost:8000 Tell me what you see on the page.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Use the browser tool to open http://localhost:8000 Tell me what you see on the page."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.2 — Steps 3–4

**Platform:** Windows 10/11 · Agent → ``Ctrl+L`` · Shell → **PowerShell** · Browser for dashboards


**Step 3:** Find specific elements:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
On that same page, find:
1. The main heading text
2. The number of buttons
3. Any error messages visible
```

<!--
Hands-on time for Exercise 3.2 — Steps 3–4. This exercise is Browser Tool. Goal: Use the Browser tool so the Agent can inspect live web pages.. Follow the detailed steps in slide-exercises/module-03/exercise-3.2-browser-tool.md. 

Platform: Windows 10/11 · Agent → `Ctrl+L` · Shell → PowerShell · Browser for dashboards Step 3: Find specific elements: Where: Cursor Agent panel — `Ctrl+L` On that same page, find: 1. The main heading text 2. The number of buttons 3. Any error messages visible

Tell them to paste this prompt into the Agent (or read it aloud while they type): "On that same page, find: 1. The main heading text 2. The number of buttons 3. Any error messages visible"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.2 — Steps 3–4 (Part 2)

**Step 4:** Check the console:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Now open the browser developer console.
Are there any errors or warnings? If so, what are they?
```

<!--
Hands-on time for Exercise 3.2 — Steps 3–4 (Part 2). This exercise is Browser Tool. Goal: Use the Browser tool so the Agent can inspect live web pages.. Follow the detailed steps in slide-exercises/module-03/exercise-3.2-browser-tool.md. 

Step 4: Check the console: Where: Cursor Agent panel — `Ctrl+L` Now open the browser developer console. Are there any errors or warnings? If so, what are they?

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Now open the browser developer console. Are there any errors or warnings? If so, what are they?"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Expected Agent Actions

<img src="assets/module-03/expected-agent-actions.svg" alt="Expected Agent Actions" />

<!--
This slide is visual: Expected Agent Actions. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Exercise 3.2 — Steps 5–6

**Platform:** Windows 10/11 · Agent → ``Ctrl+L`` · Shell → **PowerShell** · Browser for dashboards


**Step 5:** Diagnose a layout issue:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
The login button is partially hidden on mobile sizes.
Use the browser tool to check what's happening.
```

<!--
Hands-on time for Exercise 3.2 — Steps 5–6. This exercise is Browser Tool. Goal: Use the Browser tool so the Agent can inspect live web pages.. Follow the detailed steps in slide-exercises/module-03/exercise-3.2-browser-tool.md. 

Platform: Windows 10/11 · Agent → `Ctrl+L` · Shell → PowerShell · Browser for dashboards Step 5: Diagnose a layout issue: Where: Cursor Agent panel — `Ctrl+L` The login button is partially hidden on mobile sizes. Use the browser tool to check what's happening.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "The login button is partially hidden on mobile sizes. Use the browser tool to check what's happening."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.2 — Steps 5–6 (Part 2)

**Step 6:** Extract data from a page:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Go to https://example.com/pricing
Extract all pricing plan names and their monthly costs into a table.
```

<!--
Hands-on time for Exercise 3.2 — Steps 5–6 (Part 2). This exercise is Browser Tool. Goal: Use the Browser tool so the Agent can inspect live web pages.. Follow the detailed steps in slide-exercises/module-03/exercise-3.2-browser-tool.md. 

Step 6: Extract data from a page: Where: Cursor Agent panel — `Ctrl+L` Go to https://example.com/pricing Extract all pricing plan names and their monthly costs into a table.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Go to https://example.com/pricing Extract all pricing plan names and their monthly costs into a table."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Browser Tool Limitations

| Limitation | Workaround |
|------------|------------|
| Cannot log in to sites | Provide login instructions or session cookies |
| JavaScript-heavy sites may load slowly | Add wait instructions |
| Rate limits on some sites | Space out requests |
| Cannot upload files | Not supported yet |

**Success Criteria:** Opened URL · Read content · Checked console · Extracted data

<!--
Walk this table conversationally: Limitation — Workaround. Cannot log in to sites — Provide login instructions or session cookies. JavaScript-heavy sites may load slowly — Add wait instructions. Rate limits on some sites — Space out requests. Cannot upload files — Not supported yet. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


<!-- _class: lead -->

# Lesson 3.3

## Terminal Tool

*Concept · 8 min · Exercise · 12 min*

<!--
We now begin Lesson 3.3: Terminal Tool. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Use the Terminal tool to run tests, read output, and fix failures. Open the lab guide at slide-exercises/module-03/exercise-3.3-terminal-tool.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What the Terminal Tool Can Do

- Run any shell command (with approval)
- See stdout, stderr, exit codes
- Read command output as context for next actions
- Chain commands based on previous results

<!--
On this slide, What the Terminal Tool Can Do, cover these points in order: F i r s t ,   R u n   a n y   s h e l l   c o m m a n d   ( w i t h   a p p r o v a l ) . Next, See stdout, stderr, exit codes. Next, Read command output as context for next actions. Next, Chain commands based on previous results.
-->

---


## Terminal Tool Flow

<img src="assets/module-03/terminal-tool-flow.svg" alt="Terminal Tool Flow" />

<!--
This slide is visual: Terminal Tool Flow. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Exercise 3.3 — Steps 1–2

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**


**Step 1:** Check your environment:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Run these commands and tell me what versions we're using:
- python --version
- node --version (if applicable)
- git --version
```

<!--
Hands-on time for Exercise 3.3 — Steps 1–2. This exercise is Terminal Tool. Goal: Use the Terminal tool to run tests, read output, and fix failures.. Follow the detailed steps in slide-exercises/module-03/exercise-3.3-terminal-tool.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Step 1: Check your environment: Where: Cursor Agent panel — `Ctrl+L` Run these commands and tell me what versions we're using: - python --version - node --version (if applicable) - git --version

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Run these commands and tell me what versions we're using: - python --version - node --version (if applicable) - git --version"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.3 — Steps 1–2 (Part 2)

**Step 2:** Run the test suite:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Run the test suite. Show me which tests pass and which fail.
```

<!--
Hands-on time for Exercise 3.3 — Steps 1–2 (Part 2). This exercise is Terminal Tool. Goal: Use the Terminal tool to run tests, read output, and fix failures.. Follow the detailed steps in slide-exercises/module-03/exercise-3.3-terminal-tool.md. 

Step 2: Run the test suite: Where: Cursor Agent panel — `Ctrl+L` Run the test suite. Show me which tests pass and which fail.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Run the test suite. Show me which tests pass and which fail."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.3 — Steps 3–4

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**


**Step 3:** Diagnose failures:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
One or more tests failed. What's causing these failures?
Look at the specific error messages.
```

<!--
Hands-on time for Exercise 3.3 — Steps 3–4. This exercise is Terminal Tool. Goal: Use the Terminal tool to run tests, read output, and fix failures.. Follow the detailed steps in slide-exercises/module-03/exercise-3.3-terminal-tool.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Step 3: Diagnose failures: Where: Cursor Agent panel — `Ctrl+L` One or more tests failed. What's causing these failures? Look at the specific error messages.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "One or more tests failed. What's causing these failures? Look at the specific error messages."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.3 — Steps 3–4 (Part 2)

**Step 4:** Fix and verify:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Based on your diagnosis, fix the failing tests.
Show me what you're changing before you run again.
```

<!--
Hands-on time for Exercise 3.3 — Steps 3–4 (Part 2). This exercise is Terminal Tool. Goal: Use the Terminal tool to run tests, read output, and fix failures.. Follow the detailed steps in slide-exercises/module-03/exercise-3.3-terminal-tool.md. 

Step 4: Fix and verify: Where: Cursor Agent panel — `Ctrl+L` Based on your diagnosis, fix the failing tests. Show me what you're changing before you run again.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Based on your diagnosis, fix the failing tests. Show me what you're changing before you run again."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.3 — Debug Workflow (Step 5)

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

```
I found a bug where the app crashes when input is empty.

1. First, run the app to reproduce the crash
2. Then, add logging to understand why
3. Finally, fix the bug and verify it works
```

<img src="assets/module-03/exercise-3-3-debug-workflow-step-5.svg" alt="Exercise 3.3 — Debug Workflow (Step 5)" />

<!--
Hands-on time for Exercise 3.3 — Debug Workflow (Step 5). This exercise is Terminal Tool. Goal: Use the Terminal tool to run tests, read output, and fix failures.. Follow the detailed steps in slide-exercises/module-03/exercise-3.3-terminal-tool.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor I found a bug where the app crashes when input is empty. 1. First, run the app to reproduce the crash 2. Then, add logging to understand why 3. Finally, fix the bug and verify it works <img src="assets/module-03/exercise-3-3-debug-workflow-step-5.svg" alt="Exercise 3.3 — Debug Workflow (Step 5)" />

Tell them to paste this prompt into the Agent (or read it aloud while they type): "I found a bug where the app crashes when input is empty.  1. First, run the app to reproduce the crash 2. Then, add logging to understand why 3. Finally, fix the bug and verify it works"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.3 — Step 6 & Safety Rules

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**Step 6:** React to long-running commands:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Run npm install or pip install. Watch the output.
If there's a warning about deprecated packages, note it and suggest fixes.
```

| Approval Required | No Approval Needed |
|-------------------|-------------------|
| Writes files, `sudo`, `git push --force` | Version checks, `cat`, `ls` |
| `npm install -g`, start servers | `pytest`, `npm test`, `git status` |

**Success Criteria:** Ran tests · Diagnosed failure · Fixed code · Verified fix

<!--
Hands-on time for Exercise 3.3 — Step 6 & Safety Rules. This exercise is Terminal Tool. Goal: Use the Terminal tool to run tests, read output, and fix failures.. Follow the detailed steps in slide-exercises/module-03/exercise-3.3-terminal-tool.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Step 6: React to long-running commands: Where: Cursor Agent panel — `Ctrl+L` Run npm install or pip install. Watch the output. If there's a warning about deprecated packages, note it and suggest fixes. Success Criteria: Ran tests · Diagnosed failure · Fixed code · Verified fix

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Run npm install or pip install. Watch the output. If there's a warning about deprecated packages, note it and suggest fixes."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 3.4

## Effective Prompting in Practice

*Concept · 10 min · Exercise · 12 min*

<!--
We now begin Lesson 3.4: Effective Prompting in Practice. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Write constrained prompts and reusable templates for real tasks. Open the lab guide at slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Anatomy of an Effective Prompt

1. **ROLE / CONTEXT** — "You are a senior Python developer…"
2. **TASK** — "Fix the bug in calculate_total()…"
3. **CONSTRAINTS** — "Do not change the function signature…"
4. **OUTPUT FORMAT** — "Show me the diff and explain your change…"
5. **SUCCESS CRITERIA** — "Function should return 0 for empty input…"

<!--
For slide 159, Anatomy of an Effective Prompt: 1. ROLE / CONTEXT — "You are a senior Python developer…" 2. TASK — "Fix the bug in calculate_total()…" 3. CONSTRAINTS — "Do not change the function signature…" 4. OUTPUT FORMAT — "Show me the diff and explain your change…" 5. SUCCESS CRITERIA — "Function should return 0 for empty input…"

Check for questions before you advance. If the room is silent, ask a specific question tied to the slide content.
-->

---


## Bad Prompts vs. Good Prompts

| Bad Prompt | Good Prompt |
|------------|-------------|
| "Fix this code" | "Fix the IndexError in process_list() when list is empty. Do not change return type." |
| "Add logging" | "Add INFO-level logging to calculate() using existing logger config." |
| "Make it faster" | "Optimize find_user() from O(n²) to O(n log n). Don't change signature." |
| "Review my code" | "Review auth.py for SQL injection, password handling, session issues. Ignore style." |

<!--
Walk this table conversationally: Bad Prompt — Good Prompt. "Fix this code" — "Fix the IndexError in process_list() when list is empty. Do not change return type.". "Add logging" — "Add INFO-level logging to calculate() using existing logger config.". "Make it faster" — "Optimize find_user() from O(n²) to O(n log n). Don't change signature.". "Review my code" — "Review auth.py for SQL injection, password handling, session issues. Ignore style.". Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## The "Boundaries" Technique

Always tell the agent what **NOT** to touch:

```
BOUNDARIES:
- Do NOT change: function signatures, return types, existing tests
- Do NOT touch: config files, database schemas, other modules
- Do NOT delete: comments, logging, error handling
- Do NOT add: new dependencies, external APIs, global state

Change ONLY: the function body of calculate_total()
```

<!--
Always tell the agent what NOT to touch: BOUNDARIES: - Do NOT change: function signatures, return types, existing tests Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "BOUNDARIES:" and explain why it matters.
-->

---


## Avoiding Scope Creep

**The problem:**
```
User: "Fix the login bug."
Agent: "Fixed login. Also refactored auth, added OAuth, reorganized codebase."
User: "Wait, I just wanted the login bug fixed!"
```

| Technique | Example |
|-----------|---------|
| **Explicit boundaries** | "Change ONLY login.js lines 42–56" |
| **One thing at a time** | "First, just identify the issue. Don't fix yet." |
| **Ask for plan first** | "Plan Mode: Show me what you'll change before doing it" |
| **Use checkpoints** | Create checkpoint before complex requests |
| **Prefer diffs** | "Show me the diff, don't replace the whole file" |

<!--
Walk this table conversationally: Technique — Example. Explicit boundaries — "Change ONLY login.js lines 42–56". One thing at a time — "First, just identify the issue. Don't fix yet.". Ask for plan first — "Plan Mode: Show me what you'll change before doing it". Use checkpoints — Create checkpoint before complex requests. Prefer diffs — "Show me the diff, don't replace the whole file". Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Exercise 3.4 — Step 1: Constrained Prompt

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

```
Task: Fix the bug where get_user_email(user_id) returns None for valid users.

Constraints:
- Do NOT change the function signature
- Do NOT add new imports
- Do NOT modify other functions
- Do NOT add print statements (use existing logger)

Output format: Show exact diff and explain root cause.
Success criteria: Function returns email string for valid user IDs.
```

<!--
Hands-on time for Exercise 3.4 — Step 1: Constrained Prompt. This exercise is Effective Prompting in Practice. Goal: Write constrained prompts and reusable templates for real tasks.. Follow the detailed steps in slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Task: Fix the bug where get_user_email(user_id) returns None for valid users. Constraints: - Do NOT change the function signature - Do NOT add new imports - Do NOT modify other functions - Do NOT add print statements (use existing logger) Output format: Show exact diff and explain root cause. Success criteria: Function returns email string for valid user IDs.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Task: Fix the bug where get_user_email(user_id) returns None for valid users.  Constraints: - Do NOT change the function signature - Do NOT add new imports - Do NOT modify other functions - Do NOT add print statements (use existing logger)  Output format: Show exact diff and explain root cause. Success criteria: Function returns email string for valid user IDs."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.4 — Steps 2–3

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**


**Step 2:** Compare constrained vs. unconstrained:
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

```
Fix get_user_email - it's returning None sometimes.
```

<!--
Hands-on time for Exercise 3.4 — Steps 2–3. This exercise is Effective Prompting in Practice. Goal: Write constrained prompts and reusable templates for real tasks.. Follow the detailed steps in slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Step 2: Compare constrained vs. unconstrained: Where: Cursor Agent panel — `Ctrl+L (or Ctrl+I` for inline Agent) Fix get_user_email - it's returning None sometimes.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Fix get_user_email - it's returning None sometimes."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.4 — Steps 2–3 (Part 2)

**Step 3:** Plan first:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Before making any changes, answer:
1. What files would need to change?
2. What is the root cause you suspect?
3. What are the risks?
4. Are there alternative approaches?

I will review before approving any code changes.
```

<!--
Hands-on time for Exercise 3.4 — Steps 2–3 (Part 2). This exercise is Effective Prompting in Practice. Goal: Write constrained prompts and reusable templates for real tasks.. Follow the detailed steps in slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md. 

Step 3: Plan first: Where: Cursor Agent panel — `Ctrl+L` Before making any changes, answer: 1. What files would need to change? 2. What is the root cause you suspect? 3. What are the risks? 4. Are there alternative approaches? I will review before approving any code changes.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Before making any changes, answer: 1. What files would need to change? 2. What is the root cause you suspect? 3. What are the risks? 4. Are there alternative approaches?  I will review before approving any code changes."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.4 — Steps 4–5

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**


**Step 4:** Negative constraints:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Add error handling to the file parser.

But DO NOT:
- Change the return type (must remain dict)
- Add external dependencies
- Swallow exceptions silently (always log them)
- Change the existing test file
```

<!--
Hands-on time for Exercise 3.4 — Steps 4–5. This exercise is Effective Prompting in Practice. Goal: Write constrained prompts and reusable templates for real tasks.. Follow the detailed steps in slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Step 4: Negative constraints: Where: Cursor Agent panel — `Ctrl+L` Add error handling to the file parser. But DO NOT: - Change the return type (must remain dict) - Add external dependencies - Swallow exceptions silently (always log them) - Change the existing test file

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Add error handling to the file parser.  But DO NOT: - Change the return type (must remain dict) - Add external dependencies - Swallow exceptions silently (always log them) - Change the existing test file"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.4 — Steps 4–5 (Part 2)

**Step 5:** One change at a time:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
First, add input validation. Just show me what you'd add — don't modify yet.
[Review] Now add the validation. Show the diff before I accept.
```

<!--
Hands-on time for Exercise 3.4 — Steps 4–5 (Part 2). This exercise is Effective Prompting in Practice. Goal: Write constrained prompts and reusable templates for real tasks.. Follow the detailed steps in slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md. 

Step 5: One change at a time: Where: Cursor Agent panel — `Ctrl+L` First, add input validation. Just show me what you'd add — don't modify yet. [Review] Now add the validation. Show the diff before I accept.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "First, add input validation. Just show me what you'd add — don't modify yet. [Review] Now add the validation. Show the diff before I accept."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 3.4 — Step 6: Prompt Templates

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

Save as `.cursor/prompt-templates.md`:

```
## Bug Fix Template
Task: [Describe bug]  File: [path]  Lines: [range]
Constraints: Do NOT change [signatures, imports]
Success criteria: [How to verify]

## Feature Addition Template
Plan first: Yes/No  Constraints: Do NOT break [existing functionality]

## Code Review Template
Focus: [Security, Performance, Edge cases]
Ignore: [Style, formatting]
```

**Success Criteria:** Constrained prompt · Plan first · Negative constraints · Template created

<!--
Hands-on time for Exercise 3.4 — Step 6: Prompt Templates. This exercise is Effective Prompting in Practice. Goal: Write constrained prompts and reusable templates for real tasks.. Follow the detailed steps in slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Save as .cursor/prompt-templates.md: Task: [Describe bug]  File: [path]  Lines: [range] Constraints: Do NOT change [signatures, imports] Success criteria: [How to verify] Plan first: Yes/No  Constraints: Do NOT break [existing functionality] Focus: [Security, Performance, Edge cases] Ignore: [Style, formatting] Success Criteria: Constrained prompt · Plan first · Negative constraints · Template created

Tell them to paste this prompt into the Agent (or read it aloud while they type): "## Bug Fix Template Task: [Describe bug]  File: [path]  Lines: [range] Constraints: Do NOT change [signatures, imports] Success criteria: [How to verify]  ## Feature Addition Template Plan first: Yes/No  Constraints: Do NOT break [existing functionality]  ## Code Review Template Focus: [Security, Performance, Edge cases] Ignore: [Style, formatting]"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Module Summary

| Lesson | Topic | Key Takeaway |
|--------|-------|--------------|
| 3.1 | Ask vs Agent Mode | Use Ask for questions, Agent for action |
| 3.2 | Browser Tool | Agent can see live pages and console |
| 3.3 | Terminal Tool | Agent can run commands and react |
| 3.4 | Effective Prompting | Boundaries prevent scope creep |

<!--
Module 3 summary. In sixty seconds, walk the lesson table and restate one key insight per row.

Ask the closing question: what will you do differently on Monday? Take two or three answers.

Announce the break or introduce the next module with one connecting sentence.
-->

---


## Quick Reference Card

<img src="assets/module-03/quick-reference-card.svg" alt="Quick Reference Card" />

<!--
This quick reference slide is meant for post-course use. Tell participants to screenshot it or copy the commands into their team wiki.

Offer two minutes for questions on this module only, then move on.
-->

---


<!-- _header: 'Module 4 — Customizing Cursor for Your Team' -->

<!-- _class: lead -->

# Customizing Cursor for Your Team

## Module 4 · Day 1 (Hands-On + Walkthrough)

Cursor Training Program · ~60 min

<!--
We are starting Module 4: Customizing Cursor for Your Team. Cursor Training Program · ~60 min State the module goal in plain language: what participants will be able to do when we finish — not just what topics we will mention.

Preview whether this module is lecture, hands-on, or mixed. If it is hands-on, tell people when to open their laptops and which folder or repo to use. If it is concept-only, ask them to listen for one idea they can use on Monday morning.
-->

---


## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise + walkthrough |
| **Prerequisites** | Modules 1–3 completed, team repository access, Cursor installed |
| **Module Goal** | Customize Cursor for team workflows with rules, skills, MCP, and subagents |

<!--
This module overview slide sets expectations. In your own words, cover: Duration is ~60 minutes. Format is Hands-on exercise + walkthrough. Prerequisites is Modules 1–3 completed, team repository access, Cursor installed. Module Goal is Customize Cursor for team workflows with rules, skills, MCP, and subagents.  Call out prerequisites explicitly and pause until anyone blocked by missing tools has help. Do not read the table word-for-word — translate it into what the room will experience in the next hour.
-->

---


## Learning Objectives

By the end of this module, participants will be able to:

- Create Rules that encode team conventions and guardrails
- Write Repository Instructions for lightweight project guidance
- Build and invoke reusable Skills for specialized workflows
- Connect external tools via MCP and create slash workflows
- Understand when and how to use Subagents for delegation

<!--
These learning objectives describe outcomes, not topics. Paraphrase them: Create Rules that encode team conventions and guardrails. Write Repository Instructions for lightweight project guidance. Build and invoke reusable Skills for specialized workflows. Connect external tools via MCP and create slash workflows. Understand when and how to use Subagents for delegation.

Ask the room: which of these would help your team most this quarter? Note one or two answers — you can refer back at the module summary.

Tell participants they are not expected to memorize this list; they should recognize each outcome when they have done it during an exercise or demo.
-->

---


## Agenda

| Lesson | Topic | Time |
|--------|-------|------|
| 4.1 | Creating a Rule | 20 min |
| 4.2 | Repository Instructions | 13 min |
| 4.3 | Creating and Invoking a Skill | 20 min |
| 4.4 | MCP, Hooks, and Slash Workflows | 10 min |
| 4.5 | Subagents | 6 min |

<!--
Use this agenda as your pacing map for the module. You will cover: Lesson 4.1, Creating a Rule, about 20 min; Lesson 4.2, Repository Instructions, about 13 min; Lesson 4.3, Creating and Invoking a Skill, about 20 min; Lesson 4.4, MCP, Hooks, and Slash Workflows, about 10 min; Lesson 4.5, Subagents, about 6 min. Announce when the next hands-on block starts so people can close email and open Cursor. If you fall behind, shorten concept repetition before cutting exercise time.
-->

---


<!-- _class: lead -->

# Lesson 4.1

## Creating a Rule

*Concept · 8 min · Exercise · 12 min*

<!--
We now begin Lesson 4.1: Creating a Rule. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Create Cursor rules that persist coding standards for your team. Open the lab guide at slide-exercises/module-04/exercise-4.1-creating-a-rule.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What Are Rules?

Rules are Markdown files (`.cursor/rules/*.mdc`) with persistent instructions the agent automatically applies.

| Rule Type | Scope | When Applied | Example |
|-----------|-------|--------------|---------|
| **Global** | All projects | Always | "Use American English spelling" |
| **Project** | Specific repo | When opening that project | "Run `make test` before suggesting changes" |
| **File pattern** | Matching files | When editing those files | "For `*.py` files, use type hints" |
| **User** | Your account | Always across all projects | "Explain like I'm a junior developer" |

<!--
Walk this table conversationally: Rule Type — Scope, When Applied. Global — All projects, Always. Project — Specific repo, When opening that project. File pattern — Matching files, When editing those files. User — Your account, Always across all projects. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Rule Structure

```markdown

<!--
Rule Structure Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.
-->

---


description: Brief description of what this rule does
globs: *.py, src/**/*.js
alwaysApply: true

<!--
For slide 178, description: Brief description of what this rule does globs: .py, src//.js alway…: description: Brief description of what this rule does globs: .py, src//.js alwaysApply: true

Check for questions before you advance. If the room is silent, ask a specific question tied to the slide content.
-->

---


# Rule Title

## Instructions for the Agent
Write your instructions here in natural language.

## Examples
Good: ...  Bad: ...
```

<!--
Write your instructions here in natural language. Good: ...  Bad: ... Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.
-->

---


## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Cursor Agent panel** (`Ctrl+L`) is for natural-language prompts — not a shell.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Pause the slide deck for environment setup. Everyone should open PowerShell or Git Bash in Cursor's integrated terminal.

For API exercises: set keys with `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY` — never commit keys to git. On Windows, use `curl.exe` rather than the PowerShell curl alias when the lab shows curl commands.

Walk the room for two to three minutes. Common blockers: wrong key type, missing curl, wrong working directory. Do not advance until most pairs show a successful test call or are paired with someone who has.
-->

---


## Exercise 4.1 — Step 1: Setup

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)

```bash
mkdir -p .cursor/rules
```

Create **coding standards** rule at `.cursor/rules/coding-standards.mdc`:

```
globs: **/*.{js,ts,py}  |  alwaysApply: true

Python: type hints, Black (88 chars), Google docstrings
JS/TS: const over let, arrow functions, optional chaining
General: no commented-out code, no console.log in prod
```

<!--
Hands-on time for Exercise 4.1 — Step 1: Setup. This exercise is Creating a Rule. Goal: Create Cursor rules that persist coding standards for your team.. Follow the detailed steps in slide-exercises/module-04/exercise-4.1-creating-a-rule.md. 

Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts) mkdir -p .cursor/rules Create coding standards rule at .cursor/rules/coding-standards.mdc: globs: */.{js,ts,py}  |  alwaysApply: true Python: type hints, Black (88 chars), Google docstrings JS/TS: const over let, arrow functions, optional chaining General: no commented-out code, no console.log in prod

Tell them to paste this prompt into the Agent (or read it aloud while they type): "mkdir -p .cursor/rules"

Tell them to paste this prompt into the Agent (or read it aloud while they type): "globs: **/*.{js,ts,py}  |  alwaysApply: true  Python: type hints, Black (88 chars), Google docstrings JS/TS: const over let, arrow functions, optional chaining General: no commented-out code, no console.log in prod"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 4.1 — Build & Test Rule

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

Create `.cursor/rules/build-and-test.mdc`:

```
Before changes: git status, git diff
After changes:  make test / pytest / npm test → make lint
Do NOT suggest changes that break tests or need undocumented API keys
```

Create `.cursor/rules/security.mdc`:

```
Never: hardcoded secrets, eval() on user input, SQL concatenation
Always: input validation, rate limiting, HTTPS, safe error messages
Flag: exec/eval with user input, password/secret in variable names
```

<!--
Hands-on time for Exercise 4.1 — Build & Test Rule. This exercise is Creating a Rule. Goal: Create Cursor rules that persist coding standards for your team.. Follow the detailed steps in slide-exercises/module-04/exercise-4.1-creating-a-rule.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Create .cursor/rules/build-and-test.mdc: Before changes: git status, git diff After changes:  make test / pytest / npm test → make lint Do NOT suggest changes that break tests or need undocumented API keys Create .cursor/rules/security.mdc: Never: hardcoded secrets, eval() on user input, SQL concatenation Always: input validation, rate limiting, HTTPS, safe error messages Flag: exec/eval with user input, password/secret in variable names

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Before changes: git status, git diff After changes:  make test / pytest / npm test → make lint Do NOT suggest changes that break tests or need undocumented API keys"

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Never: hardcoded secrets, eval() on user input, SQL concatenation Always: input validation, rate limiting, HTTPS, safe error messages Flag: exec/eval with user input, password/secret in variable names"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 4.1 — Test & File-Specific Rules

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**


**Step 5:** Verify rules are applied:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Based on the project rules, what are the coding standards I should follow?
What are the security guardrails?
```

<!--
Hands-on time for Exercise 4.1 — Test & File-Specific Rules. This exercise is Creating a Rule. Goal: Create Cursor rules that persist coding standards for your team.. Follow the detailed steps in slide-exercises/module-04/exercise-4.1-creating-a-rule.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Step 5: Verify rules are applied: Where: Cursor Agent panel — `Ctrl+L` Based on the project rules, what are the coding standards I should follow? What are the security guardrails?

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Based on the project rules, what are the coding standards I should follow? What are the security guardrails?"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 4.1 — Test & File-Specific Rules (Part 2)

**Step 6:** Create `.cursor/rules/react-components.mdc` for `**/*.jsx, **/*.tsx`:
**Where:** **Cursor Agent panel** — ``Ctrl+L``
- Component structure, naming (PascalCase, handleSubmit)
- Performance: React.memo, useCallback, useMemo
- Accessibility: keyboard nav, alt text, semantic HTML

**Success Criteria:** Created rules directory · coding, build, security rules · verified application

<!--
Hands-on time for Exercise 4.1 — Test & File-Specific Rules (Part 2). This exercise is Creating a Rule. Goal: Create Cursor rules that persist coding standards for your team.. Follow the detailed steps in slide-exercises/module-04/exercise-4.1-creating-a-rule.md. 

Step 6: Create .cursor/rules/react-components.mdc for */.jsx, */.tsx: Where: Cursor Agent panel — `Ctrl+L` - Component structure, naming (PascalCase, handleSubmit) - Performance: React.memo, useCallback, useMemo - Accessibility: keyboard nav, alt text, semantic HTML Success Criteria: Created rules directory · coding, build, security rules · verified application

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 4.2

## Repository Instructions

*Concept · 5 min · Exercise · 8 min*

<!--
We now begin Lesson 4.2: Repository Instructions. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Add repository instructions the Agent reads automatically. Open the lab guide at slide-exercises/module-04/exercise-4.2-repository-instructions.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Rules vs. Repository Instructions

| Aspect | Rules | Repository Instructions |
|--------|-------|------------------------|
| **Location** | `.cursor/rules/*.mdc` | `.cursor/repository-instructions.md` |
| **Complexity** | Multiple files, scoped | Single file, global |
| **Granularity** | Per-file patterns | Entire repository |
| **Use case** | Detailed standards | High-level project overview |

<!--
Walk this table conversationally: Aspect — Rules, Repository Instructions. Location — .cursor/rules/*.mdc, .cursor/repository-instructions.md. Complexity — Multiple files, scoped, Single file, global. Granularity — Per-file patterns, Entire repository. Use case — Detailed standards, High-level project overview. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Repository Instructions Structure

```markdown
# Repository Instructions for [Project Name]

## Project Purpose
## Key Technologies
## Architecture Overview
## Important Conventions
## Common Tasks (make dev, make test, make build)
## External Dependencies
## Contact
```

<!--
Repository Instructions Structure Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "# Repository Instructions for [Project Name]" and explain why it matters.
-->

---


## Exercise 4.2 — Create Instructions

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

Create `.cursor/repository-instructions.md`:

<img src="assets/module-04/exercise-4-2-create-instructions.svg" alt="Exercise 4.2 — Create Instructions" />

<!--
Hands-on time for Exercise 4.2 — Create Instructions. This exercise is Repository Instructions. Goal: Add repository instructions the Agent reads automatically.. Follow the detailed steps in slide-exercises/module-04/exercise-4.2-repository-instructions.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Create .cursor/repository-instructions.md: <img src="assets/module-04/exercise-4-2-create-instructions.svg" alt="Exercise 4.2 — Create Instructions" />

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 4.2 — Verify & Maintain

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**


**Step 2:** Ask the Agent:
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

```
What are the key technologies used in this project?
How do I run the tests?
```

<!--
Hands-on time for Exercise 4.2 — Verify & Maintain. This exercise is Repository Instructions. Goal: Add repository instructions the Agent reads automatically.. Follow the detailed steps in slide-exercises/module-04/exercise-4.2-repository-instructions.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Step 2: Ask the Agent: Where: Cursor Agent panel — `Ctrl+L (or Ctrl+I` for inline Agent) What are the key technologies used in this project? How do I run the tests?

Tell them to paste this prompt into the Agent (or read it aloud while they type): "What are the key technologies used in this project? How do I run the tests?"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 4.2 — Verify & Maintain (Part 2)

**Step 3:** Update instructions when:
**Where:** **Cursor Agent panel** — ``Ctrl+L``
- New team members join → add contact info
- Architecture changes → update structure
- New dependencies or common issues discovered

**Success Criteria:** Created instructions · included purpose, stack, commands · verified agent access

<!--
Hands-on time for Exercise 4.2 — Verify & Maintain (Part 2). This exercise is Repository Instructions. Goal: Add repository instructions the Agent reads automatically.. Follow the detailed steps in slide-exercises/module-04/exercise-4.2-repository-instructions.md. 

Step 3: Update instructions when: Where: Cursor Agent panel — `Ctrl+L` - New team members join → add contact info - Architecture changes → update structure - New dependencies or common issues discovered Success Criteria: Created instructions · included purpose, stack, commands · verified agent access

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 4.3

## Creating and Invoking a Skill

*Concept · 8 min · Exercise · 12 min*

<!--
We now begin Lesson 4.3: Creating and Invoking a Skill. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Build and invoke reusable Agent skills for repeated workflows. Open the lab guide at slide-exercises/module-04/exercise-4.3-creating-and-invoking-a-skill.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What Is a Skill?

A reusable, specialized workflow the agent loads and follows — a **"prompt template with memory."**

<img src="assets/module-04/what-is-a-skill.svg" alt="What Is a Skill?" />

| Use Case | Example Skill |
|----------|---------------|
| Frequent task | "PR Review" |
| Complex workflow | "Onboarding" |
| Domain-specific | "Security Audit" |
| Documentation | "Generate API Docs" |

<!--
This slide is visual: What Is a Skill?. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Exercise 4.3 — PR Review Skill

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

Create `.cursor/skills/pr-review/SKILL.md`:

```
name: pr-review
description: Review a PR for code quality, security, and team standards

Step 1: Fetch diff (git fetch + git diff main...FETCH_HEAD)
Step 2: Review — code quality, security, testing, docs, style
Step 3: Output formatted review with Critical / Warning / Suggestion
Verdict: APPROVE / REQUEST CHANGES / COMMENT
```

<!--
Hands-on time for Exercise 4.3 — PR Review Skill. This exercise is Creating and Invoking a Skill. Goal: Build and invoke reusable Agent skills for repeated workflows.. Follow the detailed steps in slide-exercises/module-04/exercise-4.3-creating-and-invoking-a-skill.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Create .cursor/skills/pr-review/SKILL.md: name: pr-review description: Review a PR for code quality, security, and team standards Step 1: Fetch diff (git fetch + git diff main...FETCH_HEAD) Step 2: Review — code quality, security, testing, docs, style Step 3: Output formatted review with Critical / Warning / Suggestion Verdict: APPROVE / REQUEST CHANGES / COMMENT

Tell them to paste this prompt into the Agent (or read it aloud while they type): "name: pr-review description: Review a PR for code quality, security, and team standards  Step 1: Fetch diff (git fetch + git diff main...FETCH_HEAD) Step 2: Review — code quality, security, testing, docs, style Step 3: Output formatted review with Critical / Warning / Suggestion Verdict: APPROVE / REQUEST CHANGES / COMMENT"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 4.3 — Security Audit Skill

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

Create `.cursor/skills/security-audit/SKILL.md`:

```
Scan for:
  Critical: hardcoded secrets, SQL injection, command injection, eval()
  Medium:   no input validation, weak crypto, missing CSRF
  Low:      debug endpoints, verbose errors, outdated deps

Output: report with line numbers, fix suggestions, overall risk rating
```

<!--
Hands-on time for Exercise 4.3 — Security Audit Skill. This exercise is Creating and Invoking a Skill. Goal: Build and invoke reusable Agent skills for repeated workflows.. Follow the detailed steps in slide-exercises/module-04/exercise-4.3-creating-and-invoking-a-skill.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Create .cursor/skills/security-audit/SKILL.md: Scan for: Critical: hardcoded secrets, SQL injection, command injection, eval() Medium:   no input validation, weak crypto, missing CSRF Low:      debug endpoints, verbose errors, outdated deps Output: report with line numbers, fix suggestions, overall risk rating

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Scan for:   Critical: hardcoded secrets, SQL injection, command injection, eval()   Medium:   no input validation, weak crypto, missing CSRF   Low:      debug endpoints, verbose errors, outdated deps  Output: report with line numbers, fix suggestions, overall risk rating"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 4.3 — Invoke Skills

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**


**Step 4:** Invoke via slash command:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
/pr-review PR #42
/pr-review feature/payment-integration
```

<!--
Hands-on time for Exercise 4.3 — Invoke Skills. This exercise is Creating and Invoking a Skill. Goal: Build and invoke reusable Agent skills for repeated workflows.. Follow the detailed steps in slide-exercises/module-04/exercise-4.3-creating-and-invoking-a-skill.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Step 4: Invoke via slash command: Where: Cursor Agent panel — `Ctrl+L` /pr-review PR #42 /pr-review feature/payment-integration

Tell them to paste this prompt into the Agent (or read it aloud while they type): "/pr-review PR #42 /pr-review feature/payment-integration"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 4.3 — Invoke Skills (Part 2)

**Step 5:** List available skills:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
What skills are available in this project?
```

<!--
Hands-on time for Exercise 4.3 — Invoke Skills (Part 2). This exercise is Creating and Invoking a Skill. Goal: Build and invoke reusable Agent skills for repeated workflows.. Follow the detailed steps in slide-exercises/module-04/exercise-4.3-creating-and-invoking-a-skill.md. 

Step 5: List available skills: Where: Cursor Agent panel — `Ctrl+L` What skills are available in this project?

Tell them to paste this prompt into the Agent (or read it aloud while they type): "What skills are available in this project?"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 4.3 — Invoke Skills (Part 3)

**Step 6:** Create **Onboarding** skill — generates setup checklist from repo instructions
**Where:** **Cursor Agent panel** — ``Ctrl+L``

**Success Criteria:** Created skills · built PR Review + Security Audit · invoked via slash command

<!--
Hands-on time for Exercise 4.3 — Invoke Skills (Part 3). This exercise is Creating and Invoking a Skill. Goal: Build and invoke reusable Agent skills for repeated workflows.. Follow the detailed steps in slide-exercises/module-04/exercise-4.3-creating-and-invoking-a-skill.md. 

Step 6: Create Onboarding skill — generates setup checklist from repo instructions Where: Cursor Agent panel — `Ctrl+L` Success Criteria: Created skills · built PR Review + Security Audit · invoked via slash command

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 4.4

## MCP, Hooks, and Slash Workflows

*Concept · 10 min · Walkthrough*

<!--
We now begin Lesson 4.4: MCP, Hooks, and Slash Workflows. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What Is MCP?

MCP standardizes how AI agents discover and use external tools — **"USB port for AI."**

<img src="assets/module-04/what-is-mcp.svg" alt="What Is MCP?" />

| MCP Server | Capabilities |
|------------|--------------|
| **GitHub** | Create PRs, comment on issues, fetch reviews |
| **Slack** | Send messages, read channels |
| **Jira** | Create tickets, update status |
| **Database** | Query databases, run migrations |

<!--
This slide is visual: What Is MCP?. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Hooks & Slash Workflows

**Hooks** — scripts at specific agent workflow points:

| Hook | When It Runs | Use Case |
|------|--------------|----------|
| `pre-tool-use` | Before tool call | Validate permissions, log |
| `post-tool-use` | After tool returns | Transform results, audit |
| `pre-prompt` | Before sending to model | Inject context, redact secrets |
| `post-response` | After agent responds | Format output, log |

**Slash workflows** — team commands combining MCP, hooks, and prompts:

| Command | What It Does |
|---------|--------------|
| `/onboard @newdev` | Onboarding skill + GitHub issue + Slack message |
| `/deploy staging` | Tests → build → deploy → notify team |
| `/bug-report` | Analyze error → create issue → assign on-call |

<!--
Walk this table conversationally: Hook — When It Runs, Use Case. pre-tool-use — Before tool call, Validate permissions, log. post-tool-use — After tool returns, Transform results, audit. pre-prompt — Before sending to model, Inject context, redact secrets. post-response — After agent responds, Format output, log. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Walkthrough: MCP Configuration

Create `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "command": "cursor-mcp-github",
      "args": ["--token", "${GITHUB_TOKEN}"]
    },
    "slack": {
      "command": "cursor-mcp-slack",
      "args": ["--token", "${SLACK_TOKEN}"]
    }
  }
}
```

```
Create a PR from feature/payment and request review from @alice
Send a message to #deploys: "Deployment starting"
```

<!--
This is a walkthrough slide: MCP Configuration. Show the configuration or file location on your machine; participants observe unless time allows typing along.

Explain where the setting lives in Cursor or in the repository, who on a team would maintain it, and how it differs from a rule, skill, or MCP server.
-->

---


## Walkthrough: Slash Command Example

Create `.cursor/commands/deploy.md`:

<img src="assets/module-04/walkthrough-slash-command-example.svg" alt="Walkthrough: Slash Command Example" />

Usage: `/deploy staging`

**Success Criteria:** Understood MCP, hooks, slash commands · saw configuration examples

<!--
This is a walkthrough slide: Slash Command Example. Show the configuration or file location on your machine; participants observe unless time allows typing along.

Explain where the setting lives in Cursor or in the repository, who on a team would maintain it, and how it differs from a rule, skill, or MCP server.
-->

---


<!-- _class: lead -->

# Lesson 4.5

## Subagents

*Concept · 6 min · Walkthrough*

<!--
We now begin Lesson 4.5: Subagents. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What Are Subagents?

Independent agent instances for specialized tasks — own context, tools, and instructions — then report back to the main agent.

<img src="assets/module-04/what-are-subagents.svg" alt="What Are Subagents?" />

<!--
This slide is visual: What Are Subagents?. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## When to Use Subagents

| Scenario | Why Subagent | Example |
|----------|--------------|---------|
| **Parallel work** | Multiple tasks simultaneously | Scan security AND generate docs |
| **Isolation** | Separate context | Analyze large file independently |
| **Specialization** | Different instructions | Security expert vs. UI designer |
| **Sandboxing** | Limit tool access | Read-only subagent for unknown code |

<!--
Walk this table conversationally: Scenario — Why Subagent, Example. Parallel work — Multiple tasks simultaneously, Scan security AND generate docs. Isolation — Separate context, Analyze large file independently. Specialization — Different instructions, Security expert vs. UI designer. Sandboxing — Limit tool access, Read-only subagent for unknown code. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Subagent vs. Tool vs. Skill

| Concept | Best for |
|---------|----------|
| **Tool** | Single action (read file, run command) |
| **Skill** | Multi-step workflow, same context |
| **Subagent** | Parallel, isolated, specialized work |

<!--
Walk this table conversationally: Concept — Best for. Tool — Single action (read file, run command). Skill — Multi-step workflow, same context. Subagent — Parallel, isolated, specialized work. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Walkthrough: Subagents in Action

**Task:** "Review codebase for security issues and generate API documentation"

**Without subagents:** Mixed context, sequential, slower

**With subagents (parallel):**
```
→ Subagent 1 (Security): scan all files, read-only
→ Subagent 2 (Docs): generate OpenAPI spec, write to docs/

Main Agent combines: security report + openapi.yaml
```

**Invoke:**
```
Spawn a security subagent to audit src/auth/ independently.
Meanwhile, I'll work on the frontend.
```

**Success Criteria:** Understood concept · parallel execution · recognized templates

<!--
This is a walkthrough slide: Subagents in Action. Show the configuration or file location on your machine; participants observe unless time allows typing along.

Explain where the setting lives in Cursor or in the repository, who on a team would maintain it, and how it differs from a rule, skill, or MCP server.
-->

---


## Module Summary

| Lesson | Topic | Key Output |
|--------|-------|------------|
| 4.1 | Creating a Rule | `.cursor/rules/*.mdc` files |
| 4.2 | Repository Instructions | `.cursor/repository-instructions.md` |
| 4.3 | Creating Skills | `.cursor/skills/*/SKILL.md` |
| 4.4 | MCP & Slash Commands | MCP config, slash commands |
| 4.5 | Subagents | Understanding of delegation |

<!--
Module 4 summary. In sixty seconds, walk the lesson table and restate one key insight per row.

Ask the closing question: what will you do differently on Monday? Take two or three answers.

Announce the break or introduce the next module with one connecting sentence.
-->

---


## Quick Reference Card

<img src="assets/module-04/quick-reference-card.svg" alt="Quick Reference Card" />

<!--
This quick reference slide is meant for post-course use. Tell participants to screenshot it or copy the commands into their team wiki.

Offer two minutes for questions on this module only, then move on.
-->

---


<!-- _header: 'Module 5 — Cursor CLI and Local Automation' -->

<!-- _class: lead -->

# Cursor CLI and Local Automation

## Module 5 · Day 1 (Hands-On)

Cursor Training Program · ~60 min

<!--
We are starting Module 5: Cursor CLI and Local Automation. Cursor Training Program · ~60 min State the module goal in plain language: what participants will be able to do when we finish — not just what topics we will mention.

Preview whether this module is lecture, hands-on, or mixed. If it is hands-on, tell people when to open their laptops and which folder or repo to use. If it is concept-only, ask them to listen for one idea they can use on Monday morning.
-->

---


## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise |
| **Prerequisites** | Cursor CLI installed, terminal access, Modules 1–4 completed |
| **Module Goal** | Master the Cursor CLI for terminal-based AI workflows and automation |

<!--
This module overview slide sets expectations. In your own words, cover: Duration is ~60 minutes. Format is Hands-on exercise. Prerequisites is Cursor CLI installed, terminal access, Modules 1–4 completed. Module Goal is Master the Cursor CLI for terminal-based AI workflows and automation.  Call out prerequisites explicitly and pause until anyone blocked by missing tools has help. Do not read the table word-for-word — translate it into what the room will experience in the next hour.
-->

---


## Learning Objectives

By the end of this module, participants will be able to:

- Use the Cursor CLI in interactive mode for real-time AI collaboration
- Run one-shot CLI commands for scripting and CI/CD integration
- Hand off local sessions to Cloud Agents for remote execution
- List, resume, and manage concurrent sessions effectively

<!--
These learning objectives describe outcomes, not topics. Paraphrase them: Use the Cursor CLI in interactive mode for real-time AI collaboration. Run one-shot CLI commands for scripting and CI/CD integration. Hand off local sessions to Cloud Agents for remote execution. List, resume, and manage concurrent sessions effectively.

Ask the room: which of these would help your team most this quarter? Note one or two answers — you can refer back at the module summary.

Tell participants they are not expected to memorize this list; they should recognize each outcome when they have done it during an exercise or demo.
-->

---


## Agenda

| Lesson | Topic | Time |
|--------|-------|------|
| 5.1 | Interactive CLI | 20 min |
| 5.2 | One-Shot CLI | 20 min |
| 5.3 | Cloud Handoff | 18 min |
| 5.4 | Listing and Resuming Sessions | 20 min |

<!--
Use this agenda as your pacing map for the module. You will cover: Lesson 5.1, Interactive CLI, about 20 min; Lesson 5.2, One-Shot CLI, about 20 min; Lesson 5.3, Cloud Handoff, about 18 min; Lesson 5.4, Listing and Resuming Sessions, about 20 min. Announce when the next hands-on block starts so people can close email and open Cursor. If you fall behind, shorten concept repetition before cutting exercise time.
-->

---


<!-- _class: lead -->

# Lesson 5.1

## Interactive CLI

*Concept · 8 min · Exercise · 12 min*

<!--
We now begin Lesson 5.1: Interactive CLI. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Start an interactive Cursor CLI session from the terminal. Open the lab guide at slide-exercises/module-05/exercise-5.1-interactive-cli.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What Is the Cursor CLI?

The Cursor CLI brings AI-powered coding directly to your command line.

- Start AI sessions from your terminal
- Get code assistance without leaving your workflow
- Automate coding tasks with scripts
- Integrate AI into existing CLI tools

**Primary command:** `agent` (main entry point)

<!--
On this slide, What Is the Cursor CLI?, cover these points in order: F i r s t ,   S t a r t   A I   s e s s i o n s   f r o m   y o u r   t e r m i n a l . Next, Get code assistance without leaving your workflow. Next, Automate coding tasks with scripts. Next, Integrate AI into existing CLI tools.
-->

---


## Interactive Mode Commands

| Command | Purpose |
|---------|---------|
| `/model` | Switch between AI models interactively |
| `/compress` | Summarize conversation, free up context window |
| `/rules` | Create and edit rules directly from CLI |
| `/commands` | Create and modify custom commands |
| `/mcp enable/disable` | Manage MCP servers |
| `/usage` | View Cursor usage stats |
| `/about` | View environment and CLI configuration |
| `/resume` | View and resume previous sessions |

<!--
Walk this table conversationally: Command — Purpose. /model — Switch between AI models interactively. /compress — Summarize conversation, free up context window. /rules — Create and edit rules directly from CLI. /commands — Create and modify custom commands. /mcp enable/disable — Manage MCP servers. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Cursor Agent panel** (`Ctrl+L`) is for natural-language prompts — not a shell.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Pause the slide deck for environment setup. Everyone should open PowerShell or Git Bash in Cursor's integrated terminal.

For API exercises: set keys with `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY` — never commit keys to git. On Windows, use `curl.exe` rather than the PowerShell curl alias when the lab shows curl commands.

Walk the room for two to three minutes. Common blockers: wrong key type, missing curl, wrong working directory. Do not advance until most pairs show a successful test call or are paired with someone who has.
-->

---


## Exercise 5.1 — Steps 1–2

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)


**Step 1:** Start an interactive session
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent
agent "Help me understand the current codebase structure"
```

<!--
Hands-on time for Exercise 5.1 — Steps 1–2. This exercise is Interactive CLI. Goal: Start an interactive Cursor CLI session from the terminal.. Follow the detailed steps in slide-exercises/module-05/exercise-5.1-interactive-cli.md. 

Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts) Step 1: Start an interactive session Terminal: PowerShell — unless step notes Git Bash or WSL agent agent "Help me understand the current codebase structure"

Tell them to paste this prompt into the Agent (or read it aloud while they type): "agent agent "Help me understand the current codebase structure""

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.1 — Steps 1–2 (Part 2)

**Step 2:** Navigate the session (inside the running `agent` session — same terminal window) — unless step notes Git Bash or WSL
- Type prompts naturally
- `Shift+Enter` — new line without submitting
- `Enter` — submit prompt
- `Ctrl+D` twice — exit

<!--
Hands-on time for Exercise 5.1 — Steps 1–2 (Part 2). This exercise is Interactive CLI. Goal: Start an interactive Cursor CLI session from the terminal.. Follow the detailed steps in slide-exercises/module-05/exercise-5.1-interactive-cli.md. 

Step 2: Navigate the session (inside the running agent session — same terminal window) — unless step notes Git Bash or WSL - Type prompts naturally - Shift+Enter — new line without submitting - Enter — submit prompt - Ctrl+D twice — exit

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.1 — Steps 3–5

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)


**Step 3:** Switch models:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```
/model
# Or list models outside session:
agent --list-models
```

<!--
Hands-on time for Exercise 5.1 — Steps 3–5. This exercise is Interactive CLI. Goal: Start an interactive Cursor CLI session from the terminal.. Follow the detailed steps in slide-exercises/module-05/exercise-5.1-interactive-cli.md. 

Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts) Step 3: Switch models: Terminal: PowerShell — unless step notes Git Bash or WSL /model agent --list-models

Tell them to paste this prompt into the Agent (or read it aloud while they type): "/model # Or list models outside session: agent --list-models"

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.1 — Steps 3–5 (Part 2)

**Step 4:** Ask Mode (read-only):
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

```bash
agent --mode=ask "What does this project's main function do?"
# Or inside session: /ask
```

<!--
Hands-on time for Exercise 5.1 — Steps 3–5 (Part 2). This exercise is Interactive CLI. Goal: Start an interactive Cursor CLI session from the terminal.. Follow the detailed steps in slide-exercises/module-05/exercise-5.1-interactive-cli.md. 

Step 4: Ask Mode (read-only): Where: Cursor Agent panel — `Ctrl+L (or Ctrl+I` for inline Agent) agent --mode=ask "What does this project's main function do?"

Tell them to paste this prompt into the Agent (or read it aloud while they type): "agent --mode=ask "What does this project's main function do?" # Or inside session: /ask"

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.1 — Steps 3–5 (Part 3)

**Step 5:** Plan Mode:
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

```bash
agent --mode=plan "Add user authentication to this API"
```

<!--
Hands-on time for Exercise 5.1 — Steps 3–5 (Part 3). This exercise is Interactive CLI. Goal: Start an interactive Cursor CLI session from the terminal.. Follow the detailed steps in slide-exercises/module-05/exercise-5.1-interactive-cli.md. 

Step 5: Plan Mode: Where: Cursor Agent panel — `Ctrl+L (or Ctrl+I` for inline Agent) agent --mode=plan "Add user authentication to this API"

Tell them to paste this prompt into the Agent (or read it aloud while they type): "agent --mode=plan "Add user authentication to this API""

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.1 — Steps 6–7

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)


**Step 6:** Configure status line:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
npx -y cursor-statusline
# Shows: [model: claude-4.5-sonnet] [~/project] [main] [ctx: 45k/200k]
```

<!--
Hands-on time for Exercise 5.1 — Steps 6–7. This exercise is Interactive CLI. Goal: Start an interactive Cursor CLI session from the terminal.. Follow the detailed steps in slide-exercises/module-05/exercise-5.1-interactive-cli.md. 

Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts) Step 6: Configure status line: Terminal: PowerShell — unless step notes Git Bash or WSL npx -y cursor-statusline

Tell them to paste this prompt into the Agent (or read it aloud while they type): "npx -y cursor-statusline # Shows: [model: claude-4.5-sonnet] [~/project] [main] [ctx: 45k/200k]"

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.1 — Steps 6–7 (Part 2)

**Step 7:** Terminal key bindings:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent /setup-terminal
```

<!--
Hands-on time for Exercise 5.1 — Steps 6–7 (Part 2). This exercise is Interactive CLI. Goal: Start an interactive Cursor CLI session from the terminal.. Follow the detailed steps in slide-exercises/module-05/exercise-5.1-interactive-cli.md. 

Step 7: Terminal key bindings: Terminal: PowerShell — unless step notes Git Bash or WSL agent /setup-terminal

Tell them to paste this prompt into the Agent (or read it aloud while they type): "agent /setup-terminal"

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 5.2

## One-Shot CLI

*Concept · 8 min · Exercise · 12 min*

<!--
We now begin Lesson 5.2: One-Shot CLI. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Run single-shot Agent commands from scripts and CI. Open the lab guide at slide-exercises/module-05/exercise-5.2-one-shot-cli.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## One-Shot Command Structure

```bash
agent "your prompt here"                    # Basic one-shot
agent --mode=ask "question about code"      # Read-only
agent --model claude-4.5-sonnet "task"      # Specific model
agent --non-interactive "run this task"     # No prompts, just output
```

> *"Perfect for automation, CI/CD pipelines, and batch operations."*

<!--
Read or closely paraphrase the quote on screen: "Perfect for automation, CI/CD pipelines, and batch operations."

agent "your prompt here"                    # Basic one-shot agent --mode=ask "question about code"      # Read-only agent --model claude-4.5-sonnet "task"      # Specific model agent --non-interactive "run this task"     # No prompts, just output

Pause two beats after the quote so it lands. Then ask whether anyone has seen the opposite problem in real projects.
-->

---


## Use Cases for One-Shot CLI

| Use Case | Example |
|----------|---------|
| **Code generation** | `agent "Create a React component for a login form"` |
| **Documentation** | `agent "Generate JSDoc comments for src/api.js"` |
| **CI/CD tasks** | `agent "Review this PR diff for security issues"` |
| **Batch processing** | Loop through files with `agent` commands |
| **Pre-commit hooks** | `agent --mode=ask "Check for console.log statements"` |

<!--
Walk this table conversationally: Use Case — Example. Code generation — agent "Create a React component for a login form". Documentation — agent "Generate JSDoc comments for src/api.js". CI/CD tasks — agent "Review this PR diff for security issues". Batch processing — Loop through files with agent commands. Pre-commit hooks — agent --mode=ask "Check for console.log statements". Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Exercise 5.2 — Steps 1–2

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)


**Step 1:** Basic one-shot commands:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent "What is the difference between let and const in JavaScript?"
agent "Write a bash function that checks if a port is in use"
agent --mode=ask "Explain the git rebase command with examples"
```

<!--
Hands-on time for Exercise 5.2 — Steps 1–2. This exercise is One-Shot CLI. Goal: Run single-shot Agent commands from scripts and CI.. Follow the detailed steps in slide-exercises/module-05/exercise-5.2-one-shot-cli.md. 

Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts) Step 1: Basic one-shot commands: Terminal: PowerShell — unless step notes Git Bash or WSL agent "What is the difference between let and const in JavaScript?" agent "Write a bash function that checks if a port is in use" agent --mode=ask "Explain the git rebase command with examples"

Tell them to paste this prompt into the Agent (or read it aloud while they type): "agent "What is the difference between let and const in JavaScript?" agent "Write a bash function that checks if a port is in use" agent --mode=ask "Explain the git rebase command with examples""

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.2 — Steps 1–2 (Part 2)

**Step 2:** Specify models:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent --model gpt-5-mini "What does this command do: ls -la | grep .txt"
agent --model claude-4.5-opus "Design a database schema for a task management system"
```

<!--
Hands-on time for Exercise 5.2 — Steps 1–2 (Part 2). This exercise is One-Shot CLI. Goal: Run single-shot Agent commands from scripts and CI.. Follow the detailed steps in slide-exercises/module-05/exercise-5.2-one-shot-cli.md. 

Step 2: Specify models: Terminal: PowerShell — unless step notes Git Bash or WSL agent --model gpt-5-mini "What does this command do: ls -la | grep .txt" agent --model claude-4.5-opus "Design a database schema for a task management system"

Tell them to paste this prompt into the Agent (or read it aloud while they type): "agent --model gpt-5-mini "What does this command do: ls -la | grep .txt" agent --model claude-4.5-opus "Design a database schema for a task management system""

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.2 — Scriptable Code Reviewer

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

Create `bin/ai-review.sh`:

```bash
#!/bin/bash
STAGED_FILES=$(git diff --cached --name-only | tr '\n' ', ')

agent --mode=ask "Review these staged files for common issues:
Files: $STAGED_FILES
Check for: debugging statements, unused imports,
security issues, missing error handling. Be concise."
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

<!--
Hands-on time for Exercise 5.2 — Scriptable Code Reviewer. This exercise is One-Shot CLI. Goal: Run single-shot Agent commands from scripts and CI.. Follow the detailed steps in slide-exercises/module-05/exercise-5.2-one-shot-cli.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe Create bin/ai-review.sh: STAGED_FILES=$(git diff --cached --name-only | tr '\n' ', ') agent --mode=ask "Review these staged files for common issues: Files: $STAGED_FILES Check for: debugging statements, unused imports, security issues, missing error handling. Be concise." PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "#!/bin/bash STAGED_FILES=$(git diff --cached --name-only | tr '\n' ', ')  agent --mode=ask "Review these staged files for common issues: Files: $STAGED_FILES Check for: debugging statements, unused imports, security issues, missing error handling. Be concise.""

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.2 — Batch & Git Hooks

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`


**Step 4:** Batch process files:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
for file in src/**/*.py; do
    agent --mode=ask --non-interactive \
      "Summarize this Python file in one sentence: $(head -50 $file)"
done
```

<!--
Hands-on time for Exercise 5.2 — Batch & Git Hooks. This exercise is One-Shot CLI. Goal: Run single-shot Agent commands from scripts and CI.. Follow the detailed steps in slide-exercises/module-05/exercise-5.2-one-shot-cli.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe Step 4: Batch process files: Terminal: PowerShell — unless step notes Git Bash or WSL for file in src/*/.py; do agent --mode=ask --non-interactive \ "Summarize this Python file in one sentence: $(head -50 $file)" done

Tell them to paste this prompt into the Agent (or read it aloud while they type): "for file in src/**/*.py; do     agent --mode=ask --non-interactive \       "Summarize this Python file in one sentence: $(head -50 $file)" done"

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.2 — Batch & Git Hooks (Part 2)

**Step 5:** Pre-commit hook — review staged diff for secrets, debug statements, merge markers
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

**Step 6:** CI/CD — analyze test output and suggest fixes for failures
**Terminal:** **PowerShell** — clone/open repo, then continue in Agent panel

**Success Criteria:** Ran one-shots · specified models · created reviewer script · understood CI/CD use

<!--
Hands-on time for Exercise 5.2 — Batch & Git Hooks (Part 2). This exercise is One-Shot CLI. Goal: Run single-shot Agent commands from scripts and CI.. Follow the detailed steps in slide-exercises/module-05/exercise-5.2-one-shot-cli.md. 

Step 5: Pre-commit hook — review staged diff for secrets, debug statements, merge markers Where: Cursor Agent panel — `Ctrl+L (or Ctrl+I` for inline Agent) Step 6: CI/CD — analyze test output and suggest fixes for failures Terminal: PowerShell — clone/open repo, then continue in Agent panel Success Criteria: Ran one-shots · specified models · created reviewer script · understood CI/CD use

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 5.3

## Cloud Handoff

*Concept · 8 min · Exercise · 10 min*

<!--
We now begin Lesson 5.3: Cloud Handoff. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Hand off a local CLI task to a Cloud Agent with &. Open the lab guide at slide-exercises/module-05/exercise-5.3-cloud-handoff.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What Is Cloud Handoff?

Send a local conversation to a Cloud Agent:

- Continue from web or mobile (`cursor.com/agents`)
- Let the agent run long tasks while you're away
- Resume the session later from any device

**The `&` prefix:** Prepend any message with `&` to send it to the cloud.

<!--
On this slide, What Is Cloud Handoff?, cover these points in order: F i r s t ,   C o n t i n u e   f r o m   w e b   o r   m o b i l e   ( c u r s o r . c o m / a g e n t s ) . Next, Let the agent run long tasks while you're away. Next, Resume the session later from any device.
-->

---


## Cloud Handoff Flow

<img src="assets/module-05/cloud-handoff-flow.svg" alt="Cloud Handoff Flow" />

<!--
This slide is visual: Cloud Handoff Flow. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Exercise 5.3 — Steps 1–3

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)


**Step 1:** Start local session and hand off:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent
& "Analyze the entire codebase and create a dependency graph."
```

<!--
Hands-on time for Exercise 5.3 — Steps 1–3. This exercise is Cloud Handoff. Goal: Hand off a local CLI task to a Cloud Agent with &.. Follow the detailed steps in slide-exercises/module-05/exercise-5.3-cloud-handoff.md. 

Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts) Step 1: Start local session and hand off: Terminal: PowerShell — unless step notes Git Bash or WSL agent & "Analyze the entire codebase and create a dependency graph."

Tell them to paste this prompt into the Agent (or read it aloud while they type): "agent & "Analyze the entire codebase and create a dependency graph.""

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.3 — Steps 1–3 (Part 2)

**Step 2:** Verify handoff:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```
🚀 Handing off to Cloud Agent...
✅ Session running at: https://cursor.com/agents/[agent-id]
```

<!--
Hands-on time for Exercise 5.3 — Steps 1–3 (Part 2). This exercise is Cloud Handoff. Goal: Hand off a local CLI task to a Cloud Agent with &.. Follow the detailed steps in slide-exercises/module-05/exercise-5.3-cloud-handoff.md. 

Step 2: Verify handoff: Terminal: PowerShell — unless step notes Git Bash or WSL 🚀 Handing off to Cloud Agent... ✅ Session running at: https://cursor.com/agents/[agent-id]

Tell them to paste this prompt into the Agent (or read it aloud while they type): "🚀 Handing off to Cloud Agent... ✅ Session running at: https://cursor.com/agents/[agent-id]"

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.3 — Steps 1–3 (Part 3)

**Step 3:** Check status via browser or CLI
**Where:** **Web browser** — Edge or Chrome

<!--
Hands-on time for Exercise 5.3 — Steps 1–3 (Part 3). This exercise is Cloud Handoff. Goal: Hand off a local CLI task to a Cloud Agent with &.. Follow the detailed steps in slide-exercises/module-05/exercise-5.3-cloud-handoff.md. 

Step 3: Check status via browser or CLI Where: Web browser — Edge or Chrome

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.3 — Steps 4–6

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)


**Step 4:** Push existing conversation:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```
& "Continue this conversation in the cloud. I need to log off."
```

<!--
Hands-on time for Exercise 5.3 — Steps 4–6. This exercise is Cloud Handoff. Goal: Hand off a local CLI task to a Cloud Agent with &.. Follow the detailed steps in slide-exercises/module-05/exercise-5.3-cloud-handoff.md. 

Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts) Step 4: Push existing conversation: Terminal: PowerShell — unless step notes Git Bash or WSL & "Continue this conversation in the cloud. I need to log off."

Tell them to paste this prompt into the Agent (or read it aloud while they type): "& "Continue this conversation in the cloud. I need to log off.""

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.3 — Steps 4–6 (Part 2)

**Step 5:** Long-running task:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent "& Refactor the auth module to use JWT. Update all tests and docs."
```

<!--
Hands-on time for Exercise 5.3 — Steps 4–6 (Part 2). This exercise is Cloud Handoff. Goal: Hand off a local CLI task to a Cloud Agent with &.. Follow the detailed steps in slide-exercises/module-05/exercise-5.3-cloud-handoff.md. 

Step 5: Long-running task: Terminal: PowerShell — unless step notes Git Bash or WSL agent "& Refactor the auth module to use JWT. Update all tests and docs."

Tell them to paste this prompt into the Agent (or read it aloud while they type): "agent "& Refactor the auth module to use JWT. Update all tests and docs.""

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.3 — Steps 4–6 (Part 3)

**Step 6:** Resume later:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent --resume [agent-id-from-cloud]
```

<!--
Hands-on time for Exercise 5.3 — Steps 4–6 (Part 3). This exercise is Cloud Handoff. Goal: Hand off a local CLI task to a Cloud Agent with &.. Follow the detailed steps in slide-exercises/module-05/exercise-5.3-cloud-handoff.md. 

Step 6: Resume later: Terminal: PowerShell — unless step notes Git Bash or WSL agent --resume [agent-id-from-cloud]

Tell them to paste this prompt into the Agent (or read it aloud while they type): "agent --resume [agent-id-from-cloud]"

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Cloud Handoff Best Practices

| When to Use | When Not to Use |
|-------------|-----------------|
| Long-running tasks (>5 min) | Quick questions |
| When you need to close laptop | Interactive debugging |
| Overnight batch processing | Tasks needing terminal access |
| Parallel work streams | Security-sensitive code (local only) |

**Success Criteria:** Sent `&` message · verified cloud agent · accessed via web

<!--
Walk this table conversationally: When to Use — When Not to Use. Long-running tasks (>5 min) — Quick questions. When you need to close laptop — Interactive debugging. Overnight batch processing — Tasks needing terminal access. Parallel work streams — Security-sensitive code (local only). Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


<!-- _class: lead -->

# Lesson 5.4

## Listing and Resuming Sessions

*Concept · 8 min · Exercise · 12 min*

<!--
We now begin Lesson 5.4: Listing and Resuming Sessions. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

List, name, resume, and compress CLI Agent sessions. Open the lab guide at slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Session Management Commands

| Command | Purpose |
|---------|---------|
| `/resume` | List all previous sessions and resume one |
| `agent --resume [id]` | Resume a specific session by ID |
| `agent --list` | List available sessions (alternative) |

**Tip:** Name sessions with the first message:

```bash
agent "Just say one word: auth-refactor"
# Session named "auth-refactor Agent"
```

<!--
Walk this table conversationally: Command — Purpose. /resume — List all previous sessions and resume one. agent --resume [id] — Resume a specific session by ID. agent --list — List available sessions (alternative). Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Exercise 5.4 — Steps 1–2

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)


**Step 1:** Create multiple named sessions:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent "Just say one word: frontend-cleanup"   # do work, exit
agent "Just say one word: db-optimization"  # do work, exit
agent "Just say one word: docs-update"
```

<!--
Hands-on time for Exercise 5.4 — Steps 1–2. This exercise is Listing and Resuming Sessions. Goal: List, name, resume, and compress CLI Agent sessions.. Follow the detailed steps in slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md. 

Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts) Step 1: Create multiple named sessions: Terminal: PowerShell — unless step notes Git Bash or WSL agent "Just say one word: frontend-cleanup"   # do work, exit agent "Just say one word: db-optimization"  # do work, exit agent "Just say one word: docs-update"

Tell them to paste this prompt into the Agent (or read it aloud while they type): "agent "Just say one word: frontend-cleanup"   # do work, exit agent "Just say one word: db-optimization"  # do work, exit agent "Just say one word: docs-update""

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.4 — Steps 1–2 (Part 2)

**Step 2:** List all sessions:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```
/resume
# 1. frontend-cleanup Agent (2 hours ago)
# 2. db-optimization Agent (1 hour ago)
# 3. docs-update Agent (30 minutes ago)
```

<!--
Hands-on time for Exercise 5.4 — Steps 1–2 (Part 2). This exercise is Listing and Resuming Sessions. Goal: List, name, resume, and compress CLI Agent sessions.. Follow the detailed steps in slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md. 

Step 2: List all sessions: Terminal: PowerShell — unless step notes Git Bash or WSL /resume

Tell them to paste this prompt into the Agent (or read it aloud while they type): "/resume # 1. frontend-cleanup Agent (2 hours ago) # 2. db-optimization Agent (1 hour ago) # 3. docs-update Agent (30 minutes ago)"

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.4 — Steps 3–5

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)


**Step 3:** Resume by ID:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent --resume abc123-def456-ghi789
```

<!--
Hands-on time for Exercise 5.4 — Steps 3–5. This exercise is Listing and Resuming Sessions. Goal: List, name, resume, and compress CLI Agent sessions.. Follow the detailed steps in slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md. 

Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts) Step 3: Resume by ID: Terminal: PowerShell — unless step notes Git Bash or WSL agent --resume abc123-def456-ghi789

Tell them to paste this prompt into the Agent (or read it aloud while they type): "agent --resume abc123-def456-ghi789"

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.4 — Steps 3–5 (Part 2)

**Step 4:** Concurrent sessions in different terminals:
**Where:** **Cursor Agent panel** — ``Ctrl+L`` (or ``Ctrl+I`` for inline Agent)

```bash
# Terminal 1: agent --resume frontend-cleanup
# Terminal 2: agent --resume db-optimization
```

<!--
Hands-on time for Exercise 5.4 — Steps 3–5 (Part 2). This exercise is Listing and Resuming Sessions. Goal: List, name, resume, and compress CLI Agent sessions.. Follow the detailed steps in slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md. 

Step 4: Concurrent sessions in different terminals: Where: Cursor Agent panel — `Ctrl+L (or Ctrl+I` for inline Agent)

Tell them to paste this prompt into the Agent (or read it aloud while they type): "# Terminal 1: agent --resume frontend-cleanup # Terminal 2: agent --resume db-optimization"

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.4 — Steps 3–5 (Part 3)

**Step 5:** Context management:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```
/compress   # Summarize conversation, free context window
```

<!--
Hands-on time for Exercise 5.4 — Steps 3–5 (Part 3). This exercise is Listing and Resuming Sessions. Goal: List, name, resume, and compress CLI Agent sessions.. Follow the detailed steps in slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md. 

Step 5: Context management: Terminal: PowerShell — unless step notes Git Bash or WSL /compress   # Summarize conversation, free context window

Tell them to paste this prompt into the Agent (or read it aloud while they type): "/compress   # Summarize conversation, free context window"

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 5.4 — Steps 6–7 & Best Practices

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**Step 6:** Export session summary as markdown
**Where:** **Cursor Agent panel** — ``Ctrl+L``

**Step 7:** Create `bin/cursor-sessions.sh` to list and manage sessions
**Where:** **Cursor Agent panel** — ``Ctrl+L``

**Naming:** Use `[area]-[task]` format (e.g., `api-auth-fix`)

**Context:** Use `/compress` on long sessions · cloud handoff for very long tasks

**Cleanup:** Sessions persist indefinitely — manually complete or discard finished ones

**Success Criteria:** Created named sessions · listed with `/resume` · resumed · used `/compress`

<!--
Hands-on time for Exercise 5.4 — Steps 6–7 & Best Practices. This exercise is Listing and Resuming Sessions. Goal: List, name, resume, and compress CLI Agent sessions.. Follow the detailed steps in slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Step 6: Export session summary as markdown Where: Cursor Agent panel — `Ctrl+L` Step 7: Create bin/cursor-sessions.sh to list and manage sessions Where: Cursor Agent panel — `Ctrl+L` Naming: Use [area]-[task] format (e.g., api-auth-fix) Context: Use /compress on long sessions · cloud handoff for very long tasks Cleanup: Sessions persist indefinitely — manually complete or discard finished ones Success Criteria: Created named sessions · listed with /resume · resumed · used /compress

Give work time now. Circulate quietly. Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Module Summary

| Lesson | Topic | Key Skill |
|--------|-------|-----------|
| 5.1 | Interactive CLI | Real-time terminal AI |
| 5.2 | One-Shot CLI | Scripting & automation |
| 5.3 | Cloud Handoff | Remote/long-running tasks |
| 5.4 | Session Management | Concurrent work handling |

<!--
Module 5 summary. In sixty seconds, walk the lesson table and restate one key insight per row.

Ask the closing question: what will you do differently on Monday? Take two or three answers.

Announce the break or introduce the next module with one connecting sentence.
-->

---


## Quick Reference Card

```
BASIC:
  agent                  Start interactive session
  agent "prompt"         One-shot command
  agent --mode=ask       Read-only mode
  agent --mode=plan      Plan before code
  agent --model <name>   Specify model

IN SESSION:  /model  /compress  /rules  /commands  /resume  /usage

CLOUD:  & "message"  →  cursor.com/agents

KEYS:  Shift+Enter (new line)  |  Ctrl+D twice (exit)
```

<!--
This quick reference slide is meant for post-course use. Tell participants to screenshot it or copy the commands into their team wiki.

Offer two minutes for questions on this module only, then move on.
-->

---


<!-- _class: lead -->

# Day 2

## Cloud Agents, APIs & Analytics

Cursor Training Program · Complete Course

<!--
Welcome back to Day 2. Yesterday we established how AI models behave and how to use Cursor safely in real repositories. Today we extend that work outside the IDE — CLI, Cloud Agents, and production-grade API integration.

Before we continue, confirm API keys are available where needed and that everyone can open a terminal and reach api.cursor.com from this network. We will use environment variables for every key — never paste secrets on screen or into chat logs.
-->

---


<!-- _header: 'Module 6 — Cloud Agents in the UI' -->

<!-- _class: lead -->

# Cloud Agents in the UI

## Module 6 · Day 2 (Hands-On + Demonstration)

Cursor Training Program · ~90 min

<!--
We are starting Module 6: Cloud Agents in the UI. Cursor Training Program · ~90 min State the module goal in plain language: what participants will be able to do when we finish — not just what topics we will mention.

Preview whether this module is lecture, hands-on, or mixed. If it is hands-on, tell people when to open their laptops and which folder or repo to use. If it is concept-only, ask them to listen for one idea they can use on Monday morning.
-->

---


## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~90 minutes |
| **Format** | Hands-on exercise + demonstration |
| **Prerequisites** | Cursor account, GitHub repository access, Modules 1–5 completed |
| **Module Goal** | Master Cloud Agents UI for remote execution, artifact collection, and messaging integrations |

<!--
This module overview slide sets expectations. In your own words, cover: Duration is ~90 minutes. Format is Hands-on exercise + demonstration. Prerequisites is Cursor account, GitHub repository access, Modules 1–5 completed. Module Goal is Master Cloud Agents UI for remote execution, artifact collection, and messaging integrations.  Call out prerequisites explicitly and pause until anyone blocked by missing tools has help. Do not read the table word-for-word — translate it into what the room will experience in the next hour.
-->

---


## Learning Objectives

By the end of this module, participants will be able to:

- Launch and monitor Cloud Agents from the Cursor UI
- Collect and download artifacts from completed cloud runs
- Trigger Cloud Agents from messaging platforms (Slack, Discord)
- Manage cloud agent history and settings

<!--
These learning objectives describe outcomes, not topics. Paraphrase them: Launch and monitor Cloud Agents from the Cursor UI. Collect and download artifacts from completed cloud runs. Trigger Cloud Agents from messaging platforms (Slack, Discord). Manage cloud agent history and settings.

Ask the room: which of these would help your team most this quarter? Note one or two answers — you can refer back at the module summary.

Tell participants they are not expected to memorize this list; they should recognize each outcome when they have done it during an exercise or demo.
-->

---


## Agenda

| Lesson | Topic | Time |
|--------|-------|------|
| 6.1 | Launching a Cloud Agent | 25 min |
| 6.2 | Cloud Agent Artifacts | 23 min |
| 6.3 | Cloud Agents from Messaging Platforms | 20 min |

<!--
Use this agenda as your pacing map for the module. You will cover: Lesson 6.1, Launching a Cloud Agent, about 25 min; Lesson 6.2, Cloud Agent Artifacts, about 23 min; Lesson 6.3, Cloud Agents from Messaging Platforms, about 20 min. Announce when the next hands-on block starts so people can close email and open Cursor. If you fall behind, shorten concept repetition before cutting exercise time.
-->

---


<!-- _class: lead -->

# Lesson 6.1

## Launching a Cloud Agent

*Concept · 10 min · Exercise · 15 min*

<!--
We now begin Lesson 6.1: Launching a Cloud Agent. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Launch a Cloud Agent from the Cursor UI and track its run. Open the lab guide at slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Cloud Agents vs. Local Agent

| Aspect | Local Agent | Cloud Agent |
|--------|-------------|-------------|
| **Runs on** | Your machine | Cursor's infrastructure |
| **Persistence** | Ends when you quit | Continues indefinitely |
| **Access** | Local only | Web, mobile, API |
| **Terminal access** | Your terminal | Simulated/scripted |
| **File access** | Local files | GitHub repos only |
| **Best for** | Interactive work | Batch, scheduled, hands-off |

<!--
Walk this table conversationally: Aspect — Local Agent, Cloud Agent. Runs on — Your machine, Cursor's infrastructure. Persistence — Ends when you quit, Continues indefinitely. Access — Local only, Web, mobile, API. Terminal access — Your terminal, Simulated/scripted. File access — Local files, GitHub repos only. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## When to Use Cloud Agents

**Good for:**
- Long-running tasks (>10 min) · Scheduled jobs
- Tasks while offline · Parallel execution
- Team-accessible results (share agent URL)

**Bad for:**
- Interactive debugging · Local-only files
- Security-sensitive code · Quick questions

<!--
On this slide, When to Use Cloud Agents, cover these points in order: F i r s t ,   L o n g - r u n n i n g   t a s k s   ( > 1 0   m i n )   ·   S c h e d u l e d   j o b s . Next, Tasks while offline · Parallel execution. Next, Team-accessible results (share agent URL). Next, Interactive debugging · Local-only files. The remaining bullets are detail you can skip if time is short: Security-sensitive code · Quick questions.
-->

---


## Accessing Cloud Agents UI

| Method | Steps |
|--------|-------|
| **From Cursor Editor** | View → Cloud Agents (or cloud icon in sidebar) |
| **From Web** | https://cursor.com/agents |
| **From Mobile** | cursor.com/agents (responsive web) |

<!--
Walk this table conversationally: Method — Steps. From Cursor Editor — View → Cloud Agents (or cloud icon in sidebar). From Web — https://cursor.com/agents. From Mobile — cursor.com/agents (responsive web). Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Cloud Agent Dashboard

```
Active (2)
  🔄 security-audit-2024    running • 12 min elapsed
  🔄 doc-generator           running • 3 min elapsed

Completed (4)
  ✅ pr-review-42            FINISHED • 2 artifacts
  ✅ test-suite              FINISHED • 1 artifact

Failed (1)
  ❌ deploy-staging          ERROR • Auth token expired
```

<!--
Active (2) 🔄 security-audit-2024    running • 12 min elapsed 🔄 doc-generator           running • 3 min elapsed Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "Active (2)" and explain why it matters.
-->

---


## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Cursor Agent panel** (`Ctrl+L`) is for natural-language prompts — not a shell.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Pause the slide deck for environment setup. Everyone should open PowerShell or Git Bash in Cursor's integrated terminal.

For API exercises: set keys with `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY` — never commit keys to git. On Windows, use `curl.exe` rather than the PowerShell curl alias when the lab shows curl commands.

Walk the room for two to three minutes. Common blockers: wrong key type, missing curl, wrong working directory. Do not advance until most pairs show a successful test call or are paired with someone who has.
-->

---


## Exercise 6.1 — Steps 1–2

**Platform:** Windows 10/11 · **PowerShell** ``Ctrl+` `` (Git Bash/WSL for `.sh` scripts)


**Step 1:** Navigate to Cloud Agents
**Terminal:** **PowerShell** — ``Ctrl+` `` in Cursor

```bash
# Cursor Editor: cloud icon or View → Cloud Agents
open https://cursor.com/agents
```

<!--
Hands-on time for Exercise 6.1 — Steps 1–2. This exercise is Launching a Cloud Agent. Goal: Launch a Cloud Agent from the Cursor UI and track its run.. Follow the detailed steps in slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md. 

Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts) Step 1: Navigate to Cloud Agents Terminal: PowerShell — `Ctrl+ `` in Cursor open https://cursor.com/agents

Tell them to paste this prompt into the Agent (or read it aloud while they type): "# Cursor Editor: cloud icon or View → Cloud Agents open https://cursor.com/agents"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 6.1 — Steps 1–2 (Part 2)

**Step 2:** Click **"+ New"** and fill out:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```
Repository: https://github.com/YOUR_ORG/YOUR_REPO
Branch: main
Prompt: Read README and main source files. Summarize:
  - What this project does
  - Key dependencies · How to run locally · Common issues
Model: claude-4.6-sonnet
Auto-create PR: ☐
```

<!--
Hands-on time for Exercise 6.1 — Steps 1–2 (Part 2). This exercise is Launching a Cloud Agent. Goal: Launch a Cloud Agent from the Cursor UI and track its run.. Follow the detailed steps in slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md. 

Step 2: Click "+ New" and fill out: Terminal: PowerShell — unless step notes Git Bash or WSL Repository: https://github.com/YOUR_ORG/YOUR_REPO Branch: main Prompt: Read README and main source files. Summarize: - What this project does - Key dependencies · How to run locally · Common issues Model: claude-4.6-sonnet Auto-create PR: ☐

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Repository: https://github.com/YOUR_ORG/YOUR_REPO Branch: main Prompt: Read README and main source files. Summarize:   - What this project does   - Key dependencies · How to run locally · Common issues Model: claude-4.6-sonnet Auto-create PR: ☐"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 6.1 — Steps 3–4

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**


**Step 3:** Monitor live log in real time:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
[10:45:01] Agent starting...
[10:45:02] Cloning repository...
[10:45:15] Repository cloned
[10:45:16] Reading README.md
[10:45:40] Generating summary...
```

<!--
Hands-on time for Exercise 6.1 — Steps 3–4. This exercise is Launching a Cloud Agent. Goal: Launch a Cloud Agent from the Cursor UI and track its run.. Follow the detailed steps in slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Step 3: Monitor live log in real time: Where: Cursor Agent panel — `Ctrl+L` [10:45:01] Agent starting... [10:45:02] Cloning repository... [10:45:15] Repository cloned [10:45:16] Reading README.md [10:45:40] Generating summary...

Tell them to paste this prompt into the Agent (or read it aloud while they type): "[10:45:01] Agent starting... [10:45:02] Cloning repository... [10:45:15] Repository cloned [10:45:16] Reading README.md [10:45:40] Generating summary..."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 6.1 — Steps 3–4 (Part 2)

**Step 4:** Configure settings (gear icon):
**Where:** **Cursor Agent panel** — ``Ctrl+L``

| Setting | Purpose |
|---------|---------|
| Default Model | Preferred model for new agents |
| Auto-create PR | Create PRs on completion |
| Notification Email | Completion notifications |
| Webhook URL | POST completion events |
| Max Run Time | 5 min – 24 hrs |

<!--
Hands-on time for Exercise 6.1 — Steps 3–4 (Part 2). This exercise is Launching a Cloud Agent. Goal: Launch a Cloud Agent from the Cursor UI and track its run.. Follow the detailed steps in slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md. 

Step 4: Configure settings (gear icon): Where: Cursor Agent panel — `Ctrl+L`

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 6.1 — Steps 5–6

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**


**Step 5:** Launch with PR creation:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Prompt: Add CONTRIBUTING.md with dev setup, tests, PR process, code style
Auto-create PR: ✅ Yes
Branch prefix: docs/contributing
```

<!--
Hands-on time for Exercise 6.1 — Steps 5–6. This exercise is Launching a Cloud Agent. Goal: Launch a Cloud Agent from the Cursor UI and track its run.. Follow the detailed steps in slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Step 5: Launch with PR creation: Where: Cursor Agent panel — `Ctrl+L` Prompt: Add CONTRIBUTING.md with dev setup, tests, PR process, code style Auto-create PR: ✅ Yes Branch prefix: docs/contributing

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Prompt: Add CONTRIBUTING.md with dev setup, tests, PR process, code style Auto-create PR: ✅ Yes Branch prefix: docs/contributing"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 6.1 — Steps 5–6 (Part 2)

**Step 6:** Share agent URL with team:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
https://cursor.com/agents/agt_abc123def456
```

<!--
Hands-on time for Exercise 6.1 — Steps 5–6 (Part 2). This exercise is Launching a Cloud Agent. Goal: Launch a Cloud Agent from the Cursor UI and track its run.. Follow the detailed steps in slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md. 

Step 6: Share agent URL with team: Where: Cursor Agent panel — `Ctrl+L` https://cursor.com/agents/agt_abc123def456

Tell them to paste this prompt into the Agent (or read it aloud while they type): "https://cursor.com/agents/agt_abc123def456"

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 6.2

## Cloud Agent Artifacts

*Concept · 8 min · Exercise · 15 min*

<!--
We now begin Lesson 6.2: Cloud Agent Artifacts. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Collect and download artifacts produced by Cloud Agents. Open the lab guide at slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Types of Artifacts

| Artifact Type | Examples |
|---------------|----------|
| **Log files** | `agent.log`, `debug.log` |
| **Code files** | `*.py`, `*.js`, `*.html` |
| **Documents** | `*.md`, `*.txt`, `*.json` |
| **Images** | `*.png`, `*.jpg`, `*.svg` |
| **Archives** | `*.zip`, `*.tar.gz` |
| **Test results** | `junit.xml`, `coverage.json` |

> *"Files produced by the agent that you can download or view in the UI."*

<!--
Walk this table conversationally: Artifact Type — Examples. Log files — agent.log, debug.log. Code files — .py, .js, *.html. Documents — .md, .txt, *.json. Images — .png, .jpg, *.svg. Archives — .zip, .tar.gz. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Artifact Storage

- Stored for **30 days**
- Multiple artifacts per agent
- Download URLs expire after **15 minutes**
- Max **100MB** per file · **1GB** total per agent

<!--
On this slide, Artifact Storage, cover these points in order: F i r s t ,   S t o r e d   f o r   3 0   d a y s . Next, Multiple artifacts per agent. Next, Download URLs expire after 15 minutes. Next, Max 100MB per file · 1GB total per agent.
-->

---


## Exercise 6.2 — Steps 1–2

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**


**Step 1:** Launch agent that generates artifacts:
**Where:** **Cursor Agent panel** — ``Ctrl+L``

```
Generate:
1. api_documentation.md — OpenAPI-style docs for all endpoints
2. test_report.json — test suite summary
3. screenshot.png — main UI screenshot (if applicable)
4. dependencies.txt — all packages and versions

Place all in artifacts/ directory.
```

<!--
Hands-on time for Exercise 6.2 — Steps 1–2. This exercise is Cloud Agent Artifacts. Goal: Collect and download artifacts produced by Cloud Agents.. Follow the detailed steps in slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Step 1: Launch agent that generates artifacts: Where: Cursor Agent panel — `Ctrl+L` Generate: 1. api_documentation.md — OpenAPI-style docs for all endpoints 2. test_report.json — test suite summary 3. screenshot.png — main UI screenshot (if applicable) 4. dependencies.txt — all packages and versions Place all in artifacts/ directory.

Tell them to paste this prompt into the Agent (or read it aloud while they type): "Generate: 1. api_documentation.md — OpenAPI-style docs for all endpoints 2. test_report.json — test suite summary 3. screenshot.png — main UI screenshot (if applicable) 4. dependencies.txt — all packages and versions  Place all in artifacts/ directory."

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 6.2 — Steps 1–2 (Part 2)

**Step 2:** After completion, view artifact list in UI with Download buttons and **Download All (zip)**
**Where:** **Cursor Agent panel** — ``Ctrl+L``

<!--
Hands-on time for Exercise 6.2 — Steps 1–2 (Part 2). This exercise is Cloud Agent Artifacts. Goal: Collect and download artifacts produced by Cloud Agents.. Follow the detailed steps in slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md. 

Step 2: After completion, view artifact list in UI with Download buttons and Download All (zip) Where: Cursor Agent panel — `Ctrl+L`

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 6.2 — Steps 3–5

**Platform:** Windows 10/11 · Agent → ``Ctrl+L`` · Shell → **PowerShell** · Browser for dashboards


**Step 3:** Download individual artifacts
**Where:** **Cursor Agent panel** — ``Ctrl+L``

**Step 4:** Download all as zip
**Where:** **Cursor Agent panel** — ``Ctrl+L``

<!--
Hands-on time for Exercise 6.2 — Steps 3–5. This exercise is Cloud Agent Artifacts. Goal: Collect and download artifacts produced by Cloud Agents.. Follow the detailed steps in slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md. 

Platform: Windows 10/11 · Agent → `Ctrl+L` · Shell → PowerShell · Browser for dashboards Step 3: Download individual artifacts Where: Cursor Agent panel — `Ctrl+L` Step 4: Download all as zip Where: Cursor Agent panel — `Ctrl+L`

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 6.2 — Steps 3–5 (Part 2)

**Step 5:** Preview in browser:
**Where:** **Web browser** — Edge or Chrome
- Markdown → rendered HTML
- Images → inline preview
- JSON → formatted tree view

<!--
Hands-on time for Exercise 6.2 — Steps 3–5 (Part 2). This exercise is Cloud Agent Artifacts. Goal: Collect and download artifacts produced by Cloud Agents.. Follow the detailed steps in slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md. 

Step 5: Preview in browser: Where: Web browser — Edge or Chrome - Markdown → rendered HTML - Images → inline preview - JSON → formatted tree view

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 6.2 — API Access

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
# List artifacts
curl -s -u "$CURSOR_USER_API_KEY:" \
  "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts" | jq '.'

# Download specific artifact
DOWNLOAD_URL=$(curl -s -u "$CURSOR_USER_API_KEY:" \
  ".../artifacts/download?path=artifacts/report.md" | jq -r '.url')
curl -L -o report.md "$DOWNLOAD_URL"
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

Create `bin/process-artifacts.sh` to batch-download all artifacts for an agent ID.

<!--
Hands-on time for Exercise 6.2 — API Access. This exercise is Cloud Agent Artifacts. Goal: Collect and download artifacts produced by Cloud Agents.. Follow the detailed steps in slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe curl -s -u "$CURSOR_USER_API_KEY:" \ "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts" | jq '.' DOWNLOAD_URL=$(curl -s -u "$CURSOR_USER_API_KEY:" \ ".../artifacts/download?path=artifacts/report.md" | jq -r '.url') curl -L -o report.md "$DOWNLOAD_URL" PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl. Create bin/process-artifacts.sh to batch-download all artifacts for an agent ID.

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 6.2 — CI/CD Integration

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```yaml
# GitHub Actions — download test results from completed agent
- name: Download Cloud Agent artifacts
  run: |
    curl -s -u "${{ secrets.CURSOR_API_KEY }}:" \
      ".../artifacts/download?path=test_results.xml" > test_results.xml
```

**Success Criteria:** Generated artifacts · downloaded single + zip · accessed via API

<!--
Hands-on time for Exercise 6.2 — CI/CD Integration. This exercise is Cloud Agent Artifacts. Goal: Collect and download artifacts produced by Cloud Agents.. Follow the detailed steps in slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe - name: Download Cloud Agent artifacts run: | curl -s -u "${{ secrets.CURSOR_API_KEY }}:" \ ".../artifacts/download?path=test_results.xml" > test_results.xml Success Criteria: Generated artifacts · downloaded single + zip · accessed via API

Give work time now. Circulate quietly. Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 6.3

## Cloud Agents from Messaging Platforms

*Concept · 10 min · Demonstration*

<!--
We now begin Lesson 6.3: Cloud Agents from Messaging Platforms. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Supported Integrations

| Platform | Capabilities | Setup |
|----------|--------------|-------|
| **Slack** | Command triggering, notifications | Medium (Slack app) |
| **Discord** | Command triggering, webhook responses | Medium (Bot token) |
| **Teams** | Webhook integration | Medium (Webhook) |
| **Generic Webhook** | POST-triggered agents | Low (any platform) |

<!--
Walk this table conversationally: Platform — Capabilities, Setup. Slack — Command triggering, notifications, Medium (Slack app). Discord — Command triggering, webhook responses, Medium (Bot token). Teams — Webhook integration, Medium (Webhook). Generic Webhook — POST-triggered agents, Low (any platform). Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Messaging Integration Architecture

<img src="assets/module-06/messaging-integration-architecture.svg" alt="Messaging Integration Architecture" />

<!--
This slide is visual: Messaging Integration Architecture. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Demo: Slack Integration

**Step 1:** Create Slack App at api.slack.com

**Step 2:** Configure slash command:

```
Command: /cursor
Request URL: https://your-server.com/webhook/slack-cursor
Usage Hint: [prompt or command]
```

**Step 3:** Deploy webhook receiver (Flask/Python) that:
- Parses Slack command → launches Cloud Agent via API
- Acknowledges immediately with agent URL
- Posts completion summary when webhook fires

<!--
This slide supports a live demonstration: Slack Integration. Narrate every click and keystroke — assume no one has seen this screen before.

If the network fails, describe what would happen and show a screenshot or backup recording. Save questions until the demo completes unless someone is completely lost.

Close the demo by stating when they would use this in production and when they would not.
-->

---


## Demo: Slack Usage

In Slack:

```
/cursor Review the recent commits and summarize what changed
```

**Response:**

```
🤖 Launching Cloud Agent `agt_abc123`
Watch progress: https://cursor.com/agents/agt_abc123

✅ Cloud Agent Complete!
Summary: 3 commits — fixed login bug, added tests, updated README.
PR: https://github.com/your-org/your-repo/pull/43
```

<!--
This slide supports a live demonstration: Slack Usage. Narrate every click and keystroke — assume no one has seen this screen before.

If the network fails, describe what would happen and show a screenshot or backup recording. Save questions until the demo completes unless someone is completely lost.

Close the demo by stating when they would use this in production and when they would not.
-->

---


## Demo: Discord Integration

```python
@bot.command(name='cursor')
async def cursor_command(ctx, *, prompt):
    response = requests.post("https://api.cursor.com/v1/agents", ...)
    await ctx.send(f"✅ Agent launched: https://cursor.com/agents/{agent_id}")
```

Usage: `!cursor Add error handling to all API endpoints`

<!--
This slide supports a live demonstration: Discord Integration. Narrate every click and keystroke — assume no one has seen this screen before.

If the network fails, describe what would happen and show a screenshot or backup recording. Save questions until the demo completes unless someone is completely lost.

Close the demo by stating when they would use this in production and when they would not.
-->

---


## Generic Webhook & Notifications

**Any HTTP POST can trigger agents:**

```bash
curl -X POST https://your-server.com/trigger-agent \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Run the weekly security scan", "repo": "..."}'
```

**Use cases:** GitHub webhook on PR · Cron jobs · CI/CD post-deploy · Internal dashboard

**Status notifications:** configure `notifyOnStart`, `notifyOnComplete`, `notifyOnError`

**Success Criteria:** Understood architecture · saw Slack/Discord demos · webhook triggering

<!--
Any HTTP POST can trigger agents: curl -X POST https://your-server.com/trigger-agent \ -H "Content-Type: application/json" \ Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "curl -X POST https://your-server.com/trigger-agent \" and explain why it matters.

Remind the room: use environment variables for keys, redact secrets in screen shares, and never commit `.env` files with live credentials.
-->

---


## Module Summary

| Lesson | Topic | Key Skill |
|--------|-------|-----------|
| 6.1 | Launching Cloud Agents | Remote execution |
| 6.2 | Cloud Agent Artifacts | Output collection |
| 6.3 | Messaging Integrations | Chat-triggered agents |

<!--
Module 6 summary. In sixty seconds, walk the lesson table and restate one key insight per row.

Ask the closing question: what will you do differently on Monday? Take two or three answers.

Announce the break or introduce the next module with one connecting sentence.
-->

---


## Quick Reference Card

<img src="assets/module-06/quick-reference-card.svg" alt="Quick Reference Card" />

<!--
This quick reference slide is meant for post-course use. Tell participants to screenshot it or copy the commands into their team wiki.

Offer two minutes for questions on this module only, then move on.
-->

---


<!-- _header: 'Module 7 — Cursor API Foundations' -->

<!-- _class: lead -->

# Cursor API Foundations

## Module 7 · Day 2 (Concept + Hands-On)

Cursor Training Program · ~60 min

<!--
We are starting Module 7: Cursor API Foundations. Cursor Training Program · ~60 min State the module goal in plain language: what participants will be able to do when we finish — not just what topics we will mention.

Preview whether this module is lecture, hands-on, or mixed. If it is hands-on, tell people when to open their laptops and which folder or repo to use. If it is concept-only, ask them to listen for one idea they can use on Monday morning.
-->

---


## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Concept + hands-on exercise |
| **Prerequisites** | Cursor account, basic API familiarity, Python 3.8+ installed |
| **Module Goal** | Understand the Cursor API ecosystem, authenticate securely, handle errors, and optimize requests |

<!--
This module overview slide sets expectations. In your own words, cover: Duration is ~60 minutes. Format is Concept + hands-on exercise. Prerequisites is Cursor account, basic API familiarity, Python 3.8+ installed. Module Goal is Understand the Cursor API ecosystem, authenticate securely, handle errors, and optimize requests.  Call out prerequisites explicitly and pause until anyone blocked by missing tools has help. Do not read the table word-for-word — translate it into what the room will experience in the next hour.
-->

---


## Learning Objectives

By the end of this module, participants will be able to:

- Identify the five Cursor APIs and their use cases
- Generate and securely manage API keys
- Implement rate limit handling and error recovery
- Use ETag caching for efficient repeat queries
- Test authentication by listing available models

<!--
These learning objectives describe outcomes, not topics. Paraphrase them: Identify the five Cursor APIs and their use cases. Generate and securely manage API keys. Implement rate limit handling and error recovery. Use ETag caching for efficient repeat queries. Test authentication by listing available models.

Ask the room: which of these would help your team most this quarter? Note one or two answers — you can refer back at the module summary.

Tell participants they are not expected to memorize this list; they should recognize each outcome when they have done it during an exercise or demo.
-->

---


## Agenda

| Lesson | Topic | Time |
|--------|-------|------|
| 7.1 | The Cursor API Landscape | 10 min |
| 7.2 | Authentication | 20 min |
| 7.3 | Rate Limits and Error Handling | 20 min |
| 7.4 | ETag Caching | 18 min |
| 7.5 | Listing Available Models | 10 min |

<!--
Use this agenda as your pacing map for the module. You will cover: Lesson 7.1, The Cursor API Landscape, about 10 min; Lesson 7.2, Authentication, about 20 min; Lesson 7.3, Rate Limits and Error Handling, about 20 min; Lesson 7.4, ETag Caching, about 18 min; Lesson 7.5, Listing Available Models, about 10 min. Announce when the next hands-on block starts so people can close email and open Cursor. If you fall behind, shorten concept repetition before cutting exercise time.
-->

---


<!-- _class: lead -->

# Lesson 7.1

## The Cursor API Landscape

*Concept · 10 min*

<!--
We now begin Lesson 7.1: The Cursor API Landscape. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## The Five APIs

| API | Endpoint | Purpose |
|-----|----------|---------|
| **Chat Completions** | `/v1/chat/completions` | OpenAI-compatible chat interface |
| **Agents** | `/v1/agents` | Create and manage Cloud Agents |
| **Files** | `/v1/files` | Upload/download files for agents |
| **Admin** | `/v1/admin/*` | Team management, analytics, policies |
| **Webhooks** | `/v1/webhooks` | Register and manage webhook endpoints |

<!--
Walk this table conversationally: API — Endpoint, Purpose. Chat Completions — /v1/chat/completions, OpenAI-compatible chat interface. Agents — /v1/agents, Create and manage Cloud Agents. Files — /v1/files, Upload/download files for agents. Admin — /v1/admin/*, Team management, analytics, policies. Webhooks — /v1/webhooks, Register and manage webhook endpoints. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## API Comparison Matrix

| API | Auth Type | Rate Limit | Cost | Primary Use |
|-----|-----------|------------|------|-------------|
| **Chat Completions** | User or API key | Per-minute token | Pay-per-token | Direct model access |
| **Agents** | User API key | Per-minute requests | Per-run | Long-running tasks |
| **Files** | User API key | Per-minute | Storage | Context upload |
| **Admin** | Admin API key | Higher limits | Included in plan | Team management |
| **Webhooks** | User API key | Per-minute | Free | Notifications |

<!--
Walk this table conversationally: API — Auth Type, Rate Limit. Chat Completions — User or API key, Per-minute token. Agents — User API key, Per-minute requests. Files — User API key, Per-minute. Admin — Admin API key, Higher limits. Webhooks — User API key, Per-minute. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## When to Use Which API

- **Call a model directly** → Chat Completions API (OpenAI-compatible)
- **Run a long task that writes code** → Agents API
- **Manage team usage and limits** → Admin API
- **Be notified when agents complete** → Webhooks API

<!--
On this slide, When to Use Which API, cover these points in order: F i r s t ,   C a l l   a   m o d e l   d i r e c t l y   →   C h a t   C o m p l e t i o n s   A P I   ( O p e n A I - c o m p a t i b l e ) . Next, Run a long task that writes code → Agents API. Next, Manage team usage and limits → Admin API. Next, Be notified when agents complete → Webhooks API.
-->

---


## OpenAI Compatibility

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.cursor.com/v1",
    api_key="your-cursor-api-key"
)

response = client.chat.completions.create(
    model="claude-4.6-sonnet",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**Success Criteria:** Understand five APIs · select correct API · understand OpenAI compatibility

<!--
from openai import OpenAI client = OpenAI( base_url="https://api.cursor.com/v1", Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "from openai import OpenAI" and explain why it matters.

Remind the room: use environment variables for keys, redact secrets in screen shares, and never commit `.env` files with live credentials.
-->

---


<!-- _class: lead -->

# Lesson 7.2

## Authentication

*Concept · 8 min · Exercise · 12 min*

<!--
We now begin Lesson 7.2: Authentication. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Create Admin and User API keys and verify authentication. Open the lab guide at slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Authentication Methods

| Method | Format | When to Use |
|--------|--------|-------------|
| **HTTP Basic** | `-u "api_key:"` | CLI, curl, most SDKs |
| **Bearer Token** | `Authorization: Bearer <key>` | OAuth-style clients |
| **User API Key** | Regular key | Agents, Chat, Files APIs |
| **Admin API Key** | `admin_` prefixed | Admin API only |

<!--
Walk this table conversationally: Method — Format, When to Use. HTTP Basic — -u "api_key:", CLI, curl, most SDKs. Bearer Token — Authorization: Bearer <key>, OAuth-style clients. User API Key — Regular key, Agents, Chat, Files APIs. Admin API Key — admin_ prefixed, Admin API only. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## API Key Types

**User API Key**
- Generated in: Cursor Settings → API Keys
- Format: `cursor_xxxxxxxxxxxx`
- Can access: Agents, Chat, Files, Webhooks

**Admin API Key**
- Generated in: Organization Settings → API Keys
- Format: `cursor_admin_xxxxxxxxxxxx`
- Can access: Admin API + everything User can

<!--
On this slide, API Key Types, cover these points in order: F i r s t ,   G e n e r a t e d   i n :   C u r s o r   S e t t i n g s   →   A P I   K e y s . Next, Format: cursor_xxxxxxxxxxxx. Next, Can access: Agents, Chat, Files, Webhooks. Next, Generated in: Organization Settings → API Keys. The remaining bullets are detail you can skip if time is short: Format: cursor_admin_xxxxxxxxxxxx, Can access: Admin API + everything User can.
-->

---


## Security Best Practices

- Never commit API keys to git
- Use environment variables or secret managers
- Rotate keys periodically (every 90 days)
- Use different keys for dev and production
- Revoke unused keys immediately
- Use Admin API keys only when necessary
- Monitor key usage in dashboard

<!--
On this slide, Security Best Practices, cover these points in order: F i r s t ,   N e v e r   c o m m i t   A P I   k e y s   t o   g i t . Next, Use environment variables or secret managers. Next, Rotate keys periodically (every 90 days). Next, Use different keys for dev and production. The remaining bullets are detail you can skip if time is short: Revoke unused keys immediately, Use Admin API keys only when necessary, Monitor key usage in dashboard.
-->

---


## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Cursor Agent panel** (`Ctrl+L`) is for natural-language prompts — not a shell.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Pause the slide deck for environment setup. Everyone should open PowerShell or Git Bash in Cursor's integrated terminal.

For API exercises: set keys with `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY` — never commit keys to git. On Windows, use `curl.exe` rather than the PowerShell curl alias when the lab shows curl commands.

Walk the room for two to three minutes. Common blockers: wrong key type, missing curl, wrong working directory. Do not advance until most pairs show a successful test call or are paired with someone who has.
-->

---


## Exercise 7.2 — Steps 1–3

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`


**Step 1:** Generate User API Key — **Where:** **Cursor app** → **Settings** → **API Keys** → **Generate New Key** (copy the key; you will not see it again)

<!--
Hands-on time for Exercise 7.2 — Steps 1–3. This exercise is Generate and Test API Keys. Goal: Create Admin and User API keys and verify authentication.. Follow the detailed steps in slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe Step 1: Generate User API Key — Where: Cursor app → Settings → API Keys → Generate New Key (copy the key; you will not see it again)

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 7.2 — Steps 1–3 (Part 2)

**Step 2:** Set environment variable — **Terminal:** **PowerShell** (``Ctrl+` ``)

```powershell
$env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx"
$env:CURSOR_USER_API_KEY
```

<!--
Hands-on time for Exercise 7.2 — Steps 1–3 (Part 2). This exercise is Generate and Test API Keys. Goal: Create Admin and User API keys and verify authentication.. Follow the detailed steps in slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md. 

Step 2: Set environment variable — Terminal: PowerShell (`Ctrl+ ``) $env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx" $env:CURSOR_USER_API_KEY

Tell them to paste this prompt into the Agent (or read it aloud while they type): "$env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx" $env:CURSOR_USER_API_KEY"

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 7.2 — Steps 1–3 (Part 3)

**Step 3:** Test with curl — **Terminal:** **PowerShell**

```powershell
curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" `
  https://api.cursor.com/v1/models | Select-Object -First 20
```

<!--
Hands-on time for Exercise 7.2 — Steps 1–3 (Part 3). This exercise is Generate and Test API Keys. Goal: Create Admin and User API keys and verify authentication.. Follow the detailed steps in slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md. 

Step 3: Test with curl — Terminal: PowerShell curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" ` https://api.cursor.com/v1/models | Select-Object -First 20

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 7.2 — Steps 4–5

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`


**Step 4:** Test with Python requests:
**Terminal:** **PowerShell** — save as `test_models.py`, then `python test_models.py` — ``Ctrl+L``

```python
response = requests.get(
    "https://api.cursor.com/v1/models",
    auth=(API_KEY, "")  # Empty password
)
```

<!--
Hands-on time for Exercise 7.2 — Steps 4–5. This exercise is Generate and Test API Keys. Goal: Create Admin and User API keys and verify authentication.. Follow the detailed steps in slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe Step 4: Test with Python requests: Terminal: PowerShell — save as test_models.py, then python test_models.py — `Ctrl+L` response = requests.get( "https://api.cursor.com/v1/models", auth=(API_KEY, "")  # Empty password )

Tell them to paste this prompt into the Agent (or read it aloud while they type): "response = requests.get(     "https://api.cursor.com/v1/models",     auth=(API_KEY, "")  # Empty password )"

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 7.2 — Steps 4–5 (Part 2)

**Step 5:** Test with OpenAI SDK:
**Terminal:** **PowerShell** — `python test_openai_sdk.py` — ``Ctrl+L``

```python
client = OpenAI(base_url="https://api.cursor.com/v1", api_key=API_KEY)
response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[{"role": "user", "content": "Say 'API works!'"}],
    max_tokens=10
)
```

<!--
Hands-on time for Exercise 7.2 — Steps 4–5 (Part 2). This exercise is Generate and Test API Keys. Goal: Create Admin and User API keys and verify authentication.. Follow the detailed steps in slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md. 

Step 5: Test with OpenAI SDK: Terminal: PowerShell — python test_openai_sdk.py — `Ctrl+L` client = OpenAI(base_url="https://api.cursor.com/v1", api_key=API_KEY) response = client.chat.completions.create( model="gpt-5-mini", messages=[{"role": "user", "content": "Say 'API works!'"}], max_tokens=10 )

Tell them to paste this prompt into the Agent (or read it aloud while they type): "client = OpenAI(base_url="https://api.cursor.com/v1", api_key=API_KEY) response = client.chat.completions.create(     model="gpt-5-mini",     messages=[{"role": "user", "content": "Say 'API works!'"}],     max_tokens=10 )"

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 7.2 — Steps 6–7

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`


**Step 6:** Generate and test Admin API Key:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
export CURSOR_ADMIN_API_KEY="cursor_admin_xxxxxxxxxxxx"
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  https://api.cursor.com/v1/admin/organization | jq '.'
```

<!--
Hands-on time for Exercise 7.2 — Steps 6–7. This exercise is Generate and Test API Keys. Goal: Create Admin and User API keys and verify authentication.. Follow the detailed steps in slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe Step 6: Generate and test Admin API Key: Terminal: PowerShell — unless step notes Git Bash or WSL export CURSOR_ADMIN_API_KEY="cursor_admin_xxxxxxxxxxxx" curl -s -u "$CURSOR_ADMIN_API_KEY:" \ https://api.cursor.com/v1/admin/organization | jq '.'

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 7.2 — Steps 6–7 (Part 2)

**Step 7:** Revoke compromised keys via API or Settings → API Keys → Revoke
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

**Success Criteria:** Generated keys · tested curl, Python, OpenAI SDK · tested Admin key

<!--
Hands-on time for Exercise 7.2 — Steps 6–7 (Part 2). This exercise is Generate and Test API Keys. Goal: Create Admin and User API keys and verify authentication.. Follow the detailed steps in slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md. 

Step 7: Revoke compromised keys via API or Settings → API Keys → Revoke Terminal: PowerShell — unless step notes Git Bash or WSL Success Criteria: Generated keys · tested curl, Python, OpenAI SDK · tested Admin key

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 7.3

## Rate Limits and Error Handling

*Concept · 10 min · Exercise · 10 min*

<!--
We now begin Lesson 7.3: Rate Limits and Error Handling. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Handle 429 responses with backoff and rate-limit headers. Open the lab guide at slide-exercises/module-07/exercise-7.3-rate-limits-and-error-handling.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Rate Limits by API

| API | Limit | Window |
|-----|-------|--------|
| Chat Completions | 1000 requests | per minute |
| Chat Completions (tokens) | 500k tokens | per minute |
| Agents (create) | 100 requests | per minute |
| Admin API | 500 requests | per minute |
| Webhooks | 2000 requests | per minute |

<!--
Walk this table conversationally: API — Limit, Window. Chat Completions — 1000 requests, per minute. Chat Completions (tokens) — 500k tokens, per minute. Agents (create) — 100 requests, per minute. Admin API — 500 requests, per minute. Webhooks — 2000 requests, per minute. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## HTTP Status Codes to Handle

| Code | Meaning | Action |
|------|---------|--------|
| **200** | Success | Process response |
| **400** | Bad Request | Fix request parameters |
| **401** | Unauthorized | Check API key |
| **403** | Forbidden | Check permissions |
| **429** | Too Many Requests | Implement backoff |
| **500/503** | Server Error | Retry with backoff |

<!--
Walk this table conversationally: Code — Meaning, Action. 200 — Success, Process response. 400 — Bad Request, Fix request parameters. 401 — Unauthorized, Check API key. 403 — Forbidden, Check permissions. 429 — Too Many Requests, Implement backoff. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Rate Limit Headers

| Header | Description | Example |
|--------|-------------|---------|
| `X-RateLimit-Limit` | Max requests per window | `1000` |
| `X-RateLimit-Remaining` | Requests left | `942` |
| `X-RateLimit-Reset` | Window reset (Unix timestamp) | `1700000000` |
| `Retry-After` | Seconds to wait (on 429) | `60` |

<!--
Walk this table conversationally: Header — Description, Example. X-RateLimit-Limit — Max requests per window, 1000. X-RateLimit-Remaining — Requests left, 942. X-RateLimit-Reset — Window reset (Unix timestamp), 1700000000. Retry-After — Seconds to wait (on 429), 60. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Exercise 7.3 — Exponential Backoff

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```python
def call_with_retry(url, max_retries=5, base_delay=1.0):
    for attempt in range(max_retries):
        response = requests.get(url, auth=AUTH)
        if response.status_code == 200:
            return response.json()
        if 400 <= response.status_code < 500:
            return None  # Don't retry client errors
        if response.status_code in [429, 500, 502, 503, 504]:
            delay = int(response.headers.get('Retry-After',
                      min(base_delay * (2 ** attempt), 60)))
            time.sleep(delay)
    return None
```

<!--
Hands-on time for Exercise 7.3 — Exponential Backoff. This exercise is Rate Limits and Error Handling. Goal: Handle 429 responses with backoff and rate-limit headers.. Follow the detailed steps in slide-exercises/module-07/exercise-7.3-rate-limits-and-error-handling.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe def call_with_retry(url, max_retries=5, base_delay=1.0): for attempt in range(max_retries): response = requests.get(url, auth=AUTH) if response.status_code == 200: return response.json() if 400 <= response.status_code < 500: return None  # Don't retry client errors if response.status_code in [429, 500, 502, 503, 504]: delay = int(response.headers.get('Retry-After', min(base_delay  (2 * attempt), 60))) time.sleep(delay) return None

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 7.3 — Rate Limiter & Client

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**Monitor headers:** warn when `X-RateLimit-Remaining` < 10% of limit

**Token bucket rate limiter:** space requests evenly across the minute window

**CursorAPIClient:** combines rate limiting, retries on 429/5xx, timeout handling, and typed methods like `get_models()` and `create_agent()`

**Success Criteria:** Backoff · header monitoring · rate limiter · robust client class

<!--
Hands-on time for Exercise 7.3 — Rate Limiter & Client. This exercise is Rate Limits and Error Handling. Goal: Handle 429 responses with backoff and rate-limit headers.. Follow the detailed steps in slide-exercises/module-07/exercise-7.3-rate-limits-and-error-handling.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Monitor headers: warn when X-RateLimit-Remaining < 10% of limit Token bucket rate limiter: space requests evenly across the minute window CursorAPIClient: combines rate limiting, retries on 429/5xx, timeout handling, and typed methods like get_models() and create_agent() Success Criteria: Backoff · header monitoring · rate limiter · robust client class

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 7.4

## ETag Caching

*Concept · 8 min · Exercise · 10 min*

<!--
We now begin Lesson 7.4: ETag Caching. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Use ETags to avoid re-downloading unchanged API data. Open the lab guide at slide-exercises/module-07/exercise-7.4-etag-caching.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What Are ETags?

ETags are unique identifiers for API response versions.

1. Send `If-None-Match` header with previous ETag
2. Server returns `304 Not Modified` if unchanged
3. No data transfer, no rate limit consumption

<!--
For slide 316, What Are ETags?: ETags are unique identifiers for API response versions. 1. Send If-None-Match header with previous ETag 2. Server returns 304 Not Modified if unchanged 3. No data transfer, no rate limit consumption

Check for questions before you advance. If the room is silent, ask a specific question tied to the slide content.
-->

---


## ETag Flow

<img src="assets/module-07/etag-flow.svg" alt="ETag Flow" />

<!--
This slide is visual: ETag Flow. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Endpoints Supporting ETags

| Endpoint | ETag Support | Cache Freshness |
|----------|--------------|-----------------|
| `/v1/models` | ✅ Yes | Changes rarely |
| `/v1/admin/members` | ✅ Yes | Changes occasionally |
| `/v1/agents/{id}` | ✅ Yes | Changes during run |
| `/v1/analytics/usage` | ✅ Yes | Daily changes |
| `/v1/agents` (list) | ⚠️ Partial | Changes frequently |

<!--
Walk this table conversationally: Endpoint — ETag Support, Cache Freshness. /v1/models — ✅ Yes, Changes rarely. /v1/admin/members — ✅ Yes, Changes occasionally. /v1/agents/{id} — ✅ Yes, Changes during run. /v1/analytics/usage — ✅ Yes, Daily changes. /v1/agents (list) — ⚠️ Partial, Changes frequently. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Exercise 7.4 — Basic ETag Usage

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```python
def get_with_etag(url, previous_etag=None):
    headers = {'If-None-Match': previous_etag} if previous_etag else {}
    response = requests.get(url, auth=AUTH, headers=headers)

    if response.status_code == 304:
        return None, response.headers.get('ETag')  # Use cached data
    if response.status_code == 200:
        return response.json(), response.headers.get('ETag')
```

<!--
Hands-on time for Exercise 7.4 — Basic ETag Usage. This exercise is ETag Caching. Goal: Use ETags to avoid re-downloading unchanged API data.. Follow the detailed steps in slide-exercises/module-07/exercise-7.4-etag-caching.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe def get_with_etag(url, previous_etag=None): headers = {'If-None-Match': previous_etag} if previous_etag else {} response = requests.get(url, auth=AUTH, headers=headers) if response.status_code == 304: return None, response.headers.get('ETag')  # Use cached data if response.status_code == 200: return response.json(), response.headers.get('ETag')

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 7.4 — ETagCache & CachedClient

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**ETagCache:** persistent pickle-based cache keyed by URL hash

**CachedCursorClient:**
- Check local cache → send `If-None-Match`
- On 304 → return cached data (Cache HIT)
- On 200 → update cache (Cache MISS)

**Batch analytics:** fetch 30 days of usage — unchanged days return 304 instantly

**Success Criteria:** Basic ETag request · persistent cache · analytics workload caching

<!--
Hands-on time for Exercise 7.4 — ETagCache & CachedClient. This exercise is ETag Caching. Goal: Use ETags to avoid re-downloading unchanged API data.. Follow the detailed steps in slide-exercises/module-07/exercise-7.4-etag-caching.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor ETagCache: persistent pickle-based cache keyed by URL hash CachedCursorClient: - Check local cache → send If-None-Match - On 304 → return cached data (Cache HIT) - On 200 → update cache (Cache MISS) Batch analytics: fetch 30 days of usage — unchanged days return 304 instantly Success Criteria: Basic ETag request · persistent cache · analytics workload caching

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 7.5

## Listing Available Models

*Concept · 4 min · Exercise · 6 min*

<!--
We now begin Lesson 7.5: Listing Available Models. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Query available models and pick the right one programmatically. Open the lab guide at slide-exercises/module-07/exercise-7.5-list-available-models.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## The Models Endpoint

```bash
GET /v1/models
```

**Response includes:**
- Model ID · Display name · Context window size
- Pricing (input/output per 1M tokens)
- Capabilities (vision, tool calling, etc.)

> *"Simplest API call — perfect for verifying your API key works."*

<!--
Read or closely paraphrase the quote on screen: "Simplest API call — perfect for verifying your API key works."

GET /v1/models Response includes: - Model ID · Display name · Context window size - Pricing (input/output per 1M tokens) - Capabilities (vision, tool calling, etc.)

Pause two beats after the quote so it lands. Then ask whether anyone has seen the opposite problem in real projects.
-->

---


## Exercise 7.5 — Steps 1–2

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`


**Step 1:** List with curl:
**Terminal:** **PowerShell** — ``Ctrl+` `` in Cursor

```bash
curl -s -u "$CURSOR_USER_API_KEY:" \
  https://api.cursor.com/v1/models \
  | jq '.data[] | {id: .id, context: .context_window, input_price: .pricing.input}'
```

<!--
Hands-on time for Exercise 7.5 — Steps 1–2. This exercise is List Available Models. Goal: Query available models and pick the right one programmatically.. Follow the detailed steps in slide-exercises/module-07/exercise-7.5-list-available-models.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe Step 1: List with curl: Terminal: PowerShell — `Ctrl+ `` in Cursor curl -s -u "$CURSOR_USER_API_KEY:" \ https://api.cursor.com/v1/models \

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 7.5 — Steps 1–2 (Part 2)

**Step 2:** Format with Python tabulate — Model ID, Context, Input/Output Price, Vision support
**Terminal:** **PowerShell** — `python script.py`

<!--
Hands-on time for Exercise 7.5 — Steps 1–2 (Part 2). This exercise is List Available Models. Goal: Query available models and pick the right one programmatically.. Follow the detailed steps in slide-exercises/module-07/exercise-7.5-list-available-models.md. 

Step 2: Format with Python tabulate — Model ID, Context, Input/Output Price, Vision support Terminal: PowerShell — python script.py

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 7.5 — Steps 3–4

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`


**Step 3:** Filter models:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```python
# Models with 100k+ context
large_context = [m for m in models if m.get('context_window', 0) >= 100000]

# Cheapest by input price
cheapest = sorted(models, key=lambda x: x['pricing']['input'])[:5]
```

<!--
Hands-on time for Exercise 7.5 — Steps 3–4. This exercise is List Available Models. Goal: Query available models and pick the right one programmatically.. Follow the detailed steps in slide-exercises/module-07/exercise-7.5-list-available-models.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe Step 3: Filter models: Terminal: PowerShell — unless step notes Git Bash or WSL large_context = [m for m in models if m.get('context_window', 0) >= 100000] cheapest = sorted(models, key=lambda x: x['pricing']['input'])[:5]

Tell them to paste this prompt into the Agent (or read it aloud while they type): "# Models with 100k+ context large_context = [m for m in models if m.get('context_window', 0) >= 100000]  # Cheapest by input price cheapest = sorted(models, key=lambda x: x['pricing']['input'])[:5]"

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 7.5 — Steps 3–4 (Part 2)

**Step 4:** Model selection helper:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```python
select_model("code_review", "balanced")  # → claude-4.6-sonnet
select_model("simple_fix", "low")        # → gpt-5-mini
select_model("frontend_ui", "high")      # → gemini-3.1-pro
```

<!--
Hands-on time for Exercise 7.5 — Steps 3–4 (Part 2). This exercise is List Available Models. Goal: Query available models and pick the right one programmatically.. Follow the detailed steps in slide-exercises/module-07/exercise-7.5-list-available-models.md. 

Step 4: Model selection helper: Terminal: PowerShell — unless step notes Git Bash or WSL select_model("code_review", "balanced")  # → claude-4.6-sonnet select_model("simple_fix", "low")        # → gpt-5-mini select_model("frontend_ui", "high")      # → gemini-3.1-pro

Tell them to paste this prompt into the Agent (or read it aloud while they type): "select_model("code_review", "balanced")  # → claude-4.6-sonnet select_model("simple_fix", "low")        # → gpt-5-mini select_model("frontend_ui", "high")      # → gemini-3.1-pro"

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Module Summary

| Lesson | Topic | Key Skill |
|--------|-------|-----------|
| 7.1 | API Landscape | API selection |
| 7.2 | Authentication | Key management |
| 7.3 | Rate Limits & Errors | Robust clients |
| 7.4 | ETag Caching | Efficient queries |
| 7.5 | Listing Models | Auth smoke-test |

<!--
Module 7 summary. In sixty seconds, walk the lesson table and restate one key insight per row.

Ask the closing question: what will you do differently on Monday? Take two or three answers.

Announce the break or introduce the next module with one connecting sentence.
-->

---


## Quick Reference Card

<img src="assets/module-07/quick-reference-card.svg" alt="Quick Reference Card" />

<!--
This quick reference slide is meant for post-course use. Tell participants to screenshot it or copy the commands into their team wiki.

Offer two minutes for questions on this module only, then move on.
-->

---


<!-- _header: 'Module 8 — Cloud Agents API and Webhooks' -->

<!-- _class: lead -->

# Cloud Agents API and Webhooks

## Module 8 · Day 2 (Hands-On)

Cursor Training Program · ~60 min

<!--
We are starting Module 8: Cloud Agents API and Webhooks. Cursor Training Program · ~60 min State the module goal in plain language: what participants will be able to do when we finish — not just what topics we will mention.

Preview whether this module is lecture, hands-on, or mixed. If it is hands-on, tell people when to open their laptops and which folder or repo to use. If it is concept-only, ask them to listen for one idea they can use on Monday morning.
-->

---


## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise |
| **Prerequisites** | User API key (Module 7), Python 3.8+, ngrok installed, GitHub repository |
| **Module Goal** | Programmatically create, stream, and manage Cloud Agents, and set up webhook notifications |

<!--
This module overview slide sets expectations. In your own words, cover: Duration is ~60 minutes. Format is Hands-on exercise. Prerequisites is User API key (Module 7), Python 3.8+, ngrok installed, GitHub repository. Module Goal is Programmatically create, stream, and manage Cloud Agents, and set up webhook notifications.  Call out prerequisites explicitly and pause until anyone blocked by missing tools has help. Do not read the table word-for-word — translate it into what the room will experience in the next hour.
-->

---


## Learning Objectives

By the end of this module, participants will be able to:

- Create a Cloud Agent programmatically using the API
- Stream agent responses in real-time using SSE with resume support
- List and download artifacts from a completed agent
- Create a webhook endpoint with HMAC verification
- Test webhooks locally using ngrok
- Build an end-to-end automated agent workflow

<!--
These learning objectives describe outcomes, not topics. Paraphrase them: Create a Cloud Agent programmatically using the API. Stream agent responses in real-time using SSE with resume support. List and download artifacts from a completed agent. Create a webhook endpoint with HMAC verification. Test webhooks locally using ngrok. Build an end-to-end automated agent workflow.

Ask the room: which of these would help your team most this quarter? Note one or two answers — you can refer back at the module summary.

Tell participants they are not expected to memorize this list; they should recognize each outcome when they have done it during an exercise or demo.
-->

---


## Agenda

| Lesson | Topic | Time |
|--------|-------|------|
| 8.1 | Creating a Cloud Agent Programmatically | 15 min |
| 8.2 | Streaming Agent Responses (SSE) | 15 min |
| 8.3 | Listing and Downloading Artifacts | 15 min |
| 8.4 | Creating a Webhook Endpoint | 15 min |
| 8.5 | Testing Webhooks Locally with ngrok | 13 min |
| 8.6 | End-to-End Automated Agent Workflow | 17 min |

<!--
Use this agenda as your pacing map for the module. You will cover: Lesson 8.1, Creating a Cloud Agent Programmatically, about 15 min; Lesson 8.2, Streaming Agent Responses (SSE), about 15 min; Lesson 8.3, Listing and Downloading Artifacts, about 15 min; Lesson 8.4, Creating a Webhook Endpoint, about 15 min; Lesson 8.5, Testing Webhooks Locally with ngrok, about 13 min; Lesson 8.6, End-to-End Automated Agent Workflow, about 17 min. Announce when the next hands-on block starts so people can close email and open Cursor. If you fall behind, shorten concept repetition before cutting exercise time.
-->

---


<!-- _class: lead -->

# Lesson 8.1

## Creating a Cloud Agent Programmatically

*Concept · 5 min · Exercise · 10 min*

<!--
We now begin Lesson 8.1: Creating a Cloud Agent Programmatically. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Create a Cloud Agent run using curl or Python. Open the lab guide at slide-exercises/module-08/exercise-8.1-create-a-cloud-agent-via-api.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Agent + Runs

| Concept | Description |
|---------|-------------|
| **Agent** | Durable entity with conversation history and workspace state |
| **Run** | Single execution (one prompt/response cycle) |

**Key endpoint:** `POST /v1/agents`

<!--
Walk this table conversationally: Concept — Description. Agent — Durable entity with conversation history and workspace state. Run — Single execution (one prompt/response cycle). Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Request Fields

**Required:**

| Field | Example |
|-------|---------|
| `prompt.text` | "Add a README.md file" |
| `repos[].url` | "https://github.com/org/repo" |

**Optional:** `autoCreatePR` · `model.id` · `webhookUrl` · `webhookSecret`

<!--
Walk this table conversationally: Field — Example. prompt.text — "Add a README.md file". repos[].url — "https://github.com/org/repo". Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Cursor Agent panel** (`Ctrl+L`) is for natural-language prompts — not a shell.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Pause the slide deck for environment setup. Everyone should open PowerShell or Git Bash in Cursor's integrated terminal.

For API exercises: set keys with `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY` — never commit keys to git. On Windows, use `curl.exe` rather than the PowerShell curl alias when the lab shows curl commands.

Walk the room for two to three minutes. Common blockers: wrong key type, missing curl, wrong working directory. Do not advance until most pairs show a successful test call or are paired with someone who has.
-->

---


## Exercise 8.1 — Create with curl

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

**Step 1 — set API key · Terminal:** **PowerShell**

```powershell
$env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx"
```

**Step 2 — create agent · Terminal:** **PowerShell**

```powershell
curl.exe -X POST https://api.cursor.com/v1/agents `
  -u "$($env:CURSOR_USER_API_KEY):" `
  -H "Content-Type: application/json" `
  -d '{"prompt":{"text":"Add a README.md file with setup instructions"},"repos":[{"url":"https://github.com/YOUR_ORG/YOUR_REPO","startingRef":"main"}],"autoCreatePR":true}' `
  | ConvertFrom-Json
```

**Terminal (alternative):** **Git Bash** / **WSL** — bash block below.

```bash
export CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx"
curl -X POST https://api.cursor.com/v1/agents   -u "$CURSOR_USER_API_KEY:"   -H "Content-Type: application/json"   -d '{"prompt":{"text":"Add a README.md file with setup instructions"},"repos":[{"url":"https://github.com/YOUR_ORG/YOUR_REPO","startingRef":"main"}],"autoCreatePR":true}' | jq '.'
```

<!--
Hands-on time for Exercise 8.1 — Create with curl. This exercise is Create a Cloud Agent via API. Goal: Create a Cloud Agent run using curl or Python.. Follow the detailed steps in slide-exercises/module-08/exercise-8.1-create-a-cloud-agent-via-api.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe Step 1 — set API key · Terminal: PowerShell $env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx" Step 2 — create agent · Terminal: PowerShell curl.exe -X POST https://api.cursor.com/v1/agents ` -u "$($env:CURSOR_USER_API_KEY):" ` -H "Content-Type: application/json" ` -d '{"prompt":{"text":"Add a README.md file with setup instructions"},"repos":[{"url":"https://github.com/YOUR_ORG/YOUR_REPO","startingRef":"main"}],"autoCreatePR":true}' ` Terminal (alternative): Git Bash / WSL — bash block below. export CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx" curl -X POST https://api.cursor.com/v1/agents   -u "$CURSOR_USER_API_KEY:"   -H "Content-Type: application/json"   -d '{"prompt":{"text":"Add a README.md file with setup instructions"},"repos":[{"url":"https://github.com/YOUR_ORG/YOUR_REPO","startingRef":"main"}],"autoCreatePR":true}' | jq '.'

Tell them to paste this prompt into the Agent (or read it aloud while they type): "$env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx""

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 8.1 — Capture IDs

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`


**Step 1:** Save the JSON from the create-agent call — **Terminal:** **PowerShell**

```powershell
$response = curl.exe ... | ConvertFrom-Json   # reuse create-agent command
$env:AGENT_ID = $response.agent.id
$env:RUN_ID = $response.run.id
Write-Host "Agent ID: $($env:AGENT_ID)"
Write-Host "Dashboard: https://cursor.com/agents/$($env:AGENT_ID)"
```

<!--
Hands-on time for Exercise 8.1 — Capture IDs. This exercise is Create a Cloud Agent via API. Goal: Create a Cloud Agent run using curl or Python.. Follow the detailed steps in slide-exercises/module-08/exercise-8.1-create-a-cloud-agent-via-api.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe Step 1: Save the JSON from the create-agent call — Terminal: PowerShell $response = curl.exe ... | ConvertFrom-Json   # reuse create-agent command $env:AGENT_ID = $response.agent.id $env:RUN_ID = $response.run.id Write-Host "Agent ID: $($env:AGENT_ID)" Write-Host "Dashboard: https://cursor.com/agents/$($env:AGENT_ID)"

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 8.1 — Capture IDs (Part 2)

**Step 2:** Optional model override in create payload — **Where:** edit JSON before POST (any terminal)

Create with specific model: `"model": {"id": "claude-4.7-opus"}`

<!--
Hands-on time for Exercise 8.1 — Capture IDs (Part 2). This exercise is Create a Cloud Agent via API. Goal: Create a Cloud Agent run using curl or Python.. Follow the detailed steps in slide-exercises/module-08/exercise-8.1-create-a-cloud-agent-via-api.md. 

Step 2: Optional model override in create payload — Where: edit JSON before POST (any terminal) Create with specific model: "model": {"id": "claude-4.7-opus"}

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 8.1 — Python Helper

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```python
def create_agent(prompt, repo_url, auto_create_pr=False, model=None):
    payload = {
        "prompt": {"text": prompt},
        "repos": [{"url": repo_url}],
        "autoCreatePR": auto_create_pr
    }
    if model:
        payload["model"] = {"id": model}
    response = requests.post(f"{BASE_URL}/agents", auth=AUTH, json=payload)
    data = response.json()
    return data["agent"]["id"], data["run"]["id"]
```

**Success Criteria:** Agent created · IDs captured · appears in dashboard · Python function works

<!--
Hands-on time for Exercise 8.1 — Python Helper. This exercise is Create a Cloud Agent via API. Goal: Create a Cloud Agent run using curl or Python.. Follow the detailed steps in slide-exercises/module-08/exercise-8.1-create-a-cloud-agent-via-api.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe def create_agent(prompt, repo_url, auto_create_pr=False, model=None): payload = { "prompt": {"text": prompt}, "repos": [{"url": repo_url}], "autoCreatePR": auto_create_pr } if model: payload["model"] = {"id": model} response = requests.post(f"{BASE_URL}/agents", auth=AUTH, json=payload) data = response.json() return data["agent"]["id"], data["run"]["id"] Success Criteria: Agent created · IDs captured · appears in dashboard · Python function works

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 8.2

## Streaming Agent Responses (SSE)

*Concept · 5 min · Exercise · 10 min*

<!--
We now begin Lesson 8.2: Streaming Agent Responses (SSE). Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Stream Cloud Agent events with Server-Sent Events. Open the lab guide at slide-exercises/module-08/exercise-8.2-stream-agent-responses-sse.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## SSE Event Types

| Event | When It Happens | Data Example |
|-------|-----------------|--------------|
| `status` | Run status changes | `{"status":"RUNNING"}` |
| `assistant` | Agent speaks | `{"text":"I'll read the file..."}` |
| `thinking` | Agent is reasoning | `{"text":"Let me consider..."}` |
| `tool_call` | Agent uses a tool | `{"name":"read_file","status":"started"}` |
| `result` | Run completes | `{"status":"FINISHED"}` |
| `error` | Something went wrong | `{"message":"..."}` |
| `done` | Stream ends | `{}` |

<!--
Walk this table conversationally: Event — When It Happens, Data Example. status — Run status changes, {"status":"RUNNING"}. assistant — Agent speaks, {"text":"I'll read the file..."}. thinking — Agent is reasoning, {"text":"Let me consider..."}. tool_call — Agent uses a tool, {"name":"read_file","status":"started"}. result — Run completes, {"status":"FINISHED"}. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Resume Support

SSE streams support the **`Last-Event-ID`** header — if your connection drops, resume from the last received event.

<!--
For slide 343, Resume Support: SSE streams support the Last-Event-ID header — if your connection drops, resume from the last received event.

Check for questions before you advance. If the room is silent, ask a specific question tied to the slide content.
-->

---


## Exercise 8.2 — Stream with curl

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

**Terminal:** **PowerShell**

```powershell
curl.exe -N -u "$($env:CURSOR_USER_API_KEY):" `
  -H "Accept: text/event-stream" `
  "https://api.cursor.com/v1/agents/$env:AGENT_ID/runs/$env:RUN_ID/stream"
```

Set IDs first: `$env:AGENT_ID = "..."` · `$env:RUN_ID = "..."`

**Terminal (alternative):** **Git Bash** / **WSL** — bash `curl -N` block above.

Parse lines starting with `event:` and `data:` — print assistant text, tool calls, and result status.

<!--
Hands-on time for Exercise 8.2 — Stream with curl. This exercise is Stream Agent Responses (SSE). Goal: Stream Cloud Agent events with Server-Sent Events.. Follow the detailed steps in slide-exercises/module-08/exercise-8.2-stream-agent-responses-sse.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe Terminal: PowerShell curl.exe -N -u "$($env:CURSOR_USER_API_KEY):" ` -H "Accept: text/event-stream" ` "https://api.cursor.com/v1/agents/$env:AGENT_ID/runs/$env:RUN_ID/stream" Set IDs first: $env:AGENT_ID = "..." · $env:RUN_ID = "..." Terminal (alternative): Git Bash / WSL — bash curl -N block above. Parse lines starting with event: and data: — print assistant text, tool calls, and result status.

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 8.2 — Python SSE Client

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```python
def stream_agent_response(agent_id, run_id, on_event=None):
    url = f"{BASE_URL}/agents/{agent_id}/runs/{run_id}/stream"
    response = requests.get(url, auth=AUTH, stream=True)
    for line in response.iter_lines():
        if line.startswith(b'event:'):
            current_event = line[6:].strip().decode()
        elif line.startswith(b'data:'):
            data = json.loads(line[5:].strip())
            if on_event:
                on_event(current_event, data)
```

<!--
Hands-on time for Exercise 8.2 — Python SSE Client. This exercise is Stream Agent Responses (SSE). Goal: Stream Cloud Agent events with Server-Sent Events.. Follow the detailed steps in slide-exercises/module-08/exercise-8.2-stream-agent-responses-sse.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe def stream_agent_response(agent_id, run_id, on_event=None): url = f"{BASE_URL}/agents/{agent_id}/runs/{run_id}/stream" response = requests.get(url, auth=AUTH, stream=True) for line in response.iter_lines(): if line.startswith(b'event:'): current_event = line[6:].strip().decode() elif line.startswith(b'data:'): data = json.loads(line[5:].strip()) if on_event: on_event(current_event, data)

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 8.2 — ResumableSSEClient

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

Track `last_event_id` from `id:` lines → send as `Last-Event-ID` header on reconnect

**Also:** `stream_to_file()` saves full SSE log for later review

**Success Criteria:** Stream connected · received events · Python client works · resume implemented

<!--
Hands-on time for Exercise 8.2 — ResumableSSEClient. This exercise is Stream Agent Responses (SSE). Goal: Stream Cloud Agent events with Server-Sent Events.. Follow the detailed steps in slide-exercises/module-08/exercise-8.2-stream-agent-responses-sse.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Track last_event_id from id: lines → send as Last-Event-ID header on reconnect Also: stream_to_file() saves full SSE log for later review Success Criteria: Stream connected · received events · Python client works · resume implemented

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 8.3

## Listing and Downloading Artifacts

*Concept · 5 min · Exercise · 10 min*

<!--
We now begin Lesson 8.3: Listing and Downloading Artifacts. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Wait for completion, list artifacts, and download outputs. Open the lab guide at slide-exercises/module-08/exercise-8.3-list-and-download-artifacts.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Key Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/v1/agents/{id}/artifacts` | GET | List all artifacts |
| `/v1/agents/{id}/artifacts/download` | GET | Get presigned URL for download |

**Important:** Download URLs expire after **15 minutes**.

<!--
Walk this table conversationally: Endpoint — Method, Purpose. /v1/agents/{id}/artifacts — GET, List all artifacts. /v1/agents/{id}/artifacts/download — GET, Get presigned URL for download. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Exercise 8.3 — Wait & List

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```python
def wait_for_completion(agent_id, timeout=300, poll_interval=5):
    while time.time() - start < timeout:
        status = get_agent_status(agent_id).get('status')
        if status == 'FINISHED': return True
        elif status == 'ERROR': return False
        time.sleep(poll_interval)

def list_artifacts(agent_id):
    response = requests.get(f"{BASE_URL}/agents/{agent_id}/artifacts", auth=AUTH)
    return response.json().get('items', [])
```

<!--
Hands-on time for Exercise 8.3 — Wait & List. This exercise is List and Download Artifacts. Goal: Wait for completion, list artifacts, and download outputs.. Follow the detailed steps in slide-exercises/module-08/exercise-8.3-list-and-download-artifacts.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe def wait_for_completion(agent_id, timeout=300, poll_interval=5): while time.time() - start < timeout: status = get_agent_status(agent_id).get('status') if status == 'FINISHED': return True elif status == 'ERROR': return False time.sleep(poll_interval) def list_artifacts(agent_id): response = requests.get(f"{BASE_URL}/agents/{agent_id}/artifacts", auth=AUTH) return response.json().get('items', [])

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 8.3 — Download

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

**Single artifact:**

```python
response = requests.get(
    f"{BASE_URL}/agents/{agent_id}/artifacts/download",
    auth=AUTH, params={"path": artifact_path}
)
download_url = response.json().get('url')
# curl download_url → save to disk
```

**All artifacts:** loop items, create subdirs, download each via presigned URL

<!--
Hands-on time for Exercise 8.3 — Download. This exercise is List and Download Artifacts. Goal: Wait for completion, list artifacts, and download outputs.. Follow the detailed steps in slide-exercises/module-08/exercise-8.3-list-and-download-artifacts.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe Single artifact: response = requests.get( f"{BASE_URL}/agents/{agent_id}/artifacts/download", auth=AUTH, params={"path": artifact_path} ) download_url = response.json().get('url') All artifacts: loop items, create subdirs, download each via presigned URL

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 8.3 — CI Integration

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```python
def process_test_results(agent_id):
    wait_for_completion(agent_id, timeout=600)
    download_artifact(agent_id, "artifacts/junit.xml", "test_results.xml")
    # Parse XML → exit 1 if failures/errors, else exit 0
```

**Success Criteria:** Listed artifacts · downloaded single + all · CI workflow integration

<!--
Hands-on time for Exercise 8.3 — CI Integration. This exercise is List and Download Artifacts. Goal: Wait for completion, list artifacts, and download outputs.. Follow the detailed steps in slide-exercises/module-08/exercise-8.3-list-and-download-artifacts.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe def process_test_results(agent_id): wait_for_completion(agent_id, timeout=600) download_artifact(agent_id, "artifacts/junit.xml", "test_results.xml") Success Criteria: Listed artifacts · downloaded single + all · CI workflow integration

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 8.4

## Creating a Webhook Endpoint

*Concept · 5 min · Exercise · 10 min*

<!--
We now begin Lesson 8.4: Creating a Webhook Endpoint. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Receive webhooks and verify HMAC signatures. Open the lab guide at slide-exercises/module-08/exercise-8.4-webhooks-and-hmac-verification.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Webhook Headers

| Header | Description |
|--------|-------------|
| `X-Webhook-Signature` | HMAC-SHA256 signature for verification |
| `X-Webhook-ID` | Unique delivery ID |
| `X-Webhook-Event` | Event type (`statusChange`) |

<!--
Walk this table conversationally: Header — Description. X-Webhook-Signature — HMAC-SHA256 signature for verification. X-Webhook-ID — Unique delivery ID. X-Webhook-Event — Event type (statusChange). Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Webhook Payload

```json
{
  "event": "statusChange",
  "id": "agent_abc123",
  "status": "FINISHED",
  "source": {"repository": "https://github.com/your-org/your-repo"},
  "target": {"url": "...", "prUrl": "https://github.com/.../pull/123"},
  "summary": "Added README.md and fixed tests"
}
```

<!--
{ "event": "statusChange", "id": "agent_abc123", Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "{" and explain why it matters.
-->

---


## Exercise 8.4 — HMAC Verification

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```python
def verify_signature(raw_body, signature_header):
    received = signature_header[7:]  # strip "sha256="
    expected = hmac.new(
        WEBHOOK_SECRET.encode(), raw_body, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, received)
```

Flask route: verify signature → parse payload → handle FINISHED/ERROR

<!--
Hands-on time for Exercise 8.4 — HMAC Verification. This exercise is Webhooks and HMAC Verification. Goal: Receive webhooks and verify HMAC signatures.. Follow the detailed steps in slide-exercises/module-08/exercise-8.4-webhooks-and-hmac-verification.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe def verify_signature(raw_body, signature_header): received = signature_header[7:]  # strip "sha256=" expected = hmac.new( WEBHOOK_SECRET.encode(), raw_body, hashlib.sha256 ).hexdigest() return hmac.compare_digest(expected, received) Flask route: verify signature → parse payload → handle FINISHED/ERROR

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 8.4 — Configure Agent

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
curl -X POST https://api.cursor.com/v1/agents \
  -u "$CURSOR_USER_API_KEY:" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {"text": "Add a CONTRIBUTING.md file"},
    "repos": [{"url": "https://github.com/YOUR_ORG/YOUR_REPO"}],
    "webhookUrl": "https://your-domain.com/webhook/cursor",
    "webhookSecret": "your-secret-here",
    "autoCreatePR": true
  }'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

**Success Criteria:** Server running · signature verified · payload parsed · agent configured

<!--
Hands-on time for Exercise 8.4 — Configure Agent. This exercise is Webhooks and HMAC Verification. Goal: Receive webhooks and verify HMAC signatures.. Follow the detailed steps in slide-exercises/module-08/exercise-8.4-webhooks-and-hmac-verification.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe curl -X POST https://api.cursor.com/v1/agents \ -u "$CURSOR_USER_API_KEY:" \ -H "Content-Type: application/json" \ -d '{ "prompt": {"text": "Add a CONTRIBUTING.md file"}, "repos": [{"url": "https://github.com/YOUR_ORG/YOUR_REPO"}], "webhookUrl": "https://your-domain.com/webhook/cursor", "webhookSecret": "your-secret-here", "autoCreatePR": true }' PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl. Success Criteria: Server running · signature verified · payload parsed · agent configured

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 8.5

## Testing Webhooks Locally with ngrok

*Concept · 5 min · Exercise · 8 min*

<!--
We now begin Lesson 8.5: Testing Webhooks Locally with ngrok. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Expose a local server with ngrok and inspect webhook payloads. Open the lab guide at slide-exercises/module-08/exercise-8.5-test-webhooks-with-ngrok.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What Is ngrok?

Creates a secure tunnel from a public URL to your local server.

- Test webhooks without deploying
- Debug locally · Demo to stakeholders

<!--
On this slide, What Is ngrok?, cover these points in order: F i r s t ,   T e s t   w e b h o o k s   w i t h o u t   d e p l o y i n g . Next, Debug locally · Demo to stakeholders.
-->

---


## Exercise 8.5 — Steps 1–3

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`


**Step 1:** Start tunnel:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
ngrok http 5000
# Forwarding: https://abc123.ngrok.io -> http://localhost:5000
```

<!--
Hands-on time for Exercise 8.5 — Steps 1–3. This exercise is Test Webhooks with ngrok. Goal: Expose a local server with ngrok and inspect webhook payloads.. Follow the detailed steps in slide-exercises/module-08/exercise-8.5-test-webhooks-with-ngrok.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe Step 1: Start tunnel: Terminal: PowerShell — unless step notes Git Bash or WSL ngrok http 5000

Tell them to paste this prompt into the Agent (or read it aloud while they type): "ngrok http 5000 # Forwarding: https://abc123.ngrok.io -> http://localhost:5000"

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 8.5 — Steps 1–3 (Part 2)

**Step 2:** Copy HTTPS URL
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

<!--
Hands-on time for Exercise 8.5 — Steps 1–3 (Part 2). This exercise is Test Webhooks with ngrok. Goal: Expose a local server with ngrok and inspect webhook payloads.. Follow the detailed steps in slide-exercises/module-08/exercise-8.5-test-webhooks-with-ngrok.md. 

Step 2: Copy HTTPS URL Terminal: PowerShell — unless step notes Git Bash or WSL

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 8.5 — Steps 1–3 (Part 3)

**Step 3:** Create agent with ngrok URL:
**Terminal:** **PowerShell** — ``Ctrl+` `` in Cursor

```bash
curl -X POST https://api.cursor.com/v1/agents ... \
  -d '{"webhookUrl": "https://abc123.ngrok.io/webhook/cursor", ...}'
```

<!--
Hands-on time for Exercise 8.5 — Steps 1–3 (Part 3). This exercise is Test Webhooks with ngrok. Goal: Expose a local server with ngrok and inspect webhook payloads.. Follow the detailed steps in slide-exercises/module-08/exercise-8.5-test-webhooks-with-ngrok.md. 

Step 3: Create agent with ngrok URL: Terminal: PowerShell — `Ctrl+ `` in Cursor curl -X POST https://api.cursor.com/v1/agents ... \ -d '{"webhookUrl": "https://abc123.ngrok.io/webhook/cursor", ...}'

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 8.5 — Inspect & Replay

**Platform:** Windows 10/11 · Agent → ``Ctrl+L`` · Shell → **PowerShell** · Browser for dashboards

**Step 4:** Inspect requests at `http://127.0.0.1:4040`
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

**Step 5:** Replay failed webhooks (ngrok premium) — inspect raw body and headers
**Terminal:** **Git Bash** or **Ubuntu (WSL)** — bash syntax required

**Success Criteria:** Tunnel established · webhook received · signature verified · inspected in ngrok UI

<!--
Hands-on time for Exercise 8.5 — Inspect & Replay. This exercise is Test Webhooks with ngrok. Goal: Expose a local server with ngrok and inspect webhook payloads.. Follow the detailed steps in slide-exercises/module-08/exercise-8.5-test-webhooks-with-ngrok.md. 

Platform: Windows 10/11 · Agent → `Ctrl+L` · Shell → PowerShell · Browser for dashboards Step 4: Inspect requests at http://127.0.0.1:4040 Terminal: PowerShell — unless step notes Git Bash or WSL Step 5: Replay failed webhooks (ngrok premium) — inspect raw body and headers Terminal: Git Bash or Ubuntu (WSL) — bash syntax required Success Criteria: Tunnel established · webhook received · signature verified · inspected in ngrok UI

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 8.6

## End-to-End Automated Agent Workflow

*Concept · 5 min · Exercise · 12 min*

<!--
We now begin Lesson 8.6: End-to-End Automated Agent Workflow. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## The Capstone Integration

Combine everything into `automated_workflow.py`:

1. **Create agent** (with optional webhook URL)
2. **Wait for completion** (webhook or polling)
3. **Download artifacts**
4. **Process results** (CI exit codes, notifications)

<!--
For slide 364, The Capstone Integration: Combine everything into automated_workflow.py: 1. Create agent (with optional webhook URL) 2. Wait for completion (webhook or polling) 3. Download artifacts 4. Process results (CI exit codes, notifications)

Check for questions before you advance. If the room is silent, ask a specific question tied to the slide content.
-->

---


## Workflow Architecture

<img src="assets/module-08/workflow-architecture.svg" alt="Workflow Architecture" />

<!--
This slide is visual: Workflow Architecture. Point to each part of the diagram in order — left to right or top to bottom — and name it once.

After explaining the flow, ask: does this match how you thought the system worked? Misconceptions here will cause mistakes later, so pause for one question.
-->

---


## Run the Workflow

```bash
export CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx"

python automated_workflow.py \
  --repo "https://github.com/YOUR_ORG/YOUR_REPO" \
  --prompt "Add a comprehensive README.md with setup and API docs" \
  --output "./outputs"

# Polling only (no webhook):
python automated_workflow.py --repo "..." --prompt "..." --no-webhook
```

<!--
export CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx" python automated_workflow.py \ --repo "https://github.com/YOUR_ORG/YOUR_REPO" \ Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "export CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx"" and explain why it matters.
-->

---


## Workflow Output

```
🚀 CLOUD AGENT AUTOMATED WORKFLOW
📝 Creating agent... Agent ID: agt_abc123
⏳ Waiting for completion...
✅ Webhook received: Agent agt_abc123 completed
📎 Downloaded 3 artifacts to agent_outputs/
✅ WORKFLOW COMPLETE
```

**Success Criteria:** Creates agent · waits (webhook/polling) · downloads artifacts · end-to-end run

<!--
🚀 CLOUD AGENT AUTOMATED WORKFLOW 📝 Creating agent... Agent ID: agt_abc123 ⏳ Waiting for completion... Do not read every line of code unless you are teaching syntax. Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid.

For example, point at this line: "🚀 CLOUD AGENT AUTOMATED WORKFLOW" and explain why it matters.
-->

---


## Module Summary

| Lesson | Topic | Key Skill |
|--------|-------|-----------|
| 8.1 | Creating a Cloud Agent | Programmatic agent launch |
| 8.2 | Streaming Agent Responses | SSE with resume support |
| 8.3 | Listing and Downloading Artifacts | CI pipeline integration |
| 8.4 | Creating a Webhook Endpoint | HMAC verification |
| 8.5 | Testing Webhooks with ngrok | Local tunnel debugging |
| 8.6 | End-to-End Workflow | Complete automation |

<!--
Module 8 summary. In sixty seconds, walk the lesson table and restate one key insight per row.

Ask the closing question: what will you do differently on Monday? Take two or three answers.

Announce the break or introduce the next module with one connecting sentence.
-->

---


## Quick Reference Card

```
ENDPOINTS:
  POST /v1/agents                         Create agent
  GET  /v1/agents/{id}                    Get status
  GET  /v1/agents/{id}/runs/{id}/stream   SSE stream
  GET  /v1/agents/{id}/artifacts          List artifacts
  GET  /v1/agents/{id}/artifacts/download Download

WEBHOOK:  X-Webhook-Signature (HMAC-SHA256)  |  X-Webhook-Event

SSE:  status · assistant · thinking · tool_call · result · error · done

NGROK:  ngrok http 5000  |  inspect at http://127.0.0.1:4040
```

<!--
This quick reference slide is meant for post-course use. Tell participants to screenshot it or copy the commands into their team wiki.

Offer two minutes for questions on this module only, then move on.
-->

---


<!-- _header: 'Module 9 — Admin and Analytics APIs' -->

<!-- _class: lead -->

# Admin and Analytics APIs

## Module 9 · Day 2 (Hands-On + Demonstrations)

Cursor Training Program · ~75 min

<!--
We are starting Module 9: Admin and Analytics APIs. Cursor Training Program · ~75 min State the module goal in plain language: what participants will be able to do when we finish — not just what topics we will mention.

Preview whether this module is lecture, hands-on, or mixed. If it is hands-on, tell people when to open their laptops and which folder or repo to use. If it is concept-only, ask them to listen for one idea they can use on Monday morning.
-->

---


## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~75 minutes |
| **Format** | Hands-on exercise + demonstrations |
| **Prerequisites** | Admin API key (not User key), Python 3.8+, Modules 7–8 completed |
| **Module Goal** | Master team management, usage analytics, cost governance, and safe admin operations |

<!--
This module overview slide sets expectations. In your own words, cover: Duration is ~75 minutes. Format is Hands-on exercise + demonstrations. Prerequisites is Admin API key (not User key), Python 3.8+, Modules 7–8 completed. Module Goal is Master team management, usage analytics, cost governance, and safe admin operations.  Call out prerequisites explicitly and pause until anyone blocked by missing tools has help. Do not read the table word-for-word — translate it into what the room will experience in the next hour.
-->

---


## Learning Objectives

By the end of this module, participants will be able to:

- List and manage team members programmatically
- Retrieve daily usage data for cost tracking and reporting
- Set user spend limits for budget governance
- Analyze model usage for cost optimization insights
- Track daily active users for leadership reporting
- Build responsible leaderboards without privacy violations
- Analyze conversation intent and complexity (demonstration)
- Safely remove team members with proper patterns (demonstration)

<!--
These learning objectives describe outcomes, not topics. Paraphrase them: List and manage team members programmatically. Retrieve daily usage data for cost tracking and reporting. Set user spend limits for budget governance. Analyze model usage for cost optimization insights. Track daily active users for leadership reporting. Build responsible leaderboards without privacy violations. Analyze conversation intent and complexity (demonstration). Safely remove team members with proper patterns (demonstration).

Ask the room: which of these would help your team most this quarter? Note one or two answers — you can refer back at the module summary.

Tell participants they are not expected to memorize this list; they should recognize each outcome when they have done it during an exercise or demo.
-->

---


## Agenda

| Lesson | Topic | Time | Type |
|--------|-------|------|------|
| 9.1 | Listing Team Members | 8 min | Exercise |
| 9.2 | Daily Usage Data | 10 min | Exercise |
| 9.3 | Setting User Spend Limits | 8 min | Exercise |
| 9.4 | Model Usage Analytics | 8 min | Exercise |
| 9.5 | Daily Active Users | 6 min | Exercise |
| 9.6 | Leaderboards | 6 min | Exercise |
| 9.7 | Conversation Insights | 6 min | Demo |
| 9.8 | Destructive Admin Operations | 6 min | Demo |

<!--
Use this agenda as your pacing map for the module. You will cover: Lesson 9.1, Listing Team Members, about 8 min; Lesson 9.2, Daily Usage Data, about 10 min; Lesson 9.3, Setting User Spend Limits, about 8 min; Lesson 9.4, Model Usage Analytics, about 8 min; Lesson 9.5, Daily Active Users, about 6 min; Lesson 9.6, Leaderboards, about 6 min. Announce when the next hands-on block starts so people can close email and open Cursor. If you fall behind, shorten concept repetition before cutting exercise time.
-->

---


<!-- _class: lead -->

# Lesson 9.1

## Listing Team Members

*Concept · 5 min · Exercise · 8 min*

<!--
We now begin Lesson 9.1: Listing Team Members. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

List team members with pagination and export to CSV. Open the lab guide at slide-exercises/module-09/exercise-9.1-list-team-members.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## User vs. Admin API Key

| Aspect | User API Key | Admin API Key |
|--------|--------------|---------------|
| **Scope** | Your user only | Entire organization |
| **Can list members** | ❌ No | ✅ Yes |
| **Can view others' usage** | ❌ No | ✅ Yes |
| **Can modify policies** | ❌ No | ✅ Yes |
| **Format** | `cursor_xxx...` | `cursor_admin_xxx...` |

**Key endpoint:** `GET /v1/admin/members`

<!--
Walk this table conversationally: Aspect — User API Key, Admin API Key. Scope — Your user only, Entire organization. Can list members — ❌ No, ✅ Yes. Can view others' usage — ❌ No, ✅ Yes. Can modify policies — ❌ No, ✅ Yes. Format — cursor_xxx..., cursor_admin_xxx.... Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Cursor Agent panel** (`Ctrl+L`) is for natural-language prompts — not a shell.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Pause the slide deck for environment setup. Everyone should open PowerShell or Git Bash in Cursor's integrated terminal.

For API exercises: set keys with `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY` — never commit keys to git. On Windows, use `curl.exe` rather than the PowerShell curl alias when the lab shows curl commands.

Walk the room for two to three minutes. Common blockers: wrong key type, missing curl, wrong working directory. Do not advance until most pairs show a successful test call or are paired with someone who has.
-->

---


## Exercise 9.1 — Setup & List

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
export CURSOR_ADMIN_API_KEY="cursor_admin_xxxxxxxxxxxx"

# Verify admin access
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  https://api.cursor.com/v1/admin/organization | jq '.'

# List all team members
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/members" | jq '.'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

<!--
Hands-on time for Exercise 9.1 — Setup & List. This exercise is List Team Members. Goal: List team members with pagination and export to CSV.. Follow the detailed steps in slide-exercises/module-09/exercise-9.1-list-team-members.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe export CURSOR_ADMIN_API_KEY="cursor_admin_xxxxxxxxxxxx" curl -s -u "$CURSOR_ADMIN_API_KEY:" \ https://api.cursor.com/v1/admin/organization | jq '.' curl -s -u "$CURSOR_ADMIN_API_KEY:" \ "https://api.cursor.com/v1/admin/members" | jq '.' PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 9.1 — Pagination & Export

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

**Pagination:**

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/members?limit=10&offset=0"
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

**Python:** loop with offset until empty → export to `team_roster.csv` (email, role, status, joined, lastActiveAt)

**Helper:** `get_user_id_by_email(email)` for downstream admin calls

**Success Criteria:** Authenticated · listed members · handled pagination · exported CSV

<!--
Hands-on time for Exercise 9.1 — Pagination & Export. This exercise is List Team Members. Goal: List team members with pagination and export to CSV.. Follow the detailed steps in slide-exercises/module-09/exercise-9.1-list-team-members.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe Pagination: curl -s -u "$CURSOR_ADMIN_API_KEY:" \ "https://api.cursor.com/v1/admin/members?limit=10&offset=0" PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl. Python: loop with offset until empty → export to team_roster.csv (email, role, status, joined, lastActiveAt) Helper: get_user_id_by_email(email) for downstream admin calls Success Criteria: Authenticated · listed members · handled pagination · exported CSV

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 9.2

## Daily Usage Data

*Concept · 5 min · Exercise · 10 min*

<!--
We now begin Lesson 9.2: Daily Usage Data. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Pull daily usage and build a weekly cost report. Open the lab guide at slide-exercises/module-09/exercise-9.2-daily-usage-data.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Key Endpoint

`GET /v1/admin/analytics/usage/daily`

**Returns:**
- Cost per day · Input/output token counts
- Active users per day · Breakdown by user and model (optional)

> *"Finance asks: 'What did we spend yesterday?' Engineering leads ask: 'Who's using what?'"*

<!--
Read or closely paraphrase the quote on screen: "Finance asks: 'What did we spend yesterday?' Engineering leads ask: 'Who's using what?'"

GET /v1/admin/analytics/usage/daily Returns: - Cost per day · Input/output token counts - Active users per day · Breakdown by user and model (optional)

Pause two beats after the quote so it lands. Then ask whether anyone has seen the opposite problem in real projects.
-->

---


## Exercise 9.2 — Weekly Usage

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
END=$(date +%Y-%m-%d)
START=$(date -d "7 days ago" +%Y-%m-%d)

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/analytics/usage/daily?startDate=$START&endDate=$END" \
  | jq '.daily[] | {date: .date, cost: .cost, tokens: .totalTokens, users: .activeUsers}'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

<!--
Hands-on time for Exercise 9.2 — Weekly Usage. This exercise is Daily Usage Data. Goal: Pull daily usage and build a weekly cost report.. Follow the detailed steps in slide-exercises/module-09/exercise-9.2-daily-usage-data.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe END=$(date +%Y-%m-%d) START=$(date -d "7 days ago" +%Y-%m-%d) curl -s -u "$CURSOR_ADMIN_API_KEY:" \ "https://api.cursor.com/v1/admin/analytics/usage/daily?startDate=$START&endDate=$END" \ PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 9.2 — Cost Report

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

Python `generate_cost_report()` for last 30 days:

- Total cost · total tokens · average daily cost/users
- Week-over-week change · top 5 costliest days
- Daily breakdown table (last 14 days)
- Budget alerts at $300 / $500 thresholds

**Success Criteria:** Retrieved date range · calculated trends · generated readable report

<!--
Hands-on time for Exercise 9.2 — Cost Report. This exercise is Daily Usage Data. Goal: Pull daily usage and build a weekly cost report.. Follow the detailed steps in slide-exercises/module-09/exercise-9.2-daily-usage-data.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Python generate_cost_report() for last 30 days: - Total cost · total tokens · average daily cost/users - Week-over-week change · top 5 costliest days - Daily breakdown table (last 14 days) - Budget alerts at $300 / $500 thresholds Success Criteria: Retrieved date range · calculated trends · generated readable report

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 9.3

## Setting User Spend Limits

*Concept · 5 min · Exercise · 8 min*

<!--
We now begin Lesson 9.3: Setting User Spend Limits. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Set and bulk-update per-user spending limits. Open the lab guide at slide-exercises/module-09/exercise-9.3-set-user-spend-limits.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Key Endpoint

`PATCH /v1/admin/policies/users/{userId}/limits`

| Action | Behavior |
|--------|----------|
| `alert` | Send notification but allow usage |
| `block` | Prevent any further requests for the month |

<!--
Walk this table conversationally: Action — Behavior. alert — Send notification but allow usage. block — Prevent any further requests for the month. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Exercise 9.3 — Set Limits

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
USER_ID=$(curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  "https://api.cursor.com/v1/admin/members?email=developer@company.com" \
  | jq -r '.members[0].id')

curl -X PATCH ".../policies/users/$USER_ID/limits" \
  -u "$CURSOR_ADMIN_API_KEY:" \
  -d '{"monthlyLimit": 50.00, "exceedanceAction": "block"}'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

Check current limit: `GET .../policies/users/{userId}/limits`

<!--
Hands-on time for Exercise 9.3 — Set Limits. This exercise is Set User Spend Limits. Goal: Set and bulk-update per-user spending limits.. Follow the detailed steps in slide-exercises/module-09/exercise-9.3-set-user-spend-limits.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe USER_ID=$(curl -s -u "$CURSOR_ADMIN_API_KEY:" \ "https://api.cursor.com/v1/admin/members?email=developer@company.com" \ curl -X PATCH ".../policies/users/$USER_ID/limits" \ -u "$CURSOR_ADMIN_API_KEY:" \ -d '{"monthlyLimit": 50.00, "exceedanceAction": "block"}' PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl. Check current limit: GET .../policies/users/{userId}/limits

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 9.3 — Bulk Limits

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

**CSV bulk set:** `email, monthly_limit, action`

```csv
intern@company.com,20,block
contractor@company.com,50,alert
lead@company.com,200,alert
```

**Find heavy users:** query `/analytics/usage/users` for current month → filter cost > threshold

**Success Criteria:** Retrieved user ID · set limit · verified · bulk setting implemented

<!--
Hands-on time for Exercise 9.3 — Bulk Limits. This exercise is Set User Spend Limits. Goal: Set and bulk-update per-user spending limits.. Follow the detailed steps in slide-exercises/module-09/exercise-9.3-set-user-spend-limits.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor CSV bulk set: email, monthly_limit, action intern@company.com,20,block contractor@company.com,50,alert lead@company.com,200,alert Find heavy users: query /analytics/usage/users for current month → filter cost > threshold Success Criteria: Retrieved user ID · set limit · verified · bulk setting implemented

Tell them to paste this prompt into the Agent (or read it aloud while they type): "intern@company.com,20,block contractor@company.com,50,alert lead@company.com,200,alert"

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 9.4

## Model Usage Analytics

*Concept · 5 min · Exercise · 8 min*

<!--
We now begin Lesson 9.4: Model Usage Analytics. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Analyze model usage and identify optimization opportunities. Open the lab guide at slide-exercises/module-09/exercise-9.4-model-usage-analytics.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Key Endpoint

`GET /v1/admin/analytics/usage/models`

> *"Which models are actually being used? Is Opus worth the cost? Should you train people on cheaper alternatives?"*

<!--
Read or closely paraphrase the quote on screen: "Which models are actually being used? Is Opus worth the cost? Should you train people on cheaper alternatives?"

GET /v1/admin/analytics/usage/models

Pause two beats after the quote so it lands. Then ask whether anyone has seen the opposite problem in real projects.
-->

---


## Exercise 9.4 — Model Breakdown

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/usage/models?startDate=$START&endDate=$END" \
  | jq '.models[] | {model: .modelId, cost: .cost, requests: .requestCount}'

# Find Opus overuse per user
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/usage/users?startDate=$START&endDate=$END" \
  | jq '.users[] | select(.modelBreakdown."claude-4.7-opus" != null)'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

<!--
Hands-on time for Exercise 9.4 — Model Breakdown. This exercise is Model Usage Analytics. Goal: Analyze model usage and identify optimization opportunities.. Follow the detailed steps in slide-exercises/module-09/exercise-9.4-model-usage-analytics.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe curl -s -u "$CURSOR_ADMIN_API_KEY:" \ ".../analytics/usage/models?startDate=$START&endDate=$END" \ curl -s -u "$CURSOR_ADMIN_API_KEY:" \ ".../analytics/usage/users?startDate=$START&endDate=$END" \ PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 9.4 — Optimization Report

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

`generate_optimization_report()`:

- Model cost breakdown (% of total)
- Users on Claude Opus → suggest Sonnet for non-critical tasks
- High Sonnet usage → suggest GPT-5.3 Codex (40% savings)
- Estimated monthly savings if guidelines applied

**Success Criteria:** Retrieved model breakdown · identified expensive users · generated recommendations

<!--
Hands-on time for Exercise 9.4 — Optimization Report. This exercise is Model Usage Analytics. Goal: Analyze model usage and identify optimization opportunities.. Follow the detailed steps in slide-exercises/module-09/exercise-9.4-model-usage-analytics.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor generate_optimization_report(): - Model cost breakdown (% of total) - Users on Claude Opus → suggest Sonnet for non-critical tasks - High Sonnet usage → suggest GPT-5.3 Codex (40% savings) - Estimated monthly savings if guidelines applied Success Criteria: Retrieved model breakdown · identified expensive users · generated recommendations

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 9.5

## Daily Active Users (DAU)

*Concept · 4 min · Exercise · 6 min*

<!--
We now begin Lesson 9.5: Daily Active Users (DAU). Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Report daily active users over a date range. Open the lab guide at slide-exercises/module-09/exercise-9.5-daily-active-users-dau.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Why DAU Matters

- Track adoption after rollout
- Identify unused licenses for reallocation
- Measure impact of training sessions
- Justify renewal and expansion

**Source:** `activeUsers` field from `/admin/analytics/usage/daily`

<!--
On this slide, Why DAU Matters, cover these points in order: F i r s t ,   T r a c k   a d o p t i o n   a f t e r   r o l l o u t . Next, Identify unused licenses for reallocation. Next, Measure impact of training sessions. Next, Justify renewal and expansion.
-->

---


## Exercise 9.5 — DAU Report

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/usage/daily?startDate=$START&endDate=$END" \
  | jq '{avg_weekly: ([.daily[-7:] | .[].activeUsers] | add / length),
         peak: ([.daily[] | .activeUsers] | max)}'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

**Python leadership report:**
- Average/median/peak DAU · adoption rate (% of team)
- WoW growth rate · weekly averages
- Health assessment: >80% excellent · >50% good · <30% investigate

**Success Criteria:** Calculated DAU · adoption metrics · leadership-ready report

<!--
Hands-on time for Exercise 9.5 — DAU Report. This exercise is Daily Active Users (DAU). Goal: Report daily active users over a date range.. Follow the detailed steps in slide-exercises/module-09/exercise-9.5-daily-active-users-dau.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe curl -s -u "$CURSOR_ADMIN_API_KEY:" \ ".../analytics/usage/daily?startDate=$START&endDate=$END" \ peak: ([.daily[] | .activeUsers] | max)}' PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl. Python leadership report: - Average/median/peak DAU · adoption rate (% of team) - WoW growth rate · weekly averages - Health assessment: >80% excellent · >50% good · <30% investigate Success Criteria: Calculated DAU · adoption metrics · leadership-ready report

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 9.6

## Leaderboards

*Concept · 5 min · Exercise · 6 min*

<!--
We now begin Lesson 9.6: Leaderboards. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Build leaderboards for tabs, AI lines, and agent runs. Open the lab guide at slide-exercises/module-09/exercise-9.6-leaderboards.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Responsible Leaderboard Principles

| Principle | Implementation |
|-----------|----------------|
| **Anonymize** | Roles or anonymized names, not full emails |
| **Focus on positive metrics** | Show savings, not spending |
| **Opt-in only** | Allow users to choose public visibility |
| **Include context** | Show team size, role differences |

<!--
Walk this table conversationally: Principle — Implementation. Anonymize — Roles or anonymized names, not full emails. Focus on positive metrics — Show savings, not spending. Opt-in only — Allow users to choose public visibility. Include context — Show team size, role differences. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Exercise 9.6 — Three Leaderboards

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

**1. Engagement leaderboard** — rank by request count (anonymized emails)

**2. Efficiency leaderboard** — tokens per dollar spent

**3. Savings leaderboard** — users who saved by choosing efficient models over Opus

```python
def anonymize_email(email):
    local = email.split('@')[0]
    return local[:2] + "..." + local[-2:]
```

**Success Criteria:** Anonymized · efficiency-focused · savings-focused leaderboards

<!--
Hands-on time for Exercise 9.6 — Three Leaderboards. This exercise is Leaderboards. Goal: Build leaderboards for tabs, AI lines, and agent runs.. Follow the detailed steps in slide-exercises/module-09/exercise-9.6-leaderboards.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe 1. Engagement leaderboard — rank by request count (anonymized emails) 2. Efficiency leaderboard — tokens per dollar spent 3. Savings leaderboard — users who saved by choosing efficient models over Opus def anonymize_email(email): local = email.split('@')[0] return local[:2] + "..." + local[-2:] Success Criteria: Anonymized · efficiency-focused · savings-focused leaderboards

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 9.7

## Conversation Insights

*Concept · 6 min · Demonstration*

<!--
We now begin Lesson 9.7: Conversation Insights. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## What Conversation Insights Reveal

- Simple questions vs. complex refactors?
- Most common task categories
- Where users get stuck
- Which models perform best for which task types

**Endpoint:** `GET /v1/admin/analytics/conversations` (may require Enterprise plan)

<!--
On this slide, What Conversation Insights Reveal, cover these points in order: F i r s t ,   S i m p l e   q u e s t i o n s   v s .   c o m p l e x   r e f a c t o r s ? . Next, Most common task categories. Next, Where users get stuck. Next, Which models perform best for which task types.
-->

---


## Demo: Intent Analysis

<img src="assets/module-09/demo-intent-analysis.svg" alt="Demo: Intent Analysis" />

<!--
This slide supports a live demonstration: Intent Analysis. Narrate every click and keystroke — assume no one has seen this screen before.

If the network fails, describe what would happen and show a screenshot or backup recording. Save questions until the demo completes unless someone is completely lost.

Close the demo by stating when they would use this in production and when they would not.
-->

---


## Demo: Complexity & Categories

**Complexity distribution:**
- simple 45% · moderate 33% · complex 15% · architectural 7%

**Category analysis:**
- backend 40% · frontend 29% · database 15% · devops 10% · security 6%

**Stuck patterns:** conversations >5 min with `success: false` → suggest training/docs

**Success Criteria:** Understood capabilities · intent/complexity/category tracking · stuck patterns

<!--
This slide supports a live demonstration: Complexity & Categories. Narrate every click and keystroke — assume no one has seen this screen before.

If the network fails, describe what would happen and show a screenshot or backup recording. Save questions until the demo completes unless someone is completely lost.

Close the demo by stating when they would use this in production and when they would not.
-->

---


<!-- _class: lead -->

# Lesson 9.8

## Destructive Admin Operations

*Concept · 6 min · Demonstration*

<!--
We now begin Lesson 9.8: Destructive Admin Operations. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Safe Removal Playbook

1. **Audit first** — active agents, runs, API keys
2. **Soft delete** — deactivate (no new agents; existing continue)
3. **Transfer ownership** — critical agents, webhooks
4. **Log everything** — compliance audit trail
5. **Confirm before hard delete** — GDPR/security only

<!--
For slide 402, Safe Removal Playbook: 1. Audit first — active agents, runs, API keys 2. Soft delete — deactivate (no new agents; existing continue) 3. Transfer ownership — critical agents, webhooks 4. Log everything — compliance audit trail 5. Confirm before hard delete — GDPR/security only

Check for questions before you advance. If the room is silent, ask a specific question tied to the slide content.
-->

---


## Demo: SafeRemovalDemo Workflow

<img src="assets/module-09/demo-saferemovaldemo-workflow.svg" alt="Demo: SafeRemovalDemo Workflow" />

**Bulk deactivation:** find users inactive 90+ days → review → notify → deactivate

**Success Criteria:** 5-step pattern · audit-first · soft vs hard delete · resource transfer

<!--
This slide supports a live demonstration: SafeRemovalDemo Workflow. Narrate every click and keystroke — assume no one has seen this screen before.

If the network fails, describe what would happen and show a screenshot or backup recording. Save questions until the demo completes unless someone is completely lost.

Close the demo by stating when they would use this in production and when they would not.
-->

---


## Module Summary

| Lesson | Topic | Type |
|--------|-------|------|
| 9.1 | Listing Team Members | Exercise |
| 9.2 | Daily Usage Data | Exercise |
| 9.3 | Setting User Spend Limits | Exercise |
| 9.4 | Model Usage Analytics | Exercise |
| 9.5 | Daily Active Users | Exercise |
| 9.6 | Leaderboards | Exercise |
| 9.7 | Conversation Insights | Demo |
| 9.8 | Destructive Operations | Demo |

<!--
Module 9 summary. In sixty seconds, walk the lesson table and restate one key insight per row.

Ask the closing question: what will you do differently on Monday? Take two or three answers.

Announce the break or introduce the next module with one connecting sentence.
-->

---


## Quick Reference Card

<img src="assets/module-09/quick-reference-card.svg" alt="Quick Reference Card" />

<!--
This quick reference slide is meant for post-course use. Tell participants to screenshot it or copy the commands into their team wiki.

Offer two minutes for questions on this module only, then move on.
-->

---


<!-- _header: 'Module 10 — AI Code Tracking and Reporting' -->

<!-- _class: lead -->

# AI Code Tracking and Reporting

## Module 10 · Day 2 (Hands-On + Take-Home Project)

Cursor Training Program · ~20 min + take-home

<!--
We are starting Module 10: AI Code Tracking and Reporting. Cursor Training Program · ~20 min + take-home State the module goal in plain language: what participants will be able to do when we finish — not just what topics we will mention.

Preview whether this module is lecture, hands-on, or mixed. If it is hands-on, tell people when to open their laptops and which folder or repo to use. If it is concept-only, ask them to listen for one idea they can use on Monday morning.
-->

---


## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~20 minutes (plus take-home project) |
| **Format** | Hands-on exercise + take-home project |
| **Prerequisites** | Admin API key, Git repository access, Modules 8–9 completed |
| **Module Goal** | Track AI vs. human contributions, export metrics to BI tools, build compliance dashboards |

<!--
This module overview slide sets expectations. In your own words, cover: Duration is ~20 minutes (plus take-home project). Format is Hands-on exercise + take-home project. Prerequisites is Admin API key, Git repository access, Modules 8–9 completed. Module Goal is Track AI vs. human contributions, export metrics to BI tools, build compliance dashboards.  Call out prerequisites explicitly and pause until anyone blocked by missing tools has help. Do not read the table word-for-word — translate it into what the room will experience in the next hour.
-->

---


## Learning Objectives

By the end of this module, participants will be able to:

- Attribute AI vs. human contributions per commit
- Stream metrics to BI tools via CSV export
- Access granular AI change events for compliance
- Build a complete reporting dashboard combining all data sources

<!--
These learning objectives describe outcomes, not topics. Paraphrase them: Attribute AI vs. human contributions per commit. Stream metrics to BI tools via CSV export. Access granular AI change events for compliance. Build a complete reporting dashboard combining all data sources.

Ask the room: which of these would help your team most this quarter? Note one or two answers — you can refer back at the module summary.

Tell participants they are not expected to memorize this list; they should recognize each outcome when they have done it during an exercise or demo.
-->

---


## Agenda

| Lesson | Topic | Time |
|--------|-------|------|
| 10.1 | AI Commit Metrics | 8 min |
| 10.2 | Bulk Export via CSV Streaming | 7 min |
| 10.3 | Granular AI Change Events | 7 min |
| 10.4 | Reporting Dashboard Architecture | 4 min + take-home |

<!--
Use this agenda as your pacing map for the module. You will cover: Lesson 10.1, AI Commit Metrics, about 8 min; Lesson 10.2, Bulk Export via CSV Streaming, about 7 min; Lesson 10.3, Granular AI Change Events, about 7 min; Lesson 10.4, Reporting Dashboard Architecture, about 4 min + take-home. Announce when the next hands-on block starts so people can close email and open Cursor. If you fall behind, shorten concept repetition before cutting exercise time.
-->

---


<!-- _class: lead -->

# Lesson 10.1

## AI Commit Metrics

*Concept · 3 min · Exercise · 5 min*

<!--
We now begin Lesson 10.1: AI Commit Metrics. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Fetch AI commit metrics and calculate contribution percentage. Open the lab guide at slide-exercises/module-10/exercise-10.1-ai-commit-metrics.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Key Endpoint

`GET /v1/admin/analytics/commits`

**What this measures:**
- Lines added by AI vs. human
- Files modified by agent vs. manual
- Commit-level attribution · Per-developer breakdown

> *"The 'ROI of AI' metric — how much code was AI-generated vs. human-written."*

<!--
Read or closely paraphrase the quote on screen: "The 'ROI of AI' metric — how much code was AI-generated vs. human-written."

GET /v1/admin/analytics/commits What this measures: - Lines added by AI vs. human - Files modified by agent vs. manual - Commit-level attribution · Per-developer breakdown

Pause two beats after the quote so it lands. Then ask whether anyone has seen the opposite problem in real projects.
-->

---


## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Cursor Agent panel** (`Ctrl+L`) is for natural-language prompts — not a shell.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Pause the slide deck for environment setup. Everyone should open PowerShell or Git Bash in Cursor's integrated terminal.

For API exercises: set keys with `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY` — never commit keys to git. On Windows, use `curl.exe` rather than the PowerShell curl alias when the lab shows curl commands.

Walk the room for two to three minutes. Common blockers: wrong key type, missing curl, wrong working directory. Do not advance until most pairs show a successful test call or are paired with someone who has.
-->

---


## Exercise 10.1 — Fetch Metrics

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
END=$(date +%Y-%m-%d)
START=$(date -d "30 days ago" +%Y-%m-%d)

curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/commits?startDate=$START&endDate=$END&repo=https://github.com/YOUR_ORG/YOUR_REPO" \
  | jq '.'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

<!--
Hands-on time for Exercise 10.1 — Fetch Metrics. This exercise is AI Commit Metrics. Goal: Fetch AI commit metrics and calculate contribution percentage.. Follow the detailed steps in slide-exercises/module-10/exercise-10.1-ai-commit-metrics.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe END=$(date +%Y-%m-%d) START=$(date -d "30 days ago" +%Y-%m-%d) curl -s -u "$CURSOR_ADMIN_API_KEY:" \ ".../analytics/commits?startDate=$START&endDate=$END&repo=https://github.com/YOUR_ORG/YOUR_REPO" \ PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 10.1 — AI Contribution %

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/commits?startDate=$START&endDate=$END" \
  | jq '{
      total_commits: .summary.totalCommits,
      ai_commits: .summary.aiAuthoredCommits,
      ai_percentage: (.summary.aiAuthoredCommits / .summary.totalCommits * 100),
      lines_saved: .summary.aiGeneratedLines
    }'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

<!--
Hands-on time for Exercise 10.1 — AI Contribution %. This exercise is AI Commit Metrics. Goal: Fetch AI commit metrics and calculate contribution percentage.. Follow the detailed steps in slide-exercises/module-10/exercise-10.1-ai-commit-metrics.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe curl -s -u "$CURSOR_ADMIN_API_KEY:" \ ".../analytics/commits?startDate=$START&endDate=$END" \ total_commits: .summary.totalCommits, ai_commits: .summary.aiAuthoredCommits, ai_percentage: (.summary.aiAuthoredCommits / .summary.totalCommits * 100), lines_saved: .summary.aiGeneratedLines }' PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 10.1 — ROI Analysis

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

Python `calculate_ai_roi()`:

```
AI-generated lines vs. human-written lines (%)
Estimated time saved (10 lines/min assumption)
Estimated cost saved ($100/hr developer cost)
AI usage cost → Net ROI
```

`contributor_breakdown()` — AI %, AI lines, commits per developer

**Success Criteria:** Retrieved metrics · calculated AI % · generated ROI analysis

<!--
Hands-on time for Exercise 10.1 — ROI Analysis. This exercise is AI Commit Metrics. Goal: Fetch AI commit metrics and calculate contribution percentage.. Follow the detailed steps in slide-exercises/module-10/exercise-10.1-ai-commit-metrics.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor Python calculate_ai_roi(): AI-generated lines vs. human-written lines (%) Estimated time saved (10 lines/min assumption) Estimated cost saved ($100/hr developer cost) AI usage cost → Net ROI contributor_breakdown() — AI %, AI lines, commits per developer Success Criteria: Retrieved metrics · calculated AI % · generated ROI analysis

Tell them to paste this prompt into the Agent (or read it aloud while they type): "AI-generated lines vs. human-written lines (%) Estimated time saved (10 lines/min assumption) Estimated cost saved ($100/hr developer cost) AI usage cost → Net ROI"

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 10.2

## Bulk Export via CSV Streaming

*Concept · 3 min · Exercise · 4 min*

<!--
We now begin Lesson 10.2: Bulk Export via CSV Streaming. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Stream large CSV exports for BI tools. Open the lab guide at slide-exercises/module-10/exercise-10.2-bulk-export-via-csv-streaming.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Key Endpoint

`GET /v1/admin/analytics/export/csv` (streaming)

> *"Wire metrics into BI tools (Tableau, PowerBI, Looker, Metabase) without timeouts."*

**Export types:** `commits` · `events` · `usage`

<!--
Read or closely paraphrase the quote on screen: "Wire metrics into BI tools (Tableau, PowerBI, Looker, Metabase) without timeouts."

GET /v1/admin/analytics/export/csv (streaming) Export types: commits · events · usage

Pause two beats after the quote so it lands. Then ask whether anyone has seen the opposite problem in real projects.
-->

---


## Exercise 10.2 — Stream to File

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
curl -N -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/export/csv?startDate=$START&endDate=$END&type=commits" \
  -o cursor_commits_export.csv

head -10 cursor_commits_export.csv
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

<!--
Hands-on time for Exercise 10.2 — Stream to File. This exercise is Bulk Export via CSV Streaming. Goal: Stream large CSV exports for BI tools.. Follow the detailed steps in slide-exercises/module-10/exercise-10.2-bulk-export-via-csv-streaming.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe curl -N -u "$CURSOR_ADMIN_API_KEY:" \ ".../analytics/export/csv?startDate=$START&endDate=$END&type=commits" \ -o cursor_commits_export.csv head -10 cursor_commits_export.csv PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 10.2 — BI Integration

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

Python `stream_to_dataframe()` → pandas DataFrame:

```python
export_for_bi():
  bi_commits.csv   # commit data
  bi_events.csv    # event data
  bi_usage.csv     # usage data
```

Upload to Metabase, PowerBI, or Tableau via CSV import

**Success Criteria:** Streamed CSV · loaded into DataFrame · created BI-ready files

<!--
Hands-on time for Exercise 10.2 — BI Integration. This exercise is Bulk Export via CSV Streaming. Goal: Stream large CSV exports for BI tools.. Follow the detailed steps in slide-exercises/module-10/exercise-10.2-bulk-export-via-csv-streaming.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe Python stream_to_dataframe() → pandas DataFrame: export_for_bi(): bi_commits.csv   # commit data bi_events.csv    # event data bi_usage.csv     # usage data Upload to Metabase, PowerBI, or Tableau via CSV import Success Criteria: Streamed CSV · loaded into DataFrame · created BI-ready files

Tell them to paste this prompt into the Agent (or read it aloud while they type): "export_for_bi():   bi_commits.csv   # commit data   bi_events.csv    # event data   bi_usage.csv     # usage data"

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 10.3

## Granular AI Change Events

*Concept · 3 min · Exercise · 4 min*

<!--
We now begin Lesson 10.3: Granular AI Change Events. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Query per-change AI events for compliance reporting. Open the lab guide at slide-exercises/module-10/exercise-10.3-granular-ai-change-events.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Key Endpoint

`GET /v1/admin/analytics/events`

**Tracks per event:**
- File, line range, model used, timestamp
- User, accepted/rejected status

> *"Essential for SOC2, ISO, and internal audits."*

<!--
Read or closely paraphrase the quote on screen: "Essential for SOC2, ISO, and internal audits."

GET /v1/admin/analytics/events Tracks per event: - File, line range, model used, timestamp - User, accepted/rejected status

Pause two beats after the quote so it lands. Then ask whether anyone has seen the opposite problem in real projects.
-->

---


## Exercise 10.3 — Query Events

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`

```bash
curl -s -u "$CURSOR_ADMIN_API_KEY:" \
  ".../analytics/events?startDate=$START&endDate=$END&limit=100" \
  | jq '.events[] | {user: .user.email, file: .filePath, model: .modelId, accepted: .accepted}'
```

**PowerShell (Windows):** Same steps in **PowerShell** — use `$env:NAME = "value"` instead of `export`, and `curl.exe` instead of `curl`.

Acceptance rate by model: group events → total vs. accepted per model

<!--
Hands-on time for Exercise 10.3 — Query Events. This exercise is Granular AI Change Events. Goal: Query per-change AI events for compliance reporting.. Follow the detailed steps in slide-exercises/module-10/exercise-10.3-granular-ai-change-events.md. 

Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe curl -s -u "$CURSOR_ADMIN_API_KEY:" \ ".../analytics/events?startDate=$START&endDate=$END&limit=100" \ PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl. Acceptance rate by model: group events → total vs. accepted per model

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


## Exercise 10.3 — Compliance Report

**Platform:** Windows 10/11 · Prompts → **Agent panel** ``Ctrl+L`` · Diffs → **Editor**

`generate_compliance_report()` for last 90 days:

- Acceptance rate by model (table)
- Top 10 files with most AI changes (needs review)
- Export `compliance_export.csv` for auditors:
  - timestamp, user_email, model_id, file_path, line_start, line_end, accepted

**Success Criteria:** Retrieved events · calculated acceptance rates · compliance export

<!--
Hands-on time for Exercise 10.3 — Compliance Report. This exercise is Granular AI Change Events. Goal: Query per-change AI events for compliance reporting.. Follow the detailed steps in slide-exercises/module-10/exercise-10.3-granular-ai-change-events.md. 

Platform: Windows 10/11 · Prompts → Agent panel `Ctrl+L` · Diffs → Editor generate_compliance_report() for last 90 days: - Acceptance rate by model (table) - Top 10 files with most AI changes (needs review) - Export compliance_export.csv for auditors: - timestamp, user_email, model_id, file_path, line_start, line_end, accepted Success Criteria: Retrieved events · calculated acceptance rates · compliance export

Give work time now. Circulate quietly. Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell. When most are done, ask: who got a useful result? Who hit an error we should discuss?
-->

---


<!-- _class: lead -->

# Lesson 10.4

## Reporting Dashboard Architecture

*Concept · 4 min · Take-Home Project*

<!--
We now begin Lesson 10.4: Reporting Dashboard Architecture. Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — so participants know whether to listen, type along, or watch.

Design a leadership dashboard combining analytics APIs. Open the lab guide at slide-exercises/module-10/exercise-10.4-reporting-dashboard-architecture.md when we reach the exercise slides. Transition from the previous lesson with one sentence on how this topic connects to what they just learned.
-->

---


## Dashboard Components

| Component | Data Source | Purpose |
|-----------|-------------|---------|
| Usage Overview | Usage API | Cost, tokens, active users |
| AI Contribution | Commits API | ROI, adoption metrics |
| Model Performance | Events API | Acceptance rates, efficiency |
| Team Activity | Members API | Onboarding, licensing |
| Compliance | Events + Audit | Audit trail, security |

<!--
Walk this table conversationally: Component — Data Source, Purpose. Usage Overview — Usage API, Cost, tokens, active users. AI Contribution — Commits API, ROI, adoption metrics. Model Performance — Events API, Acceptance rates, efficiency. Team Activity — Members API, Onboarding, licensing. Compliance — Events + Audit, Audit trail, security. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Take-Home: Streamlit Dashboard

Run with: `streamlit run cursor_dashboard.py`

**5 panels:**
1. **Executive Summary** — cost, DAU, AI %, team size
2. **Usage Analytics** — daily cost trend (Plotly line chart)
3. **AI Code Impact** — AI vs human bar chart + acceptance by model
4. **Team Management** — member table
5. **Compliance Export** — download events CSV

<!--
For slide 426, Take-Home: Streamlit Dashboard: Run with: streamlit run cursor_dashboard.py 5 panels: 1. Executive Summary — cost, DAU, AI %, team size 2. Usage Analytics — daily cost trend (Plotly line chart) 3. AI Code Impact — AI vs human bar chart + acceptance by model 4. Team Management — member table 5. Compliance Export — download events CSV

Check for questions before you advance. If the room is silent, ask a specific question tied to the slide content.
-->

---


## Project Deliverables

| Deliverable | Description |
|-------------|-------------|
| **Working dashboard** | Streamlit, Metabase, or custom frontend |
| **Documentation** | Setup instructions and data source descriptions |
| **One insight** | Key finding from your team's data |
| **Export script** | Automated CSV export for compliance |

**Bonus:** cost alerts · spend limit UI · model A/B comparison · cloud deployment

<!--
Walk this table conversationally: Deliverable — Description. Working dashboard — Streamlit, Metabase, or custom frontend. Documentation — Setup instructions and data source descriptions. One insight — Key finding from your team's data. Export script — Automated CSV export for compliance. Pick the two rows that matter most to your audience and spend extra time there; summarize the rest in one sentence.
-->

---


## Module Summary

| Lesson | Topic | Key Skill |
|--------|-------|-----------|
| 10.1 | AI Commit Metrics | ROI calculation |
| 10.2 | Bulk Export via CSV | BI integration |
| 10.3 | Granular Change Events | Compliance reporting |
| 10.4 | Dashboard Architecture | Complete dashboard |

<!--
Module 10 summary. In sixty seconds, walk the lesson table and restate one key insight per row.

Ask the closing question: what will you do differently on Monday? Take two or three answers.

Announce the break or introduce the next module with one connecting sentence.
-->

---


## Quick Reference Card

```
ENDPOINTS:
  GET /admin/analytics/commits      AI per commit
  GET /admin/analytics/export/csv   Bulk CSV export
  GET /admin/analytics/events       Granular events

KEY METRICS:
  Adoption:  DAU / total team size
  ROI:       (Hours saved × rate) - AI cost
  Quality:   Acceptance rate by model
  Compliance: Complete change audit trail

DEPLOY:  Streamlit · Metabase · PowerBI · Custom React
```

<!--
This quick reference slide is meant for post-course use. Tell participants to screenshot it or copy the commands into their team wiki.

Offer two minutes for questions on this module only, then move on.
-->

---


<!-- _class: lead -->

# Course Complete

## Cursor Training Program — Day 2

**You can now:**
- Create and manage Cloud Agents programmatically
- Stream agent responses with SSE · Webhooks with HMAC verification
- Administer teams and enforce spending policies
- Analyze usage, model adoption, and AI contribution
- Track AI vs. human code changes per commit
- Build reporting dashboards for leadership

**Next steps:** Complete take-home dashboard · set up scheduled exports · implement cost alerts

*End of Module 10 — End of Day 2 Training Program*

<!--
We are starting Module 10: AI Code Tracking and Reporting. - Administer teams and enforce spending policies State the module goal in plain language: what participants will be able to do when we finish — not just what topics we will mention.

Preview whether this module is lecture, hands-on, or mixed. If it is hands-on, tell people when to open their laptops and which folder or repo to use. If it is concept-only, ask them to listen for one idea they can use on Monday morning.
-->
