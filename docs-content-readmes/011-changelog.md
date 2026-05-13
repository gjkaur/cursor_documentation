This is the **Cursor Changelog** – a diary of what's new, changed, or fixed in Cursor. Think of it as the "What's New" page for the software. It tells you about recent features and improvements.

Since this is a **release changelog** (focused on recent updates), I'll explain the key features mentioned in simple terms for a beginner.

Let me break down the major updates from these recent releases.

---

## Release: May 7, 2026 (Version 3.3)

### 1. PR Review (Pull Request Review) 🎯

**What is a PR (Pull Request)?**

In simple terms: When you finish coding a feature or bug fix, you create a "pull request" to ask your team to review your code before it becomes part of the main project. It's like raising your hand and saying *"Hey, can someone check my work before I merge it?"*

**What's new in Cursor?**

Cursor now has a **built-in PR review experience**. You can now:

| Feature | What it does |
|---------|--------------|
| **Reviews tab** | Shows comments from code reviewers inline |
| **Commits tab** | Shows the history of changes in the PR |
| **Changes tab** | Shows which files were changed, with a file tree for easy navigation |

**Quick action pills** let you take next steps faster (like "Approve PR" or "Request Changes").

**Why this matters for beginners:** If you're working on a team, you'll spend a lot of time reviewing code or getting your code reviewed. Having this inside Cursor means you don't have to switch to GitHub or GitLab to do it.

---

### 2. Build in Parallel from Plans 🔀

**What it means:** Cursor can now work on multiple tasks at the same time instead of one after another.

**Before:** Plan says "Step 1, then Step 2, then Step 3" → Cursor does Step 1 (wait), then Step 2 (wait), then Step 3.

**After:** Cursor can do Step 1 AND Step 2 AND Step 3 simultaneously (if they don't depend on each other).

**Example:** If your plan says:
1. Update the login page
2. Update the signup page
3. Update the password reset page

Cursor can now do all 3 at once. **Your changes happen faster.**

**Why this matters for beginners:** Less waiting = faster results. If you give Cursor a plan with independent tasks, it will finish much quicker.

---

### 3. Context Usage Breakdown 📊

**New feature:** You can now see a breakdown of what's taking up space in your AI's "context" (the memory/space the AI uses to understand your code).

**What you can see:**
- Rules (custom instructions you've given Cursor)
- Skills (specialized abilities you've enabled)
- MCPs (connections to other tools)
- Subagents (smaller AI helpers)

**Why this matters for beginners:** If Cursor seems slow or confused, you can check what's filling up its context. Too many rules or skills might be overwhelming it. Now you can diagnose and fix it.

---

## Release: May 4, 2026

### 4. Model Controls for Enterprise Admins 🛡️

**This is mainly for company administrators** (not individual users).

**What admins can now do:**

| Control | What it does |
|---------|--------------|
| **Allow/blocklist models** | Block GPT-5 but allow Claude, for example |
| **Block entire providers** | Block all OpenAI models at once |
| **Block by speed or context** | Block slow models or models with small context windows |
| **Default block new models** | Automatically block new models until approved |

**Why this matters:** Companies can control costs and security by limiting which AI models employees can use.

**For beginners:** You probably won't touch these settings unless you're an admin.

---

### 5. Soft Spend Limits and Intelligent Alerts 💰

**What's new:** Instead of hard limits (which block users completely), admins can now set **soft limits** with alerts.

**How it works:**

| Usage level | What happens |
|-------------|--------------|
| 50% of limit | User gets an alert: "You've used half your budget" |
| 80% of limit | User gets an alert: "You're getting close to your limit" |
| 100% of limit | User gets an alert: "You've reached your limit" |

**But the user can keep working** (with soft limits). Hard limits would block them completely.

**Why this matters for beginners:** If you're on a team, you'll get alerts before you hit your spending limit. No more surprise blocks in the middle of important work.

---

### 6. Updated Usage Analytics Tab 📈

**What admins can now see:**

| Filter | What it shows |
|--------|---------------|
| **By specific user** | Usage for just one team member |
| **By product surface** | Breakdown by: Clients, Cloud Agents, Automations, Bugbot, Security Review |

**Why this matters:** Teams can see exactly who is using how much, and which features are costing the most.

---

### 7. Team Marketplace Updates 🛒

**What's new:** Admins can create a team marketplace without connecting a repository first.

**Three installation behaviors for plugins:**

| Setting | What it means |
|---------|---------------|
| **Default Off** | Users can discover and choose to install |
| **Default On** | Installed by default, users can opt out |
| **Required** | Always installed, cannot uninstall |

**Why this matters:** Companies can enforce certain tools or plugins for all developers.

---

## Summary of What's New (For Beginners)

| Feature | What it does | Who cares? |
|---------|--------------|-------------|
| **PR Review** | Review code without leaving Cursor | Team developers |
| **Parallel execution** | Does multiple tasks at once | Everyone (faster!) |
| **Context breakdown** | See what's using AI memory | Power users, debugging |
| **Model controls** | Block/allow certain AI models | Admins |
| **Spend alerts** | Get warnings before hitting budget | Teams with budgets |
| **Usage analytics** | See who used what | Admins |
| **Team marketplace** | Control which plugins are available | Admins |

---

## For a Beginner: What Matters Most

The two features most relevant to you as a beginner are:

### 1. Parallel Execution ⚡
Your plans will execute faster. If you give Cursor a list of independent tasks, it will tackle them simultaneously. Less waiting!

### 2. Context Usage Breakdown 🔍
If Cursor ever seems lost or confused, you can check what's filling up its context. Maybe you added too many rules or enabled too many skills. Now you can see and fix it.

### 3. Spend Alerts (if on a team) 💰
If you're on a company team, you'll get friendly warnings before you hit your spending limit. No more sudden blocks!

---

## Changelog Format Explained

The changelog is organized by date (most recent first). Each entry includes:

| Element | Example |
|---------|---------|
| **Version** | 3.3 |
| **Date** | May 7, 2026 |
| **Feature name** | "PR Review, Build Plan in Parallel, and Split PRs" |
| **Description** | What changed and why it matters |
| **Screenshots** | Images showing the new features |

---

## How to Use the Changelog

| If you want to... | Do this |
|-------------------|---------|
| **Stay up to date** | Check the changelog monthly |
| **Learn about a new feature** | Read the description and look at screenshots |
| **See what changed in a specific version** | Look for the date or version number |
| **Report a bug** | The changelog tells you what was supposed to change |

---

## One Important Note

The PDF and PNG files you shared show **different content**:

- **The PDF** shows the real changelog entries (PR Review, Parallel Plans, Context Usage, etc.)
- **The PNG** has a bunch of repetitive "Change #X: Add Pull Request" lines (looks like a formatting/export error)

**Focus on the PDF content** – that's the real changelog for Cursor!

---

## Final Summary for Beginners

The **changelog** is Cursor's way of telling users: *"Hey, we added these cool new things!"*

**Key takeaways:**
- **PR Review** = Review code inside Cursor (no more switching to GitHub)
- **Parallel Plans** = Faster execution (Cursor does multiple tasks at once)
- **Context Breakdown** = See what's using AI memory (helps with debugging)
- **Spend Alerts** = Get warnings before hitting budget (no surprise blocks)

**For a beginner:** The most exciting feature is **parallel execution** – your AI assistant will work faster when you give it independent tasks. The context breakdown is also helpful if you run into issues.

Would you like me to explain any of these features in more detail, or help you understand how to use them in practice?