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
                The full product — including <a href="{{ '/docs/flows/' | relative_url }}" class="text-blue-600 hover:text-blue-800">DocRouter Flows</a>, the visual automation layer with document-native nodes and connector triggers — is part of the open-source tree. You can embed, modify, and redistribute it in commercial or internal products without a separate workflow license. See the <a href="{{ site.baseurl }}{% post_url 2026-06-21-docrouter-flows-bringing-the-n8n-architecture-to-intelligent-document-processing %}" class="text-blue-600 hover:text-blue-800">Flows architecture blog post</a> for how the n8n-style model applies to IDP.
            </p>
            <p class="text-gray-600 mb-6">
                DocRouter is also available under an Enterprise license, including support, maintenance and upgrades. 
            </p>
        </section>

        <section id="getting-started" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Quick Start: Docker Compose</h2>

            Install the DocRouter:

            <pre><code>curl -fsSL https://raw.githubusercontent.com/analytiq-hub/doc-router/main/tools/run-doc-router-docker.sh | bash -s -- up</code></pre>

            Configure the DocRouter:

            <ul class="text-gray-600 space-y-2 mt-4 mb-6">
                <li>Open <a href="http://localhost:8080" class="text-blue-600 hover:text-blue-800">http://localhost:8080</a></li>
                <li>Log in as <code>admin</code> / <code>admin</code></li>
                <li>Click the <strong>User Icon</strong> (top right) > <strong>Settings</strong> > <strong>Development</strong></li>
                <li>Click <strong>AWS Setup</strong> > <strong>Manage</strong>, then follow the instructions to set up your AWS account with an S3 bucket and IAM permissions.</li>
                <li>Click <strong>LLM Configuration</strong> > <strong>Manage</strong>. Set up the desired LLM key under <strong>Actions</strong> > <strong>Edit Token</strong>.</li>
            </ul>

            <h2 class="text-2xl font-semibold text-gray-900 mb-4 mt-10">Alternative: Kubernetes (Helm)</h2>

            <p class="text-gray-600 mb-6">
                Install DocRouter from the Helm chart published to GitHub Container Registry (<code>oci://ghcr.io/analytiq-hub/doc-router</code>). Prerequisites: Helm 3.8+, a Kubernetes cluster, an <strong>nginx</strong> ingress controller, MongoDB (Atlas or in-cluster), an AWS S3 bucket, and (for HTTPS) <a href="https://cert-manager.io/" class="text-blue-600 hover:text-blue-800" target="_blank" rel="noopener noreferrer">cert-manager</a> with a <code>letsencrypt-prod</code> ClusterIssuer — the chart enables TLS by default.
            </p>
            <p class="text-gray-600 mb-6">
                If you cloned the <a href="https://github.com/analytiq-hub/doc-router" class="text-blue-600 hover:text-blue-800" target="_blank" rel="noopener noreferrer">doc-router</a> repository, prefer <code>./deploy/scripts/k8s-deploy.sh &lt;overlay&gt;</code> with a <code>.env.&lt;overlay&gt;</code> file (see <a href="https://github.com/analytiq-hub/doc-router/blob/main/deploy/README.md" class="text-blue-600 hover:text-blue-800" target="_blank" rel="noopener noreferrer">deploy/README.md</a>). That script creates the namespace and secret, runs the same Helm upgrade, and restarts pods after secret changes. The steps below are the equivalent manual install.
            </p>

            <h3 class="text-lg font-medium text-gray-900 mb-3">1. Create secrets (before Helm)</h3>
            <p class="text-gray-600 mb-4">
                Credentials live in a Kubernetes Secret named <code>doc-router-secrets</code>, not in Helm values. Create or update it <strong>before</strong> <code>helm upgrade --install</code> — a pre-install migration Job reads only this Secret. Minimum keys: <code>NEXTAUTH_SECRET</code>, <code>MONGODB_URI</code>, <code>ADMIN_EMAIL</code>, <code>ADMIN_PASSWORD</code>, <code>AWS_ACCESS_KEY_ID</code>, <code>AWS_SECRET_ACCESS_KEY</code>, <code>AWS_S3_BUCKET_NAME</code>. Add LLM keys (<code>OPENAI_API_KEY</code>, etc.) in the Secret or configure them later in the UI.
            </p>
            <pre><code>kubectl create namespace doc-router --dry-run=client -o yaml | kubectl apply -f -

kubectl create secret generic doc-router-secrets \
  --namespace doc-router \
  --from-literal=NEXTAUTH_SECRET='change-me' \
  --from-literal=MONGODB_URI='mongodb+srv://user:pass@cluster.example.net/' \
  --from-literal=ADMIN_EMAIL='admin@example.com' \
  --from-literal=ADMIN_PASSWORD='change-me' \
  --from-literal=AWS_ACCESS_KEY_ID='...' \
  --from-literal=AWS_SECRET_ACCESS_KEY='...' \
  --from-literal=AWS_S3_BUCKET_NAME='your-bucket' \
  --dry-run=client -o yaml | kubectl apply -f -</code></pre>

            <h3 class="text-lg font-medium text-gray-900 mb-3 mt-6">2. Install the chart</h3>
            <p class="text-gray-600 mb-4">
                Replace <code>app.example.com</code> with your hostname (DNS must point at the ingress LoadBalancer). Pin <code>--version</code> to the chart version in <a href="https://github.com/analytiq-hub/doc-router/blob/main/deploy/charts/doc-router/Chart.yaml" class="text-blue-600 hover:text-blue-800" target="_blank" rel="noopener noreferrer">Chart.yaml</a> (currently <code>0.3.7</code>). With empty image tags, the chart pulls <code>ghcr.io/analytiq-hub/doc-router-frontend</code> and <code>doc-router-backend</code> at the chart <code>appVersion</code> (e.g. <code>v27.0.1</code>).
            </p>
            <pre><code>helm upgrade --install doc-router oci://ghcr.io/analytiq-hub/doc-router \
  --version 0.3.7 \
  --namespace doc-router \
  --set ingress.host=app.example.com \
  --set ingress.className=nginx \
  --set config.nextauthUrl=https://app.example.com \
  --set config.appBucketName=your-bucket \
  --set config.region=us-east-1 \
  --set config.environment=prod \
  --atomic \
  --timeout 10m</code></pre>

            <p class="text-gray-600 mt-4 mb-6">
                After install: <code>https://app.example.com</code> (API docs at <code>/fastapi/docs</code>). If you change the Secret later, restart workloads: <code>kubectl rollout restart deployment/frontend deployment/backend -n doc-router</code>. Rollbacks: <code>helm history doc-router -n doc-router</code>, <code>helm rollback doc-router -n doc-router</code>. More detail: <a href="{{ site.baseurl }}{% post_url 2026-03-07-deploying-doc-router-on-kubernetes %}">Deploying Doc Router on Kubernetes</a> and <a href="https://github.com/analytiq-hub/doc-router/blob/main/deploy/README.md" class="text-blue-600 hover:text-blue-800" target="_blank" rel="noopener noreferrer">deploy/README.md</a>.
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