This is the **Deeplinks** documentation – it explains how to share **prompts, commands, and rules** with others using special links. When someone clicks a deeplink, it opens Cursor with the content pre-filled.

Think of deeplinks as **shareable templates** – you can send a link to a teammate, and they can instantly add your prompt, command, or rule to their Cursor.

Let me break this down for a beginner.

---

## What Are Deeplinks? (The 10-Second Summary)

**Deeplinks allow you to share prompts, commands, and rules with others, enabling collaboration and knowledge sharing across teams and communities.**

| Without Deeplinks | With Deeplinks |
|-------------------|----------------|
| Copy-paste text manually | Click a link |
| Describe setup steps | One-click install |
| Version confusion | Always up-to-date link |

> *"Always review your prompts and commands before sharing to ensure they don't contain sensitive information like API keys, passwords, or proprietary code."*

---

## Opening Deeplinks (Two Ways)

### Method 1: In Cursor Desktop
Click the link – it opens directly in Cursor.

### Method 2: On the Web
Open via `cursor.com` by appending the path and URL parameters:

```
cursor.com/link/prompt?text=...
cursor.com/link/command?name=...&content=...
cursor.com/link/rule?name=...&content=...
```

---

## Important Security Note

> *"Always review your prompts and commands before sharing to ensure they don't contain sensitive information like API keys, passwords, or proprietary code."*

**Also:** Deeplinks never trigger automatic execution. The user must review and confirm before anything runs.

---

## Three Types of Deeplinks

| Type | What it shares | Opens in Cursor as |
|------|----------------|-------------------|
| **Prompt** | A chat prompt | Pre-filled in Agent chat |
| **Command** | A custom command | Saved in `.cursor/commands/` |
| **Rule** | A custom rule | Saved in `.cursor/rules/` |

---

## 1. Prompt Deeplinks

Share prompts that others can use to get started quickly with specific tasks or workflows.

### How It Works:

| Step | What happens |
|------|--------------|
| 1 | User clicks the deeplink |
| 2 | Cursor opens with prompt **pre-filled** in chat |
| 3 | User reviews the prompt |
| 4 | User confirms before execution |

> *"Deeplinks never trigger automatic execution."*

### Example:

**Link text:** "Research and find one bug in this codebase"  
**[Try In Cursor]** button

### URL Format:

```
cursor.com/link/prompt?text=Your prompt text here
```

---

## 2. Command Deeplinks

Share commands that others can execute directly in their Cursor environment.

### How It Works:

| Step | What happens |
|------|--------------|
| 1 | User clicks the deeplink |
| 2 | Cursor opens and creates a new command |
| 3 | User reviews the command |
| 4 | User confirms before saving |

### Command Name Rules:

> *"Use letters, numbers, dots, hyphens, and underscores only"*

**Allowed:** `debug-api`, `format-code`, `test-runner`  
**Not allowed:** Spaces, special characters (except `.`, `-`, `_`)

### Example:

**Name:** `debug-api`  
**Content:** `Add console.log statements to debug API responses`  
**[Add to Cursor]** button

### Where Commands Are Saved:

`.cursor/commands/<command-name>`

### URL Format:

```
cursor.com/link/command?name=command-name&content=command content
```

---

## 3. Rule Deeplinks

Share rules that others can add to their Cursor environment.

### How It Works:

| Step | What happens |
|------|--------------|
| 1 | User clicks the deeplink |
| 2 | Cursor opens and creates a new rule |
| 3 | User reviews the rule |
| 4 | User confirms before adding |

### Rule Name Rules:

> *"Use letters, numbers, dots, hyphens, and underscores only"*

**Allowed:** `typescript-strict`, `react-best-practices`, `code-quality`  
**Not allowed:** Spaces, special characters (except `.`, `-`, `_`)

### Example:

**Name:** `typescript-strict`  
**Content:** `Always use strict TypeScript types and avoid 'any'`  
**[Add to Cursor]** button

### Where Rules Are Saved:

`.cursor/rules/<rule-name>.mdc`

### URL Format:

```
cursor.com/link/rule?name=rule-name&content=rule content
```

---

## Playground Feature

The documentation shows a **Playground** section with:

| Language | Purpose |
|----------|---------|
| **TypeScript** | Test deeplinks with TypeScript examples |
| **Python** | Test deeplinks with Python examples |

This is likely for testing/development purposes.

---

## FAQ

The documentation lists these FAQs (full answers not shown):

| Question |
|----------|
| What is the maximum length for deeplink URLs? |
| How do I use deeplinks on the web instead of in the Cursor app? |

---

## Quick Reference Card

| Deeplink Type | Purpose | Opens as | URL format |
|---------------|---------|----------|------------|
| **Prompt** | Share a chat prompt | Pre-filled in chat | `cursor.com/link/prompt?text=...` |
| **Command** | Share a custom command | Saved in `.cursor/commands/` | `cursor.com/link/command?name=...&content=...` |
| **Rule** | Share a custom rule | Saved in `.cursor/rules/` | `cursor.com/link/rule?name=...&content=...` |

### Rules for Names:

- ✅ Letters (a-z)
- ✅ Numbers (0-9)
- ✅ Dots (.)
- ✅ Hyphens (-)
- ✅ Underscores (_)
- ❌ Spaces
- ❌ Special characters

---

## Common Beginner Questions

### Q: Are deeplinks safe?
**A:** They are safe because the user must review and confirm before anything runs. But still, don't share sensitive info.

### Q: Can I share a deeplink with someone outside my team?
**A:** Yes – deeplinks work for anyone with Cursor installed.

### Q: Can I open deeplinks on the web?
**A:** Yes – use `cursor.com/link/...` instead of `cursor://`.

### Q: What if the person doesn't have Cursor installed?
**A:** The link will prompt them to install Cursor first.

### Q: Can I use deeplinks for long prompts or rules?
**A:** There may be a URL length limit. The FAQ asks about maximum length.

### Q: Do deeplinks work on mobile?
**A:** They open in the Cursor web interface on mobile.

---

## Use Cases for Deeplinks

| Use Case | Type | Example |
|----------|------|---------|
| **Share a bug-finding prompt** | Prompt | "Find security vulnerabilities in this code" |
| **Share a custom command** | Command | `test-runner` command that runs all tests |
| **Share team coding standards** | Rule | TypeScript strict rules for the team |
| **Share a debugging workflow** | Prompt | "Debug this failed test" with context |
| **Share a code review checklist** | Rule | Rules for code review standards |

---

## The Bottom Line

**Deeplinks are shareable links that let you send prompts, commands, and rules to anyone with Cursor.**

**Think of it as:**
- **Without deeplinks** = "Copy this text and paste it into Cursor" 📋
- **With deeplinks** = "Click this link" 🔗

**For teams:** Deeplinks are great for:
1. **Onboarding** – Share setup prompts and rules
2. **Knowledge sharing** – Share debugging workflows
3. **Consistency** – Ensure everyone uses the same rules
4. **Community** – Share useful prompts on forums or social media

**Always remember:** Review what you're sharing for sensitive information, and users must confirm before anything runs.

Would you like me to explain any specific deeplink type in more detail?