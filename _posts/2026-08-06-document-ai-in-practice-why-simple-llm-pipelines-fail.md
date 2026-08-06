---
layout: post
title: "Document AI in Practice: Why Simple LLM Pipelines Fail"
date: 2026-08-06 00:00:00 +0000
author: "Andrei Radulescu-Banu"
image: /assets/images/document-ai-in-practice-splash.png
categories: [ai, engineering]
description: "Uploading a PDF to an LLM is easy. Building reliable document AI is not. The first edition of Document AI in Practice explores why simple pipelines fail when documents become large, messy, and operationally important."
---

<div class="not-prose space-y-14 text-slate-700 text-base leading-relaxed">

  <p class="text-lg md:text-xl text-slate-600 leading-relaxed max-w-3xl">
    Why simple LLM pipelines often fail when documents become large, messy, and operationally important—and how production systems are designed differently.
  </p>

  <!-- Section 1 -->
  <section class="space-y-5">
    <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] leading-tight tracking-tight">
      Uploading a PDF to an LLM is easy.<br class="hidden sm:block" />
      <span class="text-blue-600">Building reliable document AI is not.</span>
    </h2>

    <p>
      Almost every major language model now allows users to attach a PDF or Microsoft Word document and ask questions about it. That creates the impression that document processing has become simple:
    </p>

    <ol class="list-decimal pl-5 m-0 space-y-1 text-sm">
      <li>Upload a document</li>
      <li>Write a prompt</li>
      <li>Receive structured results</li>
    </ol>

    <p>
      For a short, clean document and a one-time task, that may be enough. At production scale, document processing becomes a much more complicated engineering problem. The central question is no longer simply:
    </p>

    <blockquote class="m-0 mx-auto border-l-4 border-blue-500 bg-slate-50 rounded-r-lg px-8 py-4 text-slate-700 italic" style="max-width: 36rem;">
      Can a language model read this document?
    </blockquote>

    <p class="font-medium text-[#1a2b4c]">The more useful questions are:</p>

    <ul class="grid sm:grid-cols-2 gap-x-8 gap-y-1 list-disc pl-5 m-0 text-sm">
      <li>Which model should process it?</li>
      <li>How much will processing cost?</li>
      <li>Can the entire document fit into the model's context?</li>
      <li>Does it contain handwriting, tables, images, or unusual formatting?</li>
      <li>Is it written in another language or script?</li>
      <li>Does processing require several steps?</li>
      <li>Do results need checking against an external system?</li>
      <li>What happens when the model is uncertain or wrong?</li>
    </ul>

    <figure class="m-0">
      <img
        src="{{ '/assets/images/document-ai-useful-questions.png' | relative_url }}"
        alt="The useful questions in document AI — a decision framework"
        class="w-full rounded-xl border border-slate-200 shadow-sm"
      />
      <figcaption class="mt-2 text-center text-sm text-slate-500">
        The useful questions in document AI — a decision framework
      </figcaption>
    </figure>
  </section>

  <!-- Section 2 -->
  <section class="space-y-5">
    <p class="enterprise-section-label mb-0">Model selection</p>
    <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] leading-tight tracking-tight mt-1">
      Different models have different strengths
    </h2>

    <p>
      Language models are not interchangeable. Some are especially strong conversational assistants. Others are optimized for coding, reasoning, speed, multilingual work, or visual understanding.
    </p>

    <p>
      A model that performs extremely well on software-development tasks may not be the best choice for extracting information from a complex insurance packet. A strong general-purpose conversational model may struggle with dense tables, handwritten notes, low-quality scans, or unfamiliar document layouts.
    </p>

    <p class="font-medium text-[#1a2b4c]">Document-processing quality can depend on many factors:</p>

    <ul class="grid sm:grid-cols-2 gap-x-8 gap-y-1 list-disc pl-5 m-0 text-sm">
      <li>The type of document</li>
      <li>The quality of the scan</li>
      <li>The number of pages</li>
      <li>The complexity of the layout</li>
      <li>The language used</li>
      <li>The expected output</li>
      <li>The amount of reasoning required</li>
      <li>The model's visual and OCR capabilities</li>
    </ul>

    <figure class="m-0">
      <img
        src="{{ '/assets/images/document-ai-quality-factors.png' | relative_url }}"
        alt="What affects document-processing quality?"
        class="w-full rounded-xl border border-slate-200 shadow-sm"
      />
      <figcaption class="mt-2 text-center text-sm text-slate-500">
        What affects document-processing quality?
      </figcaption>
    </figure>

    <p>
      Choosing a model should be treated as an evaluation problem, not as a matter of brand preference.
    </p>

    <aside class="flex gap-3 items-start rounded-xl bg-amber-50 px-4 py-4 ring-1 ring-amber-100">
      <span class="flex-shrink-0 mt-0.5 w-9 h-9 rounded-full bg-amber-100 text-amber-700 flex items-center justify-center" aria-hidden="true">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.75" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
        </svg>
      </span>
      <p class="m-0 pt-1.5 text-[#1a2b4c] font-semibold leading-snug">The best model is the one that performs reliably on your actual documents and your actual extraction requirements.</p>
    </aside>
  </section>

  <!-- Section 3 -->
  <section class="space-y-5">
    <p class="enterprise-section-label mb-0">Cost at scale</p>
    <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] leading-tight tracking-tight mt-1">
      Quality is only half of the equation
    </h2>

    <p>
      The highest-quality model is not always the right model. Document processing at scale can become expensive. A workflow that looks inexpensive when tested on ten documents may become costly when it processes hundreds of thousands of pages.
    </p>

    <p class="font-medium text-[#1a2b4c]">The total cost can include:</p>

    <ul class="grid sm:grid-cols-2 gap-x-8 gap-y-1 list-disc pl-5 m-0 text-sm">
      <li>OCR</li>
      <li>Input tokens</li>
      <li>Output tokens</li>
      <li>Multiple model calls</li>
      <li>Retries</li>
      <li>Validation steps</li>
      <li>Human review</li>
      <li>Data storage</li>
      <li>Workflow infrastructure</li>
    </ul>

    <figure class="m-0">
      <img
        src="{{ '/assets/images/document-ai-cost-at-scale.png' | relative_url }}"
        alt="What drives document-processing cost at scale?"
        class="w-full rounded-xl border border-slate-200 shadow-sm"
      />
      <figcaption class="mt-2 text-center text-sm text-slate-500">
        What drives document-processing cost at scale?
      </figcaption>
    </figure>

    <p>
      A more capable model may require fewer retries and less human review. A cheaper model may work perfectly well for straightforward classification or extraction tasks.
    </p>

    <aside class="flex gap-3 items-start rounded-xl bg-amber-50 px-4 py-4 ring-1 ring-amber-100">
      <span class="flex-shrink-0 mt-0.5 w-9 h-9 rounded-full bg-amber-100 text-amber-700 flex items-center justify-center" aria-hidden="true">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.75" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
        </svg>
      </span>
      <p class="m-0 pt-1.5 text-[#1a2b4c] font-semibold leading-snug">Select the least expensive architecture that produces results at the required level of quality.</p>
    </aside>

    <p>That architecture may use one model for every document. More often, it uses several:</p>

    <ul class="grid sm:grid-cols-2 gap-x-8 gap-y-3 list-disc pl-5 m-0 text-sm">
      <li>
        <span class="font-semibold text-[#1a2b4c]">Fast, inexpensive model</span>
        <span class="block text-slate-600">Classification and straightforward routing</span>
      </li>
      <li>
        <span class="font-semibold text-[#1a2b4c]">Specialized OCR</span>
        <span class="block text-slate-600">Scanned pages and layout-heavy forms</span>
      </li>
      <li>
        <span class="font-semibold text-[#1a2b4c]">Stronger reasoning model</span>
        <span class="block text-slate-600">Difficult cases and dense packets</span>
      </li>
      <li>
        <span class="font-semibold text-[#1a2b4c]">Human reviewer</span>
        <span class="block text-slate-600">Uncertain or high-stakes results</span>
      </li>
    </ul>
  </section>

  <!-- Section 4 -->
  <section class="space-y-5">
    <p class="enterprise-section-label mb-0">Large packets</p>
    <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] leading-tight tracking-tight mt-1">
      Large documents require orchestration
    </h2>

    <div class="grid sm:grid-cols-2 gap-4">
      <div class="rounded-xl border border-slate-200 bg-slate-50 p-5">
        <p class="text-xs font-semibold uppercase tracking-wide text-slate-500 mb-2">Simple case</p>
        <p class="text-lg font-bold text-[#1a2b4c] mb-1">10-page PDF</p>
        <p class="text-sm text-slate-600 m-0">Often processed in a single request</p>
      </div>
      <div class="rounded-xl border border-blue-200 bg-blue-50/60 p-5">
        <p class="text-xs font-semibold uppercase tracking-wide text-blue-600 mb-2">Production case</p>
        <p class="text-lg font-bold text-[#1a2b4c] mb-1">500-page packet</p>
        <p class="text-sm text-slate-600 m-0">Medical, legal, financial, or insurance—needs a workflow</p>
      </div>
    </div>

    <p>
      Even when a model supports a very large context window, passing the entire document in one request may not produce the best results. Important information may be scattered across hundreds of pages. Sections may need to be classified, separated, summarized, compared, or reconciled.
    </p>

    <p class="font-medium text-[#1a2b4c]">A large-document workflow might need to:</p>

    <ol class="grid sm:grid-cols-2 gap-x-8 gap-y-1 list-decimal pl-5 m-0 text-sm">
      <li>Split the packet into logical sections</li>
      <li>Classify each section</li>
      <li>Route each document type to a specialized processor</li>
      <li>Extract structured data</li>
      <li>Compare information across documents</li>
      <li>Identify contradictions or missing information</li>
      <li>Reconcile the results into a final output</li>
    </ol>

    <p>This is not a single prompt. It is an orchestrated workflow.</p>

    <figure class="m-0">
      <img
        src="{{ '/assets/images/document-ai-large-document-orchestration.png' | relative_url }}"
        alt="Why large documents require orchestration"
        class="w-full rounded-xl border border-slate-200 shadow-sm"
      />
      <figcaption class="mt-2 text-center text-sm text-slate-500">
        Why large documents require orchestration
      </figcaption>
    </figure>

    <p>
      Some models and platforms provide internal agentic capabilities that can perform several actions iteratively. In other cases, the surrounding application must manage the steps, preserve state, call tools, handle failures, and combine the outputs.
    </p>

    <aside class="flex gap-3 items-start rounded-xl bg-amber-50 px-4 py-4 ring-1 ring-amber-100">
      <span class="flex-shrink-0 mt-0.5 w-9 h-9 rounded-full bg-amber-100 text-amber-700 flex items-center justify-center" aria-hidden="true">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.75" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
        </svg>
      </span>
      <p class="m-0 pt-1.5 text-[#1a2b4c] font-semibold leading-snug">The orchestration layer becomes just as important as the model itself.</p>
    </aside>
  </section>

  <!-- Section 5 -->
  <section class="space-y-5">
    <p class="enterprise-section-label mb-0">Messy inputs</p>
    <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] leading-tight tracking-tight mt-1">
      Not every page is machine-readable
    </h2>

    <p>Real-world documents are messy. They may contain:</p>

    <ul class="grid sm:grid-cols-2 gap-x-8 gap-y-1 list-disc pl-5 m-0 text-sm">
      <li>Handwriting</li>
      <li>Fax artifacts</li>
      <li>Rotated pages</li>
      <li>Stamps</li>
      <li>Signatures</li>
      <li>Checkboxes</li>
      <li>Tables</li>
      <li>Embedded images</li>
      <li>Low-resolution scans</li>
      <li>Multiple documents combined into one packet</li>
    </ul>

    <p>
      Language models can often interpret many of these elements, but performance varies. Handwriting is particularly challenging, especially when the scan quality is poor or the writing is highly individual.
    </p>

    <p class="font-medium text-[#1a2b4c]">The right approach often combines several technologies:</p>

    <ul class="grid sm:grid-cols-2 gap-x-8 gap-y-1 list-disc pl-5 m-0 text-sm">
      <li>Traditional OCR</li>
      <li>Handwriting recognition</li>
      <li>Layout detection</li>
      <li>Computer vision</li>
      <li>Multimodal language models</li>
      <li>Human verification</li>
    </ul>

    <figure class="m-0">
      <img
        src="{{ '/assets/images/document-ai-messy-pages.png' | relative_url }}"
        alt="Not every page is machine-readable"
        class="w-full rounded-xl border border-slate-200 shadow-sm"
      />
      <figcaption class="mt-2 text-center text-sm text-slate-500">
        Not every page is machine-readable
      </figcaption>
    </figure>

    <aside class="flex gap-3 items-start rounded-xl bg-amber-50 px-4 py-4 ring-1 ring-amber-100">
      <span class="flex-shrink-0 mt-0.5 w-9 h-9 rounded-full bg-amber-100 text-amber-700 flex items-center justify-center" aria-hidden="true">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.75" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
        </svg>
      </span>
      <p class="m-0 pt-1.5 text-[#1a2b4c] font-semibold leading-snug">The language model does not need to solve every problem by itself.</p>
    </aside>
  </section>

  <!-- Section 6 -->
  <section class="space-y-5">
    <p class="enterprise-section-label mb-0">Global operations</p>
    <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] leading-tight tracking-tight mt-1">
      Language and script matter
    </h2>

    <p>
      Global document-processing systems must also handle multilingual content. A model may perform well in English but produce weaker results in another language. Performance can vary further when documents use non-Latin scripts or mix several languages on the same page.
    </p>

    <p class="font-medium text-[#1a2b4c]">The system may need to determine:</p>

    <ul class="grid sm:grid-cols-2 gap-x-8 gap-y-1 list-disc pl-5 m-0 text-sm">
      <li>What language is present</li>
      <li>Whether multiple languages are used</li>
      <li>Whether translation is required</li>
      <li>Whether to extract before or after translation</li>
      <li>Which model performs best for that language</li>
      <li>Whether original text must be preserved for audit</li>
    </ul>

    <figure class="m-0">
      <img
        src="{{ '/assets/images/document-ai-language-and-script.png' | relative_url }}"
        alt="Language and script matter"
        class="w-full rounded-xl border border-slate-200 shadow-sm"
      />
      <figcaption class="mt-2 text-center text-sm text-slate-500">
        Language and script matter
      </figcaption>
    </figure>

    <p>
      Multilingual processing should be tested by language, document type, and script—not assumed from a model's general language-support claims.
    </p>
  </section>

  <!-- Section 7 -->
  <section class="space-y-5">
    <p class="enterprise-section-label mb-0">Workflow design</p>
    <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] leading-tight tracking-tight mt-1">
      Many document tasks require multiple steps
    </h2>

    <p>A document-processing task may sound simple:</p>

    <blockquote class="m-0 mx-auto border-l-4 border-blue-500 bg-slate-50 rounded-r-lg px-8 py-4 text-slate-700 italic" style="max-width: 36rem;">
      Review insurance claim, and validate policy coverage.
    </blockquote>

    <p class="font-medium text-[#1a2b4c]">A production workflow may require much more:</p>

    <ol class="grid sm:grid-cols-2 gap-x-8 gap-y-1 list-decimal pl-5 m-0 text-sm">
      <li>Identify the document type</li>
      <li>Locate the relevant section</li>
      <li>Extract the requested fields</li>
      <li>Normalize names and dates</li>
      <li>Validate required values</li>
      <li>Compare the information with another document</li>
      <li>Check the result against a database</li>
      <li>Flag discrepancies for review</li>
      <li>Save the result in a downstream system</li>
    </ol>

    <p>Each step may use a different model, rule, service, or external tool.</p>

    <figure class="m-0">
      <img
        src="{{ '/assets/images/document-ai-multi-step-workflows.png' | relative_url }}"
        alt="Many document tasks require multiple steps"
        class="w-full rounded-xl border border-slate-200 shadow-sm"
      />
      <figcaption class="mt-2 text-center text-sm text-slate-500">
        Many document tasks require multiple steps
      </figcaption>
    </figure>

    <aside class="flex gap-3 items-start rounded-xl bg-amber-50 px-4 py-4 ring-1 ring-amber-100">
      <span class="flex-shrink-0 mt-0.5 w-9 h-9 rounded-full bg-amber-100 text-amber-700 flex items-center justify-center" aria-hidden="true">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.75" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
        </svg>
      </span>
      <p class="m-0 pt-1.5 text-[#1a2b4c] font-semibold leading-snug">Document AI should be viewed as workflow design rather than prompt design.</p>
    </aside>
  </section>

  <!-- Section 8 -->
  <section class="space-y-5">
    <p class="enterprise-section-label mb-0">Systems integration</p>
    <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] leading-tight tracking-tight mt-1">
      External tools are often essential
    </h2>

    <p>
      Language models process the information placed in their context, but many business decisions depend on information outside the document. For example, the workflow may need to:
    </p>

    <ul class="grid sm:grid-cols-2 gap-x-8 gap-y-1 list-disc pl-5 m-0 text-sm">
      <li>Verify a customer against a database</li>
      <li>Confirm that an identifier exists</li>
      <li>Retrieve an insurance policy</li>
      <li>Check a payment amount</li>
      <li>Compare a document against a contract</li>
      <li>Validate an address</li>
      <li>Look up historical records</li>
      <li>Update a claims or case-management system</li>
    </ul>

    <p>
      The model must therefore be able to interact with external tools and systems. That introduces additional engineering requirements:
    </p>

    <ul class="grid sm:grid-cols-2 gap-x-8 gap-y-1 list-disc pl-5 m-0 text-sm">
      <li>Authentication</li>
      <li>Permissions</li>
      <li>Error handling</li>
      <li>Audit trails</li>
      <li>Data validation</li>
      <li>Retry logic</li>
      <li>Human approval</li>
    </ul>

    <p>
      A useful document-processing platform must coordinate both unstructured documents and structured systems.
    </p>
  </section>

  <!-- Section 9 -->
  <section class="space-y-5">
    <p class="enterprise-section-label mb-0">DocRouter</p>
    <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] leading-tight tracking-tight mt-1">
      One platform, many processing paths
    </h2>

    <p>
      DocRouter is designed around the idea that no single model, cloud, or processing pattern is right for every document. It integrates with multiple cloud providers, OCR systems, and language models. A workflow can use a direct, single-shot model call for a simple task or a multi-step process for a large and complex document packet.
    </p>

    <p class="font-medium text-[#1a2b4c]">DocRouter workflows can include:</p>

    <ul class="grid sm:grid-cols-2 gap-x-8 gap-y-1 list-disc pl-5 m-0 text-sm">
      <li>Document classification</li>
      <li>OCR</li>
      <li>Structured extraction</li>
      <li>Multi-model routing</li>
      <li>Agents</li>
      <li>External tools</li>
      <li>Database validation</li>
      <li>Branching logic</li>
      <li>Human review</li>
      <li>Final reconciliation</li>
    </ul>

    <figure class="m-0">
      <img
        src="{{ '/assets/images/document-ai-docrouter-approach.png' | relative_url }}"
        alt="DocRouter orchestration: multi-model routing, tools, and human review"
        class="w-full rounded-xl border border-slate-200 shadow-sm"
      />
      <figcaption class="mt-2 text-center text-sm text-slate-500">
        DocRouter orchestration: multi-model routing, tools, and human review
      </figcaption>
    </figure>

    <p>
      This flexibility makes it possible to start with a straightforward pipeline and add more sophisticated processing only where it is needed.
    </p>

    <div class="grid sm:grid-cols-3 gap-3">
      <div class="rounded-xl border border-emerald-200 bg-emerald-50/70 p-4">
        <p class="text-xs font-semibold uppercase tracking-wide text-emerald-700 mb-1">Simple document</p>
        <p class="text-sm text-slate-700 m-0">Passes through automatically</p>
      </div>
      <div class="rounded-xl border border-blue-200 bg-blue-50/70 p-4">
        <p class="text-xs font-semibold uppercase tracking-wide text-blue-700 mb-1">Difficult document</p>
        <p class="text-sm text-slate-700 m-0">Routed to a stronger model</p>
      </div>
      <div class="rounded-xl border border-amber-200 bg-amber-50/70 p-4">
        <p class="text-xs font-semibold uppercase tracking-wide text-amber-700 mb-1">Low confidence</p>
        <p class="text-sm text-slate-700 m-0">Sent to a human reviewer</p>
      </div>
    </div>

    <p>
      The goal is not to place a human in every workflow. It is to involve a human only when automation cannot produce a sufficiently reliable result.
    </p>
  </section>

  <!-- Section 10 -->
  <section class="space-y-5">
    <p class="enterprise-section-label mb-0">Architecture</p>
    <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] leading-tight tracking-tight mt-1">
      Flexibility is the real requirement
    </h2>

    <p>
      Document AI is evolving quickly. Models improve, prices change, new OCR systems appear, and customer requirements become more sophisticated. A production system must therefore make it easy to:
    </p>

    <ul class="grid sm:grid-cols-2 gap-x-8 gap-y-1 list-disc pl-5 m-0 text-sm">
      <li>Define new workflows</li>
      <li>Test alternative models</li>
      <li>Compare cost and quality</li>
      <li>Add processing steps</li>
      <li>Integrate external systems</li>
      <li>Review difficult cases</li>
      <li>Move workflows into production</li>
      <li>Replace components without rebuilding everything</li>
    </ul>

    <aside class="flex gap-3 items-start rounded-xl bg-amber-50 px-4 py-4 ring-1 ring-amber-100">
      <span class="flex-shrink-0 mt-0.5 w-9 h-9 rounded-full bg-amber-100 text-amber-700 flex items-center justify-center" aria-hidden="true">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.75" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
        </svg>
      </span>
      <p class="m-0 pt-1.5 text-[#1a2b4c] font-semibold leading-snug">The winning architecture is the one that can adapt when the best model changes tomorrow.</p>
    </aside>
  </section>

  <!-- Closing -->
  <section class="space-y-5">
    <p class="enterprise-section-label mb-0">Production capabilities</p>
    <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] leading-tight tracking-tight mt-1">
      What DocRouter.AI solves
    </h2>

    <p>
      These are not open research questions for us. They are the problems DocRouter.AI was built to address in production:
    </p>

    <ul class="grid sm:grid-cols-2 gap-x-8 gap-y-2 list-none p-0 m-0 text-sm">
      <li class="flex gap-2 items-start">
        <span class="text-emerald-600 font-bold flex-shrink-0" aria-hidden="true">✓</span>
        <span>Evaluate language models on real documents—not vendor benchmarks</span>
      </li>
      <li class="flex gap-2 items-start">
        <span class="text-emerald-600 font-bold flex-shrink-0" aria-hidden="true">✓</span>
        <span>Choose OCR or a multimodal model based on the page, not a single default</span>
      </li>
      <li class="flex gap-2 items-start">
        <span class="text-emerald-600 font-bold flex-shrink-0" aria-hidden="true">✓</span>
        <span>Process packets with hundreds of pages through orchestrated workflows</span>
      </li>
      <li class="flex gap-2 items-start">
        <span class="text-emerald-600 font-bold flex-shrink-0" aria-hidden="true">✓</span>
        <span>Compare quality, latency, and cost across models and pipelines</span>
      </li>
      <li class="flex gap-2 items-start">
        <span class="text-emerald-600 font-bold flex-shrink-0" aria-hidden="true">✓</span>
        <span>Build reliable multi-step workflows with branching, tools, and state</span>
      </li>
      <li class="flex gap-2 items-start">
        <span class="text-emerald-600 font-bold flex-shrink-0" aria-hidden="true">✓</span>
        <span>Use human review only for uncertain or high-stakes results</span>
      </li>
      <li class="flex gap-2 items-start">
        <span class="text-emerald-600 font-bold flex-shrink-0" aria-hidden="true">✓</span>
        <span>Validate model output against external systems before it becomes a business decision</span>
      </li>
    </ul>

    <div class="rounded-xl bg-[#1a2b4c] text-white px-6 py-5 space-y-2">
      <p class="m-0 text-slate-200">
        Document AI is no longer limited by whether a model can read a PDF.
      </p>
      <p class="m-0 font-semibold text-white">
        With DocRouter.AI, you can process diverse documents reliably, economically, and at scale.
      </p>
    </div>

    <div class="flex flex-col sm:flex-row gap-3 pt-2 justify-center">
      <a href="{{ site.calendly_url }}"
         target="_blank"
         rel="noopener noreferrer"
         class="enterprise-btn-primary inline-flex items-center justify-center px-6 py-3 rounded-lg font-semibold text-sm no-underline">
        Schedule a demo
      </a>
      <a href="{{ '/assets/files/document-ai-in-practice-why-simple-llm-pipelines-fail.pdf' | relative_url }}"
         class="enterprise-btn-secondary inline-flex items-center justify-center px-6 py-3 rounded-lg font-semibold text-sm no-underline">
        Download the white paper
      </a>
    </div>
  </section>

</div>
