---
layout: post
title: "How AI Agent Memory Works (and How We Integrated Mem0)"
date: 2026-05-06 00:00:00 +0000
author: "Andrei Radulescu-Banu"
categories: [ai, engineering, agents, rag]
description: "A practical walkthrough of mem0 in production: async memory ingestion, reconciliation (dedupe + deletes), retrieval with Titan embeddings, and storage in Postgres/pgvector."
image: /assets/images/mem0-integration-splash.png
---

When you build an agent that chats with users over days or weeks, you quickly hit a ceiling: **context windows** are finite, and “just include the whole conversation” doesn’t scale. You need **durable memory** that’s:

- **Incrementally updated** as the conversation evolves
- **Deduplicated and reconciled** (so it doesn’t accumulate contradictions)
- **Fast to retrieve** at the start of each turn
- **Cheap enough** to run on every message

In a Learning Agent developed recently, we integrated [mem0](https://github.com/mem0ai/mem0) to do exactly that: extract durable facts from conversations and store them in a **PostgreSQL vector database** (pgvector), then retrieve the most relevant memories and inject them back into the agent prompt.

This post explains how the integration works end-to-end, using the architecture diagram below as the blueprint.

<div data-excalidraw="/assets/excalidraw/mem0-agent-system-diagram.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>

<p style="text-align: center; margin-top: 0.5rem; font-size: 0.875rem; color: #6b7280;">
  <strong>Figure 1:</strong> Agent + memory flow (mem0 integration).
</p>

<div style="text-align: center; margin-top: 1rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/mem0-agent-system-diagram.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    Edit in Excalidraw
  </a>
</div>

---

## Mental model: two parallel paths

mem0 integration is easiest to understand as **two paths that run in parallel** on each user message:

- **Memory ingestion (async, off the critical path)**: store or update long-term facts.
- **Memory retrieval (sync, on the critical path)**: fetch relevant facts to condition the next agent response.

That split is deliberate: users should get a response quickly, and memory updates should be resilient to retries, throttling, and occasional failures without blocking the chat experience.

---

## 1) Memory ingestion path (async “Memory Save”)

When the user sends a message, we enqueue a background task to update memory rather than doing it inline.

In the API, we schedule `add_memory(...)` in the request’s background tasks (both non-streaming and streaming endpoints). That means memory writes happen **after** the response is returned (or after streaming finalization), keeping the **time-to-first-token** fast even under load.

### What mem0 stores

mem0’s job is to convert raw conversation into **small, high-signal “facts”** such as:

- Stable user profile info (role, work context, preferences)
- A single current goal (with updates overwriting older ones)
- Progress on “principles” (mentioned → explored → applied)
- Session summaries and open loops that span sessions

In our integration, we provide mem0 with a **custom fact extraction prompt** tuned for coaching conversations. It returns JSON like:

```json
{"facts":["Role: Plant Manager","Work context: Texas refinery, 40 direct reports"]}
```

### The LLM used for ingestion and reconciliation

mem0 uses an LLM twice during ingestion:

1. **Fact extraction**: identify candidate facts from the new turn.
2. **Reconciliation / update**: decide how those facts modify existing memory (**ADD / UPDATE / DELETE / NONE**).

We run these steps on a low-latency, cost-efficient model: **Claude Haiku** (via **AWS Bedrock**) for both ingestion and reconciliation. GPT Mini or Gemini Flash models would work just as well.

### Reconciliation: dedupe + deletes (the important part)

The reconciliation step is what turns “memory” from a junk drawer into something you can trust. For each new fact, mem0 compares it to what’s already stored and produces an “edit plan”:

- **ADD** when it’s truly new information
- **UPDATE** when it refines or replaces an older memory (e.g., goal changes)
- **DELETE** when it’s obsolete or contradicted
- **NONE** when it’s redundant

This is how we avoid:

- Duplicates (“Role: Manager” repeated 50 times)
- Contradictions (old goal and new goal both present)
- Stale open loops lingering forever

Operationally, we also rate-limit ingestion: we cap concurrent writers per pod and retry on AWS throttling with exponential backoff.

---

## 2) Memory retrieval path (sync “Memory Retrieve”)

At the start of each agent turn, we retrieve durable memory and attach it to the agent context.

This happens while we’re building the agent LLM prompt. Memory retrieval runs concurrently with other non-dependent work (like syncing any conversation context directory from object storage), but it’s still on the critical path for prompt construction.

### Retrieval uses embeddings (not keyword search)

To fetch “what matters now,” we embed the user’s current situation and run a nearest-neighbor search over stored memories.

For retrieval embeddings we use **Amazon Titan Embed Text v2** (via **AWS Bedrock**), which produces **1024-dimensional vectors**. Those vectors are stored and searched in Postgres using **pgvector**.

---

## 3) Where memory lives: Postgres + pgvector (vector DB)

We store memory in a Postgres database that has the `vector` extension enabled (pgvector). In production, this is **AWS Aurora Postgres**, and we connect through **RDS Proxy** for connection multiplexing.

mem0 uses the `pgvector` provider, and we map agents to a single shared mem0 “collection”:

- Orchestrator + Learn + Prepare + Reflect all write to the same collection (e.g. `shared_learning_memories`)

At a high level, each memory row contains:

- **The memory text**
- **The user id** it belongs to
- **Metadata** (conversation id, message id, agent id, etc.)
- **An embedding vector** (Titan v2, 1024 dims)

mem0 also maintains an internal migrations table (e.g. `mem0migrations`) so it can evolve its schema safely over time.

---

## 4) How memory changes the agent prompt

Once retrieved, memories are injected into the request metadata and/or prompt context so the agent can respond as if it “remembers”:

- Who the user is and what context they’re operating in
- What they were working on last time
- The current open loop (what to follow up on)

The key design point is that we **don’t** try to jam all past dialogue into context. Instead we provide:

- The agent’s system prompt
- Tool definitions
- The recent conversation window (last \(N\) messages)
- A compact, semantically-retrieved memory summary.

That makes the system more stable across long sessions while keeping costs and latency bounded. The memory summary is included last, so we can use LLM caching for the previous parts of the prompt.

---

## Summary

mem0 gives you a clean separation of concerns:

- **Ingestion** (Claude Haiku): extract candidate facts and reconcile them into durable memory.
- **Storage** (Postgres + pgvector): persist memories as vectors + metadata, organized into collections.
- **Retrieval** (Titan embeddings): pull the most relevant facts at the start of each turn and inject them into the agent prompt.

The result is an agent that feels consistent over time without relying on ever-growing context windows—and without turning “memory” into an unbounded pile of stale notes.

<style>
.excalidraw-container {
  width: 100%;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  background: white;
  display: block;
  margin: 2rem 0;
  min-height: 400px;
}
.excalidraw-container svg {
  width: 100%;
  height: auto;
  display: block;
  margin: 0;
}
.loading-placeholder {
  padding: 2rem;
  text-align: center;
  color: #666;
}
</style>
<script type="module" src="/assets/js/excalidraw/render-excalidraw.js"></script>

