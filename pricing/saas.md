---
layout: default
title: "SAAS Pricing — AI Document Processing Plans"
permalink: /pricing/saas/
description: "DocRouter SAAS pricing: Individual ($250/mo), Team ($1,000/mo), and Enterprise plans. Start with 100 free SPU credits — no commitment required to get started."
---

<section class="enterprise-hero border-b border-slate-200/80 py-10 md:py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p class="enterprise-section-label mb-3">Pricing</p>
        <h1 class="text-4xl md:text-5xl font-bold text-[#1a2b4c] mb-4">SAAS plans</h1>
        <p class="text-lg text-slate-600 max-w-2xl mx-auto">
            For HIPAA-compliant workflows, use <a href="{{ '/pricing/on-prem/' | relative_url }}" class="text-blue-600 hover:text-blue-800 no-underline font-medium">on-premises plans</a>.
        </p>
    </div>
</section>

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-16">
    <main>
        <div class="text-center">
            {% include pricing-nav.html active="saas" %}
        </div>

        <section class="mb-12">
            <div class="grid md:grid-cols-3 gap-6">
                {% capture individual_features %}
                {% include pricing-feature.html text="$0.05 per SPU" %}
                {% include pricing-feature.html text="5,000 SPUs per month" %}
                {% include pricing-feature.html text="Additional SPUs at $0.05 each" %}
                {% include pricing-feature.html text="Self-service" %}
                {% endcapture %}
                {% include pricing-plan-card.html
                    name="Individual (SAAS)"
                    price="$250"
                    period="/month"
                    features=individual_features
                    button_label="Select Plan" %}

                {% capture team_features %}
                {% include pricing-feature.html text="$0.04 per SPU" %}
                {% include pricing-feature.html text="25,000 SPUs per month" %}
                {% include pricing-feature.html text="Additional SPUs at $0.05 each" %}
                {% include pricing-feature.html text="Team collaboration features" %}
                {% include pricing-feature.html text="Self-service with support available" %}
                {% endcapture %}
                {% include pricing-plan-card.html
                    name="Team (SAAS)"
                    price="$1,000"
                    period="/month"
                    badge="Popular"
                    featured=true
                    features=team_features
                    button_label="Select Plan" %}

                {% capture enterprise_features %}
                {% include pricing-feature.html text="Custom document processing" %}
                {% include pricing-feature.html text="Dedicated support" %}
                {% include pricing-feature.html text="Custom pricing — contact sales" %}
                {% endcapture %}
                {% include pricing-plan-card.html
                    name="Enterprise (SAAS)"
                    price_label="Contact sales"
                    features=enterprise_features
                    button_label="Contact Sales" %}
            </div>
        </section>

        <section class="enterprise-info-panel mb-6">
            <h2 class="text-lg font-semibold mb-2">About SPU (Service Processing Unit)</h2>
            <p class="text-slate-600 text-sm mb-3">
                An SPU is DocRouter's billing unit. Every paid operation uses the same formula:
            </p>
            <p class="text-center font-mono text-[#1a2b4c] bg-white border border-slate-200 rounded-lg px-4 py-2 mb-3 text-sm md:text-base">
                SPUs = ceil(2 &times; estimated cloud cost &divide; price per SPU)
            </p>
            <p class="text-slate-600 text-sm mb-3">
                The factor of 2 covers infrastructure and overhead on top of raw cloud cost. A minimum floor also applies: at least 1 SPU per 25 pages for OCR and document extraction, and 1 SPU per agent LLM call. Embedded-text extraction (PyMuPDF) is free.
            </p>
            <p class="text-xs text-slate-500 italic mb-0">
                SPU rates and computation methods are subject to change. We will provide advance notice of any material changes, and updates will apply only to usage on or after the effective date.
            </p>
        </section>

        <section class="enterprise-info-panel mb-10">
            <h2 class="text-lg font-semibold mb-3">About enterprise plans</h2>
            <p class="text-slate-600 text-sm mb-0">
                Enterprise plans include configuration and dataset evaluation services. On-premises / on-VPC installations require an enterprise plan.
            </p>
        </section>

        <section class="grid md:grid-cols-2 gap-6 mb-6">
            <div class="enterprise-card p-6 md:p-8">
                <h2 class="text-lg font-semibold text-[#1a2b4c] mb-4">When to use monthly plans</h2>
                <ul class="text-slate-600 text-sm space-y-2 list-disc list-inside">
                    <li>Best for predictable monthly costs</li>
                    <li>Includes SPUs with better per-unit pricing</li>
                    <li>Collaboration features in the Team plan</li>
                </ul>
            </div>
            <div class="enterprise-card p-6 md:p-8">
                <h2 class="text-lg font-semibold text-[#1a2b4c] mb-4">When to use credits</h2>
                <ul class="text-slate-600 text-sm space-y-2 list-disc list-inside">
                    <li>Best for occasional or one-off document processing</li>
                    <li>When you have exceeded the SPUs allocated in your monthly plan</li>
                    <li>Each account starts with <strong>100 SPU credits</strong> to try DocRouter. Contact us for additional credit grants.</li>
                </ul>
            </div>
        </section>

        <section class="enterprise-card p-6 md:p-8 mb-12">
            <h2 class="text-lg font-semibold text-[#1a2b4c] mb-4">When to use enterprise plans</h2>
            <ul class="text-slate-600 text-sm space-y-2 list-disc list-inside mb-0">
                <li>Best when you require configuration and dataset evaluation services</li>
            </ul>
        </section>

        {% include enterprise-cta.html
            title="Not sure which plan is right for you?"
            description="Schedule a demo to discuss your document volume, compliance needs, and deployment options." %}
    </main>
</div>
