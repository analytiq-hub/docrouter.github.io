---
marp: true
theme: docrouter
paginate: true
title: DocRouter.AI — Technical Deep Dive
description: Architecture, workflow, and integration details
---

<!-- _class: lead -->

# DocRouter.AI

## Technical Deep Dive

Architecture, workflow, and integration details.

<div class="cta center mt-5">
  <a class="btn btn-primary" href="https://docrouter.ai/docs">Docs</a>
  <a class="btn btn-secondary" href="https://app.docrouter.ai">Console</a>
</div>

---

# A pipeline built for documents

<div class="columns">
  <div>
    <h3>Core stages</h3>
    <ul>
      <li>Ingest and normalize</li>
      <li>Route by tag</li>
      <li>Extract with prompts</li>
      <li>Validate with schemas</li>
    </ul>
  </div>
  <div>
    <blockquote>
      Tags are the routing layer that connect uploads to prompts.
    </blockquote>
  </div>
</div>

---

# Ingestion is flexible

<div class="cards">
  <div class="card">
    <h3>Email and web</h3>
    <p>Quick onboarding and manual uploads</p>
  </div>
  <div class="card">
    <h3>REST API</h3>
    <p>Programmatic upload and control</p>
  </div>
  <div class="card">
    <h3>SDKs</h3>
    <p>Python and TypeScript clients</p>
  </div>
</div>

---

# Routing starts with tags

<div class="columns">
  <div>
    <h3>Why tags matter</h3>
    <ul>
      <li>Explicit document intent</li>
      <li>Predictable prompt mapping</li>
      <li>Immediate extraction results</li>
      <li>Simple onboarding flow</li>
    </ul>
  </div>
  <div>
    <h3>Onboarding flow</h3>
    <ol>
      <li>Create tag and prompt</li>
      <li>Upload with tag</li>
      <li>See extraction results</li>
    </ol>
  </div>
</div>

---

# Prompts define extraction logic

<div class="cards two">
  <div class="card">
    <h3>Instruction-driven</h3>
    <p>Natural language extraction rules</p>
  </div>
  <div class="card">
    <h3>Repeatable outputs</h3>
    <p>Consistent results across documents</p>
  </div>
</div>

<p class="text-muted text-small mt-4">Prompts are linked to tags for routing.</p>

---

# Schemas enforce structure

<div class="columns">
  <div>
    <h3>Why schemas</h3>
    <ul>
      <li>Typed output fields</li>
      <li>Stable downstream mapping</li>
      <li>Validation and consistency</li>
      <li>Faster integration</li>
    </ul>
  </div>
  <div>
    <div class="card">
      <h3>Output example</h3>
      <p>JSON shaped to your data model</p>
    </div>
  </div>
</div>

---

# Human review is optional

<div class="cards two">
  <div class="card">
    <h3>Auto-first</h3>
    <p>Default to fully automated flow</p>
  </div>
  <div class="card">
    <h3>Human-in-the-loop</h3>
    <p>Review when confidence is low</p>
  </div>
</div>

---

# Results delivered your way

<div class="cards">
  <div class="card">
    <h3>Webhooks</h3>
    <p>Event-driven completion</p>
  </div>
  <div class="card">
    <h3>REST API</h3>
    <p>Pull results on demand</p>
  </div>
  <div class="card">
    <h3>Integrations</h3>
    <p>n8n and Temporal workflows</p>
  </div>
</div>

---

# AI assistant integrations

<div class="cards two">
  <div class="card">
    <h3>MCP server</h3>
    <p>Connect Claude Code and Cursor</p>
  </div>
  <div class="card">
    <h3>Agent workflows</h3>
    <p>Automate extraction in pipelines</p>
  </div>
</div>

---

# Use cases fit real systems

<div class="cards">
  <div class="card">
    <h3>Banking</h3>
    <p>Loan docs and statements</p>
  </div>
  <div class="card">
    <h3>Insurance</h3>
    <p>Applications and claims</p>
  </div>
  <div class="card">
    <h3>Supply chain</h3>
    <p>Bills of lading</p>
  </div>
</div>

---

# Start building in minutes

<div class="columns">
  <div>
    <ul>
      <li>Create tag and prompt</li>
      <li>Upload a sample document</li>
      <li>Validate schema output</li>
      <li>Integrate via API</li>
    </ul>
    <div class="cta">
      <a class="btn btn-primary" href="https://docrouter.ai/docs/quick-start/">Quick Start</a>
      <a class="btn btn-secondary" href="https://docrouter.ai/docs/rest-api/">REST API</a>
    </div>
  </div>
  <div>
    <blockquote>
      Document to data in three steps.
    </blockquote>
  </div>
</div>

---

<!-- _class: closing -->

# Questions?

Docs: <a href="https://docrouter.ai/docs">docrouter.ai/docs</a>
