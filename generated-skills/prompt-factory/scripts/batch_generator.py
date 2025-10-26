#!/usr/bin/env python3
"""
Prompt Suite - Batch Generator

Generate multiple prompts from CSV or JSON batch configuration.
Perfect for team-wide rollouts and standardization.

Usage:
    python batch_generator.py --input team-prompts.csv --format xml --mode core --output-dir ./prompts/
    python batch_generator.py --input batch-config.json --format all --parallel 5 --output-dir ./output/
"""

import csv
import json
import argparse
import concurrent.futures
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime
from generate_prompt import PromptGenerator, create_markdown_document


class BatchGenerator:
    """Generate multiple prompts in batch mode."""

    def __init__(self, parallel_workers: int = 3):
        self.parallel_workers = parallel_workers
        self.generator = PromptGenerator()
        self.results = []

    def load_csv_batch(self, filepath: str) -> List[Dict[str, Any]]:
        """Load batch configuration from CSV file."""
        configs = []
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                configs.append(dict(row))
        return configs

    def load_json_batch(self, filepath: str) -> List[Dict[str, Any]]:
        """Load batch configuration from JSON file."""
        with open(filepath, 'r') as f:
            data = json.load(f)

        # Support both array of configs or object with configs key
        if isinstance(data, list):
            return data
        elif 'prompts' in data:
            return data['prompts']
        else:
            raise ValueError("JSON must be array of configs or object with 'prompts' key")

    def generate_single(self, config: Dict[str, Any], format_type: str, mode: str,
                       output_dir: Path) -> Dict[str, Any]:
        """Generate a single prompt from configuration."""
        try:
            # Extract metadata
            name = config.get('name', f"prompt-{datetime.now().timestamp()}")

            print(f"📝 Generating: {name}")

            # Generate prompt
            result = self.generator.generate(config, format_type, mode)

            # Create output filename
            role_slug = config.get('role', 'assistant').lower().replace(' ', '-')
            output_file = output_dir / f"{name}-{role_slug}.md"

            # Create markdown document
            markdown_doc = create_markdown_document(result, mode)

            # Write to file
            output_file.write_text(markdown_doc)

            # Validation summary
            validation_summary = {
                fmt: val['passed']
                for fmt, val in result['validation'].items()
            }

            return {
                'name': name,
                'status': 'success',
                'output_file': str(output_file),
                'validation': validation_summary
            }

        except Exception as e:
            return {
                'name': config.get('name', 'unknown'),
                'status': 'error',
                'error': str(e)
            }

    def generate_batch(self, configs: List[Dict[str, Any]], format_type: str,
                      mode: str, output_dir: Path) -> Dict[str, Any]:
        """Generate multiple prompts in parallel."""
        print(f"\n🚀 Starting batch generation:")
        print(f"   Prompts: {len(configs)}")
        print(f"   Format: {format_type}")
        print(f"   Mode: {mode}")
        print(f"   Workers: {self.parallel_workers}")
        print(f"   Output: {output_dir}")
        print()

        # Ensure output directory exists
        output_dir.mkdir(parents=True, exist_ok=True)

        # Generate prompts in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.parallel_workers) as executor:
            futures = {
                executor.submit(self.generate_single, config, format_type, mode, output_dir): config
                for config in configs
            }

            results = []
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                results.append(result)

                # Print progress
                status_emoji = "✅" if result['status'] == 'success' else "❌"
                print(f"{status_emoji} {result['name']}: {result['status']}")

        # Generate summary
        successful = sum(1 for r in results if r['status'] == 'success')
        failed = len(results) - successful

        summary = {
            'total': len(configs),
            'successful': successful,
            'failed': failed,
            'output_dir': str(output_dir),
            'generated_at': datetime.now().isoformat(),
            'results': results
        }

        return summary


def create_summary_report(summary: Dict[str, Any], output_dir: Path):
    """Create a summary report of batch generation."""
    report = f"""# Batch Generation Report

**Generated:** {summary['generated_at']}
**Output Directory:** {summary['output_dir']}

## Summary

- **Total Prompts:** {summary['total']}
- **Successful:** {summary['successful']} ✅
- **Failed:** {summary['failed']} ❌
- **Success Rate:** {(summary['successful'] / summary['total'] * 100):.1f}%

## Details

"""

    # Add details for each prompt
    for result in summary['results']:
        if result['status'] == 'success':
            report += f"\n### ✅ {result['name']}\n"
            report += f"- **File:** `{Path(result['output_file']).name}`\n"
            report += f"- **Validation:**\n"
            for fmt, passed in result['validation'].items():
                status = "✅ Passed" if passed else "⚠️ Review"
                report += f"  - {fmt.upper()}: {status}\n"
        else:
            report += f"\n### ❌ {result['name']}\n"
            report += f"- **Error:** {result['error']}\n"

    report += f"\n---\n\n*Generated by Prompt Suite Batch Generator v1.0*\n"

    # Write report
    report_file = output_dir / 'batch-generation-report.md'
    report_file.write_text(report)

    return report_file


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Generate multiple prompts in batch mode',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
CSV Format Example:
  name,role,domain,goal,output_type,tech_stack
  backend-api,Senior Backend Engineer,FinTech,Build secure APIs,code,"Python,FastAPI"
  frontend-ui,Frontend Engineer,FinTech,Build UIs,code,"React,TypeScript"

JSON Format Example:
  {
    "prompts": [
      {"name": "backend-api", "role": "Senior Backend Engineer", ...},
      {"name": "frontend-ui", "role": "Frontend Engineer", ...}
    ]
  }

Examples:
  # From CSV
  python batch_generator.py --input team.csv --format xml --mode core --output-dir ./prompts/

  # From JSON with parallel processing
  python batch_generator.py --input batch.json --format all --parallel 10 --output-dir ./output/
"""
    )

    parser.add_argument('--input', required=True,
                       help='Input CSV or JSON file with batch configuration')
    parser.add_argument('--format', required=True,
                       choices=['xml', 'claude', 'chatgpt', 'gemini', 'all'],
                       help='Output format for all prompts')
    parser.add_argument('--mode', default='core', choices=['core', 'advanced'],
                       help='Generation mode (default: core)')
    parser.add_argument('--output-dir', required=True,
                       help='Output directory for generated prompts')
    parser.add_argument('--parallel', type=int, default=3,
                       help='Number of parallel workers (default: 3)')
    parser.add_argument('--report', action='store_true',
                       help='Generate summary report (default: True)')

    args = parser.parse_args()

    # Determine input format
    input_path = Path(args.input)
    if not input_path.exists():
        parser.error(f"Input file not found: {args.input}")

    # Load configurations
    batch_gen = BatchGenerator(parallel_workers=args.parallel)

    if input_path.suffix == '.csv':
        print(f"📄 Loading CSV batch configuration...")
        configs = batch_gen.load_csv_batch(args.input)
    elif input_path.suffix == '.json':
        print(f"📄 Loading JSON batch configuration...")
        configs = batch_gen.load_json_batch(args.input)
    else:
        parser.error(f"Unsupported file format: {input_path.suffix} (use .csv or .json)")

    print(f"✓ Loaded {len(configs)} prompt configurations")

    # Generate batch
    output_dir = Path(args.output_dir)
    summary = batch_gen.generate_batch(configs, args.format, args.mode, output_dir)

    # Print summary
    print(f"\n{'=' * 60}")
    print(f"📊 Batch Generation Complete!")
    print(f"{'=' * 60}")
    print(f"Total: {summary['total']}")
    print(f"✅ Successful: {summary['successful']}")
    print(f"❌ Failed: {summary['failed']}")
    print(f"📁 Output: {summary['output_dir']}")

    # Generate report
    if args.report or summary['failed'] > 0:
        report_file = create_summary_report(summary, output_dir)
        print(f"📋 Report: {report_file}")

    # Exit with error code if any failed
    if summary['failed'] > 0:
        exit(1)
    else:
        print(f"\n✅ All prompts generated successfully!")
        exit(0)


if __name__ == "__main__":
    main()
