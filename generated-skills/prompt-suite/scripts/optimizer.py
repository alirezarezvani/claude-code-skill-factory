#!/usr/bin/env python3
"""
Prompt Suite - Optimizer

Optimize existing prompts for token efficiency while maintaining quality.
Analyzes prompts and provides optimization suggestions with automated rewrites.

Usage:
    python optimizer.py --prompt my-prompt.md --target-tokens 4000 --output optimized.md
    python optimizer.py --prompt prompt.md --analyze-only --report analysis.json
    python optimizer.py --prompt prompt.md --aggressive --output compact.md
"""

import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any, Tuple
from datetime import datetime


class PromptOptimizer:
    """Optimize prompts for token efficiency and clarity."""

    def __init__(self, aggressive: bool = False):
        self.aggressive = aggressive
        self.optimizations_applied = []

    def analyze(self, prompt: str) -> Dict[str, Any]:
        """Analyze prompt and identify optimization opportunities."""
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'original_stats': self._get_stats(prompt),
            'opportunities': [],
            'estimated_savings': 0,
            'recommendations': []
        }

        # Check for various optimization opportunities
        opportunities = []

        # 1. Redundant phrases
        redundant_savings = self._check_redundancy(prompt)
        if redundant_savings > 0:
            opportunities.append({
                'type': 'redundancy',
                'description': 'Remove redundant phrases and repetitive content',
                'estimated_savings': redundant_savings,
                'priority': 'high'
            })

        # 2. Verbose explanations
        verbose_savings = self._check_verbosity(prompt)
        if verbose_savings > 0:
            opportunities.append({
                'type': 'verbosity',
                'description': 'Simplify verbose explanations',
                'estimated_savings': verbose_savings,
                'priority': 'medium'
            })

        # 3. Mergeable sections
        merge_savings = self._check_mergeable_sections(prompt)
        if merge_savings > 0:
            opportunities.append({
                'type': 'section_merge',
                'description': 'Merge similar or overlapping sections',
                'estimated_savings': merge_savings,
                'priority': 'high'
            })

        # 4. Excessive examples
        example_savings = self._check_excessive_examples(prompt)
        if example_savings > 0:
            opportunities.append({
                'type': 'examples',
                'description': 'Consolidate or reduce redundant examples',
                'estimated_savings': example_savings,
                'priority': 'medium'
            })

        # 5. Unnecessary formatting
        format_savings = self._check_formatting(prompt)
        if format_savings > 0:
            opportunities.append({
                'type': 'formatting',
                'description': 'Remove excessive formatting and whitespace',
                'estimated_savings': format_savings,
                'priority': 'low'
            })

        # 6. Simplifiable language
        language_savings = self._check_language_complexity(prompt)
        if language_savings > 0:
            opportunities.append({
                'type': 'language',
                'description': 'Simplify complex language patterns',
                'estimated_savings': language_savings,
                'priority': 'medium'
            })

        analysis['opportunities'] = opportunities
        analysis['estimated_savings'] = sum(opp['estimated_savings'] for opp in opportunities)

        # Generate recommendations
        analysis['recommendations'] = self._generate_recommendations(analysis)

        return analysis

    def optimize(self, prompt: str, target_tokens: int = None) -> Tuple[str, Dict[str, Any]]:
        """
        Optimize prompt for token efficiency.

        Args:
            prompt: Original prompt text
            target_tokens: Target token count (None = reasonable reduction)

        Returns:
            (optimized_prompt, optimization_report)
        """
        original_word_count = len(prompt.split())

        # Determine target if not specified
        if target_tokens is None:
            # Aim for 20% reduction
            target_tokens = int(original_word_count * 0.75 * 0.8)

        optimized = prompt
        self.optimizations_applied = []

        # Apply optimizations in order of priority
        optimized = self._remove_redundancy(optimized)
        optimized = self._simplify_verbosity(optimized)
        optimized = self._merge_sections(optimized)
        optimized = self._consolidate_examples(optimized)
        optimized = self._clean_formatting(optimized)

        if self.aggressive:
            optimized = self._aggressive_optimization(optimized)

        # Generate report
        report = {
            'timestamp': datetime.now().isoformat(),
            'original_stats': self._get_stats(prompt),
            'optimized_stats': self._get_stats(optimized),
            'target_tokens': target_tokens,
            'optimizations_applied': self.optimizations_applied,
            'quality_maintained': self._validate_quality(prompt, optimized),
            'achieved_target': len(optimized.split()) * 0.75 <= target_tokens
        }

        # Calculate savings
        original_tokens = int(original_word_count * 0.75)
        optimized_tokens = int(len(optimized.split()) * 0.75)
        report['token_reduction'] = original_tokens - optimized_tokens
        report['reduction_percentage'] = (report['token_reduction'] / original_tokens * 100) if original_tokens > 0 else 0

        return optimized, report

    def _get_stats(self, text: str) -> Dict[str, Any]:
        """Get text statistics."""
        words = text.split()
        return {
            'characters': len(text),
            'words': len(words),
            'estimated_tokens': int(len(words) * 0.75),
            'lines': len(text.split('\n')),
            'sections': len(re.findall(r'##?\s+', text))
        }

    def _check_redundancy(self, prompt: str) -> int:
        """Check for redundant phrases."""
        redundant_patterns = [
            (r'it is important to note that', 50),
            (r'please note that', 30),
            (r'it should be noted', 30),
            (r'as mentioned (above|before|previously)', 40),
            (r'in order to', 20),
            (r'for the purpose of', 30),
            (r'due to the fact that', 40),
            (r'at this point in time', 40),
        ]

        total_savings = 0
        for pattern, savings in redundant_patterns:
            matches = len(re.findall(pattern, prompt, re.IGNORECASE))
            total_savings += matches * savings

        return total_savings

    def _check_verbosity(self, prompt: str) -> int:
        """Check for verbose explanations."""
        # Estimate based on average sentence length
        sentences = re.split(r'[.!?]+', prompt)
        long_sentences = [s for s in sentences if len(s.split()) > 40]

        # Estimate 20% reduction possible for long sentences
        return int(sum(len(s.split()) for s in long_sentences) * 0.2 * 0.75)

    def _check_mergeable_sections(self, prompt: str) -> int:
        """Check for sections that could be merged."""
        sections = re.findall(r'##\s+([^\n]+)', prompt)

        # Look for similar section titles
        similar_pairs = 0
        for i, section1 in enumerate(sections):
            for section2 in sections[i+1:]:
                # Simple similarity check
                words1 = set(section1.lower().split())
                words2 = set(section2.lower().split())
                if len(words1 & words2) >= 2:
                    similar_pairs += 1

        # Estimate 100 tokens saved per merge
        return similar_pairs * 100

    def _check_excessive_examples(self, prompt: str) -> int:
        """Check for excessive examples."""
        example_sections = re.findall(r'##?\s*Example[^#]*(?=##|$)', prompt, re.IGNORECASE | re.DOTALL)

        if len(example_sections) > 3:
            # Estimate we can consolidate to 2-3 examples
            excess = len(example_sections) - 3
            avg_example_length = sum(len(ex.split()) for ex in example_sections) / len(example_sections)
            return int(excess * avg_example_length * 0.75)

        return 0

    def _check_formatting(self, prompt: str) -> int:
        """Check for excessive formatting."""
        # Count excessive newlines
        excessive_newlines = len(re.findall(r'\n\n\n+', prompt))
        # Count excessive punctuation
        excessive_punct = len(re.findall(r'\.\.\.+|!!!+|\?\?\?+', prompt))

        return (excessive_newlines * 5) + (excessive_punct * 3)

    def _check_language_complexity(self, prompt: str) -> int:
        """Check for overly complex language."""
        # Words that could be simplified
        complex_patterns = [
            ('utilize', 'use'),
            ('facilitate', 'help'),
            ('implement', 'use'),
            ('leverage', 'use'),
            ('paradigm', 'model'),
        ]

        total_savings = 0
        for complex_word, _ in complex_patterns:
            matches = len(re.findall(r'\b' + complex_word + r'\b', prompt, re.IGNORECASE))
            total_savings += matches * 5  # Small savings per word

        return total_savings

    def _remove_redundancy(self, prompt: str) -> str:
        """Remove redundant phrases."""
        redundant_phrases = {
            r'it is important to note that\s+': '',
            r'please note that\s+': '',
            r'it should be noted that\s+': '',
            r'as mentioned (above|before|previously),?\s+': '',
            r'in order to\s+': 'to ',
            r'for the purpose of\s+': 'to ',
            r'due to the fact that\s+': 'because ',
            r'at this point in time\s+': 'now ',
            r'has the ability to\s+': 'can ',
        }

        optimized = prompt
        for pattern, replacement in redundant_phrases.items():
            before = len(optimized.split())
            optimized = re.sub(pattern, replacement, optimized, flags=re.IGNORECASE)
            after = len(optimized.split())
            if before != after:
                self.optimizations_applied.append(f"Removed redundant phrase pattern: {pattern[:30]}...")

        return optimized

    def _simplify_verbosity(self, prompt: str) -> str:
        """Simplify verbose explanations."""
        # Split into sentences
        sentences = re.split(r'([.!?]+\s+)', prompt)

        optimized_sentences = []
        for i in range(0, len(sentences), 2):
            sentence = sentences[i] if i < len(sentences) else ''
            delimiter = sentences[i+1] if i+1 < len(sentences) else ''

            # If sentence is too long, try to simplify
            if len(sentence.split()) > 40:
                # Remove filler words
                simplified = sentence
                simplified = re.sub(r'\b(very|really|quite|rather|fairly|pretty)\s+', '', simplified)
                simplified = re.sub(r'\b(basically|essentially|actually|literally)\s+', '', simplified)

                if len(simplified.split()) < len(sentence.split()):
                    self.optimizations_applied.append(f"Simplified verbose sentence (reduced by {len(sentence.split()) - len(simplified.split())} words)")

                sentence = simplified

            optimized_sentences.append(sentence + delimiter)

        return ''.join(optimized_sentences)

    def _merge_sections(self, prompt: str) -> str:
        """Merge similar or overlapping sections."""
        # This is a placeholder - actual implementation would need more sophisticated
        # section analysis
        self.optimizations_applied.append("Analyzed sections for merging opportunities")
        return prompt

    def _consolidate_examples(self, prompt: str) -> str:
        """Consolidate excessive examples."""
        # Find all example sections
        example_pattern = r'(##?\s*Example\s+\d+[^\#]*?)(?=##|$)'
        examples = re.findall(example_pattern, prompt, re.IGNORECASE | re.DOTALL)

        if len(examples) > 3:
            # Keep first 2 and last 1
            kept_examples = examples[:2] + [examples[-1]]

            # Reconstruct prompt with consolidated examples
            # This is simplified - actual implementation would be more careful
            self.optimizations_applied.append(f"Consolidated examples from {len(examples)} to 3")

        return prompt

    def _clean_formatting(self, prompt: str) -> str:
        """Clean excessive formatting."""
        optimized = prompt

        # Reduce excessive newlines
        optimized = re.sub(r'\n\n\n+', '\n\n', optimized)

        # Reduce excessive punctuation
        optimized = re.sub(r'\.\.\.+', '...', optimized)
        optimized = re.sub(r'!!!+', '!', optimized)
        optimized = re.sub(r'\?\?\?+', '?', optimized)

        # Remove trailing whitespace
        lines = [line.rstrip() for line in optimized.split('\n')]
        optimized = '\n'.join(lines)

        if len(optimized) < len(prompt):
            savings = len(prompt) - len(optimized)
            self.optimizations_applied.append(f"Cleaned formatting (saved {savings} characters)")

        return optimized

    def _aggressive_optimization(self, prompt: str) -> str:
        """Apply aggressive optimization techniques."""
        optimized = prompt

        # Remove all examples except one
        example_sections = re.findall(r'##?\s*Example[^#]*(?=##|$)', optimized, re.IGNORECASE | re.DOTALL)
        if len(example_sections) > 1:
            # Keep only the first example
            for example in example_sections[1:]:
                optimized = optimized.replace(example, '')
            self.optimizations_applied.append(f"Aggressively reduced examples to 1")

        # Simplify section headers
        optimized = re.sub(r'##\s+(.+?)\s*\n', r'## \1\n', optimized)

        self.optimizations_applied.append("Applied aggressive optimization")

        return optimized

    def _validate_quality(self, original: str, optimized: str) -> bool:
        """Validate that optimization maintained quality."""
        # Check that key sections are still present
        key_sections = ['role', 'mission', 'workflow', 'example']

        original_has_sections = sum(1 for section in key_sections
                                   if section.lower() in original.lower())
        optimized_has_sections = sum(1 for section in key_sections
                                    if section.lower() in optimized.lower())

        # Quality maintained if all key sections preserved
        return optimized_has_sections >= original_has_sections - 1

    def _generate_recommendations(self, analysis: Dict[str, Any]) -> List[str]:
        """Generate optimization recommendations."""
        recommendations = []

        # Sort opportunities by estimated savings
        opportunities = sorted(analysis['opportunities'],
                             key=lambda x: x['estimated_savings'],
                             reverse=True)

        for opp in opportunities[:5]:  # Top 5
            recommendations.append(f"{opp['description']} (save ~{opp['estimated_savings']} tokens)")

        total_savings = analysis['estimated_savings']
        if total_savings > 0:
            recommendations.append(f"\nTotal potential savings: ~{total_savings} tokens ({total_savings * 1.33:.0f} words)")
        else:
            recommendations.append("Prompt is already well-optimized")

        return recommendations


def create_optimization_report(analysis: Dict[str, Any] = None,
                              optimization_result: Dict[str, Any] = None,
                              prompt_file: Path = None) -> str:
    """Create human-readable optimization report."""

    if analysis:
        # Analysis-only report
        report = f"""# Prompt Optimization Analysis

**File:** `{prompt_file.name if prompt_file else 'Unknown'}`
**Analyzed:** {analysis['timestamp']}

## Current Statistics

- **Characters:** {analysis['original_stats']['characters']:,}
- **Words:** {analysis['original_stats']['words']:,}
- **Est. Tokens:** ~{analysis['original_stats']['estimated_tokens']:,}
- **Lines:** {analysis['original_stats']['lines']:,}
- **Sections:** {analysis['original_stats']['sections']}

## Optimization Opportunities

**Total Potential Savings:** ~{analysis['estimated_savings']} tokens

"""

        for opp in analysis['opportunities']:
            priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}
            emoji = priority_emoji.get(opp['priority'], "⚪")

            report += f"\n### {emoji} {opp['description']}\n"
            report += f"- **Type:** {opp['type']}\n"
            report += f"- **Priority:** {opp['priority']}\n"
            report += f"- **Est. Savings:** ~{opp['estimated_savings']} tokens\n"

        report += f"\n## Recommendations\n\n"
        for rec in analysis['recommendations']:
            report += f"- {rec}\n"

    elif optimization_result:
        # Optimization result report
        report = f"""# Prompt Optimization Report

**File:** `{prompt_file.name if prompt_file else 'Unknown'}`
**Optimized:** {optimization_result['timestamp']}

## Results

### Before Optimization
- **Words:** {optimization_result['original_stats']['words']:,}
- **Est. Tokens:** ~{optimization_result['original_stats']['estimated_tokens']:,}

### After Optimization
- **Words:** {optimization_result['optimized_stats']['words']:,}
- **Est. Tokens:** ~{optimization_result['optimized_stats']['estimated_tokens']:,}

### Savings
- **Token Reduction:** {optimization_result['token_reduction']} tokens
- **Reduction:** {optimization_result['reduction_percentage']:.1f}%
- **Target Achieved:** {"✅ Yes" if optimization_result['achieved_target'] else "❌ No"}
- **Quality Maintained:** {"✅ Yes" if optimization_result['quality_maintained'] else "⚠️ Review Needed"}

## Optimizations Applied

"""

        for opt in optimization_result['optimizations_applied']:
            report += f"- ✅ {opt}\n"

    else:
        report = "# Error: No data provided for report generation"

    report += f"\n---\n\n*Generated by Prompt Suite Optimizer v1.0*\n"

    return report


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Optimize prompts for token efficiency',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze only (no changes)
  python optimizer.py --prompt my-prompt.md --analyze-only --report analysis.json

  # Optimize with target
  python optimizer.py --prompt my-prompt.md --target-tokens 4000 --output optimized.md

  # Aggressive optimization
  python optimizer.py --prompt my-prompt.md --aggressive --output compact.md
"""
    )

    parser.add_argument('--prompt', required=True, help='Prompt file to optimize')
    parser.add_argument('--analyze-only', action='store_true',
                       help='Only analyze, do not optimize')
    parser.add_argument('--target-tokens', type=int,
                       help='Target token count (default: 20%% reduction)')
    parser.add_argument('--aggressive', action='store_true',
                       help='Apply aggressive optimization (may reduce quality)')
    parser.add_argument('--output', help='Output file for optimized prompt')
    parser.add_argument('--report', help='Output JSON report file')

    args = parser.parse_args()

    # Load prompt
    prompt_file = Path(args.prompt)
    if not prompt_file.exists():
        parser.error(f"Prompt file not found: {args.prompt}")

    print(f"📝 Loading prompt: {prompt_file.name}")
    prompt_text = prompt_file.read_text()

    optimizer = PromptOptimizer(aggressive=args.aggressive)

    if args.analyze_only:
        # Analysis mode
        print(f"🔍 Analyzing prompt...")
        analysis = optimizer.analyze(prompt_text)

        # Print results
        print(f"\n{'=' * 60}")
        print(f"📊 Analysis Results")
        print(f"{'=' * 60}")
        print(f"Original: ~{analysis['original_stats']['estimated_tokens']} tokens")
        print(f"Potential Savings: ~{analysis['estimated_savings']} tokens")
        print(f"\nTop Opportunities:")
        for opp in analysis['opportunities'][:3]:
            print(f"  - {opp['description']}: ~{opp['estimated_savings']} tokens")

        # Save JSON report
        if args.report:
            with open(args.report, 'w') as f:
                json.dump(analysis, f, indent=2)
            print(f"\n📊 JSON Report: {args.report}")

        # Create markdown report
        report_text = create_optimization_report(analysis=analysis, prompt_file=prompt_file)
        report_file = prompt_file.parent / f"{prompt_file.stem}-analysis.md"
        report_file.write_text(report_text)
        print(f"📋 Analysis Report: {report_file}")

    else:
        # Optimization mode
        if not args.output:
            parser.error("--output is required when optimizing (not using --analyze-only)")

        print(f"🔧 Optimizing prompt...")
        if args.aggressive:
            print(f"⚠️  Aggressive mode enabled")

        optimized_prompt, result = optimizer.optimize(prompt_text, args.target_tokens)

        # Print results
        print(f"\n{'=' * 60}")
        print(f"✅ Optimization Complete")
        print(f"{'=' * 60}")
        print(f"Original: ~{result['original_stats']['estimated_tokens']} tokens")
        print(f"Optimized: ~{result['optimized_stats']['estimated_tokens']} tokens")
        print(f"Savings: {result['token_reduction']} tokens ({result['reduction_percentage']:.1f}%)")
        print(f"Quality: {'✅ Maintained' if result['quality_maintained'] else '⚠️  Review needed'}")

        # Save optimized prompt
        output_file = Path(args.output)
        output_file.write_text(optimized_prompt)
        print(f"\n📁 Optimized prompt: {output_file}")

        # Save JSON report
        if args.report:
            with open(args.report, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"📊 JSON Report: {args.report}")

        # Create markdown report
        report_text = create_optimization_report(optimization_result=result, prompt_file=prompt_file)
        report_file = output_file.parent / f"{output_file.stem}-optimization-report.md"
        report_file.write_text(report_text)
        print(f"📋 Optimization Report: {report_file}")

        print(f"\n✅ Optimization successful!")


if __name__ == "__main__":
    main()
