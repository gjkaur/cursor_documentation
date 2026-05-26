# Cursor Training Program — Speaker Scripts

Full instructor scripts for [`course-complete-marp.md`](course-complete-marp.md) (433 slides). **Script** = teaching narrative; **Facilitator notes** = pacing and room management.

*Generated: 2026-05-25*

## How to use

- Match **Slide N** to the page number in the deck footer or Marp presenter view (`p`).
- **Script** = what to teach (examples, pitfalls, debriefs) — not a verbatim repeat of the slide.
- Hands-on slides reference lab guides in [`slide-exercises/`](../slide-exercises/).
- Embedded presenter notes: [`course-complete-marp-with-notes.md`](course-complete-marp-with-notes.md).

---

### Slide 1 — Cursor Training Program

**Type:** course_title

**Script**

Good morning, and welcome to the Cursor Training Program — AI-Assisted Development with Cursor. Thank you for being here. Over the next two days we will move from mental models to daily editor workflows, then into automation, Cloud Agents, and the Cursor APIs.

Springpeople · 2-day instructor-led course · Modules 1–10. Before we start, please confirm three things: Cursor is installed, you are signed in, and you have a Git repository you can experiment in — sample repos are fine if you do not want to use production code.

This course is roughly seventy percent hands-on and thirty percent concept and discussion. Questions are welcome during a slide if they are quick; save longer ones for breaks or module transitions.

---

### Slide 2 — Course Agenda

**Type:** course_agenda

**Script**

Here is the full two-day arc for our time together.

Day one builds editor fluency. Module one gives us shared mental models for how AI assistants actually work. Modules two through four are hands-on in the Cursor editor — understanding codebases, making safe changes, working with agent modes, and customizing rules and skills. Module five introduces the CLI for terminal and scripting workflows.

Day two shifts to automation and integration: Cloud Agents in the UI, API authentication and reliability, programmatic Cloud Agent launches and webhooks, admin and analytics reporting, and AI code tracking.

The total scheduled time is about eleven and a half hours across both days, plus breaks. If you have never opened Cursor before, let me know now so I can allow extra setup time in Module two.

---

### Slide 3 — Day 1 — Foundations & Editor Workflows

**Type:** day_overview

**Script**

Day one is about editor confidence — mental models first, then hands-on Cursor through Module 5. We will not call external APIs until tomorrow.

Today's modules in one breath: Module 1 (Foundations), Module 2 (Hands-On), Module 3 (Hands-On + Concept), Module 4 (Hands-On + Walkthrough). Details are on the slide.

---

### Slide 4 — Day 2 — Cloud Agents, APIs & Analytics

**Type:** day_overview

**Script**

Day two assumes yesterday's habits stuck — API keys ready, PowerShell working, and realistic expectations about agent autonomy.

Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.

Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.

Today's modules in one breath: Module 6 (Hands-On + Demonstration), Module 7 (Concept + Hands-On), Module 8 (Hands-On), Module 9 (Hands-On + Demonstrations). Details are on the slide.

---

## Module 1 — Mental Models for AI-Assisted Development

### Slide 5 — Mental Models for AI-Assisted Development

**Type:** module_intro

**Script**

Module 1 is deliberately conceptual — no Cursor setup required. We are building shared vocabulary so Module 2 hands-on work makes sense instead of feeling like magic.

If anyone feels impatient for 'real Cursor tips,' tell them the probabilistic mindset prevents the worst production mistakes later.

Timing on slide: Cursor Training Program · Concept block · ~60 min

---

### Slide 6 — Module Overview

**Type:** module_overview

**Script**

The module goal in plain language: Build accurate mental models of how AI coding assistants work, their limitations, and how to use them effectively

Glance at duration and prerequisites on screen — raise a hand if anything blocks you.

---

### Slide 7 — Learning Objectives

**Type:** learning_objectives

**Script**

These outcomes define success for Module 1 — not a reading list, but skills you will practice.

Highlight three that matter for your role: Explain why AI outputs are probabilistic, not deterministic; Identify and mitigate hallucinations in coding contexts; Understand token-based pricing and cost optimization; plus more on screen.

Next: learning objectives.

Ask who has seen the opposite problem in production — one story beats five bullets.

---

### Slide 8 — Lesson 1.1

**Type:** lesson_intro · **Lesson:** 1.1

**Script**

Lesson 1.1: How AI Models Work. Concept · 12 minutes Participation: listen and take notes — you do not need to type along yet.

This lesson installs the engine-under-the-hood mental model — no Cursor shortcuts yet. Participants should leave understanding why the same prompt can produce different code.

Connect forward: Module 2 failures often trace back to treating the Agent like a deterministic compiler.

**Facilitator notes**

- Pacing: Concept · 12 minutes. Shorten repetition before cutting exercise time.

---

### Slide 9 — Why Outputs Are Probabilistic

**Type:** quote · **Lesson:** 1.1

**Script**

Start with the line on screen: "Unlike traditional software that gives the same output for the same input, AI models generate responses based on probability distributions."

Expand in your own words — do not read the bullet text verbatim: At its simplest, an LLM is a next-token prediction engine. Given a sequence of tokens, it predicts what comes next — then samples, appends, repeats.

Next: Why Outputs Are Probabilistic.

Open with a concrete contrast: run the same unit test twice — same result every time. Run the same prompt twice in ChatGPT or Cursor — you may get different wording, structure, or even logic.

The mental model to install today: LLMs do not execute a stored program. They roll weighted dice for the next token, millions of times per answer. That is why we never ship the first output without review.

Ask the room: where has non-determinism already burned you — flaky tests, or flaky AI summaries?

Pause after the quote — let it land before you add examples.

---

### Slide 10 — Next-Token Prediction

**Type:** diagram · **Lesson:** 1.1

**Script**

This slide shows Next-token prediction probabilities.

The model reads the text so far, assigns a probability to each possible next token, samples one, appends it, and repeats. That loop is how an entire answer is generated.

Next: Next-Token Prediction.

Use the diagram to demystify the magic. Each step is not 'understanding' in the human sense — it is picking the most likely next piece of text given everything so far.

Analogy: autocomplete on your phone, extended for pages of code. The model does not re-read your intent; it extends the pattern.

If someone asks 'but it feels intelligent' — agree, then redirect: pattern completion at scale can look like reasoning, but the mechanism is still probabilistic completion.

On screen: Next-token prediction probabilities

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 11 — Traditional Code vs. AI Model

**Type:** table · **Lesson:** 1.1

**Script**

Next: Traditional Code vs. AI Model.

Do not read the table row by row. Frame it as a mindset shift: yesterday you debugged logic; with AI you debug inputs — prompt, context, model, and parameters.

The row about errors being 'features of probability' lands hard — give an example: a confident wrong import is not a bug in your repo; it is the model filling a gap.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Deterministic (same input → same output): Probabilistic (different outputs possible). You control the logic: You influence, but don't control. Errors are bugs: Errors are features of probability. Predictable behavior: Needs management via parameters.

---

### Slide 12 — Traditional vs. AI — Implication

**Type:** content · **Lesson:** 1.1

**Script**

Next: Traditional vs. AI — Implication.

Never trust a single run as ground truth.

---

### Slide 13 — What Determines AI Output?

**Type:** diagram · **Lesson:** 1.1

**Script**

This slide shows Factors that shape AI output.

Your prompt, system instructions, attached files, model choice, and parameters such as temperature all feed into the same response. When quality shifts, one of these inputs usually changed.

Next: What Determines AI Output?.

When a participant says 'the model got worse today,' walk this diagram mentally: did the model change, or did the context shrink, the prompt get vaguer, or the temperature rise?

Practical tip: before blaming the model, diff your prompt and attached files against yesterday's session.

On screen: Factors that shape AI output

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 14 — Key Parameters You Control

**Type:** table · **Lesson:** 1.1

**Script**

Next: Key Parameters You Control.

Developers rarely tune these directly in Cursor day to day, but admins and API users do. Knowing they exist explains why two teammates get different styles from the 'same' prompt.

Rule of thumb for coding: lower temperature when fixing bugs; slightly higher when exploring design alternatives — then turn it back down before merging.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Temperature: Randomness (0 = deterministic, 1 = creative). Use this when Bug fixes (low), brainstorming (high). Top-p: Nucleus sampling – limits token pool. Use this when Balanced responses. Max Tokens: Limits response length. Use this when Controlling cost.

---

### Slide 15 — Key Parameters — Example Values

**Type:** code · **Lesson:** 1.1

**Script**

Key Parameters — Example Values

These are sensible defaults for focused coding work: a low temperature around 0.2, top-p near 0.9 for balance, and a max token cap to control cost.

Next: Key Parameters — Example Values.

---

### Slide 16 — Temperature Impact

**Type:** code · **Lesson:** 1.1

**Script**

Same prompt: _"Write a function to reverse a string"_

These are sensible defaults for focused coding work: a low temperature around 0.2, top-p near 0.9 for balance, and a max token cap to control cost.

Next: Temperature Impact.

Run this verbally if you have time: same ask, three temperatures. Point out that high temperature did not get 'more creative' — it got less predictable, which is not always desirable in production code.

---

### Slide 17 — The Training Gap

**Type:** bullets · **Lesson:** 1.1

**Script**

There are 4 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Code written after their training date.

Second: Your company's internal APIs — this one usually matters most in practice.

Also on screen: Your specific architecture decisions, Recent library updates (unless in context).

Next: The Training Gap.

This slide prevents the most expensive misconception: 'the model should know our internal API.' It will not unless you put it in context — paste docs, open files, or add rules.

Story beat: a team once debugged for an hour because the model used a deprecated SDK — the fix was attaching the current internal README, not switching models.

Ask who has seen the opposite problem in production — one story beats five bullets.

Models are frozen at their training cutoff date. They don't know: - Code written after their training date

---

### Slide 18 — Lesson 1.2

**Type:** lesson_intro · **Lesson:** 1.2

**Script**

Lesson 1.2: Hallucinations. Concept · 10 minutes Participation: listen and take notes — you do not need to type along yet.

**Facilitator notes**

- Pacing: Concept · 10 minutes. Shorten repetition before cutting exercise time.

---

### Slide 19 — What Are Hallucinations?

**Type:** quote · **Lesson:** 1.2

**Script**

Start with the line on screen: "Confident-sounding outputs that are factually wrong, made up, or don't exist."

Expand in your own words — do not read the bullet text verbatim: Most dangerous form: the model sounds completely confident while being completely wrong.

Next: What Are Hallucinations?.

Emphasize confidence: the model's tone is not calibrated to truth. A wrong answer can sound like a senior engineer.

In code review, treat AI output like a junior's first PR — polite, thorough review required.

Pause after the quote — let it land before you add examples.

---

### Slide 20 — Hallucinations in Code

**Type:** table · **Lesson:** 1.2

**Script**

Next: Hallucinations in Code.

Walk one row deeply — fake APIs are the most common in this room. Mention that Python's import error is your friend; TypeScript often catches invented methods faster than runtime.

Encourage a team norm: if the Agent cites a library method, one person verifies in official docs before merge.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Fake APIs: import nonexistent_library. Use this when Check docs; import fails. Wrong parameters: Incorrect function signature. Use this when Type checking. Invented methods: list.reverse_in_place(). Use this when Know the standard library. Confident nonsense: "This is the standar

---

### Slide 21 — Why Models Hallucinate

**Type:** diagram · **Lesson:** 1.2

**Script**

This slide shows Root causes of hallucination.

Hallucinations come from gaps in training data, missing context, overconfidence, and pressure to answer even when the model should say it does not know.

Next: Why Models Hallucinate.

Root causes of hallucination

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 22 — Example: Confident Wrong

**Type:** code · **Lesson:** 1.2

**Script**

Example: Confident Wrong

The top snippet looks plausible but invents an API that does not exist. The correct approach is to use httpx or aiohttp for async HTTP in Python.

Next: Example: Confident Wrong.

---

### Slide 23 — Hallucination Mitigation Strategies

**Type:** table · **Lesson:** 1.2

**Script**

Next: Hallucination Mitigation Strategies.

Grounding and verification are the habits to take home. Rules and @mentions are how Cursor makes grounding automatic.

Ask: which strategy could your team adopt Monday — paste docs, require citations, or JSON-only outputs?

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Grounding: Provide source material. Use this when Paste library docs into context. Verification: Ask for citations. Use this when "Which line of the docs shows this?". Constrained decoding: Limit possible outputs. Use this when JSON mode, regex patterns. Self-consistency: Ask mul

---

### Slide 24 — Hallucination Detection Checklist

**Type:** bullets · **Lesson:** 1.2

**Script**

There are 6 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Do the imported libraries exist?.

Second: Are function signatures correct? — this one usually matters most in practice.

Also on screen: Does the syntax match my language version?, Are there obvious logic errors?….

Next: Hallucination Detection Checklist.

Ask who has seen the opposite problem in production — one story beats five bullets.

Before accepting AI-generated code, verify: - Do the imported libraries exist?

---

### Slide 25 — The Developer's Mindset

**Type:** quote · **Lesson:** 1.2

**Script**

Start with the line on screen: "_"Trust, but verify – especially when the AI sounds most confident."_"

Expand in your own words — do not read the bullet text verbatim: - Hallucinations decrease with better prompts and context - They never fully disappear

Next: The Developer's Mindset.

Pause after the quote — let it land before you add examples.

---

### Slide 26 — Lesson 1.3

**Type:** lesson_intro · **Lesson:** 1.3

**Script**

Lesson 1.3: Tokens and Pricing. Concept · 10 minutes Participation: listen and take notes — you do not need to type along yet.

Tokens are how vendors meter and limit context — not characters, not lines. Rough guide: 100 tokens ≈ 75 words of English.

Why instructors cover this: without token awareness, people attach entire repos and wonder why answers degrade or bills spike.

**Facilitator notes**

- Pacing: Concept · 10 minutes. Shorten repetition before cutting exercise time.

---

### Slide 27 — What Is a Token?

**Type:** table · **Lesson:** 1.3

**Script**

Next: What Is a Token?.

Tokens are how vendors meter and limit context — not characters, not lines. Rough guide: 100 tokens ≈ 75 words of English.

Why instructors cover this: without token awareness, people attach entire repos and wonder why answers degrade or bills spike.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Language: Example. Use this when Token Count. English: "Hello world". Use this when 2 tokens (~0.75 words/token). English: "Congratulations". Use this when 1 token. Code: function calculateTotal(). Use this when ~5 tokens (~2–4 chars/token). Chinese: "你好世界". Use this when 4–8 tok

---

### Slide 28 — Why Tokens Matter

**Type:** content · **Lesson:** 1.3

**Script**

Next: Why Tokens Matter.

A token is the atomic unit of processing for LLMs — not a word, not a character. You pay per token · Context windows are measured in tokens · Token limits determine how much code… (see slide)

---

### Slide 29 — Input vs. Output Pricing

**Type:** content · **Lesson:** 1.3

**Script**

Next: Input vs. Output Pricing.

Input tokens (prompt, code context, retrieved docs) cost less than output tokens (generated code and explanations). Output is often 5–8× more expensive — generation is more compute-intensive than reading.

---

### Slide 30 — Model Pricing Examples

**Type:** table · **Lesson:** 1.3

**Script**

Next: Model Pricing Examples.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Model: Input (per 1M). Use this when Output (per 1M). GPT-5 Mini: $0.25. Use this when $2.00. Claude 4.5 Haiku: $1.00. Use this when $5.00. GPT-5.3 Codex: $1.75. Use this when $14.00. Gemini 3.1 Pro: $2.00. Use this when $12.00. Claude 4.6 Sonnet: $3.00. Use this when $15.00. Cla

---

### Slide 31 — What 1 Million Tokens Looks Like

**Type:** table · **Lesson:** 1.3

**Script**

Next: What 1 Million Tokens Looks Like.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Plain English text: ~750,000 words (~1,500 pages). Python code: ~250,000–500,000 lines. Average conversation: 5–10 sessions. Full codebase: Small to medium project.

---

### Slide 32 — Cost Calculation Example

**Type:** code · **Lesson:** 1.3

**Script**

Cost Calculation Example

Focus on the first few lines — for example: prompt_tokens = 5000    # instructions + context.

Next: Cost Calculation Example.

Connect to business reality: a daily standup prompt is cheap; an agent loop over 200 files is not.

Teach bounded tasks: narrow @mentions, clear stop conditions, and checkpoints before long agent runs.

---

### Slide 33 — Cost Optimization Strategies

**Type:** table · **Lesson:** 1.3

**Script**

Next: Cost Optimization Strategies.

Connect to business reality: a daily standup prompt is cheap; an agent loop over 200 files is not.

Teach bounded tasks: narrow @mentions, clear stop conditions, and checkpoints before long agent runs.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Use cheaper models: Mini/Haiku for simple tasks. Use this when 5–20× reduction. Reduce context: Only send relevant code. Use this when 2–5× reduction. Cache responses: Reuse common answers. Use this when Variable. Batch operations: Combine multiple tasks. Use this when 30–50% red

---

### Slide 34 — Real-World Cost Bounds

**Type:** table · **Lesson:** 1.3

**Script**

Next: Real-World Cost Bounds.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Usage Level: Monthly Cost. Use this when What You Can Do. Light: $10–20. Use this when Occasional questions, small fixes. Medium: $50–100. Use this when Daily coding, regular agent use. Heavy: $200–500. Use this when Full-time AI assistance, multiple agents. Enterprise: $1000+. U

---

### Slide 35 — The Cache Effect

**Type:** code · **Lesson:** 1.3

**Script**

Models can cache frequently used content: - Cache Write: Cost to initially store - Cache Read: Much cheaper than fresh input (80–95% savings)

The important lines are: .

Next: The Cache Effect.

---

### Slide 36 — Lesson 1.4

**Type:** lesson_intro · **Lesson:** 1.4

**Script**

Lesson 1.4: Context. Concept · 12 minutes · The single most valuable AI skill Participation: listen and take notes — you do not need to type along yet.

**Facilitator notes**

- Pacing: Concept · 12 minutes · The single most valuable AI skill. Shorten repetition before cutting exercise time.

---

### Slide 37 — What Is Context?

**Type:** diagram · **Lesson:** 1.4

**Script**

This slide shows What goes into context.

Context = all the information the model has access to when generating a response. <img src="assets/module-01/context-inputs.svg" alt="What goes into context" />

Next: What Is Context?.

What goes into context

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 38 — The Context Window Limit

**Type:** table · **Lesson:** 1.4

**Script**

Next: The Context Window Limit.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Model: Context Window. Use this when Pages of Text. Claude 4 (Haiku / Sonnet / Opus): 200k. Use this when ~150. GPT-5 Mini / GPT-5.3 Codex: 272k. Use this when ~200.

---

### Slide 39 — Context Window — What Happens When Full

**Type:** content · **Lesson:** 1.4

**Script**

Next: Context Window — What Happens When Full.

When you exceed context: Oldest content gets truncated · Critical information may be dropped Context engineering = knowing what to put in, what to leave out, and how to structure it.

---

### Slide 40 — Context Checklist

**Type:** bullets · **Lesson:** 1.4

**Script**

There are 7 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: What problem am I trying to solve?.

Second: What files/code does the model need to see? — this one usually matters most in practice.

Also on screen: What would a human need to know to help me?, What information can I safely leave out?….

Next: Context Checklist.

Ask who has seen the opposite problem in production — one story beats five bullets.

Before every AI interaction, ask: - What problem am I trying to solve?

---

### Slide 41 — Good vs. Bad Context — Bad Example

**Type:** code · **Lesson:** 1.4

**Script**

BAD (vague):

The important lines are: "Fix this bug: my code doesn't work".

Next: Good vs. Bad Context — Bad Example.

---

### Slide 42 — Good vs. Bad Context — Good Example

**Type:** code · **Lesson:** 1.4

**Script**

GOOD (specific):

The important lines are: Python function sorts dicts by key but raises KeyError.; Code: def sort_by_key(data, key): ...; Input: [{'name': 'Alice'}, {'age': 30}].

Next: Good vs. Bad Context — Good Example.

---

### Slide 43 — Context Prioritization Pyramid

**Type:** diagram · **Lesson:** 1.4

**Script**

This slide shows Context prioritization pyramid.

Not all context is equal. Recent messages, open files, rules, and repository structure compete for the same token budget — put the most important material where the model will actually use it.

Next: Context Prioritization Pyramid.

Use this when teaching @mentions in Module 2: pointing at three files beats pasting ten files 'just in case.'

The pyramid is a prioritization exercise — what must the model see versus what is nice to have?

On screen: Context prioritization pyramid

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 44 — Context Window Management

**Type:** table · **Lesson:** 1.4

**Script**

Next: Context Window Management.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Summarization: Compress earlier conversation. Use this when Long sessions. Selective inclusion: Only relevant files. Use this when Large codebases. Chunking: Split across multiple calls. Use this when Exceeding limit. Hierarchical: Summaries + details on demand. Use this when Com

---

### Slide 45 — The "Lost in the Middle" Problem

**Type:** diagram · **Lesson:** 1.4

**Script**

This slide shows Lost in the middle attention chart.

Models pay most attention to the beginning and end of context, and less to the middle. <img src="assets/module-01/lost-in-middle.svg" alt="Lost in the middle attention chart" /> Implication: Put critical information at the beginning OR end, not the middle.

Next: The "Lost in the Middle" Problem.

Research finding: models attend strongly to the start and end of context, weaker in the middle. Put critical constraints at the top of the prompt and repeat them after long pasted logs.

On screen: Lost in the middle attention chart

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 46 — Lesson 1.5

**Type:** lesson_intro · **Lesson:** 1.5

**Script**

Lesson 1.5: Tool Calling and MCP. Concept · 8 minutes Participation: listen and take notes — you do not need to type along yet.

Tool calling is how the model stops guessing and starts acting — read file, run terminal, fetch URL.

Contrast with plain chat: chat only produces text; tools close the loop with real environment feedback.

MCP is plumbing: one standard way to plug databases, browsers, and internal services into Cursor without custom hacks per vendor.

You will see MCP again in team customization — rules tell the model how to behave; MCP gives it new hands.

**Facilitator notes**

- Pacing: Concept · 8 minutes. Shorten repetition before cutting exercise time.

---

### Slide 47 — What Is Tool Calling?

**Type:** diagram · **Lesson:** 1.5

**Script**

This slide shows Tool calling flow.

The agent proposes an action, Cursor runs the tool, the result returns to the model, and the loop continues until the task is done or you stop it.

Next: What Is Tool Calling?.

Tool calling is how the model stops guessing and starts acting — read file, run terminal, fetch URL.

Contrast with plain chat: chat only produces text; tools close the loop with real environment feedback.

On screen: Tool calling flow

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 48 — Common Tool Types in Development

**Type:** table · **Lesson:** 1.5

**Script**

Next: Common Tool Types in Development.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Tool: Purpose. Use this when Example. read_file: Read code files. Use this when "Show me the auth module". edit_file: Modify code. Use this when "Add error handling to line 42". search_code: Find patterns. Use this when "Find all uses of this function". run_terminal: Execute comm

---

### Slide 49 — MCP (Model Context Protocol)

**Type:** diagram · **Lesson:** 1.5

**Script**

This slide shows MCP architecture.

MCP connects Cursor to external systems through a standard protocol so tools stay outside the model but still appear in the agent loop.

Next: MCP (Model Context Protocol).

MCP is plumbing: one standard way to plug databases, browsers, and internal services into Cursor without custom hacks per vendor.

You will see MCP again in team customization — rules tell the model how to behave; MCP gives it new hands.

On screen: MCP architecture

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 50 — Why MCP Matters

**Type:** table · **Lesson:** 1.5

**Script**

Next: Why MCP Matters.

MCP is plumbing: one standard way to plug databases, browsers, and internal services into Cursor without custom hacks per vendor.

You will see MCP again in team customization — rules tell the model how to behave; MCP gives it new hands.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Interoperability: Same tools work across different AI models. Discoverability: AI can learn what tools are available. Standardization: One protocol, not dozens of custom APIs. Extensibility: Add new tools without changing AI logic.

---

### Slide 51 — Tool Calling Best Practices

**Type:** content · **Lesson:** 1.5

**Script**

Next: Tool Calling Best Practices.

Tool calling is how the model stops guessing and starts acting — read file, run terminal, fetch URL.

Contrast with plain chat: chat only produces text; tools close the loop with real environment feedback.

On screen: 1. Define clear tool schemas — name, description, parameters 2. Validate tool calls before execution — allowlist + parameter checks 3. Set timeouts — e.g., 30 seconds max per tool 4. Log all tool calls… (see slide)

---

### Slide 52 — Lesson 1.6

**Type:** lesson_intro · **Lesson:** 1.6

**Script**

Lesson 1.6: Agents. Concept · 8 minutes Participation: listen and take notes — you do not need to type along yet.

**Facilitator notes**

- Pacing: Concept · 8 minutes. Shorten repetition before cutting exercise time.

---

### Slide 53 — Agent vs. Chatbot

**Type:** table · **Lesson:** 1.6

**Script**

Next: Agent vs. Chatbot.

Chatbots answer questions; agents pursue outcomes across multiple steps. That difference drives cost, risk, and review burden.

Ask the room where they are today — mostly chat, or already letting the agent edit and run commands?

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Interaction: Single turn or simple back-and-forth. Use this when Multi-step, goal-oriented. Control: User drives each step. Use this when Agent plans and executes. Memory: Limited to conversation. Use this when Can maintain state across steps. Actions: None (text only). Use this 

---

### Slide 54 — The Agent Loop

**Type:** content · **Lesson:** 1.6

**Script**

Next: The Agent Loop.

---

### Slide 55 — The Agent Loop — Diagram

**Type:** diagram · **Lesson:** 1.6

**Script**

This slide shows Agent loop diagram.

The agent proposes an action, Cursor runs the tool, the result returns to the model, and the loop continues until the task is done or you stop it.

Next: The Agent Loop — Diagram.

Narrate one full cycle slowly: user goal → model plans → tool runs → output returns → model continues.

Safety hook: each cycle is a chance to stop — checkpoints and diff review exist because loops can run far.

On screen: Agent loop diagram

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 56 — Levels of Agent Autonomy

**Type:** table · **Lesson:** 1.6

**Script**

Next: Levels of Agent Autonomy.

Chatbots answer questions; agents pursue outcomes across multiple steps. That difference drives cost, risk, and review burden.

Ask the room where they are today — mostly chat, or already letting the agent edit and run commands?

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Level: Name. Use this when Description. L1: Assistant. Use this when Responds, needs step-by-step guidance. L2: Tool-caller. Use this when Can request tools, human approves. L3: Planner. Use this when Makes plans, executes with supervision. L4: Autonomous. Use this when Self-dire

---

### Slide 57 — How Agents Change Your Role

**Type:** diagram · **Lesson:** 1.6

**Script**

This slide shows Traditional developer workflow.

Traditional: <img src="assets/module-01/role-flow-traditional.svg" alt="Traditional developer workflow" /> Agent-Assisted: <img src="assets/module-01/role-flow-agent-assisted.svg" alt="Agent-assisted developer workflow" />

Next: How Agents Change Your Role.

Traditional developer workflow

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 58 — Developer Role Shift

**Type:** table · **Lesson:** 1.6

**Script**

Next: Developer Role Shift.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Code writer: Intent specifier. Debugger: Quality reviewer. Implementation: Orchestration. Manual testing: Acceptance testing. Problem solver: Problem framer.

---

### Slide 59 — When to Use Agents

**Type:** bullets · **Lesson:** 1.6

**Script**

There are 6 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Large, multi-step tasks · Repetitive patterns.

Second: Well-defined with clear success criteria — this one usually matters most in practice.

Also on screen: Low-risk changes · Documentation updates, Security-critical systems · Unrecoverable actions….

Next: When to Use Agents.

Ask who has seen the opposite problem in production — one story beats five bullets.

Good for agents: - Large, multi-step tasks · Repetitive patterns

---

### Slide 60 — Module Summary

**Type:** module_summary · **Lesson:** 1.6

**Script**

That completes Module 1. Lesson 1.1, How AI Models Work — key insight: Probabilistic, not deterministic – manage with temperature; Lesson 1.2, Hallucinations — key insight: Models invent confidently – always verify; Lesson 1.3, Tokens and Pricing — key insight: Output costs more – optimize context, use cheaper models; Lesson 1.4, Context — key insight: Single most valuable skill – quality in = quality out; Lesson 1.5, Tool Calling & MCP — key insight: AI requests actions, you control execution; Lesson 1.6, Agents — key insight: Goal-directed action – changes developer role

What will you do differently on Monday? I will take two or three answers before we break or move on.

---

## Module 2 — Cursor Editor Essentials

### Slide 61 — Cursor Editor Essentials

**Type:** module_intro

**Script**

Module 2 is the longest hands-on block today. Laptops open, repo loaded, Agent panel ready — Ctrl+I on Windows.

Success here is not memorizing shortcuts; it is comfort with orientation, safe diffs, and knowing when to stop the Agent.

Timing on slide: Cursor Training Program · Hands-on exercise · ~90 min

---

### Slide 62 — Module Overview

**Type:** module_overview

**Script**

The module goal in plain language: Master the core workflows of AI-assisted coding in Cursor

Glance at duration and prerequisites on screen — raise a hand if anything blocks you.

---

### Slide 63 — Learning Objectives

**Type:** learning_objectives

**Script**

These outcomes define success for Module 2 — not a reading list, but skills you will practice.

Highlight three that matter for your role: Orient an AI agent to an unfamiliar codebase; Get targeted explanations of specific files or symbols; Make safe, reviewable changes using diff review; plus more on screen.

Next: learning objectives.

Ask who has seen the opposite problem in production — one story beats five bullets.

---

### Slide 64 — Agenda

**Type:** module_agenda

**Script**

Here is how we will spend our time: Lesson 2.1, Codebase Understanding, about 20 min; Lesson 2.2, Explaining Files/Symbols, about 13 min; Lesson 2.3, Safe Reviewable Changes, about 13 min; Lesson 2.4, Plan Mode, about 13 min; Lesson 2.5, Comparing Models, about 13 min; Lesson 2.6, @mentions, about 13 min; Lesson 2.7, Checkpoints, about 8 min; Lesson 2.8, Terminal Integration, about 13 min.

**Facilitator notes**

- Announce when the next hands-on block starts so people can close email and open Cursor.

---

### Slide 65 — Lesson 2.1

**Type:** lesson_intro · **Lesson:** 2.1

**Script**

Lesson 2.1: Codebase Understanding. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Use the Cursor Agent to orient yourself in an unfamiliar repository.

Lab reference: slide-exercises/module-02/exercise-2.1-codebase-understanding.md

---

### Slide 66 — The Problem & The Solution

**Type:** quote · **Lesson:** 2.1

**Script**

Start with the line on screen: "Drop an agent into a codebase you've never seen and get a coherent explanation of how it works."

Expand in your own words — do not read the bullet text verbatim: The Problem: Opening a new codebase is overwhelming. Where do you start? What's the entry point? The Cursor Solution: Ask the agent to explain the codebase. It reads files, traces connections, and returns a roadmap.

Next: The Problem & The Solution.

This is the emotional hook for Module 2: onboarding panic is normal. The Agent is a tour guide, not a replacement for reading code.

Set expectation: the first answer will be imperfect — the skill is follow-up prompts that narrow and verify.

Pause after the quote — let it land before you add examples.

---

### Slide 67 — Exercise 2.1 — Steps 1–2

**Type:** exercise · **Lesson:** 2.1 · **Exercise:** 2.1

**Script**

Starting Exercise 2.1 — Codebase Understanding. 20 min scheduled.

Use the Cursor Agent to orient yourself in an unfamiliar repository.

The full lab guide with troubleshooting is in slide-exercises/module-02/exercise-2.1-codebase-understanding.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

For this exercise, any unfamiliar repo works — detectron2 is large on purpose; smaller repos are fine if time is tight.

Verify File → Open Folder, not a single file — the Agent needs the tree to orient.

Step 1: Open an unfamiliar repository in Cursor.

Step 2: Open the Agent panel — `Ctrl+I`.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If Agent panel doesn't open: Make sure Cursor is the active window. Try `Ctrl+Shift+I` or click the Agent icon in the left sidebar
- If Agent not responding: Check your internet connection. The Agent requires an internet connection to access AI models

---

### Slide 68 — Exercise 2.1 — Step 3: Orientation Prompt

**Type:** exercise · **Lesson:** 2.1 · **Exercise:** 2.1

**Script**

Next step — Step 3: Orientation Prompt.

Paste this into the Agent — constraints matter as much as the ask: "Explain this codebase to me as if I'm a new team member. Specifically tell me: 1. What is the main purpose of this project? 2. What are the entry points (main scripts, CLI, API)? 3. What are the key modules and how do they relate? 4. What are the main dependencies? 5. What files should I read first to understand the architecture?"

A strong answer names entry points and a reading order, not a file dump. If the Agent lists fifty files, follow up: 'Which three should I read first?'

Debrief question: what did the Agent get wrong about dependencies or architecture?

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Agent panel doesn't open: Make sure Cursor is the active window. Try `Ctrl+Shift+I` or click the Agent icon in the left sidebar
- If Agent not responding: Check your internet connection. The Agent requires an internet connection to access AI models

---

### Slide 69 — Exercise 2.1 — Step 4: Trace Data Flow

**Type:** exercise · **Lesson:** 2.1 · **Exercise:** 2.1

**Script**

Next step — Step 4: Trace Data Flow.

Step 4: Follow up — trace data flow:.

Paste this into the Agent — constraints matter as much as the ask: "Based on what you just told me, trace the flow of data from input to output. What functions get called in order?"

Follow-up prompts are the skill — the first answer is a map; this step tests whether the Agent can chain calls logically.

If the trace is wrong, ask the Agent to cite file:line for each hop — cheap verification habit.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Agent panel doesn't open: Make sure Cursor is the active window. Try `Ctrl+Shift+I` or click the Agent icon in the left sidebar
- If Agent not responding: Check your internet connection. The Agent requires an internet connection to access AI models

---

### Slide 70 — Exercise 2.1 — Step 5: Visual Overview

**Type:** exercise · **Lesson:** 2.1 · **Exercise:** 2.1

**Script**

Next step — Step 5: Visual Overview.

Step 5: Ask for a visual overview:.

Paste this into the Agent — constraints matter as much as the ask: "Create an ASCII diagram showing the module relationships in this codebase."

ASCII diagrams are good enough for onboarding docs — the point is communicating structure, not pretty graphics.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Agent panel doesn't open: Make sure Cursor is the active window. Try `Ctrl+Shift+I` or click the Agent icon in the left sidebar
- If Agent not responding: Check your internet connection. The Agent requires an internet connection to access AI models

---

### Slide 71 — Expected Agent Output (Sample)

**Type:** diagram · **Lesson:** 2.1 · **Exercise:** 2.1

**Script**

This slide shows Expected Agent Output (Sample).

<img src="assets/module-02/expected-agent-output-sample.svg" alt="Expected Agent Output (Sample)" />

Next: Expected Agent Output (Sample).

Expected Agent Output (Sample)

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 72 — Pro Tip — Save the Overview

**Type:** code · **Lesson:** 2.1 · **Exercise:** 2.1

**Script**

Pro Tip: Save the agent's explanation as a project note:

The important lines are: Save this explanation as .cursor/project-overview.md so future; team members can read it..

Next: Pro Tip — Save the Overview.

---

### Slide 73 — Exercise 2.1 — Success Criteria

**Type:** exercise · **Lesson:** 2.1 · **Exercise:** 2.1

**Script**

Let's debrief Exercise 2.1 — Codebase Understanding.

Check off what you actually completed — not what the Agent claimed: Agent described project purpose; Agent identified entry points and key modules; Agent suggested first files to read.

Close by comparing two groups: who trusted the first answer blindly vs who verified one claim in the repo?

Ask two volunteers: what did the Agent get wrong, and what prompt change fixed it? That reflection is the learning outcome.

**Facilitator notes**

- Common issues: If Agent panel doesn't open: Make sure Cursor is the active window. Try `Ctrl+Shift+I` or click the Agent icon in the left sidebar; If Agent not responding: Check your internet connection. The Agent requires an internet connection to access AI models; If "No codebase found" error: Make sure you opened a folder (File → Open Folder), not just a single file

---

### Slide 74 — Lesson 2.2

**Type:** lesson_intro · **Lesson:** 2.2

**Script**

Lesson 2.2: Explaining a Specific File or Symbol. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Get targeted explanations of one file or symbol without reading the whole repo.

Lab reference: slide-exercises/module-02/exercise-2.2-explaining-a-specific-file-or-symbol.md

---

### Slide 75 — Targeted Explanations

**Type:** quote · **Lesson:** 2.2

**Script**

Start with the line on screen: "Don't make the agent read the whole codebase when you just need to understand one function."

Expand in your own words — do not read the bullet text verbatim: Use precise context — select a function or class, then ask focused questions.

Next: Targeted Explanations.

Pause after the quote — let it land before you add examples.

---

### Slide 76 — Exercise 2.2 — Steps 1–3

**Type:** exercise · **Lesson:** 2.2 · **Exercise:** 2.2

**Script**

Starting Exercise 2.2 — Explaining a Specific File or Symbol. 13 min scheduled.

Get targeted explanations of one file or symbol without reading the whole repo.

The full lab guide with troubleshooting is in slide-exercises/module-02/exercise-2.2-explaining-a-specific-file-or-symbol.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: Open a specific file in your project.

Step 2: Select a function or class you want explained.

Step 3: Use the Agent with precise context:.

Paste this into the Agent — constraints matter as much as the ask: "Explain the function I have selected. For each major section, tell me: - What it does - Why it's designed that way (trade-offs) - Potential edge cases or bugs - How it could be improved"

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If `@filename` doesn't autocomplete: Start typing the full filename. Make sure the file exists in your project
- If Agent says "File not found": Check the exact filename including extension. Use `@` then browse the dropdown

---

### Slide 77 — Exercise 2.2 — Step 4: Example I/O

**Type:** exercise · **Lesson:** 2.2 · **Exercise:** 2.2

**Script**

Next step — Step 4: Example I/O.

Step 4: Ask for a concrete example:.

Paste this into the Agent — constraints matter as much as the ask: "Give me a concrete example of inputs and outputs for this function. Show me what happens in the normal case and one edge case."

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If `@filename` doesn't autocomplete: Start typing the full filename. Make sure the file exists in your project
- If Agent says "File not found": Check the exact filename including extension. Use `@` then browse the dropdown

---

### Slide 78 — Exercise 2.2 — Step 5: Dependencies

**Type:** exercise · **Lesson:** 2.2 · **Exercise:** 2.2

**Script**

Next step — Step 5: Dependencies.

Step 5: Ask about dependencies:.

Paste this into the Agent — constraints matter as much as the ask: "What other functions does this call? What calls this function? Trace the call chain two levels in each direction."

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If `@filename` doesn't autocomplete: Start typing the full filename. Make sure the file exists in your project
- If Agent says "File not found": Check the exact filename including extension. Use `@` then browse the dropdown

---

### Slide 79 — Inline Explanation Shortcut

**Type:** code · **Lesson:** 2.2 · **Exercise:** 2.2

**Script**

Success Criteria: - Selected specific code · Agent explained the selection - Agent provided input/output examples · Agent traced call dependencies

The important lines are: .

Next: Inline Explanation Shortcut.

---

### Slide 80 — Lesson 2.3

**Type:** lesson_intro · **Lesson:** 2.3

**Script**

Lesson 2.3: Making a Safe, Reviewable Change. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Let the Agent propose a small change and review the diff before accepting.

Lab reference: slide-exercises/module-02/exercise-2.3-making-a-safe-reviewable-change.md

---

### Slide 81 — The Diff Review Workflow

**Type:** quote · **Lesson:** 2.3

**Script**

Start with the line on screen: "Before AI changes your code, see exactly what will change and approve it."

Expand in your own words — do not read the bullet text verbatim: 1. Ask agent to propose a change 2. Review the diff (what's added/removed)

Next: The Diff Review Workflow.

Pause after the quote — let it land before you add examples.

---

### Slide 82 — Exercise 2.3 — Steps 1–2

**Type:** exercise · **Lesson:** 2.3 · **Exercise:** 2.3

**Script**

Starting Exercise 2.3 — Making a Safe, Reviewable Change. 13 min scheduled.

Let the Agent propose a small change and review the diff before accepting.

The full lab guide with troubleshooting is in slide-exercises/module-02/exercise-2.3-making-a-safe-reviewable-change.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

This exercise trains review discipline — the change is tiny on purpose. If someone accepts without reading the diff, stop and redo the step.

Step 1: Ask for a small, safe change:.

Step 2: Watch the agent generate the diff:.

Paste this into the Agent — constraints matter as much as the ask: "Change the welcome message in index.html from "Hello World" to "Welcome to My App""

Paste this into the Agent — constraints matter as much as the ask: "📝 Changes to index.html: <h1>- Hello World</h1> <h1>+ Welcome to My App</h1> Accept? [Yes] [No] [Edit]"

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Agent makes changes without showing diff: Ask: *"Show me the diff before applying"*
- If Change breaks the code: Click a checkpoint (in chat timeline) to restore previous version

---

### Slide 83 — Exercise 2.3 — Review Questions

**Type:** exercise · **Lesson:** 2.3 · **Exercise:** 2.3

**Script**

Next step — Review Questions.

Step 4: Accept · Step 5: Test manually.

This exercise trains review discipline — the change is tiny on purpose. If someone accepts without reading the diff, stop and redo the step.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If Agent makes changes without showing diff: Ask: *"Show me the diff before applying"*
- If Change breaks the code: Click a checkpoint (in chat timeline) to restore previous version

---

### Slide 84 — Exercise 2.3 — Test After Accept

**Type:** exercise · **Lesson:** 2.3 · **Exercise:** 2.3

**Script**

Next step — Test After Accept.

Paste this into the Agent — constraints matter as much as the ask: "start index.html # open HTML in default browser python script.py # run Python script npm start # Node/React dev server"

This exercise trains review discipline — the change is tiny on purpose. If someone accepts without reading the diff, stop and redo the step.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Agent makes changes without showing diff: Ask: *"Show me the diff before applying"*
- If Change breaks the code: Click a checkpoint (in chat timeline) to restore previous version

---

### Slide 85 — Exercise 2.3 — If Something Goes Wrong

**Type:** exercise · **Lesson:** 2.3 · **Exercise:** 2.3

**Script**

Next step — If Something Goes Wrong.

Paste this into the Agent — constraints matter as much as the ask: "That change didn't work. The button disappeared. Please explain what happened and suggest a fix."

This exercise trains review discipline — the change is tiny on purpose. If someone accepts without reading the diff, stop and redo the step.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Agent makes changes without showing diff: Ask: *"Show me the diff before applying"*
- If Change breaks the code: Click a checkpoint (in chat timeline) to restore previous version

---

### Slide 86 — Lesson 2.4

**Type:** lesson_intro · **Lesson:** 2.4

**Script**

Lesson 2.4: Plan Mode. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Use Plan Mode to design a change before the Agent edits files.

Plan Mode buys review time before files change — use it for multi-file refactors and unfamiliar code.

Compare to jumping straight to Agent: plans are cheaper to throw away than bad diffs.

Lab reference: slide-exercises/module-02/exercise-2.4-plan-mode.md

---

### Slide 87 — Design Before You Code

**Type:** bullets · **Lesson:** 2.4

**Script**

There are 4 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Changing multiple files · Adding a new feature.

Second: Refactoring existing code — this one usually matters most in practice.

Also on screen: You're not 100% sure of the best approach, The change is risky or hard to undo.

Next: Design Before You Code.

Ask who has seen the opposite problem in production — one story beats five bullets.

Plan Mode makes the agent create a detailed plan BEFORE writing any code. When to use Plan Mode:

---

### Slide 88 — Exercise 2.4 — Step 1: Enable Plan Mode

**Type:** exercise · **Lesson:** 2.4 · **Exercise:** 2.4

**Script**

Starting Exercise 2.4 — Plan Mode. 13 min scheduled.

Use Plan Mode to design a change before the Agent edits files.

The full lab guide with troubleshooting is in slide-exercises/module-02/exercise-2.4-plan-mode.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: Enable Plan Mode (Shift+Tab in the Agent input):.

Paste this into the Agent — constraints matter as much as the ask: "# Press Shift+Tab in the Agent input # The input border changes color to indicate Plan Mode"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If Plan Mode not activating: Press `Shift+Tab` again. Check chat input shows "Plan"
- If Agent starts coding immediately: Ask: *"I'm in Plan Mode. Please plan first, don't write code yet"*

---

### Slide 89 — Exercise 2.4 — Step 2: Describe Change

**Type:** exercise · **Lesson:** 2.4 · **Exercise:** 2.4

**Script**

Next step — Step 2: Describe Change.

Step 2: Describe a complex change:.

Paste this into the Agent — constraints matter as much as the ask: "Add user authentication to this web app. Requirements: - Email/password login · Session management - Protected routes (dashboard, settings) - Logout functionality · "Remember me" option Don't write code yet – just give me a plan."

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Plan Mode not activating: Press `Shift+Tab` again. Check chat input shows "Plan"
- If Agent starts coding immediately: Ask: *"I'm in Plan Mode. Please plan first, don't write code yet"*

---

### Slide 90 — Exercise 2.4 — Step 3: Review the Plan

**Type:** exercise · **Lesson:** 2.4 · **Exercise:** 2.4

**Script**

Next step — Step 3: Review the Plan.

Step 3: Review the agent's plan — a good plan includes:.

Paste this into the Agent — constraints matter as much as the ask: "📋 IMPLEMENTATION PLAN Step 1: Create User Model — models/user.js Step 2: Auth Routes — routes/auth.js (login, logout, register) Step 3: Session Management — middleware/session.js Step 4: Protected Route Middleware — middleware/auth.js Step 5: Update Frontend — pages/login.html, dashboard.html Step 6: Environment Variables — .env (SESSION_SECRET, REDIS_URL) Questions for you: 1. JWT or server-side sessions? 2. Existing user database? 3. Include email verification? Ready to proceed? [Yes] [No] [Modify Plan]"

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Plan Mode not activating: Press `Shift+Tab` again. Check chat input shows "Plan"
- If Agent starts coding immediately: Ask: *"I'm in Plan Mode. Please plan first, don't write code yet"*

---

### Slide 91 — Exercise 2.4 — Approve & Execute

**Type:** exercise · **Lesson:** 2.4 · **Exercise:** 2.4

**Script**

Next step — Approve & Execute.

Step 4: Answer questions and approve:.

Step 5: Watch the agent execute the plan step by step.

Paste this into the Agent — constraints matter as much as the ask: "Use JWT for simplicity. No existing database yet – use SQLite for now. Skip email verification for this version. Proceed."

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Plan Mode not activating: Press `Shift+Tab` again. Check chat input shows "Plan"
- If Agent starts coding immediately: Ask: *"I'm in Plan Mode. Please plan first, don't write code yet"*

---

### Slide 92 — Exercise 2.4 — Success Criteria

**Type:** exercise · **Lesson:** 2.4 · **Exercise:** 2.4

**Script**

Let's debrief Exercise 2.4 — Plan Mode.

Check off what you actually completed — not what the Agent claimed: Enabled Plan Mode (Shift+Tab); Agent created structured plan; Agent asked clarifying questions; Approved plan before code was written.

Ask two volunteers: what did the Agent get wrong, and what prompt change fixed it? That reflection is the learning outcome.

**Facilitator notes**

- Common issues: If Plan Mode not activating: Press `Shift+Tab` again. Check chat input shows "Plan"; If Agent starts coding immediately: Ask: *"I'm in Plan Mode. Please plan first, don't write code yet"*; If Plan is too vague: Ask: *"Be more specific. What files will you change? What functions?"*

---

### Slide 93 — Lesson 2.5

**Type:** lesson_intro · **Lesson:** 2.5

**Script**

Lesson 2.5: Comparing Two Models. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Run the same prompt on two models and compare quality, speed, and cost.

Same prompt, two models — compare correctness first, speed second, cost third. Fancy answers that fail tests lose.

Encourage documenting 'default model per task' for the team after this exercise.

Lab reference: slide-exercises/module-02/exercise-2.5-comparing-two-models.md

---

### Slide 94 — Model Selection Guide

**Type:** table · **Lesson:** 2.5

**Script**

Next: Model Selection Guide.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Task Type: Recommended Model. Use this when Why. Typo fixes, simple edits: GPT-5 Mini. Use this when Cheap, fast, good enough. Daily coding, bug fixes: Composer 2.5 or GPT-5.3 Codex. Use this when Best value in Cursor; built for agent tools. Complex logic, architecture: Claude Op

---

### Slide 95 — Exercise 2.5 — Compare Two Models

**Type:** exercise · **Lesson:** 2.5 · **Exercise:** 2.5

**Script**

Starting Exercise 2.5 — Comparing Two Models. 13 min scheduled.

Run the same prompt on two models and compare quality, speed, and cost.

The full lab guide with troubleshooting is in slide-exercises/module-02/exercise-2.5-comparing-two-models.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: Set model to Composer 2.5 (/model composer-2.5), ask:.

Step 2: Copy the response.

Step 3: Switch to GPT-5 Mini — ask the same question.

Step 4: Compare responses side by side.

Paste this into the Agent — constraints matter as much as the ask: "Explain what a closure is in JavaScript with a practical example."

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Model not available: Check your plan – some models require Pro or higher
- If `/model` command not working: Type it in the Agent chat, not in terminal

---

### Slide 96 — Exercise 2.5 — Comparison Table

**Type:** exercise · **Lesson:** 2.5 · **Exercise:** 2.5

**Script**

Next step — Comparison Table.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Model not available: Check your plan – some models require Pro or higher
- If `/model` command not working: Type it in the Agent chat, not in terminal

---

### Slide 97 — Exercise 2.5 — Cost & Decision Matrix

**Type:** exercise · **Lesson:** 2.5 · **Exercise:** 2.5

**Script**

Next step — Cost & Decision Matrix.

Step 5: Check token usage at bottom of chat after each request.

Step 6: Create a personal decision matrix:.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Model not available: Check your plan – some models require Pro or higher
- If `/model` command not working: Type it in the Agent chat, not in terminal

---

### Slide 98 — Exercise 2.5 — Success Criteria

**Type:** exercise · **Lesson:** 2.5 · **Exercise:** 2.5

**Script**

Let's debrief Exercise 2.5 — Comparing Two Models.

Check off what you actually completed — not what the Agent claimed: Same question to two models; Compared quality and speed; Created personal model-selection guide.

Ask two volunteers: what did the Agent get wrong, and what prompt change fixed it? That reflection is the learning outcome.

**Facilitator notes**

- Common issues: If Model not available: Check your plan – some models require Pro or higher; If `/model` command not working: Type it in the Agent chat, not in terminal; If Can't tell which model is active: Look at the model name in the chat input dropdown

---

### Slide 99 — Lesson 2.6

**Type:** lesson_intro · **Lesson:** 2.6

**Script**

Lesson 2.6: Precise Context with @mentions. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Use @mentions to point the Agent at exact files, symbols, and context.

Lab reference: slide-exercises/module-02/exercise-2.6-precise-context-with-mentions.md

---

### Slide 100 — @mention Types

**Type:** table · **Lesson:** 2.6

**Script**

Next: @mention Types.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): @mention: What It Does. Use this when Example. @filename: Include specific file. Use this when @auth.py. @symbol: Include function/class. Use this when @UserModel. @branch: Reference git branch. Use this when @main. @chat: Reference past conversation. Use this when @previous-chat

---

### Slide 101 — Exercise 2.6 — Steps 1–2

**Type:** exercise · **Lesson:** 2.6 · **Exercise:** 2.6

**Script**

Starting Exercise 2.6 — Precise Context with @mentions. 13 min scheduled.

Use @mentions to point the Agent at exact files, symbols, and context.

The full lab guide with troubleshooting is in slide-exercises/module-02/exercise-2.6-precise-context-with-mentions.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: Use @filename to point at a specific file:.

Step 2: Use @symbol to reference a specific function:.

Paste this into the Agent — constraints matter as much as the ask: "@database.py What are the security vulnerabilities in this database connection?"

Paste this into the Agent — constraints matter as much as the ask: "@calculate_total This function is returning NaN sometimes. Why?"

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If `@` doesn't show suggestions: Make sure you're in the Agent chat, not a code file
- If Wrong file appears: Type more letters to narrow down the suggestion

---

### Slide 102 — Exercise 2.6 — Step 3: Multiple @mentions

**Type:** exercise · **Lesson:** 2.6 · **Exercise:** 2.6

**Script**

Next step — Step 3: Multiple @mentions.

Step 3: Combine multiple @mentions:.

Paste this into the Agent — constraints matter as much as the ask: "@auth.py @UserModel @login_handler Review the authentication flow. Are there any race conditions or timing attacks?"

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If `@` doesn't show suggestions: Make sure you're in the Agent chat, not a code file
- If Wrong file appears: Type more letters to narrow down the suggestion

---

### Slide 103 — Exercise 2.6 — Step 4: @branch

**Type:** exercise · **Lesson:** 2.6 · **Exercise:** 2.6

**Script**

Next step — Step 4: @branch.

Step 4: Use @branch to reference a different branch:.

Paste this into the Agent — constraints matter as much as the ask: "Compare @main and @feature/payment branches. What are the key differences in the payment handling code?"

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If `@` doesn't show suggestions: Make sure you're in the Agent chat, not a code file
- If Wrong file appears: Type more letters to narrow down the suggestion

---

### Slide 104 — Exercise 2.6 — Step 5: @chat

**Type:** exercise · **Lesson:** 2.6 · **Exercise:** 2.6

**Script**

Next step — Step 5: @chat.

Step 5: Use @chat to refer to a previous conversation:.

Paste this into the Agent — constraints matter as much as the ask: "@chat(authentication-discussion) Based on that discussion, implement the fix we agreed on."

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If `@` doesn't show suggestions: Make sure you're in the Agent chat, not a code file
- If Wrong file appears: Type more letters to narrow down the suggestion

---

### Slide 105 — Exercise 2.6 — Steps 6–7: @folder & @web

**Type:** exercise · **Lesson:** 2.6 · **Exercise:** 2.6

**Script**

Next step — Steps 6–7: @folder & @web.

Step 6: Use @folder for directory-level context:.

Step 7: Use @web for external documentation:.

Paste this into the Agent — constraints matter as much as the ask: "@src/components Find all components that don't have loading states."

Paste this into the Agent — constraints matter as much as the ask: "@web React 19 useTransition hook How do I use it?"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If `@` doesn't show suggestions: Make sure you're in the Agent chat, not a code file
- If Wrong file appears: Type more letters to narrow down the suggestion

---

### Slide 106 — @mention Pro Tips

**Type:** bullets · **Lesson:** 2.6 · **Exercise:** 2.6

**Script**

Point 1: Start typing @ — Cursor auto-suggests available mentions.

Point 2: You can @mention multiple items in one message.

Point 3: @mentions work in both Agent and Chat modes.

Next: @mention Pro Tips.

Ask who has seen the opposite problem in production — one story beats five bullets.

- Start typing @ — Cursor auto-suggests available mentions - You can @mention multiple items in one message

---

### Slide 107 — Exercise 2.6 — Success Criteria

**Type:** exercise · **Lesson:** 2.6 · **Exercise:** 2.6

**Script**

Let's debrief Exercise 2.6 — Precise Context with @mentions.

Check off what you actually completed — not what the Agent claimed: Used @filename to target a specific file; Used @symbol to target a function or class; Used multiple @mentions together; Used @web for external search.

Ask two volunteers: what did the Agent get wrong, and what prompt change fixed it? That reflection is the learning outcome.

**Facilitator notes**

- Common issues: If `@` doesn't show suggestions: Make sure you're in the Agent chat, not a code file; If Wrong file appears: Type more letters to narrow down the suggestion; If @mention not working: Put a space after the @mention before your question

---

### Slide 108 — Lesson 2.7

**Type:** lesson_intro · **Lesson:** 2.7

**Script**

Lesson 2.7: Checkpoints. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Create and restore checkpoints before risky Agent experiments.

Checkpoints are undo for agent experiments — use before risky prompts or broad @folder mentions.

Analogy: git stash for conversation state when you want to explore without fear.

Lab reference: slide-exercises/module-02/exercise-2.7-checkpoints.md

---

### Slide 109 — A Safety Net for Experiments

**Type:** bullets · **Lesson:** 2.7

**Script**

There are 4 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Code changes made by the agent.

Second: Conversation history · File states — this one usually matters most in practice.

Also on screen: Before complex changes · At milestones (Step 2 of 5), Before risky experiments · Before terminal commands.

Next: A Safety Net for Experiments.

Ask who has seen the opposite problem in production — one story beats five bullets.

What Checkpoints Save: - Code changes made by the agent

---

### Slide 110 — Exercise 2.7 — Create & Restore

**Type:** exercise · **Lesson:** 2.7 · **Exercise:** 2.7

**Script**

Starting Exercise 2.7 — Checkpoints. 8 min scheduled.

Create and restore checkpoints before risky Agent experiments.

The full lab guide with troubleshooting is in slide-exercises/module-02/exercise-2.7-checkpoints.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: Create a checkpoint before making a change.

Paste this into the Agent — constraints matter as much as the ask: "# Click checkpoint icon in Agent panel # Windows: ``Ctrl+Shift+S`` (Mac: ``Cmd+Shift+S``)"

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If No checkpoint appears: Make sure you're in Agent mode (not Ask mode). Agent mode creates checkpoints automatically
- If Can't find checkpoint: Scroll up in chat – checkpoints are marked with a dot or icon

---

### Slide 111 — Exercise 2.7 — Steps 2–3

**Type:** exercise · **Lesson:** 2.7 · **Exercise:** 2.7

**Script**

Next step — Steps 2–3.

Step 2: Name it descriptively: "Before auth refactor - safe point".

Step 3: Let the agent make changes:.

Paste this into the Agent — constraints matter as much as the ask: "Add input validation to all form handlers."

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If No checkpoint appears: Make sure you're in Agent mode (not Ask mode). Agent mode creates checkpoints automatically
- If Can't find checkpoint: Scroll up in chat – checkpoints are marked with a dot or icon

---

### Slide 112 — Exercise 2.7 — Steps 4–5

**Type:** exercise · **Lesson:** 2.7 · **Exercise:** 2.7

**Script**

Next step — Steps 4–5.

Step 4: If something goes wrong → Restore to checkpoint.

Step 5: View history via the clock icon in Agent panel.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If No checkpoint appears: Make sure you're in Agent mode (not Ask mode). Agent mode creates checkpoints automatically
- If Can't find checkpoint: Scroll up in chat – checkpoints are marked with a dot or icon

---

### Slide 113 — Checkpoint Best Practices

**Type:** bullets · **Lesson:** 2.7 · **Exercise:** 2.7

**Script**

There are 5 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Create checkpoints every 5–10 minutes during complex work.

Second: Use descriptive names, not "checkpoint1" — this one usually matters most in practice.

Also on screen: Test the restored state before continuing, Clean up old checkpoints periodically….

Next: Checkpoint Best Practices.

Checkpoints are undo for agent experiments — use before risky prompts or broad @folder mentions.

Analogy: git stash for conversation state when you want to explore without fear.

Ask who has seen the opposite problem in production — one story beats five bullets.

- Create checkpoints every 5–10 minutes during complex work - Use descriptive names, not "checkpoint1"

---

### Slide 114 — Lesson 2.8

**Type:** lesson_intro · **Lesson:** 2.8

**Script**

Lesson 2.8: Terminal Integration. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Let the Agent run terminal commands and react to command output.

Lab reference: slide-exercises/module-02/exercise-2.8-terminal-integration.md

---

### Slide 115 — What the Agent Can Do

**Type:** bullets · **Lesson:** 2.8

**Script**

There are 6 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Run shell commands · See stdout, stderr, exit codes.

Second: React to command output · Install dependencies — this one usually matters most in practice.

Also on screen: Run tests · Start/stop services, You approve each command before execution….

Next: What the Agent Can Do.

Ask who has seen the opposite problem in production — one story beats five bullets.

- Run shell commands · See stdout, stderr, exit codes - React to command output · Install dependencies

---

### Slide 116 — Exercise 2.8 — Steps 1–3

**Type:** exercise · **Lesson:** 2.8 · **Exercise:** 2.8

**Script**

Starting Exercise 2.8 — Terminal Integration. 13 min scheduled.

Let the Agent run terminal commands and react to command output.

The full lab guide with troubleshooting is in slide-exercises/module-02/exercise-2.8-terminal-integration.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: Check the environment:.

Step 2: Approve the command when prompted.

Step 3: List project files:.

Paste this into the Agent — constraints matter as much as the ask: "Run `python --version` and `gcc --version` in PowerShell. Tell me what versions we're using."

Paste this into the Agent — constraints matter as much as the ask: "Run `dir` and tell me which file looks like the main program."

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Command not found: Ask: *"The command `xxx` is not found. How do I install it?"*
- If Permission denied: You may need to approve with `sudo` (be careful!)

---

### Slide 117 — Exercise 2.8 — Agent Terminal Loop

**Type:** exercise · **Lesson:** 2.8 · **Exercise:** 2.8

**Script**

Next step — Agent Terminal Loop.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Command not found: Ask: *"The command `xxx` is not found. How do I install it?"*
- If Permission denied: You may need to approve with `sudo` (be careful!)

---

### Slide 118 — Exercise 2.8 — Step 5: Install Dependency

**Type:** exercise · **Lesson:** 2.8 · **Exercise:** 2.8

**Script**

Next step — Step 5: Install Dependency.

Step 5: Install a dependency (Windows):.

Paste this into the Agent — constraints matter as much as the ask: "Install the requests library with pip if it's not already installed. Use: py -m pip install requests Show me the command output."

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If Command not found: Ask: *"The command `xxx` is not found. How do I install it?"*
- If Permission denied: You may need to approve with `sudo` (be careful!)

---

### Slide 119 — Exercise 2.8 — Step 6: Multi-Step Workflow

**Type:** exercise · **Lesson:** 2.8 · **Exercise:** 2.8

**Script**

Next step — Step 6: Multi-Step Workflow.

Step 6: Multi-step workflow (Windows PowerShell):.

Paste this into the Agent — constraints matter as much as the ask: "Run these commands in order: 1. git status 2. git branch 3. dir Summarize what you see after each command. Confirm before each command that might affect the repo."

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Command not found: Ask: *"The command `xxx` is not found. How do I install it?"*
- If Permission denied: You may need to approve with `sudo` (be careful!)

---

### Slide 120 — Terminal Command Safety Rules

**Type:** table · **Lesson:** 2.8 · **Exercise:** 2.8

**Script**

Next: Terminal Command Safety Rules.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Always approve first: Remove-Item, sudo, git push --force, production changes. Review carefully: pip install, npm install, git branch changes, docker. Safe to auto-approve (Windows demo): python --version, dir, Get-Location, Get-Content, pytest, npm test.

---

### Slide 121 — Module Summary

**Type:** module_summary · **Lesson:** 2.8 · **Exercise:** 2.8

**Script**

That completes Module 2. Lesson 2.1, Codebase Understanding — key insight: Orient to new repo; Lesson 2.2, Explaining Files/Symbols — key insight: Targeted explanations; Lesson 2.3, Safe Reviewable Changes — key insight: Diff review workflow; Lesson 2.4, Plan Mode — key insight: Design before code; Lesson 2.5, Comparing Models — key insight: Model selection; Lesson 2.6, @mentions — key insight: Precise context; Lesson 2.7, Checkpoints — key insight: Safety net; Lesson 2.8, Terminal Integration — key insight: Command execution

What will you do differently on Monday? I will take two or three answers before we break or move on.

---

### Slide 122 — Quick Reference Card

**Type:** quick_reference · **Lesson:** 2.8 · **Exercise:** 2.8

**Script**

This quick reference slide is for you to keep after the course — screenshot it or copy the commands into your team wiki.

Quick Reference Card

**Facilitator notes**

- Allow about two minutes for final questions on this module.

---

## Module 3 — Agent Modes and Tools

### Slide 123 — Agent Modes and Tools

**Type:** module_intro

**Script**

Module 3 connects modes and tools to the mental models from Module 1 — Ask vs Agent, browser, terminal, prompting craft.

Timing on slide: Cursor Training Program · ~60 min

---

### Slide 124 — Module Overview

**Type:** module_overview

**Script**

The module goal in plain language: Master different agent modes and the core tools that make agents powerful

Glance at duration and prerequisites on screen — raise a hand if anything blocks you.

---

### Slide 125 — Learning Objectives

**Type:** learning_objectives

**Script**

These outcomes define success for Module 3 — not a reading list, but skills you will practice.

Highlight three that matter for your role: Choose between Ask Mode and Agent Mode based on task and safety needs; Use the Browser Tool to inspect live pages and read console output; Run terminal commands through the agent and diagnose failures; plus more on screen.

Next: learning objectives.

Ask who has seen the opposite problem in production — one story beats five bullets.

---

### Slide 126 — Agenda

**Type:** module_agenda

**Script**

Here is how we will spend our time: Lesson 3.1, Ask Mode vs. Agent Mode, about 18 min; Lesson 3.2, Browser Tool, about 18 min; Lesson 3.3, Terminal Tool, about 20 min; Lesson 3.4, Effective Prompting in Practice, about 22 min.

**Facilitator notes**

- Announce when the next hands-on block starts so people can close email and open Cursor.

---

### Slide 127 — Lesson 3.1

**Type:** lesson_intro · **Lesson:** 3.1

**Script**

Lesson 3.1: Ask Mode vs. Agent Mode. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Learn when Ask Mode is read-only and when Agent Mode can edit files.

Ask Mode is your safe inspection lane — architecture questions, code reading, no surprise diffs.

Demo the footer toggle live: same question in Ask vs Agent and show that only Agent proposes edits.

Lab reference: slide-exercises/module-03/exercise-3.1-ask-mode-vs-agent-mode.md

---

### Slide 128 — The Core Distinction

**Type:** table · **Lesson:** 3.1

**Script**

Next: The Core Distinction.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Can read files: ✅ Yes (with @mentions). Use this when ✅ Yes. Can edit files: ❌ No. Use this when ✅ Yes. Can run terminal: ❌ No. Use this when ✅ Yes. Can browse web: ❌ No (limited). Use this when ✅ Yes (with tool). Can call tools: ❌ No. Use this when ✅ Yes. Safety level: Very high

---

### Slide 129 — When to Use Each Mode

**Type:** bullets · **Lesson:** 3.1

**Script**

There are 7 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: You have a question about code · Exploring a codebase.

Second: You want a second opinion on design — this one usually matters most in practice.

Also on screen: You're not ready to make changes · Production environment, You want the AI to write/change code….

Next: When to Use Each Mode.

Ask who has seen the opposite problem in production — one story beats five bullets.

USE ASK MODE when: - You have a question about code · Exploring a codebase

---

### Slide 130 — Safety Implications

**Type:** table · **Lesson:** 3.1

**Script**

Next: Safety Implications.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Risk: Ask Mode. Use this when Agent Mode. Unintended code changes: None. Use this when Moderate (requires review). File deletion: None. Use this when Possible (needs approval). Malicious commands: None. Use this when Possible (needs approval). Data leakage: Low. Use this when Med

---

### Slide 131 — The Mode Continuum

**Type:** diagram · **Lesson:** 3.1

**Script**

This slide shows The Mode Continuum.

<img src="assets/module-03/the-mode-continuum.svg" alt="The Mode Continuum" />

Next: The Mode Continuum.

The Mode Continuum

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 132 — Windows Exercise Environment

**Type:** exercise_setup · **Lesson:** 3.1

**Script**

Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

**Facilitator notes**

- Allow two to three minutes. Pair anyone blocked on keys or curl with a neighbor.

---

### Slide 133 — Exercise 3.1 — Steps 1–2

**Type:** exercise · **Lesson:** 3.1 · **Exercise:** 3.1

**Script**

Starting Exercise 3.1 — Ask Mode vs. Agent Mode. 18 min scheduled.

Learn when Ask Mode is read-only and when Agent Mode can edit files.

The full lab guide with troubleshooting is in slide-exercises/module-03/exercise-3.1-ask-mode-vs-agent-mode.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: Open Agent panel (Cmd+I / Ctrl+I) — note mode indicator at bottom.

Where: Agent panel — `Ctrl+I`.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Can't switch modes: Type `/ask` or `/agent` exactly. Use `Shift+Tab` as alternative
- If Agent still makes changes in Ask Mode: You might not be in Ask Mode. Check the mode indicator

---

### Slide 134 — Exercise 3.1 — Steps 1–2 (Part 2)

**Type:** exercise · **Lesson:** 3.1 · **Exercise:** 3.1

**Script**

Next step — Steps 1–2 (Part 2).

Step 2: Try to make a change in Ask Mode:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "Change the variable name 'temp' to 'temperature' in the current file."

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Can't switch modes: Type `/ask` or `/agent` exactly. Use `Shift+Tab` as alternative
- If Agent still makes changes in Ask Mode: You might not be in Ask Mode. Check the mode indicator

---

### Slide 135 — Exercise 3.1 — Steps 3–5

**Type:** exercise · **Lesson:** 3.1 · **Exercise:** 3.1

**Script**

Next step — Steps 3–5.

Step 3: Ask a question Ask Mode handles well:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "Explain the purpose of the main() function in this file. What edge cases does it handle?"

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Can't switch modes: Type `/ask` or `/agent` exactly. Use `Shift+Tab` as alternative
- If Agent still makes changes in Ask Mode: You might not be in Ask Mode. Check the mode indicator

---

### Slide 136 — Exercise 3.1 — Steps 3–5 (Part 2)

**Type:** exercise · **Lesson:** 3.1 · **Exercise:** 3.1

**Script**

Next step — Steps 3–5 (Part 2).

Step 4: Switch to Agent Mode via the dropdown.

Where: Agent panel — `Ctrl+I`.

Step 5: Repeat the rename request — agent shows diff for approval.

Where: Agent panel — `Ctrl+I`.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Can't switch modes: Type `/ask` or `/agent` exactly. Use `Shift+Tab` as alternative
- If Agent still makes changes in Ask Mode: You might not be in Ask Mode. Check the mode indicator

---

### Slide 137 — Exercise 3.1 — Step 6 & Success Criteria

**Type:** exercise · **Lesson:** 3.1 · **Exercise:** 3.1

**Script**

Let's debrief Exercise 3.1 — Ask Mode vs. Agent Mode.

Check off what you actually completed — not what the Agent claimed: Used Ask Mode for questions · Observed Ask Mode cannot make changes; Switched to Agent Mode · Made a change with diff review.

Ask two volunteers: what did the Agent get wrong, and what prompt change fixed it? That reflection is the learning outcome.

**Facilitator notes**

- Common issues: If Can't switch modes: Type `/ask` or `/agent` exactly. Use `Shift+Tab` as alternative; If Agent still makes changes in Ask Mode: You might not be in Ask Mode. Check the mode indicator; If Don't see mode indicator: Look near the chat input – it shows "Ask", "Agent", or "Plan"

---

### Slide 138 — Lesson 3.2

**Type:** lesson_intro · **Lesson:** 3.2

**Script**

Lesson 3.2: Browser Tool. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Use the Browser tool so the Agent can inspect live web pages.

Frontend developers love this — CSS lies, the rendered page does not. The Agent can see what users see.

Caveat: dynamic SPAs may need wait instructions; mention that if the page looks empty in the demo.

Lab reference: slide-exercises/module-03/exercise-3.2-browser-tool.md

---

### Slide 139 — What the Browser Tool Can Do

**Type:** quote · **Lesson:** 3.2

**Script**

Start with the line on screen: "See what your app actually looks like in a browser — not just the source code."

Expand in your own words — do not read the bullet text verbatim: - Navigate to URLs · Read page content and DOM structure - See console logs and errors · Take screenshots (depending on model)

Next: What the Browser Tool Can Do.

Frontend developers love this — CSS lies, the rendered page does not. The Agent can see what users see.

Caveat: dynamic SPAs may need wait instructions; mention that if the page looks empty in the demo.

Pause after the quote — let it land before you add examples.

---

### Slide 140 — Browser Tool: With vs. Without

**Type:** table · **Lesson:** 3.2

**Script**

Next: Browser Tool: With vs. Without.

Frontend developers love this — CSS lies, the rendered page does not. The Agent can see what users see.

Caveat: dynamic SPAs may need wait instructions; mention that if the page looks empty in the demo.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): "Why is the button not showing?": Guesses from CSS. Use this when Sees the rendered page. "Is the API returning data?": Checks code. Use this when Sees network tab. "What console errors?": Asks you. Use this when Reads console directly. "Does responsive layout work?": Trusts CSS.

---

### Slide 141 — Exercise 3.2 — Steps 1–2

**Type:** exercise · **Lesson:** 3.2 · **Exercise:** 3.2

**Script**

Starting Exercise 3.2 — Browser Tool. 18 min scheduled.

Use the Browser tool so the Agent can inspect live web pages.

The full lab guide with troubleshooting is in slide-exercises/module-03/exercise-3.2-browser-tool.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: Start a local web app (or use a public test page).

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "python -m http.server 8000 # Or use a public test page"

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Browser pane doesn't appear: Ask: *"Show me the browser window"* or check Cursor Settings → Features → Browser
- If Page won't load: Check internet connection. Try a different URL

---

### Slide 142 — Exercise 3.2 — Steps 1–2 (Part 2)

**Type:** exercise · **Lesson:** 3.2 · **Exercise:** 3.2

**Script**

Next step — Steps 1–2 (Part 2).

Step 2: In Agent Mode:.

Terminal: PowerShell — `Ctrl+ `` in Cursor.

Paste this into the Agent — constraints matter as much as the ask: "Use the browser tool to open http://localhost:8000 Tell me what you see on the page."

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Browser pane doesn't appear: Ask: *"Show me the browser window"* or check Cursor Settings → Features → Browser
- If Page won't load: Check internet connection. Try a different URL

---

### Slide 143 — Exercise 3.2 — Steps 3–4

**Type:** exercise · **Lesson:** 3.2 · **Exercise:** 3.2

**Script**

Next step — Steps 3–4.

Step 3: Find specific elements:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "On that same page, find: 1. The main heading text 2. The number of buttons 3. Any error messages visible"

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Browser pane doesn't appear: Ask: *"Show me the browser window"* or check Cursor Settings → Features → Browser
- If Page won't load: Check internet connection. Try a different URL

---

### Slide 144 — Exercise 3.2 — Steps 3–4 (Part 2)

**Type:** exercise · **Lesson:** 3.2 · **Exercise:** 3.2

**Script**

Next step — Steps 3–4 (Part 2).

Step 4: Check the console:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "Now open the browser developer console. Are there any errors or warnings? If so, what are they?"

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Browser pane doesn't appear: Ask: *"Show me the browser window"* or check Cursor Settings → Features → Browser
- If Page won't load: Check internet connection. Try a different URL

---

### Slide 145 — Expected Agent Actions

**Type:** diagram · **Lesson:** 3.2 · **Exercise:** 3.2

**Script**

This slide shows Expected Agent Actions.

<img src="assets/module-03/expected-agent-actions.svg" alt="Expected Agent Actions" />

Next: Expected Agent Actions.

Expected Agent Actions

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 146 — Exercise 3.2 — Steps 5–6

**Type:** exercise · **Lesson:** 3.2 · **Exercise:** 3.2

**Script**

Next step — Steps 5–6.

Step 5: Diagnose a layout issue:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "The login button is partially hidden on mobile sizes. Use the browser tool to check what's happening."

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Browser pane doesn't appear: Ask: *"Show me the browser window"* or check Cursor Settings → Features → Browser
- If Page won't load: Check internet connection. Try a different URL

---

### Slide 147 — Exercise 3.2 — Steps 5–6 (Part 2)

**Type:** exercise · **Lesson:** 3.2 · **Exercise:** 3.2

**Script**

Next step — Steps 5–6 (Part 2).

Step 6: Extract data from a page:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "Go to https://example.com/pricing Extract all pricing plan names and their monthly costs into a table."

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Browser pane doesn't appear: Ask: *"Show me the browser window"* or check Cursor Settings → Features → Browser
- If Page won't load: Check internet connection. Try a different URL

---

### Slide 148 — Browser Tool Limitations

**Type:** table · **Lesson:** 3.2 · **Exercise:** 3.2

**Script**

Next: Browser Tool Limitations.

Frontend developers love this — CSS lies, the rendered page does not. The Agent can see what users see.

Caveat: dynamic SPAs may need wait instructions; mention that if the page looks empty in the demo.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Cannot log in to sites: Provide login instructions or session cookies. JavaScript-heavy sites may load slowly: Add wait instructions. Rate limits on some sites: Space out requests. Cannot upload files: Not supported yet.

---

### Slide 149 — Lesson 3.3

**Type:** lesson_intro · **Lesson:** 3.3

**Script**

Lesson 3.3: Terminal Tool. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Use the Terminal tool to run tests, read output, and fix failures.

This closes the loop: tests and builds become ground truth. The Agent should read stderr, not invent success.

Windows note: prefer `.un_tests.bat` and `curl.exe` — say that once, not every slide.

Lab reference: slide-exercises/module-03/exercise-3.3-terminal-tool.md

---

### Slide 150 — What the Terminal Tool Can Do

**Type:** bullets · **Lesson:** 3.3

**Script**

There are 4 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Run any shell command (with approval).

Second: See stdout, stderr, exit codes — this one usually matters most in practice.

Also on screen: Read command output as context for next actions, Chain commands based on previous results.

Next: What the Terminal Tool Can Do.

This closes the loop: tests and builds become ground truth. The Agent should read stderr, not invent success.

Windows note: prefer `.un_tests.bat` and `curl.exe` — say that once, not every slide.

Ask who has seen the opposite problem in production — one story beats five bullets.

- Run any shell command (with approval) - See stdout, stderr, exit codes

---

### Slide 151 — Terminal Tool Flow

**Type:** diagram · **Lesson:** 3.3

**Script**

This slide shows Terminal Tool Flow.

<img src="assets/module-03/terminal-tool-flow.svg" alt="Terminal Tool Flow" />

Next: Terminal Tool Flow.

This closes the loop: tests and builds become ground truth. The Agent should read stderr, not invent success.

Windows note: prefer `.un_tests.bat` and `curl.exe` — say that once, not every slide.

On screen: Terminal Tool Flow

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 152 — Exercise 3.3 — Setup

**Type:** exercise · **Lesson:** 3.3 · **Exercise:** 3.3

**Script**

Starting Exercise 3.3 — Terminal Tool. 20 min scheduled.

Use the Terminal tool to run tests, read output, and fix failures.

The full lab guide with troubleshooting is in slide-exercises/module-03/exercise-3.3-terminal-tool.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Break the test on purpose if the lab says so — the Agent should read failing output, not guess.

If tests pass immediately, ask what command the Agent ran and whether output matched stderr/stdout.

Goal for this step: Use the terminal tool on the calculator test project in this repo.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If `gcc: command not found`: Install GCC, or ask Agent for install steps for your OS
- If Agent won't run command: Click **Allow** / **Run** when the approval dialog appears

---

### Slide 153 — Exercise 3.3 — Step 1: Safe Command

**Type:** exercise · **Lesson:** 3.3 · **Exercise:** 3.3

**Script**

Next step — Step 1: Safe Command.

Goal for this step: Learn which commands usually need careful review.

Step 1 — Read-only command.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "Check whether gcc and git are available. Run gcc --version and git --version. Summarize the output. Do not modify any files."

Break the test on purpose if the lab says so — the Agent should read failing output, not guess.

If tests pass immediately, ask what command the Agent ran and whether output matched stderr/stdout.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If `gcc: command not found`: Install GCC, or ask Agent for install steps for your OS
- If Agent won't run command: Click **Allow** / **Run** when the approval dialog appears

---

### Slide 154 — Exercise 3.3 — Step 2: Run Passing Tests

**Type:** exercise · **Lesson:** 3.3 · **Exercise:** 3.3

**Script**

Next step — Step 2: Run Passing Tests.

Goal for this step: Compile and run tests — all should pass first.

A good result looks like: Four PASS: lines · All tests passed!

Step 2 — Run test suite.

Paste this into the Agent — constraints matter as much as the ask: "Run .\run_tests.bat in this folder. Show full output: compilation OK? how many tests passed?"

Break the test on purpose if the lab says so — the Agent should read failing output, not guess.

If tests pass immediately, ask what command the Agent ran and whether output matched stderr/stdout.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If `gcc: command not found`: Install GCC, or ask Agent for install steps for your OS
- If Agent won't run command: Click **Allow** / **Run** when the approval dialog appears

---

### Slide 155 — Exercise 3.3 — Step 3: Break a Test

**Type:** exercise · **Lesson:** 3.3 · **Exercise:** 3.3

**Script**

Next step — Step 3: Break a Test.

Goal for this step: Compile and run tests — all should pass first.

A good result looks like: Four PASS: lines · All tests passed!

Step 3 — Introduce a failure (you edit).

Break the test on purpose if the lab says so — the Agent should read failing output, not guess.

If tests pass immediately, ask what command the Agent ran and whether output matched stderr/stdout.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If `gcc: command not found`: Install GCC, or ask Agent for install steps for your OS
- If Agent won't run command: Click **Allow** / **Run** when the approval dialog appears

---

### Slide 156 — Exercise 3.3 — Step 4: Diagnose Failure

**Type:** exercise · **Lesson:** 3.3 · **Exercise:** 3.3

**Script**

Next step — Step 4: Diagnose Failure.

Goal for this step: Use the terminal tool on the calculator test project in this repo.

Step 4 — Read terminal output.

Paste this into the Agent — constraints matter as much as the ask: "@test_calculator.c Run the test suite again. Which test failed? What assertion failed? Is the bug in the test or in add()? Explain only — do not fix yet."

Keep @calculator.c in the prompt so the Agent cannot wander to other files.

Break the test on purpose if the lab says so — the Agent should read failing output, not guess.

If tests pass immediately, ask what command the Agent ran and whether output matched stderr/stdout.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If `gcc: command not found`: Install GCC, or ask Agent for install steps for your OS
- If Agent won't run command: Click **Allow** / **Run** when the approval dialog appears

---

### Slide 157 — Exercise 3.3 — Step 5: Fix and Verify

**Type:** exercise · **Lesson:** 3.3 · **Exercise:** 3.3

**Script**

Next step — Step 5: Fix and Verify.

Goal for this step: Use the terminal tool on the calculator test project in this repo.

Step 5 — Debug workflow.

Paste this into the Agent — constraints matter as much as the ask: "@test_calculator.c 1. Run tests and confirm the failure 2. Fix the incorrect assertion in test_add() only 3. Re-run tests and confirm all pass Show the diff before I accept changes."

Keep @calculator.c in the prompt so the Agent cannot wander to other files.

Break the test on purpose if the lab says so — the Agent should read failing output, not guess.

If tests pass immediately, ask what command the Agent ran and whether output matched stderr/stdout.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If `gcc: command not found`: Install GCC, or ask Agent for install steps for your OS
- If Agent won't run command: Click **Allow** / **Run** when the approval dialog appears

---

### Slide 158 — Exercise 3.3 — Step 6: Approval Rules

**Type:** exercise · **Lesson:** 3.3 · **Exercise:** 3.3

**Script**

Next step — Step 6: Approval Rules.

Goal for this step: Use the terminal tool on the calculator test project in this repo.

Step 6 — Safe vs. risky commands.

Paste this into the Agent — constraints matter as much as the ask: "Run git status. Summarize only — do not commit or push."

Break the test on purpose if the lab says so — the Agent should read failing output, not guess.

If tests pass immediately, ask what command the Agent ran and whether output matched stderr/stdout.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If `gcc: command not found`: Install GCC, or ask Agent for install steps for your OS
- If Agent won't run command: Click **Allow** / **Run** when the approval dialog appears

---

### Slide 159 — Lesson 3.4

**Type:** lesson_intro · **Lesson:** 3.4

**Script**

Lesson 3.4: Effective Prompting in Practice. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Write constrained prompts and reusable templates for real tasks.

The through-line: vague prompts produce vague, wide diffs. Constraints — files, functions, output format — shrink the blast radius.

Exercise 3.4 on calculator.c is deliberately small so you can see how one vague sentence refactors half the file.

Lab reference: slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md

---

### Slide 160 — Anatomy of an Effective Prompt

**Type:** content · **Lesson:** 3.4

**Script**

Next: Anatomy of an Effective Prompt.

1. ROLE / CONTEXT — "You are a senior Python developer…" 2. TASK — "Fix the bug in calculate_total()…" 3. CONSTRAINTS — "Do not change the function signature…" 4. OUTPUT FORMAT — "Show me the… (see slide)

---

### Slide 161 — Bad Prompts vs. Good Prompts

**Type:** table · **Lesson:** 3.4

**Script**

Next: Bad Prompts vs. Good Prompts.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): "Fix this code": "Fix the IndexError in process_list() when list is empty. Do not change return type.". @calculator.c Fix divide: @calculator.c Improve divide() for division by zero. Change ONLY divide(). Show diff + cause.. "Add logging": "Add INFO-level logging to calculate() u

---

### Slide 162 — The "Boundaries" Technique

**Type:** code · **Lesson:** 3.4

**Script**

Always tell the agent what NOT to touch:

Focus on the first few lines — for example: BOUNDARIES:.

Next: The "Boundaries" Technique.

---

### Slide 163 — Avoiding Scope Creep

**Type:** table · **Lesson:** 3.4

**Script**

Next: Avoiding Scope Creep.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Explicit boundaries: "Change ONLY login.js lines 42–56". One thing at a time: "First, just identify the issue. Don't fix yet.". Ask for plan first: "Plan Mode: Show me what you'll change before doing it". Use checkpoints: Create checkpoint before complex requests. Prefer diffs: "

---

### Slide 164 — Exercise 3.4 — Setup

**Type:** exercise · **Lesson:** 3.4 · **Exercise:** 3.4

**Script**

Starting Exercise 3.4 — Effective Prompting in Practice. 22 min scheduled.

Write constrained prompts and reusable templates for real tasks.

The full lab guide with troubleshooting is in slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 2's vague prompt is the lesson — expect a wide diff. Step 1's constrained prompt should touch only divide().

Use @calculator.c every time; without it the Agent may edit the wrong file.

Goal for this step: Practice six prompting techniques on calculator.c from earlier exercises.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If Agent changes too many files: Add *"Change ONLY [function/file]."* Reject the diff and retry.
- If Agent edits when you wanted a plan: Switch to `/ask` or add *"Do not edit files yet."*

---

### Slide 165 — Exercise 3.4 — Step 1: Constrained Prompt

**Type:** exercise · **Lesson:** 3.4 · **Exercise:** 3.4

**Script**

Next step — Step 1: Constrained Prompt.

Goal for this step: Task + boundaries + output format + success criteria.

A good result looks like: Diff limited to divide() — not a full refactor.

Step 1 — Constrained prompt.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "@calculator.c Task: Improve divide() so it handles division by zero safely inside the function itself. Constraints: - Do NOT change any function signatures - Do NOT add new #include lines - Do NOT modify main() or other functions - Change ONLY the divide() function body Output format: Show the exact diff and explain the root cause in 2–3 sentences. Success criteria: divide(10, 0) returns safely; divide(10, 2) still returns 5."

Keep @calculator.c in the prompt so the Agent cannot wander to other files.

Step 2's vague prompt is the lesson — expect a wide diff. Step 1's constrained prompt should touch only divide().

Use @calculator.c every time; without it the Agent may edit the wrong file.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If Agent changes too many files: Add *"Change ONLY [function/file]."* Reject the diff and retry.
- If Agent edits when you wanted a plan: Switch to `/ask` or add *"Do not edit files yet."*

---

### Slide 166 — Exercise 3.4 — Step 2: Vague vs. Constrained

**Type:** exercise · **Lesson:** 3.4 · **Exercise:** 3.4

**Script**

Next step — Step 2: Vague vs. Constrained.

Goal for this step: Task + boundaries + output format + success criteria.

A good result looks like: Diff limited to divide() — not a full refactor.

Step 2 — Vague vs. constrained.

Paste this into the Agent — constraints matter as much as the ask: "@calculator.c Fix the divide function."

Keep @calculator.c in the prompt so the Agent cannot wander to other files.

Step 2's vague prompt is the lesson — expect a wide diff. Step 1's constrained prompt should touch only divide().

Use @calculator.c every time; without it the Agent may edit the wrong file.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If Agent changes too many files: Add *"Change ONLY [function/file]."* Reject the diff and retry.
- If Agent edits when you wanted a plan: Switch to `/ask` or add *"Do not edit files yet."*

---

### Slide 167 — Exercise 3.4 — Step 3: Plan Before Editing

**Type:** exercise · **Lesson:** 3.4 · **Exercise:** 3.4

**Script**

Next step — Step 3: Plan Before Editing.

Goal for this step: Approve a plan before any file changes.

A good result looks like: Written plan, no diff until you approve.

Step 3 — Plan before editing.

Where: Ask Mode (/ask) or Agent with "do not edit yet".

Paste this into the Agent — constraints matter as much as the ask: "@calculator.c Before making any changes, answer: 1. What is the smallest change needed for divide()? 2. Which lines would you change? 3. What could go wrong? 4. What will you NOT change? Do not edit files yet — I will review first."

Keep @calculator.c in the prompt so the Agent cannot wander to other files.

Step 2's vague prompt is the lesson — expect a wide diff. Step 1's constrained prompt should touch only divide().

Use @calculator.c every time; without it the Agent may edit the wrong file.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Agent changes too many files: Add *"Change ONLY [function/file]."* Reject the diff and retry.
- If Agent edits when you wanted a plan: Switch to `/ask` or add *"Do not edit files yet."*

---

### Slide 168 — Exercise 3.4 — Step 4: DO NOT List

**Type:** exercise · **Lesson:** 3.4 · **Exercise:** 3.4

**Script**

Next step — Step 4: DO NOT List.

Goal for this step: Forbid scope creep explicitly.

A good result looks like: Comment only — no logic changes.

Step 4 — DO NOT list.

Paste this into the Agent — constraints matter as much as the ask: "@calculator.c Add a one-line comment above divide() explaining it performs integer division. DO NOT: - Change any function bodies - Rename functions - Add new functions - Modify main()"

Keep @calculator.c in the prompt so the Agent cannot wander to other files.

Step 2's vague prompt is the lesson — expect a wide diff. Step 1's constrained prompt should touch only divide().

Use @calculator.c every time; without it the Agent may edit the wrong file.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Agent changes too many files: Add *"Change ONLY [function/file]."* Reject the diff and retry.
- If Agent edits when you wanted a plan: Switch to `/ask` or add *"Do not edit files yet."*

---

### Slide 169 — Exercise 3.4 — Step 5: One Change at a Time

**Type:** exercise · **Lesson:** 3.4 · **Exercise:** 3.4

**Script**

Next step — Step 5: One Change at a Time.

Goal for this step: Two messages — propose, then apply.

A good result looks like: Message 1 = no edit · Message 2 = small diff.

Step 5 — One change at a time.

Paste this into the Agent — constraints matter as much as the ask: "@calculator.c Show me the validation you would add inside divide() for division by zero. Do not edit the file yet."

Keep @calculator.c in the prompt so the Agent cannot wander to other files.

Paste this into the Agent — constraints matter as much as the ask: "Now add only that validation to divide(). Show the diff before I accept. Do not change main() or other functions."

Step 2's vague prompt is the lesson — expect a wide diff. Step 1's constrained prompt should touch only divide().

Use @calculator.c every time; without it the Agent may edit the wrong file.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Agent changes too many files: Add *"Change ONLY [function/file]."* Reject the diff and retry.
- If Agent edits when you wanted a plan: Switch to `/ask` or add *"Do not edit files yet."*

---

### Slide 170 — Exercise 3.4 — Step 6: Prompt Templates

**Type:** exercise · **Lesson:** 3.4 · **Exercise:** 3.4

**Script**

Next step — Step 6: Prompt Templates.

Goal for this step: Create prompts you can copy on real projects.

Step 6 — Prompt templates.

Paste this into the Agent — constraints matter as much as the ask: "## Bug Fix Template @{{file}} Task: [Describe bug] Constraints: Do NOT change [signatures / other files] Output: Show diff + root cause Success: [How to verify] ## Plan-First Template @{{file}} Before editing: list files, risks, and what you will NOT touch. Wait for my approval. ## Small Change Template @{{file}} Change ONLY: [function or lines] DO NOT: [forbidden changes] Show diff before applying."

Step 2's vague prompt is the lesson — expect a wide diff. Step 1's constrained prompt should touch only divide().

Use @calculator.c every time; without it the Agent may edit the wrong file.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Agent changes too many files: Add *"Change ONLY [function/file]."* Reject the diff and retry.
- If Agent edits when you wanted a plan: Switch to `/ask` or add *"Do not edit files yet."*

---

### Slide 171 — Module Summary

**Type:** module_summary · **Lesson:** 3.4 · **Exercise:** 3.4

**Script**

That completes Module 3. Lesson 3.1, Ask vs Agent Mode — key insight: Use Ask for questions, Agent for action; Lesson 3.2, Browser Tool — key insight: Agent can see live pages and console; Lesson 3.3, Terminal Tool — key insight: Agent can run commands and react; Lesson 3.4, Effective Prompting — key insight: Boundaries prevent scope creep

What will you do differently on Monday? I will take two or three answers before we break or move on.

---

### Slide 172 — Quick Reference Card

**Type:** quick_reference · **Lesson:** 3.4 · **Exercise:** 3.4

**Script**

This quick reference slide is for you to keep after the course — screenshot it or copy the commands into your team wiki.

Quick Reference Card

**Facilitator notes**

- Allow about two minutes for final questions on this module.

---

## Module 4 — Customizing Cursor for Your Team

### Slide 173 — Customizing Cursor for Your Team

**Type:** module_intro

**Script**

Module 4 is about scaling Cursor across a team — rules travel with the repo, skills encode repeat workflows.

Timing on slide: Cursor Training Program · ~60 min

---

### Slide 174 — Module Overview

**Type:** module_overview

**Script**

The module goal in plain language: Customize Cursor for team workflows with rules, skills, MCP, and subagents

Glance at duration and prerequisites on screen — raise a hand if anything blocks you.

---

### Slide 175 — Learning Objectives

**Type:** learning_objectives

**Script**

These outcomes define success for Module 4 — not a reading list, but skills you will practice.

Highlight three that matter for your role: Create Rules that encode team conventions and guardrails; Write Repository Instructions for lightweight project guidance; Build and invoke reusable Skills for specialized workflows; plus more on screen.

Next: learning objectives.

Ask who has seen the opposite problem in production — one story beats five bullets.

---

### Slide 176 — Agenda

**Type:** module_agenda

**Script**

Here is how we will spend our time: Lesson 4.1, Creating a Rule, about 20 min; Lesson 4.2, Repository Instructions, about 13 min; Lesson 4.3, Creating and Invoking a Skill, about 20 min; Lesson 4.4, MCP, Hooks, and Slash Workflows, about 10 min; Lesson 4.5, Subagents, about 6 min.

**Facilitator notes**

- Announce when the next hands-on block starts so people can close email and open Cursor.

---

### Slide 177 — Lesson 4.1

**Type:** lesson_intro · **Lesson:** 4.1

**Script**

Lesson 4.1: Creating a Rule. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Create Cursor rules that persist coding standards for your team.

Team leverage slide: rules and AGENTS.md scale your standards without repeating them in every prompt.

Who owns these on a real team? Usually tech lead or platform — not every developer inventing their own.

Lab reference: slide-exercises/module-04/exercise-4.1-creating-a-rule.md

---

### Slide 178 — What Are Rules?

**Type:** table · **Lesson:** 4.1

**Script**

Next: What Are Rules?.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Rule Type: Scope. Use this when When Applied. Global: All projects. Use this when Always. Project: Specific repo. Use this when When opening that project. File pattern: Matching files. Use this when When editing those files. User: Your account. Use this when Always across all pro

---

### Slide 179 — Rule Structure

**Type:** code · **Lesson:** 4.1

**Script**

Rule Structure

Next: Rule Structure.

---

### Slide 180 — description: Brief description of what this rule does globs: .py, src//.js alway…

**Type:** content · **Lesson:** 4.1

**Script**

Next: description: Brief description of what this rule does globs: .py, src//.js alway….

description: Brief description of what this rule does globs: .py, src//.js alwaysApply: true

---

### Slide 181 — Rule Title

**Type:** code · **Lesson:** 4.1

**Script**

Write your instructions here in natural language. Good: ...  Bad: ...

Next: Rule Title.

---

### Slide 182 — Windows Exercise Environment

**Type:** exercise_setup · **Lesson:** 4.1

**Script**

Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

**Facilitator notes**

- Allow two to three minutes. Pair anyone blocked on keys or curl with a neighbor.

---

### Slide 183 — Exercise 4.1 — Step 1: Setup

**Type:** exercise · **Lesson:** 4.1 · **Exercise:** 4.1

**Script**

Starting Exercise 4.1 — Creating a Rule. 20 min scheduled.

Create Cursor rules that persist coding standards for your team.

The full lab guide with troubleshooting is in slide-exercises/module-04/exercise-4.1-creating-a-rule.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Paste this into the Agent — constraints matter as much as the ask: "mkdir -p .cursor/rules"

Paste this into the Agent — constraints matter as much as the ask: "globs: **/*.{js,ts,py} | alwaysApply: true Python: type hints, Black (88 chars), Google docstrings JS/TS: const over let, arrow functions, optional chaining General: no commented-out code, no console.log in prod"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If Rule not being applied: Check that `alwaysApply: true` is set correctly
- If Agent ignores the rule: Restart Cursor to reload rules

---

### Slide 184 — Exercise 4.1 — Build & Test Rule

**Type:** exercise · **Lesson:** 4.1 · **Exercise:** 4.1

**Script**

Next step — Build & Test Rule.

Paste this into the Agent — constraints matter as much as the ask: "Before changes: git status, git diff After changes: make test / pytest / npm test → make lint Do NOT suggest changes that break tests or need undocumented API keys"

Paste this into the Agent — constraints matter as much as the ask: "Never: hardcoded secrets, eval() on user input, SQL concatenation Always: input validation, rate limiting, HTTPS, safe error messages Flag: exec/eval with user input, password/secret in variable names"

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Rule not being applied: Check that `alwaysApply: true` is set correctly
- If Agent ignores the rule: Restart Cursor to reload rules

---

### Slide 185 — Exercise 4.1 — Test & File-Specific Rules

**Type:** exercise · **Lesson:** 4.1 · **Exercise:** 4.1

**Script**

Next step — Test & File-Specific Rules.

Step 5: Verify rules are applied:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "Based on the project rules, what are the coding standards I should follow? What are the security guardrails?"

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Rule not being applied: Check that `alwaysApply: true` is set correctly
- If Agent ignores the rule: Restart Cursor to reload rules

---

### Slide 186 — Exercise 4.1 — Test & File-Specific Rules (Part 2)

**Type:** exercise · **Lesson:** 4.1 · **Exercise:** 4.1

**Script**

Next step — Test & File-Specific Rules (Part 2).

Step 6: Create .cursor/rules/react-components.mdc for */.jsx, */.tsx:.

Where: Agent panel — `Ctrl+I`.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Rule not being applied: Check that `alwaysApply: true` is set correctly
- If Agent ignores the rule: Restart Cursor to reload rules

---

### Slide 187 — Lesson 4.2

**Type:** lesson_intro · **Lesson:** 4.2

**Script**

Lesson 4.2: Repository Instructions. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Add repository instructions the Agent reads automatically.

Team leverage slide: rules and AGENTS.md scale your standards without repeating them in every prompt.

Who owns these on a real team? Usually tech lead or platform — not every developer inventing their own.

Lab reference: slide-exercises/module-04/exercise-4.2-repository-instructions.md

---

### Slide 188 — Rules vs. Repository Instructions

**Type:** table · **Lesson:** 4.2

**Script**

Next: Rules vs. Repository Instructions.

Team leverage slide: rules and AGENTS.md scale your standards without repeating them in every prompt.

Who owns these on a real team? Usually tech lead or platform — not every developer inventing their own.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Location: .cursor/rules/*.mdc. Use this when .cursor/repository-instructions.md. Complexity: Multiple files, scoped. Use this when Single file, global. Granularity: Per-file patterns. Use this when Entire repository. Use case: Detailed standards. Use this when High-level project 

---

### Slide 189 — Repository Instructions Structure

**Type:** code · **Lesson:** 4.2

**Script**

Repository Instructions Structure

The important lines are: .

Next: Repository Instructions Structure.

Team leverage slide: rules and AGENTS.md scale your standards without repeating them in every prompt.

Who owns these on a real team? Usually tech lead or platform — not every developer inventing their own.

---

### Slide 190 — Exercise 4.2 — Create Instructions

**Type:** exercise · **Lesson:** 4.2 · **Exercise:** 4.2

**Script**

Starting Exercise 4.2 — Repository Instructions. 13 min scheduled.

Add repository instructions the Agent reads automatically.

The full lab guide with troubleshooting is in slide-exercises/module-04/exercise-4.2-repository-instructions.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Agent ignores AGENTS.md: Make sure file is named exactly `AGENTS.md` (case-sensitive)
- If File not found: Place it in the root of your project (same level as .cursor folder)

---

### Slide 191 — Exercise 4.2 — Verify & Maintain

**Type:** exercise · **Lesson:** 4.2 · **Exercise:** 4.2

**Script**

Next step — Verify & Maintain.

Step 2: Ask the Agent:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "What are the key technologies used in this project? How do I run the tests?"

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Agent ignores AGENTS.md: Make sure file is named exactly `AGENTS.md` (case-sensitive)
- If File not found: Place it in the root of your project (same level as .cursor folder)

---

### Slide 192 — Exercise 4.2 — Verify & Maintain (Part 2)

**Type:** exercise · **Lesson:** 4.2 · **Exercise:** 4.2

**Script**

Next step — Verify & Maintain (Part 2).

Step 3: Update instructions when:.

Where: Agent panel — `Ctrl+I`.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Agent ignores AGENTS.md: Make sure file is named exactly `AGENTS.md` (case-sensitive)
- If File not found: Place it in the root of your project (same level as .cursor folder)

---

### Slide 193 — Lesson 4.3

**Type:** lesson_intro · **Lesson:** 4.3

**Script**

Lesson 4.3: Creating and Invoking a Skill. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Build and invoke reusable Agent skills for repeated workflows.

Team leverage slide: rules and AGENTS.md scale your standards without repeating them in every prompt.

Who owns these on a real team? Usually tech lead or platform — not every developer inventing their own.

Lab reference: slide-exercises/module-04/exercise-4.3-creating-and-invoking-a-skill.md

---

### Slide 194 — What Is a Skill?

**Type:** diagram · **Lesson:** 4.3

**Script**

This slide shows What Is a Skill?.

A reusable, specialized workflow the agent loads and follows — a "prompt template with memory." <img src="assets/module-04/what-is-a-skill.svg" alt="What Is a Skill?" />

Next: What Is a Skill?.

Team leverage slide: rules and AGENTS.md scale your standards without repeating them in every prompt.

Who owns these on a real team? Usually tech lead or platform — not every developer inventing their own.

On screen: What Is a Skill?

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 195 — Exercise 4.3 — PR Review Skill

**Type:** exercise · **Lesson:** 4.3 · **Exercise:** 4.3

**Script**

Starting Exercise 4.3 — Creating and Invoking a Skill. 20 min scheduled.

Build and invoke reusable Agent skills for repeated workflows.

The full lab guide with troubleshooting is in slide-exercises/module-04/exercise-4.3-creating-and-invoking-a-skill.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Paste this into the Agent — constraints matter as much as the ask: "name: pr-review description: Review a PR for code quality, security, and team standards Step 1: Fetch diff (git fetch + git diff main...FETCH_HEAD) Step 2: Review — code quality, security, testing, docs, style Step 3: Output formatted review with Critical / Warning / Suggestion Verdict: APPROVE / REQUEST CHANGES / COMMENT"

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If Skill not recognized: Check file path: `.cursor/skills/skill-name/SKILL.md`
- If Agent ignores skill: Invoke manually: `/skill-name` or "Use the [name] skill"

---

### Slide 196 — Exercise 4.3 — Security Audit Skill

**Type:** exercise · **Lesson:** 4.3 · **Exercise:** 4.3

**Script**

Next step — Security Audit Skill.

Paste this into the Agent — constraints matter as much as the ask: "Scan for: Critical: hardcoded secrets, SQL injection, command injection, eval() Medium: no input validation, weak crypto, missing CSRF Low: debug endpoints, verbose errors, outdated deps Output: report with line numbers, fix suggestions, overall risk rating"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If Skill not recognized: Check file path: `.cursor/skills/skill-name/SKILL.md`
- If Agent ignores skill: Invoke manually: `/skill-name` or "Use the [name] skill"

---

### Slide 197 — Exercise 4.3 — Invoke Skills

**Type:** exercise · **Lesson:** 4.3 · **Exercise:** 4.3

**Script**

Next step — Invoke Skills.

Step 4: Invoke via slash command:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "/pr-review PR #42 /pr-review feature/payment-integration"

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Skill not recognized: Check file path: `.cursor/skills/skill-name/SKILL.md`
- If Agent ignores skill: Invoke manually: `/skill-name` or "Use the [name] skill"

---

### Slide 198 — Exercise 4.3 — Invoke Skills (Part 2)

**Type:** exercise · **Lesson:** 4.3 · **Exercise:** 4.3

**Script**

Next step — Invoke Skills (Part 2).

Step 5: List available skills:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "What skills are available in this project?"

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Skill not recognized: Check file path: `.cursor/skills/skill-name/SKILL.md`
- If Agent ignores skill: Invoke manually: `/skill-name` or "Use the [name] skill"

---

### Slide 199 — Exercise 4.3 — Invoke Skills (Part 3)

**Type:** exercise · **Lesson:** 4.3 · **Exercise:** 4.3

**Script**

Next step — Invoke Skills (Part 3).

Step 6: Create Onboarding skill — generates setup checklist from repo instructions.

Where: Agent panel — `Ctrl+I`.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Skill not recognized: Check file path: `.cursor/skills/skill-name/SKILL.md`
- If Agent ignores skill: Invoke manually: `/skill-name` or "Use the [name] skill"

---

### Slide 200 — Lesson 4.4

**Type:** lesson_intro · **Lesson:** 4.4

**Script**

Lesson 4.4: MCP, Hooks, and Slash Workflows. Participation: listen, participate, or follow along as indicated on the next slides.

MCP is plumbing: one standard way to plug databases, browsers, and internal services into Cursor without custom hacks per vendor.

You will see MCP again in team customization — rules tell the model how to behave; MCP gives it new hands.

---

### Slide 201 — What Is MCP?

**Type:** diagram · **Lesson:** 4.4

**Script**

This slide shows What Is MCP?.

MCP connects Cursor to external systems through a standard protocol so tools stay outside the model but still appear in the agent loop.

Next: What Is MCP?.

MCP is plumbing: one standard way to plug databases, browsers, and internal services into Cursor without custom hacks per vendor.

You will see MCP again in team customization — rules tell the model how to behave; MCP gives it new hands.

On screen: What Is MCP?

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 202 — Hooks & Slash Workflows

**Type:** table · **Lesson:** 4.4

**Script**

Next: Hooks & Slash Workflows.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Hook: When It Runs. Use this when Use Case. pre-tool-use: Before tool call. Use this when Validate permissions, log. post-tool-use: After tool returns. Use this when Transform results, audit. pre-prompt: Before sending to model. Use this when Inject context, redact secrets. post-

---

### Slide 203 — Walkthrough: MCP Configuration

**Type:** walkthrough · **Lesson:** 4.4

**Script**

In this walkthrough we will look at MCP Configuration. Create ~/.cursor/mcp.json: Watch where this lives in Cursor or in the repository — that location matters as much as the content.

---

### Slide 204 — Walkthrough: Slash Command Example

**Type:** walkthrough · **Lesson:** 4.4

**Script**

In this walkthrough we will look at Slash Command Example. Create .cursor/commands/deploy.md: <img src="assets/module-04/walkthrough-slash-command-example.svg" alt="Walkthrough: Slash Command Example" /> Usage: /deploy staging Success Criteria: Understood MCP, hooks, slash commands · saw configuration examples Watch where this lives in Cursor or in the repository — that location matters as much as the content.

---

### Slide 205 — Lesson 4.5

**Type:** lesson_intro · **Lesson:** 4.5

**Script**

Lesson 4.5: Subagents. Participation: listen, participate, or follow along as indicated on the next slides.

---

### Slide 206 — What Are Subagents?

**Type:** diagram · **Lesson:** 4.5

**Script**

This slide shows What Are Subagents?.

Independent agent instances for specialized tasks — own context, tools, and instructions — then report back to the main agent. <img src="assets/module-04/what-are-subagents.svg" alt="What Are Subagents?" />

Next: What Are Subagents?.

What Are Subagents?

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 207 — When to Use Subagents

**Type:** table · **Lesson:** 4.5

**Script**

Next: When to Use Subagents.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Parallel work: Multiple tasks simultaneously. Use this when Scan security AND generate docs. Isolation: Separate context. Use this when Analyze large file independently. Specialization: Different instructions. Use this when Security expert vs. UI designer. Sandboxing: Limit tool 

---

### Slide 208 — Subagent vs. Tool vs. Skill

**Type:** table · **Lesson:** 4.5

**Script**

Next: Subagent vs. Tool vs. Skill.

Team leverage slide: rules and AGENTS.md scale your standards without repeating them in every prompt.

Who owns these on a real team? Usually tech lead or platform — not every developer inventing their own.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Tool: Single action (read file, run command). Skill: Multi-step workflow, same context. Subagent: Parallel, isolated, specialized work.

---

### Slide 209 — Walkthrough: Subagents in Action

**Type:** walkthrough · **Lesson:** 4.5

**Script**

In this walkthrough we will look at Subagents in Action. Task: "Review codebase for security issues and generate API documentation" Without subagents: Mixed context, sequential, slower With subagents (parallel): Invoke: Success Criteria: Understood concept · parallel execution · recognized templates Watch where this lives in Cursor or in the repository — that location matters as much as the content.

---

### Slide 210 — Module Summary

**Type:** module_summary · **Lesson:** 4.5

**Script**

That completes Module 4. Lesson 4.1, Creating a Rule — key insight: .cursor/rules/*.mdc files; Lesson 4.2, Repository Instructions — key insight: .cursor/repository-instructions.md; Lesson 4.3, Creating Skills — key insight: .cursor/skills/*/SKILL.md; Lesson 4.4, MCP & Slash Commands — key insight: MCP config, slash commands; Lesson 4.5, Subagents — key insight: Understanding of delegation

What will you do differently on Monday? I will take two or three answers before we break or move on.

---

### Slide 211 — Quick Reference Card

**Type:** quick_reference · **Lesson:** 4.5

**Script**

This quick reference slide is for you to keep after the course — screenshot it or copy the commands into your team wiki.

Quick Reference Card

**Facilitator notes**

- Allow about two minutes for final questions on this module.

---

## Module 5 — Cursor CLI and Local Automation

### Slide 212 — Cursor CLI and Local Automation

**Type:** module_intro

**Script**

Module 5 moves automation to the terminal — same agent brain, different interface for scripts and CI.

Timing on slide: Cursor Training Program · ~60 min

---

### Slide 213 — Module Overview

**Type:** module_overview

**Script**

The module goal in plain language: Master the Cursor CLI for terminal-based AI workflows and automation

Glance at duration and prerequisites on screen — raise a hand if anything blocks you.

---

### Slide 214 — Learning Objectives

**Type:** learning_objectives

**Script**

These outcomes define success for Module 5 — not a reading list, but skills you will practice.

Highlight three that matter for your role: Use the Cursor CLI in interactive mode for real-time AI collaboration; Run one-shot CLI commands for scripting and CI/CD integration; Hand off local sessions to Cloud Agents for remote execution; plus more on screen.

Next: learning objectives.

Ask who has seen the opposite problem in production — one story beats five bullets.

---

### Slide 215 — Agenda

**Type:** module_agenda

**Script**

Here is how we will spend our time: Lesson 5.1, Interactive CLI, about 20 min; Lesson 5.2, One-Shot CLI, about 20 min; Lesson 5.3, Cloud Handoff, about 18 min; Lesson 5.4, Listing and Resuming Sessions, about 20 min.

**Facilitator notes**

- Announce when the next hands-on block starts so people can close email and open Cursor.

---

### Slide 216 — Lesson 5.1

**Type:** lesson_intro · **Lesson:** 5.1

**Script**

Lesson 5.1: Interactive CLI. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Start an interactive Cursor CLI session from the terminal.

Lab reference: slide-exercises/module-05/exercise-5.1-interactive-cli.md

---

### Slide 217 — What Is the Cursor CLI?

**Type:** bullets · **Lesson:** 5.1

**Script**

There are 4 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Start AI sessions from your terminal.

Second: Get code assistance without leaving your workflow — this one usually matters most in practice.

Also on screen: Automate coding tasks with scripts, Integrate AI into existing CLI tools.

Next: What Is the Cursor CLI?.

Ask who has seen the opposite problem in production — one story beats five bullets.

The Cursor CLI brings AI-powered coding directly to your command line. - Start AI sessions from your terminal

---

### Slide 218 — Interactive Mode Commands

**Type:** table · **Lesson:** 5.1

**Script**

Next: Interactive Mode Commands.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): /model: Switch between AI models interactively. /compress: Summarize conversation, free up context window. /rules: Create and edit rules directly from CLI. /commands: Create and modify custom commands. /mcp enable/disable: Manage MCP servers. /usage: View Cursor usage stats. /abo

---

### Slide 219 — Windows Exercise Environment

**Type:** exercise_setup · **Lesson:** 5.1

**Script**

Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

**Facilitator notes**

- Allow two to three minutes. Pair anyone blocked on keys or curl with a neighbor.

---

### Slide 220 — Exercise 5.1 — Steps 1–2

**Type:** exercise · **Lesson:** 5.1 · **Exercise:** 5.1

**Script**

Starting Exercise 5.1 — Interactive CLI. 20 min scheduled.

Start an interactive Cursor CLI session from the terminal.

The full lab guide with troubleshooting is in slide-exercises/module-05/exercise-5.1-interactive-cli.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: Start an interactive session.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "agent agent "Help me understand the current codebase structure""

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 221 — Exercise 5.1 — Steps 1–2 (Part 2)

**Type:** exercise · **Lesson:** 5.1 · **Exercise:** 5.1

**Script**

Next step — Steps 1–2 (Part 2).

Step 2: Navigate the session (inside the running agent session — same terminal window) — unless step notes Git Bash or WSL.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 222 — Exercise 5.1 — Steps 3–5

**Type:** exercise · **Lesson:** 5.1 · **Exercise:** 5.1

**Script**

Next step — Steps 3–5.

Step 3: Switch models:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "/model # Or list models outside session: agent --list-models"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 223 — Exercise 5.1 — Steps 3–5 (Part 2)

**Type:** exercise · **Lesson:** 5.1 · **Exercise:** 5.1

**Script**

Next step — Steps 3–5 (Part 2).

Step 4: Ask Mode (read-only):.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "agent --mode=ask "What does this project's main function do?" # Or inside session: /ask"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 224 — Exercise 5.1 — Steps 3–5 (Part 3)

**Type:** exercise · **Lesson:** 5.1 · **Exercise:** 5.1

**Script**

Next step — Steps 3–5 (Part 3).

Step 5: Plan Mode:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "agent --mode=plan "Add user authentication to this API""

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 225 — Exercise 5.1 — Steps 6–7

**Type:** exercise · **Lesson:** 5.1 · **Exercise:** 5.1

**Script**

Next step — Steps 6–7.

Step 6: Configure status line:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "npx -y cursor-statusline # Shows: [model: claude-4.5-sonnet] [~/project] [main] [ctx: 45k/200k]"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 226 — Exercise 5.1 — Steps 6–7 (Part 2)

**Type:** exercise · **Lesson:** 5.1 · **Exercise:** 5.1

**Script**

Next step — Steps 6–7 (Part 2).

Step 7: Terminal key bindings:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "agent /setup-terminal"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 227 — Lesson 5.2

**Type:** lesson_intro · **Lesson:** 5.2

**Script**

Lesson 5.2: One-Shot CLI. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Run single-shot Agent commands from scripts and CI.

Lab reference: slide-exercises/module-05/exercise-5.2-one-shot-cli.md

---

### Slide 228 — One-Shot Command Structure

**Type:** quote · **Lesson:** 5.2

**Script**

Start with the line on screen: "Perfect for automation, CI/CD pipelines, and batch operations."

Next: One-Shot Command Structure.

Pause after the quote — let it land before you add examples.

---

### Slide 229 — Use Cases for One-Shot CLI

**Type:** table · **Lesson:** 5.2

**Script**

Next: Use Cases for One-Shot CLI.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Code generation: agent "Create a React component for a login form". Documentation: agent "Generate JSDoc comments for src/api.js". CI/CD tasks: agent "Review this PR diff for security issues". Batch processing: Loop through files with agent commands. Pre-commit hooks: agent --mod

---

### Slide 230 — Exercise 5.2 — Steps 1–2

**Type:** exercise · **Lesson:** 5.2 · **Exercise:** 5.2

**Script**

Starting Exercise 5.2 — One-Shot CLI. 20 min scheduled.

Run single-shot Agent commands from scripts and CI.

The full lab guide with troubleshooting is in slide-exercises/module-05/exercise-5.2-one-shot-cli.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: Basic one-shot commands:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "agent "What is the difference between let and const in JavaScript?" agent "Write a bash function that checks if a port is in use" agent --mode=ask "Explain the git rebase command with examples""

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 231 — Exercise 5.2 — Steps 1–2 (Part 2)

**Type:** exercise · **Lesson:** 5.2 · **Exercise:** 5.2

**Script**

Next step — Steps 1–2 (Part 2).

Step 2: Specify models:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "agent --model gpt-5-mini "What does this command do: ls -la | grep .txt" agent --model claude-4.5-opus "Design a database schema for a task management system""

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 232 — Exercise 5.2 — Scriptable Code Reviewer

**Type:** exercise · **Lesson:** 5.2 · **Exercise:** 5.2

**Script**

Next step — Scriptable Code Reviewer.

Paste this into the Agent — constraints matter as much as the ask: "#!/bin/bash STAGED_FILES=$(git diff --cached --name-only | tr '\n' ', ') agent --mode=ask "Review these staged files for common issues: Files: $STAGED_FILES Check for: debugging statements, unused imports, security issues, missing error handling. Be concise.""

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 233 — Exercise 5.2 — Batch & Git Hooks

**Type:** exercise · **Lesson:** 5.2 · **Exercise:** 5.2

**Script**

Next step — Batch & Git Hooks.

Step 4: Batch process files:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "for file in src/**/*.py; do agent --mode=ask --non-interactive \ "Summarize this Python file in one sentence: $(head -50 $file)" done"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 234 — Exercise 5.2 — Batch & Git Hooks (Part 2)

**Type:** exercise · **Lesson:** 5.2 · **Exercise:** 5.2

**Script**

Next step — Batch & Git Hooks (Part 2).

Step 5: Pre-commit hook — review staged diff for secrets, debug statements, merge markers.

Where: Agent panel — `Ctrl+I`.

Step 6: CI/CD — analyze test output and suggest fixes for failures.

Terminal: PowerShell — clone/open repo, then continue in Agent panel.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 235 — Lesson 5.3

**Type:** lesson_intro · **Lesson:** 5.3

**Script**

Lesson 5.3: Cloud Handoff. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Hand off a local CLI task to a Cloud Agent with &.

Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.

Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.

Lab reference: slide-exercises/module-05/exercise-5.3-cloud-handoff.md

---

### Slide 236 — What Is Cloud Handoff?

**Type:** bullets · **Lesson:** 5.3

**Script**

Point 1: Continue from web or mobile (cursor.com/agents).

Point 2: Let the agent run long tasks while you're away.

Point 3: Resume the session later from any device.

Next: What Is Cloud Handoff?.

Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.

Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.

Ask who has seen the opposite problem in production — one story beats five bullets.

Send a local conversation to a Cloud Agent: - Continue from web or mobile (cursor.com/agents)

---

### Slide 237 — Cloud Handoff Flow

**Type:** diagram · **Lesson:** 5.3

**Script**

This slide shows Cloud Handoff Flow.

<img src="assets/module-05/cloud-handoff-flow.svg" alt="Cloud Handoff Flow" />

Next: Cloud Handoff Flow.

Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.

Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.

On screen: Cloud Handoff Flow

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 238 — Exercise 5.3 — Steps 1–3

**Type:** exercise · **Lesson:** 5.3 · **Exercise:** 5.3

**Script**

Starting Exercise 5.3 — Cloud Handoff. 18 min scheduled.

Hand off a local CLI task to a Cloud Agent with &.

The full lab guide with troubleshooting is in slide-exercises/module-05/exercise-5.3-cloud-handoff.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: Start local session and hand off:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "agent & "Analyze the entire codebase and create a dependency graph.""

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 239 — Exercise 5.3 — Steps 1–3 (Part 2)

**Type:** exercise · **Lesson:** 5.3 · **Exercise:** 5.3

**Script**

Next step — Steps 1–3 (Part 2).

Step 2: Verify handoff:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "🚀 Handing off to Cloud Agent... ✅ Session running at: https://cursor.com/agents/[agent-id]"

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 240 — Exercise 5.3 — Steps 1–3 (Part 3)

**Type:** exercise · **Lesson:** 5.3 · **Exercise:** 5.3

**Script**

Next step — Steps 1–3 (Part 3).

Step 3: Check status via browser or CLI.

Where: Web browser — Edge or Chrome.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 241 — Exercise 5.3 — Steps 4–6

**Type:** exercise · **Lesson:** 5.3 · **Exercise:** 5.3

**Script**

Next step — Steps 4–6.

Step 4: Push existing conversation:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "& "Continue this conversation in the cloud. I need to log off.""

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 242 — Exercise 5.3 — Steps 4–6 (Part 2)

**Type:** exercise · **Lesson:** 5.3 · **Exercise:** 5.3

**Script**

Next step — Steps 4–6 (Part 2).

Step 5: Long-running task:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "agent "& Refactor the auth module to use JWT. Update all tests and docs.""

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 243 — Exercise 5.3 — Steps 4–6 (Part 3)

**Type:** exercise · **Lesson:** 5.3 · **Exercise:** 5.3

**Script**

Next step — Steps 4–6 (Part 3).

Step 6: Resume later:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "agent --resume [agent-id-from-cloud]"

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 244 — Cloud Handoff Best Practices

**Type:** table · **Lesson:** 5.3 · **Exercise:** 5.3

**Script**

Next: Cloud Handoff Best Practices.

Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.

Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Long-running tasks (>5 min): Quick questions. When you need to close laptop: Interactive debugging. Overnight batch processing: Tasks needing terminal access. Parallel work streams: Security-sensitive code (local only).

---

### Slide 245 — Lesson 5.4

**Type:** lesson_intro · **Lesson:** 5.4

**Script**

Lesson 5.4: Listing and Resuming Sessions. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: List, name, resume, and compress CLI Agent sessions.

Lab reference: slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md

---

### Slide 246 — Session Management Commands

**Type:** table · **Lesson:** 5.4

**Script**

Next: Session Management Commands.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): /resume: List all previous sessions and resume one. agent --resume [id]: Resume a specific session by ID. agent --list: List available sessions (alternative).

---

### Slide 247 — Exercise 5.4 — Steps 1–2

**Type:** exercise · **Lesson:** 5.4 · **Exercise:** 5.4

**Script**

Starting Exercise 5.4 — Listing and Resuming Sessions. 20 min scheduled.

List, name, resume, and compress CLI Agent sessions.

The full lab guide with troubleshooting is in slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: Create multiple named sessions:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "agent "Just say one word: frontend-cleanup" # do work, exit agent "Just say one word: db-optimization" # do work, exit agent "Just say one word: docs-update""

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 248 — Exercise 5.4 — Steps 1–2 (Part 2)

**Type:** exercise · **Lesson:** 5.4 · **Exercise:** 5.4

**Script**

Next step — Steps 1–2 (Part 2).

Step 2: List all sessions:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "/resume # 1. frontend-cleanup Agent (2 hours ago) # 2. db-optimization Agent (1 hour ago) # 3. docs-update Agent (30 minutes ago)"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 249 — Exercise 5.4 — Steps 3–5

**Type:** exercise · **Lesson:** 5.4 · **Exercise:** 5.4

**Script**

Next step — Steps 3–5.

Step 3: Resume by ID:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "agent --resume abc123-def456-ghi789"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 250 — Exercise 5.4 — Steps 3–5 (Part 2)

**Type:** exercise · **Lesson:** 5.4 · **Exercise:** 5.4

**Script**

Next step — Steps 3–5 (Part 2).

Step 4: Concurrent sessions in different terminals:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "# Terminal 1: agent --resume frontend-cleanup # Terminal 2: agent --resume db-optimization"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 251 — Exercise 5.4 — Steps 3–5 (Part 3)

**Type:** exercise · **Lesson:** 5.4 · **Exercise:** 5.4

**Script**

Next step — Steps 3–5 (Part 3).

Step 5: Context management:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "/compress # Summarize conversation, free context window"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 252 — Exercise 5.4 — Steps 6–7 & Best Practices

**Type:** exercise · **Lesson:** 5.4 · **Exercise:** 5.4

**Script**

Next step — Steps 6–7 & Best Practices.

Step 6: Export session summary as markdown.

Where: Agent panel — `Ctrl+I`.

Step 7: Create bin/cursor-sessions.sh to list and manage sessions.

Where: Agent panel — `Ctrl+I`.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- Watch PATH, working directory, and resumed session branch.

---

### Slide 253 — Module Summary

**Type:** module_summary · **Lesson:** 5.4 · **Exercise:** 5.4

**Script**

That completes Module 5. Lesson 5.1, Interactive CLI — key insight: Real-time terminal AI; Lesson 5.2, One-Shot CLI — key insight: Scripting & automation; Lesson 5.3, Cloud Handoff — key insight: Remote/long-running tasks; Lesson 5.4, Session Management — key insight: Concurrent work handling

What will you do differently on Monday? I will take two or three answers before we break or move on.

---

### Slide 254 — Quick Reference Card

**Type:** quick_reference · **Lesson:** 5.4 · **Exercise:** 5.4

**Script**

This quick reference slide is for you to keep after the course — screenshot it or copy the commands into your team wiki.

Quick Reference Card

**Facilitator notes**

- Allow about two minutes for final questions on this module.

---

### Slide 255 — Day 2

**Type:** day_break · **Lesson:** 5.4 · **Exercise:** 5.4

**Script**

Welcome back — Day 2.

Yesterday we established how AI models behave and how to use Cursor safely in real repositories. Today we extend that work outside the IDE: the CLI, Cloud Agents, and production-grade API integration.

Before we continue, make sure API keys are available where needed and that you can open PowerShell and reach api.cursor.com from this network. We will store every key in environment variables — never paste secrets on screen or into chat logs.

---

## Module 6 — Cloud Agents in the UI

### Slide 256 — Cloud Agents in the UI

**Type:** module_intro

**Script**

Module 6 introduces Cloud Agents in the product UI — watch runs, artifacts, and handoffs from local work.

Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.

Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.

Timing on slide: Cursor Training Program · ~90 min

---

### Slide 257 — Module Overview

**Type:** module_overview

**Script**

The module goal in plain language: Master Cloud Agents UI for remote execution, artifact collection, and messaging integrations

Glance at duration and prerequisites on screen — raise a hand if anything blocks you.

---

### Slide 258 — Learning Objectives

**Type:** learning_objectives

**Script**

These outcomes define success for Module 6 — not a reading list, but skills you will practice.

Highlight three that matter for your role: Launch and monitor Cloud Agents from the Cursor UI; Collect and download artifacts from completed cloud runs; Trigger Cloud Agents from messaging platforms (Slack, Microsoft Teams, Discord) and project tools (Jira); plus more on screen.

Next: learning objectives.

Ask who has seen the opposite problem in production — one story beats five bullets.

---

### Slide 259 — Agenda

**Type:** module_agenda

**Script**

Here is how we will spend our time: Lesson 6.1, Launching a Cloud Agent, about 25 min; Lesson 6.2, Cloud Agent Artifacts, about 23 min; Lesson 6.3, Cloud Agents from Messaging Platforms, about 20 min.

**Facilitator notes**

- Announce when the next hands-on block starts so people can close email and open Cursor.

---

### Slide 260 — Lesson 6.1

**Type:** lesson_intro · **Lesson:** 6.1

**Script**

Lesson 6.1: Launching a Cloud Agent. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Launch a Cloud Agent from the Cursor UI and track its run.

Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.

Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.

Lab reference: slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md

---

### Slide 261 — Cloud Agents vs. Local Agent

**Type:** table · **Lesson:** 6.1

**Script**

Next: Cloud Agents vs. Local Agent.

Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.

Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Runs on: Your machine. Use this when Cursor's infrastructure. Persistence: Ends when you quit. Use this when Continues indefinitely. Access: Local only. Use this when Web, mobile, API. Terminal access: Your terminal. Use this when Simulated/scripted. File access: Local files. Use

---

### Slide 262 — When to Use Cloud Agents

**Type:** bullets · **Lesson:** 6.1

**Script**

There are 5 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Long-running tasks (>10 min) · Scheduled jobs.

Second: Tasks while offline · Parallel execution — this one usually matters most in practice.

Also on screen: Team-accessible results (share agent URL), Interactive debugging · Local-only files….

Next: When to Use Cloud Agents.

Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.

Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.

Ask who has seen the opposite problem in production — one story beats five bullets.

Good for: - Long-running tasks (>10 min) · Scheduled jobs

---

### Slide 263 — Accessing Cloud Agents UI

**Type:** table · **Lesson:** 6.1

**Script**

Next: Accessing Cloud Agents UI.

Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.

Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): From Cursor Editor: View → Cloud Agents (or cloud icon in sidebar). From Web: https://cursor.com/agents. From Mobile: cursor.com/agents (responsive web).

---

### Slide 264 — Cloud Agent Dashboard

**Type:** code · **Lesson:** 6.1

**Script**

Cloud Agent Dashboard

Focus on the first few lines — for example: Active (2).

Next: Cloud Agent Dashboard.

Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.

Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.

---

### Slide 265 — Windows Exercise Environment

**Type:** exercise_setup · **Lesson:** 6.1

**Script**

Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

**Facilitator notes**

- Allow two to three minutes. Pair anyone blocked on keys or curl with a neighbor.

---

### Slide 266 — Exercise 6.1 — Steps 1–2

**Type:** exercise · **Lesson:** 6.1 · **Exercise:** 6.1

**Script**

Starting Exercise 6.1 — Launching a Cloud Agent. 25 min scheduled.

Launch a Cloud Agent from the Cursor UI and track its run.

The full lab guide with troubleshooting is in slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: Navigate to Cloud Agents.

Terminal: PowerShell — `Ctrl+ `` in Cursor.

Paste this into the Agent — constraints matter as much as the ask: "# Cursor Editor: cloud icon or View → Cloud Agents open https://cursor.com/agents"

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If No repositories shown: Connect GitHub in dashboard Integrations first
- If Agent fails immediately: Check logs for error messages

---

### Slide 267 — Exercise 6.1 — Steps 1–2 (Part 2)

**Type:** exercise · **Lesson:** 6.1 · **Exercise:** 6.1

**Script**

Next step — Steps 1–2 (Part 2).

Step 2: Click "+ New" and fill out:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "Repository: https://github.com/YOUR_ORG/YOUR_REPO Branch: main Prompt: Read README and main source files. Summarize: - What this project does - Key dependencies · How to run locally · Common issues Model: claude-4.6-sonnet Auto-create PR: ☐"

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If No repositories shown: Connect GitHub in dashboard Integrations first
- If Agent fails immediately: Check logs for error messages

---

### Slide 268 — Exercise 6.1 — Steps 3–4

**Type:** exercise · **Lesson:** 6.1 · **Exercise:** 6.1

**Script**

Next step — Steps 3–4.

Step 3: Monitor live log in real time:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "[10:45:01] Agent starting... [10:45:02] Cloning repository... [10:45:15] Repository cloned [10:45:16] Reading README.md [10:45:40] Generating summary..."

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If No repositories shown: Connect GitHub in dashboard Integrations first
- If Agent fails immediately: Check logs for error messages

---

### Slide 269 — Exercise 6.1 — Steps 3–4 (Part 2)

**Type:** exercise · **Lesson:** 6.1 · **Exercise:** 6.1

**Script**

Next step — Steps 3–4 (Part 2).

Step 4: Configure settings (gear icon):.

Where: Agent panel — `Ctrl+I`.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If No repositories shown: Connect GitHub in dashboard Integrations first
- If Agent fails immediately: Check logs for error messages

---

### Slide 270 — Exercise 6.1 — Steps 5–6

**Type:** exercise · **Lesson:** 6.1 · **Exercise:** 6.1

**Script**

Next step — Steps 5–6.

Step 5: Launch with PR creation:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "Prompt: Add CONTRIBUTING.md with dev setup, tests, PR process, code style Auto-create PR: ✅ Yes Branch prefix: docs/contributing"

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If No repositories shown: Connect GitHub in dashboard Integrations first
- If Agent fails immediately: Check logs for error messages

---

### Slide 271 — Exercise 6.1 — Steps 5–6 (Part 2)

**Type:** exercise · **Lesson:** 6.1 · **Exercise:** 6.1

**Script**

Next step — Steps 5–6 (Part 2).

Step 6: Share agent URL with team:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "https://cursor.com/agents/agt_abc123def456"

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If No repositories shown: Connect GitHub in dashboard Integrations first
- If Agent fails immediately: Check logs for error messages

---

### Slide 272 — Lesson 6.2

**Type:** lesson_intro · **Lesson:** 6.2

**Script**

Lesson 6.2: Cloud Agent Artifacts. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Collect and download artifacts produced by Cloud Agents.

Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.

Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.

Lab reference: slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md

---

### Slide 273 — Types of Artifacts

**Type:** table · **Lesson:** 6.2

**Script**

Next: Types of Artifacts.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Artifact Type: Examples. Log files: agent.log, debug.log. Code files: .py, .js, *.html. Documents: .md, .txt, *.json. Images: .png, .jpg, *.svg. Archives: .zip, .tar.gz. Test results: junit.xml, coverage.json.

---

### Slide 274 — Artifact Storage

**Type:** bullets · **Lesson:** 6.2

**Script**

There are 4 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Stored for 30 days.

Second: Multiple artifacts per agent — this one usually matters most in practice.

Also on screen: Download URLs expire after 15 minutes, Max 100MB per file · 1GB total per agent.

Next: Artifact Storage.

Ask who has seen the opposite problem in production — one story beats five bullets.

- Stored for 30 days - Multiple artifacts per agent

---

### Slide 275 — Exercise 6.2 — Steps 1–2

**Type:** exercise · **Lesson:** 6.2 · **Exercise:** 6.2

**Script**

Starting Exercise 6.2 — Cloud Agent Artifacts. 25 min scheduled.

Collect and download artifacts produced by Cloud Agents.

The full lab guide with troubleshooting is in slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: Launch agent that generates artifacts:.

Where: Agent panel — `Ctrl+I`.

Paste this into the Agent — constraints matter as much as the ask: "Generate: 1. api_documentation.md — OpenAPI-style docs for all endpoints 2. test_report.json — test suite summary 3. screenshot.png — main UI screenshot (if applicable) 4. dependencies.txt — all packages and versions Place all in artifacts/ directory."

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If No artifacts shown: Not all agents produce artifacts. Try a task that uses browser or generates files
- If Artifacts won't load: Check internet connection; try refreshing page

---

### Slide 276 — Exercise 6.2 — Steps 1–2 (Part 2)

**Type:** exercise · **Lesson:** 6.2 · **Exercise:** 6.2

**Script**

Next step — Steps 1–2 (Part 2).

Step 2: After completion, view artifact list in UI with Download buttons and Download All (zip).

Where: Agent panel — `Ctrl+I`.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If No artifacts shown: Not all agents produce artifacts. Try a task that uses browser or generates files
- If Artifacts won't load: Check internet connection; try refreshing page

---

### Slide 277 — Exercise 6.2 — Steps 3–5

**Type:** exercise · **Lesson:** 6.2 · **Exercise:** 6.2

**Script**

Next step — Steps 3–5.

Step 3: Download individual artifacts.

Where: Agent panel — `Ctrl+I`.

Step 4: Download all as zip.

Where: Agent panel — `Ctrl+I`.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If No artifacts shown: Not all agents produce artifacts. Try a task that uses browser or generates files
- If Artifacts won't load: Check internet connection; try refreshing page

---

### Slide 278 — Exercise 6.2 — Steps 3–5 (Part 2)

**Type:** exercise · **Lesson:** 6.2 · **Exercise:** 6.2

**Script**

Next step — Steps 3–5 (Part 2).

Step 5: Preview in browser:.

Where: Web browser — Edge or Chrome.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If No artifacts shown: Not all agents produce artifacts. Try a task that uses browser or generates files
- If Artifacts won't load: Check internet connection; try refreshing page

---

### Slide 279 — Exercise 6.2 — API Access

**Type:** exercise · **Lesson:** 6.2 · **Exercise:** 6.2

**Script**

Next step — API Access.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If No artifacts shown: Not all agents produce artifacts. Try a task that uses browser or generates files
- If Artifacts won't load: Check internet connection; try refreshing page

---

### Slide 280 — Exercise 6.2 — CI/CD Integration

**Type:** exercise · **Lesson:** 6.2 · **Exercise:** 6.2

**Script**

Next step — CI/CD Integration.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If No artifacts shown: Not all agents produce artifacts. Try a task that uses browser or generates files
- If Artifacts won't load: Check internet connection; try refreshing page

---

### Slide 281 — Lesson 6.3

**Type:** lesson_intro · **Lesson:** 6.3

**Script**

Lesson 6.3: Cloud Agents from Messaging Platforms. Participation: listen, participate, or follow along as indicated on the next slides.

Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.

Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.

---

### Slide 282 — Supported Integrations

**Type:** table · **Lesson:** 6.3

**Script**

Next: Supported Integrations.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Platform: Capabilities. Use this when Setup. Slack: @Cursor mentions, command triggering, notifications. Use this when Medium (Slack app). Microsoft Teams: @Cursor in channels, delegate tasks to cloud agents. Use this when Medium (Teams integration). Jira: Assign issues to Cursor

---

### Slide 283 — Messaging Integration Architecture

**Type:** diagram · **Lesson:** 6.3

**Script**

This slide shows Messaging Integration Architecture.

<img src="assets/module-06/messaging-integration-architecture.svg" alt="Messaging Integration Architecture" />

Next: Messaging Integration Architecture.

Messaging Integration Architecture

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 284 — Demo: Slack Integration

**Type:** demo · **Lesson:** 6.3

**Script**

I am going to demonstrate Slack Integration live on my machine. Step 1: Create Slack App at api.slack.com Step 2: Configure slash command: Step 3: Deploy webhook receiver (Flask/Python) that: - Parses Slack command → launches Cloud Agent via API - Acknowledges immediately with agent URL - Posts completion summary when webhook fires I will narrate each click and keystroke as I go.

When the demo finishes, we will discuss when slack integration belongs in production workflow and when a lighter-weight approach is enough.

**Facilitator notes**

- If the network fails, describe the expected result and use a screenshot backup.

---

### Slide 285 — Demo: Slack Usage

**Type:** demo · **Lesson:** 6.3

**Script**

I am going to demonstrate Slack Usage live on my machine. In Slack: Response: I will narrate each click and keystroke as I go.

When the demo finishes, we will discuss when slack usage belongs in production workflow and when a lighter-weight approach is enough.

**Facilitator notes**

- If the network fails, describe the expected result and use a screenshot backup.

---

### Slide 286 — Demo: Jira Integration

**Type:** demo · **Lesson:** 6.3

**Script**

I am going to demonstrate Jira Integration live on my machine. Step 1: Install the Jira integration from the Cursor dashboard (requires Cursor admin access). Step 2: Ensure Jira Commercial Cloud has Rovo enabled. Step 3: Assign a work item to Cursor or mention @Cursor in a comment: What happens: - Agent reads the issue title, description, comments, and repository settings - Agent implements the fix and opens a pull request - Jira receives a completion update with a link to the PR I will narrate each click and keystroke as I go.

When the demo finishes, we will discuss when jira integration belongs in production workflow and when a lighter-weight approach is enough.

**Facilitator notes**

- If the network fails, describe the expected result and use a screenshot backup.

---

### Slide 287 — Demo: Discord Integration

**Type:** demo · **Lesson:** 6.3

**Script**

I am going to demonstrate Discord Integration live on my machine. Usage: !cursor Add error handling to all API endpoints I will narrate each click and keystroke as I go.

When the demo finishes, we will discuss when discord integration belongs in production workflow and when a lighter-weight approach is enough.

**Facilitator notes**

- If the network fails, describe the expected result and use a screenshot backup.

---

### Slide 288 — Generic Webhook & Notifications

**Type:** code · **Lesson:** 6.3

**Script**

Any HTTP POST can trigger agents: Use cases: GitHub webhook on PR · Cron jobs · CI/CD post-deploy · Internal dashboard Status notifications: configure notifyOnStart, notifyOnComplete, notifyOnError

Run this from PowerShell with your key in an environment variable. Never paste live credentials into chat or commit them to git.

Next: Generic Webhook & Notifications.

Production API work is boring on purpose: auth, retries, caching, verified signatures.

Windows labs use `$env:VAR` and `curl.exe` — if a command fails, check quoting before re-generating the key.

---

### Slide 289 — Module Summary

**Type:** module_summary · **Lesson:** 6.3

**Script**

That completes Module 6. Lesson 6.1, Launching Cloud Agents — key insight: Remote execution; Lesson 6.2, Cloud Agent Artifacts — key insight: Output collection; Lesson 6.3, Messaging Integrations — key insight: Chat-triggered agents

What will you do differently on Monday? I will take two or three answers before we break or move on.

---

### Slide 290 — Quick Reference Card

**Type:** quick_reference · **Lesson:** 6.3

**Script**

This quick reference slide is for you to keep after the course — screenshot it or copy the commands into your team wiki.

Quick Reference Card

**Facilitator notes**

- Allow about two minutes for final questions on this module.

---

## Module 7 — Cursor API Foundations

### Slide 291 — Cursor API Foundations

**Type:** module_intro

**Script**

Module 7 is API foundations — keys, errors, caching. Boring infrastructure that keeps integrations alive in production.

Timing on slide: Cursor Training Program · ~60 min

---

### Slide 292 — Module Overview

**Type:** module_overview

**Script**

The module goal in plain language: Understand the Cursor API ecosystem, authenticate securely, handle errors, and optimize requests

Glance at duration and prerequisites on screen — raise a hand if anything blocks you.

---

### Slide 293 — Learning Objectives

**Type:** learning_objectives

**Script**

These outcomes define success for Module 7 — not a reading list, but skills you will practice.

Highlight three that matter for your role: Identify the five Cursor APIs and their use cases; Generate and securely manage API keys; Implement rate limit handling and error recovery; plus more on screen.

Next: learning objectives.

Ask who has seen the opposite problem in production — one story beats five bullets.

---

### Slide 294 — Agenda

**Type:** module_agenda

**Script**

Here is how we will spend our time: Lesson 7.1, The Cursor API Landscape, about 10 min; Lesson 7.2, Authentication, about 20 min; Lesson 7.3, Rate Limits and Error Handling, about 20 min; Lesson 7.4, ETag Caching, about 18 min; Lesson 7.5, Listing Available Models, about 10 min.

**Facilitator notes**

- Announce when the next hands-on block starts so people can close email and open Cursor.

---

### Slide 295 — Lesson 7.1

**Type:** lesson_intro · **Lesson:** 7.1

**Script**

Lesson 7.1: The Cursor API Landscape. Participation: listen, participate, or follow along as indicated on the next slides.

---

### Slide 296 — The Five APIs

**Type:** table · **Lesson:** 7.1

**Script**

Next: The Five APIs.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): API: Endpoint. Use this when Purpose. Chat Completions: /v1/chat/completions. Use this when OpenAI-compatible chat interface. Agents: /v1/agents. Use this when Create and manage Cloud Agents. Files: /v1/files. Use this when Upload/download files for agents. Admin: /v1/admin/*. Us

---

### Slide 297 — API Comparison Matrix

**Type:** table · **Lesson:** 7.1

**Script**

Next: API Comparison Matrix.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): API: Auth Type. Use this when Rate Limit. Chat Completions: User or API key. Use this when Per-minute token. Agents: User API key. Use this when Per-minute requests. Files: User API key. Use this when Per-minute. Admin: Admin API key. Use this when Higher limits. Webhooks: User A

---

### Slide 298 — When to Use Which API

**Type:** bullets · **Lesson:** 7.1

**Script**

There are 4 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Call a model directly → Chat Completions API (OpenAI-compatible).

Second: Run a long task that writes code → Agents API — this one usually matters most in practice.

Also on screen: Manage team usage and limits → Admin API, Be notified when agents complete → Webhooks API.

Next: When to Use Which API.

Ask who has seen the opposite problem in production — one story beats five bullets.

- Call a model directly → Chat Completions API (OpenAI-compatible) - Run a long task that writes code → Agents API

---

### Slide 299 — OpenAI Compatibility

**Type:** code · **Lesson:** 7.1

**Script**

Success Criteria: Understand five APIs · select correct API · understand OpenAI compatibility

Run this from PowerShell with your key in an environment variable. Never paste live credentials into chat or commit them to git.

Next: OpenAI Compatibility.

---

### Slide 300 — Lesson 7.2

**Type:** lesson_intro · **Lesson:** 7.2

**Script**

Lesson 7.2: Authentication. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Create Admin and User API keys and verify authentication.

Lab reference: slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md

---

### Slide 301 — Authentication Methods

**Type:** table · **Lesson:** 7.2

**Script**

Next: Authentication Methods.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Method: Format. Use this when When to Use. HTTP Basic: -u "api_key:". Use this when CLI, curl, most SDKs. Bearer Token: Authorization: Bearer <key>. Use this when OAuth-style clients. User API Key: Regular key. Use this when Agents, Chat, Files APIs. Admin API Key: admin_ prefixe

---

### Slide 302 — API Key Types

**Type:** bullets · **Lesson:** 7.2

**Script**

There are 6 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Generated in: Cursor Settings → API Keys.

Second: Format: cursor_xxxxxxxxxxxx — this one usually matters most in practice.

Also on screen: Can access: Agents, Chat, Files, Webhooks, Generated in: Organization Settings → API Keys….

Next: API Key Types.

Production API work is boring on purpose: auth, retries, caching, verified signatures.

Windows labs use `$env:VAR` and `curl.exe` — if a command fails, check quoting before re-generating the key.

Ask who has seen the opposite problem in production — one story beats five bullets.

User API Key - Generated in: Cursor Settings → API Keys

---

### Slide 303 — Security Best Practices

**Type:** bullets · **Lesson:** 7.2

**Script**

There are 7 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Never commit API keys to git.

Second: Use environment variables or secret managers — this one usually matters most in practice.

Also on screen: Rotate keys periodically (every 90 days), Use different keys for dev and production….

Next: Security Best Practices.

Ask who has seen the opposite problem in production — one story beats five bullets.

- Never commit API keys to git - Use environment variables or secret managers

---

### Slide 304 — Windows Exercise Environment

**Type:** exercise_setup · **Lesson:** 7.2

**Script**

Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

**Facilitator notes**

- Allow two to three minutes. Pair anyone blocked on keys or curl with a neighbor.

---

### Slide 305 — Exercise 7.2 — Steps 1–3

**Type:** exercise · **Lesson:** 7.2 · **Exercise:** 7.2

**Script**

Starting Exercise 7.2 — Generate and Test API Keys. 15 min scheduled.

Create Admin and User API keys and verify authentication.

The full lab guide with troubleshooting is in slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Admin keys and User keys are not interchangeable — 401 often means wrong key type, not a bad copy-paste.

First success is a 200 with expected JSON — celebrate that before moving to harder exercises.

Step 1: Generate User API Key — Where: Cursor app → Settings → API Keys → Generate New Key (copy the key; you will not see it again).

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If `401 Unauthorized`: Check that the API key is correct and includes the colon after it in Basic Auth
- If `403 Forbidden`: Admin API requires Enterprise plan. Use User API key for Cloud Agents API instead
- If Key not found in dashboard: Check correct section: Admin Keys vs Integrations vs Service Accounts

---

### Slide 306 — Exercise 7.2 — Steps 1–3 (Part 2)

**Type:** exercise · **Lesson:** 7.2 · **Exercise:** 7.2

**Script**

Next step — Steps 1–3 (Part 2).

Step 2: Set environment variable — Terminal: PowerShell (`Ctrl+ ``).

Paste this into the Agent — constraints matter as much as the ask: "$env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx" $env:CURSOR_USER_API_KEY"

Admin keys and User keys are not interchangeable — 401 often means wrong key type, not a bad copy-paste.

First success is a 200 with expected JSON — celebrate that before moving to harder exercises.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If `401 Unauthorized`: Check that the API key is correct and includes the colon after it in Basic Auth
- If `403 Forbidden`: Admin API requires Enterprise plan. Use User API key for Cloud Agents API instead
- If Key not found in dashboard: Check correct section: Admin Keys vs Integrations vs Service Accounts

---

### Slide 307 — Exercise 7.2 — Steps 1–3 (Part 3)

**Type:** exercise · **Lesson:** 7.2 · **Exercise:** 7.2

**Script**

Next step — Steps 1–3 (Part 3).

Step 3: Test with curl — Terminal: PowerShell.

Admin keys and User keys are not interchangeable — 401 often means wrong key type, not a bad copy-paste.

First success is a 200 with expected JSON — celebrate that before moving to harder exercises.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If `401 Unauthorized`: Check that the API key is correct and includes the colon after it in Basic Auth
- If `403 Forbidden`: Admin API requires Enterprise plan. Use User API key for Cloud Agents API instead
- If Key not found in dashboard: Check correct section: Admin Keys vs Integrations vs Service Accounts

---

### Slide 308 — Exercise 7.2 — Steps 4–5

**Type:** exercise · **Lesson:** 7.2 · **Exercise:** 7.2

**Script**

Next step — Steps 4–5.

Step 4: Test with Python requests:.

Terminal: PowerShell — save as test_models.py, then python test_models.py — `Ctrl+L`.

Paste this into the Agent — constraints matter as much as the ask: "response = requests.get( "https://api.cursor.com/v1/models", auth=(API_KEY, "") # Empty password )"

Admin keys and User keys are not interchangeable — 401 often means wrong key type, not a bad copy-paste.

First success is a 200 with expected JSON — celebrate that before moving to harder exercises.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If `401 Unauthorized`: Check that the API key is correct and includes the colon after it in Basic Auth
- If `403 Forbidden`: Admin API requires Enterprise plan. Use User API key for Cloud Agents API instead
- If Key not found in dashboard: Check correct section: Admin Keys vs Integrations vs Service Accounts

---

### Slide 309 — Exercise 7.2 — Steps 4–5 (Part 2)

**Type:** exercise · **Lesson:** 7.2 · **Exercise:** 7.2

**Script**

Next step — Steps 4–5 (Part 2).

Step 5: Test with OpenAI SDK:.

Terminal: PowerShell — python test_openai_sdk.py — `Ctrl+L`.

Paste this into the Agent — constraints matter as much as the ask: "client = OpenAI(base_url="https://api.cursor.com/v1", api_key=API_KEY) response = client.chat.completions.create( model="gpt-5-mini", messages=[{"role": "user", "content": "Say 'API works!'"}], max_tokens=10 )"

Admin keys and User keys are not interchangeable — 401 often means wrong key type, not a bad copy-paste.

First success is a 200 with expected JSON — celebrate that before moving to harder exercises.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If `401 Unauthorized`: Check that the API key is correct and includes the colon after it in Basic Auth
- If `403 Forbidden`: Admin API requires Enterprise plan. Use User API key for Cloud Agents API instead
- If Key not found in dashboard: Check correct section: Admin Keys vs Integrations vs Service Accounts

---

### Slide 310 — Exercise 7.2 — Steps 6–7

**Type:** exercise · **Lesson:** 7.2 · **Exercise:** 7.2

**Script**

Next step — Steps 6–7.

Step 6: Generate and test Admin API Key:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Admin keys and User keys are not interchangeable — 401 often means wrong key type, not a bad copy-paste.

First success is a 200 with expected JSON — celebrate that before moving to harder exercises.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If `401 Unauthorized`: Check that the API key is correct and includes the colon after it in Basic Auth
- If `403 Forbidden`: Admin API requires Enterprise plan. Use User API key for Cloud Agents API instead
- If Key not found in dashboard: Check correct section: Admin Keys vs Integrations vs Service Accounts

---

### Slide 311 — Exercise 7.2 — Steps 6–7 (Part 2)

**Type:** exercise · **Lesson:** 7.2 · **Exercise:** 7.2

**Script**

Next step — Steps 6–7 (Part 2).

Step 7: Revoke compromised keys via API or Settings → API Keys → Revoke.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Admin keys and User keys are not interchangeable — 401 often means wrong key type, not a bad copy-paste.

First success is a 200 with expected JSON — celebrate that before moving to harder exercises.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If `401 Unauthorized`: Check that the API key is correct and includes the colon after it in Basic Auth
- If `403 Forbidden`: Admin API requires Enterprise plan. Use User API key for Cloud Agents API instead
- If Key not found in dashboard: Check correct section: Admin Keys vs Integrations vs Service Accounts

---

### Slide 312 — Lesson 7.3

**Type:** lesson_intro · **Lesson:** 7.3

**Script**

Lesson 7.3: Rate Limits and Error Handling. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Handle 429 responses with backoff and rate-limit headers.

Production API work is boring on purpose: auth, retries, caching, verified signatures.

Windows labs use `$env:VAR` and `curl.exe` — if a command fails, check quoting before re-generating the key.

Lab reference: slide-exercises/module-07/exercise-7.3-rate-limits-and-error-handling.md

---

### Slide 313 — Rate Limits by API

**Type:** table · **Lesson:** 7.3

**Script**

Next: Rate Limits by API.

Production API work is boring on purpose: auth, retries, caching, verified signatures.

Windows labs use `$env:VAR` and `curl.exe` — if a command fails, check quoting before re-generating the key.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): API: Limit. Use this when Window. Chat Completions: 1000 requests. Use this when per minute. Chat Completions (tokens): 500k tokens. Use this when per minute. Agents (create): 100 requests. Use this when per minute. Admin API: 500 requests. Use this when per minute. Webhooks: 200

---

### Slide 314 — HTTP Status Codes to Handle

**Type:** table · **Lesson:** 7.3

**Script**

Next: HTTP Status Codes to Handle.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Code: Meaning. Use this when Action. 200: Success. Use this when Process response. 400: Bad Request. Use this when Fix request parameters. 401: Unauthorized. Use this when Check API key. 403: Forbidden. Use this when Check permissions. 429: Too Many Requests. Use this when Implem

---

### Slide 315 — Rate Limit Headers

**Type:** table · **Lesson:** 7.3

**Script**

Next: Rate Limit Headers.

Production API work is boring on purpose: auth, retries, caching, verified signatures.

Windows labs use `$env:VAR` and `curl.exe` — if a command fails, check quoting before re-generating the key.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Header: Description. Use this when Example. X-RateLimit-Limit: Max requests per window. Use this when 1000. X-RateLimit-Remaining: Requests left. Use this when 942. X-RateLimit-Reset: Window reset (Unix timestamp). Use this when 1700000000. Retry-After: Seconds to wait (on 429). 

---

### Slide 316 — Exercise 7.3 — Exponential Backoff

**Type:** exercise · **Lesson:** 7.3 · **Exercise:** 7.3

**Script**

Starting Exercise 7.3 — Rate Limits and Error Handling. 15 min scheduled.

Handle 429 responses with backoff and rate-limit headers.

The full lab guide with troubleshooting is in slide-exercises/module-07/exercise-7.3-rate-limits-and-error-handling.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If 401 Unauthorized: Check API key is correct and includes the colon in Basic Auth
- If 403 Forbidden: Some endpoints require Enterprise plan. Use a different endpoint or upgrade
- If 404 Not Found: Verify the endpoint URL is correct

---

### Slide 317 — Exercise 7.3 — Rate Limiter & Client

**Type:** exercise · **Lesson:** 7.3 · **Exercise:** 7.3

**Script**

Next step — Rate Limiter & Client.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If 401 Unauthorized: Check API key is correct and includes the colon in Basic Auth
- If 403 Forbidden: Some endpoints require Enterprise plan. Use a different endpoint or upgrade
- If 404 Not Found: Verify the endpoint URL is correct

---

### Slide 318 — Lesson 7.4

**Type:** lesson_intro · **Lesson:** 7.4

**Script**

Lesson 7.4: ETag Caching. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Use ETags to avoid re-downloading unchanged API data.

Production API work is boring on purpose: auth, retries, caching, verified signatures.

Windows labs use `$env:VAR` and `curl.exe` — if a command fails, check quoting before re-generating the key.

Lab reference: slide-exercises/module-07/exercise-7.4-etag-caching.md

---

### Slide 319 — What Are ETags?

**Type:** content · **Lesson:** 7.4

**Script**

Next: What Are ETags?.

Production API work is boring on purpose: auth, retries, caching, verified signatures.

Windows labs use `$env:VAR` and `curl.exe` — if a command fails, check quoting before re-generating the key.

On screen: ETags are unique identifiers for API response versions. 1. Send If-None-Match header with previous ETag 2. Server returns 304 Not Modified if unchanged 3. No data transfer, no rate limit consumption

---

### Slide 320 — ETag Flow

**Type:** diagram · **Lesson:** 7.4

**Script**

This slide shows ETag Flow.

<img src="assets/module-07/etag-flow.svg" alt="ETag Flow" />

Next: ETag Flow.

Production API work is boring on purpose: auth, retries, caching, verified signatures.

Windows labs use `$env:VAR` and `curl.exe` — if a command fails, check quoting before re-generating the key.

On screen: ETag Flow

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 321 — Endpoints Supporting ETags

**Type:** table · **Lesson:** 7.4

**Script**

Next: Endpoints Supporting ETags.

Production API work is boring on purpose: auth, retries, caching, verified signatures.

Windows labs use `$env:VAR` and `curl.exe` — if a command fails, check quoting before re-generating the key.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Endpoint: ETag Support. Use this when Cache Freshness. /v1/models: ✅ Yes. Use this when Changes rarely. /v1/admin/members: ✅ Yes. Use this when Changes occasionally. /v1/agents/{id}: ✅ Yes. Use this when Changes during run. /v1/analytics/usage: ✅ Yes. Use this when Daily changes.

---

### Slide 322 — Exercise 7.4 — Basic ETag Usage

**Type:** exercise · **Lesson:** 7.4 · **Exercise:** 7.4

**Script**

Starting Exercise 7.4 — ETag Caching. 15 min scheduled.

Use ETags to avoid re-downloading unchanged API data.

The full lab guide with troubleshooting is in slide-exercises/module-07/exercise-7.4-etag-caching.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If No ETag in response: Some endpoints don't support caching. Use Analytics or AI Code Tracking API
- If Always getting 200, not 304: Data may be changing frequently. Try a different endpoint or shorter time range
- If 304 but no cached data: Cache was cleared. Make initial request first

---

### Slide 323 — Exercise 7.4 — ETagCache & CachedClient

**Type:** exercise · **Lesson:** 7.4 · **Exercise:** 7.4

**Script**

Next step — ETagCache & CachedClient.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If No ETag in response: Some endpoints don't support caching. Use Analytics or AI Code Tracking API
- If Always getting 200, not 304: Data may be changing frequently. Try a different endpoint or shorter time range
- If 304 but no cached data: Cache was cleared. Make initial request first

---

### Slide 324 — Lesson 7.5

**Type:** lesson_intro · **Lesson:** 7.5

**Script**

Lesson 7.5: Listing Available Models. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Query available models and pick the right one programmatically.

Lab reference: slide-exercises/module-07/exercise-7.5-list-available-models.md

---

### Slide 325 — The Models Endpoint

**Type:** quote · **Lesson:** 7.5

**Script**

Start with the line on screen: "Simplest API call — perfect for verifying your API key works."

Expand in your own words — do not read the bullet text verbatim: Response includes: - Model ID · Display name · Context window size

Next: The Models Endpoint.

Pause after the quote — let it land before you add examples.

---

### Slide 326 — Exercise 7.5 — Steps 1–2

**Type:** exercise · **Lesson:** 7.5 · **Exercise:** 7.5

**Script**

Starting Exercise 7.5 — List Available Models. 10 min scheduled.

Query available models and pick the right one programmatically.

The full lab guide with troubleshooting is in slide-exercises/module-07/exercise-7.5-list-available-models.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: List with curl:.

Terminal: PowerShell — `Ctrl+ `` in Cursor.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If 401 Unauthorized: Check API key is set correctly
- If Empty models list: Your plan may have limited models. Check subscription
- If `jq: command not found`: Install jq: `brew install jq` (Mac) or `apt-get install jq` (Linux)

---

### Slide 327 — Exercise 7.5 — Steps 1–2 (Part 2)

**Type:** exercise · **Lesson:** 7.5 · **Exercise:** 7.5

**Script**

Next step — Steps 1–2 (Part 2).

Step 2: Format with Python tabulate — Model ID, Context, Input/Output Price, Vision support.

Terminal: PowerShell — python script.py.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If 401 Unauthorized: Check API key is set correctly
- If Empty models list: Your plan may have limited models. Check subscription
- If `jq: command not found`: Install jq: `brew install jq` (Mac) or `apt-get install jq` (Linux)

---

### Slide 328 — Exercise 7.5 — Steps 3–4

**Type:** exercise · **Lesson:** 7.5 · **Exercise:** 7.5

**Script**

Next step — Steps 3–4.

Step 3: Filter models:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "# Models with 100k+ context large_context = [m for m in models if m.get('context_window', 0) >= 100000] # Cheapest by input price cheapest = sorted(models, key=lambda x: x['pricing']['input'])[:5]"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If 401 Unauthorized: Check API key is set correctly
- If Empty models list: Your plan may have limited models. Check subscription
- If `jq: command not found`: Install jq: `brew install jq` (Mac) or `apt-get install jq` (Linux)

---

### Slide 329 — Exercise 7.5 — Steps 3–4 (Part 2)

**Type:** exercise · **Lesson:** 7.5 · **Exercise:** 7.5

**Script**

Next step — Steps 3–4 (Part 2).

Step 4: Model selection helper:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "select_model("code_review", "balanced") # → claude-4.6-sonnet select_model("simple_fix", "low") # → gpt-5-mini select_model("frontend_ui", "high") # → gemini-3.1-pro"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If 401 Unauthorized: Check API key is set correctly
- If Empty models list: Your plan may have limited models. Check subscription
- If `jq: command not found`: Install jq: `brew install jq` (Mac) or `apt-get install jq` (Linux)

---

### Slide 330 — Module Summary

**Type:** module_summary · **Lesson:** 7.5 · **Exercise:** 7.5

**Script**

That completes Module 7. Lesson 7.1, API Landscape — key insight: API selection; Lesson 7.2, Authentication — key insight: Key management; Lesson 7.3, Rate Limits & Errors — key insight: Robust clients; Lesson 7.4, ETag Caching — key insight: Efficient queries; Lesson 7.5, Listing Models — key insight: Auth smoke-test

What will you do differently on Monday? I will take two or three answers before we break or move on.

---

### Slide 331 — Quick Reference Card

**Type:** quick_reference · **Lesson:** 7.5 · **Exercise:** 7.5

**Script**

This quick reference slide is for you to keep after the course — screenshot it or copy the commands into your team wiki.

Quick Reference Card

**Facilitator notes**

- Allow about two minutes for final questions on this module.

---

## Module 8 — Cloud Agents API and Webhooks

### Slide 332 — Cloud Agents API and Webhooks

**Type:** module_intro

**Script**

Module 8 wires Cloud Agents programmatically — create runs, stream events, verify webhooks.

Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.

Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.

Production API work is boring on purpose: auth, retries, caching, verified signatures.

Timing on slide: Cursor Training Program · ~60 min

---

### Slide 333 — Module Overview

**Type:** module_overview

**Script**

The module goal in plain language: Programmatically create, stream, and manage Cloud Agents, and set up webhook notifications

Glance at duration and prerequisites on screen — raise a hand if anything blocks you.

---

### Slide 334 — Learning Objectives

**Type:** learning_objectives

**Script**

These outcomes define success for Module 8 — not a reading list, but skills you will practice.

Highlight three that matter for your role: Create a Cloud Agent programmatically using the API; Stream agent responses in real-time using SSE with resume support; List and download artifacts from a completed agent; plus more on screen.

Next: learning objectives.

Ask who has seen the opposite problem in production — one story beats five bullets.

---

### Slide 335 — Agenda

**Type:** module_agenda

**Script**

Here is how we will spend our time: Lesson 8.1, Creating a Cloud Agent Programmatically, about 15 min; Lesson 8.2, Streaming Agent Responses (SSE), about 15 min; Lesson 8.3, Listing and Downloading Artifacts, about 15 min; Lesson 8.4, Creating a Webhook Endpoint, about 15 min; Lesson 8.5, Testing Webhooks Locally with ngrok, about 13 min; Lesson 8.6, End-to-End Automated Agent Workflow, about 17 min.

**Facilitator notes**

- Announce when the next hands-on block starts so people can close email and open Cursor.

---

### Slide 336 — Lesson 8.1

**Type:** lesson_intro · **Lesson:** 8.1

**Script**

Lesson 8.1: Creating a Cloud Agent Programmatically. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Create a Cloud Agent run using curl or Python.

Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.

Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.

Lab reference: slide-exercises/module-08/exercise-8.1-create-a-cloud-agent-via-api.md

---

### Slide 337 — Agent + Runs

**Type:** table · **Lesson:** 8.1

**Script**

Next: Agent + Runs.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Agent: Durable entity with conversation history and workspace state. Run: Single execution (one prompt/response cycle).

---

### Slide 338 — Request Fields

**Type:** table · **Lesson:** 8.1

**Script**

Next: Request Fields.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): prompt.text: "Add a README.md file". repos[].url: "https://github.com/org/repo".

---

### Slide 339 — Windows Exercise Environment

**Type:** exercise_setup · **Lesson:** 8.1

**Script**

Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

**Facilitator notes**

- Allow two to three minutes. Pair anyone blocked on keys or curl with a neighbor.

---

### Slide 340 — Exercise 8.1 — Create with curl

**Type:** exercise · **Lesson:** 8.1 · **Exercise:** 8.1

**Script**

Starting Exercise 8.1 — Create a Cloud Agent via API. 15 min scheduled.

Create a Cloud Agent run using curl or Python.

The full lab guide with troubleshooting is in slide-exercises/module-08/exercise-8.1-create-a-cloud-agent-via-api.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1 — set API key · Terminal: PowerShell.

Step 2 — create agent · Terminal: PowerShell.

Paste this into the Agent — constraints matter as much as the ask: "$env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx""

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If 401 Unauthorized: Check API key is set correctly
- If 404 Not Found: Repository URL may be incorrect or GitHub not connected
- If 400 Bad Request: Check JSON syntax. Missing quotes or commas

---

### Slide 341 — Exercise 8.1 — Capture IDs

**Type:** exercise · **Lesson:** 8.1 · **Exercise:** 8.1

**Script**

Next step — Capture IDs.

Step 1: Save the JSON from the create-agent call — Terminal: PowerShell.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If 401 Unauthorized: Check API key is set correctly
- If 404 Not Found: Repository URL may be incorrect or GitHub not connected
- If 400 Bad Request: Check JSON syntax. Missing quotes or commas

---

### Slide 342 — Exercise 8.1 — Capture IDs (Part 2)

**Type:** exercise · **Lesson:** 8.1 · **Exercise:** 8.1

**Script**

Next step — Capture IDs (Part 2).

Step 2: Optional model override in create payload — Where: edit JSON before POST (any terminal).

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If 401 Unauthorized: Check API key is set correctly
- If 404 Not Found: Repository URL may be incorrect or GitHub not connected
- If 400 Bad Request: Check JSON syntax. Missing quotes or commas

---

### Slide 343 — Exercise 8.1 — Python Helper

**Type:** exercise · **Lesson:** 8.1 · **Exercise:** 8.1

**Script**

Next step — Python Helper.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If 401 Unauthorized: Check API key is set correctly
- If 404 Not Found: Repository URL may be incorrect or GitHub not connected
- If 400 Bad Request: Check JSON syntax. Missing quotes or commas

---

### Slide 344 — Lesson 8.2

**Type:** lesson_intro · **Lesson:** 8.2

**Script**

Lesson 8.2: Streaming Agent Responses (SSE). Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Stream Cloud Agent events with Server-Sent Events.

Lab reference: slide-exercises/module-08/exercise-8.2-stream-agent-responses-sse.md

---

### Slide 345 — SSE Event Types

**Type:** table · **Lesson:** 8.2

**Script**

Next: SSE Event Types.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Event: When It Happens. Use this when Data Example. status: Run status changes. Use this when {"status":"RUNNING"}. assistant: Agent speaks. Use this when {"text":"I'll read the file..."}. thinking: Agent is reasoning. Use this when {"text":"Let me consider..."}. tool_call: Agent

---

### Slide 346 — Resume Support

**Type:** content · **Lesson:** 8.2

**Script**

Next: Resume Support.

SSE streams support the Last-Event-ID header — if your connection drops, resume from the last received event.

---

### Slide 347 — Exercise 8.2 — Stream with curl

**Type:** exercise · **Lesson:** 8.2 · **Exercise:** 8.2

**Script**

Starting Exercise 8.2 — Stream Agent Responses (SSE). 15 min scheduled.

Stream Cloud Agent events with Server-Sent Events.

The full lab guide with troubleshooting is in slide-exercises/module-08/exercise-8.2-stream-agent-responses-sse.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Terminal: PowerShell.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If No output from curl: Use `-N` flag to disable buffering
- If Connection drops: Implement resume with `Last-Event-ID`
- If Events not parsing: Check JSON format; some events have different structures

---

### Slide 348 — Exercise 8.2 — Python SSE Client

**Type:** exercise · **Lesson:** 8.2 · **Exercise:** 8.2

**Script**

Next step — Python SSE Client.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If No output from curl: Use `-N` flag to disable buffering
- If Connection drops: Implement resume with `Last-Event-ID`
- If Events not parsing: Check JSON format; some events have different structures

---

### Slide 349 — Exercise 8.2 — ResumableSSEClient

**Type:** exercise · **Lesson:** 8.2 · **Exercise:** 8.2

**Script**

Next step — ResumableSSEClient.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If No output from curl: Use `-N` flag to disable buffering
- If Connection drops: Implement resume with `Last-Event-ID`
- If Events not parsing: Check JSON format; some events have different structures

---

### Slide 350 — Lesson 8.3

**Type:** lesson_intro · **Lesson:** 8.3

**Script**

Lesson 8.3: Listing and Downloading Artifacts. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Wait for completion, list artifacts, and download outputs.

Lab reference: slide-exercises/module-08/exercise-8.3-list-and-download-artifacts.md

---

### Slide 351 — Key Endpoints

**Type:** table · **Lesson:** 8.3

**Script**

Next: Key Endpoints.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Endpoint: Method. Use this when Purpose. /v1/agents/{id}/artifacts: GET. Use this when List all artifacts. /v1/agents/{id}/artifacts/download: GET. Use this when Get presigned URL for download.

---

### Slide 352 — Exercise 8.3 — Wait & List

**Type:** exercise · **Lesson:** 8.3 · **Exercise:** 8.3

**Script**

Starting Exercise 8.3 — List and Download Artifacts. 15 min scheduled.

Wait for completion, list artifacts, and download outputs.

The full lab guide with troubleshooting is in slide-exercises/module-08/exercise-8.3-list-and-download-artifacts.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If No artifacts found: Agent may not have produced any. Run agent with browser or file operations
- If Download URL expired: URLs expire after 15 minutes. Generate new URL
- If 404 Not Found: Agent ID may be incorrect or agent may be archived

---

### Slide 353 — Exercise 8.3 — Download

**Type:** exercise · **Lesson:** 8.3 · **Exercise:** 8.3

**Script**

Next step — Download.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If No artifacts found: Agent may not have produced any. Run agent with browser or file operations
- If Download URL expired: URLs expire after 15 minutes. Generate new URL
- If 404 Not Found: Agent ID may be incorrect or agent may be archived

---

### Slide 354 — Exercise 8.3 — CI Integration

**Type:** exercise · **Lesson:** 8.3 · **Exercise:** 8.3

**Script**

Next step — CI Integration.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If No artifacts found: Agent may not have produced any. Run agent with browser or file operations
- If Download URL expired: URLs expire after 15 minutes. Generate new URL
- If 404 Not Found: Agent ID may be incorrect or agent may be archived

---

### Slide 355 — Lesson 8.4

**Type:** lesson_intro · **Lesson:** 8.4

**Script**

Lesson 8.4: Creating a Webhook Endpoint. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Receive webhooks and verify HMAC signatures.

Production API work is boring on purpose: auth, retries, caching, verified signatures.

Windows labs use `$env:VAR` and `curl.exe` — if a command fails, check quoting before re-generating the key.

Lab reference: slide-exercises/module-08/exercise-8.4-webhooks-and-hmac-verification.md

---

### Slide 356 — Webhook Headers

**Type:** table · **Lesson:** 8.4

**Script**

Next: Webhook Headers.

Production API work is boring on purpose: auth, retries, caching, verified signatures.

Windows labs use `$env:VAR` and `curl.exe` — if a command fails, check quoting before re-generating the key.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): X-Webhook-Signature: HMAC-SHA256 signature for verification. X-Webhook-ID: Unique delivery ID. X-Webhook-Event: Event type (statusChange).

---

### Slide 357 — Webhook Payload

**Type:** code · **Lesson:** 8.4

**Script**

Webhook Payload

Focus on the first few lines — for example: {.

Next: Webhook Payload.

Production API work is boring on purpose: auth, retries, caching, verified signatures.

Windows labs use `$env:VAR` and `curl.exe` — if a command fails, check quoting before re-generating the key.

---

### Slide 358 — Exercise 8.4 — HMAC Verification

**Type:** exercise · **Lesson:** 8.4 · **Exercise:** 8.4

**Script**

Starting Exercise 8.4 — Webhooks and HMAC Verification. 15 min scheduled.

Receive webhooks and verify HMAC signatures.

The full lab guide with troubleshooting is in slide-exercises/module-08/exercise-8.4-webhooks-and-hmac-verification.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If Port 5000 in use: Change to different port (e.g., 5001)
- If ngrok not found: Install ngrok from ngrok.com/download
- If Webhook not received: Check ngrok URL is correct and server is running

---

### Slide 359 — Exercise 8.4 — Configure Agent

**Type:** exercise · **Lesson:** 8.4 · **Exercise:** 8.4

**Script**

Next step — Configure Agent.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If Port 5000 in use: Change to different port (e.g., 5001)
- If ngrok not found: Install ngrok from ngrok.com/download
- If Webhook not received: Check ngrok URL is correct and server is running

---

### Slide 360 — Lesson 8.5

**Type:** lesson_intro · **Lesson:** 8.5

**Script**

Lesson 8.5: Testing Webhooks Locally with ngrok. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Expose a local server with ngrok and inspect webhook payloads.

Production API work is boring on purpose: auth, retries, caching, verified signatures.

Windows labs use `$env:VAR` and `curl.exe` — if a command fails, check quoting before re-generating the key.

Lab reference: slide-exercises/module-08/exercise-8.5-test-webhooks-with-ngrok.md

---

### Slide 361 — What Is ngrok?

**Type:** bullets · **Lesson:** 8.5

**Script**

Point 1: Test webhooks without deploying.

Point 2: Debug locally · Demo to stakeholders.

Next: What Is ngrok?.

Ask who has seen the opposite problem in production — one story beats five bullets.

Creates a secure tunnel from a public URL to your local server. - Test webhooks without deploying

---

### Slide 362 — Exercise 8.5 — Steps 1–3

**Type:** exercise · **Lesson:** 8.5 · **Exercise:** 8.5

**Script**

Starting Exercise 8.5 — Test Webhooks with ngrok. 15 min scheduled.

Expose a local server with ngrok and inspect webhook payloads.

The full lab guide with troubleshooting is in slide-exercises/module-08/exercise-8.5-test-webhooks-with-ngrok.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Step 1: Start tunnel:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Paste this into the Agent — constraints matter as much as the ask: "ngrok http 5000 # Forwarding: https://abc123.ngrok.io -> http://localhost:5000"

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If ngrok connection refused: Start ngrok before creating agent
- If Webhook not received: Check ngrok URL is correct (use HTTPS, not HTTP)
- If 404 on webhook: Ensure endpoint path matches (`/webhook/cursor`)

---

### Slide 363 — Exercise 8.5 — Steps 1–3 (Part 2)

**Type:** exercise · **Lesson:** 8.5 · **Exercise:** 8.5

**Script**

Next step — Steps 1–3 (Part 2).

Step 2: Copy HTTPS URL.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If ngrok connection refused: Start ngrok before creating agent
- If Webhook not received: Check ngrok URL is correct (use HTTPS, not HTTP)
- If 404 on webhook: Ensure endpoint path matches (`/webhook/cursor`)

---

### Slide 364 — Exercise 8.5 — Steps 1–3 (Part 3)

**Type:** exercise · **Lesson:** 8.5 · **Exercise:** 8.5

**Script**

Next step — Steps 1–3 (Part 3).

Step 3: Create agent with ngrok URL:.

Terminal: PowerShell — `Ctrl+ `` in Cursor.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If ngrok connection refused: Start ngrok before creating agent
- If Webhook not received: Check ngrok URL is correct (use HTTPS, not HTTP)
- If 404 on webhook: Ensure endpoint path matches (`/webhook/cursor`)

---

### Slide 365 — Exercise 8.5 — Inspect & Replay

**Type:** exercise · **Lesson:** 8.5 · **Exercise:** 8.5

**Script**

Next step — Inspect & Replay.

Step 4: Inspect requests at http://127.0.0.1:4040.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Step 5: Replay failed webhooks (ngrok premium) — inspect raw body and headers.

Terminal: Git Bash or Ubuntu (WSL) — bash syntax required.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If ngrok connection refused: Start ngrok before creating agent
- If Webhook not received: Check ngrok URL is correct (use HTTPS, not HTTP)
- If 404 on webhook: Ensure endpoint path matches (`/webhook/cursor`)

---

### Slide 366 — Lesson 8.6

**Type:** lesson_intro · **Lesson:** 8.6

**Script**

Lesson 8.6: End-to-End Automated Agent Workflow. Participation: listen, participate, or follow along as indicated on the next slides.

---

### Slide 367 — The Capstone Integration

**Type:** content · **Lesson:** 8.6

**Script**

Next: The Capstone Integration.

Combine everything into automated_workflow.py: 1. Create agent (with optional webhook URL) 2. Wait for completion (webhook or polling) 3. Download artifacts 4. Process results (CI exit codes, notifications)

---

### Slide 368 — Workflow Architecture

**Type:** diagram · **Lesson:** 8.6

**Script**

This slide shows Workflow Architecture.

<img src="assets/module-08/workflow-architecture.svg" alt="Workflow Architecture" />

Next: Workflow Architecture.

Workflow Architecture

Trace the diagram once with your finger or cursor — motion helps retention.

---

### Slide 369 — Run the Workflow

**Type:** code · **Lesson:** 8.6

**Script**

Run the Workflow

Focus on the first few lines — for example: export CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx".

Next: Run the Workflow.

---

### Slide 370 — Workflow Output

**Type:** code · **Lesson:** 8.6

**Script**

Success Criteria: Creates agent · waits (webhook/polling) · downloads artifacts · end-to-end run

Focus on the first few lines — for example: 🚀 CLOUD AGENT AUTOMATED WORKFLOW.

Next: Workflow Output.

---

### Slide 371 — Module Summary

**Type:** module_summary · **Lesson:** 8.6

**Script**

That completes Module 8. Lesson 8.1, Creating a Cloud Agent — key insight: Programmatic agent launch; Lesson 8.2, Streaming Agent Responses — key insight: SSE with resume support; Lesson 8.3, Listing and Downloading Artifacts — key insight: CI pipeline integration; Lesson 8.4, Creating a Webhook Endpoint — key insight: HMAC verification; Lesson 8.5, Testing Webhooks with ngrok — key insight: Local tunnel debugging; Lesson 8.6, End-to-End Workflow — key insight: Complete automation

What will you do differently on Monday? I will take two or three answers before we break or move on.

---

### Slide 372 — Quick Reference Card

**Type:** quick_reference · **Lesson:** 8.6

**Script**

This quick reference slide is for you to keep after the course — screenshot it or copy the commands into your team wiki.

Quick Reference Card

**Facilitator notes**

- Allow about two minutes for final questions on this module.

---

## Module 9 — Admin and Analytics APIs

### Slide 373 — Admin and Analytics APIs

**Type:** module_intro

**Script**

Module 9 is admin analytics — who uses Cursor, spend, models. Enterprise audience; pair if someone lacks admin keys.

Timing on slide: Cursor Training Program · ~75 min

---

### Slide 374 — Module Overview

**Type:** module_overview

**Script**

The module goal in plain language: Master team management, usage analytics, cost governance, and safe admin operations

Glance at duration and prerequisites on screen — raise a hand if anything blocks you.

---

### Slide 375 — Learning Objectives

**Type:** learning_objectives

**Script**

These outcomes define success for Module 9 — not a reading list, but skills you will practice.

Highlight three that matter for your role: List and manage team members programmatically; Retrieve daily usage data for cost tracking and reporting; Set user spend limits for budget governance; plus more on screen.

Next: learning objectives.

Ask who has seen the opposite problem in production — one story beats five bullets.

---

### Slide 376 — Agenda

**Type:** module_agenda

**Script**

Here is how we will spend our time: Lesson 9.1, Listing Team Members, about 8 min; Lesson 9.2, Daily Usage Data, about 10 min; Lesson 9.3, Setting User Spend Limits, about 8 min; Lesson 9.4, Model Usage Analytics, about 8 min; Lesson 9.5, Daily Active Users, about 6 min; Lesson 9.6, Leaderboards, about 6 min; Lesson 9.7, Conversation Insights, about 6 min; Lesson 9.8, Destructive Admin Operations, about 6 min.

**Facilitator notes**

- Announce when the next hands-on block starts so people can close email and open Cursor.

---

### Slide 377 — Lesson 9.1

**Type:** lesson_intro · **Lesson:** 9.1

**Script**

Lesson 9.1: Listing Team Members. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: List team members with pagination and export to CSV.

Lab reference: slide-exercises/module-09/exercise-9.1-list-team-members.md

---

### Slide 378 — User vs. Admin API Key

**Type:** table · **Lesson:** 9.1

**Script**

Next: User vs. Admin API Key.

Production API work is boring on purpose: auth, retries, caching, verified signatures.

Windows labs use `$env:VAR` and `curl.exe` — if a command fails, check quoting before re-generating the key.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Scope: Your user only. Use this when Entire organization. Can list members: ❌ No. Use this when ✅ Yes. Can view others' usage: ❌ No. Use this when ✅ Yes. Can modify policies: ❌ No. Use this when ✅ Yes. Format: cursor_xxx.... Use this when cursor_admin_xxx....

---

### Slide 379 — Windows Exercise Environment

**Type:** exercise_setup · **Lesson:** 9.1

**Script**

Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

**Facilitator notes**

- Allow two to three minutes. Pair anyone blocked on keys or curl with a neighbor.

---

### Slide 380 — Exercise 9.1 — Setup & List

**Type:** exercise · **Lesson:** 9.1 · **Exercise:** 9.1

**Script**

Starting Exercise 9.1 — List Team Members. 13 min scheduled.

List team members with pagination and export to CSV.

The full lab guide with troubleshooting is in slide-exercises/module-09/exercise-9.1-list-team-members.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If 401 Unauthorized: Use Admin API key, not User API key
- If 403 Forbidden: Admin API requires Enterprise plan
- If Empty response: Team may have no members (at least one owner should exist)

---

### Slide 381 — Exercise 9.1 — Pagination & Export

**Type:** exercise · **Lesson:** 9.1 · **Exercise:** 9.1

**Script**

Next step — Pagination & Export.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If 401 Unauthorized: Use Admin API key, not User API key
- If 403 Forbidden: Admin API requires Enterprise plan
- If Empty response: Team may have no members (at least one owner should exist)

---

### Slide 382 — Lesson 9.2

**Type:** lesson_intro · **Lesson:** 9.2

**Script**

Lesson 9.2: Daily Usage Data. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Pull daily usage and build a weekly cost report.

Lab reference: slide-exercises/module-09/exercise-9.2-daily-usage-data.md

---

### Slide 383 — Key Endpoint

**Type:** quote · **Lesson:** 9.2

**Script**

Start with the line on screen: "Finance asks: 'What did we spend yesterday?' Engineering leads ask: 'Who's using what?"

Expand in your own words — do not read the bullet text verbatim: GET /v1/admin/analytics/usage/daily Returns:

Next: Key Endpoint.

Pause after the quote — let it land before you add examples.

---

### Slide 384 — Exercise 9.2 — Weekly Usage

**Type:** exercise · **Lesson:** 9.2 · **Exercise:** 9.2

**Script**

Starting Exercise 9.2 — Daily Usage Data. 15 min scheduled.

Pull daily usage and build a weekly cost report.

The full lab guide with troubleshooting is in slide-exercises/module-09/exercise-9.2-daily-usage-data.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If 401 Unauthorized: Use Admin API key, not User API key
- If 403 Forbidden: Admin API requires Enterprise plan
- If No data returned: No activity in date range; try different dates

---

### Slide 385 — Exercise 9.2 — Cost Report

**Type:** exercise · **Lesson:** 9.2 · **Exercise:** 9.2

**Script**

Next step — Cost Report.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If 401 Unauthorized: Use Admin API key, not User API key
- If 403 Forbidden: Admin API requires Enterprise plan
- If No data returned: No activity in date range; try different dates

---

### Slide 386 — Lesson 9.3

**Type:** lesson_intro · **Lesson:** 9.3

**Script**

Lesson 9.3: Setting User Spend Limits. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Set and bulk-update per-user spending limits.

Lab reference: slide-exercises/module-09/exercise-9.3-set-user-spend-limits.md

---

### Slide 387 — Key Endpoint

**Type:** table · **Lesson:** 9.3

**Script**

Next: Key Endpoint.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): alert: Send notification but allow usage. block: Prevent any further requests for the month.

---

### Slide 388 — Exercise 9.3 — Set Limits

**Type:** exercise · **Lesson:** 9.3 · **Exercise:** 9.3

**Script**

Starting Exercise 9.3 — Set User Spend Limits. 13 min scheduled.

Set and bulk-update per-user spending limits.

The full lab guide with troubleshooting is in slide-exercises/module-09/exercise-9.3-set-user-spend-limits.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If 401 Unauthorized: Use Admin API key, not User API key
- If 403 Forbidden: Spend limits require Enterprise plan
- If "User is not a member": Verify email is in your team

---

### Slide 389 — Exercise 9.3 — Bulk Limits

**Type:** exercise · **Lesson:** 9.3 · **Exercise:** 9.3

**Script**

Next step — Bulk Limits.

Paste this into the Agent — constraints matter as much as the ask: "intern@company.com,20,block contractor@company.com,50,alert lead@company.com,200,alert"

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If 401 Unauthorized: Use Admin API key, not User API key
- If 403 Forbidden: Spend limits require Enterprise plan
- If "User is not a member": Verify email is in your team

---

### Slide 390 — Lesson 9.4

**Type:** lesson_intro · **Lesson:** 9.4

**Script**

Lesson 9.4: Model Usage Analytics. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Analyze model usage and identify optimization opportunities.

Lab reference: slide-exercises/module-09/exercise-9.4-model-usage-analytics.md

---

### Slide 391 — Key Endpoint

**Type:** quote · **Lesson:** 9.4

**Script**

Start with the line on screen: "Which models are actually being used? Is Opus worth the cost? Should you train people on cheaper alternatives?"

Expand in your own words — do not read the bullet text verbatim: GET /v1/admin/analytics/usage/models

Next: Key Endpoint.

Pause after the quote — let it land before you add examples.

---

### Slide 392 — Exercise 9.4 — Model Breakdown

**Type:** exercise · **Lesson:** 9.4 · **Exercise:** 9.4

**Script**

Starting Exercise 9.4 — Model Usage Analytics. 13 min scheduled.

Analyze model usage and identify optimization opportunities.

The full lab guide with troubleshooting is in slide-exercises/module-09/exercise-9.4-model-usage-analytics.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If 401 Unauthorized: Use Admin API key
- If 403 Forbidden: Enterprise plan required
- If No data: Check date range and team activity

---

### Slide 393 — Exercise 9.4 — Optimization Report

**Type:** exercise · **Lesson:** 9.4 · **Exercise:** 9.4

**Script**

Next step — Optimization Report.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If 401 Unauthorized: Use Admin API key
- If 403 Forbidden: Enterprise plan required
- If No data: Check date range and team activity

---

### Slide 394 — Lesson 9.5

**Type:** lesson_intro · **Lesson:** 9.5

**Script**

Lesson 9.5: Daily Active Users (DAU). Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Report daily active users over a date range.

Lab reference: slide-exercises/module-09/exercise-9.5-daily-active-users-dau.md

---

### Slide 395 — Why DAU Matters

**Type:** bullets · **Lesson:** 9.5

**Script**

There are 4 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Track adoption after rollout.

Second: Identify unused licenses for reallocation — this one usually matters most in practice.

Also on screen: Measure impact of training sessions, Justify renewal and expansion.

Next: Why DAU Matters.

Ask who has seen the opposite problem in production — one story beats five bullets.

- Track adoption after rollout - Identify unused licenses for reallocation

---

### Slide 396 — Exercise 9.5 — DAU Report

**Type:** exercise · **Lesson:** 9.5 · **Exercise:** 9.5

**Script**

Starting Exercise 9.5 — Daily Active Users (DAU). 10 min scheduled.

Report daily active users over a date range.

The full lab guide with troubleshooting is in slide-exercises/module-09/exercise-9.5-daily-active-users-dau.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If No data: Team may have no activity in date range
- If 403 Forbidden: Enterprise plan required

---

### Slide 397 — Lesson 9.6

**Type:** lesson_intro · **Lesson:** 9.6

**Script**

Lesson 9.6: Leaderboards. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Build leaderboards for tabs, AI lines, and agent runs.

Lab reference: slide-exercises/module-09/exercise-9.6-leaderboards.md

---

### Slide 398 — Responsible Leaderboard Principles

**Type:** table · **Lesson:** 9.6

**Script**

Next: Responsible Leaderboard Principles.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Anonymize: Roles or anonymized names, not full emails. Focus on positive metrics: Show savings, not spending. Opt-in only: Allow users to choose public visibility. Include context: Show team size, role differences.

---

### Slide 399 — Exercise 9.6 — Three Leaderboards

**Type:** exercise · **Lesson:** 9.6 · **Exercise:** 9.6

**Script**

Starting Exercise 9.6 — Leaderboards. 11 min scheduled.

Build leaderboards for tabs, AI lines, and agent runs.

The full lab guide with troubleshooting is in slide-exercises/module-09/exercise-9.6-leaderboards.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If No data: Team may have no activity in date range
- If 403 Forbidden: Enterprise plan required
- If User not found in filter: Check email spelling or user ID format

---

### Slide 400 — Lesson 9.7

**Type:** lesson_intro · **Lesson:** 9.7

**Script**

Lesson 9.7: Conversation Insights. Participation: listen, participate, or follow along as indicated on the next slides.

---

### Slide 401 — What Conversation Insights Reveal

**Type:** bullets · **Lesson:** 9.7

**Script**

There are 4 items on this slide. I'll emphasize the first two, then you can scan the rest.

First: Simple questions vs. complex refactors?.

Second: Most common task categories — this one usually matters most in practice.

Also on screen: Where users get stuck, Which models perform best for which task types.

Next: What Conversation Insights Reveal.

Ask who has seen the opposite problem in production — one story beats five bullets.

- Simple questions vs. complex refactors? - Most common task categories

---

### Slide 402 — Demo: Intent Analysis

**Type:** demo · **Lesson:** 9.7

**Script**

I am going to demonstrate Intent Analysis live on my machine. <img src="assets/module-09/demo-intent-analysis.svg" alt="Demo: Intent Analysis" /> I will narrate each click and keystroke as I go.

When the demo finishes, we will discuss when intent analysis belongs in production workflow and when a lighter-weight approach is enough.

**Facilitator notes**

- If the network fails, describe the expected result and use a screenshot backup.

---

### Slide 403 — Demo: Complexity & Categories

**Type:** demo · **Lesson:** 9.7

**Script**

I am going to demonstrate Complexity & Categories live on my machine. Complexity distribution: - simple 45% · moderate 33% · complex 15% · architectural 7% Category analysis: - backend 40% · frontend 29% · database 15% · devops 10% · security 6% Stuck patterns: conversations >5 min with success: false → suggest training/docs Success Criteria: Understood capabilities · intent/complexity/category tracking · stuck patterns I will narrate each click and keystroke as I go.

When the demo finishes, we will discuss when complexity & categories belongs in production workflow and when a lighter-weight approach is enough.

**Facilitator notes**

- If the network fails, describe the expected result and use a screenshot backup.

---

### Slide 404 — Lesson 9.8

**Type:** lesson_intro · **Lesson:** 9.8

**Script**

Lesson 9.8: Destructive Admin Operations. Participation: listen, participate, or follow along as indicated on the next slides.

---

### Slide 405 — Safe Removal Playbook

**Type:** content · **Lesson:** 9.8

**Script**

Next: Safe Removal Playbook.

1. Audit first — active agents, runs, API keys 2. Soft delete — deactivate (no new agents; existing continue) 3. Transfer ownership — critical agents, webhooks 4. Log everything — compliance audit trail 5. Confirm… (see slide)

---

### Slide 406 — Demo: SafeRemovalDemo Workflow

**Type:** demo · **Lesson:** 9.8

**Script**

I am going to demonstrate SafeRemovalDemo Workflow live on my machine. <img src="assets/module-09/demo-saferemovaldemo-workflow.svg" alt="Demo: SafeRemovalDemo Workflow" /> Bulk deactivation: find users inactive 90+ days → review → notify → deactivate Success Criteria: 5-step pattern · audit-first · soft vs hard delete · resource transfer I will narrate each click and keystroke as I go.

When the demo finishes, we will discuss when saferemovaldemo workflow belongs in production workflow and when a lighter-weight approach is enough.

**Facilitator notes**

- If the network fails, describe the expected result and use a screenshot backup.

---

### Slide 407 — Module Summary

**Type:** module_summary · **Lesson:** 9.8

**Script**

That completes Module 9. Lesson 9.1, Listing Team Members — key insight: Exercise; Lesson 9.2, Daily Usage Data — key insight: Exercise; Lesson 9.3, Setting User Spend Limits — key insight: Exercise; Lesson 9.4, Model Usage Analytics — key insight: Exercise; Lesson 9.5, Daily Active Users — key insight: Exercise; Lesson 9.6, Leaderboards — key insight: Exercise; Lesson 9.7, Conversation Insights — key insight: Demo; Lesson 9.8, Destructive Operations — key insight: Demo

What will you do differently on Monday? I will take two or three answers before we break or move on.

---

### Slide 408 — Quick Reference Card

**Type:** quick_reference · **Lesson:** 9.8

**Script**

This quick reference slide is for you to keep after the course — screenshot it or copy the commands into your team wiki.

Quick Reference Card

**Facilitator notes**

- Allow about two minutes for final questions on this module.

---

## Module 10 — AI Code Tracking and Reporting

### Slide 409 — AI Code Tracking and Reporting

**Type:** module_intro

**Script**

Module 10 closes with AI code tracking — measuring adoption and change, not just vibes.

Timing on slide: Cursor Training Program · ~20 min + take-home

---

### Slide 410 — Module Overview

**Type:** module_overview

**Script**

The module goal in plain language: Track AI vs. human contributions, export metrics to BI tools, build compliance dashboards

Glance at duration and prerequisites on screen — raise a hand if anything blocks you.

---

### Slide 411 — Learning Objectives

**Type:** learning_objectives

**Script**

These outcomes define success for Module 10 — not a reading list, but skills you will practice.

Highlight three that matter for your role: Attribute AI vs. human contributions per commit; Stream metrics to BI tools via CSV export; Access granular AI change events for compliance; plus more on screen.

Next: learning objectives.

Ask who has seen the opposite problem in production — one story beats five bullets.

---

### Slide 412 — Agenda

**Type:** module_agenda

**Script**

Here is how we will spend our time: Lesson 10.1, AI Commit Metrics, about 8 min; Lesson 10.2, Bulk Export via CSV Streaming, about 7 min; Lesson 10.3, Granular AI Change Events, about 7 min; Lesson 10.4, Reporting Dashboard Architecture, about 4 min + take-home.

**Facilitator notes**

- Announce when the next hands-on block starts so people can close email and open Cursor.

---

### Slide 413 — Lesson 10.1

**Type:** lesson_intro · **Lesson:** 10.1

**Script**

Lesson 10.1: AI Commit Metrics. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Fetch AI commit metrics and calculate contribution percentage.

Lab reference: slide-exercises/module-10/exercise-10.1-ai-commit-metrics.md

---

### Slide 414 — Key Endpoint

**Type:** quote · **Lesson:** 10.1

**Script**

Start with the line on screen: "The 'ROI of AI' metric — how much code was AI-generated vs. human-written."

Expand in your own words — do not read the bullet text verbatim: GET /v1/admin/analytics/commits What this measures:

Next: Key Endpoint.

Pause after the quote — let it land before you add examples.

---

### Slide 415 — Windows Exercise Environment

**Type:** exercise_setup · **Lesson:** 10.1

**Script**

Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

**Facilitator notes**

- Allow two to three minutes. Pair anyone blocked on keys or curl with a neighbor.

---

### Slide 416 — Exercise 10.1 — Fetch Metrics

**Type:** exercise · **Lesson:** 10.1 · **Exercise:** 10.1

**Script**

Starting Exercise 10.1 — AI Commit Metrics. 8 min scheduled.

Fetch AI commit metrics and calculate contribution percentage.

The full lab guide with troubleshooting is in slide-exercises/module-10/exercise-10.1-ai-commit-metrics.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If 401 Unauthorized: Use Admin API key
- If 403 Forbidden: AI Code Tracking requires Enterprise plan
- If No data: No commits with AI tracking in date range

---

### Slide 417 — Exercise 10.1 — AI Contribution %

**Type:** exercise · **Lesson:** 10.1 · **Exercise:** 10.1

**Script**

Next step — AI Contribution %.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If 401 Unauthorized: Use Admin API key
- If 403 Forbidden: AI Code Tracking requires Enterprise plan
- If No data: No commits with AI tracking in date range

---

### Slide 418 — Exercise 10.1 — ROI Analysis

**Type:** exercise · **Lesson:** 10.1 · **Exercise:** 10.1

**Script**

Next step — ROI Analysis.

Paste this into the Agent — constraints matter as much as the ask: "AI-generated lines vs. human-written lines (%) Estimated time saved (10 lines/min assumption) Estimated cost saved ($100/hr developer cost) AI usage cost → Net ROI"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If 401 Unauthorized: Use Admin API key
- If 403 Forbidden: AI Code Tracking requires Enterprise plan
- If No data: No commits with AI tracking in date range

---

### Slide 419 — Lesson 10.2

**Type:** lesson_intro · **Lesson:** 10.2

**Script**

Lesson 10.2: Bulk Export via CSV Streaming. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Stream large CSV exports for BI tools.

Lab reference: slide-exercises/module-10/exercise-10.2-bulk-export-via-csv-streaming.md

---

### Slide 420 — Key Endpoint

**Type:** quote · **Lesson:** 10.2

**Script**

Start with the line on screen: "Wire metrics into BI tools (Tableau, PowerBI, Looker, Metabase) without timeouts."

Expand in your own words — do not read the bullet text verbatim: GET /v1/admin/analytics/export/csv (streaming) Export types: commits · events · usage

Next: Key Endpoint.

Pause after the quote — let it land before you add examples.

---

### Slide 421 — Exercise 10.2 — Stream to File

**Type:** exercise · **Lesson:** 10.2 · **Exercise:** 10.2

**Script**

Starting Exercise 10.2 — Bulk Export via CSV Streaming. 7 min scheduled.

Stream large CSV exports for BI tools.

The full lab guide with troubleshooting is in slide-exercises/module-10/exercise-10.2-bulk-export-via-csv-streaming.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If Empty CSV: No data in date range; try longer range
- If Partial download: Use `-L` flag with curl to follow redirects
- If Memory issues: CSV streams; shouldn't cause memory problems

---

### Slide 422 — Exercise 10.2 — BI Integration

**Type:** exercise · **Lesson:** 10.2 · **Exercise:** 10.2

**Script**

Next step — BI Integration.

Paste this into the Agent — constraints matter as much as the ask: "export_for_bi(): bi_commits.csv # commit data bi_events.csv # event data bi_usage.csv # usage data"

Work for about two to four minutes — I'll answer questions when hands go up.

**Facilitator notes**

- If Empty CSV: No data in date range; try longer range
- If Partial download: Use `-L` flag with curl to follow redirects
- If Memory issues: CSV streams; shouldn't cause memory problems

---

### Slide 423 — Lesson 10.3

**Type:** lesson_intro · **Lesson:** 10.3

**Script**

Lesson 10.3: Granular AI Change Events. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Query per-change AI events for compliance reporting.

Lab reference: slide-exercises/module-10/exercise-10.3-granular-ai-change-events.md

---

### Slide 424 — Key Endpoint

**Type:** quote · **Lesson:** 10.3

**Script**

Start with the line on screen: "Essential for SOC2, ISO, and internal audits."

Expand in your own words — do not read the bullet text verbatim: GET /v1/admin/analytics/events Tracks per event:

Next: Key Endpoint.

Pause after the quote — let it land before you add examples.

---

### Slide 425 — Exercise 10.3 — Query Events

**Type:** exercise · **Lesson:** 10.3 · **Exercise:** 10.3

**Script**

Starting Exercise 10.3 — Granular AI Change Events. 7 min scheduled.

Query per-change AI events for compliance reporting.

The full lab guide with troubleshooting is in slide-exercises/module-10/exercise-10.3-granular-ai-change-events.md.

Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. Open the repo folder, not a single file.

Pause here — most groups need a few minutes before the next step.

**Facilitator notes**

- If No data: No AI acceptances in date range
- If Empty metadata: Privacy mode may be enabled
- If 403 Forbidden: Enterprise plan required

---

### Slide 426 — Exercise 10.3 — Compliance Report

**Type:** exercise · **Lesson:** 10.3 · **Exercise:** 10.3

**Script**

Next step — Compliance Report.

Try it now; if you finish early, help a neighbor or refine your follow-up prompt.

**Facilitator notes**

- If No data: No AI acceptances in date range
- If Empty metadata: Privacy mode may be enabled
- If 403 Forbidden: Enterprise plan required

---

### Slide 427 — Lesson 10.4

**Type:** lesson_intro · **Lesson:** 10.4

**Script**

Lesson 10.4: Reporting Dashboard Architecture. Participation: listen, participate, or follow along as indicated on the next slides.

Why this lesson exists: Design a leadership dashboard combining analytics APIs.

Lab reference: slide-exercises/module-10/exercise-10.4-reporting-dashboard-architecture.md

---

### Slide 428 — Dashboard Components

**Type:** table · **Lesson:** 10.4

**Script**

Next: Dashboard Components.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Component: Data Source. Use this when Purpose. Usage Overview: Usage API. Use this when Cost, tokens, active users. AI Contribution: Commits API. Use this when ROI, adoption metrics. Model Performance: Events API. Use this when Acceptance rates, efficiency. Team Activity: Members

---

### Slide 429 — Take-Home: Streamlit Dashboard

**Type:** content · **Lesson:** 10.4

**Script**

Next: Take-Home: Streamlit Dashboard.

Run with: streamlit run cursor_dashboard.py 5 panels: 1. Executive Summary — cost, DAU, AI %, team size 2. Usage Analytics — daily cost trend (Plotly line chart) 3. AI Code Impact — AI vs human… (see slide)

---

### Slide 430 — Project Deliverables

**Type:** table · **Lesson:** 10.4

**Script**

Next: Project Deliverables.

Pick one row that matches your audience's stack and go deep; skim the rest.

Slide reference (skim, do not read every cell): Working dashboard: Streamlit, Metabase, or custom frontend. Documentation: Setup instructions and data source descriptions. One insight: Key finding from your team's data. Export script: Automated CSV export for compliance.

---

### Slide 431 — Module Summary

**Type:** module_summary · **Lesson:** 10.4

**Script**

That completes Module 10. Lesson 10.1, AI Commit Metrics — key insight: ROI calculation; Lesson 10.2, Bulk Export via CSV — key insight: BI integration; Lesson 10.3, Granular Change Events — key insight: Compliance reporting; Lesson 10.4, Dashboard Architecture — key insight: Complete dashboard

What will you do differently on Monday? I will take two or three answers before we break or move on.

---

### Slide 432 — Quick Reference Card

**Type:** quick_reference · **Lesson:** 10.4

**Script**

This quick reference slide is for you to keep after the course — screenshot it or copy the commands into your team wiki.

Quick Reference Card

**Facilitator notes**

- Allow about two minutes for final questions on this module.

---

### Slide 433 — Course Complete

**Type:** module_intro · **Lesson:** 10.4

**Script**

Module 10 closes with AI code tracking — measuring adoption and change, not just vibes.

---
