---
layout: docs
title: "Kubernetes Install"
permalink: /docs/kubernetes-install/
description: "Install DocRouter on Kubernetes with the Helm chart from GitHub Container Registry. Secrets, ingress, TLS, and post-install steps."
---

Install DocRouter from the Helm chart published to GitHub Container Registry (`oci://ghcr.io/analytiq-hub/doc-router`). For a single-host Docker Compose install, see [Docker Compose Install]({{ '/docs/docker-compose-install/' | relative_url }}).

## Prerequisites

- Helm 3.8+
- A Kubernetes cluster
- An **nginx** ingress controller
- MongoDB (Atlas or in-cluster)
- An AWS S3 bucket (see [AWS Configuration]({{ '/docs/aws-configuration/' | relative_url }}))
- For HTTPS: [cert-manager](https://cert-manager.io/) with a `letsencrypt-prod` ClusterIssuer — the chart enables TLS by default

If you cloned the [doc-router](https://github.com/analytiq-hub/doc-router) repository, prefer `./deploy/scripts/k8s-deploy.sh <overlay>` with a `.env.<overlay>` file (see [deploy/README.md](https://github.com/analytiq-hub/doc-router/blob/main/deploy/README.md)). That script creates the namespace and secret, runs the same Helm upgrade, and restarts pods after secret changes. The steps below are the equivalent manual install.

## 1. Create secrets (before Helm)

Credentials live in a Kubernetes Secret named `doc-router-secrets`, not in Helm values. Create or update it **before** `helm upgrade --install` — a pre-install migration Job reads only this Secret. Minimum keys: `NEXTAUTH_SECRET`, `MONGODB_URI`, `ADMIN_EMAIL`, `ADMIN_PASSWORD`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_S3_BUCKET_NAME`. Add LLM keys (`OPENAI_API_KEY`, etc.) in the Secret or configure them later in the UI ([LLM Configuration]({{ '/docs/llm-configuration/' | relative_url }})).

```bash
kubectl create namespace doc-router --dry-run=client -o yaml | kubectl apply -f -

kubectl create secret generic doc-router-secrets \
  --namespace doc-router \
  --from-literal=NEXTAUTH_SECRET='change-me' \
  --from-literal=MONGODB_URI='mongodb+srv://user:pass@cluster.example.net/' \
  --from-literal=ADMIN_EMAIL='admin@example.com' \
  --from-literal=ADMIN_PASSWORD='change-me' \
  --from-literal=AWS_ACCESS_KEY_ID='...' \
  --from-literal=AWS_SECRET_ACCESS_KEY='...' \
  --from-literal=AWS_S3_BUCKET_NAME='your-bucket' \
  --dry-run=client -o yaml | kubectl apply -f -
```

## 2. Install the chart

Replace `app.example.com` with your hostname (DNS must point at the ingress LoadBalancer). Pin `--version` to the chart version in [Chart.yaml](https://github.com/analytiq-hub/doc-router/blob/main/deploy/charts/doc-router/Chart.yaml) (currently `0.3.7`). With empty image tags, the chart pulls `ghcr.io/analytiq-hub/doc-router-frontend` and `doc-router-backend` at the chart `appVersion` (e.g. `v27.0.1`).

```bash
helm upgrade --install doc-router oci://ghcr.io/analytiq-hub/doc-router \
  --version 0.3.7 \
  --namespace doc-router \
  --set ingress.host=app.example.com \
  --set ingress.className=nginx \
  --set config.nextauthUrl=https://app.example.com \
  --set config.appBucketName=your-bucket \
  --set config.region=us-east-1 \
  --set config.environment=prod \
  --atomic \
  --timeout 10m
```

## After install

- App: `https://app.example.com` (API docs at `/fastapi/docs`)
- If you change the Secret later, restart workloads: `kubectl rollout restart deployment/frontend deployment/backend -n doc-router`
- Rollbacks: `helm history doc-router -n doc-router`, `helm rollback doc-router -n doc-router`

More detail: [Deploying Doc Router on Kubernetes]({{ site.baseurl }}{% post_url 2026-03-07-deploying-doc-router-on-kubernetes %}) and [deploy/README.md](https://github.com/analytiq-hub/doc-router/blob/main/deploy/README.md).

## Next steps

- [AWS Configuration]({{ '/docs/aws-configuration/' | relative_url }}) — IAM, S3, Textract, SES, Bedrock
- [LLM Configuration]({{ '/docs/llm-configuration/' | relative_url }}) — provider keys and models
- [GCP Configuration]({{ '/docs/gcp-configuration/' | relative_url }}) — Vertex AI Gemini
- [Azure Configuration]({{ '/docs/azure-configuration/' | relative_url }}) — Microsoft Foundry
- [On-Prem Installation]({{ '/docs/on-prem-installation/' | relative_url }}) — architecture and checklist
