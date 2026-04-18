---
layout: docs
title: "Platform"
permalink: /docs/platform/
description: "Hosted DocRouter (SaaS) needs no cloud or LLM configuration from you. Self-hosted DocRouter can use optional cloud accounts and LLM keys; Textract and Bedrock need AWS, Vertex AI needs GCP, Microsoft Foundry needs Azure, and Mistral OCR needs Mistral."
---

<div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-4 md:p-8 mb-6 md:mb-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-2">Platform — clouds, LLMs, and OCR</h2>
  <p class="text-sm md:text-base text-blue-100"><strong>Hosted SaaS:</strong> you do not configure cloud accounts or LLM keys—DocRouter runs everything. <strong>Self-hosted:</strong> you may supply optional cloud accounts and optional LLM keys so your deployment can reach the vendors you choose.</p>
</div>

<p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 1rem 0;"><strong>Hosted SaaS</strong> (<a href="https://app.docrouter.ai" class="text-blue-600 hover:text-blue-800" target="_blank" rel="noopener noreferrer">app.docrouter.ai</a>): there is no tenant configuration for infrastructure, model API keys, or OCR backends. <strong>Self-hosted</strong> DocRouter: you operate the stack and can optionally connect cloud accounts (AWS, GCP, Azure) and optionally configure LLM provider keys or cloud identity—only what you need for the features you turn on.</p>

---

## Hosted vs self-hosted

<div class="grid md:grid-cols-2 gap-4 md:gap-6 my-4 md:my-6">
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Hosted DocRouter (SaaS)</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">You do <strong>not</strong> configure cloud platforms (AWS, GCP, Azure) or bring your own LLM API keys. DocRouter manages models, OCR, storage, and integrations end to end on its infrastructure.</p>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Self-hosted DocRouter</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">You may supply <strong>optional</strong> cloud accounts (for storage, Textract, Bedrock, Vertex, Azure/Foundry, IAM, and so on) and <strong>optional</strong> LLM keys or cloud auth—only for the providers and features you enable. Nothing is required unless a chosen code path needs it (see below).</p>
  </div>
</div>

---

## Supported clouds (self-hosted)

<p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 1rem 0;">The following applies when <strong>you</strong> run DocRouter and connect vendor clouds. It does not describe SaaS tenant setup (there is none).</p>

<p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 1rem 0;"><strong>Feature-to-cloud dependencies</strong> (when those features are in use on a self-hosted deployment):</p>

<ul style="color: #4b5563; font-size: 0.875rem; margin: 0 0 1rem 0; padding-left: 1.25rem;">
  <li style="margin-bottom: 0.35rem;"><strong>Amazon Textract</strong> OCR and <strong>AWS Bedrock</strong> LLMs require an <strong>AWS</strong> account (credentials, IAM, and typically S3 for the pipeline as configured).</li>
  <li style="margin-bottom: 0.35rem;"><strong>Google Vertex AI</strong> LLMs require <strong>GCP</strong> (Vertex / Google Cloud project and auth as wired in your environment).</li>
  <li style="margin-bottom: 0.35rem;"><strong>Microsoft Foundry</strong> LLMs (Azure AI / <code>azure_ai</code> in LiteLLM) require <strong>Azure</strong>.</li>
  <li style="margin-bottom: 0.35rem;"><strong>Mistral OCR</strong> requires <strong>Mistral</strong> (Mistral API access—API key or auth your deployment uses for Mistral).</li>
</ul>

<div class="grid md:grid-cols-2 gap-4 md:gap-6 my-4 md:my-6">
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Amazon Web Services (AWS)</h3>
    <ul style="color: #4b5563; font-size: 0.875rem; margin: 0; padding-left: 1.25rem;">
      <li style="margin-bottom: 0.5rem;"><strong>Textract</strong> — <a href="#supported-ocr-algorithms">OCR</a> via <code>AnalyzeDocument</code> when OCR mode is <code>textract</code>; requires AWS.</li>
      <li style="margin-bottom: 0.5rem;"><strong>Bedrock</strong> — LLMs and embeddings routed through LiteLLM; requires AWS.</li>
      <li><strong>Object storage</strong> — S3-compatible storage for documents and artifacts is typical for production on AWS.</li>
    </ul>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Google Cloud (GCP)</h3>
    <ul style="color: #4b5563; font-size: 0.875rem; margin: 0; padding-left: 1.25rem;">
      <li><strong>Vertex AI</strong> — Gemini and embeddings on Vertex require GCP. (Other LiteLLM routes—for example Gemini via Google AI Studio and an API key—follow whatever credentials you configure for that provider.)</li>
    </ul>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Microsoft Azure</h3>
    <ul style="color: #4b5563; font-size: 0.875rem; margin: 0; padding-left: 1.25rem;">
      <li><strong>Microsoft Foundry</strong> / Azure AI models — require Azure. <strong>Azure OpenAI</strong> deployments also use Azure.</li>
    </ul>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Kubernetes</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;">DocRouter ships with Helm-oriented deployment; MongoDB can be Atlas or in-cluster. Cloud choice above is about <strong>vendor APIs and data planes</strong>, not about “Kubernetes itself.”</p>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Example write-ups include <strong>Amazon EKS</strong> and <strong>DigitalOcean Kubernetes</strong>; <strong>AKS</strong> is noted as planned. See <a href="{% post_url 2026-03-07-deploying-doc-router-on-kubernetes %}" class="text-blue-600 hover:text-blue-800">Deploying Doc Router on Kubernetes</a>.</p>
  </div>
</div>

<p style="color: #4b5563; font-size: 0.875rem; margin: 0;">For how components fit together, see the <a href="{{ '/docs/architecture/' | relative_url }}" class="text-blue-600 hover:text-blue-800">architecture overview</a>.</p>

---

## Supported LLM providers

<p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.75rem 0;"><strong>SaaS:</strong> DocRouter operates the models; you do not supply LLM API keys or enable providers in your tenant. <strong>Self-hosted:</strong> DocRouter routes chat, extraction, embeddings, and optional <a href="#supported-ocr-algorithms">LLM-based OCR</a> through <strong>LiteLLM</strong>; you <strong>optionally</strong> configure provider keys or cloud-side auth for only the vendors you use. Some providers are API-key based; <strong>AWS Bedrock</strong>, <strong>Vertex AI</strong>, and <strong>Microsoft Foundry</strong> tie to the clouds listed above when those routes are enabled.</p>

<p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;">First-class provider entries in the open-source product include:</p>

<ul style="color: #4b5563; font-size: 0.875rem; margin: 0 0 1rem 0; padding-left: 1.25rem;">
  <li style="margin-bottom: 0.25rem;"><strong>Anthropic</strong> (Claude)</li>
  <li style="margin-bottom: 0.25rem;"><strong>OpenAI</strong> (chat and embedding models)</li>
  <li style="margin-bottom: 0.25rem;"><strong>Gemini</strong> (Google AI Studio)</li>
  <li style="margin-bottom: 0.25rem;"><strong>Google Vertex AI</strong> — requires <strong>GCP</strong> when used</li>
  <li style="margin-bottom: 0.25rem;"><strong>AWS Bedrock</strong> — requires <strong>AWS</strong> when used</li>
  <li style="margin-bottom: 0.25rem;"><strong>Azure OpenAI</strong></li>
  <li style="margin-bottom: 0.25rem;"><strong>Microsoft Foundry</strong> — requires <strong>Azure</strong> when used</li>
  <li style="margin-bottom: 0.25rem;"><strong>Mistral</strong></li>
  <li style="margin-bottom: 0.25rem;"><strong>Groq</strong></li>
  <li style="margin-bottom: 0.25rem;"><strong>OpenRouter</strong></li>
  <li><strong>xAI</strong></li>
</ul>

<p style="color: #4b5563; font-size: 0.875rem; margin: 0;">The exact default model lists change between releases. For the authoritative catalog, see <code>get_llm_providers()</code> in the <a href="https://github.com/analytiq-hub/doc-router/blob/main/packages/python/analytiq_data/llm/providers.py" class="text-blue-600 hover:text-blue-800" target="_blank" rel="noopener noreferrer">DocRouter source</a> (<code>packages/python/analytiq_data/llm/providers.py</code>).</p>

---

## Supported OCR algorithms

<p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 1rem 0;"><strong>Self-hosted</strong> installs choose <strong>one OCR mode</strong> per organization; the pipeline runs that engine on the document PDF and stores a normalized OCR payload for downstream extraction and search. <strong>SaaS:</strong> DocRouter runs OCR as part of the managed service—you do not select engines or supply vendor credentials.</p>

<div class="overflow-x-auto my-4 md:my-6">
  <table class="min-w-full text-left border border-gray-200" style="font-size: 0.875rem; color: #374151;">
    <thead style="background-color: #f9fafb; color: #111827;">
      <tr>
        <th class="px-3 py-2 border-b border-gray-200 font-semibold">Mode</th>
        <th class="px-3 py-2 border-b border-gray-200 font-semibold">What it does</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom: 1px solid #f3f4f6;">
        <td class="px-3 py-2 font-medium text-gray-900 whitespace-nowrap"><code>textract</code></td>
        <td class="px-3 py-2"><strong>Amazon Textract</strong> <code>AnalyzeDocument</code>. Self-hosted: configurable feature types (e.g. <code>LAYOUT</code>, <code>TABLES</code>, <code>FORMS</code>, <code>SIGNATURES</code>) and AWS credentials/IAM for Textract and S3 as used by your deployment. <strong>Requires AWS.</strong></td>
      </tr>
      <tr style="border-bottom: 1px solid #f3f4f6;">
        <td class="px-3 py-2 font-medium text-gray-900 whitespace-nowrap"><code>mistral</code></td>
        <td class="px-3 py-2"><strong>Mistral OCR</strong> via the Mistral API (model <code>mistral-ocr-latest</code> in product code). Returns Mistral OCR JSON (pages and layout-oriented content). <strong>Requires Mistral.</strong></td>
      </tr>
      <tr style="border-bottom: 1px solid #f3f4f6;">
        <td class="px-3 py-2 font-medium text-gray-900 whitespace-nowrap"><code>llm</code></td>
        <td class="px-3 py-2"><strong>Vision LLM OCR</strong> — uses a LiteLLM provider and model for per-page markdown (or equivalent). <strong>Self-hosted:</strong> you configure provider, model, and credentials. <strong>SaaS:</strong> not something you configure in your tenant—processing is fully managed.</td>
      </tr>
      <tr>
        <td class="px-3 py-2 font-medium text-gray-900 whitespace-nowrap"><code>pymupdf</code></td>
        <td class="px-3 py-2"><strong>PyMuPDF</strong> — embedded text from the PDF only (no cloud OCR). No vendor cloud required.</td>
      </tr>
    </tbody>
  </table>
</div>

<p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Implementation details live under <code>analytiq_data.ocr</code> in the DocRouter repository (<code>ocr_config.py</code>, <code>ocr_runners.py</code>).</p>
