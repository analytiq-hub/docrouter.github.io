---
layout: docs
title: "N8N Integration"
permalink: /docs/n8n/
---

n8n is a visual workflow tool. Use it to connect DocRouter to other apps and services (ERP, CRM, email, databases).

## DocRouter nodes

- **Package:** [n8n-nodes-docrouter](https://www.npmjs.com/package/n8n-nodes-docrouter) — community nodes and credentials for Documents, Tags, Prompts, Schemas, Knowledge Base, Webhooks, and more.
- **Install:** In n8n: **Settings → Community Nodes → Install**, enter `n8n-nodes-docrouter`. Or: `npm install n8n-nodes-docrouter` and restart n8n.
- **Credentials:** Create an API token in DocRouter (**Settings → User → Developer**), then add a **DocRouter Organization API** credential in n8n.

For install steps, examples (e.g. Gmail → DocRouter, webhook triggers), and usage, see [How We Built the DocRouter n8n Nodes With Cursor]({{ site.baseurl }}{% post_url 2026-01-31-how-we-built-docrouter-n8n-nodes-with-cursor %}).

<p class="my-4">
  <a href="{{ site.baseurl }}{% post_url 2026-01-31-how-we-built-docrouter-n8n-nodes-with-cursor %}">
    <img src="{{ '/assets/images/n8n_gmail_to_docrouter.png' | relative_url }}" alt="Gmail to DocRouter workflow in n8n" style="max-width: 50%; display: block; margin: 0 auto;" />
  </a>
</p>

## Webhooks + n8n

Use a **DocRouter Webhook** trigger node in n8n, or create a generic Webhook node and paste its URL into **DocRouter → Organization Settings → Webhooks**. Select events such as `llm.completed` to receive extracted data. Use other n8n nodes to send that JSON to your ERP, CRM, or database.

## See also

- [Webhooks]({{ '/docs/webhooks/' | relative_url }}) — Event types, payloads, authentication
- [Workflows]({{ '/docs/workflows/' | relative_url }}) — Overview of workflow options
- [Integrations]({{ '/docs/integrations/' | relative_url }}) — All integration options
