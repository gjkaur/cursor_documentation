This is the **Security Review** documentation – it explains how Cursor can automatically scan your code for **security bugs, risky patterns, and vulnerabilities**.

Think of Security Review as having a **security expert** constantly reviewing your code – both when you create pull requests AND on a regular schedule, looking for vulnerabilities before they become problems.

Let me break this down for a beginner. (Note: This is a **Teams/Enterprise** feature.)

---

## What Is Security Review? (The 10-Second Summary)

**Security Review agents scan your code for security bugs, risky patterns, and vulnerabilities.**

| Without Security Review | With Security Review |
|------------------------|----------------------|
| Manual security checks | Automated scanning |
| Vulnerabilities reach production | Caught before merge |
| Security debt accumulates | Regular scans find existing issues |

> *"This feature is available only for Teams and Enterprise plans."*

---

## Two Types of Security Review Agents

| Agent Type | What it does | When it runs |
|------------|--------------|--------------|
| **Security Review** | Checks pull requests before they merge | On PR/merge request events |
| **Vulnerability Scanner** | Scans codebase at rest for pre-existing issues | On recurring schedule (cron) |

### Security Review (PR-Time):

Catches vulnerabilities **during code review** – before they merge to main.

### Vulnerability Scanner (At Rest):

Finds:
- Pre-existing vulnerabilities
- Long-standing issues
- Problems missed during PR review

> *"Use it to find pre-existing vulnerabilities, long-standing issues, and problems missed during PR review."*

---

## Setup

To configure Security Review:

1. Open the **Security Review Dashboard**
2. Create your first agent

---

## Triggers

### Security Review Agents (PR-Time):

Support **Git-based Automations triggers**:
- Pull request events
- Merge request events

> *"Use these triggers to run security checks when code changes."*

### Vulnerability Scanner Agents (Scheduled):

Support **cron-based triggers**:
- Run on recurring schedule
- Independent of pull request activity

**Example:** Scan your entire codebase every night at 2 AM.

---

## Security Checks

Both agent types include **built-in security checks**. You can:

| Action | What it does |
|--------|--------------|
| **Enable** individual checks | Turn on specific security rules |
| **Disable** individual checks | Turn off rules that don't apply |
| **Customize per agent** | Different agents can check different things |

---

## Custom Instructions

Give each agent more context:

| Instruction Type | Example |
|------------------|---------|
| **Prioritization** | "Focus on authentication and authorization issues" |
| **Project-specific expectations** | "Our app handles PII, prioritize data leakage" |
| **Behavior definition** | "Always include remediation steps" |

---

## Tools and MCPs

Both agent types support **tools and MCPs**.

> *"Each agent needs at least one tool or MCP to run."*

### Use Cases:

| Integration | Purpose |
|-------------|---------|
| **Slack channel** | Send vulnerability alerts to team |
| **Issue tracker** | Create tickets for security findings |
| **Connected system** | Integrate with existing security tools |

### Configuration Tips:

| Practice | Why |
|----------|-----|
| **Add custom instructions** | Explain when/how to use each MCP |
| **Give extra context** | From tools/MCPs before reporting findings |

---

## Environment Setup

Security Review agents run on **Cloud Agents**.

| Option | Description |
|--------|-------------|
| **Cursor's cloud** | No additional setup required |
| **Self-hosted Cloud Agents** | Run reviews in your own environment |

---

## Billing

Security Review is billed at the **team usage level**:

| Billing Aspect | Details |
|----------------|---------|
| **Usage charged to** | Team's usage pool |
| **Service account** | Agents run under shared team service account |
| **Individual impact** | Does NOT affect any individual user's usage |

> *"Agents run under a shared team service account, so they don't affect any individual user's usage."*

---

## Analytics

Security Review tracks **three key metrics** across agent runs:

| Metric | What it measures |
|--------|------------------|
| **Vulnerabilities found** | Number of security findings reported |
| **Issues fixed** | Number of findings resolved after reporting |
| **Resolution rate** | Percentage of findings fixed |

### How Resolution is Determined:

> *"To determine whether an issue was fixed, Cursor uses LLMs to review incremental diffs and assess whether the flagged issue was resolved."*

**This is powerful** – Cursor automatically tracks whether your team actually fixed the vulnerabilities it found.

---

## Viewing Runs

Every agent run is tracked in the dashboard.

| Information available |
|-----------------------|
| When the agent ran |
| Which tools it used |
| Final status |
| How long it took |

> *"Open a run to inspect the underlying Cloud Agent for more detail about what the agent did."*

---

## Security Review vs. Agent Review vs. Bugbot

| Feature | Security Review | Agent Review | Bugbot |
|---------|-----------------|--------------|--------|
| **Focus** | Security vulnerabilities | General code quality | Bugs + security + quality |
| **PR-time scanning** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Scheduled scanning** | ✅ Yes (cron) | ❌ No | ❌ No |
| **Custom rules** | ✅ Yes | ✅ Yes | ✅ Yes |
| **MCP integration** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Availability** | Teams/Enterprise only | All plans | All plans (free tier) |

---

## Common Beginner Questions

### Q: Is this available on Individual plans?
**A:** No – Security Review is only for Teams and Enterprise plans.

### Q: Do I need to set up Cloud Agents?
**A:** Security Review uses Cloud Agents. You can use Cursor's cloud (no setup) or configure self-hosted.

### Q: Can I schedule daily scans?
**A:** Yes – Vulnerability Scanner agents support cron-based triggers.

### Q: Can I integrate with Slack or Jira?
**A:** Yes – use MCPs and tools to send findings to connected systems.

### Q: Does Security Review affect my personal usage/billing?
**A:** No – usage is charged to the team pool, not individual users.

### Q: How does it know if an issue was fixed?
**A:** Cursor uses LLMs to review diffs and assess whether the flagged issue was resolved.

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **What it does** | Scans code for security vulnerabilities |
| **Availability** | Teams and Enterprise only |
| **Agent types** | Security Review (PR-time) + Vulnerability Scanner (scheduled) |
| **Triggers** | Git events (PRs) or cron schedules |
| **Environment** | Cloud Agents (Cursor cloud or self-hosted) |
| **Billing** | Team usage pool (no individual impact) |
| **Analytics** | Vulnerabilities found, fixed, resolution rate |
| **Integrations** | MCPs, tools, Slack, issue trackers |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is Security Review?** | Automated security scanning for your code |
| **Who can use it?** | Teams and Enterprise plans only |
| **What are the two agent types?** | PR-time review + scheduled vulnerability scanner |
| **When does it scan?** | On PR events OR on cron schedule (e.g., nightly) |
| **Can I customize what it checks?** | Yes – enable/disable individual checks + custom instructions |
| **Can I integrate with Slack/Jira?** | Yes – via MCPs and tools |
| **How much does it cost?** | Billed to team usage pool |

---

## The Bottom Line

**Security Review is like having a dedicated security engineer continuously auditing your code.**

**Think of it as:**
- **Security Review (PR-time)** = Security review at every code change 🔍
- **Vulnerability Scanner (scheduled)** = Weekly security audit 📅

**For Teams/Enterprises:** This is a critical feature for maintaining security posture. It catches vulnerabilities before they reach production, tracks resolution rates, and integrates with your existing tools.

**The most powerful features:**
1. **Two scanning modes** – PR-time AND scheduled scans
2. **Resolution tracking** – Automatically knows if issues were fixed
3. **MCP integrations** – Send findings to Slack, Jira, etc.
4. **No individual impact** – Team-level billing

Would you like me to explain any specific part of Security Review in more detail?