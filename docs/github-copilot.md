---
layout: docs
title: "GitHub Copilot Integration"
permalink: /docs/github-copilot/
description: "Connect DocRouter to GitHub Copilot via MCP. Search, read, and manage documents from Copilot Chat or the Copilot coding agent in VS Code."
---

<div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-4 md:p-8 mb-6 md:mb-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-2">Connect DocRouter to GitHub Copilot</h2>
  <p class="text-sm md:text-base text-blue-100">Use the Model Context Protocol (MCP) to search, read, and manage your documents from Copilot Chat or the Copilot coding agent.</p>
</div>

## Get started in 3 steps

<div class="bg-gray-50 rounded-lg p-4 md:p-6 my-4 md:my-6">
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
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Configure Copilot</h3>
      <p style="color: #4b5563; margin: 0;">Add the DocRouter MCP server in Copilot Chat (VS Code) or in your repository’s Copilot coding agent settings.</p>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start;">
    <div style="width: 40px; height: 40px; min-width: 40px; background-color: #2563eb; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 1.125rem; margin-right: 1rem;">3</div>
    <div style="flex: 1;">
      <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.25rem 0;">Use DocRouter from Copilot</h3>
      <p style="color: #4b5563; margin: 0;">Ask Copilot to list documents, create schemas, run prompts, and more. The organization ID is resolved automatically from your API token.</p>
    </div>
  </div>
</div>

---

## What is GitHub Copilot Integration?

By connecting DocRouter to GitHub Copilot via MCP, Copilot can search, read, and manage your documents and extraction schemas. Use it in **Copilot Chat** (in VS Code or GitHub.com) or in the **Copilot coding agent** (repository-level).

- **Direct data access**: Use real extraction results as context when building or debugging code
- **Schema management**: Update DocRouter schemas and prompts without leaving your editor
- **Same MCP server**: The same <code>@docrouter/mcp</code> server works with Cursor, Claude Code, and Copilot

---

## Copilot Chat (VS Code)

If you use **GitHub Copilot Chat** in Visual Studio Code (1.99 or later), configure the DocRouter MCP server so Copilot can call DocRouter tools.

1. Ensure <code>docrouter-mcp</code> is installed: <code>npm install -g @docrouter/mcp</code>
2. In VS Code, open **Settings** and search for **MCP** (or add a `.mcp.json` in your project or user config).
3. Add the DocRouter MCP server. Example structure:

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

Replace <code>your-org-api-token</code> with your **organization API token** from the DocRouter dashboard. The organization ID is resolved automatically.

---

## Copilot coding agent (repository)

Repository admins can configure MCP servers for the **Copilot coding agent** so it can use DocRouter when working in your repo.

1. In your GitHub repository, go to **Settings** → **Code & automation** → **Copilot** → **Coding agent**.
2. In **MCP configuration**, add the DocRouter MCP server in the required JSON format (same <code>mcpServers</code> structure as above).
3. For the API token, use a repository or organization secret (e.g. prefixed with <code>COPILOT_MCP_</code> as required by Copilot) so the agent can authenticate to DocRouter.

See [GitHub’s docs on extending the Copilot coding agent with MCP](https://docs.github.com/en/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-mcp) for the exact schema and secret naming.

---

## Example usage

Once configured, you can ask Copilot to:

- *"List the last 5 documents uploaded to DocRouter."*
- *"Show me the schema for 'Invoices'."*
- *"Create a new prompt that uses the 'Receipt' tag."*
- *"Run the extraction prompt on document doc_123."*

---

## Best practices

<div class="my-4 md:my-6">
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Secure credentials</strong> — Store your API token in VS Code secrets or GitHub repository/org secrets; never commit it.</p>
  <p style="margin: 0 0 0.75rem 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Test in Chat first</strong> — Use Copilot Chat to list documents or read a schema before asking the coding agent to perform DocRouter operations.</p>
  <p style="margin: 0;"><span style="color: #22c55e; margin-right: 0.5rem;">✓</span> <strong>Same as Cursor/Claude</strong> — The DocRouter MCP server and token work the same across Cursor, Claude Code, and Copilot.</p>
</div>

---

## Learn more

- <a href="{{ '/docs/mcp/' | relative_url }}">MCP Server</a> — Model Context Protocol and DocRouter tools
- <a href="{{ '/docs/cursor/' | relative_url }}">Cursor Integration</a> — Similar integration for Cursor
- <a href="{{ '/docs/claude-code/' | relative_url }}">Claude Code Integration</a> — Similar integration for Claude Code
- <a href="{{ '/docs/rest-api/' | relative_url }}">REST API</a> — Full API reference

---

<div class="bg-blue-600 rounded-lg p-4 md:p-8 mt-8 md:mt-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-4">Ready to connect GitHub Copilot?</h2>
  <a href="https://app.docrouter.ai" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-4 py-3 md:px-8 md:py-4 rounded-lg font-semibold text-base md:text-lg transition-colors duration-200 no-underline">
    Get API Credentials
  </a>
</div>
