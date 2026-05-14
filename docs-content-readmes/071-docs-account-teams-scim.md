This is the **SCIM** documentation – it explains how to automatically manage team members and directory groups through your identity provider using SCIM 2.0.

Think of SCIM as **automatic user lifecycle management** – when you add or remove someone from your identity provider (Okta, Azure AD, etc.), Cursor automatically updates.

Let me break this down.

---

## Overview

**SCIM 2.0 provisioning automatically manages your team members and directory groups through your identity provider.**

| Without SCIM | With SCIM |
|--------------|-----------|
| Manually add users to Cursor | Auto-provision from IDP |
| Manually remove users | Auto-deprovision from IDP |
| Manual group management | Groups sync automatically |

> *"Available on Enterprise plans with SSO enabled. Contact sales to get access."*

---

## Prerequisites

| Requirement | Description |
|-------------|-------------|
| **Cursor Enterprise plan** | Required |
| **SSO must be configured first** | SCIM requires an active SSO connection |
| **Admin access to identity provider** | Okta, Azure AD, etc. |
| **Admin access to Cursor organization** | To configure SCIM |

> *"SCIM requires SSO to be set up first. If you haven't configured SSO yet, follow the SSO setup guide before proceeding."*

---

## How It Works

### User Provisioning

| Action | Result |
|--------|--------|
| Assign user to SCIM application in IDP | User automatically added to Cursor |
| Unassign user from SCIM application | User automatically removed from Cursor |
| Profile changes (name, email) | Sync automatically |

> *"Changes sync in real-time."*

### Directory Groups

| Feature | Description |
|---------|-------------|
| **Group sync** | Directory groups and membership sync from your identity provider |
| **Management** | Group and user management must be done through your identity provider |
| **Visibility** | Cursor displays this information as read-only |

### Spend Management

| Rule | Description |
|------|-------------|
| **Group limits** | Set different per-user spend limits for each directory group |
| **Precedence** | Directory group limits take precedence over team-level limits |
| **Multiple groups** | Users in multiple groups receive the highest applicable spend limit |

---

## Setup Steps

| Step | Action |
|------|--------|
| **1** | Ensure SSO is configured. If not, follow SSO setup guide first |
| **2** | Access Active Directory Management: `cursor.com/dashboard/members/public/active-directory` (or Dashboard → Members & Groups → Directory Groups) |
| **3** | Start SCIM setup – Once SSO is verified, click the link for step-by-step SCIM setup wizard |
| **4** | Configure SCIM in your identity provider: |
| | - Create or configure your SCIM application |
| | - Use the SCIM endpoint and token provided by Cursor |
| | - Enable user and push group provisioning |
| | - Test the connection |
| **5** | Configure spend limits (optional) – View synchronized directory groups, set per-user spend limits, review limits for users in multiple groups |

---

## Identity Provider Setup Guides

Cursor provides provider-specific setup instructions for:

| Identity Provider |
|-------------------|
| Okta |
| Azure AD |
| Google Workspace |
| And more... |

---

## Managing Users and Groups

> *"All user and group management must be done through your identity provider. Changes made in your identity provider will automatically sync to Cursor, but you cannot modify users or groups directly in Cursor."*

### User Management

| Action | How to do it |
|--------|--------------|
| **Add users** | Assign them to SCIM application in your identity provider |
| **Remove users** | Unassign them from SCIM application |
| **Update profiles** | Changes (name, email) sync automatically |

### Group Management

| Feature | Description |
|---------|-------------|
| **Sync** | Directory groups automatically synced from identity provider |
| **Real-time** | Group membership changes reflected in real-time |
| **Use case** | Organize users and set different spend limits |

---

## Spend Limits via Groups

| Feature | Description |
|---------|-------------|
| **Per-group limits** | Set different per-user limits for each directory group |
| **Precedence** | Group limits override the default team-wide per-user limit |
| **Multiple groups** | Users inherit the highest spend limit from their groups |

---

## FAQ

| Question | Answer |
|----------|--------|
| **Why isn't SCIM management showing up in my dashboard?** | Ensure SSO is properly configured and working before setting up SCIM. SCIM requires an active SSO connection. |
| **Why aren't users syncing?** | Verify users are assigned to the SCIM application in your identity provider. Users must be explicitly assigned. |
| **Why aren't groups appearing?** | Check that push group provisioning is enabled in your identity provider's SCIM settings. Group sync must be configured separately from user sync. |
| **Why aren't spend limits applying?** | Confirm users are properly assigned to expected groups in your identity provider. Group membership determines which spend limits apply. |
| **Can I manage SCIM users and groups directly in Cursor?** | No – all management must be done through your identity provider. Cursor displays as read-only. |

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **Protocol** | SCIM 2.0 |
| **Availability** | Enterprise plans only |
| **Requirement** | SSO must be configured first |
| **User provisioning** | Automatic on assign/unassign in IDP |
| **Group sync** | Automatic from IDP |
| **Spend limits** | Per-group limits override team defaults |
| **Management** | Through identity provider only (Cursor read-only) |

---

## Common Beginner Questions

### Q: Is SCIM available on Teams plans?
**A:** No – SCIM is only available on Enterprise plans.

### Q: Does SCIM work without SSO?
**A:** No – SCIM requires SSO to be configured first.

### Q: Can I manually add users if I have SCIM enabled?
**A:** All user management must be done through your identity provider. Manual changes in Cursor will be overwritten.

### Q: How quickly do changes sync?
**A:** Changes sync in real-time from your identity provider to Cursor.

### Q: Can I have different spend limits for different teams?
**A:** Yes – set per-user spend limits per directory group. Groups override team-level defaults.

### Q: What happens if a user is in multiple groups with different spend limits?
**A:** They receive the highest spend limit from all their groups.

---

## The Bottom Line

**SCIM automates user lifecycle management by syncing your identity provider with Cursor.**

**Key benefits:**
- **Auto-provisioning** – New employees get access automatically
- **Auto-deprovisioning** – Departing employees lose access automatically
- **Group sync** – Directory groups and membership sync in real-time
- **Spend limits per group** – Different budgets for different teams
- **Read-only in Cursor** – All management stays in your identity provider

**Requirements:**
- Enterprise plan
- SSO configured first
- Admin access to IDP and Cursor

**For enterprise IT teams:** SCIM eliminates manual user management and ensures access is always up to date with your HR/IDP system.

