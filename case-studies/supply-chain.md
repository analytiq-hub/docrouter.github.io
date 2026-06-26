---
layout: case-study
title: "Pilot: Supply Chain Trade Documents"
subtitle: DocRouter pilot for bills of lading, commodity reports, and related trade documents
permalink: /case-studies/supply-chain/
---

*This was a **pilot**, not a production customer deployment.*

## Overview

We ran a **DocRouter pilot** to test structured extraction from complex supply chain trade documents—primarily **bills of lading** and **commodity reports**—where manual processing was slow and error-prone.

![Supply Chain Automation]({{ '/assets/images/case-studies/supply-chain/supply-chain-hero.png' | relative_url }})
*DocRouter pilot: trade document extraction*

## The Challenge

A supply chain organization needed to process trade documentation with higher accuracy and less manual effort. The pilot focused on:

- **Bills of lading**: Shipment details, carrier information, and cargo specifications
- **Commodity reports and related trade documents**: Contract terms, quantities, and supporting certificate-style content

Manual processing created bottlenecks and made it difficult to feed downstream systems consistently.

## The Solution

We used DocRouter in a pilot configuration to extract and structure fields from representative bills of lading and commodity reports, with human review on critical documents.

A separate exploratory track looked at security and SOP-style documents; that work informed future scope but was **not** the primary focus of this pilot.

## Capabilities Tested

### Trade documents (primary pilot scope)

* **Bills of lading**: Extraction of shipment, carrier, and cargo fields
* **Commodity contracts and reports**: Parsing of terms, quantities, and key metadata
* **Sampling certificates**: Extraction of certification and testing fields where present
* **Letters of credit** (sample documents): Structured field extraction in pilot samples

### Security documentation (exploratory)

We explored extraction patterns for security profiles, SOPs, and risk analysis documents. These informed possible extensions but should not be read as completed production capabilities from this pilot.

## Pilot Architecture

The pilot used OCR and LLMs on PDFs and scanned images, including multi-language samples where provided.

**Processing approach**:
- OCR for initial text extraction
- LLM-based structuring against defined schemas
- Validation and human review for critical documents
- Output structured for downstream systems (integration tested at pilot scope)

**Trade-document targets evaluated** (not all were production-hardened in the pilot):
- Commodity contract term extraction
- Bill of lading field extraction and normalization
- Certificate field extraction from sample documents

## Pilot Observations

The pilot showed meaningful improvements in tested scenarios:

- **Processing time**: Complex documents moved from **hours to minutes** in pilot runs
- **Accuracy**: Improved consistency through schema-driven extraction and review
- **Workflow**: Staff could focus on exceptions rather than full manual re-keying

These results reflect **pilot conditions** on sample and provided document sets—not a guaranteed outcome for every production environment.

## Relevance to DocRouter

This pilot validated DocRouter for bills of lading, commodity reports, and related trade documents. Patterns from the pilot inform our [supply chain solution]({{ '/solutions/supply-chain/' | relative_url }}) page.

For more details, contact Andrei Radulescu-Banu at andrei@docrouter.ai. Platform demo available at [app.docrouter.ai](https://app.docrouter.ai).
