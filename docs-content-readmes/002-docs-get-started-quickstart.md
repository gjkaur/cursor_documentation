Excellent! This is the **Quickstart guide** – the practical step-by-step tutorial that teaches you how to actually *use* Cursor. This complements the overview I explained earlier.

Let me break this down for a complete beginner in simple terms.

---

## What This Guide Does

This guide takes you from **zero to your first working change** in about 5-10 minutes. It's like having someone sit next to you and say: *"First do this, then this, then this..."*

---

## Step 1: Install Cursor and Sign In

**What you do:**
1. Go to Cursor's website and download the version for your computer:
   - **macOS** (Apple computers)
   - **Windows** (PC)
   - **Linux** (alternative operating system)
2. Open the app
3. Sign in (create an account or use Google/GitHub)
4. Pick a folder (any code project – even an empty one)
5. Start with a small task

**For a beginner:** If you don't have a code project, create a folder with a simple `index.html` file or download a small open-source project from GitHub.

---

## Step 2: Ask Cursor to Explain Your Codebase

**What you do:**
- Press `Ctrl + I` (or `Cmd + I` on Mac) to open the **Agent** (Cursor's AI assistant)
- Copy and paste this exact question:

> *"Explain this codebase. Point me to the main entry points, key modules, and anything I should read before making changes."*

**What happens next:**
Cursor will:
- Search through all your files
- Read relevant code
- Give you a summary like:
  *"This is a web app. The main entry point is `index.js`. Key modules are `auth.js` (handles logins) and `database.js` (saves data). Start by reading `README.md` and `config.js`."*

**Why this is amazing:** Normally, understanding a new codebase can take hours or days. Cursor does it in seconds.

**Real example:** Imagine opening a massive project with 500 files. Without Cursor, you'd be lost. With Cursor, it tells you exactly where to start.

---

## Step 3: Make One Small Change

**Two ways to do this:**

### Option A: Let Cursor suggest improvements (good for beginners)
Ask Cursor:

> *"Suggest three small, safe improvements in this codebase. Explain the tradeoffs and wait for me to choose one."*

Cursor might suggest:
1. "Fix a typo in the welcome message" (super safe)
2. "Change a button color" (visual only)
3. "Add a loading spinner" (small feature)

You pick one, and Cursor makes the change.

### Option B: Tell Cursor exactly what you want (faster if you know)
Just say directly:
> *"Change the welcome message from 'Hello' to 'Welcome to my app'"*

**Good first tasks are:**
- Fixing typos in text
- Changing colors or spacing
- Adding simple comments
- Small UI tweaks

**Avoid for first try:**
- Deleting files
- Changing database code
- Rewriting core logic

---

## Step 4: Review the Diff and Verify

**What is a "diff"?**
A diff shows you **what changed** – lines added (in green) and lines removed (in red). It's like a teacher highlighting your edits.

**What you do:**
1. Watch Cursor work (it shows you each change)
2. Look at the **diff view** to see exactly what was added/removed
3. Ask Cursor to check its work:

> *"Run the tests"* or *"Check for errors"*

Cursor will run your project's:
- **Tests** (automated checks)
- **Type checker** (finds data type errors)
- **Linter** (finds style/code quality issues)
- **Local build** (tries to compile/run)

**If something's wrong:** Cursor will see the error and can fix it automatically.

**If everything's good:** Your change is ready!

---

## Step 5: Use Plan Mode for Bigger Changes (Advanced Beginner)

**What is Plan Mode?**
Normal mode = Cursor just starts coding immediately  
**Plan Mode** = Cursor makes a plan FIRST, asks for your approval, THEN codes

**How to turn it on:**
Press `Shift + Tab` in the agent input

**What Plan Mode does (4 steps):**

| Step | What Cursor does |
|------|------------------|
| 1 | **Researches** your codebase to find relevant files |
| 2 | **Asks clarifying questions** (if your request is vague) |
| 3 | **Creates a detailed plan** (list of steps, files to change) |
| 4 | **Waits for your approval** before writing ANY code |

**When to use Plan Mode:**
- Changing multiple files at once
- Adding a new feature
- Refactoring (restructuring) code
- When you're not 100% sure how to do it

**Example:**
You say: *"Add a dark mode toggle to the whole app"*

Normal mode: Cursor might just start editing random files  
Plan Mode: Cursor says *"I'll need to change 5 files: index.html, styles.css, theme.js, settings.json, and app.js. Here's my plan. Should I proceed?"*

You say YES, and it does it safely.

---

## Complete Beginner Workflow Summary

Here's exactly what you do in order:

```
1. Download & install Cursor
2. Open a project folder
3. Press Ctrl+I to open Agent
4. Ask: "Explain this codebase..."
5. Read the explanation
6. Ask: "Suggest 3 small safe improvements"
7. Pick one improvement
8. Say: "Make change #1"
9. Review the green/red changes (diff)
10. Say: "Run the tests"
11. If all good → done! If errors → Cursor fixes them
```

---

## Keyboard Shortcuts Cheat Sheet

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Open Agent (AI assistant) | `Ctrl + I` | `Cmd + I` |
| Toggle Plan Mode (in Agent) | `Shift + Tab` | `Shift + Tab` |

---

## Common Beginner Questions

**Q: What if I don't have a codebase?**  
A: Create a simple HTML file with "Hello World" and use that. Or ask Cursor: *"Create a simple todo app for me to practice on."*

**Q: Can Cursor damage my code?**  
A: That's why you review the diff! You see every change before accepting it. Also, use Git (version control) to save backups.

**Q: What if I don't understand Cursor's explanation?**  
A: Ask follow-up questions! *"What does 'entry point' mean?"* or *"Explain that again like I'm 10 years old."*

**Q: How do I know if a change is "safe"?**  
A: Safe changes = only affect one small thing (text, colors, a single button). Unsafe = changes many files, changes how data flows, deletes things.

**Q: What's the difference between Agent and Plan Mode?**  
A: Agent = general AI assistant. Plan Mode = a special mode OF the Agent that plans before acting.

---

## What You've Learned

By the end of this guide, you can:
- ✅ Install and set up Cursor
- ✅ Ask Cursor to explain ANY codebase
- ✅ Get suggested improvements
- ✅ Make actual code changes using AI
- ✅ Review changes before accepting them
- ✅ Run tests to verify nothing broke
- ✅ Use planning mode for big/complex changes

**You're now a Cursor user!** 🎉

---

## Next Steps After Quickstart

Once you've made your first change:

1. Try Plan Mode on a slightly bigger task
2. Learn about **Understand your codebase** (deeper explanation features)
3. Learn about **Reviewing and testing code** (advanced verification)
4. Learn about **Build new features** (adding things from scratch)

---

## Real-World Practice Challenge

Try this exact workflow with a simple project:

**Project:** Create a file called `hello.html` with:
```html
<h1>Hello World</h1>
<p>This is my website</p>
```

**Challenge tasks:**
1. Ask Cursor to explain this tiny codebase (it'll be simple)
2. Ask for 3 improvements (it might suggest colors, fonts, etc.)
3. Pick one and have Cursor make the change
4. Review the diff
5. Open the file in a browser to see your change live

**You just did real AI-assisted coding!**

Would you like me to explain any specific step in more detail, or help you come up with a practice project to try this on?