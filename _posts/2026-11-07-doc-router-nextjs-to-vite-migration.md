---
layout: post
title: "From Next.js to Vite: Simplifying the Doc Router Frontend"
date: 2026-11-07 00:00:00 +0000
author: Andrei Radulescu-Banu
image: /assets/images/doc-router-nextjs-to-vite-splash.png
categories: [tech, webdev, docrouter, programming]
description: "Doc Router already ran on FastAPI. We moved the UI from Next.js to a static Vite SPA. Same look and feel, fewer moving parts."
---

[Doc Router](https://docrouter.ai) is a document AI product. **FastAPI** already owns auth, APIs, workers, and the database. The browser app is a logged-in **React** UI.

We moved that UI from **Next.js** to **Vite**. Same screens. A static build served by **nginx**. Generating code is easy. A simpler framework is still worth it: less to debug, fewer deploy paths, and more control over routing and auth.

## Architecture: Before and After

<div data-excalidraw="/assets/excalidraw/doc-router-nextjs-to-vite-architecture.excalidraw" class="excalidraw-container">
  <div class="loading-placeholder">Loading diagram...</div>
</div>

<p style="text-align: center; margin-top: 0.5rem; font-size: 0.875rem; color: #6b7280;">
  <strong>Figure 1:</strong> Before and after the Next.js → Vite migration.
</p>

The browser used to reach the Next.js UI, the Next.js server, and FastAPI. Now it reaches a static SPA and FastAPI, and only FastAPI talks to the database.

## What We Replaced (at a Glance)

<div class="overflow-x-auto my-6">
<table class="min-w-full text-sm border border-gray-200 rounded-lg overflow-hidden">
  <thead class="bg-slate-100">
    <tr>
      <th class="text-left p-3 font-semibold">Next.js</th>
      <th class="text-left p-3 font-semibold">Vite + React Router</th>
    </tr>
  </thead>
  <tbody class="divide-y divide-gray-200">
    <tr><td class="p-3">File-based routes</td><td class="p-3">React Router</td></tr>
    <tr class="bg-slate-50"><td class="p-3">Next image and dynamic import</td><td class="p-3">A normal image and lazy loading</td></tr>
    <tr><td class="p-3">API routes and a Node session</td><td class="p-3">A FastAPI session cookie</td></tr>
    <tr class="bg-slate-50"><td class="p-3">A Node server in production</td><td class="p-3">Static files on nginx</td></tr>
    <tr><td class="p-3"><code>NEXT_PUBLIC_*</code> env vars</td><td class="p-3"><code>VITE_*</code> env vars</td></tr>
  </tbody>
</table>
</div>

## Same Look and Feel

We kept **MUI**, **Tailwind**, **Form.io**, and the same screens.

<img src="/assets/images/doc-router-ui-vite.png" alt="The Doc Router flows editor after the Vite migration" style="width: 100%; max-width: 960px; margin: 1.5rem auto; display: block; border: 1px solid #e2e8f0; border-radius: 8px;">

<p style="text-align: center; margin-top: 0.5rem; font-size: 0.875rem; color: #6b7280;">The flows editor, unchanged.</p>

## How We Migrated (Short Version)

1. **Backend first** — moved all the Next.js server APIs to FastAPI.
2. **Vite side by side with Next.js.**
3. **Route parity** — same URLs, now in React Router.
4. **Remove Next.** CI and Docker build Vite only.
5. **Cleanup.**

The port took **two days**: about **18k** lines touched across **258** files.

The code migration was done in Cursor with **Composer 2.5 Fast**. This post was written with **Grok**, the latest Grok coding model.

## Unit Tests

About **1,400** backend unit tests and **180** frontend unit tests stayed in place. They cover login, documents, flows, and the UI. The frontend could change. The API did not.

## Conclusion: When to Pick Which Front End

| You want… | Consider |
|-----------|----------|
| SSR, SEO, file-based app + server components | **Next.js** |
| API already in Python/Go/etc., static deploy, cookie session API | **Vite + React Router** |

Doc Router fits Vite and React because FastAPI already handles auth, APIs, and the database. The Doc Router UI only has to be a static React app.

<style>
.excalidraw-container {
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  background: white;
  display: block;
  margin: 2rem 0;
  min-height: 420px;
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
