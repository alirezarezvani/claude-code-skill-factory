# Backend Development Guidelines

This file provides guidance for backend development in this project.

## Overview

Express API backend with TypeScript, PostgreSQL database, and Redis caching. RESTful API design with comprehensive error handling, testing, and security practices.

## Project Structure

```
backend/
├── src/
│   ├── controllers/         # Route handlers
│   │   ├── auth.controller.ts
│   │   ├── user.controller.ts
│   │   └── product.controller.ts
│   ├── services/            # Business logic
│   │   ├── auth.service.ts
│   │   ├── user.service.ts
│   │   └── product.service.ts
│   ├── models/              # Database models
│   │   ├── User.ts
│   │   └── Product.ts
│   ├── middleware/          # Express middleware
│   │   ├── auth.middleware.ts
│   │   ├── validation.middleware.ts
│   │   └── error.middleware.ts
│   ├── routes/              # Route definitions
│   │   ├── auth.routes.ts
│   │   ├── user.routes.ts
│   │   └── product.routes.ts
│   ├── utils/               # Utilities
│   │   ├── logger.ts
│   │   ├── validators.ts
│   │   └── crypto.ts
│   ├── config/              # Configuration
│   │   ├── database.ts
│   │   └── redis.ts
│   └── index.ts             # App entry point
├── tests/
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests
│   └── fixtures/            # Test data
├── prisma/
│   ├── schema.prisma        # Database schema
│   └── migrations/          # Migration files
├── .env.example
├── package.json
└── tsconfig.json
```

## File Structure

- **controllers/** - Handle HTTP requests, validate input, call services
- **services/** - Business logic layer, independent of HTTP
- **models/** - Database models and Prisma client usage
- **middleware/** - Express middleware (auth, validation, logging, errors)
- **routes/** - Route definitions mapping URLs to controllers
- **utils/** - Shared utility functions (logging, validation, crypto)
- **config/** - Configuration files for database, Redis, etc.
- **tests/** - Unit and integration tests

## Architecture

**Layer Pattern**: Controllers → Services → Models → Database

**Flow**:
```
HTTP Request → Route → Middleware → Controller → Service → Model → Database
                ↓
            Response
```

**Components**:
- **Controllers**: HTTP layer, request/response handling
- **Services**: Business logic, reusable across controllers
- **Models**: Data access layer with Prisma ORM
- **Middleware**: Cross-cutting concerns (auth, logging, validation)

## Setup & Installation

```bash
# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with:
# - DATABASE_URL (PostgreSQL connection string)
# - REDIS_URL (Redis connection string)
# - JWT_SECRET (secret for token signing)
# - PORT (default 3000)

# Start PostgreSQL and Redis (using Docker)
docker-compose up -d postgres redis

# Run database migrations
npx prisma migrate dev

# Generate Prisma client
npx prisma generate

# Seed database
npm run seed

# Start development server
npm run dev
```

## API Design

### RESTful Conventions

- Use RESTful conventions for API endpoints
- Implement proper HTTP status codes:
  - `200 OK` - Successful GET/PUT/PATCH
  - `201 Created` - Successful POST
  - `204 No Content` - Successful DELETE
  - `400 Bad Request` - Validation error
  - `401 Unauthorized` - Authentication required
  - `403 Forbidden` - Insufficient permissions
  - `404 Not Found` - Resource not found
  - `500 Internal Server Error` - Server error

### Versioning

- Version APIs when breaking changes are needed
- Format: `/api/v1/`, `/api/v2/`
- Example: `/api/v1/users`, `/api/v2/users`

### Documentation

- Document all endpoints with OpenAPI/Swagger
- Access docs at `/api-docs` when server running
- Include request/response examples
- Document authentication requirements

### Naming Conventions

- Use camelCase for JSON keys
- Use snake_case for database columns
- Use kebab-case for URL paths

## Database Operations

### Migrations

- Use migrations for all schema changes
- **Never edit existing migrations** - create new ones
- Test migrations on copy of production data
- Include both up and down migrations
- Name migrations descriptively: `20250112_add_user_email_index`

### Query Optimization

- Implement proper indexes for frequently queried columns
- Avoid N+1 queries - use joins or batch loading with Prisma `include`
- Use `EXPLAIN ANALYZE` to analyze slow queries
- Paginate large result sets (max 100 items per page)

### Transactions

- Use transactions for multi-step operations
- Example:
  ```typescript
  await prisma.$transaction(async (tx) => {
    await tx.user.update({ ... });
    await tx.account.create({ ... });
  });
  ```

## Error Handling

### Global Error Middleware

- Implement global error handling middleware
- Catch all errors in one place
- Log errors with context (request ID, user ID, timestamp)

### Error Response Format

Return consistent error response format:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User-friendly message",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}
```

### Error Classes

- Use custom error classes for different error types
- Examples: `ValidationError`, `AuthenticationError`, `NotFoundError`
- Never expose stack traces to clients in production
- Log full stack traces server-side

## Testing Requirements

### Unit Tests

- Write unit tests for business logic (services, utils)
- Mock external dependencies (database, APIs, Redis)
- Test edge cases and error conditions
- Aim for 80%+ code coverage

### Integration Tests

- Write integration tests for API endpoints
- Test full request/response cycle
- Use test database (separate from dev/prod)
- Reset database state between tests

### Best Practices

- Use test databases, never production
- Use factories/fixtures for test data
- Test authentication and authorization
- Test error scenarios

```bash
# Run tests
npm test                  # All tests
npm run test:unit         # Unit tests only
npm run test:integration  # Integration tests only
npm run test:coverage     # With coverage report
```

## Security Practices

### Input Validation

- Validate all input data with validation middleware
- Use schema validation (Joi, Zod, class-validator)
- Sanitize user input to prevent XSS

### Database Security

- Use parameterized queries (Prisma handles this)
- Prevents SQL injection
- Never concatenate user input into queries

### Authentication & Authorization

- Hash passwords with bcrypt (minimum 10 rounds)
- Use JWT for stateless authentication
- Implement refresh token rotation
- Use environment variables for secrets

### Rate Limiting

- Implement rate limiting on public endpoints
- Example: 100 requests per 15 minutes per IP
- Protect against brute force attacks

### CORS

- Implement proper CORS policies
- Whitelist allowed origins
- Don't use wildcard (`*`) in production

## Performance Optimization

### Caching

- Implement caching for frequently accessed data
- Use Redis for session storage and data caching
- Cache expensive computations
- Set appropriate TTL (time-to-live)

### Database

- Use database connection pooling (Prisma handles this)
- Optimize queries with proper indexes
- Monitor slow queries
- Use read replicas for heavy read workloads

### Async Operations

- Use async/await for I/O operations
- Never block the event loop
- Use worker threads for CPU-intensive tasks
- Queue background jobs with RabbitMQ/Bull

## Logging

- Use structured logging (Winston, Pino)
- Log levels: ERROR, WARN, INFO, DEBUG
- Include context: request ID, user ID, timestamp
- Never log sensitive data (passwords, tokens)
- Rotate log files in production

## Common Commands

```bash
# Development
npm run dev              # Start dev server with hot reload
npm test                 # Run all tests
npm run test:watch       # Run tests in watch mode
npm run lint             # Run ESLint
npm run format           # Format code with Prettier

# Database
npm run migrate          # Run migrations
npm run migrate:rollback # Rollback last migration
npm run migrate:reset    # Reset database (dev only)
npm run seed             # Seed database with test data
npx prisma studio        # Open Prisma Studio (DB GUI)

# Production
npm run build            # Build TypeScript
npm start                # Start production server

# Debugging
npm run dev:debug        # Start with debugger
npm run logs             # View application logs
```

## API Documentation

After starting the server, access API documentation at:

```
http://localhost:3000/api-docs
```

Swagger UI provides interactive API documentation with:
- All endpoints listed
- Request/response schemas
- Try-it-out functionality
- Authentication examples

---

**Context**: Backend (Node.js/Express/TypeScript/PostgreSQL)
**Lines**: ~200 (Backend-specific template with native format)
