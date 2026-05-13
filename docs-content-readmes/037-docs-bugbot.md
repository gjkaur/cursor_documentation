This is the **Bugbot** documentation – it explains how Cursor can **automatically review pull requests** and identify bugs, security issues, and code quality problems.

Think of Bugbot as an **AI code reviewer** that works 24/7, catches issues before they merge, and can even **automatically fix** the bugs it finds.

Let me break this down for a beginner.

---

## What Is Bugbot? (The 10-Second Summary)

**Bugbot reviews pull requests and identifies bugs, security issues, and code quality problems.**

| Without Bugbot | With Bugbot |
|----------------|--------------|
| Wait for human code review | Instant AI review |
| Missed bugs reach production | Issues caught before merge |
| Manual bug fixing | Automatic fixes available |

> *"On Teams and Individual Plans, Bugbot includes a free tier: every user gets a limited number of free PR reviews."*

---

## How Bugbot Works

| Feature | What it does |
|---------|--------------|
| **Automatic reviews** | Runs on every PR update |
| **Manual trigger** | Comment `cursor review` or `bugbot run` on any PR |
| **Context-aware** | Reads existing PR comments to avoid duplicate suggestions |
| **Fix links** | "Fix in Cursor" or "Fix in Web" open issues directly |

### What Bugbot Analyzes:

- **PR diffs** (code changes)
- **Security issues** (vulnerabilities, exposed secrets)
- **Bugs** (logic errors, edge cases)
- **Code quality** (style, maintainability)

---

## Setup

### Step 1: Connect Repositories

Connect through the Cursor dashboard:

| Platform | Support |
|----------|---------|
| **GitHub** | ✅ Including GitHub Enterprise Server |
| **GitLab** | ✅ Including GitLab Self-Hosted |

### Step 2: Enable Bugbot

After connecting, return to the **Bugbot dashboard** to enable Bugbot on specific repositories.

---

## Configuration

### Repository Settings (Team Admins)

| Setting | What it does |
|---------|--------------|
| **Enable per repository** | Turn Bugbot on/off for specific repos |
| **Allow/deny lists** | Control which reviewers can use Bugbot |
| **Run only once per PR** | Skip subsequent commits after first review |

> *"Bugbot runs for all contributors to enabled repositories, regardless of team membership."*

### Personal Settings (Team Members)

Team members can override settings for their own PRs:

| Setting | Effect |
|---------|--------|
| **Run only when mentioned** | Only trigger on `cursor review` or `bugbot run` comments |
| **Run only once per PR** | Skip subsequent commits |
| **Enable reviews on draft PRs** | Include draft PRs in automatic reviews |

---

## Rules System

Bugbot has **multiple layers** of rules that determine what to check for.

### Order of Application (Highest to Lowest Priority):

| Priority | Rule Type |
|----------|-----------|
| 1 | **Team Rules** (dashboard, organization-wide) |
| 2 | **Repository Rules** (learned + manual) |
| 3 | **Project BUGBOT.md** (in your repository) |
| 4 | **User Rules** (personal) |

### 1. Team Rules (Dashboard)

Team admins can create rules that apply to **all repositories** in the team. Enforces organization-wide standards.

### 2. Repository Rules

Two types:

| Type | Description |
|------|-------------|
| **Learned Rules** | Generated automatically from team's GitHub activity. Can also teach Bugbot inline: comment `@cursor remember [fact]` on any PR. |
| **Manual Rules** | Created manually in Bugbot dashboard for individual repositories. |

### 3. Project Rules (BUGBOT.md Files)

Create `.cursor/BUGBOT.md` files to provide **project-specific context**.

**Nested rules are automatically included** when reviewing files in that directory:

```
project/
├── .cursor/BUGBOT.md              # Always included (project-wide)
├── backend/
│   └── .cursor/BUGBOT.md          # Included when reviewing backend files
├── api/
│   └── .cursor/BUGBOT.md          # Included when reviewing API files
└── frontend/
    └── .cursor/BUGBOT.md          # Included when reviewing frontend files
```

### Rule Fields:

| Field | Description |
|-------|-------------|
| **Name** | Short title for the rule |
| **Rule content** | Instructions Bugbot should follow (style gates, paths, review expectations) |
| **Scoped paths** | Optional glob patterns (e.g., `src/components/**`). Leave empty for whole repo. |

### Example Rules:

| Category | Example Rule |
|----------|--------------|
| **Security** | "Flag any use of `eval()` or `exec()`" |
| **OSS licenses** | "Prevent importing disallowed licenses" |
| **Language standards** | "Flag React `componentWillMount` usage" |
| **Standards** | "Require tests for backend changes" |
| **Style** | "Disallow TODO comments" |

### Rule Analytics:

Track how rules perform on real PRs:

| Metric | Meaning |
|--------|---------|
| **Issues found** | Number of findings involving this rule |
| **PRs reviewed** | Number of PRs where findings appeared |
| **Accepted issues** | Number of findings your team accepted |
| **Acceptance rate** | Percentage of findings accepted |

---

## Autofix (Automatic Bug Fixing)

This is a **powerful feature** – Bugbot can automatically spawn a Cloud Agent to fix bugs found during PR reviews.

### How Autofix Works:

| Step | What happens |
|------|--------------|
| 1 | Bugbot finds bugs during PR review |
| 2 | Spawns Cloud Agent to analyze and fix issues |
| 3 | Agent pushes fixes to existing branch or new branch |
| 4 | Bugbot posts comment on PR with results |

### Autofix Modes (Team Admin Settings):

| Mode | Behavior |
|------|----------|
| **Off** | Autofix disabled by default |
| **Create New Branch (Recommended)** | Push fixes to a new branch for team members |
| **Commit to Existing Branch** | Push fixes directly to PR branch (max 3 attempts per PR to prevent loops) |

> *"Individual team members can override these defaults in their personal settings."*

### Model Selection:

Autofix uses your **Default agent model** from Settings → Models. Falls back to team default or system default if not set.

### Requirements:

| Requirement | Status |
|-------------|--------|
| **Usage-based pricing** | Required |
| **Storage enabled** | Required (not in Legacy Privacy Mode) |

### Billing:

Autofix uses **Cloud Agent credits** and is billed at your plan rates.

---

## Manual Trigger

Start a Bugbot review manually by commenting on any PR:

```
cursor review
```

or

```
bugbot run
```

### Verbose Mode (Debugging):

```
cursor review verbose=true
```

or

```
bugbot run verbose=true
```

This provides detailed logs and a request ID to help troubleshoot issues.

---

## Analytics Dashboard

The Bugbot dashboard shows:

| Metric | What it tracks |
|--------|----------------|
| **Total reviews** | Number of PRs reviewed |
| **Issues found** | Total bugs/security issues detected |
| **Acceptance rate** | Percentage of suggestions accepted |
| **Recent reviews** | List of recent PR reviews |
| **Per-rule analytics** | How each rule is performing |

---

## MCP Support (Team/Enterprise)

Bugbot is integrated with **MCP servers** so your AI tools can interact with Bugbot directly.

### To enable:

1. Follow MCP documentation for server setup
2. Add tools to Bugbot in the Bugbot dashboard

> *"MCP support is available on Team and Enterprise plans only."*

---

## Admin Configuration API (Team/Enterprise)

Team admins can use the **Bugbot Admin API** to manage repositories and control user access programmatically.

### Authentication:

All endpoints require a team **Admin API Key** passed as a Bearer token:

```
Authorization: Bearer $API_KEY
```

### Create an API Key:

1. Settings tab in Cursor dashboard
2. Under Advanced → **New Admin API Key**
3. Save the API key

**Rate limit:** 60 requests per minute per team

### Enabling/Disabling Repositories:

```bash
curl -X POST https://api.cursor.com/bugbot/repo/update \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "repoUrl": "https://github.com/your-org/your-repo",
    "enabled": true
  }'
```

### Listing Repositories:

```bash
curl https://api.cursor.com/bugbot/repos \
  -H "Authorization: Bearer $API_KEY"
```

### Managing User Access:

First, enable **allowlist** or **blocklist mode** in team Bugbot settings.

| Mode | allow: true | allow: false |
|------|-------------|--------------|
| **Allowlist** | Adds user to list (can use Bugbot) | Removes user (cannot use) |
| **Blocklist** | Removes from blocklist (can use) | Adds to blocklist (cannot use) |

**Add/remove user:**

```bash
curl -X POST https://api.cursor.com/bugbot/user/update \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "octocat", "allow": true}'
```

> *"Usernames are normalized to lowercase. Allowlist applies across all GitHub and GitLab installations owned by that team."*

---

## Pricing

### Free Tier:

| Plan | Free reviews |
|------|--------------|
| **Individual** | Limited free PR reviews per month |
| **Teams** | Each team member gets their own free reviews |

> *"When you reach the limit, reviews pause until your next billing cycle. You can upgrade anytime to a paid Bugbot plan."*

### Pro Tier (Teams):

| Pricing | Details |
|---------|---------|
| **Per-user billing** | $40 per user per month |
| **Who counts?** | Users who authored PRs reviewed by Bugbot in a month |
| **Seat assignment** | First-come, first-served each billing cycle |
| **Seat limits** | Admins can set maximum seats per month |

### Abuse Guardrails:

> *"Pooled cap of 200 pull requests per month for every Bugbot license."*

**Example:** If your team has 100 users, you can review 20,000 pull requests per month. Contact support if you need more.

---

## Troubleshooting

If Bugbot isn't working:

| Step | Action |
|------|--------|
| 1 | **Enable verbose mode** – Comment `cursor review verbose=true` or `bugbot run verbose=true` |
| 2 | **Check permissions** – Verify Bugbot has repository access |
| 3 | **Verify installation** – Confirm GitHub app is installed and enabled |
| 4 | **Include request ID** – When reporting issues, include the request ID from verbose mode |

---

## Common Beginner Questions

### Q: Does Bugbot read GitHub PR comments?
**A:** Yes – it reads existing comments to avoid duplicate suggestions and build on prior feedback.

### Q: Is Bugbot privacy-mode compliant?
**A:** Yes – respects Cursor's privacy mode settings.

### Q: What happens when I hit the free tier limit?
**A:** Reviews pause until your next billing cycle. You can upgrade to Pro anytime.

### Q: How do I give Bugbot access to my GitHub Enterprise Server instance?
**A:** See the GitHub integration documentation.

### Q: Can Bugbot automatically fix bugs?
**A:** Yes – Autofix feature spawns a Cloud Agent to fix issues (requires usage-based pricing).

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **What it does** | Automatically reviews PRs for bugs, security, quality |
| **Trigger** | Automatic on PR updates, or manual `cursor review` |
| **Free tier** | Limited reviews per month (Individual & Teams) |
| **Pro tier** | $40/user/month (Teams) |
| **Rules** | Team → Repository → Project (BUGBOT.md) → User |
| **Autofix** | Cloud Agent automatically fixes bugs (optional) |
| **MCP support** | Team/Enterprise only |
| **Admin API** | Manage repos and user access programmatically |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is Bugbot?** | AI code reviewer for pull requests |
| **How do I use it?** | Connect repository in dashboard, then it runs automatically |
| **Does it cost money?** | Free tier available; Pro tier is $40/user/month for teams |
| **Can it fix bugs automatically?** | Yes – Autofix spawns Cloud Agent to fix issues |
| **Can I customize what it checks for?** | Yes – rules in dashboard or BUGBOT.md files |
| **How do I trigger it manually?** | Comment `cursor review` on any PR |

---

## The Bottom Line

**Bugbot is like having an AI code reviewer on your team that works 24/7.**

**Think of it as:**
- **Without Bugbot** = Waiting for human code review (hours/days) ⏰
- **With Bugbot** = Instant AI review + optional automatic fixes ⚡

**For teams:** Bugbot catches bugs before they reach production, enforces coding standards, and frees up human reviewers for complex decisions. The Autofix feature is a game-changer – it doesn't just find bugs, it fixes them.

**For individuals:** The free tier gives you a limited number of reviews. Great for open source projects or personal repos.

**The most powerful features:**
1. **Autofix** – Automatically spawns Cloud Agent to fix found bugs
2. **Learned rules** – Bugbot learns from your team's activity
3. **Nested BUGBOT.md** – Project-specific rules that automatically apply to relevant files
4. **Admin API** – Programmatically manage repos and user access

Would you like me to explain any specific part of Bugbot in more detail?