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
            <div class="rounded-xl border border-blue-200 bg-blue-50 p-6 text-center shadow-lg">
                <a href="https://github.com/analytiq-hub/doc-router/tree/main/packages/typescript/mcp"
                   target="_blank"
                   rel="noopener noreferrer"
                   class="inline-flex items-center bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-lg font-medium transition-colors duration-200 no-underline">
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
        "DOCROUTER_ORG_API_TOKEN": "your-org-api-token"
      }
    }
  }
}</code></pre>
            </div>

            <div class="bg-blue-50 border-l-4 border-blue-500 p-4 mt-4">
                <p class="text-sm text-gray-700">
                    Replace <code class="bg-gray-100 px-2 py-1 rounded">your-org-api-token</code> with your actual DocRouter <strong>organization API token</strong>. The organization ID is automatically resolved from this token and does not need to be configured.
                </p>
            </div>
        </section>

        <section id="examples" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-6">Example Prompts</h2>

            <h3 class="text-lg font-semibold text-gray-900 mb-2">Create a Schema</h3>
            <div class="bg-gray-50 rounded-lg p-4 mb-4">
                <pre class="text-sm text-gray-800 overflow-x-auto"><code>Create a schema for extracting invoices with these fields:
- invoice_number (string, required)
- date (string, format: date)
- total_amount (number, required)
- vendor_name (string)
- line_items (array of objects). The line_items object: 
  - description 
  - quantity 
  - unit_price
  - total
</code></pre>
            </div>

            <h3 class="text-lg font-semibold text-gray-900 mb-2">Update a Schema</h3>
            <div class="bg-gray-50 rounded-lg p-4 mb-4">
                <pre class="text-sm text-gray-800 overflow-x-auto"><code>Update the invoice schema to add a new optional field:
- payment_terms (string)
</code></pre>
            </div>

            <h3 class="text-lg font-semibold text-gray-900 mb-2">Create a Prompt</h3>
            <div class="bg-gray-50 rounded-lg p-4 mb-4">
                <pre class="text-sm text-gray-800 overflow-x-auto"><code>Create a prompt for extracting invoice data from documents.

Configure it with the invoice schema, and tag it with a tag named 'green'
</code></pre>
            </div>

            <h3 class="text-lg font-semibold text-gray-900 mb-2">Update a Prompt</h3>
            <div class="bg-gray-50 rounded-lg p-4 mb-4">
                <pre class="text-sm text-gray-800 overflow-x-auto"><code>Update the invoice extraction prompt to ensure the date is in YYYY-MM-DD format."</code></pre>
            </div>
        </section>

        <section id="features" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">What the MCP Server Can Do</h2>
            <p class="text-gray-600 mb-4">
                The DocRouter MCP server exposes a rich set of tools for documents, OCR, LLM extraction, tags, prompts, schemas,
                forms, and chat. Instead of listing every tool here, refer to the MCP README and in-assistant <code>help()</code>
                commands for the live, authoritative list.
            </p>
            <ul class="list-disc list-inside text-gray-600 space-y-2">
                <li>Upload, list, update, and delete documents</li>
                <li>Access OCR text and structured OCR blocks</li>
                <li>Run LLM extraction and retrieve results</li>
                <li>Manage tags, prompts, schemas, and forms</li>
                <li>Run LLM chat and knowledge-base–style workflows</li>
                <li>Call <code>help()</code>, <code>help_prompts()</code>, <code>help_schemas()</code>, and <code>help_forms()</code> from your assistant for detailed usage</li>
            </ul>
        </section>

        <section id="learn-more" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Learn More</h2>
            <ul class="list-disc list-inside text-gray-600 space-y-2">
                <li>
                    <a href="/docs/claude-code/" class="text-blue-600 hover:text-blue-800">Claude Code Integration</a>
                    — Use the DocRouter MCP server from Claude Code.
                </li>
                <li>
                    <a href="/docs/cursor/" class="text-blue-600 hover:text-blue-800">Cursor Integration</a>
                    — Use the DocRouter MCP server from Cursor.
                </li>
                <li>
                    <a href="/docs/rest-api/" class="text-blue-600 hover:text-blue-800">REST API</a>
                    — Learn about the underlying HTTP endpoints the MCP server calls.
                </li>
                <li>
                    <a href="/docs/knowledge-bases/" class="text-blue-600 hover:text-blue-800">Knowledge Bases</a>
                    — Provide retrieval context for extraction and chat workflows.
                </li>
                <li>
                    <a href="/docs/chat-agents/" class="text-blue-600 hover:text-blue-800">Chat Agents</a>
                    — Build chat experiences on top of DocRouter.
                </li>
            </ul>
        </section>

        <section id="workflows" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <div class="text-center mt-8">
                <a href="https://github.com/analytiq-hub/doc-router/tree/main/packages/typescript/mcp"
                   target="_blank"
                   rel="noopener noreferrer"
                   class="inline-block bg-blue-600 text-white hover:bg-blue-700 px-6 py-3 rounded-lg font-semibold transition-colors duration-200 mr-4 no-underline">
                    View on GitHub
                </a>
                <a href="https://app.docrouter.ai"
                   target="_blank"
                   rel="noopener noreferrer"
                   class="inline-block border-2 border-blue-600 text-blue-600 hover:bg-blue-50 px-6 py-3 rounded-lg font-semibold transition-colors duration-200 no-underline">
                    Get API Credentials
                </a>
            </div>
        </section>
    </main>

    <footer class="mt-12 text-center text-gray-600">
        <p>© 2025 DocRouter MCP Server. Part of the <a href="https://github.com/analytiq-hub/doc-router" class="text-blue-600 hover:text-blue-800">docrouter.ai</a> project.</p>
    </footer>
</div>
