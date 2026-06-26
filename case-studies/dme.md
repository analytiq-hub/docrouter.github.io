---
layout: case-study
title: "Prior Consulting: DME Automation Platform"
subtitle: Custom healthcare document platform that informed DocRouter
permalink: /case-studies/dme/
---

*This describes a **prior consulting engagement**, not a DocRouter customer deployment. We built a **custom platform** for a healthcare startup client; that work was a **precursor to DocRouter** and helped shape the product.*

## Overview

A healthcare startup engaged us for a zero-to-ten implementation to digitize Durable Medical Equipment (DME) Medical Necessity Review—verifying patient eligibility, insurance coverage, and medical justification before approving equipment such as wheelchairs, oxygen concentrators, and CPAP machines.

We built their core document-processing platform from the ground up. That custom system later informed what became DocRouter.

![Illustration of a doctor with a patient in a wheelchair]({{ '/assets/images/case-studies/dme/dme.png' | relative_url }})
*Custom DME document platform built in a prior consulting engagement*

## The Challenge

The startup needed a cloud platform to replace manual, paper-based review workflows. They had industry expertise and pilot partnerships but needed engineering help to turn the product vision into a scalable foundation.

## What We Built

We delivered a **custom end-to-end document automation platform** (not DocRouter) that:

- Ingested faxes and related medical documents from common fax providers
- Extracted structured data with OCR and LLMs
- Supported operator review of AI extractions
- Integrated with DME systems such as Brightree and HDMS

During the engagement, the platform processed high document volumes in the client's environment and materially reduced manual review time compared with their prior workflow.

## Technical Approach

### Ingestion & processing
- Fax PDF ingestion on a frequent polling cadence
- AWS S3 storage with Textract OCR and LLM extraction
- Extraction of demographics, coverage, prescriptions, and supporting clinical fields
- Parallel processing for throughput during peak loads

### Stack (client platform)
- AWS S3, MongoDB, PostgreSQL, Databricks, Prefect, Terraform
- Label Studio and MLflow for annotation and experimentation
- API integrations toward Brightree and HDMS

Metrics such as extraction accuracy and throughput described in the original write-up applied to **this custom platform during the engagement**, not to DocRouter as a product today.

## Outcomes for Our Client

The following outcomes refer to **the startup we supported**, not to DocRouter customers:

- Their pilot sites adopted the custom platform for core review workflows
- The client grew its engineering team significantly during the engagement period
- The platform supported the startup's fundraising and product narrative at the time

We do not present this engagement as evidence of DocRouter production deployments or DocRouter customer ROI.

## Relationship to DocRouter

Patterns proven in this consulting work—schema-driven extraction, human-in-the-loop review, fax and EHR-adjacent ingestion, healthcare compliance constraints—directly influenced DocRouter's architecture and roadmap.

For DocRouter capabilities today, see the [DME solution]({{ '/solutions/dme/' | relative_url }}) page and [platform documentation]({{ '/docs/platform/' | relative_url }}).

For more details, contact Andrei Radulescu-Banu at andrei@docrouter.ai.
