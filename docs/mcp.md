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
            <p class="text-gray-600 mb-6">Click on any tool name to see detailed information about its parameters and usage.</p>

            <div class="space-y-8">
                <!-- Documents -->
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-4 pb-2 border-b">Documents</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full">
                            <tbody class="divide-y divide-gray-200">
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">upload_documents(documents)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Upload documents</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">list_documents(skip, limit, tagIds, nameSearch, metadataSearch)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">List documents</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">get_document(documentId, fileType)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get document by ID</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">update_document(documentId, documentName, tagIds, metadata)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Update document metadata</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">delete_document(documentId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Delete document</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- OCR -->
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-4 pb-2 border-b">OCR</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full">
                            <tbody class="divide-y divide-gray-200">
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">get_ocr_blocks(documentId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get OCR blocks</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">get_ocr_text(documentId, pageNum)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get OCR text</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">get_ocr_metadata(documentId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get OCR metadata</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- LLM Extraction -->
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-4 pb-2 border-b">LLM Extraction</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full">
                            <tbody class="divide-y divide-gray-200">
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">run_llm(documentId, promptRevId, force)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Run AI extraction</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">get_llm_result(documentId, promptRevId, fallback)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get extraction results</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">update_llm_result(documentId, promptId, result, isVerified)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Update extraction results</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">delete_llm_result(documentId, promptId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Delete extraction results</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Tags -->
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-4 pb-2 border-b">Tags</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full">
                            <tbody class="divide-y divide-gray-200">
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">create_tag(tag)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Create tag</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">list_tags(skip, limit, nameSearch)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">List tags</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">get_tag(tagId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get tag by ID</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">update_tag(tagId, tag)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Update tag</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">delete_tag(tagId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Delete tag</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Prompts -->
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-4 pb-2 border-b">Prompts</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full">
                            <tbody class="divide-y divide-gray-200">
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">create_prompt(prompt)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Create prompt</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">list_prompts(skip, limit, document_id, tag_ids, nameSearch)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">List prompts</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">get_prompt(promptRevId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get prompt by ID</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap">update_prompt(promptId, content)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Update prompt</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">delete_prompt(promptId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Delete prompt</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Schemas -->
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-4 pb-2 border-b">Schemas</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full">
                            <tbody class="divide-y divide-gray-200">
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">create_schema(name, response_format)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Create schema</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">list_schemas(skip, limit, nameSearch)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">List schemas</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">get_schema(schemaRevId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get schema by ID</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">update_schema(schemaId, schema)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Update schema</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">delete_schema(schemaId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Delete schema</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">validate_schema(schema)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Validate schema format</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">validate_against_schema(schemaRevId, data)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Validate data against schema</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Forms -->
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-4 pb-2 border-b">Forms</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full">
                            <tbody class="divide-y divide-gray-200">
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">create_form(name, response_format)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Create form</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">list_forms(skip, limit, tag_ids)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">List forms</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">get_form(formRevId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get form by ID</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">update_form(formId, form)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Update form</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">delete_form(formId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Delete form</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">submit_form(documentId, formRevId, submission_data, submitted_by)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Submit form</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">get_form_submission(documentId, formRevId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get form submission</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">delete_form_submission(documentId, formRevId)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Delete form submission</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">validate_form(form)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Validate form format</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- LLM Chat -->
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-4 pb-2 border-b">LLM Chat</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full">
                            <tbody class="divide-y divide-gray-200">
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">run_llm_chat(messages, model, temperature, max_tokens, stream)</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Run LLM chat</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Help -->
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-4 pb-2 border-b">Help</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full">
                            <tbody class="divide-y divide-gray-200">
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">help()</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get general API help</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">help_prompts()</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get prompts help</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">help_schemas()</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get schemas help</td>
                                </tr>
                                <tr>
                                    <td class="py-3 pr-4 align-top">
                                        <code class="text-xs bg-gray-100 px-2 py-1 rounded whitespace-nowrap tool-name cursor-pointer hover:bg-blue-100 transition-colors">help_forms()</code>
                                    </td>
                                    <td class="py-3 text-sm text-gray-600">Get forms help</td>
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
                <pre class="text-sm text-gray-800 overflow-x-auto"><code>// List documents and run extraction
const documents = await list_documents({ nameSearch: "invoice" });
const ocrText = await get_ocr_text({ documentId: documents.documents[0].id });
const prompts = await list_prompts({ nameSearch: "invoice" });
const extraction = await run_llm({ documentId: documents.documents[0].id, promptRevId: prompts.prompts[0].id });</code></pre>
            </div>

            <h3 class="text-lg font-semibold text-gray-900 mb-2">Discovery</h3>
            <div class="bg-gray-50 rounded-lg p-4 mb-4">
                <pre class="text-sm text-gray-800 overflow-x-auto"><code>// Get all resources
const allDocuments = await list_documents({});
const allPrompts = await list_prompts({});
const allTags = await list_tags({});</code></pre>
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

<!-- Tool Details Modal -->
<div id="toolModal" class="fixed inset-0 bg-black bg-opacity-50 hidden z-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-lg shadow-xl max-w-2xl w-full max-h-[90vh] overflow-hidden flex flex-col">
        <div class="flex justify-between items-center p-6 border-b">
            <h3 id="modalToolName" class="text-xl font-semibold text-gray-900"></h3>
            <button id="closeModal" class="text-gray-400 hover:text-gray-600 text-2xl font-bold">&times;</button>
        </div>
        <div class="p-6 overflow-y-auto flex-1">
            <div class="mb-4">
                <h4 class="text-sm font-semibold text-gray-700 mb-2">Description</h4>
                <p id="modalDescription" class="text-gray-600"></p>
            </div>
            <div class="mb-4">
                <h4 class="text-sm font-semibold text-gray-700 mb-2">Parameters</h4>
                <div id="modalParams" class="space-y-2"></div>
            </div>
            <div id="modalRequired" class="mb-4 hidden">
                <h4 class="text-sm font-semibold text-gray-700 mb-2">Required Parameters</h4>
                <div id="modalRequiredList" class="flex flex-wrap gap-2"></div>
            </div>
        </div>
    </div>
</div>

<script>
// Tool definitions extracted from the MCP server implementation
const toolDefinitions = {
    // Documents
    upload_documents: {
        description: "Upload documents to DocRouter",
        params: {
            documents: { type: "array", description: "Array of documents to upload. Each document should have: name (string), content (string, base64 encoded), tag_ids (array, optional), metadata (object, optional)" }
        },
        required: ["documents"]
    },
    list_documents: {
        description: "List documents from DocRouter",
        params: {
            skip: { type: "number", description: "Number of documents to skip", default: 0 },
            limit: { type: "number", description: "Number of documents to return", default: 10 },
            tagIds: { type: "string", description: "Comma-separated list of tag IDs to filter by" },
            nameSearch: { type: "string", description: "Search by document name" },
            metadataSearch: { type: "string", description: "Search by metadata" }
        },
        required: []
    },
    get_document: {
        description: "Get document by ID from DocRouter",
        params: {
            documentId: { type: "string", description: "ID of the document to retrieve" },
            fileType: { type: "string", description: "File type to retrieve (pdf, image, etc.)", default: "pdf" }
        },
        required: ["documentId"]
    },
    update_document: {
        description: "Update document metadata",
        params: {
            documentId: { type: "string", description: "ID of the document to update" },
            documentName: { type: "string", description: "New document name" },
            tagIds: { type: "array", description: "Array of tag IDs" },
            metadata: { type: "object", description: "Document metadata" }
        },
        required: ["documentId"]
    },
    delete_document: {
        description: "Delete a document",
        params: {
            documentId: { type: "string", description: "ID of the document to delete" }
        },
        required: ["documentId"]
    },
    // OCR
    get_ocr_blocks: {
        description: "Get OCR blocks for a document",
        params: {
            documentId: { type: "string", description: "ID of the document" }
        },
        required: ["documentId"]
    },
    get_ocr_text: {
        description: "Get OCR text for a document",
        params: {
            documentId: { type: "string", description: "ID of the document" },
            pageNum: { type: "number", description: "Optional page number" }
        },
        required: ["documentId"]
    },
    get_ocr_metadata: {
        description: "Get OCR metadata for a document",
        params: {
            documentId: { type: "string", description: "ID of the document" }
        },
        required: ["documentId"]
    },
    // LLM Extraction
    run_llm: {
        description: "Run AI extraction on a document using a specific prompt",
        params: {
            documentId: { type: "string", description: "ID of the document" },
            promptRevId: { type: "string", description: "ID of the prompt" },
            force: { type: "boolean", description: "Force re-extraction", default: false }
        },
        required: ["documentId", "promptRevId"]
    },
    get_llm_result: {
        description: "Get LLM extraction results",
        params: {
            documentId: { type: "string", description: "ID of the document" },
            promptRevId: { type: "string", description: "ID of the prompt" },
            fallback: { type: "boolean", description: "Use fallback results", default: false }
        },
        required: ["documentId", "promptRevId"]
    },
    update_llm_result: {
        description: "Update LLM extraction results",
        params: {
            documentId: { type: "string", description: "ID of the document" },
            promptId: { type: "string", description: "ID of the prompt" },
            result: { type: "object", description: "Updated result data" },
            isVerified: { type: "boolean", description: "Whether result is verified", default: false }
        },
        required: ["documentId", "promptId", "result"]
    },
    delete_llm_result: {
        description: "Delete LLM extraction results",
        params: {
            documentId: { type: "string", description: "ID of the document" },
            promptId: { type: "string", description: "ID of the prompt" }
        },
        required: ["documentId", "promptId"]
    },
    // Tags
    create_tag: {
        description: "Create a new tag",
        params: {
            tag: { type: "object", description: "Tag object with name (string) and color (string)" }
        },
        required: ["tag"]
    },
    get_tag: {
        description: "Get tag by ID",
        params: {
            tagId: { type: "string", description: "ID of the tag" }
        },
        required: ["tagId"]
    },
    list_tags: {
        description: "List all tags",
        params: {
            skip: { type: "number", description: "Number of tags to skip", default: 0 },
            limit: { type: "number", description: "Number of tags to return", default: 10 },
            nameSearch: { type: "string", description: "Search by tag name" }
        },
        required: []
    },
    update_tag: {
        description: "Update a tag",
        params: {
            tagId: { type: "string", description: "ID of the tag to update" },
            tag: { type: "object", description: "Tag object with name (string) and color (string)" }
        },
        required: ["tagId", "tag"]
    },
    delete_tag: {
        description: "Delete a tag",
        params: {
            tagId: { type: "string", description: "ID of the tag to delete" }
        },
        required: ["tagId"]
    },
    // Prompts
    create_prompt: {
        description: "Create a new prompt",
        params: {
            prompt: { type: "object", description: "Prompt object with name, description, schema_id, tag_ids, and other properties" }
        },
        required: ["prompt"]
    },
    list_prompts: {
        description: "List prompts",
        params: {
            skip: { type: "number", description: "Number of prompts to skip", default: 0 },
            limit: { type: "number", description: "Number of prompts to return", default: 10 },
            document_id: { type: "string", description: "Filter by document ID" },
            tag_ids: { type: "string", description: "Comma-separated list of tag IDs" },
            nameSearch: { type: "string", description: "Search by prompt name" }
        },
        required: []
    },
    get_prompt: {
        description: "Get prompt by ID",
        params: {
            promptRevId: { type: "string", description: "ID of the prompt revision" }
        },
        required: ["promptRevId"]
    },
    update_prompt: {
        description: "Update a prompt",
        params: {
            promptId: { type: "string", description: "ID of the prompt to update" },
            prompt: { type: "object", description: "Updated prompt object" }
        },
        required: ["promptId", "prompt"]
    },
    delete_prompt: {
        description: "Delete a prompt",
        params: {
            promptId: { type: "string", description: "ID of the prompt to delete" }
        },
        required: ["promptId"]
    },
    // Schemas
    create_schema: {
        description: "Create a new schema",
        params: {
            schema: { type: "object", description: "Schema object with name, description, and schema (JSON Schema)" }
        },
        required: ["schema"]
    },
    list_schemas: {
        description: "List all schemas",
        params: {
            skip: { type: "number", description: "Number of schemas to skip", default: 0 },
            limit: { type: "number", description: "Number of schemas to return", default: 10 },
            nameSearch: { type: "string", description: "Search by schema name" }
        },
        required: []
    },
    get_schema: {
        description: "Get schema by ID",
        params: {
            schemaId: { type: "string", description: "ID of the schema" }
        },
        required: ["schemaId"]
    },
    update_schema: {
        description: "Update a schema",
        params: {
            schemaId: { type: "string", description: "ID of the schema to update" },
            schema: { type: "object", description: "Updated schema object" }
        },
        required: ["schemaId", "schema"]
    },
    delete_schema: {
        description: "Delete a schema",
        params: {
            schemaId: { type: "string", description: "ID of the schema to delete" }
        },
        required: ["schemaId"]
    },
    validate_schema: {
        description: "Validate a schema definition",
        params: {
            schema: { type: "object", description: "Schema object to validate" }
        },
        required: ["schema"]
    },
    validate_against_schema: {
        description: "Validate data against a schema",
        params: {
            schemaId: { type: "string", description: "ID of the schema" },
            data: { type: "object", description: "Data to validate" }
        },
        required: ["schemaId", "data"]
    },
    // Forms
    create_form: {
        description: "Create a new form",
        params: {
            form: { type: "object", description: "Form object with name, description, schema_id, and other properties" }
        },
        required: ["form"]
    },
    list_forms: {
        description: "List all forms",
        params: {
            skip: { type: "number", description: "Number of forms to skip", default: 0 },
            limit: { type: "number", description: "Number of forms to return", default: 10 },
            nameSearch: { type: "string", description: "Search by form name" }
        },
        required: []
    },
    get_form: {
        description: "Get form by ID",
        params: {
            formId: { type: "string", description: "ID of the form" }
        },
        required: ["formId"]
    },
    update_form: {
        description: "Update a form",
        params: {
            formId: { type: "string", description: "ID of the form to update" },
            form: { type: "object", description: "Updated form object" }
        },
        required: ["formId", "form"]
    },
    delete_form: {
        description: "Delete a form",
        params: {
            formId: { type: "string", description: "ID of the form to delete" }
        },
        required: ["formId"]
    },
    submit_form: {
        description: "Submit form data",
        params: {
            formId: { type: "string", description: "ID of the form" },
            data: { type: "object", description: "Form submission data" }
        },
        required: ["formId", "data"]
    },
    get_form_submission: {
        description: "Get form submission by ID",
        params: {
            submissionId: { type: "string", description: "ID of the submission" }
        },
        required: ["submissionId"]
    },
    delete_form_submission: {
        description: "Delete a form submission",
        params: {
            submissionId: { type: "string", description: "ID of the submission to delete" }
        },
        required: ["submissionId"]
    },
    validate_form: {
        description: "Validate form data",
        params: {
            formId: { type: "string", description: "ID of the form" },
            data: { type: "object", description: "Data to validate" }
        },
        required: ["formId", "data"]
    },
    // LLM Chat
    run_llm_chat: {
        description: "Run a chat conversation with LLM",
        params: {
            messages: { type: "array", description: "Array of chat messages" },
            documentId: { type: "string", description: "Optional document ID to include in context" }
        },
        required: ["messages"]
    },
    // Help
    help: {
        description: "Get general help about DocRouter MCP tools",
        params: {},
        required: []
    },
    help_prompts: {
        description: "Get help about prompts",
        params: {},
        required: []
    },
    help_schemas: {
        description: "Get help about schemas",
        params: {},
        required: []
    },
    help_forms: {
        description: "Get help about forms",
        params: {},
        required: []
    }
};

// Extract tool name from code element text (e.g., "upload_documents(documents)" -> "upload_documents")
function extractToolName(text) {
    const match = text.match(/^(\w+)\s*\(/);
    return match ? match[1] : null;
}

// Display modal with tool information
function showToolModal(toolName) {
    const tool = toolDefinitions[toolName];
    if (!tool) {
        console.warn(`Tool ${toolName} not found in definitions`);
        return;
    }

    const modal = document.getElementById('toolModal');
    const toolNameEl = document.getElementById('modalToolName');
    const descriptionEl = document.getElementById('modalDescription');
    const paramsEl = document.getElementById('modalParams');
    const requiredEl = document.getElementById('modalRequired');
    const requiredListEl = document.getElementById('modalRequiredList');

    toolNameEl.textContent = toolName;
    descriptionEl.textContent = tool.description;

    // Display parameters
    paramsEl.innerHTML = '';
    if (Object.keys(tool.params).length === 0) {
        paramsEl.innerHTML = '<p class="text-gray-500 italic">No parameters</p>';
    } else {
        for (const [paramName, paramInfo] of Object.entries(tool.params)) {
            const isRequired = tool.required.includes(paramName);
            const paramDiv = document.createElement('div');
            paramDiv.className = 'border-l-4 pl-3 py-2 ' + (isRequired ? 'border-red-500' : 'border-gray-300');
            paramDiv.innerHTML = `
                <div class="flex items-center gap-2 mb-1">
                    <code class="text-sm font-mono font-semibold text-gray-900">${paramName}</code>
                    <span class="text-xs text-gray-500">${paramInfo.type}</span>
                    ${isRequired ? '<span class="text-xs bg-red-100 text-red-700 px-2 py-0.5 rounded">required</span>' : ''}
                    ${paramInfo.default !== undefined ? `<span class="text-xs bg-blue-100 text-blue-700 px-2 py-0.5 rounded">default: ${paramInfo.default}</span>` : ''}
                </div>
                <p class="text-sm text-gray-600">${paramInfo.description || 'No description'}</p>
            `;
            paramsEl.appendChild(paramDiv);
        }
    }

    // Display required parameters
    if (tool.required.length > 0) {
        requiredEl.classList.remove('hidden');
        requiredListEl.innerHTML = '';
        tool.required.forEach(param => {
            const badge = document.createElement('span');
            badge.className = 'inline-block bg-red-100 text-red-700 text-xs font-semibold px-3 py-1 rounded';
            badge.textContent = param;
            requiredListEl.appendChild(badge);
        });
    } else {
        requiredEl.classList.add('hidden');
    }

    modal.classList.remove('hidden');
}

// Close modal
function closeModal() {
    document.getElementById('toolModal').classList.add('hidden');
}

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    // Make all tool names clickable
    document.querySelectorAll('code.tool-name').forEach(codeEl => {
        codeEl.style.cursor = 'pointer';
        codeEl.addEventListener('click', function() {
            const toolName = extractToolName(this.textContent);
            if (toolName) {
                showToolModal(toolName);
            }
        });
    });

    // Close modal on X button
    document.getElementById('closeModal').addEventListener('click', closeModal);

    // Close modal on background click
    document.getElementById('toolModal').addEventListener('click', function(e) {
        if (e.target === this) {
            closeModal();
        }
    });

    // Close modal on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeModal();
        }
    });
});
</script>
