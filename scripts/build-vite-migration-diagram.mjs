#!/usr/bin/env node
/**
 * Regenerates assets/excalidraw/doc-router-nextjs-to-vite-architecture.excalidraw
 * Layout is hand-measured so labels sit inside boxes and arrows travel through gaps.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const out = path.join(
  __dirname,
  '../assets/excalidraw/doc-router-nextjs-to-vite-architecture.excalidraw',
);

let n = 1;
const elements = [];

function el(partial) {
  elements.push({
    version: 2,
    versionNonce: 8000 + n,
    isDeleted: false,
    fillStyle: 'solid',
    strokeWidth: 2,
    strokeStyle: 'solid',
    roughness: 1,
    opacity: 100,
    angle: 0,
    seed: 9000 + n,
    groupIds: [],
    frameId: null,
    boundElements: [],
    updated: 1,
    link: null,
    locked: false,
    index: `a${n}`,
    ...partial,
  });
  n += 1;
}

function text(id, x, y, content, fontSize, color, width) {
  const lines = content.split('\n').length;
  el({
    type: 'text',
    id,
    x,
    y,
    width,
    height: Math.ceil(fontSize * 1.25 * lines),
    strokeColor: color,
    backgroundColor: 'transparent',
    fontSize,
    fontFamily: 1,
    text: content,
    originalText: content,
    textAlign: 'left',
    verticalAlign: 'top',
    containerId: null,
    autoResize: true,
    lineHeight: 1.25,
  });
}

function box(id, x, y, w, h, stroke, bg) {
  el({
    type: 'rectangle',
    id,
    x,
    y,
    width: w,
    height: h,
    strokeColor: stroke,
    backgroundColor: bg,
    roundness: { type: 3 },
  });
}

function ellipse(id, x, y, w, h, stroke, bg) {
  el({
    type: 'ellipse',
    id,
    x,
    y,
    width: w,
    height: h,
    strokeColor: stroke,
    backgroundColor: bg,
  });
}

/** Cylinder: body drawn first, caps on top. Label sits under it. */
function database(id, x, y) {
  const w = 120;
  const capH = 32;
  const bodyH = 64;
  ellipse(`${id}-bot`, x, y + bodyH - 4, w, capH, '#4f46e5', '#e0e7ff');
  box(`${id}-body`, x, y + capH / 2, w, bodyH, '#4f46e5', '#eef2ff');
  ellipse(`${id}-top`, x, y, w, capH, '#4f46e5', '#c7d2fe');
  text(`${id}-label`, x + 14, y + bodyH + capH + 6, 'Database', 16, '#312e81', 100);
}

function arrow(id, x, y, points, stroke = '#475569', dashed = false) {
  const xs = points.map((p) => p[0]);
  const ys = points.map((p) => p[1]);
  el({
    type: 'arrow',
    id,
    x,
    y,
    width: Math.max(...xs) - Math.min(...xs),
    height: Math.max(...ys) - Math.min(...ys),
    strokeColor: stroke,
    backgroundColor: 'transparent',
    strokeStyle: dashed ? 'dashed' : 'solid',
    roundness: { type: 2 },
    points,
    lastCommittedPoint: null,
    startBinding: null,
    endBinding: null,
    startArrowhead: null,
    endArrowhead: 'arrow',
  });
}

// ---------------------------------------------------------------------------
// BEFORE
// Boxes are placed so the middle arrow crosses the gap between the two
// Next.js boxes instead of running through them.
// ---------------------------------------------------------------------------
box('bef-panel', 16, 12, 1120, 430, '#cbd5e1', '#f8fafc');
text('bef-title', 40, 28, 'Before', 28, '#0f172a', 160);
text(
  'bef-sub',
  140,
  36,
  'The browser talked to the UI, the Next.js server, and FastAPI',
  16,
  '#475569',
  760,
);

box('bef-browser', 48, 100, 160, 240, '#334155', '#ffffff');
text('bef-browser-t', 82, 200, 'Browser', 20, '#0f172a', 110);

box('bef-ui', 300, 96, 260, 92, '#d97706', '#fef3c7');
text('bef-ui-t', 324, 114, 'Next.js UI', 20, '#92400e', 210);
text('bef-ui-s', 324, 146, 'React pages (App Router)', 15, '#78350f', 220);

box('bef-srv', 300, 252, 260, 92, '#d97706', '#fef3c7');
text('bef-srv-t', 324, 270, 'Next.js server', 20, '#92400e', 220);
text('bef-srv-s', 324, 302, 'API routes and session', 15, '#78350f', 220);

box('bef-api', 700, 164, 200, 112, '#2563eb', '#dbeafe');
text('bef-api-t', 752, 190, 'FastAPI', 20, '#1e3a8a', 120);
text('bef-api-s', 728, 222, 'Product API', 15, '#1e40af', 150);

database('bef-db', 980, 168);

// Browser → Next.js UI
arrow('bef-a-ui', 208, 142, [[0, 0], [92, 0]]);
text('bef-l-ui', 214, 116, 'pages', 14, '#64748b', 80);

// Browser → Next.js server
arrow('bef-a-srv', 208, 298, [[0, 0], [92, 0]]);
text('bef-l-srv', 214, 272, 'session', 14, '#64748b', 90);

// Browser → FastAPI, through the gap between the two Next boxes (y = 220)
arrow('bef-a-api', 208, 220, [[0, 0], [492, 0]]);
text('bef-l-api', 575, 194, 'product API', 14, '#64748b', 120);

// Next.js server → FastAPI (dashed), under the product-API line
arrow('bef-a-ss', 560, 320, [[0, 0], [240, 0], [240, -44]], '#94a3b8', true);
text('bef-l-ss', 600, 336, 'server-side calls', 14, '#64748b', 170);

// Both servers reach the database
arrow('bef-a-db1', 900, 220, [[0, 0], [80, 0]], '#4f46e5');
arrow(
  'bef-a-db2',
  430,
  344,
  [[0, 0], [0, 28], [610, 28], [610, -90]],
  '#4f46e5',
);

text(
  'bef-note',
  48,
  400,
  'Next.js server and FastAPI both talked to the database.',
  15,
  '#475569',
  700,
);

// ---------------------------------------------------------------------------
// AFTER
// ---------------------------------------------------------------------------
box('aft-panel', 16, 460, 1120, 380, '#cbd5e1', '#f8fafc');
text('aft-title', 40, 476, 'After', 28, '#0f172a', 140);
text(
  'aft-sub',
  130,
  484,
  'Static SPA in the browser. FastAPI owns what the Next.js server used to do.',
  16,
  '#475569',
  860,
);

box('aft-browser', 48, 556, 160, 180, '#334155', '#ffffff');
text('aft-browser-t', 82, 628, 'Browser', 20, '#0f172a', 110);

box('aft-spa', 300, 544, 300, 120, '#059669', '#d1fae5');
text('aft-spa-t', 324, 560, 'Static SPA', 20, '#065f46', 200);
text('aft-spa-s1', 324, 592, 'Vite build, served by nginx', 15, '#047857', 260);
text('aft-spa-s2', 324, 616, 'Same React UI as before', 15, '#047857', 250);

box('aft-api', 720, 536, 230, 140, '#2563eb', '#dbeafe');
text('aft-api-t', 786, 552, 'FastAPI', 20, '#1e3a8a', 120);
text('aft-api-s1', 744, 584, 'Product API', 15, '#1e40af', 180);
text('aft-api-s2', 744, 608, 'Auth, OAuth, session', 15, '#1e40af', 190);
text('aft-api-s3', 744, 632, 'Next.js server routes, ported', 15, '#1e40af', 200);

database('aft-db', 1000, 552);

// Browser → SPA
arrow('aft-a-spa', 208, 592, [[0, 0], [92, 0]]);
text('aft-l-spa', 214, 566, 'HTML / JS', 14, '#64748b', 90);

// Browser → FastAPI, routed under the SPA so it does not cross the green box
arrow('aft-a-api', 128, 736, [[0, 0], [707, 0], [707, -60]]);
text('aft-l-api', 360, 744, 'API and session cookie', 14, '#64748b', 220);

// Only FastAPI reaches the database
arrow('aft-a-db', 950, 606, [[0, 0], [50, 0]], '#4f46e5');

text(
  'aft-note',
  48,
  780,
  'Only FastAPI talks to the database. There is no Node server in production.',
  15,
  '#475569',
  780,
);

const doc = {
  type: 'excalidraw',
  version: 2,
  source: 'https://excalidraw.com',
  elements,
  appState: {
    gridSize: 20,
    gridStep: 5,
    gridModeEnabled: false,
    viewBackgroundColor: '#ffffff',
  },
  files: {},
};

fs.writeFileSync(out, JSON.stringify(doc, null, 2));
console.log(`Wrote ${out} (${elements.length} elements)`);
