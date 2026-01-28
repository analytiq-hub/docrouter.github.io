---
layout: docs
title: "Document Tags"
permalink: /docs/tags/
---

<div class="bg-blue-50 rounded-2xl p-8 mb-12 border border-blue-100 shadow-lg text-center">
  <p class="text-xl text-gray-800 font-semibold mb-2">Tags connect documents to prompts.</p>
  <p class="text-gray-600">They are <strong>required</strong> for automatic data extraction in DocRouter.AI.</p>
</div>

## The Tag-Prompt Workflow

To automate your document processing, follow these three steps:

1.  **Create a Tag**: Define a category (e.g., `invoices` or `contracts`).
2.  **Create a Prompt**: Write extraction instructions and **link them to your tag**.
3.  **Upload Documents**: Apply the tag during upload to trigger the linked prompt automatically.

---

## Managing Tags

### Creating Tags
Navigate to **Tags** in the sidebar, click **Create Tag**, and assign a name and color.

### Assigning Tags
*   **During Upload**: Select tags from the dropdown in the upload dialog.
*   **Existing Docs**: Select documents in your list and use **Actions → Edit Tags**, or edit them individually from the document view.

---

## Best Practices

*   **Be Specific**: Use distinct tags like `invoice-us` vs `invoice-eu` if they need different prompts.
*   **Track Status**: Use tags like `pending-review` or `approved` to manage your document lifecycle.
*   **Stay Consistent**: Standardize naming across your team to keep your workspace organized.

---

<div class="bg-blue-600 rounded-lg shadow-lg p-8 mt-12 text-center">
  <h2 class="text-2xl font-semibold text-white mb-4">Ready to start tagging?</h2>
  <a href="https://app.docrouter.ai" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
    Open Dashboard
  </a>
</div>
