---
layout: docs
title: "Webhooks"
permalink: /docs/webhooks/
---

<div class="bg-gradient-to-br from-green-50 via-white to-blue-50 rounded-2xl p-8 mb-12 border border-green-100 shadow-lg">
  <div class="max-w-4xl mx-auto text-center">
    <p class="text-lg text-gray-600 mb-8">
      Get real-time notifications when documents are uploaded, processed, or encounter errors.
    </p>
  </div>
</div>

## Event Types {#events}

DocRouter sends webhook notifications for these events:

| Event | Description |
|-------|-------------|
| `document.uploaded` | Document uploaded and ready for processing |
| `document.error` | Document processing failed |
| `llm.completed` | LLM processing finished successfully |
| `llm.error` | LLM processing failed |
| `webhook.test` | Test event sent when testing webhook configuration |

## Setup {#setup}

1. **Access Settings**: Go to your organization settings → Webhooks tab
2. **Enable Webhooks**: Toggle "Enabled" on
3. **Set URL**: Enter your HTTPS webhook endpoint URL
4. **Choose Authentication**: Select HMAC signature (recommended) or header authentication
5. **Select Events**: Choose which events to receive
6. **Save**: Click "Save" to apply changes

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

Send a static header value (compatible with n8n, Zapier, etc.).

## Payload Format

All webhooks send JSON payloads like this:

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

## Testing

1. Configure your webhook URL and settings
2. Click "Test webhook" button
3. Check that your endpoint receives a `webhook.test` event
4. Verify authentication works correctly

## Delivery & Retries

- **Timeout**: Endpoints must respond within 10 seconds
- **Success**: Return HTTP 2xx status codes
- **Retries**: Failed deliveries retry up to 10 times with exponential backoff
- **Monitoring**: View all deliveries in the webhook settings UI
- **Manual Retry**: Click "Retry" on failed deliveries

## Example Handler

```javascript
app.post('/webhook', (req, res) => {
  const { event_type, document, llm_output, error } = req.body;

  switch(event_type) {
    case 'document.uploaded':
      console.log(`Document uploaded: ${document.document_name}`);
      break;
    case 'llm.completed':
      console.log(`Processing complete for: ${document.document_name}`);
      // Access extracted data: llm_output.extracted_data
      break;
    case 'llm.error':
      console.error(`Processing failed: ${error.message}`);
      break;
  }

  res.status(200).send('OK');
});
```

## Security Best Practices

- ✅ Use HTTPS endpoints only
- ✅ Verify HMAC signatures
- ✅ Check timestamps (reject requests >5 minutes old)
- ✅ Use `event_id` to prevent duplicate processing
- ✅ Store secrets securely

## API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v0/orgs/{org_id}/webhook` | Get webhook configuration |
| PUT | `/v0/orgs/{org_id}/webhook` | Update webhook settings |
| POST | `/v0/orgs/{org_id}/webhook/test` | Send test webhook |
| GET | `/v0/orgs/{org_id}/webhook/deliveries` | List delivery attempts |
| POST | `/v0/orgs/{org_id}/webhook/deliveries/{id}/retry` | Retry failed delivery |