---
layout: docs
title: "Document Agent"
permalink: /docs/document-agent/
---

<div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-4 md:p-8 mb-6 md:mb-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-2">Configure schemas, tags, and prompts with AI</h2>
  <p class="text-sm md:text-base text-blue-100">Use the Document Agent to set up extraction in plain language. The AI can create and edit schemas, prompts, and tags, then run extraction—all in context of the current document.</p>
</div>

## What it is

The **Document Agent** is an AI assistant that works in the context of a single document. You use it to **configure extraction with natural language**: create or edit schemas, prompts, and tags, then run extraction and tweak results—without leaving the document view.

- **Where**: Open any document in the DocRouter app and open the Document Agent (e.g. Chat / Agent tab).
- **Purpose**: Get from “I have a document” to “I have a schema, prompt, and extracted data” by talking to the AI instead of filling forms by hand.

---

## What you can do

In the Document Agent you can ask the AI to:

- **Create or edit schemas** — e.g. “Create a schema for this invoice with vendor, date, line items, and total.” The AI uses the document text to propose a JSON schema, validates it, and creates it in your org.
- **Create or edit prompts** — e.g. “Write a prompt to extract vendor name and total amount,” or “Use the Invoice schema we just created.” The AI can link prompts to schemas and run extraction.
- **Manage tags** — e.g. “Create a tag ‘Urgent’ and add it to this document,” or “List my tags.”
- **Run and fix extraction** — e.g. “Run extraction with that prompt” or “Change the total to 1,250.” The AI can run extraction and patch individual fields.
- **Document metadata** — Rename the document, set tags, or update metadata.

For **read-only** actions (e.g. “What’s on page 1?”, “List my schemas”), the AI runs tools automatically. For **write** actions (create schema, create prompt, run extraction, update document), the app can ask you to **approve** each step so you see exactly what will be created or changed before it happens.

---

## How to use it

1. **Open a document** in the DocRouter app (e.g. from Documents or from a tag).
2. **Open the Document Agent** on the document page (Chat / Agent tab or similar).
3. **Say what you want** in plain language, for example:
   - “Create a schema for this invoice: vendor, date, line items with description and amount, and total.”
   - “Create a prompt that extracts those fields and use the schema we just made.”
   - “Run extraction and show me the result.”
4. **Approve when asked** — If the AI wants to create or change something (schema, prompt, tag, extraction), you’ll see the proposed action and can approve or reject it.
5. **Iterate** — Ask to adjust the schema, change the prompt, or fix a field; the AI uses the same document context and your existing schemas/prompts/tags.

Conversations are saved in **threads** per document, so you can come back later and continue (“Add a field for PO number”) or start a new thread for a different setup.

---

## How it works under the hood

The Document Agent is backed by a **tool-calling agent** that sees:

- The **current document** (name, ID) and an **OCR/text excerpt** of the document.
- Optional **@-mentions** (e.g. a schema or prompt you’ve referenced) so the AI has the full content.
- **Working state** — the last extraction result and schema/prompt revisions used, so it can run extraction again or update fields.

The AI has tools to read and write schemas, prompts, tags, document metadata, and extraction results. It is instructed to validate schemas before creating or updating them and to use built-in help tools when creating schemas or prompts. Read-only tools run automatically; write tools (create/update/delete schema, prompt, tag, run extraction, update document) can be gated behind **approval** so you confirm each change.

---

## REST API (for integrations)

The same agent is available via REST so you can build custom UIs or automate flows.

**Base path:**

```
/v0/orgs/{organization_id}/documents/{document_id}/chat
```

**Main endpoints:**

- **POST .../chat** — Send messages, get replies (optionally streamed). Body: `messages`, `model`, `stream`, `auto_approve`, `thread_id`, optional `mentions`. When a write is requested and approval is required, the response includes `turn_id` and `tool_calls`; you then call the approve endpoint.
- **POST .../chat/approve** — Submit approvals for pending tool calls. Body: `turn_id`, `approvals` (list of `{ "call_id", "approved" }`).
- **GET .../chat/tools** — Lists `read_only` and `read_write` tool names (useful to know which actions need approval).
- **Threads**: **GET/POST .../chat/threads**, **GET/DELETE .../chat/threads/{thread_id}** — List, create, load, or delete conversation threads for the document.

Use an **organization API token** for authentication. For full request/response shapes and streaming (SSE) event types, see the [interactive API docs](https://app.docrouter.ai/fastapi/docs) (tag: **agent**).

---

## Related docs

- <a href="{{ '/docs/prompts/' | relative_url }}">Prompts</a> — Extraction prompts and how they work  
- <a href="{{ '/docs/schemas/' | relative_url }}">Schemas</a> — Structured output and validation  
- <a href="{{ '/docs/tags/' | relative_url }}">Tags</a> — Document tags and routing  
- <a href="{{ '/docs/chat-agents/' | relative_url }}">Knowledge Base Chat</a> — Chat over many documents (RAG)  
- <a href="{{ '/docs/rest-api/' | relative_url }}">REST API</a> — Authentication and API reference  
