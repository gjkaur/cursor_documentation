This is the **Browser Tool** documentation – it explains how the Agent can **control a web browser** to test applications, debug visual issues, convert designs into code, and more.

Think of the Browser tool as giving the Agent **eyes and hands to interact with websites** – it can see what's on the screen, click buttons, type text, and read console errors.

Let me break this down for a complete beginner.

---

## What Is the Browser Tool? (The 10-Second Summary)

**Agent can control a web browser** to test applications, visually edit layouts, audit accessibility, convert designs into code, and debug issues.

With access to **console logs** and **network traffic**, the Agent can see what's going wrong in your web app and fix it.

| Without Browser Tool | With Browser Tool |
|---------------------|-------------------|
| You manually test and report issues | Agent tests automatically |
| You describe visual bugs in words | Agent sees the actual page |
| You copy error messages manually | Agent reads console logs directly |

---

## What Can Agent Do with the Browser?

The Browser tool gives the Agent these capabilities:

| Capability | What it does |
|------------|--------------|
| **Navigate** | Go to URLs (localhost, production sites, etc.) |
| **Click** | Click buttons, links, and interactive elements |
| **Type** | Fill out forms, enter text |
| **Scroll** | Move around the page |
| **Screenshot** | Take pictures of what it sees |
| **Console Output** | Read JavaScript errors and warnings |
| **Network Traffic** | See API calls and network requests |

---

## Native Integration: How Agent "Sees" Your App

Cursor has optimized the browser tool to be efficient and powerful:

### 1. Efficient Log Handling 📝
Browser logs are written to files. Agent can **grep** (search) and selectively read only what it needs.

**Why this matters:** Instead of dumping thousands of lines of logs after every action, Agent reads only the relevant lines. This saves tokens and keeps context clean.

### 2. Visual Feedback with Images 🖼️
Screenshots are integrated directly with the file reading tool. Agent **actually sees** the browser state as images, not text descriptions.

**Why this matters:** Better understanding of visual layouts and UI elements. Agent can see that a button is misaligned, not just read code that says it might be.

### 3. Smart Prompting 🧠
Agent receives additional context about browser logs, including total line counts and preview snippets.

**Why this matters:** Helps Agent make informed decisions about what to inspect without reading everything.

### 4. Development Server Awareness 🚀
Agent is prompted to detect running development servers and use the correct ports.

**Why this matters:** Instead of starting duplicate servers or guessing port numbers, Agent finds your running `localhost:3000` or `localhost:5173` automatically.

**You can use Browser without installing or configuring any external tools!**

---

## The Design Sidebar: Visual Editing 🎨

The browser includes a **design sidebar** for modifying your site directly in Cursor. You can design and code simultaneously with real-time visual adjustments.

### Visual Editing Capabilities:

| Control | What you can do |
|---------|-----------------|
| **Position and layout** | Move elements, change flex direction, alignment, grid layouts |
| **Dimensions** | Adjust width, height, padding, margins with pixel values |
| **Colors** | Update colors from design system, visual color picker |
| **Appearance** | Shadows, opacity, border radius with visual sliders |
| **Theme testing** | Test across light and dark themes instantly |

### Applying Changes:

When your visual adjustments match your vision, click the **apply button** to trigger an agent that updates your codebase. The agent translates your visual changes into the appropriate code modifications.

**You can also select multiple elements across your site and describe changes in text.** Agents kick off in parallel!

---

## Session Persistence 🔄

Browser state **persists** between Agent sessions based on your workspace:

| What persists | Example |
|---------------|---------|
| **Cookies** | Authentication cookies – stay logged in between sessions |
| **Local Storage** | User preferences, saved data |
| **IndexedDB** | Database content |

**Isolation:** Each workspace has its own browser context. Different projects maintain separate storage and cookie states.

---

## Key Use Cases (When to Use Browser Tool)

### 1. Web Development Workflow 🌐

Browser integrates with tools like Figma and Linear. Test your app, see visual changes, and track issues all from Cursor.

### 2. Accessibility Improvements ♿

Agent can audit and improve web accessibility to meet WCAG compliance standards.

**Example prompt:**
> `@browser` "Check color contrast ratios, verify semantic HTML and ARIA labels, test keyboard navigation, and identify missing alt text"

### 3. Automated Testing ✅

Agent can execute comprehensive test suites and capture screenshots for visual regression testing.

**Example prompt:**
> `@browser` "Fill out forms with test data, click through workflows, test responsive designs, validate error messages, and monitor console for JavaScript errors"

### 4. Design to Code 🎨→💻

Agent can convert designs into working code with responsive layouts.

**Example prompt:**
> `@browser` "Analyze this design mockup, extract colors and typography, and generate pixel-perfect HTML and CSS code"

### 5. Adjusting UI Design from Screenshots 📸

Agent can refine existing interfaces by identifying visual discrepancies.

**Example prompt:**
> `@browser` "Compare current UI against this design screenshot and adjust spacing, colors, and typography to match"

---

## Security Features 🔒

The Browser runs as a **secure web view** and is controlled using an MCP server. Multiple layers protect you.

### Authentication and Isolation:

| Measure | What it does |
|---------|--------------|
| **Token authentication** | Random token generated before each session |
| **Tab isolation** | Each tab gets a unique random ID |
| **Session-based security** | Tokens regenerate for each new session |

**Cursor's Browser integrations have been reviewed by multiple external security auditors.**

---

## Approval Settings (Important!)

Browser tools require your **approval by default**. You review each action before Agent executes it.

### Available Modes:

| Mode | Description | Recommended for |
|------|-------------|-----------------|
| **Manual approval** | Review and approve each action individually | **Most users (safest)** |
| **Allow-listed actions** | Trusted actions run automatically; others ask | Power users |
| **Auto-run** | All actions execute immediately | **Use with extreme caution** |

### ⚠️ WARNING from the docs:

> *"Never use auto-run mode with untrusted code or unfamiliar websites. Agent could execute malicious scripts or submit sensitive data without your knowledge."*

**For beginners:** Stick with **Manual approval** until you understand what the Browser tool can do.

---

## Allow and Block Lists

Configure which browser actions run automatically:

| List | What it does |
|------|--------------|
| **Allow list** | Trusted actions that skip approval prompts |
| **Block list** | Actions that should always be blocked |

**Access settings:** Cursor Settings → Chat → Auto-Run

**Important note:** The allow/block list system provides **best-effort protection**. AI behavior can be unpredictable due to prompt injection and other issues. Review auto-approved actions regularly.

---

## Recommended Models

For the best Browser performance, use:

| Model | Why |
|-------|-----|
| **Claude 4.5 Sonnet** | Strong visual understanding |
| **GPT-5** | Good all-around |
| **Auto** | Let Cursor choose |

---

## Enterprise: Origin Allowlist

For enterprise customers, admins can restrict which sites the agent can automatically navigate to.

### How it works:

| Setting | Behavior |
|---------|----------|
| **Allowlist configured** | Agent can only navigate to allowed origins (e.g., `localhost:3000`, `https://yourcompany.com`) |
| **Allowlist empty** | All origins allowed (default) |

### Behavior with allowlist:

| Action | Result |
|--------|--------|
| **Automatic navigation** | Only allowed origins work |
| **MCP tool execution** | Only runs on allowed origins |
| **Manual navigation** | User can still go anywhere (for docs, external sites) |
| **Tool restrictions** | On non-allowed origins, browser tools are blocked |

### Edge Cases (Important!):

| Situation | What happens |
|-----------|--------------|
| **Link to non-allowed origin** | Navigation succeeds (agent clicked a link) |
| **Redirect to non-allowed origin** | Redirect permitted |
| **JavaScript navigation** | Client-side navigation succeeds |

> *"The origin allowlist restricts automatic agent navigation but cannot prevent all navigation paths."*

---

## Real-World Examples

### Example 1: Testing a Login Form

**You say:**
> `@browser` "Go to localhost:3000/login, type 'test@example.com' in email, type 'password123' in password, click login, and tell me if you see an error"

**Agent does:**
1. Navigates to localhost:3000/login
2. Types email
3. Types password
4. Clicks login
5. Takes screenshot
6. Reads console for errors
7. Reports: "The login API returned a 500 error. Here's the stack trace..."

### Example 2: Visual Bug Fix

**You say:**
> *[paste screenshot of broken layout]* `@browser` "Compare this screenshot with the actual page on localhost:3000. The button is misaligned. Fix the CSS."

**Agent does:**
1. Opens browser to your page
2. Takes screenshot
3. Compares with your image
4. Identifies margin/padding issue
5. Edits the CSS file
6. Refreshes browser to verify fix

### Example 3: Accessibility Audit

**You say:**
> `@browser` "Audit my homepage at localhost:3000 for accessibility issues"

**Agent does:**
1. Navigates to page
2. Checks color contrast
3. Verifies ARIA labels
4. Tests keyboard navigation
5. Lists missing alt text
6. Provides fixes

---

## Common Beginner Questions

### Q: Does the Browser tool work on production websites?
**A:** Yes, but be careful. Never enter sensitive information or use on untrusted sites.

### Q: Can Agent see my passwords?
**A:** Agent can see what's typed in the browser. Never ask it to handle real passwords.

### Q: How do I know what Agent is doing in the browser?
**A:** You see screenshots and actions in the chat. With manual approval, you approve each action.

### Q: Can Agent click on anything?
**A:** Yes, but you approve each click by default (unless you change settings).

### Q: Does Browser work on mobile?
**A:** The documentation mentions responsive design testing, but the browser runs on your computer.

### Q: Can multiple agents use the browser at once?
**A:** Each workspace has isolated browser context. Multiple tabs have unique IDs to prevent interference.

---

## Quick Reference Card

| Feature | Details |
|---------|---------|
| **What it does** | Agent controls a web browser |
| **Capabilities** | Navigate, click, type, scroll, screenshot, read console/network |
| **Design sidebar** | Visual editing with real-time updates |
| **Approval default** | Manual approval for each action |
| **Session persistence** | Cookies/local storage saved per workspace |
| **Recommended models** | Claude 4.5 Sonnet, GPT-5, Auto |
| **Enterprise** | Origin allowlist for site restrictions |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is the Browser tool?** | Lets Agent control a web browser |
| **What can Agent do?** | Navigate, click, type, take screenshots, read errors |
| **Is it safe?** | Yes – requires approval by default, multiple security layers |
| **What's the Design Sidebar?** | Visual editor – change designs by clicking/dragging |
| **Can Agent fix visual bugs?** | Yes – sees the page, identifies issues, edits code |
| **Do I need to install anything?** | No – works out of the box |

---

## The Bottom Line

**The Browser tool gives the Agent eyes and hands to test and debug your web applications.**

**Think of it as:**
- **Without Browser** = Telling a blindfolded person about a painting 🖼️🙈
- **With Browser** = The person can see the painting and point to what's wrong 🖼️👀

**For beginners:** Start with manual approval. Use it to test your local development server. Try simple tasks like "Go to my page and take a screenshot." As you get comfortable, try more complex testing and visual editing.

**The most exciting features:**
1. **Visual editing** – Change designs by clicking and dragging
2. **Console access** – Agent reads JavaScript errors automatically
3. **Session persistence** – Stays logged in between sessions
4. **Design to code** – Convert screenshots into working code

Would you like me to explain any specific browser capability in more detail, or move on to another document?