---
layout: docs
title: "DocRouter Open Source"
description: "Deploy DocRouter on your own infrastructure with full source code access. Self-hosted, Docker and Kubernetes ready, with enterprise security and no vendor lock-in."
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
                DocRouter source code is available under an Apache 2.0 license, giving you complete control over your document processing infrastructure. Deploy on your own infrastructure, customize the processing pipeline, and maintain full data sovereignty.
            </p>
            <p class="text-gray-600 mb-6">
                DocRouter is also available under an Enterprise license, including support, maintenance and upgrades. 
            </p>
        </section>

        <section id="getting-started" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Quick Start</h2>

            <pre><code>curl -fsSL https://raw.githubusercontent.com/analytiq-hub/doc-router/main/tools/run-doc-router-docker.sh | bash -s -- up</code></pre>

            <ul class="text-gray-600 space-y-2 mt-4 mb-6">
                <li>Open <a href="http://localhost:8080" class="text-blue-600 hover:text-blue-800">http://localhost:8080</a></li>
                <li>Log in as <code>admin</code> / <code>admin</code></li>
                <li>Click the <strong>User Icon</strong> (top right) > <strong>Settings</strong> > <strong>Development</strong></li>
                <li>Click <strong>AWS Setup</strong> > <strong>Manage</strong>, then follow the instructions to set up your AWS account with an S3 bucket and IAM permissions.</li>
                <li>Click <strong>LLM Configuration</strong> > <strong>Manage</strong>. Set up the desired LLM key under <strong>Actions</strong> > <strong>Edit Token</strong>.</li>
            </ul>

            <h2 class="text-2xl font-semibold text-gray-900 mb-4 mt-10">Repository Mode</h2>

            <p class="text-gray-600 mb-6">
                Clone the repository to build from source, customize the stack, or point <code>make deploy-compose</code> at your own MongoDB instance.
            </p>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Clone the repository</h3>
            <pre><code>git clone https://github.com/analytiq-hub/doc-router.git
cd doc-router</code></pre>

            <h3 class="text-lg font-medium text-gray-900 mb-3 mt-6">Set up the <code>.env</code> file</h3>
            <p class="text-gray-600 mb-4">
                Copy the local development template to the repo root and edit it. At minimum, set <code>NEXTAUTH_SECRET</code> and your admin credentials (<code>ADMIN_EMAIL</code>, <code>ADMIN_PASSWORD</code>). Set <code>MONGODB_URI</code> to a MongoDB server the containers can reach (or adjust <code>.env.compose</code> overrides). LLM and AWS keys can be added in <code>.env</code> or later in the UI.
            </p>
            <pre><code>cp .env.example.local .env
# Edit .env with your editor</code></pre>

            <h3 class="text-lg font-medium text-gray-900 mb-3 mt-6">Deploy with Docker Compose</h3>
            <p class="text-gray-600 mb-4">
                From the repository root, run <code>make deploy-compose</code>. This merges <code>.env</code> with <code>.env.compose</code>, builds images, and starts the stack. Requires Docker and a reachable MongoDB at <code>MONGODB_URI</code>.
            </p>
            <pre><code>make deploy-compose</code></pre>

            <p class="text-gray-600 mt-4 mb-2">
                When the stack is up, open <a href="http://localhost:3000" class="text-blue-600 hover:text-blue-800">http://localhost:3000</a> and complete AWS and LLM setup using the same steps as Quick Start above (Development settings).
            </p>
            <p class="text-gray-600 text-sm mb-6">
                For a self-contained stack with embedded MongoDB, use <code>make deploy-compose-embedded</code> instead. See the <a href="https://github.com/analytiq-hub/doc-router/blob/main/docs/docrouter_docker.md" class="text-blue-600 hover:text-blue-800" target="_blank" rel="noopener noreferrer">Docker deployment guide</a> in the repository.
            </p>

            <h3 class="text-lg font-medium text-gray-900 mb-3">Kubernetes (production)</h3>
            <p class="text-gray-600 mb-4">For production deployment with Kubernetes:</p>

            <pre><code>kubectl apply -f k8s/
kubectl port-forward svc/docrouter-frontend 8080:80</code></pre>
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