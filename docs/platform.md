---
layout: docs
title: "Platform"
permalink: /docs/platform/
description: "Hosted DocRouter (SaaS) needs no cloud or LLM configuration from you. Self-hosted DocRouter can use optional cloud accounts and LLM keys; Textract and Bedrock need AWS, Vertex AI needs GCP, Microsoft Foundry needs Azure, and Mistral OCR needs Mistral."
---

<div class="not-prose bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-4 md:p-8 mb-6 md:mb-10 text-center">
  <h2 class="text-xl md:text-2xl font-semibold text-white mb-2">Platform — clouds, LLMs, and OCR</h2>
  <p class="text-sm md:text-base text-blue-100 mb-2"><strong>Hosted SaaS:</strong> Cloud accounts and LLM keys are provided for you.</p>
  <p class="text-sm md:text-base text-blue-100 mb-0"><strong>Self-hosted:</strong> You supply cloud accounts and LLM keys.</p>
</div>

## Supported clouds

<p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 1rem 0;">Each cloud is configured under <b>Settings → Account → Development</b>. Configure only the clouds whose services you use.</p>

<div class="not-prose grid md:grid-cols-3 gap-4 md:gap-6 my-4 md:my-6">
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">AWS</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;"><b>Services:</b> S3 (document storage), Textract (OCR), Bedrock (LLMs and embeddings).</p>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;"><b>Configuration:</b> IAM user access key ID, secret access key, and S3 bucket name.</p>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">GCP</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;"><b>Services:</b> Vertex AI (Gemini and embeddings).</p>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;"><b>Configuration:</b> Google Cloud service account JSON key.</p>
  </div>
  <div class="bg-white border border-gray-200 rounded-lg p-5">
    <h3 style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin: 0 0 0.75rem 0;">Azure</h3>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 0.5rem 0;"><b>Services:</b> Azure OpenAI and Microsoft Foundry (Azure AI) LLMs.</p>
    <p style="color: #4b5563; font-size: 0.875rem; margin: 0;"><b>Configuration:</b> Microsoft Entra service principal (tenant ID, client ID, client secret) and the Foundry service API base URL.</p>
  </div>
</div>

---

## Deployment

<p style="color: #4b5563; font-size: 0.875rem; margin: 0;">Self-hosted DocRouter installs via a <b>Kubernetes Helm chart</b> or <b>Docker Compose</b>. See <a href="{% post_url 2026-03-07-deploying-doc-router-on-kubernetes %}" class="text-blue-600 hover:text-blue-800">Deploying Doc Router on Kubernetes</a> and the <a href="{{ '/docs/open-source/' | relative_url }}" class="text-blue-600 hover:text-blue-800">open source</a> page.</p>

---

## Supported LLM providers

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

<p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 1rem 0;"><strong>Organization admins</strong> choose <strong>one OCR mode</strong> per organization; the pipeline runs that engine on the document PDF and stores a normalized OCR payload for downstream extraction and search. </p>

<p style="color: #4b5563; font-size: 0.875rem; margin: 0 0 1rem 0;">All the OCR models are enabled in the SAAS version of DocRouter, at <a href="https://app.docrouter.ai>" class="text-blue-600 hover:text-blue-800" target="_blank" rel="noopener noreferrer">https://app.docrouter.ai/</a>. When installed on-prem, here are the requirements to enabled each OCR model:</p>

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
        <td class="px-3 py-2"><strong>Amazon Textract</strong> <code>AnalyzeDocument</code>. Configurable feature types (e.g. <code>LAYOUT</code>, <code>TABLES</code>, <code>FORMS</code>, <code>SIGNATURES</code>). <strong>Requires AWS.</strong></td>
      </tr>
      <tr style="border-bottom: 1px solid #f3f4f6;">
        <td class="px-3 py-2 font-medium text-gray-900 whitespace-nowrap"><code>mistral</code></td>
        <td class="px-3 py-2"><strong>Mistral OCR</strong> via the Mistral API (model <code>mistral-ocr-latest</code> in product code). Returns Mistral OCR JSON. <strong>Requires Mistral provider.</strong></td>
      </tr>
      <tr style="border-bottom: 1px solid #f3f4f6;">
        <td class="px-3 py-2 font-medium text-gray-900 whitespace-nowrap"><code>mistral-vertex</code></td>
        <td class="px-3 py-2"><strong>Mistral OCR</strong> via GCP (model <code>mistral-ocr-2505</code> in product code). Returns Mistral OCR JSON. <strong>Requires GCP.</strong></td>
      </tr>
      <tr style="border-bottom: 1px solid #f3f4f6;">
        <td class="px-3 py-2 font-medium text-gray-900 whitespace-nowrap"><code>llm</code></td>
        <td class="px-3 py-2"><strong>Vision LLM OCR</strong> — uses a LiteLLM provider and model for per-page markdown. Gemini models are best performing for LLM OCR.</td>
      </tr>
      <tr>
        <td class="px-3 py-2 font-medium text-gray-900 whitespace-nowrap"><code>pymupdf</code></td>
        <td class="px-3 py-2"><strong>PyMuPDF</strong> — embedded text from the PDF only (no cloud OCR). No vendor cloud required.</td>
      </tr>
    </tbody>
  </table>
</div>
