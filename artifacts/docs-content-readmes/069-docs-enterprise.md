This is the **Enterprise** documentation – it provides an overview of Cursor's enterprise-grade security, compliance, and administrative controls for organizations deploying AI-assisted development at scale.

Think of this as the **executive summary** for IT and security teams – covering everything from SOC2 compliance to SSO to audit logs.

Let me break this down.

---

## Security & Compliance Resources

For security reviews and compliance assessments, start with:

| Resource | Description |
|----------|-------------|
| **Trust Center** | Security practices, certifications, compliance information |
| **Security page** | Detailed security architecture and controls |
| **Privacy Overview** | Data handling and privacy guarantees |
| **Data Processing Agreement** | GDPR-compliant DPA with data protection commitments |

> *"Our certifications include SOC2 Type II, and we maintain GDPR compliance."*

---

## Enterprise Documentation Topics

| Category | What it covers |
|----------|----------------|
| **Identity & access** | SSO, SCIM, RBAC, MDM policies |
| **Privacy & data governance** | Data flows, Privacy Mode, data residency |
| **Network configuration** | Proxy setup, IP allowlisting, encryption |
| **LLM safety & controls** | Hooks, terminal sandboxing, agent controls |
| **Models & integrations** | Model controls, MCP, third-party integrations |
| **Spend Limits** | Configure spending limits to control costs |
| **Compliance & monitoring** | Audit logs and tracking |
| **HIPAA BAA** | Business Associate Agreement support |
| **Deployment patterns** | MDM-managed editor vs self-hosted CLI |

---

## Key Features by Category

### Identity and Access

| Feature | Description |
|---------|-------------|
| **SSO and SAML** | Single sign-on for streamlined authentication |
| **SCIM** | Automated user provisioning and deprovisioning |
| **MDM policies** | Enforce allowed team IDs and extensions on user devices |

### Privacy and Security

| Feature | Description |
|---------|-------------|
| **Privacy Mode** | Zero data retention with AI providers |
| **Agent Security** | Guardrails for agent tool execution |
| **Hooks** | Custom security and compliance workflows |

### Administrative Controls

| Feature | Availability | Description |
|---------|--------------|-------------|
| **Dashboard** | All plans | Team management, settings, monitoring |
| **Admin API** | Enterprise | Programmatic access to admin features |
| **Analytics** | Teams/Enterprise | Usage metrics and insights |
| **Conversation Insights** | Enterprise only | Understand type of work being done |
| **AI Code Tracking API** | Enterprise only | Per-commit AI usage metrics |
| **Cursor Blame** | Enterprise only | AI-aware git blame (AI vs human attribution) |
| **Analytics API** | Teams/Enterprise | Usage metrics and insights |
| **Billing Groups** | Enterprise only | Manage spend across user groups |
| **Service Accounts** | Enterprise only | Non-human accounts for automated workflows |

### Monitoring and Compliance

| Feature | Availability | Description |
|---------|--------------|-------------|
| **Audit logs** | Enterprise only | Track authentication, user management, admin actions |
| **SIEM integration** | Enterprise | Stream audit logs to security tools |
| **HIPAA BAA** | Enterprise | Business Associate Agreement support |

---

## Plan Comparison

### Team Admin & Billing

| Capability | Individual | Teams | Enterprise |
|------------|------------|-------|------------|
| Centralized Billing | ✓ | ✓ | ✓ |
| Usage Spend Controls | Personal limits | Team limits | Pooled usage + admin-only controls |
| Billing Groups | | | ✓ |
| Team Usage Analytics | Analytics Dashboard | Analytics Dashboard | + AI Code Tracking API, Conversation Insights, Cursor Blame |
| SSO (SAML/OIDC) | | ✓ | ✓ |
| SCIM Provisioning | | | ✓ |
| Audit Logs | | | ✓ |
| Service Accounts | | | ✓ |

### Team Marketplaces

| Capability | Teams | Enterprise |
|------------|-------|------------|
| Team marketplaces | Up to 1 | Unlimited |
| Community plugin import | On by default | Off by default |
| Marketplace edits | All team members | Only admin edits |
| SCIM distribution & access gating | No SCIM access | Scope distribution and gate access via SCIM |

### Centralized Agent Controls

| Capability | Teams | Enterprise |
|------------|-------|------------|
| Privacy Mode | Enforce org-wide | Enforce org-wide |
| Team Rules | Enforceable + Optional | Enforceable + Optional |
| Hooks for Logging, Auditing | MDM Distribution | MDM & Server-side distribution |
| Agent Sandbox Mode | | Enforce org-wide |
| Repository Blocklist | | |
| Model Access Restrictions | | Enforce org-wide |
| Auto-run, Browser, Network Controls | | Enforce org-wide |

### User Access Controls (Enterprise only)

| Capability | Description |
|------------|-------------|
| **Cloud Agents** | Restrict which users can create Cloud Agents |
| **Analytics** | Restrict analytics dashboard to admins only |
| **BYOK** | Disable users from using their own API keys |

### Support & Legal

| Capability | Individual | Teams | Enterprise |
|------------|------------|-------|------------|
| **Technical Support** | Community | Community & Standard Support | First human response times: 8 hours (critical), 24 hours (standard) |
| **Terms** | Online Terms | MSA & DPA | MSA & DPA |

---

## Getting Started (5 Steps)

| Step | Action |
|------|--------|
| 1 | Review the Trust Center and Security page for your security assessment |
| 2 | Read through the enterprise documentation to understand deployment options |
| 3 | Set up SSO and SCIM for user management |
| 4 | Deploy Cursor and configure MDM policies to enforce team IDs and extensions |
| 5 | Review the Dashboard to monitor team usage |

---

## Enterprise-Only Features Summary

| Feature | Category |
|---------|----------|
| Conversation Insights | Analytics |
| AI Code Tracking API | Analytics |
| Cursor Blame | Analytics |
| Billing Groups | Spend Management |
| Service Accounts | Automation |
| Audit Logs | Compliance |
| SIEM Integration | Compliance |
| HIPAA BAA | Compliance |
| SCIM Provisioning | Identity |
| Repository Blocklist | Security |
| Model Access Restrictions | Security |
| Agent Sandbox Mode (enforce) | Security |
| Auto-run/Browser/Network Controls (enforce) | Security |
| Per-member spend limits | Spend Management |
| Unlimited team marketplaces | Marketplace |

---

## Common Beginner Questions

### Q: What compliance certifications does Cursor have?
**A:** SOC2 Type II, GDPR compliant. Visit Trust Center for latest docs.

### Q: What is Cursor Blame?
**A:** AI-aware git blame that shows whether code was written by AI or humans (Enterprise only).

### Q: Does Enterprise include SSO?
**A:** Yes – SAML/OIDC SSO is included.

### Q: What is SCIM?
**A:** Automated user provisioning and deprovisioning from your identity provider to Cursor.

### Q: Can I get a HIPAA BAA?
**A:** Yes – Enterprise customers can request BAA support.

### Q: What are the support SLAs for Enterprise?
**A:** First human response: 8 hours for critical issues, 24 hours for standard issues.

---

## The Bottom Line

**Cursor Enterprise provides security, compliance, and administrative controls for organizations deploying AI-assisted development at scale.**

**Key differentiators from Teams:**
- **Audit logs** – Track authentication, user management, admin actions
- **SCIM** – Automated user provisioning
- **Conversation Insights** – Understand what type of work agents are doing
- **Cursor Blame** – AI vs human code attribution
- **Service Accounts** – Non-human accounts for automation
- **Billing Groups** – Manage spend across user groups
- **HIPAA BAA** – Available on request
- **Faster support** – 8-hour response for critical issues

**For security teams:** SOC2 Type II, GDPR compliance, Privacy Mode, and extensive administrative controls make Cursor enterprise-ready.

**Getting started:** Review Trust Center → Read documentation → Set up SSO/SCIM → Deploy with MDM → Monitor dashboard

