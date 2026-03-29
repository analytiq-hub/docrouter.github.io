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

The repo README documents a small reference flow you can reproduce in Power Automate: **manual trigger** → get file content from your storage connector → **Upload Document** to DocRouter (file name + Base64). Screenshots and step-by-step install are in the README:

**[Sandbox sample flow →](https://github.com/analytiq-hub/power-automate-docrouter#sandbox-sample-flow)**

## Capabilities

The connector exposes DocRouter operations for documents (upload, list, get, update, delete), tags, prompts, schemas, knowledge bases, OCR, LLM extraction, and webhook triggers—aligned with the [REST API]({{ '/docs/rest-api/' | relative_url }}) surface for organizations.

## See also

- [n8n]({{ '/docs/n8n/' | relative_url }}) — Community nodes for the same APIs in n8n
- [Workflows]({{ '/docs/workflows/' | relative_url }}) — Webhooks and automation overview
- [Webhooks]({{ '/docs/webhooks/' | relative_url }}) — Event types and payloads
- [Integrations]({{ '/docs/integrations/' | relative_url }}) — All integration options
