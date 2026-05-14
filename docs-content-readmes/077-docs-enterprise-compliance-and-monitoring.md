This is the **Compliance and Monitoring** documentation – it covers audit logs, AI code tracking, certifications, and how to meet regulatory requirements.

Think of this as the **audit and compliance guide** for enterprise security teams – tracking who did what, when, and why.

Let me break this down.

---

## Overview

**Compliance requires visibility into who did what, when, and why.** This documentation covers audit logs, AI code tracking, certifications, and regulatory requirements.

---

## Audit Logs (Enterprise)

Audit logs provide a record of security events and administrative actions. Available on the **Enterprise plan**, audit logs help you meet compliance requirements and investigate security incidents.

### Events Logged

| Category | Events |
|----------|--------|
| **Authentication** | Logins and logouts |
| **User management** | User additions (via SSO, invite, signup, team creation, auto-enrollment), removals, role changes, individual spend limits |
| **API key management** | Team and user API key creation and revocation |
| **Team settings** | Team-wide and per-user spending limits, admin settings, team name changes, Slack integration settings, repository mappings |
| **Repository management** | Repository creation, deletion, settings updates |
| **Directory groups** | Group creation, updates, deletion, membership changes, permission modifications |
| **Privacy settings** | Privacy Mode changes at user or team level |
| **Team rules** | Team rule management (including Bugbot rules) |
| **Team commands** | Custom command creation, updates, deletion |

### What Is NOT Logged

> *"We do not log agent responses or generated code content."*

**Instead, we recommend using hooks to log prompts and code.**

---

## Accessing Audit Logs

| Feature | Details |
|---------|---------|
| **Location** | Team dashboard |
| **Availability** | Enterprise plans only |
| **Access** | Requires admin access |

---

## Streaming Audit Logs (Enterprise)

For compliance and security monitoring, stream audit logs to your existing systems:

| Destination |
|-------------|
| SIEM systems (Splunk, Sumo Logic, Datadog, etc.) |
| Webhook endpoints for custom processing |
| S3 buckets for long-term retention |
| Log aggregators (Elasticsearch, CloudWatch) |

> *"Please contact hi@cursor.com if you would like to receive streaming audit logs."*

---

## Log Format

Audit logs are delivered as JSON:

```json
{
  "metadata": {
    "timestamp": "2024-10-14T18:30:45Z",
    "event_id": "evt_abc123xyz789"
  },
  "team_id": "team_xyz789",
  "ip_address": "203.0.113.42",
  "user_email": "alice@company.com",
  "event": {
    /* event-specific fields */
  }
}
```

---

## Event Types (Complete List)

| Event Type | Description |
|------------|-------------|
| `login` | User login events (web or app) |
| `logout` | User logout events |
| `add_user` | User additions (source: sso, invite, signup, createTeam, autoEnroll) |
| `remove_user` | User removals from team |
| `update_user_role` | Role changes (OWNER, ADMIN, MEMBER) |
| `user_spend_limit` | Individual user spending limit changes |
| `team_api_key` | Team API key actions (create, revoke) |
| `user_api_key` | User API key actions (create, revoke) |
| `team_settings` | Team setting modifications (spending limits, admin settings, team name, Slack settings, etc.) |
| `team_repo` | Repository actions (create, delete, update_settings) |
| `create_directory_group` | Directory group creation |
| `update_directory_group` | Directory group updates |
| `delete_directory_group` | Directory group deletion |
| `add_user_to_directory_group` | Adding users to directory groups |
| `remove_user_from_directory_group` | Removing users from directory groups |
| `privacy_mode` | Privacy Mode changes (scope: "user" or "team") |
| `team_rule` | Team rule management (create, update, delete) |
| `bugbot_team_rule` | Bugbot-specific rule management (create, update, delete) |
| `team_command` | Custom team command management (create, update, delete) |

### Team Settings Sub-Events

| Sub-event | Description |
|-----------|-------------|
| `team_hard_limit_dollars` | Team-wide spending hard limit |
| `team_hard_limit_per_user_dollars` | Per-user hard limit |
| `per_user_monthly_limit_dollars` | Monthly spending limits per user |
| `admin_only_usage_pricing` | Admin-only usage pricing settings |
| `team_admin_settings` | General admin settings |
| `team_name` | Team name changes |
| `slack_default_repo` | Slack integration repository settings |
| `slack_default_branch` | Slack integration branch settings |
| `slack_default_model` | Slack integration model settings |
| `slack_share_summary` | Slack summary sharing settings |
| `slack_share_summary_in_external_channel` | External channel sharing |
| `slack_channel_repo_mappings` | Slack channel to repository mappings |

---

## Searching and Filtering

Filter audit logs in the dashboard by:

| Filter |
|--------|
| Date range |
| Event type (authentication, user management, settings) |
| Actor (specific user) |

> *"Export filtered results to CSV for analysis or compliance reports."*

---

## Using Hooks for Compliance Logging

Audit logs track administrative actions, but some compliance requirements need logging of **development activity**. Use hooks to log:

### Prompts Submitted Hook

```bash
#!/bin/bash
input=$(cat)
prompt=$(echo "$input" | jq -r '.prompt')
user_id=$(echo "$input" | jq -r '.user_id')

# Log to your compliance system
curl -X POST "https://compliance.company.com/log" \
  -H "Content-Type: application/json" \
  -d "{\"type\":\"prompt\",\"user\":\"$user_id\",\"timestamp\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}"

cat << EOF
{
  "continue": true
}
EOF
```

### Code Generated Hook

```bash
#!/bin/bash
input=$(cat)
file_path=$(echo "$input" | jq -r '.file_path')
edits=$(echo "$input" | jq -r '.edits')

# Log the code generation event (not the actual code)
curl -X POST "https://compliance.company.com/log" \
  -H "Content-Type: application/json" \
  -d "{\"type\":\"generation\",\"file\":\"$file_path\",\"timestamp\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}"

exit 0
```

### Important Security Note

> *"Important: Be careful logging actual code or prompts. They may contain sensitive information. Log metadata (who, when, what file) rather than content when possible."*

> *"See Hooks for hook implementation details."*

---

## Certifications and Compliance

Cursor maintains compliance with industry standards:

| Certification/Standard |
|------------------------|
| SOC 2 Type II |
| GDPR |
| And more... |

### Access Compliance Documentation

Through the **Trust Center**:

| Document |
|----------|
| SOC 2 reports |
| Penetration test summaries |
| Security architecture documentation |
| Data flow diagrams |

---

## Responsible Disclosure

If you discover a security vulnerability in Cursor, report it through our responsible disclosure program.

**Email:** `security-reports@cursor.com`

**Include:**
1. A detailed description of the vulnerability
2. Steps to reproduce the issue
3. Any relevant screenshots or proof of concept

---

## Quick Reference Card

| Feature | Availability | Details |
|---------|--------------|---------|
| **Audit logs** | Enterprise | Admin dashboard, JSON format |
| **Streaming audit logs** | Enterprise | SIEM, webhooks, S3, Elasticsearch |
| **Event types** | Enterprise | Authentication, user management, settings, repositories, groups, rules |
| **Hooks for compliance** | All plans | Log prompts and code generation |
| **Certifications** | All plans | SOC 2 Type II, GDPR |
| **Responsible disclosure** | All plans | security-reports@cursor.com |

---

## Common Beginner Questions

### Q: Are audit logs available on Teams plans?
**A:** No – audit logs are only available on Enterprise plans.

### Q: What events are logged?
**A:** Administrative events (authentication, user management, API keys, settings changes, repository management, directory groups, rules, commands). Agent responses and generated code are NOT logged.

### Q: How do I log development activity (prompts, code generation)?
**A:** Use hooks – audit logs don't capture these by default.

### Q: Can I stream audit logs to my SIEM?
**A:** Yes – contact hi@cursor.com to enable streaming.

### Q: Can I export audit logs?
**A:** Yes – filter and export to CSV from the dashboard.

### Q: What compliance certifications does Cursor have?
**A:** SOC 2 Type II, GDPR compliant. Access reports via Trust Center.

---

## The Bottom Line

**Compliance and Monitoring gives enterprise security teams visibility into who did what, when, and why.**

**Key features:**
1. **Audit logs** – Track authentication, user management, API keys, settings changes, repositories, groups, rules
2. **Streaming** – Send logs to SIEM, webhooks, S3, or Elasticsearch
3. **Hooks** – Log development activity (prompts, code generation) – audit logs don't capture this
4. **Certifications** – SOC 2 Type II, GDPR
5. **Responsible disclosure** – Security vulnerability reporting

**For security teams:**
- Audit logs = administrative actions 🔐
- Hooks = development activity logging 📝
- Streaming = integration with existing security tools 🔄

**Important:** Audit logs do NOT capture agent responses or generated code. Use hooks for that.

