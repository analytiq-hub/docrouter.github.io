# Documentation Alignment with Email Campaigns

## Critical Gaps Found

### 1. **Tags Are Not Emphasized as REQUIRED**
**Problem:** Email campaigns correctly teach "Tag → Prompt → Upload" workflow, but documentation treats tags as optional.

**Current State:**
- `docs/prompts.md` mentions tags as "Document tags that trigger this prompt" but doesn't emphasize they're **required**
- No dedicated tags documentation page
- Users following docs without understanding tags won't get prompts to trigger

**Impact:** Users following documentation will fail at basic usage.

### 2. **Missing Tag System Documentation**
**Problem:** No dedicated page explaining:
- What tags are and why they're required
- How tag-prompt relationships work
- Tag management and best practices
- Tag-based routing system

**Current State:** Tags are scattered mentions in prompts.md but no comprehensive explanation.

### 3. **Workflow Clarity Issues**
**Problem:** Documentation doesn't clearly explain the prerequisite workflow.

**Current State:**
- `docs/quick-start.md` is good but could emphasize tag requirement more
- `docs/how-it-works.md` shows high-level process but doesn't explain tag system
- Users need to understand: "Tags connect documents to prompts" early

### 4. **Schema-Prompt Relationship**
**Problem:** Email campaigns teach schemas after prompts, but docs could better explain the relationship.

**Current State:** Both docs and emails are aligned here, but reinforcement wouldn't hurt.

## Recommended Documentation Updates

### High Priority (Fix Before Next Email Campaign)

#### 1. **Add Tags Documentation Page**
Create `docs/tags.md` with:
```
- What are tags and why they're required
- Tag creation and management
- Tag-prompt relationships
- Tag-based routing examples
- Best practices for tag naming
```

#### 2. **Update Prompts Documentation**
In `docs/prompts.md`:
- Move "Tags" from "No" to "Yes (Required)" in the components table
- Add prominent callout: "⚠️ **Tags are required** - prompts only trigger on tagged documents"
- Add section: "Understanding Tag-Prompt Relationships"

#### 3. **Enhance Quick Start Guide**
In `docs/quick-start.md`:
- Add step 0: "Understanding Tags" before document upload
- Emphasize: "Tags are required for prompts to work"
- Include tag creation in step 2

#### 4. **Update How It Works Page**
In `docs/how-it-works.md`:
- Add section explaining tag system in the workflow
- Include tags in the process overview
- Add FAQ: "Why do I need tags?"

### Medium Priority (Next Sprint)

#### 5. **Add Workflow Prerequisites Section**
Create consistent "Before You Start" sections across docs:
- Tags must exist before prompts
- Prompts must be linked to tags
- Documents must be tagged to trigger processing

#### 6. **Cross-Link Documentation**
Add prominent links between:
- Quick Start → Tags documentation
- Prompts → Tags documentation
- How It Works → Tags documentation

### Low Priority (Future Enhancement)

#### 7. **Add Troubleshooting Section**
Create `docs/troubleshooting.md` with:
- "My prompt isn't triggering" → Check document tags
- "Document not processing" → Verify tag-prompt association
- Common tag-related issues

#### 8. **Visual Workflow Diagrams**
Add diagrams showing:
- Tag → Prompt → Document flow
- Tag-based routing system
- Complete user journey from signup to automation

## Email Campaign Alignment Benefits

Once documentation is updated:
- **Consistency:** Docs match email teaching sequence
- **Reduced Support:** Users understand tag requirements upfront
- **Better UX:** Clear prerequisite knowledge
- **Higher Success:** Users following docs will succeed

## Implementation Order

1. **Week 1:** Create tags.md documentation page
2. **Week 1:** Update prompts.md to emphasize tag requirements
3. **Week 2:** Enhance quick-start.md with tag emphasis
4. **Week 2:** Update how-it-works.md with tag system explanation
5. **Week 3:** Add cross-links and troubleshooting sections

## Success Metrics

- **Reduced Support Tickets:** Fewer "prompt not working" issues
- **Higher Email Engagement:** Users understand email content better
- **Faster User Onboarding:** Clear prerequisite knowledge
- **Better Documentation Feedback:** Users can follow docs successfully