---
layout: docs
title: "DocRouter Python SDK"
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <header class="md:mb-12 mb-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
            <div>
                <p class="text-xl text-gray-600">Python client library for interacting with docrouter.ai</p>
            </div>
            <div class="rounded-xl border border-blue-200 bg-gradient-to-br from-blue-50 via-white to-purple-50 p-6 text-center shadow-lg">
                <a href="https://colab.research.google.com/github/analytiq-hub/docrouter.github.io/blob/main/notebooks/python_sdk/onboarding.ipynb"
                   target="_blank"
                   rel="noopener noreferrer"
                   class="inline-flex items-center bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white px-6 py-3 rounded-lg font-medium transition-colors duration-200">
                    <svg class="w-5 h-5 mr-2 text-white" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
                    </svg>
                    <span class="text-white">Open in Google Colab</span>
                </a>
            </div>
        </div>
    </header>

    <main>
        <section id="overview" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Overview</h2>
            <p class="text-gray-600 mb-0">
                The DocRouter Python SDK gives programmatic access to documents, OCR, LLM analysis, schemas, prompts, and tags—so you can automate document workflows and extract structured data directly from your apps.
            </p>
        </section>

        <section id="quickstart" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Quick Start</h2>

            <p class="text-gray-600 mb-4">To get started with the DocRouter SDK:</p>

            <ol class="list-decimal list-inside text-gray-600 space-y-2 mb-6">
                <li>Install the DocRouter SDK from PyPI: <code>pip install docrouter_sdk</code></li>
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
                   class="inline-flex items-center bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 px-5 py-2.5 rounded-lg font-medium text-white transition-colors duration-200">
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

        <section id="github" class="bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg shadow-lg p-8 mb-12">
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