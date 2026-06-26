---
layout: case-study
title: "Pilot: Insurance ACORD & Clearance Automation"
subtitle: Completed DocRouter pilot with a specialty insurance wholesaler
permalink: /case-studies/insurance_wholesaler/
---

*This was a **completed pilot**, not a production customer deployment.*

## The Challenge

A specialty insurance wholesaler processing roughly 7,000 submissions annually faced operational bottlenecks: about half of submissions were handwritten, requiring staff to manually extract data from ACORD forms, perform clearance searches in ALIS, and handle complex workflows. With hundreds of submissions per month and many hours of daily manual processing, the organization needed to test whether intelligent extraction could maintain regulatory compliance while reducing manual work.

## The Solution

We completed a **pilot on DocRouter** to automate insurance submission workflows while keeping human oversight for regulatory compliance. The pilot focused on handwritten and typed ACORD forms using OCR and LLM extraction, structured data output, and integration paths toward ALIS clearance workflows.

![Insurance Automation Platform]({{ '/assets/images/case-studies/insurance-wholesaler/insurance-wholesaler-hero.png' | relative_url }})
*DocRouter pilot: ACORD form processing and clearance automation*

## What We Proved in the Pilot

The pilot validated the following for this use case:

- **Document processing**: Handwritten and typed ACORD forms, including complex layouts and crossed-out text
- **Data extraction**: Key fields such as insured name, address, DOB, occupation, and agency information
- **Classification**: Personal vs. commercial lines and binding vs. brokerage categorization
- **ALIS integration path**: API-based clearance search and submission creation (tested in pilot scope)
- **Human-in-the-loop review**: Confidence scoring to flag low-confidence extractions before downstream steps
- **Compliance-oriented design**: Temporary data handling and audit-friendly review workflows

## Pilot Architecture

The pilot used DocRouter with supporting tooling typical of insurance document workflows:

### Ingestion & extraction
- Email forwarding and API upload for attachments
- AWS Textract OCR for handwriting, tables, and checkboxes
- LLM extraction against custom schemas for applicant, policy, and property fields
- Form-type detection (e.g. personal auto/homeowner) with low-confidence flagging

### Integration & review
- ALIS API exploration via Dyad for clearance searches and submission creation
- n8n for workflow orchestration during the pilot
- Split-screen review UI with source linking and color-coded confidence

### Platform patterns exercised
- Schema-driven ACORD extraction
- Confidence scoring (e.g. higher-confidence fields auto-proceed; lower-confidence fields flagged)
- Role-based review concepts for producers and underwriters
- Planned extensions documented in pilot scope: OFAC checks and broader AMS integration

## How the Pilot Ran

The pilot was executed in structured phases:

**Phase 1 — Discovery & analysis**: Review of SOPs, sample PDFs, and ALIS screenshots; synthetic documents for testing.

**Phase 2 — Platform setup**: Email forwarding to DocRouter and API configuration for uploads.

**Phase 3 — AI pipeline**: Prompt and schema development with OCR for handwriting; initial focus on personal lines (homeowners).

**Phase 4 — Integration**: ALIS API access and n8n orchestration for end-to-end clearance flows.

**Phase 5 — Review UI**: Color-coded validation interface with source linking.

**Phase 6 — Testing**: Edge cases (including multi-language documents) and documentation of follow-on work (OFAC, AMS).

## Pilot Findings

Results below are from **pilot testing and simulations**, not a live production rollout:

**Efficiency (pilot testing)**: Early testing indicated potential to automate a large share of clearance work—in pilot evaluation, on the order of **75%** of clearance steps—with manual entry reduced from hours to minutes per submission in tested scenarios. Projected staff-time savings were on the order of 7–14 hours per day at the wholesaler's volume.

**Accuracy (pilot testing)**:
- **90%+** on typed forms with LLM+OCR in pilot samples
- **~80%** on handwritten forms, with human review for remaining cases
- Fewer clearance search errors in tested validation flows

**Scale (simulation)**: Simulated handling of 600+ monthly submissions with document classification (personal vs. commercial) to stress-test the pipeline.

**Compliance**: Human review remained required before full automation; OFAC integration was scoped but not completed as part of this pilot.

## Relevance to DocRouter

This pilot showed DocRouter can support specialty insurance submission processing—including handwritten ACORD forms and clearance-oriented workflows. Capabilities developed here inform DocRouter's insurance solution patterns today.

For more details, contact Andrei Radulescu-Banu at andrei@docrouter.ai. Platform demo available at [app.docrouter.ai](https://app.docrouter.ai).
