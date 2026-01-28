# Email Campaign Plan for DocRouter.AI

## Overview

This document outlines the active email campaigns and their templates:
1. **Onboarding Campaign** - 3 emails for users who have registered an account
2. **Prospect Campaign** - 2 emails for potential users interested in DocRouter.AI
3. **Investor/Friends Newsletter** - Updates for investors, advisors, and close contacts
4. **Product Updates Newsletter** - 3 template types for registered users (features, tips, deep dive)

### Active Templates (9 total)
- `onboarding-email-1-upload-tailor-results.html` - Tag, prompt, upload workflow
- `onboarding-email-2-schemas.html` - Schema creation and usage
- `onboarding-email-3-checkin.html` - Week 1 check-in and support
- `prospect-email-1-demo-invitation.html` - Initial demo invitation
- `prospect-email-2-followup.html` - Follow-up demo reminder
- `investor-newsletter.html` - Strategic updates
- `updates-features.html` - New feature announcements
- `updates-tips.html` - Best practices and tips
- `updates-deep-dive.html` - Monthly educational content

### Future Campaigns (For Later Implementation)
- **Re-engagement Campaign** - For inactive users to return to the platform
- **Referral Program** - Leverage users to bring in new customers

---

## Email Templates Overview

| Campaign | Template | Subject Line | Preview Text |
|----------|----------|--------------|--------------|
| **Onboarding** | Email 1: Tag, Prompt, Upload | "DocRouter.AI: Tag, prompt, upload - Get started in 4 steps 📄" | Welcome to DocRouter.AI! Create a tag and a prompt, upload a document, and see your first extraction in minutes. |
| **Onboarding** | Email 2: Learn About Schemas | "DocRouter.AI: Learn about schemas for document extraction 🤖" | Schemas ensure consistent, validated output from your prompts. Learn how to create and use them effectively. |
| **Onboarding** | Email 3: Customer Success Check | "How's your DocRouter.AI journey going? We're here to help 👋" | You've been using DocRouter.AI for a week. We're here to help with questions and hear how it's working for you. |
| **Prospect** | Email 1: Introduction & Demo Invitation | "DocRouter.AI: Transform Your Document Processing with AI" | See how DocRouter.AI extracts data from unstructured documents with AI. Book a free demo to learn more. |
| **Prospect** | Email 2: Follow-up Demo Reminder | "Ready to See DocRouter.AI in Action?" | Book your free demo and discover how DocRouter.AI can transform your document processing workflow. |
| **Investor** | Newsletter | "DocRouter.AI Update: [Update Title]" | Update on DocRouter.AI progress, milestones, and strategic updates for our valued partners. |
| **Product Updates** | Feature Release | "DocRouter.AI: New Feature - [Feature Name]" | Exciting new feature announcement with details and benefits for DocRouter.AI users. |
| **Product Updates** | Tips & Best Practices | "DocRouter.AI Tip: [Tip Title]" | Educational content and best practices to get more value from DocRouter.AI. |
| **Product Updates** | Deep Dive | "DocRouter.AI Deep Dive: [Topic]" | Monthly educational content on advanced DocRouter.AI features and techniques. |

---

## Campaign Details

### Onboarding Campaign
**Goal:** Guide new users through their first steps with DocRouter.AI
**Audience:** New registered users
**Cadence:** 3 emails over 7 days

### Prospect Campaign
**Goal:** Convert prospects into demo bookings
**Audience:** Interested leads
**Cadence:** 2 emails over 3-5 days

### Investor/Friends Newsletter
**Goal:** Maintain relationships and share strategic updates
**Audience:** Investors, advisors, close contacts
**Cadence:** As needed

### Product Updates Newsletter
**Goal:** Keep users informed about features and improvements
**Audience:** Registered users
**Cadence:** Bi-weekly to monthly

### Product Updates - Deep Dive
**Goal:** Build expertise and engagement through advanced content
**Audience:** Active users
**Cadence:** Monthly

---

## Implementation Notes

### Email Service Provider Setup (Brevo)
- Create custom contact attributes for personalization
- Set up automation workflows for each campaign
- Configure transactional email sending for verification/password reset
- Sync user data from DocRouter to Brevo contacts

### Template Variables & Personalization
- Use `{{ contact.* }}` attributes for user-specific content
- Use `{{ params.* }}` for dynamic content (URLs, counts, etc.)
- Implement conditional logic for personalized experiences
- Test all templates across email clients (Gmail, Outlook, Apple Mail)

### Analytics & Optimization
- Track open rates, click-through rates, conversions
- A/B test subject lines and content variations
- Monitor unsubscribe rates and engagement metrics
- Adjust campaign frequency based on performance data

---

## File Naming Convention

For email templates:

**Onboarding Campaign (Registered Users):**
- `onboarding-email-1-upload-tailor-results.html` - Email 1 (Day 0): Create tag and prompt, upload with tag, see results
- `onboarding-email-2-schemas.html` - Email 2 (Day 3): Learn about schemas
- `onboarding-email-3-checkin.html` - Email 3 (Day 7): Customer success check

**Prospect Campaign (Non-Registered Users):**
- `prospect-email-1-demo-invitation.html` - Email 1 (Day 0): Introduction & demo invitation
- `prospect-email-2-followup.html` - Email 2 (Day 3-5): Follow-up demo reminder

**Investor/Friends Newsletter:**
- `investor-newsletter.html` - Comprehensive updates

**Product Updates Newsletter:**
- `updates-features.html` - New feature announcements
- `updates-tips.html` - Educational content and tips

**Educational Series:**
- `updates-deep-dive.html` - Single reusable template for monthly educational content

**Future Campaigns (Templates for Later):**
- `reengagement-email-*.html` - Re-engagement sequence templates
- `referral-program-*.html` - Referral program templates

---

## Next Steps

1. **Set up Brevo custom attributes** (see Implementation Notes above)
2. **Create email templates** for each email in the sequence using Brevo attribute syntax
3. **Set up Brevo automation workflows** for campaign emails (onboarding & prospect sequences)
4. **Integrate Brevo API/SMTP** for transactional emails (verification, password reset)
5. **Sync contact data** from DocRouter to Brevo (on registration, activity updates)
6. **Set up email triggers** in the application to update Brevo contact attributes
7. **Test email delivery** across different email clients
8. **Monitor and optimize** using Brevo analytics (open rates, click rates, conversions)

**Content:**
- Common use cases (invoice processing, form extraction, etc.)
- Industry applications
- ROI and efficiency gains
- Case studies or examples (if available)
- Before/after scenarios

**Key Sections:**
- "Real-World Applications"
- "Industries We Serve"
- "The Impact: Time & Cost Savings"
- "Example Workflows"
- CTA: "Try It Yourself" or "Schedule a Demo"

**Subject Line:**
"How Companies Use DocRouter to Save Time & Money"

**Preview Text:**
See real-world applications: invoice processing, form extraction, and automated workflows that deliver ROI.

---

#### Email 4: Technical Overview & Getting Started (Day 10)
**Trigger:** 10 days after initial contact

**Purpose:** Provide technical details for technical decision-makers.

**Content:**
- Tech stack overview
- Installation options (Docker, AWS, local)
- API and SDK capabilities
- Integration examples
- Security and compliance
- Open-source benefits

**Key Sections:**
- "Built for Developers"
- "Flexible Deployment"
- "Powerful APIs & SDKs"
- "Security & Compliance"
- "Open Source Advantage"
- CTA: "View Documentation" or "Start Building"

**Subject Line:**
"Built for Developers: DocRouter Technical Overview"

**Preview Text:**
Flexible deployment options, powerful APIs, Python/TypeScript SDKs, and open-source architecture for developers.

---

#### Email 5: Final Call to Action (Day 14)
**Trigger:** 14 days after initial contact

**Purpose:** Final encouragement to sign up with special offer or urgency.

**Content:**
- Recap of key benefits
- Limited-time offer (if applicable)
- Clear next steps
- Address common objections
- Support availability

**Key Sections:**
- "Ready to Get Started?"
- "What's Next?"
- "We're Here to Help"
- CTA: "Create Free Account" (primary) + "Schedule Demo" (secondary)

**Subject Line:**
"DocRouter.AI: Ready to Transform Your Document Workflow?"

**Preview Text:**
Get started with DocRouter.AI today. Create your free account or schedule a demo to see it in action.

---

## Campaign 3: Investor/Friends Newsletter

### Goal
Maintain relationships with investors, advisors, and close contacts through regular updates on DocRouter.AI progress and milestones.

### Target Audience
Investors, advisors, mentors, and close professional contacts who want to stay updated on DocRouter.AI's journey.

### Email Schedule
As needed - focused on major milestones and strategic updates.

### Email Content Structure

#### Updates
**Subject Line Examples:**
- "DocRouter.AI Update: Major Milestones & What's Next"
- "DocRouter.AI Update: Progress, Partnerships & Plans"
- "Behind the Scenes: Building DocRouter.AI's Future"

**Content Focus:**
- Key milestones achieved (user growth, partnerships, funding)
- DocRouter.AI product development updates (high-level, not technical)
- Team growth and hires
- Industry insights and market trends
- Challenges overcome and lessons learned
- Future plans and goals

**Tone:** Casual, authentic, relationship-focused

**Key Sections:**
- "What's New This Month"
- "Team & Company Updates"
- "Industry Insights"
- "What's Next"
- Personal note from founder

---

## Campaign 4: Product Updates Newsletter

### Goal
Keep registered users informed about new features, improvements, and important updates to reduce support inquiries and increase engagement.

### Target Audience
All registered DocRouter users who have opted into product updates.

### Email Schedule
Bi-weekly or monthly, depending on update frequency.

### Email Content Structure

#### Feature Release (`updates-features.html`)
**Subject Line Examples:**
- "DocRouter.AI: New Feature - [Feature Name]"
- "New Feature: Advanced Schema Validation"

**Content Structure:**
- Feature announcement
- Key benefits (3 customizable)
- How it works (3 steps)
- CTA to try feature
- Uses params: `feature_name`, `feature_description`, `benefit_1-3`

**Tone:** Professional, helpful, user-focused

#### Tips & Best Practices (`updates-tips.html`)
**Subject Line Examples:**
- "DocRouter.AI Tip: [Tip Title]"
- "DocRouter.AI Tip: Improve Extraction Accuracy by 30%"

**Content Structure:**
- Tip introduction
- The tip explanation
- Why it works (3 reasons)
- Related articles
- Quick tip section
- CTA to update prompts
- Uses params: `tip_title`, `main_tip`, `tip_explanation`, `why_1-3`, `quick_tip`

---

## Newsletter Implementation Notes

### Segmentation & Personalization
- **Investor Newsletter:** Highly personalized with specific updates relevant to each contact's interests
- **Product Updates:** Segmented by user type (free vs paid, active vs inactive) and feature usage

### Opt-in & Compliance
- Both newsletters require explicit opt-in
- Clear unsubscribe options in every email
- GDPR/CCPA compliant with data usage transparency

### Analytics & Optimization
- Track open rates, click-through rates, and unsubscribe rates
- A/B test subject lines and content structure
- Monitor engagement to adjust frequency and content

### Content Calendar
- **Investor Newsletter:** Plan 3 months in advance, align with board meetings and investor updates
- **Product Updates:** Release-driven, supplement with educational content during quiet periods

---

## Future Campaigns

### Campaign 5: Re-engagement Campaign (Future)

### Goal
Re-activate inactive users and bring them back to the platform.

### Target Audience
Users who haven't logged in for 30+ days or haven't uploaded documents recently.

### Email Sequence

#### Email 1: Gentle Re-engagement (Day 0)
**Subject:** "We Miss You at DocRouter - Here's What's New"
**Content:** Update on new features, gentle reminder of value, easy re-entry

#### Email 2: Value Reminder (Day 7)
**Subject:** "Quick Win: Process One Document in 2 Minutes"
**Content:** Simple tutorial, success story, clear next steps

#### Email 3: Final Attempt (Day 14)
**Subject:** "Your DocRouter Account - Last Chance to Save Progress"
**Content:** Warning about potential data loss, special offer, final CTA

---

## Product Updates - Deep Dive

### Goal
Build expertise and demonstrate thought leadership while keeping users engaged.

### Target Audience
Active users who want to get more value from DocRouter.

### Email Schedule
Monthly - Single reusable template (`updates-deep-dive.html`) with customizable content.

### Template Structure
- Topic introduction
- Key principles/content
- Resources section
- CTA to try feature
- Uses params: `series_topic`, `topic_intro`, `main_heading`, `main_content`, `principle_1-4`, `cta_button`

### Campaign 6: Referral Program (Future)

### Goal
Leverage existing users to bring in new customers through referrals.

### Target Audience
Highly engaged users (high document volume, long tenure).

### Email Sequence

#### Email 1: Program Introduction
**Subject:** "Get Free DocRouter Credits by Referring Friends"
**Content:** Explain referral program, benefits, how it works

#### Email 2: Success Story (if they haven't referred yet)
**Subject:** "How [User] Earned $500 in DocRouter Credits"
**Content:** Case study of successful referrer, program reminder

#### Email 3: Limited Time Boost (if still no referrals)
**Subject:** "Double Referral Credits - Limited Time"
**Content:** Temporary bonus offer to encourage participation

---

## Email Template Structure

### Design Principles (Inspired by Brevo)
1. **Alternating Background Colors** - Use white and light colored backgrounds (e.g., #f8f9fa) to create visual separation between sections
2. **Clear Visual Hierarchy** - Each section should be distinct and scannable
3. **Progressive Disclosure** - Start with foundational concepts, then build to specific tasks
4. **Practical Tips** - Include actionable tips with checkmarks (✓) for easy scanning
5. **Support Accessibility** - Always include a "Need a hand?" section with support links
6. **Professional but Friendly Tone** - Approachable language that doesn't overwhelm

### Standard Sections (All Emails)
1. **Header** - Logo/branding, gradient background (optional)
2. **Section 1 (White background)** - Personal greeting, introduction, primary CTA
3. **Section 2 (Light background)** - "How it works" with step-by-step guide or visual reference
4. **Section 3 (White background)** - Tips, best practices, or additional information with checkmarks
5. **Section 4 (Light background)** - "Need a hand?" support section
6. **Footer** - Copyright, unsubscribe (`{{ unsubscribe }}`), social links, "View in browser" (`{{ mirror }}`)

### Visual Elements
- **Checkmarks (✓)** for tips and best practices
- **Numbered steps** for process guides
- **Clear CTAs** - Primary action button, secondary text links
- **Illustration references** - Mention visuals/animations that would be in the actual HTML
- **Color scheme** - Primary brand color (#0070f3 blue) for CTAs, alternating white/light backgrounds

### Brevo Template Variables

#### Contact Attributes (Campaigns & Automations)
Use these for personalization in all emails:

**Built-in Contact Attributes:**
- `{{ contact.FIRSTNAME }}` - User's first name
- `{{ contact.LASTNAME }}` - User's last name
- `{{ contact.EMAIL }}` - User's email address
- `{{ contact.COMPANY }}` - Company/organization name
- `{{ contact.CITY }}` - City
- `{{ contact.COUNTRY }}` - Country
- `{{ contact.STATE }}` - State/Province

**With Fallback (Recommended):**
- `{{ contact.FIRSTNAME | default: 'there' }}` - Safe greeting if name missing
- `{{ contact.COMPANY | default: 'your organization' }}` - Safe company reference

**Custom Contact Attributes (to be created in Brevo):**
- `{{ contact.organization_name }}` - DocRouter organization name (for registered users)
- `{{ contact.user_role }}` - User role (admin, user, etc.)
- `{{ contact.signup_date }}` - Account creation date
- `{{ contact.documents_uploaded }}` - Count of uploaded documents
- `{{ contact.prompts_created }}` - Count of created prompts
- `{{ contact.last_activity_date }}` - Last activity timestamp

#### Transactional Email Attributes (API/SMTP)
Use `{{ params.* }}` for dynamic data passed via API:

**For Welcome/Verification Emails:**
- `{{ params.verification_url }}` - Email verification link
- `{{ params.site_url }}` - Base URL of the site
- `{{ params.organization_name }}` - Organization name

**For Onboarding Emails:**
- `{{ params.site_url }}` - Base URL for CTAs
- `{{ params.document_count }}` - Number of documents uploaded (if applicable)
- `{{ params.prompt_count }}` - Number of prompts created (if applicable)
- `{{ params.dashboard_url }}` - Direct link to user dashboard

**For Prospect Emails:**
- `{{ params.site_url }}` - Base URL for CTAs
- `{{ params.signup_url }}` - Direct signup link
- `{{ params.demo_url }}` - Link to schedule demo

#### System Attributes (Mandatory)
- `{{ unsubscribe }}` - Unsubscribe link (required in footer)
- `{{ update_profile }}` - Manage preferences link
- `{{ mirror }}` - View in browser link

#### Sender Attributes
- `{{ sender.name }}` - Sender name
- `{{ sender.email }}` - Sender email
- `{{ sender.company }}` - Sender company
- `{{ sender.address }}` - Sender address

#### Conditional Logic (Advanced)
```html
{% if contact.FIRSTNAME %}
  Hi {{ contact.FIRSTNAME }},
{% else %}
  Hi there,
{% endif %}
```

```html
{% if contact.documents_uploaded > 0 %}
  We noticed you've uploaded {{ contact.documents_uploaded }} documents!
{% endif %}
```

### Recommended Attribute Usage by Email Type

**Onboarding Emails (Registered Users):**
- Greeting: `{{ contact.FIRSTNAME | default: 'there' }}`
- Organization: `{{ contact.organization_name | default: contact.COMPANY | default: 'your organization' }}`
- Dynamic data: Use `{{ params.* }}` for site URLs, counts, etc.

**Prospect Emails (Non-Registered):**
- Greeting: `{{ contact.FIRSTNAME | default: 'there' }}`
- Company: `{{ contact.COMPANY | default: 'your company' }}`
- Dynamic data: Use `{{ params.* }}` for signup URLs, demo links, etc.

---

## Implementation Notes

### Brevo Setup Requirements

**1. Create Custom Contact Attributes**
Before implementing the email campaigns, create these custom attributes in Brevo:
- Go to **Contacts → Attributes → Add Attribute**
- Create the following attributes:
  - `organization_name` (Text) - DocRouter organization name
  - `user_role` (Text) - User role (admin, user, etc.)
  - `signup_date` (Date) - Account creation date
  - `documents_uploaded` (Number) - Count of uploaded documents
  - `prompts_created` (Number) - Count of created prompts
  - `last_activity_date` (Date) - Last activity timestamp

**2. Sync Contact Data**
- When users register, sync their data to Brevo contacts
- Update custom attributes when users perform actions (upload docs, create prompts)
- Use Brevo API or webhooks to keep contact data in sync

**3. Transactional Email Setup**
- For transactional emails (welcome, verification), use Brevo SMTP/API
- Pass dynamic data via `params` object in API calls
- Example API payload structure:
  ```json
  {
    "to": [{ "email": "user@example.com" }],
    "params": {
      "verification_url": "https://docrouter.ai/auth/verify?token=...",
      "site_url": "https://docrouter.ai",
      "organization_name": "Acme Corp"
    }
  }
  ```

**4. Campaign vs Transactional**
- **Campaign emails** (onboarding sequence, prospect sequence): Use Brevo Campaigns/Automations with contact attributes
- **Transactional emails** (verification, password reset): Use Brevo SMTP/API with `params`

### Design Approach (Lessons from Brevo)
- **Start with foundation, not tasks:** Email 1 focuses on understanding the workflow before jumping into tasks
- **Alternating backgrounds:** Use white and light colored backgrounds (#f8f9fa or similar) to create visual separation
- **Scannable sections:** Each section should be distinct and easy to scan
- **Progressive disclosure:** Build knowledge progressively - foundation → basic tasks → advanced features
- **Practical tips with checkmarks:** Use ✓ symbols for actionable tips that are easy to scan
- **Support always accessible:** Include "Need a hand?" section in every email
- **Professional but friendly tone:** Approachable language that doesn't overwhelm

### Timing Considerations
- **Onboarding emails:** Send based on user actions (uploaded docs, created prompts) when possible, with time-based fallbacks
- **Prospect emails:** Time-based sequence, but pause if user registers
- **Respect user preferences:** Always include `{{ unsubscribe }}` link and honor opt-outs

### Personalization
- **Use Brevo contact attributes** for personalization:
  - Greeting: `{{ contact.FIRSTNAME | default: 'there' }}`
  - Organization: `{{ contact.organization_name | default: contact.COMPANY }}`
- **Use conditional logic** to personalize content based on user activity:
  - `{% if contact.documents_uploaded > 0 %}` - Reference actual uploads
  - `{% if contact.prompts_created > 0 %}` - Reference prompt creation
- **Use transactional params** for dynamic links and counts:
  - `{{ params.document_count }}` - Show actual document count
  - `{{ params.dashboard_url }}` - Direct links to specific pages
- **Track engagement** in Brevo and adjust sequence accordingly
- **For registered users:** Reference their actual activity using custom attributes

### A/B Testing Opportunities
- Subject lines
- CTA button text and placement
- Email length (short vs. detailed)
- Visual design elements

### Metrics to Track
- Open rates
- Click-through rates (CTAs)
- Conversion rates (sign-ups, document uploads, prompt creation)
- Unsubscribe rates
- Time to first action (upload, prompt creation)

---

## Next Steps

1. **Set up Brevo custom attributes** (see Implementation Notes above)
2. **Create email templates** for each email in the sequence using Brevo attribute syntax
3. **Set up Brevo automation workflows** for campaign emails (onboarding & prospect sequences)
4. **Integrate Brevo API/SMTP** for transactional emails (verification, password reset)
5. **Sync contact data** from DocRouter to Brevo (on registration, activity updates)
6. **Set up email triggers** in the application to update Brevo contact attributes
7. **Test email delivery** across different email clients
8. **Monitor and optimize** using Brevo analytics (open rates, click rates, conversions)

---

## File Naming Convention

For email templates:

**Onboarding Campaign (Registered Users):**
- `onboarding-email-1-upload-tailor-results.html` - Email 1 (Day 0): Create tag and prompt, upload with tag, see results
- `onboarding-email-2-schemas.html` - Email 2 (Day 3): Learn about schemas
- `onboarding-email-3-checkin.html` - Email 3 (Day 7): Customer success check

**Prospect Campaign (Non-Registered Users):**
- `prospect-email-1-demo-invitation.html` - Email 1 (Day 0): Introduction & demo invitation
- `prospect-email-2-followup.html` - Email 2 (Day 3-5): Follow-up demo reminder

**Investor/Friends Newsletter:**
- `investor-newsletter.html` - Comprehensive updates

**Product Updates Newsletter:**
- `updates-features.html` - New feature announcements
- `updates-tips.html` - Educational content and tips

**Educational Series:**
- `updates-deep-dive.html` - Single reusable template for monthly educational content

**Future Campaigns (Templates for Later):**
- `reengagement-email-*.html` - Re-engagement sequence templates
- `referral-program-*.html` - Referral program templates

---

## Documentation Links in Templates

All documentation links in email templates point to `https://docrouter.ai/docs/*`. The following documentation pages are referenced:

### Core Documentation Pages
- `/docs` - Main documentation index (used in: updates-features, onboarding-email-3-checkin, onboarding-email-1-upload-tailor-results for knowledge bases)
- `/docs/schemas` - Schema documentation (used in: onboarding-email-1, onboarding-email-2, updates-tips, updates-deep-dive)
- `/docs/prompts` - Prompts guide (used in: updates-tips, updates-deep-dive)
- `/docs/rest-api` - REST API documentation (used in: onboarding-email-1, onboarding-email-2, onboarding-email-3)
- `/docs/webhooks` - Webhooks/workflows documentation (used in: onboarding-email-1, onboarding-email-2, onboarding-email-3)
- `/docs/mcp` - MCP/Claude Code documentation (used in: onboarding-email-1, onboarding-email-2)

### Documentation Needs Identified

**Missing or Needs Clarification:**
1. **Knowledge Bases** - Referenced in onboarding-email-1 but links to generic `/docs`. Needs dedicated page or section.
2. **Tags** - Core workflow concept (Tag → Prompt → Upload) mentioned in emails but no dedicated documentation page.
3. **N8N Integration** - Referenced in onboarding-email-2 but links to generic `/docs/webhooks`. May need dedicated section or page.
4. **Temporal Workflows** - Referenced in onboarding-email-2 but links to generic `/docs/webhooks`. May need dedicated section or page.

**Documentation Strategy to Avoid Repetition:**
- Create a single comprehensive guide for each topic
- Use cross-references between related topics
- Structure documentation hierarchically:
  - Quick Start → Tags → Prompts → Schemas
  - How It Works → Tags → Prompts → Schemas → Workflows
  - API Documentation → REST API → Webhooks → SDKs
- Each email should link to the most relevant documentation page, not duplicate content

---

## Template Inconsistencies & Issues

### URL Parameter Inconsistencies
1. **`params.site_url` usage:**
   - Some templates use `{{ params.site_url }}` without defaults (onboarding emails)
   - Some use `{{ params.site_url | default: 'https://docrouter.ai' }}` (prospect emails, updates)
   - **Recommendation:** Standardize to always include defaults for reliability

2. **App vs. Site URLs:**
   - Some CTAs point to `app.docrouter.ai` (updates-features, updates-tips, updates-deep-dive)
   - Some point to `docrouter.ai` (onboarding emails use `params.site_url`)
   - **Recommendation:** Use `params.site_url` consistently, or create separate `params.app_url` parameter

3. **Newsletter Preferences:**
   - Some templates use `{{ params.site_url }}/newsletter` (updates-tips, updates-deep-dive)
   - Should use `{{ update_profile }}` (Brevo system attribute) for consistency
   - **Recommendation:** Replace with `{{ update_profile }}` in all templates

### Documentation Link Inconsistencies
1. **Knowledge Bases:**
   - Links to generic `/docs` instead of specific page
   - **Action:** Create `/docs/knowledge-bases` or add section to existing docs

2. **Workflow Documentation:**
   - N8N and Temporal both link to `/docs/webhooks`
   - **Action:** Either create separate pages or add clear sections within webhooks doc

3. **MCP vs. Claude Code:**
   - Templates mention "Claude Code" but link to `/docs/mcp`
   - **Action:** Ensure documentation clarifies MCP = Claude Code integration, or update template language

### Content Inconsistencies
1. **Footer Links:**
   - Most templates: "View in browser | Contact us | Unsubscribe"
   - Some use "Newsletter Preferences" instead of "Contact us"
   - **Recommendation:** Standardize footer across all templates

2. **Support Links:**
   - Some use `{{ params.site_url }}/support`
   - Some use `{{ params.site_url }}/contact`
   - **Recommendation:** Determine if both pages exist and use consistently

3. **Feedback Links:**
   - Only onboarding-email-3-checkin has feedback link (`/feedback`)
   - **Action:** Verify if this page exists or should be added to other templates

---

## Template Content Summary

### Onboarding Email 1: Tag, Prompt, Upload
**Key Content:**
- 4-step workflow: Create tag → Create prompt → Upload documents → See results
- Learn more section: Schemas, REST API, Workflows, Claude Code, Knowledge Bases
- Links to: `/docs/schemas`, `/docs/rest-api`, `/docs/webhooks`, `/docs/mcp`, `/docs` (knowledge bases)

### Onboarding Email 2: Learn About Schemas
**Key Content:**
- What schemas are and their benefits
- 5-step schema creation process
- Example schema code
- Pro tip: Use Claude Code
- Workflows: N8N Integration, Temporal Workflows
- Links to: `/docs/mcp`, `/docs/webhooks`, `/docs/rest-api`

### Onboarding Email 3: Check-in
**Key Content:**
- Pro tip about prompt refinement
- Common questions: accuracy, automation, document types, MCP server, help
- Support section with documentation links
- Feedback request
- Links to: `/docs`, `/docs/rest-api`, `/docs/webhooks`

### Prospect Email 1: Demo Invitation
**Key Content:**
- Value proposition
- Problem/solution framing
- Social proof
- Demo CTA
- No documentation links (prospect-focused)

### Prospect Email 2: Follow-up
**Key Content:**
- Follow-up message
- Demo benefits
- Social proof/testimonial
- Demo CTA
- No documentation links (prospect-focused)

### Updates - Features
**Key Content:**
- Feature announcement
- Benefits list
- How it works (3 steps)
- CTA to try feature
- Links to: `/docs` (main documentation)

### Updates - Tips
**Key Content:**
- Tip explanation
- Why it works
- Related articles
- Quick tip section
- Links to: `/docs/prompts`, `/docs/schemas`, `/blog`

### Updates - Deep Dive
**Key Content:**
- Topic introduction
- Key principles
- Resources
- CTA to try
- Links to: `/docs/prompts`, `/docs/schemas`

### Investor Newsletter
**Key Content:**
- Key highlights (Growth & Product, Team & Milestones)
- What's next
- Personal note from CEO
- No documentation links (relationship-focused)

---

## Documentation Requirements & Strategy

### Required Documentation Pages

Based on email template analysis, the following documentation pages are needed:

#### Core Pages (Already Exist)
- ✅ `/docs` - Main documentation index
- ✅ `/docs/schemas` - Schema documentation
- ✅ `/docs/prompts` - Prompts guide
- ✅ `/docs/rest-api` - REST API documentation
- ✅ `/docs/webhooks` - Webhooks/workflows documentation
- ✅ `/docs/mcp` - MCP/Claude Code documentation

#### Missing or Needs Enhancement
- ❌ **Tags** - No dedicated page. Core workflow concept (Tag → Prompt → Upload) needs documentation
- ❌ **Knowledge Bases** - Referenced but links to generic `/docs`. Needs dedicated page or clear section
- ⚠️ **N8N Integration** - Referenced but links to generic `/docs/webhooks`. Needs dedicated section or page
- ⚠️ **Temporal Workflows** - Referenced but links to generic `/docs/webhooks`. Needs dedicated section or page

### Documentation Structure Recommendations

To avoid repetition and ensure comprehensive coverage:

#### 1. Tags Documentation (`/docs/tags`)
**Content:**
- What tags are and why they're required
- How tags route documents to prompts
- Tag creation workflow
- Best practices for tag naming
- Relationship to prompts and schemas
- Cross-references: Prompts, Quick Start, How It Works

**Avoid Repetition:**
- Don't duplicate prompt creation steps (link to prompts doc)
- Don't duplicate schema information (link to schemas doc)
- Focus on tags as routing mechanism

#### 2. Knowledge Bases Documentation (`/docs/knowledge-bases`)
**Content:**
- What knowledge bases are
- How they enhance extraction accuracy
- How to create and manage knowledge bases
- Integration with prompts
- Best practices
- Cross-references: Prompts, Schemas

**Avoid Repetition:**
- Don't duplicate prompt writing guide (link to prompts doc)
- Don't duplicate schema structure (link to schemas doc)
- Focus on knowledge base-specific features

#### 3. Workflows Documentation Enhancement (`/docs/webhooks`)
**Current:** Generic webhooks documentation
**Needs:**
- Clear sections for:
  - N8N Integration (with specific setup guide)
  - Temporal Workflows (with specific setup guide)
  - General webhook usage
- Or split into:
  - `/docs/webhooks` - General webhook documentation
  - `/docs/workflows/n8n` - N8N-specific integration
  - `/docs/workflows/temporal` - Temporal-specific integration

**Avoid Repetition:**
- Share common webhook concepts in main doc
- Link to API documentation for endpoint details
- Focus each integration guide on setup and specific use cases

#### 4. Documentation Cross-Reference Strategy

**Hierarchical Structure:**
```
/docs (index)
├── /docs/quick-start (overview → tags → prompts → schemas)
├── /docs/how-it-works (workflow explanation)
├── /docs/tags (NEW - required)
├── /docs/prompts (existing)
├── /docs/schemas (existing)
├── /docs/knowledge-bases (NEW - required)
├── /docs/mcp (existing - clarify = Claude Code)
├── /docs/webhooks (enhance with N8N/Temporal sections)
├── /docs/rest-api (existing)
└── /docs/[sdk] (Python, TypeScript)
```

**Cross-Reference Pattern:**
- Each page should link to related concepts
- Use "See also" sections at the end of each doc
- Quick Start should link to all core concepts
- How It Works should explain the workflow without duplicating step-by-step guides

### Email Template Documentation Link Mapping

| Template | Documentation Links Used | Notes |
|----------|--------------------------|-------|
| `onboarding-email-1` | `/docs/schemas`, `/docs/rest-api`, `/docs/webhooks`, `/docs/mcp`, `/docs` (knowledge bases) | Most comprehensive |
| `onboarding-email-2` | `/docs/mcp`, `/docs/webhooks`, `/docs/rest-api` | Focus on advanced features |
| `onboarding-email-3` | `/docs`, `/docs/rest-api`, `/docs/webhooks` | General resources |
| `updates-features` | `/docs` | Main documentation link |
| `updates-tips` | `/docs/prompts`, `/docs/schemas`, `/blog` | Specific guides |
| `updates-deep-dive` | `/docs/prompts`, `/docs/schemas` | Educational focus |
| `prospect-email-1` | None | Demo-focused |
| `prospect-email-2` | None | Demo-focused |
| `investor-newsletter` | None | Relationship-focused |

### Action Items for Documentation

1. **Create `/docs/tags` page** - Critical for onboarding workflow understanding
2. **Create `/docs/knowledge-bases` page** - Currently links to generic docs
3. **Enhance `/docs/webhooks`** - Add clear N8N and Temporal sections, or create separate pages
4. **Clarify `/docs/mcp`** - Ensure it's clear this is Claude Code integration
5. **Update Quick Start** - Ensure it follows Tag → Prompt → Upload workflow
6. **Update How It Works** - Ensure tags are explained as required prerequisite
7. **Add cross-references** - Link related concepts across all documentation pages
