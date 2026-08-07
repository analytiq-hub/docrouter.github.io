---
layout: case-study
title: "Consulting: Lab Informatics Support Chat"
subtitle: In-product AI support agent for Starlims LIMS
permalink: /case-studies/starlims-chat/
description: "Consulting engagement: in-product AI chat agent for Starlims LIMS—RAG over manuals and Zendesk to reduce support query resolution time for global lab teams."
---

*This describes a **consulting engagement**. As Tribe AI architect contractors, we built a **custom in-product chat agent** for Starlims. It is separate from the DocRouter product.*

## Overview

Starlims sought faster technical support for users of its LIMS suite—Life Sciences, Quality Manufacturing, Forensics, and Environmental Sciences. Working with Starlims engineering, we delivered an MVP chat agent embedded in the Starlims client, using retrieval-augmented generation (RAG) over product documentation and knowledge bases.

## The Challenge

Documentation was scattered across product manuals, installation guides, and Zendesk articles. Support engineers spent substantial time searching for answers, delaying resolution and raising operational cost. With many customer installations and potentially hundreds of users per site, Starlims needed a scalable, embedded assistant that would not disrupt existing systems, while keeping infrastructure cost low and answers accurate in a regulated scientific environment.

## What We Built

We designed an end-to-end AI chat agent embedded in the Starlims client via iframes, with multi-turn conversations grounded in retrieved documentation. The solution:

- Indexed Zendesk articles, manuals, and installation guides
- Delivered product-aware answers with semantic retrieval
- Ran on AWS with separate dev/prod environments
- Included offline and online evaluation (including Ragas) for accuracy, completeness, and cost

Retrieval accuracy figures cited during the engagement (for example, 95%+ on ground-truth datasets) applied to **this custom agent during the engagement**, not to DocRouter product claims.

## Key Capabilities

- **Knowledge integration** — Ingest and index Zendesk articles, manuals, and guides via Airbyte ETL
- **Semantic search** — RAG pipeline with Pinecone, hybrid semantic and keyword matching, multi-turn troubleshooting
- **Embedded UX** — Iframe integration into Starlims clients with license-key authentication across environments
- **Evaluation framework** — Offline and online assessments to keep responses reliable before broader rollout

## Technical Approach

### Knowledge pipeline
- ETL sync of Zendesk knowledge bases to S3 on a recurring cadence, with custom chunking for embeddings
- Processing of manuals, guides, and articles with duplicate and attachment filtering
- Pinecone vector storage for fast retrieval, including room for customer-specific indices

### Stack
- **AWS** — ECS/EC2 for chat servers, S3 for knowledge storage, Terraform for IaC
- **[MongoDB]({{ '/tech/programming/ai/databases/why-i-prefer-mongodb-for-ai-applications/' | relative_url }})** — AI portal and evaluation traces
- **Next.js & FastAPI** — Chat server and evaluation interfaces
- **Pinecone** — Serverless vector search
- **Airbyte** — Open-source ETL for Zendesk

### AI approach
- OpenAI/OpenRouter LLMs with domain-specific prompting for grounded answers
- Multi-product support across Starlims lines (LS, QM, FR, ES), with per-product indices planned for later versions
- Continuous improvement via AI portal dashboards and feedback loops
- The AI portal was based on our open-source project [SigAgent.AI](https://sigagent.ai) ([GitHub](https://github.com/analytiq-hub/sig-agent))

## Engagement Outcomes

- Internal rollout to support and product teams, with pilots showing strong accuracy and satisfaction
- Designed to **significantly reduce support query resolution time** and scale across sites without proportional infrastructure growth
- Modular design left room for agentic integrations, query rewrite, hybrid search, and monitoring dashboards

## Client Feedback

{% include testimonial-card.html
    quote="Andrei was instrumental to our efforts to build a foundation of our AI co-pilot and chat assistant at STARLIMS. Andrei quickly learned the STARLIMS product, tech, goals and deliverables. In just a few months, in partnership with our team, he delivered a foundation that will transform our business by reducing both development and support times for STARLIMS and our customers."
    name="Lauren Whitsell"
    title="Product Manager"
    company="STARLIMS"
    image="/assets/images/lauren_whitsell.jpg" %}

## Relationship to DocRouter

This engagement was **in-product support agent work**, not DocRouter document extraction. The observability portal drew on [SigAgent.AI](https://sigagent.ai). Patterns around RAG evaluation, knowledge ingestion, and embedded chat inform how we think about [chat agents]({{ '/docs/chat-agents/' | relative_url }}) and agent monitoring more broadly.

For more details, contact Andrei Radulescu-Banu at andrei@docrouter.ai.
