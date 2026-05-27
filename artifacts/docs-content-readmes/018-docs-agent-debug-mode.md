This is the **Debug Mode** documentation – one of Cursor's most powerful features for fixing tricky bugs. Instead of guessing at fixes, Debug Mode acts like a **detective** – gathering evidence (logs), forming hypotheses, and only then making a fix.

Think of it as the difference between a doctor who guesses your illness vs. one who runs tests first.

Let me break this down for a complete beginner.

---

## What Is Debug Mode? (The 10-Second Summary)

**Debug Mode helps you find root causes and fix tricky bugs that are hard to reproduce or understand.**

Instead of immediately writing code (which might be wrong), the Agent:
1. Generates hypotheses about what's wrong
2. Adds log statements to collect evidence
3. Asks you to reproduce the bug
4. Analyzes the logs to find the real cause
5. Makes a **targeted fix** (often just a few lines)
6. Removes all the temporary logs when done

| Normal Agent Mode | Debug Mode |
|-------------------|------------|
| Guesses at the fix | Gathers evidence first |
| Might fix wrong thing | Finds actual root cause |
| Can make changes that don't help | Makes targeted, effective fixes |
| Leaves debugging code behind | Cleans up after itself |

**Toggle Debug Mode:** `Shift + Tab` or use the mode picker dropdown

---

## When to Use Debug Mode (vs. Normal Agent)

### ✅ USE Debug Mode for:

| Type of Bug | Example |
|-------------|---------|
| **Bugs you can reproduce but can't figure out** | "The app crashes when I click save, but I don't know why" |
| **Race conditions** | "Sometimes the data loads, sometimes it doesn't" |
| **Timing issues** | "The animation works 50% of the time" |
| **Performance problems** | "The page gets slower the longer I use it" |
| **Memory leaks** | "The app uses more memory over time" |
| **Regressions** | "This used to work, now it doesn't" |

### ❌ SKIP Debug Mode (use normal Agent) for:

| Situation | Why |
|-----------|-----|
| **Obvious bugs** | Missing semicolon, typo |
| **Clear error messages** | "Cannot read property 'x' of undefined" points directly to the issue |
| **Simple logic errors** | Wrong condition in an if statement |

> *"When standard Agent interactions struggle with a bug, Debug Mode provides a different approach using runtime evidence rather than guessing at fixes."*

---

## How Debug Mode Works (6 Steps)

| Step | What happens | Your role |
|------|--------------|-----------|
| **1** | Agent explores files and generates hypotheses | Watch/listen |
| **2** | Agent adds log statements (instrumentation) | Approve? (usually automatic) |
| **3** | Agent asks YOU to reproduce the bug | Follow the reproduction steps |
| **4** | Agent analyzes the logs | Wait |
| **5** | Agent makes a targeted fix | Review the fix |
| **6** | Agent removes all instrumentation | Verify the bug is gone |

Let me explain each step in detail:

---

### Step 1: Explore and Hypothesize 🔍

Agent reads relevant files and builds context. It generates **multiple hypotheses** about what might be causing the bug.

**Example hypotheses for a login bug:**
- Hypothesis A: The password hashing is wrong
- Hypothesis B: The database query is timing out
- Hypothesis C: The JWT token is expired
- Hypothesis D: There's a CORS issue

**Why multiple hypotheses?** The Agent doesn't want to guess – it wants to gather evidence to prove which one is right.

---

### Step 2: Add Instrumentation 📝

Agent adds **log statements** that send data to a local debug server running in a Cursor extension.

**What are logs?** Messages that print to the console when code runs.

**Example instrumentation:**
```javascript
// Before
function login(username, password) {
  const user = db.findUser(username);
  return user.password === password;
}

// After (Agent adds logs)
function login(username, password) {
  console.log('[DEBUG] login called with username:', username);
  console.log('[DEBUG] password length:', password.length);
  
  const user = db.findUser(username);
  console.log('[DEBUG] user found:', !!user);
  
  const result = user && user.password === password;
  console.log('[DEBUG] login result:', result);
  
  return result;
}
```

**Important:** These logs go to a **debug server**, not your normal console. The Agent will read them.

---

### Step 3: Reproduce the Bug 🎮

Debug Mode **asks you to reproduce the bug** and provides specific steps.

**What Agent might say:**
> *"Please follow these steps to trigger the bug:*
> 1. *Open the login page*
> 2. *Enter username 'test@example.com'*
> 3. *Enter password 'password123'*
> 4. *Click the Login button*
> 5. *Wait for the error message"*

**Why this matters:**
- Keeps you in the loop
- Ensures the Agent captures real runtime behavior
- You're the one who knows how to trigger the bug

---

### Step 4: Analyze Logs 📊

After you reproduce the bug, the Agent **reviews the collected logs** to identify the actual root cause based on runtime evidence.

**Example log analysis:**
```
[DEBUG] login called with username: test@example.com
[DEBUG] password length: 12
[DEBUG] user found: true
[DEBUG] login result: false  <-- !!! This is wrong! Password should match!
```

**Agent's conclusion:** "The user exists, but the password comparison is failing. The issue is likely in password hashing or comparison logic."

**Notice:** The Agent didn't guess – it **proved** the problem using logs.

---

### Step 5: Make Targeted Fix 🎯

Agent makes a **focused fix** that directly addresses the root cause.

**Key insight:** The fix is often **just a few lines of code**.

**Example fix:**
```javascript
// Before (buggy)
function login(username, password) {
  const user = db.findUser(username);
  return user.password === password; // Problem: password isn't hashed!
}

// After (fixed)
function login(username, password) {
  const user = db.findUser(username);
  return bcrypt.compare(password, user.passwordHash); // Compare hashed password
}
```

**Why small fixes?** The Agent found the exact cause, so it can make a precise change.

---

### Step 6: Verify and Clean Up 🧹

**You** re-run the reproduction steps to verify the bug is fixed.

**Then:** The Agent **removes all instrumentation** (the temporary logs).

```javascript
// Cleaned up code (back to normal)
function login(username, password) {
  const user = db.findUser(username);
  return bcrypt.compare(password, user.passwordHash);
}
```

**No leftover debugging code cluttering your project!**

---

## Debug Mode vs. Normal Agent: A Real Example

### The Bug:
The shopping cart total is sometimes wrong. It works 80% of the time, fails 20%.

### Normal Agent Approach:
Agent guesses: "Maybe it's a floating point error." Adds a fix for floating point. Doesn't help. Guesses again: "Maybe it's missing an item." Adds another fix. Still not working. You waste 30 minutes.

### Debug Mode Approach:

| Step | What happens |
|------|--------------|
| 1 | Agent adds logs to cart calculation |
| 2 | You add items, reproduce the wrong total |
| 3 | Logs show: "Item price: $10.00, Quantity: 3, Total: $29.99" |
| 4 | Agent realizes: "The tax is being applied twice on some items" |
| 5 | Agent fixes the duplicate tax calculation (3 lines of code) |
| 6 | You verify: Totals are now correct |

**Time saved:** 20+ minutes

---

## Tips for Using Debug Mode

### 1. Provide Detailed Context

| What to include | Example |
|----------------|---------|
| **How to reproduce** | "Click login, enter 'test@test.com', password '123', click submit" |
| **Error messages** | Paste the full error stack trace |
| **Expected behavior** | "It should show 'Welcome, user'" |
| **Actual behavior** | "It shows 'Network error' instead" |

> *"The more you describe the bug and how to reproduce it, the better the agent's instrumentation will be."*

### 2. Follow Reproduction Steps Exactly

The Agent gives you specific steps. Follow them precisely. If you deviate, the logs might not capture the issue.

### 3. Reproduce Multiple Times if Needed

For tricky problems like **race conditions**, reproducing the bug multiple times helps the Agent see patterns.

**Example:** A bug happens 1 in 10 clicks. Reproduce it 5 times so logs show the pattern.

### 4. Be Specific About Expected vs. Actual

Help the Agent understand what **should** happen versus what **is** happening.

**Good:** "When I click Save, it should show 'Saved!' but instead it shows 'Error'"

**Bad:** "The save thing doesn't work"

---

## Switching Modes

| Method | How to do it |
|--------|--------------|
| **Keyboard shortcut** | Press `Shift + Tab` |
| **Dropdown menu** | Click the mode picker in Agent |

**You can switch modes anytime**, even mid-conversation.

---

## Debug Mode vs. Other Modes

| Mode | Best for | Approach |
|------|----------|----------|
| **Normal Agent** | Building features, simple fixes | Write code immediately |
| **Plan Mode** | Complex features, unclear requirements | Plan first, then build |
| **Debug Mode** | Tricky bugs, runtime issues | Gather evidence, then fix |
| **Agent Review** | Checking your changes | Review existing code |

---

## Common Beginner Questions

### Q: Does Debug Mode change my code permanently?
**A:** No. It adds temporary logs that are removed after verification.

### Q: How long does Debug Mode take?
**A:** Longer than normal Agent for simple bugs, but MUCH faster for complex ones.

### Q: Can I use Debug Mode for any bug?
**A:** Yes, but it's overkill for obvious bugs. Use it when you're stuck.

### Q: What if the reproduction steps don't trigger the bug?
**A:** Tell the Agent! It will adjust the instrumentation and try again.

### Q: Does Debug Mode work for backend bugs?
**A:** Yes, it works for any code that can log output.

### Q: Can I see the logs Debug Mode collects?
**A:** Possibly in the debug server interface. The Agent analyzes them automatically.

---

## Quick Reference Card

| Feature | Details |
|---------|---------|
| **What it does** | Finds root causes using runtime evidence |
| **Toggle shortcut** | `Shift + Tab` |
| **Best for** | Tricky bugs, race conditions, performance issues |
| **Not for** | Obvious bugs, typos |
| **Key steps** | Hypothesize → Instrument → Reproduce → Analyze → Fix → Clean up |
| **Output** | Targeted fix (often just a few lines) |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is Debug Mode?** | Evidence-based bug fixing |
| **When to use?** | When you're stuck on a tricky bug |
| **How is it different?** | It adds logs, collects evidence, then fixes |
| **Does it change my code permanently?** | No – logs are removed after |
| **How do I start?** | `Shift + Tab` to Debug Mode, then describe the bug |

---

## The Bottom Line

**Debug Mode is like having a detective on your team instead of a guesser.**

**Think of it as:**
- **Normal Agent** = Doctor who prescribes medicine without tests 🩺 (risky)
- **Debug Mode** = Doctor who runs tests, then prescribes the right medicine 🔬 (effective)

**For beginners:** When you encounter a bug that has you scratching your head – the kind where you've tried 3 different fixes and nothing works – THAT'S when you use Debug Mode. It will systematically find the real cause and fix it.

**The most important insight:** Debug Mode doesn't guess. It gathers **runtime evidence** (logs) to prove what's wrong before fixing it.

**The result:** Instead of trying 5 wrong fixes over 30 minutes, Debug Mode finds the right fix in 5 minutes.

