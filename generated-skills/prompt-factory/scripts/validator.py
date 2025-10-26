#!/usr/bin/env python3
"""
Prompt Suite - Validator

Validate prompt quality against 7-point quality gates.
Ensures prompts meet production standards before deployment.

Usage:
    python validator.py --prompt my-prompt.md --report validation.json
    python validator.py --dir ./prompts/ --report batch-validation.json
    python validator.py --prompt prompt.md --fail-on-error
"""

import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any, Tuple
from datetime import datetime


class PromptValidator:
    """Validate prompt quality with 7-point validation gates."""

    def __init__(self):
        self.gates = [
            ('xml_structure', 'XML Structure Valid'),
            ('completeness', 'No Empty Sections'),
            ('token_count', 'Token Count Reasonable'),
            ('no_placeholders', 'No Placeholder Text'),
            ('actionable_workflow', 'Workflow Actionable'),
            ('best_practices', 'Best Practices Present'),
            ('examples_present', 'Examples Included')
        ]

    def validate(self, prompt: str, format_hint: str = 'auto') -> Dict[str, Any]:
        """
        Run all 7 validation gates.

        Args:
            prompt: Prompt text to validate
            format_hint: 'xml', 'claude', 'chatgpt', 'gemini', or 'auto'

        Returns:
            Validation results dictionary
        """
        # Auto-detect format if not specified
        if format_hint == 'auto':
            format_hint = self._detect_format(prompt)

        results = {
            'format': format_hint,
            'timestamp': datetime.now().isoformat(),
            'gates': {},
            'score': 0,
            'max_score': 7,
            'passed': False,
            'issues': [],
            'warnings': [],
            'recommendations': []
        }

        # Gate 1: XML Structure
        if format_hint == 'xml':
            passed, details = self._check_xml_structure(prompt)
        else:
            passed, details = True, "N/A for non-XML format"

        results['gates']['xml_structure'] = {
            'passed': passed,
            'details': details
        }
        if passed:
            results['score'] += 1
        else:
            results['issues'].append(f"XML Structure: {details}")

        # Gate 2: Completeness
        passed, details = self._check_completeness(prompt)
        results['gates']['completeness'] = {
            'passed': passed,
            'details': details
        }
        if passed:
            results['score'] += 1
        else:
            results['issues'].append(f"Completeness: {details}")

        # Gate 3: Token Count
        passed, details, token_count = self._check_token_count(prompt)
        results['gates']['token_count'] = {
            'passed': passed,
            'details': details,
            'count': token_count
        }
        if passed:
            results['score'] += 1
        elif token_count < 15000:
            results['score'] += 1  # Warning but not failure
            results['warnings'].append(f"Token count high: ~{token_count} words")
        else:
            results['issues'].append(f"Token Count: {details}")

        # Gate 4: No Placeholders
        passed, details, found_placeholders = self._check_placeholders(prompt)
        results['gates']['no_placeholders'] = {
            'passed': passed,
            'details': details,
            'placeholders': found_placeholders
        }
        if passed:
            results['score'] += 1
        else:
            results['issues'].append(f"Placeholders: {details}")

        # Gate 5: Actionable Workflow
        passed, details = self._check_workflow(prompt)
        results['gates']['actionable_workflow'] = {
            'passed': passed,
            'details': details
        }
        if passed:
            results['score'] += 1
        else:
            results['issues'].append(f"Workflow: {details}")

        # Gate 6: Best Practices
        passed, details = self._check_best_practices(prompt)
        results['gates']['best_practices'] = {
            'passed': passed,
            'details': details
        }
        if passed:
            results['score'] += 1
        else:
            results['issues'].append(f"Best Practices: {details}")

        # Gate 7: Examples Present
        passed, details, example_count = self._check_examples(prompt)
        results['gates']['examples_present'] = {
            'passed': passed,
            'details': details,
            'count': example_count
        }
        if passed:
            results['score'] += 1
        else:
            results['issues'].append(f"Examples: {details}")

        # Overall pass/fail (need 6/7 to pass)
        results['passed'] = results['score'] >= 6

        # Add recommendations
        results['recommendations'] = self._generate_recommendations(results)

        return results

    def _detect_format(self, prompt: str) -> str:
        """Auto-detect prompt format."""
        if '<mega_prompt>' in prompt:
            return 'xml'
        elif 'System Configuration:' in prompt or '## Your Mission' in prompt:
            return 'claude'
        elif '**What would you like ChatGPT to know' in prompt:
            return 'chatgpt'
        elif '## Role Configuration' in prompt and 'Apply this configuration' in prompt:
            return 'gemini'
        else:
            return 'unknown'

    def _check_xml_structure(self, prompt: str) -> Tuple[bool, str]:
        """Validate XML tags are properly closed."""
        # Extract tag pairs
        opening_tags = re.findall(r'<([^/\s][^>]*)>', prompt)
        closing_tags = re.findall(r'</([^>]+)>', prompt)

        # Filter out self-closing or special tags
        opening_tags = [tag.split()[0] for tag in opening_tags if not tag.endswith('/')]
        closing_tags = [tag.strip() for tag in closing_tags]

        # Check balance
        if len(opening_tags) != len(closing_tags):
            return False, f"Unbalanced tags: {len(opening_tags)} opening, {len(closing_tags)} closing"

        # Check for unclosed specific tags
        important_tags = ['mega_prompt', 'role', 'mission', 'context', 'workflow']
        for tag in important_tags:
            open_count = opening_tags.count(tag)
            close_count = closing_tags.count(tag)
            if open_count != close_count:
                return False, f"Tag '{tag}' unbalanced: {open_count} open, {close_count} close"

        return True, f"All {len(opening_tags)} tags properly closed"

    def _check_completeness(self, prompt: str) -> Tuple[bool, str]:
        """Check for empty sections or missing content."""
        # Look for empty XML tags
        empty_xml = re.findall(r'<([^/][^>]*)>\s*</\1>', prompt)
        if empty_xml:
            return False, f"Empty sections found: {', '.join(set(empty_xml))}"

        # Look for sections with only whitespace
        section_pattern = r'##\s+([^\n]+)\s*\n\s*(?=##|$)'
        empty_sections = re.findall(section_pattern, prompt)
        if empty_sections:
            return False, f"Empty heading sections: {len(empty_sections)}"

        # Check minimum content length
        if len(prompt.strip()) < 1000:
            return False, f"Prompt too short: {len(prompt)} characters (minimum 1000)"

        return True, "All sections have content"

    def _check_token_count(self, prompt: str) -> Tuple[bool, str, int]:
        """Check token count is reasonable."""
        # Rough token estimation: ~0.75 words per token
        word_count = len(prompt.split())
        estimated_tokens = int(word_count * 0.75)

        if estimated_tokens > 8000:
            return False, f"Token count very high: ~{estimated_tokens} tokens", word_count
        elif estimated_tokens > 6000:
            return True, f"Token count acceptable but high: ~{estimated_tokens} tokens", word_count
        else:
            return True, f"Token count optimal: ~{estimated_tokens} tokens", word_count

    def _check_placeholders(self, prompt: str) -> Tuple[bool, str, List[str]]:
        """Check for placeholder text that needs filling."""
        placeholder_patterns = [
            r'\[TODO[^\]]*\]',
            r'\[FILL[^\]]*\]',
            r'\[INSERT[^\]]*\]',
            r'\[PLACEHOLDER[^\]]*\]',
            r'\[TBD[^\]]*\]',
            r'\[XXX[^\]]*\]',
            r'\[\.\.\..*?\]',
        ]

        found = []
        for pattern in placeholder_patterns:
            matches = re.findall(pattern, prompt, re.IGNORECASE)
            found.extend(matches)

        if found:
            return False, f"Found {len(found)} placeholder(s)", list(set(found))[:5]
        else:
            return True, "No placeholders found", []

    def _check_workflow(self, prompt: str) -> Tuple[bool, str]:
        """Check for presence of actionable workflow."""
        workflow_indicators = [
            'workflow', 'process', 'approach', 'method', 'steps',
            'phase', 'stage', '1.', '2.', '3.', 'first', 'then', 'next'
        ]

        # Count workflow indicators
        indicators_found = sum(1 for indicator in workflow_indicators
                             if indicator.lower() in prompt.lower())

        if indicators_found >= 5:
            return True, f"Clear workflow present ({indicators_found} indicators)"
        elif indicators_found >= 3:
            return True, f"Basic workflow present ({indicators_found} indicators)"
        else:
            return False, f"Workflow unclear ({indicators_found} indicators, need 3+)"

    def _check_best_practices(self, prompt: str) -> Tuple[bool, str]:
        """Check for inclusion of best practices."""
        best_practice_indicators = [
            'best practice', 'guideline', 'standard', 'recommendation',
            'should', 'must', 'avoid', 'ensure', 'always', 'never',
            'principle', 'rule', 'convention'
        ]

        indicators_found = sum(1 for indicator in best_practice_indicators
                             if indicator.lower() in prompt.lower())

        if indicators_found >= 8:
            return True, f"Comprehensive best practices ({indicators_found} indicators)"
        elif indicators_found >= 5:
            return True, f"Good best practices coverage ({indicators_found} indicators)"
        else:
            return False, f"Insufficient best practices ({indicators_found} indicators, need 5+)"

    def _check_examples(self, prompt: str) -> Tuple[bool, str, int]:
        """Check for presence of examples."""
        # Count explicit example sections
        example_sections = len(re.findall(r'##?\s*Example|<example', prompt, re.IGNORECASE))

        # Count example indicators
        example_words = prompt.lower().count('example')
        for_instance = prompt.lower().count('for instance')
        for_example = prompt.lower().count('for example')
        such_as = prompt.lower().count('such as')

        total_indicators = example_words + for_instance + for_example + such_as

        if example_sections >= 2 or total_indicators >= 4:
            return True, f"Good examples: {example_sections} sections, {total_indicators} indicators", example_sections
        elif example_sections >= 1 or total_indicators >= 2:
            return True, f"Basic examples: {example_sections} sections, {total_indicators} indicators", example_sections
        else:
            return False, f"Insufficient examples: {example_sections} sections (need 2+)", example_sections

    def _generate_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on validation results."""
        recommendations = []

        # Check each gate for specific recommendations
        gates = results['gates']

        if not gates['xml_structure']['passed']:
            recommendations.append("Fix XML structure: Ensure all tags are properly closed")

        if not gates['completeness']['passed']:
            recommendations.append("Fill empty sections with relevant content")

        if gates['token_count']['count'] > 6000:
            recommendations.append("Consider reducing token count: Remove redundancies, consolidate examples")

        if not gates['no_placeholders']['passed']:
            placeholders = gates['no_placeholders'].get('placeholders', [])
            recommendations.append(f"Replace placeholders: {', '.join(placeholders[:3])}")

        if not gates['actionable_workflow']['passed']:
            recommendations.append("Add clear workflow: Include numbered steps or phases")

        if not gates['best_practices']['passed']:
            recommendations.append("Enhance best practices: Add domain-specific guidelines and rules")

        if not gates['examples_present']['passed']:
            recommendations.append("Add examples: Include at least 2 concrete examples demonstrating expected behavior")

        # Overall recommendation
        if results['passed']:
            recommendations.append("✅ Prompt passes validation - ready for production use")
        else:
            recommendations.append(f"⚠️ Address {len(results['issues'])} issues before deployment")

        return recommendations


def create_validation_report(result: Dict[str, Any], prompt_file: Path) -> str:
    """Create human-readable validation report."""
    status = "✅ PASSED" if result['passed'] else "❌ FAILED"

    report = f"""# Prompt Validation Report

**File:** `{prompt_file.name}`
**Validated:** {result['timestamp']}
**Format:** {result['format']}
**Score:** {result['score']}/7
**Status:** {status}

## Validation Gates

"""

    # Add each gate result
    gate_names = {
        'xml_structure': 'XML Structure Valid',
        'completeness': 'No Empty Sections',
        'token_count': 'Token Count Reasonable',
        'no_placeholders': 'No Placeholder Text',
        'actionable_workflow': 'Workflow Actionable',
        'best_practices': 'Best Practices Present',
        'examples_present': 'Examples Included'
    }

    for gate_key, gate_name in gate_names.items():
        gate = result['gates'][gate_key]
        status_icon = "✅" if gate['passed'] else "❌"
        report += f"\n### {status_icon} {gate_name}\n\n"
        report += f"{gate['details']}\n"

    # Add issues
    if result['issues']:
        report += f"\n## Issues ({len(result['issues'])})\n\n"
        for issue in result['issues']:
            report += f"- ❌ {issue}\n"

    # Add warnings
    if result['warnings']:
        report += f"\n## Warnings ({len(result['warnings'])})\n\n"
        for warning in result['warnings']:
            report += f"- ⚠️ {warning}\n"

    # Add recommendations
    if result['recommendations']:
        report += f"\n## Recommendations\n\n"
        for rec in result['recommendations']:
            report += f"- {rec}\n"

    report += f"\n---\n\n*Generated by Prompt Suite Validator v1.0*\n"

    return report


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Validate prompt quality with 7-point validation gates',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Validation Gates:
  1. XML Structure Valid (if XML format)
  2. No Empty Sections
  3. Token Count Reasonable (<8K)
  4. No Placeholder Text
  5. Workflow Actionable
  6. Best Practices Present
  7. Examples Included

Examples:
  # Validate single prompt
  python validator.py --prompt my-prompt.md --report validation.json

  # Validate directory
  python validator.py --dir ./prompts/ --report batch-validation.json

  # Fail on validation errors
  python validator.py --prompt prompt.md --fail-on-error
"""
    )

    parser.add_argument('--prompt', help='Single prompt file to validate')
    parser.add_argument('--dir', help='Directory of prompts to validate')
    parser.add_argument('--report', help='Output JSON report file')
    parser.add_argument('--fail-on-error', action='store_true',
                       help='Exit with error code if validation fails')
    parser.add_argument('--format', default='auto',
                       choices=['auto', 'xml', 'claude', 'chatgpt', 'gemini'],
                       help='Prompt format (default: auto-detect)')

    args = parser.parse_args()

    if not args.prompt and not args.dir:
        parser.error("Either --prompt or --dir is required")

    validator = PromptValidator()
    results = []

    # Validate single prompt or directory
    if args.prompt:
        prompt_file = Path(args.prompt)
        if not prompt_file.exists():
            parser.error(f"Prompt file not found: {args.prompt}")

        print(f"📝 Validating: {prompt_file.name}")
        prompt_text = prompt_file.read_text()
        result = validator.validate(prompt_text, args.format)

        # Print result
        status = "✅ PASSED" if result['passed'] else "❌ FAILED"
        print(f"\n{status} ({result['score']}/7)")

        if result['issues']:
            print(f"\n❌ Issues:")
            for issue in result['issues']:
                print(f"   - {issue}")

        if result['warnings']:
            print(f"\n⚠️  Warnings:")
            for warning in result['warnings']:
                print(f"   - {warning}")

        # Create readable report
        report_text = create_validation_report(result, prompt_file)
        report_file = prompt_file.parent / f"{prompt_file.stem}-validation-report.md"
        report_file.write_text(report_text)
        print(f"\n📋 Report: {report_file}")

        results.append(result)

    elif args.dir:
        prompt_dir = Path(args.dir)
        if not prompt_dir.exists():
            parser.error(f"Directory not found: {args.dir}")

        prompt_files = list(prompt_dir.glob('*.md'))
        print(f"📁 Validating {len(prompt_files)} prompts in: {prompt_dir}")

        for prompt_file in prompt_files:
            print(f"\n📝 {prompt_file.name}...")
            prompt_text = prompt_file.read_text()
            result = validator.validate(prompt_text, args.format)

            status = "✅" if result['passed'] else "❌"
            print(f"   {status} {result['score']}/7")

            results.append({
                'file': str(prompt_file),
                **result
            })

    # Save JSON report
    if args.report:
        report_data = {
            'timestamp': datetime.now().isoformat(),
            'total': len(results),
            'passed': sum(1 for r in results if r['passed']),
            'failed': sum(1 for r in results if not r['passed']),
            'results': results
        }

        with open(args.report, 'w') as f:
            json.dump(report_data, f, indent=2)

        print(f"\n📊 JSON Report: {args.report}")

    # Summary
    passed = sum(1 for r in results if r['passed'])
    failed = len(results) - passed

    print(f"\n{'=' * 60}")
    print(f"📊 Validation Summary")
    print(f"{'=' * 60}")
    print(f"Total: {len(results)}")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"Success Rate: {(passed / len(results) * 100):.1f}%")

    # Exit with error if requested
    if args.fail_on_error and failed > 0:
        print(f"\n❌ Validation failed for {failed} prompt(s)")
        exit(1)
    else:
        print(f"\n✅ Validation complete!")
        exit(0)


if __name__ == "__main__":
    main()
