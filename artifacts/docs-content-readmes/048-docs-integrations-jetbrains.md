This is the **JetBrains Integration** documentation – it explains how to use Cursor's AI agent directly inside **IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs**.

Think of this as **bringing Cursor's AI coding agent into your favorite JetBrains IDE** – you don't have to switch editors to use Cursor's powerful features.

Let me break this down for a beginner.

---

## What Is the JetBrains Integration? (The 10-Second Summary)

**Use Cursor's AI agent in IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs through the Agent Client Protocol (ACP).**

| Without JetBrains Integration | With JetBrains Integration |
|------------------------------|---------------------------|
| Use Cursor editor only | Stay in your JetBrains IDE |
| Switch between tools | One workflow |
| No AI agent in JetBrains | Full Cursor agent capabilities inside JetBrains |

> *"ACP lets you stay in your JetBrains IDE while Cursor handles agent-driven development. You get access to frontier models from OpenAI, Anthropic, Google, and Cursor, along with secure codebase indexing and semantic search."*

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| **Paid Cursor plan** | You need an active Cursor subscription |
| **JetBrains IDE** | IntelliJ IDEA, PyCharm, WebStorm, or other JetBrains IDE |
| **AI Assistant plugin** | Version **2025.1+** enabled |

---

## Supported JetBrains IDEs

| IDE | Support |
|-----|---------|
| **IntelliJ IDEA** | ✅ Yes |
| **PyCharm** | ✅ Yes |
| **WebStorm** | ✅ Yes |
| **Other JetBrains IDEs** | ✅ Yes (with AI Assistant plugin) |

---

## Setup (4 Steps)

### Step 1: Open the AI Chat Plugin

Open the **AI Chat panel** in your JetBrains IDE. You can find it:
- In the **right sidebar**
- Or through **View > Tool Windows > AI Chat**

### Step 2: Install Cursor from the ACP Registry

In the AI Chat panel:
1. Open the **agent provider list**
2. Select **Add Agent from Registry**
3. Search for **Cursor**
4. **Install** it

### Step 3: Authenticate

After installing, select **Cursor** as your agent provider.

### Step 4: Start Coding

Send a prompt in the AI Chat panel. Cursor's agent will:
- Read your project
- Edit files
- Run terminal commands
- Create code directly in your JetBrains IDE

---

## What You Get (Capabilities)

Cursor ACP in JetBrains IDEs provides many of the same agent capabilities available across other Cursor surfaces:

| Capability | What it does |
|------------|--------------|
| **Model selection** | Choose from frontier models (OpenAI, Anthropic, Google, Cursor). Switch between models as needed for different tasks. |
| **Codebase understanding** | Cursor indexes your codebase and uses semantic search to find relevant code across large projects. |
| **File editing** | The agent reads and writes files in your project, with changes reflected in your JetBrains editor. |
| **Terminal commands** | The agent runs shell commands in the IDE's integrated terminal. |

---

## How It Works (Technical)

Cursor ACP uses the **Agent Client Protocol (ACP)** – an open standard for connecting AI agents to IDEs.

| Component | Role |
|-----------|------|
| **Your JetBrains IDE** | ACP client |
| **Cursor's agent** | ACP server |

### The Flow:

```
You send prompt → AI Chat plugin forwards to Cursor agent via ACP
                  ↓
         Cursor agent processes request
                  ↓
         Reads your project files
                  ↓
         Streams edits and terminal commands back to IDE
```

---

## Pricing

> *"Cursor ACP uses the same usage-based pricing as your Cursor subscription."*

No additional cost beyond your existing Cursor plan.

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **What it does** | Brings Cursor's AI agent into JetBrains IDEs |
| **Requirement** | Paid Cursor plan + JetBrains IDE + AI Assistant plugin (2025.1+) |
| **Supported IDEs** | IntelliJ, PyCharm, WebStorm, others |
| **Protocol** | Agent Client Protocol (ACP) – open standard |
| **Pricing** | Same as Cursor subscription |
| **Setup steps** | Open AI Chat → Install from Registry → Authenticate → Start |

---

## Common Beginner Questions

### Q: Do I need to install a separate Cursor app?
**A:** No – this is a plugin that works inside your existing JetBrains IDE.

### Q: Does this work with the free version of Cursor?
**A:** No – you need a **paid Cursor plan**.

### Q: Does this work with older JetBrains IDEs?
**A:** The AI Assistant plugin requires version **2025.1 or newer**.

### Q: Can I use all the same models as in Cursor?
**A:** Yes – you get access to frontier models from OpenAI, Anthropic, Google, and Cursor.

### Q: Does the agent have access to my entire project?
**A:** Yes – it indexes your codebase for semantic search and can read/write files.

### Q: Can the agent run terminal commands in my IDE?
**A:** Yes – it runs shell commands in the IDE's integrated terminal.

---

## Comparison: JetBrains Plugin vs. Cursor Editor

| Feature | Cursor Editor | JetBrains Plugin |
|---------|---------------|------------------|
| **Standalone app** | ✅ Yes | ❌ No (runs inside JetBrains) |
| **Full agent capabilities** | ✅ Yes | ✅ Yes |
| **Model selection** | ✅ Yes | ✅ Yes |
| **Codebase indexing** | ✅ Yes | ✅ Yes |
| **File editing** | ✅ Yes | ✅ Yes |
| **Terminal commands** | ✅ Yes | ✅ Yes |
| **Stay in JetBrains** | ❌ No | ✅ Yes |
| **Use JetBrains features** | ❌ No | ✅ Yes (refactoring, debugger, etc.) |

---

## The Bottom Line

**The JetBrains integration lets you use Cursor's powerful AI agent without leaving your favorite JetBrains IDE.**

**Think of it as:**
- **Using Cursor Editor** = Switching to a different tool 🔄
- **Using JetBrains plugin** = Bringing AI into your existing workflow ✨

**For JetBrains users:** This is a game-changer. You get:
1. All the power of Cursor's agent (semantic search, file editing, terminal commands)
2. All the features of your JetBrains IDE (refactoring, debugging, etc.)
3. One seamless workflow – no switching between tools

**The setup is simple:**
1. Open AI Chat panel in JetBrains
2. Install Cursor from ACP registry
3. Authenticate
4. Start coding

**No additional cost** – uses your existing Cursor subscription.

