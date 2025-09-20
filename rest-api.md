---
layout: page
title: DocRouter REST API
permalink: /rest-api/
---

<div class="flex flex-col lg:flex-row lg:justify-between lg:items-start gap-3 mb-8">
  <div class="flex-1">
    <p class="text-lg text-gray-600 leading-relaxed">
      Anything in the DocRouter UI is also available through REST APIs. The DocRouter UI runs on top of the same REST API available for external integrations.
    </p>
  </div>

  <div class="lg:w-80">
    <div class="bg-gradient-to-r from-blue-500 to-blue-600 rounded-lg p-4 text-white shadow-lg flex flex-col items-center text-center">
      <p class="text-blue-100 mb-3">Jump to our interactive REST API docs</p>
      <a href="https://app.docrouter.ai/fastapi/docs#/" target="_blank" rel="noopener noreferrer"
         class="inline-flex items-center gap-2 bg-white text-blue-600 px-4 py-2 rounded-md font-medium hover:bg-blue-50 transition-colors">
        <span>Open Swagger UI</span>
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
        </svg>
      </a>
    </div>
  </div>
</div>

## Authentication

The DocRouter REST API uses token-based authentication with two types of tokens:

<div class="grid md:grid-cols-2 gap-6 my-6">
  <div class="bg-blue-50 border border-blue-200 rounded-lg p-6">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-10 h-10 bg-blue-500 rounded-lg flex items-center justify-center mt-3">
        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0h3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
        </svg>
      </div>
      <h3 class="text-xl font-semibold text-blue-900">Account-Level Tokens</h3>
    </div>
    <div class="space-y-3 text-blue-800">
      <div class="flex items-start gap-2">
        <span class="font-medium">Scope:</span>
        <span>For APIs under <code class="bg-blue-100 px-2 py-1 rounded text-sm">/v0/account</code></span>
      </div>
      <div class="flex items-start gap-2">
        <span class="font-medium">Creation:</span>
        <span>Go to Settings > Account Tokens</span>
      </div>
    </div>
  </div>

  <div class="bg-green-50 border border-green-200 rounded-lg p-6">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-10 h-10 bg-green-500 rounded-lg flex items-center justify-center mt-3">
        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0h3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
        </svg>
      </div>
      <h3 class="text-xl font-semibold text-green-900">Organization-Level Tokens</h3>
    </div>
    <div class="space-y-3 text-green-800">
      <div class="flex items-start gap-2">
        <span class="font-medium">Scope:</span>
        <span>For APIs under <code class="bg-green-100 px-2 py-1 rounded text-sm">/v0/orgs/{organization_id}</code></span>
      </div>
      <div class="flex items-start gap-2">
        <span class="font-medium">Creation:</span>
        <span>Go to Settings > Organizations Tokens</span>
      </div>
    </div>
  </div>
</div>

## API Examples

<div class="mt-6">
  <!-- Tab Navigation -->
  <div class="border-b border-gray-200">
    <nav class="-mb-px flex space-x-8">
      <button onclick="switchTab('account')" id="account-tab" class="tab-button active py-2 px-1 border-b-2 border-blue-500 font-medium text-sm text-blue-600">
        Account-Level APIs
      </button>
      <button onclick="switchTab('organization')" id="organization-tab" class="tab-button py-2 px-1 border-b-2 border-transparent font-medium text-sm text-gray-500 hover:text-gray-700 hover:border-gray-300">
        Organization-Level APIs
      </button>
    </nav>
  </div>

  <!-- Tab Content -->
  <div class="mt-6">
    <!-- Account Tab Content -->
    <div id="account-content" class="tab-content">
      List All Organizations That The User Can Access
      
      <div class="mb-4">
        <h4 class="text-sm font-medium text-gray-700 mb-2">Request:</h4>
        <pre class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto"><code>curl -X GET "https://app.docrouter.ai/fastapi/v0/account/organizations" \
     -H "Authorization: Bearer YOUR_ACCOUNT_TOKEN" \
     -H "Content-Type: application/json"</code></pre>
      </div>

      <div>
        <h4 class="text-sm font-medium text-gray-700 mb-2">Example Response:</h4>
        <pre class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto"><code>{
  "organizations": [
    {
      "id": "12345678abcdef123456789a",
      "name": "my-organization",
      "members": [
        {
          "user_id": "12345678abcdef123456789b",
          "role": "admin"
        },
        {
          "user_id": "12345678abcdef123456789c",
          "role": "user"
        }
      ],
      "type": "team",
      "created_at": "2025-01-15T10:30:00.000000",
      "updated_at": "2025-01-15T14:20:00.000000"
    }
  ]
}</code></pre>
      </div>
    </div>

    <!-- Organization Tab Content -->
    <div id="organization-content" class="tab-content hidden">
      List All Documents In The Organization
      
      <div class="mb-4">
        <h4 class="text-sm font-medium text-gray-700 mb-2">Request:</h4>
        <pre class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto"><code>curl -X GET "https://app.docrouter.ai/fastapi/v0/orgs/12345678abcdef123456789a/documents" \
     -H "Authorization: Bearer YOUR_ORGANIZATION_TOKEN" \
     -H "Content-Type: application/json"</code></pre>
      </div>

      <div>
        <h4 class="text-sm font-medium text-gray-700 mb-2">Example Response:</h4>
        <pre class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto"><code>{
  "documents": [
    {
      "id": "12345678abcdef123456789d",
      "pdf_id": "12345678abcdef123456789e",
      "document_name": "invoice_2025_001.pdf",
      "upload_date": "2025-01-15T10:30:00.000000Z",
      "uploaded_by": "John Doe",
      "state": "llm_completed",
      "tag_ids": ["12345678abcdef123456789f"],
      "type": "invoice",
      "metadata": {}
    },
    {
      "id": "12345678abcdef123456789g",
      "pdf_id": "12345678abcdef123456789h",
      "document_name": "contract_agreement.pdf",
      "upload_date": "2025-01-14T15:20:00.000000Z",
      "uploaded_by": "Jane Smith",
      "state": "processing",
      "tag_ids": ["12345678abcdef123456789i"],
      "type": "contract",
      "metadata": {}
    }
  ],
  "total_count": 2,
  "skip": 0
}</code></pre>
      </div>
    </div>
  </div>
</div>

<script>
function switchTab(tabName) {
  // Hide all tab contents
  document.querySelectorAll('.tab-content').forEach(content => {
    content.classList.add('hidden');
  });
  
  // Remove active class from all tabs
  document.querySelectorAll('.tab-button').forEach(button => {
    button.classList.remove('active', 'border-blue-500', 'text-blue-600');
    button.classList.add('border-transparent', 'text-gray-500');
  });
  
  // Show selected tab content
  document.getElementById(tabName + '-content').classList.remove('hidden');
  
  // Add active class to selected tab
  const activeTab = document.getElementById(tabName + '-tab');
  activeTab.classList.add('active', 'border-blue-500', 'text-blue-600');
  activeTab.classList.remove('border-transparent', 'text-gray-500');
}
</script>

<div class="flex flex-col lg:flex-row lg:justify-between lg:items-start gap-3 mb-8">
  <div class="flex-1">
        <p class="text-lg text-gray-600 leading-relaxed">
          For complete API documentation with interactive testing capabilities, visit our <a href="https://app.docrouter.ai/fastapi/docs#/" target="_blank" rel="noopener noreferrer" class="font-semibold text-blue-600 hover:text-blue-800 transition-colors">Swagger</a> and <a href="https://app.docrouter.ai/fastapi/openapi.json" target="_blank" rel="noopener noreferrer" class="font-semibold text-blue-600 hover:text-blue-800 transition-colors">OpenAPI documentation</a>.
        </p>
  </div>
</div>


<div class="bg-gradient-to-br from-gray-50 to-gray-100 border border-gray-200 rounded-xl p-8 my-8">
  <div class="text-center mb-8">
    <div class="inline-flex items-center gap-3 mb-4">
      <div class="w-12 h-12 mt-3 bg-indigo-500 rounded-xl flex items-center justify-center">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
        </svg>
      </div>
      <h2 class="text-2xl font-bold text-gray-900">Using the Swagger Interface</h2>
    </div>
    <p class="text-gray-600 text-lg">Follow these simple steps to get started with our interactive API documentation</p>
  </div>

  <div class="grid md:grid-cols-3 gap-6">
    <!-- Step 1: Authentication -->
    <div class="bg-white rounded-lg p-6 border border-gray-200 shadow-sm hover:shadow-md transition-shadow">
      <div class="flex items-center gap-3 mb-4">
        <div class="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center text-white font-bold text-sm">1</div>
        <h3 class="text-lg font-semibold text-gray-900">Authentication Setup</h3>
      </div>
      <ul class="space-y-3 text-gray-700 leading-relaxed">
        <li>Click the <span class="font-semibold text-blue-600">"Authorize"</span> button at the top of the Swagger page</li>
        <li>Enter your API token (account or organization-level depending on the endpoint)</li>
        <li>Click <span class="font-semibold text-blue-600">"Authorize"</span> to authenticate your session</li>
      </ul>
    </div>

    <!-- Step 2: Testing Endpoints -->
    <div class="bg-white rounded-lg p-6 border border-gray-200 shadow-sm hover:shadow-md transition-shadow">
      <div class="flex items-center gap-3 mb-4">
        <div class="w-8 h-8 bg-green-500 rounded-full flex items-center justify-center text-white font-bold text-sm">2</div>
        <h3 class="text-lg font-semibold text-gray-900">Testing API Endpoints</h3>
      </div>
      <ul class="space-y-3 text-gray-700 leading-relaxed">
        <li>Browse the available endpoints organized by category</li>
        <li>Click on any endpoint to expand its details</li>
        <li>Click <span class="font-semibold text-green-600">"Try it out"</span> to enable the interactive form</li>
        <li>Fill in required parameters and request body, then click <span class="font-semibold text-green-600">"Execute"</span></li>
      </ul>
    </div>

    <!-- Step 3: cURL Commands -->
    <div class="bg-white rounded-lg p-6 border border-gray-200 shadow-sm hover:shadow-md transition-shadow">
      <div class="flex items-center gap-3 mb-4">
        <div class="w-8 h-8 bg-purple-500 rounded-full flex items-center justify-center text-white font-bold text-sm">3</div>
        <h3 class="text-lg font-semibold text-gray-900">Generating cURL Commands</h3>
      </div>
      <ul class="space-y-3 text-gray-700 leading-relaxed">
        <li>After executing an API call, scroll down to the <span class="font-semibold text-purple-600">"Response"</span> section</li>
        <li>Find the <span class="font-semibold text-purple-600">"Curl"</span> tab to see the equivalent cURL command</li>
        <li>Copy the command to use in your terminal or scripts</li>
      </ul>
    </div>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-6 my-6">
  <!-- OpenAPI Specification Panel -->
  <div class="bg-gradient-to-br from-blue-50 to-blue-100 border border-blue-200 rounded-lg p-6">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-10 h-10 bg-blue-500 rounded-lg flex items-center justify-center">
        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
        </svg>
      </div>
      <h3 class="text-xl font-semibold text-blue-900">OpenAPI Specification</h3>
    </div>
    <p class="text-blue-800 mb-4">Access the complete OpenAPI schema</p>
    <a href="https://app.docrouter.ai/fastapi/openapi.json" target="_blank" rel="noopener noreferrer"
       class="inline-flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded-md font-medium hover:bg-blue-700 hover:text-white transition-colors shadow-md hover:shadow-lg">
      <span class="text-white">View OpenAPI JSON</span>
      <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
      </svg>
    </a>
  </div>

  <!-- Client Libraries Panel -->
  <div class="bg-gradient-to-br from-green-50 to-green-100 border border-green-200 rounded-lg p-6">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-10 h-10 bg-green-500 rounded-lg flex items-center justify-center">
        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
        </svg>
      </div>
      <h3 class="text-xl font-semibold text-green-900">Client Libraries</h3>
    </div>
    <p class="text-green-800 mb-4">Ready-to-use SDKs and code generation</p>
    <div class="space-y-3">
      <div class="flex items-center justify-between bg-white rounded-md p-3 border border-green-200">
        <div>
          <a href="/python-sdk/" class="text-green-700 hover:text-green-800 font-medium">Python SDK</a>
          <p class="text-green-600 text-sm">Official client library</p>
        </div>
        <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
      </div>
      <div class="flex items-center justify-between bg-white rounded-md p-3 border border-green-200">
        <div>
          <a href="https://openapi-generator.tech/" target="_blank" rel="noopener noreferrer" class="text-green-700 hover:text-green-800 font-medium">OpenAPI Generator</a>
          <p class="text-green-600 text-sm">Generate clients for TypeScript, Rust, Go, Java, and more</p>
        </div>
        <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
        </svg>
      </div>
    </div>
  </div>
</div>
