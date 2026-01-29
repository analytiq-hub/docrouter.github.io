---
layout: docs
title: "Claude Code Integration"
permalink: /docs/claude-code/
---

<div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-8 mb-10 text-center">
  <h2 class="text-2xl font-semibold text-white mb-2">Connect DocRouter to Claude Code</h2>
  <p class="text-blue-100">Use the Model Context Protocol (MCP) to manage documents, schemas, and prompts directly from your terminal.</p>
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
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Configure Claude Code</h3>
      <p style="color: #4b5563; margin: 0;">Add the DocRouter MCP server to your Claude Code configuration with your DocRouter <strong>organization API token</strong>. The organization ID is resolved automatically from this token.</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">3</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Start using DocRouter</h3>
      <p style="color: #4b5563; margin: 0;">Ask Claude Code to list documents, create schemas, run prompts, and more.</p>
    </div>
  </div>
</div>

---

## What is Claude Code Integration?

Claude Code can interact directly with your DocRouter.AI organization using our MCP server. This allows you to manage documents, schemas, and prompts directly from your terminal-based AI assistant.

- **Terminal-based access**: Manage DocRouter without leaving your terminal
- **AI-powered automation**: Use Claude to script complex document processing tasks
- **Context-aware**: Claude can use document data to help you write code or documentation

---

## Configuration

Add the DocRouter MCP server to your Claude Code configuration:

```json
{
  "mcpServers": {
    "docrouter": {
      "command": "docrouter-mcp",
      "env": {
        "DOCROUTER_API_URL": "https://app.docrouter.ai/fastapi",
        "DOCROUTER_ORG_API_TOKEN": "your-org-api-token"
      }
    }
  }
}
```

You'll need your **organization API token** from the DocRouter dashboard. The organization ID is automatically resolved from the token and does not need to be configured.

---

## Example Usage

Once configured, you can ask Claude Code to perform tasks like:

- *"List the last 5 documents uploaded to DocRouter."*
- *"Create a new schema for invoice extraction."*
- *"Run the 'Extract Data' prompt on document doc_123."*
- *"What is the status of my latest upload?"*

---

## Best Practices

<div class="my-6">
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Secure Credentials</strong> — Store your API token securely and never commit it to version control.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Use Environment Variables</strong> — Configure credentials via environment variables for better security.</p>
  <p style="margin: 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Test First</strong> — Start with simple queries like listing documents before running complex operations.</p>
</div>

---

## Learn More

- <a href="/docs/mcp">MCP Server</a> — Learn about the Model Context Protocol
- <a href="/docs/rest-api">REST API</a> — Complete API reference
- <a href="/docs/cursor">Cursor Integration</a> — Similar integration for Cursor editor

---

<div class="bg-blue-600 rounded-lg p-8 mt-10 text-center">
  <h2 class="text-2xl font-semibold text-white mb-4">Ready to connect Claude Code?</h2>
  <a href="https://app.docrouter.ai" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
    Get API Credentials
  </a>
</div>
