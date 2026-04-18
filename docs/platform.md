---
layout: docs
title: "Platform — Clouds, LLMs, and OCR"
permalink: /docs/platform/
description: "What clouds, LLM providers, and OCR engines DocRouter integrates with. Use this page as a high-level compatibility guide; defaults and model catalogs evolve with each release."
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <header class="text-center md:mb-12 mb-8">
        <h1 class="text-4xl font-bold text-gray-900 mb-4">Platform overview</h1>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            DocRouter runs as a hosted product or on your own infrastructure. You connect the clouds and AI vendors your organization uses—credentials and enabled models are configured per account.
        </p>
    </header>

    <main>
        <section id="clouds" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Supported clouds</h2>
            <p class="text-gray-600 mb-6">
                “Supported” here means DocRouter has first-class integration paths for that vendor’s services (storage, OCR, or LLM routing), not that every feature runs on every cloud in every deployment.
            </p>
            <div class="space-y-6 text-gray-600">
                <div>
                    <h3 class="text-lg font-medium text-gray-900 mb-2">Amazon Web Services (AWS)</h3>
                    <ul class="list-disc pl-5 space-y-1">
                        <li><strong>Object storage</strong> — S3-compatible storage for documents and pipeline artifacts (typical production setup).</li>
                        <li><strong>OCR</strong> — <a href="#ocr" class="text-blue-600 hover:text-blue-800">Amazon Textract</a> (<code>AnalyzeDocument</code>) when the organization OCR mode is set to Textract.</li>
                        <li><strong>LLMs</strong> — Optional <strong>AWS Bedrock</strong> models (e.g. Anthropic Claude, embeddings) via LiteLLM when Bedrock is enabled and IAM allows access.</li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-lg font-medium text-gray-900 mb-2">Google Cloud</h3>
                    <ul class="list-disc pl-5 space-y-1">
                        <li><strong>LLMs</strong> — <strong>Google AI Studio / Gemini</strong> API keys, or <strong>Vertex AI</strong> for Gemini and embeddings, routed through LiteLLM.</li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-lg font-medium text-gray-900 mb-2">Microsoft Azure</h3>
                    <ul class="list-disc pl-5 space-y-1">
                        <li><strong>LLMs</strong> — <strong>Azure OpenAI</strong> deployments and <strong>Microsoft Foundry</strong> (Azure AI) models supported by LiteLLM.</li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-lg font-medium text-gray-900 mb-2">Self-hosted Kubernetes</h3>
                    <p class="mb-2">DocRouter ships with Helm-oriented deployment; MongoDB can be Atlas or in-cluster, and S3 remains a common external dependency for object storage.</p>
                    <p class="mb-0">Kubernetes targets described in depth on the blog include <strong>Amazon EKS</strong> and <strong>DigitalOcean Kubernetes</strong>; <strong>Azure Kubernetes Service (AKS)</strong> is noted as planned. See <a href="{% post_url 2026-03-07-deploying-doc-router-on-kubernetes %}" class="text-blue-600 hover:text-blue-800">Deploying Doc Router on Kubernetes</a>.</p>
                </div>
                <div>
                    <h3 class="text-lg font-medium text-gray-900 mb-2">Hosted DocRouter (SaaS)</h3>
                    <p class="mb-0">The managed application at <a href="https://app.docrouter.ai" class="text-blue-600 hover:text-blue-800" target="_blank" rel="noopener noreferrer">app.docrouter.ai</a> runs on DocRouter’s infrastructure; you still bring your own API keys or cloud credentials where the product exposes provider settings.</p>
                </div>
            </div>
            <p class="text-gray-600 mt-6 mb-0">
                For how components fit together, see the <a href="{{ '/docs/architecture/' | relative_url }}" class="text-blue-600 hover:text-blue-800">architecture overview</a>.
            </p>
        </section>

        <section id="llm" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Supported LLM providers</h2>
            <p class="text-gray-600 mb-6">
                DocRouter routes chat, extraction, embeddings, and optional <a href="#ocr">LLM-based OCR</a> through <strong>LiteLLM</strong>. Each organization stores provider configuration (which providers are on, which models are enabled, and tokens or cloud auth as applicable). Some providers use API keys; others (e.g. Bedrock, Vertex AI, Microsoft Foundry) rely on environment or cloud identity instead of a single pasted secret.
            </p>
            <p class="text-gray-600 mb-4">First-class provider entries in the open-source product include:</p>
            <ul class="text-gray-600 list-disc pl-5 space-y-2 mb-6">
                <li><strong>Anthropic</strong> (Claude)</li>
                <li><strong>OpenAI</strong> (chat and embedding models)</li>
                <li><strong>Gemini</strong> (Google AI Studio)</li>
                <li><strong>Google Vertex AI</strong> (Gemini and embeddings on GCP)</li>
                <li><strong>AWS Bedrock</strong></li>
                <li><strong>Azure OpenAI</strong></li>
                <li><strong>Microsoft Foundry</strong> (Azure AI / <code>azure_ai</code> models in LiteLLM)</li>
                <li><strong>Mistral</strong></li>
                <li><strong>Groq</strong></li>
                <li><strong>OpenRouter</strong></li>
                <li><strong>xAI</strong></li>
            </ul>
            <p class="text-gray-600 mb-0">
                The exact default model lists change between releases. For the authoritative catalog, see <code>get_llm_providers()</code> in the <a href="https://github.com/analytiq-hub/doc-router/blob/main/packages/python/analytiq_data/llm/providers.py" class="text-blue-600 hover:text-blue-800" target="_blank" rel="noopener noreferrer">DocRouter source</a> (<code>packages/python/analytiq_data/llm/providers.py</code>).
            </p>
        </section>

        <section id="ocr" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Supported OCR algorithms</h2>
            <p class="text-gray-600 mb-6">
                Each organization selects <strong>one OCR mode</strong> at a time. The pipeline runs that engine over the document PDF and stores a normalized OCR payload for downstream LLM extraction and search.
            </p>
            <div class="overflow-x-auto">
                <table class="min-w-full text-left text-sm text-gray-700 border border-gray-200">
                    <thead class="bg-gray-50 text-gray-900">
                        <tr>
                            <th class="px-4 py-3 border-b border-gray-200">Mode</th>
                            <th class="px-4 py-3 border-b border-gray-200">What it does</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-gray-100">
                            <td class="px-4 py-3 font-medium text-gray-900 whitespace-nowrap"><code>textract</code></td>
                            <td class="px-4 py-3"><strong>Amazon Textract</strong> <code>AnalyzeDocument</code>. Feature types are configurable per org (e.g. <code>LAYOUT</code>, <code>TABLES</code>, <code>FORMS</code>, <code>SIGNATURES</code>). Requires AWS credentials and suitable IAM for Textract and S3 staging as used by your deployment.</td>
                        </tr>
                        <tr class="border-b border-gray-100">
                            <td class="px-4 py-3 font-medium text-gray-900 whitespace-nowrap"><code>mistral</code></td>
                            <td class="px-4 py-3"><strong>Mistral OCR</strong> via the Mistral API (model <code>mistral-ocr-latest</code> in product code). Returns Mistral OCR JSON (pages and layout-oriented content).</td>
                        </tr>
                        <tr class="border-b border-gray-100">
                            <td class="px-4 py-3 font-medium text-gray-900 whitespace-nowrap"><code>llm</code></td>
                            <td class="px-4 py-3"><strong>Vision LLM OCR</strong> — uses a configured LiteLLM provider and model to produce per-page markdown (or equivalent structured text). Useful when you want OCR output aligned with a specific vendor’s multimodal model.</td>
                        </tr>
                        <tr>
                            <td class="px-4 py-3 font-medium text-gray-900 whitespace-nowrap"><code>pymupdf</code></td>
                            <td class="px-4 py-3"><strong>PyMuPDF</strong> text extraction — reads embedded text from the PDF (no cloud OCR). Best for digital PDFs with real text layers; does not perform full-page raster OCR.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p class="text-gray-600 mt-6 mb-0">
                Implementation details live under <code>analytiq_data.ocr</code> in the DocRouter repository (<code>ocr_config.py</code>, <code>ocr_runners.py</code>).
            </p>
        </section>
    </main>
</div>
