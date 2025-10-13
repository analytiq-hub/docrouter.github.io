---
layout: docs
title: "DocRouter MCP Server"
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <header class="md:mb-12 mb-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
            <div>
                <h1 class="text-4xl font-bold text-gray-900 mb-4">DocRouter MCP Server</h1>
                <p class="text-xl text-gray-600">Model Context Protocol server for seamless AI assistant integration</p>
            </div>
            <div class="rounded-xl border border-blue-200 bg-gradient-to-br from-blue-50 via-white to-purple-50 p-6 text-center shadow-lg">
                <a href="https://github.com/analytiq-hub/doc-router/tree/main/packages/typescript/docrouter-mcp"
                   target="_blank"
                   rel="noopener noreferrer"
                   class="inline-flex items-center bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 px-6 py-3 rounded-lg font-medium transition-colors duration-200">
                    <svg class="w-5 h-5 mr-2 text-white" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
                    </svg>
                    <span class="text-white">View on GitHub</span>
                </a>
            </div>
        </div>
    </header>

    <main>
        <section id="overview" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Overview</h2>
            <p class="text-gray-600 mb-4">
                The DocRouter MCP Server is a TypeScript-based server that implements the Model Context Protocol,
                enabling AI assistants like Claude Desktop, Cursor IDE, and other MCP-compatible tools to directly
                interact with your DocRouter organization.
            </p>
            <p class="text-gray-600 mb-4">
                This server provides seamless document processing capabilities within your AI workflows, allowing AI
                assistants to upload documents, retrieve analysis results, and manage your document processing workflows
                programmatically.
            </p>
            <ul class="list-disc list-inside text-gray-600 space-y-2">
                <li>Document management and retrieval</li>
                <li>OCR text extraction and metadata</li>
                <li>AI-powered data extraction using prompts</li>
                <li>Tag and prompt management</li>
                <li>Advanced search functionality</li>
            </ul>
        </section>

        <section id="installation" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Installation</h2>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Prerequisites</h3>
            <ul class="list-disc list-inside text-gray-600 space-y-1 mb-6">
                <li>Node.js 18+ installed on your system</li>
                <li>DocRouter Account with API access</li>
                <li>DocRouter Organization ID and API Token</li>
            </ul>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Global Installation (Recommended)</h3>
            <p class="text-gray-600 mb-3">Install the package globally to make the <code class="bg-gray-100 px-2 py-1 rounded">docrouter-mcp</code> binary available system-wide:</p>
            <div class="bg-gray-50 rounded-lg p-4 mb-6">
                <code class="text-sm text-gray-800">npm install -g @docrouter/mcp</code>
            </div>

            <p class="text-gray-600 mb-3">Verify the installation:</p>
            <div class="bg-gray-50 rounded-lg p-4 mb-6">
                <pre class="text-sm text-gray-800 overflow-x-auto"><code># Check if binary is available
which docrouter-mcp

# Test the installation
docrouter-mcp --help</code></pre>
            </div>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Local Installation</h3>
            <p class="text-gray-600 mb-3">For project-specific installation:</p>
            <div class="bg-gray-50 rounded-lg p-4">
                <code class="text-sm text-gray-800">npm install @docrouter/mcp</code>
            </div>
            <p class="text-gray-600 mt-2 text-sm">Note: Local installation requires using the full path to the executable in your MCP configuration.</p>
        </section>

        <section id="configuration" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Configuration</h2>

            <h3 class="text-lg font-medium text-gray-900 mb-3">For Cursor IDE</h3>
            <p class="text-gray-600 mb-3">Create <code class="bg-gray-100 px-2 py-1 rounded">.mcp.json</code> in your project root:</p>
            <div class="bg-gray-50 rounded-lg p-4 mb-6">
                <pre class="text-sm text-gray-800 overflow-x-auto"><code>{
  "mcpServers": {
    "docrouter": {
      "command": "docrouter-mcp",
      "env": {
        "DOCROUTER_API_URL": "https://app.docrouter.ai/fastapi",
        "DOCROUTER_ORG_ID": "your-org-id",
        "DOCROUTER_ORG_API_TOKEN": "your-api-token"
      }
    }
  }
}</code></pre>
            </div>

            <h3 class="text-lg font-medium text-gray-900 mb-3">For Claude Desktop</h3>
            <p class="text-gray-600 mb-3">Add to your <code class="bg-gray-100 px-2 py-1 rounded">claude_desktop_config.json</code>:</p>
            <div class="bg-gray-50 rounded-lg p-4 mb-6">
                <pre class="text-sm text-gray-800 overflow-x-auto"><code>{
  "mcpServers": {
    "docrouter": {
      "command": "docrouter-mcp",
      "env": {
        "DOCROUTER_API_URL": "https://app.docrouter.ai/fastapi",
        "DOCROUTER_ORG_ID": "your-org-id",
        "DOCROUTER_ORG_API_TOKEN": "your-api-token"
      }
    }
  }
}</code></pre>
            </div>

            <div class="bg-blue-50 border-l-4 border-blue-500 p-4">
                <p class="text-sm text-gray-700">
                    <strong>Important:</strong> Replace <code class="bg-gray-100 px-2 py-1 rounded">your-org-id</code> and
                    <code class="bg-gray-100 px-2 py-1 rounded">your-api-token</code> with your actual DocRouter credentials.
                </p>
            </div>
        </section>

        <section id="features" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-6">Available MCP Tools</h2>
            <p class="text-gray-600 mb-6">Once configured, the following tools become available in your AI application:</p>

            <div class="space-y-8">
                <!-- Document Management -->
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-4 pb-2 border-b">Document Management</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full">
                            <tbody class="divide-y divide-gray-200">
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">get_docrouter_documents()</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">List all documents</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">get_docrouter_document(documentId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get document by ID</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">get_docrouter_document_ocr(documentId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get raw OCR text</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">get_docrouter_document_ocr_metadata(documentId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get OCR metadata</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Data Extraction -->
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-4 pb-2 border-b">Data Extraction</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full">
                            <tbody class="divide-y divide-gray-200">
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">run_docrouter_extraction(documentId, promptRevId, force)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Run AI extraction</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">get_docrouter_extraction(documentId, promptRevId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get extraction results</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Search and Discovery -->
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-4 pb-2 border-b">Search and Discovery</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full">
                            <tbody class="divide-y divide-gray-200">
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">search_docrouter_documents(query, tagIds)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Search documents</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">search_docrouter_prompts(query)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Search prompts</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">search_docrouter_tags(query)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Search tags</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Management -->
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-4 pb-2 border-b">Management</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full">
                            <tbody class="divide-y divide-gray-200">
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">get_docrouter_prompts()</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">List all prompts</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">get_docrouter_prompt(promptRevId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get prompt by ID</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">get_docrouter_tags()</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">List all tags</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">get_docrouter_tag(tagId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get tag by ID</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Help and Guidance -->
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-4 pb-2 border-b">Help and Guidance</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full">
                            <tbody class="divide-y divide-gray-200">
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">docrouter_help()</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get help information</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">docrouter_document_analysis_guide(documentId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Generate analysis guide</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>

        <section id="workflows" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-6">Example Workflows</h2>

            <div class="space-y-6">
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">1. Document Analysis Workflow</h3>
                    <div class="bg-gray-50 rounded-lg p-4">
                        <pre class="text-sm text-gray-800 overflow-x-auto"><code>// Search for invoice documents
const documents = await search_docrouter_documents("invoice");

// Get OCR text for the first document
const ocrText = await get_docrouter_document_ocr(documents.documents[0].id);

// Find available prompts for invoice processing
const prompts = await search_docrouter_prompts("invoice");

// Run extraction with a specific prompt
const extraction = await run_docrouter_extraction(
  documents.documents[0].id,
  prompts.prompts[0].id
);</code></pre>
                    </div>
                </div>

                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">2. Document Discovery Workflow</h3>
                    <div class="bg-gray-50 rounded-lg p-4">
                        <pre class="text-sm text-gray-800 overflow-x-auto"><code>// Get all documents
const allDocuments = await get_docrouter_documents();

// Get all available prompts
const allPrompts = await get_docrouter_prompts();

// Get all tags for categorization
const allTags = await get_docrouter_tags();</code></pre>
                    </div>
                </div>

                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">3. Guided Analysis Workflow</h3>
                    <div class="bg-gray-50 rounded-lg p-4">
                        <pre class="text-sm text-gray-800 overflow-x-auto"><code>// Get a step-by-step guide for analyzing a specific document
const guide = await docrouter_document_analysis_guide("document-id");

// Follow the guide to analyze the document
// The guide will provide specific prompts and extraction strategies</code></pre>
                    </div>
                </div>
            </div>
        </section>

        <section id="troubleshooting" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-6">Troubleshooting</h2>

            <div class="space-y-6">
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">MCP Server Not Connecting</h3>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>Verify the binary exists: <code class="bg-gray-100 px-2 py-1 rounded text-sm">which docrouter-mcp</code></li>
                        <li>Check configuration syntax in your <code class="bg-gray-100 px-2 py-1 rounded text-sm">.mcp.json</code></li>
                        <li>Ensure environment variables are set correctly</li>
                        <li>Test the server manually: <code class="bg-gray-100 px-2 py-1 rounded text-sm">docrouter-mcp</code></li>
                    </ul>
                </div>

                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">Command Not Found</h3>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>Reinstall globally: <code class="bg-gray-100 px-2 py-1 rounded text-sm">npm install -g @docrouter/mcp</code></li>
                        <li>Check your PATH: <code class="bg-gray-100 px-2 py-1 rounded text-sm">echo $PATH</code></li>
                        <li>Use full path in configuration if needed</li>
                    </ul>
                </div>

                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">Environment Variables Not Set</h3>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>Verify variable names: <code class="bg-gray-100 px-2 py-1 rounded text-sm">DOCROUTER_ORG_ID</code>, <code class="bg-gray-100 px-2 py-1 rounded text-sm">DOCROUTER_ORG_API_TOKEN</code></li>
                        <li>Check variable values are correct and not expired</li>
                        <li>Test API access with your credentials</li>
                    </ul>
                </div>

                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">Enable Debug Mode</h3>
                    <p class="text-gray-600 mb-3">Add debug logging to your environment:</p>
                    <div class="bg-gray-50 rounded-lg p-4">
                        <pre class="text-sm text-gray-800 overflow-x-auto"><code>"env": {
  "DOCROUTER_API_URL": "https://app.docrouter.ai/fastapi",
  "DOCROUTER_ORG_ID": "your-org-id",
  "DOCROUTER_ORG_API_TOKEN": "your-api-token",
  "DEBUG": "mcp:*"
}</code></pre>
                    </div>
                </div>
            </div>
        </section>

        <section id="security" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-6">Security Best Practices</h2>

            <div class="space-y-4">
                <div class="flex items-start">
                    <svg class="w-6 h-6 text-green-600 mr-3 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                    </svg>
                    <div>
                        <h3 class="font-semibold text-gray-900">Never Commit Credentials</h3>
                        <p class="text-gray-600">Add <code class="bg-gray-100 px-2 py-1 rounded text-sm">.mcp.json</code> to <code class="bg-gray-100 px-2 py-1 rounded text-sm">.gitignore</code> if it contains real credentials</p>
                    </div>
                </div>

                <div class="flex items-start">
                    <svg class="w-6 h-6 text-green-600 mr-3 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                    </svg>
                    <div>
                        <h3 class="font-semibold text-gray-900">Use Environment Variables</h3>
                        <p class="text-gray-600">Store credentials in environment variables instead of hardcoded values</p>
                    </div>
                </div>

                <div class="flex items-start">
                    <svg class="w-6 h-6 text-green-600 mr-3 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                    </svg>
                    <div>
                        <h3 class="font-semibold text-gray-900">Rotate API Tokens</h3>
                        <p class="text-gray-600">Regularly rotate API tokens and limit permissions to minimum required access</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg shadow-lg p-8">
            <h2 class="text-2xl font-semibold text-white mb-4 text-center">Ready to Get Started?</h2>
            <div class="text-center">
                <p class="text-blue-100 mb-6">
                    Install the MCP server and start processing documents with AI assistance.
                </p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                    <a href="https://github.com/analytiq-hub/doc-router/tree/main/packages/typescript/docrouter-mcp"
                       target="_blank"
                       rel="noopener noreferrer"
                       class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200">
                        View on GitHub
                    </a>
                    <a href="https://app.docrouter.ai"
                       target="_blank"
                       rel="noopener noreferrer"
                       class="inline-block border-2 border-white text-white hover:bg-blue-700 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200">
                        Get API Credentials
                    </a>
                </div>
            </div>
        </section>
    </main>

    <footer class="mt-12 text-center text-gray-600">
        <p>© 2025 DocRouter MCP Server. Part of the <a href="https://github.com/analytiq-hub/doc-router" class="text-blue-600 hover:text-blue-800">docrouter.ai</a> project.</p>
    </footer>
</div>
