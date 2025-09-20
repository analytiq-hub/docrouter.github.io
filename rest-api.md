---
layout: page
title: DocRouter REST API
permalink: /rest-api/
---

<!-- Hero Section -->
<div class="bg-gradient-to-br from-blue-50 via-white to-indigo-50 rounded-2xl p-8 mb-12 border border-blue-100">
  <div class="max-w-4xl mx-auto text-center">
    <div class="inline-flex items-center justify-center w-16 h-16 bg-blue-500 rounded-2xl mb-6">
      <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v14a2 2 0 002 2z"/>
      </svg>
    </div>
    <h2 class="text-2xl font-bold text-gray-900 mb-4">Complete API Access</h2>
    <p class="text-lg text-gray-600 leading-relaxed mb-8 max-w-3xl mx-auto">
      Everything in the DocRouter UI is available through REST APIs. Build custom integrations, automate workflows, and access all features programmatically.
    </p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
      <a href="https://app.docrouter.ai/fastapi/docs#/" target="_blank" rel="noopener noreferrer"
         class="inline-flex items-center gap-2 bg-blue-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-blue-700 transition-colors shadow-lg hover:shadow-xl">
        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
        </svg>
        <span class="text-white">Interactive API Docs</span>
      </a>
      <a href="https://app.docrouter.ai/fastapi/openapi.json" target="_blank" rel="noopener noreferrer"
         class="inline-flex items-center gap-2 bg-white text-blue-600 px-6 py-3 rounded-lg font-medium hover:bg-blue-50 transition-colors border border-blue-200">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
        </svg>
        <span>OpenAPI Schema</span>
      </a>
    </div>
  </div>
</div>

## Authentication

<div class="bg-gray-50 rounded-xl p-6 mb-8 border border-gray-200">
  <p class="text-gray-700 leading-relaxed mb-6">
    The DocRouter REST API uses token-based authentication. Choose the appropriate token type based on your integration needs:
  </p>
  
  <div class="grid md:grid-cols-2 gap-6">
    <div class="bg-white border border-blue-200 rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow">
      <div class="flex items-center gap-3 mb-4">
        <div class="w-12 h-12 bg-blue-500 rounded-xl flex items-center justify-center">
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
          </svg>
        </div>
        <div>
          <h3 class="text-lg font-semibold text-gray-900">Account-Level Tokens</h3>
          <p class="text-sm text-gray-600">User-scoped access</p>
        </div>
      </div>
      <div class="space-y-3">
        <div class="flex items-start gap-3">
          <div class="w-2 h-2 bg-blue-500 rounded-full mt-2 flex-shrink-0"></div>
          <div>
            <span class="font-medium text-gray-900">Scope:</span>
            <span class="text-gray-700">APIs under <code class="bg-blue-50 text-blue-700 px-2 py-1 rounded text-sm font-mono">/v0/account</code></span>
          </div>
        </div>
        <div class="flex items-start gap-3">
          <div class="w-2 h-2 bg-blue-500 rounded-full mt-2 flex-shrink-0"></div>
          <div>
            <span class="font-medium text-gray-900">Creation:</span>
            <span class="text-gray-700">Settings → Account Tokens</span>
          </div>
        </div>
      </div>
    </div>

    <div class="bg-white border border-green-200 rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow">
      <div class="flex items-center gap-3 mb-4">
        <div class="w-12 h-12 bg-green-500 rounded-xl flex items-center justify-center">
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0h3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
          </svg>
        </div>
        <div>
          <h3 class="text-lg font-semibold text-gray-900">Organization-Level Tokens</h3>
          <p class="text-sm text-gray-600">Team-scoped access</p>
        </div>
      </div>
      <div class="space-y-3">
        <div class="flex items-start gap-3">
          <div class="w-2 h-2 bg-green-500 rounded-full mt-2 flex-shrink-0"></div>
          <div>
            <span class="font-medium text-gray-900">Scope:</span>
            <span class="text-gray-700">APIs under <code class="bg-green-50 text-green-700 px-2 py-1 rounded text-sm font-mono">/v0/orgs/{organization_id}</code></span>
          </div>
        </div>
        <div class="flex items-start gap-3">
          <div class="w-2 h-2 bg-green-500 rounded-full mt-2 flex-shrink-0"></div>
          <div>
            <span class="font-medium text-gray-900">Creation:</span>
            <span class="text-gray-700">Settings → Organization Tokens</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

## API Examples

<div class="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
  <!-- Tab Navigation -->
  <div class="bg-gray-50 border-b border-gray-200 px-6">
    <nav class="flex space-x-8">
      <button onclick="switchTab('account')" id="account-tab" class="tab-button active py-4 px-1 border-b-2 border-blue-500 font-medium text-sm text-blue-600">
        Account-Level APIs
      </button>
      <button onclick="switchTab('organization')" id="organization-tab" class="tab-button py-4 px-1 border-b-2 border-transparent font-medium text-sm text-gray-500 hover:text-gray-700 hover:border-gray-300">
        Organization-Level APIs
      </button>
    </nav>
  </div>

  <!-- Tab Content -->
  <div class="p-6">
    <!-- Account Tab Content -->
    <div id="account-content" class="tab-content">
      <div class="mb-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-2">List All Organizations</h3>
        <p class="text-gray-600">Retrieve all organizations that the authenticated user can access.</p>
      </div>
      
      <div class="space-y-6">
        <div>
          <h4 class="text-sm font-medium text-gray-900 mb-3 flex items-center gap-2">
            <svg class="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v14a2 2 0 002 2z"/>
            </svg>
            Request
          </h4>
          <pre class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto border border-gray-700"><code>curl -X GET "https://app.docrouter.ai/fastapi/v0/account/organizations" \
     -H "Authorization: Bearer YOUR_ACCOUNT_TOKEN" \
     -H "Content-Type: application/json"</code></pre>
        </div>

        <div>
          <h4 class="text-sm font-medium text-gray-900 mb-3 flex items-center gap-2">
            <svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            Response
          </h4>
          <pre class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto border border-gray-700"><code>{
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
    </div>

    <!-- Organization Tab Content -->
    <div id="organization-content" class="tab-content hidden">
      <div class="mb-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-2">List All Documents</h3>
        <p class="text-gray-600">Retrieve all documents within a specific organization.</p>
      </div>
      
      <div class="space-y-6">
        <div>
          <h4 class="text-sm font-medium text-gray-900 mb-3 flex items-center gap-2">
            <svg class="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v14a2 2 0 002 2z"/>
            </svg>
            Request
          </h4>
          <pre class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto border border-gray-700"><code>curl -X GET "https://app.docrouter.ai/fastapi/v0/orgs/12345678abcdef123456789a/documents" \
     -H "Authorization: Bearer YOUR_ORGANIZATION_TOKEN" \
     -H "Content-Type: application/json"</code></pre>
        </div>

        <div>
          <h4 class="text-sm font-medium text-gray-900 mb-3 flex items-center gap-2">
            <svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            Response
          </h4>
          <pre class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto border border-gray-700"><code>{
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



## Interactive Documentation

<div class="bg-gradient-to-br from-indigo-50 via-white to-blue-50 rounded-2xl p-8 mb-8 border border-indigo-100">
  <div class="text-center mb-8">
    <div class="inline-flex items-center justify-center w-16 h-16 bg-indigo-500 rounded-2xl mb-6">
      <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
      </svg>
    </div>
    <h2 class="text-2xl font-bold text-gray-900 mb-4">Get Started with Swagger UI</h2>
    <p class="text-lg text-gray-600 max-w-2xl mx-auto">
      Our interactive API documentation makes it easy to test endpoints, generate code samples, and understand the API structure.
    </p>
  </div>

  <div class="grid md:grid-cols-3 gap-6">
    <!-- Step 1: Authentication -->
    <div class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm hover:shadow-lg transition-all duration-200">
      <div class="flex items-center gap-3 mb-4">
        <div class="w-10 h-10 bg-blue-500 rounded-xl flex items-center justify-center text-white font-bold text-sm">1</div>
        <h3 class="text-lg font-semibold text-gray-900">Authenticate</h3>
      </div>
      <ul class="space-y-3 text-gray-700 leading-relaxed">
        <li class="flex items-start gap-2">
          <div class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-2 flex-shrink-0"></div>
          <span>Click the <span class="font-semibold text-blue-600">"Authorize"</span> button</span>
        </li>
        <li class="flex items-start gap-2">
          <div class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-2 flex-shrink-0"></div>
          <span>Enter your API token</span>
        </li>
        <li class="flex items-start gap-2">
          <div class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-2 flex-shrink-0"></div>
          <span>Click <span class="font-semibold text-blue-600">"Authorize"</span> to authenticate</span>
        </li>
      </ul>
    </div>

    <!-- Step 2: Testing Endpoints -->
    <div class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm hover:shadow-lg transition-all duration-200">
      <div class="flex items-center gap-3 mb-4">
        <div class="w-10 h-10 bg-green-500 rounded-xl flex items-center justify-center text-white font-bold text-sm">2</div>
        <h3 class="text-lg font-semibold text-gray-900">Test Endpoints</h3>
      </div>
      <ul class="space-y-3 text-gray-700 leading-relaxed">
        <li class="flex items-start gap-2">
          <div class="w-1.5 h-1.5 bg-green-500 rounded-full mt-2 flex-shrink-0"></div>
          <span>Browse endpoints by category</span>
        </li>
        <li class="flex items-start gap-2">
          <div class="w-1.5 h-1.5 bg-green-500 rounded-full mt-2 flex-shrink-0"></div>
          <span>Click <span class="font-semibold text-green-600">"Try it out"</span> to enable forms</span>
        </li>
        <li class="flex items-start gap-2">
          <div class="w-1.5 h-1.5 bg-green-500 rounded-full mt-2 flex-shrink-0"></div>
          <span>Fill parameters and click <span class="font-semibold text-green-600">"Execute"</span></span>
        </li>
      </ul>
    </div>

    <!-- Step 3: cURL Commands -->
    <div class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm hover:shadow-lg transition-all duration-200">
      <div class="flex items-center gap-3 mb-4">
        <div class="w-10 h-10 bg-purple-500 rounded-xl flex items-center justify-center text-white font-bold text-sm">3</div>
        <h3 class="text-lg font-semibold text-gray-900">Generate Code</h3>
      </div>
      <ul class="space-y-3 text-gray-700 leading-relaxed">
        <li class="flex items-start gap-2">
          <div class="w-1.5 h-1.5 bg-purple-500 rounded-full mt-2 flex-shrink-0"></div>
          <span>View the <span class="font-semibold text-purple-600">"Response"</span> section</span>
        </li>
        <li class="flex items-start gap-2">
          <div class="w-1.5 h-1.5 bg-purple-500 rounded-full mt-2 flex-shrink-0"></div>
          <span>Find the <span class="font-semibold text-purple-600">"Curl"</span> tab</span>
        </li>
        <li class="flex items-start gap-2">
          <div class="w-1.5 h-1.5 bg-purple-500 rounded-full mt-2 flex-shrink-0"></div>
          <span>Copy commands for your scripts</span>
        </li>
      </ul>
    </div>
  </div>
</div>

## Resources & Tools

<div class="grid md:grid-cols-2 gap-6">
  <!-- OpenAPI Specification Panel -->
  <div class="bg-white border border-gray-200 rounded-xl p-6 shadow-sm hover:shadow-lg transition-shadow">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-12 h-12 bg-blue-500 rounded-xl flex items-center justify-center">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
        </svg>
      </div>
      <div>
        <h3 class="text-lg font-semibold text-gray-900">OpenAPI Specification</h3>
        <p class="text-sm text-gray-600">Complete API schema</p>
      </div>
    </div>
    <p class="text-gray-700 mb-4">Access the complete OpenAPI 3.0 specification for code generation and API exploration.</p>
    <a href="https://app.docrouter.ai/fastapi/openapi.json" target="_blank" rel="noopener noreferrer"
       class="inline-flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded-lg font-medium hover:bg-blue-700 transition-colors">
      <span class="text-white">View OpenAPI JSON</span>
      <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
      </svg>
    </a>
  </div>

  <!-- Client Libraries Panel -->
  <div class="bg-white border border-gray-200 rounded-xl p-6 shadow-sm hover:shadow-lg transition-shadow">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-12 h-12 bg-green-500 rounded-xl flex items-center justify-center">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
        </svg>
      </div>
      <div>
        <h3 class="text-lg font-semibold text-gray-900">Client Libraries</h3>
        <p class="text-sm text-gray-600">SDKs and code generation</p>
      </div>
    </div>
    <p class="text-gray-700 mb-4">Ready-to-use SDKs and tools for generating client libraries in your preferred language.</p>
    <div class="space-y-3">
      <a href="/python-sdk/" class="flex items-center justify-between bg-gray-50 hover:bg-gray-100 rounded-lg p-3 transition-colors group">
        <div>
          <span class="font-medium text-gray-900 group-hover:text-green-600">Python SDK</span>
          <p class="text-sm text-gray-600">Official client library</p>
        </div>
        <svg class="w-5 h-5 text-gray-400 group-hover:text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
      </a>
      <a href="https://openapi-generator.tech/" target="_blank" rel="noopener noreferrer" class="flex items-center justify-between bg-gray-50 hover:bg-gray-100 rounded-lg p-3 transition-colors group">
        <div>
          <span class="font-medium text-gray-900 group-hover:text-green-600">OpenAPI Generator</span>
          <p class="text-sm text-gray-600">Generate clients for TypeScript, Rust, Go, Java, and more</p>
        </div>
        <svg class="w-5 h-5 text-gray-400 group-hover:text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
        </svg>
      </a>
    </div>
  </div>
</div>
