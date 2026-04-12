---
layout: docs
title: "DocRouter Microsoft Power Automate Integration"
permalink: /docs/power-automate/
description: "Use DocRouter from Microsoft Power Automate with the open-source DocRouter Organization custom connector. Deploy with paconn and follow the sandbox sample flow on GitHub."
---

**Microsoft Power Automate** (cloud flows) connects to DocRouter through the **DocRouter Organization** custom connector—an independent-publisher connector that wraps the same organization-scoped REST API as the [n8n nodes]({{ '/docs/n8n/' | relative_url }}) (`/v0/orgs/{organization_id}/...`).

## Open-source connector

The connector source, OpenAPI definition, C# script (org id injection), and helper scripts live on GitHub:

**[github.com/analytiq-hub/power-automate-docrouter](https://github.com/analytiq-hub/power-automate-docrouter)**

- Deploy with the Power Platform CLI (**`paconn`**) using `create.sh` / `update.sh`.
- Authentication: **Organization Token** (API key) and **Organization ID** (same concepts as in DocRouter and n8n).

## Sandbox sample flow

The repo README documents a small reference flow you can reproduce in Power Automate: **manual trigger** → get file content from your storage connector → **Upload Document** to DocRouter (file name + Base64). Full setup steps are in the README: **[Sandbox sample flow →](https://github.com/analytiq-hub/power-automate-docrouter#sandbox-sample-flow)**

<p class="my-4">
  <img src="{{ '/assets/images/power-automate-sandbox-flow.png' | relative_url }}" alt="Power Automate flow: manual trigger, get file metadata, get file content, Upload Document to DocRouter" style="max-width: 100%; height: auto; display: block; margin: 0 auto; border: 1px solid #e5e7eb; border-radius: 8px;" />
</p>

## DocRouter actions in Power Automate

When you add an action from **DocRouter Organization RC1**, the designer lists the same organization-scoped operations as in the OpenAPI definition (documents, tags, prompts, OCR, LLM, knowledge bases, webhooks, and more).

<p class="my-4">
  <img src="{{ '/assets/images/power-automate-connector-actions.png' | relative_url }}" alt="DocRouter Organization RC1 actions listed in the Power Automate add-an-action panel" style="max-width: 100%; height: auto; display: block; margin: 0 auto; border: 1px solid #e5e7eb; border-radius: 8px;" />
</p>

## Capabilities

The connector exposes DocRouter operations for documents (upload, list, get, update, delete), tags, prompts, schemas, knowledge bases, OCR, LLM extraction, and webhook triggers—aligned with the [REST API]({{ '/docs/rest-api/' | relative_url }}) surface for organizations.

## See also

- [n8n]({{ '/docs/n8n/' | relative_url }}) — Community nodes for the same APIs in n8n
- [Workflows]({{ '/docs/workflows/' | relative_url }}) — Webhooks and automation overview
- [Webhooks]({{ '/docs/webhooks/' | relative_url }}) — Event types and payloads
- [Integrations]({{ '/docs/integrations/' | relative_url }}) — All integration options
