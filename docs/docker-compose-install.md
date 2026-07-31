---
layout: docs
title: "Docker Compose Install"
permalink: /docs/docker-compose-install/
description: "Install DocRouter on a single host with Docker Compose. Quick start script, admin login, and next steps for AWS and LLM configuration."
---

The fastest way to run DocRouter on a single host. For Kubernetes, see [Kubernetes Install]({{ '/docs/kubernetes-install/' | relative_url }}). For architecture and the full checklist, see [On-Prem Installation]({{ '/docs/on-prem-installation/' | relative_url }}).

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/analytiq-hub/doc-router/main/tools/run-doc-router-docker.sh | bash -s -- up
```

## Configure

1. Open [http://localhost:8080](http://localhost:8080)
2. Log in as `admin` / `admin`
3. Click the **User Icon** (top right) → **Settings** → **Development**
4. Click **AWS Setup** → **Manage**, then follow the instructions to set up your AWS account with an S3 bucket and IAM permissions. Details: [AWS Configuration]({{ '/docs/aws-configuration/' | relative_url }}).
5. Click **LLM Configuration** → **Manage**. Set up the desired LLM key under **Actions** → **Edit Token**. Details: [LLM Configuration]({{ '/docs/llm-configuration/' | relative_url }}).

## Next steps

- [AWS Configuration]({{ '/docs/aws-configuration/' | relative_url }}) — IAM, S3, Textract, SES, Bedrock
- [LLM Configuration]({{ '/docs/llm-configuration/' | relative_url }}) — provider keys and models
- [GCP Configuration]({{ '/docs/gcp-configuration/' | relative_url }}) — Vertex AI Gemini
- [Azure Configuration]({{ '/docs/azure-configuration/' | relative_url }}) — Microsoft Foundry
- [Open Source]({{ '/docs/open-source/' | relative_url }}) — licensing and source access
