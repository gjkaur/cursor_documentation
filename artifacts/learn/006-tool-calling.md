# AI Foundations – Tool Calling

## Complete Beginner's Guide

This document explains the **Tool Calling** lesson from Cursor Learn. It covers how AI models can do more than generate text – they can actually take actions and retrieve information dynamically through tools.

Let me break this down for a complete beginner.

---

## What Is Tool Calling? (The 10-Second Summary)

**Tool calling is giving AI models the ability to call other APIs themselves.** It's as if the AI model can learn new skills beyond just generating text.

| Without Tool Calling | With Tool Calling |
|---------------------|-------------------|
| Model only generates text | Model can take actions |
| Limited to provided context | Can fetch real-time information |
| Cannot interact with external systems | Can read files, search web, run commands |

> *"Remember how we compared AI models to API endpoints? Well, tool calling is like giving those models the ability to call other APIs themselves."*

---

## The Cooking Analogy (Over the Phone)

### Without Tool Calling:

| Limitation | Why It Matters |
|------------|----------------|
| Can't see what's in the fridge | Can't suggest recipes based on available ingredients |
| Can't taste the food | Can't adjust seasoning |
| Can't see oven temperature | Can't give precise cooking instructions |

### With Tool Calling:

| Capability | Result |
|------------|--------|
| Friend sends photos of fridge | Better recipe suggestions |
| Friend tells oven temperature | Precise cooking guidance |
| Friend describes taste | Adjustments in real-time |

> *"That's essentially what tool calling does for AI models – gives them access to real-time information."*

---

## How Tool Calling Works (Under the Hood)

| Step | What Happens |
|------|--------------|
| **1** | AI model receives your request and recognizes it needs additional capabilities |
| **2** | Model formats a special response in JSON specifying which tool to use and what parameters to pass |
| **3** | The application runs that tool and returns the results |
| **4** | The AI model incorporates those results into its context and continues the conversation |

---

## You've Already Used Tool Calling!

| Example | Tool Being Used |
|---------|-----------------|
| Asking ChatGPT to generate an image | Image generation tool |
| Asking ChatGPT to search the web | Web search tool |
| Asking ChatGPT to run code | Code execution tool |

> *"You've probably already used tool calling without realizing it!"*

---

## Why Tools Matter for Coding

For building software, tools are incredibly powerful because they let the AI model:

| Tool Capability | What It Does |
|-----------------|--------------|
| **Read and write files** | Modify your codebase |
| **Search through code** | Find relevant functions or patterns |
| **Run shell commands** | Test code, install packages |
| **Access documentation** | Get current information |
| **Check for errors** | Run linters or tests |

> *"Without tools, the AI model would be limited to only the information you explicitly provide in the context. With tools, it can actively explore and interact with your codebase."*

---

## The Three Components of Every Tool

| Component | Description | Example |
|-----------|-------------|---------|
| **Name** | Identifies the tool | `read_file` |
| **Description** | Tells model when/how to use it | "Read the contents of a file" |
| **Parameters** | Inputs the tool needs | `{"filepath": "path/to/file"}` |

---

## Tool Definition Example

```json
{
  "name": "read_file",
  "description": "Read the contents of a file from the codebase",
  "parameters": {
    "filepath": "The path to the file to read"
  }
}
```

## Tool Call Example (What the Model Generates)

```json
{
  "tool": "read_file",
  "parameters": {
    "filepath": "src/components/Button.tsx"
  }
}
```

> *"The application then reads that file and adds the contents to the conversation context, allowing the model to understand your code."*

---

## Interactive Quiz (Part 1)

The course includes this quiz question:

> *"Which are core parts of a tool definition?"*

| Option | Part of Tool? | Why |
|--------|---------------|-----|
| **Name** | ✅ Yes | Identifies the tool |
| **Description** | ✅ Yes | Tells model when/how to use |
| **Parameters schema** | ✅ Yes | Defines required inputs |
| Provider API key | ❌ No | Authentication, not tool definition |

---

## The Cost of Tools (Token Usage)

Tool calls consume tokens in two ways:

| Token Type | What It Includes | Cost Impact |
|------------|------------------|-------------|
| **Tool definitions (input)** | Tool names, descriptions, parameters | Added to every request (hundreds of tokens) |
| **Tool results (output)** | What the tool returns (file contents, command output) | Varies based on return size |

> *"Conversations with lots of tool usage will fill up the context window faster and cost more. But the tradeoff is usually worth it because the AI can be much more helpful."*

---

## Tool Calls and Context Re-evaluation

| Concept | What Happens |
|---------|--------------|
| **Before tool call** | Model processes context |
| **Tool executes** | Returns results |
| **After tool call** | Model re-evaluates context with new information |

> *"When tool calls happen, AI models re-evaluate context up until the tool call itself. Inside of tools like Cursor, this means you'll see more cached input token usage."*

---

## Interactive Quiz (Part 2)

The course includes this quiz question:

> *"Tool calls affect token usage in which two ways?"*

| Option | Correct? | Why |
|--------|----------|-----|
| **Tool definitions add input tokens** | ✅ Yes | Added to every request |
| **Tool results add output tokens** | ✅ Yes | Return values consume tokens |
| Tool calls are free once defined | ❌ No | They always consume tokens |
| Streaming removes token costs | ❌ No | Streaming doesn't remove costs |

---

## Beyond Built-in Tools: MCP

**MCP (Model Context Protocol)** is a new standard for connecting tools to AI models.

| Analogy | Explanation |
|---------|-------------|
| **USB** | Universal standard for connecting devices to computers |
| **MCP** | Universal standard for connecting tools to AI models |

> *"Just like how USB became a standard for connecting devices to computers, MCP aims to be a standard for connecting tools to AI models."*

### What MCP Enables:

| Integration | Example |
|-------------|---------|
| **Figma** | Access design files |
| **Linear** | View and manage issues |
| **Databases** | Query data directly |
| **Internal tools** | Connect to custom APIs |

> *"You can also create your own MCP servers to integrate with internal tools and APIs."*

---

## From Tools to Agents

> *"Now that you understand tool calling, let's see what happens when we let AI models use multiple tools in sequence. That's where things get interesting with agents."*

| Single Tool Call | Multiple Tools (Agent) |
|------------------|----------------------|
| Model uses one tool | Model chains multiple tools |
| Simple action | Complex workflows |
| Read file OR run command | Read file → analyze → run test → fix code |

---

## Tool Calling in Cursor

Cursor provides many built-in tools:

| Tool | Purpose |
|------|---------|
| **read_file** | Read file contents |
| **edit_file** | Edit code files |
| **search_code** | Find code by meaning or pattern |
| **run_command** | Execute terminal commands |
| **browser** | Navigate and test web pages |

---

## Key Takeaways for Engineers

| Takeaway | Action |
|----------|--------|
| **Tools extend AI capabilities** | Model can take real actions |
| **Tools have three components** | Name, description, parameters |
| **Tools consume tokens** | Definitions + results count |
| **MCP is the new standard** | Universal tool connectivity |
| **Multiple tools = agents** | Complex sequences possible |

---

## Tool Calling Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    TOOL CALLING FLOW                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  User: "Read the main.c file and explain what it does"         │
│                    ↓                                           │
│  Model recognizes need for read_file tool                      │
│                    ↓                                           │
│  Model generates: {"tool": "read_file", "parameters": {...}}   │
│                    ↓                                           │
│  Application executes read_file                                │
│                    ↓                                           │
│  File contents returned to model                               │
│                    ↓                                           │
│  Model incorporates content into context                       │
│                    ↓                                           │
│  Model generates: "This file contains..."                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Summary for Engineers

| Question | Answer |
|----------|--------|
| **What is tool calling?** | AI models calling external functions |
| **What are tool components?** | Name, description, parameters |
| **Why do tools matter for coding?** | Read/write files, run commands, search code |
| **How do tools affect tokens?** | Definitions (input) + Results (output) |
| **What is MCP?** | Universal standard for AI tool integration |

---

## The Bottom Line

**Tool calling turns AI from a text generator into an action-taker that can interact with your codebase.**

**Think of it as:**
- **Without tools** = Consultant who only gives advice 🧐
- **With tools** = Developer who can actually do the work 👩‍💻

**For your engineers:**
- Tools let AI read, write, search, and run commands
- Each tool call consumes tokens (definitions + results)
- Multiple tools in sequence create powerful agents
- MCP enables custom tool integration
