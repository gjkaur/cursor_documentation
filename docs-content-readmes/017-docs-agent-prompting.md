This is the **Prompting Agents** documentation – it teaches you how to **talk to the Agent effectively**. Think of this as learning the "language" of Cursor to get better results.

Good prompting is like giving good instructions to a smart assistant. Be specific, provide context, and use the right tools.

Let me break this down for a complete beginner.

---

## What Is Prompting? (The 10-Second Summary)

**Prompting is how you tell the Agent what you want it to do.**

You type instructions in the chat input, and the Agent follows them. But you can make your prompts much more powerful by **attaching context** (files, images, terminal output, etc.) using special features.

| Basic Prompt | Better Prompt with Context |
|--------------|---------------------------|
| "Fix this bug" | @auth.ts "Fix the login bug in this file" |
| "Make it look better" | *screenshot* + "Make the button match this design" |
| "Something's wrong" | @Terminals "Here's the error, fix it" |

---

## How to Prompt (The Basics)

The chat input is where you type. You can:

| Method | How to do it |
|--------|--------------|
| **Text** | Just type your instructions |
| **Images** | Drag and drop, or paste from clipboard |
| **Voice** | Click the microphone icon and speak |

**You can switch models at any point** using the model picker dropdown.

---

## @Mentions: The Most Powerful Feature 🎯

**@mentions** let you attach specific context to your prompt. Type `@` in the chat input, then start typing to see suggestions.

Think of `@` as pointing at something and saying *"Look at THIS when you answer."*

### All @Mention Types:

| @Mention | What it does | Example |
|----------|--------------|---------|
| **Files & Folders** | Include specific files or entire folders | `@auth.ts` or `@src/components/` |
| **Docs** | Search indexed documentation | `@Docs React` to get React docs |
| **Terminals** | Include terminal output as context | `@Terminals` to show error messages |
| **Past Chats** | Reference previous conversations | `@Past Chats` to continue an earlier thread |
| **Git diffs** | Include uncommitted changes or branch differences | `@Commit` or `@Branch (Diff with Main)` |
| **Browser** | Attach context from built-in browser | `@Browser` to reference a webpage |

### Pro Tip: You Don't Always Need @Mentions

> *"Use @ mentions when you know which files are relevant. If you're not sure which files matter, skip it – Agent finds relevant files through its own search."*

**This is important!** The Agent is smart enough to search your codebase. You only need `@` to point it in the right direction or be specific.

---

## @Mentions in Detail

### 1. Files & Folders 📁

**What it does:** Tells the Agent to read specific files or folders.

**Example:** `@auth.ts` "Check if this has any security issues"

**With folders:** `@src/components/` "Look at all components and tell me which ones use the old API"

**Navigation trick:** Type `/` after selecting a folder to navigate deeper.

### 2. Docs 📚

**What it does:** Searches indexed documentation (including docs you add yourself).

**Example:** `@Docs` "How do I use the new useState hook?"

**Add your own docs:** Type `@Docs > Add new doc` to include your team's internal documentation.

### 3. Terminals 💻

**What it does:** Includes terminal output as context for the Agent.

**Example:** Your build failed with errors. Type `@Terminals` "Fix these errors"

**Perfect for:** Debugging error messages, failed builds, test failures.

### 4. Past Chats 💬

**What it does:** References context from a previous conversation.

**Example:** You were working on a feature yesterday. Today, `@Past Chats` "Continue from where we left off"

### 5. Git Diffs 🔀

**What it does:** Shows what changed in your code.

| Option | What it shows |
|--------|---------------|
| `@Commit (Diff of Working State)` | Changes you haven't committed yet |
| `@Branch (Diff with Main)` | All changes in your current branch vs. main |

**Example:** `@Commit` "Review my changes before I commit"

### 6. Browser 🌐

**What it does:** Attaches context from the built-in browser.

**Example:** You're looking at a design on a webpage. `@Browser` "Turn this into HTML/CSS"

---

## Image Input 🖼️

**Attach images to your prompt** to provide visual context.

### How to add images:

| Method | How to do it |
|--------|--------------|
| **Drag and drop** | Drag an image file into the chat input |
| **Paste from clipboard** | Take a screenshot, then `Ctrl+V` |

### When to use images:

| Use Case | Example |
|----------|---------|
| **Design mockups** | "Turn this Figma design into code" |
| **Debugging visual issues** | "The button is misaligned in the screenshot" |
| **Error messages** | "Here's the error popup, fix it" |
| **UI implementation** | "Make it look exactly like this image" |

**Why this is powerful:** Instead of describing a design with words ("make a blue button with rounded corners..."), you just show it. The AI sees exactly what you want.

---

## Voice Input 🎤

**Click the microphone icon** in the chat input to dictate instead of typing.

### Best for:

| Situation | Why |
|-----------|-----|
| Long prompts | Speaking is faster than typing |
| Mobile/away from keyboard | Hands-free input |
| Natural explanation | Just talk like you would to a person |

**Pro tip:** Review the transcription before sending. Technical terms (file names, function names) might need correction.

---

## Context Usage: The Ring and the Tray 📊

### The Context Ring

Next to your prompt input, there's a **ring** that shows how full your context window is.

| Ring color/amount | What it means |
|-------------------|---------------|
| Empty/green | Plenty of space left |
| Partially filled | Getting full |
| Almost full | Near limit – Agent may start compressing |

### Click the Ring to Open the Breakdown Tray

The tray shows exactly what's using your context tokens:

| Category | What it includes |
|----------|------------------|
| **System prompt** | Cursor's built-in instructions |
| **Tools** | Definitions of every tool available |
| **Rules** | Your custom project and user rules |
| **Skills** | Skill descriptions in the context |
| **MCP** | Instructions from connected servers |
| **Subagents** | Documentation for subagent types |
| **Summarized conversation** | Compressed summaries of older messages |
| **Conversation** | Your messages, Agent replies, tool results |

**Hover over any segment to highlight that category!**

### What Happens When Context Gets Full?

> *"When the window gets close to full, Cursor compresses older parts of the conversation into a summary to leave more room for new conversation."*

**This is automatic.** You don't need to do anything. Cursor summarizes old messages to make space for new ones.

---

## Changing Models Mid-Conversation

Use the **model picker dropdown** at the top of the chat input, or press `Ctrl + /` to cycle through models.

### When to switch models:

| Start with... | Switch to... | Why |
|---------------|--------------|-----|
| **Fast model** (Grok, Haiku) | **Capable model** (Opus, GPT-5.5) | Exploration → Implementation |
| **Cheap model** (Mini) | **Smart model** (Sonnet) | Simple → Complex task |
| **General model** | **Codex/Composer** | Need specialized coding |

**Example workflow:**
1. Start with **Grok** (fast) to explore the codebase
2. Find what needs to change
3. Switch to **Claude Opus** (smart) for complex implementation

**Set a default model** in Cursor Settings > Models.

---

## Prompting Best Practices

### DO ✅

| Practice | Example |
|----------|---------|
| **Be specific** | "Change the login button color to blue (#0000FF)" |
| **Use @mentions for relevant files** | `@auth.ts` "Add password reset here" |
| **Include images for designs** | *screenshot* + "Match this layout" |
| **Add terminal output for errors** | `@Terminals` "Fix this build error" |
| **Give context first, then task** | "This is an e-commerce app. Add a cart feature." |
| **Use voice for long explanations** | (much faster than typing) |

### DON'T ❌

| Practice | Why it's bad |
|----------|---------------|
| Vague instructions | "Make it better" – better how? |
| No context | "Fix the bug" – what bug? |
| Extremely long prompts | Context window fills up |
| Changing task mid-stream | Confuses the Agent |

---

## Real-World Prompting Examples

### Example 1: Fixing a bug

**Bad prompt:**
> "Fix the login bug"

**Good prompt:**
> `@auth.ts` `@Terminals` "The login button gives a 'network error' when clicked. Here's the terminal error. Fix it."

### Example 2: Implementing a design

**Bad prompt:**
> "Make a button like the image"

**Good prompt:**
> *[paste screenshot of design]* "Create a React component that matches this button exactly – blue background, white text, rounded corners, hover effect that darkens slightly."

### Example 3: Complex feature

**Bad prompt:**
> "Add search"

**Good prompt (with Plan Mode):**
> *[Plan Mode ON]* "Add a product search feature that filters by name and category, with debounced input to avoid too many API calls."

### Example 4: Continuing work

**Bad prompt:**
> "Keep going"

**Good prompt:**
> `@Past Chats` "Continue the authentication feature we were building yesterday. Next step is adding the password reset flow."

---

## Common Beginner Questions

### Q: Do I need to use @mentions every time?
**A:** No. Agent can search your codebase on its own. Use @mentions when you know exactly which files matter.

### Q: Can I use multiple @mentions in one prompt?
**A:** Yes! `@auth.ts` `@database.ts` "Connect these two files"

### Q: How many images can I attach?
**A:** As many as fit in your context window. But each image uses tokens.

### Q: Does voice input work for all languages?
**A:** Check Cursor's documentation for language support.

### Q: What happens if I paste a very large image?
**A:** It uses many tokens. Resize images before attaching if possible.

### Q: Can I see my context usage history?
**A:** Click the ring to see current usage. Past usage isn't saved.

---

## Quick Reference Card

| Feature | How to use |
|---------|------------|
| **@mentions** | Type `@` then choose file, folder, docs, terminal, etc. |
| **Images** | Drag and drop, or `Ctrl+V` from clipboard |
| **Voice** | Click microphone icon |
| **Context ring** | Shows how full your context is |
| **Switch models** | Dropdown or `Ctrl+/` |
| **Set default model** | Settings → Models |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is prompting?** | How you tell the Agent what to do |
| **What are @mentions?** | Way to attach specific context (files, terminal, etc.) |
| **What's the context ring?** | Visual indicator of how full your context window is |
| **Can I use images?** | Yes, drag and drop or paste |
| **Can I use voice?** | Yes, click the microphone |
| **Can I switch models mid-chat?** | Yes, dropdown or `Ctrl+/` |

---

## The Bottom Line

**Good prompting = Good results.**

**The three most important things to remember:**

1. **Use @mentions** when you know which files matter
2. **Don't worry if you don't know** – Agent can find files on its own
3. **Images are powerful** – show, don't just tell

**For beginners:** Start with simple text prompts. Add `@Terminals` when debugging errors. Add screenshots for design work. As you get comfortable, experiment with other @mentions.

**The best prompt is specific, provides context, and clearly states what you want.**

Would you like me to explain any specific @mention type in more detail, or move on to another document?