This is the **Teams Dashboard** documentation – it explains the features and sections available in the Cursor team admin dashboard.

Think of this as the **control center** for managing your Cursor team – from billing and members to security settings and usage analytics.

Let me break this down.

---

## Dashboard Overview

**The dashboard lets you access billing, set up usage-based pricing, and manage your Team.**

The overview page provides a quick summary of your team's activity, usage statistics, and recent changes – at-a-glance insights into your workspace.

---

## Dashboard Sections

| Section | Description |
|---------|-------------|
| **Overview** | Team activity summary, usage statistics, recent changes |
| **Settings** | Team-wide preferences and security settings |
| **Members** | Manage team members, invite users, control permissions |
| **Audit Log** | Track security events and administrative actions (Enterprise only) |
| **Integrations** | Connect Cursor with GitHub, Slack, Linear, etc. |
| **Cloud Agents** | Monitor and manage cloud agents |
| **Bugbot** | Automated bug detection and fixing |
| **Usage** | Track detailed usage metrics across team members |
| **Billing & Invoices** | Manage subscription, view invoices, set spending limits |

---

## Settings (Team Configuration)

Available settings in the dashboard:

| Setting | Description |
|---------|-------------|
| **Privacy Settings** | Configure data sharing and privacy mode |
| **Usage-Based Pricing Settings** | Enable/configure usage-based pricing |
| **Team Marketplaces** | Manage private plugin marketplaces |
| **Bedrock IAM Role** | AWS IAM role configuration |
| **Single Sign-On (SSO)** | Configure SAML 2.0 SSO |
| **Cursor Admin API Keys** | Generate and manage API keys |
| **Active Sessions** | View active user sessions |
| **Invite Code Management** | Manage team invite codes |
| **API Endpoints** | Configure API endpoint settings |

---

## Enterprise-Only Settings

| Setting | Description |
|---------|-------------|
| **Model Access Control** | Control which models team members can use |
| **Enhanced Spend Limits** | More granular spending controls |
| **Auto Run Configuration** | Configure auto-run behavior |
| **Repository Blocklist** | Block access to specific repos |
| **MCP Configuration** | Manage MCP servers |
| **Cursor Ignore Configuration** | Configure ignore patterns |
| **.cursor Directory Protection** | Protect Cursor config directories |
| **AI Code Tracking API** | Track AI-generated code |
| **Audit Log** | Security event logging |
| **SCIM** | User provisioning (Enterprise) |

> *"Device-level enforcement: In addition to dashboard settings, enterprises can enforce policies like allowed team IDs and allowed extensions on user devices through MDM."*

---

## Members Section

Manage your team members, invite new users, and control access permissions.

| Feature | Description |
|---------|-------------|
| **Member list** | View all team members with names, emails, roles |
| **Usage tracking** | See each member's request count and spend |
| **Role management** | Assign Member, Admin, or Unpaid Admin roles |
| **Invite members** | Send email invites or generate invite links |

---

## Audit Log (Enterprise Only)

Track security events, administrative actions, and team changes.

**Audit log captures:**
- Authentication events (login, logout)
- Membership changes (add, remove, role updates)
- Permission updates
- API key actions
- Settings modifications

> *"Audit Log is available exclusively on Enterprise plans and can only be viewed by admins."*

Example entries:
- User Removed
- Team Settings Updated
- Team API Key actions
- User Role Updated
- Login/Logout events

---

## Integrations

Connect Cursor with your favorite tools and services:

| Integration | Purpose |
|-------------|---------|
| **GitHub** | Code repositories, PRs |
| **GitLab** | Code repositories, MRs |
| **Slack** | Agent commands and notifications |
| **Linear** | Issue tracking |

---

## Cloud Agents

Monitor and manage cloud agents running in your workspace:
- View agent status
- View logs
- Track resource usage

---

## Bugbot

Access automated bug detection and fixing capabilities:
- Automated PR reviews
- Security issue detection
- Code quality problems

---

## Usage Tracking

Track detailed usage metrics:

| Metric | Description |
|--------|-------------|
| **AI requests** | Number of agent requests |
| **Model usage** | Which models are being used |
| **Resource consumption** | Token usage per user |
| **Filtering** | Search by email/name, date ranges |

Columns include:
- Date/time
- User email
- Request type (Usage-based, Errored, Not Charged)
- Max Mode status
- Model used
- Count

---

## Billing & Invoices

Manage your team's subscription and billing:

| Feature | Description |
|---------|-------------|
| **Spending limit** | Set monthly team spending limit |
| **Usage breakdown** | View token-based usage costs by model |
| **Invoice history** | View past invoices |
| **Subscription management** | Change plan, update billing |
| **Upgrade** | Switch from monthly to yearly (save 20%) |

Example billing items:
- token-based usage calls to models
- extra fast premium requests beyond included limit
- per-request charges

---

## Dashboard Sections Summary

| Section | Available on | Key features |
|---------|--------------|--------------|
| **Overview** | All plans | Team activity summary |
| **Settings** | All plans | Team configuration |
| **Members** | All plans | User management |
| **Audit Log** | Enterprise only | Security event tracking |
| **Integrations** | All plans | GitHub, Slack, Linear |
| **Cloud Agents** | All plans | Agent monitoring |
| **Bugbot** | All plans | Automated reviews |
| **Usage** | All plans | Usage analytics |
| **Billing** | All plans | Invoices, spending limits |

---

## Common Beginner Questions

### Q: How do I access the dashboard?
**A:** Go to `cursor.com/dashboard` and sign in with admin credentials.

### Q: Can regular members see the dashboard?
**A:** Members can see their own usage but not admin sections (settings, billing, members management).

### Q: What's the difference between Teams and Enterprise dashboard?
**A:** Enterprise has additional settings like Audit Log, SCIM, Model Access Control, and Enhanced Spend Limits.

### Q: How do I set a team spending limit?
**A:** Navigate to Billing & Invoices → Set Spending Limit.

### Q: Can I see which team member used which model?
**A:** Yes – in the Usage section, you can filter by user and see model usage.

### Q: How do I invite new team members?
**A:** Go to Members section → Invite Team → Enter email addresses or copy invite link.

---

## The Bottom Line

**The Cursor Teams Dashboard is the central management hub for your organization – from member management to billing to security settings.**

**Key sections to know:**
- **Members** – Add/remove users, change roles
- **Settings** – Configure SSO, API keys, privacy
- **Usage** – Track who's using what
- **Billing** – Set spending limits, view invoices
- **Audit Log** (Enterprise) – Security compliance

**For team admins:** The dashboard gives you full control over your team's Cursor experience – manage access, control costs, and ensure security compliance.

