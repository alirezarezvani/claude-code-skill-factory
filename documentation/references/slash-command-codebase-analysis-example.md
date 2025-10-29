---
allowed-tools: Bash(find:*), Bash(ls:*), Bash(tree:*), Bash(grep:*), Bash(wc:*), Bash(du:*), Bash(head:*), Bash(tail:*), Bash(cat:*), Bash(touch:*)
description: Generate comprehensive analysis and documentation of entire codebase
---

# Comprehensive Codebase Analysis

## Project Discovery Phase

### Directory Structure
!`find . -type d -not -path "./node_modules/*" -not -path "./.git/*" -not -path "./dist/*" -not -path "./build/*" -not -path "./.next/*" -not -path "./coverage/*" | sort`

### Complete File Tree
!`tree -a -I 'node_modules|.git|dist|build|.next|coverage|*.log' -L 4`

### File Count and Size Analysis
- Total files: !`find . -type f -not -path "./node_modules/*" -not -path "./.git/*" | wc -l`
- Code files: !`find . -name "*.js" -o -name "*.ts" -o -name "*.jsx" -o -name "*.tsx" -o -name "*.py" -o -name "*.java" -o -name "*.php" -o -name "*.rb" -o -name "*.go" -o -name "*.rs" -o -name "*.cpp" -o -name "*.c" | grep -v node_modules | wc -l`
- Project size: !`du -sh . --exclude=node_modules --exclude=.git --exclude=dist --exclude=build`

## Configuration Files Analysis

### Package Management
- Package.json: @package.json
- Package-lock.json exists: !`ls package-lock.json 2>/dev/null || echo "Not found"`
- Yarn.lock exists: !`ls yarn.lock 2>/dev/null || echo "Not found"`
- Requirements.txt: @requirements.txt
- Gemfile: @Gemfile
- Cargo.toml: @Cargo.toml
- Go.mod: @go.mod
- Composer.json: @composer.json

### Build & Dev Tools
- Webpack config: @webpack.config.js
- Vite config: @vite.config.js
- Rollup config: @rollup.config.js
- Babel config: @.babelrc
- ESLint config: @.eslintrc.js
- Prettier config: @.prettierrc
- TypeScript config: @tsconfig.json
- Tailwind config: @tailwind.config.js
- Next.js config: @next.config.js

### Environment & Docker
- .env files: !`find . -name ".env*" -type f`
- Docker files: !`find . -name "Dockerfile*" -o -name "docker-compose*"`
- Kubernetes files: !`find . -name "*.yaml" -o -name "*.yml" | grep -E "(k8s|kubernetes|deployment|service)"`

### CI/CD Configuration
- GitHub Actions: !`find .github -name "*.yml" -o -name "*.yaml" 2>/dev/null || echo "No GitHub Actions"`
- GitLab CI: @.gitlab-ci.yml
- Travis CI: @.travis.yml
- Circle CI: @.circleci/config.yml

## Source Code Analysis

### Main Application Files
- Main entry points: !`find . -name "main.*" -o -name "index.*" -o -name "app.*" -o -name "server.*" | grep -v node_modules | head -10`
- Routes/Controllers: !`find . -path "*/routes/*" -o -path "*/controllers/*" -o -path "*/api/*" | grep -v node_modules | head -20`
- Models/Schemas: !`find . -path "*/models/*" -o -path "*/schemas/*" -o -path "*/entities/*" | grep -v node_modules | head -20`
- Components: !`find . -path "*/components/*" -o -path "*/views/*" -o -path "*/pages/*" | grep -v node_modules | head -20`

### Database & Storage
- Database configs: !`find . -name "*database*" -o -name "*db*" -o -name "*connection*" | grep -v node_modules | head -10`
- Migration files: !`find . -path "*/migrations/*" -o -path "*/migrate/*" | head -10`
- Seed files: !`find . -path "*/seeds/*" -o -path "*/seeders/*" | head -10`

### Testing Files
- Test files: !`find . -name "*test*" -o -name "*spec*" | grep -v node_modules | head -15`
- Test config: @jest.config.js

### API Documentation
- API docs: !`find . -name "*api*" -name "*.md" -o -name "swagger*" -o -name "openapi*" | head -10`

## Key Files Content Analysis

### Root Configuration Files
@README.md
@LICENSE
@.gitignore

### Main Application Entry Points
!`find . -name "index.js" -o -name "index.ts" -o -name "main.js" -o -name "main.ts" -o -name "app.js" -o -name "app.ts" -o -name "server.js" -o -name "server.ts" | grep -v node_modules | head -5 | while read file; do echo "=== $file ==="; head -50 "$file"; echo; done`

## Your Task

Based on all the discovered information above, create a comprehensive analysis that includes:

## 1. Project Overview
- Project type (web app, API, library, etc.)
- Tech stack and frameworks
- Architecture pattern (MVC, microservices, etc.)
- Language(s) and versions

## 2. Detailed Directory Structure Analysis
For each major directory, explain:
- Purpose and role in the application
- Key files and their functions
- How it connects to other parts

## 3. File-by-File Breakdown
Organize by category:
- **Core Application Files**: Main entry points, routing, business logic
- **Configuration Files**: Build tools, environment, deployment
- **Data Layer**: Models, database connections, migrations
- **Frontend/UI**: Components, pages, styles, assets  
- **Testing**: Test files, mocks, fixtures
- **Documentation**: README, API docs, guides
- **DevOps**: CI/CD, Docker, deployment scripts

## 4. API Endpoints Analysis
If applicable, document:
- All discovered endpoints and their methods
- Authentication/authorization patterns
- Request/response formats
- API versioning strategy

## 5. Architecture Deep Dive
Explain:
- Overall application architecture
- Data flow and request lifecycle
- Key design patterns used
- Dependencies between modules

## 6. Environment & Setup Analysis
Document:
- Required environment variables
- Installation and setup process
- Development workflow
- Production deployment strategy

## 7. Technology Stack Breakdown
List and explain:
- Runtime environment
- Frameworks and libraries
- Database technologies
- Build tools and bundlers
- Testing frameworks
- Deployment technologies

## 8. Visual Architecture Diagram
Create a comprehensive diagram showing:
- High-level system architecture
- Component relationships
- Data flow
- External integrations
- File structure hierarchy

Use ASCII art, mermaid syntax, or detailed text representation to show:
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│     Frontend    │────▶│      API        │────▶│    Database     │
│   (React/Vue)   │     │   (Node/Flask)  │     │ (Postgres/Mongo)│
└─────────────────┘     └─────────────────┘     └─────────────────┘

## 9. Key Insights & Recommendations
Provide:
- Code quality assessment
- Potential improvements
- Security considerations
- Performance optimization opportunities
- Maintainability suggestions

Think deeply about the codebase structure and provide comprehensive insights that would be valuable for new developers joining the project or for architectural decision-making.

At the end, write all of the output into a file called "codebase_analysis.md"