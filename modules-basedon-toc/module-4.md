# Module 4: Customizing Cursor for Your Team

## Cursor Training Program — Day 1 (Hands-On + Walkthrough)

---

## Module Overview

| Aspect | Details |
|--------|---------|
| **Duration** | ~60 minutes |
| **Format** | Hands-on exercise + walkthrough |
| **Prerequisites** | Modules 1-3 completed, team repository access, Cursor installed |
| **Module Goal** | Customize Cursor for team workflows with rules, skills, MCP, and subagents |

---

## Learning Objectives

By the end of this module, participants will be able to:

- Create Rules that encode team conventions and guardrails
- Write Repository Instructions for lightweight project guidance
- Build and invoke reusable Skills for specialized workflows
- Connect external tools via MCP and create slash workflows
- Understand when and how to use Subagents for delegation

---

## Lesson 4.1: Creating a Rule

### Concept (8 minutes)

> *"Encoding team conventions, build commands, and guardrails. Rules are persistent instructions that the agent follows for every interaction in a project."*

### What Are Rules?

Rules are Markdown files (`.cursor/rules/*.mdc`) that contain persistent instructions the agent automatically applies.

**Types of Rules:**

| Rule Type | Scope | When Applied | Example |
|-----------|-------|--------------|---------|
| **Global** | All projects | Always | "Use American English spelling" |
| **Project** | Specific repo | When opening that project | "Run `make test` before suggesting changes" |
| **File pattern** | Matching files | When editing those files | "For `*.py` files, use type hints" |
| **User** | Your account | Always across all projects | "Explain like I'm a junior developer" |

### Rule Structure

```markdown
---
description: Brief description of what this rule does
globs: *.py, src/**/*.js  # Optional: file patterns
alwaysApply: true          # Apply without asking
---

# Rule Title

## Instructions for the Agent

Write your instructions here in natural language.

## Examples

Good: ...
Bad: ...

## Checklist (optional)

- [ ] Check this
- [ ] Verify that
```

### Hands-On Exercise (12 minutes)

**Step 1:** Create the `.cursor` directory

```bash
mkdir -p .cursor/rules
```

**Step 2:** Create a team coding standards rule

Create file `.cursor/rules/coding-standards.mdc`:

```markdown
---
description: Team coding standards and conventions
globs: **/*.{js,ts,py}
alwaysApply: true
---

# Team Coding Standards

## Python Standards (for .py files)

- Use type hints for all function parameters and returns
- Maximum line length: 88 characters (Black formatter)
- Docstrings: Google style format
- Error handling: Use specific exception types, never bare `except:`

## JavaScript/TypeScript Standards (for .js/.ts files)

- Use `const` over `let`, avoid `var`
- Prefer arrow functions for callbacks
- Use optional chaining (`?.`) and nullish coalescing (`??`)
- Export named exports over default exports when possible

## General Rules for All Code

- No commented-out code in commits
- No `console.log` in production code (use proper logging)
- Add JSDoc/docstring for public functions
- Keep functions under 50 lines when possible

## Example: Good Python Function

```python
def calculate_total(prices: list[float], tax_rate: float = 0.0) -> float:
    """Calculate total price including tax.
    
    Args:
        prices: List of item prices
        tax_rate: Tax rate as decimal (default 0.0)
    
    Returns:
        Total including tax
    """
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)
```

## Example: Bad Python Function (Avoid)

```python
def calc(prices, tax):  # No type hints
    total = 0
    for p in prices:
        total = total + p  # Could use sum()
    # Missing docstring
    return total + (total * tax)
```
```

**Step 3:** Create a build/test rule

Create file `.cursor/rules/build-and-test.mdc`:

```markdown
---
description: Build and test commands for this project
globs: **/*
alwaysApply: true
---

# Build & Test Commands

## Before making changes

Always check the current state:
```bash
git status
git diff
```

## After making changes

1. Run the test suite:
```bash
make test
# or
pytest
# or
npm test
```

2. Run the linter:
```bash
make lint
```

3. If tests fail, fix them before proposing changes.

## Build commands

- Development: `make dev`
- Production build: `make build`
- Database migrations: `make migrate`

## Rule for the Agent

Do NOT suggest changes that:
- Would break the test suite
- Require external API keys not documented
- Would change database schema without a migration
```

**Step 4:** Create a security guardrail rule

Create file `.cursor/rules/security.mdc`:

```markdown
---
description: Security guardrails for code changes
globs: **/*
alwaysApply: true
---

# Security Guardrails

## Never Suggest

- Hardcoded secrets, API keys, or passwords
- Using `eval()` or `exec()` on user input
- SQL string concatenation (use parameters)
- Disabling SSL verification
- `pickle` on untrusted data

## Always Include

- Input validation for all user-provided data
- Rate limiting for public endpoints
- HTTPS for external requests
- Proper error messages (no stack traces to users)

## Sensitive Patterns to Flag

If you see any of these, warn the user:
- `exec()` or `eval()` with user input
- `password` or `secret` in variable names
- Commented-out code with credentials

## Example: SQL Injection (Bad)

```python
# NEVER DO THIS
query = f"SELECT * FROM users WHERE email = '{email}'"
```

## Example: Parameterized Query (Good)

```python
# ALWAYS DO THIS
query = "SELECT * FROM users WHERE email = ?"
cursor.execute(query, (email,))
```
```

**Step 5:** Test that rules are applied

Open the Agent and ask:

```
Based on the project rules, what are the coding standards I should follow?
What are the security guardrails?
```

**Step 6:** Create a file-specific rule

Create `.cursor/rules/react-components.mdc`:

```markdown
---
description: React component best practices
globs: **/*.jsx, **/*.tsx
alwaysApply: true
---

# React Component Rules

## Component Structure

1. Imports (React, third-party, local)
2. Types/props definition
3. Component function
4. Hooks (useState, useEffect, etc.)
5. Event handlers
6. JSX return
7. Export

## Naming

- Components: PascalCase (`UserProfile`)
- Hooks: usePascalCase (`useAuth`)
- Event handlers: handlePascalCase (`handleSubmit`)
- Props: camelCase (`isActive`, `onClick`)

## Performance

- Use `React.memo` for expensive components
- Use `useCallback` for functions passed to memoized children
- Use `useMemo` for expensive calculations

## Accessibility (a11y)

- All interactive elements must be keyboard accessible
- Include `alt` text for images
- Use semantic HTML (button, nav, main)
- Include `aria-label` when needed

## Example Component

```tsx
import React, { useState, useCallback } from 'react';

interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
}

export const Button: React.FC<ButtonProps> = React.memo(({
  label,
  onClick,
  disabled = false
}) => {
  const [isHovered, setIsHovered] = useState(false);
  
  const handleClick = useCallback(() => {
    if (!disabled) onClick();
  }, [disabled, onClick]);
  
  return (
    <button
      onClick={handleClick}
      disabled={disabled}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      aria-disabled={disabled}
    >
      {label}
    </button>
  );
});
```
```

**Success Criteria:**
- [ ] Created `.cursor/rules/` directory
- [ ] Created coding standards rule
- [ ] Created build/test rule
- [ ] Created security guardrail rule
- [ ] Verified rules are being applied

---

## Lesson 4.2: Repository Instructions

### Concept (5 minutes)

> *"Lightweight project-level guidance. Repository Instructions are simpler than Rules – they live in a single file and provide high-level project context."*

### Rules vs. Repository Instructions

| Aspect | Rules | Repository Instructions |
|--------|-------|------------------------|
| **Location** | `.cursor/rules/*.mdc` | `.cursor/repository-instructions.md` |
| **Complexity** | Multiple files, scoped | Single file, global |
| **Granularity** | Per-file patterns | Entire repository |
| **Use case** | Detailed standards | High-level project overview |
| **When to use** | Coding standards, security | Project purpose, architecture |

### Repository Instructions Structure

```markdown
# Repository Instructions for [Project Name]

## Project Purpose
[One paragraph describing what this project does]

## Key Technologies
- Backend: Python 3.11 + FastAPI
- Frontend: React 18 + TypeScript
- Database: PostgreSQL
- Cache: Redis

## Architecture Overview
[2-3 sentences about high-level structure]

## Important Conventions
- Use environment variables for configuration
- All API endpoints must have OpenAPI docs
- Tests go in `tests/` mirroring source structure

## Common Tasks
- Running locally: `make dev`
- Running tests: `make test`
- Building: `make build`

## External Dependencies
- [List key APIs or services the project interacts with]

## Contact
- On-call: #team-name on Slack
- Docs: link-to-internal-wiki
```

### Hands-On Exercise (8 minutes)

**Step 1:** Create repository instructions

Create file `.cursor/repository-instructions.md`:

```markdown
# Repository Instructions for Task Manager API

## Project Purpose
REST API for a team task management system. Users can create tasks, assign them, track status, and generate reports.

## Key Technologies
- Backend: Python 3.11 + FastAPI
- Database: PostgreSQL 15
- ORM: SQLAlchemy 2.0
- Authentication: JWT
- Testing: pytest + factory_boy

## Architecture Overview
```
src/
├── api/         # Route handlers
├── models/      # SQLAlchemy models
├── schemas/     # Pydantic schemas
├── services/    # Business logic
├── repositories/# Database operations
└── utils/       # Helpers
```

## Important Conventions
- Use dependency injection for services
- All database queries must be in repositories, never in api handlers
- Use async/await throughout
- Type hints required for all functions

## Authentication
- JWT tokens in `Authorization: Bearer <token>` header
- Token expires in 24 hours
- Refresh token endpoint at `/auth/refresh`

## Common Tasks
- Run dev server: `uvicorn src.main:app --reload`
- Run tests: `pytest -v`
- Run migrations: `alembic upgrade head`
- Format code: `black src/ tests/`
- Lint: `ruff check src/`

## Environment Variables Required
- `DATABASE_URL`: PostgreSQL connection string
- `JWT_SECRET_KEY`: 32+ characters
- `REDIS_URL`: For rate limiting (optional)

## Testing
- Unit tests: `tests/unit/`
- Integration tests: `tests/integration/`
- Mock external APIs using pytest-mock

## CI/CD
- PRs require passing tests and linting
- Main branch deploys automatically to staging
- Tags with `v*` deploy to production
```

**Step 2:** Verify the agent can access repository instructions

Ask the Agent:

```
What are the key technologies used in this project?
How do I run the tests?
```

**Step 3:** Update instructions as your project evolves

```markdown
# Add to repository instructions when:
- New team members join → add contact info
- Architecture changes → update structure
- New dependencies → add to list
- Common issues discovered → add troubleshooting section
```

**Success Criteria:**
- [ ] Created `.cursor/repository-instructions.md`
- [ ] Included project purpose, tech stack, architecture
- [ ] Added common commands and conventions
- [ ] Verified agent can access the instructions

---

## Lesson 4.3: Creating and Invoking a Skill

### Concept (8 minutes)

> *"Building and using a reusable specialized workflow. Skills are like macros or scripts for the agent – a set of instructions that can be invoked by name to perform a specific task."*

### What Is a Skill?

A Skill is a reusable, specialized workflow that the agent can load and follow. Think of it as a "prompt template with memory."

**Skill Structure:**

```
.cursor/skills/
├── skill-name/
│   ├── SKILL.md          # Main instructions (required)
│   ├── scripts/          # Optional helper scripts
│   ├── references/       # Optional reference docs
│   └── templates/        # Optional output templates
```

**When to Create a Skill:**

| Use Case | Example Skill |
|----------|---------------|
| Frequent task | "PR Review" – review PRs with team checklist |
| Complex workflow | "Onboarding" – set up new dev environment |
| Domain-specific | "Security Audit" – check for vulnerabilities |
| Documentation | "Generate API Docs" – create OpenAPI spec |

### Hands-On Exercise (12 minutes)

**Step 1:** Create the skills directory

```bash
mkdir -p .cursor/skills
```

**Step 2:** Create a PR Review skill

Create file `.cursor/skills/pr-review/SKILL.md`:

```markdown
---
name: pr-review
description: Review a pull request for code quality, security, and team standards
---

# PR Review Skill

You are an expert code reviewer. When invoked with a PR number or branch name, you will:

## Step 1: Understand the Changes

Fetch the PR diff using git:
```bash
git fetch origin pull/{PR_NUMBER}/head
git diff main...FETCH_HEAD
```

## Step 2: Review Categories

Check each category and report findings:

### Code Quality
- [ ] No commented-out code
- [ ] No debugging statements (console.log, print)
- [ ] Functions are under 50 lines where reasonable
- [ ] No duplicate code (DRY principle)

### Security
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] SQL queries parameterized
- [ ] No eval() or similar dangerous functions

### Testing
- [ ] New code has tests
- [ ] Existing tests pass (check CI)
- [ ] Edge cases covered

### Documentation
- [ ] Public APIs have docstrings/JSDoc
- [ ] README updated if needed
- [ ] Complex logic has comments

### Style (per team standards)
- [ ] Follows project formatting
- [ ] Variable names are descriptive
- [ ] Consistent with codebase

## Step 3: Output Format

```markdown
## PR Review: [PR Title]

### Summary
[2-3 sentence overview of changes]

### Issues Found

🔴 **Critical (must fix)**
- [Issue] - [Location] - [Why] - [Suggestion]

🟡 **Warning (should fix)**
- [Issue] - [Location] - [Suggestion]

🟢 **Suggestion (consider)**
- [Suggestion] - [Why it would help]

### What's Working Well
- [Positive observation 1]
- [Positive observation 2]

### Verdict
[APPROVE / REQUEST CHANGES / COMMENT]
```

## Example

User: "Review PR #42"

Agent: [Runs through steps above, produces formatted review]
```

**Step 3:** Create a Security Audit skill

Create file `.cursor/skills/security-audit/SKILL.md`:

```markdown
---
name: security-audit
description: Perform a security audit on a file or directory
---

# Security Audit Skill

You are a security expert. When invoked with a file path, you will:

## Step 1: Scan for Vulnerabilities

Check for these patterns:

### High Severity (Critical)
- Hardcoded secrets: `password=`, `api_key=`, `secret=`
- SQL injection: string concatenation in queries
- Command injection: `os.system(user_input)`
- eval/exec on user input

### Medium Severity (Important)
- No input validation on user data
- Weak cryptography (md5, sha1)
- Missing CSRF protection
- Insecure deserialization (pickle, yaml.load)

### Low Severity (Nice to fix)
- Debug endpoints left enabled
- Verbose error messages exposing internals
- Outdated dependency versions

## Step 2: Produce Report

```markdown
## Security Audit: [File Path]

### Critical Issues (Fix Immediately)
[Detailed description + line number + fix suggestion]

### Important Issues (Fix Soon)
[Detailed description + fix suggestion]

### Low Risk (Consider)
[Observations + recommendations]

### Secure Patterns Found
[Positive findings worth noting]

### Overall Risk Rating
[CRITICAL / HIGH / MEDIUM / LOW / PASS]
```

## Step 3: Suggest Remediation

For each critical/important issue, provide:
- Why it's dangerous (CWE reference if applicable)
- Example of vulnerable code
- Example of fixed code
```

**Step 4:** Invoke a skill

```
# In the Agent, invoke the PR review skill
/pr-review PR #42

# Or with a branch name
/pr-review feature/payment-integration
```

**Step 5:** List available skills

```
What skills are available in this project?
```

**Step 6:** Create a simple "Onboarding" skill

Create file `.cursor/skills/onboarding/SKILL.md`:

```markdown
---
name: onboarding
description: Generate a developer onboarding checklist for this project
---

# Onboarding Skill

You will generate a developer onboarding checklist based on the repository instructions and project structure.

## Step 1: Analyze Project

From the repository instructions and codebase, identify:
- Required tools (Python version, Node version, etc.)
- Dependencies (pip install, npm install commands)
- Database setup (migrations, seed data)
- Environment variables needed
- First-time setup commands

## Step 2: Generate Checklist

```markdown
# Developer Onboarding: [Project Name]

## Prerequisites (Install these first)
- [ ] Python 3.11+
- [ ] PostgreSQL 15
- [ ] Git

## Initial Setup
```bash
git clone [url]
cd [project]
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your values
```

## Database Setup
```bash
createdb [db_name]
alembic upgrade head
python scripts/seed_data.py
```

## Verify Installation
```bash
pytest
make dev
# Should see "Server running on http://localhost:8000"
```

## Next Steps
- Read the Architecture section in repository instructions
- Run through the tutorial in /docs/tutorial.md
- Join #project-name on Slack
```

## Step 3: Offer to Customize

After generating, ask:
- "Should I add any project-specific steps?"
- "Would you like me to create a setup script?"
```

**Success Criteria:**
- [ ] Created skills directory
- [ ] Built PR Review skill
- [ ] Built Security Audit skill
- [ ] Invoked a skill using slash command
- [ ] Listed available skills

---

## Lesson 4.4: MCP, Hooks, and Slash Workflows (Walkthrough)

### Concept (10 minutes)

> *"Connecting external tools and shipping team commands. MCP (Model Context Protocol) lets you plug in external servers that provide tools, data, or actions to the agent."*

### What Is MCP?

MCP is a protocol that standardizes how AI agents discover and use external tools. It's like a USB port for AI – plug in any MCP-compatible server and the agent can use its capabilities.

**MCP Architecture:**

```
┌─────────────────────────────────────────────────────────────┐
│                      MCP OVERVIEW                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Cursor Agent ←─MCP Protocol─→ MCP Server                   │
│                                      │                       │
│                                      ├─→ GitHub API         │
│                                      ├─→ Jira API           │
│                                      ├─→ Slack API          │
│                                      ├─→ Internal Database  │
│                                      └─→ Custom Tools       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### What You Can Do with MCP

| MCP Server | Capabilities |
|------------|--------------|
| **GitHub MCP** | Create PRs, comment on issues, fetch reviews |
| **Slack MCP** | Send messages, read channels, react to threads |
| **Jira MCP** | Create tickets, update status, add comments |
| **Filesystem MCP** | Read/write files outside project |
| **Database MCP** | Query databases, run migrations |
| **Custom MCP** | Your own internal tools |

### Hooks

Hooks are scripts that run at specific points in the agent's workflow.

**Hook Types:**

| Hook | When It Runs | Use Case |
|------|--------------|----------|
| `pre-tool-use` | Before agent calls a tool | Validate permissions, log |
| `post-tool-use` | After tool returns | Transform results, audit |
| `pre-prompt` | Before sending to model | Inject context, redact secrets |
| `post-response` | After agent responds | Format output, log conversations |

### Slash Workflows

Slash workflows are team commands that combine MCP tools, hooks, and prompts into one-click actions.

**Example Slash Commands:**

| Command | What It Does |
|---------|--------------|
| `/onboard @newdev` | Run onboarding skill, create GitHub issue, send Slack message |
| `/deploy staging` | Run tests, build, deploy to staging, notify team |
| `/bug-report` | Analyze error, create GitHub issue, assign to on-call |
| `/docs-update` | Review doc changes, build docs, deploy |

### Walkthrough: Setting Up an MCP Server (Demonstration)

**Step 1:** Install an MCP server (example: GitHub MCP)

```bash
npm install -g @cursor/mcp-github
```

**Step 2:** Configure MCP in Cursor

Create or edit `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "command": "cursor-mcp-github",
      "args": ["--token", "${GITHUB_TOKEN}"],
      "env": {
        "GITHUB_TOKEN": "your-token-here"
      }
    },
    "slack": {
      "command": "cursor-mcp-slack",
      "args": ["--token", "${SLACK_TOKEN}"]
    }
  }
}
```

**Step 3:** Use MCP tools in Agent

```
# With GitHub MCP enabled
Create a PR from my feature/payment branch and request review from @alice

# With Slack MCP
Send a message to #deploys channel saying "Deployment starting"
```

**Walkthrough: Creating a Slash Command (Demonstration)**

Create file `.cursor/commands/deploy.md`:

```markdown
---
name: deploy
description: Deploy to staging environment
arguments: 
  - name: environment
    required: true
    description: staging or production
---

# Deploy Workflow

You will deploy to {{environment}} by following these steps:

## Pre-deploy Checks
1. Run `make test` – all tests must pass
2. Run `make lint` – no linting errors
3. Check `git status` – working directory clean

## Deploy Steps
For staging:
```bash
git push origin main
kubectl set image deployment/app app=$IMAGE
```

For production:
```bash
# Requires approval
git tag v$(date +%Y%m%d-%H%M)
git push --tags
./scripts/deploy-prod.sh
```

## Post-deploy
1. Verify health endpoint: `curl https://{{environment}}.app/health`
2. Run smoke tests: `make smoke-test-{{environment}}`
3. Notify team via Slack (if MCP available)

## Safety Rules
- Never deploy to production without --force flag confirmation
- Always verify database migrations are backward compatible
- Rollback plan: `./scripts/rollback.sh {{environment}}`
```

**Using the slash command:**

```
/deploy staging
```

**Success Criteria (Walkthrough):**
- [ ] Understood MCP concept and architecture
- [ ] Saw example MCP configuration
- [ ] Understood hook types and use cases
- [ ] Saw slash command example
- [ ] Understood how to create team commands

---

## Lesson 4.5: Subagents (Walkthrough)

### Concept (6 minutes)

> *"A brief look at delegating specialized work to focused sub-agents. Subagents are separate agent instances that handle specific tasks and report back."*

### What Are Subagents?

Subagents are independent agent instances that you can spawn to handle specialized tasks. They operate with their own context, tools, and instructions, then return results to the main agent.

**Subagent Architecture:**

```
┌─────────────────────────────────────────────────────────────┐
│                    SUBAGENT ARCHITECTURE                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Main Agent                                                  │
│      │                                                       │
│      ├──→ Subagent: Security Scanner                        │
│      │       └──→ Returns: "2 critical issues found"        │
│      │                                                       │
│      ├──→ Subagent: Documentation Generator                  │
│      │       └──→ Returns: "Updated README.md"              │
│      │                                                       │
│      └──→ Subagent: Test Writer                             │
│              └──→ Returns: "Added 5 test cases"             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### When to Use Subagents

| Scenario | Why Subagent | Example |
|----------|--------------|---------|
| **Parallel work** | Multiple tasks simultaneously | Scan security AND generate docs |
| **Isolation** | Separate context to avoid confusion | Analyze large file independently |
| **Specialization** | Different prompts/instructions | Security expert vs. UI designer |
| **Sandboxing** | Limit tool access | Read-only subagent for unknown code |

### Subagent vs. Tool vs. Skill

| Concept | Best for |
|---------|----------|
| **Tool** | Single action (read file, run command) |
| **Skill** | Multi-step workflow, same context |
| **Subagent** | Parallel, isolated, specialized work |

### Walkthrough: Subagent in Action (Demonstration)

**Scenario:** You ask the main agent to "Review the entire codebase for security issues and generate API documentation"

**Without subagents (one agent does both):**
- Context gets mixed
- Security focus may distract from docs
- Slower (sequential)

**With subagents (parallel):**
```
Main Agent: I'll spawn two subagents to work in parallel.

→ Subagent 1 (Security Expert): 
   - Context: Security rules from .cursor/rules/security.mdc
   - Task: Scan all files for vulnerabilities
   - Tool access: Read-only

→ Subagent 2 (Doc Writer):
   - Context: API structure and doc standards
   - Task: Generate OpenAPI spec
   - Tool access: Read + write to docs/

[Both work simultaneously]

Results:
- Subagent 1: Found 3 critical issues
- Subagent 2: Generated openapi.yaml

Main Agent combines: "Here's the security report and API docs."
```

**How to invoke subagents (Cursor interface):**

```
# In the Agent, you can request subagents:
Spawn a security subagent to audit src/auth/ independently.
Meanwhile, I'll work on the frontend.

# Or use the UI:
Click "New Subagent" button in the Agent panel
Select template: Security Scanner
Assign task: "Audit all database queries for injection vulnerabilities"
```

**Built-in Subagent Templates (Cursor Enterprise):**

| Template | Purpose |
|----------|---------|
| Security Scanner | Vulnerability detection |
| Test Generator | Create unit/integration tests |
| Documentation Writer | Generate API docs, READMEs |
| Code Reviewer | PR review with different focus |
| Performance Analyzer | Find bottlenecks |

**Success Criteria (Walkthrough):**
- [ ] Understood subagent concept
- [ ] Saw when to use vs. regular agent
- [ ] Understood parallel execution benefit
- [ ] Recognized subagent templates

---

## Module Summary

| Lesson | Topic | Time | Key Output |
|--------|-------|------|------------|
| 4.1 | Creating a Rule | 12 min | `.cursor/rules/*.mdc` files |
| 4.2 | Repository Instructions | 8 min | `.cursor/repository-instructions.md` |
| 4.3 | Creating Skills | 12 min | `.cursor/skills/*/SKILL.md` |
| 4.4 | MCP & Slash Commands | 10 min | MCP config, slash commands |
| 4.5 | Subagents | 6 min | Understanding of delegation |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│              CUSTOMIZATION QUICK REFERENCE                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  RULES (.cursor/rules/*.mdc)                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • Coding standards, security, build commands        │   │
│  │ • Applied automatically to matching files           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  REPOSITORY INSTRUCTIONS                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • .cursor/repository-instructions.md                │   │
│  │ • High-level project overview                       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  SKILLS (.cursor/skills/*/SKILL.md)                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • Reusable workflows                                 │   │
│  │ • Invoke with /skill-name                           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  MCP (~/.cursor/mcp.json)                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • Connect external tools (GitHub, Slack, Jira)      │   │
│  │ • Agent gains new capabilities                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  SLASH COMMANDS (.cursor/commands/*.md)                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • Team shortcuts: /deploy, /onboard, /triage        │   │
│  │ • Combine MCP tools, hooks, skills                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  SUBAGENTS                                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • Parallel, isolated execution                      │   │
│  │ • Specialized per task                              │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Transition to Module 5

> *"Now that you've customized Cursor for your team, Module 5 will cover Model Configuration – selecting the right models, managing API keys, and optimizing cost vs. quality."*

---

*End of Module 4*