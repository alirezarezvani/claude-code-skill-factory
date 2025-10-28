# Contributing to Claude Code Skills & Agents Factory

Thank you for your interest in contributing! This repository provides templates and examples for generating Claude Skills and Claude Code Agents.

---

## 🎯 Types of Contributions

### 1. New Example Skills
Add new skill examples to `claude-skills-examples/` (reference implementations only, not production skills).

### 2. Generated Skills
Share production-ready skills you've created using the factory templates.

### 3. Documentation Improvements
- Clarify existing documentation
- Add troubleshooting guides
- Improve setup instructions
- Translate documentation

### 4. Template Enhancements
- Improve SKILLS_FACTORY_PROMPT.md
- Enhance AGENTS_FACTORY_PROMPT.md
- Add PROMPTS_FACTORY_PROMPT.md examples

### 5. Bug Reports
Report issues with templates, examples, or documentation.

---

## 📋 Contribution Guidelines

### Before Contributing

1. **Search existing issues** to avoid duplicates
2. **Check if the contribution fits** the repository's scope
3. **Read the documentation** (README, CLAUDE.md, GISTS.md)

### Code Standards

**Python**:
- Type hints for all functions
- Docstrings (Google style)
- PEP 8 compliance
- Error handling for edge cases
- >80% test coverage

**YAML Frontmatter**:
- Use kebab-case for skill names
- Clear, concise descriptions
- No reserved words ("claude" prohibited in skill names)

**Markdown**:
- Clear headings (H1, H2, H3)
- Code blocks with syntax highlighting
- Examples for complex concepts
- Links to related documentation

### Documentation Standards

- **User-facing**: Clear, actionable, beginner-friendly
- **Technical**: Comprehensive, with code examples
- **Bilingual** (if healthcare): German + English
- **Reading level**: Appropriate for audience

---

## 🚀 How to Contribute

### Contributing Skills or Agents

1. **Fork the repository**
2. **Create your skill/agent** using factory templates
3. **Test thoroughly** - ensure it works as documented
4. **Document completely**:
   - SKILL.md with proper YAML frontmatter
   - HOW_TO_USE.md with clear examples
   - Sample input/output (if applicable)
   - Python implementation (if needed)
5. **Submit pull request** with:
   - Clear title describing the skill
   - Description of what it does
   - Usage examples
   - Testing evidence

### Contributing Documentation

1. **Fork the repository**
2. **Make improvements**:
   - Fix typos or unclear sections
   - Add missing information
   - Improve examples
   - Translate content
3. **Test links** and code examples
4. **Submit pull request** with:
   - Clear description of changes
   - Why the change improves documentation

### Contributing Bug Fixes

1. **Create issue** describing the bug
2. **Fork and fix** in a feature branch
3. **Test the fix** thoroughly
4. **Submit pull request** with:
   - Reference to issue: "Fixes #123"
   - Description of fix
   - Test evidence

---

## 🏗️ Development Process

### Setting Up Development Environment

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/claude-code-skills-factory.git
cd claude-code-skills-factory

# Create feature branch
git checkout -b feature/my-contribution

# Make changes
# ... edit files ...

# Test (if applicable)
pytest tests/ -v  # If Python code
yamllint .github/workflows/*.yml  # If workflows

# Commit with conventional commits
git commit -m "feat(skills): Add new financial forecasting skill"

# Push
git push origin feature/my-contribution
```

### Commit Message Format

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `chore`: Maintenance
- `refactor`: Code restructuring
- `test`: Adding tests

**Examples**:
```
feat(skills): Add AWS cost optimization skill
docs(readme): Add healthcare skills section
fix(workflows): Correct plan-validator task count
chore(gitignore): Add test-workspace exclusion
```

---

## ✅ Pull Request Checklist

Before submitting:

- [ ] Code follows style guidelines
- [ ] Documentation is complete and clear
- [ ] YAML frontmatter is valid (if skill/agent)
- [ ] Examples work as documented
- [ ] Tests pass (if applicable)
- [ ] No secrets or API keys in code
- [ ] Commit messages follow conventional format
- [ ] PR description is clear and complete

---

## 🔒 Security Guidelines

**NEVER commit**:
- API keys or tokens
- Personal credentials
- .env files with secrets
- Private patient data (healthcare skills)
- Proprietary information

**Always**:
- Use .env.example templates
- Document required environment variables
- Use gitignore for sensitive files
- Review commits before pushing

---

## 🏥 Healthcare Skills - Special Requirements

**If contributing healthcare-related skills**:

- [ ] **Compliance**: HIPAA/GDPR/DSGVO documentation included
- [ ] **Evidence-based**: Reference clinical sources
- [ ] **Safety**: Crisis detection for mental health apps
- [ ] **Reading level**: 8th-10th grade for patient content
- [ ] **Multilingual**: German + English (if applicable)
- [ ] **Disclaimers**: Clear scope limitations
- [ ] **Ethics**: Professional boundaries maintained

**Medical accuracy**: Have healthcare professionals review before contributing.

---

## 🎓 Learning Resources

**Claude Skills**:
- [Official Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- [Skills Marketplace](https://github.com/anthropics/skills)
- [Engineering Blog](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

**Claude Code Agents**:
- [Agent Documentation](https://docs.claude.com/en/docs/claude-code/agents)

**This Repository**:
- README.md - Overview and quick start
- CLAUDE.md - Repository guidance
- GISTS.md - SEO/AEO strategy
- .github/GITHUB_WORKFLOWS_GUIDE.md - Automation system

---

## 🤝 Community

**Discussion**:
- Open issues for questions
- Use `question` label for help
- Share your use cases and success stories

**Support**:
- Read documentation first
- Search existing issues
- Provide complete information when reporting bugs

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License (same as this project).

---

## ✨ Recognition

Contributors will be:
- Listed in release notes
- Mentioned in documentation (if significant contribution)
- Credited in skill files (if skill contributor)

---

## 🙏 Thank You!

Your contributions help the Claude AI community build better skills, agents, and automation systems.

**Questions?** Open an issue with the `question` label.

---

**Last Updated**: October 28, 2025
**Version**: 1.0.0
