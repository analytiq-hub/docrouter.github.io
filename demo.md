---
layout: default
title: "DocRouter Demo"
permalink: /demo/
description: "Watch DocRouter process real insurance documents: an agent builds an extraction pipeline, tags trigger the work, answers cite the policy, and a mixed packet is split by patient with a human-review flag."
image: https://media.docrouter.ai/demos/datos-2026/poster-v1.jpg
---

{% assign video_base = "https://media.docrouter.ai/demos/datos-2026" %}

<section class="enterprise-hero border-b border-slate-200/80 py-10 md:py-14">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p class="enterprise-section-label mb-3">Product demo · 3:40</p>
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-bold text-[#1a2b4c] mb-4 leading-tight">
            See DocRouter work on real insurance documents
        </h1>
        <p class="text-base sm:text-lg text-slate-600 max-w-2xl mx-auto mb-8">
            Claim files, policy packets and a mixed pre-op packet: from first notice of loss to a cited
            answer and a human-review flag. Captions are on screen, so no sound is needed.
        </p>
        <div class="flex flex-col sm:flex-row gap-3 justify-center items-stretch sm:items-center">
            <a href="{{ site.calendly_url }}"
               target="_blank"
               rel="noopener noreferrer"
               class="enterprise-btn-primary inline-flex items-center justify-center px-7 py-3.5 rounded-lg font-semibold text-base transition-colors duration-200 no-underline">
                Book a live demo
            </a>
            <a href="/contact/"
               class="enterprise-btn-secondary inline-flex items-center justify-center px-7 py-3.5 rounded-lg font-semibold text-base transition-colors duration-200 no-underline">
                Contact us
            </a>
        </div>
    </div>
</section>

<div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 md:py-12">
    <main>
        <section class="mb-10 md:mb-14">
            <div class="demo-video-frame">
                <video id="demo-video"
                       controls
                       playsinline
                       preload="metadata"
                       poster="{{ video_base }}/poster-v1.jpg">
                    <source src="{{ video_base }}/docrouter-datos-2026-v1.mp4" type="video/mp4">
                    Your browser can't play this video.
                    <a href="{{ video_base }}/docrouter-datos-2026-v1.mp4">Download it (MP4, 11 MB)</a>.
                </video>
            </div>
            <p class="text-sm text-slate-500 mt-3 text-center">
                Recorded on a live DocRouter instance with synthetic documents.
            </p>
        </section>

        <section class="mb-10 md:mb-14">
            <h2 class="text-2xl font-bold text-[#1a2b4c] mb-2">Jump to a chapter</h2>
            <p class="text-slate-600 mb-6">Each chapter stands on its own.</p>
            <ol class="demo-chapters grid gap-3 sm:grid-cols-2 list-none p-0 m-0">
                <li><button type="button" data-t="2.8">
                    <span class="demo-chapter-time">0:02</span>
                    <span class="demo-chapter-title">The archive</span>
                    <span class="demo-chapter-desc">Claim and policy documents indexed beside the system of record, grouped into cases.</span>
                </button></li>
                <li><button type="button" data-t="19.5">
                    <span class="demo-chapter-time">0:19</span>
                    <span class="demo-chapter-title">The agent builds a pipeline</span>
                    <span class="demo-chapter-desc">One sentence to the agent creates a tag, a schema and a versioned prompt, then extracts the FNOL.</span>
                </button></li>
                <li><button type="button" data-t="73.3">
                    <span class="demo-chapter-time">1:13</span>
                    <span class="demo-chapter-title">Tags trigger the work</span>
                    <span class="demo-chapter-desc">A new loss notice is uploaded with the tag, and OCR and extraction run on their own.</span>
                </button></li>
                <li><button type="button" data-t="95.7">
                    <span class="demo-chapter-time">1:35</span>
                    <span class="demo-chapter-title">Cited answers</span>
                    <span class="demo-chapter-desc">A knowledge base answers from the issued policy and quotes the passage it read.</span>
                </button></li>
                <li><button type="button" data-t="118.8">
                    <span class="demo-chapter-time">1:58</span>
                    <span class="demo-chapter-title">A mixed packet, end to end</span>
                    <span class="demo-chapter-desc">A flow splits 13 pages, classifies each one, groups them by patient and sets a human-review flag.</span>
                </button></li>
                <li><button type="button" data-t="187.8">
                    <span class="demo-chapter-time">3:07</span>
                    <span class="demo-chapter-title">Everything is an API</span>
                    <span class="demo-chapter-desc">Every screen runs on the same REST API, with Python and TypeScript SDKs and an MCP server.</span>
                </button></li>
            </ol>
        </section>

        {% include enterprise-cta.html
            title="See it on your own documents"
            description="Book a live demo and we'll walk through your document types, your review steps and how DocRouter fits beside your core systems." %}
    </main>
</div>

<style>
    .demo-video-frame {
        position: relative;
        aspect-ratio: 16 / 9;
        width: 100%;
        background: #0b1220;
        border-radius: 0.875rem;
        overflow: hidden;
        box-shadow: 0 20px 45px -20px rgba(15, 23, 42, 0.45);
    }
    .demo-video-frame video {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: contain;
        display: block;
    }
    .demo-chapters button {
        display: grid;
        grid-template-columns: auto 1fr;
        column-gap: 0.875rem;
        row-gap: 0.25rem;
        width: 100%;
        text-align: left;
        padding: 1rem 1.125rem;
        border: 1px solid #e2e8f0;
        border-radius: 0.75rem;
        background: #fff;
        cursor: pointer;
        transition: border-color 0.15s, box-shadow 0.15s, background 0.15s;
    }
    .demo-chapters button:hover,
    .demo-chapters button:focus-visible {
        border-color: #93c5fd;
        box-shadow: 0 4px 14px -6px rgba(37, 99, 235, 0.35);
        outline: none;
    }
    .demo-chapters button.is-active {
        border-color: #2563eb;
        background: #eff6ff;
    }
    .demo-chapter-time {
        grid-row: span 2;
        font: 600 0.875rem/1.5rem "JetBrains Mono", ui-monospace, monospace;
        color: #2563eb;
    }
    .demo-chapter-title {
        font-weight: 600;
        color: #1a2b4c;
    }
    .demo-chapter-desc {
        font-size: 0.875rem;
        line-height: 1.4;
        color: #475569;
    }
</style>

<script>
    (function () {
        var video = document.getElementById('demo-video');
        if (!video) return;
        var buttons = Array.prototype.slice.call(document.querySelectorAll('.demo-chapters button'));

        buttons.forEach(function (btn) {
            btn.addEventListener('click', function () {
                video.currentTime = parseFloat(btn.getAttribute('data-t'));
                var p = video.play();
                if (p && p.catch) p.catch(function () {});
                video.scrollIntoView({ behavior: 'smooth', block: 'center' });
            });
        });

        // Mark the chapter that is playing.
        video.addEventListener('timeupdate', function () {
            var t = video.currentTime, active = null;
            buttons.forEach(function (btn) {
                if (t >= parseFloat(btn.getAttribute('data-t')) - 0.25) active = btn;
            });
            buttons.forEach(function (btn) { btn.classList.toggle('is-active', btn === active); });
        });
    })();
</script>
