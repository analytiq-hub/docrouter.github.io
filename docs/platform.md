---
layout: docs
title: "Platform"
permalink: /docs/platform/
description: "What clouds, LLM providers, and OCR engines DocRouter integrates with. Use this page as a high-level compatibility guide; defaults and model catalogs evolve with each release."
---

<div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-4 md:p-8 mb-6 md:mb-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-2">Platform — clouds, LLMs, and OCR</h2>
  <p class="text-sm md:text-base text-blue-100">What DocRouter can connect to: infrastructure, model vendors, and OCR engines. Details vary by deployment (hosted vs self-hosted).</p>
</div>

<p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 1rem 0;">DocRouter runs as a hosted SaaS product or on your own infrastructure. You connect the clouds and AI vendors your organization uses—credentials and enabled models are configured per account.</p>

---

## Supported clouds

<p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 1rem 0;"><strong>Supported</strong> here means DocRouter has first-class integration paths for that vendor’s services (storage, OCR, or LLM routing), not that every feature runs on every cloud in every deployment.</p>

<div class="grid md:grid-cols-2 gap-4 md:gap-6 my-4 md:my-6">
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Amazon Web Services (AWS)</h3>
    <ul style="color: #4b5563; font-size: 0.875rem; margin: 0; padding-left: 1.25rem;">
      <li style="margin-bottom: 0.5rem;"><strong>Object storage</strong> — S3-compatible storage for documents and pipeline artifacts (typical production setup).</li>
      <li style="margin-bottom: 0.5rem;"><strong>OCR</strong> — <a href="#supported-ocr-algorithms">Amazon Textract</a> (<code>AnalyzeDocument</code>) when the organization OCR mode is set to Textract.</li>
      <li><strong>LLMs</strong> — Optional <strong>AWS Bedrock</strong> models (e.g. Anthropic Claude, embeddings) via LiteLLM when Bedrock is enabled and IAM allows access.</li>
    </ul>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Google Cloud</h3>
    <ul style="color: #4b5563; font-size: 0.875rem; margin: 0; padding-left: 1.25rem;">
      <li><strong>LLMs</strong> — <strong>Google AI Studio / Gemini</strong> API keys, or <strong>Vertex AI</strong> for Gemini and embeddings, routed through LiteLLM.</li>
    </ul>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Microsoft Azure</h3>
    <ul style="color: #4b5563; font-size: 0.875rem; margin: 0; padding-left: 1.25rem;">
      <li><strong>LLMs</strong> — <strong>Azure OpenAI</strong> deployments and <strong>Microsoft Foundry</strong> (Azure AI) models supported by LiteLLM.</li>
    </ul>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Self-hosted Kubernetes</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;">DocRouter ships with Helm-oriented deployment; MongoDB can be Atlas or in-cluster, and S3 remains a common external dependency for object storage.</p>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Kubernetes targets described in depth on the blog include <strong>Amazon EKS</strong> and <strong>DigitalOcean Kubernetes</strong>; <strong>Azure Kubernetes Service (AKS)</strong> is noted as planned. See <a href="{% post_url 2026-03-07-deploying-doc-router-on-kubernetes %}" class="text-blue-600 hover:text-blue-800">Deploying Doc Router on Kubernetes</a>.</p>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5 md:col-span-2">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Hosted DocRouter (SaaS)</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;">The managed application at <a href="https://app.docrouter.ai" class="text-blue-600 hover:text-blue-800" target="_blank" rel="noopener noreferrer">app.docrouter.ai</a> runs on DocRouter’s infrastructure; you still bring your own API keys or cloud credentials where the product exposes provider settings.</p>
  </div>
</div>

<p style="color: #4b5563; font-size: 0.875rem; margin: 0;">For how components fit together, see the <a href="{{ '/docs/architecture/' | relative_url }}" class="text-blue-600 hover:text-blue-800">architecture overview</a>.</p>

---

## Supported LLM providers

<p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.75rem 0;">DocRouter routes chat, extraction, embeddings, and optional <a href="#supported-ocr-algorithms">LLM-based OCR</a> through <strong>LiteLLM</strong>. Each organization stores provider configuration (which providers are on, which models are enabled, and tokens or cloud auth as applicable). Some providers use API keys; others (e.g. Bedrock, Vertex AI, Microsoft Foundry) rely on environment or cloud identity instead of a single pasted secret.</p>

<p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;">First-class provider entries in the open-source product include:</p>

<ul style="color: #4b5563; font-size: 0.875rem; margin: 0 0 1rem 0; padding-left: 1.25rem;">
  <li style="margin-bottom: 0.25rem;"><strong>Anthropic</strong> (Claude)</li>
  <li style="margin-bottom: 0.25rem;"><strong>OpenAI</strong> (chat and embedding models)</li>
  <li style="margin-bottom: 0.25rem;"><strong>Gemini</strong> (Google AI Studio)</li>
  <li style="margin-bottom: 0.25rem;"><strong>Google Vertex AI</strong> (Gemini and embeddings on GCP)</li>
  <li style="margin-bottom: 0.25rem;"><strong>AWS Bedrock</strong></li>
  <li style="margin-bottom: 0.25rem;"><strong>Azure OpenAI</strong></li>
  <li style="margin-bottom: 0.25rem;"><strong>Microsoft Foundry</strong> (Azure AI / <code>azure_ai</code> models in LiteLLM)</li>
  <li style="margin-bottom: 0.25rem;"><strong>Mistral</strong></li>
  <li style="margin-bottom: 0.25rem;"><strong>Groq</strong></li>
  <li style="margin-bottom: 0.25rem;"><strong>OpenRouter</strong></li>
  <li><strong>xAI</strong></li>
</ul>

<p style="color: #4b5563; font-size: 0.875rem; margin: 0;">The exact default model lists change between releases. For the authoritative catalog, see <code>get_llm_providers()</code> in the <a href="https://github.com/analytiq-hub/doc-router/blob/main/packages/python/analytiq_data/llm/providers.py" class="text-blue-600 hover:text-blue-800" target="_blank" rel="noopener noreferrer">DocRouter source</a> (<code>packages/python/analytiq_data/llm/providers.py</code>).</p>

---

## Supported OCR algorithms

<p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 1rem 0;">Each organization selects <strong>one OCR mode</strong> at a time. The pipeline runs that engine over the document PDF and stores a normalized OCR payload for downstream LLM extraction and search.</p>

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
        <td class="px-3 py-2"><strong>Amazon Textract</strong> <code>AnalyzeDocument</code>. Feature types are configurable per org (e.g. <code>LAYOUT</code>, <code>TABLES</code>, <code>FORMS</code>, <code>SIGNATURES</code>). Requires AWS credentials and suitable IAM for Textract and S3 staging as used by your deployment.</td>
      </tr>
      <tr style="border-bottom: 1px solid #f3f4f6;">
        <td class="px-3 py-2 font-medium text-gray-900 whitespace-nowrap"><code>mistral</code></td>
        <td class="px-3 py-2"><strong>Mistral OCR</strong> via the Mistral API (model <code>mistral-ocr-latest</code> in product code). Returns Mistral OCR JSON (pages and layout-oriented content).</td>
      </tr>
      <tr style="border-bottom: 1px solid #f3f4f6;">
        <td class="px-3 py-2 font-medium text-gray-900 whitespace-nowrap"><code>llm</code></td>
        <td class="px-3 py-2"><strong>Vision LLM OCR</strong> — uses a configured LiteLLM provider and model to produce per-page markdown (or equivalent structured text). Useful when you want OCR output aligned with a specific vendor’s multimodal model.</td>
      </tr>
      <tr>
        <td class="px-3 py-2 font-medium text-gray-900 whitespace-nowrap"><code>pymupdf</code></td>
        <td class="px-3 py-2"><strong>PyMuPDF</strong> text extraction — reads embedded text from the PDF (no cloud OCR). Best for digital PDFs with real text layers; does not perform full-page raster OCR.</td>
      </tr>
    </tbody>
  </table>
</div>

<p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Implementation details live under <code>analytiq_data.ocr</code> in the DocRouter repository (<code>ocr_config.py</code>, <code>ocr_runners.py</code>).</p>
