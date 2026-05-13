This is the **Rules** documentation – it explains how to give **persistent instructions** to the Agent. Rules are like having a **cheat sheet** that the AI reads before every task, ensuring it follows your preferences consistently.

Think of rules as **coding standards that the AI actually follows** – you don't have to repeat yourself every time.

Let me break this down for a complete beginner.

---

## What Are Rules? (The 10-Second Summary)

**Rules provide system-level instructions to Agent.** They bundle prompts, scripts, and more together, making it easy to manage and share workflows across your team.

| Without Rules | With Rules |
|---------------|------------|
| Repeat the same instructions every time | Agent always knows your preferences |
| Team members configure individually | Everyone gets same rules automatically |
| Inconsistent code style | Consistent across all projects |

> *"Large language models don't retain memory between completions. Rules provide persistent, reusable context at the prompt level."*

---

## The 4 Types of Rules

Cursor supports **four types** of rules, each for different situations:

| Rule Type | Where it lives | Who can use it | Best for |
|-----------|---------------|----------------|----------|
| **Project Rules** | `.cursor/rules` (in your codebase) | Anyone with the repo | Project-specific standards |
| **Team Rules** | Cursor Dashboard | Team/Enterprise plans | Organization-wide standards |
| **User Rules** | Your Cursor settings | Just you | Personal preferences |
| **AGENTS.md** | Project root (plain markdown) | Anyone | Simple, readable instructions |

---

## How Rules Work

When a rule is applied, its contents are **included at the start of the model context**. This gives the AI consistent guidance.

**Analogy:** Imagine telling a new team member: *"Before you start working, read this handbook."* Rules are that handbook for the AI.

---

## 1. Project Rules (Most Common for Beginners)

Project rules live in `.cursor/rules` as markdown files and are **version-controlled** (checked into git).

### File Structure:

```
.cursor/rules/
├── react-patterns.mdc      # Rule with frontmatter (description, globs)
├── api-guidelines.md        # Simple markdown rule
└── frontend/                # Organize rules in folders
    └── components.md
```

**File extensions:**
- `.md` – Simple markdown
- `.mdc` – Markdown with frontmatter metadata (more control)

### How Project Rules Are Applied:

| Rule Type | How it works |
|-----------|--------------|
| **Always Apply** | Rule is included in every chat session |
| **Apply Intelligently** | Agent decides when it's relevant based on description |
| **Apply to Specific Files** | Only applies when matching file pattern is in context |
| **Apply Manually** | Only when you `@mention` the rule in chat |

### The 3 Frontmatter Fields (For `.mdc` files):

| Field | What it does |
|-------|--------------|
| `alwaysApply` | If `true`, rule always included (ignores `description` and `globs`) |
| `description` | Tells Agent what the rule is about (used for intelligent matching) |
| `globs` | File patterns that trigger the rule |

### Rule Anatomy Examples:

#### Always Applied:
```yaml
---
alwaysApply: true
---
- All source files must include the company copyright header
- When you are unsure about implementation details, read the relevant source files
- Never modify generated files in the 'dist/*' or 'build/*' directories
```

#### Auto-attached by File Pattern:
```yaml
---
globs: src/components/**/*.tsx
alwaysApply: false
---
- Use named exports, not default exports
- Co-locate styles in a module CSS file next to the component
- Keep components under 200 lines
```

#### Agent-selected based on Description:
```yaml
---
description: RPC service conventions and patterns for the backend
alwaysApply: false
---
- Define each service in its own file under 'src/services/'
- Always validate inputs at the service boundary
- Return structured error objects with 'code' and 'message' fields
```

#### Manual (only via @mention):
```yaml
---
alwaysApply: false
---
- Every database migration must have both 'up' and 'down' functions
- Never alter a column type in-place. Add a new column, backfill, then drop
```

---

## Glob Pattern Examples (For File Scoping)

Use **globs** to scope a rule to specific files or directories:

| Pattern | What it matches |
|---------|-----------------|
| `*` | Any single file name segment |
| `**` | Any number of directories (recursive) |
| `*.ts` | All .ts files in the root |
| `**/*.ts` | All .ts files in any directory |
| `src/**` | All files anywhere under src/ |
| `src/**/*.tsx` | All .tsx files anywhere under src/ |
| `docs/**/*.md, docs/**/*.mdx` | .md and .mdx files under docs/ |
| `tailwind.config.*` | tailwind.config with any extension |

---

## Creating a Rule (2 Ways)

### Method 1: Via Chat (Easiest!)

Type `/create-rule` in Agent and describe what you want.

**Example:** `/create-rule Always use TypeScript for new files`

Agent generates the rule file with proper frontmatter and saves it to `.cursor/rules`.

### Method 2: Via Settings

1. Open **Cursor Settings > Rules, Commands**
2. Click **+ Add Rule**
3. Creates a new rule file in `.cursor/rules`

From settings you can see all rules and their status.

---

## Best Practices for Writing Rules

### DO ✅

| Practice | Why |
|----------|-----|
| **Keep rules under 500 lines** | Shorter rules are more likely to be followed |
| **Split large rules into multiple smaller ones** | Easier to manage and reuse |
| **Provide concrete examples** | "Like this file: @template.ts" |
| **Write rules like clear internal docs** | Be specific and actionable |
| **Reuse rules when repeating prompts** | Don't repeat yourself |
| **Reference files instead of copying contents** | Keeps rules short and prevents stale content |

### DON'T ❌

| Practice | Why |
|----------|-----|
| **Copying entire style guides** | Agent already knows common style conventions. Use a linter instead. |
| **Documenting every possible command** | Agent knows common tools (npm, git, pytest) |
| **Adding rarely-used edge cases** | Keep rules focused on frequent patterns |
| **Duplicating code from your codebase** | Point to canonical examples instead |

> *"Start simple. Add rules only when you notice Agent making the same mistake repeatedly. Don't over-optimize before you understand your patterns."*

---

## Check Rules Into Git

> *"Check your rules into git so your whole team benefits. When you see Agent make a mistake, update the rule. You can even tag @cursor on a GitHub issue or PR to have Agent update the rule for you."*

**This is powerful:** Your whole team gets the same AI guidance automatically.

---

## 2. Team Rules (For Organizations)

Team and Enterprise plans can create and enforce rules across their entire organization from the Cursor dashboard.

### Key Features:

| Feature | What it means |
|---------|---------------|
| **Enable immediately** | Rule is active as soon as you create it |
| **Enforce this rule** | Required for all team members (cannot be disabled) |
| **Not enforced** | Team members can toggle the rule off |

### How Team Rules Are Applied:

| Aspect | Behavior |
|--------|----------|
| **Content** | Free-form text (no folder structure) |
| **Glob patterns** | Supports file-scoped application (e.g., `**/*.py`) |
| **Where they apply** | Across ALL repositories and projects for that team |
| **Precedence** | Team Rules → Project Rules → User Rules |

> *"Some teams use enforced rules as part of internal compliance workflows. While this is supported, AI guidance should not be your only security control."*

---

## 3. User Rules (Personal Preferences)

User Rules are **global preferences** defined in Cursor Settings → Rules that apply across all projects.

### Perfect for:

- Setting preferred communication style
- Personal coding conventions
- Default behaviors

**Example:**
```
Please reply in a concise style. Avoid unnecessary repetition or filler language.
```

---

## 4. AGENTS.md (Simple Alternative)

**AGENTS.md** is a simple markdown file for defining agent instructions. Place it in your project root.

### Why use AGENTS.md?

| Instead of `.cursor/rules`... | Use AGENTS.md |
|-------------------------------|---------------|
| Complex frontmatter | Plain markdown |
| Multiple files | Single file |
| Configuration overhead | Simple and readable |

### Example AGENTS.md:

```markdown
# Project Instructions

## Code Style
- Use TypeScript for all new files
- Prefer functional components in React
- Use snake_case for database columns

## Architecture
- Follow the repository pattern
- Keep business logic in service layers
```

**Nested AGENTS.md supported** – you can have AGENTS.md in subdirectories!

---

## Importing Rules (Remote Rules via GitHub)

You can import rules directly from any GitHub repository.

### Steps:

| Step | Action |
|------|--------|
| 1 | Open Cursor Settings → Rules, Commands |
| 2 | Click + Add Rule next to Project Rules, select **Remote Rule (GitHub)** |
| 3 | Paste the GitHub repository URL |
| 4 | Cursor scans for all `.mdc` files and syncs them |

**Rules are placed in:** `.cursor/rules/imported/<repoName>/`

---

## Real-World Examples

### Example 1: Enforce TypeScript

**Rule (always apply):**
```yaml
---
alwaysApply: true
---
- Always use TypeScript for new files. Never use plain JavaScript.
- All functions must have explicit return types.
```

### Example 2: React Component Standards

**Rule (auto-attached to `.tsx` files):**
```yaml
---
globs: src/**/*.tsx
alwaysApply: false
---
- Use functional components with hooks, not class components
- Extract logic into custom hooks when reusable
- Keep components under 200 lines
```

### Example 3: API Design

**Rule (agent-selected):**
```yaml
---
description: REST API endpoint conventions for our backend
alwaysApply: false
---
- Use plural nouns for endpoints (/users not /user)
- Return 404 for not found, 400 for validation errors
- Always include a request ID in error responses
```

### Example 4: Team Rule (Enforced)

**From Dashboard:**
- Name: "GraphQL Standards"
- Content: "Always use Apollo Hooks for GraphQL queries"
- Enforced: ✅ Yes (cannot be disabled by developers)

---

## Common Beginner Questions

### Q: How do I know if my rule is being applied?
**A:** Check Cursor Settings → Rules to see rule status. You can also ask the Agent "What rules are active?"

### Q: Can rules reference other rules or files?
**A:** Yes, you can reference files using `@filename` syntax.

### Q: Do rules impact Cursor Tab or other AI features?
**A:** Rules primarily affect Agent (Chat). Some rules may affect other features.

### Q: Can I create a rule from chat?
**A:** Yes! Use `/create-rule` in Agent.

### Q: Do User Rules apply to inline Edit (Cmd/Ctrl+K)?
**A:** Check documentation – some rules may apply, others may not.

### Q: Why isn't my rule being applied?
**A:** Common issues:
- `alwaysApply: false` with no `description` or `globs` → only works via @mention
- Glob pattern might not match your files
- Rule might be disabled in settings

---

## Quick Reference Card

| Rule Type | Location | Scope | Best for |
|-----------|----------|-------|----------|
| **Project Rules** | `.cursor/rules/` | Current project | Project-specific standards |
| **Team Rules** | Dashboard | Entire organization | Company-wide standards |
| **User Rules** | Settings | All your projects | Personal preferences |
| **AGENTS.md** | Project root | Current project | Simple instructions |

| Application Mode | How it works |
|------------------|--------------|
| **Always Apply** | Every chat session |
| **Apply Intelligently** | Agent decides based on description |
| **Apply to Specific Files** | When glob pattern matches |
| **Apply Manually** | Only when @mentioned |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What are Rules?** | Persistent instructions that guide the Agent |
| **Why use them?** | Stop repeating yourself, ensure consistency |
| **Where do I put them?** | `.cursor/rules/` or use `/create-rule` in chat |
| **What's the simplest format?** | AGENTS.md in your project root |
| **Can my team share rules?** | Yes – check into git or use Team Rules |
| **How do I create a rule?** | `/create-rule` in chat or via Settings |

---

## The Bottom Line

**Rules are how you teach the Agent your preferences once, and it remembers forever.**

**Think of it as:**
- **Without Rules** = Training a new employee every day 📝
- **With Rules** = Giving them a handbook that never changes 📚

**For beginners:** Start with AGENTS.md – it's the simplest. Put a few basic instructions in your project root. As you notice the Agent making the same mistakes, add rules to `.cursor/rules/`. Use `/create-rule` in chat – it's magic.

**The most powerful feature:** Team Rules + enforcement. Your entire organization can have consistent AI guidance that developers cannot accidentally disable.

Would you like me to explain how to write effective rule content, or move on to another document?