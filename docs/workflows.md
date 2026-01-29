---
layout: docs
title: "Workflows"
permalink: /docs/workflows/
---

<div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-4 md:p-8 mb-6 md:mb-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-2">Automate document processing workflows</h2>
  <p class="text-sm md:text-base text-blue-100">Connect DocRouter to your systems via webhooks and workflow platforms.</p>
</div>

## Overview

Workflows react to DocRouter events (e.g. document processed, extraction completed) and trigger actions in your systems. Configure <a href="/docs/webhooks">webhooks</a> in DocRouter, then connect your webhook endpoint to a workflow platform or your own code.

---

## N8N

**N8N** is a visual workflow tool. Use it to integrate DocRouter with third‑party services—for example: ingest email attachments into DocRouter, or send extracted results to a database, CRM, or ERP. Set up a Webhook node in N8N, add its URL in DocRouter webhook settings, and subscribe to events like <code class="bg-gray-100 px-1 rounded">llm.completed</code>. See <a href="/docs/webhooks">Webhooks</a> for setup.

---

## Temporal

**Temporal** is for coded workflows where you need durable orchestration—e.g. classify pages, group them by class, then process each group. Use it when documents must be split, classified, grouped, and processed by group (e.g. multi‑page surgery schedules). For a full walkthrough with DocRouter, see our blog post: <a href="/tech/programming/ai/tutorials/how-to-create-document-workflows-with-temporal-and-docrouter-ai/">How to create document workflows with Temporal and DocRouter.AI</a>.

---

## Other workflow tools

DocRouter exposes a full suite of <a href="/docs/rest-api">REST APIs</a>, including webhooks. You can integrate with any workflow tool that supports REST APIs—Zapier, Make, custom scripts, or your own backend. Configure webhooks to receive events, and use the REST API to upload documents, list results, and manage resources.

---

## Learn more

- <a href="/docs/webhooks">Webhooks</a> — Event types, payloads, and configuration
- <a href="/docs/integrations">Integrations</a> — Overview of integration options

---

<div class="bg-blue-600 rounded-lg p-4 md:p-8 mt-8 md:mt-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-4">Ready to automate your workflows?</h2>
  <a href="https://app.docrouter.ai" class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-4 py-3 md:px-8 md:py-4 rounded-lg font-semibold text-base md:text-lg transition-colors duration-200 no-underline">
    Open Dashboard
  </a>
</div>
