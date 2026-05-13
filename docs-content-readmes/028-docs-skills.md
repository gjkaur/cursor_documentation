This is the **Agent Skills** documentation – it explains how to extend Cursor's AI with **specialized capabilities**. Skills are like **training modules** that teach the agent how to perform specific tasks.

Think of skills as **plug-and-play expertise** – you can give the agent a "deploy app" skill, and it will learn the exact steps to deploy your app.

Let me break this down for a complete beginner.

---

## What Are Skills? (The 10-Second Summary)

**A skill is a portable, version-controlled package that teaches agents how to perform domain-specific tasks.** Skills can include scripts, templates, and references that agents can act on using their tools.

| Without Skills | With Skills |
|----------------|--------------|
| You explain steps every time | Agent already knows the workflow |
| Agent guesses how to deploy | Agent follows your exact deployment process |
| Inconsistent results | Predictable, repeatable outcomes |

> *"Agent Skills is an open standard for extending AI agents with specialized capabilities."*

---

## Key Properties of Skills

| Property | What it means |
|----------|---------------|
| **Portable** | Skills work across any agent that supports the Agent Skills standard |
| **Version-controlled** | Stored as files, tracked in your repository, installed via GitHub |
| **Actionable** | Can include scripts, templates, and references agents can run |
| **Progressive** | Load resources on demand, keeping context usage efficient |

---

## How Skills Work

1. **Cursor automatically discovers** skills from skill directories when it starts
2. **Agent sees available skills** and decides when they're relevant based on context
3. **Manual invocation**: Type `/` in Agent chat and search for the skill name

**You don't need to tell the agent which skill to use** – it figures it out from context!

---

## Skill Directories (Where to Put Skills)

Skills are automatically loaded from these locations:

| Location | Scope |
|----------|-------|
| `.agents/skills/` | Project-level |
| `.cursor/skills/` | Project-level |
| `~/.agents/skills/` | User-level (global) |
| `~/.cursor/skills/` | User-level (global) |

### Compatibility with Other Tools:

Cursor also loads skills from Claude and Codex directories:
- `.claude/skills/`
- `.codex/skills/`
- `~/.claude/skills/`
- `~/.codex/skills/`

**This means skills you create for Claude or Codex work in Cursor!**

---

## Skill Folder Structure

### Minimal Skill:

```
.agents/skills/
└── my-skill/
    └── SKILL.md
```

### Full Skill with Optional Directories:

```
.agents/skills/
└── deploy-app/
    ├── SKILL.md
    ├── scripts/
    │   ├── deploy.sh
    │   └── validate.py
    ├── references/
    │   └── REFERENCE.md
    └── assets/
        └── config-template.json
```

### Optional Directories:

| Directory | Purpose |
|-----------|---------|
| `scripts/` | Executable code that agents can run |
| `references/` | Additional documentation loaded on demand |
| `assets/` | Static resources like templates, images, data files |

---

## Nested Skill Directories (Organizing by Category)

You can organize skills into subdirectories for grouping:

```
.cursor/skills/
├── deployment/
│   ├── deploy-web/
│   │   └── SKILL.md
│   └── deploy-api/
│       └── SKILL.md
├── testing/
│   ├── unit-tests/
│   │   └── SKILL.md
│   └── e2e-tests/
│       └── SKILL.md
└── documentation/
    └── generate-docs/
        └── SKILL.md
```

> *"The category folder is purely organizational. The skill's identity comes from the folder containing SKILL.md, not the parent category."*

### Monorepo Support:

Skills in nested project directories are **automatically scoped** to files inside that directory:

```
my-monorepo/
├── .cursor/skills/           # Available everywhere
│   └── repo-wide-skill/
│       └── SKILL.md
├── apps/
│   ├── web/
│   │   └── .cursor/skills/   # Only for apps/web/
│   │       └── deploy-web/
│   │           └── SKILL.md
│   └── api/
│       └── .cursor/skills/   # Only for apps/api/
│           └── deploy-api/
│               └── SKILL.md
```

**This is similar to the `paths` frontmatter field** – you don't need to set `paths` on a nested skill; it's automatically scoped to its directory.

---

## SKILL.md File Format

Each skill is defined in a `SKILL.md` file with **YAML frontmatter**:

```markdown
---
name: deploy-app
description: Deploy the application to staging or production environments.
---

# Deploy App

## When to Use
- Use this skill when deploying the application
- This is helpful for consistent deployment workflows

## Instructions
1. Run validation script: `python scripts/validate.py`
2. Run deployment: `scripts/deploy.sh staging`
3. Verify deployment succeeded

## Best Practices
- Always validate before deploying
- Use the ask questions tool if requirements are unclear
```

---

## Frontmatter Fields (Required & Optional)

| Field | Required | Description |
|-------|----------|-------------|
| **name** | ✅ Yes | Skill identifier. Lowercase letters, numbers, and hyphens only. Must match parent folder name. |
| **description** | ✅ Yes | Describes what the skill does and when to use it. Used by agent to determine relevance. |
| **paths** | ❌ No | Glob patterns that scope the skill to matching files. |
| **license** | ❌ No | License name or reference to bundled license file. |
| **compatibility** | ❌ No | Environment requirements (system packages, network access, etc.). |
| **metadata** | ❌ No | Arbitrary key-value mapping for additional metadata. |
| **disable-model-invocation** | ❌ No | When true, skill is only included when explicitly invoked via `/skill-name`. |

---

## Scoping a Skill to Specific Files

Use the `paths` field to limit a skill to specific files:

```yaml
---
name: react-component-patterns
description: Conventions for writing React components in this codebase.
paths:
  - "**/*.tsx"
  - "packages/ui/**/*.ts"
---
```

**Or as a comma-separated string:**

```yaml
---
name: python-style
description: Style rules for Python files.
paths: "**/*.py, scripts/**/*.py"
---
```

> *"Leave paths unset for a skill that should be available regardless of which files are open."*

**Legacy note:** The `globs` field is still accepted for older skills, but new skills should use `paths`.

---

## Disabling Automatic Invocation

By default, skills are **automatically applied** when the agent determines they're relevant.

Set `disable-model-invocation: true` to make a skill behave like a traditional slash command:

```yaml
---
name: review-code
description: Perform a security review of the codebase.
disable-model-invocation: true
---
```

Then invoke manually: `/review-code` in Agent chat.

---

## Including Scripts in Skills

Skills can include executable code that agents can run.

### Scripts Directory Structure:

```
deploy-app/
├── SKILL.md
└── scripts/
    ├── deploy.sh
    └── validate.py
```

### Referencing Scripts in SKILL.md:

```markdown
---
name: deploy-app
description: Deploy the application to staging or production environments.
---

# Deploy App

## Usage
Run the deployment script:
`scripts/deploy.sh <environment>`

Where `<environment>` is either 'staging' or 'production'.

## Pre-deployment Validation
Before deploying, run the validation script:
`python scripts/validate.py`
```

### Script Requirements:

| Requirement | Why |
|-------------|-----|
| **Self-contained** | Should work without external dependencies |
| **Helpful error messages** | User knows what went wrong |
| **Handle edge cases** | Graceful failure |
| **Any language** | Bash, Python, JavaScript, etc. |

---

## Viewing Available Skills

1. Open **Cursor Settings** (`Cmd+Shift+J` on Mac, `Ctrl+Shift+J` on Windows/Linux)
2. Navigate to **Rules**
3. Skills appear in the **Agent Decides** section

---

## Installing Skills from GitHub

| Step | Action |
|------|--------|
| 1 | Open Cursor Settings → Rules |
| 2 | In Project Rules section, click **Add Rule** |
| 3 | Select **Remote Rule (GitHub)** |
| 4 | Enter the GitHub repository URL |

Cursor will scan for all `SKILL.md` files and import them.

---

## Migrating Rules and Commands to Skills

Cursor includes a built-in `/migrate-to-skills` skill (available in version 2.4+) that helps you convert existing dynamic rules and slash commands to skills.

### What Gets Converted:

| Type | Conversion |
|------|------------|
| **Dynamic rules** (alwaysApply: false, no globs) | Converted to standard skills |
| **Slash commands** | Converted to skills with `disable-model-invocation: true` |

### What Does NOT Get Converted:

| Type | Why |
|------|-----|
| Rules with `alwaysApply: true` | Have explicit triggering conditions different from skills |
| Rules with specific globs patterns | Have explicit triggering conditions |
| User rules | Not stored on file system |

### How to Migrate:

1. Type `/migrate-to-skills` in Agent chat
2. Agent identifies eligible rules and commands
3. Review generated skills in `.cursor/skills/`

---

## Skills vs. Rules: What's the Difference?

| Feature | Rules | Skills |
|---------|-------|--------|
| **Purpose** | Persistent guidelines | Specialized workflows |
| **Can include scripts** | ❌ No | ✅ Yes |
| **Progressive loading** | ❌ No | ✅ Yes (load resources on demand) |
| **Auto-discovery** | ✅ Yes | ✅ Yes |
| **Manual invocation** | `@rule-name` | `/skill-name` |
| **File format** | `.md` or `.mdc` | `SKILL.md` + optional scripts |

**Simple distinction:**
- **Rules** = "Always do this" (guidelines)
- **Skills** = "Here's how to do a specific task" (workflows)

---

## Real-World Skill Examples

### Example 1: Deploy to Staging

```markdown
---
name: deploy-staging
description: Deploy the current branch to the staging environment.
---

# Deploy to Staging

## Instructions
1. Run tests: `npm test`
2. Build the app: `npm run build`
3. Deploy: `scripts/deploy.sh staging`
4. Verify health: `curl https://staging.myapp.com/health`

## After Deployment
- Post the deployment URL in Slack
- Run smoke tests
```

### Example 2: Generate API Documentation

```markdown
---
name: generate-api-docs
description: Generate OpenAPI documentation from code comments.
paths: "**/*.ts, **/*.js"
---

# Generate API Documentation

## Instructions
1. Scan for JSDoc comments
2. Run: `npx swagger-jsdoc -o docs/api.yaml`
3. Generate HTML: `npx redoc-cli bundle docs/api.yaml`
4. Save to `docs/api.html`
```

### Example 3: Code Review Skill

```markdown
---
name: security-review
description: Perform security audit on changed files.
disable-model-invocation: true
---

# Security Review

## What to Check
- No hardcoded secrets
- Input validation on all user data
- SQL injection vulnerabilities
- XSS risks

## Output Format
- Critical: Must fix before merge
- Warning: Should fix soon
- Suggestion: Nice to have
```

---

## Common Beginner Questions

### Q: Do I need to create skills as a beginner?
**A:** Not at all! Skills are for advanced users and teams. Start with simple prompts.

### Q: How is a skill different from just telling the agent what to do?
**A:** Skills save the instructions so you don't type them every time. They can also include executable scripts.

### Q: Can I use skills other people made?
**A:** Yes! Install them from GitHub via Remote Rule.

### Q: Do skills cost extra tokens?
**A:** Skills use **progressive loading** – they only load resources when needed, keeping context efficient.

### Q: Can skills run scripts on my computer?
**A:** Yes, but scripts are subject to the same security approvals as terminal commands.

### Q: What's the Agent Skills standard?
**A:** An open standard for skills to work across any compatible AI agent (Cursor, Claude, Codex, etc.). Learn more at `agentskills.io`.

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **What is a skill?** | Package that teaches agents domain-specific tasks |
| **Location** | `.cursor/skills/` or `.agents/skills/` |
| **Required files** | `SKILL.md` with YAML frontmatter |
| **Optional directories** | `scripts/`, `references/`, `assets/` |
| **Auto-discovery** | Yes – Cursor finds skills automatically |
| **Manual invocation** | `/skill-name` in chat |
| **Scope control** | `paths` field or nested directory |
| **Open standard** | `agentskills.io` |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What are Skills?** | Packages that teach agents specialized tasks |
| **Why use them?** | Consistent, repeatable workflows without repeating yourself |
| **Where do I put them?** | `.cursor/skills/` in your project |
| **What's in a skill?** | `SKILL.md` + optional scripts, references, assets |
| **Can I share skills?** | Yes – via GitHub or as files |
| **Do I need to make skills?** | No – start with simple prompts first |

---

## The Bottom Line

**Skills are like "recipe books" for the agent – they teach it how to perform specific tasks step by step.**

**Think of it as:**
- **Without Skills** = Telling a chef "make dinner" each time 🍳
- **With Skills** = Giving the chef a recipe book 📖

**For beginners:** You don't need to create skills yet. But you might enjoy **installing** skills from GitHub. Look for skills that automate tasks you do repeatedly.

**The most powerful features:**
1. **Portability** – Skills work across Cursor, Claude, and Codex
2. **Progressive loading** – Only loads what's needed, saving tokens
3. **Executable scripts** – Skills can actually RUN code
4. **Auto-discovery** – Agent knows which skill to use from context

**When you're ready to create your first skill:** Start with a task you do repeatedly (like "deploy to staging") and write a simple `SKILL.md` with step-by-step instructions. It's easier than you think!

Would you like me to explain how to create a specific skill, or move on to another document?