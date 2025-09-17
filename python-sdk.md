---
layout: default
title: "DocRouter Python SDK"
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <header class="text-center md:mb-12 mb-4">
        <h1 class="text-4xl font-bold text-gray-900 mb-4 hidden sm:block">DocRouter Python SDK</h1>
        <div class="text-xl text-gray-600">
            <p class="mb-2">Python client library for interacting with docrouter.ai</p>
        </div>
    </header>

    <main>
        <section id="overview" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Overview</h2>
            <p class="text-gray-600 mb-6">
                The DocRouter Python SDK provides a simple and powerful way to interact with the DocRouter API.
                It enables programmatic access to your documents, OCR data, LLM analysis, schemas, prompts, and tags.
            </p>
            <p class="text-gray-600 mb-6">
                This SDK makes it easy to integrate DocRouter's document processing capabilities into your Python applications,
                allowing you to automate document workflows and extract structured data from your documents.
            </p>
        </section>

        <section id="installation" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Installation</h2>
            <p class="text-gray-600 mb-6">You can install the DocRouter SDK directly from GitHub:</p>

            <pre><code>pip install git+https://github.com/analytiq-hub/doc-router.git#subdirectory=packages</code></pre>

            <p class="text-gray-600 mt-6 mb-6">Alternatively, you can clone the repository and install in development mode:</p>

            <pre><code>git clone https://github.com/analytiq-hub/doc-router.git
cd doc-router/packages
pip install -e .</code></pre>
        </section>

        <section id="quickstart" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Quick Start</h2>

            <p class="text-gray-600 mb-4">To get started with the DocRouter SDK:</p>

            <ol class="list-decimal list-inside text-gray-600 space-y-2 mb-6">
                <li>Get your DocRouter organization ID from the URL, e.g. <code class="bg-gray-100 px-2 py-1 rounded">https://app.docrouter.ai/orgs/&lt;docrouter_org_id&gt;</code></li>
                <li>Create an organization API token from your organization settings</li>
                <li>Initialize the client and start making API calls</li>
            </ol>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Basic Usage</h3>

            <pre><code>from docrouter_sdk import DocRouterClient

# Initialize the client
client = DocRouterClient(
    base_url="https://app.docrouter.ai/fastapi",  # Replace with your API URL
    api_token="your_org_api_token"               # Replace with your API token
)

# Example: List documents
organization_id = "your_organization_id"  # Replace with your organization ID
documents = client.documents.list(organization_id)
print(f"Found {documents.total_count} documents")

# Example: List tags
tags = client.tags.list(organization_id)
print(f"Found {tags.total_count} tags")

# Example: List available LLM models
models = client.llm.list_models()
print(f"Available LLM models: {[model.name for model in models.models]}")</code></pre>
        </section>

        <section id="modules" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-6">SDK Modules</h2>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="border rounded-lg p-6 shadow-sm">
                    <h3 class="text-xl font-semibold text-gray-900 mb-3">Documents API</h3>
                    <p class="text-gray-600 mb-4">Manage documents in your workspace</p>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>List documents with optional filtering</li>
                        <li>Upload new documents</li>
                        <li>Get document details</li>
                        <li>Update document properties</li>
                        <li>Delete documents</li>
                    </ul>
                </div>

                <div class="border rounded-lg p-6 shadow-sm">
                    <h3 class="text-xl font-semibold text-gray-900 mb-3">OCR API</h3>
                    <p class="text-gray-600 mb-4">Access document OCR data</p>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>Get OCR text from documents</li>
                        <li>Get OCR text for specific pages</li>
                        <li>Get OCR blocks with position data</li>
                        <li>Access document OCR metadata</li>
                    </ul>
                </div>

                <div class="border rounded-lg p-6 shadow-sm">
                    <h3 class="text-xl font-semibold text-gray-900 mb-3">LLM API</h3>
                    <p class="text-gray-600 mb-4">Run and manage LLM analysis</p>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>List available LLM models</li>
                        <li>Run LLM analysis on documents</li>
                        <li>Get LLM extraction results</li>
                        <li>Update and verify extraction results</li>
                        <li>Delete LLM results</li>
                    </ul>
                </div>

                <div class="border rounded-lg p-6 shadow-sm">
                    <h3 class="text-xl font-semibold text-gray-900 mb-3">Schemas API</h3>
                    <p class="text-gray-600 mb-4">Manage extraction schemas</p>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>Create new extraction schemas</li>
                        <li>List existing schemas</li>
                        <li>Get schema details</li>
                        <li>Update schemas</li>
                        <li>Delete schemas</li>
                        <li>Validate data against schemas</li>
                    </ul>
                </div>

                <div class="border rounded-lg p-6 shadow-sm">
                    <h3 class="text-xl font-semibold text-gray-900 mb-3">Prompts API</h3>
                    <p class="text-gray-600 mb-4">Manage extraction prompts</p>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>Create new prompts</li>
                        <li>List existing prompts</li>
                        <li>Get prompt details</li>
                        <li>Update prompts</li>
                        <li>Delete prompts</li>
                    </ul>
                </div>

                <div class="border rounded-lg p-6 shadow-sm">
                    <h3 class="text-xl font-semibold text-gray-900 mb-3">Tags API</h3>
                    <p class="text-gray-600 mb-4">Manage document tags</p>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>Create new tags</li>
                        <li>List existing tags</li>
                        <li>Update tags</li>
                        <li>Delete tags</li>
                    </ul>
                </div>
            </div>
        </section>

        <section id="examples" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Code Examples</h2>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Documents API</h3>
            <pre><code># List documents
documents = client.documents.list(organization_id, skip=0, limit=10, tag_ids=["tag1", "tag2"])

# Get a document
document = client.documents.get(organization_id, document_id)

# Update a document
client.documents.update(organization_id, document_id, document_name="New Name", tag_ids=["tag1"])

# Delete a document
client.documents.delete(organization_id, document_id)

# Upload a document
import base64
with open("sample.pdf", "rb") as f:
    content = base64.b64encode(f.read()).decode("utf-8")

result = client.documents.upload(organization_id, [{
    "name": "sample.pdf",
    "content": content,
    "tag_ids": []
}])</code></pre>

            <h3 class="text-lg font-medium text-gray-900 mt-6 mb-3">OCR API</h3>
            <pre><code># Get OCR blocks
blocks = client.ocr.get_blocks(organization_id, document_id)

# Get OCR text
text = client.ocr.get_text(organization_id, document_id, page_num=1)

# Get OCR metadata
metadata = client.ocr.get_metadata(organization_id, document_id)
print(f"Number of pages: {metadata.n_pages}")</code></pre>

            <h3 class="text-lg font-medium text-gray-900 mt-6 mb-3">LLM API</h3>
            <pre><code># List LLM models
models = client.llm.list_models()

# Run LLM analysis
result = client.llm.run(organization_id, document_id, prompt_id="default", force=False)

# Get LLM result
llm_result = client.llm.get_result(organization_id, document_id, prompt_id="default")

# Update LLM result
updated_result = client.llm.update_result(
    organization_id,
    document_id,
    updated_llm_result={"key": "value"},
    prompt_id="default",
    is_verified=True
)

# Delete LLM result
client.llm.delete_result(organization_id, document_id, prompt_id="default")</code></pre>

            <h3 class="text-lg font-medium text-gray-900 mt-6 mb-3">Schemas API</h3>
            <pre><code># Create a schema
schema_config = {
    "name": "Invoice Schema",
    "response_format": {
        "type": "json_schema",
        "json_schema": {
            "name": "invoice_extraction",
            "schema": {
                "type": "object",
                "properties": {
                    "invoice_date": {
                        "type": "string",
                        "description": "invoice date"
                    }
                },
                "required": ["invoice_date"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
}
new_schema = client.schemas.create(organization_id, schema_config)

# List schemas
schemas = client.schemas.list(organization_id)

# Get a schema
schema = client.schemas.get(organization_id, schema_id)

# Validate data against a schema
validation_result = client.schemas.validate(organization_id, schema_id, {"invoice_date": "2023-01-01"})</code></pre>

            <h3 class="text-lg font-medium text-gray-900 mt-6 mb-3">Prompts API</h3>
            <pre><code># Create a prompt
prompt_config = {
    "name": "Invoice Extractor",
    "content": "Extract the following fields from the invoice...",
    "schema_id": "schema_id_here",
    "schema_version": 1,
    "tag_ids": ["tag1", "tag2"],
    "model": "gpt-4o-mini"
}
new_prompt = client.prompts.create(organization_id, prompt_config)

# List prompts
prompts = client.prompts.list(organization_id, document_id="doc_id", tag_ids=["tag1"])

# Get a prompt
prompt = client.prompts.get(organization_id, prompt_id)</code></pre>

            <h3 class="text-lg font-medium text-gray-900 mt-6 mb-3">Tags API</h3>
            <pre><code># Create a tag
tag_config = {
    "name": "Invoices",
    "color": "#FF5733",
    "description": "All invoice documents"
}
new_tag = client.tags.create(organization_id, tag_config)

# List tags
tags = client.tags.list(organization_id)

# Update a tag
updated_tag = client.tags.update(organization_id, tag_id, tag_config)</code></pre>
        </section>

        <section id="error-handling" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Error Handling</h2>
            <p class="text-gray-600 mb-4">The SDK provides detailed error messages when API calls fail:</p>
            <pre><code>try:
    result = client.documents.get(organization_id, "invalid_id")
except Exception as e:
    print(f"API Error: {str(e)}")</code></pre>
        </section>

        <section id="structure" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">SDK Structure</h2>
            <p class="text-gray-600 mb-4">The DocRouter SDK is organized into several modules:</p>
            <pre><code>docrouter_sdk/
├── __init__.py                 # Package initialization
├── api/                        # API client modules
│   ├── __init__.py
│   ├── client.py               # Main client class
│   ├── documents.py            # Documents API
│   ├── llm.py                  # LLM API
│   ├── ocr.py                  # OCR API
│   ├── prompts.py              # Prompts API
│   ├── schemas.py              # Schemas API
│   └── tags.py                 # Tags API
├── models/                     # Data models
│   ├── __init__.py
│   ├── document.py             # Document models
│   ├── llm.py                  # LLM models
│   ├── ocr.py                  # OCR models
│   ├── prompt.py               # Prompt models
│   ├── schema.py               # Schema models
│   └── tag.py                  # Tag models
└── examples/                   # Usage examples
    ├── README.md
    └── basic_docrouter_client.py</code></pre>
        </section>

        <section id="github" class="bg-gradient-to-r from-blue-600 to-blue-800 rounded-lg shadow-lg p-8 mb-12">
            <div class="text-center">
                <h2 class="text-2xl font-semibold text-white mb-4">GitHub Repository</h2>
                <p class="text-blue-100 mb-6">
                    The DocRouter Python SDK is part of the docrouter.ai open source project.
                    You can find the source code on GitHub.
                </p>
                <a href="https://github.com/analytiq-hub/doc-router"
                   target="_blank"
                   rel="noopener noreferrer"
                   class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-8 py-3 rounded-lg font-medium transition-colors duration-200">
                    View on GitHub
                </a>
            </div>
        </section>
    </main>

    <footer class="mt-12 text-center text-gray-600">
        <p>© 2025 DocRouter Python SDK. Part of the <a href="https://github.com/analytiq-hub/doc-router" class="text-blue-600 hover:text-blue-800">docrouter.ai</a> project.</p>
    </footer>
</div>