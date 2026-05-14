This is the **Members & Roles** documentation – it explains the different user roles in a Cursor team and how to manage team members.

Think of this as the **team administration guide** – who can do what, how to add/remove members, and how roles affect billing.

Let me break this down.

---

## Three Roles

| Role | Description | Paid? |
|------|-------------|-------|
| **Member** | Default role with access to Pro features | ✅ Paid seat |
| **Admin** | Full team management and security controls | ✅ Paid seat |
| **Unpaid Admin** | Manage teams without using a paid seat (IT/finance staff who don't need Cursor access) | ❌ Free |

> *"Unpaid Admins require at least one paid user on the team."*

---

## Role Comparison

| Capability | Member | Admin | Unpaid Admin |
|------------|--------|-------|--------------|
| Use Cursor features | ✅ | ✅ | ❌ (no Pro features) |
| Invite members | ❌ | ✅ | ✅ |
| Remove members | ❌ | ✅ | ✅ |
| Change user role | ❌ | ✅ | ✅ |
| Admin dashboard | ❌ | ✅ | ✅ |
| Configure SSO/Security | ❌ | ✅ | ✅ |
| Manage billing | ❌ | ✅ | ✅ |
| View analytics | ❌ | ✅ | ✅ |
| Set usage controls | ❌ | ✅ | ✅ |
| **Requires paid seat** | ✅ | ✅ | ❌ |

---

## Member Role

Members are the default role with access to Cursor's Pro features.

| Access | Description |
|--------|-------------|
| **Pro features** | Full access |
| **Billing settings** | ❌ No access |
| **Admin dashboard** | ❌ No access |
| **Usage visibility** | Can see their own usage and remaining usage-based budget |

---

## Admin Role

Admins control team management and security settings.

| Access | Description |
|--------|-------------|
| **Pro features** | Full access |
| **Member management** | Add/remove members, modify roles |
| **Security** | Setup SSO |
| **Usage controls** | Configure usage-based pricing and spending limits |
| **Analytics** | Access to team analytics |

---

## Unpaid Admin Role

Unpaid Admins manage teams without using a paid seat – ideal for IT or finance staff who don't need Cursor access.

| Feature | Description |
|---------|-------------|
| **Billable** | ❌ Not billable |
| **Pro features** | ❌ No |
| **Admin capabilities** | ✅ Same as Admins |

> *"Unpaid Admins require at least one paid user on the team."*

---

## Adding Members (4 Ways)

| Method | How it works |
|--------|--------------|
| **Email invitation** | Click "Invite Members" → Enter email addresses → Users receive email invites |
| **Invite link** | Click "Invite Members" → Copy Invite Link → Share with team members |
| **SSO** | Configure SSO in admin dashboard → Users auto-join when logging in via SSO email |
| **Domain matching** | Teammates with verified, matching email domain can join without invite (enable in team settings) |

> *"Invite links have a long expiration date. Anyone with the link can join. Revoke them regularly, or use SSO or domain restrictions to control access."*

---

## Removing Members

| Action | Details |
|--------|---------|
| **Who can remove** | Admins can remove members anytime via context menu → "Remove" |
| **Billing** | If a member has used any credits, their seat remains occupied until the end of the billing cycle |
| **Credit adjustment** | Billing is automatically adjusted with pro-rated credit for removed members applied to the next invoice |
| **Data deletion** | When a user is removed, their data (including Memories and Cloud Agent data) is permanently deleted |

> *"There must be at least one Admin and one paid member on the team at all times."*

---

## Changing Roles

Admins can change roles for other members by clicking the context menu and then using the "Change role" option.

> *"There must be at least one Admin, and one paid member on the team at all times."*

---

## Domain Settings

Admins can configure two domain-based controls in team settings. Both require at least one verified domain and are available on Team and Enterprise plans for teams **not using SCIM provisioning**.

### Domain Matching

When enabled, anyone with a verified, matching email domain can join your team directly from the dashboard – no invite needed.

> *"This is useful for letting teammates self-serve without admins manually sending invitations."*

### Restrict Invites to Verified Domains

When enabled, team members can only invite users whose email addresses match a verified domain. Invitations to email addresses outside your verified domains are blocked.

> *"This prevents accidental or unauthorized additions and gives admins tighter control over who joins the team."*

---

## Security & SSO

SAML 2.0 Single Sign-On (SSO) is available on Team plans.

| Feature | Description |
|---------|-------------|
| Configure SSO connections | Set up identity provider (Okta, etc.) |
| Set up domain verification | Required for SSO |
| Automatic user enrollment | Users auto-join via SSO |
| SSO enforcement options | Require SSO for all team members |

---

## Billing Rules

| Scenario | Billing treatment |
|----------|-------------------|
| **Adding members** | Each member or admin adds a billable seat. New members charged pro-rata for remaining time in billing period. Unpaid admin seats not counted. |
| **Mid-month additions** | Charged only for days used |
| **Removing members with credits used** | Seat remains occupied until end of billing cycle – no pro-rated refunds |
| **Role changes** | (e.g., Admin to Unpaid Admin) adjust billing from change date |

> *"Monthly/yearly renewal occurs on your original signup date, regardless of member changes."*

---

## Switching to Yearly Billing

Save **20%** by switching from monthly to yearly:

1. Go to `cursor.com/dashboard/billing`
2. Click **"Upgrade Now"** on the green banner at the top

> *"There is no way to switch from yearly to monthly mid-plan. You'll need to cancel, wait for the year to end, then re-subscribe on a monthly plan."*

---

## Role Summary Table

| Role | Paid Seat | Pro Features | Admin Features | Best for |
|------|-----------|--------------|----------------|----------|
| **Member** | ✅ | ✅ | ❌ | Regular developers |
| **Admin** | ✅ | ✅ | ✅ | Team managers |
| **Unpaid Admin** | ❌ | ❌ | ✅ | IT/finance staff |

---

## Team Data Deletion

| Event | Data deletion |
|-------|---------------|
| **User removed from team** | Their data (Memories, Cloud Agent data) permanently deleted |
| **Entire team deleted** | All associated data permanently deleted |

> *"There must be at least one Admin and one paid member on the team at all times."*

---

## Common Beginner Questions

### Q: Can I be both an Admin and a Member?
**A:** Admin role already includes all Member capabilities. You don't need both.

### Q: What is an Unpaid Admin used for?
**A:** IT or finance staff who need to manage team settings (billing, members) but don't need to use Cursor themselves.

### Q: Can a team have only Unpaid Admins?
**A:** No – Unpaid Admins require at least one paid user (Member or Admin) on the team.

### Q: How do I invite members without email invites?
**A:** Use invite link, SSO, or domain matching.

### Q: What happens to a removed member's data?
**A:** Permanently deleted – including Memories and Cloud Agent data.

### Q: Can I switch from monthly to yearly billing?
**A:** Yes – save 20%. But you cannot switch back mid-year.

---

## The Bottom Line

**Cursor teams have three roles: Members (regular users), Admins (full control), and Unpaid Admins (admin access without a paid seat).**

**Key takeaways:**
- **Members** – Use Cursor Pro features, no admin access
- **Admins** – Full control over team, security, billing, members
- **Unpaid Admins** – Admin without paid seat (IT/finance staff)
- Add members via email, invite link, SSO, or domain matching
- Billing is pro-rated for mid-month additions
- Removed members' data is permanently deleted

**For team admins:** Understand the role differences to assign the right access levels. Use domain matching and SSO for easier onboarding.

