---
layout: default
title: "DocRouter MCP Server"
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <header class="text-center md:mb-12 mb-4">
        <h1 class="text-4xl font-bold text-gray-900 mb-4">DocRouter MCP Server</h1>
        <div class="text-xl text-gray-600">
            <p class="mb-2">Model Context Protocol server for seamless AI assistant integration</p>
        </div>
    </header>

    <main>
        <section id="overview" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Overview</h2>
            <p class="text-gray-600 mb-6">
                The DocRouter MCP Server enables AI assistants like Claude to directly interact with your DocRouter organization,
                providing seamless document processing capabilities within your AI workflows.
            </p>
            <p class="text-gray-600 mb-6">
                This server implements the Model Context Protocol (MCP), allowing AI assistants to upload documents,
                retrieve analysis results, and manage your document processing workflows programmatically.
            </p>
        </section>

        <section id="features" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Features</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <div>
                    <h3 class="text-lg font-medium text-gray-900 mb-3">Document Operations</h3>
                    <ul class="text-gray-600 space-y-2">
                        <li>• Upload documents for processing</li>
                        <li>• Retrieve document analysis results</li>
                        <li>• List and search documents</li>
                        <li>• Download processed documents</li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-lg font-medium text-gray-900 mb-3">Organization Management</h3>
                    <ul class="text-gray-600 space-y-2">
                        <li>• Manage tags and schemas</li>
                        <li>• Configure processing prompts</li>
                        <li>• Monitor processing status</li>
                        <li>• Access usage analytics</li>
                    </ul>
                </div>
            </div>
        </section>

        <section id="installation" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Installation</h2>
            <p class="text-gray-600 mb-6">Install the MCP server from the DocRouter repository:</p>

            <pre class="bg-gray-800 text-white p-4 rounded-lg overflow-x-auto mb-6"><code>pip install git+https://github.com/analytiq-hub/doc-router.git#subdirectory=mcp_server</code></pre>

            <p class="text-gray-600 mt-6 mb-6">Or clone and install in development mode:</p>

            <pre class="bg-gray-800 text-white p-4 rounded-lg overflow-x-auto mb-6"><code>git clone https://github.com/analytiq-hub/doc-router.git
cd doc-router/mcp_server
pip install -e .</code></pre>
        </section>

        <section id="configuration" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Configuration</h2>
            <p class="text-gray-600 mb-6">Configure the MCP server by adding it to your Claude Desktop configuration:</p>

            <pre class="bg-gray-800 text-white p-4 rounded-lg overflow-x-auto mb-6"><code>{
  "mcpServers": {
    "docrouter": {
      "command": "python",
      "args": ["-m", "docrouter_mcp"],
      "env": {
        "DOCROUTER_ORG_ID": "your-org-id",
        "DOCROUTER_TOKEN": "your-api-token"
      }
    }
  }
}</code></pre>

            <p class="text-gray-600 mt-6">Replace <code class="bg-gray-100 px-2 py-1 rounded">your-org-id</code> and <code class="bg-gray-100 px-2 py-1 rounded">your-api-token</code> with your actual DocRouter credentials.</p>
        </section>

        <section class="bg-gray-50 rounded-lg p-8">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4 text-center">Ready to Get Started?</h2>
            <div class="text-center">
                <p class="text-gray-600 mb-6">
                    Install the MCP server and start processing documents with AI assistance.
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
                        Get API Credentials
                    </a>
                </div>
            </div>
        </section>
    </main>
</div>