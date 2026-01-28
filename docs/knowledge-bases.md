---
layout: docs
title: "Knowledge Bases"
permalink: /docs/knowledge-bases/
---

<div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-8 mb-10 text-center">
  <h2 class="text-2xl font-semibold text-white mb-2">Knowledge bases provide context for better extraction</h2>
  <p class="text-blue-100">Upload reference documents so the AI can use them to improve accuracy and understand your specific terminology.</p>
</div>

## Get started in 3 steps

<div class="bg-gray-50 rounded-lg p-6 my-6">
  <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">1</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Create a knowledge base</h3>
      <p style="color: #4b5563; margin: 0;">Go to <strong>Knowledge Bases</strong> in the sidebar, click <strong>New Knowledge Base</strong>, and give it a name.</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">2</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Upload reference documents</h3>
      <p style="color: #4b5563; margin: 0;">Add PDFs, TXT, or Markdown files with your reference materials (price lists, catalogs, terminology guides).</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">3</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Test the knowledge base by chatting with it</h3>
      <p style="color: #4b5563; margin: 0;">Open the knowledge base and use the chat interface to ask questions and verify it's working correctly.</p>
    </div>
  </div>
</div>

<p style="color: #4b5563; margin-top: 1rem;">To use your knowledge base with extraction prompts, select it in the prompt editor. The AI will automatically use it when processing documents.</p>

---

## What are Knowledge Bases?

Knowledge bases are collections of reference documents that help the AI understand your specific terminology, rules, and context. They use RAG (Retrieval-Augmented Generation) to find relevant information and include it in the AI's context.

- **Better accuracy**: AI uses your reference materials to improve extraction
- **Industry terminology**: Teach the AI specific terms used in your business
- **Reference data**: Provide price lists, SKU catalogs, vendor IDs, or guidelines
- **Chat agents**: Use knowledge bases as the backend for chat agents so users can ask questions over your documents

---

## Configuration Settings

When creating a knowledge base, you can configure how documents are indexed and searched. Some settings are **immutable** after creation (you'll need to create a new KB to change them), while others can be updated anytime.

### Basic Settings

- **Name** (required) — A descriptive name for your knowledge base
- **Description** (optional) — Additional context about the knowledge base's purpose
- **Tags** (optional) — Document tags that automatically index documents into this knowledge base

### Indexing Configuration (Immutable)

These settings determine how documents are split into chunks and embedded. **They cannot be changed after creation** — create a new knowledge base if you need different settings.

<div class="grid md:grid-cols-2 gap-6 my-6">
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Chunker Type</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;">How documents are split into chunks:</p>
    <ul style="color: #4b5563; font-size: 0.875rem; margin: 0; padding-left: 1.25rem;">
      <li><strong>recursive</strong> (default) — Smart splitting that respects document structure</li>
      <li><strong>token</strong> — Split by token count</li>
      <li><strong>word</strong> — Split by word boundaries</li>
      <li><strong>sentence</strong> — Split by sentence boundaries</li>
    </ul>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Chunk Size</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;"><strong>Default:</strong> 512 tokens</p>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Range: 50-2000 tokens. Larger chunks preserve more context but may be less precise for retrieval.</p>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Chunk Overlap</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;"><strong>Default:</strong> 128 tokens</p>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Range: 0 to (chunk_size - 1). Overlap helps preserve context across chunk boundaries.</p>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Embedding Model</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;"><strong>Default:</strong> text-embedding-3-small</p>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">The model used to create vector embeddings. Available models depend on your configured LLM providers.</p>
  </div>
</div>

### Search Configuration (Mutable)

These settings control how search results are returned and can be updated anytime.

- **Coalesce Neighbors** (default: 0, range: 0-5) — Number of neighboring chunks to include with each search result for additional context. Set to 0 to return only matched chunks.

### Reconciliation Settings (Mutable)

Reconciliation automatically fixes drift between document tags and knowledge base indexes, detecting:
- **Missing documents** — Documents with matching tags that aren't indexed
- **Stale documents** — Indexed documents that no longer have matching tags
- **Orphaned vectors** — Vector embeddings without corresponding documents

- **Reconcile Enabled** (default: false) — Enable automatic periodic reconciliation
- **Reconcile Interval** (minimum: 60 seconds) — How often reconciliation runs when enabled

You can also manually trigger reconciliation at any time from the knowledge base details page.

---

## Managing Knowledge Bases

<div class="grid md:grid-cols-2 gap-6 my-6">
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Creating Knowledge Bases</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;">Go to <strong>Knowledge Bases</strong> in the sidebar, click <strong>New Knowledge Base</strong>, configure indexing settings, and assign tags.</p>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;"><strong>Note:</strong> Indexing settings (chunker type, chunk size, embedding model) cannot be changed after creation.</p>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Automatic Indexing</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Documents with matching tags are automatically indexed into the knowledge base. No manual upload needed — just tag your documents.</p>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Using with Prompts</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">In the prompt editor, select a knowledge base from the dropdown. The AI will automatically use it when processing documents.</p>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Reconciliation</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Enable periodic reconciliation to automatically fix drift between document tags and indexes, or trigger it manually.</p>
  </div>
</div>

---

## Best Practices

<div class="my-6">
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Keep It Focused</strong> — Create separate knowledge bases for different topics (e.g., "Legal Terms" vs "Product Specs").</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Clean Data</strong> — Ensure reference documents are clear, well-formatted, and up-to-date for best results.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Update Regularly</strong> — Keep price lists, catalogs, and reference materials current to maintain accuracy.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Use Markdown for Chat Agents</strong> — When building knowledge bases as a chat agent backend, use documents in Markdown format for better structure and readability.</p>
  <p style="margin: 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Use for Chat</strong> — Knowledge bases can power chat agents, allowing users to ask natural-language questions over your documents.</p>
</div>

---

## Learn More

- <a href="/docs/prompts">Prompts</a> — Link knowledge bases to your extraction prompts
- <a href="/docs/rest-api">REST API</a> — Create and manage knowledge bases programmatically

---

<div class="bg-blue-600 rounded-lg p-8 mt-10 text-center">
  <h2 class="text-2xl font-semibold text-white mb-4">Ready to create your first knowledge base?</h2>
  <a href="https://app.docrouter.ai" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
    Open Dashboard
  </a>
</div>
