# Mandatory Questions Fix - v1.2

**Date:** January 23, 2025
**Issue:** Claude AI was skipping ALL questions
**Status:** Fixed ✅

---

## Problem Identified

**User Report:**
> "I just typed in 'Write a product manager prompt for creating a PRD' and started creating the prompt. Why the questions haven't displayed?"

**Root Cause:**
The skill said "Skip obvious questions based on inferred context" - when the user said "product manager prompt for creating a PRD", Claude inferred:
- Role: Product Manager ✓
- Use case: Create PRD ✓
- Domain: Product Management ✓
- Output: PRD document ✓

Claude thought ALL questions were "obvious" and skipped them entirely, jumping straight to prompt generation.

**Why This Is a Problem:**
1. **No specificity:** Generic prompts without details about industry, constraints, success criteria
2. **Low quality:** Missing critical context leads to suboptimal prompts
3. **Defeats purpose:** The interactive flow is a key feature of the skill
4. **No validation:** User can't correct misunderstandings before generation

---

## Solution Implemented

### Changed from OPTIONAL to MANDATORY Questioning

**Before (v1.1 - Too Permissive):**
```markdown
Present **MAX 7 questions** with example answers.
Skip obvious questions based on inferred context.

**Skip rules:**
- Skip Q2 if domain is obvious from Q1
- Skip Q5 if tech stack mentioned in Q3
- Skip Q6 if no constraints needed for use case
```

**After (v1.2 - Strict Minimum):**
```markdown
**MANDATORY: You MUST ask questions before generating any prompt.**

**Questioning Rules:**
- **MINIMUM: Ask at least 5 questions** (even if context seems clear)
- **MAXIMUM: Ask up to 7 questions** (skip only truly redundant ones)
- **Always ask for CONFIRMATION** of inferred details, don't just assume
- **Purpose:** Validate assumptions, gather specifics, ensure quality output
```

### Added Strict Minimum Requirements

**Cannot Skip These:**
- ✅ MUST ask at least 1 question about role/domain (even if "obvious")
- ✅ MUST ask at least 1 question about use case/task details
- ✅ MUST ask about constraints OR success criteria (at minimum one)
- ✅ MUST ask about output format preference
- ✅ MUST ask about mode (core vs. advanced)

**Total: MINIMUM 5 questions, MAXIMUM 7 questions**

### Added Explicit Example for "Obvious" Requests

**Example - User says:**
```
"Write a product manager prompt for creating a PRD"
```

**Skill MUST still ask:**
1. "I'm inferring role = Product Manager. What domain/industry? (e.g., B2B SaaS, Mobile Apps, Healthcare)"
2. "What type of PRD? (e.g., New Feature, Platform Migration, MVP Launch)"
3. "What are the constraints? (e.g., Team size, Timeline, Budget, Technical stack)"
4. "What are the success criteria? (e.g., Stakeholder approval, Dev handoff ready, Measurable KPIs)"
5. "What output format? (XML [default], Claude, ChatGPT, Gemini, All)"

**DO NOT skip questions just because you can infer answers. ALWAYS ask for validation and specifics.**

---

## Changes Made to SKILL.md

### 1. Updated CRITICAL CONSTRAINTS Section
**Location:** Top of file (lines 16-21)

**Added:**
```markdown
✅ **Ask 5-7 questions to understand requirements** (MANDATORY - no skipping)
```

### 2. Updated Expected Workflow
**Location:** Lines 32-38

**Before:**
```
2. Skill asks max 7 questions
```

**After:**
```
2. **Skill MUST ask 5-7 questions** (even if context seems obvious)
3. User answers questions with specific details
```

### 3. Updated Overview
**Location:** Lines 53

**Before:**
```
1. **Smart 7-question flow** (max) with example answers
```

**After:**
```
1. **Mandatory 5-7 question flow** (MUST ask, even if context obvious) with example answers
```

### 4. Updated Path 2 Title and Description
**Location:** Lines 74-82

**Before:**
```
### Path 2: Custom Prompt (7 Questions)
```

**After:**
```
### Path 2: Custom Prompt (5-7 Questions - MANDATORY)

**Note:** Even if the request seems clear (e.g., "product manager PRD prompt"),
you MUST still ask questions to gather specifics, validate assumptions, and
ensure a high-quality output.
```

### 5. Rewrote Step 2 Questioning Rules
**Location:** Lines 113-242

**Major Changes:**
- Added **MANDATORY** warning at top
- Changed from "max 7" to "MINIMUM 5, MAXIMUM 7"
- Replaced "Skip obvious questions" with "Always ask for CONFIRMATION"
- Added explicit "When to skip" vs. "When to ask" rules
- Added example interaction for "obvious" request
- Added "DO NOT skip questions just because you can infer answers"

**Before (Permissive):**
```
Skip rules:
- Skip Q2 if domain is obvious from Q1
- Skip Q5 if tech stack mentioned in Q3
```

**After (Strict):**
```
Strict Minimum Requirements (Cannot Skip):
- ✅ MUST ask at least 1 question about role/domain (even if "obvious")
- ✅ MUST ask at least 1 question about use case/task details
- ✅ MUST ask about constraints OR success criteria (at minimum one)
```

---

## Before vs. After Comparison

### Scenario: User says "Write a product manager prompt for creating a PRD"

#### Before (v1.1 - Skipped All Questions):
**Claude's behavior:**
1. Infers: role=PM, task=PRD, domain=product, output=document
2. Thinks: "Everything is obvious, skip all questions"
3. Generates generic PRD prompt immediately
4. No user interaction or validation

**Result:**
- ❌ Generic prompt without specifics
- ❌ No industry context
- ❌ No constraints (budget, timeline, team)
- ❌ No success criteria
- ❌ User can't correct misunderstandings

#### After (v1.2 - Mandatory 5 Questions):
**Claude's behavior:**
1. Reads: "MANDATORY: You MUST ask questions"
2. Sees example: "Even for 'product manager PRD' you MUST ask..."
3. Asks 5 questions:
   - Domain/industry specifics
   - PRD type details
   - Constraints
   - Success criteria
   - Output format
4. User provides specific answers
5. Generates tailored prompt with all context

**Result:**
- ✅ Specific prompt for user's exact context
- ✅ Industry-specific considerations
- ✅ Realistic constraints incorporated
- ✅ Measurable success criteria
- ✅ User validates all assumptions

---

## Testing the Fix

### Test Case 1: "Obvious" Request
**User input:**
```
"Create a prompt for a senior full-stack engineer building an API"
```

**Expected behavior (v1.2):**
Claude MUST ask at least 5 questions:
1. "What tech stack? (e.g., Node.js, Python, Go)"
2. "What domain/industry? (e.g., FinTech, Healthcare, E-commerce)"
3. "What are the constraints? (e.g., Budget, Timeline, Team size)"
4. "What are the success criteria? (e.g., Performance, Scalability, Security)"
5. "What output format? (XML, Claude, ChatGPT, Gemini, All)"

**Incorrect behavior (should NOT happen):**
❌ Immediately generates prompt without questions
❌ Asks only 1-2 questions
❌ Says "I'll infer the details and generate the prompt"

### Test Case 2: Detailed Request
**User input:**
```
"Create a prompt for a DevOps engineer setting up AWS infrastructure
with Terraform for a microservices e-commerce platform, budget $5K/month,
6-week timeline, team of 2 engineers"
```

**Expected behavior (v1.2):**
Claude MUST still ask at least 5 questions (even though much is specified):
1. "Confirmed: AWS + Terraform + microservices. How many services? (e.g., 5-10, 10-20)"
2. "What traffic expectations? (e.g., 1K req/min, 10K req/min)"
3. "What security/compliance requirements? (e.g., SOC2, HIPAA, PCI-DSS)"
4. "What output format? (XML [default], Claude, ChatGPT, Gemini)"
5. "Core or Advanced mode?"

**Incorrect behavior (should NOT happen):**
❌ Says "You provided all details, generating now..."
❌ Skips questions because request was detailed
❌ Asks fewer than 5 questions

### Test Case 3: Vague Request
**User input:**
```
"I need a prompt for marketing"
```

**Expected behavior (v1.2):**
Claude asks 7 questions (maximum):
1. "What specific marketing role? (e.g., Content Strategist, Growth Marketer, Social Media Manager)"
2. "What domain/industry? (e.g., B2B SaaS, E-commerce, Healthcare)"
3. "What's the primary task? (e.g., Campaign planning, Content strategy, SEO optimization)"
4. "What are the constraints? (e.g., Budget, Timeline, Team resources)"
5. "What are the success criteria? (e.g., Traffic goals, Lead generation, Conversion rates)"
6. "What output format?"
7. "Core or Advanced mode?"

---

## Red Flags (Report These If They Occur)

### ❌ Skipping Questions
**What to look for:**
- Claude says "Based on your request, I'll generate..."
- Claude asks 0-4 questions instead of 5-7
- Claude says "I'm inferring [details], generating now..."

**What to do:**
Stop and say:
```
"This skill MUST ask 5-7 questions before generating. Please ask questions first."
```

### ❌ Generic Prompts
**What to look for:**
- Prompt has [PLACEHOLDER] or [INSERT X HERE]
- Prompt lacks specific industry context
- Prompt missing constraints or success criteria
- Prompt feels template-y instead of tailored

**What to do:**
This indicates questions were skipped. Ask Claude to:
```
"Regenerate, but ask me 5-7 questions first to gather specifics."
```

### ❌ No Token Count
**What to look for:**
- Prompt delivered without token count announcement
- Missing "~4,200 tokens" style announcement

**What to do:**
This indicates the delivery message wasn't followed. Remind:
```
"Please announce the token count as specified in the skill."
```

---

## File Changes Summary

### Modified Files:
1. **SKILL.md**
   - Lines 18, 33-34, 53, 74-82, 113-242 updated
   - Added ~40 lines of mandatory questioning rules
   - Added explicit example for "obvious" requests
   - Changed "max 7" to "MINIMUM 5, MAXIMUM 7" throughout

### Added Files:
1. **MANDATORY_QUESTIONS_FIX.md** (this document)
   - Documents the issue, solution, and testing

### ZIP File Updated:
- **Before:** 106KB (v1.1)
- **After:** 110KB (v1.2)
- **Location:** `generated-skills/prompt-suite.zip`

---

## Key Takeaways

### Why This Fix Matters:
1. **Quality Control:** Questions ensure prompts are specific and high-quality
2. **User Validation:** User can correct misunderstandings before generation
3. **Context Gathering:** Gets critical details that can't be inferred
4. **Feature Completeness:** Interactive flow is a core feature, not optional

### What Changed:
- **v1.0:** No constraints on questions
- **v1.1:** "Max 7, skip obvious" (too permissive → skipped all)
- **v1.2:** "MINIMUM 5, MAXIMUM 7, MANDATORY" (strict enforcement)

### Design Philosophy:
**Old approach:** "Be smart and efficient, skip what you can infer"
- Result: Skipped everything, low-quality prompts

**New approach:** "Always ask for validation, even if you think you know"
- Result: High-quality, tailored prompts with user confirmation

---

## Version History

- **v1.0 (2025-01-23):** Initial MVP release
  - No question constraints

- **v1.1 (2025-01-23):** Scope control update
  - Added STOP signals
  - Added token count announcements
  - Still had "skip obvious" questions bug

- **v1.2 (2025-01-23):** Mandatory questions fix
  - Changed to MINIMUM 5 questions (MANDATORY)
  - Removed permissive "skip obvious" rules
  - Added explicit "always ask for confirmation" guidance
  - Added example for "obvious" requests

---

## Next Steps for User

1. **Delete old ZIP** (v1.0 or v1.1 if you have them)
2. **Download new ZIP:** `generated-skills/prompt-suite.zip` (110KB, v1.2)
3. **Test with Claude AI:**
   - Upload ZIP
   - Try: "Write a product manager prompt for creating a PRD"
   - **Verify Claude asks 5-7 questions** before generating
4. **Report results:**
   - If Claude still skips questions → report for further hardening
   - If Claude asks questions correctly → skill is working as intended

---

**Status:** Ready for testing ✅

**Expected behavior:**
- Claude MUST ask 5-7 questions
- Claude MUST ask even for "obvious" requests
- Claude MUST confirm inferred details with user

**No longer acceptable:**
- ❌ Skipping questions because "context is clear"
- ❌ Asking fewer than 5 questions
- ❌ Generating without user interaction

---

*This fix ensures the Prompt Suite skill ALWAYS engages users interactively, gathering specifics and validating assumptions before generating prompts.*
