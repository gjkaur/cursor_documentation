This is the **SSO (Single Sign-On)** documentation – it explains how to set up SAML 2.0 SSO for Cursor Teams and Enterprise plans.

Think of this as the **login integration guide** – allowing your team members to use their existing corporate credentials (via Okta, Azure AD, Google Workspace, etc.) to access Cursor.

Let me break this down.

---

## Overview

**SAML 2.0 SSO is available at no additional cost on Teams and Enterprise plans.** Use your existing identity provider (IdP) to authenticate team members without separate Cursor accounts.

| Without SSO | With SSO |
|-------------|----------|
| Separate Cursor accounts | Use existing corporate credentials |
| Manual invite process | Auto-enrollment via IdP |
| Password management per user | Centralized identity management |

---

## Prerequisites

| Requirement | Description |
|-------------|-------------|
| **Cursor Team or Enterprise plan** | SSO is included at no extra cost |
| **Admin access to your identity provider** | e.g., Okta, Azure AD, Google Workspace |
| **Admin access to your Cursor organization** | To configure SSO settings |

---

## Configuration Steps

| Step | Action |
|------|--------|
| **1** | Sign in to your Cursor account – Navigate to `cursor.com/dashboard/settings` with an admin account |
| **2** | Locate the SSO configuration – Find the "Single Sign-On (SSO)" section and expand it |
| **3** | Begin the setup process – Click the "SSO Provider Connection settings" button and follow the wizard |
| **4** | Configure your identity provider (Okta, Azure AD, etc.): |
| | - Create new SAML application |
| | - Configure SAML settings using Cursor's information |
| | - Set up Just-in-Time (JIT) provisioning |
| **5** | Verify domain – Verify the domain of your users in Cursor by clicking the "Domain verification settings" button |

---

## Identity Provider Setup Guides

Cursor provides setup instructions for:

| Identity Provider |
|-------------------|
| Okta |
| Azure AD |
| Google Workspace |
| And more... |

> *"For provider-specific setup instructions, see the Identity Provider Guides."*

---

## Multiple Domains

If your organization uses multiple email domains:

| Step | Action |
|------|--------|
| 1 | Verify each domain separately in Cursor through the domain verification settings |
| 2 | Configure each domain in your identity provider |
| 3 | Each domain needs to go through the verification process independently |

---

## Additional Settings

| Feature | Description |
|---------|-------------|
| **SSO enforcement** | Manage through admin dashboard |
| **Auto-enrollment** | New users auto-enroll when signing in through SSO |
| **User management** | Handle through your identity provider |

---

## Troubleshooting

If issues occur:

| Check | Description |
|-------|-------------|
| **Domain verification** | Verify domain is verified in Cursor |
| **SAML attribute mapping** | Ensure SAML attributes are properly mapped |
| **SSO enabled** | Check SSO is enabled in admin dashboard |
| **Name matching** | Match first and last names between identity provider and Cursor |
| **Provider guides** | Check provider-specific guides |
| **Help center** | Visit the SSO help center if issues persist |

---

## Flow Summary

```
User clicks "Sign in with SSO"
        ↓
Redirected to Identity Provider (Okta, Azure AD, etc.)
        ↓
User authenticates with corporate credentials
        ↓
IdP sends SAML assertion to Cursor
        ↓
Cursor verifies domain and creates/updates user
        ↓
User logged in to Cursor (auto-created if new)
```

---

## Quick Reference Card

| Feature | Details |
|---------|---------|
| **Protocol** | SAML 2.0 |
| **Cost** | Included (Teams/Enterprise) |
| **Auto-enrollment** | Yes (Just-in-Time provisioning) |
| **Domain verification** | Required |
| **Multiple domains** | Supported (verify each separately) |
| **SSO enforcement** | Configurable |

---

## Common Beginner Questions

### Q: Is SSO available on Individual plans?
**A:** No – SSO is only available on Teams and Enterprise plans.

### Q: Does SSO cost extra?
**A:** No – it's included at no additional cost on Teams and Enterprise plans.

### Q: What is Just-in-Time (JIT) provisioning?
**A:** When a user signs in via SSO for the first time, Cursor automatically creates their account. No manual invite needed.

### Q: Can I enforce SSO only?
**A:** Yes – you can configure SSO enforcement in the admin dashboard.

### Q: Can I use multiple identity providers?
**A:** You can configure multiple domains, each with its own IdP configuration.

### Q: What if a user's email domain isn't verified?
**A:** They cannot use SSO. Domain verification is required.

---

## The Bottom Line

**SSO allows your team to use existing corporate credentials to log into Cursor – no separate accounts or passwords needed.**

**Key benefits:**
- Centralized identity management
- Auto-enrollment (JIT provisioning)
- No extra cost on Teams/Enterprise
- Support for Okta, Azure AD, Google Workspace, and more

**Setup steps:**
1. Navigate to dashboard settings (admin required)
2. Configure SSO provider connection
3. Set up SAML app in your identity provider
4. Verify your domain in Cursor
5. Enable SSO

**For team admins:** This is the recommended way to manage team access, especially for larger organizations. Users auto-join when they first sign in via SSO.

