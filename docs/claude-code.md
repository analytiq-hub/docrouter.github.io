---
layout: docs
title: "Claude Code Integration"
permalink: /docs/claude-code/
---

<div class="bg-blue-50 rounded-2xl p-8 mb-12 border border-blue-100 shadow-lg text-center">
  <h1 class="text-4xl font-bold text-gray-900 mb-4">Claude Code Integration</h1>
  <p class="text-lg text-gray-600">
    Connect DocRouter.AI to Claude Code using the Model Context Protocol (MCP) for a seamless developer experience.
  </p>
</div>

## Overview

Claude Code can interact directly with your DocRouter.AI organization using our MCP server. This allows you to manage documents, schemas, and prompts directly from your terminal-based AI assistant.

---

## Setup Instructions

### 1. Install the MCP Server
Ensure you have Node.js installed, then run:

```bash
npm install -g @docrouter/mcp
```

### 2. Configure Claude Code
Add the DocRouter MCP server to your Claude Code configuration. You will need your **Organization ID** and **API Token** from the DocRouter dashboard.

```bash
# Edit your config (usually ~/.claude_desktop_config.json or similar for CLI)
{
  "mcpServers": {
    "docrouter": {
      "command": "docrouter-mcp",
      "env": {
        "DOCROUTER_API_URL": "https://app.docrouter.ai/fastapi",
        "DOCROUTER_ORG_ID": "your-org-id",
        "DOCROUTER_ORG_API_TOKEN": "your-api-token"
      }
    }
  }
}
```

---

## Example Usage

Once configured, you can ask Claude Code to perform tasks like:

- *"List the last 5 documents uploaded to DocRouter."*
- *"Create a new schema for invoice extraction."*
- *"Run the 'Extract Data' prompt on document doc_123."*
- *"What is the status of my latest upload?"*

---

## Benefits

- **Speed**: No need to switch between your terminal and the web UI.
- **Automation**: Use Claude to script complex document processing tasks.
- **Context**: Claude can use document data to help you write code or documentation.

---

<div class="bg-blue-600 rounded-lg shadow-lg p-8 mt-12 text-center">
  <h2 class="text-2xl font-semibold text-white mb-4">Get your API credentials</h2>
  <a href="https://app.docrouter.ai/settings/api" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
    API Settings
  </a>
</div>
