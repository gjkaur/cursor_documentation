This is the **Identity and Access Management** documentation – it explains how to control who can use Cursor in your organization and what they can do.

Think of this as the **security setup guide** for Enterprise IT teams – covering SSO, SCIM, MDM policies, allowed team IDs, and extension controls.

Let me break this down.

---

## Recommended Implementation Order

| Step | Action |
|------|--------|
| **1** | Set up SSO – Get centralized authentication working first |
| **2** | Enable SCIM – Automate user lifecycle management |
| **3** | Deploy MDM policies – Enforce allowed team IDs and extensions |
| **4** | Assign roles – Grant admin access to the right people |

---

## 1. Single Sign-On (SSO) and SAML

**SSO lets your users authenticate to Cursor using your existing identity provider.** Instead of creating separate Cursor passwords, users log in with their corporate credentials.

| Feature | Details |
|---------|---------|
| **Protocol** | SAML 2.0 |
| **Supported providers** | Okta, Azure AD, Google Workspace, OneLogin |
| **Enforcement** | Can require SSO for all team members, preventing password-based authentication entirely |

> *"See SSO and SAML setup for detailed configuration instructions."*

---

## 2. SCIM Provisioning

**SCIM 2.0 provisioning automatically manages your team members and directory groups through your identity provider.**

| Without SCIM | With SCIM |
|--------------|-----------|
| Manually add users | New employees get access automatically when added to right group |
| Manually remove users | Departing employees lose access when removed from IDP |
| Manual group changes | Group membership changes propagate automatically |

> *"Available on Enterprise plans with SSO enabled."*
> *"See SCIM provisioning for setup instructions."*

---

## 3. Role-Based Access Control (RBAC)

Cursor teams have three roles:

| Role | Description |
|------|-------------|
| **Members** | Regular users with Pro features |
| **Admins** | Full team management and security controls |
| **Unpaid Admins** | Admin access without a paid seat (IT/finance staff) |

> *"See Members & Roles for more information."*

---

## 4. MDM Policies

Mobile Device Management (MDM) systems let you enforce policies on user devices.

| Platform | Supported MDM |
|----------|---------------|
| **macOS** | MDM-based policies |
| **Windows** | Intune / Group Policy |

> *"See Deployment Patterns for platform-specific MDM configuration instructions."*

---

## Allowed Team IDs (Critical MDM Policy)

**The most important MDM policy prevents users from logging into personal Cursor accounts on corporate devices.**

When you set an allowed team ID policy, Cursor only permits authentication to those specific team IDs. If a user tries to log in with a different team ID (like a personal account), Cursor logs them out immediately.

### Example:

If your employees have corporate laptops, you can set the allowed team ID to your enterprise team ID. This prevents them from accidentally using personal accounts that might not have Privacy Mode enabled.

### Configuration:

The `cursorAuth.allowedTeamId` setting controls which team IDs are permitted. Accepts a comma-separated list.

**Example:** `cursorAuth.allowedTeamId = "1,3,7"` allows users from team IDs 1, 3, and 7.

### When a user attempts to log in with a disallowed team ID:

| Action | Description |
|--------|-------------|
| Force logout | Immediately logged out |
| Error message | Displayed to user |
| Prevention | Further authentication attempts blocked until valid team ID is used |

### MDM Configuration:

To centrally manage allowed team IDs, configure the `AllowedTeamId` policy using your device management solution. This policy overrides the `cursorAuth.allowedTeamId` setting on users' devices.

> *"See Deployment Patterns for platform-specific MDM configuration instructions."*

---

## Allowed Extensions

Control which extensions users can install in Cursor. Extensions can access your workspace, so you want to ensure only trusted extensions run.

### How It Works:

The `extensions.allowed` setting controls which extensions can be installed. Accepts a JSON object where keys are publisher names and values are booleans.

**Examples:**

| Setting | Effect |
|---------|--------|
| `{"anysphere": true, "github": true}` | Allows extensions from Anysphere and GitHub |
| `{"anysphere": false}` | Blocks Anysphere extensions |

### More specific (full extension ID):

```json
{
  "anysphere": true,
  "github": true,
  "esbenp.prettier-vscode": true,
  "ms-azuretools.vscode-containers": false,
  "dbaeumer.vscode-eslint": "3.0.0",
  "github.vscode-pull-request-github": "stable"
}
```

### Admin Portal Configuration:

Team admins can configure allowed extensions through the **team dashboard** in the Security & Identity section.

- Configuration applied automatically to all team members
- Leave empty to allow all extensions
- **Requires Cursor client version 21 or later** – older versions don't have restrictions applied

### MDM Configuration:

To centrally manage allowed extensions, configure the `AllowedExtensions` policy using your device management solution. This policy overrides both the admin portal setting and user-configured settings.

> *"See Deployment Patterns for platform-specific MDM configuration instructions."*

---

## The `.cursor` Folder

When you open a project in Cursor, the editor creates a `.cursor` folder at the root of your repository.

| Contains | Description |
|----------|-------------|
| Project-specific settings | Configuration for the project |
| Indexing cache | For faster search |
| Project rules and context | Rules files |

> *"These configurations are visible to anyone with repository access."*

### Security Note:

For repositories you don't control access to, review the `.cursor` folder contents before committing. **Don't put sensitive information in rules files.**

You can also manage rules and commands through the server on the team dashboard.

---

## Workspace Trust

The `security.workspace.trust.enabled` setting controls whether the Workspace Trust feature is enabled.

| Setting | Effect |
|---------|--------|
| `true` | Users prompted to trust each new workspace; untrusted workspaces run in restricted mode |
| `false` | Feature disabled – all workspaces automatically trusted |

### When Workspace Trust is Enabled:

- Users prompted to trust each new workspace when opening for the first time
- Untrusted workspaces run in restricted mode with limited functionality
- Trust decisions saved and remembered per workspace

### MDM Configuration:

To centrally manage workspace trust, configure the `WorkspaceTrustEnabled` policy using your device management solution. Overrides the `security.workspace.trust.enabled` setting on users' devices.

> *"See Deployment Patterns for platform-specific MDM configuration instructions."*

---

## Quick Reference Card

| Feature | Availability | Purpose |
|---------|--------------|---------|
| **SSO (SAML 2.0)** | Teams/Enterprise | Centralized authentication |
| **SCIM 2.0** | Enterprise | Automated user provisioning |
| **RBAC** | All team plans | Members, Admins, Unpaid Admins |
| **MDM policies** | Enterprise | Enforce security policies |
| **Allowed Team IDs** | Enterprise | Prevent personal account usage |
| **Allowed Extensions** | Enterprise | Control which extensions can be installed |
| **Workspace Trust** | All plans | Restrict untrusted workspaces |

---

## Common Beginner Questions

### Q: What's the most important MDM policy?
**A:** Allowed Team IDs – prevents users from logging into personal Cursor accounts on corporate devices.

### Q: What happens if a user has an older Cursor version?
**A:** Extension restrictions are not applied. Admin portal configuration requires client version 21 or later.

### Q: Can I combine multiple identity controls?
**A:** Yes – recommended order: SSO → SCIM → MDM policies → assign roles.

### Q: Does SCIM work without SSO?
**A:** No – SCIM is available on Enterprise plans **with SSO enabled**.

### Q: Can I see which extensions are allowed?
**A:** Admin portal shows the configuration; users on version 21+ have restrictions applied.

### Q: What's in the `.cursor` folder?
**A:** Project settings, indexing cache, and rules. Don't commit sensitive information.

---

## The Bottom Line

**Identity and Access Management gives enterprises control over authentication, user provisioning, device policies, and extension security.**

**The recommended implementation order:**
1. **SSO** – Centralized authentication (Okta, Azure AD, Google Workspace)
2. **SCIM** – Automated user lifecycle management (Enterprise only)
3. **MDM policies** – Enforce allowed team IDs and extensions
4. **Assign roles** – Members, Admins, Unpaid Admins

**Most important MDM policy:** Allowed Team IDs – prevents personal account usage on corporate devices.

**For security teams:** These controls ensure only authorized users with compliant devices can access Cursor, and only trusted extensions can run.

Would you like me to explain any specific identity control in more detail?