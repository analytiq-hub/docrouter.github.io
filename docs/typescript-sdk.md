---
layout: docs
title: "DocRouter TypeScript SDK"
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <header class="md:mb-12 mb-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
            <div>
                <p class="text-xl text-gray-600">Type-safe TypeScript client library for interacting with docrouter.ai</p>
            </div>
            <div class="rounded-xl border border-blue-200 bg-gradient-to-br from-blue-50 via-white to-purple-50 p-6 text-center shadow-lg">
                <a href="https://github.com/analytiq-hub/doc-router/tree/main/packages/typescript/docrouter-sdk"
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
                The DocRouter TypeScript SDK provides type-safe access to the DocRouter API, enabling developers to integrate document processing, OCR, LLM operations, and organization management into their applications. The SDK supports both Node.js and browser environments with comprehensive TypeScript support.
            </p>
            <ul class="list-disc list-inside text-gray-600 space-y-2">
                <li>Full TypeScript type definitions for enhanced developer experience</li>
                <li>Support for both server-side (Node.js) and client-side (browser) usage</li>
                <li>Comprehensive API coverage including documents, OCR, LLM, schemas, and more</li>
                <li>Built-in error handling with retry logic</li>
                <li>Streaming support for real-time LLM operations</li>
            </ul>
        </section>

        <section id="installation" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Installation</h2>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Prerequisites</h3>
            <ul class="list-disc list-inside text-gray-600 space-y-1 mb-6">
                <li>Node.js 16+ (for Node.js usage)</li>
                <li>TypeScript 4.9+ (recommended for type safety)</li>
                <li>DocRouter API access with appropriate tokens</li>
            </ul>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Install the Package</h3>
            <div class="bg-gray-50 rounded-lg p-4 mb-6">
                <code class="text-sm text-gray-800">npm install @docrouter/sdk</code>
            </div>

            <h3 class="text-lg font-medium text-gray-900 mb-3">TypeScript Configuration</h3>
            <p class="text-gray-600 mb-3">For optimal TypeScript support, ensure your <code class="bg-gray-100 px-2 py-1 rounded">tsconfig.json</code> includes:</p>
            <div class="bg-gray-50 rounded-lg p-4">
                <pre class="text-sm text-gray-800 overflow-x-auto"><code>{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "node",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  }
}</code></pre>
            </div>
        </section>

        <section id="quickstart" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Quick Start</h2>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Authentication</h3>
            <p class="text-gray-600 mb-4">The SDK supports three authentication strategies:</p>

            <div class="space-y-6 mb-6">
                <div class="border-l-4 border-blue-500 pl-4">
                    <h4 class="font-semibold text-gray-900 mb-2">1. Account Token (Server-to-Server)</h4>
                    <p class="text-gray-600 mb-3">Use <code class="bg-gray-100 px-2 py-1 rounded">DocRouterAccount</code> for account-level operations:</p>
                    <div class="bg-gray-50 rounded-lg p-4">
                        <pre class="text-sm text-gray-800 overflow-x-auto"><code>import { DocRouterAccount } from '@docrouter/sdk';

const client = new DocRouterAccount({
  baseURL: 'https://api.docrouter.com',
  accountToken: 'your-account-token-here'
});</code></pre>
                    </div>
                </div>

                <div class="border-l-4 border-green-500 pl-4">
                    <h4 class="font-semibold text-gray-900 mb-2">2. Organization Token</h4>
                    <p class="text-gray-600 mb-3">Use <code class="bg-gray-100 px-2 py-1 rounded">DocRouterOrg</code> for organization-scoped operations:</p>
                    <div class="bg-gray-50 rounded-lg p-4">
                        <pre class="text-sm text-gray-800 overflow-x-auto"><code>import { DocRouterOrg } from '@docrouter/sdk';

const client = new DocRouterOrg({
  baseURL: 'https://api.docrouter.com',
  orgToken: 'your-org-token-here',
  organizationId: 'org-123'
});</code></pre>
                    </div>
                </div>

                <div class="border-l-4 border-purple-500 pl-4">
                    <h4 class="font-semibold text-gray-900 mb-2">3. JWT Token (Browser)</h4>
                    <p class="text-gray-600 mb-3">Use <code class="bg-gray-100 px-2 py-1 rounded">DocRouterOrg</code> with JWT tokens for browser applications:</p>
                    <div class="bg-gray-50 rounded-lg p-4">
                        <pre class="text-sm text-gray-800 overflow-x-auto"><code>import { DocRouterOrg } from '@docrouter/sdk';

const client = new DocRouterOrg({
  baseURL: 'https://api.docrouter.com',
  orgToken: 'your-jwt-token-here',
  organizationId: 'your-org-id'
});</code></pre>
                    </div>
                </div>
            </div>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Basic Usage Example</h3>
            <div class="bg-gray-50 rounded-lg p-4">
                <pre class="text-sm text-gray-800 overflow-x-auto"><code>import { DocRouterOrg } from '@docrouter/sdk';

const client = new DocRouterOrg({
  baseURL: 'https://api.docrouter.com',
  orgToken: 'your-org-token',
  organizationId: 'org-123'
});

// Upload documents
const result = await client.uploadDocuments({
  documents: [
    {
      name: 'document.pdf',
      content: fileBuffer,
      type: 'application/pdf'
    }
  ]
});

// List documents
const documents = await client.listDocuments();

// Get document details
const document = await client.getDocument({
  documentId: 'doc-123',
  fileType: 'pdf'
});</code></pre>
            </div>
        </section>

        <section id="modules" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-6">SDK Modules</h2>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="border rounded-lg p-6 shadow-sm">
                    <h3 class="text-xl font-semibold text-gray-900 mb-3">Documents API</h3>
                    <p class="text-gray-600 mb-4">Manage documents in your workspace</p>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>Upload new documents</li>
                        <li>List documents with optional filtering</li>
                        <li>Get document details and content</li>
                        <li>Update document metadata</li>
                        <li>Delete documents</li>
                    </ul>
                </div>

                <div class="border rounded-lg p-6 shadow-sm">
                    <h3 class="text-xl font-semibold text-gray-900 mb-3">OCR API</h3>
                    <p class="text-gray-600 mb-4">Access document OCR data</p>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>Get OCR blocks with position data</li>
                        <li>Get OCR text from documents</li>
                        <li>Access document OCR metadata</li>
                        <li>Get OCR text for specific pages</li>
                    </ul>
                </div>

                <div class="border rounded-lg p-6 shadow-sm">
                    <h3 class="text-xl font-semibold text-gray-900 mb-3">LLM API</h3>
                    <p class="text-gray-600 mb-4">Run and manage LLM analysis</p>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>Run LLM analysis on documents</li>
                        <li>Run LLM chat with streaming support</li>
                        <li>Get LLM extraction results</li>
                        <li>Update and verify extraction results</li>
                        <li>List available LLM models</li>
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

                <div class="border rounded-lg p-6 shadow-sm">
                    <h3 class="text-xl font-semibold text-gray-900 mb-3">Forms API</h3>
                    <p class="text-gray-600 mb-4">Manage document forms</p>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>Create form definitions</li>
                        <li>List existing forms</li>
                        <li>Get form details</li>
                        <li>Submit form data</li>
                        <li>Update and delete forms</li>
                    </ul>
                </div>

                <div class="border rounded-lg p-6 shadow-sm">
                    <h3 class="text-xl font-semibold text-gray-900 mb-3">Organization Management</h3>
                    <p class="text-gray-600 mb-4">Account-level operations</p>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>Organization CRUD operations</li>
                        <li>Token creation and management</li>
                        <li>User management</li>
                        <li>Subscription and billing</li>
                    </ul>
                </div>
            </div>
        </section>

        <section id="features" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-6">Key Features</h2>

            <div class="space-y-6">
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">Type Safety</h3>
                    <p class="text-gray-600">Full TypeScript support with comprehensive type definitions for all API operations, ensuring type safety and excellent IDE autocomplete support.</p>
                </div>

                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">Error Handling</h3>
                    <p class="text-gray-600">Built-in error handling with retry logic and authentication callbacks for robust API interactions.</p>
                </div>

                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">Streaming Support</h3>
                    <p class="text-gray-600">Real-time streaming for LLM operations with <code class="bg-gray-100 px-2 py-1 rounded">runLLMChatStream()</code>, perfect for building interactive chat interfaces.</p>
                </div>

                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">Browser & Node.js</h3>
                    <p class="text-gray-600">Works seamlessly in both Node.js server environments and browser applications with proper polyfills.</p>
                </div>

                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">Environment Configuration</h3>
                    <p class="text-gray-600">Easy configuration for different environments (development, staging, production) with support for custom HTTP client settings.</p>
                </div>
            </div>
        </section>

        <section id="examples" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-6">Example Use Cases</h2>

            <div class="space-y-6">
                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">Document Processing Workflow</h3>
                    <div class="bg-gray-50 rounded-lg p-4">
                        <pre class="text-sm text-gray-800 overflow-x-auto"><code>// Upload, OCR, and extract data
const uploadResult = await client.uploadDocuments({
  documents: [{ name: 'invoice.pdf', content: buffer, type: 'application/pdf' }]
});

const docId = uploadResult.documents[0].id;

// Get OCR text
const ocrText = await client.getOCRText({ documentId: docId });

// Run LLM extraction
const llmResult = await client.runLLM({
  documentId: docId,
  promptRevId: 'prompt-123'
});</code></pre>
                    </div>
                </div>

                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">Streaming LLM Chat</h3>
                    <div class="bg-gray-50 rounded-lg p-4">
                        <pre class="text-sm text-gray-800 overflow-x-auto"><code>// Real-time streaming chat
await client.runLLMChatStream({
  messages: [
    { role: 'user', content: 'Analyze this document' }
  ],
  model: 'gpt-4'
}, (chunk) => {
  console.log('Received:', chunk);
}, (error) => {
  console.error('Error:', error);
});</code></pre>
                    </div>
                </div>

                <div>
                    <h3 class="text-lg font-semibold text-gray-900 mb-2">Browser File Upload</h3>
                    <div class="bg-gray-50 rounded-lg p-4">
                        <pre class="text-sm text-gray-800 overflow-x-auto"><code>// Upload from browser file input
const fileInput = document.getElementById('fileInput');
const file = fileInput.files[0];
const fileBuffer = await file.arrayBuffer();

const result = await client.uploadDocuments({
  documents: [{
    name: file.name,
    content: fileBuffer,
    type: file.type
  }]
});</code></pre>
                    </div>
                </div>
            </div>
        </section>

        <section id="github" class="bg-gradient-to-r from-blue-600 to-blue-800 rounded-lg shadow-lg p-8 mb-12">
            <div class="text-center">
                <span class="text-2xl font-semibold text-white mb-4">
                <h2>GitHub Repository</h2>
                </span>
                <p class="text-blue-100 mb-6">
                    The DocRouter TypeScript SDK is part of the docrouter.ai open source project.
                    You can find the source code, examples, and full documentation on GitHub.
                </p>
                <a href="https://github.com/analytiq-hub/doc-router/tree/main/packages/typescript/docrouter-sdk"
                   target="_blank"
                   rel="noopener noreferrer"
                   class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-8 py-3 rounded-lg font-medium transition-colors duration-200 no-underline">
                    View on GitHub
                </a>
            </div>
        </section>
    </main>

    <footer class="mt-12 text-center text-gray-600">
        <p>© 2025 DocRouter TypeScript SDK. Part of the <a href="https://github.com/analytiq-hub/doc-router" class="text-blue-600 hover:text-blue-800">docrouter.ai</a> project.</p>
    </footer>
</div>
