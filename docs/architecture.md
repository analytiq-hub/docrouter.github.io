---
layout: docs
title: "DocRouter Architecture"
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <header class="text-center md:mb-12 mb-4">
        <h1 class="text-4xl font-bold text-gray-900 mb-4">DocRouter Architecture</h1>
        <div class="text-xl text-gray-600">
            <p class="mb-2">Scalable document processing with AI-powered extraction</p>
        </div>
    </header>

    <main>
        <section id="overview" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">System Overview</h2>
            <p class="text-gray-600 mb-6">
                DocRouter is built on a modern, cloud-native architecture designed for scalability, reliability, and ease of integration.
                The system processes documents through a multi-stage pipeline that combines OCR, AI analysis, and structured data extraction.
            </p>
            <div class="flex justify-center mb-6">
                <img src="{{ '/assets/images/docrouter/doc-router-arch.png' | relative_url }}" alt="DocRouter Architecture Diagram" class="w-full max-w-4xl rounded-lg shadow-md">
            </div>
        </section>

        <section id="components" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Core Components</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <div>
                    <h3 class="text-lg font-medium text-gray-900 mb-3">Document Ingestion</h3>
                    <ul class="text-gray-600 space-y-2 mb-6">
                        <li>• Multi-format document support (PDF, images, Office docs)</li>
                        <li>• Secure file upload with encryption</li>
                        <li>• Automatic format detection and conversion</li>
                        <li>• Batch processing capabilities</li>
                    </ul>

                    <h3 class="text-lg font-medium text-gray-900 mb-3">OCR Processing</h3>
                    <ul class="text-gray-600 space-y-2">
                        <li>• Advanced optical character recognition</li>
                        <li>• Handwriting recognition support</li>
                        <li>• Multi-language text extraction</li>
                        <li>• Table and form structure detection</li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-lg font-medium text-gray-900 mb-3">AI Analysis Engine</h3>
                    <ul class="text-gray-600 space-y-2 mb-6">
                        <li>• Large language model integration</li>
                        <li>• Custom prompt engineering</li>
                        <li>• Schema-based data extraction</li>
                        <li>• Confidence scoring and validation</li>
                    </ul>

                    <h3 class="text-lg font-medium text-gray-900 mb-3">Integration Layer</h3>
                    <ul class="text-gray-600 space-y-2">
                        <li>• REST API for programmatic access</li>
                        <li>• Webhook notifications</li>
                        <li>• Third-party system integrations</li>
                        <li>• Real-time status updates</li>
                    </ul>
                </div>
            </div>
        </section>

        <section id="deployment" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Deployment Options</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <div class="overflow-hidden rounded-lg shadow-lg">
                    <img src="{{ '/assets/images/docrouter/architecture_erp.png' | relative_url }}" alt="ERP Integration Architecture" class="w-full">
                    <div class="p-4 bg-gray-50">
                        <h3 class="text-lg font-medium text-gray-900 mb-2">ERP Integration</h3>
                        <p class="text-gray-600">Direct integration with existing ERP and business systems</p>
                    </div>
                </div>
                <div class="overflow-hidden rounded-lg shadow-lg">
                    <img src="{{ '/assets/images/docrouter/architecture_ai_enabler.png' | relative_url }}" alt="AI Tech Stack Architecture" class="w-full">
                    <div class="p-4 bg-gray-50">
                        <h3 class="text-lg font-medium text-gray-900 mb-2">AI Tech Stack</h3>
                        <p class="text-gray-600">Enabling component for AI-powered applications</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="security" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Security & Compliance</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="text-center">
                    <div class="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                        <span class="text-2xl">🔒</span>
                    </div>
                    <h3 class="text-lg font-medium text-gray-900 mb-2">Data Encryption</h3>
                    <p class="text-gray-600">End-to-end encryption for documents in transit and at rest</p>
                </div>
                <div class="text-center">
                    <div class="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                        <span class="text-2xl">📄</span>
                    </div>
                    <h3 class="text-lg font-medium text-gray-900 mb-2">Audit Trails</h3>
                    <p class="text-gray-600">Comprehensive logging and audit trails for compliance</p>
                </div>
                <div class="text-center">
                    <div class="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                        <span class="text-2xl">🏢</span>
                    </div>
                    <h3 class="text-lg font-medium text-gray-900 mb-2">On-Premise Options</h3>
                    <p class="text-gray-600">Self-hosted deployment for maximum data control</p>
                </div>
            </div>
        </section>

        <section class="bg-gray-50 rounded-lg p-8">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4 text-center">Ready to Learn More?</h2>
            <div class="text-center">
                <p class="text-gray-600 mb-6">
                    Contact us to discuss architecture options and deployment strategies for your organization.
                </p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                    <button onclick="openCalendly()"
                            class="inline-block bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
                        Schedule Architecture Review
                    </button>
                    <a href="https://github.com/analytiq-hub/doc-router"
                       target="_blank"
                       rel="noopener noreferrer"
                       class="inline-block border-2 border-blue-600 text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
                        View Source Code
                    </a>
                </div>
            </div>
        </section>
    </main>
</div>