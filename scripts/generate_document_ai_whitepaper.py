#!/usr/bin/env python3
"""Generate the Document AI in Practice white paper PDF from the blog post HTML."""

from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POST = ROOT / "_posts" / "2026-08-06-document-ai-in-practice-why-simple-llm-pipelines-fail.md"
IMAGES = ROOT / "assets" / "images"
OUT = ROOT / "assets" / "files" / "document-ai-in-practice-why-simple-llm-pipelines-fail.pdf"
LOGO = IMAGES / "analytiq_hub_logo_80.png"
SPLASH = IMAGES / "document-ai-in-practice-splash.png"
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
CALENDLY = "https://calendly.com/analytiqhub"

PRINT_CSS = """
@page {
  size: Letter;
  margin: 0;
}

* { box-sizing: border-box; }

body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 10.5pt;
  line-height: 1.55;
  color: #334155;
  margin: 0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

/* Cover */
.cover {
  width: 8.5in;
  height: 11in;
  padding: 0.75in 0.85in 0.55in;
  background: linear-gradient(165deg, #0b1f3a 0%, #123a66 45%, #1d4f8c 100%);
  color: #ffffff;
  position: relative;
  overflow: hidden;
  page-break-after: always;
  break-after: page;
}
.cover-brand { display: flex; align-items: center; gap: 12px; margin-bottom: 0.55in; }
.cover-brand img {
  width: 36px; height: 36px; background: #fff; border-radius: 8px; padding: 3px;
}
.cover-brand-text { font-size: 12pt; font-weight: 600; letter-spacing: 0.02em; }
.cover-eyebrow {
  display: inline-block; font-size: 9pt; font-weight: 600; letter-spacing: 0.12em;
  text-transform: uppercase; color: #93c5fd;
  border: 1px solid rgba(147, 197, 253, 0.45); border-radius: 999px;
  padding: 5px 12px; margin-bottom: 16px;
}
.cover h1 {
  font-size: 24pt; line-height: 1.18; font-weight: 700; margin: 0 0 14px;
  max-width: 6.4in; color: #fff;
}
.cover .subtitle {
  font-size: 11.5pt; line-height: 1.4; color: #dbeafe; max-width: 6.2in; margin: 0 0 0.28in;
}
.cover-meta { font-size: 10pt; color: #bfdbfe; margin-bottom: 0.28in; }
.cover-meta strong { color: #fff; font-weight: 600; }
.cover-splash {
  width: 100%; max-height: 5.0in; object-fit: contain; object-position: top center;
  border-radius: 10px; border: 1px solid rgba(255,255,255,0.18); background: #fff;
}
.cover-footer {
  position: absolute; left: 0.85in; right: 0.85in; bottom: 0.45in;
  font-size: 9pt; color: #93c5fd; display: flex; justify-content: space-between;
}

.page-footer {
  position: fixed; bottom: 0.35in; left: 0.85in; right: 0.85in;
  font-size: 8.5pt; color: #64748b;
  border-top: 1px solid #e2e8f0; padding-top: 6px;
}

/* Content shell */
.content {
  padding: 0.7in 0.85in 0.95in;
}

/* Tailwind-like utilities used by the post */
.not-prose { max-width: none; }
.space-y-14 > * + * { margin-top: 0.55in; }
.space-y-5 > * + * { margin-top: 0.18in; }
.space-y-2 > * + * { margin-top: 0.08in; }
.space-y-1 > * + * { margin-top: 0.04in; }

p { margin: 0; orphans: 3; widows: 3; }

.text-slate-700 { color: #334155; }
.text-slate-600 { color: #475569; }
.text-slate-500 { color: #64748b; }
.text-slate-200 { color: #e2e8f0; }
.text-white { color: #ffffff; }
.text-\\[\\#1a2b4c\\], .text-navy { color: #1a2b4c; }
.text-blue-600 { color: #2563eb; }
.text-blue-700 { color: #1d4ed8; }
.text-emerald-600 { color: #059669; }
.text-emerald-700 { color: #047857; }
.text-amber-700 { color: #b45309; }

.text-base { font-size: 10.5pt; }
.text-sm { font-size: 9.5pt; }
.text-xs { font-size: 8pt; }
.text-lg { font-size: 12pt; }
.text-xl { font-size: 13pt; }
.text-2xl { font-size: 16pt; }
.text-3xl { font-size: 18pt; }

.leading-relaxed { line-height: 1.55; }
.leading-tight { line-height: 1.25; }
.leading-snug { line-height: 1.35; }

.font-bold { font-weight: 700; }
.font-semibold { font-weight: 600; }
.font-medium { font-weight: 500; }

.tracking-tight { letter-spacing: -0.01em; }
.tracking-wide { letter-spacing: 0.04em; }
.uppercase { text-transform: uppercase; }
.italic { font-style: italic; }
.text-center { text-align: center; }

.max-w-3xl { max-width: 100%; }
.m-0 { margin: 0; }
.mt-0 { margin-top: 0; }
.mt-1 { margin-top: 0.15rem; }
.mt-2 { margin-top: 0.35rem; }
.mb-0 { margin-bottom: 0; }
.mb-1 { margin-bottom: 0.2rem; }
.mb-1\\.5 { margin-bottom: 0.3rem; }
.pt-1 { padding-top: 0.2rem; }
.pt-1\\.5 { padding-top: 0.3rem; }
.pt-2 { padding-top: 0.4rem; }
.px-4 { padding-left: 0.85rem; padding-right: 0.85rem; }
.px-5 { padding-left: 1rem; padding-right: 1rem; }
.px-6 { padding-left: 1.15rem; padding-right: 1.15rem; }
.py-3 { padding-top: 0.55rem; padding-bottom: 0.55rem; }
.py-4 { padding-top: 0.75rem; padding-bottom: 0.75rem; }
.py-5 { padding-top: 0.9rem; padding-bottom: 0.9rem; }
.pl-5 { padding-left: 1.15rem; }
.p-4 { padding: 0.75rem; }

.hidden { display: none; }

h2 {
  color: #1a2b4c;
  page-break-after: avoid;
  break-after: avoid;
}

.enterprise-section-label {
  color: #007bff;
  font-size: 8pt;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin: 0;
}

section {
  page-break-inside: auto;
}

ul, ol {
  margin: 0;
}

.list-disc { list-style-type: disc; }
.list-decimal { list-style-type: decimal; }
.list-none { list-style: none; }

.grid {
  display: grid;
}
.sm\\:grid-cols-2, .grid-cols-2 {
  grid-template-columns: 1fr 1fr;
}
.sm\\:grid-cols-3, .grid-cols-3 {
  grid-template-columns: 1fr 1fr 1fr;
}
.gap-x-8 { column-gap: 1.5rem; }
.gap-y-1 { row-gap: 0.2rem; }
.gap-y-2 { row-gap: 0.4rem; }
.gap-3 { gap: 0.65rem; }
.gap-2 { gap: 0.4rem; }

.flex { display: flex; }
.flex-col { flex-direction: column; }
.flex-row { flex-direction: row; }
.items-start { align-items: flex-start; }
.items-center { align-items: center; }
.justify-center { justify-content: center; }
.flex-shrink-0 { flex-shrink: 0; }
.gap-3 { gap: 0.65rem; }

.border-l-4 { border-left: 4px solid; }
.border-blue-500 { border-color: #3b82f6; }
.bg-slate-50 { background: #f8fafc; }
.rounded-r-lg { border-top-right-radius: 0.5rem; border-bottom-right-radius: 0.5rem; }
.rounded-xl { border-radius: 0.75rem; }
.rounded-lg { border-radius: 0.5rem; }
.rounded-full { border-radius: 9999px; }

blockquote {
  margin: 0 auto;
  max-width: 36rem;
  border-left: 4px solid #3b82f6;
  background: #f8fafc;
  border-top-right-radius: 0.5rem;
  border-bottom-right-radius: 0.5rem;
  padding: 0.75rem 2rem;
  color: #334155;
  font-style: italic;
}

figure {
  margin: 0.1in 0 0.15in;
  page-break-inside: avoid;
  break-inside: avoid;
}
figure img, img.w-full {
  display: block;
  width: 100%;
  height: auto;
  border: 1px solid #e2e8f0;
  border-radius: 0.75rem;
}
figcaption {
  margin-top: 0.35rem;
  text-align: center;
  font-size: 8.5pt;
  color: #64748b;
}

aside {
  page-break-inside: avoid;
  break-inside: avoid;
}
aside.flex {
  display: flex;
  gap: 0.65rem;
  align-items: flex-start;
  border-radius: 0.75rem;
  background: #fffbeb;
  padding: 0.75rem 0.85rem;
  box-shadow: inset 0 0 0 1px #fef3c7;
}
aside .w-9 {
  width: 1.75rem;
  height: 1.75rem;
  border-radius: 9999px;
  background: #fde68a;
  color: #b45309;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  margin-top: 0.1rem;
}
aside svg { width: 0.95rem; height: 0.95rem; }

.border { border-width: 1px; border-style: solid; }
.border-slate-200 { border-color: #e2e8f0; }
.border-emerald-200 { border-color: #a7f3d0; }
.border-blue-200 { border-color: #bfdbfe; }
.border-amber-200 { border-color: #fde68a; }
.bg-emerald-50\\/70 { background: #ecfdf5; }
.bg-blue-50\\/70, .bg-blue-50\\/60 { background: #eff6ff; }
.bg-amber-50\\/70, .bg-amber-50 { background: #fffbeb; }
.bg-\\[\\#1a2b4c\\] { background: #1a2b4c; color: #fff; }
.ring-1 { box-shadow: inset 0 0 0 1px rgba(0,0,0,0.04); }
.ring-amber-100 { box-shadow: inset 0 0 0 1px #fef3c7; }
.shadow-sm { box-shadow: 0 1px 2px rgba(15, 23, 42, 0.05); }

.w-5 { width: 1.1rem; }
.h-5 { height: 1.1rem; }
.w-full { width: 100%; }

a {
  color: #1d4ed8;
  text-decoration: none;
}

/* Hide web-only CTAs in the PDF */
.pdf-hide { display: none !important; }

/* Color chips used for routing outcomes */
.rounded-xl.border.border-emerald-200,
.rounded-xl.border.border-blue-200,
.rounded-xl.border.border-amber-200 {
  page-break-inside: avoid;
}
"""


def strip_front_matter(text: str) -> tuple[dict[str, str], str]:
    meta: dict[str, str] = {}
    if not text.startswith("---"):
        return meta, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return meta, text
    for line in parts[1].strip().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"')
    return meta, parts[2].lstrip("\n")


def resolve_liquid(html: str) -> str:
    def asset_uri(match: re.Match[str]) -> str:
        rel = match.group(1).lstrip("/")
        return (ROOT / rel).as_uri()

    html = re.sub(
        r"\{\{\s*'(/assets/[^']+)'\s*\|\s*relative_url\s*\}\}",
        asset_uri,
        html,
    )
    html = html.replace("{{ site.calendly_url }}", CALENDLY)
    return html


def adapt_for_pdf(html: str) -> str:
    # Fix escaped Tailwind color class written as text-[#1a2b4c] in HTML attributes —
    # keep as-is; CSS below targets via attribute-free utility duplicates where needed.
    # Hide CTA row that links back to the white paper / demo.
    html = re.sub(
        r'<div class="flex flex-col sm:flex-row gap-3 pt-2 justify-center">.*?</div>\s*',
        "",
        html,
        count=1,
        flags=re.S,
    )
    # Escape hatch: map literal text-[#1a2b4c] class tokens for print CSS.
    html = html.replace("text-[#1a2b4c]", "text-navy")
    html = html.replace("bg-[#1a2b4c]", "bg-[#1a2b4c]")
    # Prefer print-friendly line breaks.
    html = html.replace('<br class="hidden sm:block" />', " ")
    return html


def build_html(body_html: str, title: str, author: str, description: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>{title}</title>
  <style>{PRINT_CSS}</style>
</head>
<body>
  <div class="page-footer">DocRouter.AI  ·  Document AI in Practice  ·  docrouter.ai</div>

  <section class="cover">
    <div class="cover-brand">
      <img src="{LOGO.as_uri()}" alt="DocRouter" />
      <div class="cover-brand-text">DocRouter.AI</div>
    </div>
    <div class="cover-eyebrow">White Paper</div>
    <h1>{title}</h1>
    <p class="subtitle">{description}</p>
    <div class="cover-meta">
      <strong>{author}</strong><br />
      August 2026 &nbsp;·&nbsp; Document AI in Practice, Edition 1
    </div>
    <img class="cover-splash" src="{SPLASH.as_uri()}" alt="Document AI decision framework" />
    <div class="cover-footer">
      <span>docrouter.ai</span>
      <span>Building reliable document-processing systems</span>
    </div>
  </section>

  <section class="content">
    {body_html}
  </section>
</body>
</html>
"""


def chrome_print_pdf(html_path: Path, pdf_path: Path) -> None:
    if not CHROME.exists():
        raise FileNotFoundError(f"Google Chrome not found at {CHROME}")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(CHROME),
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        "--print-to-pdf-no-header",
        html_path.as_uri(),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0 or not pdf_path.exists():
        raise RuntimeError(
            "Chrome PDF generation failed.\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}"
        )


def main() -> None:
    raw = POST.read_text(encoding="utf-8")
    meta, body = strip_front_matter(raw)
    body = resolve_liquid(body)
    body = adapt_for_pdf(body)

    title = meta.get("title", "Document AI in Practice")
    author = meta.get("author", "Andrei Radulescu-Banu")
    description = meta.get(
        "description",
        "Uploading a PDF to an LLM is easy. Building reliable document AI is not.",
    )

    html = build_html(body, title, author, description)

    with tempfile.TemporaryDirectory() as tmp:
        html_path = Path(tmp) / "whitepaper.html"
        html_path.write_text(html, encoding="utf-8")
        # Keep a debug copy for inspection if needed
        debug = ROOT / "assets" / "files" / "document-ai-in-practice-whitepaper-debug.html"
        debug.write_text(html, encoding="utf-8")
        chrome_print_pdf(html_path, OUT)

    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
