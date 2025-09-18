---
layout: page
title: DocRouter REST API
permalink: /rest-api/
---

<div class="flex flex-col lg:flex-row lg:justify-between lg:items-start gap-3 mb-8">
  <div class="flex-1">
    <p class="text-lg text-gray-600 leading-relaxed">
      The DocRouter platform provides a comprehensive REST API that mirrors all functionality available in the UI.
    </p>
  </div>

  <div class="lg:w-80">
    <div class="bg-gradient-to-r from-blue-500 to-blue-600 rounded-lg p-4 text-white shadow-lg flex flex-col items-center text-center">
      <p class="text-blue-100 mb-3">Jump to our interactive API docs</p>
      <a href="https://app.docrouter.ai/fastapi/docs/#/" target="_blank" rel="noopener noreferrer"
         class="inline-flex items-center gap-2 bg-white text-blue-600 px-4 py-2 rounded-md font-medium hover:bg-blue-50 transition-colors">
        <span>Open Swagger UI</span>
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
        </svg>
      </a>
    </div>
  </div>
</div>

## Authentication

DocRouter uses token-based authentication with two types of tokens:

<div class="grid md:grid-cols-2 gap-6 my-6">
  <div class="bg-blue-50 border border-blue-200 rounded-lg p-6">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-10 h-10 bg-blue-500 rounded-lg flex items-center justify-center mt-3">
        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0h3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
        </svg>
      </div>
      <h3 class="text-xl font-semibold text-blue-900">Account-Level Tokens</h3>
    </div>
    <div class="space-y-3 text-blue-800">
      <div class="flex items-start gap-2">
        <span class="font-medium">Usage:</span>
        <span>For APIs under <code class="bg-blue-100 px-2 py-1 rounded text-sm">/v0/account</code></span>
      </div>
      <div class="flex items-start gap-2">
        <span class="font-medium">Scope:</span>
        <span>Account Access</span>
      </div>
      <div class="flex items-start gap-2">
        <span class="font-medium">Creation:</span>
        <span>Go to Settings > Account Tokens</span>
      </div>
    </div>
  </div>

  <div class="bg-green-50 border border-green-200 rounded-lg p-6">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-10 h-10 bg-green-500 rounded-lg flex items-center justify-center mt-3">
        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0h3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
        </svg>
      </div>
      <h3 class="text-xl font-semibold text-green-900">Organization-Level Tokens</h3>
    </div>
    <div class="space-y-3 text-green-800">
      <div class="flex items-start gap-2">
        <span class="font-medium">Usage:</span>
        <span>For APIs under <code class="bg-green-100 px-2 py-1 rounded text-sm">/v0/orgs/{organization_id}</code></span>
      </div>
      <div class="flex items-start gap-2">
        <span class="font-medium">Scope:</span>
        <span>Organization Access</span>
      </div>
      <div class="flex items-start gap-2">
        <span class="font-medium">Creation:</span>
        <span>Go to Settings > Organizations Tokens</span>
      </div>
    </div>
  </div>
</div>

## API Examples

### Account-Level API Examples

#### List All Organizations
```bash
curl -X GET "https://app.docrouter.ai/fastapi/v0/account/organizations" \
     -H "Authorization: Bearer YOUR_ACCOUNT_TOKEN" \
     -H "Content-Type: application/json"
```

**Example Response:**
```json
{
  "organizations": [
    {
      "id": "12345678abcdef123456789a",
      "name": "my-organization",
      "members": [
        {
          "user_id": "12345678abcdef123456789b",
          "role": "admin"
        },
        {
          "user_id": "12345678abcdef123456789c",
          "role": "user"
        }
      ],
      "type": "team",
      "created_at": "2025-01-15T10:30:00.000000",
      "updated_at": "2025-01-15T14:20:00.000000"
    }
  ]
}
```

### Organization-Level API Examples

#### List Documents
```bash
curl -X GET "https://app.docrouter.ai/fastapi/v0/orgs/12345678abcdef123456789a/documents" \
     -H "Authorization: Bearer YOUR_ORGANIZATION_TOKEN" \
     -H "Content-Type: application/json"
```

**Example Response:**
```json
{
  "documents": [
    {
      "id": "12345678abcdef123456789d",
      "pdf_id": "12345678abcdef123456789e",
      "document_name": "invoice_2025_001.pdf",
      "upload_date": "2025-01-15T10:30:00.000000Z",
      "uploaded_by": "John Doe",
      "state": "llm_completed",
      "tag_ids": ["12345678abcdef123456789f"],
      "type": "invoice",
      "metadata": {}
    },
    {
      "id": "12345678abcdef123456789g",
      "pdf_id": "12345678abcdef123456789h",
      "document_name": "contract_agreement.pdf",
      "upload_date": "2025-01-14T15:20:00.000000Z",
      "uploaded_by": "Jane Smith",
      "state": "processing",
      "tag_ids": ["12345678abcdef123456789i"],
      "type": "contract",
      "metadata": {}
    }
  ],
  "total_count": 2,
  "skip": 0
}
```

## Interactive API Documentation

For complete API documentation with interactive testing capabilities, visit our **Swagger/OpenAPI documentation** at:

🔗 **[docs/#/](https://app.docrouter.ai/fastapi/docs/#/)**

### Using the Swagger Interface

#### 1. Authentication Setup
- Click the **"Authorize"** button at the top of the Swagger page
- Enter your API token (account or organization-level depending on the endpoint)
- Click **"Authorize"** to authenticate your session

#### 2. Testing API Endpoints
- Browse the available endpoints organized by category
- Click on any endpoint to expand its details
- Click **"Try it out"** to enable the interactive form
- Fill in required parameters and request body
- Click **"Execute"** to make the API call

#### 3. Generating cURL Commands
- After executing an API call, scroll down to the **"Response"** section
- Find the **"Curl"** tab to see the equivalent cURL command
- Copy the command to use in your terminal or scripts

### Example Workflow in Swagger UI

1. **Authenticate**: Use the Authorize button with your token
2. **Upload Document**: Use `/v0/orgs/{organization_id}/documents/upload`
3. **Check Status**: Use `/v0/orgs/{organization_id}/documents/{document_id}/status`
4. **Get Results**: Use `/v0/orgs/{organization_id}/documents/{document_id}/results`

## Rate Limits and Best Practices

- **Rate Limits**: API calls are subject to rate limiting based on your subscription plan
- **Async Processing**: Document processing is asynchronous - poll the status endpoint for completion
- **Error Handling**: All endpoints return standard HTTP status codes with descriptive error messages
- **Pagination**: List endpoints support pagination with `limit` and `offset` parameters

## Support

For API support and questions:
- Review the interactive documentation at [docs/#/](https://app.docrouter.ai/fastapi/docs/#/)
- Contact our support team through the DocRouter UI
- Check our [Python SDK](/python-sdk) for ready-to-use client libraries