---
layout: docs
title: "Datos Insights Insurance AI Showcase — Interview Responses"
permalink: /docs/datos-insights-insurance-ai-showcase/
description: "Spoken answers for the December 2026 Datos Insights Insurance AI Showcase. Internal prep."
published: false
---

Internal prep for the December 2026 Datos Insights Insurance AI Showcase. Do not name the carrier. The claims deployment and the wholesaler pilot may be described only as anonymized examples.

Send Datos two capabilities: **Data Readiness** and **Technology and Infrastructure**. If they want a third tag, add **Human-AI Oversight**. The claims work is the proof of that one: the agent recommends, a person decides, and the package can be reconstructed.

Line for the holding slide. Datos will not ask about the company facts. DocRouter is the index and pipeline layer in front of a carrier's archive. It does not replace the system of record.

## 2. What problem are you solving?

The system of record already has the files. It is not shaped for an AI pipeline. Claims and policy content sit in a content system whose document types drifted over years of configuration. The tags a clerk uses are not the tags a model can trust. A multi-terabyte data lake does not fix that. A lake is built for batch and bulk jobs. Discovery, extraction, and a knowledge base an agent can cite are a different layer, and that layer is missing.

It shows up differently by company. A large P&C carrier feels it as cycle time after first notice of loss: the file is open, the endorsements are somewhere in the archive, and an adjuster still assembles the first coverage pass by hand. A smaller carrier or an MGA feels it as headcount on submissions, often handwritten ACORD forms, clearance, and rekeying into an agency system. Life is slower and more application-driven. The acute cases are the same shape everywhere: a live archive or a lake, high document variety, and a leadership ask to put an agent on top before the documents are indexed for that agent.

The carriers who feel it first are the ones whose documents are the product. Claims shops. Wholesale and MGA submission desks. Anyone whose core system is excellent at the structured record and blind to the PDF behind it.

## 3. What is happening in the market?

Eighteen months ago the request was field extraction. "Read this ACORD, this invoice, this loss run, and give me the fields." That is the intelligent-document-processing bake-off, and it is what Hyperscience and Indico are built for.

The request now is an agent that can answer a question from the file: is this loss likely covered, which form governs it, what is still missing. Extraction is still required. It is no longer the whole job. What changed is that boards started asking for agents, and the archives were never indexed for retrieval.

The market is splitting. Capture vendors are adding workflow around keying. Core-system vendors are adding copilots that only see what is already structured. Lakes are filling up with unstructured files and still cannot answer "which endorsement applies." Over the next 12 to 18 months the carriers who get value will be the ones who put an index, a knowledge base, and a human review step on the archive they already have. The chat pilots that cannot cite a passage will get shut off.

## 4. What does the product do?

Bumper sticker: **an AI index for the archive.**

A connector indexes the content system or the lake. It stores the location and the metadata, and it fetches the page when a pipeline needs it, rather than standing up a second copy of the archive. Tags decide what happens next. A tag runs OCR, runs an extraction schema, and admits the document to a knowledge base. People use the product through the UI to search, filter, and review. The same index is an API, so an agent or a downstream system can call it. The pipeline itself, from classification through extraction to a cited answer, can run inside DocRouter.

That is the integration story. DocRouter sits beside the core, whether that is a policy admin system, a claims content system, or an S3 lake. Security review is a service account, on-demand reads, and an on-premises option when the bytes cannot leave. An MGA without a full core uses the same path with a thinner front door: email, API, or a bucket. The taxonomy and the schemas are the work. The core replacement is not.

Against Hyperscience and Indico, the split is the job each product optimizes. Those platforms are built to teach a model a form and key it into another system, with a strong review step for that keying. DocRouter is built for the layer in front of a live archive: tag the file, extract what a workflow needs, and keep a knowledge base an agent can search with the passage attached. Cases group the documents that belong together. The system of record stays the store.

## 5. Pitfalls

**Latency.** The index is what is always on. The bytes are read when an agent needs that document, not when the whole drawer is copied. On a claim, the first investigation pass can run from the notice of loss and the policy context already available, and it refreshes when a new document arrives. Structured policy data still comes from the core system's API. DocRouter is not a second policy admin system. If the loss history is not in the archive yet, the output says it is missing.

**Multi-step work, and where the person stays.** A claims pass is a fixed sequence, not one prompt. Gather the file. Run the checks that have to be explainable in an audit, such as territory and policy age, as rules. Fan out by coverage. Search the forms the carrier actually issues. Draft a finding, critique it, and store a package: recommended actions, questions for the insured, and the passages that were read. The adjuster decides. The same pattern fits underwriting triage. Low-confidence extractions stop for a person before they move downstream.

**The question a CTO should ask.** "When the source document changes, what in the index, the extraction, and the agent trace is marked stale, and can you show me exactly what the model read?" A weak answer is "the model has the documents." The answer you want is versioned prompts, cited chunks, a trace, and derived data that goes stale with the original.

## 6. ROI

Clients are buying cycle time and a stop to rekeying. On claims, that is the time from first notice to a cited first pass. On submissions, it is clearance work that today takes hours of reading. The cost is new infrastructure. It replaces manual assembly and some outsourced keying. It does not replace the adjuster or the underwriter.

What the carrier puts in is access, a sample of real files, and a reviewer for the first schemas. The taxonomy is the project. For a smaller carrier or an MGA that is one line of business, an inbox or a bucket, and a few weeks. For a large carrier the long pole is the security review and the connector, not the model.

On prompt debt: a prompt is bound to a tag and a schema, and it is versioned. A change is a release. We keep an offline set of real files with agreed outcomes, and in production the reviewer can mark a bad answer so that case joins the set. The prompts do not live in a chat log.

Pricing for a carrier is enterprise: a platform subscription plus usage, not a per-seat charge. The self-serve plans on the site are not the thing to describe on stage.

**Proof point, anonymized.** Say yes to this question, and use the claims story. At a mid-size P&C carrier, the gap after first notice was that the file could be opened and the coverage question still took a person digging through forms and endorsements. The deployment produces an adjuster-ready package: which coverages might apply, findings tied to the forms that carrier issues, the red flags that are rules rather than guesses, and the questions still owed to the insured. The agent does not deny and does not close the claim. The lesson was that the policy text had to be a curated knowledge base. A model that "remembers" a form will not survive an audit.

If they want a second example, label it as a pilot. A specialty wholesaler, about 7,000 submissions a year, roughly half handwritten. The pilot extracted ACORD fields, separated personal from commercial, and flagged low-confidence reads for a person. In test samples, typed forms were above 90 percent and handwritten forms around 80 percent, with review on the rest. That one is a pilot, not a production rollout.

## 7. Roadmap, next 12 months

The index, the connectors, tag-driven OCR and extraction, and the knowledge base are in the product. The next year is about operating that layer at carrier scale: bulk runs over a drawer or a lake, webhooks so the core system can subscribe to a result, retention that matches a carrier's schedule, and flows so a multi-step claims or submission chain is configured rather than coded. Quality work follows the evidence from review: better chunking and retrieval where the citations are weak. The direction is the same as the talk. Make the archive something an agent can use, and keep the person on the decision.

## 8. The one thing

The archive is not an AI system. An agent on top of an unindexed content system, or on top of a data lake, will guess. The work is the index, the extraction, and the knowledge base in front of the files the carrier already has, with a person still closing the decision.

## If they fall back to the spare questions

**Resource constraints.** The scarce thing is not a model. It is people who know the document types. The staff who can say what a drawer means are retiring or buried in the queue. DocRouter's ask of them is a taxonomy and a review of the first schemas, not a data-science team.

**Client data.** Unstructured files stay unstructured until a tag puts them through OCR and a schema. Structured fields from the core stay in the core and are read when needed. The knowledge base is built from the documents the carrier governs, scoped by tag, so a claims agent searches issued forms and endorsements rather than the whole lake.
