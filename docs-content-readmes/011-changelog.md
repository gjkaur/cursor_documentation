This is the **Cursor Changelog** – a diary of what's new, changed, or fixed in Cursor. Think of it as the "What's New" page for the software. It tells you about recent features and improvements.

Since this is a **release changelog** (focused on recent updates), I'll explain the key features mentioned in simple terms for a beginner.

Let me break down the major updates from these recent releases.

---

## Release: May 20, 2026 (Version 3.5) – Improvements to Cursor Automations 🤖

### What's New?

> *"This release brings Cursor Automations into the Agents Window and adds support for configuring automations with multiple attached repositories or no repositories at all."*

| Before | After |
|--------|-------|
| Automations managed mainly at `cursor.com/automations` | Create and manage automations in the **Agents Window** alongside agents |
| One repo per automation | **Multi-repo** or **no-repo** automations |
| Manual setup each time | Templates and reusable automation configs |

**Launch promotion:** For the next 7 days, all agent runs for **newly created automations are 50% off**.

---

### 1. Automations in the Agents Window 🪟

| Feature | What It Means |
|---------|---------------|
| **Same workspace as agents** | Create, edit, and monitor automations without leaving Cursor |
| **Template gallery** | Start from examples like fixing Slack-reported bugs or cleaning up feature flags |
| **Faster iteration** | Test triggers and prompts in the same UI you use for interactive agents |

**Example templates shown in docs:**
- Fix Bugs Reported in Slack
- Investigate Top Datadog Errors
- Clean up feature flags

**Why this matters for beginners:** Automations are no longer a separate website workflow — they live next to the Agent you already use.

---

### 2. Multi-Repo Automations 📦

> *"You can now attach multiple repositories to a single automation."*

| Feature | What It Means |
|---------|---------------|
| **Cross-repo context** | One automation can reason across frontend, backend, and shared libraries |
| **End-to-end tasks** | Delivery, testing, and verification can span multiple codebases |
| **Reusable environments** | Configure once, reuse across sessions |

**Why this matters:** Real products rarely live in a single repo. Automations can now mirror how your team actually works.

---

## Release: May 19, 2026 – No-Repo Automations 🔌

### What's New?

> *"You can now create automations with agents that monitor tools and act on signals without needing an attached repository."*

| Use Case | Example |
|----------|---------|
| **Daily digests** | Slack digest agent summarizes unread DMs and key channels every morning |
| **Metrics monitoring** | Product analytics agent pulls weekly metrics from Databricks |
| **Support triage** | Product FAQ agent drafts first responses from docs and past threads |
| **Finance reporting** | Product finance agent pulls recurring revenue from Stripe |
| **Customer health** | Customer health agent flags accounts with shifting signals across Granola, Slack, and Databricks |

**New marketplace templates:** Slack digest, product analytics, product FAQ, product finance, and customer health agents.

**Why this matters for beginners:** Not every automation needs code. You can automate ops, analytics, and support workflows with tool access alone.

---

## Release: May 19, 2026 – Cursor in Jira 🎫

### What's New?

> *"Cursor is now available in Jira. Assign work items to Cursor or mention @Cursor in a comment to kick off a cloud agent."*

| Step | What Happens |
|------|--------------|
| 1 | Assign a Jira issue to Cursor or mention `@Cursor` in a comment |
| 2 | Agent reads title, description, comments, and team repository settings |
| 3 | Agent fixes bugs, adds features, updates tests, or investigates the ticket |
| 4 | Agent posts completion updates in Jira with a link to the pull request |

**Setup requirements:**

| Requirement | Details |
|-------------|---------|
| **Installation** | Cursor integrations in the Cursor dashboard |
| **Access** | Cursor admin access |
| **Jira plan** | Jira Commercial Cloud with **Rovo** enabled |

**Why this matters for beginners:** If your team lives in Jira, you can delegate engineering work from a ticket — without copying context into Cursor manually.

---

## Release: May 18, 2026 – Composer 2.5 Available 🚀

### What's New?

> *"Composer 2.5 is now available in Cursor. It is a substantial improvement over Composer 2, with better intelligence and behavior, stronger performance on sustained long-running tasks, more reliable following of complex instructions, and an improved collaborative experience."*

| Aspect | Composer 2.5 | Composer 2 (prior) |
|--------|--------------|-------------------|
| **Model ID** | `composer-2.5` | `composer-2` |
| **Long-horizon tasks** | Reinforcement learning on sustained agentic work | Good, but less capable |
| **Standard pricing** | $0.50 input / $2.50 output per 1M tokens | Same pricing tier |
| **Fast pricing (default)** | $3.00 input / $15.00 output per 1M tokens | Prior fast tier was lower |
| **Launch promo** | **Double usage** for the first week | — |

### Benchmark Highlights (from Cursor docs)

| Benchmark | Composer 2.5 | Opus 4.7 | GPT-5.5 | Composer 2 |
|-----------|--------------|----------|---------|------------|
| **Terminal-Bench 2.0** | 69.3% | 69.4% | 82.7% | 61.7% |
| **SWE-Bench Multilingual** | 79.8% | 80.5% | 77.8% | 73.7% |
| **CursorBench v3.1** | 63.2% | 64.8% max | 64.3% xhigh | 52.2% |

**Why this matters for beginners:** Composer 2.5 is Cursor's default agentic model path forward — frontier intelligence with strong tool use inside Cursor. See [010-docs-models-cursor-composer-2-5.md](010-docs-models-cursor-composer-2-5.md) for full pricing and usage guidance.

---

## Release: May 13, 2026 (Version 3.4) – Full-Screen Tabs and Compact Chats 🖥️

### What's New?

> *"This release introduces quality-of-life improvements to the Agents Window."*

---

### 1. Full-Screen Tabs 📐

Maximize the right panel to focus on a single tab — files, changes, canvases, PRs, browsers, and terminals can all expand to fill the working area.

| Feature | What It Does |
|---------|--------------|
| **Full-screen mode** | Hides distractions; agent chat becomes a **floating prompt bar** |
| **Enter/exit** | Panel header button, command palette, or **`Cmd/Ctrl+Shift+M`** |
| **Supported tabs** | Files, changes, canvases, PRs, browser, terminal |

**Why this matters for beginners:** Review diffs, PRs, or browser output without fighting for screen space.

---

### 2. Compact Chat Responses 💬

> *"Compact chats give you a tighter view of your agent conversations so you can read threads more quickly without losing important context."*

**Tool call density** controls how much tool activity appears in each response:

| Setting | What You See |
|---------|--------------|
| **Compact** | Concise results, minimal tool traces |
| **Balanced** | Important intermediate steps included |
| **Detailed** | Near-complete step-by-step context |

**Why this matters:** Long agent runs become easier to scan — choose how much "behind the scenes" detail you want.

---

### Improvements & Bug Fixes (May 13, Version 3.4)

| Category | Count |
|----------|-------|
| **Improvements** | 8 |
| **Bug fixes** | 9 |

---

## Release: May 13, 2026 – Development Environments for Cloud Agents 🌐

### What's New?

> *"To take engineering tasks from start to finish, agents need a development environment similar to the setup on your laptop: cloned repositories, installed dependencies, credentials for internal toolchains, and access to build systems."*

Cloud agents now run inside **full development environments** – not just bare-bones sandboxes. They have everything a real developer would have on their laptop: cloned repos, installed packages, credentials, and access to build systems.

| Before | After |
|--------|-------|
| Agents ran in basic environments | Full development environments |
| Limited dependencies | Cloned repos, installed packages, credentials |
| Manual setup per agent | Configure once, reuse across sessions |

> *"This makes it easier for teams to run fleets of parallelized agents that handle tasks from end-to-end, inside development environments you fully control."*

**Why this matters for beginners:** Cloud agents can now do real engineering tasks – not just isolated code snippets. They have the same tools and access your team has.

---

### 1. Multi-Repo Environments 📦

> *"Cloud agents and automations now support multi-repo environments, building off our work on multi-root workspaces."*

| Feature | What It Means |
|---------|---------------|
| **Multiple repositories** | One environment with all repos an agent needs |
| **Re-use across sessions** | Configure once, use many times |

**Why this matters:** Real projects often span multiple repos (frontend, backend, shared libs). Now an agent can work across all of them.

---

### 2. Environment Configuration as Code 🐳

> *"To make it easier to change, debug, and review environment definitions, we have improved Dockerfile-based configuration."*

You define your environment in a Dockerfile (treated like code), so it can be version-controlled, reviewed, and reused.

| Improvement | Benefit |
|-------------|---------|
| **Build secrets** | Securely access private package registries |
| **Layer caching** | Only rebuilds changed layers |
| **70% faster builds** | Cache hits dramatically speed up builds |

> *"Build secrets are scoped to the build step and aren't passed to the running agent's environment."*

**Why this matters:** Faster build times and secure access to private packages – without leaking credentials to the running agent.

---

### 3. Improved Agent-Led Environment Setup 🤖

> *"As Cursor configures your environment, it will ask you questions, flag missing credentials, and validate that your environment is set up properly."*

| Feature | What It Does |
|---------|--------------|
| **Asks questions** | Clarifies missing information |
| **Flags missing credentials** | Tells you what's needed |
| **Validates setup** | Ensures environment works |
| **Shows environment version** | Always know what's running |
| **Fallback base image** | If config fails, uses base image with warning |

> *"If your environment configuration fails, it will default to a base image with clear warning signs so that your cloud agents can keep running instead of immediately failing."*

**Why this matters:** Setup is interactive and resilient. Even if something goes wrong, the agent can still run while you fix the config.

---

### 4. Environment Governance and Security Controls 🔒

| Feature | Benefit |
|---------|---------|
| **Version history** | Review and roll back environments |
| **Restrict rollback permissions** | Admins can limit who can roll back |
| **Audit log** | Track all environment actions |
| **Scoped egress and secrets** | Secrets for one environment not accessible from others |

> *"An audit log captures every action team members take on environments, giving security teams full visibility into who changed what."*

**Why this matters for admins:** Full visibility and control. You can see who did what, roll back bad changes, and keep secrets isolated to specific environments.

---

## Release: May 11, 2026 – Cursor in Microsoft Teams 💬

### What's New?

> *"Cursor is now available in Microsoft Teams. Mention @Cursor in any Teams channel to delegate a task to a cloud agent or pull information from Cursor into Teams."*

| Platform | Now Supported |
|----------|---------------|
| Slack | ✅ Already supported |
| Microsoft Teams | ✅ Now supported |

### How It Works:

| Step | What Happens |
|------|--------------|
| 1 | Mention `@Cursor` in any Teams channel |
| 2 | Cursor picks the right repository and model |
| 3 | Agent reads entire thread for context |
| 4 | Implements solution |
| 5 | Creates PR for team to review |

> *"Get started by installing the integration in the Cursor dashboard."*

**Why this matters for beginners:** If your company uses Microsoft Teams, you can now ask Cursor for help right inside a chat – without switching apps. Just `@Cursor` and describe what you need.

---

## Release: May 11, 2026 – Bugbot Effort Levels 🐛

### What is Bugbot?

Bugbot is Cursor's automated code reviewer. It reads your PRs and flags potential bugs before a human reviewer sees them.

### What's New?

> *"Teams admins and Individual plan users can now customize the effort level Bugbot uses for its PR reviews."*

### Three Configurations:

| Effort Level | What It Does |
|--------------|--------------|
| **Default** | Same as today – optimized for efficiency and speed |
| **High** | Spends more time reasoning – more expensive, takes longer, may find more bugs |
| **Custom** | Describe in natural language when to use default vs. high effort |

> *"Customers must be on usage-based billing for Bugbot to customize effort levels."*

**Why this matters for beginners:** You can now trade speed for thoroughness. Quick PRs? Use Default. Critical security PRs? Crank it to High.

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

> *"Click 'Build in Parallel' to have it identify independent parts of your plan and run them simultaneously using async subagents. Cursor will keep dependent steps in order when needed."*

---

### 3. Split Changes into PRs ✂️

> *"When multitasking in Cursor, you can now use a built-in quick action to split changes into PRs."*

Instead of one giant PR with 30 file changes, Cursor can split your work into smaller, logical PRs that are much easier to review.

| Feature | What It Does |
|---------|--------------|
| **Identifies logical slices** | Uses chat context to find natural splits |
| **Default independent PRs** | Creates separate PRs unless dependencies required |
| **Backup snapshot** | Creates safety backup before splitting |
| **Split plan** | Proposes plan for your approval |

**Why this matters for beginners:** Reviewers love small PRs. They're faster to review, less risky to merge, and easier to roll back if needed.

---

### 4. Pin Skills as Quick Actions 📌

> *"You can now pin your most commonly used skills as quick-action pills for faster access."*

| Before | After |
|--------|-------|
| Type `/skill-name` each time | Click pinned quick-action pill |

**Why this matters:** If you use the same skills over and over (like running tests, formatting code, or generating commits), pin them and skip the typing.

---

### Improvements (May 7)

| Improvement | Description |
|-------------|-------------|
| **Explore subagent control** | Choose specific model, inherit parent, or disable |
| **General model names** | Use `model: opus` – always uses newest Opus |
| **/multitask in editor** | Run async subagents to parallelize requests |
| **Better undo grouping** | Undo/redo feels more natural during edits |
| **Improved long-chat handling** | Less jumpiness, fewer surprises |
| **MCP connection improvements** | More predictable, explicit stale token cleanup |

### Bug Fixes (May 7)

| Fix | Description |
|-----|-------------|
| Terminal interaction bugs | Fixed editing shortcut issues, approval/overlay edge cases |
| Slash menu regressions | Fixed input-approval issues |
| MCP auth edge cases | Fixed transient 401 handling, stale credential behavior |
| Multi-repo environment | Fixed selection and cache issues |
| Cloud agent timing | Fixed hydration edge cases that degraded reliability |

---

## Release: May 6, 2026 – Context Usage Breakdown 📊

### What's New?

> *"You can now see a breakdown of your agent's context usage. Use these stats to diagnose context issues and improve your setup across rules, skills, MCPs, and subagents."*

You can now see a breakdown of what's taking up space in your AI's "context" (the memory/space the AI uses to understand your code).

**What you can see:**

| What You Can See |
|------------------|
| Rules usage (custom instructions you've given Cursor) |
| Skills usage (specialized abilities you've enabled) |
| MCPs usage (connections to other tools) |
| Subagents usage (smaller AI helpers) |

> *"Use these stats to diagnose context issues and improve your setup."*

**Why this matters for beginners:** If Cursor seems slow or confused, you can check what's filling up its context. Too many rules or skills might be overwhelming it. Now you can diagnose and fix it.

---

## Release: May 4, 2026

### 1. Model Controls for Enterprise Admins 🛡️

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

### 2. Soft Spend Limits and Intelligent Alerts 💰

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

### 3. Updated Usage Analytics Tab 📈

**What admins can now see:**

| Filter | What it shows |
|--------|---------------|
| **By specific user** | Usage for just one team member |
| **By product surface** | Breakdown by: Clients, Cloud Agents, Automations, Bugbot, Security Review |

**Why this matters:** Teams can see exactly who is using how much, and which features are costing the most.

---

### 4. Team Marketplace Updates 🛒

**What's new:** Admins can create a team marketplace without connecting a repository first.

**Three installation behaviors for plugins:**

| Setting | What it means |
|---------|---------------|
| **Default Off** | Users can discover and choose to install |
| **Default On** | Installed by default, users can opt out |
| **Required** | Always installed, cannot uninstall |

**Why this matters:** Companies can enforce certain tools or plugins for all developers.

---

## Summary of May 2026 Updates

| Date | Feature | What It Does |
|------|---------|--------------|
| May 20 | **Automations in Agents Window (3.5)** | Create/manage automations alongside agents; multi-repo or no-repo |
| May 20 | **Automation launch promo** | 50% off agent runs for newly created automations (7 days) |
| May 19 | **No-repo automations** | Monitor tools and act on signals without an attached repository |
| May 19 | **Cursor in Jira** | Assign issues or `@Cursor` in comments; agent updates Jira with PR link |
| May 18 | **Composer 2.5** | Frontier agentic model; double usage first week |
| May 13 | **Full-screen tabs (3.4)** | Maximize files, PRs, browser, terminal tabs; `Cmd/Ctrl+Shift+M` |
| May 13 | **Compact chats (3.4)** | Tool call density: Compact / Balanced / Detailed |
| May 13 | **Dev environments** | Full environments for cloud agents (multi-repo, config as code, governance) |
| May 11 | **Microsoft Teams** | `@Cursor` in Teams channels |
| May 11 | **Bugbot effort levels** | Customize review depth (Default, High, Custom) |
| May 7 | **PR Review (3.3)** | Complete PR workflow inside Cursor |
| May 7 | **Build in parallel** | Execute plan tasks simultaneously |
| May 7 | **Split PRs** | Split changes into logical PRs |
| May 7 | **Pin skills** | Quick-access skill pills |
| May 6 | **Context breakdown** | See what's using context space |
| May 4 | **Model controls** | Admins block/allow specific models |
| May 4 | **Spend alerts** | Get warnings before hitting budget |
| May 4 | **Usage analytics** | See who used what |
| May 4 | **Team marketplace** | Control which plugins are available |

---

## Summary of What's New (For Beginners)

| Feature | What it does | Who cares? |
|---------|--------------|-------------|
| **Automations in Agents Window** | Build automations next to interactive agents | Teams automating repetitive work |
| **Multi-repo / no-repo automations** | Automate across repos or without code at all | Platform and ops teams |
| **Cursor in Jira** | Delegate tickets to `@Cursor` from Jira | Teams using Jira + Rovo |
| **Composer 2.5** | Cursor's improved default agentic model | Everyone using Cursor agents |
| **Full-screen tabs** | Focus on diffs, PRs, browser, or terminal | Anyone reviewing agent output |
| **Compact chats** | Control how much tool detail you see | Power users in long threads |
| **Dev environments** | Cloud agents get a full laptop-like setup | Teams running cloud agents |
| **Multi-repo** | One environment spans all your repos | Teams with multiple repos |
| **Microsoft Teams** | `@Cursor` works in Teams channels | Teams using MS Teams |
| **Bugbot effort levels** | Trade speed for thoroughness | Teams using Bugbot |
| **PR Review** | Review code without leaving Cursor | Team developers |
| **Parallel execution** | Does multiple tasks at once | Everyone (faster!) |
| **Split PRs** | Smaller, easier-to-review PRs | Code reviewers |
| **Pin skills** | One-click access to common skills | Power users |
| **Context breakdown** | See what's using AI memory | Power users, debugging |
| **Model controls** | Block/allow certain AI models | Admins |
| **Spend alerts** | Get warnings before hitting budget | Teams with budgets |
| **Usage analytics** | See who used what | Admins |
| **Team marketplace** | Control which plugins are available | Admins |

---

## Key Takeaways for Engineers

| Update | Why It Matters |
|--------|----------------|
| **Automations in Agents Window** | Automations are first-class in the main agent UI |
| **Multi-repo / no-repo automations** | Automate real-world cross-system workflows |
| **Jira integration** | Delegate engineering work from Jira tickets |
| **Composer 2.5** | Better long-running agentic tasks at frontier quality |
| **Full-screen tabs + compact chats** | Easier to review and scan agent work |
| **Dev environments** | Agents can have full setup like your laptop |
| **Multi-repo** | Agents can work across multiple repos |
| **Teams integration** | Use Cursor from Microsoft Teams |
| **Bugbot effort** | Control review depth vs. cost |
| **Parallel builds** | Faster execution of plans |
| **Split PRs** | Easier code review |
| **Context breakdown** | Debug context issues |

---

## For a Beginner: What Matters Most

The features most relevant to you as a beginner are:

### 1. Composer 2.5 🚀
Cursor's own agentic model got a major upgrade. If you use Cursor daily, this is likely your best default for agent work.

### 2. Automations in the Agents Window 🤖
You can now set up scheduled or event-driven agents without leaving the editor — great for "fix bugs from Slack" or "clean up flags" workflows.

### 3. Parallel Execution ⚡
Your plans will execute faster. If you give Cursor a list of independent tasks, it will tackle them simultaneously. Less waiting!

### 4. Full-Screen Tabs & Compact Chats 🖥️
Review agent output more comfortably, and tune how much tool detail you see in long conversations.

### 5. Context Usage Breakdown 🔍
If Cursor ever seems lost or confused, you can check what's filling up its context. Maybe you added too many rules or enabled too many skills. Now you can see and fix it.

### 6. Jira & Microsoft Teams Integrations 💬
If your company uses Jira or Teams, delegate work with `@Cursor` without switching apps.

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

## The Bottom Line

**Cursor's May 2026 updates focus on four main areas: smarter default models (Composer 2.5), richer automations (Agents Window, multi-repo, no-repo), more integrations (Jira and Microsoft Teams), and better agent UX (full-screen tabs, compact chats, parallel plans, PR review, context visibility).**

**For your engineers:**
- Use **Composer 2.5** for long-running agentic tasks
- Build **automations in the Agents Window** — with multiple repos or no repo at all
- Delegate work from **Jira** (`@Cursor` or assign to Cursor) and **Microsoft Teams**
- Use **full-screen tabs** and **compact chats** to review agent output faster
- Cloud agents can now have **full development environments**
- Customize **Bugbot effort** for deeper reviews
- **Build plans in parallel** and **split changes into logical PRs**
- Use **context usage breakdown** to debug issues

---

## Final Summary for Beginners

The **changelog** is Cursor's way of telling users: *"Hey, we added these cool new things!"*

**Key takeaways:**
- **Composer 2.5** = Cursor's improved frontier agentic model (double usage first week at launch)
- **Automations in Agents Window** = Set up background agents without leaving Cursor
- **No-repo automations** = Automate Slack digests, analytics, finance, and support without code
- **Jira** = Assign tickets or `@Cursor` in comments; get PR links back in Jira
- **Dev Environments** = Cloud agents get a full laptop-like setup (multi-repo, secrets, audit logs)
- **Microsoft Teams** = `@Cursor` works in Teams channels (just like Slack)
- **Full-screen tabs** = Focus on diffs, PRs, browser, or terminal (`Cmd/Ctrl+Shift+M`)
- **Compact chats** = Choose Compact / Balanced / Detailed tool-call density
- **Bugbot Effort Levels** = Trade speed for thoroughness on PR reviews
- **PR Review** = Review code inside Cursor (no more switching to GitHub)
- **Parallel Plans** = Faster execution (Cursor does multiple tasks at once)
- **Split PRs** = Smaller, easier-to-review changes
- **Pin Skills** = One-click access to your favorite skills
- **Context Breakdown** = See what's using AI memory (helps with debugging)
- **Spend Alerts** = Get warnings before hitting budget (no surprise blocks)

**For a beginner:** The most exciting features are **Composer 2.5**, **automations in the Agents Window**, and **parallel execution / split PRs** — your AI assistant is smarter, easier to automate, and faster. The context breakdown is also helpful if you run into issues.

