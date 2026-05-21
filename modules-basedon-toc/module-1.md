# Module 1: Mental Models for AI-Assisted Development

## Cursor Training Program — Day 1 (Foundations)

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Concept block (foundational theory) |
| **Prerequisites** | None – this is the starting point |
| **Module Goal** | Build accurate mental models of how AI coding assistants work, their limitations, and how to use them effectively |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Explain why AI outputs are probabilistic, not deterministic
- Identify and mitigate hallucinations in coding contexts
- Understand token-based pricing and cost optimization
- Master context as the single most valuable AI skill
- Distinguish between tool calling, MCP, and autonomous agents
- Define the developer's evolving role with AI agents

---

## Lesson 1.1: How AI Models Work

### Concept (12 minutes)

> *"Why AI outputs are probabilistic and what determines them. Unlike traditional software that gives the same output for the same input, AI models generate responses based on probability distributions."*

### The Core Mental Model: Next-Token Prediction

At its simplest, an AI model (LLM) is a **next-token prediction engine**. Given a sequence of tokens (words, code characters), it predicts what comes next.

```
Input: "def calculate_sum(a, b):"
Model thinks: "What's most likely next?"
Probabilities:
  - "return" → 85%
  - "print" → 8%
  - "pass" → 4%
  - "for" → 2%
  - Other → 1%
```

**Why this matters for developers:**

| Traditional Code | AI Model |
|----------------|----------|
| Deterministic (same input → same output) | Probabilistic (same input → different outputs possible) |
| You control the logic | You influence, but don't control |
| Errors are bugs | Errors are features of probability |
| Predictable behavior | Needs management via parameters |

### What Determines AI Output?

```
┌─────────────────────────────────────────────────────────────┐
│                    Factors That Shape Output                 │
├─────────────────────────────────────────────────────────────┤
│  1. Training Data      → What the model "learned"           │
│  2. Prompt             → Your instruction (most influential)│
│  3. Temperature        → Randomness level (0 = deterministic)│
│  4. Top-p / Top-k      → Token selection pool size          │
│  5. System Prompt      → Persistent behavioral guidelines   │
│  6. Context Window     → What the model can "see"           │
│  7. Model Architecture → Different models, different biases │
└─────────────────────────────────────────────────────────────┘
```

### Key Parameters You Control

| Parameter | What It Does | Code Example | Best For |
|-----------|--------------|--------------|----------|
| **Temperature** | Controls randomness (0 = deterministic, 1 = creative) | `temperature: 0.2` | Bug fixes (low), brainstorming (high) |
| **Top-p** | Nucleus sampling – limits token pool | `top_p: 0.9` | Balanced responses |
| **Max Tokens** | Limits response length | `max_tokens: 4000` | Controlling cost |

### Practical Example: Temperature Impact

```python
# Same prompt, different temperature
prompt = "Write a function to reverse a string"

# Temperature 0.1 (very deterministic)
output = """def reverse_string(s):
    return s[::-1]"""

# Temperature 0.7 (balanced)
output = """def reverse_string(s):
    # Handle edge cases
    if not s:
        return s
    return s[::-1]"""

# Temperature 1.2 (creative, potentially unstable)
output = """def flip_the_text(text):
    # Let's do something unusual
    result = ""
    for char in reversed(text):
        result += char
    return result
    # Alternative: use list comprehension? etc."""
```

### The Training Gap

Models are frozen at their training cutoff date. They don't know:

- Code written after their training date
- Your company's internal APIs
- Your specific architecture decisions
- Recent library updates (unless in context)

**Implication:** You must provide this information in the prompt or context.

---

## Lesson 1.2: Hallucinations

### Concept (10 minutes)

> *"Why models invent things and how to spot it in coding contexts. Hallucinations are confident-sounding outputs that are factually wrong, made up, or don't exist."*

### What Hallucinations Look Like in Code

| Type | Example | How to Spot |
|------|---------|--------------|
| **Fake APIs** | `import nonexistent_library` | Check docs; import fails |
| **Wrong parameters** | `sorted(list, reverse=True)` instead of `reverse=True` | Type checking |
| **Invented methods** | `list.reverse_in_place()` | Know the standard library |
| **Confident nonsense** | "This is the standard way to..." | Cross-reference |
| **Outdated syntax** | Old Python 2 style | Know version differences |

### Why Models Hallucinate

```
┌─────────────────────────────────────────────────────────────┐
│                  Root Causes of Hallucination                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Training Data Gaps     → Model "guesses" when uncertain    │
│  Probability Pressure   → Must output SOMETHING             │
│  Pattern Overfitting    → Sees patterns that don't exist    │
│  No True/False Circuit  → Models don't have truth checking  │
│  Confidence Calibration → Sounds confident when wrong       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### The "Confident Wrong" Problem

Most dangerous hallucination: the model sounds **completely confident** while being **completely wrong**.

```python
# Example hallucination
User: "How do I use the requests library to make async calls?"

# Hallucinated response (confident, wrong)
"""
The requests library has built-in async support. Use:

import requests.async as async_requests
response = await async_requests.get('https://api.example.com')
"""

# Reality: requests library does NOT have async support.
# Correct answer: Use httpx or aiohttp
```

### Hallucination Mitigation Strategies

| Strategy | How It Works | Example |
|----------|--------------|---------|
| **Grounding** | Provide source material | Paste library docs into context |
| **Verification** | Ask for citations | "Which line of the docs shows this?" |
| **Constrained decoding** | Limit possible outputs | Use JSON mode, regex patterns |
| **Self-consistency** | Ask multiple times, compare | Run same prompt 3x, take majority |
| **Low temperature** | Reduce randomness | `temperature: 0.1` |
| **Tool use** | Let model search/lookup | Enable web search for docs |

### Hallucination Detection Checklist for Code

```markdown
Before accepting AI-generated code, verify:

□ Do the imported libraries exist? (pip install / npm install check)
□ Are function signatures correct? (check official docs)
□ Does the syntax match my language version?
□ Are there obvious logic errors?
□ Would this code actually run?
□ Have I seen this pattern before?
□ Does the model cite specific sources I can verify?
```

### The Developer's Mindset

> *"Trust, but verify – especially when the AI sounds most confident."*

- Hallucinations decrease with better prompts and context
- They never fully disappear
- You are the human-in-the-loop responsible for verification
- Experience helps you "smell" potential hallucinations

---

## Lesson 1.3: Tokens and Pricing

### Concept (10 minutes)

> *"What you actually pay for and how to keep costs predictable. Every API call has a cost – understanding tokens helps you control spending."*

### What Is a Token?

A token is the atomic unit of processing for LLMs. Not a word, not a character – somewhere in between.

| Language | Example | Token Count | Approximate |
|----------|---------|-------------|-------------|
| English | "Hello world" | 2 tokens | ~0.75 words/token |
| English | "Congratulations" | 1 token | Longer words can be 1 token |
| Code | `function calculateTotal()` | ~5 tokens | ~2-4 chars/token for code |
| Chinese | "你好世界" | 4-8 tokens | More tokens per character |

**Why tokens matter:**
- You pay per token (input + output)
- Context windows are measured in tokens
- Token limits determine how much code the AI can "see"

### Token Pricing: Input vs Output

**Input tokens** (your prompt, code context, retrieved docs) cost less than **output tokens** (generated code and explanations), often by 5–8×, because generation is more compute-intensive than reading.

### Real Pricing Examples (from Module 8 chat)

| Model | Input (per 1M) | Output (per 1M) | Output/Input Ratio |
|-------|---------------|----------------|-------------------|
| GPT-5 Mini | $0.25 | $2.00 | 8x |
| Claude 4.5 Haiku | $1.00 | $5.00 | 5x |
| GPT-5.3 Codex | $1.75 | $14.00 | 8x |
| Gemini 3.1 Pro | $2.00 | $12.00 | 6x |
| Claude 4.6 Sonnet | $3.00 | $15.00 | 5x |
| Claude 4.7 Opus | $5.00 | $25.00 | 5x |
| GPT-5.5 | $5.00 | $30.00 | 6x |

### What 1 Million Tokens Looks Like

| Content Type | Approximate Amount |
|--------------|-------------------|
| Plain English text | ~750,000 words (~1,500 pages) |
| Python code | ~250,000-500,000 lines |
| Average conversation | 5-10 sessions |
| Full codebase | Small to medium project |

### Cost Calculation Example

```python
# Calculate cost for a coding session
prompt_tokens = 5000   # Your instructions + some context
output_tokens = 2000   # AI's response

model = "claude-4.6-sonnet"
input_price = 3.00     # per 1M tokens
output_price = 15.00   # per 1M tokens

input_cost = (prompt_tokens / 1_000_000) * input_price
output_cost = (output_tokens / 1_000_000) * output_price
total_cost = input_cost + output_cost

print(f"Session cost: ${total_cost:.4f}")  # ~$0.045 (4.5 cents)
```

### Cost Optimization Strategies

| Strategy | How It Works | Impact |
|----------|--------------|--------|
| **Use cheaper models** | Mini/Haiku for simple tasks | 5-20x cost reduction |
| **Reduce context** | Only send relevant code | 2-5x reduction |
| **Cache responses** | Reuse common answers | Variable |
| **Batch operations** | Combine multiple tasks | 30-50% reduction |
| **Monitor usage** | Track spending per user | Prevents surprises |
| **Set limits** | Monthly spending caps | Budget protection |

### Real-World Cost Bounds

| Usage Level | Monthly Cost | What You Can Do |
|-------------|--------------|-----------------|
| Light | $10-20 | Occasional questions, small fixes |
| Medium | $50-100 | Daily coding, regular agent use |
| Heavy | $200-500 | Full-time AI assistance, multiple agents |
| Enterprise | $1000+ | Team usage, automation, CI/CD |

### The Cache Effect (Important!)

Models can cache frequently used content. When you reuse cached content:

- Cache Write: Cost to initially store
- Cache Read: **Much cheaper** than fresh input

```python
# First request (pays full input price)
# Second request with same context (pays cache read price)
# Cache read can be 80-95% cheaper than fresh input!
```

---

## Lesson 1.4: Context

### Concept (12 minutes)

> *"Managing what the model sees – the single most valuable AI skill. Context determines everything about the quality of AI responses."*

### What Is Context?

Context = all the information the model has access to when generating a response.

```
┌─────────────────────────────────────────────────────────────┐
│                    What Goes Into Context                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  System Prompt      → "You are a helpful coding assistant"  │
│  User Prompt        → "Fix this bug: ..."                   │
│  Code Files         → Current file, related files           │
│  Conversation       → Previous exchanges                    │
│  Retrieved Docs     → Library documentation, examples       │
│  Tool Outputs       → Results from search, file reads       │
│  Constraints        → "Only use standard library"           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### The Context Window Limit

Every model has a maximum context size (in tokens).

| Model | Context Window | Pages of Text | Lines of Code |
|-------|---------------|---------------|---------------|
| Claude 4 (Haiku / Sonnet / Opus) | 200k | ~150 | ~50,000 |
| GPT-5 Mini / GPT-5.3 Codex | 272k | ~200 | ~70,000 |

**What happens when you exceed context?**
- Oldest content gets truncated ("forgotten")
- Model loses earlier parts of conversation
- Critical information may be dropped

**Context engineering** = knowing what to put in, what to leave out, and how to structure it.

### Context Checklist Before Every AI Interaction

```markdown
□ What problem am I trying to solve?
□ What files/code does the model need to see?
□ What would a human need to know to help me?
□ What information can I safely leave out?
□ Is my context under the token limit?
□ Have I included relevant error messages?
□ Have I specified constraints (libraries, version, style)?
```

### Good vs Bad Context Examples

**BAD Context (vague):**
```
"Fix this bug: my code doesn't work"
```

**GOOD Context:**
```
"I have a Python function that should sort a list of dictionaries by
a specific key, but it's raising a KeyError. Here's the code:

def sort_by_key(data, key):
    return sorted(data, key=lambda x: x[key])

And here's the input causing the error:
data = [{'name': 'Alice'}, {'age': 30}]  # Second dict has no 'name'

I'm using Python 3.11. Expected behavior: skip dicts without the key.
```

### Context Prioritization Pyramid

```
                    ┌─────────────┐
                    │  Critical   │  MUST include
                    │  (must have)│  (~10-20% of context)
                  ┌┴─────────────┴┐
                  │   Important   │  Should include
                  │ (should have) │  (~20-30% of context)
                ┌┴───────────────┴┐
                │     Helpful     │  Nice to have
                │   (could have)  │  (~30-40% of context)
              ┌┴─────────────────┴┐
              │    Low Value       │  Omit if possible
              │   (can omit)       │  (~remaining)
              └───────────────────┘
```

### Context Window Management Strategies

| Strategy | How It Works | When to Use |
|----------|--------------|-------------|
| **Summarization** | Compress earlier conversation | Long sessions |
| **Selective inclusion** | Only relevant files | Large codebases |
| **Chunking** | Split across multiple calls | Exceeding limit |
| **Hierarchical** | Summaries + details on demand | Complex projects |
| **Vector retrieval** | Semantic search for relevant context | Very large codebases |

### The Lost in the Middle Problem

Research shows models pay **most attention to the beginning and end** of context, and **less to the middle**.

```
Context Position Attention:
├─────────────────────────────────────────────────────────┤
│ BEGINNING  ████████████████████████████████  (high)    │
│ MIDDLE     ████████                           (low)     │
│ END        ████████████████████████████████  (high)    │
└─────────────────────────────────────────────────────────┘
```

**Implication:** Put critical information at the beginning OR end, not the middle.

---

## Lesson 1.5: Tool Calling and MCP

### Concept (8 minutes)

> *"How models take real actions through external tools. Tool calling transforms AI from a text predictor into an action-taker."*

### What Is Tool Calling?

Tool calling (also called function calling) allows the AI to request execution of external functions. The AI doesn't execute code – it outputs a structured request that YOUR system executes.

```
┌─────────────────────────────────────────────────────────────┐
│                    Tool Calling Flow                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User: "What's the weather in Tokyo?"                       │
│                    ↓                                         │
│  AI decides: need weather data                              │
│                    ↓                                         │
│  AI outputs: tool_call {                                    │
│    name: "get_weather",                                      │
│    arguments: {"city": "Tokyo"}                             │
│  }                                                           │
│                    ↓                                         │
│  Your system executes get_weather("Tokyo")                  │
│                    ↓                                         │
│  Result returned to AI                                      │
│                    ↓                                         │
│  AI: "The weather in Tokyo is 22°C and sunny"               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Common Tool Types in Development

| Tool | Purpose | Example |
|------|---------|---------|
| **read_file** | Read code files | "Show me the auth module" |
| **edit_file** | Modify code | "Add error handling to line 42" |
| **search_code** | Find patterns | "Find all uses of this function" |
| **run_terminal** | Execute commands | "Run the tests" |
| **web_search** | Find documentation | "Look up pandas DataFrame API" |
| **browser** | Browse web pages | "Open the PR and review it" |
| **git** | Version control | "Create a branch and commit" |

### MCP (Model Context Protocol)

> *"MCP is a standardized way for AI models to discover and use tools. Think of it as USB-C for AI – one protocol that works across different tools."*

**Without MCP:** Each tool needs custom integration
**With MCP:** Tools advertise their capabilities; AI discovers them dynamically

```
MCP Architecture:
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   AI Model   │ ←→ │   MCP Host   │ ←→ │   Tools      │
│  (Claude,    │     │  (Cursor,    │     │  (Files,     │
│   GPT, etc)  │     │   Claude,    │     │   Terminal,  │
│              │     │   etc)       │     │   Web, etc)  │
└──────────────┘     └──────────────┘     └──────────────┘
```

### Why MCP Matters for Developers

| Benefit | Explanation |
|---------|-------------|
| **Interoperability** | Same tools work across different AI models |
| **Discoverability** | AI can learn what tools are available |
| **Standardization** | One protocol, not dozens of custom APIs |
| **Extensibility** | Add new tools without changing AI logic |

### Tool Calling Best Practices

```python
# 1. Define clear tool schemas
tool = {
    "name": "read_file",
    "description": "Read contents of a file",
    "parameters": {
        "path": {"type": "string", "description": "File path"},
        "lines": {"type": "integer", "description": "Lines to read (optional)"}
    }
}

# 2. Validate tool calls before execution
def validate_tool_call(tool_call):
    allowed_tools = ["read_file", "search_code", "run_tests"]
    if tool_call["name"] not in allowed_tools:
        return False, "Tool not allowed"
    # Validate parameters
    return True, "OK"

# 3. Set timeouts
# Tool execution should have limits (e.g., 30 seconds)

# 4. Log all tool calls
# 5. Require human approval for destructive actions; never auto-run writes/deletes
```

---

## Lesson 1.6: Agents

### Concept (8 minutes)

> *"What an agent is and how it changes the developer's role. Agents are AI systems that can pursue goals, make decisions, and take actions – not just respond to prompts."*

### Agent vs. Chatbot: The Critical Distinction

| Aspect | Chatbot | Agent |
|--------|---------|-------|
| **Interaction** | Single turn or simple back-and-forth | Multi-step, goal-oriented |
| **Control** | User drives each step | Agent plans and executes |
| **Memory** | Limited to conversation | Can maintain state across steps |
| **Actions** | None (text only) | Can call tools, modify files |
| **Autonomy** | None | Goal-directed autonomy |
| **Example** | "Explain this code" | "Fix all bugs in this repository" |

### The Agent Loop

```
┌─────────────────────────────────────────────────────────────┐
│                      Agent Loop                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│    ┌──────────┐                                             │
│    │  GOAL    │  "Add dark mode to the entire app"         │
│    └────┬─────┘                                             │
│         ↓                                                   │
│    ┌──────────┐                                             │
│    │  PLAN    │  Break goal into steps                      │
│    └────┬─────┘                                             │
│         ↓                                                   │
│    ┌──────────┐     ┌──────────┐                            │
│    │  ACT     │ ←→  │  OBSERVE │  (Tool call → result)     │
│    └────┬─────┘     └──────────┘                            │
│         ↓                                                   │
│    ┌──────────┐                                             │
│    │  THINK   │  Evaluate progress, adjust plan            │
│    └────┬─────┘                                             │
│         ↓                                                   │
│    ┌──────────┐                                             │
│    │  REPEAT  │  Until goal achieved or blocked            │
│    └──────────┘                                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Levels of Agent Autonomy

| Level | Name | Description | Example |
|-------|------|-------------|---------|
| **L1** | Assistant | Responds, but needs step-by-step guidance | Basic chatbot |
| **L2** | Tool-caller | Can request tools, human approves | Cursor Agent with approval |
| **L3** | Planner | Makes plans, executes with supervision | Auto-code review |
| **L4** | Autonomous | Self-directed, minimal supervision | CI/CD agent |
| **L5** | Full Agent | Complete task ownership, escalation only | Enterprise automation |

### How Agents Change the Developer's Role

**Traditional Development:**
```
Developer writes every line of code → tests → deploys
```

**Agent-Assisted Development:**
```
Developer defines intent → Agent executes → Developer reviews → Agent iterates
```

**Role Evolution:**

| Old Role | New Role |
|----------|----------|
| Code writer | Intent specifier |
| Debugger | Quality reviewer |
| Implementation | Orchestration |
| Manual testing | Acceptance testing |
| Problem solver | Problem framer |

### When to Use Agents (and When Not To)

**✅ GOOD for agents:**
- Large, multi-step tasks
- Repetitive patterns
- Well-defined with clear success criteria
- Low-risk changes
- Documentation updates

**❌ BAD for agents:**
- Security-critical systems
- Unrecoverable actions
- Poorly defined goals
- Real-time requirements
- High-cost of failure

---

## Module Summary

| Lesson | Topic | Key Insight |
|--------|-------|-------------|
| 1.1 | How AI Models Work | Probabilistic, not deterministic – manage with temperature |
| 1.2 | Hallucinations | Models invent confidently – always verify |
| 1.3 | Tokens and Pricing | Output costs more – optimize context, use cheaper models |
| 1.4 | Context | Single most valuable skill – quality in = quality out |
| 1.5 | Tool Calling & MCP | AI requests actions, you control execution |
| 1.6 | Agents | Goal-directed action – changes developer role |

---

## Transition to Module 2

> *"Now that you understand how AI models think, what they cost, and how agents work, we'll move to Module 2: Prompt Patterns – practical techniques for getting the best results from these systems."*

---

*End of Module 1*