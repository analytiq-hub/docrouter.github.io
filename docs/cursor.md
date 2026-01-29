---
layout: docs
title: "Cursor Integration"
permalink: /docs/cursor/
---

<div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-8 mb-10 text-center">
  <h2 class="text-2xl font-semibold text-white mb-2">Power Cursor AI with DocRouter data</h2>
  <p class="text-blue-100">Use the Model Context Protocol (MCP) to search, read, and manage your documents directly from Cursor.</p>
</div>

## Get started in 3 steps

<div class="bg-gray-50 rounded-lg p-6 my-6">
  <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">1</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Install the MCP server</h3>
      <p style="color: #4b5563; margin: 0;">Run <code class="bg-gray-100 px-1 rounded">npm install -g @docrouter/mcp</code> to install the DocRouter MCP server.</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">2</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Add to Cursor settings</h3>
      <p style="color: #4b5563; margin: 0;">Open Cursor Settings → Features → MCP, then add a new MCP server with command <code class="bg-gray-100 px-1 rounded">docrouter-mcp</code>.</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">3</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Configure credentials</h3>
      <p style="color: #4b5563; margin: 0;">Add environment variable: <code class="bg-gray-100 px-1 rounded">DOCROUTER_ORG_API_TOKEN</code>. The organization ID is resolved automatically from this token.</p>
    </div>
  </div>
</div>

---

## What is Cursor Integration?

By connecting DocRouter.AI to Cursor via MCP, you enable Cursor's AI to search, read, and manage your documents and extraction schemas. This is perfect for building applications that rely on DocRouter's structured data.

- **Direct data access**: Build frontend or backend logic using real extraction results as context
- **Schema management**: Update your DocRouter schemas without leaving your editor
- **Rapid prototyping**: Quickly test how different prompts affect your application's data flow

---

## Configuration Steps

1. Open Cursor **Settings** (Cmd+,)
2. Navigate to **Features** → **MCP**
3. Click **+ Add New MCP Server**
4. Fill in the details:
   - **Name**: `DocRouter`
   - **Type**: `command`
   - **Command**: `docrouter-mcp`
5. Add Environment Variables:
   - `DOCROUTER_ORG_API_TOKEN`: Your organization API token (organization ID is resolved automatically)

---

## How to Use

In Cursor Chat (Cmd+L) or Composer (Cmd+I), you can now use DocRouter tools:

- *"Show me the schema for 'Invoices'."*
- *"Download the extraction results for the latest document."*
- *"Create a new prompt that uses the 'Receipt' tag."*

---

## Best Practices

<div class="my-6">
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Secure Credentials</strong> — Store your API token securely in Cursor's environment variables.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Use Real Data</strong> — Leverage actual extraction results to build more accurate application logic.</p>
  <p style="margin: 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Iterate Quickly</strong> — Test schema changes and prompt variations without switching tools.</p>
</div>

---

## Learn More

- <a href="/docs/mcp">MCP Server</a> — Learn about the Model Context Protocol
- <a href="/docs/claude-code">Claude Code Integration</a> — Similar integration for Claude Code
- <a href="/docs/rest-api">REST API</a> — Complete API reference

---

<div class="bg-blue-600 rounded-lg p-8 mt-10 text-center">
  <h2 class="text-2xl font-semibold text-white mb-4">Ready to connect Cursor?</h2>
  <a href="https://app.docrouter.ai" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
    Get API Credentials
  </a>
</div>
