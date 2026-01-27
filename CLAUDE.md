# Claude Code Development Notes

This file tracks development decisions, patterns, and conventions for this Jekyll site.

## Source Code Reference

**Important:** The source code for DocRouter.AI is checked out in `../doc-router` (relative to this repository).

When creating documentation or marketing material for this site, you should browse the `../doc-router` directory to:
- Understand the project structure and architecture
- Learn about features, APIs, and capabilities
- Ensure documentation accuracy and completeness
- Reference actual code examples and implementations

This helps maintain consistency between the documentation site and the actual product.

## DocRouter Workflow Understanding

**Key Technical Insight:** Tags are required for prompts to trigger on documents. The correct onboarding workflow is:
1. Create a tag and a prompt (categorization and extraction instructions)
2. Upload documents with the tag applied
3. See automatic extraction results

This counter-intuitive but efficient flow ensures immediate results for new users.

**Email Campaign Strategy:**
- **Onboarding (Registered Users):** 3 emails over 7 days - progressive learning from setup to advanced features
- **Prospects (Non-Registered):** 2 emails max - focus on demo booking, not product education
- **Investor/Friends Newsletter:** Quarterly - relationship building and milestone updates
- **Product Updates Newsletter:** Bi-weekly/monthly - feature announcements and user education
- **Educational Series:** Monthly - build expertise and engagement

**Future Campaigns:**
- **Re-engagement:** 3 emails over 14 days - bring back inactive users (when retention becomes priority)
- **Referral Program:** 3 emails - leverage users for growth (when scale requires user acquisition)

## Include File Architecture

### Overview
The site uses a modular include file structure that separates theme-specific components from site-specific customizations.

### File Structure
```
_includes/
├── head.html           → custom-head.html
├── header.html         → custom-header.html  
└── footer.html         → custom-footer.html
```

### Theme vs. Custom Content Division

#### Theme Files (Reusable/Portable)
**`head.html`:**
- Tailwind CSS CDN and configuration
- Highlight.js syntax highlighting setup
- Responsive viewport meta tags
- Jekyll SEO and feed meta tags
- Core fonts (JetBrains Mono, Inter)
- Standard Jekyll integrations

**`header.html`:**
- Responsive navigation structure
- Mobile hamburger menu with JavaScript
- Dropdown menu functionality
- Tailwind utility classes for layout
- Navigation component architecture

**`footer.html`:**
- Responsive grid layout
- RSS feed integration
- Social media hooks
- Standard author/contact patterns

#### Custom Files (Site-Specific)
**`custom-head.html`:**
- Google Analytics (moved from head.html)
- Site-specific meta tags
- Custom favicons
- Additional tracking codes
- Site-specific fonts/styling

**`custom-header.html`:**
- Site announcements
- Additional navigation items
- Search functionality
- Custom branding elements

**`custom-footer.html`:**
- Copyright notices
- Privacy/terms links
- Newsletter signup
- Legal disclaimers
- Additional contact info

### Usage Guidelines
1. **Keep theme files portable** - Avoid site-specific content
2. **Use custom files for personalization** - Analytics, branding, site-specific features
3. **Maintain consistent patterns** - Each major section has theme + custom pair
4. **Document customizations** - Add comments explaining site-specific additions

This architecture allows for easy theme updates while preserving site customizations.