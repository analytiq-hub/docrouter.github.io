---
layout: default
title: "DocRouter.AI — AI Data Layer for Operational Documents"
description: "DocRouter is the AI data layer for operational documents. Extract structured data from invoices, manifests, insurance forms, and more—cut manual data entry by 90% and processing errors by 95%."
image: /assets/images/og-default.png
---

<!-- Hero -->
<section class="enterprise-hero border-b border-slate-200/80">
    <div class="enterprise-hero-ring w-96 h-96 -top-20 -right-20 hidden lg:block" aria-hidden="true"></div>
    <div class="enterprise-hero-ring w-64 h-64 top-1/2 -left-16 hidden lg:block" aria-hidden="true"></div>

    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-20">
        <div class="grid lg:grid-cols-2 gap-10 lg:gap-16 items-center">
            <div class="text-left">
                <p class="enterprise-section-label mb-4">Enterprise document intelligence</p>
                <h1 class="text-4xl md:text-5xl lg:text-[3.25rem] font-bold text-[#1a2b4c] mb-5 leading-tight tracking-tight">
                    AI data layer for
                    <span class="text-blue-600">operational documents</span>
                </h1>
                <p class="text-lg md:text-xl text-slate-600 mb-8 max-w-xl leading-relaxed">
                    Extract, validate, and route structured data from invoices, manifests, ACORD forms, and any document—at enterprise scale.
                </p>
                <div class="flex flex-col sm:flex-row gap-3 mb-10">
                    <a href="{{ site.calendly_url }}"
                       target="_blank"
                       rel="noopener noreferrer"
                       class="enterprise-btn-primary inline-flex items-center justify-center px-7 py-3.5 rounded-lg font-semibold text-base transition-colors duration-200 no-underline">
                        Schedule a Demo
                    </a>
                    <a href="{{ '/docs/how-it-works/' | relative_url }}"
                       class="enterprise-btn-secondary inline-flex items-center justify-center px-7 py-3.5 rounded-lg font-semibold text-base transition-colors duration-200 no-underline">
                        View Documentation
                    </a>
                </div>
                <div class="flex flex-wrap items-center gap-6 pt-2 border-t border-slate-200/80">
                    <span class="text-sm text-slate-500 font-medium">Member of</span>
                    <img src="{{ '/assets/images/mit_startup_exchage.png' | relative_url }}" alt="MIT Startup Exchange" class="h-10 w-auto object-contain opacity-90" />
                    <img src="{{ '/assets/images/nvidia_inception.png' | relative_url }}" alt="NVIDIA Inception" class="h-10 w-auto object-contain opacity-90" />
                </div>
            </div>
            <div class="relative">
                <div class="rounded-xl border border-slate-200 bg-white p-2 shadow-lg shadow-slate-900/5">
                    <img src="{{ '/assets/images/doc_router_user_experience.png' | relative_url }}"
                         alt="DocRouter document processing platform"
                         class="w-full h-auto rounded-lg" />
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Document pipeline (LinkedIn brand journey) -->
<section class="bg-white border-b border-slate-200/80 py-10 md:py-14">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <p class="text-center text-slate-600 mb-8 max-w-2xl mx-auto">
            From raw documents to structured data in your systems
        </p>
        <div class="flex flex-col md:flex-row items-center justify-between gap-6 md:gap-4">
            <div class="flex flex-col items-center text-center flex-1">
                <div class="enterprise-icon-tile w-14 h-14 flex items-center justify-center mb-3">
                    <svg class="w-7 h-7 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                    </svg>
                </div>
                <span class="text-sm font-semibold text-[#1a2b4c]">Ingest</span>
                <span class="text-xs text-slate-500 mt-1">PDFs, faxes, email</span>
            </div>
            <div class="hidden md:block enterprise-pipeline-line flex-1 max-w-[4rem]" aria-hidden="true"></div>
            <div class="flex flex-col items-center text-center flex-1">
                <div class="enterprise-icon-tile w-14 h-14 flex items-center justify-center mb-3">
                    <svg class="w-7 h-7 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/>
                    </svg>
                </div>
                <span class="text-sm font-semibold text-[#1a2b4c]">Classify</span>
                <span class="text-xs text-slate-500 mt-1">Tags &amp; schemas</span>
            </div>
            <div class="hidden md:block enterprise-pipeline-line flex-1 max-w-[4rem]" aria-hidden="true"></div>
            <div class="flex flex-col items-center text-center flex-1">
                <div class="enterprise-icon-tile w-14 h-14 flex items-center justify-center mb-3">
                    <svg class="w-7 h-7 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/>
                    </svg>
                </div>
                <span class="text-sm font-semibold text-[#1a2b4c]">Extract</span>
                <span class="text-xs text-slate-500 mt-1">AI-powered fields</span>
            </div>
            <div class="hidden md:block enterprise-pipeline-line flex-1 max-w-[4rem]" aria-hidden="true"></div>
            <div class="flex flex-col items-center text-center flex-1">
                <div class="enterprise-icon-tile w-14 h-14 flex items-center justify-center mb-3">
                    <svg class="w-7 h-7 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/>
                    </svg>
                </div>
                <span class="text-sm font-semibold text-[#1a2b4c]">Integrate</span>
                <span class="text-xs text-slate-500 mt-1">APIs &amp; webhooks</span>
            </div>
        </div>
    </div>
</section>

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-16">
    <main>

        <!-- Platform capabilities -->
        <section class="mb-16 md:mb-20">
            <div class="text-center mb-10">
                <p class="enterprise-section-label mb-3">Platform</p>
                <h2 class="text-3xl md:text-4xl font-bold text-[#1a2b4c] mb-4">Built for operational scale</h2>
                <p class="text-lg text-slate-600 max-w-2xl mx-auto">
                    Everything you need to turn document chaos into reliable, structured data pipelines.
                </p>
            </div>
            <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="enterprise-card p-6">
                    <div class="w-10 h-10 rounded-lg bg-blue-50 flex items-center justify-center mb-4">
                        <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                    </div>
                    <h3 class="text-lg font-semibold text-[#1a2b4c] mb-2">Extract</h3>
                    <p class="text-slate-600 text-sm leading-relaxed">Pull structured fields from any document type with schema-driven AI extraction.</p>
                </div>
                <div class="enterprise-card p-6">
                    <div class="w-10 h-10 rounded-lg bg-blue-50 flex items-center justify-center mb-4">
                        <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                    </div>
                    <h3 class="text-lg font-semibold text-[#1a2b4c] mb-2">Validate</h3>
                    <p class="text-slate-600 text-sm leading-relaxed">Confidence scoring and human-in-the-loop review for compliance-critical workflows.</p>
                </div>
                <div class="enterprise-card p-6">
                    <div class="w-10 h-10 rounded-lg bg-blue-50 flex items-center justify-center mb-4">
                        <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                    </div>
                    <h3 class="text-lg font-semibold text-[#1a2b4c] mb-2">Route</h3>
                    <p class="text-slate-600 text-sm leading-relaxed">Visual flows and workflows that automate decisions across your document pipeline.</p>
                </div>
                <div class="enterprise-card p-6">
                    <div class="w-10 h-10 rounded-lg bg-blue-50 flex items-center justify-center mb-4">
                        <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                    </div>
                    <h3 class="text-lg font-semibold text-[#1a2b4c] mb-2">Integrate</h3>
                    <p class="text-slate-600 text-sm leading-relaxed">REST APIs, SDKs, webhooks, and N8N nodes for seamless system connectivity.</p>
                </div>
            </div>
        </section>

        <!-- Problems eliminated -->
        <section class="mb-16 md:mb-20">
            <div class="enterprise-card p-8 md:p-10">
                <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] mb-8 text-center">The problems we eliminate</h2>
                <div class="grid md:grid-cols-3 gap-8">
                    <div class="text-center md:text-left">
                        <div class="w-11 h-11 rounded-lg bg-slate-100 flex items-center justify-center mx-auto md:mx-0 mb-4">
                            <svg class="w-5 h-5 text-[#1a2b4c]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                        </div>
                        <h3 class="text-lg font-semibold text-[#1a2b4c] mb-2">Manual data entry</h3>
                        <p class="text-slate-600 text-sm leading-relaxed">Stop wasting hours typing data from invoices, manifests, and reports.</p>
                    </div>
                    <div class="text-center md:text-left">
                        <div class="w-11 h-11 rounded-lg bg-slate-100 flex items-center justify-center mx-auto md:mx-0 mb-4">
                            <svg class="w-5 h-5 text-[#1a2b4c]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                        </div>
                        <h3 class="text-lg font-semibold text-[#1a2b4c] mb-2">Human errors</h3>
                        <p class="text-slate-600 text-sm leading-relaxed">Eliminate costly mistakes and compliance issues from manual entry.</p>
                    </div>
                    <div class="text-center md:text-left">
                        <div class="w-11 h-11 rounded-lg bg-slate-100 flex items-center justify-center mx-auto md:mx-0 mb-4">
                            <svg class="w-5 h-5 text-[#1a2b4c]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                        </div>
                        <h3 class="text-lg font-semibold text-[#1a2b4c] mb-2">Growing backlog</h3>
                        <p class="text-slate-600 text-sm leading-relaxed">Clear document backlogs with automated, always-on processing.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Results -->
        <section class="mb-16 md:mb-20 bg-slate-50 rounded-xl border border-slate-200/80 p-8 md:p-12">
            <p class="enterprise-section-label text-center mb-3">Proven outcomes</p>
            <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] mb-10 text-center">What our clients achieve</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="text-center">
                    <div class="text-4xl md:text-5xl font-bold enterprise-metric mb-2">90%</div>
                    <div class="text-slate-600 font-medium">Faster processing</div>
                </div>
                <div class="text-center">
                    <div class="text-4xl md:text-5xl font-bold enterprise-metric mb-2">95%</div>
                    <div class="text-slate-600 font-medium">Error reduction</div>
                </div>
                <div class="text-center">
                    <div class="text-4xl md:text-5xl font-bold enterprise-metric mb-2">$50K+</div>
                    <div class="text-slate-600 font-medium">Annual savings</div>
                </div>
            </div>
        </section>

        <!-- Customer proof -->
        <section class="mb-16 md:mb-20">
            <div class="text-center mb-10">
                <p class="enterprise-section-label mb-3">Case studies</p>
                <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] mb-4">Trusted in regulated industries</h2>
            </div>
            <div class="grid md:grid-cols-3 gap-6">
                <a href="{{ '/case-studies/insurance_wholesaler/' | relative_url }}" class="enterprise-card enterprise-proof-card p-6 no-underline block">
                    <p class="text-3xl font-bold text-blue-600 mb-2">75%</p>
                    <p class="text-[#1a2b4c] font-semibold mb-2">Less manual work</p>
                    <p class="text-slate-600 text-sm mb-4">Insurance wholesaler automating ACORD form processing with ALIS integration.</p>
                    <span class="text-blue-600 text-sm font-medium">Read case study →</span>
                </a>
                <a href="{{ '/case-studies/epic_dme_order_processing/' | relative_url }}" class="enterprise-card enterprise-proof-card p-6 no-underline block">
                    <p class="text-3xl font-bold text-blue-600 mb-2">90%</p>
                    <p class="text-[#1a2b4c] font-semibold mb-2">Faster Epic integration</p>
                    <p class="text-slate-600 text-sm mb-4">Zero-touch DME order automation with 100% compliance in healthcare workflows.</p>
                    <span class="text-blue-600 text-sm font-medium">Read case study →</span>
                </a>
                <a href="{{ '/case-studies/supply-chain/' | relative_url }}" class="enterprise-card enterprise-proof-card p-6 no-underline block">
                    <p class="text-3xl font-bold text-blue-600 mb-2">Hours → min</p>
                    <p class="text-[#1a2b4c] font-semibold mb-2">Trade document processing</p>
                    <p class="text-slate-600 text-sm mb-4">AI-powered manifest and shipping document extraction for supply chain operations.</p>
                    <span class="text-blue-600 text-sm font-medium">Read case study →</span>
                </a>
            </div>
        </section>

        <!-- Industry solutions -->
        <section id="featured-solutions" class="mb-16 md:mb-20">
            <div class="text-center mb-10">
                <p class="enterprise-section-label mb-3">Solutions</p>
                <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] mb-4">Built for your industry</h2>
                <p class="text-slate-600 text-lg max-w-2xl mx-auto">
                    Specialized document processing for regulated, high-volume operations. Don't see yours? We can build it.
                </p>
            </div>
            <div class="grid md:grid-cols-2 gap-6">
                <div class="enterprise-card p-6">
                    <div class="flex items-start gap-4 mb-4">
                        <div class="w-10 h-10 rounded-lg bg-blue-50 flex items-center justify-center flex-shrink-0">
                            <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                        </div>
                        <div>
                            <h3 class="text-lg font-semibold text-[#1a2b4c] mb-2">Insurance Claims &amp; ACORD Forms</h3>
                            <p class="text-slate-600 text-sm leading-relaxed mb-3">Process claims and ACORD forms for faster payouts. Extract customer data and integrate with your AMS system.</p>
                            <p class="text-xs text-slate-500"><span class="font-semibold text-slate-600">Use case:</span> Accelerate claims processing and reduce payout times</p>
                        </div>
                    </div>
                    <a href="{{ '/solutions/insurance/' | relative_url }}" class="text-blue-600 hover:text-blue-800 text-sm font-medium no-underline">Learn more →</a>
                </div>
                <div class="enterprise-card p-6">
                    <div class="flex items-start gap-4 mb-4">
                        <div class="w-10 h-10 rounded-lg bg-blue-50 flex items-center justify-center flex-shrink-0">
                            <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg>
                        </div>
                        <div>
                            <h3 class="text-lg font-semibold text-[#1a2b4c] mb-2">Shipping Manifests</h3>
                            <p class="text-slate-600 text-sm leading-relaxed mb-3">Extract container data, item quantities, and special instructions from manifests. Match against inventory systems.</p>
                            <p class="text-xs text-slate-500"><span class="font-semibold text-slate-600">Problem:</span> Manual verification of manifest data against physical inventory</p>
                        </div>
                    </div>
                    <a href="{{ '/solutions/supply-chain/' | relative_url }}" class="text-blue-600 hover:text-blue-800 text-sm font-medium no-underline">Learn more →</a>
                </div>
                <div class="enterprise-card p-6">
                    <div class="flex items-start gap-4 mb-4">
                        <div class="w-10 h-10 rounded-lg bg-blue-50 flex items-center justify-center flex-shrink-0">
                            <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
                        </div>
                        <div>
                            <h3 class="text-lg font-semibold text-[#1a2b4c] mb-2">Healthcare Denials &amp; Lab Results</h3>
                            <p class="text-slate-600 text-sm leading-relaxed mb-3">Handle denials, patient records, and lab results with precision. Process complex medical documents automatically.</p>
                            <p class="text-xs text-slate-500"><span class="font-semibold text-slate-600">Use case:</span> Streamline medical document processing and reduce errors</p>
                        </div>
                    </div>
                    <a href="{{ '/solutions/dme/' | relative_url }}" class="text-blue-600 hover:text-blue-800 text-sm font-medium no-underline">Learn more →</a>
                </div>
                <div class="enterprise-card p-6">
                    <div class="flex items-start gap-4 mb-4">
                        <div class="w-10 h-10 rounded-lg bg-blue-50 flex items-center justify-center flex-shrink-0">
                            <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        </div>
                        <div>
                            <h3 class="text-lg font-semibold text-[#1a2b4c] mb-2">Finance: Loan Origination &amp; KYC</h3>
                            <p class="text-slate-600 text-sm leading-relaxed mb-3">Accelerate loan origination, KYC checks, and audits. Process financial documents and compliance forms automatically.</p>
                            <p class="text-xs text-slate-500"><span class="font-semibold text-slate-600">Use case:</span> Speed up financial processes and reduce compliance risk</p>
                        </div>
                    </div>
                    <a href="{{ '/solutions/banking/' | relative_url }}" class="text-blue-600 hover:text-blue-800 text-sm font-medium no-underline">Learn more →</a>
                </div>
            </div>
            <div class="text-center mt-8">
                <a href="{{ '/solutions/' | relative_url }}"
                   class="enterprise-btn-secondary inline-flex items-center justify-center px-6 py-3 rounded-lg font-semibold text-base transition-colors duration-200 no-underline">
                    See all solutions
                </a>
            </div>
        </section>

        <!-- Security & deployment -->
        <section class="mb-16 md:mb-20">
            <div class="rounded-xl bg-[#1a2b4c] text-white p-8 md:p-12">
                <div class="grid md:grid-cols-2 gap-10 items-center">
                    <div>
                        <p class="enterprise-section-label text-blue-300 mb-3">Enterprise ready</p>
                        <h2 class="text-2xl md:text-3xl font-bold mb-4">Deploy your way</h2>
                        <p class="text-slate-300 leading-relaxed mb-6">
                            SaaS or on-premises. API-first architecture with sandbox environments, role-based access, and audit-ready workflows.
                        </p>
                        <a href="{{ '/docs/on-prem-installation/' | relative_url }}"
                           class="inline-flex items-center text-blue-300 hover:text-white font-medium text-sm no-underline transition-colors">
                            On-premises deployment guide →
                        </a>
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <div class="rounded-lg bg-white/5 border border-white/10 p-4">
                            <svg class="w-6 h-6 text-blue-400 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2"/></svg>
                            <p class="text-sm font-medium">On-premises</p>
                        </div>
                        <div class="rounded-lg bg-white/5 border border-white/10 p-4">
                            <svg class="w-6 h-6 text-blue-400 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
                            <p class="text-sm font-medium">VPC deployment</p>
                        </div>
                        <div class="rounded-lg bg-white/5 border border-white/10 p-4">
                            <svg class="w-6 h-6 text-blue-400 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                            <p class="text-sm font-medium">Compliance-first</p>
                        </div>
                        <div class="rounded-lg bg-white/5 border border-white/10 p-4">
                            <svg class="w-6 h-6 text-blue-400 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                            <p class="text-sm font-medium">Audit trails</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Developer section -->
        <section class="mb-16 md:mb-20">
            <div class="text-center mb-10">
                <p class="enterprise-section-label mb-3">For developers</p>
                <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] mb-4">Built for developers, designed for business users</h2>
                <p class="text-slate-600 text-lg max-w-2xl mx-auto">
                    Give your technical team the tools and support they need to integrate seamlessly.
                </p>
            </div>
            <div class="grid md:grid-cols-2 gap-6">
                <div class="enterprise-card p-8">
                    <h3 class="text-xl font-semibold text-[#1a2b4c] mb-4">What your developers get</h3>
                    <ul class="text-slate-600 space-y-3 text-sm mb-6">
                        <li class="flex gap-2"><span class="text-blue-600 font-bold">·</span> REST APIs, Python &amp; TypeScript SDKs, N8N nodes, MCP server</li>
                        <li class="flex gap-2"><span class="text-blue-600 font-bold">·</span> Webhooks for real-time event delivery</li>
                        <li class="flex gap-2"><span class="text-blue-600 font-bold">·</span> Sandbox environment for testing integrations</li>
                        <li class="flex gap-2"><span class="text-blue-600 font-bold">·</span> Enterprise-grade security and compliance</li>
                        <li class="flex gap-2"><span class="text-blue-600 font-bold">·</span> Dedicated developer support and technical guidance</li>
                    </ul>
                    <div class="flex flex-wrap gap-2">
                        <a href="{{ '/docs/rest-api/' | relative_url }}" class="text-sm font-medium text-blue-600 hover:text-blue-800 no-underline px-3 py-1.5 rounded-md bg-blue-50">API docs</a>
                        <a href="{{ '/docs/python-sdk/' | relative_url }}" class="text-sm font-medium text-blue-600 hover:text-blue-800 no-underline px-3 py-1.5 rounded-md bg-blue-50">Python SDK</a>
                        <a href="{{ '/docs/typescript-sdk/' | relative_url }}" class="text-sm font-medium text-blue-600 hover:text-blue-800 no-underline px-3 py-1.5 rounded-md bg-blue-50">TypeScript SDK</a>
                    </div>
                </div>
                <div class="enterprise-card p-8">
                    <h3 class="text-xl font-semibold text-[#1a2b4c] mb-4">Implementation services &amp; support</h3>
                    <ul class="text-slate-600 space-y-3 text-sm mb-6">
                        <li class="flex gap-2"><span class="text-blue-600 font-bold">·</span> Custom integration architecture design</li>
                        <li class="flex gap-2"><span class="text-blue-600 font-bold">·</span> End-to-end implementation and deployment</li>
                        <li class="flex gap-2"><span class="text-blue-600 font-bold">·</span> Team training and knowledge transfer</li>
                        <li class="flex gap-2"><span class="text-blue-600 font-bold">·</span> Claude integration for intelligent code generation</li>
                        <li class="flex gap-2"><span class="text-blue-600 font-bold">·</span> Ongoing technical support and maintenance</li>
                    </ul>
                    <a href="{{ site.calendly_url }}"
                       target="_blank"
                       rel="noopener noreferrer"
                       class="enterprise-btn-primary inline-flex items-center justify-center px-5 py-2.5 rounded-lg font-medium text-sm transition-colors duration-200 no-underline">
                        Discuss implementation
                    </a>
                </div>
            </div>
        </section>

        <!-- Video -->
        <section class="mb-16 md:mb-20">
            <div class="text-center mb-8">
                <p class="enterprise-section-label mb-3">Overview</p>
                <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c]">See DocRouter in action</h2>
            </div>
            <div class="enterprise-card p-2 max-w-4xl mx-auto">
                <div class="relative w-full rounded-lg overflow-hidden" style="padding-bottom: 56.25%; height: 0;">
                    <iframe
                        src="https://player.vimeo.com/video/1130281211?title=0&byline=0&portrait=0&color=ffffff"
                        title="DocRouter - AI-Powered Document Processing Introduction"
                        frameborder="0"
                        allow="autoplay; fullscreen; picture-in-picture"
                        allowfullscreen
                        class="absolute top-0 left-0 w-full h-full">
                    </iframe>
                </div>
            </div>
        </section>

        <!-- CTA band -->
        <section class="mb-16 md:mb-20">
            <div class="rounded-xl border border-slate-200 bg-slate-50 p-8 md:p-12 text-center">
                <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c] mb-4">Ready to transform your document workflows?</h2>
                <p class="text-slate-600 mb-8 max-w-xl mx-auto">
                    Schedule a demo to see how DocRouter can streamline your operations—or launch the app to get started today.
                </p>
                <div class="flex flex-col sm:flex-row gap-3 justify-center">
                    <a href="{{ site.calendly_url }}"
                       target="_blank"
                       rel="noopener noreferrer"
                       class="enterprise-btn-primary inline-flex items-center justify-center px-7 py-3.5 rounded-lg font-semibold text-base transition-colors duration-200 no-underline">
                        Schedule a Demo
                    </a>
                    <a href="https://app.docrouter.ai"
                       target="_blank"
                       rel="noopener noreferrer"
                       class="enterprise-btn-secondary inline-flex items-center justify-center px-7 py-3.5 rounded-lg font-semibold text-base transition-colors duration-200 no-underline">
                        Launch App
                    </a>
                    <a href="{{ '/pricing/' | relative_url }}"
                       class="inline-flex items-center justify-center px-7 py-3.5 rounded-lg font-semibold text-base text-slate-600 hover:text-[#1a2b4c] transition-colors duration-200 no-underline">
                        View pricing
                    </a>
                </div>
            </div>
        </section>

        <!-- Contact -->
        <section class="enterprise-card p-8 md:p-10">
            <div class="text-center mb-8">
                <p class="enterprise-section-label mb-3">Contact</p>
                <h2 class="text-2xl md:text-3xl font-bold text-[#1a2b4c]">Talk to our team</h2>
            </div>
            <div class="grid md:grid-cols-2 gap-10 max-w-3xl mx-auto">
                <div class="space-y-5">
                    <div class="flex items-center gap-4">
                        <div class="w-10 h-10 rounded-lg bg-blue-50 flex items-center justify-center flex-shrink-0">
                            <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                        </div>
                        <div>
                            <p class="font-medium text-[#1a2b4c] text-sm">Email</p>
                            <a href="mailto:andrei@analytiqhub.com" class="text-blue-600 hover:text-blue-800 text-sm no-underline">andrei@analytiqhub.com</a>
                        </div>
                    </div>
                    <div class="flex items-center gap-4">
                        <div class="w-10 h-10 rounded-lg bg-blue-50 flex items-center justify-center flex-shrink-0">
                            <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                        </div>
                        <div>
                            <p class="font-medium text-[#1a2b4c] text-sm">Phone</p>
                            <a href="tel:6172168509" class="text-blue-600 hover:text-blue-800 text-sm no-underline">617.216.8509</a>
                        </div>
                    </div>
                    <div class="flex items-center gap-4">
                        <div class="w-10 h-10 rounded-lg bg-blue-50 flex items-center justify-center flex-shrink-0">
                            <svg class="w-5 h-5 text-blue-600" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                        </div>
                        <div>
                            <p class="font-medium text-[#1a2b4c] text-sm">LinkedIn</p>
                            <a href="https://www.linkedin.com/company/docrouter" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-800 text-sm no-underline">linkedin.com/company/docrouter</a>
                        </div>
                    </div>
                </div>
                <div class="flex flex-col justify-center">
                    <a href="{{ site.calendly_url }}"
                       target="_blank"
                       rel="noopener noreferrer"
                       class="enterprise-btn-primary inline-flex items-center justify-center px-6 py-3.5 rounded-lg font-semibold text-base transition-colors duration-200 no-underline mb-4">
                        Schedule a Meeting
                    </a>
                    <p class="text-sm text-slate-600 leading-relaxed">
                        Book a time to discuss your document processing needs and see how DocRouter can help streamline your operations.
                    </p>
                </div>
            </div>
        </section>

    </main>
</div>
