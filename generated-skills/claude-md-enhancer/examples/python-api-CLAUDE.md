# CLAUDE.md

This file provides guidance for Claude Code when working with this Python API project.

## Overview

FastAPI-based RESTful API with PostgreSQL database, JWT authentication, and async SQLAlchemy. Small team (6 developers) following TDD practices with 90%+ test coverage requirement.

## Project Structure

```
project-root/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/       # API endpoints
│   │   │   │   ├── auth.py
│   │   │   │   ├── users.py
│   │   │   │   └── products.py
│   │   │   ├── dependencies.py  # Shared dependencies
│   │   │   └── router.py        # API router
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py            # App configuration
│   │   ├── security.py          # Auth utilities
│   │   └── database.py          # DB connection
│   ├── models/
│   │   ├── user.py              # SQLAlchemy models
│   │   └── product.py
│   ├── schemas/
│   │   ├── user.py              # Pydantic schemas
│   │   └── product.py
│   ├── services/
│   │   ├── auth_service.py      # Business logic
│   │   ├── user_service.py
│   │   └── product_service.py
│   ├── utils/
│   │   ├── logging.py           # Logging utilities
│   │   └── validators.py
│   ├── middleware/
│   │   ├── logging.py           # Logging middleware
│   │   └── rate_limit.py        # Rate limiting
│   └── main.py                  # App entry point
├── tests/
│   ├── unit/                    # Unit tests
│   ├── integration/             # Integration tests
│   ├── conftest.py              # Pytest fixtures
│   └── test_main.py
├── alembic/
│   ├── versions/                # Migration files
│   └── env.py                   # Alembic config
├── .env.example
├── alembic.ini
├── pyproject.toml
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

## File Structure

- **app/** - Main application package
  - **api/v1/** - API version 1 endpoints and routing
    - **endpoints/** - Path operation functions
    - **dependencies.py** - Dependency injection (DB sessions, auth)
  - **core/** - Core utilities (config, security, database)
  - **models/** - SQLAlchemy ORM models
  - **schemas/** - Pydantic models for request/response validation
  - **services/** - Business logic layer (separate from HTTP)
  - **utils/** - Helper functions (logging, validation)
  - **middleware/** - FastAPI middleware components
- **tests/** - Test suite with pytest
- **alembic/** - Database migrations

## Architecture

**Layer Pattern**: FastAPI → Services → Models → Database

**Flow**:
```
HTTP Request → Router → Dependency Injection → Endpoint → Service → Model → Database
                 ↓
            Response (Pydantic schema)
```

**Components**:
- **Endpoints**: HTTP layer, request/response handling with Pydantic
- **Services**: Business logic, reusable across endpoints
- **Models**: Data access layer with async SQLAlchemy 2.0
- **Schemas**: Request/response validation with Pydantic
- **Dependencies**: Shared dependencies (DB session, current user)

## Setup & Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with:
# - DATABASE_URL (PostgreSQL connection string)
# - SECRET_KEY (for JWT token signing)
# - ENVIRONMENT (development/staging/production)

# Start PostgreSQL (using Docker)
docker-compose up -d postgres

# Run database migrations
alembic upgrade head

# Seed database (if needed)
python -m app.scripts.seed

# Start development server
uvicorn app.main:app --reload

# Server runs at http://localhost:8000
# API docs at http://localhost:8000/docs (Swagger UI)
# Alternative docs at http://localhost:8000/redoc (ReDoc)
```

## Core Principles

1. **Type Hints First**: Use type hints for all function signatures (Python 3.10+)
2. **Test-Driven Development**: Write tests before implementation
3. **API Design**: Follow RESTful conventions and OpenAPI standards
4. **Error Handling**: Comprehensive error handling with proper logging
5. **Code Quality**: Black formatting, Ruff linting, 90%+ test coverage

## Tech Stack

- **Framework**: FastAPI 0.104+
- **Database**: PostgreSQL 15 with async SQLAlchemy 2.0
- **Authentication**: JWT with python-jose
- **Validation**: Pydantic v2
- **Testing**: Pytest, Pytest-asyncio, HTTPX
- **Deployment**: Docker, Uvicorn, Gunicorn
- **Logging**: Structlog (JSON format)
- **Code Quality**: Black, Ruff, MyPy

## Development Workflow

### Development Process

1. Create feature branch from `main`: `git checkout -b feature/name`
2. Write tests first (TDD with pytest)
3. Implement feature with type hints
4. Run formatter, linter, and tests locally
5. Create pull request with description
6. Code review (minimum 1 approval required)
7. Merge to main (auto-deploy to staging)

### Code Style

- Use Black for formatting (line length: 100)
- Use Ruff for linting (replaces flake8, isort, etc.)
- Type hints on all functions and methods
- Docstrings for all public functions (Google style)
- Example:
  ```python
  def create_user(db: Session, user_in: UserCreate) -> User:
      """Create a new user in the database.

      Args:
          db: Database session
          user_in: User creation data

      Returns:
          Created user object

      Raises:
          ValueError: If email already exists
      """
      # Implementation...
  ```

## API Design Guidelines

### FastAPI Path Operations

- Use FastAPI path operations (`@app.get`, `@app.post`, etc.)
- Version APIs: `/api/v1/users`, `/api/v2/users`
- Use Pydantic models for request/response validation
- Implement proper HTTP status codes:
  - `200 OK` - Successful GET/PUT/PATCH
  - `201 Created` - Successful POST
  - `204 No Content` - Successful DELETE
  - `400 Bad Request` - Validation error
  - `401 Unauthorized` - Authentication required
  - `403 Forbidden` - Insufficient permissions
  - `404 Not Found` - Resource not found
  - `422 Unprocessable Entity` - Pydantic validation error
  - `500 Internal Server Error` - Server error

### Documentation

- Document with OpenAPI (auto-generated by FastAPI)
- Access Swagger UI at `/docs`
- Access ReDoc at `/redoc`
- Add descriptions to path operations:
  ```python
  @router.get("/users/{user_id}", response_model=UserResponse)
  async def get_user(user_id: int, db: Session = Depends(get_db)):
      """Retrieve a single user by ID."""
      # Implementation...
  ```

## Database Guidelines

### Migrations with Alembic

- Use Alembic for migrations
- **Never edit existing migrations** - create new ones
- Auto-generate migrations: `alembic revision --autogenerate -m "description"`
- Review generated migrations before applying
- Test migrations on copy of production data
- Name migrations descriptively: `add_user_email_index`

### SQLAlchemy 2.0 Async Style

- Use async SQLAlchemy 2.0 style
- Example:
  ```python
  from sqlalchemy import select
  from sqlalchemy.ext.asyncio import AsyncSession

  async def get_user(db: AsyncSession, user_id: int) -> User | None:
      result = await db.execute(select(User).where(User.id == user_id))
      return result.scalar_one_or_none()
  ```

### Query Optimization

- Implement proper indexes for frequently queried columns
- Avoid N+1 queries - use `selectinload` or `joinedload`
- Use database transactions for multi-step operations
- Paginate large result sets (max 100 items per page)

## Error Handling

### FastAPI Exception Handlers

- Use FastAPI exception handlers
- Create custom exceptions:
  ```python
  class UserNotFoundException(HTTPException):
      def __init__(self, user_id: int):
          super().__init__(
              status_code=404,
              detail=f"User {user_id} not found"
          )
  ```

### Error Response Format

Return consistent error format:

```python
{
  "detail": {
    "code": "VALIDATION_ERROR",
    "message": "User-friendly message",
    "errors": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}
```

### Logging

- Log errors with structlog (JSON format)
- Include context (request ID, user ID, timestamp)
- Log levels: ERROR, WARNING, INFO, DEBUG
- Never log sensitive data (passwords, tokens)
- Never expose stack traces in production

## Testing Requirements

### Pytest Best Practices

- Use pytest for all tests
- Use pytest fixtures for test setup
- Mock external dependencies (httpx, boto3, etc.)
- Aim for 90%+ code coverage
- Test both success and error paths

### Example Test

```python
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_user(client: AsyncClient):
    """Test user creation endpoint."""
    response = await client.post(
        "/api/v1/users",
        json={"email": "test@example.com", "name": "Test User"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

@pytest.mark.asyncio
async def test_create_user_duplicate_email(client: AsyncClient):
    """Test user creation with duplicate email."""
    # First creation
    await client.post("/api/v1/users", json={"email": "test@example.com"})

    # Duplicate should fail
    response = await client.post("/api/v1/users", json={"email": "test@example.com"})
    assert response.status_code == 400
```

### Test Categories

```bash
# Run all tests
pytest

# Run specific test categories
pytest tests/unit/                # Unit tests only
pytest tests/integration/         # Integration tests only
pytest -m slow                    # Slow tests (marked with @pytest.mark.slow)

# Run with coverage
pytest --cov=app --cov-report=html
```

## Security Practices

### Input Validation

- Validate all input with Pydantic models
- Use Pydantic validators for complex validation
- Sanitize user input to prevent XSS

### Database Security

- Use parameterized queries (SQLAlchemy handles this)
- Prevents SQL injection
- Never concatenate user input into queries

### Authentication & Authorization

- Hash passwords with passlib + bcrypt
- Use JWT for stateless authentication
- Implement refresh token rotation
- Use environment variables for secrets
- Example:
  ```python
  from passlib.context import CryptContext

  pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
  hashed_password = pwd_context.hash(plain_password)
  ```

### Rate Limiting

- Implement rate limiting with slowapi
- Example: 100 requests per 15 minutes per IP
- Protect against brute force attacks

### CORS

- Enable CORS properly with CORSMiddleware
- Whitelist allowed origins in production
- Don't use wildcard (`*`) in production

## Performance Optimization

### Async/Await

- Use async/await for all I/O operations
- Use AsyncSession for database operations
- Use httpx.AsyncClient for external HTTP calls

### Caching

- Implement caching for frequently accessed data
- Use Redis for caching (with aioredis)
- Cache expensive computations
- Set appropriate TTL (time-to-live)

### Database Connection Pooling

- Configure SQLAlchemy connection pool
- Set appropriate pool size and overflow

## Common Commands

```bash
# Development
uvicorn app.main:app --reload     # Start dev server with hot reload
pytest                            # Run all tests
pytest --cov=app                  # Run tests with coverage
black .                           # Format code
ruff check .                      # Lint code
mypy app/                         # Type checking

# Database
alembic upgrade head              # Run all pending migrations
alembic downgrade -1              # Rollback last migration
alembic revision --autogenerate -m "description"  # Create migration
alembic current                   # Show current migration
alembic history                   # Show migration history

# Production
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker

# Docker
docker-compose up -d              # Start all services
docker-compose logs -f app        # View application logs
docker-compose down               # Stop all services
```

## API Documentation

After starting the server, access API documentation at:

- **Swagger UI**: http://localhost:8000/docs (interactive)
- **ReDoc**: http://localhost:8000/redoc (readable)
- **OpenAPI JSON**: http://localhost:8000/openapi.json (raw schema)

## Environment Variables

Required environment variables (see `.env.example`):

```bash
# Application
ENVIRONMENT=development
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname

# Authentication
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
```

---

**Project Type**: Python API (FastAPI)
**Team Size**: Small (6 developers)
**Lines**: ~225 (Python API template with native format)
