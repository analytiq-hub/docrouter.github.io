---
layout: post
title: "How We Built the Document Agent: Architecture and Decisions"
date: 2026-02-22 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: /assets/images/document-agent-blog-splash.png
categories: [ai, programming, engineering, product]
---

The **Document Agent** is the chat on the document page in DocRouter: you talk to an AI in the context of a single document to create or edit schemas, prompts, and tags, run extraction, and tweak results. This post explains how we implemented it—the architecture and the decisions that shaped it.

---

## What the agent does

The agent is a **tool-calling LLM** scoped to one document. It sees the document’s metadata, an OCR text excerpt, optional @-mentions (schemas, prompts, tags you’ve referenced), and the current extraction. It has **25 tools**: schema CRUD and validation, prompt CRUD, tag CRUD, document list/update/delete, get OCR text, run extraction, patch extraction fields, and two help tools (`help_schemas`, `help_prompts`). Read-only tools run automatically; **read-write** tools (create schema, run extraction, update document, etc.) can pause and ask the user to approve or reject each call. Conversations are stored in **threads** per document so you can resume or start a new one.

---

## Architecture overview

Three layers matter: the **agent loop**, the **context** we give the LLM, and the **state** we keep between requests.

**1. Agent loop**  
The core is a loop: send messages to the LLM (system + conversation + tool definitions) → get back text and/or tool calls. If there are tool calls and any of them is read-write and not auto-approved, we **stop**, persist the turn state, and return a `turn_id` and the pending tool calls to the client. The client shows approve/reject UI and then calls **POST /chat/approve** with the same `turn_id` and the user’s approvals. The backend executes the approved tools, appends tool-result messages to the conversation, and sends that back to the LLM **once**. We do **not** loop on the approve endpoint: each approve is one LLM round. If the LLM returns more tool calls, we again return them to the client for approval. So the loop is “LLM → maybe pause for user → execute tools → LLM again,” with the pause happening in the client, not in a long-running server loop. We cap the number of tool rounds (e.g. 10) so a turn can’t run forever.

**2. Context (system message)**  
Every turn gets a **system message** built from: (a) document ID and file name, (b) **OCR excerpt** of the document (truncated to ~8k characters so we don’t blow the context window), (c) **resolved @-mentions**—if the user referenced a schema, prompt, or tag, we resolve it server-side and inject the full content (e.g. full JSON schema) into the system message so the LLM doesn’t have to call `get_schema` just to see what they meant, (d) **working state**: the last `schema_revid`, `prompt_revid`, and **extraction** result from this conversation. That way the agent always knows “the schema I just created,” “the prompt I just created,” and “the extraction I just ran,” and can say “run extraction with that prompt” without the user re-specifying IDs. We also inject instructions: use `help_schemas` / `help_prompts` when creating or modifying those artifacts, and **always** call `validate_schema` before `create_schema` or `update_schema` so we never persist invalid schemas.

**3. State: turn state vs threads**  
We keep two kinds of state. **Turn state** is short-lived and in-memory: when we pause for approval, we store the current message list, pending tool calls, working state, model, and related bits keyed by `turn_id`, with a **TTL of 5 minutes**. The approve endpoint looks up by `turn_id`, applies approvals, runs tools, and then clears that turn state. We don’t put this in the database because it’s transient—if the user abandons the tab or the server restarts, the turn simply expires and they can re-send their message. **Threads** are persistent (MongoDB, `agent_threads`): organization, document, and user-scoped. When a turn finishes (no more pending tool calls), we append the user and assistant messages (and the latest extraction) to the thread. So: turn state = “in-flight approval”; threads = “saved conversations” you can list, load, and resume.

---

## Key decisions

**Read-only vs read-write tools**  
We split tools into two sets. **Read-only** (e.g. `get_ocr_text`, `list_schemas`, `validate_schema`, `help_schemas`) never require approval—they’re safe to run as soon as the LLM asks. **Read-write** (e.g. `create_schema`, `run_extraction`, `update_document`) require approval by default. The client can send `auto_approve: true` (run everything) or `auto_approved_tools: ["run_extraction"]` (only those run without pausing). That way power users can say “just run extraction when I ask” while still being prompted for “create a new schema.” The backend exposes **GET /chat/tools** returning the two lists so the UI can explain which actions will pause.

**One LLM round per approve**  
When the user approves tool calls, we execute them and call the LLM **once** with the new tool results. If the LLM returns more tool calls, we return those to the client again—we don’t keep looping on the server. The reason is **control**: the user sees each batch of proposed actions and can approve or reject. If we looped server-side until “no more tool calls,” a single request could do many creates/updates before the user saw anything. So the “loop” is really a handshake: chat → (optional approve) → chat → (optional approve) → …

**Sanitizing messages when loading from a thread**  
When the user resumes a thread, we send the saved messages back to the LLM. But the API requires that every assistant message with `tool_calls` is **immediately** followed by `tool` messages (one per call). If the user had left mid-approval or we stored a partial state, we might have an assistant message with tool_calls and no following tool results. So before building the LLM request we **sanitize**: we walk the message list and, for any assistant message with tool_calls, check that the next messages are tool results for those call IDs. If not, we strip the tool_calls from that assistant message and send it as content-only. That keeps the API happy and avoids confusing the model with an invalid history.

**Working state in the loop**  
`working_state` (schema_revid, prompt_revid, extraction) is updated by the tool implementations as they run (e.g. `run_extraction` sets `working_state["extraction"]` and `working_state["prompt_revid"]`). The system message is built once per turn with the **current** working state. So when the agent says “I’ll use the prompt we just created,” the next LLM call already has that prompt_revid in the system message and the agent can call `run_extraction` without a prompt_revid argument (we use working state as default). Same for “update the total to 1,250”—the agent sees the current extraction JSON and can call `update_extraction_field` with the right path.

**Streaming and approval**  
We support **streaming** (SSE) for the main chat endpoint: the client gets events for thinking chunks, text chunks, tool calls, tool results, and a final `done` payload. The **approve** endpoint is non-streaming: one request, one response. That keeps the approve flow simple (no need to stream a single round) and keeps the “pause for approval” contract clear: you get a full set of tool calls, you approve, you get one full response. Streaming is for the interactive chat experience; approve is for the control boundary.

**Thinking blocks and API compatibility**  
Some models (e.g. Claude with extended thinking) return **thinking_blocks** in the response. When we continue the conversation (e.g. after tool execution), we must send those blocks back to the API in the right format—Anthropic requires a non-empty `signature` on each block. Our streaming path sometimes produces blocks without signatures, so we have a pass that only includes blocks that have a signature when we rebuild the message for the next call. We also avoid sending the `thinking` parameter when the last assistant message had tool_calls but no thinking_blocks, so we don’t trigger API warnings or rejections.

**SPU and cost**  
Each LLM call in the agent (and each call inside `run_extraction`) checks **SPU** (our credit system) independently. We don’t reserve or estimate “total cost for this turn” upfront—we charge as we go. If the org runs out of credits mid-turn, that LLM call fails and we surface the error; the turn ends. That matches how the rest of the app works and avoids over-engineering reservation logic.

---

## Frontend and API

The frontend has a chat panel (message list, input, model/tools settings), **tool-call cards** (approve/reject per call, with expandable arguments), a **thinking block** (collapsible, with optional live timer), and a **thread dropdown** (list threads, create, load, delete). When the backend returns a `turn_id` and pending tool_calls, the UI shows the cards and disables send until the user approves or rejects. The same agent is exposed over REST so custom UIs or automation can call **POST /chat** (and **POST /chat/approve** when needed), with optional streaming and thread_id for persistence.

---

## Summary

The Document Agent is a tool-calling LLM with a **bounded loop** (LLM → optional user approval → tools → LLM again), **rich context** (document, OCR, @-mentions, working state), and **two-state model** (short-lived turn state for approval handoff, persistent threads for conversation history). Splitting read-only and read-write tools keeps approval predictable; one round per approve keeps the user in control; message sanitization keeps thread reloads valid; and working state keeps “what we just created” visible to the agent without extra round-trips. If you’re building something similar—an in-context agent that can read and write—this architecture is a solid starting point.

To use the Document Agent, open any document in [DocRouter](https://app.docrouter.ai) and open the Chat / Agent tab. For API details, see [Document Agent](/docs/document-agent/) in the docs.
