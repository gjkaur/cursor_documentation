This is the **Network Configuration** documentation – it explains how to configure Cursor to work within your enterprise network infrastructure, including proxies, firewalls, and encryption requirements.

Think of this as the **IT setup guide** – for network admins who need to allow Cursor traffic through corporate firewalls and proxies.

Let me break this down.

---

## Overview

**Cursor needs to communicate with backend services and AI providers.** This documentation covers proxies, firewalls, encryption, and troubleshooting.

---

## Proxy Configuration

Many enterprises route traffic through proxy servers for monitoring and security. Cursor works with most proxy configurations, but some settings can cause issues.

### HTTP/2 vs HTTP/1.1

| Protocol | Description |
|----------|-------------|
| **HTTP/2 bidirectional streaming** | Cursor's default for real-time chat and agent experiences |
| **HTTP/1.1 Server-Sent Events (SSE)** | Fallback when HTTP/2 doesn't work |

> *"Zscaler is the most widely used proxy with this limitation"* (doesn't support HTTP/2 streaming correctly).

**Fallback behavior:** If you experience issues, Cursor automatically falls back to HTTP/1 SSE mode. This fallback was specifically designed to work with Zscaler and similar proxies. The fallback happens **transparently**.

---

## SSL Inspection and DLP

Many corporate proxies perform **SSL man-in-the-middle inspection** to scan traffic for security threats or data loss prevention (DLP). This replaces Cursor's SSL certificates with your proxy's certificates.

### The Problem:

> *"When Cursor traffic goes through Secure Web Gateways (SWG), SSL inspection, or DLP, it often causes timeouts, slowness, or errors when using Cursor's Agent capabilities. This is one of the most common deployment blockers for enterprise customers."*

### Recommendation:

Cursor's services are already encrypted end-to-end. **We recommend disabling SSL inspection for these domains:**

| Domain |
|--------|
| `*.cursor.sh` |
| `*.cursor-cdn.com` |
| `*.cursorapi.com` |
| `authenticate.cursor.sh` |
| `authenticator.cursor.sh` |

### If SSL Inspection is Required:

Your proxy must support:

| Requirement | Description |
|-------------|-------------|
| **HTTP/2 bidirectional streaming** | Or Cursor's HTTP/1 fallback must work |
| **Server-Sent Events (SSE) passthrough** | Without buffering |
| **Long-running connections** | Without forced timeouts |
| **No response buffering** | For streaming content types |

---

## Testing Proxy Connectivity

Use these `curl` commands to diagnose connectivity issues.

### Test 1: Basic Connectivity

```bash
curl -v https://api2.cursor.sh 2>&1 | grep -C1 "issuer:"
```

**What to expect:** You should see "Amazon RSA". If you see your proxy provider (like Zscaler), SSL inspection is active.

### Test 2: HTTP/1.1 Streaming

```bash
echo -ne "\x01\x01\x01\x11payload\"foo\"" | \
curl -N -XPOST \
  -H "Content-Type: application/connect+json" \
  --data-binary @- \
  https://api2.cursor.sh/aiserver.v1.HealthService/StreamSSE
```

**What to expect:** Output appears line by line over 5 seconds. If it appears all at once after 5 seconds, your proxy is buffering streaming responses.

### Test 3: HTTP/2 Bidirectional Streaming

```bash
for i in 1 2 3 4 5; do
  echo -ne "\x01\x01\x01\x12payload\"foo$i\"";
  sleep 1;
done | curl -N -XPOST \
  -H "Content-Type: application/connect+json" \
  -T - \
  https://api2.cursor.sh/aiserver.v1.HealthService/StreamBidi
```

**What to expect:** Output should appear once per second. If buffered for 5 seconds, your proxy doesn't support HTTP/2 bidirectional streaming.

---

## IP Allowlisting

If your network uses IP-based access controls, rather than maintaining IP address lists (which can change), configure your firewall to allow traffic to these **domain patterns**:

| Domain Pattern |
|----------------|
| `*.cursor.sh` |
| `*.cursor-cdn.com` |
| `*.cursorapi.com` |

---

## VPC Peering

> *"Cursor doesn't currently offer VPC peering or private connectivity options."*

**However,** when you run Cursor on a machine within your VPC, agent operations inherit:

| Inherited configuration |
|-------------------------|
| Your network security groups |
| Your firewall rules |
| Your DNS configuration |
| Your VPN or private network access |

> *"This means Cursor agents can access internal resources that the machine can reach, while following your existing network security controls."*

---

## Encryption

### In Transit

| Standard | Description |
|----------|-------------|
| **TLS 1.2 or higher** | All connections to Cursor services |
| **TLS** | Connections to third-party AI providers |
| **Certificate pinning** | For critical services |

### At Rest

| Standard | Description |
|----------|-------------|
| **AES-256** | For stored data |
| **Encrypted vector database** | For embeddings |
| **Encrypted code storage** | For Cloud Agents (when enabled) |

### Key Management

Cursor manages encryption keys. Keys are rotated according to security best practices and stored in secure key management systems.

For enhanced security control, enterprise customers can use **Customer Managed Encryption Keys (CMEK)**. See Data Encryption for details.

---

## LLM Gateways

Some enterprises want to route LLM traffic through their own gateways for additional monitoring and control.

> *"Custom gateways can introduce additional latency, rate limiting, and compatibility issues. We instead recommend using Cursor's built-in hooks feature to implement your own security controls."*

**Important:** Cursor's Zero Data Retention policy does **not** apply when using your own API keys. Your data handling will be subject to the privacy policies of your chosen AI provider.

---

## Cloud Agents Networking

Cloud Agents run on Cursor's infrastructure, not your local network.

### Can Access:

| Resource |
|----------|
| Public GitHub repositories |
| GitHub Enterprise Cloud (with granted access) |
| GitHub Enterprise Server (self-hosted) |
| On-prem + cloud-based GitLab and Bitbucket |
| Public package registries (npm, PyPI, etc.) |

### Cannot Access:

| Resource |
|----------|
| Resources behind your corporate firewall |
| On-premises GitHub Enterprise Server (without public access) |
| Private package registries without internet access |

> *"If your development workflow requires access to internal resources, use the Cursor editor on machines within your network instead of Cloud Agents."*

---

## Troubleshooting Checklist

If you experience connection issues:

| Step | Action |
|------|--------|
| 1 | Test basic connectivity to `api2.cursor.sh` |
| 2 | Check if SSL inspection is active and consider excluding Cursor domains |
| 3 | Verify streaming works using the curl tests above |
| 4 | Check firewall rules allow traffic to `*.cursor.sh` and related domains |
| 5 | Review proxy logs for connection errors or timeouts |
| 6 | Test from a machine outside your network to isolate network-specific issues |

> *"Most connectivity issues stem from proxies buffering streaming responses. Work with your network team to disable buffering for Cursor domains or implement proper streaming support."*

---

## Quick Reference Card

| Topic | Key Points |
|-------|------------|
| **Default protocol** | HTTP/2 bidirectional streaming |
| **Fallback** | HTTP/1 SSE (for Zscaler, etc.) |
| **SSL inspection** | Recommend disabling for `*.cursor.sh`, `*.cursor-cdn.com`, `*.cursorapi.com` |
| **Domains to allow** | `*.cursor.sh`, `*.cursor-cdn.com`, `*.cursorapi.com` |
| **Encryption in transit** | TLS 1.2+ |
| **Encryption at rest** | AES-256 |
| **CMEK** | Available for Enterprise |
| **Cloud Agents** | Cannot access resources behind corporate firewall |

---

## Common Beginner Questions

### Q: Why does Cursor need special network configuration?
**A:** Cursor uses streaming for real-time AI responses. Some corporate proxies buffer or break these streams.

### Q: What proxy causes the most issues?
**A:** Zscaler is the most widely used proxy with HTTP/2 streaming limitations. Cursor has a fallback for it.

### Q: Should we disable SSL inspection for Cursor domains?
**A:** Recommended – Cursor traffic is already encrypted end-to-end, and SSL inspection often causes issues.

### Q: Can Cursor agents access our internal resources?
**A:** Local agents (running on your machine) can access internal resources. Cloud Agents cannot.

### Q: Does Cursor support VPC peering?
**A:** Not currently. But agents running on machines in your VPC inherit your network configuration.

### Q: How do I test if my proxy is causing issues?
**A:** Run the curl tests above – they'll show if streaming is buffered or broken.

---

## The Bottom Line

**Network configuration is one of the most common deployment blockers for enterprise customers, but most issues can be resolved by:**

1. **Disabling SSL inspection** for Cursor domains (recommended)
2. **Allowing traffic** to `*.cursor.sh`, `*.cursor-cdn.com`, `*.cursorapi.com`
3. **Ensuring your proxy supports** streaming (HTTP/2 or Cursor's HTTP/1 fallback)
4. **Testing connectivity** with the curl commands provided

**For IT/network teams:** The key is streaming support. If your proxy buffers responses, Cursor's real-time agent experience will be broken. Work with your network team to disable buffering for Cursor domains or implement proper streaming passthrough.

Would you like me to explain any specific network configuration topic in more detail?