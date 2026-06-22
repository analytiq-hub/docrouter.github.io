---
layout: docs
title: "Workflows"
permalink: /docs/workflows/
description: "Automate document processing with DocRouter Flows (built-in) or external platforms — n8n, Microsoft Power Automate, Temporal, webhooks, and custom backends."
---

<div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-4 md:p-8 mb-6 md:mb-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-2">Automate document processing</h2>
  <p class="text-sm md:text-base text-blue-100">Built-in visual flows inside DocRouter, or connect to external workflow platforms.</p>
</div>

## Overview

DocRouter supports two automation tiers:

1. **Built-in** — [DocRouter Flows]({{ '/docs/flows/' | relative_url }}) — visual canvas, document-native nodes, connectors, execution logs
2. **External** — n8n, Power Automate, Temporal, webhooks, REST API, SDKs

---

## Choose an approach

| Goal | Use |
|---|---|
| Visual pipelines inside DocRouter (OCR, LLM, Gmail, ERP POST) | [DocRouter Flows]({{ '/docs/flows/' | relative_url }}) |
| Tag → prompt extraction without a canvas | [Quick Start]({{ '/docs/quick-start/' | relative_url }}) |
| Notify your backend when extraction completes | [Webhooks]({{ '/docs/webhooks/' | relative_url }}) |
| n8n community nodes and hundreds of SaaS connectors | [n8n]({{ '/docs/n8n/' | relative_url }}) |
| Microsoft Power Platform / cloud flows | [Power Automate]({{ '/docs/power-automate/' | relative_url }}) |
| Durable coded orchestration with custom logic | [Temporal]({{ '/docs/temporal/' | relative_url }}) |
| Zapier, Make, or any REST client | [REST API]({{ '/docs/rest-api/' | relative_url }}) |

---

## DocRouter Flows (built-in)

**DocRouter Flows** is the first-party visual workflow editor — n8n-style canvas with document-native nodes (Split, OCR, LLM), connector triggers (Gmail, Drive, …), code nodes, and HTTP request nodes.

See [DocRouter Flows]({{ '/docs/flows/' | relative_url }}) for concepts, quick start, connector setup, and example recipes.

---

## External platforms

### N8N

**N8N** is a visual workflow tool. Use it to connect DocRouter to other apps and services. See [N8N]({{ '/docs/n8n/' | relative_url }}) for package, install, credentials, and webhook setup.

If you want n8n-style flows **inside** DocRouter without a separate n8n instance, use [DocRouter Flows]({{ '/docs/flows/' | relative_url }}) instead.

---

### Microsoft Power Automate

**Microsoft Power Automate** uses the **DocRouter Organization** custom connector (open source, deployed with `paconn`). See [Power Automate integration]({{ '/docs/power-automate/' | relative_url }}) for the GitHub repo, deployment steps, and a [sandbox sample flow](https://github.com/analytiq-hub/power-automate-docrouter#sandbox-sample-flow).

---

### Temporal

**Temporal** is for coded workflows where you need durable orchestration—e.g. classify pages, group them by class, then process each group. See [Temporal]({{ '/docs/temporal/' | relative_url }}) for how it fits with DocRouter and a full walkthrough.

For visual document pipelines without writing workflow code, prefer [DocRouter Flows]({{ '/docs/flows/' | relative_url }}).

---

### Other workflow tools

DocRouter exposes a full suite of <a href="/docs/rest-api">REST APIs</a>, including webhooks. You can integrate with any workflow tool that supports REST APIs—Zapier, Make, custom scripts, or your own backend. Configure webhooks to receive events, and use the REST API to upload documents, list results, and manage resources.

---

## Learn more

- [DocRouter Flows]({{ '/docs/flows/' | relative_url }}) — Built-in visual automation
- <a href="/docs/webhooks">Webhooks</a> — Product event notifications
- <a href="/docs/integrations">Integrations</a> — Overview of integration options

---

<div class="bg-blue-600 rounded-lg p-4 md:p-8 mt-8 md:mt-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-4">Ready to automate?</h2>
  <a href="https://app.docrouter.ai" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-4 py-3 md:px-8 md:py-4 rounded-lg font-semibold text-base md:text-lg transition-colors duration-200 no-underline">
    Open Dashboard
  </a>
</div>
