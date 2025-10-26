#!/usr/bin/env python3
"""
Prompt Suite - Enhanced Prompt Generator

Generates world-class mega-prompts in multiple formats (XML, Claude, ChatGPT, Gemini)
with quality validation and contextual best practices.

Usage:
    python generate_prompt.py --responses responses.json --format xml --mode core --output prompt.md
    python generate_prompt.py --preset fullstack-engineer --format all --mode advanced --output prompt.md
"""

import json
import argparse
import re
from datetime import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path


class PromptGenerator:
    """Enhanced prompt generator with multi-format support and quality validation."""

    def __init__(self):
        self.validation_score = 0
        self.validation_issues = []

    def load_responses(self, filepath: str) -> Dict[str, Any]:
        """Load questionnaire responses from JSON file."""
        with open(filepath, 'r') as f:
            return json.load(f)

    def load_preset(self, preset_name: str) -> Dict[str, Any]:
        """Load a quick-start preset template."""
        preset_path = Path(__file__).parent.parent / 'templates' / 'presets'

        # Map preset names to files
        preset_map = {
            'fullstack-engineer': 'technical/fullstack-engineer.md',
            'ml-engineer': 'technical/ml-engineer.md',
            'devops-engineer': 'technical/devops-engineer.md',
            'mobile-engineer': 'technical/mobile-engineer.md',
            'solutions-architect': 'technical/solutions-architect.md',
            'product-manager': 'business/product-manager.md',
            'marketing-strategist': 'business/marketing-strategist.md',
            'business-analyst': 'business/business-analyst.md',
            'operations-manager': 'business/operations-manager.md',
            'content-strategist': 'creative/content-strategist.md',
            'ux-designer': 'creative/ux-designer.md',
            'technical-writer': 'creative/technical-writer.md',
            'healthcare-consultant': 'specialized/healthcare-consultant.md',
            'fintech-advisor': 'specialized/fintech-advisor.md',
            'legal-specialist': 'specialized/legal-specialist.md',
        }

        if preset_name not in preset_map:
            raise ValueError(f"Unknown preset: {preset_name}")

        # Return default configuration for preset
        # In production, this would load from actual template files
        return {
            'role': preset_name.replace('-', ' ').title(),
            'preset': preset_name,
            'template': preset_map[preset_name]
        }

    def generate_xml_format(self, responses: Dict[str, Any]) -> str:
        """Generate prompt in XML format."""
        role = responses.get('role', 'Expert AI Assistant')
        role_context = responses.get('role_context', '')
        domain = responses.get('domain', '')
        goal = responses.get('goal', 'assist the user effectively')
        output_type = responses.get('output_type', 'comprehensive response')
        success_criteria = responses.get('success_criteria', 'Meeting user requirements with high quality')
        tech_stack = responses.get('tech_stack', '')
        constraints = responses.get('constraints', '')
        must_avoid = responses.get('must_avoid', '')
        target_audience = responses.get('target_audience', 'general')
        tone = responses.get('tone', 'professional')
        detail_level = responses.get('detail_level', 'moderate')
        format_preference = responses.get('format_preference', 'mixed')

        # Build role section
        role_text = f"{role}"
        if role_context:
            role_text += f" with expertise in {role_context}"
        if domain:
            role_text += f", specializing in {domain}"

        # Build context section
        context_parts = []
        if domain:
            context_parts.append(f"  <domain>{domain}</domain>")
        if tech_stack:
            context_parts.append(f"  <tech_stack>{tech_stack}</tech_stack>")
        if constraints:
            context_parts.append(f"  <constraints>{constraints}</constraints>")
        if must_avoid:
            context_parts.append(f"  <avoidance_rules>{must_avoid}</avoidance_rules>")

        context_content = "\n".join(context_parts) if context_parts else "  <domain>General</domain>"

        # Get workflow based on output type
        workflow = self._get_workflow_for_output_type(output_type)

        # Generate best practices
        best_practices = self._get_best_practices(output_type, domain)

        # Build the prompt
        prompt = f"""<mega_prompt>

<role>
{role_text}
</role>

<mission>
Your primary objective is to {goal}.

Success is defined by: {success_criteria}
</mission>

<context>
{context_content}
</context>

{workflow}

<output_specifications>
  <format>{output_type}</format>
  <structure>{format_preference} format with clear organization</structure>
  <depth_level>{detail_level}</depth_level>
  <quality_criteria>{success_criteria}</quality_criteria>
</output_specifications>

<communication_guidelines>
  <tone>{tone}</tone>
  <audience>{target_audience}</audience>
  <formatting>{format_preference}</formatting>
  <examples_usage>Provide relevant examples when they clarify complex concepts or demonstrate best practices</examples_usage>
</communication_guidelines>

{best_practices}

<critical_instructions>
  <priority_1>
    - Ensure all information is accurate and verified
    - Follow ALL constraints specified in the context section
    {f'- DO NOT include or suggest: {must_avoid}' if must_avoid else ''}
  </priority_1>

  <priority_2>
    - Provide complete, production-ready output
    - Include proper error handling and edge cases
    - Maintain specified communication style
  </priority_2>

  <priority_3>
    - Optimize for clarity and maintainability
    - Consider scalability and future extensibility
    - Provide actionable guidance
  </priority_3>
</critical_instructions>

<examples>
## Example 1: Standard Request
**User Request:** [Typical request for this role]

**Expected Response Structure:**
- Analyze the request thoroughly
- Apply the workflow systematically
- Deliver output meeting quality criteria
- Include relevant examples

## Example 2: Complex Scenario
**User Request:** [More complex request]

**Expected Response Structure:**
- Break down into manageable components
- Address each component systematically
- Integrate solutions coherently
- Validate against success criteria
</examples>

<execution_trigger>
You are now fully configured as {role}{f' specialized in {domain}' if domain else ''}.

When the user provides a request:
1. Analyze their specific needs using the workflow above
2. Apply relevant best practices contextually
3. Generate output meeting quality criteria
4. Deliver complete solution in one comprehensive response

Begin assisting the user now with this configuration.
</execution_trigger>

</mega_prompt>"""

        return prompt

    def generate_claude_format(self, responses: Dict[str, Any]) -> str:
        """Generate prompt optimized for Claude."""
        role = responses.get('role', 'Expert AI Assistant')
        domain = responses.get('domain', '')
        goal = responses.get('goal', 'assist the user effectively')
        output_type = responses.get('output_type', 'comprehensive response')
        tech_stack = responses.get('tech_stack', '')
        constraints = responses.get('constraints', '')
        tone = responses.get('tone', 'professional')
        detail_level = responses.get('detail_level', 'moderate')

        workflow_steps = self._get_workflow_steps(output_type)

        prompt = f"""# System Configuration: {role}

You are {role}{f' specialized in {domain}' if domain else ''}.

## Your Mission

{goal}

## Your Expertise

{f'Domain: {domain}' if domain else 'General expertise across domains'}
{f'Technical Stack: {tech_stack}' if tech_stack else ''}

## Your Workflow

When given a task:
{workflow_steps}

## Output Standards

- Format: {output_type}
- Depth: {detail_level} detail
- Quality: Production-ready, complete, accurate

## Communication Style

- Tone: {tone}
- Clarity: Crystal clear with concrete examples
- Structure: Well-organized with logical flow

## Critical Rules

**Must follow:**
{f'- Constraints: {constraints}' if constraints else '- Follow standard best practices'}
- Verify all information is accurate
- Provide complete, actionable solutions
- Include relevant examples

**Always include:**
- Clear explanations
- Practical examples
- Edge case handling
- Quality validation

## Best Practices

{self._get_best_practices_list(output_type, domain)}

## Response Examples

[Include 2-3 examples of expected response patterns based on typical requests]

---

Execute your role now, following all guidelines above. When the user makes a request, apply this configuration to deliver high-quality, comprehensive responses.
"""

        return prompt

    def generate_chatgpt_format(self, responses: Dict[str, Any]) -> str:
        """Generate prompt for ChatGPT custom instructions."""
        role = responses.get('role', 'Expert AI Assistant')
        domain = responses.get('domain', '')
        goal = responses.get('goal', 'assist effectively')
        output_type = responses.get('output_type', 'comprehensive response')
        tech_stack = responses.get('tech_stack', '')
        constraints = responses.get('constraints', '')
        tone = responses.get('tone', 'professional')
        detail_level = responses.get('detail_level', 'moderate')
        format_preference = responses.get('format_preference', 'mixed')

        about_section = f"""I need you to act as {role}{f' specialized in {domain}' if domain else ''}.

My domain: {domain if domain else 'General'}
{f'My tech stack: {tech_stack}' if tech_stack else ''}
{f'My constraints: {constraints}' if constraints else ''}

My goal: {goal}"""

        workflow_steps = self._get_workflow_steps(output_type)

        response_section = f"""WORKFLOW:
{workflow_steps}

OUTPUT REQUIREMENTS:
- Format: {output_type}
- Style: {tone} tone, {detail_level} detail
- Structure: {format_preference} with clear organization
- Quality: Production-ready, complete, accurate

CRITICAL RULES:
{f'- Constraints: {constraints}' if constraints else '- Follow best practices'}
- Verify accuracy
- Provide complete solutions
- Include examples
- Handle edge cases

BEST PRACTICES:
{self._get_best_practices_list(output_type, domain)}

Always provide {format_preference} responses with concrete examples and ensure {output_type} meets production quality standards."""

        return f"""**What would you like ChatGPT to know about you to provide better responses?**

{about_section}

**How would you like ChatGPT to respond?**

{response_section}"""

    def generate_gemini_format(self, responses: Dict[str, Any]) -> str:
        """Generate prompt optimized for Google Gemini."""
        role = responses.get('role', 'Expert AI Assistant')
        domain = responses.get('domain', '')
        goal = responses.get('goal', 'assist effectively')
        output_type = responses.get('output_type', 'comprehensive response')
        detail_level = responses.get('detail_level', 'moderate')

        workflow_simple = self._get_workflow_simple(output_type)

        prompt = f"""## Role Configuration
You are: {role}{f' specialized in {domain}' if domain else ''}

## Task Approach
{workflow_simple}

## Output Format
- Type: {output_type}
- Detail: {detail_level}
- Quality: Complete and production-ready

## Quality Standards
- Accurate and verified information
- Clear, practical examples
- Complete solutions
- Edge case handling

## Examples
[Example 1: Show typical interaction]
[Example 2: Show complex scenario handling]

Apply this configuration to all responses. Maintain this role and follow these standards consistently.
"""

        return prompt

    def _get_workflow_for_output_type(self, output_type: str) -> str:
        """Get detailed workflow XML for given output type."""
        workflows = {
            'code': """<workflow>
  <analysis_phase>
    1. Understand requirements and technical constraints
    2. Identify key components and dependencies
    3. Consider edge cases and error scenarios
    4. Evaluate technology options
  </analysis_phase>

  <solution_design>
    1. Design system architecture or component structure
    2. Define data models and interfaces
    3. Plan error handling strategy
    4. Consider performance and security implications
  </solution_design>

  <execution>
    1. Write clean, well-documented code
    2. Implement comprehensive error handling
    3. Follow best practices and design patterns
    4. Include inline documentation
  </execution>

  <validation>
    1. Review code for bugs and edge cases
    2. Ensure test coverage
    3. Verify performance characteristics
    4. Confirm security best practices
  </validation>
</workflow>""",
            'documentation': """<workflow>
  <analysis_phase>
    1. Understand the subject matter and audience
    2. Identify key concepts to document
    3. Determine optimal document structure
    4. Gather necessary technical details
  </analysis_phase>

  <content_creation>
    1. Create clear outline with logical flow
    2. Write comprehensive yet accessible content
    3. Include relevant examples and diagrams
    4. Add code snippets or references where appropriate
  </content_creation>

  <refinement>
    1. Review for clarity and completeness
    2. Check technical accuracy
    3. Ensure consistent terminology
    4. Optimize for readability
  </refinement>
</workflow>""",
            'strategy': """<workflow>
  <analysis_phase>
    1. Assess current situation and challenges
    2. Analyze market dynamics and competition
    3. Identify opportunities and threats
    4. Evaluate capabilities and resources
  </analysis_phase>

  <strategy_development>
    1. Define strategic objectives
    2. Develop strategic options
    3. Evaluate options against criteria
    4. Select recommended approach
  </strategy_development>

  <implementation_planning>
    1. Create detailed roadmap
    2. Define success metrics and KPIs
    3. Identify resource requirements
    4. Plan risk mitigation strategies
  </implementation_planning>
</workflow>""",
            'analysis': """<workflow>
  <data_gathering>
    1. Identify relevant data sources
    2. Collect and validate data
    3. Clean and preprocess data
    4. Understand data limitations
  </data_gathering>

  <analysis_execution>
    1. Apply appropriate analytical methods
    2. Identify patterns and trends
    3. Test hypotheses and validate findings
    4. Consider alternative explanations
  </analysis_execution>

  <insight_generation>
    1. Translate findings into business insights
    2. Provide actionable recommendations
    3. Quantify impact where possible
    4. Address limitations and caveats
  </insight_generation>
</workflow>"""
        }

        return workflows.get(output_type, workflows['code'])

    def _get_workflow_steps(self, output_type: str) -> str:
        """Get workflow steps as numbered list."""
        workflows = {
            'code': """1. Analyze requirements and constraints
2. Design solution architecture
3. Implement with best practices
4. Validate and test thoroughly""",
            'documentation': """1. Understand audience and content needs
2. Create structured outline
3. Write clear, comprehensive content
4. Review and refine for clarity""",
            'strategy': """1. Assess current situation
2. Develop strategic options
3. Evaluate and recommend
4. Plan implementation""",
            'analysis': """1. Gather and validate data
2. Execute analytical methods
3. Generate insights
4. Provide recommendations"""
        }

        return workflows.get(output_type, workflows['code'])

    def _get_workflow_simple(self, output_type: str) -> str:
        """Get simplified workflow for Gemini."""
        workflows = {
            'code': "Analyze → Design → Implement → Validate",
            'documentation': "Research → Outline → Write → Refine",
            'strategy': "Assess → Strategize → Recommend → Plan",
            'analysis': "Collect Data → Analyze → Generate Insights → Recommend"
        }

        return workflows.get(output_type, "Analyze → Plan → Execute → Validate")

    def _get_best_practices(self, output_type: str, domain: str) -> str:
        """Get best practices XML section."""
        practices = {
            'code': """<best_practices>
**OpenAI Best Practices:**
- Write clear, specific instructions
- Provide examples for complex patterns
- Request step-by-step reasoning

**Anthropic Best Practices:**
- Use structured output format
- Include error handling
- Document complex logic

**Google Best Practices:**
- Break complex tasks into subtasks
- Provide concrete examples
- Specify output format clearly

**Domain-Specific:**
- Follow language-specific idioms
- Implement comprehensive testing
- Consider security implications
- Optimize for performance
</best_practices>""",
            'documentation': """<best_practices>
**OpenAI Best Practices:**
- Structure content logically
- Use clear, concise language
- Provide practical examples

**Anthropic Best Practices:**
- Progressive information disclosure
- Consistent terminology
- Clear hierarchy

**Google Best Practices:**
- Visual aids where helpful
- Multiple audience levels
- Searchable structure

**Domain-Specific:**
- Audience-appropriate depth
- Practical use cases
- Troubleshooting guidance
- Keep content updated
</best_practices>""",
            'strategy': """<best_practices>
**OpenAI Best Practices:**
- Data-driven recommendations
- Clear reasoning
- Scenario analysis

**Anthropic Best Practices:**
- Structured framework
- Risk assessment
- Implementation feasibility

**Google Best Practices:**
- Measurable outcomes
- Actionable insights
- Priority ranking

**Domain-Specific:**
- Industry benchmarks
- Competitive context
- Resource considerations
- Change management
</best_practices>"""
        }

        return practices.get(output_type, practices['code'])

    def _get_best_practices_list(self, output_type: str, domain: str) -> str:
        """Get best practices as bullet list."""
        practices = {
            'code': """- Follow language-specific idioms and conventions
- Write self-documenting code
- Implement comprehensive error handling
- Include proper testing
- Consider security and performance""",
            'documentation': """- Use clear, concise language
- Structure content logically
- Include practical examples
- Maintain consistent terminology
- Keep content updated""",
            'strategy': """- Base on data and evidence
- Consider multiple scenarios
- Provide clear rationale
- Include risk assessment
- Define measurable success criteria"""
        }

        return practices.get(output_type, practices['code'])

    def validate_prompt(self, prompt: str, format_type: str) -> tuple:
        """
        Validate prompt against 7 quality gates.
        Returns (score, issues_list)
        """
        score = 0
        issues = []

        # Gate 1: XML structure (if XML format)
        if format_type == 'xml':
            if self._validate_xml_structure(prompt):
                score += 1
            else:
                issues.append("XML structure invalid: unclosed tags detected")
        else:
            score += 1  # N/A for non-XML formats

        # Gate 2: Completeness (no empty sections)
        if self._validate_completeness(prompt):
            score += 1
        else:
            issues.append("Incomplete: empty sections detected")

        # Gate 3: Token count reasonable
        token_count = len(prompt.split())
        if token_count < 8000:
            score += 1
        else:
            issues.append(f"Token count high: ~{token_count} words (recommended < 8000)")

        # Gate 4: No placeholders
        if not re.search(r'\[TODO\]|\[FILL.*?\]|\[\.\.\..*?\]', prompt):
            score += 1
        else:
            issues.append("Placeholder text found (TODO, FILL, etc.)")

        # Gate 5: Workflow present
        if 'workflow' in prompt.lower() or 'process' in prompt.lower():
            score += 1
        else:
            issues.append("No clear workflow/process defined")

        # Gate 6: Best practices mentioned
        if 'best practice' in prompt.lower() or 'guideline' in prompt.lower():
            score += 1
        else:
            issues.append("Best practices section missing or incomplete")

        # Gate 7: Examples present
        if 'example' in prompt.lower() and prompt.lower().count('example') >= 2:
            score += 1
        else:
            issues.append("Insufficient examples (need at least 2)")

        return score, issues

    def _validate_xml_structure(self, prompt: str) -> bool:
        """Validate XML tags are properly closed."""
        # Find all XML tags
        opening_tags = re.findall(r'<([^/][^>]*)>', prompt)
        closing_tags = re.findall(r'</([^>]+)>', prompt)

        # Simple validation: same count of opening and closing
        return len(opening_tags) == len(closing_tags)

    def _validate_completeness(self, prompt: str) -> bool:
        """Check for empty sections."""
        # Look for tags with no content
        empty_pattern = r'<([^>]+)>\s*</\1>'
        return not re.search(empty_pattern, prompt)

    def generate(self, responses: Dict[str, Any], format_type: str = 'xml',
                 mode: str = 'core') -> Dict[str, Any]:
        """
        Generate complete mega-prompt.

        Args:
            responses: Questionnaire responses
            format_type: 'xml', 'claude', 'chatgpt', 'gemini', or 'all'
            mode: 'core' or 'advanced'

        Returns:
            Dict with generated prompt(s) and metadata
        """
        result = {
            'formats': {},
            'metadata': {
                'role': responses.get('role'),
                'domain': responses.get('domain'),
                'output_type': responses.get('output_type'),
                'mode': mode,
                'generated_at': datetime.now().isoformat()
            },
            'validation': {}
        }

        # Generate requested format(s)
        if format_type == 'all':
            formats_to_generate = ['xml', 'claude', 'chatgpt', 'gemini']
        else:
            formats_to_generate = [format_type]

        for fmt in formats_to_generate:
            if fmt == 'xml':
                prompt = self.generate_xml_format(responses)
            elif fmt == 'claude':
                prompt = self.generate_claude_format(responses)
            elif fmt == 'chatgpt':
                prompt = self.generate_chatgpt_format(responses)
            elif fmt == 'gemini':
                prompt = self.generate_gemini_format(responses)
            else:
                raise ValueError(f"Unknown format: {fmt}")

            # Validate
            score, issues = self.validate_prompt(prompt, fmt)

            result['formats'][fmt] = prompt
            result['validation'][fmt] = {
                'score': score,
                'max_score': 7,
                'passed': score >= 6,
                'issues': issues
            }

        return result


def create_markdown_document(result: Dict[str, Any], mode: str) -> str:
    """Create complete markdown document with prompt(s) and instructions."""
    metadata = result['metadata']
    role = metadata['role']
    domain = metadata.get('domain', 'General')
    output_type = metadata.get('output_type', 'Comprehensive')

    doc = f"""# {role} Mega-Prompt

## Metadata
- **Created**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Role**: {role}
- **Domain**: {domain}
- **Output Type**: {output_type}
- **Mode**: {mode}
- **Generated by**: Prompt Suite v1.0

---

## Quality Validation

"""

    # Add validation results
    for fmt, validation in result['validation'].items():
        status = "✅ PASSED" if validation['passed'] else "⚠️ NEEDS REVIEW"
        doc += f"**{fmt.upper()} Format**: {status} ({validation['score']}/7)\n"
        if validation['issues']:
            doc += f"Issues:\n"
            for issue in validation['issues']:
                doc += f"- {issue}\n"
        doc += "\n"

    doc += "---\n\n"

    # Add each format
    for fmt, prompt in result['formats'].items():
        doc += f"## {fmt.upper()} Format\n\n"

        if fmt == 'xml':
            doc += "**Best for:** All LLMs, maximum compatibility, clear structure\n\n"
            doc += "**How to use:**\n"
            doc += "1. Copy the entire `<mega_prompt>` block below\n"
            doc += "2. Paste into your LLM conversation\n"
            doc += "3. Follow with your specific request\n\n"
            doc += "```xml\n"
            doc += prompt
            doc += "\n```\n\n"

        elif fmt == 'claude':
            doc += "**Best for:** Claude conversations, system-level configuration\n\n"
            doc += "**How to use:**\n"
            doc += "1. Copy the prompt below\n"
            doc += "2. Paste as system prompt or start of conversation\n"
            doc += "3. Claude maintains this configuration throughout\n\n"
            doc += "```markdown\n"
            doc += prompt
            doc += "\n```\n\n"

        elif fmt == 'chatgpt':
            doc += "**Best for:** ChatGPT persistent configuration\n\n"
            doc += "**How to use:**\n"
            doc += "1. Go to ChatGPT Settings → Personalization → Custom Instructions\n"
            doc += "2. Split prompt at '**How would you like ChatGPT to respond?**'\n"
            doc += "3. Paste first part in top box, second part in bottom box\n\n"
            doc += "```\n"
            doc += prompt
            doc += "\n```\n\n"

        elif fmt == 'gemini':
            doc += "**Best for:** Google Gemini conversations\n\n"
            doc += "**How to use:**\n"
            doc += "1. Copy the prompt below\n"
            doc += "2. Paste at start of Gemini conversation\n"
            doc += "3. Gemini maintains configuration\n\n"
            doc += "```markdown\n"
            doc += prompt
            doc += "\n```\n\n"

        doc += "---\n\n"

    # Add tips
    doc += """## Tips for Best Results

1. **Test with sample queries** - Validate the prompt works as expected
2. **Start with specific requests** - Provide clear context in your queries
3. **Iterate on sections** - Refine specific parts rather than regenerating
4. **Save successful versions** - Keep prompts that work well
5. **Monitor responses** - Note what works and what needs adjustment

## Next Steps

1. Copy your preferred format above
2. Test with 2-3 real queries
3. Note effectiveness
4. Request refinements if needed

---

*Generated by Prompt Suite - World-Class Prompt Powerhouse*
*Learn more: https://github.com/your-repo/prompt-suite*
"""

    return doc


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Generate world-class mega-prompts in multiple formats',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate from JSON config
  python generate_prompt.py --responses config.json --format xml --mode core --output prompt.md

  # Use a preset
  python generate_prompt.py --preset fullstack-engineer --format claude --mode advanced --output prompt.md

  # Generate all formats
  python generate_prompt.py --responses config.json --format all --mode core --output prompt.md
"""
    )

    parser.add_argument('--responses', help='Path to responses JSON file')
    parser.add_argument('--preset', help='Use a quick-start preset')
    parser.add_argument('--format', required=True,
                       choices=['xml', 'claude', 'chatgpt', 'gemini', 'all'],
                       help='Output format')
    parser.add_argument('--mode', default='core', choices=['core', 'advanced'],
                       help='Generation mode (default: core)')
    parser.add_argument('--output', required=True, help='Output markdown file path')

    args = parser.parse_args()

    # Load responses or preset
    generator = PromptGenerator()

    if args.preset:
        responses = generator.load_preset(args.preset)
        print(f"✓ Loaded preset: {args.preset}")
    elif args.responses:
        responses = generator.load_responses(args.responses)
        print(f"✓ Loaded responses from: {args.responses}")
    else:
        parser.error("Either --responses or --preset is required")

    # Generate prompt
    print(f"🔄 Generating {args.format} format in {args.mode} mode...")
    result = generator.generate(responses, args.format, args.mode)

    # Validate
    print("\n📊 Quality Validation:")
    for fmt, validation in result['validation'].items():
        status = "✅ PASSED" if validation['passed'] else "⚠️ REVIEW NEEDED"
        print(f"  {fmt.upper()}: {status} ({validation['score']}/7)")
        if validation['issues']:
            for issue in validation['issues']:
                print(f"    - {issue}")

    # Create markdown document
    markdown_doc = create_markdown_document(result, args.mode)

    # Write output
    with open(args.output, 'w') as f:
        f.write(markdown_doc)

    print(f"\n✅ Mega-prompt generated successfully!")
    print(f"📁 Output: {args.output}")
    print(f"📊 Total formats: {len(result['formats'])}")
    print(f"⏱️  Generated at: {result['metadata']['generated_at']}")


if __name__ == "__main__":
    main()
