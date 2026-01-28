---
layout: docs
title: "Cursor Integration"
permalink: /docs/cursor/
---

<div class="bg-blue-50 rounded-2xl p-8 mb-12 border border-blue-100 shadow-lg text-center">
  <h1 class="text-4xl font-bold text-gray-900 mb-4">Cursor Integration</h1>
  <p class="text-lg text-gray-600">
    Power your Cursor AI with DocRouter.AI data using the Model Context Protocol (MCP).
  </p>
</div>

## Overview

By connecting DocRouter.AI to Cursor via MCP, you enable Cursor's AI to search, read, and manage your documents and extraction schemas. This is perfect for building applications that rely on DocRouter's structured data.

---

## Setup Instructions

### 1. Install the MCP Server
Open your terminal and run:

```bash
npm install -g @docrouter/mcp
```

### 2. Add to Cursor
1. Open Cursor **Settings** (Cmd+,).
2. Navigate to **Features** → **MCP**.
3. Click **+ Add New MCP Server**.
4. Fill in the details:
   - **Name**: `DocRouter`
   - **Type**: `command`
   - **Command**: `docrouter-mcp`
5. Add Environment Variables:
   - `DOCROUTER_ORG_ID`: Your Org ID
   - `DOCROUTER_ORG_API_TOKEN`: Your API Token

---

## How to Use

In Cursor Chat (Cmd+L) or Composer (Cmd+I), you can now use DocRouter tools:

- *"Show me the schema for 'Invoices'."*
- *"Download the extraction results for the latest document."*
- *"Create a new prompt that uses the 'Receipt' tag."*

---

## Why use MCP with Cursor?

- **Direct Data Access**: Build your frontend or backend logic using real extraction results as context.
- **Schema Management**: Update your DocRouter schemas without leaving your editor.
- **Rapid Prototyping**: Quickly test how different prompts affect your application's data flow.

---

<div class="bg-blue-600 rounded-lg shadow-lg p-8 mt-12 text-center">
  <h2 class="text-2xl font-semibold text-white mb-4">Learn more about MCP</h2>
  <a href="/docs/mcp" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
    MCP Guide
  </a>
</div>
