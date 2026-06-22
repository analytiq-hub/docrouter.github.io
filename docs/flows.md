---
layout: docs
title: "DocRouter Flows — Visual Document Automation"
permalink: /docs/flows/
description: "Build document processing pipelines on a visual canvas inside DocRouter. Drag-and-drop nodes for OCR, LLM extraction, connectors, code, and HTTP — with n8n-style execution logs and pin data."
---

<div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-4 md:p-8 mb-6 md:mb-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-2">DocRouter Flows</h2>
  <p class="text-sm md:text-base text-blue-100">Visual, node-based automation for intelligent document processing — built into DocRouter.</p>
</div>

## Overview

**DocRouter Flows** is a visual workflow editor inside DocRouter. You drag nodes onto a canvas, connect them, run the pipeline, and inspect every input and output per step — the same interaction model [n8n](https://n8n.io) popularised, extended with **document-native nodes** (split, OCR, LLM extraction) and **Apache 2.0** licensing so you can embed the platform in commercial products.

Flows connects ingestion, extraction, post-processing, and delivery in one product. No separate glue service required for the common path: **Gmail → Document Split → OCR → LLM → ERP**.

<div class="rounded-xl border-2 border-blue-200 bg-gradient-to-br from-blue-50 to-indigo-50/90 p-5 md:p-6 my-6 shadow-md ring-1 ring-blue-100/50">
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6">
    <p class="text-gray-800"><strong class="text-blue-900">Before:</strong> Upload in DocRouter, wire <a href="{{ '/docs/webhooks/' | relative_url }}">webhooks</a> to n8n or custom code, glue OCR and LLM steps yourself.</p>
    <p class="text-gray-800"><strong class="text-blue-900">Now:</strong> Drag a canvas: <strong>Gmail → Split → OCR → LLM → ERP</strong> — one product, full execution log.</p>
  </div>
</div>

Open **Flows** from the left sidebar in the DocRouter app to create or edit pipelines for your organisation.

---

## When to use Flows

| Goal | Recommended approach |
|---|---|
| Visual end-to-end document pipelines inside DocRouter | **DocRouter Flows** (this page) |
| Tag → prompt → upload extraction only | <a href="{{ '/docs/quick-start/' | relative_url }}">Quick Start</a> — tags and prompts |
| Push extraction results to your backend on events | <a href="{{ '/docs/webhooks/' | relative_url }}">Product webhooks</a> |
| Already use n8n community nodes | <a href="{{ '/docs/n8n/' | relative_url }}">n8n integration</a> |
| Microsoft Power Platform / cloud flows | <a href="{{ '/docs/power-automate/' | relative_url }}">Power Automate</a> |
| Durable **coded** orchestration with custom retry semantics | <a href="{{ '/docs/temporal/' | relative_url }}">Temporal</a> |
| Simple REST upload and poll | <a href="{{ '/docs/rest-api/' | relative_url }}">REST API</a> or SDKs |

For a deeper architectural walkthrough, see the blog post [DocRouter Flows: Bringing the n8n Architecture to Intelligent Document Processing]({{ site.baseurl }}{% post_url 2026-06-21-docrouter-flows-bringing-the-n8n-architecture-to-intelligent-document-processing %}).

---

## Core concepts

If you have used n8n, these will feel familiar:

- **Canvas** — Drag nodes from a palette, connect output handles to inputs. Node shapes and connection style mirror n8n's look and feel.
- **Items** — Every node receives and produces a list of *items*. Each item has a `json` payload (structured data) and a `binary` payload (PDF pages, attachments).
- **Expressions** — Parameters prefixed with `=` reference upstream outputs (e.g. `={{ $json.invoice_number }}`).
- **Pin data** — Freeze a node's output so downstream nodes reuse it without re-running expensive OCR or LLM calls.
- **Execution log** — Per-node status, timing, inputs, outputs, and code-node print output. Click any node after a run to inspect what flowed through it.
- **Credentials** — OAuth tokens and API keys stored once per organisation under **Settings → Credentials**, injected at runtime — never stored in the graph.

**Per-node error handling:** Each node has an **on error** setting — stop the run (default) or continue with an error-envelope item downstream.

---

## Node types

### Document-native

Nodes purpose-built for IDP — no n8n equivalent:

| Node | Purpose |
|---|---|
| **Document event trigger** | Fires on `document.uploaded`, `llm.completed`, etc., filtered by tag |
| **Document Split** | Splits a multi-page PDF into one item per page |
| **Run OCR** | OCR on PDF pages; output on a typed port |
| **Run LLM** | Runs a configured <a href="{{ '/docs/prompts/' | relative_url }}">DocRouter prompt</a> on binary input items; accepts OCR text on a second typed port |

The OCR output port only connects to the LLM node's second input — one OCR result per page, matched to the corresponding LLM item.

### Generic

| Node | Purpose |
|---|---|
| **Code (Python)** | Sandboxed `def run(items, context)` transforms |
| **HTTP Request** | Outbound REST to any API |
| **Branch / Merge** | Conditional routing and synchronisation |
| **Webhook trigger** | Start a flow from an inbound HTTP call (sync or async) |
| **Schedule trigger** | Cron-based runs with timezone support |
| **Poll triggers** | Gmail, Outlook, Google Drive, OneDrive — poll for new messages or files |

**Disabled nodes** are skipped during execution — useful when testing one part of a flow.

---

## Quick start

After completing the <a href="{{ '/docs/quick-start/' | relative_url }}">Tag → Prompt → Upload</a> path (Steps 1–3), build your first flow:

1. Open **Flows** in the sidebar → **Create flow**.
2. Add a **Document event trigger**. Set the event to `document.uploaded` and filter by the tag you created in Quick Start.
3. Add **Document Split** → **Run OCR** → **Run LLM**. Wire OCR output to the LLM node's second input.
4. In **Run LLM**, select your prompt from the searchable list. The node runs it against each binary input item (one page per item after split).
5. Click **Execute workflow**. Click each node to inspect inputs and outputs in the execution log.

### What a flow looks like

<p class="my-4">
  <img src="{{ '/assets/images/docrouter_flow_post_to_erp_or_db.png' | relative_url }}" alt="Gmail trigger through Document Split, OCR, LLM, and post-processing to ERP" style="max-width: 100%; height: auto; display: block; margin: 0 auto; border: 1px solid #e5e7eb; border-radius: 8px;" />
</p>

### Configuring a node

Click any node to open its panel. The **Run LLM** node lets you pick one of your organisation's DocRouter prompts and runs it against binary items from upstream nodes:

<p class="my-4">
  <img src="{{ '/assets/images/docrouter_flow_llm_node.png' | relative_url }}" alt="Run LLM node — prompt selection, input schema, and output panel" style="max-width: 100%; height: auto; display: block; margin: 0 auto; border: 1px solid #e5e7eb; border-radius: 8px;" />
</p>

---

## Cloud document connectors

Built-in trigger and action nodes for common enterprise sources:

| Source | Trigger | Action nodes |
|---|---|---|
| Gmail | Poll for messages matching a search query | Send, reply, update labels |
| Microsoft Outlook | Poll by received date | Send, reply, forward, move, flag |
| Google Drive | Watch a folder for new or updated files | Search, download, create folder, move, delete |
| Microsoft OneDrive | Watch a path for new or updated files | Search, list, download, upload |

**Setup:**

1. **Create a credential** — **Settings → Credentials** → choose connector type (e.g. Gmail OAuth2) → complete OAuth.
2. **Add the trigger node** — select credential, set poll interval, optional filter (e.g. `from:vendor@acme.com has:attachment`).
3. **Wire the rest** — trigger emits one item per message or file; attachments arrive in the item's `binary` payload.

The connector list is not closed. Once the architecture is in place, new integrations follow the same pattern — manifest, credentials, HTTP executor — and can often be scaffolded quickly with AI coding assistants like <a href="{{ '/docs/cursor/' | relative_url }}">Cursor</a>.

### Recipe: Gmail → extraction → ERP

```
[Gmail trigger]
      │  (binary: pdf attachment)
      ▼
[Document Split]      ← one item per page
      │
   ┌──┴─────────────┐
   ▼                ▼
[Run OCR] ─────▶ [Run LLM]
                    │
                    ▼
        [Code (Python)]        ← shape fields for your ERP schema
                    │
                    ▼
          [HTTP Request]       ← POST to ERP or database
```

Example post-processing in a **Code (Python)** node:

```python
def run(items, context):
    """Normalize LLM extraction fields before posting to ERP."""
    out = []
    for item in items:
        data = item.get("extraction") or item
        out.append({
            "vendor_name": (data.get("vendor_name") or "").strip(),
            "invoice_number": data.get("invoice_number"),
            "invoice_date": data.get("invoice_date"),
            "total_amount": float(data.get("total_amount") or 0),
            "currency": data.get("currency") or "USD",
            "line_items": data.get("line_items") or [],
        })
    return out
```

The **HTTP Request** node references these fields with expressions — e.g. `={{ $json.invoice_number }}` in the POST body.

---

## Recipe: Human-in-the-loop

For cases where LLM confidence is low or regulations require human sign-off, combine **Branch**, **Code (Python)**, and **HTTP Request** nodes:

<p class="my-4">
  <img src="{{ '/assets/images/docrouter_flow_document_split.png' | relative_url }}" alt="Document upload through split, OCR, LLM, grouping, and branch to EHR or Slack" style="max-width: 100%; height: auto; display: block; margin: 0 auto; border: 1px solid #e5e7eb; border-radius: 8px;" />
</p>

Typical pattern:

1. **Document event trigger** → **Document Split** → **Run OCR** → **Run LLM** (extract patient or record identifiers).
2. **Code (Python)** groups pages and sets a `human_review` flag when grouping is ambiguous.
3. **Branch** routes clean records to an EHR integration; flagged records go to Slack, a ticketing system, or a review queue.
4. Optional second flow with a **Webhook trigger** waits for an approval callback before continuing.

Every execution records per-node inputs, outputs, timing, and logs in the **Executions** panel.

---

## Learn more

- [Architecture blog post]({{ site.baseurl }}{% post_url 2026-06-21-docrouter-flows-bringing-the-n8n-architecture-to-intelligent-document-processing %}) — Full walkthrough of the n8n model applied to IDP
- <a href="{{ '/docs/architecture/' | relative_url }}">Architecture</a> — Flows engine and system overview
- <a href="{{ '/docs/prompts/' | relative_url }}">Prompts</a> — LLM instructions used by the Run LLM node
- <a href="{{ '/docs/tags/' | relative_url }}">Tags</a> — Filter document event triggers and route uploads
- <a href="{{ '/docs/webhooks/' | relative_url }}">Webhooks</a> — Product event notifications (distinct from flow webhook triggers)
- <a href="{{ '/docs/workflows/' | relative_url }}">External workflows</a> — n8n, Power Automate, Temporal
- <a href="{{ '/docs/rest-api/' | relative_url }}">REST API</a> — Programmatic flow management (coming to SDK docs)
- <a href="{{ '/docs/open-source/' | relative_url }}">Open Source</a> — Apache 2.0 license and self-hosting

---

<div class="bg-blue-600 rounded-lg p-4 md:p-8 mt-8 md:mt-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-4">Build your first flow</h2>
  <a href="https://app.docrouter.ai" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-4 py-3 md:px-8 md:py-4 rounded-lg font-semibold text-base md:text-lg transition-colors duration-200 no-underline">
    Open Dashboard
  </a>
</div>
