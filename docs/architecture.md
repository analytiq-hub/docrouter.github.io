---
layout: docs
title: "DocRouter Architecture"
permalink: /docs/architecture/
description: "How DocRouter is built: frontend, API, queue workers, MongoDB, OCR and LLM services, the document pipeline, and workflow automation via Flows and external platforms."
---

DocRouter is a multi-tenant document intelligence platform: ingest documents, run OCR, extract structured data with LLMs, and automate the path into downstream systems. This page describes how the pieces fit together. For deploy and cloud keys, see [On-Prem Installation]({{ '/docs/on-prem-installation/' | relative_url }}) and [Platform]({{ '/docs/platform/' | relative_url }}). For the product walkthrough, see [How It Works]({{ '/docs/how-it-works/' | relative_url }}).

## System overview

| Layer | Role |
| ----- | ---- |
| **Frontend (Next.js)** | Document library, prompts/schemas/tags, PDF review, Flows canvas, admin settings |
| **Backend (FastAPI)** | REST API: documents, OCR, LLM results, prompts, schemas, tags, flows, webhooks, account config |
| **Workers** | Async consumers for OCR, LLM extraction, knowledge-base indexing, webhooks, and flow runs |
| **MongoDB** | App state, versioned prompts/schemas, encrypted credentials, flow definitions and executions, work queues |
| **Blob storage** | Document binaries and OCR output |
| **LLM providers** | Inference via [LiteLLM](https://github.com/BerriAI/litellm) (OpenAI, Anthropic, Bedrock, Vertex, Azure, …) |

<div data-excalidraw="/assets/excalidraw/doc_router_architecture.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>

<p style="text-align: center; margin-top: 0.5rem; font-size: 0.875rem; color: #6b7280;">
  <strong>Figure 1:</strong> DocRouter system architecture — application services, cloud APIs, and OCR/LLM providers.
</p>

<div style="text-align: center; margin-top: 1rem; margin-bottom: 2rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/doc_router_architecture.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    Edit in Excalidraw
  </a>
</div>

On-prem, the same services run under Docker Compose or Kubernetes and call managed cloud APIs for storage, OCR, email, and models. See the [on-prem architecture diagram]({{ '/docs/on-prem-installation/' | relative_url }}).

### Request path

1. UI or SDK/REST client calls the FastAPI backend (org-scoped routes under `/v0/orgs/{org_id}/…`).
2. Synchronous work (auth, CRUD, reads) completes in the API process.
3. Heavy work (OCR, LLM, flow execution, outbound webhooks) is enqueued; workers process messages and update MongoDB (and document state).
4. Optionally, multi-step workflows are triggered
4. Clients poll status, subscribe via webhooks, or rely on workflow nodes to send result to target system

Worker pool sizes are configurable per queue (`ocr`, `llm`, `kb_index`, `webhook`, `flow_run`).

## Document pipeline

The default extraction path is tag- and prompt-driven:

1. **Upload** — Document stored; tags select which prompts apply ([Tags]({{ '/docs/tags/' | relative_url }}), [Quick Start]({{ '/docs/quick-start/' | relative_url }})).
2. **OCR** — Org OCR mode runs (e.g. Textract); normalized OCR payload stored for extraction and search ([Platform]({{ '/docs/platform/' | relative_url }})).
3. **LLM extraction** — Matching [prompts]({{ '/docs/prompts/' | relative_url }}) and optional [schemas]({{ '/docs/schemas/' | relative_url }}) produce structured results via LiteLLM.
4. Opional **Workflow steps**, including human-in-the-loop triggers
5. **Export / notify** — REST/SDK download, webhooks, or push to ERP.

Statuses progress through states such as `ocr_completed` → `llm_completed`. Flows and external workflows extend or replace the “what happens after upload” story.

## Automation layer (workflows)

Customers need more than a fixed Upload → OCR → LLM path: branching, schedules, email/drive triggers, agents, and delivery to ERP or review queues. DocRouter supports built-in and external [workflows]({{ '/docs/workflows/' | relative_url }}).

### Built-in: DocRouter Flows

[DocRouter Flows]({{ '/docs/flows/' | relative_url }}) is a first-party visual DAG editor and runtime in the same deployment (no separate Temporal/n8n cluster required).

<div class="my-6">
  <img src="{{ '/assets/images/docrouter_flow_post_to_erp_or_db.png' | relative_url }}" alt="DocRouter Flows canvas with Gmail trigger, Document Split, OCR, LLM, and HTTP nodes" class="w-full rounded-lg shadow-md ring-1 ring-gray-200" />
</div>

Triggers include manual, schedule, webhook, chat, poll, and document events. Execution history (inputs, outputs, timing, logs) is available in the UI. Details: [Flows]({{ '/docs/flows/' | relative_url }}) and the [Flows blog post]({{ site.baseurl }}{% post_url 2026-06-21-docrouter-flows-visual-workflow-automation-for-intelligent-document-processing %}).

### External workflow platforms

When automation lives outside DocRouter, treat DocRouter as the document/OCR/LLM service and orchestrate from elsewhere:

| Platform | Role |
| -------- | ---- |
| [n8n]({{ '/docs/n8n/' | relative_url }}) | Visual flows with community nodes and SaaS connectors |
| [Power Automate]({{ '/docs/power-automate/' | relative_url }}) | Microsoft cloud flows via the DocRouter custom connector |
| [Temporal]({{ '/docs/temporal/' | relative_url }}) | Durable coded orchestration |
| [Webhooks]({{ '/docs/webhooks/' | relative_url }}) + [REST API]({{ '/docs/rest-api/' | relative_url }}) | Event-driven or pull-based custom backends |

Product webhooks (extraction completed, etc.) are distinct from Flow webhook *triggers*.

## Deployment topology

| Mode | What you run | Cloud / LLM config |
| ---- | ------------ | ------------------ |
| **Hosted SaaS** | Nothing — [app.docrouter.ai](https://app.docrouter.ai) | Provided for you ([Platform]({{ '/docs/platform/' | relative_url }})) |
| **Self-hosted** | Frontend, backend, workers, MongoDB, reverse proxy | You supply AWS/GCP/Azure and LLM keys ([On-Prem Installation]({{ '/docs/on-prem-installation/' | relative_url }})) |

Self-host via [Docker Compose]({{ '/docs/docker-compose-install/' | relative_url }}) or [Kubernetes]({{ '/docs/kubernetes-install/' | relative_url }}). DocRouter does not require AWS Lambda/ECS/EKS for on-prem; it uses cloud *APIs* (S3, Textract, SES, Bedrock, Vertex, Foundry, etc.) as configured.

## Security & credentials

- Documents and secrets use encryption in transit and at rest where configured for the deployment.
- Deployment-wide cloud credentials live in MongoDB `cloud_config` (AWS, GCP, Azure); per-provider LLM keys in encrypted `llm_providers`.
- Org and role-based access control scopes documents, prompts, and flows.
- Audit-oriented logging supports compliance review; enable CloudTrail (and equivalents) in your cloud accounts for infrastructure audit.

Admin UIs: **Account → Development** for AWS / GCP / Azure setup and LLM Manager. See [LLM Configuration]({{ '/docs/llm-configuration/' | relative_url }}).

## Integration patterns

How DocRouter typically sits in a larger stack (not alternate product architectures):

<div class="grid md:grid-cols-2 gap-6 my-6">
  <div>
    <img src="{{ '/assets/images/docrouter/architecture_erp.png' | relative_url }}" alt="DocRouter feeding structured data into an ERP" class="w-full rounded-lg shadow-md ring-1 ring-gray-200">
    <p class="text-sm text-gray-600 mt-2"><strong>ERP / ops systems</strong> — Extract with prompts or Flows, then POST or sync into ERP, EHR, or databases.</p>
  </div>
  <div>
    <img src="{{ '/assets/images/docrouter/architecture_ai_enabler.png' | relative_url }}" alt="DocRouter as an AI document layer in a larger application stack" class="w-full rounded-lg shadow-md ring-1 ring-gray-200">
    <p class="text-sm text-gray-600 mt-2"><strong>AI application layer</strong> — Use DocRouter as the document understanding service behind your own product UI and agents.</p>
  </div>
</div>

## Related docs

- [How It Works]({{ '/docs/how-it-works/' | relative_url }}) — User-facing pipeline
- [Workflows]({{ '/docs/workflows/' | relative_url }}) / [Flows]({{ '/docs/flows/' | relative_url }}) — Automation
- [Platform]({{ '/docs/platform/' | relative_url }}) — Clouds, LLMs, OCR modes
- [On-Prem Installation]({{ '/docs/on-prem-installation/' | relative_url }}) — Install and cloud setup
- [Open Source]({{ '/docs/open-source/' | relative_url }}) — License and source
- [REST API]({{ '/docs/rest-api/' | relative_url }}) / [Python SDK]({{ '/docs/python-sdk/' | relative_url }}) / [TypeScript SDK]({{ '/docs/typescript-sdk/' | relative_url }}) — Programmatic access

<style>
.excalidraw-container {
  width: 100%;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  background: white;
  display: block;
  margin: 2rem 0;
  min-height: 400px;
}
.excalidraw-container svg {
  width: 100%;
  height: auto;
  display: block;
  margin: 0;
}
.loading-placeholder {
  padding: 2rem;
  text-align: center;
  color: #666;
}
</style>
<script type="module" src="/assets/js/excalidraw/render-excalidraw.js"></script>
