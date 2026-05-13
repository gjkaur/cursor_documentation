This is the **Team Pricing** documentation – it explains the pricing structure for Cursor's Teams and Enterprise plans.

Think of this as the **cost breakdown** for using Cursor with a team – how much per user, what's included, and how usage-based pricing works.

Let me break this down.

---

## Two Plans

| Plan | Price | Best for |
|------|-------|----------|
| **Teams** | $40/user/month | Customers happy self-serving |
| **Enterprise** | Custom | Priority support, pooled usage, invoicing, SCIM, advanced security controls |

> *"Contact sales to get started"* for Enterprise.

---

## Team Plan Features

| Feature | Included |
|---------|----------|
| Privacy Mode enforcement | ✅ |
| Admin Dashboard with usage stats (via Admin API) | ✅ |
| Centralized team billing | ✅ |
| SAML/OIDC SSO | ✅ |

---

## How Pricing Works

**Teams pricing is usage-based.** Each seat includes monthly usage, and you can continue using Cursor beyond that with on-demand usage.

---

## Included Usage

**Each team seat ($40/month) comes with $20/month of included usage.**

| Rule | Description |
|------|-------------|
| **Allocation** | Per user (each user gets their own $20) |
| **Transfer** | Does NOT transfer between team members |
| **Reset** | Resets at the start of each billing cycle |
| **Coverage** | All agent requests at public list API prices + Cursor Token Rate |

> *"Our Enterprise plan offers pooled usage shared between all users in a team."*

---

## On-Demand Usage

When exceeding the $20 of included usage, team members automatically continue with on-demand usage:

| Feature | Description |
|---------|-------------|
| **Billing** | Monthly, at same rates (API prices + Cursor Token Rate) |
| **Service** | No interruption or quality degradation |
| **Tracking** | Per user in admin dashboard (spending data API) |
| **Control** | Spending limits available |

> *"On-demand usage is enabled by default for the Teams plan."*

---

## Cursor Token Rate

**All non-Auto agent requests include a Cursor Token Rate of $0.25 per million tokens.**

This covers:
- Semantic search
- Custom model execution (Tab, Apply, etc.)
- Infrastructure and processing costs

> *"The Cursor Token Rate applies to all tokens: input, output, and cached tokens. This applies to BYOK as well."*

---

## Active Seats (Billing Model)

> *"Cursor bills per active user, not pre-allocated seats. Add or remove users anytime and billing will adjust immediately."*

| Feature | Description |
|---------|-------------|
| **Billing model** | Per active user (not pre-allocated seats) |
| **Changes** | Add or remove users anytime – billing adjusts immediately |
| **Refunds** | Appear as account credit on next invoice |
| **Renewal date** | Stays the same |

---

## Spending Controls

| Plan | Control |
|------|---------|
| **Teams** | Monthly team-wide spending limits (via dashboard) |
| **Enterprise** | Per-member spend limits available |

> *"Contact enterprise@cursor.com for volume discounts on larger teams."*

---

## Model Pricing (API Rates + Cursor Token Rate)

All prices are **per million tokens**. Teams are charged at **public list API prices + Cursor Token Rate ($0.25 per million tokens)**.

| Model | Input | Output |
|-------|-------|--------|
| Composer 2 | $0.50 | $2.50 |
| GPT-5 Mini | $0.25 | $2.00 |
| Gemini 2.5 Flash | $0.30 | $2.50 |
| GPT-5 | $1.25 | $10.00 |
| Claude 4.5 Haiku | $1.00 | $5.00 |
| Claude 4.6 Sonnet | $3.00 | $15.00 |
| Claude 4.7 Opus | $5.00 | $25.00 |
| GPT-5.5 | $5.00 | $30.00 |
| Claude 4.6 Opus (Fast) | $30.00 | $150.00 |

*Full model pricing table available in documentation.*

---

## Pricing Summary Table

| Component | Amount |
|-----------|--------|
| **Team seat** | $40/user/month |
| **Included usage per seat** | $20/month |
| **Cursor Token Rate** | $0.25 per million tokens |
| **On-demand** | Automatic after included usage exhausted |

---

## Example Monthly Cost Calculation

**For a 5-person team:**

| Item | Calculation | Total |
|------|-------------|-------|
| Seat cost | 5 × $40 | $200 |
| Included usage | 5 × $20 = $100 value | Included |
| Total base | | **$200/month** |

**If each user uses $30 of API usage:**

| User | Included | Overage |
|------|----------|---------|
| Each user | $20 | $10 |
| 5 users | $100 total | $50 total overage |

Total cost: $200 (seats) + $50 (overage) = **$250/month**

---

## Teams vs. Enterprise

| Feature | Teams | Enterprise |
|---------|-------|------------|
| **Price** | $40/user/month | Custom |
| **Usage pooling** | ❌ Per user | ✅ Pooled |
| **Per-member spend limits** | ❌ | ✅ |
| **Priority support** | ❌ | ✅ |
| **Invoicing** | ❌ | ✅ |
| **SCIM** | ❌ | ✅ |
| **Advanced security controls** | ❌ | ✅ |
| **SAML/OIDC SSO** | ✅ | ✅ |
| **Admin Dashboard** | ✅ | ✅ |
| **Privacy Mode enforcement** | ✅ | ✅ |

---

## Common Beginner Questions

### Q: Is Teams pricing per user or per seat?
**A:** Per active user. You only pay for users actually using Cursor, not pre-allocated seats.

### Q: What happens if a user exceeds their $20 included usage?
**A:** On-demand usage kicks in automatically. No service interruption.

### Q: Can unused included usage be shared?
**A:** No – each user gets their own $20. It does not transfer between team members. (Enterprise has pooled usage.)

### Q: What is the Cursor Token Rate?
**A:** An additional $0.25 per million tokens covering semantic search, infrastructure, and processing costs.

### Q: Can I set spending limits?
**A:** Teams can set team-wide monthly limits. Enterprise can set per-member limits.

### Q: Does the Cursor Token Rate apply to BYOK?
**A:** Yes.

---

## The Bottom Line

**Teams pricing is $40 per user per month, with each user getting $20 of included API usage. Beyond that, on-demand usage at API rates + $0.25 Cursor Token Rate kicks in automatically.**

**Key takeaways:**
- Pay per active user (not pre-allocated seats)
- Each user gets $20 monthly usage included
- Automatic on-demand usage after included amount
- $0.25 per million tokens Cursor Token Rate on all non-Auto requests
- Team-wide spending limits available
- Enterprise offers pooled usage, per-member limits, and more

**For larger teams:** Contact `enterprise@cursor.com` for volume discounts and Enterprise plan details.

Would you like me to explain any specific pricing detail in more detail?