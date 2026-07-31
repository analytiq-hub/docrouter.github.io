---
layout: docs
title: "Azure Configuration"
permalink: /docs/azure-configuration/
description: "Configure Microsoft Azure for DocRouter: Entra service principal and Microsoft Foundry (azure_ai) endpoint for on-prem deployments."
---

Configure Microsoft Entra service principal credentials so DocRouter can call **Microsoft Foundry** models via the `azure_ai` LiteLLM provider. For Azure OpenAI API-key auth (`AZURE_OPENAI_API_KEY`), use [LLM Configuration]({{ '/docs/llm-configuration/' | relative_url }}) instead.

Install the app first via [Docker Compose]({{ '/docs/docker-compose-install/' | relative_url }}) or [Kubernetes]({{ '/docs/kubernetes-install/' | relative_url }}).

## What DocRouter uses Azure for

| Capability | Auth | Notes |
| ---------- | ---- | ----- |
| Microsoft Foundry (`azure_ai`) | Entra service principal | Tenant ID, client ID, client secret, and Foundry API base URL |
| Azure OpenAI (`azure`) | API key | Set `AZURE_OPENAI_API_KEY` in LLM Manager or `.env` |

Foundry auth uses `AsyncClientSecretCredential` and scope `https://ai.azure.com/.default`. Tokens are cached and refreshed by the Azure Identity client.

## 1. Create a Microsoft Foundry resource

1. In the [Azure portal](https://portal.azure.com), create or open a Microsoft Foundry (Azure AI) resource.
2. Note the **endpoint** URL (example: `https://<resource>.services.ai.azure.com`). This becomes `AZURE_API_BASE`.
3. Deploy the models you plan to use (for example `deepseek-v3-0324`, `kimi-k2.5`).

## 2. Create an Entra service principal

1. **Microsoft Entra ID → App registrations → New registration**.
2. Create a client secret (**Certificates & secrets**).
3. Note **Directory (tenant) ID**, **Application (client) ID**, and the **client secret** value.
4. On the Foundry resource, assign the service principal the **Cognitive Services User** role.

## 3. Configure DocRouter

### Option A — Admin UI (preferred)

1. **Account → Development → Azure setup** (`/settings/account/development/azure-config`).
2. Enter:
   - **Tenant ID**
   - **Client ID**
   - **Client secret**
   - **API base URL** (must start with `https://`)
3. Save.

Credentials are stored encrypted in `cloud_config` (`type: "azure"`).

### Option B — `.env` at install time

```bash
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_CLIENT_SECRET=...
AZURE_API_BASE=https://<resource>.services.ai.azure.com
```

On startup, if no Azure config exists yet in the database, non-empty values are seeded into `cloud_config`.

## 4. Enable Foundry models in LLM Manager

1. **Account → Development → LLM Manager → Microsoft Foundry** (provider `azure_ai`).
2. Enable the provider. Do **not** paste an API key — Foundry uses the service principal from Azure setup.
3. Enable models such as:
   - `azure_ai/deepseek-v3-0324`
   - `azure_ai/kimi-k2.5`
4. Run **Test** on a model to confirm connectivity.

## Azure OpenAI (API key)

For the separate `azure` provider (Azure OpenAI with an API key):

1. Set `AZURE_OPENAI_API_KEY` in `.env`, or paste the key in **LLM Manager → Azure OpenAI**.
2. Enable models such as `azure/gpt-4.1-nano`.

This path does not use the Azure setup service principal.

## Verify

- Success: LLM Manager **Test** succeeds for an `azure_ai/...` model
- Failure: missing tenant/client/secret, missing `api_base`, or the service principal lacks **Cognitive Services User** on the Foundry resource

## Credential storage

| Credential | Storage | Admin UI |
| ---------- | ------- | -------- |
| Entra SP + API base | `cloud_config` `type: "azure"` | Account → Development → Azure setup |
| Azure OpenAI API key | `llm_providers.token` | Account → Development → LLM Manager |
