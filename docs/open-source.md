---
layout: docs
title: "DocRouter Open Source"
description: "Deploy DocRouter on your own infrastructure with full source code access. Self-hosted, Docker and Kubernetes ready, with enterprise security and no vendor lock-in."
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <header class="text-center md:mb-12 mb-4">
        <div class="text-xl text-gray-600">
            <p class="mb-2">Self-hosted document processing with full source code access</p>
        </div>
    </header>

    <main>
        <section id="overview" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Open Source Benefits</h2>
            <p class="text-gray-600 mb-6">
                DocRouter source code is available under an Apache 2.0 license, giving you complete control over your document processing infrastructure. Deploy on your own infrastructure, customize the processing pipeline, and maintain full data sovereignty.
            </p>
            <p class="text-gray-600 mb-6">
                The full product — including <a href="{{ '/docs/flows/' | relative_url }}" class="text-blue-600 hover:text-blue-800">DocRouter Flows</a>, the visual automation layer with document-native nodes and connector triggers — is part of the open-source tree. You can embed, modify, and redistribute it in commercial or internal products without a separate workflow license. See the <a href="{{ site.baseurl }}{% post_url 2026-06-21-docrouter-flows-visual-workflow-automation-for-intelligent-document-processing %}" class="text-blue-600 hover:text-blue-800">Flows blog post</a> for a walkthrough of visual workflow automation for IDP.
            </p>
            <p class="text-gray-600 mb-6">
                DocRouter is also available under an Enterprise license, including support, maintenance and upgrades.
            </p>
        </section>

        <section id="self-host" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Self-Host DocRouter</h2>
            <p class="text-gray-600 mb-0">
                Install and configure DocRouter on your own servers with Docker Compose or Kubernetes, then connect AWS, GCP, Azure, and LLM providers. See the <a href="{{ '/docs/on-prem-installation/' | relative_url }}" class="text-blue-600 hover:text-blue-800">On-Prem Installation</a> overview for architecture, install options, and an end-to-end checklist.
            </p>
        </section>

        <section class="bg-gray-50 rounded-lg p-8">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4 text-center">Ready to Self-Host?</h2>
            <div class="text-center">
                <p class="text-gray-600 mb-6">
                    Get started with DocRouter open source or contact us for enterprise support and services.
                </p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                    <a href="https://github.com/analytiq-hub/doc-router"
                       target="_blank"
                       rel="noopener noreferrer"
                       class="inline-block bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
                        View on GitHub
                    </a>
                    <button onclick="openCalendly()"
                            class="inline-block border-2 border-blue-600 text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
                        Enterprise Support
                    </button>
                </div>
            </div>
        </section>
    </main>
</div>
