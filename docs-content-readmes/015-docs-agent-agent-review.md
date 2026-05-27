This is the **Agent Review** documentation – a feature that automatically reviews your code changes and catches issues before they become problems.

Think of Agent Review as having a **senior developer look over your shoulder** every time you make changes, pointing out potential bugs, style issues, or security problems.

Let me break this down for a complete beginner.

---

## What Is Agent Review? (The 10-Second Summary)

**Agent Review runs a dedicated code review on your local changes from inside Cursor.**

Instead of waiting for a human teammate to review your code (which can take hours or days), Agent Review does it **instantly** using AI.

| Without Agent Review | With Agent Review |
|---------------------|-------------------|
| You write code | You write code |
| You commit/push | Agent Review checks your changes |
| Wait for human review | **Instant AI feedback** |
| Fix issues days later | Fix issues immediately |

---

## Setup (One-Time Configuration)

Setting up Agent Review is simple:

```
Step 1: Open Cursor Settings
Step 2: Go to "Agents"
Step 3: Find "Agent Review"
Step 4: Configure your preferences
```

### Two Review Modes:

| Mode | What happens |
|------|--------------|
| **Automatic** | Runs after every commit (set it and forget it) |
| **Manual** | You trigger it yourself when you want a review |

### Custom Rules (Advanced)

Agent Review can read rules from `BUGBOT.md` files. This lets you define custom review guidelines like:

```markdown
# My Coding Rules
- Always use TypeScript over JavaScript
- Never use console.log in production code
- All API calls must have error handling
```

**For beginners:** Start with the default settings. Add custom rules as you learn what you want to enforce.

---

## 3 Ways to Run a Review

| Method | How to do it | Best for |
|--------|--------------|----------|
| **Automatic** | Enable in settings | "Set it and forget it" – reviews every commit |
| **Slash command** | Type `/agent-review` in agent window | On-demand review when you want it |
| **Source Control tab** | Open Source Control → Run Agent Review | Reviewing ALL local changes against main branch |

### The Source Control tab method is special:

Instead of just reviewing your last edit, it compares **all your local changes** against your main branch. This catches issues across your full set of changes.

**Example:** You've been working for 3 days on a feature. Run Agent Review from Source Control to review everything at once before merging.

---

## Review Depth: Quick vs. Deep

Agent Review offers **two depth levels**. Choose based on your needs:

| Depth | Speed | Cost | Best for |
|-------|-------|------|----------|
| **Quick** | Fast ⚡ | Low 💰 | Small diffs, formatting changes, fast sanity check |
| **Deep** | Slow 🐢 | High 💰💰 | Complex logic, security-sensitive code, large refactors |

### When to use each:

| Use Quick when... | Use Deep when... |
|-------------------|------------------|
| Fixing a typo | Rewriting a core function |
| Changing a color | Adding authentication |
| Formatting code | Working with sensitive data |
| Small, obvious changes | Large refactors (many files) |
| You just want a sanity check | You need thorough analysis |

---

## What Agent Review Looks For

While the documentation doesn't list everything, here's what typical AI code reviews catch:

| Category | Examples |
|----------|----------|
| **Bugs** | Null pointer errors, off-by-one mistakes, missing error handling |
| **Security** | Exposed API keys, SQL injection risks, unsafe data handling |
| **Style** | Inconsistent formatting, naming convention violations |
| **Performance** | Inefficient loops, unnecessary re-renders, memory leaks |
| **Best practices** | Deprecated functions, anti-patterns, code smells |
| **Edge cases** | Empty states, missing validation, boundary conditions |

---

## Real-World Example

### Scenario: You're adding a login feature

**You write this code:**
```javascript
function login(username, password) {
  const user = db.findUser(username);
  if (user.password === password) {
    return { success: true, token: "abc123" };
  }
  return { success: false };
}
```

**Agent Review (Deep) might flag:**
1. ❌ Password comparison is vulnerable to timing attacks
2. ❌ No password hashing (storing plain text?)
3. ❌ Token is hardcoded ("abc123")
4. ❌ No rate limiting (vulnerable to brute force)
5. ❌ No logging of failed attempts

**Agent Review suggests:**
```javascript
function login(username, password) {
  // 1. Rate limit check
  // 2. Find user
  // 3. Compare hashed password using constant-time comparison
  // 4. Generate secure JWT token
  // 5. Log attempt
  // 6. Return result
}
```

**Without Agent Review:** You'd commit this, a teammate would find these issues days later, and you'd have to fix them after the fact.

**With Agent Review:** You find and fix everything immediately.

---

## Agent Review vs. Human Review

| Aspect | Agent Review | Human Review |
|--------|--------------|--------------|
| **Speed** | Instant (seconds) | Hours to days |
| **Availability** | 24/7 | Business hours only |
| **Consistency** | Always the same | Varies by person |
| **Cost** | Included in your plan | Team member's time ($) |
| **Nuance** | Can miss context | Understands business logic |
| **Best for** | First pass, catching obvious issues | Final approval, complex decisions |

**Best practice:** Use **Agent Review first** (catch obvious issues), then send to **humans** (for nuanced feedback).

---

## Integration with BugBot

Agent Review reads rules from `BUGBOT.md` files. BugBot is Cursor's automated bug-finding tool.

**What this means:** You can write rules once in a `BUGBOT.md` file, and both BugBot AND Agent Review will follow them.

**Example `BUGBOT.md`:**
```markdown
# Security Rules
- Never commit API keys
- All database queries must use parameterized statements

# Style Rules  
- Use 2 spaces for indentation
- Maximum line length: 100 characters
```

**For beginners:** You don't need to worry about this initially. Just know it exists for advanced customization.

---

## Beginner's Guide to Using Agent Review

### Step 1: Enable Automatic Reviews
Go to Settings → Agents → Agent Review → Turn on "Automatic after commits"

### Step 2: Make a change
Write some code, save it, commit it.

### Step 3: Review the feedback
Agent Review will show you:
- What issues it found
- Where they are (file + line number)
- Suggestions for fixing them

### Step 4: Fix the issues
Use the Agent to fix the problems, or fix them manually.

### Step 5: Commit again
Agent Review will run again on your fixes.

### For manual reviews:
Type `/agent-review` in the agent window anytime you want a review.

---

## Settings to Consider

| Setting | Recommendation for beginners |
|---------|------------------------------|
| **Automatic after commits** | ✅ ON – catches issues early |
| **Review depth** | Quick for most tasks, Deep for important changes |
| **Custom rules** | Start empty, add as you learn |
| **Run on all local changes** | ✅ ON when using Source Control tab |

---

## Common Beginner Questions

### Q: Does Agent Review cost extra?
**A:** It uses your existing usage (tokens). Quick reviews are cheap, Deep reviews cost more.

### Q: Can Agent Review approve my code for merging?
**A:** No, it suggests improvements. A human still needs to approve.

### Q: What if Agent Review is wrong?
**A:** It happens! Use your judgment. You can ignore suggestions.

### Q: Will Agent Review slow down my commits?
**A:** Quick reviews are very fast (seconds). Deep reviews take longer but you control when to run them.

### Q: Can I use Agent Review without Git?
**A:** The Source Control tab method requires Git. The slash command works anytime.

### Q: What's the difference between Agent Review and BugBot?
**A:** BugBot finds bugs automatically. Agent Review is a specific review you run on your changes. They share the same rule system.

---

## Pro Tips

### Tip 1: Run Deep review before big merges
Before merging a feature branch, run a Deep review on all changes.

### Tip 2: Use Quick review for fast feedback
While actively coding, run Quick reviews to catch issues early.

### Tip 3: Create custom rules for your team
If your team has specific standards, put them in `BUGBOT.md`.

### Tip 4: Don't skip reviews on "small" changes
Small changes can have big bugs. Let Agent Review check everything.

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is it?** | AI-powered code review for your changes |
| **How to start?** | Settings → Agents → Agent Review |
| **Quick vs Deep?** | Quick = fast/cheap; Deep = thorough/expensive |
| **3 ways to run?** | Automatic, `/agent-review` slash command, Source Control tab |
| **Cost?** | Uses your token usage |
| **Can it approve code?** | No, suggests improvements only |

---

## The Bottom Line

**Agent Review is like having a senior developer instantly review every change you make.**

**Think of it as:**
- **Without review** = Sending an email without spell-check ✉️
- **With Agent Review** = Running spell-check before sending ✨

**For beginners:** Turn on automatic reviews after commits. You'll catch mistakes immediately instead of days later. Use Quick reviews for daily work, Deep reviews for important changes.

**The best part:** It works 24/7, never gets tired, and is always consistent. Your human teammates will thank you for sending them cleaner code.

