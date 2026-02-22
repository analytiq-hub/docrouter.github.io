---
layout: docs
title: Quick Start Guide
permalink: /docs/quick-start/
---

<div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
  <div class="rounded-xl border border-gray-200 bg-white p-6">
    <h2 class="text-2xl font-bold mb-3">Overview</h2>
    <p>Get up and running with DocRouter in minutes. This guide walks you through the complete workflow from setup to automation. DocRouter transforms your document processing workflow through these key steps:</p>
    <ul class="list-decimal pl-5 space-y-2 mt-2">
      <li><b>Step 1</b> - Create a tag and a prompt</li>
      <li><b>Step 2</b> - Upload your first document with the tag</li>
      <li><b>Step 3</b> - See automatic extraction results</li>
      <li><b>Step 4</b> - Prompt Engineering to improve extraction quality</li>
      <li><b>Step 5</b> - Manual Automation using bulk actions</li>
      <li><b>Step 6</b> - Full Automation with REST API or Python SDK</li>
    </ul>
  </div>
  <div class="rounded-xl border border-blue-200 bg-blue-50 p-6">
    <h2 class="text-2xl font-bold mb-3">Documents You Will Need</h2>
    <div class="grid grid-cols-1 gap-3">
      <a href="/assets/files/Acord80_Homeowners_App.pdf" class="group block rounded-lg border border-gray-200 p-3 hover:shadow-sm hover:border-gray-300 transition bg-white no-underline">
        <div class="flex items-center gap-3 min-w-0">
          <span class="inline-flex h-8 w-8 items-center justify-center rounded bg-gray-100 text-gray-700 text-xs">PDF</span>
          <div class="min-w-0">
            <div class="text-gray-700"><span class="font-bold">Sample Document</span> - A homeowners insurance application form</div>
            <div class="text-xs text-gray-500 truncate" title="Acord80_Homeowners_App.pdf">Acord80_Homeowners_App.pdf</div>
          </div>
        </div>
      </a>
      <a href="/assets/files/acord_clearance_search_prompt.txt" class="group block rounded-lg border border-gray-200 p-3 hover:shadow-sm hover:border-gray-300 transition bg-white no-underline">
        <div class="flex items-center gap-3 min-w-0">
          <span class="inline-flex h-8 w-8 items-center justify-center rounded bg-gray-100 text-gray-700 text-xs">TXT</span>
          <div class="min-w-0">
            <div class="text-gray-700"><span class="font-bold">Sample Prompt</span> - Prompt to extract fields from insurance form</div>
            <div class="text-xs text-gray-500 truncate" title="acord_clearance_search_prompt.txt">acord_clearance_search_prompt.txt</div>
          </div>
        </div>
      </a>
      <a href="/assets/files/acord_clearance_search_schema.json" class="group block rounded-lg border border-gray-200 p-3 hover:shadow-sm hover:border-gray-300 transition bg-white no-underline">
        <div class="flex items-center gap-3 min-w-0">
          <span class="inline-flex h-8 w-8 items-center justify-center rounded bg-gray-100 text-gray-700 text-xs">JSON</span>
          <div class="min-w-0">
            <div class="text-gray-700"><span class="font-bold">Sample Schema</span> - Schema for structured output</div>
            <div class="text-xs text-gray-500 truncate" title="acord_clearance_search_schema.json">acord_clearance_search_schema.json</div>
          </div>
        </div>
      </a>
    </div>
  </div>
</div>

<!-- Progress Indicator -->
<div class="bg-gray-100 rounded-lg p-4 mb-8 sticky top-4 z-10">
  <div class="flex items-center justify-between text-sm">
    <span class="font-medium">Quick Start Progress</span>
    <span class="text-gray-600">Step <span id="current-step">1</span> of 6</span>
  </div>
  <div class="w-full bg-gray-200 rounded-full h-2 mt-2">
    <div id="progress-bar" class="bg-blue-600 h-2 rounded-full transition-all duration-300" style="width: 16.67%"></div>
  </div>
</div>

---

<div class="rounded-lg bg-blue-50 border-l-4 border-blue-500 px-4 py-3 mb-3" id="step-1">
  <div class="flex items-center mb-2">
    <span class="bg-blue-600 text-white text-sm font-bold px-3 py-1 rounded-full mr-3">Step 1</span>
    <span class="text-2xl font-bold text-blue-800">Create a Tag and a Prompt</span>
  </div>
  <p class="text-base text-gray-600 mt-1">We'll set up tags and prompts first so your documents process automatically upon upload.</p>
</div>

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-start bg-white rounded-xl p-4">
  <div>
    <h3 class="text-xl font-semibold mb-3">1. Create a Tag</h3>
    <ol class="list-decimal pl-5 space-y-2">
      <li>Go to <strong>Tags</strong> in the left sidebar.</li>
      <li>Click <strong>Create Tag</strong>.</li>
      <li>Enter a descriptive name (e.g., <code>invoice</code>).</li>
      <li>Click <strong>Save tag</strong>.</li>
    </ol>
  </div>
  <div>
    <img src="/assets/images/create_tag.png" alt="Create Tag dialog" class="w-full rounded-lg shadow-md ring-1 ring-gray-200" />
  </div>
</div>

<div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6 items-start bg-white rounded-xl p-4">
  <div>
    <h3 class="text-xl font-semibold mb-3">2. Create a Prompt</h3>
    <ol class="list-decimal pl-5 space-y-2">
      <li>Go to <strong>Prompts</strong> in the left sidebar.</li>
      <li>Click <strong>Create Prompt</strong>.</li>
      <li>Enter a name and instructions for the AI.</li>
      <li><strong>Crucial:</strong> Assign the tag you just created.</li>
      <li>Click <strong>Save prompt</strong>.</li>
    </ol>
  </div>
  <div>
    <img src="/assets/images/create_prompt.png" alt="Create Prompt screen" class="w-full rounded-lg shadow-md ring-1 ring-gray-200" />
  </div>
</div>

---

<div class="rounded-lg bg-blue-50 border-l-4 border-blue-500 px-4 py-3 mb-3 mt-10" id="step-2">
  <div class="flex items-center mb-2">
    <span class="bg-blue-600 text-white text-sm font-bold px-3 py-1 rounded-full mr-3">Step 2</span>
    <span class="text-2xl font-bold text-blue-800">Upload Your First Document</span>
  </div>
  <p class="text-base text-gray-600 mt-1">Now, upload a file and apply the tag to trigger the prompt.</p>
</div>

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-start bg-white rounded-xl p-4">
  <div>
    <h3 class="text-xl font-semibold mb-3">Manual Upload with Tag</h3>
    <ol class="list-decimal pl-5 space-y-2">
      <li>Click <strong>"Upload Document"</strong>.</li>
      <li>Select your file.</li>
      <li>In the <strong>Tags</strong> dropdown, select the tag you created in Step 1.</li>
      <li>Click <strong>Continue</strong>.</li>
    </ol>
  </div>
  <div>
    <img src="/assets/images/upload_file.png" alt="Upload Documents screen" class="w-full rounded-lg shadow-md ring-1 ring-gray-200" />
  </div>
</div>

---

<div class="rounded-lg bg-blue-50 border-l-4 border-blue-500 px-4 py-3 mb-3 mt-10" id="step-3">
  <div class="flex items-center mb-2">
    <span class="bg-blue-600 text-white text-sm font-bold px-3 py-1 rounded-full mr-3">Step 3</span>
    <span class="text-2xl font-bold text-blue-800">See Automatic Extraction Results</span>
  </div>
  <p class="text-base text-gray-600 mt-1">Wait for processing to complete and view your data.</p>
</div>

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-start bg-white rounded-xl p-4">
  <div>
    <h3 class="text-xl font-semibold mb-3">Review Extractions</h3>
    <ol class="list-decimal pl-5 space-y-2">
      <li>Wait for status <code>llm_completed</code>.</li>
      <li>Click the document name.</li>
      <li>Go to the <strong>Extractions</strong> tab to see structured data.</li>
    </ol>
  </div>
  <div>
    <img src="/assets/images/extractions2.png" alt="Extractions results view" class="w-full rounded-lg shadow-md ring-1 ring-gray-200" />
  </div>
</div>

---

<div class="rounded-lg bg-blue-50 border-l-4 border-blue-500 px-4 py-3 mb-3 mt-10" id="step-4">
  <div class="flex items-center mb-2">
    <span class="bg-blue-600 text-white text-sm font-bold px-3 py-1 rounded-full mr-3">Step 4</span>
    <span class="text-2xl font-bold text-blue-800">Prompt Engineering</span>
  </div>
  <p class="text-base text-gray-600 mt-1">We'll refine our prompts to get better and more accurate results.</p>
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

<div class="rounded-lg bg-blue-50 border-l-4 border-blue-500 px-4 py-3 mb-3 mt-10" id="step-5">
  <div class="flex items-center mb-2">
    <span class="bg-blue-600 text-white text-sm font-bold px-3 py-1 rounded-full mr-3">Step 5</span>
    <span class="text-2xl font-bold text-blue-800">Manual Automation</span>
  </div>
  <p class="text-base text-gray-600 mt-1">We'll process multiple documents at once to handle larger volumes.</p>
</div>

<div class="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6 items-start bg-white rounded-xl p-4">
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

<div class="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6 items-start bg-white rounded-xl p-4">
  <div>
    <h4 class="text-lg font-semibold mb-2">Update prompts and re-run on documents at scale</h4>
    <ol class="list-decimal pl-5 space-y-2">
      <li>Open the <strong>Documents</strong> list and filter by the tag used by your prompt.</li>
      <li>Click <strong>Actions</strong> → <strong>Run LLM</strong>.</li>
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

<div class="rounded-lg bg-blue-50 border-l-4 border-blue-500 px-4 py-3 mb-3 mt-10" id="step-6">
  <div class="flex items-center mb-2">
    <span class="bg-blue-600 text-white text-sm font-bold px-3 py-1 rounded-full mr-3">Step 6</span>
    <span class="text-2xl font-bold text-blue-800">Full Automation with APIs</span>
  </div>
  <p class="text-base text-gray-600 mt-1">We'll connect DocRouter to your systems for fully automated processing.</p>
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

For more details, see - [REST API Documentation](/docs/rest-api).

### Python SDK Automation

Refer to the [Python SDK Reference](/docs/python-sdk).

## Learn More

- <a href="/docs/tags">Tags</a> — Required routing mechanism that connects uploads to prompts
- <a href="/docs/prompts">Prompts</a> — Author extraction instructions for your documents
- <a href="/docs/schemas">Schemas</a> — Define structured JSON output for extractions
- <a href="/docs/document-agent">Document Agent</a> - Configure schemas, tags, and prompts with AI
- <a href="/docs/knowledge-bases">Knowledge Bases</a> — Add reference context and power Knowledge Base Chat
- <a href="/docs/chat-agents">Knowledge Base Chat</a> — Chat over your knowledge bases

---

<script>
// Interactive Progress Indicator
document.addEventListener('DOMContentLoaded', function() {
  const progressBar = document.getElementById('progress-bar');
  const currentStepSpan = document.getElementById('current-step');
  const steps = ['step-1', 'step-2', 'step-3', 'step-4', 'step-5', 'step-6'];
  
  function updateProgress() {
    let currentStep = 1;
    
    // Find the step that's most prominently in view
    steps.forEach((stepId, index) => {
      const element = document.getElementById(stepId);
      if (element) {
        const rect = element.getBoundingClientRect();
        const stepTop = rect.top;
        const stepBottom = rect.bottom;
        const viewportCenter = window.innerHeight * 0.5;
        
        // If step is above the center of viewport, we've passed it
        if (stepBottom < viewportCenter) {
          currentStep = index + 1;
        }
        // If step is in the center area of viewport, it's the current step
        else if (stepTop <= viewportCenter && stepBottom >= viewportCenter) {
          currentStep = index + 1;
        }
      }
    });
    
    // Update progress bar and current step
    const progress = (currentStep / 6) * 100;
    progressBar.style.width = progress + '%';
    currentStepSpan.textContent = currentStep;
  }
  
  // Update progress on scroll
  window.addEventListener('scroll', updateProgress);
  
  // Update progress on page load
  updateProgress();
});
</script>
