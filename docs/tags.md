---
layout: docs
title: "Document Tags"
permalink: /docs/tags/
---

<div class="bg-blue-50 rounded-2xl p-8 mb-12 border border-blue-100 shadow-lg text-center">
  <p class="text-lg text-gray-600">
    Tag are the core routing mechanism that connects documents to prompts and automates your workflow.
  </p>
</div>

## What are Tags?

Tags are labels that help organize and route documents to the appropriate prompts. In DocRouter.AI, tags are **required** for prompts to trigger on documents. They enable:

- **Automatic processing**: Documents with matching tags trigger specific prompts immediately.
- **Organization**: Group related prompts and documents by type or category.
- **Workflow automation**: Route documents based on their content type (e.g., "invoice", "receipt").

---

## The Tag-Prompt Workflow

The correct onboarding workflow in DocRouter.AI follows these three steps:

1. **Create a Tag**: Set up a category (e.g., `invoices`).
2. **Create a Prompt**: Write instructions and **link it to the tag**.
3. **Upload Documents**: Apply the tag during upload.

Once the upload is complete, the linked prompt will run automatically.

---

## Managing Tags

### Creating a Tag
1. Navigate to **Tags** in the left sidebar.
2. Click **Create Tag**.
3. Enter a descriptive name (e.g., `legal-contracts`).
4. Choose a color for visual organization.
5. Click **Save Tag**.

### Assigning Tags to Documents
- **During Upload**: Select tags from the dropdown in the upload dialog.
- **Bulk Action**: Select multiple documents in the list, click **Actions** → **Edit Tags**.
- **Individual**: Open a document, click the three dots menu → **Edit Tags & Metadata**.

---

## Best Practices

- **Be Specific**: Use tags like `invoice-us` or `invoice-eu` if they require different extraction prompts.
- **Workflow Stages**: Use tags like `pending-review` or `approved` to track document status.
- **Consistency**: Standardize tag naming across your organization to avoid confusion.

---

<div class="bg-blue-600 rounded-lg shadow-lg p-8 mt-12 text-center">
  <h2 class="text-2xl font-semibold text-white mb-4">Ready to start tagging?</h2>
  <a href="https://app.docrouter.ai" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
    Open Dashboard
  </a>
</div>
