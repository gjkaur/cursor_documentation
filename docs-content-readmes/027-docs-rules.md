I see you've shared the **Rules** documentation again. This appears to be the same as the previous Rules document (from `screencapture-cursor-docs-rules-2026-05-09-16_05_55.pdf`).

Since I already provided a **detailed explanation** of Rules in my previous response, let me instead give you a **quick reference summary** of the key points, plus some additional practical examples and troubleshooting tips.

---

## Rules: Quick Reference Card

### The 4 Types of Rules

| Type | Location | Scope |
|------|----------|-------|
| **Project Rules** | `.cursor/rules/` | Current project only |
| **Team Rules** | Cursor Dashboard | Entire organization |
| **User Rules** | Cursor Settings | All your projects |
| **AGENTS.md** | Project root | Current project (simple) |

---

### How Rules Are Applied

| Application Mode | How it works |
|------------------|--------------|
| **Always Apply** | Rule is included in every chat session |
| **Apply Intelligently** | Agent decides when relevant based on description |
| **Apply to Specific Files** | Only when file matches glob pattern |
| **Apply Manually** | Only when you `@mention` the rule |

---

### Quick Rule Creation

**Easiest method:** In chat, type:
```
/create-rule Always use TypeScript for new files
```

Agent generates the rule file automatically.

---

### Simple Rule Examples

#### AGENTS.md (simplest - put in project root):
```markdown
# Code Style
- Use TypeScript for all new files
- Use functional components in React
- Never use console.log in production
```

#### Project Rule (.cursor/rules/):
```yaml
---
alwaysApply: true
---
- All API endpoints must have error handling
- Use environment variables for secrets
- Write tests for new features
```

---

### Common Issues & Fixes

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
| Rule not applied | `alwaysApply: false` with no description/globs | Add description or use @mention |
| Rule not working for specific files | Wrong glob pattern | Test pattern with glob tester |
| Team rule not showing | Not enforced, user disabled it | Check user settings or enforce rule |

---

### Best Practices (Reminder)

- ✅ Keep rules under 500 lines
- ✅ Split large rules into smaller ones
- ✅ Reference files instead of copying content
- ✅ Check rules into git for team sharing
- ❌ Don't copy entire style guides (use linter)
- ❌ Don't document every command (Agent knows common tools)

---

Would you like me to:
1. Explain a specific aspect of Rules in more detail?
2. Move on to another document?
3. Help you write a specific rule for your use case?