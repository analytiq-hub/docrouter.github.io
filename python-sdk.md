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

            <pre><code>from docrouter import DocRouterClient

# Initialize the client
client = DocRouterClient(
    docrouter_org_id="your-org-id",
    token="your-api-token"
)

# Upload a document
with open("invoice.pdf", "rb") as f:
    document = client.documents.upload(f, tags=["invoice"])

# Get document analysis
analysis = client.documents.get_analysis(document.id)
print(analysis.structured_data)</code></pre>
        </section>

        <section id="api-reference" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">API Reference</h2>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Documents</h3>
            <div class="space-y-4 mb-6">
                <div class="border-l-4 border-blue-500 pl-4">
                    <code class="text-sm bg-gray-100 px-2 py-1 rounded">client.documents.upload(file, tags=[])</code>
                    <p class="text-gray-600 mt-1">Upload a document for processing</p>
                </div>
                <div class="border-l-4 border-blue-500 pl-4">
                    <code class="text-sm bg-gray-100 px-2 py-1 rounded">client.documents.list()</code>
                    <p class="text-gray-600 mt-1">List all documents in your organization</p>
                </div>
                <div class="border-l-4 border-blue-500 pl-4">
                    <code class="text-sm bg-gray-100 px-2 py-1 rounded">client.documents.get(document_id)</code>
                    <p class="text-gray-600 mt-1">Get a specific document by ID</p>
                </div>
                <div class="border-l-4 border-blue-500 pl-4">
                    <code class="text-sm bg-gray-100 px-2 py-1 rounded">client.documents.get_analysis(document_id)</code>
                    <p class="text-gray-600 mt-1">Get the AI analysis results for a document</p>
                </div>
            </div>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Schemas & Prompts</h3>
            <div class="space-y-4 mb-6">
                <div class="border-l-4 border-green-500 pl-4">
                    <code class="text-sm bg-gray-100 px-2 py-1 rounded">client.schemas.list()</code>
                    <p class="text-gray-600 mt-1">List all schemas in your organization</p>
                </div>
                <div class="border-l-4 border-green-500 pl-4">
                    <code class="text-sm bg-gray-100 px-2 py-1 rounded">client.prompts.list()</code>
                    <p class="text-gray-600 mt-1">List all prompts in your organization</p>
                </div>
            </div>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Tags</h3>
            <div class="space-y-4">
                <div class="border-l-4 border-purple-500 pl-4">
                    <code class="text-sm bg-gray-100 px-2 py-1 rounded">client.tags.list()</code>
                    <p class="text-gray-600 mt-1">List all tags in your organization</p>
                </div>
                <div class="border-l-4 border-purple-500 pl-4">
                    <code class="text-sm bg-gray-100 px-2 py-1 rounded">client.tags.create(name, description)</code>
                    <p class="text-gray-600 mt-1">Create a new tag</p>
                </div>
            </div>
        </section>

        <section id="examples" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Examples</h2>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Batch Document Processing</h3>
            <pre><code>import os
from docrouter import DocRouterClient

client = DocRouterClient(
    docrouter_org_id="your-org-id",
    token="your-api-token"
)

# Process all PDFs in a directory
for filename in os.listdir("./invoices"):
    if filename.endswith(".pdf"):
        with open(f"./invoices/{filename}", "rb") as f:
            document = client.documents.upload(f, tags=["invoice", "batch"])
            print(f"Uploaded {filename}: {document.id}")

# Check processing status
documents = client.documents.list()
for doc in documents:
    if "batch" in doc.tags:
        analysis = client.documents.get_analysis(doc.id)
        if analysis.status == "completed":
            print(f"Document {doc.filename} processed successfully")
            print(f"Extracted data: {analysis.structured_data}")
</code></pre>
        </section>

        <section class="bg-gray-50 rounded-lg p-8">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4 text-center">Ready to Get Started?</h2>
            <div class="text-center">
                <p class="text-gray-600 mb-6">
                    Install the SDK and start automating your document processing workflows today.
                </p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                    <a href="https://github.com/analytiq-hub/doc-router"
                       target="_blank"
                       rel="noopener noreferrer"
                       class="inline-block bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200">
                        View on GitHub
                    </a>
                    <a href="https://app.docrouter.ai"
                       target="_blank"
                       rel="noopener noreferrer"
                       class="inline-block border-2 border-blue-600 text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200">
                        Try DocRouter
                    </a>
                </div>
            </div>
        </section>
    </main>
</div>