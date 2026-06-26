---
layout: default
title: "On-Prem Pricing — AI Document Processing Plans"
permalink: /pricing/on-prem/
description: "DocRouter on-premises / on-VPC pricing. Deploy DocRouter inside your own cloud or data center with your own LLM APIs."
---

<section class="enterprise-hero border-b border-slate-200/80 py-10 md:py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p class="enterprise-section-label mb-3">Pricing</p>
        <h1 class="text-4xl md:text-5xl font-bold text-[#1a2b4c] mb-4">On-premises plans</h1>
        <p class="text-lg text-slate-600 max-w-2xl mx-auto">
            Deploy DocRouter inside your cloud or data center with your own LLM APIs. For hosted plans, see <a href="{{ '/pricing/saas/' | relative_url }}" class="text-blue-600 hover:text-blue-800 no-underline font-medium">SAAS pricing</a>.
        </p>
    </div>
</section>

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-16">
    <main>
        <div class="text-center">
            {% include pricing-nav.html active="on-prem" %}
        </div>

        <section class="mb-12">
            <div class="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
                {% capture team_features %}
                {% include pricing-feature.html text="Up to 300,000 pages per year" %}
                {% include pricing-feature.html text="Advanced document processing" %}
                {% include pricing-feature.html text="Team collaboration features" %}
                {% include pricing-feature.html text="Free upgrades" %}
                {% include pricing-feature.html text="Basic technical support" %}
                {% include pricing-feature.html text="Developer tools" %}
                {% endcapture %}
                {% include pricing-plan-card.html
                    name="Team"
                    price="$24,000"
                    period="/year"
                    featured=true
                    features=team_features
                    button_label="Select Plan" %}

                {% capture enterprise_features %}
                {% include pricing-feature.html text="Volumes above 300,000 pages per year" %}
                {% endcapture %}
                {% include pricing-plan-card.html
                    name="Enterprise"
                    price_label="Call for pricing"
                    features=enterprise_features
                    button_label="Contact Sales" %}
            </div>
        </section>

        <section class="grid md:grid-cols-2 gap-6 mb-12">
            <div class="enterprise-card p-6 md:p-8">
                <h2 class="text-lg font-semibold text-[#1a2b4c] mb-4">Professional services</h2>
                <ul class="text-slate-600 text-sm space-y-2 list-disc list-inside">
                    <li>Configuration</li>
                    <li>Dataset evaluation</li>
                    <li>Dataset tuning</li>
                    <li>Custom integration architecture design</li>
                    <li>End-to-end implementation and deployment</li>
                    <li>Team training and knowledge transfer</li>
                </ul>
            </div>
            <div class="enterprise-card p-6 md:p-8">
                <h2 class="text-lg font-semibold text-[#1a2b4c] mb-4">System requirements</h2>
                <ul class="text-slate-600 text-sm space-y-2 list-disc list-inside">
                    <li>DocRouter runs on customer's cloud infrastructure</li>
                    <li>DocRouter uses customer's AI licensing</li>
                </ul>
            </div>
        </section>

        {% include enterprise-cta.html
            title="Not sure which plan is right for you?"
            description="Schedule a demo to discuss on-premises deployment, volume requirements, and professional services." %}
    </main>
</div>
