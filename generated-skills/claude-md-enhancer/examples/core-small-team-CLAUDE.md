# CLAUDE.md

This file provides guidance for Claude Code when working with this project.

## Overview

Full-stack web application built with React, Node.js, and PostgreSQL. Small team (5 developers) following TDD and code review practices for MVP development.

## Project Structure

```
project-root/
├── client/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   ├── hooks/           # Custom hooks
│   │   ├── services/        # API client services
│   │   └── utils/           # Utility functions
│   ├── public/              # Static assets
│   └── package.json
├── server/
│   ├── src/
│   │   ├── controllers/     # Route handlers
│   │   ├── services/        # Business logic
│   │   ├── models/          # Database models
│   │   ├── middleware/      # Express middleware
│   │   └── routes/          # API routes
│   ├── tests/               # Server tests
│   └── package.json
├── database/
│   ├── migrations/          # Database migrations
│   └── seeds/               # Seed data
├── docker-compose.yml
└── README.md
```

## File Structure

- **client/** - React frontend application
  - **src/components/** - Reusable UI components
  - **src/pages/** - Route-level page components
  - **src/services/** - API client functions
- **server/** - Node.js backend API
  - **src/controllers/** - Request handlers and route logic
  - **src/services/** - Business logic layer
  - **src/models/** - Database models and schemas
  - **src/middleware/** - Express middleware (auth, validation, logging)
- **database/** - Database migrations and seed data

## Architecture

**Stack**: React SPA + Express API + PostgreSQL

**Flow**: Client → Express API → PostgreSQL
- Frontend: React SPA with client-side routing
- Backend: RESTful API with Express
- Database: PostgreSQL with migration-based schema management
- Communication: JSON over HTTP/HTTPS

## Setup & Installation

```bash
# Install dependencies for both client and server
npm install
cd client && npm install
cd ../server && npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your database credentials and API keys

# Start PostgreSQL (using Docker)
docker-compose up -d postgres

# Run database migrations
cd server && npm run migrate

# Seed database with initial data
npm run seed

# Start development servers
npm run dev              # Starts both client and server
```

## Core Principles

1. **Test-Driven Development**: Write tests before implementation
2. **Code Quality**: Maintain high standards with clean, readable code
3. **Documentation**: Keep docs in sync with code changes
4. **Collaboration**: Clear communication and code reviews
5. **Performance**: Consider performance implications early

## Tech Stack

- **Frontend**: React 18, TypeScript 5, Tailwind CSS
- **Backend**: Node.js 20, Express 4, TypeScript
- **Database**: PostgreSQL 15, Prisma ORM
- **Testing**: Jest, React Testing Library, Supertest
- **Build**: Vite, Docker, GitHub Actions

## Development Workflow

### Development Process

1. Create feature branch from `main`: `git checkout -b feature/name`
2. Write tests first (TDD approach)
3. Implement feature with proper error handling
4. Run linter and tests locally: `npm run lint && npm test`
5. Create pull request with description
6. Code review (minimum 1 approval required)
7. Merge to main (auto-deploy to staging)

### Testing Requirements

- Unit tests for all business logic
- Integration tests for API endpoints
- E2E tests for critical user flows
- Minimum 80% code coverage
- All tests must pass before merge

## Error Handling

- Use try-catch blocks for async operations
- Log errors with context (user ID, request ID, timestamp)
- Return meaningful error messages to clients
- Never expose stack traces in production
- Implement global error handling middleware

## Code Review Checklist

Before requesting review, ensure:

- [ ] Tests written and passing (80%+ coverage)
- [ ] No console.log or debugger statements
- [ ] Error handling implemented properly
- [ ] Documentation updated (README, API docs)
- [ ] No hardcoded values (use environment variables)
- [ ] TypeScript types defined (no `any` types)
- [ ] Performance considerations addressed
- [ ] Security best practices followed

## Common Commands

```bash
# Development
npm run dev              # Start both client and server
npm run dev:client       # Start client only
npm run dev:server       # Start server only
npm test                 # Run all tests
npm run test:watch       # Run tests in watch mode
npm run lint             # Run ESLint
npm run format           # Format code with Prettier

# Production
npm run build            # Build client and server
npm run start            # Start production servers

# Database
npm run migrate          # Run database migrations
npm run migrate:rollback # Rollback last migration
npm run seed             # Seed database with test data
npm run db:reset         # Reset database (dev only)

# Docker
docker-compose up        # Start all services
docker-compose down      # Stop all services
docker-compose logs -f   # View logs
```

## API Documentation

API endpoints are documented using Swagger/OpenAPI. After starting the server, visit:

```
http://localhost:3000/api-docs
```

---

**Project Type**: Web Application (MVP)
**Team Size**: Small (5 developers)
**Lines**: ~175 (Core template with native format)
