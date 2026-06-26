---
layout: case-study
title: "Prior Consulting: Epic EHR Order Automation"
subtitle: Custom Epic integration for DME order processing
permalink: /case-studies/epic_dme_order_processing/
---

*This describes a **prior consulting engagement**, not a DocRouter customer deployment. We built a **custom Epic automation system** for a DME provider; it is **not** DocRouter and should not be read as a DocRouter case study.*

## The Challenge

A Durable Medical Equipment (DME) provider serving major regional health systems faced a growing share of CPAP orders originating in Epic EHR. Staff spent hours daily pulling orders from Epic's In Basket, locating supporting documents (facesheets, sleep studies, office notes), and handling duplicates across chart types—work that was costly, error-prone, and hard to scale as hospitals reduced fax-based workflows.

Medicare documentation requirements added compliance pressure on top of operational cost.

## What We Built

We delivered a **custom zero-touch Epic automation system** for this client that:

- Automated Epic login (including MFA handling via AWS SES)
- Retrieved facesheets, orders, notes, encounters, and related artifacts
- Cached and processed downloads through OCR and LLM parsing pipelines
- Deduplicated orders and documents with content-similarity logic
- Connected into existing fax and Brightree MyForms workflows

This was bespoke engineering for one client environment. It is separate from the DocRouter SaaS product.

![Epic EHR Integration]({{ '/assets/images/case-studies/epic-dme/epic-dme-hero.png' | relative_url }})
*Custom Epic automation built in a prior consulting engagement*

## Technical Approach

### Epic integration pipeline
- Selenium-based RPA for Epic access with automated MFA code retrieval
- Scraping of CC'd patient lists and download of chart artifacts into MongoDB-backed caching
- SQS and Databricks jobs for reassembly, OCR, and LLM parsing
- AWS S3, Terraform, and Lambda for storage and event-driven processing

### Processing goals in the engagement
- Structured extraction from orders, notes, media, and encounters
- Deduplication of duplicate orders and documents
- Filtering of non-DME artifacts before downstream steps
- Documentation sequencing aligned with Medicare-oriented review requirements

Any percentage improvements (processing time, error rates, operational overhead) reported in earlier versions of this page referred to **targets or measurements within this custom build during the engagement**, not guaranteed DocRouter outcomes.

## Engagement Outcomes

In tested workflows, the client was able to:

- Reduce manual Epic retrieval work substantially compared with the prior manual process
- Process orders faster in automated paths that previously took hours
- Scale order handling without linear headcount growth for the automated portion

We are not publishing specific dollar ROI figures here; those depended on the client's internal cost structure and deployment scope.

## Relationship to DocRouter

Epic-specific RPA and deep EHR scraping remain **custom integration** work. DocRouter today focuses on document ingestion, extraction, validation, and API-driven integration patterns that can complement—but are not the same as—this engagement.

For related healthcare document processing on DocRouter, see the [DME solution]({{ '/solutions/dme/' | relative_url }}) page.

For more details, contact Andrei Radulescu-Banu at andrei@docrouter.ai.
