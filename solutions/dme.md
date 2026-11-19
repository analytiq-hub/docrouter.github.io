---
layout: default
title: "Medical Revenue Cycle"
description: "Prepare the documents a revenue-cycle team bills from. Anesthesia records and durable medical equipment are two of the lines."
---

<section class="enterprise-hero border-b border-slate-200/80 py-10 md:py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p class="enterprise-section-label mb-3">Solutions</p>
        <h1 class="text-4xl md:text-5xl font-bold text-[#1a2b4c] mb-4">Medical Revenue Cycle</h1>
        <p class="text-lg text-slate-600 max-w-2xl mx-auto">Prepare the documents a revenue-cycle team bills from. Anesthesia records and durable medical equipment are two of the lines.</p>
        <p class="mt-6"><a href="{{ '/solutions/' | relative_url }}" class="text-sm font-medium text-blue-600 hover:text-blue-800 no-underline">← All solutions</a></p>
    </div>
</section>

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-16">
    <main>
        <section class="enterprise-card p-8 mb-12">
            <h2 class="text-2xl font-bold text-[#1a2b4c] mb-8 text-center">The revenue-cycle challenge</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <div>
                    <div class="solution-challenge-icon text-blue-600">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                    </div>
                    <h3 class="text-lg font-semibold text-[#1a2b4c] mb-2">The chart is read again</h3>
                    <p class="text-slate-600 text-sm">Eligibility, medical necessity, and the claim each start from the same records</p>
                </div>
                <div>
                    <div class="solution-challenge-icon text-blue-600">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                    </div>
                    <h3 class="text-lg font-semibold text-[#1a2b4c] mb-2">Two different lines</h3>
                    <p class="text-slate-600 text-sm">An anesthesia record and a DME order ask for different documents, and the same kind of proof</p>
                </div>
                <div>
                    <div class="solution-challenge-icon text-blue-600">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    </div>
                    <h3 class="text-lg font-semibold text-[#1a2b4c] mb-2">Payment waits on the file</h3>
                    <p class="text-slate-600 text-sm">A missing record delays the claim, the authorization, or the equipment</p>
                </div>
            </div>
        </section>

        <section class="enterprise-band rounded-xl p-8 md:p-10 mb-12">
            <div class="text-center mb-8">
                <h2 class="text-2xl md:text-3xl font-bold mb-3">Two lines, one document job</h2>
                <p class="text-slate-300 max-w-2xl mx-auto">DocRouter reads the records the claim depends on and keeps the supporting page attached.</p>
            </div>
            <div class="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
                <div class="enterprise-band-card">
                    <h3 class="text-lg font-semibold text-white mb-3">Anesthesia</h3>
                    <ul class="space-y-2 text-sm">
                        <li>Anesthesia records and operative notes</li>
                        <li>Charge tickets and time documentation</li>
                        <li>Eligibility and coverage support</li>
                        <li>The page a biller cites on the claim</li>
                    </ul>
                    <a href="{{ '/case-studies/boston-medical-data/' | relative_url }}"
                       class="inline-block mt-4 text-sm font-semibold text-white underline hover:text-blue-200">
                        Read the Boston Medical Data case study →
                    </a>
                </div>
                <div class="enterprise-band-card">
                    <h3 class="text-lg font-semibold text-white mb-3">Durable medical equipment</h3>
                    <ul class="space-y-2 text-sm">
                        <li>Orders and prescriptions</li>
                        <li>Medical necessity documentation</li>
                        <li>Prior authorization forms</li>
                        <li>Patient information and eligibility</li>
                    </ul>
                    <div class="mt-4 flex flex-col items-start gap-2">
                        <a href="{{ '/case-studies/dme/' | relative_url }}"
                           class="text-sm font-semibold text-white underline hover:text-blue-200">
                            Read the Ashvin AI case study →
                        </a>
                        <a href="{{ '/case-studies/epic_dme_order_processing/' | relative_url }}"
                           class="text-sm font-semibold text-white underline hover:text-blue-200">
                            Read the Epic EHR order automation case study →
                        </a>
                    </div>
                </div>
            </div>
        </section>

        {% include solution-related-docs.html
            quick_start="Set up extraction for an anesthesia record or a DME order"
            schemas="Define fields for records, prescriptions, CMNs, and authorization forms"
            knowledge="Store and query coverage policies and eligibility requirements"
            workflows="Move a record from the chart to eligibility, authorization, and the claim" %}

        {% include enterprise-cta.html
            title="Ready to prepare the documents behind the claim?"
            description="Schedule a demo to discuss anesthesia or durable medical equipment workflows—or launch the app to explore DocRouter." %}
    </main>
</div>
