---
layout: page
title: REST API
permalink: /rest-api/
---

# DocRouter REST API

The DocRouter platform provides a comprehensive REST API that mirrors all functionality available in the UI. This allows you to integrate DocRouter's document processing capabilities directly into your applications and workflows.

## Authentication

DocRouter uses token-based authentication with two types of tokens:

### Account-Level Tokens
- **Usage**: For APIs under `/v0/account`
- **Scope**: Full account access across all organizations
- **Creation**: Go to Account Settings > API Tokens in the DocRouter UI

### Workspace-Level Tokens
- **Usage**: For APIs under `/v0/orgs/{organization_id}`
- **Scope**: Limited to specific workspace/organization
- **Creation**: Go to Workspace Settings > API Tokens in the DocRouter UI

## API Examples

### Account-Level API Examples

#### Get Account Information
```bash
curl -X GET "https://api.docrouter.ai/v0/account/profile" \
     -H "Authorization: Bearer YOUR_ACCOUNT_TOKEN" \
     -H "Content-Type: application/json"
```

#### List All Organizations
```bash
curl -X GET "https://api.docrouter.ai/v0/account/organizations" \
     -H "Authorization: Bearer YOUR_ACCOUNT_TOKEN" \
     -H "Content-Type: application/json"
```

### Workspace-Level API Examples

#### Upload and Process Document
```bash
curl -X POST "https://api.docrouter.ai/v0/orgs/{organization_id}/documents/upload" \
     -H "Authorization: Bearer YOUR_WORKSPACE_TOKEN" \
     -F "file=@/path/to/your/document.pdf" \
     -F "processor_type=invoice"
```

#### Get Processing Results
```bash
curl -X GET "https://api.docrouter.ai/v0/orgs/{organization_id}/documents/{document_id}/results" \
     -H "Authorization: Bearer YOUR_WORKSPACE_TOKEN" \
     -H "Content-Type: application/json"
```

## Interactive API Documentation

For complete API documentation with interactive testing capabilities, visit our **Swagger/OpenAPI documentation** at:

🔗 **[docs/#/](https://docrouter.ai/docs/#/)**

### Using the Swagger Interface

#### 1. Authentication Setup
- Click the **"Authorize"** button at the top of the Swagger page
- Enter your API token (account or workspace-level depending on the endpoint)
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
- Review the interactive documentation at [docs/#/](https://docrouter.ai/docs/#/)
- Contact our support team through the DocRouter UI
- Check our [Python SDK](/python-sdk) for ready-to-use client libraries