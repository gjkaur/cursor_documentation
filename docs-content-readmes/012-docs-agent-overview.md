This is the **Agent Overview** documentation – it explains Cursor's **most powerful feature**: the AI assistant that can work independently on complex coding tasks.

Think of the Agent as your **autonomous coding partner**. Unlike a simple chat bot that just answers questions, the Agent can actually **do things** – edit files, run commands, search your codebase, and complete multi-step tasks on its own.

Let me break this down for a complete beginner.

---

## What Is the Agent? (The 10-Second Summary)

**The Agent is Cursor's AI assistant that can complete complex coding tasks independently.** It's not just a chat bot – it's an **autonomous worker** that can:

- Read and edit your files
- Run terminal commands
- Search your codebase
- Browse the web
- And much more...

**Access it with `Ctrl + I`** (or `Cmd + I` on Mac).

| Analogy | What it means |
|---------|----------------|
| **Chat bot** = A consultant who gives advice | Tells you WHAT to do |
| **Agent** = A junior developer who works for you | Actually DOES the work |

---

## How the Agent Works (3 Components)

The Agent is built on three things working together:

### 1. Instructions 📋
**What it is:** The "rules" that guide how the Agent behaves.

This includes:
- **System prompt** (the core instructions from Cursor)
- **Rules** (custom rules you can add)

**Example rule:** "Always use TypeScript instead of JavaScript" or "Never delete files without asking first"

### 2. Tools 🛠️
**What it is:** The capabilities the Agent has to interact with your system.

We'll cover these in detail below – but think of tools as the Agent's "hands" and "eyes."

### 3. Model 🧠
**What it is:** The AI brain powering the Agent (Claude, GPT, Composer 2, etc.)

You can choose which model the Agent uses for each task.

---

## The Magic: Cursor Handles the Optimizations

> *"As new models are released, you can focus on building software while Cursor handles the model-specific optimizations."*

**What this means:** You don't need to worry about which tools work with which model. Cursor automatically tunes the instructions and tools for each model.

**Example:** When a new version of Claude comes out, Cursor figures out how to best use it. You just keep coding.

---

## Tools: The Agent's Capabilities (Full List)

Tools are what allow the Agent to actually **do things**. Here's every tool the Agent has access to:

| Tool | What it does | Example use |
|------|--------------|-------------|
| **Semantic search** | Finds code by meaning, not just exact words | "Find where we handle user login" |
| **Search files/folders** | Finds specific files by name | "Find `config.js`" |
| **Web** | Searches the internet | "Look up the React docs for hooks" |
| **Fetch Rules** | Reads your custom rules | "Check my coding guidelines" |
| **Read files** | Opens and reads file contents | "Read `app.js` so you understand it" |
| **Edit files** | Makes changes to your code | "Change the button color to blue" |
| **Run shell commands** | Executes terminal commands | "Run `npm install`" or "Run the tests" |
| **Browser** | Opens and interacts with web pages | "Open localhost:3000 and check the homepage" |
| **Image generation** | Creates images (with compatible models) | "Create an icon for the settings page" |
| **Ask questions** | Asks YOU for clarification | "Should I use an array or an object here?" |

**Important:** There is **no limit** on the number of tool calls the Agent can make during a task. It can keep working until the job is done.

---

## Checkpoints: Your Safety Net 🛡️

This is a **critical feature** for beginners. Checkpoints are automatic save points that let you undo mistakes.

### What are Checkpoints?

Before making significant changes, the Agent automatically creates a **snapshot** (checkpoint) of your codebase. It captures the state of all modified files.

### How to use Checkpoints:

| What happened | What to do |
|---------------|------------|
| Agent made a mistake | Click the checkpoint in the chat timeline |
| Preview the old state | See what your files looked like before |
| Restore | Revert all files to that checkpoint |

**Visual:** There's a "Restore Checkpoint" button on previous requests, and a `+` button when hovering over a message.

### When are Checkpoints useful?

| Scenario | Why it helps |
|----------|--------------|
| **Exploratory work** | Try something risky, easily undo if it fails |
| **Complex refactoring** | Multiple changes across many files – one-click restore |
| **Iterative development** | Safe rollback points as you experiment |

### Important: Checkpoints vs. Git

| Checkpoints | Git |
|-------------|-----|
| Stored locally | Stored in your repository |
| Automatic | Manual commits |
| For undoing Agent changes | For permanent version control |
| Temporary safety net | Permanent history |

> *"Only use checkpoints for undoing Agent changes; use Git for permanent version control."*

**For beginners:** Think of checkpoints as an "undo" button for Agent actions. Git is for saving permanent history.

---

## Queued Messages: Supercharge Your Workflow 📨

This feature lets you **keep working** while the Agent is busy.

### The Problem:

Without queued messages, you have to wait for the Agent to finish before you can type your next instruction.

### The Solution:

Type your next instruction while the Agent is working. It gets added to a **queue** and executes automatically when the Agent is ready.

### How to use the queue:

```
Step 1: Agent is working on something
Step 2: Type your next instruction (don't wait!)
Step 3: Press Enter to add it to the queue
Step 4: Agent finishes current task
Step 5: Agent automatically starts your queued instruction
```

**Bonus:** You can drag queued messages to reorder them!

---

## Keyboard Shortcuts (Crucial!)

| Action | Shortcut | What happens |
|--------|----------|--------------|
| **Queue message** | `Enter` | Your message waits until Agent finishes current task |
| **Send immediately** | `Ctrl + Enter` (or `Cmd + Enter` on Mac) | Interrupts current work and processes your message NOW |
| **Open Agent** | `Ctrl + I` (or `Cmd + I` on Mac) | Opens the Agent in the sidepane |

### When to use each:

| Use `Enter` (queue) when... | Use `Ctrl+Enter` (immediate) when... |
|-----------------------------|---------------------------------------|
| Agent is working fine | Agent is going in the wrong direction |
| You're adding follow-up tasks | You need to interrupt and redirect |
| You're in no hurry | There's an emergency or mistake |

---

## Agent vs. Chat: What's the Difference?

This is a common point of confusion for beginners.

| Feature | Chat (Simple) | Agent (Full) |
|---------|---------------|--------------|
| **Answers questions** | ✅ Yes | ✅ Yes |
| **Reads files** | ✅ Yes | ✅ Yes |
| **Edits files** | ❌ No (suggests changes) | ✅ Yes (makes changes) |
| **Runs terminal commands** | ❌ No | ✅ Yes |
| **Searches codebase** | Limited | Full semantic search |
| **Browses web** | ❌ No | ✅ Yes |
| **Autonomous multi-step tasks** | ❌ No | ✅ Yes |
| **Checkpoints** | ❌ No | ✅ Yes |

**Simple rule:** Use **Chat** for questions and explanations. Use **Agent** when you want the AI to actually **do** something.

---

## Real-World Example: Agent in Action

Let me show you what a real Agent session looks like:

### Your request:
> *"Add a dark mode toggle to my React app"*

### What the Agent does (automatically):

| Step | Action | Tool used |
|------|--------|-----------|
| 1 | Searches for React components | Semantic search |
| 2 | Reads `App.js` to understand structure | Read files |
| 3 | Reads `index.css` to see styling | Read files |
| 4 | Creates `ThemeContext.js` | Edit files |
| 5 | Adds CSS variables for dark/light mode | Edit files |
| 6 | Adds toggle button to `App.js` | Edit files |
| 7 | Runs `npm test` to verify nothing broke | Run shell commands |
| 8 | Opens browser to preview | Browser |
| 9 | Asks "Should I save user preference?" | Ask questions |

**All of this happens automatically.** You just watch and approve.

---

## Best Practices for Using Agent

### 1. Start with clear instructions
Don't be vague. Say *"Add a dark mode toggle that saves user preference to localStorage"* not *"Make it look better."*

### 2. Use checkpoints liberally
Checkpoints are free and automatic. Don't be afraid to restore if something goes wrong.

### 3. Queue messages for efficiency
While Agent is working on one thing, queue up the next task. You'll get more done.

### 4. Use `Ctrl+Enter` to redirect
If Agent is going the wrong way, interrupt immediately with `Ctrl+Enter`.

### 5. Let Agent use its tools
Don't micromanage. The Agent knows when to search, read, edit, or run commands.

### 6. Don't worry about tool limits
There's no limit on tool calls. Agent will keep working until the task is complete.

---

## Common Beginner Questions

### Q: Can Agent delete my files?
A: Yes, it can edit and delete files. **That's why checkpoints exist!** Always review changes before approving major deletions.

### Q: Does Agent cost more than Chat?
A: Yes, Agent uses more tokens because it makes multiple tool calls. But it also gets more done.

### Q: Can I stop Agent mid-task?
A: Yes! Use `Ctrl+Enter` with a message like "Stop what you're doing."

### Q: Are checkpoints permanent?
A: No, they're stored locally and temporary. Use Git for permanent history.

### Q: Can Agent work with my Git repository?
A: Yes, it can run `git commit`, `git push`, etc. through terminal commands.

---

## Summary for Beginners

| Concept | Simple explanation |
|---------|-------------------|
| **Agent** | AI assistant that can actually DO coding work |
| **Tools** | The Agent's abilities (edit files, run commands, etc.) |
| **Checkpoints** | Automatic save points to undo mistakes |
| **Queued messages** | Type next task while Agent is busy |
| **`Enter`** | Add message to queue (waits) |
| **`Ctrl+Enter`** | Send immediately (interrupts) |
| **`Ctrl+I`** | Open Agent |

---

## The Bottom Line

**The Agent is the heart of Cursor.** It's what makes Cursor more than just a chat bot in an editor.

**Think of the Agent as:**
- **Chat** = Asking a friend for advice 👨‍🏫
- **Agent** = Hiring that friend to do the work 👨‍💻

**For beginners:** Start with simple Agent tasks. Let it read files, make small edits, and run commands. Use checkpoints as your safety net. As you get comfortable, give it more complex multi-step tasks.

**The keyboard shortcuts matter:** `Enter` to queue, `Ctrl+Enter` to interrupt. Learn these and you'll work much faster.

