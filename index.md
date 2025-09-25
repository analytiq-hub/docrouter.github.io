---
layout: default
title: "DocRouter - AI-Powered Document Processing"
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <!-- Hero Section - Lead with Problem -->
    <header class="text-center md:mb-12 mb-8">
        <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
            Stop Wasting Hours on Manual Data Entry
        </h1>
        <div class="text-xl md:text-2xl text-gray-600 mb-8">
            <p class="mb-4">We automate document processing for invoices, manifests, and reports - reducing processing time by <span class="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent font-bold">90%</span></p>
        </div>

        <!-- Primary CTA -->
        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <a href="https://app.docrouter.ai"
               target="_blank"
               rel="noopener noreferrer"
               class="inline-block bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 border-2 border-transparent">
                Try It Free
            </a>
            <a href="#featured-use-cases"
               class="inline-block border-2 border-blue-600 text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200">
                See How It Works
            </a>
        </div>
    </header>

    <!-- Banner Graphic Section -->
    <section class="bg-white rounded-lg shadow-lg p-8 mb-12">
        <div class="text-center">
            <img src="{{ '/assets/images/banner_graphic.jpg' | relative_url }}" 
                 alt="DocRouter Banner" 
                 class="w-full max-w-4xl mx-auto rounded-lg">
        </div>
    </section>

    <main>
        <!-- Problem Statement Section -->
        <section class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-3xl font-semibold text-gray-900 mb-6 text-center">The Problems We Eliminate</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="text-center">
                    <div class="bg-red-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                        <span class="text-2xl">🖊️</span>
                    </div>
                    <h3 class="text-xl font-medium text-gray-900 mb-2">Manual Data Entry</h3>
                    <p class="text-gray-600">Stop wasting hours typing data from invoices, manifests, and reports</p>
                </div>
                <div class="text-center">
                    <div class="bg-red-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                        <span class="text-2xl">⚠️</span>
                    </div>
                    <h3 class="text-xl font-medium text-gray-900 mb-2">Human Errors</h3>
                    <p class="text-gray-600">Eliminate costly mistakes and compliance issues from manual entry</p>
                </div>
                <div class="text-center">
                    <div class="bg-red-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                        <span class="text-2xl">📚</span>
                    </div>
                    <h3 class="text-xl font-medium text-gray-900 mb-2">Growing Backlog</h3>
                    <p class="text-gray-600">Clear document backlogs with automated processing</p>
                </div>
            </div>
        </section>

        <!-- Why Choose Us - Small Company Advantage -->
        <section class="bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg shadow-lg p-8 mb-12">
            <div class="text-center">
                <h2 class="text-3xl font-semibold text-white mb-6">Why Choose a Specialized Solution?</h2>
                <p class="text-xl text-blue-100 mb-8">
                    Big companies can't afford to customize for your specific needs. We can.
                </p>
                <div class="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
                    <div class="bg-white bg-opacity-10 rounded-lg p-6">
                        <h3 class="text-xl font-medium text-white mb-3">Big Company Problems</h3>
                        <ul class="text-blue-100 space-y-2 text-left">
                            <li>• One-size-fits-all solutions</li>
                            <li>• Expensive enterprise pricing</li>
                            <li>• Long implementation cycles</li>
                            <li>• Generic support</li>
                        </ul>
                    </div>
                    <div class="bg-white bg-opacity-10 rounded-lg p-6">
                        <h3 class="text-xl font-medium text-white mb-3">Our Advantage</h3>
                        <ul class="text-blue-100 space-y-2 text-left">
                            <li>• Customized for your industry</li>
                            <li>• Affordable pricing</li>
                            <li>• Quick setup and training</li>
                            <li>• Direct access to our team</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Featured Use Cases - Above the Fold -->
        <section id="featured-use-cases" class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-3xl font-semibold text-gray-900 mb-6 text-center">Solutions for Your Industry</h2>
            <p class="text-gray-600 mb-8 text-center text-lg">
                We specialize in these document processing challenges. Don't see yours? We can build it.
            </p>

            <div class="grid md:grid-cols-2 gap-8">
                <!-- Insurance Applications -->
                <div class="border border-gray-200 rounded-lg p-6 hover:shadow-lg transition-shadow">
                    <div class="flex items-center mb-4">
                        <div class="bg-blue-100 rounded-full w-12 h-12 flex items-center justify-center mr-4">
                            <span class="text-xl">📋</span>
                        </div>
                        <h3 class="text-xl font-medium text-gray-900">Insurance Applications</h3>
                    </div>
                    <p class="text-gray-600 mb-4">
                        Process handwritten and typed insurance applications from email. Extract customer data and integrate with your AMS system.
                    </p>
                    <div class="text-sm text-gray-500 mb-4">
                        <strong>Problem:</strong> 50% handwritten applications, manual data entry into Ellis AMS
                    </div>
                    <a href="{{ '/use-cases/insurance/' | relative_url }}" class="text-blue-600 hover:text-blue-800 font-medium">Learn more →</a>
                </div>

                <!-- Shipping Manifests -->
                <div class="border border-gray-200 rounded-lg p-6 hover:shadow-lg transition-shadow">
                    <div class="flex items-center mb-4">
                        <div class="bg-blue-100 rounded-full w-12 h-12 flex items-center justify-center mr-4">
                            <span class="text-xl">📦</span>
                        </div>
                        <h3 class="text-xl font-medium text-gray-900">Shipping Manifests</h3>
                    </div>
                    <p class="text-gray-600 mb-4">
                        Extract container data, item quantities, and special instructions from manifests. Match against inventory systems.
                    </p>
                    <div class="text-sm text-gray-500 mb-4">
                        <strong>Problem:</strong> Manual verification of manifest data against physical inventory
                    </div>
                    <a href="{{ '/use-cases/supply-chain/' | relative_url }}" class="text-blue-600 hover:text-blue-800 font-medium">Learn more →</a>
                </div>

                <!-- Clinical Trial Invoices -->
                <div class="border border-gray-200 rounded-lg p-6 hover:shadow-lg transition-shadow">
                    <div class="flex items-center mb-4">
                        <div class="bg-blue-100 rounded-full w-12 h-12 flex items-center justify-center mr-4">
                            <span class="text-xl">🧪</span>
                        </div>
                        <h3 class="text-xl font-medium text-gray-900">Clinical Trial Invoices</h3>
                    </div>
                    <p class="text-gray-600 mb-4">
                        Verify lab service invoices against contracts. Check rates, service eligibility, and billing cycles automatically.
                    </p>
                    <div class="text-sm text-gray-500 mb-4">
                        <strong>Problem:</strong> Manual verification of complex contract terms
                    </div>
                    <a href="{{ '/use-cases/clinical-trials/' | relative_url }}" class="text-blue-600 hover:text-blue-800 font-medium">Learn more →</a>
                </div>

                <!-- Private Equity Statements -->
                <div class="border border-gray-200 rounded-lg p-6 hover:shadow-lg transition-shadow">
                    <div class="flex items-center mb-4">
                        <div class="bg-blue-100 rounded-full w-12 h-12 flex items-center justify-center mr-4">
                            <span class="text-xl">💰</span>
                        </div>
                        <h3 class="text-xl font-medium text-gray-900">Private Equity Reports</h3>
                    </div>
                    <p class="text-gray-600 mb-4">
                        Process 30-50 quarterly statements from fund managers. Extract financial data for Excel and PowerPoint reporting.
                    </p>
                    <div class="text-sm text-gray-500 mb-4">
                        <strong>Problem:</strong> Manual extraction consuming 20-40% of team time
                    </div>
                    <a href="{{ '/use-cases/private-equity/' | relative_url }}" class="text-blue-600 hover:text-blue-800 font-medium">Learn more →</a>
                </div>
            </div>

            <div class="text-center mt-8">
                <a href="{{ '/use-cases/' | relative_url }}"
                   class="inline-block bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white px-6 py-3 rounded-lg font-medium transition-colors duration-200">
                    See More Use Cases
                </a>
            </div>
        </section>

        <!-- Results Section -->
        <section class="bg-gray-50 rounded-lg p-8 mb-12">
            <h2 class="text-3xl font-semibold text-gray-900 mb-6 text-center">What Our Clients Achieve</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="text-center">
                    <div class="text-4xl font-bold text-blue-600 mb-2">90%</div>
                    <div class="text-gray-600">Faster Processing</div>
                </div>
                <div class="text-center">
                    <div class="text-4xl font-bold text-blue-600 mb-2">95%</div>
                    <div class="text-gray-600">Error Reduction</div>
                </div>
                <div class="text-center">
                    <div class="text-4xl font-bold text-blue-600 mb-2">$50K+</div>
                    <div class="text-gray-600">Annual Savings</div>
                </div>
            </div>
        </section>

        <!-- User Experience Section -->
        <section class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">User Experience</h2>
            <div class="grid md:grid-cols-2 gap-6">
                <div class="overflow-hidden rounded-lg shadow-lg">
                    <img src="{{ '/assets/images/docrouter/files.png' | relative_url }}" alt="Document List Interface" class="w-full">
                </div>
                <div class="overflow-hidden rounded-lg shadow-lg">
                    <img src="{{ '/assets/images/docrouter/extractions.png' | relative_url }}" alt="Data Extraction Interface" class="w-full">
                </div>
            </div>
        </section>

        <!-- DocRouter Workflow Sections -->
        <section class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <div class="flex justify-center">
                <img src="{{ '/assets/images/docrouter/flow.svg' | relative_url }}" alt="DocRouter Workflow" class="w-full max-w-2xl">
            </div>
        </section>

        <section class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <div class="flex justify-center">
                <img src="{{ '/assets/images/docrouter/docrouter-workflow.svg' | relative_url }}" alt="Detailed Workflow" class="w-full max-w-4xl">
            </div>
            <div class="mt-6 text-center text-sm text-gray-600">
                <p>Documents flow through automated processing with human oversight for quality control</p>
            </div>
        </section>

        <!-- Contact Section -->
        <section class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-3xl font-semibold text-gray-900 mb-6 text-center">Get In Touch</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <div>
                    <h3 class="text-xl font-medium text-gray-900 mb-4">Contact Information</h3>
                    <div class="space-y-4">
                        <div class="flex items-center">
                            <div class="bg-blue-100 rounded-full w-10 h-10 flex items-center justify-center mr-4">
                                <span class="text-lg">📧</span>
                            </div>
                            <div>
                                <p class="font-medium text-gray-900">Andrei Radulescu-Banu</p>
                                <a href="mailto:andrei@analytiqhub.com" class="text-blue-600 hover:text-blue-800">
                                    andrei@analytiqhub.com
                                </a>
                            </div>
                        </div>
                        <div class="flex items-center">
                            <div class="bg-blue-100 rounded-full w-10 h-10 flex items-center justify-center mr-4">
                                <span class="text-lg">📞</span>
                            </div>
                            <div>
                                <p class="font-medium text-gray-900">Phone</p>
                                <a href="tel:6172168509" class="text-blue-600 hover:text-blue-800">
                                    617.216.8509
                                </a>
                            </div>
                        </div>
                        <div class="flex items-center">
                            <div class="bg-blue-100 rounded-full w-10 h-10 flex items-center justify-center mr-4">
                                <span class="text-lg">🔗</span>
                            </div>
                            <div>
                                <p class="font-medium text-gray-900">LinkedIn</p>
                                <a href="https://www.linkedin.com/company/docrouter"
                                   target="_blank"
                                   rel="noopener noreferrer"
                                   class="text-blue-600 hover:text-blue-800">
                                    linkedin.com/company/docrouter
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <h3 class="text-xl font-medium text-gray-900 mb-4">Schedule a Meeting</h3>
                    <div class="space-y-4">
                        <a href="javascript:void(0)" onclick="openCalendly()"
                           class="block border-2 border-blue-600 text-blue-600 hover:bg-blue-50 px-6 py-3 rounded-lg font-medium text-center transition-colors duration-200">
                            Schedule a Meeting
                        </a>
                        <p class="text-sm text-gray-600">
                            Book a time to discuss your document processing needs and see how DocRouter can help streamline your operations.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer class="mt-12 text-center text-gray-600">
        <p>© 2024 DocRouter.AI. All rights reserved.</p>
        <div class="mt-4">
            <a href="https://github.com/analytiq-hub/doc-router"
               class="text-blue-600 hover:text-blue-800">
                View on GitHub
            </a>
        </div>
    </footer>
</div>