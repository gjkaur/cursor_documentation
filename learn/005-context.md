# AI Foundations – Context

## Complete Beginner's Guide

This document explains the **Context** lesson from Cursor Learn. It covers how to improve AI output by managing the context you provide, including system prompts, user messages, conversation history, and context limits.

Let me break this down for a complete beginner.

---

## The Big Insight: It's About Context, Not Just Prompts

> *"You might think to improve the model output you need to write better prompts. And that will certainly help, but it's missing the bigger point: working with AI models is all about managing the context you provide them."*

| Common Misconception | Reality |
|---------------------|---------|
| Better prompts = better output | Context management is more important |
| Just type a good prompt | What you provide (files, errors, history) matters |
| The AI should know what I want | You must provide the right context |

---

## The Cooking Analogy

### Making Soup:

| Step | Cooking | AI Coding |
|------|---------|-----------|
| **Inputs** | Ingredients | Codebase, files, prompt |
| **Process** | Follow recipe | Follow plan, todo list |
| **Output** | Tasty soup | Generated code |

> *"Different chefs might add or modify the ingredients to their taste, and even if you follow the same recipe exactly, it might taste slightly different at the end."*

### Coding Parallel:

| Cooking Step | AI Coding Equivalent |
|--------------|---------------------|
| Ingredients | Current codebase and files |
| Recipe instructions | Your prompt |
| Following the recipe | Following a plan (human or AI-generated) |
| Checking off steps | Todo list completion |
| Tasting the soup | Reviewing generated code |

---

## What Is Context?

**Context is like a long list where the AI model keeps a working memory for the conversation.**

Think of context as everything the AI can "see" and "remember" when generating a response.

| Context Includes | Description |
|-----------------|-------------|
| **System prompt** | Instructions from tool creator |
| **User messages** | Your prompts and questions |
| **Model outputs** | Previous AI responses |
| **Attached files** | Code files, documentation |
| **Tool outputs** | Terminal errors, linter results |
| **Conversation history** | All previous turns |

---

## System vs. User Prompts

### System Prompt (Tool Creator Instructions)

| Aspect | Description |
|--------|-------------|
| **Who sets it** | Tool creator (e.g., Cursor) |
| **Purpose** | Inject instructions or style for the model |
| **Examples** | "Be helpful", "Use concise responses", "Follow coding standards" |

> *"This is how the tool creator can inject some instructions or style for the model to follow. It's trying to help nudge the output in a certain direction."*

### User Prompt (Your Instructions)

| Aspect | Description |
|--------|-------------|
| **Who sets it** | You (the user) |
| **Purpose** | Give directions to the model |
| **Examples** | "Add a new route to manage user accounts" |

> *"You don't have to use proper spelling or grammar, as AI models are surprisingly good at figuring out what you meant, but it still can't hurt."*

---

## Context Can Include Images

Many AI products support attaching images. The model can:

| Capability | Example |
|------------|---------|
| **Read images** | Understand UI mockups |
| **Extract text** | Read text from screenshots |
| **Analyze content** | Understand diagrams, charts |

> *"Many AI products now support attaching images, where the underlying AI model can read and understand the contents of the image."*

---

## Interactive Quiz

The course includes this quiz question:

> *"Which items are part of the model's context during a chat?"*

| Option | Part of Context? | Why |
|--------|-----------------|-----|
| **System prompt** | ✅ Yes | Tool creator instructions |
| **The existing conversation history** | ✅ Yes | Working memory |
| **Attached files and tool outputs** | ✅ Yes | Additional context |
| Your API key string | ❌ No | Authentication, not context |

---

## Automatic Context Inclusion

Tools like Cursor automatically include relevant context:

| Context Source | Example |
|----------------|---------|
| **Open files** | Current file being edited |
| **Terminal output** | Error messages, build logs |
| **Linter errors** | Code quality warnings |
| **Selected code** | Highlighted sections |

> *"Tools like Cursor can automatically include other relevant information in the input context based on the state of your codebase."*

---

## Conversation Turns

Each back-and-forth between you and the AI is a "turn":

```
Turn 1: You ask → AI responds
Turn 2: You follow up → AI responds
Turn 3: You ask for clarification → AI responds
...
```

> *"Every message in the conversation, including both inputs and outputs, is stored as part of the working memory in context."*

---

## The Context Window Grows

```
Start: [System Prompt]
Turn 1: [User] + [AI Response]
Turn 2: [User] + [AI Response]
Turn 3: [User] + [AI Response]
...
Context gets longer and longer
```

### The Problem:

> *"Just like if you were having a conversation with a human, there's only so much context you can keep in your brain at one time. As the conversation goes on for a while, it gets harder to remember things people might have said 3 hours ago."*

---

## Context Limits

Every AI model has a **context limit** – maximum tokens it can process.

| Model | Context Limit |
|-------|---------------|
| Smaller models | 200K tokens |
| Larger models | 1M tokens (Max Mode) |

### What Happens at the Limit:

| Consequence | Description |
|-------------|-------------|
| **Can't accept more messages** | Conversation stops |
| **Old messages forgotten** | Model loses earlier context |
| **Need compression** | Summarize to stay under limit |

> *"Many AI tools give the user feedback on how close they are to those limits or provide ways to compress and summarize the current conversation to stay under the limit."*

---

## Managing Context (Preview)

| Technique | Description |
|-----------|-------------|
| **Compression** | Summarize long conversations |
| **Checkpoints** | Save and restore context |
| **Subagents** | Isolate context for specific tasks |
| **Context ring** | Visual indicator of usage |

> *"Later on in the course, we'll cover practical examples for how to manage context inside of Cursor."*

---

## Tool Calling (Preview)

> *"What about if we want the model to dynamically retrieve context itself? That's where tool calling comes in."*

| Without Tool Calling | With Tool Calling |
|--------------------|------------------|
| You provide all context | Model fetches context as needed |
| Static information | Dynamic information |
| Manual context inclusion | Automatic context retrieval |

---

## Key Takeaways for Engineers

| Takeaway | Action |
|----------|--------|
| **Context is more important than prompts** | Manage what the AI sees |
| **System prompt sets the tone** | Use rules to guide behavior |
| **Conversation history accumulates** | Compress when needed |
| **Context limits exist** | Stay within model limits |
| **Tools auto-include context** | Leverage Cursor's features |

---

## Practical Tips

| Tip | Why |
|-----|-----|
| **Include relevant files** | Gives model correct context |
| **Share terminal errors** | Helps model debug |
| **Keep conversations focused** | Avoid unnecessary context bloat |
| **Compress long conversations** | Stay under context limits |
| **Use system prompts for rules** | Consistent behavior |

---

## Visual: Context Window Growth

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONTEXT WINDOW                               │
├─────────────────────────────────────────────────────────────────┤
│  [System Prompt]                                                │
│  [User: "What does this function do?"]                         │
│  [AI: "This function calculates..."]]                          │
│  [User: "How can I optimize it?"]                              │
│  [AI: "You could use memoization..."]]                         │
│  [User: "Show me an example"]                                  │
│  [AI: "Here's an example..."]]                                 │
│  [Tool: read_file output]                                      │
│  [Tool: terminal error]                                        │
│  ... grows over time ...                                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Summary for Engineers

| Question | Answer |
|----------|--------|
| **What is context?** | Everything the AI can see/remember |
| **What's in context?** | System prompt, user messages, AI outputs, files, tools |
| **Why does context matter?** | Better context = better output |
| **What are context limits?** | Maximum tokens a model can process |
| **How to manage context?** | Compress, summarize, use tools |

---

## The Bottom Line

**Working with AI is about managing context – what the model sees and remembers.**

**Think of it as:**
- **Without context management** = Giving directions to someone blindfolded 🙈
- **With context management** = Giving directions with a map 🗺️

**For your engineers:**
- Context includes system prompts, your prompts, previous responses, files, and errors
- Context limits exist – stay within them
- Tools like Cursor auto-include relevant context
- Managing context is a skill that improves with practice
