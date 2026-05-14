# AI Foundations – Tokens & Pricing

## Complete Beginner's Guide

This document explains the **Tokens & Pricing** lesson from Cursor Learn. It covers how AI models measure input/output, how pricing works, and how streaming responses function.

Let me break this down for a complete beginner.

---

## What Are Tokens? (The 10-Second Summary)

**Tokens are like the "words" that AI models actually understand.** But they're not quite the same as human words – models break text into smaller chunks called tokens.

| Human Understanding | AI Understanding |
|--------------------|------------------|
| Words and sentences | Tokens (word pieces) |
| "Hello world" = 2 words | "Hello world" = 2 tokens |
| "Understanding" = 1 word | "Understanding" = 3 tokens (under, stand, ing) |

> *"Just like how your computer doesn't actually understand the letter 'A' but instead works with binary code (1s and 0s), AI models don't work directly with words."*

---

## How Tokenization Works

### Examples:

| Text | How It Might Tokenize |
|------|----------------------|
| "hello" | 1 token |
| "world" | 1 token |
| "understanding" | 3 tokens (under + stand + ing) |
| "I'm" | 2 tokens (I + 'm) |
| "https://cursor.com" | Multiple tokens |
| " " (space) | Sometimes its own token |

> *"Sometimes even parts of words, punctuation, or spaces become their own tokens."*

---

## Why Tokens Matter (2 Reasons)

| Reason | Explanation |
|--------|-------------|
| **Pricing** | You pay per token, not per word or character |
| **Speed** | Models measured by TPS (Tokens Per Second) |

> *"If we keep the analogy going that AI models are like APIs, then tokens are the units we use to measure and charge for input and output traffic."*

---

## Two Types of Tokens

| Token Type | What It Includes | Cost Comparison |
|------------|------------------|-----------------|
| **Input Tokens** | Your prompt + previous conversation | Lower cost (baseline) |
| **Output Tokens** | Everything the model generates | 2-4x more expensive |

> *"Output tokens typically cost 2-4x more than input tokens, because generating new content requires more computational work than just processing what you sent."*

### Why Output Costs More:

| Input Processing | Output Generation |
|------------------|-------------------|
| Read and understand | Create new content |
| Less computation | More computation |
| Cheaper | More expensive |

---

## Token Pricing Analogy

| Analogy | Explanation |
|---------|-------------|
| **API calls** | Tokens = units of measurement |
| **Server costs** | You pay for what you use |
| **Intentional usage** | Be mindful of how much you send |

> *"Think of it like knowing what your server costs are. You'll want to be intentional about how much information you include."*

---

## Streaming Responses

### How AI Models Generate Text:

```
Token 1 → Token 2 → Token 3 → Token 4 → ... → Complete Response
```

Models generate tokens **one at a time**, in sequence. They predict the next token, then use that prediction to predict the next one.

> *"AI models generate tokens one at a time, in sequence. They predict the next token, then use that prediction to help predict the next token after that, and so on."*

### Why Streaming Matters:

| Without Streaming | With Streaming |
|------------------|----------------|
| Wait for entire response | See tokens as they're generated |
| Can't interrupt | Can stop model if it goes off track |
| Long wait for long responses | Immediate feedback |

> *"This is great because you don't have to wait for the entire response to finish, which could take minutes, and you can interrupt the model if it starts to go off track."*

---

## Interactive Quiz

The course includes this quiz question:

> *"Which statement about streaming is correct?"*

| Option | Correct? | Why |
|--------|----------|-----|
| Streaming is purely a UI trick; models generate the full text instantly | ❌ No | Models actually generate token by token |
| **Models generate tokens one by one and can stream partial outputs** | ✅ **Yes** | This is how streaming actually works |
| Streaming reduces output token costs | ❌ No | Same number of tokens, just delivered faster |
| Streaming disables interruptions | ❌ No | Streaming enables interruptions |

---

## Optimizing Token Usage

AI tools use techniques to reduce token usage:

| Technique | Description |
|-----------|-------------|
| **Caching** | Automatically cache parts of your prompt used repeatedly |
| **Context management** | Help you manage included information |
| **Concise responses** | Steer model toward shorter outputs |

> *"AI tools often use techniques to reduce the number of tokens sent to the underlying models. For example, automatically caching parts of your prompt that you use repeatedly."*

---

## Practical Tips for Engineers

| Tip | Why It Matters |
|-----|----------------|
| **Be concise in prompts** | Fewer input tokens = lower cost |
| **Request concise responses** | Fewer output tokens = lower cost |
| **Use caching when possible** | Reuse repeated context |
| **Monitor token usage** | Understand your costs |
| **Interrupt off-track responses** | Save tokens by stopping early |

---

## Token Costs in Cursor

| Model | Input Cost (per 1M tokens) | Output Cost (per 1M tokens) |
|-------|---------------------------|----------------------------|
| GPT-5 Mini | $0.25 | $2.00 |
| Composer 2 | $0.50 | $2.50 |
| GPT-5.3 Codex | $1.75 | $14.00 |
| Claude 4.6 Sonnet | $3.00 | $15.00 |
| Claude 4.7 Opus | $5.00 | $25.00 |

> *"Output tokens typically cost 2-4x more than input tokens."*

---

## Key Takeaways for Engineers

| Takeaway | Action |
|----------|--------|
| **Tokens ≠ words** | Be aware of tokenization |
| **Output costs more** | Request concise responses |
| **Streaming enables interruption** | Stop off-track responses early |
| **Caching saves money** | Reuse repeated context |
| **Measure in tokens** | Not characters or words |

---

## Connection to Your Training

| Concept | How to Apply |
|---------|--------------|
| **Token counting** | Show examples of tokenization |
| **Pricing awareness** | Engineers understand costs |
| **Streaming** | Use Cursor's streaming responses |
| **Optimization** | Teach concise prompting |

---

## Summary

| Question | Answer |
|----------|--------|
| **What are tokens?** | The units AI models understand (word pieces) |
| **Two token types?** | Input (cheaper) and Output (2-4x more expensive) |
| **What is TPS?** | Tokens Per Second (measure of speed) |
| **How does streaming work?** | Tokens generated one at a time |
| **Why stream?** | See partial results, interrupt if needed |

---

## The Bottom Line

**Tokens are the currency of AI – you pay for them, and speed is measured by them.**

**Think of it as:**
- **Input tokens** = What you say 📝
- **Output tokens** = What AI says back 💬
- **Streaming** = Watching AI type in real-time ⌨️

**For your engineers:**
- Output costs 2-4x more than input – request concise responses
- Streaming enables interruption – use it to save tokens
- Monitor token usage to manage costs
- Caching can reduce repeated token costs
