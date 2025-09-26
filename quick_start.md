---
layout: docs
title: Quick Start Guide
permalink: /quick-start/
---

Get up and running with DocRouter in minutes. This guide walks you through the complete workflow from document upload to automation.

<div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
  <div class="rounded-xl border border-gray-200 bg-white p-6">
    <h2 class="text-2xl font-bold mb-3">Overview</h2>
    <p>DocRouter transforms your document processing workflow through these key steps:</p>
    <ol class="list-decimal pl-5 space-y-2 mt-2">
      <li><strong>Upload</strong> your first document</li>
      <li><strong>Configure</strong> a tag, schema, and prompt</li>
      <li><strong>Run</strong> the prompt on tagged document(s)</li>
      <li><strong>Prompt Engineering</strong> to improve extraction quality</li>
      <li><strong>Manual Automation</strong> using bulk actions</li>
      <li><strong>Full Automation</strong> with REST API or Python SDK</li>
    </ol>
  </div>
  <div class="rounded-xl border border-indigo-200 bg-indigo-50 p-6">
    <h2 class="text-2xl font-bold mb-3">Sample File, Schema and Prompt</h2>
    <div class="grid grid-cols-1 gap-3">
      <a href="/assets/files/Acord80_Homeowners_App.pdf" class="group block rounded-lg border border-gray-200 p-3 hover:shadow-sm hover:border-gray-300 transition bg-white">
        <div class="flex items-center gap-3 min-w-0">
          <span class="inline-flex h-8 w-8 items-center justify-center rounded bg-gray-100 text-gray-700 text-xs">PDF</span>
          <div class="min-w-0">
            <div class="font-medium group-hover:text-blue-700 truncate" title="Acord80_Homeowners_App.pdf">Acord80_Homeowners_App.pdf</div>
            <div class="text-xs text-gray-500">Sample document</div>
          </div>
        </div>
      </a>
      <a href="/assets/files/acord_clearance_search_prompt.txt" class="group block rounded-lg border border-gray-200 p-3 hover:shadow-sm hover:border-gray-300 transition bg-white">
        <div class="flex items-center gap-3 min-w-0">
          <span class="inline-flex h-8 w-8 items-center justify-center rounded bg-gray-100 text-gray-700 text-xs">TXT</span>
          <div class="min-w-0">
            <div class="font-medium group-hover:text-blue-700 truncate" title="acord_clearance_search_prompt.txt">acord_clearance_search_prompt.txt</div>
            <div class="text-xs text-gray-500">Prompt to extract fields</div>
          </div>
        </div>
      </a>
      <a href="/assets/files/acord_clearance_search_schema.json" class="group block rounded-lg border border-gray-200 p-3 hover:shadow-sm hover:border-gray-300 transition bg-white">
        <div class="flex items-center gap-3 min-w-0">
          <span class="inline-flex h-8 w-8 items-center justify-center rounded bg-gray-100 text-gray-700 text-xs">JSON</span>
          <div class="min-w-0">
            <div class="font-medium group-hover:text-blue-700 truncate" title="acord_clearance_search_schema.json">acord_clearance_search_schema.json</div>
            <div class="text-xs text-gray-500">Schema for structured output</div>
          </div>
        </div>
      </a>
    </div>
  </div>
</div>

---

<div class="rounded-lg bg-indigo-50 border border-indigo-200 px-4 py-3 mb-3">
  <span class="text-2xl font-bold text-indigo-800" role="heading" aria-level="2">Step 1: Upload Your First Document</span>
  <p class="text-sm text-gray-600 mt-1">Start by uploading a file and verifying it processed.</p>
</div>

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-start bg-gray-100 rounded-xl p-4">
  <div>
    <h3 class="text-xl font-semibold mb-3">Manual Upload via Web Interface</h3>
    <ol class="list-decimal pl-5 space-y-2">
      <li>
        Navigate to <a href="https://app.docrouter.ai" class="text-blue-600 underline">app.docrouter.ai</a>
      </li>
      <li>
        Click <strong>"Upload Document"</strong> or drag and drop your file
      </li>
      <li>
        Supported formats:
        <div class="mt-2 flex flex-wrap gap-2">
          <span class="px-2 py-1 rounded bg-gray-100 text-gray-800 text-sm">PDF</span>
          <span class="px-2 py-1 rounded bg-gray-100 text-gray-800 text-sm">DOC</span>
          <span class="px-2 py-1 rounded bg-gray-100 text-gray-800 text-sm">XLS</span>
          <span class="px-2 py-1 rounded bg-gray-100 text-gray-800 text-sm">CSV</span>
          <span class="px-2 py-1 rounded bg-gray-100 text-gray-800 text-sm">TXT</span>
          <span class="px-2 py-1 rounded bg-gray-100 text-gray-800 text-sm">PNG</span>
          <span class="px-2 py-1 rounded bg-gray-100 text-gray-800 text-sm">JPG</span>
        </div>
      </li>
      <li>
        Skip tag or metadata assignment. Wait for the upload confirmation.
      </li>
    </ol>
  </div>
  <div>
    <img src="/assets/images/upload_file.png" alt="Upload Documents screen with drag-and-drop area and Continue button" class="w-full rounded-lg shadow-md ring-1 ring-gray-200" />
    <p class="text-sm text-gray-500 mt-2">Upload screen: drag-and-drop files, then select Continue.</p>
  </div>
</div>

<div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6 items-start rounded-xl p-4">
  <div>
    <h3 class="text-xl font-semibold mb-3">Verify Processing in Document List</h3>
    <ol class="list-decimal pl-5 space-y-2">
      <li>Open the <strong>Documents</strong> list from the left sidebar.</li>
      <li>Wait until your document status becomes <code>llm_completed</code>.</li>
      <li>Click the <strong>document name</strong> to open and view the results.</li>
    </ol>
  </div>
  <div>
    <img src="/assets/images/document_list.png" alt="Document list view highlighting status and document link" class="w-full rounded-lg shadow-md ring-1 ring-gray-200" />
    <p class="text-sm text-gray-500 mt-2">Documents list: wait for status <code>llm_completed</code>, then open the document.</p>
  </div>
</div>

<div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6 items-start bg-gray-100 rounded-xl p-4">
  <div>
    <h3 class="text-xl font-semibold mb-3">Review the Document</h3>
    <ol class="list-decimal pl-5 space-y-2">
      <li>On the document page, use the viewer to page through the file.</li>
      <li>Initially, only a Document Summary is extracted.</li>
    </ol>
  </div>
  <div>
    <img src="/assets/images/document_show1.png" alt="Document viewer screen for reviewing extracted data" class="w-full rounded-lg shadow-md ring-1 ring-gray-200" />
    <p class="text-sm text-gray-500 mt-2">Document review: navigate pages and inspect extracted fields.</p>
  </div>
</div>

---

<div class="rounded-lg bg-indigo-50 border border-indigo-200 px-4 py-3 mb-3 mt-10">
  <span class="text-2xl font-bold text-indigo-800" role="heading" aria-level="2">Step 2: Configure a Tag, Schema and Prompt</span>
  <p class="text-sm text-gray-600 mt-1">To prevent running all the prompts on all the documents, we use a tag mechanism to assign which prompts run on which documents.
</p>
</div>

<div class="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6 items-start bg-gray-100 rounded-xl p-4">
  <div>
    <h4 class="text-lg font-semibold mb-2">Create a Tag</h4>
    <ol class="list-decimal pl-5 space-y-2">
      <li>Go to <strong>Tags</strong> in the left sidebar.</li>
      <li>Click <strong>Create Tag</strong>.</li>
      <li>Enter a descriptive tag name (e.g., <code>invoice</code>).</li>
      <li>Click <strong>Save tag</strong>.</li>
    </ol>
  </div>
  <div>
    <img src="/assets/images/create_tag.png" alt="Create Tag dialog showing tag name input" class="w-full rounded-lg shadow-md ring-1 ring-gray-200" />
    <p class="text-sm text-gray-500 mt-2">Create a new tag to scope which prompts run on which documents.</p>
  </div>
</div>

<div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6 items-start rounded-xl p-4">
  <div>
    <h4 class="text-lg font-semibold mb-2">Create Schema (Drag & Drop)</h4>
    <ol class="list-decimal pl-5 space-y-2">
      <li>Go to <strong>Schemas</strong> in the left sidebar.</li>
      <li>Click <strong>Create Schema</strong>.</li>
      <li>Set schema name</li>
      <li>Add schema elements.</li>
    </ol>
    Schema elements can be of <strong>String, Integer, Float, Boolean, Object, Array</strong> type. Each element has an optional description, aiding the LLM detection. <strong>Object</strong> and <strong>Array</strong> can have embedded elements.
  </div>
  <div>
    <img src="/assets/images/create_schema1.png" alt="Create Schema screen showing drag-and-drop area" class="w-full rounded-lg shadow-md ring-1 ring-gray-200" />
    <p class="text-sm text-gray-500 mt-2">Use drag-and-drop to start a schema from a sample document.</p>
  </div>
</div>

<div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6 items-start bg-gray-100 rounded-xl p-4">
  <div>
    <h4 class="text-lg font-semibold mb-2">Create Schema (JSON Editor)</h4>
    <ol class="list-decimal pl-5 space-y-2">
      <li>Open the <strong>JSON</strong> tab in the schema editor.</li>
      <li>Paste the contents of the downloaded schema file
        (<a href="/assets/files/acord_clearance_search_schema.json" class="text-blue-600 underline">acord_clearance_search_schema.json</a>).
      </li>
      <li>Click <strong>Save Schema</strong>.</li>
    </ol>
  </div>
  <div>
    <img src="/assets/images/create_schema2.png" alt="Schema JSON editor with pasted schema" class="w-full rounded-lg shadow-md ring-1 ring-gray-200" />
    <p class="text-sm text-gray-500 mt-2">Paste the JSON schema and save.</p>
  </div>
</div>


---


<div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6 items-start">
  <div>
    <h4 class="text-lg font-semibold mb-2">Create a Prompt</h4>
    <ol class="list-decimal pl-5 space-y-2">
      <li>Go to <strong>Prompts</strong> in the left sidebar.</li>
      <li>Create a new prompt.</li>
      <li>Paste the contents of the downloaded prompt file
        (<a href="/assets/files/acord_clearance_search_prompt.txt" class="text-blue-600 underline">acord_clearance_search_prompt.txt</a>).</li>
      <li>Assign the <strong>schema</strong> and <strong>tag</strong> you created so it runs only on the intended documents.</li>
      <li>Select one of the <strong>language models</strong> available. <strong>Gemini 2.5 Flash</strong> and <strong>GPT 4.0 Mini</strong> are good choices for simple document layouts.</li>
    </ol>
  </div>
  <div class="max-h-[520px] overflow-auto">
    <img src="/assets/images/create_prompt.png" alt="Prompt selection screen" class="w-full h-auto rounded-lg shadow-md ring-1 ring-gray-200 object-contain" />
    <p class="text-sm text-gray-500 mt-2">Select or create a prompt and align it with your tag.</p>
  </div>
</div>


<div class="rounded-lg bg-indigo-50 border border-indigo-200 px-4 py-3 mb-3 mt-10">
  <span class="text-2xl font-bold text-indigo-800" role="heading" aria-level="2">Step 3: Run The Prompt On The Tagged Document(s)</span>
  <p class="text-sm text-gray-600 mt-1">If a document is tagged at upload time, all prompts with that tag will be run automatically. However, if a prompt is added, updated or tagged after the document has been uploaded, the prompt will need to be manually run on the matching documents.</p>
  <p class="text-sm text-gray-600 mt-1">A separate mechanism, using file <strong>Actions</strong>, is available to run a new prompt in bulk on all matching documents that already exist.</p>
</div>

<div class="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6 items-start bg-gray-100 rounded-xl p-4">
  <div>
    <h4 class="text-lg font-semibold mb-2">Assign Tag to Existing Document</h4>
    <ol class="list-decimal pl-5 space-y-2">
      <li>Open the <strong>Documents</strong> list.</li>
      <li>Click the document three dots action menu, and select <strong>Edit Tags & Metadata</strong>.</li>
      <li>Add the tag linked to your prompt and save.</li>
    </ol>
    Tags can be assigned in bulk, and LLMs can be run in bulk using the <strong>Actions</strong> button.
  </div>
  <div class="max-h-[520px] overflow-auto">
    <img src="/assets/images/assign_tag_to_doc.png" alt="Assign tag to document UI" class="w-full h-auto rounded-lg shadow-md ring-1 ring-gray-200 object-contain" />
    <p class="text-sm text-gray-500 mt-2">Tag existing documents to trigger the correct prompts.</p>
  </div>
</div>

<div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6 items-start rounded-xl p-4">
  <div>
    <h4 class="text-lg font-semibold mb-2">Run Prompt on Document</h4>
    <ol class="list-decimal pl-5 space-y-2">
      <li>Open the document, and switch to the <strong>Extractions</strong> tab.</li>
      <li>Click spinner to (re)run prompt.</li>
      <li>Review extraction.</li>
      <li>Refine prompt, schema then re-run on similar documents to improve quality</li>
      <li>Optionally edit result, clicking on pencil icon.</li>
      <li>Export JSON or copy values into your workflow.</li>
    </ol>
  </div>
  <div class="max-h-[520px] overflow-auto">
    <img src="/assets/images/extractions2.png" alt="Extractions results view" class="w-full h-auto rounded-lg shadow-md ring-1 ring-gray-200 object-contain" />
    <p class="text-sm text-gray-500 mt-2">The Extractions tab shows structured results for your schema.</p>
  </div>
</div>

---


<div class="rounded-lg bg-indigo-50 border border-indigo-200 px-4 py-3 mb-3 mt-10">
  <span class="text-2xl font-bold text-indigo-800" role="heading" aria-level="2">Step 4. Prompt Engineering</span>
  <p class="text-sm text-gray-600 mt-1">Iterate on prompts to improve extraction quality.</p>
</div>

```text
Extract the following information from this invoice:
- Invoice number
- Invoice date (format: YYYY-MM-DD)
- Vendor/supplier name
- Total amount
- All line items with descriptions, quantities, unit prices, and totals

Format the response as JSON matching the provided schema.
Be precise with numbers and dates.
```

### Testing and Iteration

1. **Test with sample documents**
2. **Review extracted data quality**
3. **Refine schema and prompts**
4. **Repeat until accuracy meets requirements**

---

<div class="rounded-lg bg-indigo-50 border border-indigo-200 px-4 py-3 mb-3 mt-10">
  <span class="text-2xl font-bold text-indigo-800" role="heading" aria-level="2">Step 5: Manual Automation</span>
  <p class="text-sm text-gray-600 mt-1">Leverage bulk uploads and actions for scale.</p>
</div>

<div class="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6 items-start bg-gray-100 rounded-xl p-4">
  <div>
    <h4 class="text-lg font-semibold mb-2">Upload pre-tagged documents at scale</h4>
    <ol class="list-decimal pl-5 space-y-2">
      <li>Setting the document tag at upload time</li>
      <li>Prompts matching the tag will run automatically.</li>
    </ol>
  </div>
  <div class="max-h-[520px] overflow-auto">
    <img src="/assets/images/upload_files_bulk.png" alt="Bulk upload with tags assigned" class="w-full h-auto rounded-lg shadow-md ring-1 ring-gray-200 object-contain" />
    <p class="text-sm text-gray-500 mt-2">Upload many files at once and apply tags so prompts run automatically.</p>
  </div>
</div>

<div class="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6 items-start rounded-xl p-4">  <div>
    <h4 class="text-lg font-semibold mb-2">Update prompts and re-run on documents at scale</h4>
    <ol class="list-decimal pl-5 space-y-2">
      <li>Open the <strong>Documents</strong> list and filter by the tag used by your prompt.</li>
      <li>Click <strong>Actions</strong> → <strong>Run Prompt</strong>.</li>
      <li>Select the updated prompt and confirm to run across all filtered documents.</li>
      <li>Monitor progress; re-run as you iterate on prompt or schema.</li>
    </ol>
  </div>
  <div class="max-h-[520px] overflow-auto">
    <img src="/assets/images/bulk_actions.png" alt="Bulk actions to run prompt on many documents" class="w-full h-auto rounded-lg shadow-md ring-1 ring-gray-200 object-contain" />
    <p class="text-sm text-gray-500 mt-2">Use bulk Actions to apply an updated prompt to many documents at once.</p>
  </div>
</div>

---

<div class="rounded-lg bg-indigo-50 border border-indigo-200 px-4 py-3 mb-3 mt-10">
  <span class="text-2xl font-bold text-indigo-800" role="heading" aria-level="2">Step 6: Full Automation with APIs</span>
  <p class="text-sm text-gray-600 mt-1">Automate end-to-end with REST API or Python SDK.</p>
</div>

### REST API Automation

DocRouter provides REST endpoints for automated document processing. Here are the key operations:

#### 1. Upload Documents with Tags

```bash
# Upload documents with tags for automatic processing
curl -X POST https://api.docrouter.ai/v0/orgs/YOUR_ORG_ID/documents \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "documents": [{
      "name": "fi.pdf",
      "content": "BASE64_ENCODED_CONTENT",
      "tag_ids": ["invoice_tag_id"],
      "metadata": {"source": "api_upload"}
    }]
  }'
```

#### 2. List Documents and Check Status

```bash
# List documents with filtering
curl -X GET "https://api.docrouter.ai/v0/orgs/YOUR_ORG_ID/documents?skip=0&limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY"

# Get specific document details
curl -X GET https://api.docrouter.ai/v0/orgs/YOUR_ORG_ID/documents/DOCUMENT_ID \
  -H "Authorization: Bearer YOUR_API_KEY"
```

#### 3. Retrieve Extraction Results

```bash
# Get LLM extraction results (wait for state: "llm_completed")
curl -X GET https://api.docrouter.ai/v0/orgs/YOUR_ORG_ID/llm/result/DOCUMENT_ID \
  -H "Authorization: Bearer YOUR_API_KEY"

# Download all results for a document
curl -X GET https://api.docrouter.ai/v0/orgs/YOUR_ORG_ID/llm/results/DOCUMENT_ID/download \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Document Processing States:**
- `uploaded`: Document uploaded, OCR pending
- `ocr_processing`: OCR in progress
- `ocr_completed`: OCR complete, LLM processing pending
- `llm_processing`: LLM extraction in progress
- `llm_completed`: All processing complete, results available
- `llm_failed`: Processing failed

For more details, see - [REST API Documentation](/rest-api).

### Python SDK Automation

Refer to the [Python SDK Reference](/python-sdk).

---

For **Support**: Contact our technical support team.

Ready to get started? [Launch DocRouter Application](https://app.docrouter.ai) or explore our [REST API](/rest-api) and [Python SDK](/python-sdk) documentation.