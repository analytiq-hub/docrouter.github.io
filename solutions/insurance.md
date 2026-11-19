---
layout: default
title: "Insurance document indexing"
description: "Index your insurance file store so claims, underwriting, and recovery workflows can retrieve and cite the original pages."
---

<section class="enterprise-hero border-b border-slate-200/80 py-10 md:py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p class="enterprise-section-label mb-3">Insurance document indexing</p>
        <h1 class="text-4xl md:text-5xl font-bold text-[#1a2b4c] mb-4">Put the right policy page in front of the agent</h1>
        <p class="text-lg text-slate-600 max-w-2xl mx-auto">A coverage review can miss an exclusion when the endorsement never reaches the agent. DocRouter indexes your insurance file store so workflows can retrieve and cite the original pages.</p>
        <p class="mt-4 font-semibold text-[#1a2b4c]">Index once. Let every agent use it.</p>
        <p class="mt-6"><a href="{{ '/solutions/' | relative_url }}" class="text-sm font-medium text-blue-600 hover:text-blue-800 no-underline">← All solutions</a></p>
    </div>
</section>

<main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-16">
    <section class="enterprise-card p-8 md:p-10 mb-12">
        <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] mb-6">From first notice to first coverage review</h2>
        <ol class="grid md:grid-cols-3 gap-6 text-slate-600">
            <li><strong class="block text-[#1a2b4c] mb-1">The loss is reported</strong>The insured reports water damage. The workflow looks up the claim and policy.</li>
            <li><strong class="block text-[#1a2b4c] mb-1">The endorsement surfaces</strong>The agent finds a water backup endorsement and cites the page in its first coverage review.</li>
            <li><strong class="block text-[#1a2b4c] mb-1">The adjuster opens the page</strong>The adjuster checks the cited language, follows up with the insured, and makes the coverage decision.</li>
        </ol>
        <div class="mt-8 rounded-lg border border-slate-200 bg-slate-50 p-5">
            <p class="text-sm font-semibold text-[#1a2b4c] mb-2">Illustrative finding</p>
            <p class="text-slate-600">Water backup coverage may apply. Confirm where the water entered.</p>
            <p class="mt-2 text-sm text-slate-600"><strong>Source:</strong> Water Backup Endorsement, page 2.<br><strong>Ask the insured:</strong> Did the water come up through a drain?</p>
        </div>
        <p class="mt-6 text-sm text-slate-600">In a consulting engagement, we deployed an Investigation Support agent that gives adjusters a cited first pass. <a href="{{ '/case-studies/investigation-support-agent/' | relative_url }}" class="text-blue-600 underline">Read the case study</a> or <a href="{% post_url 2026-11-14-investigation-support-agent-for-insurance-claims %}" class="text-blue-600 underline">explore the agent design</a>.</p>
    </section>

    <section class="enterprise-card p-8 md:p-10 mb-12">
        <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] mb-3">One index for claims, underwriting, and recovery</h2>
        <p class="text-slate-600 mb-6">Files stay in the insurer’s existing systems. Workflows built in DocRouter or on the insurer’s own platform can call the same index through an API.</p>
        <figure class="max-w-4xl mx-auto">
            <img src="{{ '/assets/images/index-once-shared-architecture.png' | relative_url }}"
                 alt="Claims, underwriting, and recovery workflows share one prepared DocRouter index instead of repeating document processing."
                 class="w-full rounded-lg border border-slate-200" loading="lazy">
            <figcaption class="mt-3 text-sm text-slate-600">A recovery workflow can reuse the same indexed policy packet that claims used.</figcaption>
        </figure>
        <p class="mt-6 text-sm"><a href="{% post_url 2026-11-16-indexing-the-insurance-document-store %}" class="text-blue-600 underline">Read how the shared index works</a></p>
    </section>

    <section class="enterprise-card p-8 md:p-10 mb-12">
        <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] mb-3">Test one claims workflow</h2>
        <p class="text-slate-600 mb-6">Start with access to the relevant files and a claims expert who can mark the pages that matter. Agree on a retrieval target before running the cases.</p>
        <ul class="grid md:grid-cols-3 gap-6 text-slate-600">
            <li><strong class="block text-[#1a2b4c] mb-1">Evidence found</strong>Which expert-marked pages did the workflow find or miss?</li>
            <li><strong class="block text-[#1a2b4c] mb-1">Reviewer corrections</strong>How often did the adjuster change a finding?</li>
            <li><strong class="block text-[#1a2b4c] mb-1">Time spent gathering evidence</strong>How does the first pass compare with the current process?</li>
        </ul>
        <p class="mt-6 text-sm text-slate-600">When you add a second workflow, measure how much document processing it can reuse.</p>
        <a href="{{ site.calendly_url }}" target="_blank" rel="noopener noreferrer"
           class="enterprise-btn-primary inline-flex mt-6 px-7 py-3.5 rounded-lg font-semibold text-base transition-colors duration-200 no-underline">
            Discuss a claims pilot
        </a>
    </section>
</main>
