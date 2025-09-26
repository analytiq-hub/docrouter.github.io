---
layout: page
title: Quick Start Guide
permalink: /quick-start/
---

Get up and running with DocRouter in minutes. This guide walks you through the complete workflow from document upload to automation.

<div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
  <div class="rounded-xl border border-gray-200 bg-white p-6">
    <h2 class="text-2xl font-bold mb-3">Overview</h2>
    <p>DocRouter transforms your document processing workflow through these key steps:</p>
    <ol class="list-decimal pl-5 space-y-2 mt-2">
      <li><strong>Upload</strong> documents (PDFs, images, or text files)</li>
      <li><strong>Tag</strong> documents with labels for organization</li>
      <li><strong>Iterate</strong> on schema and prompt definitions</li>
      <li><strong>Automate</strong> the process using REST APIs or Python SDK</li>
    </ol>
  </div>
  <div class="rounded-xl border border-indigo-200 bg-indigo-50 p-6">
    <h2 class="text-2xl font-bold mb-3">Sample File, Schema and Prompt</h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-1 xl:grid-cols-3 gap-3">
      <a href="/assets/files/Acord80_Homeowners_App.pdf" class="group block rounded-lg border border-gray-200 p-3 hover:shadow-sm hover:border-gray-300 transition bg-white">
        <div class="flex items-center gap-3 min-w-0">
          <span class="inline-flex h-8 w-8 items-center justify-center rounded bg-gray-100 text-gray-700 text-xs">PDF</span>
          <div class="min-w-0">
            <div class="font-medium group-hover:text-blue-700 truncate" title="Acord80_Homeowners_App.pdf">Acord80_Homeowners_App.pdf</div>
            <div class="text-xs text-gray-500">Sample document</div>
          </div>
        </div>
      </a>
      <a href="/assets/files/acord_80_homeowners_app_prompt.txt" class="group block rounded-lg border border-gray-200 p-3 hover:shadow-sm hover:border-gray-300 transition bg-white">
        <div class="flex items-center gap-3 min-w-0">
          <span class="inline-flex h-8 w-8 items-center justify-center rounded bg-gray-100 text-gray-700 text-xs">TXT</span>
          <div class="min-w-0">
            <div class="font-medium group-hover:text-blue-700 truncate" title="acord_80_homeowners_app_prompt.txt">acord_80_homeowners_app_prompt.txt</div>
            <div class="text-xs text-gray-500">Prompt to extract fields</div>
          </div>
        </div>
      </a>
      <a href="/assets/files/acord_80_homeowners_app_schema.json" class="group block rounded-lg border border-gray-200 p-3 hover:shadow-sm hover:border-gray-300 transition bg-white">
        <div class="flex items-center gap-3 min-w-0">
          <span class="inline-flex h-8 w-8 items-center justify-center rounded bg-gray-100 text-gray-700 text-xs">JSON</span>
          <div class="min-w-0">
            <div class="font-medium group-hover:text-blue-700 truncate" title="acord_80_homeowners_app_schema.json">acord_80_homeowners_app_schema.json</div>
            <div class="text-xs text-gray-500">Schema for structured output</div>
          </div>
        </div>
      </a>
    </div>
  </div>
</div>

---

## Step 1: Upload Your First Document

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-start">
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

<div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6 items-start">
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

<div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6 items-start">
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

## Step 2: Configure a Tag, Schema and Prompt

To prevent running all the prompts on all the documents, we use a tag mechanism to assign which prompts run on which documents.

<div class="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6 items-start">
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

<div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6 items-start">
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

<div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6 items-start">
  <div>
    <h4 class="text-lg font-semibold mb-2">Create Schema (JSON Editor)</h4>
    <ol class="list-decimal pl-5 space-y-2">
      <li>Open the <strong>JSON</strong> tab in the schema editor.</li>
      <li>Paste the contents of the downloaded schema file
        (<a href="/assets/files/acord_80_homeowners_app_schema.json" class="text-blue-600 underline">acord_80_homeowners_app_schema.json</a>).
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



## Step 3: Define Schema and Prompts

### Schema Definition

Create a JSON schema to define the structure of data you want to extract:

```json
{
  "type": "object",
  "properties": {
    "invoice_number": {"type": "string"},
    "date": {"type": "string", "format": "date"},
    "vendor": {"type": "string"},
    "total_amount": {"type": "number"},
    "line_items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "description": {"type": "string"},
          "quantity": {"type": "number"},
          "unit_price": {"type": "number"},
          "total": {"type": "number"}
        }
      }
    }
  },
  "required": ["invoice_number", "date", "vendor", "total_amount"]
}
```

### Prompt Engineering

Craft effective prompts for data extraction:

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

## Step 4: Manual Automation

### Batch Processing

Process multiple documents with the same schema:

```python
# Process multiple documents
documents = client.documents.list(tags=["invoice"])

results = []
for doc in documents:
    result = client.documents.extract(
        document_id=doc.id,
        schema=invoice_schema,
        prompt=extraction_prompt
    )
    results.append(result)
```

### Workflow Automation

Create reusable workflows:

```python
# Define a workflow
workflow = client.workflows.create(
    name="Invoice Processing",
    schema=invoice_schema,
    prompt=extraction_prompt,
    tags=["invoice"],
    output_format="json"
)

# Apply workflow to documents
for doc in new_invoices:
    client.workflows.apply(
        workflow_id=workflow.id,
        document_id=doc.id
    )
```

---

## Step 5: Full Automation with APIs

### REST API Automation

Set up automated processing endpoints:

```bash
# Create processing pipeline
curl -X POST https://api.docrouter.ai/v1/pipelines \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Invoice Pipeline",
    "triggers": ["upload", "tag:invoice"],
    "schema": {...},
    "prompt": "Extract invoice data...",
    "webhook_url": "https://yourapp.com/webhook"
  }'
```

### Python SDK Automation

Complete automation workflow:

```python
from docrouter import DocRouter
import json

client = DocRouter(api_key="YOUR_API_KEY")

class InvoiceProcessor:
    def __init__(self):
        self.schema = {...}  # Your invoice schema
        self.prompt = "..."  # Your extraction prompt

    def process_invoice(self, file_path):
        # Upload document
        document = client.documents.upload(
            file_path=file_path,
            tags=["invoice", "auto-processed"]
        )

        # Extract data
        result = client.documents.extract(
            document_id=document.id,
            schema=self.schema,
            prompt=self.prompt
        )

        # Post-process and validate
        return self.validate_and_format(result.data)

    def validate_and_format(self, data):
        # Add custom validation logic
        if not data.get('invoice_number'):
            raise ValueError("Invoice number is required")

        return {
            'document_id': data['document_id'],
            'extracted_data': data,
            'processed_at': datetime.now().isoformat()
        }

# Use the processor
processor = InvoiceProcessor()
result = processor.process_invoice("new_invoice.pdf")
print(json.dumps(result, indent=2))
```

### Webhook Integration

Handle processing results automatically:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_docrouter_webhook():
    data = request.json

    if data['event'] == 'extraction_completed':
        # Process the extracted data
        extracted_data = data['result']['extracted_data']
        document_id = data['document_id']

        # Save to your database, trigger workflows, etc.
        save_to_database(document_id, extracted_data)

    return jsonify({'status': 'received'})
```

---

## Next Steps

1. **Explore Advanced Features**
   - [REST API Documentation](/rest-api)
   - [Python SDK Reference](/python-sdk)
   - [Architecture Overview](/architecture)

2. **Integration Patterns**
   - Set up webhooks for real-time processing
   - Implement error handling and retries
   - Create monitoring and alerting

3. **Scale Your Solution**
   - Batch processing for high volumes
   - Multi-tenant configurations
   - Custom model fine-tuning

---

## Support

- **Documentation**: Comprehensive guides and API references
- **Community**: Join our developer community
- **Support**: Contact our technical support team

Ready to get started? [Launch DocRouter Application](https://app.docrouter.ai) or explore our [REST API](/rest-api) and [Python SDK](/python-sdk) documentation.