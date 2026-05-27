# Cursor Training Program — Course Cheatsheet

**Full-form definitions and technical terms** for all **10 modules** of the 2-day course. Use alongside [`FINAL_TABLE_OF_CONTENTS.md`](FINAL_TABLE_OF_CONTENTS.md), the slide deck, and [`slide-exercises/`](slide-exercises/) lab guides.

*Aligned to `slides/course-complete-marp-with-notes.md` · Last updated: 2026-05-26*

---

## How to use this cheatsheet

| Section | Contents |
|---------|----------|
| **Quick acronym index** | A–Z lookup across the whole course |
| **Modules 1–10** | Terms, definitions, and module-specific shortcuts grouped by day |
| **Cross-cutting reference** | HTTP status codes, Cursor APIs, Windows/PowerShell tips |
| **Keyboard shortcuts** | Editor and Agent shortcuts taught in the course |

**Format:** Each term lists **full form** (if it is an acronym), then a **plain-language definition** for learners and instructors.

---

## Quick acronym index (A–Z)

| Term | Full form | One-line meaning |
|------|-----------|------------------|
| **API** | Application Programming Interface | Contract for programs to request data or actions from a service |
| **BI** | Business Intelligence | Dashboards and reports built from exported usage data |
| **CI/CD** | Continuous Integration / Continuous Deployment | Automated build, test, and release pipelines |
| **CLI** | Command-Line Interface | Run Cursor Agent from a terminal (`agent`) |
| **CSRF** | Cross-Site Request Forgery | Attack where another site triggers actions in your logged-in session |
| **CSV** | Comma-Separated Values | Tabular text export for spreadsheets and BI tools |
| **DAU** | Daily Active Users | Distinct users active on a given day |
| **DOM** | Document Object Model | Tree of elements on a web page (Browser tool) |
| **ETag** | Entity Tag | Version fingerprint for conditional HTTP caching |
| **GDPR** | General Data Protection Regulation | EU privacy rules affecting user data handling |
| **HMAC** | Hash-based Message Authentication Code | Signed digest proving a webhook payload was not tampered with |
| **HTTP** | Hypertext Transfer Protocol | Request/response protocol for web and APIs |
| **HTTPS** | HTTP Secure (TLS) | Encrypted HTTP — required for production APIs and webhooks |
| **IDE** | Integrated Development Environment | Editor like Cursor (code + terminal + tools) |
| **ISO** | International Organization for Standardization | Audit/compliance frameworks (e.g. ISO 27001) |
| **JSON** | JavaScript Object Notation | Structured text format for API bodies and responses |
| **JWT** | JSON Web Token | Compact signed token format for authentication |
| **LLM** | Large Language Model | Neural network that generates text one token at a time |
| **LSP** | Language Server Protocol | Backend that powers go-to-definition, diagnostics, etc. |
| **MCP** | Model Context Protocol | Standard for connecting AI to external tools and data |
| **OAuth** | Open Authorization | Delegated login without sharing passwords |
| **OpenAPI** | Open API Specification | Machine-readable description of REST endpoints |
| **PR** | Pull Request | Proposed code change reviewed before merge |
| **PWA** | Progressive Web App | Installable web app (e.g. `cursor.com/agents` on mobile) |
| **REST** | Representational State Transfer | HTTP APIs built around resources and verbs (GET, POST, …) |
| **ROI** | Return on Investment | Whether tool spend pays back in time or shipped work |
| **SDK** | Software Development Kit | Libraries for calling an API from your language |
| **SHA-256** | Secure Hash Algorithm (256-bit) | Common hash for webhook signature verification |
| **SOC 2** | Service Organization Control 2 | SaaS security/compliance audit framework |
| **SQL** | Structured Query Language | Language for relational databases |
| **SSE** | Server-Sent Events | Server pushes live events over one long HTTP connection |
| **TLS** | Transport Layer Security | Encryption layer under HTTPS |
| **URI** | Uniform Resource Identifier | General identifier (URLs are URIs) |
| **URL** | Uniform Resource Locator | Web address (browser, API, webhook endpoint) |
| **VM** | Virtual Machine | Isolated machine in the cloud (Cloud Agents run in VMs) |
| **WoW** | Week over Week | Compare this week’s metric to last week’s |
| **WSL** | Windows Subsystem for Linux | Run Linux tools on Windows |
| **YAML** | YAML Ain’t Markup Language | Human-readable config format (hooks, CI, etc.) |
| **npm** | Node Package Manager | JavaScript package registry and CLI |

---

## Day 1 overview

| Module | Title | Focus |
|--------|-------|-------|
| **1** | Mental Models for AI-Assisted Development | How LLMs work, limits, tokens, context, MCP, agents |
| **2** | Cursor Editor Essentials | Codebase orientation, diffs, Plan Mode, models, @mentions |
| **3** | Agent Modes and Tools | Ask / Agent / Plan, Browser & Terminal tools, prompting |
| **4** | Customizing Cursor for Your Team | Rules, repo instructions, Skills, MCP, hooks, subagents |
| **5** | Cursor CLI and Local Automation | Interactive CLI, one-shot, cloud handoff (`&`), sessions |

---

## Module 1 — Mental Models for AI-Assisted Development

**Goal:** Accurate mental models of how AI assistants work, their limits, and how to use them safely.

**Lessons:** 1.1 How AI Models Work · 1.2 Hallucinations · 1.3 Tokens and Pricing · 1.4 Context · 1.5 Tool Calling and MCP · 1.6 Agents

### Core terms

| Term | Full form | Definition |
|------|-----------|------------|
| **LLM** | Large Language Model | Model trained to predict the next token; powers Cursor’s chat and Agent. Not executing your code — predicting text. |
| **Next-token prediction** | — | Reads context, ranks likely next tokens, picks one, appends, repeats. Explains non-deterministic output. |
| **Probabilistic** | — | Same input can yield different outputs (unlike traditional `if`/`else` code). |
| **Deterministic** | — | Same input always same output — how conventional software behaves. |
| **Temperature** | — | Randomness knob: low = focused/repeatable; high = more creative/varied. |
| **Top-p** (nucleus sampling) | — | Limits the pool of tokens the model may choose on each step. |
| **Max tokens** | — | Cap on how long the model’s reply can be (cost and verbosity control). |
| **Training cutoff** | — | Date after which the model has no built-in knowledge unless you add context. |
| **Hallucination** | — | Confident but wrong output (fake API, wrong library, invented method). |
| **Grounding** | — | Tying answers to real sources: files, docs, URLs, tests — reduces hallucinations. |
| **Constrained decoding** | — | Restricting output shape (e.g. JSON mode, regex) so structure is valid. |
| **Self-consistency** | — | Running the same prompt multiple times and comparing/voting on answers. |
| **Human-in-the-loop** | — | Person reviews AI output before merge/deploy — core safety pattern in this course. |
| **Token** | — | Billing and context unit; smaller than a sentence (word fragment or symbol). |
| **Input token** | — | Prompt, attached files, instructions you send (usually cheaper). |
| **Output token** | — | Text the model generates (usually more expensive). |
| **Context** | — | Everything the model can “see” in one request: files, history, rules, @mentions. |
| **Context window** | — | Maximum context size; overflow drops or summarizes older material. |
| **Lost in the middle** | — | Models often under-use information buried in the middle of long context. |
| **Context engineering** | — | Deliberately choosing what to include/exclude in context for quality and cost. |
| **Tool calling** (function calling) | — | Model requests an action (read file, run command); host executes it. |
| **MCP** | Model Context Protocol | Open standard: AI hosts connect to tools, DBs, APIs via MCP servers. |
| **Agent** | — | In Cursor: AI that can use tools, edit files, run terminal — not chat-only. |
| **Agent loop** | — | Plan → act with tools → observe results → repeat until done or stopped. |
| **Autonomous agent** | — | Pursues a goal across many steps with minimal prompting; needs strong guardrails. |
| **Chatbot** | — | Q&A without file edits or tools — lower autonomy than Agent. |
| **AI debt** | — | Code that looked fine in chat but fails in CI or production without verification. |

### Module 1 — Instructor reminders

- Verify cited APIs and imports before merge.
- Prefer grounding (@files, docs) over open-ended “fix everything” prompts.
- Cost scales with tokens — context size and model choice matter.

---

## Module 2 — Cursor Editor Essentials

**Goal:** Core AI-assisted coding workflows in the Cursor editor.

**Lessons:** 2.1 Codebase Understanding · 2.2 Explaining Files/Symbols · 2.3 Safe Reviewable Changes · 2.4 Plan Mode · 2.5 Comparing Models · 2.6 @Mentions · 2.7 Checkpoints · 2.8 Terminal Tool (intro)

### Core terms

| Term | Full form | Definition |
|------|-----------|------------|
| **Cursor Agent** | — | AI panel that edits files, runs tools, uses terminal (with your approval). |
| **Ask Mode** | — | Read-only: answers questions, no file edits or tool execution. |
| **Agent Mode** | — | Can edit files, run terminal, use Browser/MCP — review diffs before accept. |
| **Plan Mode** | — | Agent drafts a step-by-step plan and asks questions before coding (`Shift+Tab`). |
| **Composer 2.5** | — | Cursor’s agent-optimized model family for multi-step coding and tools. |
| **Diff review** | — | Read added/removed lines before accepting AI edits — primary quality gate. |
| **Checkpoint** | — | Snapshot of code + conversation to roll back after an experiment. |
| **@mention** | — | Point Agent at precise context: file, folder, symbol, web, branch, etc. |
| **@file / @folder / @symbol** | — | Include specific paths or symbols in context. |
| **@web** | — | Pull web page content into context (verify freshness). |
| **@branch** | — | Include branch-related context for PR-oriented work. |
| **Semantic search** | — | Find code/docs by meaning, not only exact keywords (codebase indexing). |
| **Vector retrieval** | — | Embeddings of text to find similar concepts with different wording. |
| **Scope creep** | — | Agent changes more than asked — constrain with explicit scope and “DO NOT” lists. |
| **LSP** | Language Server Protocol | Powers diagnostics, go-to-definition — Agent uses it indirectly via the editor. |

### Module 2 — Key shortcuts

| Action | Shortcut (Windows) |
|--------|-------------------|
| Open Agent panel | `Ctrl+I` |
| Open terminal | `` Ctrl+` `` |
| Plan Mode toggle | `Shift+Tab` (in Agent input) |
| Command Palette | `Ctrl+Shift+P` |
| Inline edit (where taught) | `Ctrl+K` |

### Module 2 — File patterns

| Path | Purpose |
|------|---------|
| `.cursor/project-overview.md` | Saved codebase orientation for the team |

---

## Module 3 — Agent Modes and Tools

**Goal:** Use modes and tools effectively; write constrained, verifiable prompts.

**Lessons:** 3.1 Mode Continuum · 3.2 Browser Tool · 3.3 Terminal Tool · 3.4 Effective Prompting

### Core terms

| Term | Full form | Definition |
|------|-----------|------------|
| **Mode continuum** | — | Spectrum from Ask (read-only) → Agent (edit + tools) → Plan (design first). |
| **Browser tool** | — | Agent opens a page, inspects DOM, reads console/network (with approval). |
| **Terminal tool** | — | Agent proposes shell commands; you approve; it reads stdout/stderr. |
| **Constrained prompt** | — | Explicit files, patterns, scope, success criteria — reduces guesswork. |
| **DO NOT list** | — | Boundaries: files or behaviors the agent must not touch. |
| **Prompt template** | — | Reusable prompt skeleton (e.g. `.cursor/prompt-templates.md`). |
| **Approval rules** | — | Team policy for which commands/edits require human OK every time. |

### Module 3 — Safety patterns

- Terminal: start with read-only commands (`ls`, `git status`) before destructive ops.
- Browser: use for UI verification, not as a substitute for automated tests.
- One logical change per Agent turn when learning diff review.

---

## Module 4 — Customizing Cursor for Your Team

**Goal:** Encode team standards in Rules, instructions, Skills, MCP, hooks, and subagents.

**Lessons:** 4.1 Creating a Rule · 4.2 Repository Instructions · 4.3 Skills · 4.4 MCP & Hooks · 4.5 Subagents

### Core terms

| Term | Full form | Definition |
|------|-----------|------------|
| **Rule** | — | Persistent Markdown instructions in `.cursor/rules/*.mdc` applied automatically. |
| **`.mdc`** | Markdown Cursor | Rule file extension; can include glob patterns for when rule applies. |
| **Repository Instructions** | — | Single project overview: stack, commands, conventions (`.cursor/repository-instructions.md`). |
| **AGENTS.md** | — | Common filename/convention for repo-level agent guidance (team docs may alias this). |
| **Skill** | — | Packaged workflow in `.cursor/skills/<name>/SKILL.md` invoked on demand or via slash command. |
| **Slash command** | — | Typed shortcut (e.g. `/review`) often backed by a Skill or hook workflow. |
| **Hook** | — | Script run on agent events (`beforeShellExecution`, `afterFileEdit`, …) from `.cursor/hooks.json`. |
| **MCP server** | Model Context Protocol server | Exposes tools/resources (DB, APIs, issue trackers) to the Agent. |
| **stdio transport** | standard I/O transport | MCP server speaks over stdin/stdout (local process). |
| **HTTP transport** | — | MCP server exposed as HTTP endpoint (remote or local). |
| **Subagent** | — | Delegated specialist agent for a subtask; can run in parallel or isolation. |
| **Team hook** | — | Org-wide hooks on Enterprise; plus repo `.cursor/hooks.json`. |

### Module 4 — File layout

| Path | Purpose |
|------|---------|
| `.cursor/rules/*.mdc` | Team coding standards, security, per-glob rules |
| `.cursor/repository-instructions.md` | Lightweight repo context |
| `.cursor/skills/*/SKILL.md` | Reusable workflows (PR review, security audit) |
| `.cursor/hooks.json` | Event-driven automation and guardrails |
| `~/.cursor/mcp.json` | User-level MCP server config (example in course) |

---

## Module 5 — Cursor CLI and Local Automation

**Goal:** Terminal-based Agent workflows, scripting, and cloud handoff.

**Lessons:** 5.1 Interactive CLI · 5.2 One-Shot CLI · 5.3 Cloud Handoff · 5.4 Listing and Resuming Sessions

### Core terms

| Term | Full form | Definition |
|------|-----------|------------|
| **Cursor CLI** | — | `agent` command: interactive sessions or one-shot prompts from shell/CI. |
| **Interactive CLI** | — | Long-lived `agent` session: chat, models, `/commands`, resume later. |
| **One-shot CLI** | — | `agent -p "..."` — single prompt, exits (scripts, CI). |
| **Cloud handoff** | — | Prefix message with `&` in CLI to continue work as a **Cloud Agent** on Cursor infra. |
| **Cloud Agent** | — | Agent running in Cursor’s cloud VM against a connected GitHub/GitLab repo. |
| **Agent ID** | — | Identifier for a run; used in dashboard URL and `agent --resume`. |
| **`/resume`** | — | CLI command to list or resume saved sessions. |
| **`/compress`** | — | Summarize long session context to free context window. |
| **`/quit`** | — | Exit interactive CLI (cloud task keeps running after `&` handoff). |

### Module 5 — Commands (Windows / PowerShell)

| Command | Purpose |
|---------|---------|
| `agent` | Start interactive CLI |
| `agent -p "prompt"` | One-shot prompt |
| `agent --version` | Verify CLI installed |
| `agent --resume <id>` | Resume session by ID |
| `& your prompt` | At CLI `>` prompt — hand off to Cloud Agent |
| `irm 'https://cursor.com/install?win32=true' \| iex` | Install CLI on Windows (lab) |

### Module 5 — Notifications (cloud handoff)

| Channel | Expectation |
|---------|-------------|
| **Dashboard** | **Always** — `https://cursor.com/agents` shows Running → Completed/Failed |
| **Email** | **Optional** — only if enabled in account/cloud notification settings |
| **Slack** | **Optional** — if workspace Cursor Slack app is configured |
| **Webhooks** | **Automation** — Module 8; not automatic for every CLI handoff |

---

## Day 2 overview

| Module | Title | Focus |
|--------|-------|-------|
| **6** | Cloud Agents in the UI | Launch, monitor, artifacts, Slack/Discord |
| **7** | Cursor API Foundations | Keys, rate limits, ETag, models |
| **8** | Cloud Agents API and Webhooks | Create agents, SSE, artifacts, HMAC, ngrok |
| **9** | Admin and Analytics APIs | Team, usage, spend limits, DAU, leaderboards |
| **10** | AI Code Tracking and Reporting | Commit metrics, exports, compliance reporting |

---

## Module 6 — Cloud Agents in the UI

**Goal:** Launch and monitor Cloud Agents from the web UI; artifacts and integrations.

**Lessons:** 6.1 Launching a Cloud Agent · 6.2 Artifacts · 6.3 Messaging (Slack, Discord)

### Core terms

| Term | Full form | Definition |
|------|-----------|------------|
| **Cloud Agent** (UI) | — | Start from Desktop (Cloud dropdown), `cursor.com/agents`, Slack, GitHub `@cursor`, Linear, API. |
| **Background Agent** | — | Former product name for Cloud Agents (same idea: runs off your laptop). |
| **Max Mode** | — | Cloud Agents use high-capability models; no Max Mode off toggle for cloud runs. |
| **Development environment** | — | VM image: deps, secrets, startup commands — agent can build/test like a dev machine. |
| **`.cursor/environment.json`** | — | Dockerfile or env config for cloud agent setup. |
| **Snapshot** | — | Saved base environment image for faster agent startup. |
| **Artifact** | — | Downloadable output: logs, patches, screenshots, videos from a run. |
| **Auto-create PR** | — | Setting for agent to open a pull request when work completes. |
| **Remote desktop control** | — | Take over agent’s VM desktop to manually verify UI changes. |
| **Automations** | — | Scheduled/event-driven cloud agents (GitHub, Slack, webhooks, etc.) at `cursor.com/automations`. |
| **PWA** | — | Install `cursor.com/agents` to home screen for mobile monitoring. |

### Module 6 — Integrations

| Platform | Trigger pattern |
|----------|-----------------|
| **Slack** | `@cursor` — launch agents; notifications when configured |
| **GitHub** | Comment `@cursor` on PR/issue |
| **Linear** | `@cursor` on issues |
| **Discord** | Bot/integration (demo in course) |

---

## Module 7 — Cursor API Foundations

**Goal:** Authenticate, handle errors, cache with ETags, list models.

**Lessons:** 7.1 API Landscape · 7.2 Authentication · 7.3 Rate Limits · 7.4 ETag Caching · 7.5 List Models

### Cursor API families (course)

| API | Key type | Typical use |
|-----|----------|-------------|
| **Cloud Agents API** | User API key | Create/monitor agents, artifacts, webhooks |
| **Admin API** | Admin API key | Team members, usage, spend limits, analytics |
| **AI Code Tracking API** | Admin API key | Commit metrics, change events, exports |
| **Webhooks** | User API key | Receive completion events (no polling) |
| **OpenAI-compatible API** | User API key | Drop-in for tools expecting OpenAI-style endpoints |

### Core terms

| Term | Full form | Definition |
|------|-----------|------------|
| **User API Key** | — | Scoped to your user — agents, user-level endpoints. |
| **Admin API Key** | — | Org-wide — team, usage, governance (never in client apps). |
| **HTTP Basic auth** | — | API key as username, empty password (`-u "KEY:"`) — common in curl examples. |
| **Bearer token** | — | `Authorization: Bearer <key>` — alternative auth style. |
| **Rate limit** | — | Max requests per time window; exceed → **HTTP 429 Too Many Requests**. |
| **Exponential backoff** | — | Increase wait between retries after 429/5xx. |
| **ETag** | Entity Tag | Opaque version string returned by server (often in `ETag` header). |
| **If-None-Match** | — | Request header sending cached ETag; server returns **304** if unchanged. |
| **304 Not Modified** | — | No response body — use cached copy; saves bandwidth and cost. |
| **Pagination** | — | Split large lists with `offset`/`limit` or cursor parameters. |
| **Idempotent** | — | Repeating the same request doesn’t change state (important for retries). |

### Module 7 — HTTP status codes (course)

| Code | Meaning | Typical action |
|------|---------|----------------|
| **200** | OK | Parse JSON body |
| **401** | Unauthorized | Fix API key / auth header |
| **403** | Forbidden | Wrong key type or insufficient permissions |
| **429** | Too Many Requests | Backoff; read rate-limit headers |
| **304** | Not Modified | Use cached ETag response |
| **5xx** | Server error | Retry with backoff |

### Module 7 — Windows API tips

| Tip | Detail |
|-----|--------|
| **`curl.exe`** | Use explicit `.exe` in PowerShell to avoid alias issues |
| **`$env:VAR`** | Store API keys in session env vars (not committed) |
| **`ConvertFrom-Json`** | Parse API responses in PowerShell |

---

## Module 8 — Cloud Agents API and Webhooks

**Goal:** Programmatic agents, SSE streaming, artifacts, verified webhooks.

**Lessons:** 8.1 Create via API · 8.2 SSE · 8.3 Artifacts · 8.4 HMAC · 8.5 ngrok · 8.6 E2E workflow

### Core terms

| Term | Full form | Definition |
|------|-----------|------------|
| **POST** | — | HTTP verb to create a resource (e.g. launch agent). |
| **SSE** | Server-Sent Events | One HTTP connection; server streams `event:` lines over time. |
| **Last-Event-ID** | — | Header to resume SSE stream after disconnect. |
| **Webhook** | — | HTTP POST to your URL when agent status changes (e.g. FINISHED). |
| **HMAC-SHA256** | Hash-based Message Authentication Code (SHA-256) | Verify webhook body using shared secret and signature header. |
| **ngrok** | — | Public HTTPS tunnel to localhost for receiving webhooks in dev. |
| **Presigned URL** | — | Time-limited download link for artifacts (expires). |
| **`notifyOnStart` / `notifyOnComplete` / `notifyOnError`** | — | Webhook payload flags for which events to send. |
| **Polling** | — | Repeatedly calling status API until FINISHED — alternative to webhooks. |
| **`agent.id` / `run.id`** | — | IDs returned from create-agent API; used in URLs and follow-up calls. |
| **`autoCreatePR`** | — | JSON field to request automatic pull request creation. |
| **`startingRef`** | — | Git branch/ref the cloud agent starts from (e.g. `main`). |

### Module 8 — Webhook security checklist

1. Use **HTTPS** endpoint only in production.
2. Verify **HMAC** signature before trusting body.
3. Treat payload as untrusted input — validate schema.
4. Respond quickly (e.g. `200`) then process async if needed.

---

## Module 9 — Admin and Analytics APIs

**Goal:** Team governance, usage reporting, spend limits, responsible leaderboards.

**Lessons:** 9.1 Team Members · 9.2 Daily Usage · 9.3 Spend Limits · 9.4 Model Usage · 9.5 DAU · 9.6 Leaderboards · 9.7 Conversation Insights (demo) · 9.8 Safe Removal (demo)

### Core terms

| Term | Full form | Definition |
|------|-----------|------------|
| **Admin API** | — | Requires **Admin** key — not User key — for team and analytics endpoints. |
| **Daily usage data** | — | Per-day token/cost aggregates for chargeback and budgeting. |
| **Spend limit** | — | Monthly cap per user; can **alert** or **block** overage. |
| **`alert` vs `block`** | — | Alert: notify but allow usage; block: stop usage over limit. |
| **Model usage analytics** | — | Breakdown by model to find expensive defaults. |
| **DAU** | Daily Active Users | Count of distinct users active on a date. |
| **WoW** | Week over Week | Compare metric to prior week for trends. |
| **Leaderboard** | — | Ranked usage views — must avoid exposing private data. |
| **Anonymization** | — | Mask emails/names in exports (roles or hashed IDs). |
| **Soft delete** | — | Deactivate account; retain audit trail. |
| **Hard delete** | — | Permanent removal — irreversible; compliance-sensitive. |
| **Audit-first** | — | Log and review before destructive admin actions. |
| **Resource transfer** | — | Reassign repos/tickets when removing a team member. |
| **Intent analysis** | — | (Demo) Categorize what developers ask agents to do. |
| **Conversation complexity** | — | (Demo) Rough difficulty/depth of agent conversations. |

### Module 9 — Governance principles

- Use **Admin API key** only on secure servers — never in front-end code.
- Leaderboards: prefer **aggregates** and **anonymized** identifiers.
- Bulk CSV updates (spend limits): validate rows before apply.

---

## Module 10 — AI Code Tracking and Reporting

**Goal:** Measure AI-assisted contribution; export for BI and compliance dashboards.

**Lessons:** 10.1 AI Commit Metrics · 10.2 Bulk CSV Export · 10.3 Granular Change Events · 10.4 Reporting Architecture (take-home)

### Core terms

| Term | Full form | Definition |
|------|-----------|------------|
| **AI commit metrics** | — | How much committed code came from AI assistance vs human-only. |
| **Acceptance rate** | — | Share of AI-suggested edits accepted vs rejected. |
| **Granular change events** | — | Per-edit audit: file, lines, model, accepted/rejected. |
| **Streaming export** | — | Large CSV/event streams without loading entire dataset in memory. |
| **Bulk export** | — | Admin API export for BI tools (Power BI, Tableau, etc.). |
| **Reporting dashboard architecture** | — | ETL: API → warehouse → dashboards + alerts (take-home design). |
| **Compliance reporting** | — | Evidence of AI usage policies, retention, and anonymization. |

### Module 10 — Privacy and compliance

| Practice | Why |
|----------|-----|
| **Anonymize** emails in org-wide leaderboards | Reduces GDPR/privacy risk |
| **Retention policy** | Define how long granular events are stored |
| **Purpose limitation** | Use metrics for improvement — not punitive surveillance without policy |

---

## Cross-cutting reference

### Cursor product surfaces

| Surface | Access | Best for |
|---------|--------|----------|
| **Editor Agent** | `Ctrl+I`, Agent mode | Daily coding, diffs, local tools |
| **Plan Mode** | `Shift+Tab` | Large features before edits |
| **CLI** | `agent` / `agent -p` | Scripts, CI, terminal-first |
| **Cloud UI** | `cursor.com/agents` | Long runs, parallel agents, mobile check-in |
| **API** | User/Admin keys | Automation, webhooks, analytics |

### Git and Cloud Agent workflow

| Term | Definition |
|------|------------|
| **Clone** | Cloud agent copies repo from GitHub/GitLab to its VM |
| **Branch** | Agent works on a separate branch; may push for PR |
| **PR** | Review merge-ready changes; CI runs on agent branches |
| **Secrets** | Stored in Cursor cloud agent settings — not committed to git |

### Security terms (course)

| Term | Full form | Definition |
|------|-----------|------------|
| **Secret** | — | API key, password, token — never commit; use env or Cursor secrets |
| **Least privilege** | — | User key for agents; Admin key only on backend for analytics |
| **Webhook signing** | — | HMAC proves payload from Cursor, not a random POST |

### Cost and model selection (reminder)

| Concept | Tip |
|---------|-----|
| **Input vs output pricing** | Output tokens usually cost more — long Agent replies add up |
| **Context size** | Larger context = more input tokens per turn |
| **Model tier** | Use smaller/faster models for simple tasks; reserve premium for hard problems |
| **Cache** | Repeated identical prefix may be cheaper (provider-dependent) |

---

## Keyboard shortcuts (Windows, as taught)

| Shortcut | Action |
|----------|--------|
| `Ctrl+I` | Open Agent panel |
| `` Ctrl+` `` | Toggle terminal |
| `Ctrl+Shift+P` | Command Palette |
| `Shift+Tab` | Plan Mode (in Agent input) |
| `Ctrl+K` | Inline edit (where used in Module 2) |
| `Ctrl+L` | Chat (if referenced in your delivery) |

**Terminal profile:** `` Ctrl+` `` → **Terminal: Select Default Profile** → **PowerShell** (Modules 5–10 labs).

---

## CLI slash commands (Module 5)

| Command | Purpose |
|---------|---------|
| `/resume` | List or resume sessions |
| `/compress` | Summarize long session history |
| `/quit` | Exit interactive CLI |
| `/help` | CLI help (if available in your CLI version) |

---

## Related repository files

| Resource | Path |
|----------|------|
| Full course index | [`FINAL_TABLE_OF_CONTENTS.md`](FINAL_TABLE_OF_CONTENTS.md) |
| Slide deck (present) | [`slides/course-complete-marp-with-notes.html`](slides/course-complete-marp-with-notes.html) |
| Lab guides | [`slide-exercises/`](slide-exercises/) |
| Optional deep labs | [`core-exercises/`](core-exercises/) · [`api-exercises/`](api-exercises/) |
| Concept readmes | [`learn/`](learn/) · [`docs-content-readmes/`](docs-content-readmes/) |
| API summaries | [`api-content-readmes/`](api-content-readmes/) |
| Instructor speaker script | [`slides/course-complete-speaker-notes.md`](slides/course-complete-speaker-notes.md) |

---

## Glossary source

Term definitions in this cheatsheet align with the course speaker-notes glossary in [`scripts/speaker_notes_glossary.py`](scripts/speaker_notes_glossary.py). When Cursor product behavior changes, update lab guides and this file together.

---

*Cursor Training Program — 10 modules · 52 lessons · 40 slide exercises · ~11.5 hours*
