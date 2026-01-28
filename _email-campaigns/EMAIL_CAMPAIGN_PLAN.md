eyJhcGlfa2V5IjoieGtleXNpYi05YmJiZjIyMmIwZTRmMTU4ZTVkNDhlMWM1M2FiZjBjMzViNjg0Njg4ZDFiOTQxZmI2OTFmYWY0NzYxMTc2MDVjLXdoTzg5VThZdGFUbzg4cVYifQ==
# Email Campaign Plan for DocRouter.AI

## Overview

This document outlines five active email campaigns plus future campaigns:
1. **Onboarding Campaign** - For users who have registered an account
2. **Prospect Campaign** - For potential users who might be interested in DocRouter.AI
3. **Investor/Friends Newsletter** - For investors, advisors, and close contacts
4. **Product Updates Newsletter** - For registered users with product announcements
5. **Educational Series** - Monthly deep-dive content for active users

### Future Campaigns (For Later Implementation)
6. **Re-engagement Campaign** - For inactive users to return to the platform
7. **Referral Program** - Leverage users to bring in new customers

---

## Email Templates Overview

| Campaign | Template | Subject Line | Preview Text |
|----------|----------|--------------|--------------|
| **Onboarding** | Email 1: Tag, Prompt, Upload | "DocRouter.AI: Tag, prompt, upload - Get started in 4 steps 📄" | Welcome to DocRouter.AI! Create a tag and a prompt, upload a document, and see your first extraction in minutes. |
| **Onboarding** | Email 2: Learn About Schemas | "DocRouter.AI: Learn about schemas for document extraction 🤖" | Schemas ensure consistent, validated output from your prompts. Learn how to create and use them effectively. |
| **Onboarding** | Email 3: Customer Success Check | "How's your DocRouter.AI journey going? We're here to help 👋" | You've been using DocRouter.AI for a week. We're here to help with questions and hear how it's working for you. |
| **Prospect** | Email 1: Introduction & Demo Invitation | "DocRouter.AI: Transform Your Document Processing with AI" | See how DocRouter.AI extracts data from unstructured documents with AI. Book a free demo to learn more. |
| **Prospect** | Email 2: Follow-up Demo Reminder | "Ready to See DocRouter.AI in Action?" | Book your free demo and discover how DocRouter.AI can transform your document processing workflow. |
| **Investor** | Quarterly Newsletter | "DocRouter.AI Quarterly Update: [Quarter] [Year]" | Quarterly update on DocRouter.AI progress, milestones, and strategic updates for our valued partners. |
| **Product Updates** | Feature Release | "DocRouter.AI: New Feature - [Feature Name]" | Exciting new feature announcement with details and benefits for DocRouter.AI users. |
| **Product Updates** | Maintenance & Security | "DocRouter.AI Update: [Update Title]" | Security, performance, and bug fix updates for DocRouter.AI users. |
| **Product Updates** | Tips & Best Practices | "DocRouter.AI Tip: [Tip Title]" | Educational content and best practices to get more value from DocRouter.AI. |
| **Educational** | Monthly Deep Dive | "DocRouter.AI Deep Dive: [Topic]" | Monthly educational content on advanced DocRouter.AI features and techniques. |

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
**Cadence:** Quarterly

### Product Updates Newsletter
**Goal:** Keep users informed about features and improvements
**Audience:** Registered users
**Cadence:** Bi-weekly to monthly

### Educational Series
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
- `investor-newsletter-quarterly.html` - Quarterly comprehensive updates

**Product Updates Newsletter:**
- `product-updates-feature-release.html` - New feature announcements
- `product-updates-maintenance.html` - Maintenance and security updates
- `product-updates-tips.html` - Educational content and tips

**Educational Series:**
- `educational-series-template.html` - Single reusable template for monthly educational content

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
Quarterly only - focused on major milestones and strategic updates.

### Email Content Structure

#### Quarterly Updates
**Subject Line Examples:**
- "Q4 DocRouter.AI Update: Major Milestones & What's Next"
- "DocRouter.AI Quarterly: Progress, Partnerships & Plans"
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

#### Feature Release Announcements
**Subject Line Examples:**
- "New Feature: Advanced Schema Validation"
- "DocRouter Update: Enhanced API Rate Limits"
- "What's New: Improved Document Processing"

**Content Focus:**
- New DocRouter.AI features and capabilities
- Performance improvements
- Bug fixes and security updates
- API changes or deprecations
- Integration updates
- Usage tips and best practices

**Tone:** Professional, helpful, user-focused

**Key Sections:**
- "🚀 New Features"
- "⚡ Performance & Reliability"
- "🐛 Bug Fixes & Security"
- "📚 Resources & Tips"
- "🔮 Coming Soon"

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

## Campaign 5: Educational Series

### Goal
Build expertise and demonstrate thought leadership while keeping users engaged.

### Target Audience
Active users who want to get more value from DocRouter.

### Email Schedule
Monthly series: "DocRouter.AI Deep Dives" - 4 emails over a month.

#### Email 1: Advanced Prompting Techniques
#### Email 2: Schema Design Best Practices
#### Email 3: Workflow Automation with N8N/Temporal
#### Email 4: API Integration Examples

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
- `investor-newsletter-quarterly.html` - Quarterly comprehensive updates

**Product Updates Newsletter:**
- `product-updates-feature-release.html` - New feature announcements
- `product-updates-maintenance.html` - Maintenance and security updates
- `product-updates-tips.html` - Educational content and tips

**Educational Series:**
- `educational-series-template.html` - Single reusable template for monthly educational content

**Future Campaigns (Templates for Later):**
- `reengagement-email-*.html` - Re-engagement sequence templates
- `referral-program-*.html` - Referral program templates

**Note:** The existing `welcome-email-template.html` and `onboarding-email-*.html` files may need to be updated or replaced to match the new structure.
