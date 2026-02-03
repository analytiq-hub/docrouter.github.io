---
marp: true
theme: docrouter
paginate: true
title: DocRouter.AI — Technical Deep Dive
description: Architecture, workflow, and integration details
---

<!-- _class: lead -->

# DocRouter.AI

## Technical Deep Dive

Architecture, APIs, and integration patterns for engineering teams.

<div class="cta center mt-5">
  <a class="btn btn-primary" href="https://docrouter.ai/docs">Read the Docs</a>
  <a class="btn btn-secondary" href="https://app.docrouter.ai">Open Console</a>
</div>

---

# End-to-end pipeline overview

Document-to-data: unstructured files → structured JSON → API or webhooks.

1. **Ingest** — email, web UI, REST API, SDKs
2. **Normalize** — OCR, segmentation, image cleanup
3. **Route** — tag-based mapping to prompts and schemas
4. **Extract** — prompt-driven field extraction
5. **Validate** — schema + confidence checks
6. **Deliver** — webhooks, API pulls, workflows

Tags connect uploads to prompts.

---

# Ingestion and normalization

**Ingestion:** Web UI, email, REST API, Python/TypeScript SDKs

**Normalization:** OCR, layout analysis, multi-page handling, image enhancement (deskew, denoise)

---

# Tags + prompts + schemas = deterministic routing

Tags define document intent and drive deterministic routing.

**Onboarding sequence**
1. Create a tag and prompt
2. Attach schema to prompt (typed output)
3. Upload documents with the tag
4. Results appear immediately

**Why this matters**
- No ambiguity about which prompt runs
- Stable outputs as document volumes grow
- Fast iteration on prompt quality

---

# Prompt-driven extraction

Prompts specify the extraction logic in natural language and control:
- What fields to extract
- Where to look for each field
- How to handle missing or ambiguous values
- Formatting requirements (dates, currencies, IDs)

Prompts are linked to tags, ensuring deterministic routing.

---

# Schemas enforce typed output

- Strongly typed outputs (strings, numbers, arrays, objects)
- Stable downstream integrations
- Field-level validation

Example:
```json
{ "invoice_number": "string", "invoice_date": "date",
  "vendor_name": "string", "total_amount": "number" }
```

---

# Confidence and review workflow

DocRouter supports auto-first processing with optional human review.
- Confidence thresholds can trigger review
- Review UI for field-level correction
- Auditability for regulated workflows

---

# Results delivery patterns

**Delivery options**
- **Webhooks:** event-driven completion callbacks
- **REST API:** polling or on-demand pulls
- **Workflows:** n8n or Temporal integration

Typical webhook payload includes document ID, status, and extraction JSON.

---

# API integration surface

Core REST endpoints:
- `POST /documents` — upload
- `GET /documents/{id}` — status
- `GET /documents/{id}/extractions` — results
- `POST /webhooks` — register callbacks

SDKs wrap these endpoints with typed clients.

---

# AI agent and MCP integrations

DocRouter ships an MCP server so AI agents can:
- Upload documents
- Fetch extraction results
- Reason over outputs
- Orchestrate multi-step workflows

---

# Document classes and common schemas

**Classes:** Invoices, insurance apps, bills of lading, medical auth, PE reports

**Common fields:** Identifiers, dates (issue/due/effective), parties, line items and totals

---

# Implementation checklist

1. Define document classes and tags
2. Draft prompts for each class
3. Attach schemas for typed outputs
4. Upload sample docs and iterate
5. Wire webhooks or API pulls
6. Add review step if needed

---

<!-- _class: closing -->

# Questions?

<div class="cta center mt-5">
  <a class="btn btn-primary" href="https://docrouter.ai/docs">Documentation</a>
  <a class="btn btn-secondary" href="mailto:hello@docrouter.ai">Contact Us</a>
</div>

**docrouter.ai**
