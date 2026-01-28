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
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Link to prompts</h3>
      <p style="color: #4b5563; margin: 0;">Select the knowledge base in your prompt editor. The AI will use it automatically when processing documents.</p>
    </div>
  </div>
</div>

---

## What are Knowledge Bases?

Knowledge bases are collections of reference documents that help the AI understand your specific terminology, rules, and context. They use RAG (Retrieval-Augmented Generation) to find relevant information and include it in the AI's context.

- **Better accuracy**: AI uses your reference materials to improve extraction
- **Industry terminology**: Teach the AI specific terms used in your business
- **Reference data**: Provide price lists, SKU catalogs, vendor IDs, or guidelines
- **Chat agents**: Use knowledge bases as the backend for chat agents so users can ask questions over your documents

---

## Managing Knowledge Bases

<div class="grid md:grid-cols-2 gap-6 my-6">
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Creating Knowledge Bases</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Go to <strong>Knowledge Bases</strong> in the sidebar, click <strong>New Knowledge Base</strong>, name it, and upload your reference files.</p>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Using with Prompts</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">In the prompt editor, select a knowledge base from the dropdown. The AI will automatically use it when processing documents.</p>
  </div>
</div>

---

## Best Practices

<div class="my-6">
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Keep It Focused</strong> — Create separate knowledge bases for different topics (e.g., "Legal Terms" vs "Product Specs").</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Clean Data</strong> — Ensure reference documents are clear, well-formatted, and up-to-date for best results.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Update Regularly</strong> — Keep price lists, catalogs, and reference materials current to maintain accuracy.</p>
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
