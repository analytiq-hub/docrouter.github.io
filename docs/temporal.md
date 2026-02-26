---
layout: docs
title: "DocRouter Temporal Integration — Durable Workflows"
permalink: /docs/temporal/
description: "Integrate DocRouter with Temporal for durable document workflow orchestration. Classify, group, and process multi-page documents with retryable, scalable workflows."
---

Temporal is for **coded workflows** where you need durable orchestration—e.g. classify pages, group them by class, then process each group with DocRouter.

**Use it when** documents must be split, classified, grouped, and processed by group (e.g. multi-page surgery schedules, batch processing by type).

## How it fits with DocRouter

- Configure [webhooks]({{ '/docs/webhooks/' | relative_url }}) in DocRouter and point them at your Temporal workflow (or a small HTTP handler that forwards to Temporal).
- Use Temporal **signals** to wait for the `llm.completed` webhook, then continue with validation, human-in-the-loop steps, or downstream integrations.
- Your workflow code calls the DocRouter [REST API]({{ '/docs/rest-api/' | relative_url }}) to upload documents, list results, and manage resources.

For a full walkthrough, see [How to create document workflows with Temporal and DocRouter.AI]({{ '/blog/2025/12/25/how-to-create-document-workflows-with-temporal-and-docrouter-ai/' | relative_url }}).

## See also

- [Webhooks]({{ '/docs/webhooks/' | relative_url }}) — Event types, payloads, authentication
- [Workflows]({{ '/docs/workflows/' | relative_url }}) — Overview of workflow options
- [Integrations]({{ '/docs/integrations/' | relative_url }}) — All integration options
