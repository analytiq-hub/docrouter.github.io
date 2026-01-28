---
layout: docs
title: "Knowledge Bases"
permalink: /docs/knowledge-bases/
---

<div class="bg-blue-50 rounded-2xl p-8 mb-12 border border-blue-100 shadow-lg text-center">
  <h1 class="text-4xl font-bold text-gray-900 mb-4">Knowledge Bases</h1>
  <p class="text-lg text-gray-600">
    Enhance extraction accuracy by providing the AI with context from your own documentation and reference materials.
  </p>
</div>

## What is a Knowledge Base?

A Knowledge Base (KB) in DocRouter.AI is a collection of reference documents that the AI can "read" before processing your files. This is particularly useful for:

- **Industry Jargon**: Teaching the AI specific terms used in your business.
- **Reference Tables**: Providing price lists, SKU catalogs, or vendor IDs.
- **Complex Rules**: Giving the AI a set of guidelines for how to interpret specific document sections.

---

## How it Works

When you associate a Knowledge Base with a prompt, DocRouter uses **RAG (Retrieval-Augmented Generation)** to find the most relevant parts of your KB and includes them in the AI's context window.

1. **Upload KB Documents**: Add PDFs, TXT, or Markdown files to your Knowledge Base.
2. **Link to Prompt**: In the prompt editor, select the Knowledge Base you want to use.
3. **Process**: When the prompt runs, the AI uses the KB to improve its answers.

---

## Creating a Knowledge Base

1. Go to **Knowledge Bases** in the sidebar.
2. Click **New Knowledge Base**.
3. Give it a name (e.g., `Vendor-Price-List-2026`).
4. Upload your reference files.
5. Wait for the status to become `ready` (this means the files have been indexed).

---

## Best Practices

- **Keep it Focused**: Create separate Knowledge Bases for different topics (e.g., one for "Legal Terms", another for "Product Specs").
- **Clean Data**: Ensure your reference documents are clear and well-formatted.
- **Update Regularly**: Keep your price lists and catalogs up to date for the best results.

---

<div class="bg-blue-600 rounded-lg shadow-lg p-8 mt-12 text-center">
  <h2 class="text-2xl font-semibold text-white mb-4">Improve your extractions today</h2>
  <a href="https://app.docrouter.ai" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
    Create Knowledge Base
  </a>
</div>
