---
layout: default
title: "How It Works - DocRouter"
permalink: /docs/how-it-works/
---

<div class="max-w-6xl mx-auto px-4 sm:px-6 md:px-8 py-4 md:py-12">
    <!-- Hero Section -->
    <header class="text-center md:mb-12 mb-8">
        <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
            How DocRouter Works
        </h1>
        <p class="text-xl md:text-2xl text-gray-600 mb-8">
            Simple, powerful document processing that integrates seamlessly into your workflow
        </p>
    </header>

    <main>

           <!-- Process Overview -->
        <section class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-3xl font-semibold text-gray-900 mb-6 text-center">The DocRouter Process</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <!-- Step 1 -->
                <div class="text-center">
                    <div class="bg-blue-100 rounded-full w-20 h-20 flex items-center justify-center mx-auto mb-4">
                        <span class="text-3xl">📄</span>
                    </div>
                    <h3 class="text-xl font-medium text-gray-900 mb-3">1. Upload Documents</h3>
                    <p class="text-gray-600">Send documents via email, API, or web interface. We support PDFs, images, and scanned documents.</p>
                </div>

                <!-- Step 2 -->
                <div class="text-center">
                    <div class="bg-purple-100 rounded-full w-20 h-20 flex items-center justify-center mx-auto mb-4">
                        <span class="text-3xl">🤖</span>
                    </div>
                    <h3 class="text-xl font-medium text-gray-900 mb-3">2. AI Processing</h3>
                    <p class="text-gray-600">Our AI extracts data, validates information, and structures it according to your specifications.</p>
                </div>

                <!-- Step 3 -->
                <div class="text-center">
                    <div class="bg-green-100 rounded-full w-20 h-20 flex items-center justify-center mx-auto mb-4">
                        <span class="text-3xl">📊</span>
                    </div>
                    <h3 class="text-xl font-medium text-gray-900 mb-3">3. Get Results</h3>
                    <p class="text-gray-600">Receive structured data via API, webhook, or direct integration with your existing systems.</p>
                </div>
            </div>
        </section>

    
        <!-- How It Works Image -->
        <section class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <div class="flex justify-center">
                <img src="{{ '/assets/images/docrouter/flow.svg' | relative_url }}" alt="DocRouter Workflow" class="w-full max-w-2xl">
            </div>
        </section>
        
        <!-- DocRouter Workflow Sections -->
        <section class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <div class="flex justify-center">
                <img src="{{ '/assets/images/docrouter/docrouter-workflow.svg' | relative_url }}" alt="Detailed Workflow" class="w-full max-w-4xl">
            </div>
            <div class="mt-6 text-center text-sm text-gray-600">
                <p>Documents flow through automated processing with human oversight for quality control</p>
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

        <section class="bg-blue-50 rounded-lg p-8 mb-12">
            <h2 class="text-3xl font-semibold text-gray-900 mb-6 text-center">Integration Methods</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <!-- API Integration -->
                <div class="bg-white rounded-lg p-6">
                    <h3 class="text-xl font-semibold text-gray-900 mb-4">REST API</h3>
                    <p class="text-gray-600 mb-4">Integrate directly with your applications using our comprehensive REST API.</p>
                    <ul class="text-gray-600 space-y-2 mb-6">
                        <li>• Upload documents via HTTP POST</li>
                        <li>• Real-time processing status</li>
                        <li>• Webhook notifications</li>
                        <li>• Batch processing support</li>
                    </ul>
                    <a href="{{ '/docs/rest-api/' | relative_url }}" 
                       class="inline-block border-2 border-blue-600 text-blue-600 hover:bg-blue-50 px-4 py-2 rounded-lg font-medium transition-colors duration-200 no-underline">
                        View API Docs
                    </a>
                </div>

                <!-- Email and Faxes Integration -->
                <div class="bg-white rounded-lg p-6">
                    <h3 class="text-xl font-semibold text-gray-900 mb-4">Email and Fax Processing</h3>
                    <p class="text-gray-600 mb-4">Send documents via email or fax and receive results automatically.</p>
                    <ul class="text-gray-600 space-y-2 mb-6">
                        <li>• Forward emails with attachments</li>
                        <li>• Automatic document detection</li>
                        <li>• Email notifications</li>
                        <li>• Fax processing</li>
                    </ul>
                    <a href="javascript:void(0)" onclick="openCalendly()" 
                       class="inline-block border-2 border-gray-600 text-gray-600 hover:bg-gray-50 px-4 py-2 rounded-lg font-medium transition-colors duration-200 no-underline">
                        Schedule a Meeting to Discuss
                    </a>
                </div>
            </div>
        </section>

        <!-- Technical Details -->
        <section class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-3xl font-semibold text-gray-900 mb-6 text-center">Technical Details</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <!-- Processing Capabilities -->
                <div>
                    <h3 class="text-xl font-semibold text-gray-900 mb-4">Processing Capabilities</h3>
                    <ul class="text-gray-600 space-y-2">
                        <li>• Handwritten text recognition</li>
                        <li>• Printed text extraction</li>
                        <li>• Table and form parsing</li>
                        <li>• Signature detection</li>
                        <li>• Multi-language support</li>
                        <li>• Image quality enhancement</li>
                    </ul>
                </div>

                <!-- Supported Formats -->
                <div>
                    <h3 class="text-xl font-semibold text-gray-900 mb-4">Supported Formats</h3>
                    <ul class="text-gray-600 space-y-2">
                        <li>• PDF documents</li>
                        <li>• JPEG, PNG images</li>
                        <li>• Scanned documents</li>
                        <li>• Emails and Faxes</li>
                        <li>• ...and many more!</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- Security & Compliance 
        <section class="bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg shadow-lg p-8 mb-12">
            <div class="text-center">
                <h2 class="text-3xl font-semibold text-white mb-6">Security & Compliance</h2>
                <p class="text-xl text-blue-100 mb-8">
                    Enterprise-grade security built into every step of the process
                </p>
                <div class="grid md:grid-cols-3 gap-6 max-w-4xl mx-auto">
                    <div class="bg-white bg-opacity-10 rounded-lg p-6">
                        <h3 class="text-lg font-medium text-white mb-3">Data Security</h3>
                        <ul class="text-blue-100 space-y-1 text-sm">
                            <li>• End-to-end encryption</li>
                            <li>• SOC 2 compliant</li>
                            <li>• Data retention policies</li>
                            <li>• Secure data transmission</li>
                        </ul>
                    </div>
                    <div class="bg-white bg-opacity-10 rounded-lg p-6">
                        <h3 class="text-lg font-medium text-white mb-3">Privacy</h3>
                        <ul class="text-blue-100 space-y-1 text-sm">
                            <li>• GDPR compliant</li>
                            <li>• No data mining</li>
                            <li>• Client data isolation</li>
                            <li>• Audit trails</li>
                        </ul>
                    </div>
                    <div class="bg-white bg-opacity-10 rounded-lg p-6">
                        <h3 class="text-lg font-medium text-white mb-3">Reliability</h3>
                        <ul class="text-blue-100 space-y-1 text-sm">
                            <li>• 99.9% uptime SLA</li>
                            <li>• Redundant infrastructure</li>
                            <li>• Automated backups</li>
                            <li>• 24/7 monitoring</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
        -->

        <section class="bg-white rounded-lg shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-semibold text-gray-900 mb-4">Learn More</h2>
            <p class="text-gray-600 mb-4">
                Once you understand the high-level flow, these docs cover each building block in more detail:
            </p>
            <ul class="list-disc list-inside text-gray-600 space-y-2">
                <li>
                    <a href="{{ '/docs/quick-start/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Quick Start</a>
                    — Step-by-step Tag → Prompt → Upload workflow.
                </li>
                <li>
                    <a href="{{ '/docs/tags/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Tags</a>
                    — Required routing layer that connects uploads to prompts.
                </li>
                <li>
                    <a href="{{ '/docs/prompts/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Prompts</a>
                    — Instructions that drive AI extraction.
                </li>
                <li>
                    <a href="{{ '/docs/schemas/' | relative_url }}" class="text-blue-600 hover:text-blue-800">Schemas</a>
                    — Structured output for your extraction results.
                </li>
            </ul>
        </section>

        <section class="bg-blue-600 rounded-lg shadow-lg p-8 mb-12">
            <div class="text-center">
                <h2 class="text-3xl font-semibold text-white mb-6">Get Started Today</h2>
                <p class="text-lg text-blue-100 mb-8">
                    Ready to automate your document processing? Choose the path that works best for your team.
                </p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                    <a href="https://app.docrouter.ai"
                       target="_blank"
                       rel="noopener noreferrer"
                       class="inline-block bg-white text-blue-600 hover:bg-blue-50 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
                        Try It Free
                    </a>
                    <a href="{{ '/docs/quick-start/' | relative_url }}"
                       class="inline-block border-2 border-white text-white hover:bg-white hover:text-blue-600 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
                        Use the Quick Start
                    </a>
                    <a href="javascript:void(0)" onclick="openCalendly()"
                       class="inline-block border-2 border-blue-200 text-blue-100 hover:bg-blue-700 px-8 py-4 rounded-lg font-semibold text-lg transition-colors duration-200 no-underline">
                        Schedule a Meeting
                    </a>
                </div>
            </div>
        </section>
    </main>
</div>
