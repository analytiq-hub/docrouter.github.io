---
layout: post
title: "How We Built the DocRouter n8n Nodes With Cursor (In the Open)"
date: 2026-01-31 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: "assets/images/n8n_gmail_to_docrouter.png"
categories: [ai, programming, engineering, tutorials]
---

We shipped **[n8n-nodes-docrouter](https://www.npmjs.com/package/n8n-nodes-docrouter)**—a full set of n8n community nodes and credentials for [DocRouter.ai](https://app.docrouter.ai). This post does three things: **how to use the nodes** (with examples), **how we built them** in a single Cursor thread while cross-checking the real backend in `../doc-router`, and **how this blog post was written**.

---

## How to Use the DocRouter n8n Nodes

### Install the package

The easiest way is in the n8n UI: **Settings → Community Nodes → Install**, then enter the package name **n8n-nodes-docrouter**.[^1]

The DocRouter nodes then become available in the node search list.

<div class="n8n-img-cred-wrap">
  <span class="n8n-img-modal-wrap"><img class="n8n-img-modal-trigger" src="/assets/images/n8n_docrouter_nodes.png" alt="DocRouter nodes in n8n" data-modal-src="/assets/images/n8n_docrouter_nodes.png" /></span>
</div>

### Credentials

You need one of two credential types:

- **DocRouter Organization API** – organization-level token. Use it for: Documents, Tags, LLM, Prompts, Schemas, Knowledge Base, Webhook.
- **DocRouter Account API** – account-level token. Use it only for the **DocRouter Account** node (users and organizations).

Create the API token in **DocRouter** (Settings → User → Developer). Then create the credential in **n8n** (Settings → Credentials or when adding a DocRouter node), paste your API token from DocRouter, and optionally override the base URL for self-hosted or staging (default: `https://app.docrouter.ai/fastapi`).

<div class="n8n-img-cred-wrap">
  <span class="n8n-img-modal-wrap"><img class="n8n-img-modal-trigger" src="/assets/images/n8n_org_creds.png" alt="DocRouter Organization API credential in n8n" data-modal-src="/assets/images/n8n_org_creds.png" /></span>
</div>

### Example: List documents and get one

1. Add a **DocRouter Document** node.
2. Choose credential: **DocRouter Organization API**.
3. Operation: **List** (optional: limit, skip, name search).
4. Run the workflow → you get a list of documents (and total count).
5. Add another **DocRouter Document** node, Operation: **Get**, set **Document ID** (e.g. from the first node’s output: `{% raw %}{{ $json.id }}{% endraw %}`).
6. Run → you get that document’s metadata; if it has content, it’s in **binary** (downloadable).

<div class="grid md:grid-cols-2 gap-4 md:gap-6 my-4 md:my-6">
  <span class="n8n-img-modal-wrap"><img class="n8n-img-modal-trigger" src="/assets/images/n8n_list_documents.png" alt="DocRouter List Documents in n8n" data-modal-src="/assets/images/n8n_list_documents.png" /></span>
  <span class="n8n-img-modal-wrap"><img class="n8n-img-modal-trigger" src="/assets/images/n8n_get_document.png" alt="DocRouter Get Document in n8n" data-modal-src="/assets/images/n8n_get_document.png" /></span>
</div>

### Example: Chat with a knowledge base

1. Add a **DocRouter Knowledge Base** node.
2. Credential: **DocRouter Organization API**.
3. Operation: **Chat**.
4. Set **Knowledge Base ID**, **Model** (e.g. `gpt-4o-mini`), **Messages** (JSON array, e.g. `[{"role":"user","content":"What do we have on resumes?"}]`).
5. **Stream**: off → you get a single JSON object with `text`, `tool_calls`, `tool_results`. Stream on → you get the same shape after the node parses SSE for you.
6. Run → the output has the assistant’s answer and any tool calls (e.g. `search_knowledge_base`) and results.

<div class="n8n-img-cred-wrap">
  <span class="n8n-img-modal-wrap"><img class="n8n-img-modal-trigger" src="/assets/images/n8n_chat_with_kb.png" alt="DocRouter Chat with Knowledge Base in n8n" data-modal-src="/assets/images/n8n_chat_with_kb.png" /></span>
</div>

### Example: Manage users (account admin)

1. Add a **DocRouter Account** node.
2. Credential: **DocRouter Account API** (account-level token).
3. Operation: **List Users** (optional: limit, skip, organization ID filter, search name).
4. Or **Create User** (email, name, password), **Update User** (user ID + optional name, password, role, etc.), **Delete User** (user ID).

Same node supports **List / Get / Create / Update / Delete Organizations** with the same account credential.

<div class="n8n-img-cred-wrap">
  <span class="n8n-img-modal-wrap"><img class="n8n-img-modal-trigger" src="/assets/images/n8n_list_users.png" alt="DocRouter List Users in n8n" data-modal-src="/assets/images/n8n_list_users.png" /></span>
</div>

### Example: Webhook trigger

1. Add a **DocRouter Webhook** node (trigger).
2. Configure **Webhook path** and, if you use HMAC in DocRouter, the **Secret** and optional **Timestamp tolerance**.
3. When DocRouter sends an event to that URL, the workflow runs; you can verify the signature and use the payload in the next nodes.

Other nodes (**DocRouter Tag**, **LLM**, **Prompt**, **Schema**) follow the same pattern: pick operation (List, Get, Create, Update, Delete—or operation-specific ones like Run LLM, Validate Schema, Search KB), fill resource IDs and body fields, run.

---

## How It Was Implemented “In the Open”

The nodes were built in **one Cursor thread**, with the codebase and the **real DocRouter backend** in `../doc-router` open in the same workspace. That made it possible to implement, then immediately check and fix behavior against the actual API and Python code.

### What we had at the start

- An n8n community node repo derived from the n8n starter (with Example and GitHub Issues nodes).
- DocRouter Organization API credentials type already present.
- A goal: “Build n8n nodes for DocRouter.ai” and, step by step, add all the APIs we use.

### Prompts and steps (in order)

Roughly, the conversation went like this:

1. **Document node and binary content**  
   Ask: what’s the right n8n pattern for document content—binary vs base64? Answer: use the **binary** property. Then: add an “Output Document As” option; later: remove it and only support binary when content exists.

2. **Webhook trigger**  
   Ask: add a trigger node for DocRouter webhooks with HMAC verification and optional timestamp check. Implemented; then we hit `_a.trim is not a function` because the secret wasn’t always a string—fixed with a type guard (`typeof rawSecret === 'string' ? rawSecret.trim() : ''`).

3. **Tags, then “Custom API Call”**  
   Ask: add a node for DocRouter tags (List, Get, Create, Update, Delete). After that, “remove the Custom API Call option.” That option comes from n8n core for credential-based nodes. We can’t remove it from the UI, so we handled `__CUSTOM_API_CALL__` in the switch and threw a clear error telling users to use the HTTP Request node for custom calls. That pattern was reused in every DocRouter node.

4. **GitHub nodes gone**  
   Ask: remove all GitHub-related nodes, credentials, and icons. We deleted those files and cleaned up `package.json`.

5. **LLM, Prompts, Schemas, Knowledge Base**  
   One after the other: “Add a node for DocRouter LLM (run, get, update, delete result),” “Add a node for DocRouter Prompts (all APIs),” “Add a node for DocRouter Schemas (including validate and list versions),” “Add a node for DocRouter Knowledge Base (list, get, create, update, delete, list documents/chunks, search, chat, reconcile).” Each time we followed the same structure: operations, parameters, one List/Get-style “run once” path and per-item paths for Create/Update/Delete, plus the `__CUSTOM_API_CALL__` branch.

6. **Knowledge Base Chat and streaming**  
   In use we saw: with **stream on**, the result was parsed correctly; with **stream off**, the API was still returning SSE. Prompt: “When stream is off, the result is still sent as stream, is that correct?” We fixed the **n8n node** first: detect SSE-shaped responses and always parse them into one object (`text`, `tool_calls`, `tool_results`) so the output is consistent. Then: “Look under ../doc-router, is stream=false supported as a parameter?” We checked the Python API: the parameter existed but the KB chat handler always returned a streaming response. So the next prompt was: “Fix it in ../doc-router.” We added a non-streaming path in `run_kb_chat`: when `request.stream` is false, run the same agentic loop but collect into a single dict and return JSON instead of `StreamingResponse`. After that: “Fix the n8n node now to expect non-streaming response in non-streaming mode”—so when stream is off we use the response as-is (one JSON object) and only parse SSE when stream is on.

7. **Account node**  
   “Create a docrouter node for accounts, with all apis for account/users and account/organizations.” We already had DocRouter Account API credentials. We added the **DocRouter Account** node with List/Get/Create/Update/Delete for both Users and Organizations, using the account-level API and the same patterns as the other nodes.

8. **Publishing**  
   “I’d like to publish it as n8n-nodes-docrouter” → we confirmed the name, fixed the README to match the real package contents, removed the wrong `main` field from `package.json`, and left publish steps (including `npm publish --otp=...` for 2FA). Then: “Publish it.” The `prepublishOnly` script was still `n8n-node prerelease`, which blocked publish and said to use `npm run release`. We changed it to `npm run build` so `npm publish` builds and publishes; publish then succeeded. “OK - the README was not updated to reflect the correct package contents” → we rewrote the README with the actual nodes and credentials, installation, and usage. “What version is the package now” → 0.1.0. “Bump version and release” → we bumped to 0.1.1 and ran `npm publish` again (tag `v0.1.1` was created in git).

### Hooking up to ../doc-router

Having **doc-router** in the same workspace (as `../doc-router`) was critical:

- **Stream parameter:** We didn’t assume the API “must” support `stream=false`; we searched the Python routes and `run_kb_chat` and saw the parameter existed but the handler always returned a stream. So we fixed the backend first, then the node.
- **Optional parameters:** The Knowledge Base node had “Could not get parameter” for optional fields like `coalesceNeighborsSearch` and `maxTokens`. We avoided calling `getNodeParameter` for those unless the parameter key existed in `this.getNode().parameters`, matching how n8n omits optional params.
- **SSE shape:** We matched the backend’s SSE format (`data: {"type":"tool_call",...}`, `data: {"chunk":"H",...}`, etc.) so the node’s parser could aggregate tool calls, tool results, and text chunks correctly.

So: **implement in the node repo, verify and fix against the real API and backend in doc-router.** No guessing the contract.

### How this blog post was written

You’re reading the result of another Cursor prompt in the same “in the open” style:

- **Request:** Write a markdown blog post that (1) at the top explains how to use the DocRouter n8n nodes with examples, (2) in the middle explains step-by-step how the nodes were created in this Cursor thread, what prompts were used, and how we hooked up to the ../doc-router sandbox to review and fix things, and (3) explains how the blog post itself was written. 

- **What Cursor did:** It read a couple of existing posts for front matter and tone, and created a new one, as a synthesis of the conversation summary and the steps we just walked through: usage first, then implementation story and prompts, then “how this post was written.” So this post is both the doc and the meta-story of how it was generated.

---

## Summary

- **Use the nodes:** Install via **Settings → Community Nodes → Install** (package name: **n8n-nodes-docrouter**),[^1] add DocRouter Org or Account credentials, then add DocRouter nodes and pick operations (List, Get, Create, Update, Delete, or operation-specific ones like Chat, Run LLM, Validate Schema).
- **Build process:** One Cursor thread, incremental prompts (documents → webhook → tags → remove GitHub → LLM → Prompts → Schemas → Knowledge Base → stream fix in backend + node → Account node → README → publish and version bump). Cross-checking against `../doc-router` ensured the nodes matched the real API and behavior.
- **This post:** The workflow—prompt used for the current blog post.

[n8n-nodes-docrouter on npm](https://www.npmjs.com/package/n8n-nodes-docrouter) · [Source on GitHub](https://github.com/analytiqhub/n8n-nodes-docrouter) · [DocRouter docs](https://app.docrouter.ai)

----

## Footnotes

[^1]: **Alternative ways to install (npm or Docker):** Where n8n is installed, run `npm install n8n-nodes-docrouter` and restart n8n. For Docker, set `N8N_COMMUNITY_PACKAGES=n8n-nodes-docrouter`.

<style>
.n8n-img-cred-wrap { display: flex; justify-content: center; margin: 1rem 0; }
.n8n-img-cred-wrap .n8n-img-modal-wrap { max-width: 50%; }
.n8n-img-cred-wrap .n8n-img-modal-wrap img { width: 100%; height: auto; display: block; }
.n8n-img-modal-wrap { position: relative; display: inline-block; }
.n8n-img-modal-wrap::after { content: "Click to expand"; position: absolute; bottom: 8px; left: 50%; transform: translateX(-50%); background: rgba(0,0,0,0.75); color: #fff; padding: 4px 10px; border-radius: 4px; font-size: 12px; white-space: nowrap; opacity: 0; transition: opacity 0.2s ease; pointer-events: none; }
.n8n-img-modal-wrap:hover::after { opacity: 1; }
.n8n-img-modal-backdrop { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.85); z-index: 9999; align-items: center; justify-content: center; cursor: pointer; }
.n8n-img-modal-backdrop.is-open { display: flex; }
.n8n-img-modal-backdrop img { max-width: 95vw; max-height: 95vh; object-fit: contain; pointer-events: none; }
.n8n-img-modal-trigger { cursor: pointer; }
</style>
<div class="n8n-img-modal-backdrop" id="n8n-img-modal" role="button" tabindex="-1" aria-label="Close">
  <img src="" alt="" id="n8n-img-modal-img" />
</div>
<script>
(function() {
  var backdrop = document.getElementById('n8n-img-modal');
  var modalImg = document.getElementById('n8n-img-modal-img');
  var triggers = document.querySelectorAll('.n8n-img-modal-trigger');
  function openModal(src, alt) { modalImg.src = src; modalImg.alt = alt; backdrop.classList.add('is-open'); }
  function closeModal() { backdrop.classList.remove('is-open'); }
  triggers.forEach(function(el) { el.addEventListener('click', function() { openModal(el.dataset.modalSrc, el.alt); }); });
  backdrop.addEventListener('click', closeModal);
  document.addEventListener('keydown', function(e) { if (e.key === 'Escape') closeModal(); });
})();
</script>
