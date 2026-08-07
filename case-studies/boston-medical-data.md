---
layout: case-study
title: "Boston Medical Data"
subtitle: DocRouter for anesthesia RCM packet processing
permalink: /case-studies/boston-medical-data/
description: "Boston Medical Data runs DocRouter on-prem for anesthesia revenue cycle—classifying multi-page surgery packets, grouping by patient, and extracting billing-critical fields at 99.9% precision across 175,000+ documents."
---

*This is a **live DocRouter deployment** (on-prem).*

## Overview

[Boston Medical Data](https://bostonmds.com) processes high-volume peri-operative document packets for **anesthesia revenue cycle management (RCM)**. Packets arrive as mixed fax/PDF bundles—often covering many patients and facilities in a single file—and must become validated, patient-level structured data for billing workflows.

DocRouter runs **on-premises** in their environment. The live path is a **native DocRouter workflow**: upload → page split → OCR → page classification → patient grouping → per-patient PDF merge and downstream extraction, with human review when pages cannot be assigned confidently.

## The Challenge

Anesthesia RCM depends on complete, accurate encounter and coverage data pulled from messy clinical packets:

- **Multi-document bundles** mixing surgery schedules, cover sheets, demographics, insurance cards, pre-op forms, and anesthesia records
- **Wide page range** — packets from a single page up to hundreds of pages (up to ~500)
- **Many facilities and schedule formats** in the same operational pipeline
- **Billing-critical fields** — patient identity, MRN, insurance, procedure timing, providers, ASA status, and related clinical details
- **Scale** that made manual split-and-key entry slow and error-prone

Staff previously had to visually sort packets by patient, then re-key structured fields into RCM systems—work that did not scale with packet volume or page count.

## The Solution

We deployed DocRouter for end-to-end packet processing aligned to anesthesia RCM:

1. **Ingest** tagged multi-page PDFs (fax and scan packets)
2. **Split and OCR** each page (Textract in the live flow)
3. **Classify** page type and extract identity anchors (name, DOB, MRN) in one pass
4. **Group** pages into patient sets; separate schedule and cover pages
5. **Merge** per-patient PDFs for targeted extraction (demographics, insurance card, anesthesia record, and related schemas)
6. **Flag** unassigned pages for human review before downstream RCM action
7. **Emit** structured JSON via API for billing and ops systems

### Common pattern

**Messy document packets → validated structured data → workflow action**

## What Runs in Production

### Native DocRouter workflow (live path)

On `document.uploaded` for the anesthesia packet tag, the flow:

- Splits the PDF into pages
- Runs OCR and the page-classifier LLM prompt in parallel per page
- Executes a code step that groups pages by MRN or name+DOB (with adjacency heuristics for weakly identified pages), builds one merged PDF per patient, and sets `human_review` when unknown pages remain

That native flow is what runs in production today.

### Temporal during development

Before DocRouter had built-in workflows, we prototyped the same pattern with [Temporal](https://temporal.io/) in [`doc-router-temporal`](https://github.com/analytiq-hub/doc-router-temporal): chunk pages, classify, group patients, create patient PDFs, extract insurance cards, with durable retries and polling.

Temporal was the **development and early orchestration path**. Once native DocRouter workflows were ready, production moved to the built-in flow. The technical write-up of that Temporal design is in [How To Create Document Workflows With Temporal And DocRouter.AI]({% post_url 2025-12-25-how-to-create-document-workflows-with-temporal-and-docrouter-ai %}).

## Extraction Library

Schema-driven prompts cover the RCM packet surface:

| Capability | Role in anesthesia RCM |
|---|---|
| **Packet page classifier** | Labels cover, surgery schedule, pre-op, anesthesia record, demographics, insurance card, ID card, or unknown—and pulls patient identity fields for grouping |
| **Surgery schedule batch** | Extracts multi-patient encounters (times, surgeon, MRN, room, procedure) from OR schedules across facilities |
| **Patient demographics** | Face-sheet / registration demographics plus primary, secondary, and tertiary insurance |
| **Insurance card** | Member ID, plan, group, Rx BIN/PCN, payer ID |
| **Anesthesia record** | Diagnoses, procedures, surgeons, anesthesia providers/CRNAs, start/stop times, ASA, block type |
| **Epic anesthesia record** | Combined demographics/insurance with Epic Procedure Summary care-team rules |
| **Presurgery features** | Deeper clinical extraction (ASA, PONV risk, airway, meds, labs, history) when the packet includes preprocedure documentation |

Downstream RCM systems consume the structured output; reviewers intervene only on flagged pages and low-confidence edge cases.

## Outcomes

Results below are from **Boston Medical Data's live on-prem DocRouter deployment**:

- **175,000+ documents** processed
- **1–500 pages** per document
- **99.9% precision** on extractions in production
- **Human-in-the-loop** retained for pages the classifier cannot assign to a patient group
- **API-ready structured data** feeding anesthesia RCM workflows

## Relevance to DocRouter

This deployment is DocRouter's primary **live healthcare customer proof** for multi-document packet processing: on-prem operation, native workflows at volume, and schema libraries tuned for anesthesia RCM—not a one-off consulting build.

It also shaped the product path from external Temporal orchestration to **first-class DocRouter workflows** for the same classify → group → extract pattern.

For more details, contact Andrei Radulescu-Banu at andrei@docrouter.ai. Platform demo available at [app.docrouter.ai](https://app.docrouter.ai).
