---
layout: docs
title: "DocRouter Python SDK"
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <header class="text-center md:mb-12 mb-4">
        <h1 class="text-4xl font-bold text-gray-900 mb-4 hidden sm:block">DocRouter Python SDK</h1>
        <div class="text-xl text-gray-600">
            <p class="mb-2">Python client library for interacting with docrouter.ai</p>
        </div>
        <div class="mt-6">
            <a href="https://colab.research.google.com/github/analytiq-hub/docrouter.github.io/blob/main/notebooks/python_sdk/onboarding.ipynb"
               target="_blank"
               rel="noopener noreferrer"
               class="inline-flex items-center bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-lg font-medium transition-colors duration-200">
                <svg class="w-5 h-5 mr-2 text-white" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
                </svg>
                <span class="text-white">Open in Google Colab</span>
            </a>
        </div>
    </header>

    <main>
        <section id="overview" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Overview</h2>
            <p class="text-gray-600 mb-0">
                The DocRouter Python SDK gives programmatic access to documents, OCR, LLM analysis, schemas, prompts, and tags—so you can automate document workflows and extract structured data directly from your apps.
            </p>
        </section>

        <section id="installation" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Installation</h2>
            <p class="text-gray-600 mb-6">Install the DocRouter SDK from PyPI:</p>

            <pre><code>pip install docrouter_sdk</code></pre>

            <details class="mt-6">
                <summary class="cursor-pointer text-gray-900 font-medium">Developer setup (editable install)</summary>
                <div class="mt-4">
                    <pre><code>git clone https://github.com/analytiq-hub/doc-router.git
cd doc-router/packages/docrouter_sdk
pip install -e .</code></pre>
                </div>
            </details>
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

            <p class="text-gray-600 mb-4">
                For a guided, runnable walkthrough, please use the Google Colab notebook linked at the top of this page.
                It includes end-to-end examples for authentication, listing documents and tags, running LLM analysis, and more.
            </p>
            <div>
                <a href="https://colab.research.google.com/github/analytiq-hub/docrouter.github.io/blob/main/notebooks/python_sdk/onboarding.ipynb"
                   target="_blank"
                   rel="noopener noreferrer"
                   class="inline-flex items-center bg-blue-600 hover:bg-blue-700 px-5 py-2.5 rounded-lg font-medium text-white transition-colors duration-200">
                    <span class="text-white">Open the DocRouter Python SDK Colab</span>
                </a>
            </div>
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
            <p class="text-gray-600 mb-4">Expand a section to view examples. For a runnable walkthrough, use the Colab at the top.</p>

            <details class="mb-4">
                <summary class="cursor-pointer text-gray-900 font-medium">Documents API</summary>
                <div class="mt-3">
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
                </div>
            </details>

            <details class="mb-4">
                <summary class="cursor-pointer text-gray-900 font-medium">OCR API</summary>
                <div class="mt-3">
                    <pre><code># Get OCR blocks
blocks = client.ocr.get_blocks(organization_id, document_id)

# Get OCR text
text = client.ocr.get_text(organization_id, document_id, page_num=1)

# Get OCR metadata
metadata = client.ocr.get_metadata(organization_id, document_id)
print(f"Number of pages: {metadata.n_pages}")</code></pre>
                </div>
            </details>

            <details class="mb-4">
                <summary class="cursor-pointer text-gray-900 font-medium">LLM API</summary>
                <div class="mt-3">
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
                </div>
            </details>

            <details class="mb-4">
                <summary class="cursor-pointer text-gray-900 font-medium">Schemas API</summary>
                <div class="mt-3">
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
                </div>
            </details>

            <details class="mb-4">
                <summary class="cursor-pointer text-gray-900 font-medium">Prompts API</summary>
                <div class="mt-3">
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
                </div>
            </details>

            <details>
                <summary class="cursor-pointer text-gray-900 font-medium">Tags API</summary>
                <div class="mt-3">
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
                </div>
            </details>
        </section>

        <section id="error-handling" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <details>
                <summary class="cursor-pointer text-gray-900 font-semibold text-2xl">Error Handling</summary>
                <div class="mt-4">
                    <p class="text-gray-600 mb-4">The SDK provides detailed error messages when API calls fail:</p>
                    <pre><code>try:
    result = client.documents.get(organization_id, "invalid_id")
except Exception as e:
    print(f"API Error: {str(e)}")</code></pre>
                </div>
            </details>
        </section>

        <section id="structure" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <details>
                <summary class="cursor-pointer text-gray-900 font-semibold text-2xl">SDK Structure</summary>
                <div class="mt-4">
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
                </div>
            </details>
        </section>

        <section id="github" class="bg-gradient-to-r from-blue-600 to-blue-800 rounded-lg shadow-lg p-8 mb-12">
            <div class="text-center">
                <span class="text-2xl font-semibold text-white mb-4">
                <h2>GitHub Repository</h2>
                </span>
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