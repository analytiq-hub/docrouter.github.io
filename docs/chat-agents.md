---
layout: docs
title: "Knowledge Base Chat"
permalink: /docs/chat-agents/
description: "Build conversational interfaces over your documents with DocRouter Knowledge Base Chat. Ask natural-language questions via the built-in UI or REST API."
---

<div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-4 md:p-8 mb-6 md:mb-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-2">Chat powered by knowledge bases</h2>
  <p class="text-sm md:text-base text-blue-100">Build conversational interfaces that let users ask natural-language questions over your documents.</p>
</div>

## Get started in 3 steps

<div class="bg-gray-50 rounded-lg p-4 md:p-6 my-4 md:my-6">
  <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">1</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Create a knowledge base</h3>
      <p style="color: #4b5563; margin: 0;">Set up a knowledge base with your documents. Use Markdown format for best results when building Knowledge Base Chat.</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">2</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Test with the built-in chat window</h3>
      <p style="color: #4b5563; margin: 0;">Open your knowledge base and use the chat interface to test questions and verify responses.</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">3</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Integrate via REST API</h3>
      <p style="color: #4b5563; margin: 0;">Use the REST API to build custom chat interfaces in your applications, websites, or services.</p>
    </div>
  </div>
</div>

---

## What is Knowledge Base Chat?

Knowledge Base Chat is a conversational interface that uses knowledge bases to answer questions about your documents. They combine RAG (Retrieval-Augmented Generation) with LLM chat capabilities to provide accurate, context-aware responses.

- **Natural language queries**: Users ask questions in plain English
- **Automatic search**: The AI searches your knowledge base to find relevant information
- **Context-aware responses**: Answers are grounded in your actual documents
- **Streaming support**: Real-time responses for better user experience

---

## Using the Built-in Chat Window

Every knowledge base includes a built-in chat interface accessible from the knowledge base details page.

### Accessing the Chat Window

1. Navigate to **Knowledge Bases** in the sidebar
2. Click on a knowledge base to open its details
3. Select the **Chat** tab

### Chat Features

The chat window provides:

- **Model selection**: Choose from available LLM models (Claude, GPT-4, Gemini, etc.)
- **Conversation history**: Maintains context across multiple messages
- **Streaming responses**: See answers appear in real-time as they're generated
- **Search filters**: Optionally filter by tags or upload date ranges
- **Tool call visibility**: See when the AI searches the knowledge base and how many results it finds

### Using Filters

You can optionally set filters that suggest constraints to the AI:

- **Tag filters**: Limit searches to documents with specific tags
- **Date ranges**: Filter by document upload date (from/to)

Filters are suggestions — the AI can choose whether to use them when searching.

---

## REST API Integration

Use the REST API to build custom chat interfaces that integrate with your applications.

### Endpoint

```
POST /v0/orgs/{organization_id}/knowledge-bases/{kb_id}/chat
```

### Request Format

```json
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": "What is the return policy?"
    }
  ],
  "stream": true,
  "temperature": 0.7,
  "max_tokens": 1000,
  "metadata_filter": {
    "tag_ids": ["tag_id_1", "tag_id_2"]
  },
  "upload_date_from": "2024-01-01",
  "upload_date_to": "2024-12-31"
}
```

### Request Parameters

- **model** (required) — LLM model to use (e.g., `gpt-4o-mini`, `claude-3-5-sonnet-20241022`)
- **messages** (required) — Array of conversation messages with `role` ("user" or "assistant") and `content`
- **stream** (required) — Must be `true` for streaming responses
- **temperature** (optional) — Controls randomness (0.0-2.0, default: 0.7)
- **max_tokens** (optional) — Maximum tokens in the response
- **metadata_filter** (optional) — Filter by document metadata (e.g., `tag_ids`)
- **upload_date_from** (optional) — Filter documents uploaded after this date (ISO format)
- **upload_date_to** (optional) — Filter documents uploaded before this date (ISO format)

### Streaming Response

The API returns a streaming response with chunks that include:

- **Text chunks**: `{"chunk": "text content", "done": false}`
- **Tool call events**: `{"type": "tool_call", "tool_name": "kb_search", "arguments": {...}, "iteration": 1}`
- **Tool result events**: `{"type": "tool_result", "tool_name": "kb_search", "results_count": 5, "iteration": 1}`
- **Completion**: `{"done": true}`
- **Errors**: `{"error": "error message", "done": true}`

### Example: TypeScript SDK

```typescript
import { DocRouterOrgApi } from '@docrouter/sdk';

const api = new DocRouterOrgApi(organizationId);

const request = {
  model: 'gpt-4o-mini',
  messages: [
    { role: 'user', content: 'What is the return policy?' }
  ],
  stream: true,
  temperature: 0.7
};

await api.runKBChatStream(
  kbId,
  request,
  (chunk) => {
    if ('chunk' in chunk) {
      process.stdout.write(chunk.chunk);
    } else if (chunk.type === 'tool_call') {
      console.log(`\n[Searching: ${chunk.tool_name}]`);
    } else if (chunk.done) {
      console.log('\n[Complete]');
    }
  }
);
```

### Example: cURL

```bash
curl -X POST \
  "https://app.docrouter.ai/fastapi/v0/orgs/{organization_id}/knowledge-bases/{kb_id}/chat" \
  -H "Authorization: Bearer your_org_api_token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [
      {"role": "user", "content": "What is the return policy?"}
    ],
    "stream": true
  }'
```

---

## How It Works

When a user asks a question:

1. **Question received**: Knowledge Base Chat receives the user's question
2. **Knowledge base search**: The AI automatically searches the knowledge base for relevant chunks
3. **Context assembly**: Relevant document chunks are assembled into context
4. **Response generation**: The LLM generates an answer grounded in the retrieved context
5. **Streaming delivery**: The response is streamed back to the user in real-time

The AI can make multiple search iterations if needed to gather comprehensive information before answering.

---

## Best Practices

<div class="my-4 md:my-6">
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Use Markdown Documents</strong> — Format your knowledge base documents in Markdown for better structure and readability in chat responses.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Test Thoroughly</strong> — Use the built-in chat window to test various questions and refine your knowledge base content.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Choose the Right Model</strong> — Use faster models like <code class="bg-gray-100 px-1 rounded">gpt-4o-mini</code> for simple queries, and more capable models for complex reasoning.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Use Filters Strategically</strong> — Apply tag or date filters when you want to limit the search scope, but let the AI decide when to use them.</p>
  <p style="margin: 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Handle Streaming</strong> — Implement proper streaming handling in your client to show real-time responses and improve user experience.</p>
</div>

---

## Learn More

- <a href="/docs/knowledge-bases">Knowledge Bases</a> — Learn how to create and manage knowledge bases
- <a href="/docs/rest-api">REST API</a> — Complete API reference for chat endpoints
- <a href="/docs/python-sdk">Python SDK</a> — Python client library (chat support coming soon)
- <a href="/docs/typescript-sdk">TypeScript SDK</a> — TypeScript/JavaScript client library

---

<div class="bg-blue-600 rounded-lg p-4 md:p-8 mt-8 md:mt-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-4">Ready to try Knowledge Base Chat?</h2>
  <a href="https://app.docrouter.ai" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-4 py-3 md:px-8 md:py-4 rounded-lg font-semibold text-base md:text-lg transition-colors duration-200 no-underline">
    Open Dashboard
  </a>
</div>
