# GitHub Wiki Content

This directory contains content designed for the GitHub Wiki.

## Files

- **Home.md** - Main landing page for the GitHub Wiki

## How to Use

GitHub Wikis are stored in a separate repository from the main codebase. To publish this content to the wiki:

### Option 1: Manual Copy (Recommended)

1. Navigate to the wiki repository:
   ```bash
   git clone https://github.com/rezashabrang/claude-code-skills-factory.wiki.git
   cd claude-code-skills-factory.wiki
   ```

2. Copy the Home.md content:
   ```bash
   cp ../claude-code-skills-factory/documentation/wiki/Home.md ./Home.md
   ```

3. Commit and push:
   ```bash
   git add Home.md
   git commit -m "docs: Add GitHub Wiki Home page"
   git push origin master
   ```

### Option 2: Direct Edit on GitHub

1. Go to: https://github.com/rezashabrang/claude-code-skills-factory/wiki
2. Click "Edit" on the Home page
3. Copy content from `documentation/wiki/Home.md`
4. Paste and save

## Wiki Structure

The GitHub Wiki should include these pages:

- **Home** (Home.md) - Main landing page
- **Getting-Started** - Quick start guide
- **Skills-Catalog** - List of all production skills
- **Agents-Catalog** - List of all example agents
- **Installation** - Installation instructions
- **Skills-vs-Agents** - When to use which
- **Customization-Guide** - How to adapt skills
- **Architecture-Patterns** - Design best practices
- **YAML-Standards** - Frontmatter requirements
- **GitHub-Automation** - Workflow documentation
- **API-Reference** - Skills API integration

## Content Design

The Home.md page follows these principles:

1. **Hook in first 10 seconds** - Clear value proposition
2. **Scannable hierarchy** - Tables, bullets, headers
3. **Concrete metrics** - "5 minutes" not "fast", "606 KB" not "lots"
4. **Multiple entry points** - For developers, enterprises, content creators, startups
5. **Clear CTAs** - Direct links to getting started
6. **Visual organization** - Emoji icons, tables, sections

## Updating

When updating wiki content:

1. Edit files in `documentation/wiki/`
2. Test locally if possible
3. Copy to wiki repository
4. Verify links work in wiki context

## Notes

- Wiki links use wiki syntax (no .md extension)
- Internal links: `[Page Title](Page-Title)`
- External links: Full URLs
- File paths in code blocks are relative to project root
