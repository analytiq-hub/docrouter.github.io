---
layout: default
title: "Support — DocRouter"
permalink: /support/
description: "Get help with DocRouter—documentation, email support, and technical assistance for your document processing workflows."
---

<section class="enterprise-hero border-b border-slate-200/80 py-10 md:py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p class="enterprise-section-label mb-3">Support</p>
        <h1 class="text-4xl md:text-5xl font-bold text-[#1a2b4c] mb-4">We're here to help</h1>
        <p class="text-lg text-slate-600 max-w-2xl mx-auto">
            Get the help you need to make the most of DocRouter's document processing platform.
        </p>
    </div>
</section>

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-16">
    <main>
        <section class="enterprise-card p-8 md:p-10 mb-12">
            <div class="grid md:grid-cols-2 gap-10">
                <div>
                    <h2 class="text-2xl font-bold text-[#1a2b4c] mb-8">Support resources</h2>
                    <div class="space-y-6">
                        <div class="flex items-center gap-4">
                            <div class="solution-challenge-icon solution-challenge-icon--inline text-blue-600 flex-shrink-0">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
                                </svg>
                            </div>
                            <div>
                                <p class="text-sm font-semibold text-[#1a2b4c] m-0 mb-1">Documentation</p>
                                <a href="{{ '/docs/' | relative_url }}" class="text-blue-600 hover:text-blue-800 text-sm no-underline">
                                    Browse the docs →
                                </a>
                            </div>
                        </div>

                        <div class="flex items-center gap-4">
                            <div class="solution-challenge-icon solution-challenge-icon--inline text-blue-600 flex-shrink-0">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                                </svg>
                            </div>
                            <div>
                                <p class="text-sm font-semibold text-[#1a2b4c] m-0 mb-1">Email support</p>
                                <a href="mailto:andrei@docrouter.ai" class="text-blue-600 hover:text-blue-800 text-sm no-underline">
                                    andrei@docrouter.ai
                                </a>
                            </div>
                        </div>
                    </div>
                </div>

                <div>
                    <h2 class="text-2xl font-bold text-[#1a2b4c] mb-8">Get help</h2>
                    <div class="space-y-4">
                        <a href="mailto:andrei@docrouter.ai?subject=Support Request"
                           class="enterprise-btn-primary block w-full text-center px-8 py-4 rounded-lg font-semibold text-base transition-colors duration-200 no-underline">
                            Submit support ticket
                        </a>
                        <a href="{{ site.calendly_url }}"
                           target="_blank"
                           rel="noopener noreferrer"
                           class="enterprise-btn-secondary block w-full text-center px-8 py-4 rounded-lg font-semibold text-base transition-colors duration-200 no-underline">
                            Schedule technical call
                        </a>
                    </div>
                </div>
            </div>
        </section>

        {% include enterprise-cta.html
            title="Need hands-on implementation help?"
            description="Schedule a demo to discuss deployment, integrations, and professional services for your document workflows." %}
    </main>
</div>
