---
layout: page
title: Quick Start Guide
permalink: /quick-start/
---

Get up and running with DocRouter in minutes. This guide walks you through the complete workflow from document upload to automation.

## Overview

DocRouter transforms your document processing workflow through these key steps:

1. **Upload** documents (PDFs, images, or text files)
2. **Tag** documents with labels for organization
3. **Iterate** on schema and prompt definitions
4. **Automate** the process using REST APIs or Python SDK

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

## Step 2: Tag Your Documents

### Manual Tagging

1. Select your uploaded document
2. Click **"Add Tags"**
3. Add relevant tags like:
   - `invoice`
   - `Q4-2024`
   - `acme-corp`
   - `high-priority`

### API Tagging

```bash
curl -X POST https://api.docrouter.ai/v1/documents/{document_id}/tags \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tags": ["invoice", "Q4-2024", "acme-corp"]}'
```

### Python SDK Tagging

```python
# Add tags to document
client.documents.add_tags(
    document_id=document.id,
    tags=["invoice", "Q4-2024", "acme-corp"]
)
```

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