---
layout: docs
title: "LLM Configuration"
permalink: /docs/llm-configuration/
description: "Configure DocRouter LLM providers via LiteLLM. API keys for OpenAI, Anthropic, Gemini, Bedrock, Vertex AI, Azure, and recommended models for document extraction."
---

DocRouter routes all LLM calls through [LiteLLM](https://github.com/BerriAI/litellm). Providers are defined in code (`packages/python/analytiq_data/llm/providers.py`), seeded into MongoDB on startup, and configured per deployment. See the [Platform]({{ '/docs/platform/' | relative_url }}) page for a summary of supported clouds and providers.

After install ([Docker Compose]({{ '/docs/docker-compose-install/' | relative_url }}) or [Kubernetes]({{ '/docs/kubernetes-install/' | relative_url }})), add provider keys here. Cloud-specific setup: [AWS]({{ '/docs/aws-configuration/' | relative_url }}), [GCP]({{ '/docs/gcp-configuration/' | relative_url }}), [Azure]({{ '/docs/azure-configuration/' | relative_url }}).

## Supported providers (summary)

| Provider               | Auth                     | Env variable                                                                  | Default enabled |
| ---------------------- | ------------------------ | ----------------------------------------------------------------------------- | --------------- |
| OpenAI                 | API key                  | `OPENAI_API_KEY`                                                              | Yes             |
| Anthropic              | API key                  | `ANTHROPIC_API_KEY`                                                           | Yes             |
| Gemini (Google AI API) | API key                  | `GEMINI_API_KEY`                                                              | Yes             |
| Mistral                | API key                  | `MISTRAL_API_KEY`                                                             | Yes             |
| Groq                   | API key                  | `GROQ_API_KEY`                                                                | Yes             |
| xAI                    | API key                  | `XAI_API_KEY`                                                                 | Yes             |
| OpenRouter             | API key                  | `OPENROUTER_API_KEY`                                                          | Yes             |
| Azure OpenAI           | API key                  | `AZURE_OPENAI_API_KEY`                                                        | No              |
| Microsoft Foundry      | Service principal        | `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, `AZURE_API_BASE` | No              |
| AWS Bedrock            | AWS user keys            | (same as AWS)                                                                 | No              |
| Google Vertex AI       | GCP service account JSON | GCP setup UI                                                                  | No              |

## How to add API keys

### Option 1 — `.env` at install time

```bash
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
MISTRAL_API_KEY=...
GEMINI_API_KEY=...
GROQ_API_KEY=...
```

On first startup, `setup_llm_providers` copies non-empty env values into encrypted `llm_providers.token` fields.

### Option 2 — Admin UI (preferred after install)

1. Sign in as admin.
2. Go to **Account → Development → LLM Manager** (`/settings/account/development/llm-manager`).
3. Open a provider (e.g. OpenAI, Mistral).
4. Paste the API key, enable the provider, and select which models are enabled.
5. Use **Test** on a model to confirm connectivity.

API: `PUT /v0/account/llm/provider/{provider_name}` with `{ "token": "...", "enabled": true, ... }`.

**Bedrock** — no separate API key; enable the provider and ensure the AWS user has `bedrock:InvokeModel` and models are enabled in the Bedrock console. See [AWS Configuration]({{ '/docs/aws-configuration/' | relative_url }}).

**Vertex AI** — do not set a token on the LLM provider; use [GCP Configuration]({{ '/docs/gcp-configuration/' | relative_url }}).

**Microsoft Foundry** — do not set a token on the `azure_ai` provider; use [Azure Configuration]({{ '/docs/azure-configuration/' | relative_url }}).

## Recommended models for document extraction

For speed and cost on production document workflows:

| Use case                 | Recommended model               | Provider                 |
| ------------------------ | ------------------------------- | ------------------------ |
| Document processing      | `gemini/gemini-3-flash-preview` | Vertex AI or Gemini API  |
| Document Agent           | `claude-opus-4-6`               | AWS Bedrock or Anthropic |
| Chat With Knowledge Base | openai-5.2                      | OpenAI                   |

See [knowledge_base/prompts.md](https://github.com/analytiq-hub/doc-router/blob/main/knowledge_base/prompts.md) in the doc-router repository for model-selection guidance used by built-in agents.

## Credential storage

| Credential            | Storage                           | Admin UI                            |
| --------------------- | --------------------------------- | ----------------------------------- |
| OpenAI, Mistral, etc. | `llm_providers.token` (encrypted) | Account → Development → LLM Manager |
| AWS (for Bedrock)     | `cloud_config` `type: "aws"`      | Account → Development → AWS setup   |
| GCP (for Vertex AI)   | `cloud_config` `type: "gcp"`      | Account → Development → GCP setup   |
| Azure Foundry SP      | `cloud_config` `type: "azure"`    | Account → Development → Azure setup |
