---
layout: docs
title: "DocRouter REST API Reference"
permalink: /docs/rest-api/
description: "Access all DocRouter features via REST API. Upload documents, manage schemas and prompts, retrieve extracted data, and build custom integrations programmatically."
---

<!-- Hero Section -->
<div class="bg-gradient-to-br from-blue-50 via-white to-purple-50 rounded-2xl p-4 md:p-8 mb-8 md:mb-12 border border-blue-100 shadow-lg">
  <div class="max-w-4xl mx-auto text-center">
    <p class="text-lg text-gray-600 leading-relaxed mb-8 max-w-3xl mx-auto">
      Everything in the DocRouter UI is available through REST APIs. Build custom integrations, automate workflows, and access all features programmatically.
    </p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
      <a href="https://app.docrouter.ai/fastapi/docs#/" target="_blank" rel="noopener noreferrer"
         class="inline-flex items-center gap-2 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white px-6 py-3 rounded-lg font-medium transition-colors shadow-lg hover:shadow-xl no-underline">
        <svg class="w-5 h-5 text-white hover:text-blue-100" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
        </svg>
        <span class="text-white hover:text-blue-100">Interactive API Docs</span>
      </a>
      <a href="https://app.docrouter.ai/fastapi/openapi.json" target="_blank" rel="noopener noreferrer"
         class="inline-flex items-center gap-2 bg-white text-blue-600 px-6 py-3 rounded-lg font-medium hover:bg-blue-50 transition-colors border border-blue-200 no-underline">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
        </svg>
        <span>OpenAPI Schema</span>
      </a>
    </div>
  </div>
</div>

## Authentication

<div class="bg-gradient-to-br from-blue-50 via-white to-purple-50 rounded-2xl p-4 md:p-8 mb-6 md:mb-8 border border-blue-100 shadow-lg">
  <p class="text-gray-700 leading-relaxed mb-6">
    The DocRouter REST API uses token-based authentication. Choose the appropriate token type based on your integration needs:
  </p>
  
  <div class="grid md:grid-cols-2 gap-6">
    <div class="bg-white border border-blue-200 rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow">
      <div class="flex items-center gap-3 mb-4 mt-4">
        <div class="w-12 h-12 bg-blue-500 rounded-xl flex items-center justify-center">
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
          </svg>
        </div>
          <div>
            <div class="text-xl font-semibold text-gray-900 leading-tight">Account Tokens</div>
            <div class="text-sm text-gray-600">User-scoped access</div>
          </div>
      </div>
      <div class="space-y-3">
        <div class="flex items-start gap-3">
          <div class="w-2 h-2 bg-blue-500 rounded-full mt-2.5 flex-shrink-0"></div>
          <div>
            <span class="font-medium text-gray-900">Scope:</span>
            <span class="text-gray-700">APIs under <code class="bg-blue-50 text-blue-700 px-2 py-1 rounded text-sm font-mono">/v0/account</code></span>
          </div>
        </div>
        <div class="flex items-start gap-3">
          <div class="w-2 h-2 bg-blue-500 rounded-full mt-2.5 flex-shrink-0"></div>
          <div>
            <span class="font-medium text-gray-900">To Create:</span>
            <span class="text-gray-700">Click <code class="bg-blue-50 text-blue-700 px-2 py-1 rounded text-sm font-mono">Settings → Account Tokens</code></span>
          </div>
        </div>
      </div>
    </div>

    <div class="bg-white border border-green-200 rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow">
      <div class="flex items-center gap-3 mb-4 mt-4">
        <div class="w-12 h-12 bg-green-500 rounded-xl flex items-center justify-center">
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0h3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
          </svg>
        </div>
        <div>
          <div class="text-xl font-semibold text-gray-900 leading-tight">Organization Tokens</div>
          <div class="text-sm text-gray-600">Team-scoped access</div>
        </div>
      </div>
      <div class="space-y-3">
        <div class="flex items-start gap-3">
          <div class="w-2 h-2 bg-green-500 rounded-full mt-2.5 flex-shrink-0"></div>
          <div>
            <span class="font-medium text-gray-900">Scope:</span>
            <span class="text-gray-700">APIs under <code class="bg-green-50 text-green-700 px-2 py-1 rounded text-sm font-mono">/v0/orgs/{organization_id}</code></span>
          </div>
        </div>
        <div class="flex items-start gap-3">
          <div class="w-2 h-2 bg-green-500 rounded-full mt-2.5 flex-shrink-0"></div>
          <div>
            <span class="font-medium text-gray-900">To Create:</span>
            <span class="text-gray-700">Click <code class="bg-green-50 text-green-700 px-2 py-1 rounded text-sm font-mono">Settings → Organization Tokens</code></span>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <!-- Token Management Screenshots -->
  <div class="mt-8 pt-6 border-t border-gray-200">
    <h3 class="text-lg font-semibold text-gray-900 mb-4 text-center">Token Management Interface</h3>
    <div class="space-y-6 max-w-4xl mx-auto">
      <div class="bg-white rounded-lg p-4 border border-gray-200 shadow-sm">
        <div style="display: flex; align-items: flex-start; margin-bottom: 1rem;">
          <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">1</div>
          <div style="flex: 1;">
            <h4 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.5rem 0;">Access Settings</h4>
            <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 1rem 0;">Click your user menu → Settings</p>
            <img src="/assets/images/manage_tokens1.jpeg" 
                 alt="Step 1: Access Settings menu" 
                 class="w-full h-auto rounded border border-gray-200 shadow-sm hover:shadow-md transition-shadow">
          </div>
        </div>
      </div>
      <div class="bg-white rounded-lg p-4 border border-gray-200 shadow-sm">
        <div style="display: flex; align-items: flex-start; margin-bottom: 1rem;">
          <div style="width: 40px; height: 40px; min-width: 40px; background-color: #22c55e; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">2</div>
          <div style="flex: 1;">
            <h4 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.5rem 0;">Manage Tokens</h4>
            <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 1rem 0;">Click "Manage" for Account or Organization Tokens</p>
            <img src="/assets/images/manage_tokens2.jpeg" 
                 alt="Step 2: Manage tokens interface" 
                 class="w-full h-auto rounded border border-gray-200 shadow-sm hover:shadow-md transition-shadow">
          </div>
        </div>
      </div>
    </div>
    <p class="text-xs text-gray-600 text-center mt-4">
      Screenshots showing how to access the token management interface in the DocRouter application
    </p>
  </div>
</div>

## API Examples

<div class="space-y-4">
  <!-- Account-Level APIs Accordion -->
  <div class="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
    <button onclick="toggleAccordion('account')" class="w-full px-6 py-4 text-left bg-gray-50 hover:bg-gray-100 transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-inset">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3 mb-4 mt-4">
          <div class="w-12 h-12 bg-blue-500 rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
            </svg>
          </div>
          <div>
            <div class="text-xl font-semibold text-gray-900 leading-tight">Account-Level APIs</div>
            <div class="text-sm text-gray-600">User-scoped operations and account management</div>
          </div>
        </div>
        <svg id="account-chevron" class="w-5 h-5 text-gray-500 transform transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
        </svg>
      </div>
    </button>
    
    <div id="account-content" class="accordion-content hidden">
      <div class="p-6 border-t border-gray-200">
        <div class="mb-6">
          <h4 class="text-lg font-semibold text-gray-900 mb-2">List All Organizations</h4>
          <p class="text-gray-600">Retrieve all organizations that the authenticated user can access.</p>
        </div>
        
        <div class="space-y-6">
          <div>
            <h5 class="text-sm font-medium text-gray-900 mb-3 flex items-center gap-2">
              <svg class="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v14a2 2 0 002 2z"/>
              </svg>
              Request
            </h5>
            <div class="relative">
              <button onclick="copyToClipboard('account-curl')" class="absolute top-2 right-2 bg-gray-700 hover:bg-gray-600 text-white px-3 py-1 rounded text-xs transition-colors">
                Copy
              </button>
              <pre id="account-curl" class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto border border-gray-700"><code>curl -X GET "https://app.docrouter.ai/fastapi/v0/account/organizations" \
     -H "Authorization: Bearer YOUR_ACCOUNT_TOKEN" \
     -H "Content-Type: application/json"</code></pre>
            </div>
          </div>

          <div>
            <h5 class="text-sm font-medium text-gray-900 mb-3 flex items-center gap-2">
              <svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              Response (200 OK)
            </h5>
            <div class="relative">
              <button onclick="copyToClipboard('account-response')" class="absolute top-2 right-2 bg-gray-700 hover:bg-gray-600 text-white px-3 py-1 rounded text-xs transition-colors">
                Copy
              </button>
              <pre id="account-response" class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto border border-gray-700"><code>{
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
      </div>
    </div>
  </div>

  <!-- Organization-Level APIs Accordion -->
  <div class="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
    <button onclick="toggleAccordion('organization')" class="w-full px-6 py-4 text-left bg-gray-50 hover:bg-gray-100 transition-colors focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-inset">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3 mb-4 mt-4">
          <div class="w-12 h-12 bg-green-500 rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0h3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
            </svg>
          </div>
          <div>
            <div class="text-xl font-semibold text-gray-900 leading-tight">Organization-Level APIs</div>
            <div class="text-sm text-gray-600">Team-scoped operations and document management</div>
          </div>
        </div>
        <svg id="organization-chevron" class="w-5 h-5 text-gray-500 transform transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
        </svg>
      </div>
    </button>
    
    <div id="organization-content" class="accordion-content hidden">
      <div class="p-6 border-t border-gray-200">
        <div class="mb-6">
          <h4 class="text-lg font-semibold text-gray-900 mb-2">List All Documents</h4>
          <p class="text-gray-600">Retrieve all documents within a specific organization.</p>
        </div>
        
        <div class="space-y-6">
          <div>
            <h5 class="text-sm font-medium text-gray-900 mb-3 flex items-center gap-2">
              <svg class="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v14a2 2 0 002 2z"/>
              </svg>
              Request
            </h5>
            <div class="relative">
              <button onclick="copyToClipboard('org-curl')" class="absolute top-2 right-2 bg-gray-700 hover:bg-gray-600 text-white px-3 py-1 rounded text-xs transition-colors">
                Copy
              </button>
              <pre id="org-curl" class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto border border-gray-700"><code>curl -X GET "https://app.docrouter.ai/fastapi/v0/orgs/12345678abcdef123456789a/documents" \
     -H "Authorization: Bearer YOUR_ORGANIZATION_TOKEN" \
     -H "Content-Type: application/json"</code></pre>
            </div>
          </div>

          <div>
            <h5 class="text-sm font-medium text-gray-900 mb-3 flex items-center gap-2">
              <svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              Response (200 OK)
            </h5>
            <div class="relative">
              <button onclick="copyToClipboard('org-response')" class="absolute top-2 right-2 bg-gray-700 hover:bg-gray-600 text-white px-3 py-1 rounded text-xs transition-colors">
                Copy
              </button>
              <pre id="org-response" class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto border border-gray-700"><code>{
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
  </div>
</div>

<script>
function toggleAccordion(sectionName) {
  const content = document.getElementById(sectionName + '-content');
  const chevron = document.getElementById(sectionName + '-chevron');
  
  if (content.classList.contains('hidden')) {
    // Expand the accordion
    content.classList.remove('hidden');
    chevron.style.transform = 'rotate(180deg)';
  } else {
    // Collapse the accordion
    content.classList.add('hidden');
    chevron.style.transform = 'rotate(0deg)';
  }
}

function copyToClipboard(elementId) {
  const element = document.getElementById(elementId);
  const text = element.textContent || element.innerText;
  
  navigator.clipboard.writeText(text).then(() => {
    // Show feedback
    const button = element.parentElement.querySelector('button');
    const originalText = button.textContent;
    button.textContent = 'Copied!';
    button.classList.add('bg-green-600', 'hover:bg-green-700');
    button.classList.remove('bg-gray-700', 'hover:bg-gray-600');
    
    setTimeout(() => {
      button.textContent = originalText;
      button.classList.remove('bg-green-600', 'hover:bg-green-700');
      button.classList.add('bg-gray-700', 'hover:bg-gray-600');
    }, 2000);
  }).catch(err => {
    console.error('Failed to copy text: ', err);
  });
}
</script>



## Interactive Documentation

<div class="bg-gradient-to-br from-blue-50 via-white to-purple-50 rounded-2xl p-4 md:p-8 mb-6 md:mb-8 border border-blue-100 shadow-lg">
  <div class="text-center mb-8">
    <a href="https://app.docrouter.ai/fastapi/docs#/" target="_blank" rel="noopener noreferrer"
         class="inline-flex items-center gap-2 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white px-4 py-3 md:px-8 md:py-4 rounded-xl font-semibold transition-colors shadow-lg hover:shadow-xl text-base md:text-lg no-underline">
      <svg class="w-5 h-5 text-white hover:text-blue-100" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
        </svg>
      <span class="text-white hover:text-blue-100">Open Swagger UI</span>
    </a>
    <p class="text-lg text-gray-600 max-w-2xl mx-auto mb-6">
      Our interactive API documentation makes it easy to test endpoints, generate code samples, and understand the API structure.
    </p>

  </div>

  <div class="grid md:grid-cols-3 gap-6">
    <!-- Step 1: Authentication -->
    <div class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm hover:shadow-lg transition-all duration-200">
      <div class="flex items-center gap-3 mb-4">
        <div class="w-10 h-10 sm:w-12 sm:h-12 mt-4 bg-blue-500 rounded-xl flex items-center justify-center text-white font-bold text-sm sm:text-base flex-shrink-0">1</div>
        <h3 class="text-lg font-semibold text-gray-900">Authenticate</h3>
      </div>
      <ul class="list-disc list-inside space-y-3 text-sm text-gray-700 leading-relaxed ml-4">
        <li class="text-blue-500">
          <span class="text-gray-700">Click the <span class="font-semibold text-blue-600">"Authorize"</span> button</span>
        </li>
        <li class="text-blue-500">
          <span class="text-gray-700">Enter your API token</span>
        </li>
        <li class="text-blue-500">
          <span class="text-gray-700">Click <span class="font-semibold text-blue-600">"Authorize"</span> to authenticate</span>
        </li>
      </ul>
    </div>

    <!-- Step 2: Testing Endpoints -->
    <div class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm hover:shadow-lg transition-all duration-200">
      <div class="flex items-center gap-3 mb-4">
        <div class="w-10 h-10 sm:w-12 sm:h-12 mt-4 bg-green-500 rounded-xl flex items-center justify-center text-white font-bold text-sm sm:text-base flex-shrink-0">2</div>
        <h3 class="text-lg font-semibold text-gray-900">Test Endpoints</h3>
      </div>
      <ul class="list-disc list-inside space-y-3 text-sm text-gray-700 leading-relaxed ml-4">
        <li class="text-green-500">
          <span class="text-gray-700">Browse endpoints by category</span>
        </li>
        <li class="text-green-500">
          <span class="text-gray-700">Click <span class="font-semibold text-green-600">"Try it out"</span> to enable</span>
        </li>
        <li class="text-green-500">
          <span class="text-gray-700">Fill parameters and click <span class="font-semibold text-green-600">"Execute"</span></span>
        </li>
      </ul>
    </div>

    <!-- Step 3: cURL Commands -->
    <div class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm hover:shadow-lg transition-all duration-200">
      <div class="flex items-center gap-3 mb-4">
        <div class="w-10 h-10 sm:w-12 sm:h-12 mt-4 bg-purple-500 rounded-xl flex items-center justify-center text-white font-bold text-sm sm:text-base flex-shrink-0">3</div>
        <h3 class="text-lg font-semibold text-gray-900">Generate Code</h3>
      </div>
      <ul class="list-disc list-inside space-y-3 text-sm text-gray-700 leading-relaxed ml-4">
        <li class="text-purple-500">
          <span class="text-gray-700">View the <span class="font-semibold text-purple-600">"Response"</span> section</span>
        </li>
        <li class="text-purple-500">
          <span class="text-gray-700">Find the <span class="font-semibold text-purple-600">"Curl"</span> tab</span>
        </li>
        <li class="text-purple-500">
          <span class="text-gray-700">Copy commands for your scripts</span>
        </li>
      </ul>
    </div>
  </div>
</div>

## Resources & Tools

<div class="bg-gradient-to-br from-blue-50 via-white to-purple-50 rounded-2xl p-4 md:p-8 mb-6 md:mb-8 border border-blue-100 shadow-lg">
  <div class="grid md:grid-cols-2 gap-6">
  <!-- OpenAPI Specification Panel -->
  <div class="bg-white border border-gray-200 rounded-xl p-6 shadow-sm hover:shadow-lg transition-shadow">
    <div class="flex items-center gap-3 mb-4 mt-4">
      <div class="w-12 h-12 bg-blue-500 rounded-xl flex items-center justify-center">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
        </svg>
      </div>
      <div>
        <div class="text-xl font-semibold text-gray-900 leading-tight">OpenAPI Specification</div>
        <div class="text-sm text-gray-600">Complete API schema</div>
      </div>
    </div>
    <p class="text-gray-700 mb-4">Access the complete OpenAPI 3.0 specification for code generation and API exploration.</p>
    <div class="space-y-3">
      <a href="https://app.docrouter.ai/fastapi/openapi.json" target="_blank" rel="noopener noreferrer"
         class="inline-flex items-center gap-2 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white px-4 py-2 rounded-lg font-medium transition-colors no-underline">
        <span class="text-white hover:text-blue-100">View OpenAPI JSON</span>
        <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
        </svg>
      </a>
      <a href="https://openapi-generator.tech/" target="_blank" rel="noopener noreferrer" class="flex items-center justify-between bg-gray-50 hover:bg-gray-100 rounded-lg p-3 transition-colors group">
        <div>
          <span class="font-medium text-gray-900 group-hover:text-blue-600">OpenAPI Generator</span>
          <p class="text-sm text-gray-600">Generate clients for Rust, Go, Java, and more</p>
        </div>
        <svg class="w-5 h-5 text-gray-400 group-hover:text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
        </svg>
      </a>
    </div>
  </div>

  <!-- Client Libraries Panel -->
  <div class="bg-white border border-gray-200 rounded-xl p-6 shadow-sm hover:shadow-lg transition-shadow">
    <div class="flex items-center gap-3 mb-4 mt-4">
      <div class="w-12 h-12 bg-green-500 rounded-xl flex items-center justify-center">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
        </svg>
      </div>
      <div>
        <div class="text-xl font-semibold text-gray-900 leading-tight">Client Libraries</div>
        <div class="text-sm text-gray-600">SDKs and code generation</div>
      </div>
    </div>
    <p class="text-gray-700 mb-4">Ready-to-use SDKs for integrating DocRouter into your applications.</p>
    <div class="space-y-3">
      <a href="/docs/python-sdk/" class="flex items-center justify-between bg-gray-50 hover:bg-gray-100 rounded-lg p-3 transition-colors group">
        <div>
          <span class="font-medium text-gray-900 group-hover:text-green-600">Python SDK</span>
          <p class="text-sm text-gray-600">Official client library</p>
        </div>
        <svg class="w-5 h-5 text-gray-400 group-hover:text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
      </a>
      <a href="/docs/typescript-sdk/" class="flex items-center justify-between bg-gray-50 hover:bg-gray-100 rounded-lg p-3 transition-colors group">
        <div>
          <span class="font-medium text-gray-900 group-hover:text-green-600">TypeScript SDK</span>
          <p class="text-sm text-gray-600">Official client library</p>
        </div>
        <svg class="w-5 h-5 text-gray-400 group-hover:text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
      </a>
    </div>
  </div>
</div>
</div>
