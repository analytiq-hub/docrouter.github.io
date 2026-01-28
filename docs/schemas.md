---
layout: docs
title: "Schemas"
permalink: /docs/schemas/
---

<div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-8 mb-10 text-center">
  <h2 class="text-2xl font-semibold text-white mb-2">Schemas define structured data extraction</h2>
  <p class="text-blue-100">Use JSON schemas to ensure consistent, validated output from your prompts.</p>
</div>

## Get started in 3 steps

<div class="bg-gray-50 rounded-lg p-6 my-6">
  <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">1</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Design your schema</h3>
      <p style="color: #4b5563; margin: 0;">Identify the fields you need to extract and choose appropriate types (string, number, array, object).</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">2</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Create the schema</h3>
      <p style="color: #4b5563; margin: 0;">Use the schema editor or API to define your fields with clear descriptions. All fields are required in strict mode.</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">3</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Link to prompts</h3>
      <p style="color: #4b5563; margin: 0;">Connect your schema to prompts so extracted data matches your defined structure exactly.</p>
    </div>
  </div>
</div>

---

## What are Schemas?

Schemas define the structure and format of data extracted from documents. They use JSON Schema format with strict mode enabled, ensuring 100% adherence to your defined structure.

- **Structured output**: Data is returned in consistent JSON format
- **Type validation**: Fields are validated against defined types
- **Strict mode**: All fields are required, ensuring complete output
- **No post-processing**: Output is immediately usable by your application

---

## Schema Format

Schemas follow OpenAI's Structured Outputs format:

```json
{
  "type": "json_schema",
  "json_schema": {
    "name": "document_extraction",
    "schema": {
      "type": "object",
      "properties": {
        "field_name": {
          "type": "string",
          "description": "Clear description of what to extract"
        }
      },
      "required": ["field_name"],
      "additionalProperties": false
    },
    "strict": true
  }
}
```

**Key requirements:**
- All properties must be in the `required` array
- `additionalProperties: false` must be set at every level
- `strict: true` ensures 100% schema adherence

---

## Field Types

<div class="grid md:grid-cols-2 gap-6 my-6">
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Basic Types</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;"><strong>string</strong> — Text, names, addresses, formatted numbers</p>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;"><strong>number</strong> — Numeric values for calculations</p>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;"><strong>integer</strong> — Whole numbers</p>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;"><strong>boolean</strong> — True/false values</p>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Complex Types</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;"><strong>array</strong> — Lists of items (e.g., line items, skills)</p>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;"><strong>object</strong> — Nested structures (e.g., address, contact info)</p>
  </div>
</div>

---

## Best Practices

<div class="my-6">
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Clear Descriptions</strong> — Write detailed field descriptions that guide the AI on what to extract and expected formats.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Choose Right Types</strong> — Use <code class="bg-gray-100 px-1 rounded">string</code> for formatted values (currency), <code class="bg-gray-100 px-1 rounded">number</code> for calculations.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Keep It Simple</strong> — Use basic types only for maximum portability across LLM providers.</p>
  <p style="margin: 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>All Fields Required</strong> — In strict mode, all fields must be in the <code class="bg-gray-100 px-1 rounded">required</code> array. Missing data returns empty strings or defaults.</p>
</div>

---

## Learn More

- <a href="/docs/prompts">Prompts</a> — Write instructions for data extraction
- <a href="/docs/rest-api">REST API</a> — Create and manage schemas programmatically
- <a href="https://json-schema.org/">JSON Schema Specification</a> — Learn the standard format

---

<div class="bg-blue-600 rounded-lg p-8 mt-10 text-center">
  <h2 class="text-2xl font-semibold text-white mb-4">Ready to create your first schema?</h2>
  <a href="https://app.docrouter.ai" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
    Open Dashboard
  </a>
</div>
