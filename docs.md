---
layout: default
title: "Documentation - DocRouter.AI"
permalink: /docs/
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <header class="text-center md:mb-12 mb-8">
        <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
            DocRouter.AI Documentation
        </h1>
        <p class="text-xl text-gray-600 max-w-2xl mx-auto">
            Everything you need to set up tags, prompts, schemas, and integrations for AI-powered document processing.
        </p>
    </header>

    <main>
        <section class="bg-white rounded-lg shadow-lg p-6 md:p-8 mb-8">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Getting started</h2>
            <ul class="space-y-3 text-gray-600">
                <li><a href="{{ '/docs/how-it-works/' | relative_url }}" class="text-blue-600 hover:text-blue-800">How It Works</a> — High-level workflow and concepts</li>
                <li><a href="{{ '/docs/quick-start/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Quick Start Guide</a> — Tag, prompt, upload in minutes</li>
            </ul>
        </section>

        <section class="bg-white rounded-lg shadow-lg p-6 md:p-8 mb-8">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Core concepts</h2>
            <ul class="space-y-3 text-gray-600">
                <li><a href="{{ '/docs/tags/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Tags</a> — Route documents to the right prompts</li>
                <li><a href="{{ '/docs/prompts/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Prompts</a> — Instructions for data extraction</li>
                <li><a href="{{ '/docs/schemas/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Schemas</a> — Structured output and validation</li>
                <li><a href="{{ '/docs/knowledge-bases/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Knowledge Bases</a> — Context for better accuracy</li>
                <li><a href="{{ '/docs/chat-agents/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Chat Agents</a> — Chat with your documents</li>
            </ul>
        </section>

        <section class="bg-white rounded-lg shadow-lg p-6 md:p-8 mb-8">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">APIs &amp; SDKs</h2>
            <ul class="space-y-3 text-gray-600">
                <li><a href="{{ '/docs/rest-api/' | relative_url }}" class="text-blue-600 hover:text-blue-800">REST API</a> — Upload, manage, and query programmatically</li>
                <li><a href="{{ '/docs/webhooks/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Webhooks</a> — Real-time events and workflows</li>
                <li><a href="{{ '/docs/workflows/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Workflows</a> — N8N, Temporal, and automation</li>
                <li><a href="{{ '/docs/python-sdk/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Python SDK</a> — Python client</li>
                <li><a href="{{ '/docs/typescript-sdk/' | relative_url }}" class="text-blue-600 hover:text-blue-800">TypeScript SDK</a> — TypeScript/Node client</li>
            </ul>
        </section>

        <section class="bg-white rounded-lg shadow-lg p-6 md:p-8 mb-8">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Integrations</h2>
            <ul class="space-y-3 text-gray-600">
                <li><a href="{{ '/docs/integrations/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Integrations</a> — Overview of integration options</li>
                <li><a href="{{ '/docs/n8n/' | relative_url }}" class="text-blue-600 hover:text-blue-800">N8N</a> — Visual workflow automation</li>
                <li><a href="{{ '/docs/temporal/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Temporal</a> — Durable workflow orchestration</li>
                <li><a href="{{ '/docs/mcp/' | relative_url }}" class="text-blue-600 hover:text-blue-800">MCP Server</a> — Use DocRouter from AI assistants</li>
                <li><a href="{{ '/docs/claude-code/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Claude Code</a> — DocRouter in Claude Code</li>
                <li><a href="{{ '/docs/cursor/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Cursor</a> — DocRouter in Cursor</li>
                <li><a href="{{ '/docs/github-copilot/' | relative_url }}" class="text-blue-600 hover:text-blue-800">GitHub Copilot</a> — DocRouter in GitHub Copilot</li>
            </ul>
        </section>

        <section class="bg-blue-50 rounded-lg p-6 md:p-8 border border-blue-100">
            <div class="flex flex-wrap items-center justify-center gap-3">
                <h2 class="text-xl font-semibold text-gray-900 m-0">Need help?</h2>
                <a href="{{ '/support/' | relative_url }}" class="inline-block bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 no-underline">
                    Support
                </a>
                <a href="{{ '/contact/' | relative_url }}" class="inline-block bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 no-underline">
                    Contact us
                </a>
                <a href="https://app.docrouter.ai" target="_blank" rel="noopener noreferrer" class="inline-block bg-white text-blue-600 border-2 border-blue-600 px-6 py-3 rounded-lg font-semibold hover:bg-blue-50 no-underline">
                    Open DocRouter App
                </a>
            </div>
        </section>
    </main>
</div>
