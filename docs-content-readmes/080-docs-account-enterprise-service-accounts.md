This is the **Service Accounts** documentation – it explains how to use non-human accounts to securely automate Cursor-powered workflows at scale.

Think of this as the **automation identity** for enterprises – APIs, CI/CD pipelines, and integrations can run without tying to individual developers' personal accounts.

Let me break this down.

---

## What Are Service Accounts?

**Service accounts are non-human accounts that enable teams to securely automate Cursor-powered workflows at scale.** With service accounts, you can consume APIs, authenticate the CLI, and invoke cloud agents without tying integrations to individual developers' personal accounts.

> *"Service accounts are available on the Enterprise plan."*

---

## Why Use Service Accounts

| Benefit | Description |
|---------|-------------|
| **Decoupling from individuals** | Automations continue running even as people and roles change |
| **Secure credential management** | Easily rotate API keys without disrupting workflows |
| **Centralized access control** | Admins manage all service account permissions in one place |
| **Attribution and auditability** | Tie cloud agent runs to the initiating service or system |

---

## Key Features

### No Additional Seat Required

> *"Service accounts are included with your Enterprise plan at no extra cost. They do not consume a seat license."*

### Usage Consumption

Service accounts consume usage from your **team's usage pool**, just like human users. All usage is tracked and visible in your team's analytics and billing.

### Cloud Agent Integration

Service accounts can initiate cloud agent runs programmatically. Automation scenarios include:

| Scenario | Example |
|----------|---------|
| **Linear** | Ticket created triggers cloud agent to implement feature |
| **Sentry** | Error initiates cloud agent to investigate and fix |
| **Internal services** | Kicking off migrations or refactoring tasks |

### Admin Visibility

> *"Cloud agent runs initiated by service accounts are accessible to all team admins. This ensures visibility and oversight of automated workflows across your organization."*

### Repository Access

Service accounts can initiate cloud agent runs on any repository authorized via the Cursor GitHub app.

> *"The GitHub integration must be connected at the team level for service accounts to access repositories. If you have a personal GitHub integration but no team-level integration, service accounts will not be able to initiate cloud agent runs."*

**To connect GitHub at team level:**
1. Navigate to Dashboard → Settings → Integrations
2. Connect the Cursor GitHub app to your organization
3. Authorize the repositories you want service accounts to access

---

## Creating a Service Account

Admins can create and manage service accounts from the Cursor Dashboard.

| Step | Action |
|------|--------|
| 1 | Navigate to **Dashboard → Settings → Service Accounts** |
| 2 | Click **New Service Account** |
| 3 | Enter a name and optional description |
| 4 | Click **Create** |

> *"When you create a service account, an API key is generated. Copy this key immediately – it will only be shown once and cannot be retrieved later."*

> *"Store your API key securely. If you lose it, you'll need to rotate it to generate a new one."*

---

## Managing API Keys

Each service account can have API keys associated with it. You can:

| Action | Description |
|--------|-------------|
| **View masked keys** | See the last few characters of each key for identification |
| **Rotate keys** | Generate a new key and invalidate the old one |
| **Archive service accounts** | Archive an account and revoke all its API keys |

---

## Rotating an API Key

| Step | Action |
|------|--------|
| 1 | Navigate to **Dashboard → Settings → Service Accounts** |
| 2 | Find the service account and click the rotate icon next to its API key |
| 3 | Copy the new key immediately |

> *"The old key is immediately invalidated. Update any integrations using the old key."*

---

## Using Service Accounts with the API

Service accounts authenticate using their API key. Use the key in the **Authorization** header:

```bash
curl -X POST https://api.cursor.com/agents \
  -H "Authorization: Bearer YOUR_SERVICE_ACCOUNT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "repo": "owner/repo",
    "prompt": "Implement the feature described in issue #123"
  }'
```

> *"See the Cloud Agents API documentation for the full API reference."*

---

## Using Service Accounts with the CLI

Service accounts can authenticate the Cursor CLI by setting the API key as `CURSOR_API_KEY`. This is the recommended way to run the CLI in CI/CD pipelines, cron jobs, and other non-interactive environments where browser login isn't possible.

```bash
export CURSOR_API_KEY=your_service_account_api_key

# Run a task in a CI pipeline
agent -p --force "Refactor the authentication module to use OAuth 2.0"
```

> *"The same environment variable works in any context, including local development."*

---

## Best Practices

| Practice | Description |
|----------|-------------|
| **Rotate keys regularly** | Establish a key rotation schedule for your service accounts |
| **Use descriptive names** | Name service accounts after their purpose (e.g., "Linear Integration", "Sentry Auto-Fix") |
| **Limit scope** | Create separate service accounts for different automation workflows |
| **Monitor usage** | Review service account activity in your team's analytics dashboard |
| **Revoke unused accounts** | Archive service accounts that are no longer in use |

---

## Archiving a Service Account

Archiving a service account:
- Revokes all API keys associated with the account
- Breaks any integrations using those keys
- Preserves the account record for auditability

**To archive:**
1. Navigate to Dashboard → Settings → Service Accounts
2. Click the archive icon next to the service account
3. Confirm the archive action

> *"Archived accounts can be viewed by clicking 'Show Archived' on the Service Accounts page. This helps maintain a complete audit trail of service accounts used by your team."*

---

## Quick Reference Card

| Feature | Details |
|---------|---------|
| **Availability** | Enterprise plan only |
| **Seat cost** | No additional seat required |
| **Usage billing** | Consumes from team's usage pool |
| **Authentication** | API key (Bearer token) |
| **API integration** | Cloud Agents API |
| **CLI integration** | `CURSOR_API_KEY` environment variable |
| **Repository access** | Requires team-level GitHub integration |

---

## Use Cases Summary

| Integration | Automation |
|-------------|------------|
| **Linear** | Ticket → cloud agent implements feature |
| **Sentry** | Error → cloud agent investigates and fixes |
| **CI/CD pipelines** | Automated refactoring, testing |
| **Cron jobs** | Scheduled maintenance tasks |
| **Internal services** | Migrations, bulk operations |

---

## Common Beginner Questions

### Q: Are service accounts available on Teams plans?
**A:** No – service accounts are only available on Enterprise plans.

### Q: Do service accounts cost extra?
**A:** No – they are included with your Enterprise plan at no extra cost and do not consume seat licenses.

### Q: How is usage billed?
**A:** Service accounts consume usage from your team's usage pool, just like human users.

### Q: What happens if I lose the API key?
**A:** You cannot retrieve it. You'll need to rotate the key to generate a new one.

### Q: Can service accounts access repositories?
**A:** Yes – but the GitHub integration must be connected at the team level.

### Q: Who can see service account activity?
**A:** All team admins can see cloud agent runs initiated by service accounts.

---

## The Bottom Line

**Service accounts are non-human identities for automating Cursor-powered workflows at scale – with no additional seat cost.**

**Key benefits:**
- **Decoupled from individuals** – automations survive personnel changes
- **Secure credential management** – rotate keys without workflow disruption
- **Centralized control** – admins manage all permissions in one place
- **Attribution & auditability** – trace runs to the service or system

**Common automation scenarios:**
- Linear ticket → cloud agent implements feature
- Sentry error → cloud agent investigates and fixes
- CI/CD pipelines → automated refactoring
- Cron jobs → scheduled maintenance

**For enterprise teams:** Service accounts are essential for building reliable, secure automations that don't depend on individual developers' accounts.

Would you like me to explain any specific service account feature in more detail?