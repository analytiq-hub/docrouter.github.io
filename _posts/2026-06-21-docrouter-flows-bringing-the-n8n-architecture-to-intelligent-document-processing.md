---
layout: post
title: "DocRouter Flows: Bringing the n8n Architecture to Intelligent Document Processing"
date: 2026-06-21 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: /assets/images/docrouter-flows-splash.png
categories: [ai, engineering]
description: "How DocRouter Flows brings the n8n workflow model to intelligent document processing — visual canvas, typed items, pin data, execution logs, and document-native OCR and LLM nodes."
---

[n8n](https://n8n.io) popularised a way of building automation workflows that developers and power users actually want to use: a visual, node-based canvas where you connect steps into a pipeline, run it, inspect every input and output, and iterate fast. That model turned out to be exactly right for document AI too — and that is what DocRouter Flows is built on.

DocRouter is an open-source **Intelligent Document Processing (IDP)** platform, released under the **Apache 2.0 license**. It can be embedded freely in any commercial or internal product. While DocRouter can serve as a general-purpose workflow automation tool, its primary purpose is IDP: extracting structured data from unstructured documents — PDFs, scanned forms, emails with attachments — using OCR, LLMs, and human-in-the-loop review. Flows is the automation layer that connects those capabilities into end-to-end pipelines.

The short version: **DocRouter brought the n8n architecture to IDP.**

<div class="rounded-xl border-2 border-blue-200 bg-gradient-to-br from-blue-50 to-indigo-50/90 p-5 md:p-6 my-6 shadow-md ring-1 ring-blue-100/50">
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6">
    <p class="text-gray-800"><strong class="text-blue-900">Before:</strong> Upload in DocRouter, wire webhooks to n8n or custom code, glue OCR and LLM steps yourself.</p>
    <p class="text-gray-800"><strong class="text-blue-900">Now:</strong> Drag a canvas: <strong>Gmail → Split → OCR → LLM → ERP</strong> — one product, full execution log.</p>
  </div>
</div>

Here is what a workflow looks like in the DocRouter Flows editor — a visual canvas of connected nodes, with per-step input and output you can inspect after each run:

![Gmail trigger through Document Split, OCR, LLM, and post-processing to ERP](/assets/images/docrouter_flow_post_to_erp_or_db.png)

And here is how you configure a node. Click any node to open its panel on the right. The **Run LLM** node, for example, lets you select one of your organisation's configured [DocRouter prompts](/docs/prompts/) from a searchable list. It runs that prompt against the **binary input items** arriving from upstream nodes — typically one PDF page or attachment per item. When an OCR node is connected to the second input port, the model also receives the matching page text alongside the binary.

![Run LLM node configuration — prompt selection, input schema, and output panel](/assets/images/docrouter_flow_llm_node.png)

---

## What DocRouter Flows shares with n8n

When we designed DocRouter Flows, we modelled it closely on n8n's execution model. If you have used n8n, the concepts will feel familiar.

**Visual, drag-and-drop flow design.** Flows are built on a canvas. You drag nodes from a palette, drop them onto the canvas, and draw connections between their output and input handles. The layout, node shapes, and connection style are intentionally compatible with n8n's look and feel.

**Typed input and output items.** Every node receives and produces a list of *items*. Each item carries a `json` payload (structured data) and a `binary` payload (file attachments — PDFs, images, or any binary blob). This is the same dual-channel data model n8n uses, and it means a single node can pass both extracted text and the original document binary to the next step without extra wiring.

**Expression system.** Node parameters accept expressions — prefixed with `=` — that reference outputs from any upstream node. For example, a parameter value can dynamically pull a patient name from the LLM node's output without writing any code. The syntax mirrors n8n's `$json` / `$node` reference model.

**Pin data.** Any node's output can be pinned: frozen to a saved snapshot. Downstream nodes then use the pinned data instead of re-executing. This is the same pin data feature n8n provides, and it is essential for iterating on one part of a flow without re-running expensive OCR or LLM calls every time.

**Execution log.** Every flow run records a per-node execution log: status (success / error / skipped), timing, the exact input items the node received, the output items it produced, any print output from code nodes, and a stack trace on error. The visual editor shows this inline — click any node after a run to inspect what flowed through it.

**Per-node error handling.** Each node has an `on error` setting: stop the run (default) or continue and pass an error-envelope item downstream. This matches n8n's `continueOnFail` behaviour and lets you build flows that degrade gracefully rather than halting entirely.

**Merge and branch nodes.** A branch node routes items to one of two output paths based on a condition. A merge node waits for all of its wired inputs to arrive before proceeding — the same synchronisation semantics n8n's merge node provides. Together they cover the most common control-flow patterns without any code.

**Code node.** A Python code node lets you drop arbitrary logic into a flow when no built-in node fits. It receives items, transforms them, and returns new items. The runtime is sandboxed.

**HTTP request node.** A generic outbound HTTP node supports all common methods, headers, query parameters, JSON and form bodies, and automatic binary response handling. It covers any REST API that does not have a dedicated connector.

**Webhook trigger.** A flow can be started by an inbound HTTP call. The webhook trigger supports both synchronous mode (the HTTP response is held open until the flow produces a result) and async mode (the call returns immediately and the flow runs in the background).

**Schedule trigger.** A flow can run on a cron schedule, with timezone support.

**Poll triggers.** Connector triggers poll external systems at a configurable interval and emit one item per new message or file found since the last check.

**Credential management.** OAuth tokens and API keys are stored once per organisation and injected into node executions at runtime. Credentials never appear in the flow graph itself.

**Disabled nodes.** Any node can be disabled. Disabled nodes are skipped during execution and pass their input through as an empty output, making it easy to test a flow without a particular step.

---

## What is different: DocRouter is an IDP platform

n8n is a general-purpose automation tool. DocRouter is purpose-built for intelligent document processing, and that shapes both which node types exist and how the platform is licensed.

### Document-native node types

DocRouter adds a category of nodes that have no n8n equivalent:

- **Document Split** — splits a multi-page PDF into one item per page, with configurable start, stop, and step slicing.
- **OCR** — runs optical character recognition on PDF pages using configurable providers. Produces per-page text output on a typed port.
- **LLM Run** — sends items to a configured LLM prompt. Accepts OCR text on a second typed port so the model always sees the right page's text alongside the item. Supports batching.
- **Document event trigger** — fires automatically when a document is uploaded to DocRouter, filtered by tag or other criteria. This is the entry point for fully automated document processing pipelines.

The typed port between OCR and LLM nodes is worth highlighting: the OCR node's output handle is a distinct type that only connects to the LLM node's second input. This prevents wiring mistakes and makes the pairing — one OCR result per page, matched to the corresponding LLM input item — explicit in the graph.

### Apache 2.0 license

DocRouter is Apache 2.0: you can embed it in any product, modify it, and redistribute it without restriction. This makes it suitable for ISVs building document automation into vertical SaaS products, healthcare platforms, legal tech, or financial services applications.

---

## Use Case 1: Connecting Cloud Document Sources

DocRouter includes trigger and action nodes for the four most common enterprise document sources.

| Source | What the trigger does | What the action nodes do |
|---|---|---|
| Gmail | Poll for new messages matching a search query | Send, reply, update labels |
| Microsoft Outlook | Poll for new messages by received date | Send, reply, forward, move, flag |
| Google Drive | Watch a folder for new or updated files | Search, download, create folder, move, delete |
| Microsoft OneDrive | Watch a path for new or updated files | Search, list, download, upload |

The four connectors above are examples, not a closed list. Once the connector architecture is in place — manifest schema, credential types, poll triggers, and the declarative HTTP executor — **adding a new integration is a matter of minutes**. Each connector follows the same pattern: define parameters, wire OAuth or API-key credentials, and describe the HTTP calls the node makes. The platform handles the rest (polling, item emission, binary attachment handling, execution logging).

That consistency is what makes AI coding assistants like [Cursor](https://cursor.com) so effective here. Point an assistant at an existing connector and the target API's documentation, and it can scaffold a new node package quickly: the conventions are explicit, the examples are right there in the repo, and there is little bespoke glue to invent. We have used this workflow ourselves — see [How We Built the DocRouter n8n Nodes With Cursor]({% post_url 2026-01-31-how-we-built-docrouter-n8n-nodes-with-cursor %}) — and the same approach applies inside DocRouter Flows. Need a Box, Dropbox, or Salesforce connector? The architecture is already built; filling in the next one is routine.

Setting up a connector takes three steps:

1. **Create a credential.** Go to Settings → Credentials, choose the connector type (e.g. Gmail OAuth2), and complete the OAuth flow. DocRouter stores the refresh token for your organisation.
2. **Add the trigger node.** Drag the trigger onto the canvas, select the credential, set a poll interval, and optionally filter (e.g. Gmail search query `from:vendor@acme.com has:attachment`).
3. **Wire the rest of the flow.** The trigger emits one item per new email or file. Binary attachments arrive in the item's `binary` payload, ready to pass directly to a Document Split or OCR node.

A minimal connector flow looks like this:

```
[Gmail trigger]
      │  (binary: pdf attachment)
      ▼
[Document Split]      ← one item per page
      │
   ┌──┴─────────────┐
   ▼                ▼
[Run OCR] ─────▶ [Run LLM]   ← OCR output pairs with LLM input
                    │
                    ▼
        [Code (Python)]        ← validate and shape fields for your ERP schema
                    │
                    ▼
          [HTTP Request]       ← POST to ERP or database
```

![Gmail trigger through Document Split, OCR, LLM, and post-processing to ERP](/assets/images/docrouter_flow_post_to_erp_or_db.png)

The code node is where you adapt LLM output to whatever your downstream system expects — field renaming, type coercion, dropping low-confidence rows, or collapsing per-page results into one payload:

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

The HTTP Request node then references these fields with expressions — for example, `={{ $json.invoice_number }}` in the POST body — and sends the result to your ERP or database endpoint.

The same pattern works identically starting from an Outlook, Google Drive, or OneDrive trigger — only the first node changes.

---

## Use Case 2: Multi-Step Document Processing with Human-in-the-Loop

Full automation is not always appropriate. A field may be missing, LLM confidence may be low, or a regulation may require human sign-off before data enters a system of record. DocRouter handles this by combining the branch node, the code node, and webhook callbacks into a review pattern.

### The scenario

A hospital receives pre-surgery document batches by email. Each batch is a single PDF that mixes pages for multiple patients: surgery schedules, consent forms, insurance cards, lab results — in no guaranteed order. The pipeline must:

1. Split the PDF into pages.
2. Run OCR and LLM extraction on each page to identify the patient and document type.
3. Group pages by patient.
4. Auto-file records where the grouping is confident.
5. Route records with ambiguous page assignments to a human reviewer.

### The flow

```
[Document event trigger]   ← fires on document.uploaded, filtered by tag
          │
          ▼
[Document Split]           ← one item per page
          │
    ┌─────┴─────────┐
    ▼               ▼
[Run OCR] ─────▶ [Run LLM]     ← extract patient name, DOB, MRN, document type
                    │
                    ▼
        [Code (Python)]    ← group pages by patient; flag unknowns
                 │
                 ▼
           [Branch]        ← route on human_review flag
              │   │
              │   └──▶  [HTTP Request]   ← auto-file to EHR (clean records)
              │
              └──▶  [HTTP Request]       ← post to review queue / Slack / ticketing
```

![Document upload through split, OCR, LLM, grouping, and branch to EHR or Slack](/assets/images/docrouter_flow_document_split.png)

The code node runs a patient-grouping algorithm: it normalises names, dates of birth, and medical record numbers, assigns pages to patient groups using MRN as the primary key (falling back to name + DOB), and marks any page that could not be placed as an unknown. If any unknowns remain, it sets a `human_review` flag on the output item.

The branch node reads that flag. Clean records flow automatically to the EHR integration. Records with unknowns are posted to a review queue — a Slack channel, a ticketing system, or a custom review UI — where a human can examine the flagged pages and resolve the grouping.

### Synchronous approval with a webhook

For cases where the flow must wait for a human response before continuing, a second flow handles the approval callback:

1. The first flow posts a review request to an external approval service, including a callback URL pointing to a DocRouter webhook trigger.
2. The reviewer inspects the document in their tool and clicks Approve or Reject.
3. The external tool calls the callback URL with the approval payload.
4. The webhook trigger fires the approval flow, which routes approved records to the EHR and rejected records to a correction queue.

The result is a complete human-in-the-loop cycle with a full audit trail: every execution records per-node inputs, outputs, timing, and logs, visible in the Executions panel.

---

## Summary

DocRouter Flows takes the workflow automation model that n8n made popular — visual canvas, typed items with JSON and binary payloads, pin data, execution logs, expressions, credentials, merge/branch/code/HTTP nodes — and extends it with document-native capabilities: OCR, LLM extraction, document splitting, and document event triggers.

The architecture is the same. The license is Apache 2.0, so it embeds freely in any product. And the domain is IDP: turning unstructured documents into structured, actionable data, with humans in the loop exactly where they are needed.

If n8n showed the world what visual workflow automation could look like, DocRouter shows what it looks like when that same architecture is purpose-built for intelligent document processing.
