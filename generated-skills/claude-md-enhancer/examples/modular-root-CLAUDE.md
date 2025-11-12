# CLAUDE.md

This file provides top-level guidance for Claude Code when working with this full-stack project.

## Overview

Full-stack application with separated backend API and frontend SPA. Uses modular CLAUDE.md architecture with context-specific files for detailed guidance. Medium team (12 developers) in production phase.

## Quick Navigation

- [Backend Guidelines](backend/CLAUDE.md) - API, services, database operations
- [Frontend Guidelines](frontend/CLAUDE.md) - Components, state management, styling
- [Database Operations](database/CLAUDE.md) - Schemas, migrations, query optimization
- [CI/CD Workflows](.github/CLAUDE.md) - Automation, testing, deployments

## Project Structure

```
project-root/
├── backend/
│   ├── src/
│   │   ├── controllers/     # API route handlers
│   │   ├── services/        # Business logic
│   │   ├── models/          # Database models
│   │   ├── middleware/      # Express middleware
│   │   └── utils/           # Shared utilities
│   ├── tests/               # Backend tests
│   └── CLAUDE.md           # Backend-specific guidance
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   ├── hooks/           # Custom hooks
│   │   ├── store/           # State management
│   │   └── styles/          # CSS/styling
│   ├── public/              # Static assets
│   └── CLAUDE.md           # Frontend-specific guidance
├── database/
│   ├── migrations/          # Schema migrations
│   ├── seeds/               # Seed data
│   └── CLAUDE.md           # Database guidance
├── .github/
│   ├── workflows/           # CI/CD workflows
│   └── CLAUDE.md           # CI/CD guidance
├── docker-compose.yml
├── package.json
└── README.md
```

## File Structure

This project uses **modular architecture** with context-specific CLAUDE.md files:

- **backend/** - Express API server
  - See [backend/CLAUDE.md](backend/CLAUDE.md) for API design, error handling, testing
- **frontend/** - React SPA
  - See [frontend/CLAUDE.md](frontend/CLAUDE.md) for component standards, state, styling
- **database/** - PostgreSQL database
  - See [database/CLAUDE.md](database/CLAUDE.md) for migrations, schemas, queries
- **.github/** - CI/CD workflows
  - See [.github/CLAUDE.md](.github/CLAUDE.md) for deployment, automation

## Architecture

**Stack**: React SPA + Express API + PostgreSQL + Redis Cache

**Services**:
- Frontend: React 18 with TypeScript, served via Nginx
- Backend: Node.js 20 with Express 4, TypeScript
- Database: PostgreSQL 15 with Prisma ORM
- Cache: Redis 7 for session and data caching
- Message Queue: RabbitMQ for async processing
- Infrastructure: Docker containers, Kubernetes orchestration

**Flow**:
```
Client (React) → Nginx → Express API → PostgreSQL
                              ↓
                          Redis Cache
                              ↓
                         RabbitMQ Queue
```

## Setup & Installation

```bash
# Install dependencies for entire monorepo
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your credentials

# Start all services with Docker
docker-compose up -d

# Run database migrations
npm run db:migrate

# Seed initial data
npm run db:seed

# Start development servers
npm run dev              # Starts backend and frontend
```

## Core Principles

1. **Test-Driven Development**: Write tests before implementation
2. **Type Safety First**: Use TypeScript strict mode throughout
3. **Component Composition**: Favor small, reusable components
4. **API Design**: RESTful conventions with proper versioning
5. **Error Handling**: Comprehensive error handling from the start
6. **Performance**: Optimize for scale (caching, CDN, lazy loading)

## Tech Stack

- **Frontend**: React 18, TypeScript 5, Tailwind CSS, React Query
- **Backend**: Node.js 20, Express 4, TypeScript, Prisma
- **Database**: PostgreSQL 15, Redis 7
- **Infrastructure**: Docker, Kubernetes, Nginx, GitHub Actions
- **Testing**: Jest, React Testing Library, Supertest, Playwright

## Development Workflow

1. **Feature Development**:
   - Create feature branch: `git checkout -b feature/name`
   - Work in appropriate context (backend/ or frontend/)
   - Follow context-specific CLAUDE.md guidelines
   - Write tests first (TDD)
   - Run local validation: `npm run lint && npm test`

2. **Code Review**:
   - Create PR with detailed description
   - Ensure CI passes (lint, tests, build)
   - Get minimum 2 approvals
   - Address review comments

3. **Deployment**:
   - Merge to `main` triggers staging deployment
   - QA validation on staging
   - Manual promotion to production
   - Monitor metrics and logs

## Quick Reference

```bash
# Development
npm run dev:backend      # Start backend server (port 3000)
npm run dev:frontend     # Start frontend dev server (port 5173)
npm run dev              # Start both servers
npm test                 # Run all tests (backend + frontend)
npm run lint             # Lint all code

# Production
npm run build            # Build frontend and backend
npm run start            # Start production servers

# Database
npm run db:migrate       # Run migrations
npm run db:seed          # Seed data
npm run db:reset         # Reset database (dev only)

# Docker
docker-compose up -d     # Start all services
docker-compose logs -f   # View logs
docker-compose down      # Stop all services
```

## Testing Strategy

- **Unit Tests**: All business logic (80%+ coverage)
- **Integration Tests**: API endpoints and database operations
- **E2E Tests**: Critical user flows with Playwright
- **Performance Tests**: Load testing for API endpoints
- **Security Tests**: OWASP compliance scans

## Important Notes

- **Context-Specific Guidelines**: Always check subdirectory CLAUDE.md files for detailed guidance
- **Modular Architecture**: Each major component has its own CLAUDE.md file
- **Navigation**: Use Quick Navigation section to find relevant guidelines
- **Production Ready**: This is a production-grade setup with enterprise patterns

---

For detailed guidelines, see context-specific CLAUDE.md files in subdirectories.

**Project Type**: Full-Stack Application (Production)
**Team Size**: Medium (12 developers)
**Architecture**: Modular with context-specific CLAUDE.md files
**Lines**: ~150 (Modular root template with native format)
