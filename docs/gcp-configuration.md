---
layout: docs
title: "GCP Configuration"
permalink: /docs/gcp-configuration/
description: "Configure Google Cloud for DocRouter: Vertex AI Gemini, service account setup, and Mistral Vertex OCR."
---

Vertex AI is the recommended path when you want Gemini in a **GCP project** (enterprise billing, VPC-SC, data residency) rather than the consumer **Gemini API** (`GEMINI_API_KEY`). Vertex also unlocks **Mistral Vertex OCR** (`mistral_vertex` OCR mode), which uses the same GCP service account.

Install the app first via [Docker Compose]({{ '/docs/docker-compose-install/' | relative_url }}) or [Kubernetes]({{ '/docs/kubernetes-install/' | relative_url }}). Provider keys and model selection: [LLM Configuration]({{ '/docs/llm-configuration/' | relative_url }}).

## 1. Create a GCP project

1. Open [Google Cloud Console](https://console.cloud.google.com).
2. Create a project (note the **Project ID**).
3. Enable billing on the project.

## 2. Enable APIs

In **APIs & Services → Enable APIs**, enable:

- **Vertex AI API** (`aiplatform.googleapis.com`)

For Mistral Vertex OCR only, no extra publisher API is required beyond Vertex AI and Cloud Platform scope.

## 3. Create a service account

1. **IAM & Admin → Service Accounts → Create**.
2. Name example: `docrouter-vertex`.
3. Grant roles (minimum practical set):
   - **Vertex AI User** (`roles/aiplatform.user`)
4. Create a **JSON key** and download it securely.

## 4. Configure DocRouter

### Option A — Admin UI

1. **Account → Development → GCP setup** (`/settings/account/development/gcp-config`).
2. Paste the full service account JSON.
3. Save.

### Option B — Environment (legacy / automation)

Some deployments set `GOOGLE_APPLICATION_CREDENTIALS` to a JSON file path on the server. The primary supported path for on-prem is the GCP setup UI, which stores encrypted JSON in `cloud_config` (`type: "gcp"`).

### Optional — region

Set in `.env`:

```bash
VERTEX_AI_LOCATION=global
```

Default is `global`. LiteLLM uses this as `vertex_location` with `vertex_project` from the service account `project_id`. For Mistral Vertex OCR, the Mistral endpoint is fixed to `us-central1` in code.

## 5. Enable Vertex models in LLM Manager

1. **Account → Development → LLM Manager → Google Vertex AI**.
2. Enable the provider.
3. Enable models, for example:
   - `vertex_ai/gemini-2.5-flash` — strong quality/latency balance for extraction
   - `vertex_ai/gemini-3.1-flash-lite-preview` — newer flash tier
   - `vertex_ai/gemini-embedding-001` — embeddings for knowledge bases
4. Run **Test** on `vertex_ai/gemini-2.5-flash`.

## Gemini API vs Vertex AI

|              | Gemini API (`GEMINI_API_KEY`)   | Vertex AI (GCP service account)     |
| ------------ | ------------------------------- | ----------------------------------- |
| Setup        | API key from Google AI Studio   | GCP project + service account JSON  |
| Model prefix | `gemini/gemini-3-flash-preview` | `vertex_ai/gemini-2.5-flash`        |
| Best for     | Quick start, dev                | Enterprise GCP, Mistral Vertex OCR  |
| DocRouter UI | LLM Manager → Gemini            | GCP setup + LLM Manager → Vertex AI |

For the best **quality/performance** combo on Vertex, start with **`vertex_ai/gemini-2.5-flash`**; move to **`vertex_ai/gemini-3.1-flash-lite-preview`** when you want the newest flash generation.
