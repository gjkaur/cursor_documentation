# Module 1: Mental Models for AI-Assisted Development

## Cursor Training Program — Day 1

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Concept block (no hands-on exercises) |
| **Prerequisites** | None |
| **Module Goal** | Build correct mental models for how AI works, why it behaves unpredictably, and how to use it effectively as an engineering tool |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Explain why AI model outputs are probabilistic, not deterministic
- Identify hallucinations in AI-generated code and responses
- Understand how tokens work and how pricing is calculated
- Describe what context is and why it's the most important skill in AI-assisted development
- Explain how tool calling and MCP extend AI capabilities
- Define what an agent is and how it changes the developer's role

---

## Lesson 1.1: How AI Models Work

### The Core Mental Model

> *"Think of AI models like super intelligent, general purpose API endpoints. Just like you would integrate Stripe for payments or Twilio for messages, you can call an AI model to solve a variety of tasks."*

**The biggest difference:** You are not guaranteed to get the same results every time.

### Deterministic vs. Probabilistic

| Traditional Software (Deterministic) | AI Models (Probabilistic) |
|--------------------------------------|---------------------------|
| Given same input → same output | Given same input → different possible outputs |
| Explicitly programmed | Learned from training data |
| Predictable results | Results vary |
| Example: `add(2,3)` always returns `5` | Example: "What is 2+3?" → "5", "Five", "The sum is 5" |

> *"There are many different paths the model might take given the same input."*

### What Determines AI Output?

AI models predict the next chunk of text based on two things:

| Factor | Description | Example |
|--------|-------------|---------|
| **Training Data** | Information the model was trained on | All code, documentation, and text on the internet |
| **Prompt** | What you provide as input | "Write a function to sort an array" |

```
AI Output = f(Training Data + Prompt)
```

### Key Insight for Engineers

> *"The first piece of your AI mental model is to never assume you are guaranteed to get the same answer every time."*

**Implications for daily work:**
- Always review AI-generated code before accepting
- Same prompt may yield different results on different days
- Model updates can change behavior

---

## Lesson 1.2: Hallucinations

### What Is Hallucination?

> *"Hallucination is when an AI model confidently generates information that seems plausible but is actually incorrect. It's like when someone tries to bluff their way through a conversation about a topic they don't really know."*

| Not Hallucination | Hallucination |
|-------------------|---------------|
| "I don't know" | "Here's a detailed (but wrong) answer" |
| Admits uncertainty | Confidently wrong |

### Why Do Models Hallucinate?

> *"When an AI model doesn't know something, it doesn't always say 'I don't know.' Instead, it generates what seems most likely based on patterns it has seen."*

### Common Coding Hallucinations

| Type | Example |
|------|---------|
| **Invented API methods** | `df.remove_outliers(threshold=3)` — pandas doesn't have this |
| **Wrong imports** | `import { debounce } from "react"` — debounce is from lodash |
| **Invalid configuration** | `"browser": true` in package.json — not a valid field |
| **Mixed syntax** | React syntax in a Vue project |

### The Knowledge Cutoff

> *"AI models are trained up until a date called the 'knowledge cutoff.' Models may suggest incorrect solutions if you ask about libraries created after this date."*

### The Verification Mindset

> *"The key to working effectively with AI is developing a verification mindset. Every suggestion is a starting point, not a final answer."*

| Without Verification | With Verification |
|---------------------|-------------------|
| Copy/paste → doesn't work → frustration | Verify in docs → test → refine → works |

### How to Spot Hallucinations

| Red Flag | What to Check |
|----------|---------------|
| Method seems plausible but unfamiliar | Check official documentation |
| Import from unexpected package | Verify package exports that method |
| Configuration looks "almost right" | Check config schema |
| Library created after knowledge cutoff | Be extra skeptical |

---

## Lesson 1.3: Tokens and Pricing

### What Are Tokens?

> *"Tokens are like the 'words' that AI models actually understand. But they're not quite the same as the words you and I would use."*

| Human Understanding | AI Understanding |
|--------------------|------------------|
| "hello" = 1 word | "hello" = 1 token |
| "understanding" = 1 word | "understanding" = 3 tokens (under + stand + ing) |
| "I'm" = 1 word (contraction) | "I'm" = 2 tokens (I + 'm) |

### Why Tokens Matter (2 Reasons)

| Reason | Explanation |
|--------|-------------|
| **Pricing** | You pay per token, not per word or character |
| **Speed** | Models measured by TPS (Tokens Per Second) |

### Two Types of Tokens

| Token Type | What It Includes | Cost |
|------------|------------------|------|
| **Input Tokens** | Your prompt + previous conversation | Lower cost (baseline) |
| **Output Tokens** | Everything the model generates | 2-4x more expensive |

> *"Output tokens typically cost 2-4x more than input tokens, because generating new content requires more computational work than just processing what you sent."*

### Streaming Responses

> *"AI models generate tokens one at a time, in sequence. They predict the next token, then use that prediction to help predict the next token after that."*

| Without Streaming | With Streaming |
|------------------|----------------|
| Wait for entire response | See tokens as they're generated |
| Can't interrupt | Can stop model if it goes off track |

### Pricing Examples (Cursor)

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|-------|----------------------|----------------------|
| GPT-5 Mini | $0.25 | $2.00 |
| Composer 2 | $0.50 | $2.50 |
| GPT-5.3 Codex | $1.75 | $14.00 |
| Claude 4.6 Sonnet | $3.00 | $15.00 |
| Claude 4.7 Opus | $5.00 | $25.00 |

### Practical Tips for Engineers

| Tip | Why |
|-----|-----|
| Be concise in prompts | Fewer input tokens = lower cost |
| Request concise responses | Fewer output tokens = lower cost |
| Use caching when possible | Reuse repeated context |
| Interrupt off-track responses | Save tokens by stopping early |

---

## Lesson 1.4: Context

### The Big Insight

> *"You might think to improve the model output you need to write better prompts. But it's missing the bigger point: working with AI models is all about managing the context you provide them."*

### What Is Context?

**Context is the AI's working memory** — everything it can "see" and "remember" when generating a response.

| Context Includes | Description |
|-----------------|-------------|
| System prompt | Instructions from tool creator |
| User messages | Your prompts and questions |
| Model outputs | Previous AI responses |
| Attached files | Code files, documentation |
| Tool outputs | Terminal errors, linter results |
| Conversation history | All previous turns |

### System vs. User Prompts

| Prompt Type | Who Sets It | Purpose |
|-------------|-------------|---------|
| **System Prompt** | Tool creator (e.g., Cursor) | Inject instructions or style |
| **User Prompt** | You | Give directions to the model |

### Context Window Growth

```
Start: [System Prompt]
Turn 1: [User] + [AI Response]
Turn 2: [User] + [AI Response]
Turn 3: [User] + [AI Response]
...
Context gets longer and longer
```

### Context Limits

Every AI model has a **context limit** — maximum tokens it can process.

| Model | Context Limit |
|-------|---------------|
| Smaller models | 200K tokens |
| Larger models (Max Mode) | 1M tokens |

### What Happens at the Limit

| Consequence | Description |
|-------------|-------------|
| Can't accept more messages | Conversation stops |
| Old messages forgotten | Model loses earlier context |
| Need compression | Summarize to stay under limit |

> *"Just like if you were having a conversation with a human, there's only so much context you can keep in your brain at one time."*

---

## Lesson 1.5: Tool Calling and MCP

### What Is Tool Calling?

> *"Tool calling is giving AI models the ability to call other APIs themselves. It's as if the AI model can learn new skills."*

| Without Tool Calling | With Tool Calling |
|---------------------|-------------------|
| Model only generates text | Model can take actions |
| Limited to provided context | Can fetch real-time information |
| Cannot interact with external systems | Can read files, search web, run commands |

### The Cooking Analogy

| Without Tool Calling | With Tool Calling |
|---------------------|-------------------|
| Can't see what's in the fridge | Friend sends photo of fridge → better advice |
| Can't taste the food | Friend describes taste → adjust seasoning |

### How Tool Calling Works

| Step | What Happens |
|------|--------------|
| 1 | Model recognizes it needs additional capabilities |
| 2 | Model formats JSON specifying which tool to use |
| 3 | Application runs that tool and returns results |
| 4 | Model incorporates results into context and continues |

### The Three Components of Every Tool

| Component | Description | Example |
|-----------|-------------|---------|
| **Name** | Identifies the tool | `read_file` |
| **Description** | Tells model when/how to use it | "Read the contents of a file" |
| **Parameters** | Inputs the tool needs | `{"filepath": "src/main.c"}` |

### Why Tools Matter for Coding

| Tool Capability | What It Does |
|-----------------|--------------|
| Read and write files | Modify your codebase |
| Search through code | Find relevant functions or patterns |
| Run shell commands | Test code, install packages |
| Access documentation | Get current information |
| Check for errors | Run linters or tests |

> *"Without tools, the AI model would be limited to only the information you explicitly provide. With tools, it can actively explore and interact with your codebase."*

### The Cost of Tools

| Token Type | What It Includes |
|------------|------------------|
| **Tool definitions (input)** | Added to every request (hundreds of tokens) |
| **Tool results (output)** | Varies based on what the tool returns |

### MCP (Model Context Protocol)

> *"MCP is a universal standard for connecting tools to AI models. Just like USB became a standard for connecting devices to computers, MCP aims to be a standard for connecting tools to AI models."*

| Integration | What Agent Can Do |
|-------------|-------------------|
| Figma | Pull design tokens, component specs |
| Linear | View and manage issues |
| Sentry | Look up error details |
| Databases | Query data directly |
| Slack | Read messages, post updates |

---

## Lesson 1.6: Agents

### What Is an Agent?

> *"At its core, an agent is simply tools in a loop."*

| Without Agent | With Agent |
|---------------|------------|
| You give turn-by-turn directions | You give the destination |
| You plan each step | Agent figures out the plan |
| You execute each action | Agent executes autonomously |

> *"It's the difference between giving someone turn-by-turn directions versus just telling them the destination and letting them use GPS."*

### How an Agent Works (Example)

**Request:** "Add a dark mode toggle to my settings page."

| Step | Action | Tool Used |
|------|--------|-----------|
| 1 | Search codebase for settings page | Semantic search |
| 2 | Read relevant files | Read files |
| 3 | Create a plan | Planning |
| 4 | Add state variable | Edit file |
| 5 | Create new CSS classes | Edit file |
| 6 | Implement toggle component | Edit file |
| 7 | Run tests to verify | Run command |
| 8 | Fix any errors | Self-correct |

### Agents Change Your Role

| Traditional Role | Agent-Era Role |
|------------------|----------------|
| Task doer | Task manager |
| Implementer | Architect and reviewer |
| Writes all code | Delegates and verifies |

> *"This is a large shift because it turns you into a task manager instead of a task doer. You can have multiple agents working on different parts of your codebase simultaneously."*

### What Agents Are Good At

| Task Type | Example |
|-----------|---------|
| Clear objectives | "Add a login button" |
| Established patterns | Refactoring with consistent style |
| Adding tests | Write tests for existing code |
| Updating documentation | Generate API docs |

### What Agents Struggle With

| Task Type | Why It's Hard |
|-----------|---------------|
| Complex debugging | Requires deep system understanding |
| Pixel-perfect designs | Visual precision, subjective |
| New libraries | Not in training data |

### The Reality of Working with Agents

> *"Think of agents like fast junior developers who need clear direction, who also can easily forget things, so they require oversight."*

| Behavior | Description |
|----------|-------------|
| Get stuck in loops | Repeat same failing approach |
| Forget context | Need reminders of constraints |
| Make unintended changes | May be too enthusiastic |
| Need verification | You're still responsible |

### The Art of Delegation

> *"Working effectively with agents is about learning what to delegate and when."*

| Stage | Approach |
|-------|----------|
| Beginner | Small, well-defined tasks |
| Intermediate | Larger chunks with checkpoints |
| Advanced | Complex workflows with verification |

---

## Module Summary

| Lesson | Key Takeaway |
|--------|--------------|
| 1.1 How AI Models Work | AI is probabilistic, not deterministic — same input can yield different outputs |
| 1.2 Hallucinations | AI confidently generates incorrect information — always verify |
| 1.3 Tokens and Pricing | Output tokens cost 2-4x more than input tokens |
| 1.4 Context | Managing what the AI "sees" is the most important skill |
| 1.5 Tool Calling and MCP | Tools let AI take real actions; MCP is the universal standard |
| 1.6 Agents | Tools in a loop — you become a task manager, not a task doer |

---

## Discussion Questions

1. Think of a time when an AI tool gave you a confidently wrong answer. What happened? How could you have caught it?

2. Your team wants to adopt AI coding assistants. What mental models would you share with them first?

3. How might your daily workflow change if you had multiple agents working in parallel?

4. What are the risks of accepting AI-generated code without verification? How would you mitigate them?

---

## Transition to Module 2

> *"Now that we understand how AI models work, their limitations, and the mental models for working with them effectively, let's put these concepts into practice. In Module 2, we'll open Cursor and start using the Agent to understand and modify real code."*

---

*End of Module 1*