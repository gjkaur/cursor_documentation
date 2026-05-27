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

This course is roughly seventy percent hands-on and thirty percent concept and discussion. Questions are welcome during a slide if they are quick; save longer ones for breaks or module transitions.

The slide title is: Cursor Training Program.

You will also see the heading: AI-Assisted Development with Cursor.

The slide says: Springpeople · 2-day instructor-led course · Modules 1–10.
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
Here is the full two-day arc for our time together.

Day one builds editor fluency. Module one gives us shared mental models for how AI assistants actually work. Modules two through four are hands-on in the Cursor editor — understanding codebases, making safe changes, working with agent modes, and customizing rules and skills. Module five introduces the CLI for terminal and scripting workflows.

Day two shifts to automation and integration: Cloud Agents in the UI, API authentication and reliability, programmatic Cloud Agent launches and webhooks, admin and analytics reporting, and AI code tracking.

The total scheduled time is about eleven and a half hours across both days, plus breaks. If you have never opened Cursor before, let me know now so I can allow extra setup time in Module two.

The slide title is: Course Agenda.

The slide says: Total: ~11.5 hours across 2 days (hands-on labs + demonstrations).

The table header columns are: Module, Title, Day, Duration.

Table row: **1**, Mental Models for AI-Assisted Development, Day 1, ~60 min.

Table row: **2**, Cursor Editor Essentials, Day 1, ~90 min.

Table row: **3**, Agent Modes and Tools, Day 1, ~60 min.

Table row: **4**, Customizing Cursor for Your Team, Day 1, ~60 min.

Table row: **5**, Cursor CLI and Local Automation, Day 1, ~60 min.

Table row: **6**, Cloud Agents in the UI, Day 2, ~90 min.

Table row: **7**, Cursor API Foundations, Day 2, ~60 min.

Table row: **8**, Cloud Agents API and Webhooks, Day 2, ~60 min.

Table row: **9**, Admin and Analytics APIs, Day 2, ~75 min.

Table row: **10**, AI Code Tracking and Reporting, Day 2, ~20 min.

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.
-->

---







<!-- _header: 'Module 1 — Mental Models for AI-Assisted Development' -->

<!-- _class: lead -->

# Mental Models for AI-Assisted Development

## Module 1 · Day 1 (Foundations)

Cursor Training Program · Concept block · ~60 min

<!--
Welcome to Module 1. This block is about sixty minutes of concepts — keep Cursor closed for now.

We are building vocabulary so tomorrow's hands-on work feels predictable instead of magical.

The slide title is: Mental Models for AI-Assisted Development.

You will also see the heading: Module 1 · Day 1 (Foundations).

The slide says: Cursor Training Program · Concept block · ~60 min.
-->

---







<!-- _class: fit-md -->

## Module Overview

| Aspect            | Details                                                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Duration**      | ~60 minutes                                                                                                       |
| **Format**        | Concept block (foundational theory)                                                                               |
| **Prerequisites** | None – this is the starting point                                                                                 |
| **Module Goal**   | Build accurate mental models of how AI coding assistants work, their limitations, and how to use them effectively |

<!--
Here is the overview for Module 1.

The slide title is: Module Overview.

The table header columns are: Aspect, Details.

In the table, **Duration**: ~60 minutes.

In the table, **Format**: Concept block (foundational theory).

In the table, **Prerequisites**: None – this is the starting point.

In the table, **Module Goal**: Build accurate mental models of how AI coding assistants work, their limitations, and how to use them effectively.
-->

---



<!-- _class: lead -->

# Lesson 1.1

## How AI Models Work

_Concept · 12 minutes_

<!--
Lesson 1.1: How AI Models Work. Concept · 12 minutes For this lesson, listen and take notes — you do not need to type along yet.

In this lesson we look under the hood at how large language models actually produce text. You won't need Cursor open yet — just listen and connect this to the Agent behavior you'll see all day tomorrow.

The key takeaway is this: the same prompt can produce different code on different runs. That is normal, not a broken tool.

The slide title is: Lesson 1.1.

You will also see the heading: How AI Models Work.

The slide says: _Concept · 12 minutes_.
-->

---







## Why Outputs Are Probabilistic

> Unlike traditional software that gives the same output for the same input, AI models generate responses based on **probability distributions**.

At its simplest, an LLM is a **next-token prediction engine**.

Given a sequence of tokens, it predicts what comes next — then samples, appends, repeats.

<!--
This slide highlights a key quote — Why Outputs Are Probabilistic.

The slide title is: Why Outputs Are Probabilistic.

The slide quotes: "Unlike traditional software that gives the same output for the same input, AI models generate responses based on probability distributions."

The slide says: At its simplest, an LLM is a next-token prediction engine.

The slide says: Given a sequence of tokens, it predicts what comes next — then samples, appends, repeats.

Terms on this slide — quick definitions for the room:

Next-token prediction means the model reads everything so far, ranks likely next pieces of text, picks one, appends it, and repeats.

Probabilistic means the same input can produce different outputs — unlike traditional code that always returns the same result.

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.

LLM stands for Large Language Model — a neural network trained to generate text one token at a time.

Run the same unit test twice and you get the same result every time. Run the same prompt in Cursor twice and you may get different wording, structure, or even logic.

An LLM is not executing a program you wrote. It predicts the next token, samples one, appends it, and repeats — millions of times per answer. That is why we never treat a single Agent run as final without review.
-->

---







<!-- _class: fit-sm -->

## Next-Token Prediction

<img src="assets/module-01/next-token-prediction.svg" alt="Next-token prediction probabilities" />

<!--
This slide includes a diagram — Next-Token Prediction.

The slide title is: Next-Token Prediction.

The figure on this slide is titled: Next-token prediction probabilities.

Terms on this slide — quick definitions for the room:

Next-token prediction means the model reads everything so far, ranks likely next pieces of text, picks one, appends it, and repeats.

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.

Look at the diagram. The model reads everything so far, ranks possible next tokens by probability, picks one, appends it, and runs the loop again. That is the entire answer — autocomplete at scale.

It can feel like reasoning, but the mechanism is still pattern completion. Keeping that in mind will save you hours of false expectations later today.
-->

---







<!-- _class: fit-md -->

## Traditional Code vs. AI Model

| Traditional Code                         | AI Model                                   |
| ---------------------------------------- | ------------------------------------------ |
| Deterministic (same input → same output) | Probabilistic (different outputs possible) |
| You control the logic                    | You influence, but don't control           |
| Errors are bugs                          | Errors are features of probability         |
| Predictable behavior                     | Needs management via parameters            |

<!--
This slide is a table — Traditional Code vs. AI Model.

The slide title is: Traditional Code vs. AI Model.

The table header columns are: Traditional Code, AI Model.

In the table, Deterministic (same input → same output): Probabilistic (different outputs possible).

In the table, You control the logic: You influence, but don't control.

In the table, Errors are bugs: Errors are features of probability.

In the table, Predictable behavior: Needs management via parameters.

Terms on this slide — quick definitions for the room:

Probabilistic means the same input can produce different outputs — unlike traditional code that always returns the same result.

Deterministic means the same input always produces the same output — how conventional software behaves.

Traditional software is deterministic — same input, same output. You own every branch and bug fix.

AI models are probabilistic — you influence them through prompts, context, and settings, but you do not fully control them.
-->

---







## Traditional vs. AI — Implication

**Implication:** Never trust a single run as ground truth.

<!--
Let's look at Traditional vs. AI — Implication.

The slide title is: Traditional vs. AI — Implication.

The implication on the slide: Never trust a single run as ground truth..

The practical rule is on the slide: never trust a single run as ground truth. Run the code, read the diff, check the docs — every time.

Teams that skip verification accumulate AI debt — code that looked fine in chat but fails in CI.
-->

---







<!-- _class: fit-sm -->

## What Determines AI Output?

<img src="assets/module-01/factors-output.svg" alt="Factors that shape AI output" />

<!--
This slide includes a diagram — What Determines AI Output?.

The slide title is: What Determines AI Output?.

The figure on this slide is titled: Factors that shape AI output.

When output quality drops, walk through these inputs: your prompt, system instructions, open files, model choice, and parameters like temperature. One of them changed — not necessarily the model itself.

Before you switch models, compare today's prompt and attachments to yesterday's session. That diff often explains the regression.
-->

---







## Key Parameters You Control

| Parameter       | What It Does                                 | Best For                              |
| --------------- | -------------------------------------------- | ------------------------------------- |
| **Temperature** | Randomness (0 = deterministic, 1 = creative) | Bug fixes (low), brainstorming (high) |
| **Top-p**       | Nucleus sampling – limits token pool         | Balanced responses                    |
| **Max Tokens**  | Limits response length                       | Controlling cost                      |

<!--
This slide is a table — Key Parameters You Control.

The slide title is: Key Parameters You Control.

The table header columns are: Parameter, What It Does, Best For.

In the table, **Temperature** — Randomness (0 = deterministic, 1 = creative). Use case on slide: Bug fixes (low), brainstorming (high).

In the table, **Top-p** — Nucleus sampling – limits token pool. Use case on slide: Balanced responses.

In the table, **Max Tokens** — Limits response length. Use case on slide: Controlling cost.

Terms on this slide — quick definitions for the room:

Deterministic means the same input always produces the same output — how conventional software behaves.

Temperature controls randomness — low values stay focused and repeatable; high values add creativity and variation.

Max tokens caps how long the model's answer can be — useful for controlling cost and verbosity.

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.

Top-p, also called nucleus sampling, limits the pool of tokens the model may choose from on each step.

Temperature controls randomness — keep it low for bug fixes, slightly higher for brainstorming, then back down before you merge.

Top-p and max tokens shape breadth and length. Two teammates with the same prompt can still differ if their settings differ.
-->

---







## Key Parameters — Example Values

```python
temperature: 0.2   # focused
top_p: 0.9         # balanced
max_tokens: 4000   # cap length
```

<!--
The slide title is: Key Parameters — Example Values.

The code on the slide reads: temperature: 0.2   # focused top_p: 0.9         # balanced max_tokens: 4000   # cap length.

Terms on this slide — quick definitions for the room:

Temperature controls randomness — low values stay focused and repeatable; high values add creativity and variation.
-->

---







<!-- _class: fit-xs -->

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
The slide title is: Temperature Impact.

You will also see the heading: Temperature 0.1 — very deterministic.

You will also see the heading: Temperature 0.7 — balanced (adds edge cases).

You will also see the heading: Temperature 1.2 — creative, potentially unstable.

The slide says: Same prompt: _"Write a function to reverse a string"_.

The code on the slide reads: # Temperature 0.1 — very deterministic def reverse_string(s):     return s[::-1] # Temperature 0.7 — balanced (adds edge cases) def reverse_string(s):     if not s: return s     return s[::-1] # Temperature 1.2 — creative, potentially unstable def flip_the_text(text): ....

Terms on this slide — quick definitions for the room:

Deterministic means the same input always produces the same output — how conventional software behaves.

Temperature controls randomness — low values stay focused and repeatable; high values add creativity and variation.

Same ask, three temperatures on the slide. Notice low temperature stays close to the obvious solution; high temperature adds variation — and sometimes instability you do not want in production code.
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
This slide lists key points under The Training Gap.

The slide title is: The Training Gap.

The slide says: Models are frozen at their training cutoff date. They don't know:.

The implication on the slide: You must provide this information in the prompt or context..

Bullet 1 on the slide: Code written after their training date.

Bullet 2 on the slide: Your company's internal APIs.

Bullet 3 on the slide: Your specific architecture decisions.

Bullet 4 on the slide: Recent library updates (unless in context).

Terms on this slide — quick definitions for the room:

Training cutoff is the date the model's knowledge was frozen — it will not know about releases after that unless you add context.

Models are frozen at a training cutoff. They do not automatically know your internal APIs, your architecture decisions, or libraries released last month unless you put that information in context.

If the Agent guesses wrong about your stack, the fix is usually better context — not a different model.
-->

---



<!-- _class: lead -->

# Lesson 1.2

## Hallucinations

_Concept · 10 minutes_

<!--
Lesson 1.2: Hallucinations. Concept · 10 minutes For this lesson, listen and take notes — you do not need to type along yet.

The slide title is: Lesson 1.2.

You will also see the heading: Hallucinations.

The slide says: _Concept · 10 minutes_.

Terms on this slide — quick definitions for the room:

A hallucination is a confident answer that is wrong — for example an API or library that does not exist.
-->

---







## What Are Hallucinations?

> Confident-sounding outputs that are **factually wrong**, made up, or don't exist.

Most dangerous form: the model sounds **completely confident** while being **completely wrong**.

<!--
This slide highlights a key quote — What Are Hallucinations?.

The slide title is: What Are Hallucinations?.

The slide quotes: "Confident-sounding outputs that are factually wrong, made up, or don't exist."

The slide says: Most dangerous form: the model sounds completely confident while being completely wrong.

Terms on this slide — quick definitions for the room:

A hallucination is a confident answer that is wrong — for example an API or library that does not exist.

A hallucination is a confident answer that is wrong — a library that does not exist, a method that was never in the API, outdated syntax presented as current best practice.

The danger is the tone: the model sounds as sure as a senior engineer in a code review.
-->

---







<!-- _class: fit-md -->

## Hallucinations in Code

| Type                   | Example                        | How to Spot               |
| ---------------------- | ------------------------------ | ------------------------- |
| **Fake APIs**          | `import nonexistent_library`   | Check docs; import fails  |
| **Wrong parameters**   | Incorrect function signature   | Type checking             |
| **Invented methods**   | `list.reverse_in_place()`      | Know the standard library |
| **Confident nonsense** | "This is the standard way to…" | Cross-reference           |
| **Outdated syntax**    | Old Python 2 style             | Know version differences  |

<!--
This slide is a table — Hallucinations in Code.

The slide title is: Hallucinations in Code.

The table header columns are: Type, Example, How to Spot.

In the table, **Fake APIs** — `import nonexistent_library`. Use case on slide: Check docs; import fails.

In the table, **Wrong parameters** — Incorrect function signature. Use case on slide: Type checking.

In the table, **Invented methods** — `list.reverse_in_place()`. Use case on slide: Know the standard library.

In the table, **Confident nonsense** — "This is the standard way to…". Use case on slide: Cross-reference.

In the table, **Outdated syntax** — Old Python 2 style. Use case on slide: Know version differences.

Terms on this slide — quick definitions for the room:

A hallucination is a confident answer that is wrong — for example an API or library that does not exist.

Fake imports and invented methods show up constantly. Your fastest checks are: does it import, does the type checker agree, does the official doc mention this API?

Build a team habit: if the Agent cites an API, someone verifies it before merge.
-->

---







<!-- _class: fit-sm -->

## Why Models Hallucinate

<img src="assets/module-01/hallucination-causes.svg" alt="Root causes of hallucination" />

<!--
This slide includes a diagram — Why Models Hallucinate.

The slide title is: Why Models Hallucinate.

The figure on this slide is titled: Root causes of hallucination.

Terms on this slide — quick definitions for the room:

A hallucination is a confident answer that is wrong — for example an API or library that does not exist.
-->

---







<!-- _class: fit-xs -->

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
The slide title is: Example: Confident Wrong.

You will also see the heading: Hallucinated (confident, wrong).

You will also see the heading: Reality: requests does NOT have async support..

You will also see the heading: Correct answer: Use httpx or aiohttp.

The code on the slide reads: User: "How do I use requests for async calls?" # Hallucinated (confident, wrong) import requests.async as async_requests response = await async_requests.get('https://api.example.com') # Reality: requests does NOT have async support. # Correct answer: Use httpx or aiohttp.

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-sm -->

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
This slide is a table — Hallucination Mitigation Strategies.

The slide title is: Hallucination Mitigation Strategies.

The table header columns are: Strategy, How It Works, Example.

In the table, **Grounding** — Provide source material. Use case on slide: Paste library docs into context.

In the table, **Verification** — Ask for citations. Use case on slide: "Which line of the docs shows this?".

In the table, **Constrained decoding** — Limit possible outputs. Use case on slide: JSON mode, regex patterns.

In the table, **Self-consistency** — Ask multiple times, compare. Use case on slide: Run same prompt 3×, take majority.

In the table, **Low temperature** — Reduce randomness. Use case on slide: `temperature: 0.1`.

In the table, **Tool use** — Let model search/lookup. Use case on slide: Enable web search for docs.

Terms on this slide — quick definitions for the room:

Constrained decoding restricts output shape — for example JSON mode or regex patterns the model must follow.

Self-consistency means running the same prompt several times and comparing or voting on answers to reduce random errors.

A hallucination is a confident answer that is wrong — for example an API or library that does not exist.

Temperature controls randomness — low values stay focused and repeatable; high values add creativity and variation.

Grounding means giving the model source material — files, docs, or URLs — so answers stay tied to facts instead of guesses.

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.

Ground the model with docs and @mentions. Ask it to cite sources. Use structured outputs when you need predictable shape.

Which of these can your team adopt Monday — paste docs, require citations, or JSON-only responses for scripts?
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
This slide lists key points under Hallucination Detection Checklist.

The slide title is: Hallucination Detection Checklist.

The slide says: Before accepting AI-generated code, verify:.

Bullet 1 on the slide: Do the imported libraries exist?.

Bullet 2 on the slide: Are function signatures correct?.

Bullet 3 on the slide: Does the syntax match my language version?.

Bullet 4 on the slide: Are there obvious logic errors?.

Bullet 5 on the slide: Would this code actually run?.

Bullet 6 on the slide: Does the model cite sources you can verify?.

Terms on this slide — quick definitions for the room:

A hallucination is a confident answer that is wrong — for example an API or library that does not exist.
-->

---







## The Developer's Mindset

> _"Trust, but verify – especially when the AI sounds most confident."_

- Hallucinations decrease with better prompts and context
- They never fully disappear
- You are the human-in-the-loop responsible for verification
- Experience helps you "smell" potential hallucinations

<!--
This slide highlights a key quote — The Developer's Mindset.

The slide title is: The Developer's Mindset.

The slide quotes: "_"Trust, but verify – especially when the AI sounds most confident."_"

Bullet 1 on the slide: Hallucinations decrease with better prompts and context.

Bullet 2 on the slide: They never fully disappear.

Bullet 3 on the slide: You are the human-in-the-loop responsible for verification.

Bullet 4 on the slide: Experience helps you "smell" potential hallucinations.

Terms on this slide — quick definitions for the room:

Human-in-the-loop means a person reviews AI output before it ships — the safety pattern we use throughout this course.

A hallucination is a confident answer that is wrong — for example an API or library that does not exist.
-->

---



<!-- _class: lead -->

# Lesson 1.3

## Tokens and Pricing

_Concept · 10 minutes_

<!--
Lesson 1.3: Tokens and Pricing. Concept · 10 minutes For this lesson, listen and take notes — you do not need to type along yet.

Tokens are how models meter context and cost — roughly three quarters of a word in English.

Small chat prompts are cheap; agent loops over large repos are not. Narrow context saves money and often improves quality.

The slide title is: Lesson 1.3.

You will also see the heading: Tokens and Pricing.

The slide says: _Concept · 10 minutes_.

Terms on this slide — quick definitions for the room:

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.
-->

---







<!-- _class: fit-md -->

## What Is a Token?

| Language | Example                     | Token Count                  |
| -------- | --------------------------- | ---------------------------- |
| English  | "Hello world"               | 2 tokens (~0.75 words/token) |
| English  | "Congratulations"           | 1 token                      |
| Code     | `function calculateTotal()` | ~5 tokens (~2–4 chars/token) |
| Chinese  | "你好世界"                  | 4–8 tokens                   |

<!--
This slide is a table — What Is a Token?.

The slide title is: What Is a Token?.

The table header columns are: Language, Example, Token Count.

In the table, English — "Hello world". Use case on slide: 2 tokens (~0.75 words/token).

In the table, English — "Congratulations". Use case on slide: 1 token.

In the table, Code — `function calculateTotal()`. Use case on slide: ~5 tokens (~2–4 chars/token).

In the table, Chinese — "你好世界". Use case on slide: 4–8 tokens.

Terms on this slide — quick definitions for the room:

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.

Tokens are how models meter context and cost — roughly three quarters of a word in English.

Small chat prompts are cheap; agent loops over large repos are not. Narrow context saves money and often improves quality.
-->

---







## Why Tokens Matter

A token is the atomic unit of processing for LLMs — not a word, not a character.

You pay per token · Context windows are measured in tokens · Token limits determine how much code the AI can "see"

<!--
Let's look at Why Tokens Matter.

The slide title is: Why Tokens Matter.

The slide says: A token is the atomic unit of processing for LLMs — not a word, not a character.

The slide says: You pay per token · Context windows are measured in tokens · Token limits determine how much code the AI can "see".

Terms on this slide — quick definitions for the room:

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.
-->

---







## Input vs. Output Pricing

**Input tokens** (prompt, code context, retrieved docs) cost **less** than **output tokens** (generated code and explanations).

Output is often **5–8× more expensive** — generation is more compute-intensive than reading.

<!--
Let's look at Input vs. Output Pricing.

The slide title is: Input vs. Output Pricing.

The slide says: Input tokens (prompt, code context, retrieved docs) cost less than output tokens (generated code and explanations).

The slide says: Output is often 5–8× more expensive — generation is more compute-intensive than reading.

Terms on this slide — quick definitions for the room:

Output tokens are the text the model generates — explanations and code — and they typically cost more than input.

Input tokens are the prompt, attached files, and instructions you send — they usually cost less than generated output.
-->

---







<!-- _class: fit-xs -->

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
This slide is a table — Model Pricing Examples.

The slide title is: Model Pricing Examples.

Table row: Model, Input (per 1M), Output (per 1M), Output/Input.

Table row: GPT-5 Mini, $0.25, $2.00, 8×.

Table row: Claude 4.5 Haiku, $1.00, $5.00, 5×.

Table row: GPT-5.3 Codex, $1.75, $14.00, 8×.

Table row: Gemini 3.1 Pro, $2.00, $12.00, 6×.

Table row: Claude 4.6 Sonnet, $3.00, $15.00, 5×.

Table row: Claude 4.7 Opus, $5.00, $25.00, 5×.

Table row: GPT-5.5, $5.00, $30.00, 6×.
-->

---







<!-- _class: fit-md -->

## What 1 Million Tokens Looks Like

| Content Type         | Approximate Amount            |
| -------------------- | ----------------------------- |
| Plain English text   | ~750,000 words (~1,500 pages) |
| Python code          | ~250,000–500,000 lines        |
| Average conversation | 5–10 sessions                 |
| Full codebase        | Small to medium project       |

<!--
This slide is a table — What 1 Million Tokens Looks Like.

The slide title is: What 1 Million Tokens Looks Like.

In the table, Content Type: Approximate Amount.

In the table, Plain English text: ~750,000 words (~1,500 pages).

In the table, Python code: ~250,000–500,000 lines.

In the table, Average conversation: 5–10 sessions.

In the table, Full codebase: Small to medium project.

Terms on this slide — quick definitions for the room:

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.
-->

---







<!-- _class: fit-xs -->

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
The slide title is: Cost Calculation Example.

The code on the slide reads: prompt_tokens = 5000    # instructions + context output_tokens = 2000    # AI response model = "claude-4.6-sonnet" input_price  = 3.00     # per 1M tokens output_price = 15.00    # per 1M tokens input_cost  = (5000 / 1_000_000) * 3.00 output_cost = (2000 / 1_000_000) * 15.00 total_cost  = input_cost + output_cost   # ~$0.045 (4.5 cents).

Terms on this slide — quick definitions for the room:

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.

Bound your tasks: specific @mentions, clear stop conditions, checkpoints before long agent runs.

A five-minute agent loop on two files beats a twenty-minute loop on the whole tree.
-->

---







<!-- _class: fit-sm -->

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
This slide is a table — Cost Optimization Strategies.

The slide title is: Cost Optimization Strategies.

The table header columns are: Strategy, How It Works, Impact.

In the table, **Use cheaper models** — Mini/Haiku for simple tasks. Use case on slide: 5–20× reduction.

In the table, **Reduce context** — Only send relevant code. Use case on slide: 2–5× reduction.

In the table, **Cache responses** — Reuse common answers. Use case on slide: Variable.

In the table, **Batch operations** — Combine multiple tasks. Use case on slide: 30–50% reduction.

In the table, **Monitor usage** — Track spending per user. Use case on slide: Prevents surprises.

In the table, **Set limits** — Monthly spending caps. Use case on slide: Budget protection.

Bound your tasks: specific @mentions, clear stop conditions, checkpoints before long agent runs.

A five-minute agent loop on two files beats a twenty-minute loop on the whole tree.
-->

---







<!-- _class: fit-md -->

## Real-World Cost Bounds

| Usage Level | Monthly Cost | What You Can Do                          |
| ----------- | ------------ | ---------------------------------------- |
| Light       | $10–20       | Occasional questions, small fixes        |
| Medium      | $50–100      | Daily coding, regular agent use          |
| Heavy       | $200–500     | Full-time AI assistance, multiple agents |
| Enterprise  | $1000+       | Team usage, automation, CI/CD            |

<!--
This slide is a table — Real-World Cost Bounds.

The slide title is: Real-World Cost Bounds.

In the table, Usage Level — Monthly Cost. Use case on slide: What You Can Do.

In the table, Light — $10–20. Use case on slide: Occasional questions, small fixes.

In the table, Medium — $50–100. Use case on slide: Daily coding, regular agent use.

In the table, Heavy — $200–500. Use case on slide: Full-time AI assistance, multiple agents.

In the table, Enterprise — $1000+. Use case on slide: Team usage, automation, CI/CD.

Terms on this slide — quick definitions for the room:

CI/CD stands for Continuous Integration and Continuous Deployment — automated build, test, and release pipelines.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-md -->

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
The slide title is: The Cache Effect.

You will also see the heading: First request  → pays full input price.

You will also see the heading: Second request → same context → pays cache read price.

The slide says: Models can cache frequently used content:.

The slide says: Context discipline = cost discipline.

Bullet 1 on the slide: Cache Write: Cost to initially store.

Bullet 2 on the slide: Cache Read: Much cheaper than fresh input (80–95% savings).

The code on the slide reads: # First request  → pays full input price # Second request → same context → pays cache read price.
-->

---



<!-- _class: lead -->

# Lesson 1.4

## Context

_Concept · 12 minutes · The single most valuable AI skill_

<!--
Lesson 1.4: Context. Concept · 12 minutes · The single most valuable AI skill For this lesson, listen and take notes — you do not need to type along yet.

The slide title is: Lesson 1.4.

You will also see the heading: Context.

The slide says: _Concept · 12 minutes · The single most valuable AI skill_.
-->

---







<!-- _class: fit-sm -->

## What Is Context?

Context = all the information the model has access to when generating a response.

<img src="assets/module-01/context-inputs.svg" alt="What goes into context" />

<!--
This slide includes a diagram — What Is Context?.

The slide title is: What Is Context?.

The slide says: Context = all the information the model has access to when generating a response.

The figure on this slide is titled: What goes into context.
-->

---







## The Context Window Limit

| Model                            | Context Window | Pages of Text | Lines of Code |
| -------------------------------- | -------------: | ------------: | ------------: |
| Claude 4 (Haiku / Sonnet / Opus) |           200k |          ~150 |       ~50,000 |
| GPT-5 Mini / GPT-5.3 Codex       |           272k |          ~200 |       ~70,000 |

<!--
This slide is a table — The Context Window Limit.

The slide title is: The Context Window Limit.

Table row: Model, Context Window, Pages of Text, Lines of Code.

Table row: Claude 4 (Haiku / Sonnet / Opus), 200k, ~150, ~50,000.

Table row: GPT-5 Mini / GPT-5.3 Codex, 272k, ~200, ~70,000.

Terms on this slide — quick definitions for the room:

Context window is the maximum amount of text the model can consider at once — when you exceed it, older content drops off.
-->

---







## Context Window — What Happens When Full

**When you exceed context:** Oldest content gets truncated · Critical information may be dropped

**Context engineering** = knowing what to put in, what to leave out, and how to structure it.

<!--
Let's look at Context Window — What Happens When Full.

The slide title is: Context Window — What Happens When Full.

The slide says: When you exceed context: Oldest content gets truncated · Critical information may be dropped.

The slide says: Context engineering = knowing what to put in, what to leave out, and how to structure it.

Terms on this slide — quick definitions for the room:

Context engineering is deliberately choosing what files, rules, and history you include — and what you leave out.

Context window is the maximum amount of text the model can consider at once — when you exceed it, older content drops off.
-->

---







<!-- _class: fit-md -->

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
This slide lists key points under Context Checklist.

The slide title is: Context Checklist.

The slide says: Before every AI interaction, ask:.

Bullet 1 on the slide: What problem am I trying to solve?.

Bullet 2 on the slide: What files/code does the model need to see?.

Bullet 3 on the slide: What would a human need to know to help me?.

Bullet 4 on the slide: What information can I safely leave out?.

Bullet 5 on the slide: Is my context under the token limit?.

Bullet 6 on the slide: Have I included relevant error messages?.

Bullet 7 on the slide: Have I specified constraints (libraries, version, style)?.

Terms on this slide — quick definitions for the room:

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.
-->

---







## Good vs. Bad Context — Bad Example

**BAD (vague):**

```
"Fix this bug: my code doesn't work"
```

<!--
The slide title is: Good vs. Bad Context — Bad Example.

The slide says: BAD (vague):.

The code on the slide reads: "Fix this bug: my code doesn't work".
-->

---







<!-- _class: fit-md -->

## Good vs. Bad Context — Good Example

**GOOD (specific):**

```
Python function sorts dicts by key but raises KeyError.
Code: def sort_by_key(data, key): ...
Input: [{'name': 'Alice'}, {'age': 30}]
Using Python 3.11. Expected: skip dicts without the key.
```

<!--
The slide title is: Good vs. Bad Context — Good Example.

The slide says: GOOD (specific):.

The code on the slide reads: Python function sorts dicts by key but raises KeyError. Code: def sort_by_key(data, key): ... Input: [{'name': 'Alice'}, {'age': 30}] Using Python 3.11. Expected: skip dicts without the key..
-->

---







<!-- _class: fit-sm -->

## Context Prioritization Pyramid

<img src="assets/module-01/context-pyramid.svg" alt="Context prioritization pyramid" />

<!--
This slide includes a diagram — Context Prioritization Pyramid.

The slide title is: Context Prioritization Pyramid.

The figure on this slide is titled: Context prioritization pyramid.

Not all context is equal. Recent messages, open files, and rules compete for the same token budget. Three precise @mentions beat ten files attached just in case.
-->

---







<!-- _class: fit-md -->

## Context Window Management

| Strategy                | How It Works                         | When to Use          |
| ----------------------- | ------------------------------------ | -------------------- |
| **Summarization**       | Compress earlier conversation        | Long sessions        |
| **Selective inclusion** | Only relevant files                  | Large codebases      |
| **Chunking**            | Split across multiple calls          | Exceeding limit      |
| **Hierarchical**        | Summaries + details on demand        | Complex projects     |
| **Vector retrieval**    | Semantic search for relevant context | Very large codebases |

<!--
This slide is a table — Context Window Management.

The slide title is: Context Window Management.

The table header columns are: Strategy, How It Works, When to Use.

In the table, **Summarization** — Compress earlier conversation. Use case on slide: Long sessions.

In the table, **Selective inclusion** — Only relevant files. Use case on slide: Large codebases.

In the table, **Chunking** — Split across multiple calls. Use case on slide: Exceeding limit.

In the table, **Hierarchical** — Summaries + details on demand. Use case on slide: Complex projects.

In the table, **Vector retrieval** — Semantic search for relevant context. Use case on slide: Very large codebases.

Terms on this slide — quick definitions for the room:

Vector retrieval stores embeddings of text so similar concepts can be found even when wording differs.

Semantic search finds relevant code or docs by meaning, not just exact keyword matches.

Context window is the maximum amount of text the model can consider at once — when you exceed it, older content drops off.
-->

---







<!-- _class: fit-xs -->

## The "Lost in the Middle" Problem

Models pay **most attention to the beginning and end** of context, and **less to the middle**.

<img src="assets/module-01/lost-in-middle.svg" alt="Lost in the middle attention chart" />

**Implication:** Put critical information at the beginning OR end, not the middle.

<!--
This slide includes a diagram — The "Lost in the Middle" Problem.

The slide title is: The "Lost in the Middle" Problem.

The slide says: Models pay most attention to the beginning and end of context, and less to the middle.

The implication on the slide: Put critical information at the beginning OR end, not the middle..

The figure on this slide is titled: Lost in the middle attention chart.

Terms on this slide — quick definitions for the room:

Lost in the middle is the tendency for models to pay less attention to information buried in the middle of a long context.

Models attend strongly to the beginning and end of context and weaker to the middle. Put critical constraints at the top of your prompt and repeat them after large pasted logs.
-->

---



<!-- _class: lead -->

# Lesson 1.5

## Tool Calling and MCP

_Concept · 8 minutes_

<!--
Lesson 1.5: Tool Calling and MCP. Concept · 8 minutes For this lesson, listen and take notes — you do not need to type along yet.

Tool calling is how the model stops guessing and starts acting — read a file, run a terminal command, fetch a URL.

Plain chat only produces text. Tools close the loop with real feedback from your environment.

MCP is standard plumbing for connecting Cursor to databases, browsers, and internal services — one protocol instead of a custom integration per tool.

The slide title is: Lesson 1.5.

You will also see the heading: Tool Calling and MCP.

The slide says: _Concept · 8 minutes_.

Terms on this slide — quick definitions for the room:

Tool calling means the model requests an action — read a file, run a command — and the host executes it; the model does not run code itself.

MCP stands for Model Context Protocol — a standard for connecting AI assistants to external tools, databases, and APIs.
-->

---







<!-- _class: fit-xs -->

## What Is Tool Calling?

Tool calling (function calling) lets the AI request execution of external functions.

The AI **doesn't execute code** — it outputs a structured request that **your system** executes.

<img src="assets/module-01/tool-calling-flow.svg" alt="Tool calling flow" />

<!--
This slide includes a diagram — What Is Tool Calling?.

The slide title is: What Is Tool Calling?.

The slide says: Tool calling (function calling) lets the AI request execution of external functions.

The slide says: The AI doesn't execute code — it outputs a structured request that your system executes.

The figure on this slide is titled: Tool calling flow.

Terms on this slide — quick definitions for the room:

Tool calling means the model requests an action — read a file, run a command — and the host executes it; the model does not run code itself.

Tool calling is how the model stops guessing and starts acting — read a file, run a terminal command, fetch a URL.

Plain chat only produces text. Tools close the loop with real feedback from your environment.
-->

---







<!-- _class: fit-sm -->

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
This slide is a table — Common Tool Types in Development.

The slide title is: Common Tool Types in Development.

The table header columns are: Tool, Purpose, Example.

In the table, **read_file** — Read code files. Use case on slide: "Show me the auth module".

In the table, **edit_file** — Modify code. Use case on slide: "Add error handling to line 42".

In the table, **search_code** — Find patterns. Use case on slide: "Find all uses of this function".

In the table, **run_terminal** — Execute commands. Use case on slide: "Run the tests".

In the table, **web_search** — Find documentation. Use case on slide: "Look up pandas DataFrame API".

In the table, **browser** — Browse web pages. Use case on slide: "Open the PR and review it".

In the table, **git** — Version control. Use case on slide: "Create a branch and commit".

Terms on this slide — quick definitions for the room:

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

PR stands for Pull Request — a proposed code change others review before it merges.
-->

---







<!-- _class: fit-xs -->

## MCP (Model Context Protocol)

> _"USB-C for AI — one protocol that works across different tools."_

**Without MCP:** Each tool needs custom integration

**With MCP:** Tools advertise their capabilities; AI discovers them dynamically

<img src="assets/module-01/mcp-architecture.svg" alt="MCP architecture" />

<!--
This slide includes a diagram — MCP (Model Context Protocol).

The slide title is: MCP (Model Context Protocol).

The slide quotes: "_"USB-C for AI — one protocol that works across different tools."_"

The slide says: Without MCP: Each tool needs custom integration.

The slide says: With MCP: Tools advertise their capabilities; AI discovers them dynamically.

The figure on this slide is titled: MCP architecture.

Terms on this slide — quick definitions for the room:

MCP stands for Model Context Protocol — a standard for connecting AI assistants to external tools, databases, and APIs.

MCP is standard plumbing for connecting Cursor to databases, browsers, and internal services — one protocol instead of a custom integration per tool.
-->

---







<!-- _class: fit-md -->

## Why MCP Matters

| Benefit              | Explanation                                |
| -------------------- | ------------------------------------------ |
| **Interoperability** | Same tools work across different AI models |
| **Discoverability**  | AI can learn what tools are available      |
| **Standardization**  | One protocol, not dozens of custom APIs    |
| **Extensibility**    | Add new tools without changing AI logic    |

<!--
This slide is a table — Why MCP Matters.

The slide title is: Why MCP Matters.

The table header columns are: Benefit, Explanation.

In the table, **Interoperability**: Same tools work across different AI models.

In the table, **Discoverability**: AI can learn what tools are available.

In the table, **Standardization**: One protocol, not dozens of custom APIs.

In the table, **Extensibility**: Add new tools without changing AI logic.

Terms on this slide — quick definitions for the room:

MCP stands for Model Context Protocol — a standard for connecting AI assistants to external tools, databases, and APIs.

MCP is standard plumbing for connecting Cursor to databases, browsers, and internal services — one protocol instead of a custom integration per tool.
-->

---







## Tool Calling Best Practices

1. **Define clear tool schemas** — name, description, parameters
2. **Validate tool calls** before execution — allowlist + parameter checks
3. **Set timeouts** — e.g., 30 seconds max per tool
4. **Log all tool calls** — audit trail for debugging
5. **Require human approval** for destructive actions — never auto-run writes/deletes

<!--
Let's look at Tool Calling Best Practices.

The slide title is: Tool Calling Best Practices.

The slide says: 1. Define clear tool schemas — name, description, parameters.

The slide says: 2. Validate tool calls before execution — allowlist + parameter checks.

The slide says: 3. Set timeouts — e.g., 30 seconds max per tool.

The slide says: 4. Log all tool calls — audit trail for debugging.

The slide says: 5. Require human approval for destructive actions — never auto-run writes/deletes.

Number 1 on the slide: Define clear tool schemas — name, description, parameters.

Number 2 on the slide: Validate tool calls before execution — allowlist + parameter checks.

Number 3 on the slide: Set timeouts — e.g., 30 seconds max per tool.

Number 4 on the slide: Log all tool calls — audit trail for debugging.

Number 5 on the slide: Require human approval for destructive actions — never auto-run writes/deletes.

Terms on this slide — quick definitions for the room:

Tool calling means the model requests an action — read a file, run a command — and the host executes it; the model does not run code itself.

Tool calling is how the model stops guessing and starts acting — read a file, run a terminal command, fetch a URL.

Plain chat only produces text. Tools close the loop with real feedback from your environment.
-->

---



<!-- _class: lead -->

# Lesson 1.6

## Agents

_Concept · 8 minutes_

<!--
Lesson 1.6: Agents. Concept · 8 minutes For this lesson, listen and take notes — you do not need to type along yet.

The slide title is: Lesson 1.6.

You will also see the heading: Agents.

The slide says: _Concept · 8 minutes_.
-->

---







<!-- _class: fit-sm -->

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
This slide is a table — Agent vs. Chatbot.

The slide title is: Agent vs. Chatbot.

The table header columns are: Aspect, Chatbot, Agent.

In the table, **Interaction** — Single turn or simple back-and-forth. Use case on slide: Multi-step, goal-oriented.

In the table, **Control** — User drives each step. Use case on slide: Agent plans and executes.

In the table, **Memory** — Limited to conversation. Use case on slide: Can maintain state across steps.

In the table, **Actions** — None (text only). Use case on slide: Can call tools, modify files.

In the table, **Autonomy** — None. Use case on slide: Goal-directed autonomy.

In the table, **Example** — "Explain this code". Use case on slide: "Fix all bugs in this repository".

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

Chatbots answer questions. Agents pursue outcomes across multiple steps — edits, commands, follow-ups.

That difference drives cost, risk, and how carefully you review each step.
-->

---







## The Agent Loop

<!--
Let's look at The Agent Loop.

The slide title is: The Agent Loop.

Terms on this slide — quick definitions for the room:

The agent loop is plan, act with tools, observe results, and repeat until the task is done or you stop it.
-->

---







<!-- _class: fit-sm -->

## The Agent Loop — Diagram

<img src="assets/module-01/agent-loop.svg" alt="Agent loop diagram" />

<!--
This slide includes a diagram — The Agent Loop — Diagram.

The slide title is: The Agent Loop — Diagram.

The figure on this slide is titled: Agent loop diagram.

Terms on this slide — quick definitions for the room:

The agent loop is plan, act with tools, observe results, and repeat until the task is done or you stop it.

Follow the loop on the slide: you state a goal, the model plans, Cursor runs a tool, results return, and the cycle repeats until the task finishes or you stop it. Each cycle is a chance to review before more changes land.
-->

---







<!-- _class: fit-sm -->

## Levels of Agent Autonomy

| Level  | Name        | Description                            | Example                    |
| ------ | ----------- | -------------------------------------- | -------------------------- |
| **L1** | Assistant   | Responds, needs step-by-step guidance  | Basic chatbot              |
| **L2** | Tool-caller | Can request tools, human approves      | Cursor Agent with approval |
| **L3** | Planner     | Makes plans, executes with supervision | Auto-code review           |
| **L4** | Autonomous  | Self-directed, minimal supervision     | CI/CD agent                |
| **L5** | Full Agent  | Complete task ownership                | Enterprise automation      |

<!--
This slide is a table — Levels of Agent Autonomy.

The slide title is: Levels of Agent Autonomy.

The table header columns are: Level, Name, Description, Example.

Table row: **L1**, Assistant, Responds, needs step-by-step guidance, Basic chatbot.

Table row: **L2**, Tool-caller, Can request tools, human approves, Cursor Agent with approval.

Table row: **L3**, Planner, Makes plans, executes with supervision, Auto-code review.

Table row: **L4**, Autonomous, Self-directed, minimal supervision, CI/CD agent.

Table row: **L5**, Full Agent, Complete task ownership, Enterprise automation.

Terms on this slide — quick definitions for the room:

CI/CD stands for Continuous Integration and Continuous Deployment — automated build, test, and release pipelines.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

Chatbots answer questions. Agents pursue outcomes across multiple steps — edits, commands, follow-ups.

That difference drives cost, risk, and how carefully you review each step.
-->

---







<!-- _class: fit-xs -->

## How Agents Change Your Role

**Traditional:**

<img src="assets/module-01/role-flow-traditional.svg" alt="Traditional developer workflow" />

**Agent-Assisted:**

<img src="assets/module-01/role-flow-agent-assisted.svg" alt="Agent-assisted developer workflow" />

<!--
This slide includes a diagram — How Agents Change Your Role.

The slide title is: How Agents Change Your Role.

The slide says: Traditional:.

The slide says: Agent-Assisted:.

The figure on this slide is titled: Traditional developer workflow.

The figure on this slide is titled: Agent-assisted developer workflow.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-md -->

## Developer Role Shift

| Old Role       | New Role           |
| -------------- | ------------------ |
| Code writer    | Intent specifier   |
| Debugger       | Quality reviewer   |
| Implementation | Orchestration      |
| Manual testing | Acceptance testing |
| Problem solver | Problem framer     |

<!--
This slide is a table — Developer Role Shift.

The slide title is: Developer Role Shift.

The table header columns are: Old Role, New Role.

In the table, Code writer: Intent specifier.

In the table, Debugger: Quality reviewer.

In the table, Implementation: Orchestration.

In the table, Manual testing: Acceptance testing.

In the table, Problem solver: Problem framer.
-->

---







<!-- _class: fit-md -->

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
This slide lists key points under When to Use Agents.

The slide title is: When to Use Agents.

The slide says: Good for agents:.

The slide says: Bad for agents:.

Bullet 1 on the slide: Large, multi-step tasks · Repetitive patterns.

Bullet 2 on the slide: Well-defined with clear success criteria.

Bullet 3 on the slide: Low-risk changes · Documentation updates.

Bullet 4 on the slide: Security-critical systems · Unrecoverable actions.

Bullet 5 on the slide: Poorly defined goals · Real-time requirements.

Bullet 6 on the slide: High cost of failure.
-->

---







<!-- _header: 'Module 2 — Cursor Editor Essentials' -->

<!-- _class: lead -->

# Cursor Editor Essentials

## Module 2 · Day 1 (Hands-On)

Cursor Training Program · Hands-on exercise · ~90 min

<!--
Module 2 is our longest hands-on block. Open Cursor now, load your repo with File → Open Folder, and keep the Agent panel ready — Ctrl+I on Windows.

The slide title is: Cursor Editor Essentials.

You will also see the heading: Module 2 · Day 1 (Hands-On).

The slide says: Cursor Training Program · Hands-on exercise · ~90 min.
-->

---







<!-- _class: fit-md -->

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~90 minutes |
| **Format** | Hands-on exercise |
| **Prerequisites** | Module 1 completed, Cursor installed, Git repository access |
| **Module Goal** | Master the core workflows of AI-assisted coding in Cursor |

### Lessons

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
Here is the overview for Module 2.

The slide title is: Module Overview.

The table header columns are: Aspect, Details.

In the table, **Duration**: ~90 minutes.

In the table, **Format**: Hands-on exercise.

In the table, **Prerequisites**: Module 1 completed, Cursor installed, Git repository access.

In the table, **Module Goal**: Master the core workflows of AI-assisted coding in Cursor.
-->

---



<!-- _class: lead -->

# Lesson 2.1

## Codebase Understanding

*Concept · 8 min · Exercise · 12 min*

**Lab guide:** [`Exercise 2.1](../slide-exercises/module-02/exercise-2.1-codebase-understanding.md)

<!--
Lesson 2.1: Codebase Understanding. For this lesson, listen, participate, or follow along as indicated on the next slides.

Use the Cursor Agent to orient yourself in an unfamiliar repository.

The detailed lab guide is slide-exercises/module-02/exercise-2.1-codebase-understanding.md.

The slide title is: Lesson 2.1.

You will also see the heading: Codebase Understanding.

The note on screen reads: Concept · 8 min · Exercise · 12 min.

The slide says: Lab guide: [`Exercise 2.1](../slide-exercises/module-02/exercise-2.1-codebase-understanding.md).
-->

---







## The Problem & The Solution

**The Problem:** Opening a new codebase is overwhelming. Where do you start? What's the entry point?

**The Cursor Solution:** Ask the agent to explain the codebase. It reads files, traces connections, and returns a roadmap.

> *"Drop an agent into a codebase you've never seen and get a coherent explanation of how it works."*

<!--
This slide highlights a key quote — The Problem & The Solution.

The slide title is: The Problem & The Solution.

The slide quotes: ""Drop an agent into a codebase you've never seen and get a coherent explanation of how it works.""

The slide says: The Problem: Opening a new codebase is overwhelming. Where do you start? What's the entry point?.

The slide says: The Cursor Solution: Ask the agent to explain the codebase. It reads files, traces connections, and returns a roadmap.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

Every one of us has opened a repo and wondered where to start. The Agent can produce a roadmap in minutes — but the first answer is a draft, not gospel. Your job is to verify and follow up.
-->

---







<!-- _class: fit-md -->

## Exercise 2.1 — Steps 1–2

**Step 1:** Open an unfamiliar repository in Cursor

**Windows (PowerShell)** in Cursor's integrated terminal (``Ctrl+` `` → **PowerShell**):

```bash
git clone https://github.com/facebookresearch/detectron2
cd detectron2
cursor .
```

**Step 2:** Open the Agent panel — ``Ctrl+I``

<!--
We are starting Exercise 2.1 — Codebase Understanding. We have about 20 min for this lab.

Use the Cursor Agent to orient yourself in an unfamiliar repository.

The full lab guide is in slide-exercises/module-02/exercise-2.1-codebase-understanding.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Any unfamiliar repository works here — detectron2 is on the slide, but a smaller repo is fine if we are short on time.

Use File → Open Folder, not a single file, so the Agent can see the project tree.

Step 1: Open an unfamiliar repository in Cursor.

Step 2: Open the Agent panel — `Ctrl+I`.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.1 — Steps 1–2.

The slide says: Windows (PowerShell) in Cursor's integrated terminal (`Ctrl+ `` → PowerShell):.

The code on the slide reads: git clone https://github.com/facebookresearch/detectron2 cd detectron2 cursor ..

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-xs -->

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
Now for Step 3: Orientation Prompt.

Copy this into the Agent chat: "Explain this codebase to me as if I'm a new team member. Specifically tell me: 1. What is the main purpose of this project? 2. What are the entry points (main scripts, CLI, API)? 3. What are the key modules and how do they relate? 4. What are the main dependencies? 5. What files should I read first to understand the architecture?"

You want a reading order and named entry points — not a flat list of every filename.

If the Agent dumps dozens of files, reply in chat: which three should I read first?

When we debrief, I will ask what the Agent got wrong about dependencies or architecture.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.1 — Step 3: Orientation Prompt.

The code on the slide reads: Explain this codebase to me as if I'm a new team member. Specifically tell me: 1. What is the main purpose of this project? 2. What are the entry points (main scripts, CLI, API)? 3. What are the key modules and how do they relate? 4. What are the main dependencies? 5. What files should I read first to understand the architecture?.

Terms on this slide — quick definitions for the room:

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.
-->

---







## Exercise 2.1 — Step 4: Trace Data Flow

**Step 4:** Follow up — trace data flow:

```
Based on what you just told me, trace the flow of data from input
to output. What functions get called in order?
```

<!--
Now for Step 4: Trace Data Flow.

Copy this into the Agent chat: "Based on what you just told me, trace the flow of data from input to output. What functions get called in order?"

The first answer was a map; this follow-up tests whether the Agent can chain function calls logically.

If the trace looks wrong, ask it to cite file and line for each hop — that is a verification habit worth keeping.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.1 — Step 4: Trace Data Flow.

Step 4: Follow up — trace data flow:.

The code on the slide reads: Based on what you just told me, trace the flow of data from input to output. What functions get called in order?.
-->

---







## Exercise 2.1 — Step 5: Visual Overview

**Step 5:** Ask for a visual overview:

```
Create an ASCII diagram showing the module relationships in this codebase.
```

<!--
Now for Step 5: Visual Overview.

Copy this into the Agent chat: "Create an ASCII diagram showing the module relationships in this codebase."

An ASCII diagram is enough for onboarding — we care about communicating structure, not graphic design.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.1 — Step 5: Visual Overview.

Step 5: Ask for a visual overview:.

The code on the slide reads: Create an ASCII diagram showing the module relationships in this codebase..
-->

---







<!-- _class: fit-sm -->

## Expected Agent Output (Sample)

<img src="assets/module-02/expected-agent-output-sample.svg" alt="Expected Agent Output (Sample)" />

<!--
This slide includes a diagram — Expected Agent Output (Sample).

The slide title is: Expected Agent Output (Sample).

The figure on this slide is titled: Expected Agent Output (Sample).

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Pro Tip — Save the Overview

**Pro Tip:** Save the agent's explanation as a project note:

```
Save this explanation as .cursor/project-overview.md so future
team members can read it.
```

<!--
The slide title is: Pro Tip — Save the Overview.

The slide says: Pro Tip: Save the agent's explanation as a project note:.

The code on the slide reads: Save this explanation as .cursor/project-overview.md so future team members can read it..

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 2.1 — Success Criteria

**Success Criteria:**
- Agent described project purpose
- Agent identified entry points and key modules
- Agent suggested first files to read

<!--
That finishes Exercise 2.1 — Codebase Understanding.

Check off what you actually did: Agent described project purpose; Agent identified entry points and key modules; Agent suggested first files to read.

Who completed all three parts? What did the Agent get wrong, and what prompt change fixed it?

Raise your hand if you finished. What did the Agent get wrong, and what prompt change fixed it?

The slide title is: Exercise 2.1 — Success Criteria.

Success criteria are listed on the slide as follows.

Bullet 1 on the slide: Agent described project purpose.

Bullet 2 on the slide: Agent identified entry points and key modules.

Bullet 3 on the slide: Agent suggested first files to read.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---



<!-- _class: lead -->

# Lesson 2.2

## Explaining a Specific File or Symbol

*Concept · 5 min · Exercise · 8 min*

**Lab guide:** [`Exercise 2.2](../slide-exercises/module-02/exercise-2.2-explaining-a-specific-file-or-symbol.md)

<!--
Lesson 2.2: Explaining a Specific File or Symbol. For this lesson, listen, participate, or follow along as indicated on the next slides.

Get targeted explanations of one file or symbol without reading the whole repo.

The detailed lab guide is slide-exercises/module-02/exercise-2.2-explaining-a-specific-file-or-symbol.md.

The slide title is: Lesson 2.2.

You will also see the heading: Explaining a Specific File or Symbol.

The note on screen reads: Concept · 5 min · Exercise · 8 min.

The slide says: Lab guide: [`Exercise 2.2](../slide-exercises/module-02/exercise-2.2-explaining-a-specific-file-or-symbol.md).
-->

---







## Targeted Explanations

> *"Don't make the agent read the whole codebase when you just need to understand one function."*

Use **precise context** — select a function or class, then ask focused questions.

<!--
This slide highlights a key quote — Targeted Explanations.

The slide title is: Targeted Explanations.

The slide quotes: ""Don't make the agent read the whole codebase when you just need to understand one function.""

The slide says: Use precise context — select a function or class, then ask focused questions.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-sm -->

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
We are starting Exercise 2.2 — Explaining a Specific File or Symbol. We have about 13 min for this lab.

Get targeted explanations of one file or symbol without reading the whole repo.

The full lab guide is in slide-exercises/module-02/exercise-2.2-explaining-a-specific-file-or-symbol.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: Open a specific file in your project.

Step 2: Select a function or class you want explained.

Step 3: Use the Agent with precise context:.

Copy this into the Agent chat: "Explain the function I have selected. For each major section, tell me: - What it does - Why it's designed that way (trade-offs) - Potential edge cases or bugs - How it could be improved"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.2 — Steps 1–3.

Bullet 1 on the slide: What it does.

Bullet 2 on the slide: Why it's designed that way (trade-offs).

Bullet 3 on the slide: Potential edge cases or bugs.

Bullet 4 on the slide: How it could be improved.

The code on the slide reads: Explain the function I have selected. For each major section, tell me: - What it does - Why it's designed that way (trade-offs) - Potential edge cases or bugs - How it could be improved.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 2.2 — Step 4: Example I/O

**Step 4:** Ask for a concrete example:

```
Give me a concrete example of inputs and outputs for this function.
Show me what happens in the normal case and one edge case.
```

<!--
Now for Step 4: Example I/O.

Copy this into the Agent chat: "Give me a concrete example of inputs and outputs for this function. Show me what happens in the normal case and one edge case."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.2 — Step 4: Example I/O.

Step 4: Ask for a concrete example:.

The code on the slide reads: Give me a concrete example of inputs and outputs for this function. Show me what happens in the normal case and one edge case..
-->

---







## Exercise 2.2 — Step 5: Dependencies

**Step 5:** Ask about dependencies:

```
What other functions does this call? What calls this function?
Trace the call chain two levels in each direction.
```

<!--
Now for Step 5: Dependencies.

Copy this into the Agent chat: "What other functions does this call? What calls this function? Trace the call chain two levels in each direction."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.2 — Step 5: Dependencies.

Step 5: Ask about dependencies:.

The code on the slide reads: What other functions does this call? What calls this function? Trace the call chain two levels in each direction..
-->

---







<!-- _class: fit-md -->

## Inline Explanation Shortcut

```bash
# Select code, press Cmd+L (or Ctrl+L)
# The agent explains the selected code in the chat panel
```

**Success Criteria:**
- Selected specific code · Agent explained the selection
- Agent provided input/output examples · Agent traced call dependencies

<!--
The slide title is: Inline Explanation Shortcut.

You will also see the heading: Select code, press Cmd+L (or Ctrl+L).

You will also see the heading: The agent explains the selected code in the chat panel.

Success criteria are listed on the slide as follows.

Bullet 1 on the slide: Selected specific code · Agent explained the selection.

Bullet 2 on the slide: Agent provided input/output examples · Agent traced call dependencies.

The code on the slide reads: # Select code, press Cmd+L (or Ctrl+L) # The agent explains the selected code in the chat panel.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---



<!-- _class: lead -->

# Lesson 2.3

## Making a Safe, Reviewable Change

*Concept · 5 min · Exercise · 8 min*

**Lab guide:** [`Exercise 2.3](../slide-exercises/module-02/exercise-2.3-making-a-safe-reviewable-change.md)

<!--
Lesson 2.3: Making a Safe, Reviewable Change. For this lesson, listen, participate, or follow along as indicated on the next slides.

Let the Agent propose a small change and review the diff before accepting.

The detailed lab guide is slide-exercises/module-02/exercise-2.3-making-a-safe-reviewable-change.md.

The slide title is: Lesson 2.3.

You will also see the heading: Making a Safe, Reviewable Change.

The note on screen reads: Concept · 5 min · Exercise · 8 min.

The slide says: Lab guide: [`Exercise 2.3](../slide-exercises/module-02/exercise-2.3-making-a-safe-reviewable-change.md).
-->

---







## The Diff Review Workflow

1. Ask agent to propose a change
2. Review the diff (what's added/removed)
3. Accept or reject changes
4. Test after acceptance

> *"Before AI changes your code, see exactly what will change and approve it."*

<!--
This slide highlights a key quote — The Diff Review Workflow.

The slide title is: The Diff Review Workflow.

The slide quotes: ""Before AI changes your code, see exactly what will change and approve it.""

The slide says: 1. Ask agent to propose a change.

The slide says: 2. Review the diff (what's added/removed).

The slide says: 3. Accept or reject changes.

The slide says: 4. Test after acceptance.

Number 1 on the slide: Ask agent to propose a change.

Number 2 on the slide: Review the diff (what's added/removed).

Number 3 on the slide: Accept or reject changes.

Number 4 on the slide: Test after acceptance.

Terms on this slide — quick definitions for the room:

Diff review is reading added and removed lines before you accept an AI edit — your primary quality gate.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-sm -->

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
We are starting Exercise 2.3 — Making a Safe, Reviewable Change. We have about 13 min for this lab.

Let the Agent propose a small change and review the diff before accepting.

The full lab guide is in slide-exercises/module-02/exercise-2.3-making-a-safe-reviewable-change.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

The change is tiny on purpose — read every line of the diff before you click Accept. If you accepted without reading, undo and do it again; that is the exercise.

Step 1: Ask for a small, safe change:.

Step 2: Watch the agent generate the diff:.

Copy this into the Agent chat: "Change the welcome message in index.html from "Hello World" to "Welcome to My App""

Copy this into the Agent chat: "📝 Changes to index.html: <h1>- Hello World</h1> <h1>+ Welcome to My App</h1> Accept? [Yes] [No] [Edit]"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.3 — Steps 1–2.

The code on the slide reads: Change the welcome message in index.html from "Hello World" to "Welcome to My App".

The code on the slide reads: 📝 Changes to index.html:   <h1>- Hello World</h1>   <h1>+ Welcome to My App</h1> Accept? [Yes] [No] [Edit].

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
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
Now for Review Questions.

Step 4: Accept · Step 5: Test manually.

The change is tiny on purpose — read every line of the diff before you click Accept. If you accepted without reading, undo and do it again; that is the exercise.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.3 — Review Questions.

The slide says: Before accepting, ask yourself:.

Bullet 1 on the slide: Are the changes only what I asked for?.

Bullet 2 on the slide: Are there unexpected additions or deletions?.

Bullet 3 on the slide: Does the syntax look correct?.

Bullet 4 on the slide: Will this break anything else?.
-->

---







## Exercise 2.3 — Test After Accept

**Windows (PowerShell) — use these in the demo:**

```powershell
start index.html          # open HTML in default browser
python script.py          # run Python script
npm start                 # Node/React dev server
```

**Other platforms:** Mac — `open index.html` · same `python` / `npm` commands.

<!--
Now for Test After Accept.

Copy this into the Agent chat: "start index.html # open HTML in default browser python script.py # run Python script npm start # Node/React dev server"

The change is tiny on purpose — read every line of the diff before you click Accept. If you accepted without reading, undo and do it again; that is the exercise.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.3 — Test After Accept.

The slide says: Windows (PowerShell) — use these in the demo:.

The slide says: Other platforms: Mac — open index.html · same python / npm commands.

The code on the slide reads: start index.html          # open HTML in default browser python script.py          # run Python script npm start                 # Node/React dev server.

Terms on this slide — quick definitions for the room:

npm is the Node Package Manager — the default registry and tool for JavaScript packages.
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
Now for If Something Goes Wrong.

Copy this into the Agent chat: "That change didn't work. The button disappeared. Please explain what happened and suggest a fix."

The change is tiny on purpose — read every line of the diff before you click Accept. If you accepted without reading, undo and do it again; that is the exercise.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.3 — If Something Goes Wrong.

Success criteria are listed on the slide as follows.

Bullet 1 on the slide: Agent proposed a change · Reviewed diff before accepting.

Bullet 2 on the slide: Accepted only after verification · Tested the change.

The code on the slide reads: That change didn't work. The button disappeared. Please explain what happened and suggest a fix..

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---



<!-- _class: lead -->

# Lesson 2.4

## Plan Mode

*Concept · 5 min · Exercise · 8 min*

**Lab guide:** [`Exercise 2.4](../slide-exercises/module-02/exercise-2.4-plan-mode.md)

<!--
Lesson 2.4: Plan Mode. For this lesson, listen, participate, or follow along as indicated on the next slides.

Use Plan Mode to design a change before the Agent edits files.

Plan Mode shows you the design before files change. Use it for multi-file work and unfamiliar codebases — plans are cheaper to throw away than bad diffs.

The detailed lab guide is slide-exercises/module-02/exercise-2.4-plan-mode.md.

The slide title is: Lesson 2.4.

You will also see the heading: Plan Mode.

The note on screen reads: Concept · 5 min · Exercise · 8 min.

The slide says: Lab guide: [`Exercise 2.4](../slide-exercises/module-02/exercise-2.4-plan-mode.md).

Terms on this slide — quick definitions for the room:

Plan Mode makes the agent draft a step-by-step plan and ask clarifying questions before it writes code — toggle with Shift+Tab.
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
This slide lists key points under Design Before You Code.

The slide title is: Design Before You Code.

The slide says: Plan Mode makes the agent create a detailed plan BEFORE writing any code.

The slide says: When to use Plan Mode:.

Bullet 1 on the slide: Changing multiple files · Adding a new feature.

Bullet 2 on the slide: Refactoring existing code.

Bullet 3 on the slide: You're not 100% sure of the best approach.

Bullet 4 on the slide: The change is risky or hard to undo.

Terms on this slide — quick definitions for the room:

Plan Mode makes the agent draft a step-by-step plan and ask clarifying questions before it writes code — toggle with Shift+Tab.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 2.4 — Step 1: Enable Plan Mode

**Step 1:** Enable Plan Mode (Shift+Tab in the Agent input):

```bash
# Press Shift+Tab in the Agent input
# The input border changes color to indicate Plan Mode
```

<!--
We are starting Exercise 2.4 — Plan Mode. We have about 13 min for this lab.

Use Plan Mode to design a change before the Agent edits files.

The full lab guide is in slide-exercises/module-02/exercise-2.4-plan-mode.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: Enable Plan Mode (Shift+Tab in the Agent input):.

Copy this into the Agent chat: "# Press Shift+Tab in the Agent input # The input border changes color to indicate Plan Mode"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.4 — Step 1: Enable Plan Mode.

You will also see the heading: Press Shift+Tab in the Agent input.

You will also see the heading: The input border changes color to indicate Plan Mode.

The code on the slide reads: # Press Shift+Tab in the Agent input # The input border changes color to indicate Plan Mode.

Terms on this slide — quick definitions for the room:

Plan Mode makes the agent draft a step-by-step plan and ask clarifying questions before it writes code — toggle with Shift+Tab.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

Plan Mode shows you the design before files change. Use it for multi-file work and unfamiliar codebases — plans are cheaper to throw away than bad diffs.
-->

---







<!-- _class: fit-sm -->

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
Now for Step 2: Describe Change.

Copy this into the Agent chat: "Add user authentication to this web app. Requirements: - Email/password login · Session management - Protected routes (dashboard, settings) - Logout functionality · "Remember me" option Don't write code yet – just give me a plan."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.4 — Step 2: Describe Change.

Step 2: Describe a complex change:.

Bullet 1 on the slide: Email/password login · Session management.

Bullet 2 on the slide: Protected routes (dashboard, settings).

Bullet 3 on the slide: Logout functionality · "Remember me" option.

The code on the slide reads: Add user authentication to this web app. Requirements: - Email/password login · Session management - Protected routes (dashboard, settings) - Logout functionality · "Remember me" option Don't write code yet – just give me a plan..
-->

---







<!-- _class: fit-xs -->

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
Now for Step 3: Review the Plan.

Copy this into the Agent chat: "📋 IMPLEMENTATION PLAN Step 1: Create User Model — models/user.js Step 2: Auth Routes — routes/auth.js (login, logout, register) Step 3: Session Management — middleware/session.js Step 4: Protected Route Middleware — middleware/auth.js Step 5: Update Frontend — pages/login.html, dashboard.html Step 6: Environment Variables — .env (SESSION_SECRET, REDIS_URL) Questions for you: 1. JWT or server-side sessions? 2. Existing user database? 3. Include email verification? Ready to proceed? [Yes] [No] [Modify Plan]"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.4 — Step 3: Review the Plan.

Step 3: Review the agent's plan — a good plan includes:.

The code on the slide begins: 📋 IMPLEMENTATION PLAN Step 1: Create User Model — models/user.js Step 2: Auth Routes — routes/auth.js (login, logout, register) Step 3: Session Management — middleware/session.js Step 4: Protected Route Middleware — middleware/auth.js Step 5: Update Frontend — pages/login.html, dashboard.html. The rest of the block continues on the slide.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

JWT stands for JSON Web Token — a compact, signed token format often used for authentication.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.
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
Now for Approve & Execute.

Step 4: Answer questions and approve:.

Step 5: Watch the agent execute the plan step by step.

Copy this into the Agent chat: "Use JWT for simplicity. No existing database yet – use SQLite for now. Skip email verification for this version. Proceed."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.4 — Approve & Execute.

The code on the slide reads: Use JWT for simplicity. No existing database yet – use SQLite for now. Skip email verification for this version. Proceed..

Terms on this slide — quick definitions for the room:

SQLite is a lightweight file-based database — no separate server process required.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

JWT stands for JSON Web Token — a compact, signed token format often used for authentication.
-->

---







## Exercise 2.4 — Success Criteria

**Success Criteria:**
- Enabled Plan Mode (Shift+Tab)
- Agent created structured plan
- Agent asked clarifying questions
- Approved plan before code was written

<!--
That finishes Exercise 2.4 — Plan Mode.

Check off what you actually did: Enabled Plan Mode (Shift+Tab); Agent created structured plan; Agent asked clarifying questions; Approved plan before code was written.

Raise your hand if you finished. What did the Agent get wrong, and what prompt change fixed it?

The slide title is: Exercise 2.4 — Success Criteria.

Success criteria are listed on the slide as follows.

Bullet 1 on the slide: Enabled Plan Mode (Shift+Tab).

Bullet 2 on the slide: Agent created structured plan.

Bullet 3 on the slide: Agent asked clarifying questions.

Bullet 4 on the slide: Approved plan before code was written.

Terms on this slide — quick definitions for the room:

Plan Mode makes the agent draft a step-by-step plan and ask clarifying questions before it writes code — toggle with Shift+Tab.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---



<!-- _class: lead -->

# Lesson 2.5

## Comparing Two Models

*Concept · 5 min · Exercise · 8 min*

**Lab guide:** [`Exercise 2.5](../slide-exercises/module-02/exercise-2.5-comparing-two-models.md)

<!--
Lesson 2.5: Comparing Two Models. For this lesson, listen, participate, or follow along as indicated on the next slides.

Run the same prompt on two models and compare quality, speed, and cost.

Run the same prompt on two models. Judge correctness first, then speed, then cost. The prettiest answer that fails tests loses.

The detailed lab guide is slide-exercises/module-02/exercise-2.5-comparing-two-models.md.

The slide title is: Lesson 2.5.

You will also see the heading: Comparing Two Models.

The note on screen reads: Concept · 5 min · Exercise · 8 min.

The slide says: Lab guide: [`Exercise 2.5](../slide-exercises/module-02/exercise-2.5-comparing-two-models.md).
-->

---







<!-- _class: fit-sm -->

## Model Selection Guide

| Task Type | Recommended Model | Why |
|-----------|-------------------|-----|
| Typo fixes, simple edits | GPT-5 Mini | Cheap, fast, good enough |
| Daily coding, bug fixes | **Composer 2.5** or GPT-5.3 Codex | Best value in Cursor; built for agent tools |
| Complex logic, architecture | Claude Opus or GPT-5.5 | Smartest, but expensive |
| Frontend/visual work | Gemini 3.1 Pro | Can see images |
| Fast, simple questions | Claude Haiku | Fastest responses |

**Model reference:** [`docs-content-readmes/010-docs-models-cursor-composer-2-5.md`](../docs-content-readmes/010-docs-models-cursor-composer-2-5.md)

<!--
This slide is a table — Model Selection Guide.

The slide title is: Model Selection Guide.

The slide says: Model reference: [docs-content-readmes/010-docs-models-cursor-composer-2-5.md](../docs-content-readmes/010-docs-models-cursor-composer-2-5.md).

The table header columns are: Task Type, Recommended Model, Why.

In the table, Typo fixes, simple edits — GPT-5 Mini. Use case on slide: Cheap, fast, good enough.

In the table, Daily coding, bug fixes — **Composer 2.5** or GPT-5.3 Codex. Use case on slide: Best value in Cursor; built for agent tools.

In the table, Complex logic, architecture — Claude Opus or GPT-5.5. Use case on slide: Smartest, but expensive.

In the table, Frontend/visual work — Gemini 3.1 Pro. Use case on slide: Can see images.

In the table, Fast, simple questions — Claude Haiku. Use case on slide: Fastest responses.

Terms on this slide — quick definitions for the room:

Composer 2.5 is Cursor's agent-optimized model — tuned for multi-step coding tasks and tool use inside the editor.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 2.5 — Compare Two Models

**Step 1:** Set model to **Composer 2.5** (`/model composer-2.5`), ask:

```
Explain what a closure is in JavaScript with a practical example.
```

**Step 2:** Copy the response

**Step 3:** Switch to GPT-5 Mini — ask the **same question**

**Step 4:** Compare responses side by side

<!--
We are starting Exercise 2.5 — Comparing Two Models. We have about 13 min for this lab.

Run the same prompt on two models and compare quality, speed, and cost.

The full lab guide is in slide-exercises/module-02/exercise-2.5-comparing-two-models.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: Set model to Composer 2.5 (/model composer-2.5), ask:.

Step 2: Copy the response.

Step 3: Switch to GPT-5 Mini — ask the same question.

Step 4: Compare responses side by side.

Copy this into the Agent chat: "Explain what a closure is in JavaScript with a practical example."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.5 — Compare Two Models.

The code on the slide reads: Explain what a closure is in JavaScript with a practical example..

Terms on this slide — quick definitions for the room:

Composer 2.5 is Cursor's agent-optimized model — tuned for multi-step coding tasks and tool use inside the editor.
-->

---







<!-- _class: fit-md -->

## Exercise 2.5 — Comparison Table

| Comparison Point | Composer 2.5 | GPT-5 Mini |
|-----------------|---------------|------------|
| Length | | |
| Code example quality | | |
| Explanation clarity | | |
| Speed | | |

<!--
Now for Comparison Table.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.5 — Comparison Table.

In the table, Comparison Point — Composer 2.5. Use case on slide: GPT-5 Mini.

In the table, Length — . Use case on slide: .

In the table, Code example quality — . Use case on slide: .

In the table, Explanation clarity — . Use case on slide: .

In the table, Speed — . Use case on slide: .

Terms on this slide — quick definitions for the room:

Composer 2.5 is Cursor's agent-optimized model — tuned for multi-step coding tasks and tool use inside the editor.
-->

---







<!-- _class: fit-xs -->

## Exercise 2.5 — Cost & Decision Matrix

**Step 5:** Check token usage at bottom of chat after each request

**Step 6:** Create a personal decision matrix:

<img src="assets/module-02/exercise-2-5-cost-decision-matrix.svg" alt="Exercise 2.5 — Cost & Decision Matrix" />

<!--
Now for Cost & Decision Matrix.

Step 5: Check token usage at bottom of chat after each request.

Step 6: Create a personal decision matrix:.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.5 — Cost & Decision Matrix.

The figure on this slide is titled: Exercise 2.5 — Cost & Decision Matrix.

Terms on this slide — quick definitions for the room:

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.
-->

---







## Exercise 2.5 — Success Criteria

**Success Criteria:**
- Same question to two models
- Compared quality and speed
- Created personal model-selection guide

<!--
That finishes Exercise 2.5 — Comparing Two Models.

Check off what you actually did: Same question to two models; Compared quality and speed; Created personal model-selection guide.

Raise your hand if you finished. What did the Agent get wrong, and what prompt change fixed it?

The slide title is: Exercise 2.5 — Success Criteria.

Success criteria are listed on the slide as follows.

Bullet 1 on the slide: Same question to two models.

Bullet 2 on the slide: Compared quality and speed.

Bullet 3 on the slide: Created personal model-selection guide.
-->

---



<!-- _class: lead -->

# Lesson 2.6

## Precise Context with @mentions

*Concept · 5 min · Exercise · 8 min*

**Lab guide:** [`Exercise 2.6](../slide-exercises/module-02/exercise-2.6-precise-context-with-mentions.md)

<!--
Lesson 2.6: Precise Context with @mentions. For this lesson, listen, participate, or follow along as indicated on the next slides.

Use @mentions to point the Agent at exact files, symbols, and context.

The detailed lab guide is slide-exercises/module-02/exercise-2.6-precise-context-with-mentions.md.

The slide title is: Lesson 2.6.

You will also see the heading: Precise Context with @mentions.

The note on screen reads: Concept · 5 min · Exercise · 8 min.

The slide says: Lab guide: [`Exercise 2.6](../slide-exercises/module-02/exercise-2.6-precise-context-with-mentions.md).

Terms on this slide — quick definitions for the room:

An @mention points the agent at specific context — a file, folder, symbol, branch, or the web.
-->

---







<!-- _class: fit-xs -->

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
This slide is a table — @mention Types.

The slide title is: @mention Types.

The slide quotes: ""Laser-targeting instead of spraying the whole codebase.""

The table header columns are: @mention, What It Does, Example.

In the table, `@filename` — Include specific file. Use case on slide: `@auth.py`.

In the table, `@symbol` — Include function/class. Use case on slide: `@UserModel`.

In the table, `@branch` — Reference git branch. Use case on slide: `@main`.

In the table, `@chat` — Reference past conversation. Use case on slide: `@previous-chat`.

In the table, `@folder` — Reference entire directory. Use case on slide: `@/src/utils`.

In the table, `@web` — Search the web. Use case on slide: `@web pandas DataFrame`.

Terms on this slide — quick definitions for the room:

An @mention points the agent at specific context — a file, folder, symbol, branch, or the web.
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
We are starting Exercise 2.6 — Precise Context with @mentions. We have about 13 min for this lab.

Use @mentions to point the Agent at exact files, symbols, and context.

The full lab guide is in slide-exercises/module-02/exercise-2.6-precise-context-with-mentions.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: Use @filename to point at a specific file:.

Step 2: Use @symbol to reference a specific function:.

Copy this into the Agent chat: "@database.py What are the security vulnerabilities in this database connection?"

Copy this into the Agent chat: "@calculate_total This function is returning NaN sometimes. Why?"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.6 — Steps 1–2.

The code on the slide reads: @database.py What are the security vulnerabilities in this database connection?.

The code on the slide reads: @calculate_total This function is returning NaN sometimes. Why?.

Terms on this slide — quick definitions for the room:

An @mention points the agent at specific context — a file, folder, symbol, branch, or the web.
-->

---







## Exercise 2.6 — Step 3: Multiple @mentions

**Step 3:** Combine multiple @mentions:

```
@auth.py @UserModel @login_handler Review the authentication flow.
Are there any race conditions or timing attacks?
```

<!--
Now for Step 3: Multiple @mentions.

Copy this into the Agent chat: "@auth.py @UserModel @login_handler Review the authentication flow. Are there any race conditions or timing attacks?"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.6 — Step 3: Multiple @mentions.

Step 3: Combine multiple @mentions:.

The code on the slide reads: @auth.py @UserModel @login_handler Review the authentication flow. Are there any race conditions or timing attacks?.

Terms on this slide — quick definitions for the room:

An @mention points the agent at specific context — a file, folder, symbol, branch, or the web.
-->

---







## Exercise 2.6 — Step 4: @branch

**Step 4:** Use @branch to reference a different branch:

```
Compare @main and @feature/payment branches.
What are the key differences in the payment handling code?
```

<!--
Now for Step 4: @branch.

Copy this into the Agent chat: "Compare @main and @feature/payment branches. What are the key differences in the payment handling code?"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.6 — Step 4: @branch.

Step 4: Use @branch to reference a different branch:.

The code on the slide reads: Compare @main and @feature/payment branches. What are the key differences in the payment handling code?.

Terms on this slide — quick definitions for the room:

An @mention points the agent at specific context — a file, folder, symbol, branch, or the web.
-->

---







## Exercise 2.6 — Step 5: @chat

**Step 5:** Use @chat to refer to a previous conversation:

```
@chat(authentication-discussion) Based on that discussion,
implement the fix we agreed on.
```

<!--
Now for Step 5: @chat.

Copy this into the Agent chat: "@chat(authentication-discussion) Based on that discussion, implement the fix we agreed on."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.6 — Step 5: @chat.

Step 5: Use @chat to refer to a previous conversation:.

The code on the slide reads: @chat(authentication-discussion) Based on that discussion, implement the fix we agreed on..
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
Now for Steps 6–7: @folder & @web.

Step 6: Use @folder for directory-level context:.

Step 7: Use @web for external documentation:.

Copy this into the Agent chat: "@src/components Find all components that don't have loading states."

Copy this into the Agent chat: "@web React 19 useTransition hook How do I use it?"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.6 — Steps 6–7: @folder & @web.

The code on the slide reads: @src/components Find all components that don't have loading states..

The code on the slide reads: @web React 19 useTransition hook How do I use it?.

Terms on this slide — quick definitions for the room:

An @mention points the agent at specific context — a file, folder, symbol, branch, or the web.
-->

---







## @mention Pro Tips

- Start typing **@** — Cursor auto-suggests available mentions
- You can @mention **multiple items** in one message
- @mentions work in both **Agent** and **Chat** modes

<!--
This slide lists key points under @mention Pro Tips.

The slide title is: @mention Pro Tips.

Bullet 1 on the slide: Start typing @ — Cursor auto-suggests available mentions.

Bullet 2 on the slide: You can @mention multiple items in one message.

Bullet 3 on the slide: @mentions work in both Agent and Chat modes.

Terms on this slide — quick definitions for the room:

An @mention points the agent at specific context — a file, folder, symbol, branch, or the web.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 2.6 — Success Criteria

**Success Criteria:**
- Used @filename to target a specific file
- Used @symbol to target a function or class
- Used multiple @mentions together
- Used @web for external search

<!--
That finishes Exercise 2.6 — Precise Context with @mentions.

Check off what you actually did: Used @filename to target a specific file; Used @symbol to target a function or class; Used multiple @mentions together; Used @web for external search.

Raise your hand if you finished. What did the Agent get wrong, and what prompt change fixed it?

The slide title is: Exercise 2.6 — Success Criteria.

Success criteria are listed on the slide as follows.

Bullet 1 on the slide: Used @filename to target a specific file.

Bullet 2 on the slide: Used @symbol to target a function or class.

Bullet 3 on the slide: Used multiple @mentions together.

Bullet 4 on the slide: Used @web for external search.

Terms on this slide — quick definitions for the room:

An @mention points the agent at specific context — a file, folder, symbol, branch, or the web.
-->

---



<!-- _class: lead -->

# Lesson 2.7

## Checkpoints

*Concept · 4 min · Exercise · 4 min*

**Lab guide:** [`Exercise 2.7](../slide-exercises/module-02/exercise-2.7-checkpoints.md)

<!--
Lesson 2.7: Checkpoints. For this lesson, listen, participate, or follow along as indicated on the next slides.

Create and restore checkpoints before risky Agent experiments.

Checkpoints are undo for agent experiments — create one before risky prompts or broad @folder mentions.

The detailed lab guide is slide-exercises/module-02/exercise-2.7-checkpoints.md.

The slide title is: Lesson 2.7.

You will also see the heading: Checkpoints.

The note on screen reads: Concept · 4 min · Exercise · 4 min.

The slide says: Lab guide: [`Exercise 2.7](../slide-exercises/module-02/exercise-2.7-checkpoints.md).

Terms on this slide — quick definitions for the room:

A checkpoint is a saved snapshot of your code and conversation you can roll back to after an experiment.
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
This slide lists key points under A Safety Net for Experiments.

The slide title is: A Safety Net for Experiments.

The slide says: What Checkpoints Save:.

The slide says: When to Create Checkpoints:.

Bullet 1 on the slide: Code changes made by the agent.

Bullet 2 on the slide: Conversation history · File states.

Bullet 3 on the slide: Before complex changes · At milestones (Step 2 of 5).

Bullet 4 on the slide: Before risky experiments · Before terminal commands.

Terms on this slide — quick definitions for the room:

A checkpoint is a saved snapshot of your code and conversation you can roll back to after an experiment.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 2.7 — Create & Restore

**Step 1:** Create a checkpoint before making a change

```bash
# Click checkpoint icon in Agent panel
# Windows: ``Ctrl+Shift+S`` (Mac: ``Cmd+Shift+S``)
```

<!--
We are starting Exercise 2.7 — Checkpoints. We have about 8 min for this lab.

Create and restore checkpoints before risky Agent experiments.

The full lab guide is in slide-exercises/module-02/exercise-2.7-checkpoints.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: Create a checkpoint before making a change.

Copy this into the Agent chat: "# Click checkpoint icon in Agent panel # Windows: ``Ctrl+Shift+S`` (Mac: ``Cmd+Shift+S``)"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.7 — Create & Restore.

You will also see the heading: Click checkpoint icon in Agent panel.

You will also see the heading: Windows: `Ctrl+Shift+S (Mac: Cmd+Shift+S`).

The code on the slide reads: # Click checkpoint icon in Agent panel # Windows: ``Ctrl+Shift+S`` (Mac: ``Cmd+Shift+S``).

Terms on this slide — quick definitions for the room:

A checkpoint is a saved snapshot of your code and conversation you can roll back to after an experiment.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 2.7 — Steps 2–3

**Step 2:** Name it descriptively: `"Before auth refactor - safe point"`

**Step 3:** Let the agent make changes:

```
Add input validation to all form handlers.
```

<!--
Now for Steps 2–3.

Step 2: Name it descriptively: "Before auth refactor - safe point".

Step 3: Let the agent make changes:.

Copy this into the Agent chat: "Add input validation to all form handlers."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.7 — Steps 2–3.

The code on the slide reads: Add input validation to all form handlers..

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 2.7 — Steps 4–5

**Step 4:** If something goes wrong → **Restore to checkpoint**

**Step 5:** View history via the clock icon in Agent panel

<!--
Now for Steps 4–5.

Step 4: If something goes wrong → Restore to checkpoint.

Step 5: View history via the clock icon in Agent panel.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.7 — Steps 4–5.

Terms on this slide — quick definitions for the room:

A checkpoint is a saved snapshot of your code and conversation you can roll back to after an experiment.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
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
This slide lists key points under Checkpoint Best Practices.

The slide title is: Checkpoint Best Practices.

Success criteria are listed on the slide as follows.

Bullet 1 on the slide: Create checkpoints every 5–10 minutes during complex work.

Bullet 2 on the slide: Use descriptive names, not "checkpoint1".

Bullet 3 on the slide: Test the restored state before continuing.

Bullet 4 on the slide: Clean up old checkpoints periodically.

Bullet 5 on the slide: Created checkpoint · Made changes · Restored · Verified restoration.

Terms on this slide — quick definitions for the room:

A checkpoint is a saved snapshot of your code and conversation you can roll back to after an experiment.

Checkpoints are undo for agent experiments — create one before risky prompts or broad @folder mentions.
-->

---



<!-- _class: lead -->

# Lesson 2.8

## Terminal Integration

*Concept · 5 min · Exercise · 8 min*

**Lab guide:** [`Exercise 2.8](../slide-exercises/module-02/exercise-2.8-terminal-integration.md)

<!--
Lesson 2.8: Terminal Integration. For this lesson, listen, participate, or follow along as indicated on the next slides.

Let the Agent run terminal commands and react to command output.

The detailed lab guide is slide-exercises/module-02/exercise-2.8-terminal-integration.md.

The slide title is: Lesson 2.8.

You will also see the heading: Terminal Integration.

The note on screen reads: Concept · 5 min · Exercise · 8 min.

The slide says: Lab guide: [`Exercise 2.8](../slide-exercises/module-02/exercise-2.8-terminal-integration.md).
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
This slide lists key points under What the Agent Can Do.

The slide title is: What the Agent Can Do.

The slide says: Safety Features:.

Bullet 1 on the slide: Run shell commands · See stdout, stderr, exit codes.

Bullet 2 on the slide: React to command output · Install dependencies.

Bullet 3 on the slide: Run tests · Start/stop services.

Bullet 4 on the slide: You approve each command before execution.

Bullet 5 on the slide: Commands appear in terminal for you to see.

Bullet 6 on the slide: You can reject dangerous commands.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-md -->

## Exercise 2.8 — Steps 1–3

**Demonstration (Windows):** **PowerShell** · Agent ``Ctrl+I``

**Step 1:** Check the environment:

```
Run `python --version` and `gcc --version` in PowerShell.
Tell me what versions we're using.
```

**Step 2:** Approve the command when prompted

**Step 3:** List project files:

```
Run `dir` and tell me which file looks like the main program.
```

<!--
We are starting Exercise 2.8 — Terminal Integration. We have about 13 min for this lab.

Let the Agent run terminal commands and react to command output.

The full lab guide is in slide-exercises/module-02/exercise-2.8-terminal-integration.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: Check the environment:.

Step 2: Approve the command when prompted.

Step 3: List project files:.

Copy this into the Agent chat: "Run `python --version` and `gcc --version` in PowerShell. Tell me what versions we're using."

Copy this into the Agent chat: "Run `dir` and tell me which file looks like the main program."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.8 — Steps 1–3.

Environment note on the slide: Demonstration (Windows): PowerShell · Agent `Ctrl+I`.

The code on the slide reads: Run `python --version` and `gcc --version` in PowerShell. Tell me what versions we're using..

The code on the slide reads: Run `dir` and tell me which file looks like the main program..

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-sm -->

## Exercise 2.8 — Agent Terminal Loop

<img src="assets/module-02/exercise-2-8-agent-terminal-loop.svg" alt="Exercise 2.8 — Agent Terminal Loop" />

<!--
Now for Agent Terminal Loop.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.8 — Agent Terminal Loop.

The figure on this slide is titled: Exercise 2.8 — Agent Terminal Loop.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 2.8 — Step 5: Install Dependency

**Step 5:** Install a dependency (Windows):

```
Install the requests library with pip if it's not already installed.
Use: py -m pip install requests
Show me the command output.
```

<!--
Now for Step 5: Install Dependency.

Copy this into the Agent chat: "Install the requests library with pip if it's not already installed. Use: py -m pip install requests Show me the command output."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.8 — Step 5: Install Dependency.

Step 5: Install a dependency (Windows):.

The code on the slide reads: Install the requests library with pip if it's not already installed. Use: py -m pip install requests Show me the command output..
-->

---







<!-- _class: fit-sm -->

## Exercise 2.8 — Step 6: Multi-Step Workflow

**Step 6:** Multi-step workflow (Windows PowerShell):

```
Run these commands in order:
1. git status
2. git branch
3. dir

Summarize what you see after each command.
Confirm before each command that might affect the repo.
```

<!--
Now for Step 6: Multi-Step Workflow.

Copy this into the Agent chat: "Run these commands in order: 1. git status 2. git branch 3. dir Summarize what you see after each command. Confirm before each command that might affect the repo."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 2.8 — Step 6: Multi-Step Workflow.

Step 6: Multi-step workflow (Windows PowerShell):.

The code on the slide reads: Run these commands in order: 1. git status 2. git branch 3. dir Summarize what you see after each command. Confirm before each command that might affect the repo..
-->

---







<!-- _class: fit-md -->

## Terminal Command Safety Rules

| Category | Commands |
|----------|----------|
| **Always approve first** | `Remove-Item`, `sudo`, `git push --force`, production changes |
| **Review carefully** | `pip install`, `npm install`, git branch changes, docker |
| **Safe to auto-approve (Windows demo)** | `python --version`, `dir`, `Get-Location`, `Get-Content`, `pytest`, `npm test` |

**Success Criteria:**
- Ran version check · Ran tests and reacted to output
- Installed dependency · Executed multi-step workflow

<!--
This slide is a table — Terminal Command Safety Rules.

The slide title is: Terminal Command Safety Rules.

Success criteria are listed on the slide as follows.

Bullet 1 on the slide: Ran version check · Ran tests and reacted to output.

Bullet 2 on the slide: Installed dependency · Executed multi-step workflow.

The table header columns are: Category, Commands.

In the table, **Always approve first**: `Remove-Item`, `sudo`, `git push --force`, production changes.

In the table, **Review carefully**: `pip install`, `npm install`, git branch changes, docker.

In the table, **Safe to auto-approve (Windows demo)**: `python --version`, `dir`, `Get-Location`, `Get-Content`, `pytest`, `npm test`.

Terms on this slide — quick definitions for the room:

npm is the Node Package Manager — the default registry and tool for JavaScript packages.
-->

---







<!-- _header: 'Module 3 — Agent Modes and Tools' -->

<!-- _class: lead -->

# Agent Modes and Tools

## Module 3 · Day 1 (Hands-On + Concept)

Cursor Training Program · ~60 min

<!--
Module 3 connects Ask Mode, Agent Mode, the browser, the terminal, and prompting craft to the mental models from Module 1.

The slide title is: Agent Modes and Tools.

You will also see the heading: Module 3 · Day 1 (Hands-On + Concept).

The slide says: Cursor Training Program · ~60 min.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-md -->

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise + concept |
| **Prerequisites** | Module 2 completed, live web app available (or sample provided) |
| **Module Goal** | Master different agent modes and the core tools that make agents powerful |

### Lessons

| Lesson | Topic | Time |
|--------|-------|------|
| 3.1 | Ask Mode vs. Agent Mode | 18 min |
| 3.2 | Browser Tool | 18 min |
| 3.3 | Terminal Tool | 20 min |
| 3.4 | Effective Prompting in Practice | 22 min |

<!--
Here is the overview for Module 3.

The slide title is: Module Overview.

The table header columns are: Aspect, Details.

In the table, **Duration**: ~60 minutes.

In the table, **Format**: Hands-on exercise + concept.

In the table, **Prerequisites**: Module 2 completed, live web app available (or sample provided).

In the table, **Module Goal**: Master different agent modes and the core tools that make agents powerful.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---



<!-- _class: lead -->

# Lesson 3.1

## Ask Mode vs. Agent Mode

*Concept · 10 min · Exercise · 8 min*

**Lab guide:** [`Exercise 3.1](../slide-exercises/module-03/exercise-3.1-ask-mode-vs-agent-mode.md)

<!--
Lesson 3.1: Ask Mode vs. Agent Mode. For this lesson, listen, participate, or follow along as indicated on the next slides.

Learn when Ask Mode is read-only and when Agent Mode can edit files.

Ask Mode is read-only — great for architecture questions and understanding code without surprise diffs.

Agent Mode can edit files. Same question, different risk profile. Watch the mode indicator in the panel footer before you send.

The detailed lab guide is slide-exercises/module-03/exercise-3.1-ask-mode-vs-agent-mode.md.

The slide title is: Lesson 3.1.

You will also see the heading: Ask Mode vs. Agent Mode.

The note on screen reads: Concept · 10 min · Exercise · 8 min.

The slide says: Lab guide: [`Exercise 3.1](../slide-exercises/module-03/exercise-3.1-ask-mode-vs-agent-mode.md).

Terms on this slide — quick definitions for the room:

Agent Mode lets Cursor edit files, run terminal commands, and use tools — always with your review before changes land.

Ask Mode is Cursor's read-only mode — the model can answer questions but cannot edit files or run tools.
-->

---







<!-- _class: fit-sm -->

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
This slide is a table — The Core Distinction.

The slide title is: The Core Distinction.

The table header columns are: Aspect, Ask Mode, Agent Mode.

In the table, **Can read files** — ✅ Yes (with @mentions). Use case on slide: ✅ Yes.

In the table, **Can edit files** — ❌ No. Use case on slide: ✅ Yes.

In the table, **Can run terminal** — ❌ No. Use case on slide: ✅ Yes.

In the table, **Can browse web** — ❌ No (limited). Use case on slide: ✅ Yes (with tool).

In the table, **Can call tools** — ❌ No. Use case on slide: ✅ Yes.

In the table, **Safety level** — Very high (read-only). Use case on slide: Moderate (needs oversight).

In the table, **Best for** — Questions, learning, code review. Use case on slide: Implementation, debugging, automation.

Terms on this slide — quick definitions for the room:

Agent Mode lets Cursor edit files, run terminal commands, and use tools — always with your review before changes land.

Ask Mode is Cursor's read-only mode — the model can answer questions but cannot edit files or run tools.

An @mention points the agent at specific context — a file, folder, symbol, branch, or the web.
-->

---







<!-- _class: fit-md -->

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
This slide lists key points under When to Use Each Mode.

The slide title is: When to Use Each Mode.

The slide says: USE ASK MODE when:.

The slide says: USE AGENT MODE when:.

Bullet 1 on the slide: You have a question about code · Exploring a codebase.

Bullet 2 on the slide: You want a second opinion on design.

Bullet 3 on the slide: You're not ready to make changes · Production environment.

Bullet 4 on the slide: You want the AI to write/change code.

Bullet 5 on the slide: You need to run and react to commands.

Bullet 6 on the slide: Multi-step tasks · Development environment.

Bullet 7 on the slide: You're prepared to review changes.

Terms on this slide — quick definitions for the room:

Agent Mode lets Cursor edit files, run terminal commands, and use tools — always with your review before changes land.

Ask Mode is Cursor's read-only mode — the model can answer questions but cannot edit files or run tools.
-->

---







<!-- _class: fit-md -->

## Safety Implications

| Risk | Ask Mode | Agent Mode |
|------|----------|------------|
| Unintended code changes | None | Moderate (requires review) |
| File deletion | None | Possible (needs approval) |
| Malicious commands | None | Possible (needs approval) |
| Data leakage | Low | Medium (can read files) |
| API cost | Low (no tool calls) | Higher (multiple tool calls) |

<!--
This slide is a table — Safety Implications.

The slide title is: Safety Implications.

The table header columns are: Risk, Ask Mode, Agent Mode.

In the table, Unintended code changes — None. Use case on slide: Moderate (requires review).

In the table, File deletion — None. Use case on slide: Possible (needs approval).

In the table, Malicious commands — None. Use case on slide: Possible (needs approval).

In the table, Data leakage — Low. Use case on slide: Medium (can read files).

In the table, API cost — Low (no tool calls). Use case on slide: Higher (multiple tool calls).

Terms on this slide — quick definitions for the room:

Agent Mode lets Cursor edit files, run terminal commands, and use tools — always with your review before changes land.

Ask Mode is Cursor's read-only mode — the model can answer questions but cannot edit files or run tools.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

The practical rule is on the slide: never trust a single run as ground truth. Run the code, read the diff, check the docs — every time.

Teams that skip verification accumulate AI debt — code that looked fine in chat but fails in CI.
-->

---







<!-- _class: fit-xs -->

## The Mode Continuum

<img src="assets/module-03/the-mode-continuum.svg" alt="The Mode Continuum" />

> *"Not every AI interaction needs full agent capabilities."*

<!--
This slide includes a diagram — The Mode Continuum.

The slide title is: The Mode Continuum.

The slide quotes: ""Not every AI interaction needs full agent capabilities.""

The figure on this slide is titled: The Mode Continuum.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-sm -->

## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Agent panel** (``Ctrl+I``) is for prompts and tool use · **Chat** (``Ctrl+L``) is read-only Q&A.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

The slide title is: Windows Exercise Environment.

The slide says: All exercises in this module assume Windows 10/11 with Cursor installed.

The slide says: Agent panel (`Ctrl+I) is for prompts and tool use · Chat (Ctrl+L`) is read-only Q&A.

The slide says: Set default profile: Settings → terminal.integrated.defaultProfile.windows → PowerShell.

The table header columns are: Terminal, Use when, Open in Cursor.

In the table, **PowerShell** — Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`). Use case on slide: ``Ctrl+` `` → **PowerShell**.

In the table, **Git Bash** — Bash syntax, `export VAR=...`, shell scripts ending in `.sh`. Use case on slide: Terminal menu → **Git Bash**.

In the table, **Command Prompt** — Legacy `.bat` files only. Use case on slide: Terminal menu → **Command Prompt**.

In the table, **Ubuntu (WSL)** — Linux-only tools or native bash without Git Bash. Use case on slide: Terminal menu → **Ubuntu (WSL)**.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.

npm is the Node Package Manager — the default registry and tool for JavaScript packages.
-->

---







## Exercise 3.1 — Steps 1–2

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**


**Step 1:** Open Agent panel (`Cmd+I` / `Ctrl+I`) — note mode indicator at bottom
**Where:** **Agent panel** — ``Ctrl+I``

<!--
We are starting Exercise 3.1 — Ask Mode vs. Agent Mode. We have about 18 min for this lab.

Learn when Ask Mode is read-only and when Agent Mode can edit files.

The full lab guide is in slide-exercises/module-03/exercise-3.1-ask-mode-vs-agent-mode.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: Open Agent panel (Cmd+I / Ctrl+I) — note mode indicator at bottom.

Where: Agent panel — `Ctrl+I`.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.1 — Steps 1–2.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 3.1 — Steps 1–2 (Part 2)

**Step 2:** Try to make a change in **Ask Mode**:
**Where:** **Agent panel** — ``Ctrl+I``

```
Change the variable name 'temp' to 'temperature' in the current file.
```

<!--
Now for Steps 1–2 (Part 2).

Step 2: Try to make a change in Ask Mode:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "Change the variable name 'temp' to 'temperature' in the current file."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.1 — Steps 1–2 (Part 2).

The code on the slide reads: Change the variable name 'temp' to 'temperature' in the current file..

Terms on this slide — quick definitions for the room:

Temperature controls randomness — low values stay focused and repeatable; high values add creativity and variation.

Ask Mode is Cursor's read-only mode — the model can answer questions but cannot edit files or run tools.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 3.1 — Steps 3–5

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**


**Step 3:** Ask a question Ask Mode handles well:
**Where:** **Agent panel** — ``Ctrl+I``

```
Explain the purpose of the main() function in this file.
What edge cases does it handle?
```

<!--
Now for Steps 3–5.

Step 3: Ask a question Ask Mode handles well:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "Explain the purpose of the main() function in this file. What edge cases does it handle?"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.1 — Steps 3–5.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The code on the slide reads: Explain the purpose of the main() function in this file. What edge cases does it handle?.

Terms on this slide — quick definitions for the room:

Ask Mode is Cursor's read-only mode — the model can answer questions but cannot edit files or run tools.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 3.1 — Steps 3–5 (Part 2)

**Step 4:** Switch to **Agent Mode** via the dropdown
**Where:** **Agent panel** — ``Ctrl+I``

**Step 5:** Repeat the rename request — agent shows diff for approval
**Where:** **Agent panel** — ``Ctrl+I``

<!--
Now for Steps 3–5 (Part 2).

Step 4: Switch to Agent Mode via the dropdown.

Where: Agent panel — `Ctrl+I`.

Step 5: Repeat the rename request — agent shows diff for approval.

Where: Agent panel — `Ctrl+I`.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.1 — Steps 3–5 (Part 2).

Terms on this slide — quick definitions for the room:

Agent Mode lets Cursor edit files, run terminal commands, and use tools — always with your review before changes land.
-->

---







<!-- _class: fit-sm -->

## Exercise 3.1 — Step 6 & Success Criteria

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

**Step 6:** Practice mode-switching mid-conversation:
**Where:** **Agent panel** — ``Ctrl+I``

```
# Start in Ask Mode: What does this function return?
# Then: "Switch to Agent Mode and fix the off-by-one error"
```

**Success Criteria:**
- Used Ask Mode for questions · Observed Ask Mode cannot make changes
- Switched to Agent Mode · Made a change with diff review

<!--
That finishes Exercise 3.1 — Ask Mode vs. Agent Mode.

Check off what you actually did: Used Ask Mode for questions · Observed Ask Mode cannot make changes; Switched to Agent Mode · Made a change with diff review.

Raise your hand if you finished. What did the Agent get wrong, and what prompt change fixed it?

The slide title is: Exercise 3.1 — Step 6 & Success Criteria.

You will also see the heading: Start in Ask Mode: What does this function return?.

You will also see the heading: Then: "Switch to Agent Mode and fix the off-by-one error".

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

Step 6: Practice mode-switching mid-conversation:.

Where: Agent panel — `Ctrl+I`.

Success criteria are listed on the slide as follows.

Bullet 1 on the slide: Used Ask Mode for questions · Observed Ask Mode cannot make changes.

Bullet 2 on the slide: Switched to Agent Mode · Made a change with diff review.

The code on the slide reads: # Start in Ask Mode: What does this function return? # Then: "Switch to Agent Mode and fix the off-by-one error".

Terms on this slide — quick definitions for the room:

Diff review is reading added and removed lines before you accept an AI edit — your primary quality gate.

Agent Mode lets Cursor edit files, run terminal commands, and use tools — always with your review before changes land.

Ask Mode is Cursor's read-only mode — the model can answer questions but cannot edit files or run tools.
-->

---



<!-- _class: lead -->

# Lesson 3.2

## Browser Tool

*Concept · 8 min · Exercise · 10 min*

**Lab guide:** [`Exercise 3.2](../slide-exercises/module-03/exercise-3.2-browser-tool.md)

<!--
Lesson 3.2: Browser Tool. For this lesson, listen, participate, or follow along as indicated on the next slides.

Use the Browser tool so the Agent can inspect live web pages.

The Browser tool lets the Agent see what users see — rendered pages, console errors, layout issues CSS alone won't reveal.

The detailed lab guide is slide-exercises/module-03/exercise-3.2-browser-tool.md.

The slide title is: Lesson 3.2.

You will also see the heading: Browser Tool.

The note on screen reads: Concept · 8 min · Exercise · 10 min.

The slide says: Lab guide: [`Exercise 3.2](../slide-exercises/module-03/exercise-3.2-browser-tool.md).

Terms on this slide — quick definitions for the room:

The Browser tool lets the agent open a live page, inspect the DOM, and read console or network activity.
-->

---







## What the Browser Tool Can Do

- Navigate to URLs · Read page content and DOM structure
- See console logs and errors · Take screenshots (depending on model)
- Click elements and interact with pages
- Extract data from live pages

> *"See what your app actually looks like in a browser — not just the source code."*

<!--
This slide highlights a key quote — What the Browser Tool Can Do.

The slide title is: What the Browser Tool Can Do.

The slide quotes: ""See what your app actually looks like in a browser — not just the source code.""

Bullet 1 on the slide: Navigate to URLs · Read page content and DOM structure.

Bullet 2 on the slide: See console logs and errors · Take screenshots (depending on model).

Bullet 3 on the slide: Click elements and interact with pages.

Bullet 4 on the slide: Extract data from live pages.

Terms on this slide — quick definitions for the room:

The Browser tool lets the agent open a live page, inspect the DOM, and read console or network activity.

DOM stands for Document Object Model — the live tree structure of elements on a web page.

The Browser tool lets the Agent see what users see — rendered pages, console errors, layout issues CSS alone won't reveal.
-->

---







<!-- _class: fit-md -->

## Browser Tool: With vs. Without

| Scenario | Without Browser | With Browser |
|----------|----------------|--------------|
| "Why is the button not showing?" | Guesses from CSS | Sees the rendered page |
| "Is the API returning data?" | Checks code | Sees network tab |
| "What console errors?" | Asks you | Reads console directly |
| "Does responsive layout work?" | Trusts CSS | Views at different sizes |

<!--
This slide is a table — Browser Tool: With vs. Without.

The slide title is: Browser Tool: With vs. Without.

The table header columns are: Scenario, Without Browser, With Browser.

In the table, "Why is the button not showing?" — Guesses from CSS. Use case on slide: Sees the rendered page.

In the table, "Is the API returning data?" — Checks code. Use case on slide: Sees network tab.

In the table, "What console errors?" — Asks you. Use case on slide: Reads console directly.

In the table, "Does responsive layout work?" — Trusts CSS. Use case on slide: Views at different sizes.

Terms on this slide — quick definitions for the room:

The Browser tool lets the agent open a live page, inspect the DOM, and read console or network activity.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

The Browser tool lets the Agent see what users see — rendered pages, console errors, layout issues CSS alone won't reveal.
-->

---







## Exercise 3.2 — Steps 1–2

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent ``Ctrl+I``


**Step 1:** Start a local web app (or use a public test page)
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
python -m http.server 8000
# Or use a public test page
```

<!--
We are starting Exercise 3.2 — Browser Tool. We have about 18 min for this lab.

Use the Browser tool so the Agent can inspect live web pages.

The full lab guide is in slide-exercises/module-03/exercise-3.2-browser-tool.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: Start a local web app (or use a public test page).

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "python -m http.server 8000 # Or use a public test page"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.2 — Steps 1–2.

You will also see the heading: Or use a public test page.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent Ctrl+I`.

The code on the slide reads: python -m http.server 8000 # Or use a public test page.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

HTTP stands for Hypertext Transfer Protocol — the request/response protocol browsers and APIs use.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
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
Now for Steps 1–2 (Part 2).

Step 2: In Agent Mode:.

Terminal: PowerShell — `Ctrl+ `` in Cursor.

Copy this into the Agent chat: "Use the browser tool to open http://localhost:8000 Tell me what you see on the page."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.2 — Steps 1–2 (Part 2).

The code on the slide reads: Use the browser tool to open http://localhost:8000 Tell me what you see on the page..

Terms on this slide — quick definitions for the room:

The Browser tool lets the agent open a live page, inspect the DOM, and read console or network activity.

Agent Mode lets Cursor edit files, run terminal commands, and use tools — always with your review before changes land.

HTTP stands for Hypertext Transfer Protocol — the request/response protocol browsers and APIs use.
-->

---







<!-- _class: fit-sm -->

## Exercise 3.2 — Steps 3–4

**Demonstration (Windows):** Agent ``Ctrl+I`` · **PowerShell** · Browser for dashboards


**Step 3:** Find specific elements:
**Where:** **Agent panel** — ``Ctrl+I``

```
On that same page, find:
1. The main heading text
2. The number of buttons
3. Any error messages visible
```

<!--
Now for Steps 3–4.

Step 3: Find specific elements:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "On that same page, find: 1. The main heading text 2. The number of buttons 3. Any error messages visible"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.2 — Steps 3–4.

Environment note on the slide: Demonstration (Windows): Agent `Ctrl+I` · PowerShell · Browser for dashboards.

The code on the slide reads: On that same page, find: 1. The main heading text 2. The number of buttons 3. Any error messages visible.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 3.2 — Steps 3–4 (Part 2)

**Step 4:** Check the console:
**Where:** **Agent panel** — ``Ctrl+I``

```
Now open the browser developer console.
Are there any errors or warnings? If so, what are they?
```

<!--
Now for Steps 3–4 (Part 2).

Step 4: Check the console:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "Now open the browser developer console. Are there any errors or warnings? If so, what are they?"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.2 — Steps 3–4 (Part 2).

The code on the slide reads: Now open the browser developer console. Are there any errors or warnings? If so, what are they?.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-sm -->

## Expected Agent Actions

<img src="assets/module-03/expected-agent-actions.svg" alt="Expected Agent Actions" />

<!--
This slide includes a diagram — Expected Agent Actions.

The slide title is: Expected Agent Actions.

The figure on this slide is titled: Expected Agent Actions.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 3.2 — Steps 5–6

**Demonstration (Windows):** Agent ``Ctrl+I`` · **PowerShell** · Browser for dashboards


**Step 5:** Diagnose a layout issue:
**Where:** **Agent panel** — ``Ctrl+I``

```
The login button is partially hidden on mobile sizes.
Use the browser tool to check what's happening.
```

<!--
Now for Steps 5–6.

Step 5: Diagnose a layout issue:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "The login button is partially hidden on mobile sizes. Use the browser tool to check what's happening."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.2 — Steps 5–6.

Environment note on the slide: Demonstration (Windows): Agent `Ctrl+I` · PowerShell · Browser for dashboards.

The code on the slide reads: The login button is partially hidden on mobile sizes. Use the browser tool to check what's happening..

Terms on this slide — quick definitions for the room:

The Browser tool lets the agent open a live page, inspect the DOM, and read console or network activity.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 3.2 — Steps 5–6 (Part 2)

**Step 6:** Extract data from a page:
**Where:** **Agent panel** — ``Ctrl+I``

```
Go to https://example.com/pricing
Extract all pricing plan names and their monthly costs into a table.
```

<!--
Now for Steps 5–6 (Part 2).

Step 6: Extract data from a page:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "Go to https://example.com/pricing Extract all pricing plan names and their monthly costs into a table."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.2 — Steps 5–6 (Part 2).

The code on the slide reads: Go to https://example.com/pricing Extract all pricing plan names and their monthly costs into a table..

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-md -->

## Browser Tool Limitations

| Limitation | Workaround |
|------------|------------|
| Cannot log in to sites | Provide login instructions or session cookies |
| JavaScript-heavy sites may load slowly | Add wait instructions |
| Rate limits on some sites | Space out requests |
| Cannot upload files | Not supported yet |

**Success Criteria:** Opened URL · Read content · Checked console · Extracted data

<!--
This slide is a table — Browser Tool Limitations.

The slide title is: Browser Tool Limitations.

Success criteria listed: Opened URL · Read content · Checked console · Extracted data.

The table header columns are: Limitation, Workaround.

In the table, Cannot log in to sites: Provide login instructions or session cookies.

In the table, JavaScript-heavy sites may load slowly: Add wait instructions.

In the table, Rate limits on some sites: Space out requests.

In the table, Cannot upload files: Not supported yet.

Terms on this slide — quick definitions for the room:

The Browser tool lets the agent open a live page, inspect the DOM, and read console or network activity.

A rate limit caps how many API requests you can make in a time window — exceed it and you get HTTP 429.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.

The Browser tool lets the Agent see what users see — rendered pages, console errors, layout issues CSS alone won't reveal.
-->

---



<!-- _class: lead -->

# Lesson 3.3

## Terminal Tool

*Concept · 8 min · Exercise · 12 min*

**Lab guide:** [`Exercise 3.3](../slide-exercises/module-03/exercise-3.3-terminal-tool.md)

<!--
Lesson 3.3: Terminal Tool. For this lesson, listen, participate, or follow along as indicated on the next slides.

Use the Terminal tool to run tests, read output, and fix failures.

The Terminal tool lets the Agent run tests and builds and read real output. That is how we turn guesses into evidence.

The detailed lab guide is slide-exercises/module-03/exercise-3.3-terminal-tool.md.

The slide title is: Lesson 3.3.

You will also see the heading: Terminal Tool.

The note on screen reads: Concept · 8 min · Exercise · 12 min.

The slide says: Lab guide: [`Exercise 3.3](../slide-exercises/module-03/exercise-3.3-terminal-tool.md).

Terms on this slide — quick definitions for the room:

The Terminal tool lets the agent propose shell commands — you approve them, then it reads stdout and stderr.
-->

---







## What the Terminal Tool Can Do

- Run any shell command (with approval)
- See stdout, stderr, exit codes
- Read command output as context for next actions
- Chain commands based on previous results

<!--
This slide lists key points under What the Terminal Tool Can Do.

The slide title is: What the Terminal Tool Can Do.

Bullet 1 on the slide: Run any shell command (with approval).

Bullet 2 on the slide: See stdout, stderr, exit codes.

Bullet 3 on the slide: Read command output as context for next actions.

Bullet 4 on the slide: Chain commands based on previous results.

Terms on this slide — quick definitions for the room:

The Terminal tool lets the agent propose shell commands — you approve them, then it reads stdout and stderr.

The Terminal tool lets the Agent run tests and builds and read real output. That is how we turn guesses into evidence.
-->

---







<!-- _class: fit-sm -->

## Terminal Tool Flow

<img src="assets/module-03/terminal-tool-flow.svg" alt="Terminal Tool Flow" />

<!--
This slide includes a diagram — Terminal Tool Flow.

The slide title is: Terminal Tool Flow.

The figure on this slide is titled: Terminal Tool Flow.

Terms on this slide — quick definitions for the room:

The Terminal tool lets the agent propose shell commands — you approve them, then it reads stdout and stderr.

The Terminal tool lets the Agent run tests and builds and read real output. That is how we turn guesses into evidence.
-->

---







## Exercise 3.3 — Setup

**Before you start**

**Goal:** Use the terminal tool on the calculator test project in this repo.

**Do this first:**
1. **File → Open Folder** → `core-exercises/exercise-11/`
2. Open **Agent panel** — ``Ctrl+I``
3. Confirm **Agent Mode** (`/agent`)
4. Need **`gcc`** installed (compile C tests)

Files in folder: `test_calculator.c`, `run_tests.bat`, `run_tests.sh`

<!--
We are starting Exercise 3.3 — Terminal Tool. We have about 20 min for this lab.

Use the Terminal tool to run tests, read output, and fix failures.

The full lab guide is in slide-exercises/module-03/exercise-3.3-terminal-tool.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

If the lab asked you to break a test, the Agent should read the failing output — not guess the fix.

Use the terminal tool on the calculator test project in this repo.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.3 — Setup.

The slide says: Before you start.

The slide says: Do this first:.

The slide says: 1. File → Open Folder → core-exercises/exercise-11/.

The slide says: 2. Open Agent panel — `Ctrl+I`.

The slide says: 3. Confirm Agent Mode (/agent).

The slide says: 4. Need gcc installed (compile C tests).

The slide says: Files in folder: test_calculator.c, run_tests.bat, run_tests.sh.

Number 1 on the slide: File → Open Folder → core-exercises/exercise-11/.

Number 2 on the slide: Open Agent panel — `Ctrl+I`.

Number 3 on the slide: Confirm Agent Mode (/agent).

Number 4 on the slide: Need gcc installed (compile C tests).

Terms on this slide — quick definitions for the room:

The Terminal tool lets the agent propose shell commands — you approve them, then it reads stdout and stderr.

Agent Mode lets Cursor edit files, run terminal commands, and use tools — always with your review before changes land.
-->

---







<!-- _class: fit-md -->

## Exercise 3.3 — Step 1: Safe Command

**Step 1 — Read-only command**

**Goal:** Approve a low-risk terminal command.

**Where:** **Agent panel** — ``Ctrl+I``

```
Check whether gcc and git are available.

Run gcc --version and git --version.
Summarize the output. Do not modify any files.
```

**Look for:** Version strings in chat · no file edits

<!--
Now for Step 1: Safe Command.

Learn which commands usually need careful review.

Step 1 — Read-only command.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "Check whether gcc and git are available. Run gcc --version and git --version. Summarize the output. Do not modify any files."

If the lab asked you to break a test, the Agent should read the failing output — not guess the fix.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.3 — Step 1: Safe Command.

Goal: Approve a low-risk terminal command.

Look for: Version strings in chat · no file edits.

The code on the slide reads: Check whether gcc and git are available. Run gcc --version and git --version. Summarize the output. Do not modify any files..

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-md -->

## Exercise 3.3 — Step 2: Run Passing Tests

**Step 2 — Run test suite**

**Goal:** Compile and run tests — all should pass first.

**Windows (demo — PowerShell):**
```
Run .\run_tests.bat in this folder.
Show full output: compilation OK? how many tests passed?
```

**Other platforms (optional):** Mac/Linux — `./run_tests.sh`

**Look for:** Four `PASS:` lines · `All tests passed!`

<!--
Now for Step 2: Run Passing Tests.

Compile and run tests — all should pass first.

You should see: Four PASS: lines · All tests passed!

Step 2 — Run test suite.

Copy this into the Agent chat: "Run .\run_tests.bat in this folder. Show full output: compilation OK? how many tests passed?"

If the lab asked you to break a test, the Agent should read the failing output — not guess the fix.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.3 — Step 2: Run Passing Tests.

The slide says: Windows (demo — PowerShell):.

The slide says: Other platforms (optional): Mac/Linux — ./run_tests.sh.

Look for: Four PASS: lines · All tests passed!.

The code on the slide reads: Run .\run_tests.bat in this folder. Show full output: compilation OK? how many tests passed?.
-->

---







## Exercise 3.3 — Step 3: Break a Test

**Step 3 — Introduce a failure (you edit)**

**Goal:** Create a known bug before debugging.

1. Open **`test_calculator.c`**
2. Change `assert(add(2, 3) == 5);` → **`== 6`**
3. Save — **do not ask Agent to edit yet**

**Look for:** File saved with wrong expected value

<!--
Now for Step 3: Break a Test.

Compile and run tests — all should pass first.

You should see: Four PASS: lines · All tests passed!

Step 3 — Introduce a failure (you edit).

If the lab asked you to break a test, the Agent should read the failing output — not guess the fix.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.3 — Step 3: Break a Test.

Goal: Create a known bug before debugging.

The slide says: 1. Open test_calculator.c.

The slide says: 2. Change assert(add(2, 3) == 5); → == 6.

The slide says: 3. Save — do not ask Agent to edit yet.

Look for: File saved with wrong expected value.

Number 1 on the slide: Open test_calculator.c.

Number 2 on the slide: Change assert(add(2, 3) == 5); → == 6.

Number 3 on the slide: Save — do not ask Agent to edit yet.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-md -->

## Exercise 3.3 — Step 4: Diagnose Failure

**Step 4 — Read terminal output**

**Goal:** Agent explains the failure without fixing yet.

```
@test_calculator.c

Run the test suite again.
Which test failed? What assertion failed?
Is the bug in the test or in add()? Explain only — do not fix yet.
```

**Look for:** Names `test_add` · expects 6, got 5 · test is wrong

<!--
Now for Step 4: Diagnose Failure.

Use the terminal tool on the calculator test project in this repo.

Step 4 — Read terminal output.

Copy this into the Agent chat: "@test_calculator.c Run the test suite again. Which test failed? What assertion failed? Is the bug in the test or in add()? Explain only — do not fix yet."

Keep @calculator.c in the prompt so the Agent stays in the right file.

If the lab asked you to break a test, the Agent should read the failing output — not guess the fix.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.3 — Step 4: Diagnose Failure.

Goal: Agent explains the failure without fixing yet.

Look for: Names test_add · expects 6, got 5 · test is wrong.

The code on the slide reads: @test_calculator.c Run the test suite again. Which test failed? What assertion failed? Is the bug in the test or in add()? Explain only — do not fix yet..

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-xs -->

## Exercise 3.3 — Step 5: Fix and Verify

**Step 5 — Debug workflow**

**Goal:** Run → fix → re-run until green.

```
@test_calculator.c

1. Run tests and confirm the failure
2. Fix the incorrect assertion in test_add() only
3. Re-run tests and confirm all pass
Show the diff before I accept changes.
```

<img src="assets/module-03/exercise-3-3-debug-workflow-step-5.svg" alt="Debug workflow: run → analyze → fix → verify" />

**Look for:** Two test runs · one-line fix · all tests pass

<!--
Now for Step 5: Fix and Verify.

Use the terminal tool on the calculator test project in this repo.

Step 5 — Debug workflow.

Copy this into the Agent chat: "@test_calculator.c 1. Run tests and confirm the failure 2. Fix the incorrect assertion in test_add() only 3. Re-run tests and confirm all pass Show the diff before I accept changes."

Keep @calculator.c in the prompt so the Agent stays in the right file.

If the lab asked you to break a test, the Agent should read the failing output — not guess the fix.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.3 — Step 5: Fix and Verify.

Goal: Run → fix → re-run until green.

Look for: Two test runs · one-line fix · all tests pass.

The figure on this slide is titled: Debug workflow: run → analyze → fix → verify.

The code on the slide reads: @test_calculator.c 1. Run tests and confirm the failure 2. Fix the incorrect assertion in test_add() only 3. Re-run tests and confirm all pass Show the diff before I accept changes..
-->

---







<!-- _class: fit-sm -->

## Exercise 3.3 — Step 6: Approval Rules

**Step 6 — Safe vs. risky commands**

**Goal:** Know what to review before approving.

**Optional prompt:**
```
Run git status. Summarize only — do not commit or push.
```

| Review carefully | Usually lower risk |
|------------------|-------------------|
| Deletes, `sudo`, `git push --force` | `gcc --version`, `git status`, `ls` |
| Global installs, servers | Project test scripts, local compile |

**Success Criteria:**
- Read-only command run · Tests run with output shown
- Failure introduced · Diagnosis from terminal output
- Fix verified by re-run · Approval rules understood

<!--
Now for Step 6: Approval Rules.

Use the terminal tool on the calculator test project in this repo.

Step 6 — Safe vs. risky commands.

Copy this into the Agent chat: "Run git status. Summarize only — do not commit or push."

If the lab asked you to break a test, the Agent should read the failing output — not guess the fix.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.3 — Step 6: Approval Rules.

Goal: Know what to review before approving.

The slide says: Optional prompt:.

Success criteria are listed on the slide as follows.

Bullet 1 on the slide: Read-only command run · Tests run with output shown.

Bullet 2 on the slide: Failure introduced · Diagnosis from terminal output.

Bullet 3 on the slide: Fix verified by re-run · Approval rules understood.

The table header columns are: Review carefully, Usually lower risk.

In the table, Deletes, `sudo`, `git push --force`: `gcc --version`, `git status`, `ls`.

In the table, Global installs, servers: Project test scripts, local compile.

The code on the slide reads: Run git status. Summarize only — do not commit or push..
-->

---



<!-- _class: lead -->

# Lesson 3.4

## Effective Prompting in Practice

*Concept · 10 min · Exercise · 12 min*

**Lab guide:** [`Exercise 3.4](../slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md)

<!--
Lesson 3.4: Effective Prompting in Practice. For this lesson, listen, participate, or follow along as indicated on the next slides.

Write constrained prompts and reusable templates for real tasks.

Vague prompts produce wide diffs. Constraints — which file, which function, what format — shrink the blast radius.

In the next exercise we use calculator.c on purpose: you will see one vague sentence refactor half the file.

The detailed lab guide is slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md.

The slide title is: Lesson 3.4.

You will also see the heading: Effective Prompting in Practice.

The note on screen reads: Concept · 10 min · Exercise · 12 min.

The slide says: Lab guide: [`Exercise 3.4](../slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md).
-->

---







## Anatomy of an Effective Prompt

1. **ROLE / CONTEXT** — "You are a senior Python developer…"
2. **TASK** — "Fix the bug in calculate_total()…"
3. **CONSTRAINTS** — "Do not change the function signature…"
4. **OUTPUT FORMAT** — "Show me the diff and explain your change…"
5. **SUCCESS CRITERIA** — "Function should return 0 for empty input…"

<!--
Let's look at Anatomy of an Effective Prompt.

The slide title is: Anatomy of an Effective Prompt.

The slide says: 1. ROLE / CONTEXT — "You are a senior Python developer…".

The slide says: 2. TASK — "Fix the bug in calculate_total()…".

The slide says: 3. CONSTRAINTS — "Do not change the function signature…".

The slide says: 4. OUTPUT FORMAT — "Show me the diff and explain your change…".

The slide says: 5. SUCCESS CRITERIA — "Function should return 0 for empty input…".

Number 1 on the slide: ROLE / CONTEXT — "You are a senior Python developer…".

Number 2 on the slide: TASK — "Fix the bug in calculate_total()…".

Number 3 on the slide: CONSTRAINTS — "Do not change the function signature…".

Number 4 on the slide: OUTPUT FORMAT — "Show me the diff and explain your change…".

Number 5 on the slide: SUCCESS CRITERIA — "Function should return 0 for empty input…".
-->

---







<!-- _class: fit-md -->

## Bad Prompts vs. Good Prompts

| Bad Prompt | Good Prompt |
|------------|-------------|
| "Fix this code" | "Fix the IndexError in process_list() when list is empty. Do not change return type." |
| `@calculator.c Fix divide` | `@calculator.c Improve divide() for division by zero. Change ONLY divide(). Show diff + cause.` |
| "Add logging" | "Add INFO-level logging to calculate() using existing logger config." |
| "Make it faster" | "Optimize find_user() from O(n²) to O(n log n). Don't change signature." |
| "Review my code" | "Review auth.py for SQL injection, password handling, session issues. Ignore style." |

<!--
This slide is a table — Bad Prompts vs. Good Prompts.

The slide title is: Bad Prompts vs. Good Prompts.

The table header columns are: Bad Prompt, Good Prompt.

In the table, "Fix this code": "Fix the IndexError in process_list() when list is empty. Do not change return type.".

In the table, `@calculator.c Fix divide`: `@calculator.c Improve divide() for division by zero. Change ONLY divide(). Show diff + cause.`.

In the table, "Add logging": "Add INFO-level logging to calculate() using existing logger config.".

In the table, "Make it faster": "Optimize find_user() from O(n²) to O(n log n). Don't change signature.".

In the table, "Review my code": "Review auth.py for SQL injection, password handling, session issues. Ignore style.".

Terms on this slide — quick definitions for the room:

SQL stands for Structured Query Language — the language relational databases use for queries and updates.
-->

---







<!-- _class: fit-sm -->

## The "Boundaries" Technique

Always tell the agent what **NOT** to touch:

<img src="assets/module-03/the-boundaries-technique.svg" alt="The &quot;Boundaries&quot; Technique" />

<!--
This slide includes a diagram — The "Boundaries" Technique.

The slide title is: The "Boundaries" Technique.

The slide says: Always tell the agent what NOT to touch:.

The figure on this slide is titled: The &quot;Boundaries&quot; Technique.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-xs -->

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
This slide is a table — Avoiding Scope Creep.

The slide title is: Avoiding Scope Creep.

The slide says: The problem:.

The table header columns are: Technique, Example.

In the table, **Explicit boundaries**: "Change ONLY login.js lines 42–56".

In the table, **One thing at a time**: "First, just identify the issue. Don't fix yet.".

In the table, **Ask for plan first**: "Plan Mode: Show me what you'll change before doing it".

In the table, **Use checkpoints**: Create checkpoint before complex requests.

In the table, **Prefer diffs**: "Show me the diff, don't replace the whole file".

The code on the slide reads: User: "Fix the login bug." Agent: "Fixed login. Also refactored auth, added OAuth, reorganized codebase." User: "Wait, I just wanted the login bug fixed!".

Terms on this slide — quick definitions for the room:

Scope creep is when the agent changes more files or behavior than you asked for — constrain with explicit DO NOT lists.

A checkpoint is a saved snapshot of your code and conversation you can roll back to after an experiment.

Plan Mode makes the agent draft a step-by-step plan and ask clarifying questions before it writes code — toggle with Shift+Tab.

OAuth stands for Open Authorization — a standard for delegated login without sharing passwords.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 3.4 — Setup

**Before you start**

**Goal:** Practice six prompting techniques on `calculator.c` from earlier exercises.

**Do this first:**
1. **File → Open Folder** → `core-exercises/exercise-3/`
2. Open **Agent panel** — ``Ctrl+I``
3. Confirm **Agent Mode** (footer shows Agent, or type `/agent`)

Use **`@calculator.c`** in every prompt below.

<!--
We are starting Exercise 3.4 — Effective Prompting in Practice. We have about 22 min for this lab.

Write constrained prompts and reusable templates for real tasks.

The full lab guide is in slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step two's vague prompt may refactor more than divide() — that is the lesson.

Keep @calculator.c in every prompt so the Agent stays in the right file.

Practice six prompting techniques on calculator.c from earlier exercises.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.4 — Setup.

The slide says: Before you start.

The slide says: Do this first:.

The slide says: 1. File → Open Folder → core-exercises/exercise-3/.

The slide says: 2. Open Agent panel — `Ctrl+I`.

The slide says: 3. Confirm Agent Mode (footer shows Agent, or type /agent).

The slide says: Use @calculator.c in every prompt below.

Number 1 on the slide: File → Open Folder → core-exercises/exercise-3/.

Number 2 on the slide: Open Agent panel — `Ctrl+I`.

Number 3 on the slide: Confirm Agent Mode (footer shows Agent, or type /agent).

Terms on this slide — quick definitions for the room:

Agent Mode lets Cursor edit files, run terminal commands, and use tools — always with your review before changes land.
-->

---







<!-- _class: fit-xs -->

## Exercise 3.4 — Step 1: Constrained Prompt

**Step 1 — Constrained prompt**

**Goal:** Task + boundaries + output format + success criteria.

**Where:** **Agent panel** — ``Ctrl+I``

```
@calculator.c

Task: Improve divide() so it handles division by zero safely inside the function itself.

Constraints:
- Do NOT change any function signatures
- Do NOT add new #include lines
- Do NOT modify main() or other functions
- Change ONLY the divide() function body

Output format: Show the exact diff and explain the root cause in 2–3 sentences.

Success criteria: divide(10, 0) returns safely; divide(10, 2) still returns 5.
```

**Look for:** Diff limited to `divide()` — not a full refactor.

<!--
Now for Step 1: Constrained Prompt.

Task + boundaries + output format + success criteria.

You should see: Diff limited to divide() — not a full refactor.

Step 1 — Constrained prompt.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "@calculator.c Task: Improve divide() so it handles division by zero safely inside the function itself. Constraints: - Do NOT change any function signatures - Do NOT add new #include lines - Do NOT modify main() or other functions - Change ONLY the divide() function body Output format: Show the exact diff and explain the root cause in 2–3 sentences. Success criteria: divide(10, 0) returns safely; divide(10, 2) still returns 5."

Keep @calculator.c in the prompt so the Agent stays in the right file.

Step two's vague prompt may refactor more than divide() — that is the lesson.

Keep @calculator.c in every prompt so the Agent stays in the right file.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.4 — Step 1: Constrained Prompt.

Look for: Diff limited to divide() — not a full refactor.

Bullet 1 on the slide: Do NOT change any function signatures.

Bullet 2 on the slide: Do NOT add new #include lines.

Bullet 3 on the slide: Do NOT modify main() or other functions.

Bullet 4 on the slide: Change ONLY the divide() function body.

The code on the slide reads: @calculator.c Task: Improve divide() so it handles division by zero safely inside the function itself. Constraints: - Do NOT change any function signatures - Do NOT add new #include lines - Do NOT modify main() or other functions - Change ONLY the divide() function body Output format: Show the exact diff and explain the root cause in 2–3 sentences. Success criteria: divide(10, 0) returns safely; divide(10, 2) still returns 5..

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 3.4 — Step 2: Vague vs. Constrained

**Step 2 — Vague vs. constrained**

**Goal:** See why boundaries matter.

**Part A — vague** (new message or `/clear`):

```
@calculator.c Fix the divide function.
```

Note: Did the Agent change more than `divide()`?

**Part B — constrained:** Re-send the **Step 1** prompt.

**Look for:** Constrained prompt → smaller, reviewable diff.

<!--
Now for Step 2: Vague vs. Constrained.

Task + boundaries + output format + success criteria.

You should see: Diff limited to divide() — not a full refactor.

Step 2 — Vague vs. constrained.

Copy this into the Agent chat: "@calculator.c Fix the divide function."

Keep @calculator.c in the prompt so the Agent stays in the right file.

Step two's vague prompt may refactor more than divide() — that is the lesson.

Keep @calculator.c in every prompt so the Agent stays in the right file.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.4 — Step 2: Vague vs. Constrained.

Goal: See why boundaries matter.

The slide says: Part A — vague (new message or /clear):.

The slide says: Note: Did the Agent change more than divide()?.

The slide says: Part B — constrained: Re-send the Step 1 prompt.

Look for: Constrained prompt → smaller, reviewable diff.

The code on the slide reads: @calculator.c Fix the divide function..

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-xs -->

## Exercise 3.4 — Step 3: Plan Before Editing

**Step 3 — Plan before editing**

**Goal:** Approve a plan before any file changes.

**Where:** Ask Mode (`/ask`) or Agent with *"do not edit yet"*

```
@calculator.c

Before making any changes, answer:
1. What is the smallest change needed for divide()?
2. Which lines would you change?
3. What could go wrong?
4. What will you NOT change?

Do not edit files yet — I will review first.
```

**Look for:** Written plan, **no diff** until you approve.

<!--
Now for Step 3: Plan Before Editing.

Approve a plan before any file changes.

You should see: Written plan, no diff until you approve.

Step 3 — Plan before editing.

Where: Ask Mode (/ask) or Agent with "do not edit yet".

Copy this into the Agent chat: "@calculator.c Before making any changes, answer: 1. What is the smallest change needed for divide()? 2. Which lines would you change? 3. What could go wrong? 4. What will you NOT change? Do not edit files yet — I will review first."

Keep @calculator.c in the prompt so the Agent stays in the right file.

Step two's vague prompt may refactor more than divide() — that is the lesson.

Keep @calculator.c in every prompt so the Agent stays in the right file.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.4 — Step 3: Plan Before Editing.

Look for: Written plan, no diff until you approve.

The code on the slide reads: @calculator.c Before making any changes, answer: 1. What is the smallest change needed for divide()? 2. Which lines would you change? 3. What could go wrong? 4. What will you NOT change? Do not edit files yet — I will review first..

Terms on this slide — quick definitions for the room:

Ask Mode is Cursor's read-only mode — the model can answer questions but cannot edit files or run tools.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-xs -->

## Exercise 3.4 — Step 4: DO NOT List

**Step 4 — DO NOT list**

**Goal:** Forbid scope creep explicitly.

```
@calculator.c

Add a one-line comment above divide() explaining it performs integer division.

DO NOT:
- Change any function bodies
- Rename functions
- Add new functions
- Modify main()
```

**Look for:** Comment only — no logic changes.

<!--
Now for Step 4: DO NOT List.

Forbid scope creep explicitly.

You should see: Comment only — no logic changes.

Step 4 — DO NOT list.

Copy this into the Agent chat: "@calculator.c Add a one-line comment above divide() explaining it performs integer division. DO NOT: - Change any function bodies - Rename functions - Add new functions - Modify main()"

Keep @calculator.c in the prompt so the Agent stays in the right file.

Step two's vague prompt may refactor more than divide() — that is the lesson.

Keep @calculator.c in every prompt so the Agent stays in the right file.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.4 — Step 4: DO NOT List.

Look for: Comment only — no logic changes.

Bullet 1 on the slide: Change any function bodies.

Bullet 2 on the slide: Rename functions.

Bullet 3 on the slide: Add new functions.

Bullet 4 on the slide: Modify main().

The code on the slide reads: @calculator.c Add a one-line comment above divide() explaining it performs integer division. DO NOT: - Change any function bodies - Rename functions - Add new functions - Modify main().

Terms on this slide — quick definitions for the room:

Scope creep is when the agent changes more files or behavior than you asked for — constrain with explicit DO NOT lists.
-->

---







<!-- _class: fit-sm -->

## Exercise 3.4 — Step 5: One Change at a Time

**Step 5 — One change at a time**

**Goal:** Two messages — propose, then apply.

**Message 1:**
```
@calculator.c

Show me the validation you would add inside divide() for division by zero.
Do not edit the file yet.
```

**Message 2** (after you review Message 1):
```
Now add only that validation to divide(). Show the diff before I accept.
Do not change main() or other functions.
```

**Look for:** Message 1 = no edit · Message 2 = small diff.

<!--
Now for Step 5: One Change at a Time.

Two messages — propose, then apply.

You should see: Message 1 = no edit · Message 2 = small diff.

Step 5 — One change at a time.

Copy this into the Agent chat: "@calculator.c Show me the validation you would add inside divide() for division by zero. Do not edit the file yet."

Keep @calculator.c in the prompt so the Agent stays in the right file.

Copy this into the Agent chat: "Now add only that validation to divide(). Show the diff before I accept. Do not change main() or other functions."

Step two's vague prompt may refactor more than divide() — that is the lesson.

Keep @calculator.c in every prompt so the Agent stays in the right file.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.4 — Step 5: One Change at a Time.

The slide says: Message 1:.

The slide says: Message 2 (after you review Message 1):.

Look for: Message 1 = no edit · Message 2 = small diff.

The code on the slide reads: @calculator.c Show me the validation you would add inside divide() for division by zero. Do not edit the file yet..

The code on the slide reads: Now add only that validation to divide(). Show the diff before I accept. Do not change main() or other functions..
-->

---







<!-- _class: fit-xs -->

## Exercise 3.4 — Step 6: Prompt Templates

**Step 6 — Prompt templates**

**Goal:** Reusable prompts for real projects.

Create **`.cursor/prompt-templates.md`**:

```
## Bug Fix Template
@{{file}}
Task: [Describe bug]
Constraints: Do NOT change [signatures / other files]
Output: Show diff + root cause
Success: [How to verify]

## Plan-First Template
@{{file}}
Before editing: list files, risks, and what you will NOT touch.
Wait for my approval.

## Small Change Template
@{{file}}
Change ONLY: [function or lines]
DO NOT: [forbidden changes]
Show diff before applying.
```

**Success Criteria:**
- Constrained prompt sent · Vague vs. constrained compared
- Plan before edit · DO NOT list used · Two-message flow tried
- `.cursor/prompt-templates.md` created

<!--
Now for Step 6: Prompt Templates.

Create prompts you can copy on real projects.

Step 6 — Prompt templates.

Copy this into the Agent chat: "## Bug Fix Template @{{file}} Task: [Describe bug] Constraints: Do NOT change [signatures / other files] Output: Show diff + root cause Success: [How to verify] ## Plan-First Template @{{file}} Before editing: list files, risks, and what you will NOT touch. Wait for my approval. ## Small Change Template @{{file}} Change ONLY: [function or lines] DO NOT: [forbidden changes] Show diff before applying."

Step two's vague prompt may refactor more than divide() — that is the lesson.

Keep @calculator.c in every prompt so the Agent stays in the right file.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 3.4 — Step 6: Prompt Templates.

You will also see the heading: Bug Fix Template.

You will also see the heading: Plan-First Template.

You will also see the heading: Small Change Template.

Goal: Reusable prompts for real projects.

The slide says: Create .cursor/prompt-templates.md:.

Success criteria are listed on the slide as follows.

Bullet 1 on the slide: Constrained prompt sent · Vague vs. constrained compared.

Bullet 2 on the slide: Plan before edit · DO NOT list used · Two-message flow tried.

Bullet 3 on the slide: .cursor/prompt-templates.md created.

The code on the slide begins: ## Bug Fix Template @{{file}} Task: [Describe bug] Constraints: Do NOT change [signatures / other files] Output: Show diff + root cause Success: [How to verify]. The rest of the block continues on the slide.
-->

---







<!-- _header: 'Module 4 — Customizing Cursor for Your Team' -->

<!-- _class: lead -->

# Customizing Cursor for Your Team

## Module 4 · Day 1 (Hands-On + Walkthrough)

Cursor Training Program · ~60 min

<!--
Module 4 is about scaling Cursor for your team — rules, repository instructions, and reusable skills.

The slide title is: Customizing Cursor for Your Team.

You will also see the heading: Module 4 · Day 1 (Hands-On + Walkthrough).

The slide says: Cursor Training Program · ~60 min.
-->

---







<!-- _class: fit-md -->

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise + walkthrough |
| **Prerequisites** | Modules 1–3 completed, team repository access, Cursor installed |
| **Module Goal** | Customize Cursor for team workflows with rules, skills, MCP, and subagents |

### Lessons

| Lesson | Topic | Time |
|--------|-------|------|
| 4.1 | Creating a Rule | 20 min |
| 4.2 | Repository Instructions | 13 min |
| 4.3 | Creating and Invoking a Skill | 20 min |
| 4.4 | MCP, Hooks, and Slash Workflows | 10 min |
| 4.5 | Subagents | 6 min |

<!--
Here is the overview for Module 4.

The slide title is: Module Overview.

The table header columns are: Aspect, Details.

In the table, **Duration**: ~60 minutes.

In the table, **Format**: Hands-on exercise + walkthrough.

In the table, **Prerequisites**: Modules 1–3 completed, team repository access, Cursor installed.

In the table, **Module Goal**: Customize Cursor for team workflows with rules, skills, MCP, and subagents.

Terms on this slide — quick definitions for the room:

A subagent is a delegated specialist agent — often run in parallel or in isolation for a subtask.

MCP stands for Model Context Protocol — a standard for connecting AI assistants to external tools, databases, and APIs.
-->

---



<!-- _class: lead -->

# Lesson 4.1

## Creating a Rule

*Concept · 8 min · Exercise · 12 min*

**Lab guide:** [`Exercise 4.1](../slide-exercises/module-04/exercise-4.1-creating-a-rule.md)

<!--
Lesson 4.1: Creating a Rule. For this lesson, listen, participate, or follow along as indicated on the next slides.

Create Cursor rules that persist coding standards for your team.

Rules and AGENTS.md travel with the repo so the whole team gets the same standards without repeating them in every prompt.

The detailed lab guide is slide-exercises/module-04/exercise-4.1-creating-a-rule.md.

The slide title is: Lesson 4.1.

You will also see the heading: Creating a Rule.

The note on screen reads: Concept · 8 min · Exercise · 12 min.

The slide says: Lab guide: [`Exercise 4.1](../slide-exercises/module-04/exercise-4.1-creating-a-rule.md).
-->

---







<!-- _class: fit-md -->

## What Are Rules?

Rules are Markdown files (`.cursor/rules/*.mdc`) with persistent instructions the agent automatically applies.

| Rule Type | Scope | When Applied | Example |
|-----------|-------|--------------|---------|
| **Global** | All projects | Always | "Use American English spelling" |
| **Project** | Specific repo | When opening that project | "Run `make test` before suggesting changes" |
| **File pattern** | Matching files | When editing those files | "For `*.py` files, use type hints" |
| **User** | Your account | Always across all projects | "Explain like I'm a junior developer" |

<!--
This slide is a table — What Are Rules?.

The slide title is: What Are Rules?.

The slide says: Rules are Markdown files (.cursor/rules/*.mdc) with persistent instructions the agent automatically applies.

The table header columns are: Rule Type, Scope, When Applied, Example.

Table row: **Global**, All projects, Always, "Use American English spelling".

Table row: **Project**, Specific repo, When opening that project, "Run `make test` before suggesting changes".

Table row: **File pattern**, Matching files, When editing those files, "For `*.py` files, use type hints".

Table row: **User**, Your account, Always across all projects, "Explain like I'm a junior developer".

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Rule Structure

```markdown

<!--
The slide title is: Rule Structure.
-->

---







description: Brief description of what this rule does
globs: *.py, src/**/*.js
alwaysApply: true

<!--
Let's look at description: Brief description of what this rule does globs: .py, src//.js alway….

The slide title is: description: Brief description of what this rule does globs: .py, src//.js alway….

The slide says: description: Brief description of what this rule does.

The slide says: globs: .py, src//.js.

The slide says: alwaysApply: true.
-->

---







# Rule Title

## Instructions for the Agent
Write your instructions here in natural language.

## Examples
Good: ...  Bad: ...
```

<!--
The slide title is: Rule Title.

You will also see the heading: Instructions for the Agent.

You will also see the heading: Examples.

The slide says: Write your instructions here in natural language.

The slide says: Good: ...  Bad: .

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-sm -->

## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Agent panel** (``Ctrl+I``) is for prompts and tool use · **Chat** (``Ctrl+L``) is read-only Q&A.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

The slide title is: Windows Exercise Environment.

The slide says: All exercises in this module assume Windows 10/11 with Cursor installed.

The slide says: Agent panel (`Ctrl+I) is for prompts and tool use · Chat (Ctrl+L`) is read-only Q&A.

The slide says: Set default profile: Settings → terminal.integrated.defaultProfile.windows → PowerShell.

The table header columns are: Terminal, Use when, Open in Cursor.

In the table, **PowerShell** — Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`). Use case on slide: ``Ctrl+` `` → **PowerShell**.

In the table, **Git Bash** — Bash syntax, `export VAR=...`, shell scripts ending in `.sh`. Use case on slide: Terminal menu → **Git Bash**.

In the table, **Command Prompt** — Legacy `.bat` files only. Use case on slide: Terminal menu → **Command Prompt**.

In the table, **Ubuntu (WSL)** — Linux-only tools or native bash without Git Bash. Use case on slide: Terminal menu → **Ubuntu (WSL)**.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.

npm is the Node Package Manager — the default registry and tool for JavaScript packages.
-->

---







<!-- _class: fit-sm -->

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
We are starting Exercise 4.1 — Creating a Rule. We have about 20 min for this lab.

Create Cursor rules that persist coding standards for your team.

The full lab guide is in slide-exercises/module-04/exercise-4.1-creating-a-rule.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Copy this into the Agent chat: "mkdir -p .cursor/rules"

Copy this into the Agent chat: "globs: **/*.{js,ts,py} | alwaysApply: true Python: type hints, Black (88 chars), Google docstrings JS/TS: const over let, arrow functions, optional chaining General: no commented-out code, no console.log in prod"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 4.1 — Step 1: Setup.

Environment note on the slide: Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts).

The slide says: Create coding standards rule at .cursor/rules/coding-standards.mdc:.

The code on the slide reads: mkdir -p .cursor/rules.

The code on the slide reads: globs: **/*.{js,ts,py}  |  alwaysApply: true Python: type hints, Black (88 chars), Google docstrings JS/TS: const over let, arrow functions, optional chaining General: no commented-out code, no console.log in prod.

Terms on this slide — quick definitions for the room:

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







<!-- _class: fit-xs -->

## Exercise 4.1 — Build & Test Rule

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

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
Now for Build & Test Rule.

Copy this into the Agent chat: "Before changes: git status, git diff After changes: make test / pytest / npm test → make lint Do NOT suggest changes that break tests or need undocumented API keys"

Copy this into the Agent chat: "Never: hardcoded secrets, eval() on user input, SQL concatenation Always: input validation, rate limiting, HTTPS, safe error messages Flag: exec/eval with user input, password/secret in variable names"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 4.1 — Build & Test Rule.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The slide says: Create .cursor/rules/build-and-test.mdc:.

The slide says: Create .cursor/rules/security.mdc:.

The code on the slide reads: Before changes: git status, git diff After changes:  make test / pytest / npm test → make lint Do NOT suggest changes that break tests or need undocumented API keys.

The code on the slide reads: Never: hardcoded secrets, eval() on user input, SQL concatenation Always: input validation, rate limiting, HTTPS, safe error messages Flag: exec/eval with user input, password/secret in variable names.

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

SQL stands for Structured Query Language — the language relational databases use for queries and updates.

npm is the Node Package Manager — the default registry and tool for JavaScript packages.
-->

---







## Exercise 4.1 — Test & File-Specific Rules

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**


**Step 5:** Verify rules are applied:
**Where:** **Agent panel** — ``Ctrl+I``

```
Based on the project rules, what are the coding standards I should follow?
What are the security guardrails?
```

<!--
Now for Test & File-Specific Rules.

Step 5: Verify rules are applied:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "Based on the project rules, what are the coding standards I should follow? What are the security guardrails?"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 4.1 — Test & File-Specific Rules.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The code on the slide reads: Based on the project rules, what are the coding standards I should follow? What are the security guardrails?.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 4.1 — Test & File-Specific Rules (Part 2)

**Step 6:** Create `.cursor/rules/react-components.mdc` for `**/*.jsx, **/*.tsx`:
**Where:** **Agent panel** — ``Ctrl+I``
- Component structure, naming (PascalCase, handleSubmit)
- Performance: React.memo, useCallback, useMemo
- Accessibility: keyboard nav, alt text, semantic HTML

**Success Criteria:** Created rules directory · coding, build, security rules · verified application

<!--
Now for Test & File-Specific Rules (Part 2).

Step 6: Create .cursor/rules/react-components.mdc for */.jsx, */.tsx:.

Where: Agent panel — `Ctrl+I`.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 4.1 — Test & File-Specific Rules (Part 2).

Success criteria listed: Created rules directory · coding, build, security rules · verified application.

Bullet 1 on the slide: Component structure, naming (PascalCase, handleSubmit).

Bullet 2 on the slide: Performance: React.memo, useCallback, useMemo.

Bullet 3 on the slide: Accessibility: keyboard nav, alt text, semantic HTML.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---



<!-- _class: lead -->

# Lesson 4.2

## Repository Instructions

*Concept · 5 min · Exercise · 8 min*

**Lab guide:** [`Exercise 4.2](../slide-exercises/module-04/exercise-4.2-repository-instructions.md)

<!--
Lesson 4.2: Repository Instructions. For this lesson, listen, participate, or follow along as indicated on the next slides.

Add repository instructions the Agent reads automatically.

Rules and AGENTS.md travel with the repo so the whole team gets the same standards without repeating them in every prompt.

The detailed lab guide is slide-exercises/module-04/exercise-4.2-repository-instructions.md.

The slide title is: Lesson 4.2.

You will also see the heading: Repository Instructions.

The note on screen reads: Concept · 5 min · Exercise · 8 min.

The slide says: Lab guide: [`Exercise 4.2](../slide-exercises/module-04/exercise-4.2-repository-instructions.md).

Terms on this slide — quick definitions for the room:

Repository Instructions are a single project overview file the agent reads for stack, commands, and conventions.
-->

---







<!-- _class: fit-md -->

## Rules vs. Repository Instructions

| Aspect | Rules | Repository Instructions |
|--------|-------|------------------------|
| **Location** | `.cursor/rules/*.mdc` | `.cursor/repository-instructions.md` |
| **Complexity** | Multiple files, scoped | Single file, global |
| **Granularity** | Per-file patterns | Entire repository |
| **Use case** | Detailed standards | High-level project overview |

<!--
This slide is a table — Rules vs. Repository Instructions.

The slide title is: Rules vs. Repository Instructions.

The table header columns are: Aspect, Rules, Repository Instructions.

In the table, **Location** — `.cursor/rules/*.mdc`. Use case on slide: `.cursor/repository-instructions.md`.

In the table, **Complexity** — Multiple files, scoped. Use case on slide: Single file, global.

In the table, **Granularity** — Per-file patterns. Use case on slide: Entire repository.

In the table, **Use case** — Detailed standards. Use case on slide: High-level project overview.

Terms on this slide — quick definitions for the room:

Repository Instructions are a single project overview file the agent reads for stack, commands, and conventions.

Rules and AGENTS.md travel with the repo so the whole team gets the same standards without repeating them in every prompt.
-->

---







<!-- _class: fit-xs -->

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
The slide title is: Repository Instructions Structure.

You will also see the heading: Repository Instructions for [Project Name].

You will also see the heading: Project Purpose.

You will also see the heading: Key Technologies.

You will also see the heading: Architecture Overview.

You will also see the heading: Important Conventions.

You will also see the heading: Common Tasks (make dev, make test, make build).

You will also see the heading: External Dependencies.

You will also see the heading: Contact.

The code on the slide reads: # Repository Instructions for [Project Name] ## Project Purpose ## Key Technologies ## Architecture Overview ## Important Conventions ## Common Tasks (make dev, make test, make build) ## External Dependencies ## Contact.

Terms on this slide — quick definitions for the room:

Repository Instructions are a single project overview file the agent reads for stack, commands, and conventions.

Rules and AGENTS.md travel with the repo so the whole team gets the same standards without repeating them in every prompt.
-->

---







<!-- _class: fit-xs -->

## Exercise 4.2 — Create Instructions

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

Create `.cursor/repository-instructions.md`:

<img src="assets/module-04/exercise-4-2-create-instructions.svg" alt="Exercise 4.2 — Create Instructions" />

<!--
We are starting Exercise 4.2 — Repository Instructions. We have about 13 min for this lab.

Add repository instructions the Agent reads automatically.

The full lab guide is in slide-exercises/module-04/exercise-4.2-repository-instructions.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 4.2 — Create Instructions.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The slide says: Create .cursor/repository-instructions.md:.

The figure on this slide is titled: Exercise 4.2 — Create Instructions.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 4.2 — Verify & Maintain

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**


**Step 2:** Ask the Agent:
**Where:** **Agent panel** — ``Ctrl+I``

```
What are the key technologies used in this project?
How do I run the tests?
```

<!--
Now for Verify & Maintain.

Step 2: Ask the Agent:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "What are the key technologies used in this project? How do I run the tests?"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 4.2 — Verify & Maintain.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The code on the slide reads: What are the key technologies used in this project? How do I run the tests?.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 4.2 — Verify & Maintain (Part 2)

**Step 3:** Update instructions when:
**Where:** **Agent panel** — ``Ctrl+I``
- New team members join → add contact info
- Architecture changes → update structure
- New dependencies or common issues discovered

**Success Criteria:** Created instructions · included purpose, stack, commands · verified agent access

<!--
Now for Verify & Maintain (Part 2).

Step 3: Update instructions when:.

Where: Agent panel — `Ctrl+I`.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 4.2 — Verify & Maintain (Part 2).

Success criteria listed: Created instructions · included purpose, stack, commands · verified agent access.

Bullet 1 on the slide: New team members join → add contact info.

Bullet 2 on the slide: Architecture changes → update structure.

Bullet 3 on the slide: New dependencies or common issues discovered.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---



<!-- _class: lead -->

# Lesson 4.3

## Creating and Invoking a Skill

*Concept · 8 min · Exercise · 12 min*

**Lab guide:** [`Exercise 4.3](../slide-exercises/module-04/exercise-4.3-creating-and-invoking-a-skill.md)

<!--
Lesson 4.3: Creating and Invoking a Skill. For this lesson, listen, participate, or follow along as indicated on the next slides.

Build and invoke reusable Agent skills for repeated workflows.

Rules and AGENTS.md travel with the repo so the whole team gets the same standards without repeating them in every prompt.

The detailed lab guide is slide-exercises/module-04/exercise-4.3-creating-and-invoking-a-skill.md.

The slide title is: Lesson 4.3.

You will also see the heading: Creating and Invoking a Skill.

The note on screen reads: Concept · 8 min · Exercise · 12 min.

The slide says: Lab guide: [`Exercise 4.3](../slide-exercises/module-04/exercise-4.3-creating-and-invoking-a-skill.md).
-->

---







<!-- _class: fit-xs -->

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
This slide includes a diagram — What Is a Skill?.

The slide title is: What Is a Skill?.

The slide says: A reusable, specialized workflow the agent loads and follows — a "prompt template with memory.".

In the table, Use Case: Example Skill.

In the table, Frequent task: "PR Review".

In the table, Complex workflow: "Onboarding".

In the table, Domain-specific: "Security Audit".

In the table, Documentation: "Generate API Docs".

The figure on this slide is titled: What Is a Skill?.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

PR stands for Pull Request — a proposed code change others review before it merges.

Rules and AGENTS.md travel with the repo so the whole team gets the same standards without repeating them in every prompt.
-->

---







<!-- _class: fit-sm -->

## Exercise 4.3 — PR Review Skill

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

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
We are starting Exercise 4.3 — Creating and Invoking a Skill. We have about 20 min for this lab.

Build and invoke reusable Agent skills for repeated workflows.

The full lab guide is in slide-exercises/module-04/exercise-4.3-creating-and-invoking-a-skill.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Copy this into the Agent chat: "name: pr-review description: Review a PR for code quality, security, and team standards Step 1: Fetch diff (git fetch + git diff main...FETCH_HEAD) Step 2: Review — code quality, security, testing, docs, style Step 3: Output formatted review with Critical / Warning / Suggestion Verdict: APPROVE / REQUEST CHANGES / COMMENT"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 4.3 — PR Review Skill.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The slide says: Create .cursor/skills/pr-review/SKILL.md:.

The code on the slide reads: name: pr-review description: Review a PR for code quality, security, and team standards Step 1: Fetch diff (git fetch + git diff main...FETCH_HEAD) Step 2: Review — code quality, security, testing, docs, style Step 3: Output formatted review with Critical / Warning / Suggestion Verdict: APPROVE / REQUEST CHANGES / COMMENT.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

PR stands for Pull Request — a proposed code change others review before it merges.

Rules and AGENTS.md travel with the repo so the whole team gets the same standards without repeating them in every prompt.
-->

---







<!-- _class: fit-sm -->

## Exercise 4.3 — Security Audit Skill

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

Create `.cursor/skills/security-audit/SKILL.md`:

```
Scan for:
  Critical: hardcoded secrets, SQL injection, command injection, eval()
  Medium:   no input validation, weak crypto, missing CSRF
  Low:      debug endpoints, verbose errors, outdated deps

Output: report with line numbers, fix suggestions, overall risk rating
```

<!--
Now for Security Audit Skill.

Copy this into the Agent chat: "Scan for: Critical: hardcoded secrets, SQL injection, command injection, eval() Medium: no input validation, weak crypto, missing CSRF Low: debug endpoints, verbose errors, outdated deps Output: report with line numbers, fix suggestions, overall risk rating"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 4.3 — Security Audit Skill.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The slide says: Create .cursor/skills/security-audit/SKILL.md:.

The code on the slide reads: Scan for:   Critical: hardcoded secrets, SQL injection, command injection, eval()   Medium:   no input validation, weak crypto, missing CSRF   Low:      debug endpoints, verbose errors, outdated deps Output: report with line numbers, fix suggestions, overall risk rating.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

CSRF stands for Cross-Site Request Forgery — an attack where a malicious site triggers actions in another site you are logged into.

SQL stands for Structured Query Language — the language relational databases use for queries and updates.

Rules and AGENTS.md travel with the repo so the whole team gets the same standards without repeating them in every prompt.
-->

---







## Exercise 4.3 — Invoke Skills

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**


**Step 4:** Invoke via slash command:
**Where:** **Agent panel** — ``Ctrl+I``

```
/pr-review PR #42
/pr-review feature/payment-integration
```

<!--
Now for Invoke Skills.

Step 4: Invoke via slash command:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "/pr-review PR #42 /pr-review feature/payment-integration"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 4.3 — Invoke Skills.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The code on the slide reads: /pr-review PR #42 /pr-review feature/payment-integration.

Terms on this slide — quick definitions for the room:

A slash command is a typed shortcut — often backed by a skill — that triggers a repeatable workflow.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

PR stands for Pull Request — a proposed code change others review before it merges.

Rules and AGENTS.md travel with the repo so the whole team gets the same standards without repeating them in every prompt.
-->

---







## Exercise 4.3 — Invoke Skills (Part 2)

**Step 5:** List available skills:
**Where:** **Agent panel** — ``Ctrl+I``

```
What skills are available in this project?
```

<!--
Now for Invoke Skills (Part 2).

Step 5: List available skills:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "What skills are available in this project?"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 4.3 — Invoke Skills (Part 2).

The code on the slide reads: What skills are available in this project?.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

Rules and AGENTS.md travel with the repo so the whole team gets the same standards without repeating them in every prompt.
-->

---







## Exercise 4.3 — Invoke Skills (Part 3)

**Step 6:** Create **Onboarding** skill — generates setup checklist from repo instructions
**Where:** **Agent panel** — ``Ctrl+I``

**Success Criteria:** Created skills · built PR Review + Security Audit · invoked via slash command

<!--
Now for Invoke Skills (Part 3).

Step 6: Create Onboarding skill — generates setup checklist from repo instructions.

Where: Agent panel — `Ctrl+I`.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 4.3 — Invoke Skills (Part 3).

Success criteria listed: Created skills · built PR Review + Security Audit · invoked via slash command.

Terms on this slide — quick definitions for the room:

A slash command is a typed shortcut — often backed by a skill — that triggers a repeatable workflow.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

PR stands for Pull Request — a proposed code change others review before it merges.

Rules and AGENTS.md travel with the repo so the whole team gets the same standards without repeating them in every prompt.
-->

---



<!-- _class: lead -->

# Lesson 4.4

## MCP, Hooks, and Slash Workflows

*Concept · 10 min · Walkthrough*

<!--
Lesson 4.4: MCP, Hooks, and Slash Workflows. For this lesson, listen, participate, or follow along as indicated on the next slides.

MCP is standard plumbing for connecting Cursor to databases, browsers, and internal services — one protocol instead of a custom integration per tool.

The slide title is: Lesson 4.4.

You will also see the heading: MCP, Hooks, and Slash Workflows.

The note on screen reads: Concept · 10 min · Walkthrough.

Terms on this slide — quick definitions for the room:

MCP stands for Model Context Protocol — a standard for connecting AI assistants to external tools, databases, and APIs.
-->

---







<!-- _class: fit-xs -->

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
This slide includes a diagram — What Is MCP?.

The slide title is: What Is MCP?.

The slide says: MCP standardizes how AI agents discover and use external tools — "USB port for AI.".

The table header columns are: MCP Server, Capabilities.

In the table, **GitHub**: Create PRs, comment on issues, fetch reviews.

In the table, **Slack**: Send messages, read channels.

In the table, **Jira**: Create tickets, update status.

In the table, **Database**: Query databases, run migrations.

The figure on this slide is titled: What Is MCP?.

Terms on this slide — quick definitions for the room:

MCP stands for Model Context Protocol — a standard for connecting AI assistants to external tools, databases, and APIs.

MCP is standard plumbing for connecting Cursor to databases, browsers, and internal services — one protocol instead of a custom integration per tool.
-->

---







<!-- _class: fit-xs -->

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
This slide is a table — Hooks & Slash Workflows.

The slide title is: Hooks & Slash Workflows.

The slide says: Hooks — scripts at specific agent workflow points:.

The slide says: Slash workflows — team commands combining MCP, hooks, and prompts:.

The table header columns are: Hook, When It Runs, Use Case.

In the table, `pre-tool-use` — Before tool call. Use case on slide: Validate permissions, log.

In the table, `post-tool-use` — After tool returns. Use case on slide: Transform results, audit.

In the table, `pre-prompt` — Before sending to model. Use case on slide: Inject context, redact secrets.

In the table, `post-response` — After agent responds. Use case on slide: Format output, log.

The table header columns are: Command, What It Does.

In the table, `/onboard @newdev`: Onboarding skill + GitHub issue + Slack message.

In the table, `/deploy staging`: Tests → build → deploy → notify team.

In the table, `/bug-report`: Analyze error → create issue → assign on-call.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

MCP stands for Model Context Protocol — a standard for connecting AI assistants to external tools, databases, and APIs.
-->

---







<!-- _class: fit-xs -->

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
In this walkthrough we will look at MCP Configuration. Create ~/.cursor/mcp.json: Watch where this lives in Cursor or in the repository — that location matters as much as the content.

The slide title is: Walkthrough: MCP Configuration.

The slide says: Create ~/.cursor/mcp.json:.

The code on the slide begins: {   "mcpServers": {     "github": {       "command": "cursor-mcp-github",       "args": ["--token", "${GITHUB_TOKEN}"]     },. The rest of the block continues on the slide.

The code on the slide reads: Create a PR from feature/payment and request review from @alice Send a message to #deploys: "Deployment starting".

Terms on this slide — quick definitions for the room:

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.

MCP stands for Model Context Protocol — a standard for connecting AI assistants to external tools, databases, and APIs.

PR stands for Pull Request — a proposed code change others review before it merges.

MCP is standard plumbing for connecting Cursor to databases, browsers, and internal services — one protocol instead of a custom integration per tool.
-->

---







<!-- _class: fit-xs -->

## Walkthrough: Slash Command Example

Create `.cursor/commands/deploy.md`:

<img src="assets/module-04/walkthrough-slash-command-example.svg" alt="Walkthrough: Slash Command Example" />

Usage: `/deploy staging`

**Success Criteria:** Understood MCP, hooks, slash commands · saw configuration examples

<!--
In this walkthrough we will look at Slash Command Example. Create .cursor/commands/deploy.md: Usage: /deploy staging Success Criteria: Understood MCP, hooks, slash commands · saw configuration examples Watch where this lives in Cursor or in the repository — that location matters as much as the content.

The slide title is: Walkthrough: Slash Command Example.

The slide says: Create .cursor/commands/deploy.md:.

The slide says: Usage: /deploy staging.

Success criteria listed: Understood MCP, hooks, slash commands · saw configuration examples.

The figure on this slide is titled: Walkthrough: Slash Command Example.

Terms on this slide — quick definitions for the room:

A slash command is a typed shortcut — often backed by a skill — that triggers a repeatable workflow.

MCP stands for Model Context Protocol — a standard for connecting AI assistants to external tools, databases, and APIs.
-->

---



<!-- _class: lead -->

# Lesson 4.5

## Subagents

*Concept · 6 min · Walkthrough*

<!--
Lesson 4.5: Subagents. For this lesson, listen, participate, or follow along as indicated on the next slides.

The slide title is: Lesson 4.5.

You will also see the heading: Subagents.

The note on screen reads: Concept · 6 min · Walkthrough.

Terms on this slide — quick definitions for the room:

A subagent is a delegated specialist agent — often run in parallel or in isolation for a subtask.
-->

---







<!-- _class: fit-sm -->

## What Are Subagents?

Independent agent instances for specialized tasks — own context, tools, and instructions — then report back to the main agent.

<img src="assets/module-04/what-are-subagents.svg" alt="What Are Subagents?" />

<!--
This slide includes a diagram — What Are Subagents?.

The slide title is: What Are Subagents?.

The slide says: Independent agent instances for specialized tasks — own context, tools, and instructions — then report back to the main agent.

The figure on this slide is titled: What Are Subagents?.

Terms on this slide — quick definitions for the room:

A subagent is a delegated specialist agent — often run in parallel or in isolation for a subtask.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-md -->

## When to Use Subagents

| Scenario | Why Subagent | Example |
|----------|--------------|---------|
| **Parallel work** | Multiple tasks simultaneously | Scan security AND generate docs |
| **Isolation** | Separate context | Analyze large file independently |
| **Specialization** | Different instructions | Security expert vs. UI designer |
| **Sandboxing** | Limit tool access | Read-only subagent for unknown code |

<!--
This slide is a table — When to Use Subagents.

The slide title is: When to Use Subagents.

The table header columns are: Scenario, Why Subagent, Example.

In the table, **Parallel work** — Multiple tasks simultaneously. Use case on slide: Scan security AND generate docs.

In the table, **Isolation** — Separate context. Use case on slide: Analyze large file independently.

In the table, **Specialization** — Different instructions. Use case on slide: Security expert vs. UI designer.

In the table, **Sandboxing** — Limit tool access. Use case on slide: Read-only subagent for unknown code.

Terms on this slide — quick definitions for the room:

A subagent is a delegated specialist agent — often run in parallel or in isolation for a subtask.
-->

---







## Subagent vs. Tool vs. Skill

| Concept | Best for |
|---------|----------|
| **Tool** | Single action (read file, run command) |
| **Skill** | Multi-step workflow, same context |
| **Subagent** | Parallel, isolated, specialized work |

<!--
This slide is a table — Subagent vs. Tool vs. Skill.

The slide title is: Subagent vs. Tool vs. Skill.

The table header columns are: Concept, Best for.

In the table, **Tool**: Single action (read file, run command).

In the table, **Skill**: Multi-step workflow, same context.

In the table, **Subagent**: Parallel, isolated, specialized work.

Terms on this slide — quick definitions for the room:

A subagent is a delegated specialist agent — often run in parallel or in isolation for a subtask.

Rules and AGENTS.md travel with the repo so the whole team gets the same standards without repeating them in every prompt.
-->

---







<!-- _class: fit-xs -->

## Walkthrough: Subagents in Action

**Task:** "Review codebase for security issues and generate API documentation"

**Without subagents:** Mixed context, sequential, slower

**With subagents (parallel):**
<img src="assets/module-04/walkthrough-subagents-parallel.svg" alt="Walkthrough: Subagents in Action" />

**Invoke:**
```
Spawn a security subagent to audit src/auth/ independently.
Meanwhile, I'll work on the frontend.
```

**Success Criteria:** Understood concept · parallel execution · recognized templates

<!--
In this walkthrough we will look at Subagents in Action. Task: "Review codebase for security issues and generate API documentation" Without subagents: Mixed context, sequential, slower With subagents (parallel): Invoke: Success Criteria: Understood concept · parallel execution · recognized templates Watch where this lives in Cursor or in the repository — that location matters as much as the content.

The slide title is: Walkthrough: Subagents in Action.

The slide says: Task: "Review codebase for security issues and generate API documentation".

The slide says: Without subagents: Mixed context, sequential, slower.

The slide says: With subagents (parallel):.

The slide says: Invoke:.

Success criteria listed: Understood concept · parallel execution · recognized templates.

The figure on this slide is titled: Walkthrough: Subagents in Action.

The code on the slide reads: Spawn a security subagent to audit src/auth/ independently. Meanwhile, I'll work on the frontend..

Terms on this slide — quick definitions for the room:

A subagent is a delegated specialist agent — often run in parallel or in isolation for a subtask.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _header: 'Module 5 — Cursor CLI and Local Automation' -->

<!-- _class: lead -->

# Cursor CLI and Local Automation

## Module 5 · Day 1 (Hands-On)

Cursor Training Program · ~60 min

<!--
Module 5 moves the same agent to the terminal and to scripts you can automate.

The slide title is: Cursor CLI and Local Automation.

You will also see the heading: Module 5 · Day 1 (Hands-On).

The slide says: Cursor Training Program · ~60 min.

Terms on this slide — quick definitions for the room:

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.
-->

---







<!-- _class: fit-md -->

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise |
| **Prerequisites** | Cursor CLI installed, terminal access, Modules 1–4 completed |
| **Module Goal** | Master the Cursor CLI for terminal-based AI workflows and automation |

### Lessons

| Lesson | Topic | Time |
|--------|-------|------|
| 5.1 | Interactive CLI | 20 min |
| 5.2 | One-Shot CLI | 20 min |
| 5.3 | Cloud Handoff | 18 min |
| 5.4 | Listing and Resuming Sessions | 20 min |

<!--
Here is the overview for Module 5.

The slide title is: Module Overview.

The table header columns are: Aspect, Details.

In the table, **Duration**: ~60 minutes.

In the table, **Format**: Hands-on exercise.

In the table, **Prerequisites**: Cursor CLI installed, terminal access, Modules 1–4 completed.

In the table, **Module Goal**: Master the Cursor CLI for terminal-based AI workflows and automation.

Terms on this slide — quick definitions for the room:

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.
-->

---



<!-- _class: lead -->

# Lesson 5.1

## Interactive CLI

*Concept · 8 min · Exercise · 12 min*

**Lab guide:** [`Exercise 5.1](../slide-exercises/module-05/exercise-5.1-interactive-cli.md)

<!--
Lesson 5.1: Interactive CLI. For this lesson, listen, participate, or follow along as indicated on the next slides.

Start an interactive Cursor CLI session from the terminal.

The detailed lab guide is slide-exercises/module-05/exercise-5.1-interactive-cli.md.

The slide title is: Lesson 5.1.

You will also see the heading: Interactive CLI.

The note on screen reads: Concept · 8 min · Exercise · 12 min.

The slide says: Lab guide: [`Exercise 5.1](../slide-exercises/module-05/exercise-5.1-interactive-cli.md).

Terms on this slide — quick definitions for the room:

Interactive CLI is a long-lived terminal session where you chat with agent, switch models, and resume later.
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
This slide lists key points under What Is the Cursor CLI?.

The slide title is: What Is the Cursor CLI?.

The slide says: The Cursor CLI brings AI-powered coding directly to your command line.

The slide says: Primary command: agent (main entry point).

Bullet 1 on the slide: Start AI sessions from your terminal.

Bullet 2 on the slide: Get code assistance without leaving your workflow.

Bullet 3 on the slide: Automate coding tasks with scripts.

Bullet 4 on the slide: Integrate AI into existing CLI tools.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.
-->

---







<!-- _class: fit-xs -->

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
This slide is a table — Interactive Mode Commands.

The slide title is: Interactive Mode Commands.

The table header columns are: Command, Purpose.

In the table, `/model`: Switch between AI models interactively.

In the table, `/compress`: Summarize conversation, free up context window.

In the table, `/rules`: Create and edit rules directly from CLI.

In the table, `/commands`: Create and modify custom commands.

In the table, `/mcp enable/disable`: Manage MCP servers.

In the table, `/usage`: View Cursor usage stats.

In the table, `/about`: View environment and CLI configuration.

In the table, `/resume`: View and resume previous sessions.

Terms on this slide — quick definitions for the room:

Context window is the maximum amount of text the model can consider at once — when you exceed it, older content drops off.

MCP stands for Model Context Protocol — a standard for connecting AI assistants to external tools, databases, and APIs.

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.
-->

---







<!-- _class: fit-sm -->

## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Agent panel** (``Ctrl+I``) is for prompts and tool use · **Chat** (``Ctrl+L``) is read-only Q&A.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

The slide title is: Windows Exercise Environment.

The slide says: All exercises in this module assume Windows 10/11 with Cursor installed.

The slide says: Agent panel (`Ctrl+I) is for prompts and tool use · Chat (Ctrl+L`) is read-only Q&A.

The slide says: Set default profile: Settings → terminal.integrated.defaultProfile.windows → PowerShell.

The table header columns are: Terminal, Use when, Open in Cursor.

In the table, **PowerShell** — Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`). Use case on slide: ``Ctrl+` `` → **PowerShell**.

In the table, **Git Bash** — Bash syntax, `export VAR=...`, shell scripts ending in `.sh`. Use case on slide: Terminal menu → **Git Bash**.

In the table, **Command Prompt** — Legacy `.bat` files only. Use case on slide: Terminal menu → **Command Prompt**.

In the table, **Ubuntu (WSL)** — Linux-only tools or native bash without Git Bash. Use case on slide: Terminal menu → **Ubuntu (WSL)**.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.

npm is the Node Package Manager — the default registry and tool for JavaScript packages.
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
We are starting Exercise 5.1 — Interactive CLI. We have about 20 min for this lab.

Start an interactive Cursor CLI session from the terminal.

The full lab guide is in slide-exercises/module-05/exercise-5.1-interactive-cli.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: Start an interactive session.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "agent agent "Help me understand the current codebase structure""

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.1 — Steps 1–2.

Environment note on the slide: Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts).

The code on the slide reads: agent agent "Help me understand the current codebase structure".

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







## Exercise 5.1 — Steps 1–2 (Part 2)

**Step 2:** Navigate the session (inside the running `agent` session — same terminal window) — unless step notes Git Bash or WSL
- Type prompts naturally
- `Shift+Enter` — new line without submitting
- `Enter` — submit prompt
- `Ctrl+D` twice — exit

<!--
Now for Steps 1–2 (Part 2).

Step 2: Navigate the session (inside the running agent session — same terminal window) — unless step notes Git Bash or WSL.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.1 — Steps 1–2 (Part 2).

Bullet 1 on the slide: Type prompts naturally.

Bullet 2 on the slide: Shift+Enter — new line without submitting.

Bullet 3 on the slide: Enter — submit prompt.

Bullet 4 on the slide: Ctrl+D twice — exit.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







<!-- _class: fit-md -->

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
Now for Steps 3–5.

Step 3: Switch models:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "/model # Or list models outside session: agent --list-models"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.1 — Steps 3–5.

You will also see the heading: Or list models outside session:.

Environment note on the slide: Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts).

The code on the slide reads: /model # Or list models outside session: agent --list-models.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







## Exercise 5.1 — Steps 3–5 (Part 2)

**Step 4:** Ask Mode (read-only):
**Where:** **Agent panel** — ``Ctrl+I``

```bash
agent --mode=ask "What does this project's main function do?"
# Or inside session: /ask
```

<!--
Now for Steps 3–5 (Part 2).

Step 4: Ask Mode (read-only):.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "agent --mode=ask "What does this project's main function do?" # Or inside session: /ask"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.1 — Steps 3–5 (Part 2).

You will also see the heading: Or inside session: /ask.

The code on the slide reads: agent --mode=ask "What does this project's main function do?" # Or inside session: /ask.

Terms on this slide — quick definitions for the room:

Ask Mode is Cursor's read-only mode — the model can answer questions but cannot edit files or run tools.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 5.1 — Steps 3–5 (Part 3)

**Step 5:** Plan Mode:
**Where:** **Agent panel** — ``Ctrl+I``

```bash
agent --mode=plan "Add user authentication to this API"
```

<!--
Now for Steps 3–5 (Part 3).

Step 5: Plan Mode:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "agent --mode=plan "Add user authentication to this API""

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.1 — Steps 3–5 (Part 3).

Step 5: Plan Mode:.

The code on the slide reads: agent --mode=plan "Add user authentication to this API".

Terms on this slide — quick definitions for the room:

Plan Mode makes the agent draft a step-by-step plan and ask clarifying questions before it writes code — toggle with Shift+Tab.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
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
Now for Steps 6–7.

Step 6: Configure status line:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "npx -y cursor-statusline # Shows: [model: claude-4.5-sonnet] [~/project] [main] [ctx: 45k/200k]"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.1 — Steps 6–7.

You will also see the heading: Shows: [model: claude-4.5-sonnet] [~/project] [main] [ctx: 45k/200k].

Environment note on the slide: Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts).

The code on the slide reads: npx -y cursor-statusline # Shows: [model: claude-4.5-sonnet] [~/project] [main] [ctx: 45k/200k].

Terms on this slide — quick definitions for the room:

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







## Exercise 5.1 — Steps 6–7 (Part 2)

**Step 7:** Terminal key bindings:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent /setup-terminal
```

<!--
Now for Steps 6–7 (Part 2).

Step 7: Terminal key bindings:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "agent /setup-terminal"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.1 — Steps 6–7 (Part 2).

The code on the slide reads: agent /setup-terminal.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---



<!-- _class: lead -->

# Lesson 5.2

## One-Shot CLI

*Concept · 8 min · Exercise · 12 min*

**Lab guide:** [`Exercise 5.2](../slide-exercises/module-05/exercise-5.2-one-shot-cli.md)

<!--
Lesson 5.2: One-Shot CLI. For this lesson, listen, participate, or follow along as indicated on the next slides.

Run single-shot Agent commands from scripts and CI.

The detailed lab guide is slide-exercises/module-05/exercise-5.2-one-shot-cli.md.

The slide title is: Lesson 5.2.

You will also see the heading: One-Shot CLI.

The note on screen reads: Concept · 8 min · Exercise · 12 min.

The slide says: Lab guide: [`Exercise 5.2](../slide-exercises/module-05/exercise-5.2-one-shot-cli.md).

Terms on this slide — quick definitions for the room:

One-shot CLI means a single non-interactive agent command — ideal for scripts and CI pipelines.
-->

---







<!-- _class: fit-md -->

## One-Shot Command Structure

```bash
agent "your prompt here"                    # Basic one-shot
agent --mode=ask "question about code"      # Read-only
agent --model claude-4.5-sonnet "task"      # Specific model
agent --non-interactive "run this task"     # No prompts, just output
```

> *"Perfect for automation, CI/CD pipelines, and batch operations."*

<!--
This slide highlights a key quote — One-Shot Command Structure.

The slide title is: One-Shot Command Structure.

The slide quotes: ""Perfect for automation, CI/CD pipelines, and batch operations.""

The code on the slide reads: agent "your prompt here"                    # Basic one-shot agent --mode=ask "question about code"      # Read-only agent --model claude-4.5-sonnet "task"      # Specific model agent --non-interactive "run this task"     # No prompts, just output.

Terms on this slide — quick definitions for the room:

CI/CD stands for Continuous Integration and Continuous Deployment — automated build, test, and release pipelines.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-md -->

## Use Cases for One-Shot CLI

| Use Case | Example |
|----------|---------|
| **Code generation** | `agent "Create a React component for a login form"` |
| **Documentation** | `agent "Generate JSDoc comments for src/api.js"` |
| **CI/CD tasks** | `agent "Review this PR diff for security issues"` |
| **Batch processing** | Loop through files with `agent` commands |
| **Pre-commit hooks** | `agent --mode=ask "Check for console.log statements"` |

<!--
This slide is a table — Use Cases for One-Shot CLI.

The slide title is: Use Cases for One-Shot CLI.

The table header columns are: Use Case, Example.

In the table, **Code generation**: `agent "Create a React component for a login form"`.

In the table, **Documentation**: `agent "Generate JSDoc comments for src/api.js"`.

In the table, **CI/CD tasks**: `agent "Review this PR diff for security issues"`.

In the table, **Batch processing**: Loop through files with `agent` commands.

In the table, **Pre-commit hooks**: `agent --mode=ask "Check for console.log statements"`.

Terms on this slide — quick definitions for the room:

One-shot CLI means a single non-interactive agent command — ideal for scripts and CI pipelines.

CI/CD stands for Continuous Integration and Continuous Deployment — automated build, test, and release pipelines.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

PR stands for Pull Request — a proposed code change others review before it merges.
-->

---







<!-- _class: fit-md -->

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
We are starting Exercise 5.2 — One-Shot CLI. We have about 20 min for this lab.

Run single-shot Agent commands from scripts and CI.

The full lab guide is in slide-exercises/module-05/exercise-5.2-one-shot-cli.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: Basic one-shot commands:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "agent "What is the difference between let and const in JavaScript?" agent "Write a bash function that checks if a port is in use" agent --mode=ask "Explain the git rebase command with examples""

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.2 — Steps 1–2.

Environment note on the slide: Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts).

The code on the slide reads: agent "What is the difference between let and const in JavaScript?" agent "Write a bash function that checks if a port is in use" agent --mode=ask "Explain the git rebase command with examples".

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
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
Now for Steps 1–2 (Part 2).

Step 2: Specify models:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "agent --model gpt-5-mini "What does this command do: ls -la | grep .txt" agent --model claude-4.5-opus "Design a database schema for a task management system""

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.2 — Steps 1–2 (Part 2).

The code on the slide reads: agent --model gpt-5-mini "What does this command do: ls -la | grep .txt" agent --model claude-4.5-opus "Design a database schema for a task management system".

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







<!-- _class: fit-sm -->

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
Now for Scriptable Code Reviewer.

Copy this into the Agent chat: "#!/bin/bash STAGED_FILES=$(git diff --cached --name-only | tr '\n' ', ') agent --mode=ask "Review these staged files for common issues: Files: $STAGED_FILES Check for: debugging statements, unused imports, security issues, missing error handling. Be concise.""

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.2 — Scriptable Code Reviewer.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: Create bin/ai-review.sh:.

The slide says: PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

The code on the slide reads: #!/bin/bash STAGED_FILES=$(git diff --cached --name-only | tr '\n' ', ') agent --mode=ask "Review these staged files for common issues: Files: $STAGED_FILES Check for: debugging statements, unused imports, security issues, missing error handling. Be concise.".

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-md -->

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
Now for Batch & Git Hooks.

Step 4: Batch process files:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "for file in src/**/*.py; do agent --mode=ask --non-interactive \ "Summarize this Python file in one sentence: $(head -50 $file)" done"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.2 — Batch & Git Hooks.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The code on the slide reads: for file in src/**/*.py; do     agent --mode=ask --non-interactive \       "Summarize this Python file in one sentence: $(head -50 $file)" done.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







## Exercise 5.2 — Batch & Git Hooks (Part 2)

**Step 5:** Pre-commit hook — review staged diff for secrets, debug statements, merge markers
**Where:** **Agent panel** — ``Ctrl+I``

**Step 6:** CI/CD — analyze test output and suggest fixes for failures
**Terminal:** **PowerShell** — clone/open repo, then continue in Agent panel

**Success Criteria:** Ran one-shots · specified models · created reviewer script · understood CI/CD use

<!--
Now for Batch & Git Hooks (Part 2).

Step 5: Pre-commit hook — review staged diff for secrets, debug statements, merge markers.

Where: Agent panel — `Ctrl+I`.

Step 6: CI/CD — analyze test output and suggest fixes for failures.

Terminal: PowerShell — clone/open repo, then continue in Agent panel.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.2 — Batch & Git Hooks (Part 2).

Success criteria listed: Ran one-shots · specified models · created reviewer script · understood CI/CD use.

Terms on this slide — quick definitions for the room:

CI/CD stands for Continuous Integration and Continuous Deployment — automated build, test, and release pipelines.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---



<!-- _class: lead -->

# Lesson 5.3

## Cloud Handoff

*Concept · 8 min · Exercise · 10 min*

**Lab guide:** [`Exercise 5.3](../slide-exercises/module-05/exercise-5.3-cloud-handoff.md)

<!--
Lesson 5.3: Cloud Handoff. For this lesson, listen, participate, or follow along as indicated on the next slides.

Hand off a local CLI task to a Cloud Agent with &.

Cloud Agents keep working when your laptop is closed — long tasks, parallel runs, handoffs from local sessions.

When the PR comes back, the same review discipline applies.

The detailed lab guide is slide-exercises/module-05/exercise-5.3-cloud-handoff.md.

The slide title is: Lesson 5.3.

You will also see the heading: Cloud Handoff.

The note on screen reads: Concept · 8 min · Exercise · 10 min.

The slide says: Lab guide: [`Exercise 5.3](../slide-exercises/module-05/exercise-5.3-cloud-handoff.md).

Terms on this slide — quick definitions for the room:

Cloud handoff is when you prefix a message with ampersand in the CLI to continue the work as a Cloud Agent.
-->

---







## What Is Cloud Handoff?

Send a local conversation to a Cloud Agent:

- Continue from web or mobile (`cursor.com/agents`)
- Let the agent run long tasks while you're away
- Resume the session later from any device

**The `&` prefix:** Prepend any message with `&` to send it to the cloud.

<!--
This slide lists key points under What Is Cloud Handoff?.

The slide title is: What Is Cloud Handoff?.

The slide says: Send a local conversation to a Cloud Agent:.

The slide says: The & prefix: Prepend any message with & to send it to the cloud.

Bullet 1 on the slide: Continue from web or mobile (cursor.com/agents).

Bullet 2 on the slide: Let the agent run long tasks while you're away.

Bullet 3 on the slide: Resume the session later from any device.

Terms on this slide — quick definitions for the room:

Cloud handoff is when you prefix a message with ampersand in the CLI to continue the work as a Cloud Agent.

A Cloud Agent is a Cursor agent that runs on Cursor's infrastructure against a GitHub repository — you can launch it from the web UI or API.

Cloud Agents keep working when your laptop is closed — long tasks, parallel runs, handoffs from local sessions.

When the PR comes back, the same review discipline applies.
-->

---







<!-- _class: fit-sm -->

## Cloud Handoff Flow

<img src="assets/module-05/cloud-handoff-flow.svg" alt="Cloud Handoff Flow" />

<!--
This slide includes a diagram — Cloud Handoff Flow.

The slide title is: Cloud Handoff Flow.

The figure on this slide is titled: Cloud Handoff Flow.

Terms on this slide — quick definitions for the room:

Cloud handoff is when you prefix a message with ampersand in the CLI to continue the work as a Cloud Agent.

Cloud Agents keep working when your laptop is closed — long tasks, parallel runs, handoffs from local sessions.

When the PR comes back, the same review discipline applies.
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
We are starting Exercise 5.3 — Cloud Handoff. We have about 18 min for this lab.

Hand off a local CLI task to a Cloud Agent with &.

The full lab guide is in slide-exercises/module-05/exercise-5.3-cloud-handoff.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: Start local session and hand off:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "agent & "Analyze the entire codebase and create a dependency graph.""

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.3 — Steps 1–3.

Environment note on the slide: Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts).

The code on the slide reads: agent & "Analyze the entire codebase and create a dependency graph.".

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
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
Now for Steps 1–3 (Part 2).

Step 2: Verify handoff:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "🚀 Handing off to Cloud Agent... ✅ Session running at: https://cursor.com/agents/[agent-id]"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.3 — Steps 1–3 (Part 2).

The code on the slide reads: 🚀 Handing off to Cloud Agent... ✅ Session running at: https://cursor.com/agents/[agent-id].

Terms on this slide — quick definitions for the room:

A Cloud Agent is a Cursor agent that runs on Cursor's infrastructure against a GitHub repository — you can launch it from the web UI or API.

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







## Exercise 5.3 — Steps 1–3 (Part 3)

**Step 3:** Check status via browser or CLI
**Where:** **Web browser** — Edge or Chrome

<!--
Now for Steps 1–3 (Part 3).

Step 3: Check status via browser or CLI.

Where: Web browser — Edge or Chrome.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.3 — Steps 1–3 (Part 3).

Terms on this slide — quick definitions for the room:

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.
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
Now for Steps 4–6.

Step 4: Push existing conversation:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "& "Continue this conversation in the cloud. I need to log off.""

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.3 — Steps 4–6.

Environment note on the slide: Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts).

The code on the slide reads: & "Continue this conversation in the cloud. I need to log off.".

Terms on this slide — quick definitions for the room:

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







## Exercise 5.3 — Steps 4–6 (Part 2)

**Step 5:** Long-running task:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent "& Refactor the auth module to use JWT. Update all tests and docs."
```

<!--
Now for Steps 4–6 (Part 2).

Step 5: Long-running task:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "agent "& Refactor the auth module to use JWT. Update all tests and docs.""

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.3 — Steps 4–6 (Part 2).

The code on the slide reads: agent "& Refactor the auth module to use JWT. Update all tests and docs.".

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

JWT stands for JSON Web Token — a compact, signed token format often used for authentication.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







## Exercise 5.3 — Steps 4–6 (Part 3)

**Step 6:** Resume later:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```bash
agent --resume [agent-id-from-cloud]
```

<!--
Now for Steps 4–6 (Part 3).

Step 6: Resume later:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "agent --resume [agent-id-from-cloud]"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.3 — Steps 4–6 (Part 3).

The code on the slide reads: agent --resume [agent-id-from-cloud].

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







<!-- _class: fit-md -->

## Cloud Handoff Best Practices

| When to Use | When Not to Use |
|-------------|-----------------|
| Long-running tasks (>5 min) | Quick questions |
| When you need to close laptop | Interactive debugging |
| Overnight batch processing | Tasks needing terminal access |
| Parallel work streams | Security-sensitive code (local only) |

**Success Criteria:** Sent `&` message · verified cloud agent · accessed via web

<!--
This slide is a table — Cloud Handoff Best Practices.

The slide title is: Cloud Handoff Best Practices.

Success criteria listed: Sent & message · verified cloud agent · accessed via web.

The table header columns are: When to Use, When Not to Use.

In the table, Long-running tasks (>5 min): Quick questions.

In the table, When you need to close laptop: Interactive debugging.

In the table, Overnight batch processing: Tasks needing terminal access.

In the table, Parallel work streams: Security-sensitive code (local only).

Terms on this slide — quick definitions for the room:

Cloud handoff is when you prefix a message with ampersand in the CLI to continue the work as a Cloud Agent.

A Cloud Agent is a Cursor agent that runs on Cursor's infrastructure against a GitHub repository — you can launch it from the web UI or API.

Cloud Agents keep working when your laptop is closed — long tasks, parallel runs, handoffs from local sessions.

When the PR comes back, the same review discipline applies.
-->

---



<!-- _class: lead -->

# Lesson 5.4

## Listing and Resuming Sessions

*Concept · 8 min · Exercise · 12 min*

**Lab guide:** [`Exercise 5.4](../slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md)

<!--
Lesson 5.4: Listing and Resuming Sessions. For this lesson, listen, participate, or follow along as indicated on the next slides.

List, name, resume, and compress CLI Agent sessions.

The detailed lab guide is slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md.

The slide title is: Lesson 5.4.

You will also see the heading: Listing and Resuming Sessions.

The note on screen reads: Concept · 8 min · Exercise · 12 min.

The slide says: Lab guide: [`Exercise 5.4](../slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md).
-->

---







<!-- _class: fit-sm -->

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
This slide is a table — Session Management Commands.

The slide title is: Session Management Commands.

You will also see the heading: Session named "auth-refactor Agent".

The slide says: Tip: Name sessions with the first message:.

The table header columns are: Command, Purpose.

In the table, `/resume`: List all previous sessions and resume one.

In the table, `agent --resume [id]`: Resume a specific session by ID.

In the table, `agent --list`: List available sessions (alternative).

The code on the slide reads: agent "Just say one word: auth-refactor" # Session named "auth-refactor Agent".

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-md -->

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
We are starting Exercise 5.4 — Listing and Resuming Sessions. We have about 20 min for this lab.

List, name, resume, and compress CLI Agent sessions.

The full lab guide is in slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: Create multiple named sessions:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "agent "Just say one word: frontend-cleanup" # do work, exit agent "Just say one word: db-optimization" # do work, exit agent "Just say one word: docs-update""

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.4 — Steps 1–2.

Environment note on the slide: Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts).

The code on the slide reads: agent "Just say one word: frontend-cleanup"   # do work, exit agent "Just say one word: db-optimization"  # do work, exit agent "Just say one word: docs-update".

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







<!-- _class: fit-sm -->

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
Now for Steps 1–2 (Part 2).

Step 2: List all sessions:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "/resume # 1. frontend-cleanup Agent (2 hours ago) # 2. db-optimization Agent (1 hour ago) # 3. docs-update Agent (30 minutes ago)"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.4 — Steps 1–2 (Part 2).

You will also see the heading: 1. frontend-cleanup Agent (2 hours ago).

You will also see the heading: 2. db-optimization Agent (1 hour ago).

You will also see the heading: 3. docs-update Agent (30 minutes ago).

The code on the slide reads: /resume # 1. frontend-cleanup Agent (2 hours ago) # 2. db-optimization Agent (1 hour ago) # 3. docs-update Agent (30 minutes ago).

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
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
Now for Steps 3–5.

Step 3: Resume by ID:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "agent --resume abc123-def456-ghi789"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.4 — Steps 3–5.

Environment note on the slide: Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts).

The code on the slide reads: agent --resume abc123-def456-ghi789.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







## Exercise 5.4 — Steps 3–5 (Part 2)

**Step 4:** Concurrent sessions in different terminals:
**Where:** **Agent panel** — ``Ctrl+I``

```bash
# Terminal 1: agent --resume frontend-cleanup
# Terminal 2: agent --resume db-optimization
```

<!--
Now for Steps 3–5 (Part 2).

Step 4: Concurrent sessions in different terminals:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "# Terminal 1: agent --resume frontend-cleanup # Terminal 2: agent --resume db-optimization"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.4 — Steps 3–5 (Part 2).

You will also see the heading: Terminal 1: agent --resume frontend-cleanup.

You will also see the heading: Terminal 2: agent --resume db-optimization.

The code on the slide reads: # Terminal 1: agent --resume frontend-cleanup # Terminal 2: agent --resume db-optimization.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 5.4 — Steps 3–5 (Part 3)

**Step 5:** Context management:
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

```
/compress   # Summarize conversation, free context window
```

<!--
Now for Steps 3–5 (Part 3).

Step 5: Context management:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "/compress # Summarize conversation, free context window"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.4 — Steps 3–5 (Part 3).

The code on the slide reads: /compress   # Summarize conversation, free context window.

Terms on this slide — quick definitions for the room:

Context window is the maximum amount of text the model can consider at once — when you exceed it, older content drops off.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







## Exercise 5.4 — Steps 6–7 & Best Practices

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

**Step 6:** Export session summary as markdown
**Where:** **Agent panel** — ``Ctrl+I``

**Step 7:** Create `scripts/cursor-sessions.ps1` to list and manage sessions (optional `.sh` on Mac/Linux)
**Where:** **Agent panel** — ``Ctrl+I``

**Naming:** Use `[area]-[task]` format (e.g., `api-auth-fix`)

**Context:** Use `/compress` on long sessions · cloud handoff for very long tasks

**Cleanup:** Sessions persist indefinitely — manually complete or discard finished ones

**Success Criteria:** Created named sessions · listed with `/resume` · resumed · used `/compress`

<!--
Now for Steps 6–7 & Best Practices.

Step 6: Export session summary as markdown.

Where: Agent panel — `Ctrl+I`.

Step 7: Create scripts/cursor-sessions.ps1 to list and manage sessions (optional .sh on Mac/Linux).

Where: Agent panel — `Ctrl+I`.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 5.4 — Steps 6–7 & Best Practices.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The slide says: Naming: Use [area]-[task] format (e.g., api-auth-fix).

The slide says: Context: Use /compress on long sessions · cloud handoff for very long tasks.

The slide says: Cleanup: Sessions persist indefinitely — manually complete or discard finished ones.

Success criteria listed: Created named sessions · listed with /resume · resumed · used /compress.

Terms on this slide — quick definitions for the room:

Cloud handoff is when you prefix a message with ampersand in the CLI to continue the work as a Cloud Agent.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: lead -->

# Day 2

## Cloud Agents, APIs & Analytics

Cursor Training Program · Complete Course

<!--
Welcome back — Day 2.

Yesterday we established how AI models behave and how to use Cursor safely in real repositories. Today we extend that work outside the IDE: the CLI, Cloud Agents, and production-grade API integration.

Before we continue, make sure API keys are available where needed and that you can open PowerShell and reach api.cursor.com from this network. We will store every key in environment variables — never paste secrets on screen or into chat logs.

The slide title is: Day 2.

You will also see the heading: Cloud Agents, APIs & Analytics.

The slide says: Cursor Training Program · Complete Course.
-->

---







<!-- _header: 'Module 6 — Cloud Agents in the UI' -->

<!-- _class: lead -->

# Cloud Agents in the UI

## Module 6 · Day 2 (Hands-On + Demonstration)

Cursor Training Program · ~90 min

<!--
Module 6 introduces Cloud Agents in the Cursor UI — launching runs, tracking progress, and collecting artifacts.

Cloud Agents keep working when your laptop is closed — long tasks, parallel runs, handoffs from local sessions.

When the PR comes back, the same review discipline applies.

The slide title is: Cloud Agents in the UI.

You will also see the heading: Module 6 · Day 2 (Hands-On + Demonstration).

The slide says: Cursor Training Program · ~90 min.
-->

---







<!-- _class: fit-md -->

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~90 minutes |
| **Format** | Hands-on exercise + demonstration |
| **Prerequisites** | Cursor account, GitHub repository access, Modules 1–5 completed |
| **Module Goal** | Master Cloud Agents UI for remote execution, artifact collection, and messaging integrations |

### Lessons

| Lesson | Topic | Time |
|--------|-------|------|
| 6.1 | Launching a Cloud Agent | 25 min |
| 6.2 | Cloud Agent Artifacts | 23 min |
| 6.3 | Cloud Agents from Messaging Platforms | 20 min |

<!--
Here is the overview for Module 6.

The slide title is: Module Overview.

The table header columns are: Aspect, Details.

In the table, **Duration**: ~90 minutes.

In the table, **Format**: Hands-on exercise + demonstration.

In the table, **Prerequisites**: Cursor account, GitHub repository access, Modules 1–5 completed.

In the table, **Module Goal**: Master Cloud Agents UI for remote execution, artifact collection, and messaging integrations.

Terms on this slide — quick definitions for the room:

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.
-->

---



<!-- _class: lead -->

# Lesson 6.1

## Launching a Cloud Agent

*Concept · 10 min · Exercise · 15 min*

**Lab guide:** [`Exercise 6.1](../slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md)

<!--
Lesson 6.1: Launching a Cloud Agent. For this lesson, listen, participate, or follow along as indicated on the next slides.

Launch a Cloud Agent from the Cursor UI and track its run.

Cloud Agents keep working when your laptop is closed — long tasks, parallel runs, handoffs from local sessions.

When the PR comes back, the same review discipline applies.

The detailed lab guide is slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md.

The slide title is: Lesson 6.1.

You will also see the heading: Launching a Cloud Agent.

The note on screen reads: Concept · 10 min · Exercise · 15 min.

The slide says: Lab guide: [`Exercise 6.1](../slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md).

Terms on this slide — quick definitions for the room:

A Cloud Agent is a Cursor agent that runs on Cursor's infrastructure against a GitHub repository — you can launch it from the web UI or API.
-->

---







<!-- _class: fit-sm -->

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
This slide is a table — Cloud Agents vs. Local Agent.

The slide title is: Cloud Agents vs. Local Agent.

The table header columns are: Aspect, Local Agent, Cloud Agent.

In the table, **Runs on** — Your machine. Use case on slide: Cursor's infrastructure.

In the table, **Persistence** — Ends when you quit. Use case on slide: Continues indefinitely.

In the table, **Access** — Local only. Use case on slide: Web, mobile, API.

In the table, **Terminal access** — Your terminal. Use case on slide: Simulated/scripted.

In the table, **File access** — Local files. Use case on slide: GitHub repos only.

In the table, **Best for** — Interactive work. Use case on slide: Batch, scheduled, hands-off.

Terms on this slide — quick definitions for the room:

A Cloud Agent is a Cursor agent that runs on Cursor's infrastructure against a GitHub repository — you can launch it from the web UI or API.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

Cloud Agents keep working when your laptop is closed — long tasks, parallel runs, handoffs from local sessions.

When the PR comes back, the same review discipline applies.
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
This slide lists key points under When to Use Cloud Agents.

The slide title is: When to Use Cloud Agents.

The slide says: Good for:.

The slide says: Bad for:.

Bullet 1 on the slide: Long-running tasks (>10 min) · Scheduled jobs.

Bullet 2 on the slide: Tasks while offline · Parallel execution.

Bullet 3 on the slide: Team-accessible results (share agent URL).

Bullet 4 on the slide: Interactive debugging · Local-only files.

Bullet 5 on the slide: Security-sensitive code · Quick questions.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.

Cloud Agents keep working when your laptop is closed — long tasks, parallel runs, handoffs from local sessions.

When the PR comes back, the same review discipline applies.
-->

---







## Accessing Cloud Agents UI

| Method | Steps |
|--------|-------|
| **From Cursor Editor** | View → Cloud Agents (or cloud icon in sidebar) |
| **From Web** | https://cursor.com/agents |
| **From Mobile** | cursor.com/agents (responsive web) |

<!--
This slide is a table — Accessing Cloud Agents UI.

The slide title is: Accessing Cloud Agents UI.

The table header columns are: Method, Steps.

In the table, **From Cursor Editor**: View → Cloud Agents (or cloud icon in sidebar).

In the table, **From Web**: https://cursor.com/agents.

In the table, **From Mobile**: cursor.com/agents (responsive web).

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

Cloud Agents keep working when your laptop is closed — long tasks, parallel runs, handoffs from local sessions.

When the PR comes back, the same review discipline applies.
-->

---







<!-- _class: fit-sm -->

## Cloud Agent Dashboard

<img src="assets/module-06/cloud-agent-dashboard.svg" alt="Cloud Agent Dashboard" />

<!--
This slide includes a diagram — Cloud Agent Dashboard.

The slide title is: Cloud Agent Dashboard.

The figure on this slide is titled: Cloud Agent Dashboard.

Terms on this slide — quick definitions for the room:

A Cloud Agent is a Cursor agent that runs on Cursor's infrastructure against a GitHub repository — you can launch it from the web UI or API.

Cloud Agents keep working when your laptop is closed — long tasks, parallel runs, handoffs from local sessions.

When the PR comes back, the same review discipline applies.
-->

---







<!-- _class: fit-sm -->

## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Agent panel** (``Ctrl+I``) is for prompts and tool use · **Chat** (``Ctrl+L``) is read-only Q&A.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

The slide title is: Windows Exercise Environment.

The slide says: All exercises in this module assume Windows 10/11 with Cursor installed.

The slide says: Agent panel (`Ctrl+I) is for prompts and tool use · Chat (Ctrl+L`) is read-only Q&A.

The slide says: Set default profile: Settings → terminal.integrated.defaultProfile.windows → PowerShell.

The table header columns are: Terminal, Use when, Open in Cursor.

In the table, **PowerShell** — Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`). Use case on slide: ``Ctrl+` `` → **PowerShell**.

In the table, **Git Bash** — Bash syntax, `export VAR=...`, shell scripts ending in `.sh`. Use case on slide: Terminal menu → **Git Bash**.

In the table, **Command Prompt** — Legacy `.bat` files only. Use case on slide: Terminal menu → **Command Prompt**.

In the table, **Ubuntu (WSL)** — Linux-only tools or native bash without Git Bash. Use case on slide: Terminal menu → **Ubuntu (WSL)**.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.

npm is the Node Package Manager — the default registry and tool for JavaScript packages.
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
We are starting Exercise 6.1 — Launching a Cloud Agent. We have about 25 min for this lab.

Launch a Cloud Agent from the Cursor UI and track its run.

The full lab guide is in slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: Navigate to Cloud Agents.

Terminal: PowerShell — `Ctrl+ `` in Cursor.

Copy this into the Agent chat: "# Cursor Editor: cloud icon or View → Cloud Agents open https://cursor.com/agents"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 6.1 — Steps 1–2.

You will also see the heading: Cursor Editor: cloud icon or View → Cloud Agents.

Environment note on the slide: Platform: Windows 10/11 · PowerShell `Ctrl+ ` (Git Bash/WSL for .sh` scripts).

The code on the slide reads: # Cursor Editor: cloud icon or View → Cloud Agents open https://cursor.com/agents.

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







<!-- _class: fit-xs -->

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
Now for Steps 1–2 (Part 2).

Step 2: Click "+ New" and fill out:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "Repository: https://github.com/YOUR_ORG/YOUR_REPO Branch: main Prompt: Read README and main source files. Summarize: - What this project does - Key dependencies · How to run locally · Common issues Model: claude-4.6-sonnet Auto-create PR: ☐"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 6.1 — Steps 1–2 (Part 2).

Bullet 1 on the slide: What this project does.

Bullet 2 on the slide: Key dependencies · How to run locally · Common issues.

The code on the slide reads: Repository: https://github.com/YOUR_ORG/YOUR_REPO Branch: main Prompt: Read README and main source files. Summarize:   - What this project does   - Key dependencies · How to run locally · Common issues Model: claude-4.6-sonnet Auto-create PR: ☐.

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.

PR stands for Pull Request — a proposed code change others review before it merges.
-->

---







<!-- _class: fit-sm -->

## Exercise 6.1 — Steps 3–4

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**


**Step 3:** Monitor live log in real time:
**Where:** **Agent panel** — ``Ctrl+I``

```
[10:45:01] Agent starting...
[10:45:02] Cloning repository...
[10:45:15] Repository cloned
[10:45:16] Reading README.md
[10:45:40] Generating summary...
```

<!--
Now for Steps 3–4.

Step 3: Monitor live log in real time:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "[10:45:01] Agent starting... [10:45:02] Cloning repository... [10:45:15] Repository cloned [10:45:16] Reading README.md [10:45:40] Generating summary..."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 6.1 — Steps 3–4.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The code on the slide reads: [10:45:01] Agent starting... [10:45:02] Cloning repository... [10:45:15] Repository cloned [10:45:16] Reading README.md [10:45:40] Generating summary....

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-sm -->

## Exercise 6.1 — Steps 3–4 (Part 2)

**Step 4:** Configure settings (gear icon):
**Where:** **Agent panel** — ``Ctrl+I``

| Setting | Purpose |
|---------|---------|
| Default Model | Preferred model for new agents |
| Auto-create PR | Create PRs on completion |
| Notification Email | Completion notifications |
| Webhook URL | POST completion events |
| Max Run Time | 5 min – 24 hrs |

<!--
Now for Steps 3–4 (Part 2).

Step 4: Configure settings (gear icon):.

Where: Agent panel — `Ctrl+I`.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 6.1 — Steps 3–4 (Part 2).

The table header columns are: Setting, Purpose.

In the table, Default Model: Preferred model for new agents.

In the table, Auto-create PR: Create PRs on completion.

In the table, Notification Email: Completion notifications.

In the table, Webhook URL: POST completion events.

In the table, Max Run Time: 5 min – 24 hrs.

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.

PR stands for Pull Request — a proposed code change others review before it merges.
-->

---







<!-- _class: fit-md -->

## Exercise 6.1 — Steps 5–6

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**


**Step 5:** Launch with PR creation:
**Where:** **Agent panel** — ``Ctrl+I``

```
Prompt: Add CONTRIBUTING.md with dev setup, tests, PR process, code style
Auto-create PR: ✅ Yes
Branch prefix: docs/contributing
```

<!--
Now for Steps 5–6.

Step 5: Launch with PR creation:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "Prompt: Add CONTRIBUTING.md with dev setup, tests, PR process, code style Auto-create PR: ✅ Yes Branch prefix: docs/contributing"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 6.1 — Steps 5–6.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The code on the slide reads: Prompt: Add CONTRIBUTING.md with dev setup, tests, PR process, code style Auto-create PR: ✅ Yes Branch prefix: docs/contributing.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

PR stands for Pull Request — a proposed code change others review before it merges.
-->

---







## Exercise 6.1 — Steps 5–6 (Part 2)

**Step 6:** Share agent URL with team:
**Where:** **Agent panel** — ``Ctrl+I``

```
https://cursor.com/agents/agt_abc123def456
```

<!--
Now for Steps 5–6 (Part 2).

Step 6: Share agent URL with team:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "https://cursor.com/agents/agt_abc123def456"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 6.1 — Steps 5–6 (Part 2).

The code on the slide reads: https://cursor.com/agents/agt_abc123def456.

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.
-->

---



<!-- _class: lead -->

# Lesson 6.2

## Cloud Agent Artifacts

*Concept · 8 min · Exercise · 15 min*

**Lab guide:** [`Exercise 6.2](../slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md)

<!--
Lesson 6.2: Cloud Agent Artifacts. For this lesson, listen, participate, or follow along as indicated on the next slides.

Collect and download artifacts produced by Cloud Agents.

Cloud Agents keep working when your laptop is closed — long tasks, parallel runs, handoffs from local sessions.

When the PR comes back, the same review discipline applies.

The detailed lab guide is slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md.

The slide title is: Lesson 6.2.

You will also see the heading: Cloud Agent Artifacts.

The note on screen reads: Concept · 8 min · Exercise · 15 min.

The slide says: Lab guide: [`Exercise 6.2](../slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md).

Terms on this slide — quick definitions for the room:

A Cloud Agent is a Cursor agent that runs on Cursor's infrastructure against a GitHub repository — you can launch it from the web UI or API.

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.
-->

---







<!-- _class: fit-sm -->

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
This slide is a table — Types of Artifacts.

The slide title is: Types of Artifacts.

The slide quotes: ""Files produced by the agent that you can download or view in the UI.""

The table header columns are: Artifact Type, Examples.

In the table, **Log files**: `agent.log`, `debug.log`.

In the table, **Code files**: `*.py`, `*.js`, `*.html`.

In the table, **Documents**: `*.md`, `*.txt`, `*.json`.

In the table, **Images**: `*.png`, `*.jpg`, `*.svg`.

In the table, **Archives**: `*.zip`, `*.tar.gz`.

In the table, **Test results**: `junit.xml`, `coverage.json`.

Terms on this slide — quick definitions for the room:

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.
-->

---







## Artifact Storage

- Stored for **30 days**
- Multiple artifacts per agent
- Download URLs expire after **15 minutes**
- Max **100MB** per file · **1GB** total per agent

<!--
This slide lists key points under Artifact Storage.

The slide title is: Artifact Storage.

Bullet 1 on the slide: Stored for 30 days.

Bullet 2 on the slide: Multiple artifacts per agent.

Bullet 3 on the slide: Download URLs expire after 15 minutes.

Bullet 4 on the slide: Max 100MB per file · 1GB total per agent.

Terms on this slide — quick definitions for the room:

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







<!-- _class: fit-xs -->

## Exercise 6.2 — Steps 1–2

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**


**Step 1:** Launch agent that generates artifacts:
**Where:** **Agent panel** — ``Ctrl+I``

```
Generate:
1. api_documentation.md — OpenAPI-style docs for all endpoints
2. test_report.json — test suite summary
3. screenshot.png — main UI screenshot (if applicable)
4. dependencies.txt — all packages and versions

Place all in artifacts/ directory.
```

<!--
We are starting Exercise 6.2 — Cloud Agent Artifacts. We have about 25 min for this lab.

Collect and download artifacts produced by Cloud Agents.

The full lab guide is in slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: Launch agent that generates artifacts:.

Where: Agent panel — `Ctrl+I`.

Copy this into the Agent chat: "Generate: 1. api_documentation.md — OpenAPI-style docs for all endpoints 2. test_report.json — test suite summary 3. screenshot.png — main UI screenshot (if applicable) 4. dependencies.txt — all packages and versions Place all in artifacts/ directory."

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 6.2 — Steps 1–2.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The code on the slide reads: Generate: 1. api_documentation.md — OpenAPI-style docs for all endpoints 2. test_report.json — test suite summary 3. screenshot.png — main UI screenshot (if applicable) 4. dependencies.txt — all packages and versions Place all in artifacts/ directory..

Terms on this slide — quick definitions for the room:

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.

OpenAPI is the Open API Specification — a machine-readable description of REST endpoints.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







## Exercise 6.2 — Steps 1–2 (Part 2)

**Step 2:** After completion, view artifact list in UI with Download buttons and **Download All (zip)**
**Where:** **Agent panel** — ``Ctrl+I``

<!--
Now for Steps 1–2 (Part 2).

Step 2: After completion, view artifact list in UI with Download buttons and Download All (zip).

Where: Agent panel — `Ctrl+I`.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 6.2 — Steps 1–2 (Part 2).

Terms on this slide — quick definitions for the room:

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 6.2 — Steps 3–5

**Demonstration (Windows):** Agent ``Ctrl+I`` · **PowerShell** · Browser for dashboards


**Step 3:** Download individual artifacts
**Where:** **Agent panel** — ``Ctrl+I``

**Step 4:** Download all as zip
**Where:** **Agent panel** — ``Ctrl+I``

<!--
Now for Steps 3–5.

Step 3: Download individual artifacts.

Where: Agent panel — `Ctrl+I`.

Step 4: Download all as zip.

Where: Agent panel — `Ctrl+I`.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 6.2 — Steps 3–5.

Environment note on the slide: Demonstration (Windows): Agent `Ctrl+I` · PowerShell · Browser for dashboards.

Terms on this slide — quick definitions for the room:

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## Exercise 6.2 — Steps 3–5 (Part 2)

**Step 5:** Preview in browser:
**Where:** **Web browser** — Edge or Chrome
- Markdown → rendered HTML
- Images → inline preview
- JSON → formatted tree view

<!--
Now for Steps 3–5 (Part 2).

Step 5: Preview in browser:.

Where: Web browser — Edge or Chrome.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 6.2 — Steps 3–5 (Part 2).

Bullet 1 on the slide: Markdown → rendered HTML.

Bullet 2 on the slide: Images → inline preview.

Bullet 3 on the slide: JSON → formatted tree view.

Terms on this slide — quick definitions for the room:

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.
-->

---







<!-- _class: fit-xs -->

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
Now for API Access.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 6.2 — API Access.

You will also see the heading: List artifacts.

You will also see the heading: Download specific artifact.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

The slide says: Create bin/process-artifacts.sh to batch-download all artifacts for an agent ID.

The code on the slide reads: # List artifacts curl -s -u "$CURSOR_USER_API_KEY:" \   "https://api.cursor.com/v1/agents/$AGENT_ID/artifacts" | jq '.' # Download specific artifact DOWNLOAD_URL=$(curl -s -u "$CURSOR_USER_API_KEY:" \   ".../artifacts/download?path=artifacts/report.md" | jq -r '.url') curl -L -o report.md "$DOWNLOAD_URL".

Terms on this slide — quick definitions for the room:

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.
-->

---







<!-- _class: fit-sm -->

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
Now for CI/CD Integration.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 6.2 — CI/CD Integration.

You will also see the heading: GitHub Actions — download test results from completed agent.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

Success criteria listed: Generated artifacts · downloaded single + zip · accessed via API.

Bullet 1 on the slide: name: Download Cloud Agent artifacts.

The code on the slide reads: # GitHub Actions — download test results from completed agent - name: Download Cloud Agent artifacts   run: |     curl -s -u "${{ secrets.CURSOR_API_KEY }}:" \       ".../artifacts/download?path=test_results.xml" > test_results.xml.

Terms on this slide — quick definitions for the room:

A Cloud Agent is a Cursor agent that runs on Cursor's infrastructure against a GitHub repository — you can launch it from the web UI or API.

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.

CI/CD stands for Continuous Integration and Continuous Deployment — automated build, test, and release pipelines.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---



<!-- _class: lead -->

# Lesson 6.3

## Cloud Agents from Messaging Platforms

*Concept · 10 min · Demonstration*

<!--
Lesson 6.3: Cloud Agents from Messaging Platforms. For this lesson, listen, participate, or follow along as indicated on the next slides.

Cloud Agents keep working when your laptop is closed — long tasks, parallel runs, handoffs from local sessions.

When the PR comes back, the same review discipline applies.

The slide title is: Lesson 6.3.

You will also see the heading: Cloud Agents from Messaging Platforms.

The note on screen reads: Concept · 10 min · Demonstration.
-->

---







<!-- _class: fit-md -->

## Supported Integrations

| Platform | Capabilities | Setup |
|----------|--------------|-------|
| **Slack** | `@Cursor` mentions, command triggering, notifications | Medium (Slack app) |
| **Microsoft Teams** | `@Cursor` in channels, delegate tasks to cloud agents | Medium (Teams integration) |
| **Jira** | Assign issues to Cursor, `@Cursor` in comments, PR updates in Jira | Medium (requires Rovo) |
| **Discord** | Command triggering, webhook responses | Medium (Bot token) |
| **Generic Webhook** | POST-triggered agents | Low (any platform) |

<!--
This slide is a table — Supported Integrations.

The slide title is: Supported Integrations.

The table header columns are: Platform, Capabilities, Setup.

In the table, **Slack** — `@Cursor` mentions, command triggering, notifications. Use case on slide: Medium (Slack app).

In the table, **Microsoft Teams** — `@Cursor` in channels, delegate tasks to cloud agents. Use case on slide: Medium (Teams integration).

In the table, **Jira** — Assign issues to Cursor, `@Cursor` in comments, PR updates in Jira. Use case on slide: Medium (requires Rovo).

In the table, **Discord** — Command triggering, webhook responses. Use case on slide: Medium (Bot token).

In the table, **Generic Webhook** — POST-triggered agents. Use case on slide: Low (any platform).

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.

PR stands for Pull Request — a proposed code change others review before it merges.
-->

---







<!-- _class: fit-sm -->

## Messaging Integration Architecture

<img src="assets/module-06/messaging-integration-architecture.svg" alt="Messaging Integration Architecture" />

<!--
This slide includes a diagram — Messaging Integration Architecture.

The slide title is: Messaging Integration Architecture.

The figure on this slide is titled: Messaging Integration Architecture.
-->

---







<!-- _class: fit-sm -->

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
I am going to demonstrate Slack Integration live on my machine. Step 1: Create Slack App at api.slack.com Step 2: Configure slash command: Step 3: Deploy webhook receiver (Flask/Python) that: I will narrate each click and keystroke as I go.

When the demo finishes, we will discuss when slack integration belongs in production workflow and when a lighter-weight approach is enough.

The slide title is: Demo: Slack Integration.

Step 1: Create Slack App at api.slack.com.

Step 2: Configure slash command:.

Step 3: Deploy webhook receiver (Flask/Python) that:.

Bullet 1 on the slide: Parses Slack command → launches Cloud Agent via API.

Bullet 2 on the slide: Acknowledges immediately with agent URL.

Bullet 3 on the slide: Posts completion summary when webhook fires.

The code on the slide reads: Command: /cursor Request URL: https://your-server.com/webhook/slack-cursor Usage Hint: [prompt or command].

Terms on this slide — quick definitions for the room:

A slash command is a typed shortcut — often backed by a skill — that triggers a repeatable workflow.

A Cloud Agent is a Cursor agent that runs on Cursor's infrastructure against a GitHub repository — you can launch it from the web UI or API.

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.
-->

---







<!-- _class: fit-sm -->

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
I am going to demonstrate Slack Usage live on my machine. In Slack: Response: I will narrate each click and keystroke as I go.

When the demo finishes, we will discuss when slack usage belongs in production workflow and when a lighter-weight approach is enough.

The slide title is: Demo: Slack Usage.

The slide says: In Slack:.

The slide says: Response:.

The code on the slide reads: /cursor Review the recent commits and summarize what changed.

The code on the slide reads: 🤖 Launching Cloud Agent `agt_abc123` Watch progress: https://cursor.com/agents/agt_abc123 ✅ Cloud Agent Complete! Summary: 3 commits — fixed login bug, added tests, updated README. PR: https://github.com/your-org/your-repo/pull/43.

Terms on this slide — quick definitions for the room:

A Cloud Agent is a Cursor agent that runs on Cursor's infrastructure against a GitHub repository — you can launch it from the web UI or API.

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

PR stands for Pull Request — a proposed code change others review before it merges.
-->

---







<!-- _class: fit-md -->

## Demo: Jira Integration

**Step 1:** Install the Jira integration from the Cursor dashboard (requires Cursor admin access).

**Step 2:** Ensure Jira Commercial Cloud has **Rovo** enabled.

**Step 3:** Assign a work item to **Cursor** or mention `@Cursor` in a comment:

```
@Cursor Add input validation to the signup form and update tests.
```

**What happens:**
- Agent reads the issue title, description, comments, and repository settings
- Agent implements the fix and opens a pull request
- Jira receives a completion update with a link to the PR

<!--
I am going to demonstrate Jira Integration live on my machine. Step 1: Install the Jira integration from the Cursor dashboard (requires Cursor admin access). Step 2: Ensure Jira Commercial Cloud has Rovo enabled. Step 3: Assign a work item to Cursor or mention @Cursor in a comment: What happens: I will narrate each click and keystroke as I go.

When the demo finishes, we will discuss when jira integration belongs in production workflow and when a lighter-weight approach is enough.

The slide title is: Demo: Jira Integration.

Step 3: Assign a work item to Cursor or mention @Cursor in a comment:.

The slide says: What happens:.

Bullet 1 on the slide: Agent reads the issue title, description, comments, and repository settings.

Bullet 2 on the slide: Agent implements the fix and opens a pull request.

Bullet 3 on the slide: Jira receives a completion update with a link to the PR.

The code on the slide reads: @Cursor Add input validation to the signup form and update tests..

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

PR stands for Pull Request — a proposed code change others review before it merges.
-->

---







<!-- _class: fit-md -->

## Demo: Discord Integration

```python
@bot.command(name='cursor')
async def cursor_command(ctx, *, prompt):
    response = requests.post("https://api.cursor.com/v1/agents", ...)
    await ctx.send(f"✅ Agent launched: https://cursor.com/agents/{agent_id}")
```

Usage: `!cursor Add error handling to all API endpoints`

<!--
I am going to demonstrate Discord Integration live on my machine. Usage: !cursor Add error handling to all API endpoints I will narrate each click and keystroke as I go.

When the demo finishes, we will discuss when discord integration belongs in production workflow and when a lighter-weight approach is enough.

The slide title is: Demo: Discord Integration.

The slide says: Usage: !cursor Add error handling to all API endpoints.

The code on the slide reads: @bot.command(name='cursor') async def cursor_command(ctx, *, prompt):     response = requests.post("https://api.cursor.com/v1/agents", ...)     await ctx.send(f"✅ Agent launched: https://cursor.com/agents/{agent_id}").

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-md -->

## Generic Webhook & Notifications

**Any HTTP POST can trigger agents:**

```bash
curl -X POST https://your-server.com/trigger-agent \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Run the weekly security scan", "repo": "..."}'
```

**Use cases:** GitHub webhook on PR · Cron jobs · CI/CD post-deploy · Internal dashboard

**Status notifications:** configure `notifyOnStart`, `notifyOnComplete`, `notifyOnError`

**Success Criteria:** Understood architecture · saw Slack/Jira/Discord demos · webhook triggering

<!--
The slide title is: Generic Webhook & Notifications.

The slide says: Any HTTP POST can trigger agents:.

The slide says: Use cases: GitHub webhook on PR · Cron jobs · CI/CD post-deploy · Internal dashboard.

The slide says: Status notifications: configure notifyOnStart, notifyOnComplete, notifyOnError.

Success criteria listed: Understood architecture · saw Slack/Jira/Discord demos · webhook triggering.

The code on the slide reads: curl -X POST https://your-server.com/trigger-agent \   -H "Content-Type: application/json" \   -d '{"prompt": "Run the weekly security scan", "repo": "..."}'.

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

CI/CD stands for Continuous Integration and Continuous Deployment — automated build, test, and release pipelines.

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

HTTP stands for Hypertext Transfer Protocol — the request/response protocol browsers and APIs use.

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.

PR stands for Pull Request — a proposed code change others review before it merges.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.
-->

---







<!-- _header: 'Module 7 — Cursor API Foundations' -->

<!-- _class: lead -->

# Cursor API Foundations

## Module 7 · Day 2 (Concept + Hands-On)

Cursor Training Program · ~60 min

<!--
Module 7 covers API foundations — keys, errors, and caching — the infrastructure that keeps integrations running.

The slide title is: Cursor API Foundations.

You will also see the heading: Module 7 · Day 2 (Concept + Hands-On).

The slide says: Cursor Training Program · ~60 min.

Terms on this slide — quick definitions for the room:

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-md -->

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Concept + hands-on exercise |
| **Prerequisites** | Cursor account, basic API familiarity, Python 3.8+ installed |
| **Module Goal** | Understand the Cursor API ecosystem, authenticate securely, handle errors, and optimize requests |

### Lessons

| Lesson | Topic | Time |
|--------|-------|------|
| 7.1 | The Cursor API Landscape | 10 min |
| 7.2 | Authentication | 20 min |
| 7.3 | Rate Limits and Error Handling | 20 min |
| 7.4 | ETag Caching | 18 min |
| 7.5 | Listing Available Models | 10 min |

<!--
Here is the overview for Module 7.

The slide title is: Module Overview.

The table header columns are: Aspect, Details.

In the table, **Duration**: ~60 minutes.

In the table, **Format**: Concept + hands-on exercise.

In the table, **Prerequisites**: Cursor account, basic API familiarity, Python 3.8+ installed.

In the table, **Module Goal**: Understand the Cursor API ecosystem, authenticate securely, handle errors, and optimize requests.

Terms on this slide — quick definitions for the room:

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---



<!-- _class: lead -->

# Lesson 7.1

## The Cursor API Landscape

*Concept · 10 min*

<!--
Lesson 7.1: The Cursor API Landscape. For this lesson, listen, participate, or follow along as indicated on the next slides.

The slide title is: Lesson 7.1.

You will also see the heading: The Cursor API Landscape.

The note on screen reads: Concept · 10 min.

Terms on this slide — quick definitions for the room:

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-md -->

## The Five APIs

| API | Endpoint | Purpose |
|-----|----------|---------|
| **Chat Completions** | `/v1/chat/completions` | OpenAI-compatible chat interface |
| **Agents** | `/v1/agents` | Create and manage Cloud Agents |
| **Files** | `/v1/files` | Upload/download files for agents |
| **Admin** | `/v1/admin/*` | Team management, analytics, policies |
| **Webhooks** | `/v1/webhooks` | Register and manage webhook endpoints |

<!--
This slide is a table — The Five APIs.

The slide title is: The Five APIs.

The table header columns are: API, Endpoint, Purpose.

In the table, **Chat Completions** — `/v1/chat/completions`. Use case on slide: OpenAI-compatible chat interface.

In the table, **Agents** — `/v1/agents`. Use case on slide: Create and manage Cloud Agents.

In the table, **Files** — `/v1/files`. Use case on slide: Upload/download files for agents.

In the table, **Admin** — `/v1/admin/*`. Use case on slide: Team management, analytics, policies.

In the table, **Webhooks** — `/v1/webhooks`. Use case on slide: Register and manage webhook endpoints.

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-sm -->

## API Comparison Matrix

| API | Auth Type | Rate Limit | Cost | Primary Use |
|-----|-----------|------------|------|-------------|
| **Chat Completions** | User or API key | Per-minute token | Pay-per-token | Direct model access |
| **Agents** | User API key | Per-minute requests | Per-run | Long-running tasks |
| **Files** | User API key | Per-minute | Storage | Context upload |
| **Admin** | Admin API key | Higher limits | Included in plan | Team management |
| **Webhooks** | User API key | Per-minute | Free | Notifications |

<!--
This slide is a table — API Comparison Matrix.

The slide title is: API Comparison Matrix.

The table header columns are: API, Auth Type, Rate Limit, Cost, Primary Use.

Table row: **Chat Completions**, User or API key, Per-minute token, Pay-per-token.

Table row: **Agents**, User API key, Per-minute requests, Per-run.

Table row: **Files**, User API key, Per-minute, Storage.

Table row: **Admin**, Admin API key, Higher limits, Included in plan.

Table row: **Webhooks**, User API key, Per-minute, Free.

Terms on this slide — quick definitions for the room:

An Admin API Key is org-wide — for team membership, usage analytics, and spend limits.

A User API Key is scoped to your account — for launching agents and calling user-level endpoints.

A rate limit caps how many API requests you can make in a time window — exceed it and you get HTTP 429.

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.
-->

---







## When to Use Which API

- **Call a model directly** → Chat Completions API (OpenAI-compatible)
- **Run a long task that writes code** → Agents API
- **Manage team usage and limits** → Admin API
- **Be notified when agents complete** → Webhooks API

<!--
This slide lists key points under When to Use Which API.

The slide title is: When to Use Which API.

Bullet 1 on the slide: Call a model directly → Chat Completions API (OpenAI-compatible).

Bullet 2 on the slide: Run a long task that writes code → Agents API.

Bullet 3 on the slide: Manage team usage and limits → Admin API.

Bullet 4 on the slide: Be notified when agents complete → Webhooks API.

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-xs -->

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
The slide title is: OpenAI Compatibility.

Success criteria listed: Understand five APIs · select correct API · understand OpenAI compatibility.

The code on the slide reads: from openai import OpenAI client = OpenAI(     base_url="https://api.cursor.com/v1",     api_key="your-cursor-api-key" ) response = client.chat.completions.create(     model="claude-4.6-sonnet",     messages=[{"role": "user", "content": "Hello!"}] ).

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.
-->

---



<!-- _class: lead -->

# Lesson 7.2

## Authentication

*Concept · 8 min · Exercise · 12 min*

**Lab guide:** [`Exercise 7.2](../slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md)

<!--
Lesson 7.2: Authentication. For this lesson, listen, participate, or follow along as indicated on the next slides.

Create Admin and User API keys and verify authentication.

The detailed lab guide is slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md.

The slide title is: Lesson 7.2.

You will also see the heading: Authentication.

The note on screen reads: Concept · 8 min · Exercise · 12 min.

The slide says: Lab guide: [`Exercise 7.2](../slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md).

Terms on this slide — quick definitions for the room:

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-md -->

## Authentication Methods

| Method | Format | When to Use |
|--------|--------|-------------|
| **HTTP Basic** | `-u "api_key:"` | CLI, curl, most SDKs |
| **Bearer Token** | `Authorization: Bearer <key>` | OAuth-style clients |
| **User API Key** | Regular key | Agents, Chat, Files APIs |
| **Admin API Key** | `admin_` prefixed | Admin API only |

<!--
This slide is a table — Authentication Methods.

The slide title is: Authentication Methods.

The table header columns are: Method, Format, When to Use.

In the table, **HTTP Basic** — `-u "api_key:"`. Use case on slide: CLI, curl, most SDKs.

In the table, **Bearer Token** — `Authorization: Bearer <key>`. Use case on slide: OAuth-style clients.

In the table, **User API Key** — Regular key. Use case on slide: Agents, Chat, Files APIs.

In the table, **Admin API Key** — `admin_` prefixed. Use case on slide: Admin API only.

Terms on this slide — quick definitions for the room:

An Admin API Key is org-wide — for team membership, usage analytics, and spend limits.

A User API Key is scoped to your account — for launching agents and calling user-level endpoints.

Bearer token auth puts the key in an Authorization Bearer header — another common API style.

OAuth stands for Open Authorization — a standard for delegated login without sharing passwords.

HTTP stands for Hypertext Transfer Protocol — the request/response protocol browsers and APIs use.

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.
-->

---







<!-- _class: fit-md -->

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
This slide lists key points under API Key Types.

The slide title is: API Key Types.

The slide says: User API Key.

The slide says: Admin API Key.

Bullet 1 on the slide: Generated in: Cursor Settings → API Keys.

Bullet 2 on the slide: Format: cursor_xxxxxxxxxxxx.

Bullet 3 on the slide: Can access: Agents, Chat, Files, Webhooks.

Bullet 4 on the slide: Generated in: Organization Settings → API Keys.

Bullet 5 on the slide: Format: cursor_admin_xxxxxxxxxxxx.

Bullet 6 on the slide: Can access: Admin API + everything User can.

Terms on this slide — quick definitions for the room:

An Admin API Key is org-wide — for team membership, usage analytics, and spend limits.

A User API Key is scoped to your account — for launching agents and calling user-level endpoints.

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.
-->

---







<!-- _class: fit-md -->

## Security Best Practices

- Never commit API keys to git
- Use environment variables or secret managers
- Rotate keys periodically (every 90 days)
- Use different keys for dev and production
- Revoke unused keys immediately
- Use Admin API keys only when necessary
- Monitor key usage in dashboard

<!--
This slide lists key points under Security Best Practices.

The slide title is: Security Best Practices.

Bullet 1 on the slide: Never commit API keys to git.

Bullet 2 on the slide: Use environment variables or secret managers.

Bullet 3 on the slide: Rotate keys periodically (every 90 days).

Bullet 4 on the slide: Use different keys for dev and production.

Bullet 5 on the slide: Revoke unused keys immediately.

Bullet 6 on the slide: Use Admin API keys only when necessary.

Bullet 7 on the slide: Monitor key usage in dashboard.

Terms on this slide — quick definitions for the room:

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-sm -->

## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Agent panel** (``Ctrl+I``) is for prompts and tool use · **Chat** (``Ctrl+L``) is read-only Q&A.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

The slide title is: Windows Exercise Environment.

The slide says: All exercises in this module assume Windows 10/11 with Cursor installed.

The slide says: Agent panel (`Ctrl+I) is for prompts and tool use · Chat (Ctrl+L`) is read-only Q&A.

The slide says: Set default profile: Settings → terminal.integrated.defaultProfile.windows → PowerShell.

The table header columns are: Terminal, Use when, Open in Cursor.

In the table, **PowerShell** — Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`). Use case on slide: ``Ctrl+` `` → **PowerShell**.

In the table, **Git Bash** — Bash syntax, `export VAR=...`, shell scripts ending in `.sh`. Use case on slide: Terminal menu → **Git Bash**.

In the table, **Command Prompt** — Legacy `.bat` files only. Use case on slide: Terminal menu → **Command Prompt**.

In the table, **Ubuntu (WSL)** — Linux-only tools or native bash without Git Bash. Use case on slide: Terminal menu → **Ubuntu (WSL)**.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.

npm is the Node Package Manager — the default registry and tool for JavaScript packages.
-->

---







## Exercise 7.2 — Steps 1–3

**Platform:** Windows 10/11 · **PowerShell** for API · `$env:VAR` · `curl.exe`


**Step 1:** Generate User API Key — **Where:** **Cursor app** → **Settings** → **API Keys** → **Generate New Key** (copy the key; you will not see it again)

<!--
We are starting Exercise 7.2 — Generate and Test API Keys. We have about 15 min for this lab.

Create Admin and User API keys and verify authentication.

The full lab guide is in slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

A 401 usually means the wrong key type — Admin versus User — not a bad copy-paste.

Once you see a 200 with the expected JSON, you are ready for the rest of today's API labs.

Step 1: Generate User API Key — Where: Cursor app → Settings → API Keys → Generate New Key (copy the key; you will not see it again).

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 7.2 — Steps 1–3.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

Terms on this slide — quick definitions for the room:

A User API Key is scoped to your account — for launching agents and calling user-level endpoints.
-->

---







## Exercise 7.2 — Steps 1–3 (Part 2)

**Step 2:** Set environment variable — **Terminal:** **PowerShell** (``Ctrl+` ``)

```powershell
$env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx"
$env:CURSOR_USER_API_KEY
```

<!--
Now for Steps 1–3 (Part 2).

Step 2: Set environment variable — Terminal: PowerShell (`Ctrl+ ``).

Copy this into the Agent chat: "$env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx" $env:CURSOR_USER_API_KEY"

A 401 usually means the wrong key type — Admin versus User — not a bad copy-paste.

Once you see a 200 with the expected JSON, you are ready for the rest of today's API labs.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 7.2 — Steps 1–3 (Part 2).

The code on the slide reads: $env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx" $env:CURSOR_USER_API_KEY.

Terms on this slide — quick definitions for the room:

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







## Exercise 7.2 — Steps 1–3 (Part 3)

**Step 3:** Test with curl — **Terminal:** **PowerShell**

```powershell
curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" `
  https://api.cursor.com/v1/models | Select-Object -First 20
```

<!--
Now for Steps 1–3 (Part 3).

Step 3: Test with curl — Terminal: PowerShell.

A 401 usually means the wrong key type — Admin versus User — not a bad copy-paste.

Once you see a 200 with the expected JSON, you are ready for the rest of today's API labs.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 7.2 — Steps 1–3 (Part 3).

The code on the slide reads: curl.exe -s -u "$($env:CURSOR_USER_API_KEY):" `   https://api.cursor.com/v1/models | Select-Object -First 20.

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-md -->

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
Now for Steps 4–5.

Step 4: Test with Python requests:.

Terminal: PowerShell — save as test_models.py, then python test_models.py — `Ctrl+L`.

Copy this into the Agent chat: "response = requests.get( "https://api.cursor.com/v1/models", auth=(API_KEY, "") # Empty password )"

A 401 usually means the wrong key type — Admin versus User — not a bad copy-paste.

Once you see a 200 with the expected JSON, you are ready for the rest of today's API labs.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 7.2 — Steps 4–5.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The code on the slide reads: response = requests.get(     "https://api.cursor.com/v1/models",     auth=(API_KEY, "")  # Empty password ).

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-sm -->

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
Now for Steps 4–5 (Part 2).

Step 5: Test with OpenAI SDK:.

Terminal: PowerShell — python test_openai_sdk.py — `Ctrl+L`.

Copy this into the Agent chat: "client = OpenAI(base_url="https://api.cursor.com/v1", api_key=API_KEY) response = client.chat.completions.create( model="gpt-5-mini", messages=[{"role": "user", "content": "Say 'API works!'"}], max_tokens=10 )"

A 401 usually means the wrong key type — Admin versus User — not a bad copy-paste.

Once you see a 200 with the expected JSON, you are ready for the rest of today's API labs.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 7.2 — Steps 4–5 (Part 2).

The code on the slide reads: client = OpenAI(base_url="https://api.cursor.com/v1", api_key=API_KEY) response = client.chat.completions.create(     model="gpt-5-mini",     messages=[{"role": "user", "content": "Say 'API works!'"}],     max_tokens=10 ).

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

SDK stands for Software Development Kit — a library and helpers for calling an API from your language of choice.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.
-->

---







<!-- _class: fit-md -->

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
Now for Steps 6–7.

Step 6: Generate and test Admin API Key:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

A 401 usually means the wrong key type — Admin versus User — not a bad copy-paste.

Once you see a 200 with the expected JSON, you are ready for the rest of today's API labs.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 7.2 — Steps 6–7.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The code on the slide reads: export CURSOR_ADMIN_API_KEY="cursor_admin_xxxxxxxxxxxx" curl -s -u "$CURSOR_ADMIN_API_KEY:" \   https://api.cursor.com/v1/admin/organization | jq '.'.

Terms on this slide — quick definitions for the room:

An Admin API Key is org-wide — for team membership, usage analytics, and spend limits.

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







## Exercise 7.2 — Steps 6–7 (Part 2)

**Step 7:** Revoke compromised keys via API or Settings → API Keys → Revoke
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

**Success Criteria:** Generated keys · tested curl, Python, OpenAI SDK · tested Admin key

<!--
Now for Steps 6–7 (Part 2).

Step 7: Revoke compromised keys via API or Settings → API Keys → Revoke.

Terminal: PowerShell — unless step notes Git Bash or WSL.

A 401 usually means the wrong key type — Admin versus User — not a bad copy-paste.

Once you see a 200 with the expected JSON, you are ready for the rest of today's API labs.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 7.2 — Steps 6–7 (Part 2).

Success criteria listed: Generated keys · tested curl, Python, OpenAI SDK · tested Admin key.

Terms on this slide — quick definitions for the room:

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

SDK stands for Software Development Kit — a library and helpers for calling an API from your language of choice.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---



<!-- _class: lead -->

# Lesson 7.3

## Rate Limits and Error Handling

*Concept · 10 min · Exercise · 10 min*

**Lab guide:** [`Exercise 7.3](../slide-exercises/module-07/exercise-7.3-rate-limits-and-error-handling.md)

<!--
Lesson 7.3: Rate Limits and Error Handling. For this lesson, listen, participate, or follow along as indicated on the next slides.

Handle 429 responses with backoff and rate-limit headers.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.

The detailed lab guide is slide-exercises/module-07/exercise-7.3-rate-limits-and-error-handling.md.

The slide title is: Lesson 7.3.

You will also see the heading: Rate Limits and Error Handling.

The note on screen reads: Concept · 10 min · Exercise · 10 min.

The slide says: Lab guide: [`Exercise 7.3](../slide-exercises/module-07/exercise-7.3-rate-limits-and-error-handling.md).

Terms on this slide — quick definitions for the room:

A rate limit caps how many API requests you can make in a time window — exceed it and you get HTTP 429.
-->

---







<!-- _class: fit-md -->

## Rate Limits by API

| API | Limit | Window |
|-----|-------|--------|
| Chat Completions | 1000 requests | per minute |
| Chat Completions (tokens) | 500k tokens | per minute |
| Agents (create) | 100 requests | per minute |
| Admin API | 500 requests | per minute |
| Webhooks | 2000 requests | per minute |

<!--
This slide is a table — Rate Limits by API.

The slide title is: Rate Limits by API.

The table header columns are: API, Limit, Window.

In the table, Chat Completions — 1000 requests. Use case on slide: per minute.

In the table, Chat Completions (tokens) — 500k tokens. Use case on slide: per minute.

In the table, Agents (create) — 100 requests. Use case on slide: per minute.

In the table, Admin API — 500 requests. Use case on slide: per minute.

In the table, Webhooks — 2000 requests. Use case on slide: per minute.

Terms on this slide — quick definitions for the room:

A rate limit caps how many API requests you can make in a time window — exceed it and you get HTTP 429.

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.
-->

---







<!-- _class: fit-sm -->

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
This slide is a table — HTTP Status Codes to Handle.

The slide title is: HTTP Status Codes to Handle.

The table header columns are: Code, Meaning, Action.

In the table, **200** — Success. Use case on slide: Process response.

In the table, **400** — Bad Request. Use case on slide: Fix request parameters.

In the table, **401** — Unauthorized. Use case on slide: Check API key.

In the table, **403** — Forbidden. Use case on slide: Check permissions.

In the table, **429** — Too Many Requests. Use case on slide: Implement backoff.

In the table, **500/503** — Server Error. Use case on slide: Retry with backoff.

Terms on this slide — quick definitions for the room:

HTTP stands for Hypertext Transfer Protocol — the request/response protocol browsers and APIs use.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-md -->

## Rate Limit Headers

| Header | Description | Example |
|--------|-------------|---------|
| `X-RateLimit-Limit` | Max requests per window | `1000` |
| `X-RateLimit-Remaining` | Requests left | `942` |
| `X-RateLimit-Reset` | Window reset (Unix timestamp) | `1700000000` |
| `Retry-After` | Seconds to wait (on 429) | `60` |

<!--
This slide is a table — Rate Limit Headers.

The slide title is: Rate Limit Headers.

The table header columns are: Header, Description, Example.

In the table, `X-RateLimit-Limit` — Max requests per window. Use case on slide: `1000`.

In the table, `X-RateLimit-Remaining` — Requests left. Use case on slide: `942`.

In the table, `X-RateLimit-Reset` — Window reset (Unix timestamp). Use case on slide: `1700000000`.

In the table, `Retry-After` — Seconds to wait (on 429). Use case on slide: `60`.

Terms on this slide — quick definitions for the room:

A rate limit caps how many API requests you can make in a time window — exceed it and you get HTTP 429.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.
-->

---







<!-- _class: fit-xs -->

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
We are starting Exercise 7.3 — Rate Limits and Error Handling. We have about 15 min for this lab.

Handle 429 responses with backoff and rate-limit headers.

The full lab guide is in slide-exercises/module-07/exercise-7.3-rate-limits-and-error-handling.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 7.3 — Exponential Backoff.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The code on the slide begins: def call_with_retry(url, max_retries=5, base_delay=1.0):     for attempt in range(max_retries):         response = requests.get(url, auth=AUTH)         if response.status_code == 200:             return response.json()         if 400 <= response.status_code < 500:. The rest of the block continues on the slide.

Terms on this slide — quick definitions for the room:

Exponential backoff means waiting longer after each failed retry — standard practice when APIs return 429 or 5xx errors.

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.
-->

---







## Exercise 7.3 — Rate Limiter & Client

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

**Monitor headers:** warn when `X-RateLimit-Remaining` < 10% of limit

**Token bucket rate limiter:** space requests evenly across the minute window

**CursorAPIClient:** combines rate limiting, retries on 429/5xx, timeout handling, and typed methods like `get_models()` and `create_agent()`

**Success Criteria:** Backoff · header monitoring · rate limiter · robust client class

<!--
Now for Rate Limiter & Client.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 7.3 — Rate Limiter & Client.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The slide says: Monitor headers: warn when X-RateLimit-Remaining < 10% of limit.

The slide says: Token bucket rate limiter: space requests evenly across the minute window.

The slide says: CursorAPIClient: combines rate limiting, retries on 429/5xx, timeout handling, and typed methods like get_models() and create_agent().

Success criteria listed: Backoff · header monitoring · rate limiter · robust client class.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.
-->

---



<!-- _class: lead -->

# Lesson 7.4

## ETag Caching

*Concept · 8 min · Exercise · 10 min*

**Lab guide:** [`Exercise 7.4](../slide-exercises/module-07/exercise-7.4-etag-caching.md)

<!--
Lesson 7.4: ETag Caching. For this lesson, listen, participate, or follow along as indicated on the next slides.

Use ETags to avoid re-downloading unchanged API data.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.

The detailed lab guide is slide-exercises/module-07/exercise-7.4-etag-caching.md.

The slide title is: Lesson 7.4.

You will also see the heading: ETag Caching.

The note on screen reads: Concept · 8 min · Exercise · 10 min.

The slide says: Lab guide: [`Exercise 7.4](../slide-exercises/module-07/exercise-7.4-etag-caching.md).

Terms on this slide — quick definitions for the room:

ETag caching sends If-None-Match on repeat requests — if nothing changed, the server returns 304 and you skip re-downloading the body.
-->

---







## What Are ETags?

ETags are unique identifiers for API response versions.

1. Send `If-None-Match` header with previous ETag
2. Server returns `304 Not Modified` if unchanged
3. No data transfer, no rate limit consumption

<!--
Let's look at What Are ETags?.

The slide title is: What Are ETags?.

The slide says: ETags are unique identifiers for API response versions.

The slide says: 1. Send If-None-Match header with previous ETag.

The slide says: 2. Server returns 304 Not Modified if unchanged.

The slide says: 3. No data transfer, no rate limit consumption.

Number 1 on the slide: Send If-None-Match header with previous ETag.

Number 2 on the slide: Server returns 304 Not Modified if unchanged.

Number 3 on the slide: No data transfer, no rate limit consumption.

Terms on this slide — quick definitions for the room:

HTTP 304 Not Modified means your cached copy is still current — no response body, so you save bandwidth and time.

If-None-Match is an HTTP header carrying your cached ETag — the server uses it to decide whether data changed.

A rate limit caps how many API requests you can make in a time window — exceed it and you get HTTP 429.

ETag stands for Entity Tag — a version fingerprint the server returns so clients can ask whether data changed.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.
-->

---







<!-- _class: fit-sm -->

## ETag Flow

<img src="assets/module-07/etag-flow.svg" alt="ETag Flow" />

<!--
This slide includes a diagram — ETag Flow.

The slide title is: ETag Flow.

The figure on this slide is titled: ETag Flow.

Terms on this slide — quick definitions for the room:

ETag stands for Entity Tag — a version fingerprint the server returns so clients can ask whether data changed.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.
-->

---







<!-- _class: fit-md -->

## Endpoints Supporting ETags

| Endpoint | ETag Support | Cache Freshness |
|----------|--------------|-----------------|
| `/v1/models` | ✅ Yes | Changes rarely |
| `/v1/admin/members` | ✅ Yes | Changes occasionally |
| `/v1/agents/{id}` | ✅ Yes | Changes during run |
| `/v1/analytics/usage` | ✅ Yes | Daily changes |
| `/v1/agents` (list) | ⚠️ Partial | Changes frequently |

<!--
This slide is a table — Endpoints Supporting ETags.

The slide title is: Endpoints Supporting ETags.

In the table, Endpoint — ETag Support. Use case on slide: Cache Freshness.

In the table, `/v1/models` — ✅ Yes. Use case on slide: Changes rarely.

In the table, `/v1/admin/members` — ✅ Yes. Use case on slide: Changes occasionally.

In the table, `/v1/agents/{id}` — ✅ Yes. Use case on slide: Changes during run.

In the table, `/v1/analytics/usage` — ✅ Yes. Use case on slide: Daily changes.

In the table, `/v1/agents` (list) — ⚠️ Partial. Use case on slide: Changes frequently.

Terms on this slide — quick definitions for the room:

ETag stands for Entity Tag — a version fingerprint the server returns so clients can ask whether data changed.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.
-->

---







<!-- _class: fit-xs -->

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
We are starting Exercise 7.4 — ETag Caching. We have about 18 min for this lab.

Use ETags to avoid re-downloading unchanged API data.

The full lab guide is in slide-exercises/module-07/exercise-7.4-etag-caching.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 7.4 — Basic ETag Usage.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The code on the slide reads: def get_with_etag(url, previous_etag=None):     headers = {'If-None-Match': previous_etag} if previous_etag else {}     response = requests.get(url, auth=AUTH, headers=headers)     if response.status_code == 304:         return None, response.headers.get('ETag')  # Use cached data     if response.status_code == 200:         return response.json(), response.headers.get('ETag').

Terms on this slide — quick definitions for the room:

HTTP 304 Not Modified means your cached copy is still current — no response body, so you save bandwidth and time.

If-None-Match is an HTTP header carrying your cached ETag — the server uses it to decide whether data changed.

ETag stands for Entity Tag — a version fingerprint the server returns so clients can ask whether data changed.

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.
-->

---







## Exercise 7.4 — ETagCache & CachedClient

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

**ETagCache:** persistent pickle-based cache keyed by URL hash

**CachedCursorClient:**
- Check local cache → send `If-None-Match`
- On 304 → return cached data (Cache HIT)
- On 200 → update cache (Cache MISS)

**Batch analytics:** fetch 30 days of usage — unchanged days return 304 instantly

**Success Criteria:** Basic ETag request · persistent cache · analytics workload caching

<!--
Now for ETagCache & CachedClient.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 7.4 — ETagCache & CachedClient.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The slide says: ETagCache: persistent pickle-based cache keyed by URL hash.

The slide says: CachedCursorClient:.

The slide says: Batch analytics: fetch 30 days of usage — unchanged days return 304 instantly.

Success criteria listed: Basic ETag request · persistent cache · analytics workload caching.

Bullet 1 on the slide: Check local cache → send If-None-Match.

Bullet 2 on the slide: On 304 → return cached data (Cache HIT).

Bullet 3 on the slide: On 200 → update cache (Cache MISS).

Terms on this slide — quick definitions for the room:

HTTP 304 Not Modified means your cached copy is still current — no response body, so you save bandwidth and time.

If-None-Match is an HTTP header carrying your cached ETag — the server uses it to decide whether data changed.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

ETag stands for Entity Tag — a version fingerprint the server returns so clients can ask whether data changed.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.
-->

---



<!-- _class: lead -->

# Lesson 7.5

## Listing Available Models

*Concept · 4 min · Exercise · 6 min*

**Lab guide:** [`Exercise 7.5](../slide-exercises/module-07/exercise-7.5-list-available-models.md)

<!--
Lesson 7.5: Listing Available Models. For this lesson, listen, participate, or follow along as indicated on the next slides.

Query available models and pick the right one programmatically.

The detailed lab guide is slide-exercises/module-07/exercise-7.5-list-available-models.md.

The slide title is: Lesson 7.5.

You will also see the heading: Listing Available Models.

The note on screen reads: Concept · 4 min · Exercise · 6 min.

The slide says: Lab guide: [`Exercise 7.5](../slide-exercises/module-07/exercise-7.5-list-available-models.md).
-->

---







<!-- _class: fit-md -->

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
This slide highlights a key quote — The Models Endpoint.

The slide title is: The Models Endpoint.

The slide quotes: ""Simplest API call — perfect for verifying your API key works.""

The slide says: Response includes:.

Bullet 1 on the slide: Model ID · Display name · Context window size.

Bullet 2 on the slide: Pricing (input/output per 1M tokens).

Bullet 3 on the slide: Capabilities (vision, tool calling, etc.).

The code on the slide reads: GET /v1/models.

Terms on this slide — quick definitions for the room:

Context window is the maximum amount of text the model can consider at once — when you exceed it, older content drops off.

Tool calling means the model requests an action — read a file, run a command — and the host executes it; the model does not run code itself.

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
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
We are starting Exercise 7.5 — List Available Models. We have about 10 min for this lab.

Query available models and pick the right one programmatically.

The full lab guide is in slide-exercises/module-07/exercise-7.5-list-available-models.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: List with curl:.

Terminal: PowerShell — `Ctrl+ `` in Cursor.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 7.5 — Steps 1–2.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The code on the slide reads: curl -s -u "$CURSOR_USER_API_KEY:" \   https://api.cursor.com/v1/models \   | jq '.data[] | {id: .id, context: .context_window, input_price: .pricing.input}'.

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







## Exercise 7.5 — Steps 1–2 (Part 2)

**Step 2:** Format with Python tabulate — Model ID, Context, Input/Output Price, Vision support
**Terminal:** **PowerShell** — `python script.py`

<!--
Now for Steps 1–2 (Part 2).

Step 2: Format with Python tabulate — Model ID, Context, Input/Output Price, Vision support.

Terminal: PowerShell — python script.py.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 7.5 — Steps 1–2 (Part 2).
-->

---







<!-- _class: fit-sm -->

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
Now for Steps 3–4.

Step 3: Filter models:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "# Models with 100k+ context large_context = [m for m in models if m.get('context_window', 0) >= 100000] # Cheapest by input price cheapest = sorted(models, key=lambda x: x['pricing']['input'])[:5]"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 7.5 — Steps 3–4.

You will also see the heading: Models with 100k+ context.

You will also see the heading: Cheapest by input price.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The code on the slide reads: # Models with 100k+ context large_context = [m for m in models if m.get('context_window', 0) >= 100000] # Cheapest by input price cheapest = sorted(models, key=lambda x: x['pricing']['input'])[:5].

Terms on this slide — quick definitions for the room:

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
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
Now for Steps 3–4 (Part 2).

Step 4: Model selection helper:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "select_model("code_review", "balanced") # → claude-4.6-sonnet select_model("simple_fix", "low") # → gpt-5-mini select_model("frontend_ui", "high") # → gemini-3.1-pro"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 7.5 — Steps 3–4 (Part 2).

The code on the slide reads: select_model("code_review", "balanced")  # → claude-4.6-sonnet select_model("simple_fix", "low")        # → gpt-5-mini select_model("frontend_ui", "high")      # → gemini-3.1-pro.

Terms on this slide — quick definitions for the room:

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







<!-- _header: 'Module 8 — Cloud Agents API and Webhooks' -->

<!-- _class: lead -->

# Cloud Agents API and Webhooks

## Module 8 · Day 2 (Hands-On)

Cursor Training Program · ~60 min

<!--
Module 8 wires Cloud Agents programmatically: create runs, stream events, and verify webhooks.

Cloud Agents keep working when your laptop is closed — long tasks, parallel runs, handoffs from local sessions.

When the PR comes back, the same review discipline applies.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.

The slide title is: Cloud Agents API and Webhooks.

You will also see the heading: Module 8 · Day 2 (Hands-On).

The slide says: Cursor Training Program · ~60 min.

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-md -->

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise |
| **Prerequisites** | User API key (Module 7), Python 3.8+, ngrok installed, GitHub repository |
| **Module Goal** | Programmatically create, stream, and manage Cloud Agents, and set up webhook notifications |

### Lessons

| Lesson | Topic | Time |
|--------|-------|------|
| 8.1 | Creating a Cloud Agent Programmatically | 15 min |
| 8.2 | Streaming Agent Responses (SSE) | 15 min |
| 8.3 | Listing and Downloading Artifacts | 15 min |
| 8.4 | Creating a Webhook Endpoint | 15 min |
| 8.5 | Testing Webhooks Locally with ngrok | 13 min |
| 8.6 | End-to-End Automated Agent Workflow | 17 min |

<!--
Here is the overview for Module 8.

The slide title is: Module Overview.

The table header columns are: Aspect, Details.

In the table, **Duration**: ~60 minutes.

In the table, **Format**: Hands-on exercise.

In the table, **Prerequisites**: User API key (Module 7), Python 3.8+, ngrok installed, GitHub repository.

In the table, **Module Goal**: Programmatically create, stream, and manage Cloud Agents, and set up webhook notifications.

Terms on this slide — quick definitions for the room:

A User API Key is scoped to your account — for launching agents and calling user-level endpoints.

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

ngrok creates a public HTTPS tunnel to your laptop so Cursor can deliver webhooks to a local dev server.
-->

---



<!-- _class: lead -->

# Lesson 8.1

## Creating a Cloud Agent Programmatically

*Concept · 5 min · Exercise · 10 min*

**Lab guide:** [`Exercise 8.1](../slide-exercises/module-08/exercise-8.1-create-a-cloud-agent-via-api.md)

<!--
Lesson 8.1: Creating a Cloud Agent Programmatically. For this lesson, listen, participate, or follow along as indicated on the next slides.

Create a Cloud Agent run using curl or Python.

Cloud Agents keep working when your laptop is closed — long tasks, parallel runs, handoffs from local sessions.

When the PR comes back, the same review discipline applies.

The detailed lab guide is slide-exercises/module-08/exercise-8.1-create-a-cloud-agent-via-api.md.

The slide title is: Lesson 8.1.

You will also see the heading: Creating a Cloud Agent Programmatically.

The note on screen reads: Concept · 5 min · Exercise · 10 min.

The slide says: Lab guide: [`Exercise 8.1](../slide-exercises/module-08/exercise-8.1-create-a-cloud-agent-via-api.md).

Terms on this slide — quick definitions for the room:

A Cloud Agent is a Cursor agent that runs on Cursor's infrastructure against a GitHub repository — you can launch it from the web UI or API.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







## Agent + Runs

| Concept | Description |
|---------|-------------|
| **Agent** | Durable entity with conversation history and workspace state |
| **Run** | Single execution (one prompt/response cycle) |

**Key endpoint:** `POST /v1/agents`

<!--
This slide is a table — Agent + Runs.

The slide title is: Agent + Runs.

The slide says: Key endpoint: POST /v1/agents.

The table header columns are: Concept, Description.

In the table, **Agent**: Durable entity with conversation history and workspace state.

In the table, **Run**: Single execution (one prompt/response cycle).

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
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
This slide is a table — Request Fields.

The slide title is: Request Fields.

The slide says: Required:.

The slide says: Optional: autoCreatePR · model.id · webhookUrl · webhookSecret.

The table header columns are: Field, Example.

In the table, `prompt.text`: "Add a README.md file".

In the table, `repos[].url`: "https://github.com/org/repo".

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.
-->

---







<!-- _class: fit-sm -->

## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Agent panel** (``Ctrl+I``) is for prompts and tool use · **Chat** (``Ctrl+L``) is read-only Q&A.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

The slide title is: Windows Exercise Environment.

The slide says: All exercises in this module assume Windows 10/11 with Cursor installed.

The slide says: Agent panel (`Ctrl+I) is for prompts and tool use · Chat (Ctrl+L`) is read-only Q&A.

The slide says: Set default profile: Settings → terminal.integrated.defaultProfile.windows → PowerShell.

The table header columns are: Terminal, Use when, Open in Cursor.

In the table, **PowerShell** — Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`). Use case on slide: ``Ctrl+` `` → **PowerShell**.

In the table, **Git Bash** — Bash syntax, `export VAR=...`, shell scripts ending in `.sh`. Use case on slide: Terminal menu → **Git Bash**.

In the table, **Command Prompt** — Legacy `.bat` files only. Use case on slide: Terminal menu → **Command Prompt**.

In the table, **Ubuntu (WSL)** — Linux-only tools or native bash without Git Bash. Use case on slide: Terminal menu → **Ubuntu (WSL)**.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.

npm is the Node Package Manager — the default registry and tool for JavaScript packages.
-->

---







<!-- _class: fit-xs -->

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
We are starting Exercise 8.1 — Create a Cloud Agent via API. We have about 15 min for this lab.

Create a Cloud Agent run using curl or Python.

The full lab guide is in slide-exercises/module-08/exercise-8.1-create-a-cloud-agent-via-api.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1 — set API key · Terminal: PowerShell.

Step 2 — create agent · Terminal: PowerShell.

Copy this into the Agent chat: "$env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx""

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.1 — Create with curl.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: Terminal (alternative): Git Bash / WSL — bash block below.

The code on the slide reads: $env:CURSOR_USER_API_KEY = "cursor_xxxxxxxxxxxx".

The code on the slide reads: curl.exe -X POST https://api.cursor.com/v1/agents `   -u "$($env:CURSOR_USER_API_KEY):" `   -H "Content-Type: application/json" `   -d '{"prompt":{"text":"Add a README.md file with setup instructions"},"repos":[{"url":"https://github.com/YOUR_ORG/YOUR_REPO","startingRef":"main"}],"autoCreatePR":true}' `   | ConvertFrom-Json.

The code on the slide reads: export CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx" curl -X POST https://api.cursor.com/v1/agents   -u "$CURSOR_USER_API_KEY:"   -H "Content-Type: application/json"   -d '{"prompt":{"text":"Add a README.md file with setup instructions"},"repos":[{"url":"https://github.com/YOUR_ORG/YOUR_REPO","startingRef":"main"}],"autoCreatePR":true}' | jq '.'.

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







<!-- _class: fit-sm -->

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
Now for Capture IDs.

Step 1: Save the JSON from the create-agent call — Terminal: PowerShell.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.1 — Capture IDs.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The code on the slide reads: $response = curl.exe ... | ConvertFrom-Json   # reuse create-agent command $env:AGENT_ID = $response.agent.id $env:RUN_ID = $response.run.id Write-Host "Agent ID: $($env:AGENT_ID)" Write-Host "Dashboard: https://cursor.com/agents/$($env:AGENT_ID)".

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







## Exercise 8.1 — Capture IDs (Part 2)

**Step 2:** Optional model override in create payload — **Where:** edit JSON before POST (any terminal)

Create with specific model: `"model": {"id": "claude-4.7-opus"}`

<!--
Now for Capture IDs (Part 2).

Step 2: Optional model override in create payload — Where: edit JSON before POST (any terminal).

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.1 — Capture IDs (Part 2).

The slide says: Create with specific model: "model": {"id": "claude-4.7-opus"}.

Terms on this slide — quick definitions for the room:

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.
-->

---







<!-- _class: fit-xs -->

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
Now for Python Helper.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.1 — Python Helper.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

Success criteria listed: Agent created · IDs captured · appears in dashboard · Python function works.

The code on the slide begins: def create_agent(prompt, repo_url, auto_create_pr=False, model=None):     payload = {         "prompt": {"text": prompt},         "repos": [{"url": repo_url}],         "autoCreatePR": auto_create_pr     }. The rest of the block continues on the slide.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.

PR stands for Pull Request — a proposed code change others review before it merges.
-->

---



<!-- _class: lead -->

# Lesson 8.2

## Streaming Agent Responses (SSE)

*Concept · 5 min · Exercise · 10 min*

**Lab guide:** [`Exercise 8.2](../slide-exercises/module-08/exercise-8.2-stream-agent-responses-sse.md)

<!--
Lesson 8.2: Streaming Agent Responses (SSE). For this lesson, listen, participate, or follow along as indicated on the next slides.

Stream Cloud Agent events with Server-Sent Events.

The detailed lab guide is slide-exercises/module-08/exercise-8.2-stream-agent-responses-sse.md.

The slide title is: Lesson 8.2.

You will also see the heading: Streaming Agent Responses (SSE).

The note on screen reads: Concept · 5 min · Exercise · 10 min.

The slide says: Lab guide: [`Exercise 8.2](../slide-exercises/module-08/exercise-8.2-stream-agent-responses-sse.md).

Terms on this slide — quick definitions for the room:

Streaming means events arrive incrementally over SSE instead of waiting for one complete response at the end.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

SSE stands for Server-Sent Events — a way the server pushes live updates over one long HTTP connection.
-->

---







<!-- _class: fit-sm -->

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
This slide is a table — SSE Event Types.

The slide title is: SSE Event Types.

The table header columns are: Event, When It Happens, Data Example.

In the table, `status` — Run status changes. Use case on slide: `{"status":"RUNNING"}`.

In the table, `assistant` — Agent speaks. Use case on slide: `{"text":"I'll read the file..."}`.

In the table, `thinking` — Agent is reasoning. Use case on slide: `{"text":"Let me consider..."}`.

In the table, `tool_call` — Agent uses a tool. Use case on slide: `{"name":"read_file","status":"started"}`.

In the table, `result` — Run completes. Use case on slide: `{"status":"FINISHED"}`.

In the table, `error` — Something went wrong. Use case on slide: `{"message":"..."}`.

In the table, `done` — Stream ends. Use case on slide: `{}`.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

SSE stands for Server-Sent Events — a way the server pushes live updates over one long HTTP connection.
-->

---







## Resume Support

SSE streams support the **`Last-Event-ID`** header — if your connection drops, resume from the last received event.

<!--
Let's look at Resume Support.

The slide title is: Resume Support.

The slide says: SSE streams support the Last-Event-ID header — if your connection drops, resume from the last received event.

Terms on this slide — quick definitions for the room:

Last-Event-ID lets you resume an SSE stream after a disconnect — the server continues from the last event you received.

SSE stands for Server-Sent Events — a way the server pushes live updates over one long HTTP connection.
-->

---







<!-- _class: fit-md -->

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
We are starting Exercise 8.2 — Stream Agent Responses (SSE). We have about 15 min for this lab.

Stream Cloud Agent events with Server-Sent Events.

The full lab guide is in slide-exercises/module-08/exercise-8.2-stream-agent-responses-sse.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Terminal: PowerShell.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.2 — Stream with curl.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: Set IDs first: $env:AGENT_ID = "..." · $env:RUN_ID = "...".

The slide says: Terminal (alternative): Git Bash / WSL — bash curl -N block above.

The slide says: Parse lines starting with event: and data: — print assistant text, tool calls, and result status.

The code on the slide reads: curl.exe -N -u "$($env:CURSOR_USER_API_KEY):" `   -H "Accept: text/event-stream" `   "https://api.cursor.com/v1/agents/$env:AGENT_ID/runs/$env:RUN_ID/stream".

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







<!-- _class: fit-xs -->

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
Now for Python SSE Client.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.2 — Python SSE Client.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The code on the slide reads: def stream_agent_response(agent_id, run_id, on_event=None):     url = f"{BASE_URL}/agents/{agent_id}/runs/{run_id}/stream"     response = requests.get(url, auth=AUTH, stream=True)     for line in response.iter_lines():         if line.startswith(b'event:'):             current_event = line[6:].strip().decode()         elif line.startswith(b'data:'):             data = json.loads(line[5:].strip())             if on_event:                 on_event(current_event, data).

Terms on this slide — quick definitions for the room:

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

SSE stands for Server-Sent Events — a way the server pushes live updates over one long HTTP connection.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.
-->

---







## Exercise 8.2 — ResumableSSEClient

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

Track `last_event_id` from `id:` lines → send as `Last-Event-ID` header on reconnect

**Also:** `stream_to_file()` saves full SSE log for later review

**Success Criteria:** Stream connected · received events · Python client works · resume implemented

<!--
Now for ResumableSSEClient.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.2 — ResumableSSEClient.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The slide says: Track last_event_id from id: lines → send as Last-Event-ID header on reconnect.

The slide says: Also: stream_to_file() saves full SSE log for later review.

Success criteria listed: Stream connected · received events · Python client works · resume implemented.

Terms on this slide — quick definitions for the room:

Last-Event-ID lets you resume an SSE stream after a disconnect — the server continues from the last event you received.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

SSE stands for Server-Sent Events — a way the server pushes live updates over one long HTTP connection.
-->

---



<!-- _class: lead -->

# Lesson 8.3

## Listing and Downloading Artifacts

*Concept · 5 min · Exercise · 10 min*

**Lab guide:** [`Exercise 8.3](../slide-exercises/module-08/exercise-8.3-list-and-download-artifacts.md)

<!--
Lesson 8.3: Listing and Downloading Artifacts. For this lesson, listen, participate, or follow along as indicated on the next slides.

Wait for completion, list artifacts, and download outputs.

The detailed lab guide is slide-exercises/module-08/exercise-8.3-list-and-download-artifacts.md.

The slide title is: Lesson 8.3.

You will also see the heading: Listing and Downloading Artifacts.

The note on screen reads: Concept · 5 min · Exercise · 10 min.

The slide says: Lab guide: [`Exercise 8.3](../slide-exercises/module-08/exercise-8.3-list-and-download-artifacts.md).

Terms on this slide — quick definitions for the room:

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.
-->

---







## Key Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/v1/agents/{id}/artifacts` | GET | List all artifacts |
| `/v1/agents/{id}/artifacts/download` | GET | Get presigned URL for download |

**Important:** Download URLs expire after **15 minutes**.

<!--
This slide is a table — Key Endpoints.

The slide title is: Key Endpoints.

The slide says: Important: Download URLs expire after 15 minutes.

The table header columns are: Endpoint, Method, Purpose.

In the table, `/v1/agents/{id}/artifacts` — GET. Use case on slide: List all artifacts.

In the table, `/v1/agents/{id}/artifacts/download` — GET. Use case on slide: Get presigned URL for download.

Terms on this slide — quick definitions for the room:

A presigned URL is a time-limited download link — common for Cloud Agent artifacts that expire after a short window.

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.
-->

---







<!-- _class: fit-xs -->

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
We are starting Exercise 8.3 — List and Download Artifacts. We have about 15 min for this lab.

Wait for completion, list artifacts, and download outputs.

The full lab guide is in slide-exercises/module-08/exercise-8.3-list-and-download-artifacts.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.3 — Wait & List.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The code on the slide reads: def wait_for_completion(agent_id, timeout=300, poll_interval=5):     while time.time() - start < timeout:         status = get_agent_status(agent_id).get('status')         if status == 'FINISHED': return True         elif status == 'ERROR': return False         time.sleep(poll_interval) def list_artifacts(agent_id):     response = requests.get(f"{BASE_URL}/agents/{agent_id}/artifacts", auth=AUTH)     return response.json().get('items', []).

Terms on this slide — quick definitions for the room:

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.
-->

---







<!-- _class: fit-xs -->

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
Now for Download.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.3 — Download.

You will also see the heading: curl download_url → save to disk.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: Single artifact:.

The slide says: All artifacts: loop items, create subdirs, download each via presigned URL.

The code on the slide reads: response = requests.get(     f"{BASE_URL}/agents/{agent_id}/artifacts/download",     auth=AUTH, params={"path": artifact_path} ) download_url = response.json().get('url') # curl download_url → save to disk.

Terms on this slide — quick definitions for the room:

A presigned URL is a time-limited download link — common for Cloud Agent artifacts that expire after a short window.

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-md -->

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
Now for CI Integration.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.3 — CI Integration.

You will also see the heading: Parse XML → exit 1 if failures/errors, else exit 0.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

Success criteria listed: Listed artifacts · downloaded single + all · CI workflow integration.

The code on the slide reads: def process_test_results(agent_id):     wait_for_completion(agent_id, timeout=600)     download_artifact(agent_id, "artifacts/junit.xml", "test_results.xml")     # Parse XML → exit 1 if failures/errors, else exit 0.

Terms on this slide — quick definitions for the room:

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---



<!-- _class: lead -->

# Lesson 8.4

## Creating a Webhook Endpoint

*Concept · 5 min · Exercise · 10 min*

**Lab guide:** [`Exercise 8.4](../slide-exercises/module-08/exercise-8.4-webhooks-and-hmac-verification.md)

<!--
Lesson 8.4: Creating a Webhook Endpoint. For this lesson, listen, participate, or follow along as indicated on the next slides.

Receive webhooks and verify HMAC signatures.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.

The detailed lab guide is slide-exercises/module-08/exercise-8.4-webhooks-and-hmac-verification.md.

The slide title is: Lesson 8.4.

You will also see the heading: Creating a Webhook Endpoint.

The note on screen reads: Concept · 5 min · Exercise · 10 min.

The slide says: Lab guide: [`Exercise 8.4](../slide-exercises/module-08/exercise-8.4-webhooks-and-hmac-verification.md).

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

HMAC stands for Hash-based Message Authentication Code — a signed digest that proves a webhook payload was not tampered with.
-->

---







## Webhook Headers

| Header | Description |
|--------|-------------|
| `X-Webhook-Signature` | HMAC-SHA256 signature for verification |
| `X-Webhook-ID` | Unique delivery ID |
| `X-Webhook-Event` | Event type (`statusChange`) |

<!--
This slide is a table — Webhook Headers.

The slide title is: Webhook Headers.

The table header columns are: Header, Description.

In the table, `X-Webhook-Signature`: HMAC-SHA256 signature for verification.

In the table, `X-Webhook-ID`: Unique delivery ID.

In the table, `X-Webhook-Event`: Event type (`statusChange`).

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

HMAC stands for Hash-based Message Authentication Code — a signed digest that proves a webhook payload was not tampered with.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.
-->

---







<!-- _class: fit-xs -->

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
The slide title is: Webhook Payload.

The code on the slide reads: {   "event": "statusChange",   "id": "agent_abc123",   "status": "FINISHED",   "source": {"repository": "https://github.com/your-org/your-repo"},   "target": {"url": "...", "prUrl": "https://github.com/.../pull/123"},   "summary": "Added README.md and fixed tests" }.

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.
-->

---







<!-- _class: fit-sm -->

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
We are starting Exercise 8.4 — Webhooks and HMAC Verification. We have about 15 min for this lab.

Receive webhooks and verify HMAC signatures.

The full lab guide is in slide-exercises/module-08/exercise-8.4-webhooks-and-hmac-verification.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.4 — HMAC Verification.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: Flask route: verify signature → parse payload → handle FINISHED/ERROR.

The code on the slide reads: def verify_signature(raw_body, signature_header):     received = signature_header[7:]  # strip "sha256="     expected = hmac.new(         WEBHOOK_SECRET.encode(), raw_body, hashlib.sha256     ).hexdigest()     return hmac.compare_digest(expected, received).

Terms on this slide — quick definitions for the room:

HMAC stands for Hash-based Message Authentication Code — a signed digest that proves a webhook payload was not tampered with.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-xs -->

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
Now for Configure Agent.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.4 — Configure Agent.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

Success criteria listed: Server running · signature verified · payload parsed · agent configured.

The code on the slide reads: curl -X POST https://api.cursor.com/v1/agents \   -u "$CURSOR_USER_API_KEY:" \   -H "Content-Type: application/json" \   -d '{     "prompt": {"text": "Add a CONTRIBUTING.md file"},     "repos": [{"url": "https://github.com/YOUR_ORG/YOUR_REPO"}],     "webhookUrl": "https://your-domain.com/webhook/cursor",     "webhookSecret": "your-secret-here",     "autoCreatePR": true   }'.

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.
-->

---



<!-- _class: lead -->

# Lesson 8.5

## Testing Webhooks Locally with ngrok

*Concept · 5 min · Exercise · 8 min*

**Lab guide:** [`Exercise 8.5](../slide-exercises/module-08/exercise-8.5-test-webhooks-with-ngrok.md)

<!--
Lesson 8.5: Testing Webhooks Locally with ngrok. For this lesson, listen, participate, or follow along as indicated on the next slides.

Expose a local server with ngrok and inspect webhook payloads.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.

The detailed lab guide is slide-exercises/module-08/exercise-8.5-test-webhooks-with-ngrok.md.

The slide title is: Lesson 8.5.

You will also see the heading: Testing Webhooks Locally with ngrok.

The note on screen reads: Concept · 5 min · Exercise · 8 min.

The slide says: Lab guide: [`Exercise 8.5](../slide-exercises/module-08/exercise-8.5-test-webhooks-with-ngrok.md).

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

ngrok creates a public HTTPS tunnel to your laptop so Cursor can deliver webhooks to a local dev server.
-->

---







## What Is ngrok?

Creates a secure tunnel from a public URL to your local server.

- Test webhooks without deploying
- Debug locally · Demo to stakeholders

<!--
This slide lists key points under What Is ngrok?.

The slide title is: What Is ngrok?.

The slide says: Creates a secure tunnel from a public URL to your local server.

Bullet 1 on the slide: Test webhooks without deploying.

Bullet 2 on the slide: Debug locally · Demo to stakeholders.

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

ngrok creates a public HTTPS tunnel to your laptop so Cursor can deliver webhooks to a local dev server.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.
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
We are starting Exercise 8.5 — Test Webhooks with ngrok. We have about 15 min for this lab.

Expose a local server with ngrok and inspect webhook payloads.

The full lab guide is in slide-exercises/module-08/exercise-8.5-test-webhooks-with-ngrok.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

Step 1: Start tunnel:.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Copy this into the Agent chat: "ngrok http 5000 # Forwarding: https://abc123.ngrok.io -> http://localhost:5000"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.5 — Steps 1–3.

You will also see the heading: Forwarding: https://abc123.ngrok.io -> http://localhost:5000.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The code on the slide reads: ngrok http 5000 # Forwarding: https://abc123.ngrok.io -> http://localhost:5000.

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

ngrok creates a public HTTPS tunnel to your laptop so Cursor can deliver webhooks to a local dev server.

HTTP stands for Hypertext Transfer Protocol — the request/response protocol browsers and APIs use.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---







## Exercise 8.5 — Steps 1–3 (Part 2)

**Step 2:** Copy HTTPS URL
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

<!--
Now for Steps 1–3 (Part 2).

Step 2: Copy HTTPS URL.

Terminal: PowerShell — unless step notes Git Bash or WSL.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.5 — Steps 1–3 (Part 2).

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
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
Now for Steps 1–3 (Part 3).

Step 3: Create agent with ngrok URL:.

Terminal: PowerShell — `Ctrl+ `` in Cursor.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.5 — Steps 1–3 (Part 3).

The code on the slide reads: curl -X POST https://api.cursor.com/v1/agents ... \   -d '{"webhookUrl": "https://abc123.ngrok.io/webhook/cursor", ...}'.

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

ngrok creates a public HTTPS tunnel to your laptop so Cursor can deliver webhooks to a local dev server.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.
-->

---







## Exercise 8.5 — Inspect & Replay

**Demonstration (Windows):** Agent ``Ctrl+I`` · **PowerShell** · Browser for dashboards

**Step 4:** Inspect requests at `http://127.0.0.1:4040`
**Terminal:** **PowerShell** — unless step notes Git Bash or WSL

**Step 5:** Replay failed webhooks (ngrok premium) — inspect raw body and headers
**Terminal:** **Git Bash** or **Ubuntu (WSL)** — bash syntax required

**Success Criteria:** Tunnel established · webhook received · signature verified · inspected in ngrok UI

<!--
Now for Inspect & Replay.

Step 4: Inspect requests at http://127.0.0.1:4040.

Terminal: PowerShell — unless step notes Git Bash or WSL.

Step 5: Replay failed webhooks (ngrok premium) — inspect raw body and headers.

Terminal: Git Bash or Ubuntu (WSL) — bash syntax required.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 8.5 — Inspect & Replay.

Environment note on the slide: Demonstration (Windows): Agent `Ctrl+I` · PowerShell · Browser for dashboards.

Success criteria listed: Tunnel established · webhook received · signature verified · inspected in ngrok UI.

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

ngrok creates a public HTTPS tunnel to your laptop so Cursor can deliver webhooks to a local dev server.

HTTP stands for Hypertext Transfer Protocol — the request/response protocol browsers and APIs use.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.
-->

---



<!-- _class: lead -->

# Lesson 8.6

## End-to-End Automated Agent Workflow

*Concept · 5 min · Exercise · 12 min*

<!--
Lesson 8.6: End-to-End Automated Agent Workflow. For this lesson, listen, participate, or follow along as indicated on the next slides.

The slide title is: Lesson 8.6.

You will also see the heading: End-to-End Automated Agent Workflow.

The note on screen reads: Concept · 5 min · Exercise · 12 min.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---







## The Capstone Integration

Combine everything into `automated_workflow.py`:

1. **Create agent** (with optional webhook URL)
2. **Wait for completion** (webhook or polling)
3. **Download artifacts**
4. **Process results** (CI exit codes, notifications)

<!--
Let's look at The Capstone Integration.

The slide title is: The Capstone Integration.

The slide says: Combine everything into automated_workflow.py:.

The slide says: 1. Create agent (with optional webhook URL).

The slide says: 2. Wait for completion (webhook or polling).

The slide says: 3. Download artifacts.

The slide says: 4. Process results (CI exit codes, notifications).

Number 1 on the slide: Create agent (with optional webhook URL).

Number 2 on the slide: Wait for completion (webhook or polling).

Number 3 on the slide: Download artifacts.

Number 4 on the slide: Process results (CI exit codes, notifications).

Terms on this slide — quick definitions for the room:

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.
-->

---







<!-- _class: fit-sm -->

## Workflow Architecture

<img src="assets/module-08/workflow-architecture.svg" alt="Workflow Architecture" />

<!--
This slide includes a diagram — Workflow Architecture.

The slide title is: Workflow Architecture.

The figure on this slide is titled: Workflow Architecture.
-->

---







<!-- _class: fit-xs -->

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
The slide title is: Run the Workflow.

You will also see the heading: Polling only (no webhook):.

The code on the slide reads: export CURSOR_USER_API_KEY="cursor_xxxxxxxxxxxx" python automated_workflow.py \   --repo "https://github.com/YOUR_ORG/YOUR_REPO" \   --prompt "Add a comprehensive README.md with setup and API docs" \   --output "./outputs" # Polling only (no webhook): python automated_workflow.py --repo "..." --prompt "..." --no-webhook.

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-sm -->

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
The slide title is: Workflow Output.

Success criteria listed: Creates agent · waits (webhook/polling) · downloads artifacts · end-to-end run.

The code on the slide reads: 🚀 CLOUD AGENT AUTOMATED WORKFLOW 📝 Creating agent... Agent ID: agt_abc123 ⏳ Waiting for completion... ✅ Webhook received: Agent agt_abc123 completed 📎 Downloaded 3 artifacts to agent_outputs/ ✅ WORKFLOW COMPLETE.

Terms on this slide — quick definitions for the room:

A Cloud Agent is a Cursor agent that runs on Cursor's infrastructure against a GitHub repository — you can launch it from the web UI or API.

An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.
-->

---







<!-- _header: 'Module 9 — Admin and Analytics APIs' -->

<!-- _class: lead -->

# Admin and Analytics APIs

## Module 9 · Day 2 (Hands-On + Demonstrations)

Cursor Training Program · ~75 min

<!--
Module 9 is admin and analytics — usage, spend, and models across your organization.

The slide title is: Admin and Analytics APIs.

You will also see the heading: Module 9 · Day 2 (Hands-On + Demonstrations).

The slide says: Cursor Training Program · ~75 min.
-->

---







<!-- _class: fit-md -->

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~75 minutes |
| **Format** | Hands-on exercise + demonstrations |
| **Prerequisites** | Admin API key (not User key), Python 3.8+, Modules 7–8 completed |
| **Module Goal** | Master team management, usage analytics, cost governance, and safe admin operations |

### Lessons

| Lesson | Topic | Time | Type |
|--------|-------|------|------|
| 9.1 | Listing Team Members | 13 min | Exercise |
| 9.2 | Daily Usage Data | 15 min | Exercise |
| 9.3 | Setting User Spend Limits | 13 min | Exercise |
| 9.4 | Model Usage Analytics | 13 min | Exercise |
| 9.5 | Daily Active Users | 10 min | Exercise |
| 9.6 | Leaderboards | 11 min | Exercise |
| 9.7 | Conversation Insights | 6 min | Demo |
| 9.8 | Destructive Admin Operations | 6 min | Demo |

<!--
Here is the overview for Module 9.

The slide title is: Module Overview.

The table header columns are: Aspect, Details.

In the table, **Duration**: ~75 minutes.

In the table, **Format**: Hands-on exercise + demonstrations.

In the table, **Prerequisites**: Admin API key (not User key), Python 3.8+, Modules 7–8 completed.

In the table, **Module Goal**: Master team management, usage analytics, cost governance, and safe admin operations.

Terms on this slide — quick definitions for the room:

An Admin API Key is org-wide — for team membership, usage analytics, and spend limits.
-->

---



<!-- _class: lead -->

# Lesson 9.1

## Listing Team Members

*13 min total · Concept · 5 min · Exercise · 8 min*

**Lab guide:** [`Exercise 9.1](../slide-exercises/module-09/exercise-9.1-list-team-members.md)

<!--
Lesson 9.1: Listing Team Members. For this lesson, listen, participate, or follow along as indicated on the next slides.

List team members with pagination and export to CSV.

The detailed lab guide is slide-exercises/module-09/exercise-9.1-list-team-members.md.

The slide title is: Lesson 9.1.

You will also see the heading: Listing Team Members.

The note on screen reads: 13 min total · Concept · 5 min · Exercise · 8 min.

The slide says: Lab guide: [`Exercise 9.1](../slide-exercises/module-09/exercise-9.1-list-team-members.md).
-->

---







<!-- _class: fit-sm -->

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
This slide is a table — User vs. Admin API Key.

The slide title is: User vs. Admin API Key.

The slide says: Key endpoint: GET /v1/admin/members.

In the table, **Scope** — Your user only. Use case on slide: Entire organization.

In the table, **Can list members** — ❌ No. Use case on slide: ✅ Yes.

In the table, **Can view others' usage** — ❌ No. Use case on slide: ✅ Yes.

In the table, **Can modify policies** — ❌ No. Use case on slide: ✅ Yes.

In the table, **Format** — `cursor_xxx...`. Use case on slide: `cursor_admin_xxx...`.

Terms on this slide — quick definitions for the room:

An Admin API Key is org-wide — for team membership, usage analytics, and spend limits.

A User API Key is scoped to your account — for launching agents and calling user-level endpoints.

Production API work comes down to auth, retries, caching, and verified webhooks. On Windows we use environment variables and curl.exe — details are in the lab steps on screen.
-->

---







<!-- _class: fit-sm -->

## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Agent panel** (``Ctrl+I``) is for prompts and tool use · **Chat** (``Ctrl+L``) is read-only Q&A.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

The slide title is: Windows Exercise Environment.

The slide says: All exercises in this module assume Windows 10/11 with Cursor installed.

The slide says: Agent panel (`Ctrl+I) is for prompts and tool use · Chat (Ctrl+L`) is read-only Q&A.

The slide says: Set default profile: Settings → terminal.integrated.defaultProfile.windows → PowerShell.

The table header columns are: Terminal, Use when, Open in Cursor.

In the table, **PowerShell** — Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`). Use case on slide: ``Ctrl+` `` → **PowerShell**.

In the table, **Git Bash** — Bash syntax, `export VAR=...`, shell scripts ending in `.sh`. Use case on slide: Terminal menu → **Git Bash**.

In the table, **Command Prompt** — Legacy `.bat` files only. Use case on slide: Terminal menu → **Command Prompt**.

In the table, **Ubuntu (WSL)** — Linux-only tools or native bash without Git Bash. Use case on slide: Terminal menu → **Ubuntu (WSL)**.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.

npm is the Node Package Manager — the default registry and tool for JavaScript packages.
-->

---







<!-- _class: fit-xs -->

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
We are starting Exercise 9.1 — List Team Members. We have about 13 min for this lab.

List team members with pagination and export to CSV.

The full lab guide is in slide-exercises/module-09/exercise-9.1-list-team-members.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 9.1 — Setup & List.

You will also see the heading: Verify admin access.

You will also see the heading: List all team members.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

The code on the slide reads: export CURSOR_ADMIN_API_KEY="cursor_admin_xxxxxxxxxxxx" # Verify admin access curl -s -u "$CURSOR_ADMIN_API_KEY:" \   https://api.cursor.com/v1/admin/organization | jq '.' # List all team members curl -s -u "$CURSOR_ADMIN_API_KEY:" \   "https://api.cursor.com/v1/admin/members" | jq '.'.

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-md -->

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
Now for Pagination & Export.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 9.1 — Pagination & Export.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: Pagination:.

The slide says: PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

The slide says: Python: loop with offset until empty → export to team_roster.csv (email, role, status, joined, lastActiveAt).

The slide says: Helper: get_user_id_by_email(email) for downstream admin calls.

Success criteria listed: Authenticated · listed members · handled pagination · exported CSV.

The code on the slide reads: curl -s -u "$CURSOR_ADMIN_API_KEY:" \   "https://api.cursor.com/v1/admin/members?limit=10&offset=0".

Terms on this slide — quick definitions for the room:

Pagination splits large result sets into pages — you walk them with offset and limit or cursor parameters.

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

CSV stands for Comma-Separated Values — a simple tabular export format spreadsheets and BI tools can ingest.
-->

---



<!-- _class: lead -->

# Lesson 9.2

## Daily Usage Data

*15 min total · Concept · 5 min · Exercise · 10 min*

**Lab guide:** [`Exercise 9.2](../slide-exercises/module-09/exercise-9.2-daily-usage-data.md)

<!--
Lesson 9.2: Daily Usage Data. For this lesson, listen, participate, or follow along as indicated on the next slides.

Pull daily usage and build a weekly cost report.

The detailed lab guide is slide-exercises/module-09/exercise-9.2-daily-usage-data.md.

The slide title is: Lesson 9.2.

You will also see the heading: Daily Usage Data.

The note on screen reads: 15 min total · Concept · 5 min · Exercise · 10 min.

The slide says: Lab guide: [`Exercise 9.2](../slide-exercises/module-09/exercise-9.2-daily-usage-data.md).
-->

---







## Key Endpoint

`GET /v1/admin/analytics/usage/daily`

**Returns:**
- Cost per day · Input/output token counts
- Active users per day · Breakdown by user and model (optional)

> *"Finance asks: 'What did we spend yesterday?' Engineering leads ask: 'Who's using what?'"*

<!--
This slide highlights a key quote — Key Endpoint.

The slide title is: Key Endpoint.

The slide quotes: ""Finance asks: 'What did we spend yesterday?' Engineering leads ask: 'Who's using what?'""

The slide says: GET /v1/admin/analytics/usage/daily.

The slide says: Returns:.

Bullet 1 on the slide: Cost per day · Input/output token counts.

Bullet 2 on the slide: Active users per day · Breakdown by user and model (optional).

Terms on this slide — quick definitions for the room:

Output tokens are the text the model generates — explanations and code — and they typically cost more than input.
-->

---







<!-- _class: fit-md -->

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
We are starting Exercise 9.2 — Daily Usage Data. We have about 15 min for this lab.

Pull daily usage and build a weekly cost report.

The full lab guide is in slide-exercises/module-09/exercise-9.2-daily-usage-data.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 9.2 — Weekly Usage.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

The code on the slide reads: END=$(date +%Y-%m-%d) START=$(date -d "7 days ago" +%Y-%m-%d) curl -s -u "$CURSOR_ADMIN_API_KEY:" \   "https://api.cursor.com/v1/admin/analytics/usage/daily?startDate=$START&endDate=$END" \   | jq '.daily[] | {date: .date, cost: .cost, tokens: .totalTokens, users: .activeUsers}'.

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







## Exercise 9.2 — Cost Report

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

Python `generate_cost_report()` for last 30 days:

- Total cost · total tokens · average daily cost/users
- Week-over-week change · top 5 costliest days
- Daily breakdown table (last 14 days)
- Budget alerts at $300 / $500 thresholds

**Success Criteria:** Retrieved date range · calculated trends · generated readable report

<!--
Now for Cost Report.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 9.2 — Cost Report.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The slide says: Python generate_cost_report() for last 30 days:.

Success criteria listed: Retrieved date range · calculated trends · generated readable report.

Bullet 1 on the slide: Total cost · total tokens · average daily cost/users.

Bullet 2 on the slide: Week-over-week change · top 5 costliest days.

Bullet 3 on the slide: Daily breakdown table (last 14 days).

Bullet 4 on the slide: Budget alerts at $300 / $500 thresholds.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.
-->

---



<!-- _class: lead -->

# Lesson 9.3

## Setting User Spend Limits

*13 min total · Concept · 5 min · Exercise · 8 min*

**Lab guide:** [`Exercise 9.3](../slide-exercises/module-09/exercise-9.3-set-user-spend-limits.md)

<!--
Lesson 9.3: Setting User Spend Limits. For this lesson, listen, participate, or follow along as indicated on the next slides.

Set and bulk-update per-user spending limits.

The detailed lab guide is slide-exercises/module-09/exercise-9.3-set-user-spend-limits.md.

The slide title is: Lesson 9.3.

You will also see the heading: Setting User Spend Limits.

The note on screen reads: 13 min total · Concept · 5 min · Exercise · 8 min.

The slide says: Lab guide: [`Exercise 9.3](../slide-exercises/module-09/exercise-9.3-set-user-spend-limits.md).

Terms on this slide — quick definitions for the room:

A spend limit is a monthly cap on a user's Cursor usage — can alert or block when exceeded.
-->

---







## Key Endpoint

`PATCH /v1/admin/policies/users/{userId}/limits`

| Action | Behavior |
|--------|----------|
| `alert` | Send notification but allow usage |
| `block` | Prevent any further requests for the month |

<!--
This slide is a table — Key Endpoint.

The slide title is: Key Endpoint.

The slide says: PATCH /v1/admin/policies/users/{userId}/limits.

The table header columns are: Action, Behavior.

In the table, `alert`: Send notification but allow usage.

In the table, `block`: Prevent any further requests for the month.
-->

---







<!-- _class: fit-sm -->

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
We are starting Exercise 9.3 — Set User Spend Limits. We have about 13 min for this lab.

Set and bulk-update per-user spending limits.

The full lab guide is in slide-exercises/module-09/exercise-9.3-set-user-spend-limits.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 9.3 — Set Limits.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

The slide says: Check current limit: GET .../policies/users/{userId}/limits.

The code on the slide reads: USER_ID=$(curl -s -u "$CURSOR_ADMIN_API_KEY:" \   "https://api.cursor.com/v1/admin/members?email=developer@company.com" \   | jq -r '.members[0].id') curl -X PATCH ".../policies/users/$USER_ID/limits" \   -u "$CURSOR_ADMIN_API_KEY:" \   -d '{"monthlyLimit": 50.00, "exceedanceAction": "block"}'.

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-md -->

## Exercise 9.3 — Bulk Limits

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

**CSV bulk set:** `email, monthly_limit, action`

```csv
intern@company.com,20,block
contractor@company.com,50,alert
lead@company.com,200,alert
```

**Find heavy users:** query `/analytics/usage/users` for current month → filter cost > threshold

**Success Criteria:** Retrieved user ID · set limit · verified · bulk setting implemented

<!--
Now for Bulk Limits.

Copy this into the Agent chat: "intern@company.com,20,block contractor@company.com,50,alert lead@company.com,200,alert"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 9.3 — Bulk Limits.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The slide says: CSV bulk set: email, monthly_limit, action.

The slide says: Find heavy users: query /analytics/usage/users for current month → filter cost > threshold.

Success criteria listed: Retrieved user ID · set limit · verified · bulk setting implemented.

The code on the slide reads: intern@company.com,20,block contractor@company.com,50,alert lead@company.com,200,alert.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

CSV stands for Comma-Separated Values — a simple tabular export format spreadsheets and BI tools can ingest.
-->

---



<!-- _class: lead -->

# Lesson 9.4

## Model Usage Analytics

*13 min total · Concept · 5 min · Exercise · 8 min*

**Lab guide:** [`Exercise 9.4](../slide-exercises/module-09/exercise-9.4-model-usage-analytics.md)

<!--
Lesson 9.4: Model Usage Analytics. For this lesson, listen, participate, or follow along as indicated on the next slides.

Analyze model usage and identify optimization opportunities.

The detailed lab guide is slide-exercises/module-09/exercise-9.4-model-usage-analytics.md.

The slide title is: Lesson 9.4.

You will also see the heading: Model Usage Analytics.

The note on screen reads: 13 min total · Concept · 5 min · Exercise · 8 min.

The slide says: Lab guide: [`Exercise 9.4](../slide-exercises/module-09/exercise-9.4-model-usage-analytics.md).
-->

---







## Key Endpoint

`GET /v1/admin/analytics/usage/models`

> *"Which models are actually being used? Is Opus worth the cost? Should you train people on cheaper alternatives?"*

<!--
This slide highlights a key quote — Key Endpoint.

The slide title is: Key Endpoint.

The slide quotes: ""Which models are actually being used? Is Opus worth the cost? Should you train people on cheaper alternatives?""

The slide says: GET /v1/admin/analytics/usage/models.
-->

---







<!-- _class: fit-xs -->

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
We are starting Exercise 9.4 — Model Usage Analytics. We have about 13 min for this lab.

Analyze model usage and identify optimization opportunities.

The full lab guide is in slide-exercises/module-09/exercise-9.4-model-usage-analytics.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 9.4 — Model Breakdown.

You will also see the heading: Find Opus overuse per user.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

The code on the slide reads: curl -s -u "$CURSOR_ADMIN_API_KEY:" \   ".../analytics/usage/models?startDate=$START&endDate=$END" \   | jq '.models[] | {model: .modelId, cost: .cost, requests: .requestCount}' # Find Opus overuse per user curl -s -u "$CURSOR_ADMIN_API_KEY:" \   ".../analytics/usage/users?startDate=$START&endDate=$END" \   | jq '.users[] | select(.modelBreakdown."claude-4.7-opus" != null)'.

Terms on this slide — quick definitions for the room:

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







## Exercise 9.4 — Optimization Report

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

`generate_optimization_report()`:

- Model cost breakdown (% of total)
- Users on Claude Opus → suggest Sonnet for non-critical tasks
- High Sonnet usage → suggest GPT-5.3 Codex (40% savings)
- Estimated monthly savings if guidelines applied

**Success Criteria:** Retrieved model breakdown · identified expensive users · generated recommendations

<!--
Now for Optimization Report.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 9.4 — Optimization Report.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The slide says: generate_optimization_report():.

Success criteria listed: Retrieved model breakdown · identified expensive users · generated recommendations.

Bullet 1 on the slide: Model cost breakdown (% of total).

Bullet 2 on the slide: Users on Claude Opus → suggest Sonnet for non-critical tasks.

Bullet 3 on the slide: High Sonnet usage → suggest GPT-5.3 Codex (40% savings).

Bullet 4 on the slide: Estimated monthly savings if guidelines applied.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.
-->

---



<!-- _class: lead -->

# Lesson 9.5

## Daily Active Users (DAU)

*10 min total · Concept · 4 min · Exercise · 6 min*

**Lab guide:** [`Exercise 9.5](../slide-exercises/module-09/exercise-9.5-daily-active-users-dau.md)

<!--
Lesson 9.5: Daily Active Users (DAU). For this lesson, listen, participate, or follow along as indicated on the next slides.

Report daily active users over a date range.

The detailed lab guide is slide-exercises/module-09/exercise-9.5-daily-active-users-dau.md.

The slide title is: Lesson 9.5.

You will also see the heading: Daily Active Users (DAU).

The note on screen reads: 10 min total · Concept · 4 min · Exercise · 6 min.

The slide says: Lab guide: [`Exercise 9.5](../slide-exercises/module-09/exercise-9.5-daily-active-users-dau.md).

Terms on this slide — quick definitions for the room:

DAU stands for Daily Active Users — the count of distinct people who used the product on a given day.
-->

---







## Why DAU Matters

- Track adoption after rollout
- Identify unused licenses for reallocation
- Measure impact of training sessions
- Justify renewal and expansion

**Source:** `activeUsers` field from `/admin/analytics/usage/daily`

<!--
This slide lists key points under Why DAU Matters.

The slide title is: Why DAU Matters.

The slide says: Source: activeUsers field from /admin/analytics/usage/daily.

Bullet 1 on the slide: Track adoption after rollout.

Bullet 2 on the slide: Identify unused licenses for reallocation.

Bullet 3 on the slide: Measure impact of training sessions.

Bullet 4 on the slide: Justify renewal and expansion.

Terms on this slide — quick definitions for the room:

DAU stands for Daily Active Users — the count of distinct people who used the product on a given day.
-->

---







<!-- _class: fit-sm -->

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
We are starting Exercise 9.5 — Daily Active Users (DAU). We have about 10 min for this lab.

Report daily active users over a date range.

The full lab guide is in slide-exercises/module-09/exercise-9.5-daily-active-users-dau.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 9.5 — DAU Report.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

The slide says: Python leadership report:.

Success criteria listed: Calculated DAU · adoption metrics · leadership-ready report.

Bullet 1 on the slide: Average/median/peak DAU · adoption rate (% of team).

Bullet 2 on the slide: WoW growth rate · weekly averages.

Bullet 3 on the slide: Health assessment: >80% excellent · >50% good · <30% investigate.

The code on the slide reads: curl -s -u "$CURSOR_ADMIN_API_KEY:" \   ".../analytics/usage/daily?startDate=$START&endDate=$END" \   | jq '{avg_weekly: ([.daily[-7:] | .[].activeUsers] | add / length),          peak: ([.daily[] | .activeUsers] | max)}'.

Terms on this slide — quick definitions for the room:

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

DAU stands for Daily Active Users — the count of distinct people who used the product on a given day.

WoW stands for Week over Week — comparing this week's metric to last week's.
-->

---



<!-- _class: lead -->

# Lesson 9.6

## Leaderboards

*11 min total · Concept · 5 min · Exercise · 6 min*

**Lab guide:** [`Exercise 9.6](../slide-exercises/module-09/exercise-9.6-leaderboards.md)

<!--
Lesson 9.6: Leaderboards. For this lesson, listen, participate, or follow along as indicated on the next slides.

Build leaderboards for tabs, AI lines, and agent runs.

The detailed lab guide is slide-exercises/module-09/exercise-9.6-leaderboards.md.

The slide title is: Lesson 9.6.

You will also see the heading: Leaderboards.

The note on screen reads: 11 min total · Concept · 5 min · Exercise · 6 min.

The slide says: Lab guide: [`Exercise 9.6](../slide-exercises/module-09/exercise-9.6-leaderboards.md).
-->

---







<!-- _class: fit-md -->

## Responsible Leaderboard Principles

| Principle | Implementation |
|-----------|----------------|
| **Anonymize** | Roles or anonymized names, not full emails |
| **Focus on positive metrics** | Show savings, not spending |
| **Opt-in only** | Allow users to choose public visibility |
| **Include context** | Show team size, role differences |

<!--
This slide is a table — Responsible Leaderboard Principles.

The slide title is: Responsible Leaderboard Principles.

The table header columns are: Principle, Implementation.

In the table, **Anonymize**: Roles or anonymized names, not full emails.

In the table, **Focus on positive metrics**: Show savings, not spending.

In the table, **Opt-in only**: Allow users to choose public visibility.

In the table, **Include context**: Show team size, role differences.
-->

---







<!-- _class: fit-md -->

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
We are starting Exercise 9.6 — Leaderboards. We have about 11 min for this lab.

Build leaderboards for tabs, AI lines, and agent runs.

The full lab guide is in slide-exercises/module-09/exercise-9.6-leaderboards.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 9.6 — Three Leaderboards.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: 1. Engagement leaderboard — rank by request count (anonymized emails).

The slide says: 2. Efficiency leaderboard — tokens per dollar spent.

The slide says: 3. Savings leaderboard — users who saved by choosing efficient models over Opus.

Success criteria listed: Anonymized · efficiency-focused · savings-focused leaderboards.

The code on the slide reads: def anonymize_email(email):     local = email.split('@')[0]     return local[:2] + "..." + local[-2:].

Terms on this slide — quick definitions for the room:

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---



<!-- _class: lead -->

# Lesson 9.7

## Conversation Insights

*6 min total · Concept · 6 min · Demonstration*

<!--
Lesson 9.7: Conversation Insights. For this lesson, listen, participate, or follow along as indicated on the next slides.

The slide title is: Lesson 9.7.

You will also see the heading: Conversation Insights.

The note on screen reads: 6 min total · Concept · 6 min · Demonstration.
-->

---







## What Conversation Insights Reveal

- Simple questions vs. complex refactors?
- Most common task categories
- Where users get stuck
- Which models perform best for which task types

**Endpoint:** `GET /v1/admin/analytics/conversations` (may require Enterprise plan)

<!--
This slide lists key points under What Conversation Insights Reveal.

The slide title is: What Conversation Insights Reveal.

The slide says: Endpoint: GET /v1/admin/analytics/conversations (may require Enterprise plan).

Bullet 1 on the slide: Simple questions vs. complex refactors?.

Bullet 2 on the slide: Most common task categories.

Bullet 3 on the slide: Where users get stuck.

Bullet 4 on the slide: Which models perform best for which task types.
-->

---







<!-- _class: fit-sm -->

## Demo: Intent Analysis

<img src="assets/module-09/demo-intent-analysis.svg" alt="Demo: Intent Analysis" />

<!--
I am going to demonstrate Intent Analysis live on my machine. Watch where each control appears in Cursor. I will narrate each click and keystroke as I go.

When the demo finishes, we will discuss when intent analysis belongs in production workflow and when a lighter-weight approach is enough.

The slide title is: Demo: Intent Analysis.

The figure on this slide is titled: Demo: Intent Analysis.
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
I am going to demonstrate Complexity & Categories live on my machine. Complexity distribution: Category analysis: Stuck patterns: conversations >5 min with success: false → suggest training/docs Success Criteria: Understood capabilities · intent/complexity/category tracking · stuck patterns I will narrate each click and keystroke as I go.

When the demo finishes, we will discuss when complexity & categories belongs in production workflow and when a lighter-weight approach is enough.

The slide title is: Demo: Complexity & Categories.

The slide says: Complexity distribution:.

The slide says: Category analysis:.

The slide says: Stuck patterns: conversations >5 min with success: false → suggest training/docs.

Success criteria listed: Understood capabilities · intent/complexity/category tracking · stuck patterns.

Bullet 1 on the slide: simple 45% · moderate 33% · complex 15% · architectural 7%.

Bullet 2 on the slide: backend 40% · frontend 29% · database 15% · devops 10% · security 6%.
-->

---



<!-- _class: lead -->

# Lesson 9.8

## Destructive Admin Operations

*6 min total · Concept · 6 min · Demonstration*

<!--
Lesson 9.8: Destructive Admin Operations. For this lesson, listen, participate, or follow along as indicated on the next slides.

The slide title is: Lesson 9.8.

You will also see the heading: Destructive Admin Operations.

The note on screen reads: 6 min total · Concept · 6 min · Demonstration.
-->

---







## Safe Removal Playbook

1. **Audit first** — active agents, runs, API keys
2. **Soft delete** — deactivate (no new agents; existing continue)
3. **Transfer ownership** — critical agents, webhooks
4. **Log everything** — compliance audit trail
5. **Confirm before hard delete** — GDPR/security only

<!--
Let's look at Safe Removal Playbook.

The slide title is: Safe Removal Playbook.

The slide says: 1. Audit first — active agents, runs, API keys.

The slide says: 2. Soft delete — deactivate (no new agents; existing continue).

The slide says: 3. Transfer ownership — critical agents, webhooks.

The slide says: 4. Log everything — compliance audit trail.

The slide says: 5. Confirm before hard delete — GDPR/security only.

Number 1 on the slide: Audit first — active agents, runs, API keys.

Number 2 on the slide: Soft delete — deactivate (no new agents; existing continue).

Number 3 on the slide: Transfer ownership — critical agents, webhooks.

Number 4 on the slide: Log everything — compliance audit trail.

Number 5 on the slide: Confirm before hard delete — GDPR/security only.

Terms on this slide — quick definitions for the room:

Soft delete deactivates a user account while retaining audit history — common before permanent removal.

Hard delete permanently removes a user and associated data — irreversible and compliance-sensitive.

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

GDPR is the General Data Protection Regulation — European privacy rules that affect how you store user data.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-xs -->

## Demo: SafeRemovalDemo Workflow

<img src="assets/module-09/demo-saferemovaldemo-workflow.svg" alt="Demo: SafeRemovalDemo Workflow" />

**Bulk deactivation:** find users inactive 90+ days → review → notify → deactivate

**Success Criteria:** 5-step pattern · audit-first · soft vs hard delete · resource transfer

<!--
I am going to demonstrate SafeRemovalDemo Workflow live on my machine. Bulk deactivation: find users inactive 90+ days → review → notify → deactivate Success Criteria: 5-step pattern · audit-first · soft vs hard delete · resource transfer I will narrate each click and keystroke as I go.

When the demo finishes, we will discuss when saferemovaldemo workflow belongs in production workflow and when a lighter-weight approach is enough.

The slide title is: Demo: SafeRemovalDemo Workflow.

The slide says: Bulk deactivation: find users inactive 90+ days → review → notify → deactivate.

Success criteria listed: 5-step pattern · audit-first · soft vs hard delete · resource transfer.

The figure on this slide is titled: Demo: SafeRemovalDemo Workflow.

Terms on this slide — quick definitions for the room:

Hard delete permanently removes a user and associated data — irreversible and compliance-sensitive.
-->

---







<!-- _header: 'Module 10 — AI Code Tracking and Reporting' -->

<!-- _class: lead -->

# AI Code Tracking and Reporting

## Module 10 · Day 2 (Hands-On + Take-Home Project)

Cursor Training Program · ~20 min + take-home

<!--
Module 10 closes with AI code tracking — measuring adoption and change in your codebase.

The slide title is: AI Code Tracking and Reporting.

You will also see the heading: Module 10 · Day 2 (Hands-On + Take-Home Project).

The slide says: Cursor Training Program · ~20 min + take-home.
-->

---







<!-- _class: fit-md -->

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~20 minutes (plus take-home project) |
| **Format** | Hands-on exercise + take-home project |
| **Prerequisites** | Admin API key, Git repository access, Modules 8–9 completed |
| **Module Goal** | Track AI vs. human contributions, export metrics to BI tools, build compliance dashboards |

### Lessons

| Lesson | Topic | Time |
|--------|-------|------|
| 10.1 | AI Commit Metrics | 8 min |
| 10.2 | Bulk Export via CSV Streaming | 7 min |
| 10.3 | Granular AI Change Events | 7 min |
| 10.4 | Reporting Dashboard Architecture | 4 min + take-home |

<!--
Here is the overview for Module 10.

The slide title is: Module Overview.

The table header columns are: Aspect, Details.

In the table, **Duration**: ~20 minutes (plus take-home project).

In the table, **Format**: Hands-on exercise + take-home project.

In the table, **Prerequisites**: Admin API key, Git repository access, Modules 8–9 completed.

In the table, **Module Goal**: Track AI vs. human contributions, export metrics to BI tools, build compliance dashboards.

Terms on this slide — quick definitions for the room:

An Admin API Key is org-wide — for team membership, usage analytics, and spend limits.

BI stands for Business Intelligence — dashboards and reports built from exported usage data.
-->

---



<!-- _class: lead -->

# Lesson 10.1

## AI Commit Metrics

*Concept · 3 min · Exercise · 5 min*

**Lab guide:** [`Exercise 10.1](../slide-exercises/module-10/exercise-10.1-ai-commit-metrics.md)

<!--
Lesson 10.1: AI Commit Metrics. For this lesson, listen, participate, or follow along as indicated on the next slides.

Fetch AI commit metrics and calculate contribution percentage.

The detailed lab guide is slide-exercises/module-10/exercise-10.1-ai-commit-metrics.md.

The slide title is: Lesson 10.1.

You will also see the heading: AI Commit Metrics.

The note on screen reads: Concept · 3 min · Exercise · 5 min.

The slide says: Lab guide: [`Exercise 10.1](../slide-exercises/module-10/exercise-10.1-ai-commit-metrics.md).

Terms on this slide — quick definitions for the room:

AI commit metrics track how much committed code came from AI assistance versus human-only edits.
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
This slide highlights a key quote — Key Endpoint.

The slide title is: Key Endpoint.

The slide quotes: ""The 'ROI of AI' metric — how much code was AI-generated vs. human-written.""

The slide says: GET /v1/admin/analytics/commits.

The slide says: What this measures:.

Bullet 1 on the slide: Lines added by AI vs. human.

Bullet 2 on the slide: Files modified by agent vs. manual.

Bullet 3 on the slide: Commit-level attribution · Per-developer breakdown.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

ROI stands for Return on Investment — whether tool spend pays back in saved time or shipped work.
-->

---







<!-- _class: fit-sm -->

## Windows Exercise Environment

All exercises in this module assume **Windows 10/11** with Cursor installed.

| Terminal | Use when | Open in Cursor |
|----------|----------|----------------|
| **PowerShell** | Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`) | ``Ctrl+` `` → **PowerShell** |
| **Git Bash** | Bash syntax, `export VAR=...`, shell scripts ending in `.sh` | Terminal menu → **Git Bash** |
| **Command Prompt** | Legacy `.bat` files only | Terminal menu → **Command Prompt** |
| **Ubuntu (WSL)** | Linux-only tools or native bash without Git Bash | Terminal menu → **Ubuntu (WSL)** |

**Agent panel** (``Ctrl+I``) is for prompts and tool use · **Chat** (``Ctrl+L``) is read-only Q&A.

**Set default profile:** Settings → `terminal.integrated.defaultProfile.windows` → **PowerShell**

<!--
Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.

For API exercises, set your keys in the session, for example `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.

On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.

Once your test call succeeds, give me a thumbs-up and we will continue.

The slide title is: Windows Exercise Environment.

The slide says: All exercises in this module assume Windows 10/11 with Cursor installed.

The slide says: Agent panel (`Ctrl+I) is for prompts and tool use · Chat (Ctrl+L`) is read-only Q&A.

The slide says: Set default profile: Settings → terminal.integrated.defaultProfile.windows → PowerShell.

The table header columns are: Terminal, Use when, Open in Cursor.

In the table, **PowerShell** — Default — Python, Git, `curl.exe`, npm, Cursor CLI (`agent`). Use case on slide: ``Ctrl+` `` → **PowerShell**.

In the table, **Git Bash** — Bash syntax, `export VAR=...`, shell scripts ending in `.sh`. Use case on slide: Terminal menu → **Git Bash**.

In the table, **Command Prompt** — Legacy `.bat` files only. Use case on slide: Terminal menu → **Command Prompt**.

In the table, **Ubuntu (WSL)** — Linux-only tools or native bash without Git Bash. Use case on slide: Terminal menu → **Ubuntu (WSL)**.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.

WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.

npm is the Node Package Manager — the default registry and tool for JavaScript packages.
-->

---







<!-- _class: fit-md -->

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
We are starting Exercise 10.1 — AI Commit Metrics. We have about 8 min for this lab.

Fetch AI commit metrics and calculate contribution percentage.

The full lab guide is in slide-exercises/module-10/exercise-10.1-ai-commit-metrics.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 10.1 — Fetch Metrics.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

The code on the slide reads: END=$(date +%Y-%m-%d) START=$(date -d "30 days ago" +%Y-%m-%d) curl -s -u "$CURSOR_ADMIN_API_KEY:" \   ".../analytics/commits?startDate=$START&endDate=$END&repo=https://github.com/YOUR_ORG/YOUR_REPO" \   | jq '.'.

Terms on this slide — quick definitions for the room:

HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-xs -->

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
Now for AI Contribution %.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 10.1 — AI Contribution %.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

The code on the slide reads: curl -s -u "$CURSOR_ADMIN_API_KEY:" \   ".../analytics/commits?startDate=$START&endDate=$END" \   | jq '{       total_commits: .summary.totalCommits,       ai_commits: .summary.aiAuthoredCommits,       ai_percentage: (.summary.aiAuthoredCommits / .summary.totalCommits * 100),       lines_saved: .summary.aiGeneratedLines     }'.

Terms on this slide — quick definitions for the room:

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







<!-- _class: fit-md -->

## Exercise 10.1 — ROI Analysis

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

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
Now for ROI Analysis.

Copy this into the Agent chat: "AI-generated lines vs. human-written lines (%) Estimated time saved (10 lines/min assumption) Estimated cost saved ($100/hr developer cost) AI usage cost → Net ROI"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 10.1 — ROI Analysis.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The slide says: Python calculate_ai_roi():.

The slide says: contributor_breakdown() — AI %, AI lines, commits per developer.

Success criteria listed: Retrieved metrics · calculated AI % · generated ROI analysis.

The code on the slide reads: AI-generated lines vs. human-written lines (%) Estimated time saved (10 lines/min assumption) Estimated cost saved ($100/hr developer cost) AI usage cost → Net ROI.

Terms on this slide — quick definitions for the room:

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

ROI stands for Return on Investment — whether tool spend pays back in saved time or shipped work.
-->

---



<!-- _class: lead -->

# Lesson 10.2

## Bulk Export via CSV Streaming

*Concept · 3 min · Exercise · 4 min*

**Lab guide:** [`Exercise 10.2](../slide-exercises/module-10/exercise-10.2-bulk-export-via-csv-streaming.md)

<!--
Lesson 10.2: Bulk Export via CSV Streaming. For this lesson, listen, participate, or follow along as indicated on the next slides.

Stream large CSV exports for BI tools.

The detailed lab guide is slide-exercises/module-10/exercise-10.2-bulk-export-via-csv-streaming.md.

The slide title is: Lesson 10.2.

You will also see the heading: Bulk Export via CSV Streaming.

The note on screen reads: Concept · 3 min · Exercise · 4 min.

The slide says: Lab guide: [`Exercise 10.2](../slide-exercises/module-10/exercise-10.2-bulk-export-via-csv-streaming.md).

Terms on this slide — quick definitions for the room:

Streaming means events arrive incrementally over SSE instead of waiting for one complete response at the end.

CSV stands for Comma-Separated Values — a simple tabular export format spreadsheets and BI tools can ingest.
-->

---







## Key Endpoint

`GET /v1/admin/analytics/export/csv` (streaming)

> *"Wire metrics into BI tools (Tableau, PowerBI, Looker, Metabase) without timeouts."*

**Export types:** `commits` · `events` · `usage`

<!--
This slide highlights a key quote — Key Endpoint.

The slide title is: Key Endpoint.

The slide quotes: ""Wire metrics into BI tools (Tableau, PowerBI, Looker, Metabase) without timeouts.""

The slide says: GET /v1/admin/analytics/export/csv (streaming).

The slide says: Export types: commits · events · usage.

Terms on this slide — quick definitions for the room:

Streaming means events arrive incrementally over SSE instead of waiting for one complete response at the end.

CSV stands for Comma-Separated Values — a simple tabular export format spreadsheets and BI tools can ingest.

BI stands for Business Intelligence — dashboards and reports built from exported usage data.
-->

---







<!-- _class: fit-md -->

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
We are starting Exercise 10.2 — Bulk Export via CSV Streaming. We have about 7 min for this lab.

Stream large CSV exports for BI tools.

The full lab guide is in slide-exercises/module-10/exercise-10.2-bulk-export-via-csv-streaming.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 10.2 — Stream to File.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

The code on the slide reads: curl -N -u "$CURSOR_ADMIN_API_KEY:" \   ".../analytics/export/csv?startDate=$START&endDate=$END&type=commits" \   -o cursor_commits_export.csv head -10 cursor_commits_export.csv.

Terms on this slide — quick definitions for the room:

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

CSV stands for Comma-Separated Values — a simple tabular export format spreadsheets and BI tools can ingest.
-->

---







<!-- _class: fit-md -->

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
Now for BI Integration.

Copy this into the Agent chat: "export_for_bi(): bi_commits.csv # commit data bi_events.csv # event data bi_usage.csv # usage data"

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 10.2 — BI Integration.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: Python stream_to_dataframe() → pandas DataFrame:.

The slide says: Upload to Metabase, PowerBI, or Tableau via CSV import.

Success criteria listed: Streamed CSV · loaded into DataFrame · created BI-ready files.

The code on the slide reads: export_for_bi():   bi_commits.csv   # commit data   bi_events.csv    # event data   bi_usage.csv     # usage data.

Terms on this slide — quick definitions for the room:

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

CSV stands for Comma-Separated Values — a simple tabular export format spreadsheets and BI tools can ingest.

BI stands for Business Intelligence — dashboards and reports built from exported usage data.
-->

---



<!-- _class: lead -->

# Lesson 10.3

## Granular AI Change Events

*Concept · 3 min · Exercise · 4 min*

**Lab guide:** [`Exercise 10.3](../slide-exercises/module-10/exercise-10.3-granular-ai-change-events.md)

<!--
Lesson 10.3: Granular AI Change Events. For this lesson, listen, participate, or follow along as indicated on the next slides.

Query per-change AI events for compliance reporting.

The detailed lab guide is slide-exercises/module-10/exercise-10.3-granular-ai-change-events.md.

The slide title is: Lesson 10.3.

You will also see the heading: Granular AI Change Events.

The note on screen reads: Concept · 3 min · Exercise · 4 min.

The slide says: Lab guide: [`Exercise 10.3](../slide-exercises/module-10/exercise-10.3-granular-ai-change-events.md).
-->

---







## Key Endpoint

`GET /v1/admin/analytics/events`

**Tracks per event:**
- File, line range, model used, timestamp
- User, accepted/rejected status

> *"Essential for SOC2, ISO, and internal audits."*

<!--
This slide highlights a key quote — Key Endpoint.

The slide title is: Key Endpoint.

The slide quotes: ""Essential for SOC2, ISO, and internal audits.""

The slide says: GET /v1/admin/analytics/events.

The slide says: Tracks per event:.

Bullet 1 on the slide: File, line range, model used, timestamp.

Bullet 2 on the slide: User, accepted/rejected status.

Terms on this slide — quick definitions for the room:

SOC2 is Service Organization Control 2 — a common security and compliance audit framework for SaaS vendors.

ISO refers to International Organization for Standardization frameworks — audit and compliance standards many enterprises require.
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
We are starting Exercise 10.3 — Granular AI Change Events. We have about 7 min for this lab.

Query per-change AI events for compliance reporting.

The full lab guide is in slide-exercises/module-10/exercise-10.3-granular-ai-change-events.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 10.3 — Query Events.

Environment note on the slide: Platform: Windows 10/11 · PowerShell for API · $env:VAR · curl.exe.

The slide says: PowerShell (Windows): Same steps in PowerShell — use $env:NAME = "value" instead of export, and curl.exe instead of curl.

The slide says: Acceptance rate by model: group events → total vs. accepted per model.

The code on the slide reads: curl -s -u "$CURSOR_ADMIN_API_KEY:" \   ".../analytics/events?startDate=$START&endDate=$END&limit=100" \   | jq '.events[] | {user: .user.email, file: .filePath, model: .modelId, accepted: .accepted}'.

Terms on this slide — quick definitions for the room:

Acceptance rate is the share of AI-suggested edits a developer accepted versus rejected.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.
-->

---







## Exercise 10.3 — Compliance Report

**Demonstration (Windows):** **PowerShell** terminal (``Ctrl+` ``) · Agent panel ``Ctrl+I`` · shortcuts use **Ctrl**

`generate_compliance_report()` for last 90 days:

- Acceptance rate by model (table)
- Top 10 files with most AI changes (needs review)
- Export `compliance_export.csv` for auditors:
  - timestamp, user_email, model_id, file_path, line_start, line_end, accepted

**Success Criteria:** Retrieved events · calculated acceptance rates · compliance export

<!--
Now for Compliance Report.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 10.3 — Compliance Report.

Environment note on the slide: Demonstration (Windows): PowerShell terminal (`Ctrl+ `) · Agent panel Ctrl+I` · shortcuts use Ctrl.

The slide says: generate_compliance_report() for last 90 days:.

Success criteria listed: Retrieved events · calculated acceptance rates · compliance export.

Bullet 1 on the slide: Acceptance rate by model (table).

Bullet 2 on the slide: Top 10 files with most AI changes (needs review).

Bullet 3 on the slide: Export compliance_export.csv for auditors:.

Bullet 4 on the slide: timestamp, user_email, model_id, file_path, line_start, line_end, accepted.

Terms on this slide — quick definitions for the room:

Acceptance rate is the share of AI-suggested edits a developer accepted versus rejected.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

CSV stands for Comma-Separated Values — a simple tabular export format spreadsheets and BI tools can ingest.
-->

---



<!-- _class: lead -->

# Lesson 10.4

## Reporting Dashboard Architecture

*Concept · 4 min · Take-Home Project*

**Lab guide:** [`Exercise 10.4](../slide-exercises/module-10/exercise-10.4-reporting-dashboard-architecture.md)

**Lab guide:** [`Exercise 10.4`](../slide-exercises/module-10/exercise-10.4-reporting-dashboard-architecture.md)

<!--
Lesson 10.4: Reporting Dashboard Architecture. For this lesson, listen, participate, or follow along as indicated on the next slides.

Design a leadership dashboard combining analytics APIs.

The detailed lab guide is slide-exercises/module-10/exercise-10.4-reporting-dashboard-architecture.md.

The slide title is: Lesson 10.4.

You will also see the heading: Reporting Dashboard Architecture.

The note on screen reads: Concept · 4 min · Take-Home Project.

The slide says: Lab guide: [`Exercise 10.4](../slide-exercises/module-10/exercise-10.4-reporting-dashboard-architecture.md).

The slide says: Lab guide: [Exercise 10.4](../slide-exercises/module-10/exercise-10.4-reporting-dashboard-architecture.md).
-->

---







<!-- _class: fit-md -->

## Exercise 10.4 — Dashboard Components

| Component | Data Source | Purpose |
|-----------|-------------|---------|
| Usage Overview | Usage API | Cost, tokens, active users |
| AI Contribution | Commits API | ROI, adoption metrics |
| Model Performance | Events API | Acceptance rates, efficiency |
| Team Activity | Members API | Onboarding, licensing |
| Compliance | Events + Audit | Audit trail, security |
<!--
We are starting Exercise 10.4 — Reporting Dashboard Architecture. We have about Take-home for this lab.

Design a leadership dashboard combining analytics APIs.

The full lab guide is in slide-exercises/module-10/exercise-10.4-reporting-dashboard-architecture.md if you need extra detail.

On Windows: PowerShell in the integrated terminal — Ctrl+backtick — and the Agent panel — Ctrl+I. Open the repo folder with File → Open Folder.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 10.4 — Dashboard Components.

The table header columns are: Component, Data Source, Purpose.

In the table, Usage Overview — Usage API. Use case on slide: Cost, tokens, active users.

In the table, AI Contribution — Commits API. Use case on slide: ROI, adoption metrics.

In the table, Model Performance — Events API. Use case on slide: Acceptance rates, efficiency.

In the table, Team Activity — Members API. Use case on slide: Onboarding, licensing.

In the table, Compliance — Events + Audit. Use case on slide: Audit trail, security.

Terms on this slide — quick definitions for the room:

A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.

API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.

ROI stands for Return on Investment — whether tool spend pays back in saved time or shipped work.
-->

---







## Exercise 10.4 — Streamlit Dashboard

Run with: `streamlit run cursor_dashboard.py`

**5 panels:**
1. **Executive Summary** — cost, DAU, AI %, team size
2. **Usage Analytics** — daily cost trend (Plotly line chart)
3. **AI Code Impact** — AI vs human bar chart + acceptance by model
4. **Team Management** — member table
5. **Compliance Export** — download events CSV

<!--
Now for Streamlit Dashboard.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 10.4 — Streamlit Dashboard.

The slide says: Run with: streamlit run cursor_dashboard.py.

The slide says: 5 panels:.

The slide says: 1. Executive Summary — cost, DAU, AI %, team size.

The slide says: 2. Usage Analytics — daily cost trend (Plotly line chart).

The slide says: 3. AI Code Impact — AI vs human bar chart + acceptance by model.

The slide says: 4. Team Management — member table.

The slide says: 5. Compliance Export — download events CSV.

Number 1 on the slide: Executive Summary — cost, DAU, AI %, team size.

Number 2 on the slide: Usage Analytics — daily cost trend (Plotly line chart).

Number 3 on the slide: AI Code Impact — AI vs human bar chart + acceptance by model.

Number 4 on the slide: Team Management — member table.

Number 5 on the slide: Compliance Export — download events CSV.

Terms on this slide — quick definitions for the room:

DAU stands for Daily Active Users — the count of distinct people who used the product on a given day.

CSV stands for Comma-Separated Values — a simple tabular export format spreadsheets and BI tools can ingest.
-->

---







<!-- _class: fit-md -->

## Exercise 10.4 — Deliverables

| Deliverable | Description |
|-------------|-------------|
| **Working dashboard** | Streamlit, Metabase, or custom frontend |
| **Documentation** | Setup instructions and data source descriptions |
| **One insight** | Key finding from your team's data |
| **Export script** | Automated CSV export for compliance |

**Bonus:** cost alerts · spend limit UI · model A/B comparison · cloud deployment

<!--
Now for Deliverables.

I'll give you a few minutes to work — raise your hand if you get stuck.

The slide title is: Exercise 10.4 — Deliverables.

The slide says: Bonus: cost alerts · spend limit UI · model A/B comparison · cloud deployment.

The table header columns are: Deliverable, Description.

In the table, **Working dashboard**: Streamlit, Metabase, or custom frontend.

In the table, **Documentation**: Setup instructions and data source descriptions.

In the table, **One insight**: Key finding from your team's data.

In the table, **Export script**: Automated CSV export for compliance.

Terms on this slide — quick definitions for the room:

A spend limit is a monthly cap on a user's Cursor usage — can alert or block when exceeded.

CSV stands for Comma-Separated Values — a simple tabular export format spreadsheets and BI tools can ingest.
-->

---







<!-- _header: "" -->
<!-- _class: lead fit-sm -->

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
This slide lists key points under Course Complete.

The slide title is: Course Complete.

You will also see the heading: Cursor Training Program — Day 2.

The note on screen reads: End of Module 10 — End of Day 2 Training Program.

The slide says: You can now:.

The slide says: Next steps: Complete take-home dashboard · set up scheduled exports · implement cost alerts.

Bullet 1 on the slide: Create and manage Cloud Agents programmatically.

Bullet 2 on the slide: Stream agent responses with SSE · Webhooks with HMAC verification.

Bullet 3 on the slide: Administer teams and enforce spending policies.

Bullet 4 on the slide: Analyze usage, model adoption, and AI contribution.

Bullet 5 on the slide: Track AI vs. human code changes per commit.

Bullet 6 on the slide: Build reporting dashboards for leadership.

Terms on this slide — quick definitions for the room:

A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.

In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.

HMAC stands for Hash-based Message Authentication Code — a signed digest that proves a webhook payload was not tampered with.

SSE stands for Server-Sent Events — a way the server pushes live updates over one long HTTP connection.
-->
