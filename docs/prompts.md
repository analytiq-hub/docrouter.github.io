---
layout: docs
title: "Prompts"
permalink: /docs/prompts/
---

<div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-4 md:p-8 mb-6 md:mb-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-2">Prompts guide AI models to extract data</h2>
  <p class="text-sm md:text-base text-blue-100">Write clear instructions that tell the AI what information to extract from your documents.</p>
</div>

## Get started in 3 steps

<div class="bg-gray-50 rounded-lg p-4 md:p-6 my-4 md:my-6">
  <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">1</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Create a prompt</h3>
      <p style="color: #4b5563; margin: 0;">Write clear instructions describing what data to extract from your documents.</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">2</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Associate to tags and schemas</h3>
      <p style="color: #4b5563; margin: 0;">Configure your prompt with <strong>tags</strong> for automatic processing and optionally to a <strong>schema</strong> for structured output.</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">3</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Upload documents</h3>
      <p style="color: #4b5563; margin: 0;">When documents with matching tags are uploaded, the prompt runs automatically and extracts data.</p>
    </div>
  </div>
</div>

---

## What are Prompts?

Prompts are text instructions that guide AI language models to extract specific information from documents. They tell the AI what to look for and how to format the results.

- **Clear instructions**: Describe exactly what data to extract
- **Schema integration**: Optionally link to a schema for structured JSON output
- **Tag-based routing**: Connect to tags so prompts run automatically
- **Model selection**: Choose from OpenAI, Claude, Gemini, and more

---

## Managing Prompts

<div class="grid md:grid-cols-2 gap-4 md:gap-6 my-4 md:my-6">
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Creating Prompts</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Go to <strong>Prompts</strong> in the sidebar, click <strong>Create Prompt</strong>, write your instructions, and link to tags and schemas.</p>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Choosing Models</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Select from <strong>gpt-4o-mini</strong> (default), <strong>Claude</strong>, <strong>Gemini</strong>, or others based on your needs for speed, cost, or complexity.</p>
  </div>
</div>

---

## Best Practices

<div class="my-4 md:my-6">
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Be Specific</strong> — Clearly describe each field to extract, include format requirements, and mention edge cases.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Give Examples and Counter-Examples</strong> — Provide examples of what to extract and clear counter-examples of what to ignore to resolve ambiguity.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Reference Schemas</strong> — When using a schema, mention it in your prompt and highlight important fields.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Use Tags Strategically</strong> — Link prompts to document type tags (e.g., "invoice", "receipt") for automatic processing.</p>
  <p style="margin: 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Monitor and Iterate</strong> — Review extraction results in Operations, identify corner cases, and update prompts to handle them.</p>
</div>

---

## Iteration and Monitoring

To achieve high extraction accuracy, treat prompt engineering as an iterative process.

### Using Examples and Counter-Examples
AI models perform significantly better when they know both what to look for and what to skip.

*   **Positive Example**: "Extract the 'Total Amount' which is the final sum at the bottom of the invoice."
*   **Counter-Example**: "Ignore 'Subtotal' or 'Balance Forward' amounts. Do not extract tax-only line items as the total."

### Handling Corner Cases
As you process more documents, you will encounter edge cases that require specific instructions.

1.  **Monitor Operations**: Regularly check the **Operations** logs to see extraction results for diverse documents.
2.  **Identify Failures**: Look for patterns where the AI misidentified a field or missed information.
3.  **Update Prompts**: Add specific "IF/THEN" logic to handle these cases.
    - *Example*: "If the document is a credit memo instead of an invoice, extract the total as a negative number."
    - *Example*: "When multiple addresses are present, use the 'Remit To' address for the vendor location."
4.  **Bulk Re-run**: Use the **Actions** menu in the document list to re-run your updated prompt on existing documents to verify the fix.

---

## Learn More

- <a href="/docs/schemas">Schemas</a> — Define structured output formats
- <a href="/docs/tags">Tags</a> — Organize documents and trigger prompts automatically
- <a href="/docs/rest-api">REST API</a> — Create and manage prompts programmatically

---

<div class="bg-blue-600 rounded-lg p-4 md:p-8 mt-8 md:mt-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-4">Ready to create your first prompt?</h2>
  <a href="https://app.docrouter.ai" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-4 py-3 md:px-8 md:py-4 rounded-lg font-semibold text-base md:text-lg transition-colors duration-200 no-underline">
    Open Dashboard
  </a>
</div>
