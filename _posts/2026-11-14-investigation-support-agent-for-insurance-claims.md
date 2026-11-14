---
layout: post
title: "From First Notice to First Answers: Architecting an Investigation Support Agent"
date: 2026-11-14 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: /assets/images/investigation-support-agent-splash.jpg
categories: [ai, engineering, insurance]
description: "Architecture and implementation patterns for a governed Investigation Support agent—first coverage answers, cited policy evidence, and adjuster-ready packages after FNOL."
---

When a policyholder reports a loss—by phone, web, mobile app, email, or voice—the clock starts. First notice of loss (FNOL) captures what the customer knows at that moment. What an adjuster needs next is different: *Is the loss likely covered? Which policy forms matter? What evidence is still missing?* Historically that first pass of investigation was assembled by hand, claim by claim.

We architected an **Investigation Support agent** so that legwork happens automatically after FNOL. Adjusters start from an organized, cited evidence package instead of a blank screen.

While the agent was deployed at a mid-size property-and-casualty carrier, this post stays at the product-pattern level and describes implementation best practices.

## The gap after FNOL

FNOL is built for speed and empathy on the intake side. Investigation is built for accuracy, traceability, and consistency. The handoff between them is where teams lose time:

- Claim data may be complete enough to open a file but not enough to decide coverage.
- Policy language lives across dec pages, forms, and endorsements—not in a single paragraph an LLM can guess from memory.
- Classic red flags—loss location vs. policy territory, brand-new policies, mismatched facts—need **deterministic** checks, not probabilistic guesses.

The agent’s job is not to replace the adjuster. It produces a **first investigation pass** that is structured, cited, and ready for adjuster review—and refreshes that package as more information arrives. The adjuster always has the last word.

## Where it sits in the flow

Intake can arrive on any channel; the investigation logic should not fork per channel. The pattern we used:

1. **Claim intake** normalizes the FNOL into a claim summary the rest of the stack understands.
2. **Investigation Support** runs against that summary (and can re-run when new evidence arrives, even before the claim is fully committed to the system of record).
3. **Output** feeds triage, assignment, and the adjuster’s workspace as an “investigation support” bundle alongside other AI-assisted views (summary, coverage walkthrough, and similar).

That separation—intake vs. investigation vs. presentation—is what keeps the agent maintainable as channels multiply.

## What the agent produces

For each claim, the agent works through a fixed sequence:

1. **Validate and gather** claim and policy context (including the documents that actually govern coverage).
2. **Investigation checks** apply rule-based signals adjusters already care about (geography, policy age, inconsistencies, and similar).
3. A **coverage router** decides which coverages might apply and fans out work in parallel—one review path per coverage, not one monolithic prompt.
4. For each coverage, the agent **searches governed policy text** (forms and endorsements), drafts a finding, and **critiques** its own draft before finalizing.
5. The run ends in an **adjuster-ready package**: recommended actions, plain-language questions for the insured where data is missing, and an audit-friendly trail of what was read and concluded.

Denials and material adverse decisions remain **human decisions**. The agent may recommend; it does not auto-close claims.

## Architecture patterns that mattered

### Governed policy knowledge, not model memory

Coverage language is retrieved from a **curated policy knowledge base** (search over forms and endorsements the carrier actually issues). Every substantive statement in the output is tied back to **cited passages**, not to what the model “remembers” from training.

### Rules where you need defensibility, models where you need judgment

We followed this pattern:

- **Deterministic checks** for investigative signals that must be explainable in a dispute or audit.
- **LLM steps** for reading long policy text, comparing scenarios, and drafting narrative findings—always followed by a critique pass before the result is stored.

That split is how you move fast in insurance without betting the company on a single chat completion.

### One investigation service, multiple surfaces

The same Investigation Support capability is exposed to the adjuster portal and to other assistant experiences, with **role-based access** (for example, investigation bundles limited to authorized adjusters). Feedback—thumbs, reasons—feeds the improvement loop described below.

## Trust, security, and operations

Carrier claims environments impose constraints that shaped the design from day one:

- **PII-aware** handling and enterprise identity for who can run or view investigation output.
- **Tracing and retention** suitable for operational audit.
- **A deliberate, code-first agent loop** on the critical path: explicit services, prompts versioned with deploys, and line-of-business configuration without rewriting core logic.

## How we built confidence before scale

### Development harness

Before automating the full loop, we stood up a small **engineering harness**: each data source the agent needs (claim details, policy data, documents, policy-language search, model access) exposed through a UI so engineers and product partners could replay real claims manually. The production agent reuses those same integration boundaries.

### Offline evaluation

We curated **real claims with expert-agreed outcomes** and replay them through the agent after each meaningful change. Scoring mixes deterministic checks with an LLM-as-judge where human labels exist. A release candidate must consistently improve accuracy tracked through evaluation scores.

### Online evaluation

In production, adjusters rate outputs and leave reasons. Traces bucket into recurring failure patterns; the highest-impact gaps become new offline cases. That closed loop is how investigation quality improves without silent drift.

## Lessons for other regulated document + decision workflows

If you are building something similar—not only in insurance—three ideas travel well:

1. **Treat “first answers after intake” as a product**, not a one-off prompt. Users need packages, citations, and next steps—not just chat.
2. **Understand early what information is available** through existing APIs (claim details, policy forms, SOPs, contracts). Make that information available to the AI agent through tools or prompt context.
3. **Pair offline evaluation with production feedback.**

DocRouter’s document intelligence stack—ingestion, OCR, schema-driven extraction, and human-in-the-loop review—is aimed at the same class of problems. Investigation Support is the claims-native expression: **documents plus policy language plus adjuster workflow**, with AI doing the first pass and people maintaining decision control.

*Building in claims? Start with lesson #2: inventory your APIs before you prompt-engineer. Want a second pair of eyes on architecture or eval design? [Let's talk](/contact).* 