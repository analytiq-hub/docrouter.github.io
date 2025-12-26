---
layout: docs
title: "DocRouter MCP Server"
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <header class="md:mb-12 mb-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
            <div>
                <p class="text-xl text-gray-600">Model Context Protocol server for seamless AI assistant integration</p>
            </div>
            <div class="rounded-xl border border-blue-200 bg-gradient-to-br from-blue-50 via-white to-purple-50 p-6 text-center shadow-lg">
                <a href="https://github.com/analytiq-hub/doc-router/tree/main/packages/typescript/mcp"
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
                The DocRouter MCP Server enables AI agents to interact directly with DocRouter.AI for document processing workflows.
            </p>
            <ul class="list-disc list-inside text-gray-600 space-y-2">
                <li>Document management and retrieval</li>
                <li>AI-powered document processing</li>
                <li>Schema and prompt configuration</li>
                <li>Web forms configuration</li>
            </ul>
        </section>

        <section id="installation" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Installation</h2>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Prerequisites</h3>
            <ul class="list-disc list-inside text-gray-600 space-y-1 mb-6">
                <li>Node.js 18+ installed on your system</li>
            </ul>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Installation</h3>
            <div class="bg-gray-50 rounded-lg p-4 mb-6">
                <code class="text-sm text-gray-800">npm install -g @docrouter/mcp</code>
            </div>

            <p class="text-gray-600 mb-3">Verify installation:</p>
            <div class="bg-gray-50 rounded-lg p-4 mb-6">
                <pre class="text-sm text-gray-800 overflow-x-auto"><code>which docrouter-mcp
docrouter-mcp --help</code></pre>
            </div>

        </section>

        <section id="configuration" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Configuration</h2>

            <p class="text-gray-600 mb-6">Configure the MCP server for your AI assistant:</p>

            <ul class="list-disc list-inside text-gray-600 space-y-2 mb-6">
                <li><strong>Cursor IDE:</strong> Create <code class="bg-gray-100 px-2 py-1 rounded">.mcp.json</code></li>
                <li><strong>Claude Desktop:</strong> Update <code class="bg-gray-100 px-2 py-1 rounded">claude_desktop_config.json</code></li>
                <li><strong>Claude Agent:</strong> Configure MCP server</li>
            </ul>

            <div class="bg-gray-50 rounded-lg p-6 mt-6">
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

            <div class="bg-blue-50 border-l-4 border-blue-500 p-4 mt-4">
                <p class="text-sm text-gray-700">
                    Replace <code class="bg-gray-100 px-2 py-1 rounded">your-org-id</code> and <code class="bg-gray-100 px-2 py-1 rounded">your-api-token</code> with your actual DocRouter credentials.
                </p>
            </div>
        </section>

        <section id="features" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-6">Available Tools</h2>

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

            <h3 class="text-lg font-semibold text-gray-900 mb-2">Document Analysis</h3>
            <div class="bg-gray-50 rounded-lg p-4 mb-4">
                <pre class="text-sm text-gray-800 overflow-x-auto"><code>// Search for documents and run extraction
const documents = await search_docrouter_documents("invoice");
const ocrText = await get_docrouter_document_ocr(documents.documents[0].id);
const prompts = await search_docrouter_prompts("invoice");
const extraction = await run_docrouter_extraction(documents.documents[0].id, prompts.prompts[0].id);</code></pre>
            </div>

            <h3 class="text-lg font-semibold text-gray-900 mb-2">Discovery</h3>
            <div class="bg-gray-50 rounded-lg p-4 mb-4">
                <pre class="text-sm text-gray-800 overflow-x-auto"><code>// Get all resources
const allDocuments = await get_docrouter_documents();
const allPrompts = await get_docrouter_prompts();
const allTags = await get_docrouter_tags();</code></pre>
            </div>
        </section>

        <section id="troubleshooting" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-6">Troubleshooting</h2>

            <h3 class="text-lg font-semibold text-gray-900 mb-2">Connection Issues</h3>
            <ul class="list-disc list-inside text-gray-600 space-y-1 mb-4">
                <li>Verify binary: <code class="bg-gray-100 px-2 py-1 rounded text-sm">which docrouter-mcp</code></li>
                <li>Check config syntax in <code class="bg-gray-100 px-2 py-1 rounded text-sm">.mcp.json</code></li>
                <li>Verify environment variables</li>
            </ul>

            <h3 class="text-lg font-semibold text-gray-900 mb-2">Command Not Found</h3>
            <ul class="list-disc list-inside text-gray-600 space-y-1 mb-4">
                <li>Reinstall: <code class="bg-gray-100 px-2 py-1 rounded text-sm">npm install -g @docrouter/mcp</code></li>
                <li>Check PATH or use full path</li>
            </ul>

            <h3 class="text-lg font-semibold text-gray-900 mb-2">Debug Mode</h3>
            <div class="bg-gray-50 rounded-lg p-4">
                <pre class="text-sm text-gray-800 overflow-x-auto"><code>"env": {
  "DEBUG": "mcp:*"
}</code></pre>
            </div>
        </section>

        <section id="security" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-6">Security</h2>

            <ul class="list-disc list-inside text-gray-600 space-y-2">
                <li>Add <code class="bg-gray-100 px-2 py-1 rounded text-sm">.mcp.json</code> to <code class="bg-gray-100 px-2 py-1 rounded text-sm">.gitignore</code> to avoid committing credentials</li>
                <li>Use environment variables for sensitive data</li>
                <li>Regularly rotate API tokens</li>
            </ul>
        </section>

        <div class="text-center mt-8">
            <a href="https://github.com/analytiq-hub/doc-router/tree/main/packages/typescript/docrouter-mcp"
               target="_blank"
               rel="noopener noreferrer"
               class="inline-block bg-blue-600 text-white hover:bg-blue-700 px-6 py-3 rounded-lg font-semibold transition-colors duration-200 mr-4">
                View on GitHub
            </a>
            <a href="https://app.docrouter.ai"
               target="_blank"
               rel="noopener noreferrer"
               class="inline-block border-2 border-blue-600 text-blue-600 hover:bg-blue-50 px-6 py-3 rounded-lg font-semibold transition-colors duration-200">
                Get API Credentials
            </a>
        </div>
    </main>

    <footer class="mt-12 text-center text-gray-600">
        <p>© 2025 DocRouter MCP Server. Part of the <a href="https://github.com/analytiq-hub/doc-router" class="text-blue-600 hover:text-blue-800">docrouter.ai</a> project.</p>
    </footer>
</div>
