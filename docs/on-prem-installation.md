---
layout: docs
title: "On-Prem Installation"
permalink: /docs/on-prem-installation/
description: "Deploy DocRouter on customer-owned infrastructure with Docker Compose or Kubernetes. Configure AWS, GCP, Azure, and LLM providers."
---

Deploy DocRouter on your servers (Docker Compose or Kubernetes) while connecting to managed cloud APIs for OCR, storage, email, and LLM inference.

## Guides

| Guide | Description |
| ----- | ----------- |
| [Docker Compose Install](/docs/docker-compose-install/) | Single-host quick start |
| [Kubernetes Install](/docs/kubernetes-install/) | Helm chart for production clusters |
| [LLM Configuration](/docs/llm-configuration/) | Provider API keys and model selection |
| [AWS Configuration](/docs/aws-configuration/) | S3, Textract, SES, Bedrock, IAM |
| [GCP Configuration](/docs/gcp-configuration/) | Vertex AI Gemini and Mistral Vertex OCR |
| [Azure Configuration](/docs/azure-configuration/) | Microsoft Foundry service principal |

For licensing and source access, see [Open Source]({{ '/docs/open-source/' | relative_url }}).

## Overview

DocRouter is a multi-service application that runs on your servers but calls out to managed cloud APIs for document OCR, object storage, email, and LLM inference.

<div data-excalidraw="/assets/excalidraw/on_prem_installation_architecture.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>

<p style="text-align: center; margin-top: 0.5rem; font-size: 0.875rem; color: #6b7280;">
  <strong>Figure 1:</strong> On-prem installation architecture — customer infrastructure, AWS account, and optional third-party LLM APIs.
</p>

<div style="text-align: center; margin-top: 1rem; margin-bottom: 2rem;">
  <a href="/excalidraw-edit?file=/assets/excalidraw/on_prem_installation_architecture.excalidraw" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: 500;">
    Edit in Excalidraw
  </a>
</div>

### Typical on-prem stack

| Component            | Where it runs                  | Notes                                              |
| -------------------- | ------------------------------ | -------------------------------------------------- |
| Frontend (Next.js)   | Docker Compose / K8s           | Port 3000                                          |
| Backend (FastAPI)    | Docker Compose / K8s           | Port 8000                                          |
| Workers              | Docker Compose / K8s           | OCR, LLMs, and flows (queue-based processing)      |
| MongoDB              | Embedded, Atlas, or DocumentDB | App state, encrypted credentials, login passwords  |
| AWS                  | Customer AWS account           | S3, Textract, SES (optional), Bedrock (optional)   |
| Third-party LLM APIs | Vendor SaaS (optional)         | OpenAI, Anthropic, Vertex AI & Gemini, Azure, etc. |

Credentials are stored encrypted in MongoDB (`cloud_config` for deployment-wide AWS/GCP/Azure; `llm_providers` for per-provider API keys; user login passwords). On first startup, values from `.env` are seeded into the database when admin bootstrap completes.

---

## End-to-end checklist

### Application platform

- Provision server or containers ([Docker Compose]({{ '/docs/docker-compose-install/' | relative_url }}) or [Kubernetes]({{ '/docs/kubernetes-install/' | relative_url }}))
- Install MongoDB and set `MONGODB_URI`
- Set `ADMIN_EMAIL`, `ADMIN_PASSWORD`, `NEXTAUTH_SECRET`, `NEXTAUTH_URL`
- Deploy frontend, backend, worker, and reverse proxy (nginx)
- Confirm migrations ran and admin can log in

### AWS

- Follow [AWS Configuration]({{ '/docs/aws-configuration/' | relative_url }}): S3 bucket, IAM user/role, optional SES and Bedrock
- Put `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_S3_BUCKET_NAME` in `.env` or AWS setup UI

### LLM

- Add API keys via `.env` or **LLM Manager** — see [LLM Configuration]({{ '/docs/llm-configuration/' | relative_url }})
- (Optional) Enable Bedrock after AWS + model access
- (Optional) Complete [GCP]({{ '/docs/gcp-configuration/' | relative_url }}) Vertex setup
- (Optional) Complete [Azure]({{ '/docs/azure-configuration/' | relative_url }}) Foundry setup

### Validation

- Upload a PDF; confirm Textract OCR completes
- Run a prompt against your chosen model
- (Optional) Send a test email if using SES
- (Optional) Test Bedrock, Vertex, or Foundry from LLM Manager

---

## Credential storage reference

| Credential            | Storage                           | Admin UI                            |
| --------------------- | --------------------------------- | ----------------------------------- |
| AWS keys + bucket     | `cloud_config` `type: "aws"`      | Account → Development → AWS setup   |
| GCP service account   | `cloud_config` `type: "gcp"`      | Account → Development → GCP setup   |
| Azure Foundry SP      | `cloud_config` `type: "azure"`    | Account → Development → Azure setup |
| OpenAI, Mistral, etc. | `llm_providers.token` (encrypted) | Account → Development → LLM Manager |

<style>
.excalidraw-container {
  width: 100%;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  background: white;
  display: block;
  margin: 2rem 0;
  min-height: 400px;
}
.excalidraw-container svg {
  width: 100%;
  height: auto;
  display: block;
  margin: 0;
}
.loading-placeholder {
  padding: 2rem;
  text-align: center;
  color: #666;
}
</style>
<script type="module" src="/assets/js/excalidraw/render-excalidraw.js"></script>
