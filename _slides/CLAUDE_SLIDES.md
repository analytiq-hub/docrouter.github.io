# CLAUDE_DESIGN.md
## Slide Design Contract (Markdown → Slides)

This document defines non-negotiable design rules for generating slide decks.
Claude must follow these rules by default when producing slides, slide CSS, or slide content.

---

## 1. Design Philosophy

Slides are:

- Visual arguments, not documents
- Sparse, not verbose
- Readable from 10 feet away
- One idea per slide

Design should feel:

- Calm
- Modern
- Intentional
- Professional (investor / exec / technical audience)

---

## 2. Slide Structure Rules

### 2.1 One Thought Per Slide

Each slide should express one primary idea.

❌ Multiple paragraphs
❌ Dense bullet lists
❌ Long explanations

✅ Headline + 2–4 short bullets
✅ Headline + diagram
✅ Headline + single sentence

### 2.2 Headline-First Slides

Every slide must start with a strong headline, not a label.

❌ "Problem"
❌ "Architecture"

✅ "Manual workflows don't scale"
✅ "Schema-first extraction enables reliability"

---

## 3. Typography System

### 3.1 Font Priorities

Claude should assume:

- Sans-serif
- Neutral, modern
- High x-height

Preferred defaults:

- Inter
- System UI stack

### 3.2 Type Scale (Required)

Use a clear hierarchy:

| Element | Size |
|---------|------|
| Title | 2.2–2.6rem |
| Section | 1.6–1.9rem |
| Body | 1.0–1.2rem |
| Caption | 0.8–0.9rem |

Use `clamp()` for responsive scaling when possible.

```css
h1 {
  font-size: clamp(2.2rem, 4vw, 2.6rem);
  line-height: 1.15;
}
```

### 3.3 Line Length & Density

- Max 60–70 characters per line
- Prefer short phrases over full sentences
- Avoid punctuation where possible

---

## 4. Spacing & Layout

### 4.1 Spacing System (8px Rhythm)

All spacing must follow this scale:

- 4px
- 8px
- 16px
- 24px
- 32px
- 48px
- 64px

No arbitrary spacing values.

### 4.2 Layout Rules

- Use grid for slide structure
- Use flex for internal alignment
- Prefer asymmetry over centering everything
- Leave negative space intentionally

Example:

```css
.slide {
  display: grid;
  grid-template-columns: 1fr;
  padding: 48px;
}
```

---

## 5. Color System

### 5.1 Palette Rules

Slides must use a limited palette:

- Background
- Surface
- Primary accent
- Muted text

Example:

```css
--color-bg: #0b0b0c;
--color-surface: #141416;
--color-primary: #5b8cff;
--color-muted: #9ca3af;
```

### 5.2 Color Usage Guidelines

- Use accent color only for emphasis
- Never color entire paragraphs
- Prefer contrast over decoration

---

## 6. Visual Hierarchy

Claude must ensure:

- Headline dominates the slide
- Supporting content is visually secondary
- No competing focal points

If a slide feels busy, remove content.

---

## 7. Bullets & Lists

### 7.1 Bullet Rules

- Max 4 bullets per slide
- Each bullet ≤ 8 words
- No punctuation at the end of bullets

❌ Long explanations
❌ Nested bullet lists

### 7.2 Icon Usage (Optional)

Icons may be used if:

- Simple
- Consistent
- Meaningful

Never decorative.

---

## 8. Motion & Transitions

Motion should be:

- Subtle
- Functional
- Rare

Recommended:

```css
transition: all 180ms ease-out;
```

Avoid:

- Bounce
- Dramatic easing
- Long animations

---

## 9. Code & Diagrams

### 9.1 Code Slides

- Show only the essential lines
- Highlight the concept, not syntax
- Prefer pseudo-code when possible

### 9.2 Diagrams

- Prefer simple box-and-arrow layouts
- Label relationships clearly
- Avoid excessive detail

---

## 10. Slide Count Guidance

- 1 idea = 1 slide
- 10–12 slides for a short talk
- 15–20 slides for a full presentation

If content exceeds this, split the deck.

---

## 11. Export Assumptions

Claude should assume slides may be exported to:

- PDF
- HTML
- PPTX (via Pandoc)

Avoid:

- Fixed pixel positioning
- Overflow-dependent layouts

---

## 12. Default Behavior Checklist

Before finalizing a slide deck, Claude should verify:

- [ ] Every slide has a clear headline
- [ ] No slide exceeds visual capacity
- [ ] Spacing follows the 8px system
- [ ] Typography hierarchy is clear
- [ ] Colors are minimal and intentional
- [ ] Slides are readable from a distance

---

## 13. When in Doubt

When uncertain:

- Reduce content
- Increase whitespace
- Simplify language
- Prefer clarity over cleverness

---

## Final Rule

**Slides are for presenting ideas, not storing information.**
