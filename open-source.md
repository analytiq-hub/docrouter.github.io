---
layout: docs
title: "DocRouter Open Source"
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <header class="text-center md:mb-12 mb-4">
        <h1 class="text-4xl font-bold text-gray-900 mb-4">DocRouter Open Source</h1>
        <div class="text-xl text-gray-600">
            <p class="mb-2">Self-hosted document processing with full source code access</p>
        </div>
    </header>

    <main>
        <section id="overview" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Open Source Benefits</h2>
            <p class="text-gray-600 mb-6">
                DocRouter is available as an open source project, giving you complete control over your document processing infrastructure.
                Deploy on your own infrastructure, customize the processing pipeline, and maintain full data sovereignty.
            </p>
            <div class="grid md:grid-cols-2 gap-8">
                <div>
                    <h3 class="text-lg font-medium text-gray-900 mb-3">Full Control</h3>
                    <ul class="text-gray-600 space-y-2">
                        <li>• Complete source code access</li>
                        <li>• Self-hosted deployment options</li>
                        <li>• Custom modifications and extensions</li>
                        <li>• No vendor lock-in</li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-lg font-medium text-gray-900 mb-3">Enterprise Ready</h3>
                    <ul class="text-gray-600 space-y-2">
                        <li>• Docker and Kubernetes support</li>
                        <li>• Scalable microservices architecture</li>
                        <li>• Enterprise security features</li>
                        <li>• Professional support available</li>
                    </ul>
                </div>
            </div>
        </section>

        <section id="getting-started" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Getting Started</h2>
            <p class="text-gray-600 mb-6">Clone the repository and start with Docker Compose for local development:</p>

            <pre><code>git clone https://github.com/analytiq-hub/doc-router.git
cd doc-router
docker-compose up -d</code></pre>

            <p class="text-gray-600 mt-6 mb-6">For production deployment with Kubernetes:</p>

            <pre><code>kubectl apply -f k8s/
kubectl port-forward svc/docrouter-frontend 8080:80</code></pre>
        </section>

        <section id="customization" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Customization Options</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <div>
                    <h3 class="text-lg font-medium text-gray-900 mb-3">Processing Pipeline</h3>
                    <ul class="text-gray-600 space-y-2">
                        <li>• Custom OCR engines</li>
                        <li>• Additional AI model integrations</li>
                        <li>• Custom document type handlers</li>
                        <li>• Workflow customization</li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-lg font-medium text-gray-900 mb-3">Integration Points</h3>
                    <ul class="text-gray-600 space-y-2">
                        <li>• Custom API endpoints</li>
                        <li>• Database connectors</li>
                        <li>• Message queue integrations</li>
                        <li>• Authentication providers</li>
                    </ul>
                </div>
            </div>
        </section>

        <section id="community" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Community & Support</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="text-center">
                    <div class="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                        <span class="text-2xl">👥</span>
                    </div>
                    <h3 class="text-lg font-medium text-gray-900 mb-2">Community Support</h3>
                    <p class="text-gray-600">GitHub issues, discussions, and community contributions</p>
                </div>
                <div class="text-center">
                    <div class="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                        <span class="text-2xl">📚</span>
                    </div>
                    <h3 class="text-lg font-medium text-gray-900 mb-2">Documentation</h3>
                    <p class="text-gray-600">Comprehensive setup guides, API docs, and tutorials</p>
                </div>
                <div class="text-center">
                    <div class="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                        <span class="text-2xl">🔧</span>
                    </div>
                    <h3 class="text-lg font-medium text-gray-900 mb-2">Professional Services</h3>
                    <p class="text-gray-600">Enterprise support, training, and custom development</p>
                </div>
            </div>
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
                       class="inline-block bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200">
                        View on GitHub
                    </a>
                    <button onclick="openCalendly()"
                            class="inline-block border-2 border-blue-600 text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200">
                        Enterprise Support
                    </button>
                </div>
            </div>
        </section>
    </main>
</div>