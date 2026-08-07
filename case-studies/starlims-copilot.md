---
layout: case-study
title: "Consulting: Lab Informatics Coding Copilot"
subtitle: AI-powered VS Code copilot for Starlims LIMS development
permalink: /case-studies/starlims-copilot/
description: "Consulting engagement: AI coding copilot for Starlims LIMS with VS Code, Claude, and MCP—reducing form and script configuration time for XFD, SSL, and JavaScript."
---

*This describes a **consulting engagement**. As Tribe AI architect contractors, we built a **custom coding copilot** for Starlims. It is separate from the DocRouter product.*

## Overview

Starlims, a laboratory information management system (LIMS) provider spanning Life Sciences, Quality Manufacturing, Forensics, and Environmental Sciences, needed to accelerate custom development in proprietary languages.

From concept through MVP, we delivered a VS Code–integrated coding copilot using [Claude Code]({{ '/ai/programming/tech/reviews/claude-code-vs-cursor-july-25/' | relative_url }}) and a custom Model Context Protocol (MCP) server for automated generation of XFD forms, SSL scripts, and JavaScript.

## The Challenge

Starlims developers spent significant time on manual coding in specialized languages, driving high implementation cost and slow customer-specific lab workflow configuration. The MVP needed to support a small set of internal users while remaining extensible to broader teams—automating repetitive form design and script work, connecting to complex data sources, and staying accurate in regulated environments. Existing tools did not integrate with Starlims' proprietary systems.

## What We Built

We architected an end-to-end coding copilot embedded in VS Code so developers could generate, modify, and validate code with natural language prompts. The MVP included:

- Local file mirroring for safe edits
- RAG-based knowledge retrieval from Pinecone indices
- MCP tools for database discovery and schema-aware coding
- Offline evaluation against ground-truth tasks (steps, token usage, accuracy)

Deployed locally with a single-script installer, the copilot was designed to cut form and script development cycles and support iterative internal testing ahead of broader rollout.

## Key Capabilities

- **Automated code generation** — Prompt-based creation and modification of XFD forms, SSL scripts, and JavaScript
- **Integrated data tools** — MCP utilities to discover tables, query schemas, and fetch sample rows without leaving VS Code
- **Local file mirroring** — Mirrored checkout environment with bridge components for legacy forms and a "Designer Lite" preview
- **Evaluation harness** — Offline ground-truth assessments measuring completeness, token efficiency, and accuracy

## Technical Approach

### Coding pipeline
- Local MCP server processes prompts via Claude Code and integrates with Starlims servers for file checkout and push
- Natural language prompts trigger tools such as `get_table_schema` and `global_find` for schema-aware generation
- Files are mirrored locally for safe iteration; sync was manual in the MVP, with automation planned for later versions

### Stack
- **AWS** — S3 for knowledge bases (SSL/XFD/JS), ECS for dev instances, Terraform for IaC
- **Pinecone** — Vector indices for RAG over manuals and code snippets (separate indices for XFD and SSL)
- **[MongoDB]({{ '/tech/programming/ai/databases/why-i-prefer-mongodb-for-ai-applications/' | relative_url }})** — AI portal data for evaluation traces and telemetry
- **Next.js & FastAPI** — AI portal for monitoring copilot usage
- **VS Code extension** — Bridge for form visualization and SCM check-in/out APIs

### AI approach
- Claude Code with MCP for domain-specific coding tasks
- Custom tools such as `discover_tables` and `query_table` for database-aware scripts
- Activation wizard to install MCP, download skills, and configure `.mcp.json` for Pinecone and Starlims credentials
- AI portal dashboards for metrics and feedback loops

Accuracy figures cited during the engagement (for example, 90%+ on evaluation sets) applied to **this custom copilot during the engagement**, not to DocRouter product claims.

## Engagement Outcomes

- Internal pilots with developers across QM, LS, LPH, and FR teams validated the MVP and surfaced usability feedback
- The platform helped Starlims **significantly reduce form and script configuration time** for participating teams
- Extensible design left room for later features such as deeper Claude SDK integration in VS Code and fuller Form Designer embedding

## Client Feedback

{% include testimonial-card.html
    quote="Andrei helped us bring several AI initiatives to MVP stage. I was impressed with Andrei's expertise across a wide range of subjects. He has a deep understanding of AI and software architecture and the experience with real-life implementation to turn ideas into production-ready solutions. Thanks to his contributions, we made tremendous progress and significantly accelerated our AI roadmap.

    Would definitely recommend him to any team that is looking for guidance in implementing AI. He is an outstanding engineer and architect."
    name="Marius Popovici"
    title="Senior Software Engineering Manager"
    company="STARLIMS"
    image="/assets/images/marius_popovici.jpg" %}

## Relationship to DocRouter

This engagement was **agent and developer-tooling work**, not document extraction. Patterns around MCP tooling, offline evaluation, and AI portal observability overlap with how we build and monitor agents elsewhere in our stack (including [SigAgent.AI](https://sigagent.ai)).

DocRouter remains focused on document ingestion, extraction, validation, and API-driven workflows. For related agent topics, see [How to train your AI agent]({{ '/ai/programming/tutorials/how-to-train-your-ai-agent/' | relative_url }}) and [offline evaluation for AI agents]({{ '/ai/engineering/offline-evaluation-for-ai-agents/' | relative_url }}).

For more details, contact Andrei Radulescu-Banu at andrei@docrouter.ai.
