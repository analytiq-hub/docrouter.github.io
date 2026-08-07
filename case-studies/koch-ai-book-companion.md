---
layout: case-study
title: "Consulting: Koch AI Book Companion"
subtitle: Multi-agent companion for Principle-Based Management education
permalink: /case-studies/koch-ai-book-companion/
description: "Consulting engagement: multi-agent AI book companion for Koch Industries—enterprise auth, per-user memory, and observability for public readers and employees."
---

*This describes a **consulting engagement**. Koch Industries engaged Tribe AI to build an intelligent Book Companion; we served as a **subcontractor**, providing hands-on technical leadership and architecture. This work is separate from the DocRouter product.*

## Overview

Koch Industries set out to make Principle-Based Management (PBM)—from the book by Chase and Charles Koch—accessible to both the reading public and Koch employees. The Book Companion helps users learn, internalize, and apply PBM principles.

We contributed production-grade [multi-agent]({{ '/ai/programming/tutorials/how-to-train-your-ai-agent/' | relative_url }}) architecture, enterprise authentication, per-user memory, observability, and progressive-disclosure UX—designed for roughly 8,000 to 100,000 monthly users.

## The Challenge

The product needed to serve two audiences at scale: public book readers and Koch employees applying PBM at work. Requirements included enterprise security and compliance, authentication for public users and employees via SSO, audit logging and retention policies, and careful separation of principles vs. personal experience in AI responses—without losing the nuance PBM education demands.

## What We Built

We helped architect a multi-agent AI Book Companion with three specialized agents—Learn, Prepare, and Reflect—coordinated by an orchestration layer that routes interactions by intent and context. The system included:

- Per-user memory for personalized learning journeys
- Enterprise authentication (public and SSO)
- Observability and tracing for agents and infrastructure
- Feedback mechanisms for continuous improvement

Deployed on AWS, the platform was validated through user testing and advanced toward broader launch.

## Key Capabilities

- **Multi-agent architecture** — Learn, Prepare, and Reflect agents with a router/orchestrator
- **Per-user memory** — MEM0 with PGVector and AWS Bedrock for personalized context
- **Enterprise authentication** — AWS Cognito and Auth0, including SSO and guest-to-authenticated transitions
- **Observability** — Langfuse for agent traces and prompt monitoring; CloudWatch for infrastructure logs
- **Progressive disclosure UX** — React frontend guiding deeper engagement with PBM content

## Technical Approach

### Agent pipeline
- **Learn** — Guides users through PBM concepts with source-grounded responses
- **Prepare** — Helps plan application of principles to upcoming scenarios
- **Reflect** — Supports post-action reflection through a PBM lens
- **Router/orchestrator** — Directs conversations based on intent and context

### Stack
- **AWS Bedrock** — Claude models for the agents
- **MEM0 + PGVector** — Per-user memory storage and retrieval ([how we integrate Mem0]({{ '/ai/engineering/agents/rag/how-mem0-works-and-how-we-integrated-it/' | relative_url }}))
- **AWS Cognito / Auth0** — Public sign-up and enterprise SSO, with admin tooling for large MAU targets
- **Langfuse** — Production tracing of agent interactions and prompts
- **React** — Progressive disclosure frontend
- **AWS / Kubernetes** — Cluster deployments, VPC configuration, and cross-account auth

### Infrastructure goals
- Per-user cost modeling for capacity planning
- Load testing toward high monthly active user targets
- Multi-tier logging separating infrastructure logs from application traces

## Our Contributions

As a subcontractor providing hands-on technical leadership, we drove work across:

- **Infrastructure & DevOps** — Langfuse deployment, Kubernetes/VPC setup, cross-account auth, cost models
- **Evaluation & quality** — Golden Q&A datasets for principles-based answers; synthesis of tester feedback into priorities
- **Authentication & user management** — Auth0/Cognito flows, guest-to-authenticated transitions, admin portal needs at scale
- **Memory system** — MEM0 integration testing and architecture decisions vs. custom Postgres
- **Engineering leadership** — Stand-ups, blocker removal, onsite demos, mentoring through architectural choices
- **Security & compliance** — Privacy, retention, audit logging, and account deletion workflows

## Engagement Outcomes

- User testing validated the multi-agent architecture, memory system, and authentication flows for enterprise requirements
- Architecture designed and tested for tens of thousands of monthly users across public and employee paths
- Experienced technical leadership helped move the team from concept toward a production-grade platform

## Relationship to DocRouter

This engagement was **multi-agent education and enterprise agent infrastructure**, not DocRouter document processing. Lessons on memory, evaluation datasets, observability, and auth at scale inform how we build agent systems adjacent to DocRouter (including work covered in our [Mem0]({{ '/ai/engineering/agents/rag/how-mem0-works-and-how-we-integrated-it/' | relative_url }}) and [learning-agent architecture]({{ '/ai/programming/engineering/how-to-build-a-learning-agent-architecture-knowledge-base-and-production-lessons/' | relative_url }}) posts).

For more details, contact Andrei Radulescu-Banu at andrei@docrouter.ai.
