---
layout: docs
title: "Document Tags"
permalink: /docs/tags/
---

<div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-8 mb-10 text-center">
  <h2 class="text-2xl font-semibold text-white mb-2">Tags connect documents to prompts</h2>
  <p class="text-blue-100">They are <strong class="text-white">required</strong> for automatic data extraction in DocRouter.AI.</p>
</div>

## Get started in 3 steps

<div class="bg-gray-50 rounded-lg p-6 my-6">
  <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">1</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Create a tag</h3>
      <p style="color: #4b5563; margin: 0;">Set up a category for your document type (e.g., "invoices", "receipts").</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">2</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Create a prompt</h3>
      <p style="color: #4b5563; margin: 0;">Write extraction instructions and <strong>link them to your tag</strong>.</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">3</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Upload documents</h3>
      <p style="color: #4b5563; margin: 0;">Apply the tag during upload to trigger the linked prompt automatically.</p>
    </div>
  </div>
</div>

---

## Managing Tags

<div class="grid md:grid-cols-2 gap-6 my-6">
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Creating Tags</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Go to <strong>Tags</strong> in the sidebar, click <strong>Create Tag</strong>, and assign a name and color.</p>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Assigning Tags</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Select tags during upload, or use <strong>Actions → Edit Tags</strong> for existing documents.</p>
  </div>
</div>

---

## Best Practices

<div class="my-6">
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Be Specific</strong> — Use distinct tags like <code class="bg-gray-100 px-1 rounded">invoice-us</code> vs <code class="bg-gray-100 px-1 rounded">invoice-eu</code> if they need different prompts.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Track Status</strong> — Use tags like <code class="bg-gray-100 px-1 rounded">pending-review</code> or <code class="bg-gray-100 px-1 rounded">approved</code> for workflow stages.</p>
  <p style="margin: 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Stay Consistent</strong> — Standardize naming across your team to keep your workspace organized.</p>
</div>

---
## Learn More

- <a href="/docs/prompts">Prompts</a> — Write extraction instructions that run on tagged documents
- <a href="/docs/schemas">Schemas</a> — Define structured output for your prompts
- <a href="/docs/quick-start">Quick Start</a> — See the full Tag → Prompt → Upload workflow

---

<div class="bg-blue-600 rounded-lg p-8 mt-10 text-center">
  <h2 class="text-2xl font-semibold text-white mb-4">Ready to start tagging?</h2>
  <a href="https://app.docrouter.ai" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
    Open Dashboard
  </a>
</div>
