---
layout: default
title: Pilots & Engagements
subtitle: DocRouter pilots and consulting work in regulated industries
permalink: /case-studies/
---

<section class="enterprise-hero border-b border-slate-200/80 py-10 md:py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p class="enterprise-section-label mb-3">Experience</p>
        <h1 class="text-4xl md:text-5xl font-bold text-[#1a2b4c] mb-4">{{ page.title }}</h1>
        <p class="text-lg text-slate-600 max-w-2xl mx-auto">{{ page.subtitle }}</p>
    </div>
</section>

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-16">
    <main>
        <section class="mb-14">
            <p class="enterprise-section-label mb-2">DocRouter pilots</p>
            <h2 class="text-2xl font-bold text-[#1a2b4c] mb-6">Completed and exploratory pilots</h2>
            <div class="grid md:grid-cols-2 gap-6">
                {% include case-study-card.html
                    badge="Pilot"
                    title="Pilot: Insurance ACORD & Clearance Automation"
                    description="Completed DocRouter pilot with a specialty insurance wholesaler—ACORD forms and ALIS clearance workflows."
                    url="/case-studies/insurance_wholesaler/" %}
                {% include case-study-card.html
                    badge="Pilot"
                    title="Pilot: Supply Chain Trade Documents"
                    description="Pilot for bills of lading, commodity reports, and related trade documents."
                    url="/case-studies/supply-chain/" %}
            </div>
        </section>

        <section>
            <p class="enterprise-section-label mb-2">Consulting</p>
            <h2 class="text-2xl font-bold text-[#1a2b4c] mb-3">Projects for Document Processing and AI Agents</h2>
            <p class="text-slate-600 text-sm mb-6 max-w-3xl">These engagements predate or are separate from the DocRouter product. They are documented as consulting projects.</p>
            <div class="grid md:grid-cols-2 gap-6">
                {% include case-study-card.html
                    badge="Consulting"
                    title="Consulting: DME Automation Platform"
                    description="Custom healthcare document platform for a startup—precursor to DocRouter."
                    url="/case-studies/dme/" %}
                {% include case-study-card.html
                    badge="Consulting"
                    title="Consulting: Epic EHR Order Automation"
                    description="Custom Epic integration for DME order processing."
                    url="/case-studies/epic_dme_order_processing/" %}
                {% include case-study-card.html
                    badge="Consulting"
                    title="Consulting: Lab Informatics Coding Copilot"
                    description="VS Code / Claude / MCP coding agent for Starlims LIMS development."
                    url="/case-studies/starlims-copilot/" %}
                {% include case-study-card.html
                    badge="Consulting"
                    title="Consulting: Lab Informatics Support Chat"
                    description="In-product RAG support agent for Starlims—SigAgent-based AI portal."
                    url="/case-studies/starlims-chat/" %}
                {% include case-study-card.html
                    badge="Consulting"
                    title="Consulting: Koch AI Book Companion"
                    description="Multi-agent PBM book companion—memory, auth, and observability at scale."
                    url="/case-studies/koch-ai-book-companion/" %}
            </div>
        </section>

        <section class="mt-14">
            {% include enterprise-cta.html
                title="Discuss your document workflow"
                description="Schedule a demo to see how DocRouter can support your industry—or explore our solution pages for specific document types." %}
        </section>
    </main>
</div>
