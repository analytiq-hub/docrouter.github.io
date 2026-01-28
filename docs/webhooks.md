---
layout: docs
title: "Webhooks"
permalink: /docs/webhooks/
---

<div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-8 mb-10 text-center">
  <h2 class="text-2xl font-semibold text-white mb-2">Webhooks deliver real-time notifications</h2>
  <p class="text-blue-100">Get notified instantly when documents are processed, completed, or encounter errors.</p>
</div>

## Get started in 3 steps

<div class="bg-gray-50 rounded-lg p-6 my-6">
  <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">1</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Create your webhook endpoint</h3>
      <p style="color: #4b5563; margin: 0;">Set up an HTTPS endpoint that can receive POST requests with JSON payloads.</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">2</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Configure in DocRouter</h3>
      <p style="color: #4b5563; margin: 0;">Go to <strong>Organization Settings → Webhooks</strong>, enable webhooks, enter your URL, and select events.</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">3</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Test and verify</h3>
      <p style="color: #4b5563; margin: 0;">Click <strong>Test webhook</strong> to verify your endpoint receives events correctly.</p>
    </div>
  </div>
</div>

---

## What are Webhooks?

Webhooks are HTTP callbacks that notify your application when events occur in DocRouter. They enable real-time integrations without polling.

- **Real-time notifications**: Get instant alerts when documents are processed
- **Event-driven workflows**: Trigger actions in your systems automatically
- **Reliable delivery**: Automatic retries with exponential backoff
- **Secure**: HMAC signature verification for authentication

---

## Event Types

DocRouter sends webhook notifications for these events:

- **`document.uploaded`** — Document uploaded and ready for processing
- **`llm.completed`** — LLM processing finished successfully
- **`llm.error`** — LLM processing failed
- **`document.error`** — Document processing failed
- **`webhook.test`** — Test event sent when testing webhook configuration

---

## Integration Guides

<div class="grid md:grid-cols-2 gap-6 my-6">
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">N8N Integration</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;">Create a Webhook node in N8N, copy the URL, and paste it into DocRouter webhook settings. Select <code class="bg-gray-100 px-1 rounded">llm.completed</code> to receive extracted data.</p>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Use N8N nodes to send extracted JSON to your ERP, CRM, or database.</p>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Temporal Workflows</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;">For complex, long-running workflows, use Temporal signals to wait for the <code class="bg-gray-100 px-1 rounded">llm.completed</code> webhook.</p>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Once received, continue with validation, human-in-the-loop steps, or downstream integrations.</p>
  </div>
</div>

---

## Authentication

### HMAC Signature (Recommended)

DocRouter sends a cryptographic signature in the `X-DocRouter-Signature` header.

**Verification** (Node.js):
```javascript
const crypto = require('crypto');

function verifySignature(secret, timestamp, body, signature) {
  const message = `${timestamp}.${body}`;
  const expected = crypto.createHmac('sha256', secret).update(message).digest('hex');
  return `sha256=${expected}` === signature;
}
```

### Header Authentication

Send a static header value (compatible with N8N, Zapier, etc.).

---

## Payload Format

All webhooks send JSON payloads:

```json
{
  "event_id": "unique-event-id",
  "event_type": "document.uploaded",
  "timestamp": 1640995200,
  "organization_id": "your-org-id",
  "document": {
    "document_id": "doc-123",
    "document_name": "invoice.pdf",
    "tag_ids": ["tag1", "tag2"],
    "metadata": {}
  }
}
```

---

## Best Practices

<div class="my-6">
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Use HTTPS</strong> — Only use HTTPS endpoints for secure delivery.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Verify Signatures</strong> — Always verify HMAC signatures to ensure authenticity.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Check Timestamps</strong> — Reject requests older than 5 minutes to prevent replay attacks.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Prevent Duplicates</strong> — Use <code class="bg-gray-100 px-1 rounded">event_id</code> to prevent duplicate processing.</p>
  <p style="margin: 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Respond Quickly</strong> — Endpoints must respond within 10 seconds. Return HTTP 2xx for success.</p>
</div>

---

## Delivery & Retries

- **Timeout**: Endpoints must respond within 10 seconds
- **Success**: Return HTTP 2xx status codes
- **Retries**: Failed deliveries retry up to 10 times with exponential backoff
- **Monitoring**: View all deliveries in the webhook settings UI
- **Manual Retry**: Click "Retry" on failed deliveries

---

## Learn More

- <a href="/docs/rest-api">REST API</a> — Complete API reference for webhook endpoints
- <a href="https://app.docrouter.ai/fastapi/docs">Interactive API Docs</a> — Test webhook endpoints

---

<div class="bg-blue-600 rounded-lg p-8 mt-10 text-center">
  <h2 class="text-2xl font-semibold text-white mb-4">Ready to set up webhooks?</h2>
  <a href="https://app.docrouter.ai" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
    Open Dashboard
  </a>
</div>
