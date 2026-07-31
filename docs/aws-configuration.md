---
layout: docs
title: "AWS Configuration"
permalink: /docs/aws-configuration/
description: "Configure AWS for DocRouter on-prem: account setup, IAM user/role pattern, Terraform, S3, Textract, SES, and Bedrock."
---

Provision and connect AWS so DocRouter can use S3, Textract, optional SES, and optional Bedrock. Install the app first via [Docker Compose]({{ '/docs/docker-compose-install/' | relative_url }}) or [Kubernetes]({{ '/docs/kubernetes-install/' | relative_url }}). Overview: [On-Prem Installation]({{ '/docs/on-prem-installation/' | relative_url }}).

## Step 1 — Create an AWS account

1. Go to [https://aws.amazon.com](https://aws.amazon.com) and create an account (or use an existing organizational account).
2. Enable MFA on the root user; do **not** use root credentials for DocRouter.
3. Create an IAM admin user (or use AWS IAM Identity Center) for console and Terraform work.
4. Choose a primary region. DocRouter defaults to **us-east-1** for AWS clients (S3, Textract, SES, Bedrock). Keep S3, Textract, and SES in the same region when possible.
5. (Recommended) Enable AWS CloudTrail in the account for audit and troubleshooting.

## Step 2 — Provision AWS resources

You can provision infrastructure manually (console) or with the reference Terraform in the [analytiq-terraform](https://github.com/analytiq-hub/analytiq-terraform) sandbox ([applications/docrouter](https://github.com/analytiq-hub/analytiq-terraform/tree/main/applications/docrouter)), which wraps [modules/docrouter](https://github.com/analytiq-hub/analytiq-terraform/tree/main/modules/docrouter).

### Option A — Terraform (recommended)

Clone the sandbox and apply from the DocRouter application module:

```bash
git clone https://github.com/analytiq-hub/analytiq-terraform.git
cd analytiq-terraform/applications/docrouter
terraform init
terraform apply -var='prefix=docrouter' -var='bucket_name=your-company-docrouter-data'
```

Capture outputs:

| Output           | Use in DocRouter                      |
| ---------------- | ------------------------------------- |
| `app_access_key` | `AWS_ACCESS_KEY_ID`                   |
| `app_secret_key` | `AWS_SECRET_ACCESS_KEY`               |
| `bucket_name`    | `AWS_S3_BUCKET_NAME`                  |
| `app_role_arn`   | Verify role exists (see naming below) |

### Option B — Manual console setup

Follow the IAM layout below so it matches what the application expects.

## Step 3 — IAM roles, users, and permissions

The reference Terraform module [modules/docrouter](https://github.com/analytiq-hub/analytiq-terraform/tree/main/modules/docrouter) in [analytiq-terraform](https://github.com/analytiq-hub/analytiq-terraform) creates a **user + role** pattern. DocRouter authenticates with the IAM **user** access keys, then **assumes an IAM role** for S3 and Textract. Bedrock is invoked with the **user** credentials directly (not the assumed role).

### Naming convention (required)

The backend derives the role ARN from the IAM user name:

- IAM user: `{prefix}-app-user` (e.g. `docrouter-app-user`)
- IAM role: `{prefix}-app-role` (e.g. `docrouter-app-role`)

If the user name does not follow `{prefix}-{suffix}-user`, role assumption fails and Textract/S3 will not work. Use the Terraform module or mirror its names exactly.

### Resources created by Terraform

| Resource   | Name pattern           | Purpose                                     |
| ---------- | ---------------------- | ------------------------------------------- |
| IAM user   | `{prefix}-app-user`    | Long-lived access keys in `.env` / admin UI |
| IAM role   | `{prefix}-app-role`    | Assumed for S3 and Textract                 |
| S3 bucket  | `bucket_name` variable | Document storage and Textract staging       |
| Access key | (attached to user)     | Programmatic access                         |

### Permissions on the IAM role (`{prefix}-app-role`)

| Permission source                           | AWS service     | What DocRouter uses it for                                                          |
| ------------------------------------------- | --------------- | ----------------------------------------------------------------------------------- |
| Managed policy `AmazonTextractFullAccess`   | Amazon Textract | OCR on uploaded PDFs and images                                                     |
| Managed policy `AmazonSESFullAccess`        | Amazon SES      | Invitation, verification, and notification email                                    |
| Inline policy `{prefix}-app-role-s3-access` | Amazon S3       | `GetObject`, `PutObject`, `ListBucket`, `DeleteObject` on the DocRouter bucket only |

S3 bucket settings from Terraform:

- Server-side encryption: AES-256
- Bucket policy grants the app role `s3:*` on bucket objects

### Permissions on the IAM user (`{prefix}-app-user`)

| Policy                                | Actions                                                           | Why on the user (not the role)                            |
| ------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------- |
| Inline `assume-{prefix}-app-role`     | `sts:AssumeRole` on `{prefix}-app-role`                           | Allows the app to assume the role for S3/Textract         |
| Inline `{prefix}-bedrock-user-policy` | `bedrock:InvokeModel` on foundation models and inference profiles | Bedrock auth uses user keys, not assumed-role credentials |

Bedrock policy (from Terraform):

```json
{
  "Effect": "Allow",
  "Action": "bedrock:InvokeModel",
  "Resource": [
    "arn:aws:bedrock:*::foundation-model/*",
    "arn:aws:bedrock:*:*:inference-profile/*"
  ]
}
```

### Minimal manual IAM policy (if not using managed policies)

For least-privilege manual setup, attach equivalent permissions to the **role**:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:ListBucket",
        "s3:DeleteObject"
      ],
      "Resource": [
        "arn:aws:s3:::YOUR-BUCKET-NAME",
        "arn:aws:s3:::YOUR-BUCKET-NAME/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "textract:StartDocumentAnalysis",
        "textract:GetDocumentAnalysis",
        "textract:StartDocumentTextDetection",
        "textract:GetDocumentTextDetection"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ses:SendEmail",
        "ses:SendRawEmail"
      ],
      "Resource": "*"
    }
  ]
}
```

On the **user**, add `sts:AssumeRole` for the role ARN and `bedrock:InvokeModel` if you use Bedrock.

## Step 4 — AWS services used by DocRouter

| Service             | Required?                            | Used for                                                                    |
| ------------------- | ------------------------------------ | --------------------------------------------------------------------------- |
| **Amazon S3**       | Yes (for default OCR pipeline)       | Document binaries, Textract temp uploads, exports                           |
| **Amazon Textract** | Yes (unless org OCR mode is changed) | Default OCR engine (`textract` mode)                                        |
| **Amazon SES**      | Optional                             | Outbound email when `SES_FROM_EMAIL` is set; sender must be verified in SES |
| **Amazon Bedrock**  | Optional                             | Claude and embedding models via `bedrock` LLM provider                      |
| **AWS STS**         | Yes (with role pattern)              | `AssumeRole` from user to role                                              |

DocRouter does **not** require AWS Lambda, ECS, or EKS for on-prem installs; only the APIs above.

### Bedrock model access

After IAM is in place, open the **Amazon Bedrock** console → **Model access** (or **Foundation models**) and enable the models you plan to use, for example:

- `us.anthropic.claude-sonnet-4-6`
- `us.anthropic.claude-opus-4-6-v1`
- `cohere.embed-v4:0`
- `amazon.titan-embed-text-v2:0`

Then enable the **Bedrock** provider in DocRouter (see [LLM Configuration]({{ '/docs/llm-configuration/' | relative_url }})).

### SES setup (optional)

1. Verify the sender address or domain in SES.
2. If the account is in the SES sandbox, verify recipient addresses or request production access.
3. Set `SES_FROM_EMAIL` in `.env` to the verified sender.

## Step 5 — Configure AWS in DocRouter

### Via `.env` (first boot)

Add to the project root `.env` (see `.env.example.aws_lightsail` in the [doc-router](https://github.com/analytiq-hub/doc-router) repository):

```bash
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=...
AWS_S3_BUCKET_NAME=your-company-docrouter-data
SES_FROM_EMAIL=noreply@yourdomain.com   # optional
```

On startup, after the admin user exists, these values are encrypted and stored in `cloud_config` (`type: "aws"`).

### Via admin UI (ongoing)

**Account → Development → AWS setup** (`/settings/account/development/aws-config`)

Stores access key ID, secret access key, and S3 bucket name in `cloud_config`. This overrides `.env` for runtime behavior.

### Verify

Check backend logs after restart:

- Success: AWS clients initialize and Textract runs on document upload
- Failure: `AWS credentials are not correct` or `AWS role assumption failed` — usually wrong keys, missing `AssumeRole`, or user/role naming mismatch

## Related Terraform sandbox

The canonical IAM and S3 layout lives in the [analytiq-terraform](https://github.com/analytiq-hub/analytiq-terraform) GitHub sandbox:

- [applications/docrouter/main.tf](https://github.com/analytiq-hub/analytiq-terraform/blob/main/applications/docrouter/main.tf) — application entrypoint
- [modules/docrouter/main.tf](https://github.com/analytiq-hub/analytiq-terraform/blob/main/modules/docrouter/main.tf) — IAM user, role, policies, S3 bucket

When in doubt, clone the sandbox, run `terraform apply` from `applications/docrouter`, and use the outputs in DocRouter `.env`.
