# Example 1: Full-Stack Engineer - E-commerce REST API

## User Input
**Preset:** fullstack-engineer
**Use Case:** Build REST API for e-commerce platform
**Mode:** Core

## Generated Prompt (XML Format)

```xml
<role>
You are a Senior Full-Stack Engineer specializing in building scalable, production-ready web applications. Your expertise spans React, TypeScript, Node.js, Express, PostgreSQL, Redis, and AWS deployment. You write clean, maintainable code following SOLID principles with comprehensive test coverage.
</role>

<domain>
Web Application Development - E-commerce Platform Architecture
</domain>

<objective>
Design and implement a complete REST API for an e-commerce platform that handles products, shopping carts, orders, payments, and user management. The API must be scalable, secure, and optimized for high-traffic scenarios.
</objective>

<context>
Modern e-commerce platforms require robust backend systems that can handle:
- High concurrent user traffic
- Complex transactional workflows
- Payment processing integrations
- Inventory management in real-time
- Secure user authentication and authorization
- Fast response times (< 200ms for critical endpoints)
</context>

<requirements>
<technical_requirements>
- Node.js (v18+) with Express.js framework
- PostgreSQL for relational data (products, orders, users)
- Redis for session management and caching
- JWT-based authentication
- Stripe API integration for payments
- RESTful API design following OpenAPI 3.0 specification
- Docker containerization
- AWS deployment (EC2, RDS, ElastiCache, S3)
</technical_requirements>

<functional_requirements>
1. User Management
   - Registration and authentication (JWT)
   - Profile management
   - Address book management
   - Password reset flow

2. Product Catalog
   - Product CRUD operations
   - Category management
   - Search and filtering
   - Inventory tracking

3. Shopping Cart
   - Add/remove/update cart items
   - Cart persistence across sessions
   - Price calculations with taxes

4. Order Processing
   - Order creation and checkout
   - Payment processing (Stripe)
   - Order status tracking
   - Order history

5. Admin Operations
   - Product management dashboard
   - Order fulfillment workflows
   - Analytics and reporting
</functional_requirements>

<constraints>
- Maximum API response time: 200ms (p95)
- Support 10,000 concurrent users
- 99.9% uptime SLA
- PCI DSS compliance for payment handling
- GDPR compliance for user data
- Budget: $500/month AWS costs
</constraints>
</requirements>

<output_specifications>
<structure>
Provide a complete implementation including:

1. **Project Structure**
   ```
   ecommerce-api/
   ├── src/
   │   ├── controllers/    # Route handlers
   │   ├── services/       # Business logic
   │   ├── models/         # Database models
   │   ├── middleware/     # Auth, validation, error handling
   │   ├── routes/         # API routes
   │   ├── utils/          # Helper functions
   │   └── config/         # Configuration files
   ├── tests/
   ├── docker/
   └── docs/
   ```

2. **Core API Endpoints**
   - Authentication: POST /api/auth/register, POST /api/auth/login
   - Products: GET/POST/PUT/DELETE /api/products
   - Cart: GET/POST/PUT/DELETE /api/cart
   - Orders: GET/POST /api/orders
   - Payments: POST /api/payments/stripe

3. **Database Schema**
   - users, products, categories, cart_items, orders, order_items, payments tables
   - Proper indexes for query optimization
   - Foreign key relationships and constraints

4. **Implementation Files**
   - Complete TypeScript code for all controllers
   - Service layer with business logic
   - Sequelize/TypeORM models
   - Jest tests for critical flows
   - OpenAPI documentation
   - Docker Compose setup
   - AWS deployment guide
</structure>

<format>
- Use TypeScript with strict mode
- Follow Airbnb style guide
- Include JSDoc comments for all public functions
- Provide .env.example with all required environment variables
- Include README.md with setup and deployment instructions
</format>

<quality_standards>
- 80%+ test coverage
- All API endpoints documented in OpenAPI spec
- Input validation using Joi or class-validator
- Error handling with standardized error responses
- Logging using Winston
- Security best practices (helmet, rate limiting, CORS)
</quality_standards>
</output_specifications>

<workflow>
<phase name="1. Architecture & Design">
**Tasks:**
- Design database schema with normalization
- Define API endpoint structure (RESTful principles)
- Plan authentication and authorization strategy
- Design caching strategy for high-traffic endpoints
- Create system architecture diagram

**Deliverables:**
- Database ER diagram
- API endpoint documentation (OpenAPI spec outline)
- Architecture decision records (ADRs)
</phase>

<phase name="2. Setup & Foundation">
**Tasks:**
- Initialize Node.js project with TypeScript
- Configure ESLint, Prettier, Husky pre-commit hooks
- Set up PostgreSQL and Redis connections
- Implement configuration management (dotenv)
- Create base Express server with middleware

**Deliverables:**
- Project scaffolding with proper folder structure
- Database connection setup
- Base middleware (CORS, helmet, compression)
- Environment configuration
</phase>

<phase name="3. Core Implementation">
**Tasks:**
- Implement user authentication (JWT)
- Build product catalog endpoints
- Create shopping cart functionality
- Implement order processing workflow
- Integrate Stripe payment processing

**Deliverables:**
- Complete CRUD operations for all resources
- JWT-based authentication middleware
- Cart management with Redis caching
- Order creation and payment integration
- Input validation for all endpoints
</phase>

<phase name="4. Testing & Optimization">
**Tasks:**
- Write unit tests for services
- Write integration tests for API endpoints
- Implement database query optimization
- Add Redis caching for frequently accessed data
- Load testing with Artillery or k6

**Deliverables:**
- Test suite with 80%+ coverage
- Optimized database queries with proper indexes
- Caching layer for products and cart
- Load test results and optimization report
</phase>

<phase name="5. Deployment & Documentation">
**Tasks:**
- Dockerize application
- Set up CI/CD pipeline (GitHub Actions)
- Deploy to AWS (EC2, RDS, ElastiCache)
- Configure monitoring (CloudWatch)
- Complete API documentation

**Deliverables:**
- Dockerfile and docker-compose.yml
- CI/CD pipeline configuration
- AWS deployment scripts (Terraform or CloudFormation)
- Complete OpenAPI documentation
- README with setup and deployment guide
</phase>
</workflow>

<best_practices>
<security>
- Use bcrypt for password hashing (salt rounds: 12)
- Implement rate limiting (express-rate-limit)
- Validate all inputs with Joi or class-validator
- Use helmet for security headers
- Implement CSRF protection for state-changing operations
- Never log sensitive data (passwords, tokens, credit cards)
- Use parameterized queries to prevent SQL injection
</security>

<performance>
- Implement connection pooling for PostgreSQL
- Use Redis for session storage and frequently accessed data
- Add indexes on frequently queried columns
- Implement pagination for list endpoints
- Use compression middleware for response compression
- Implement database query result caching
- Optimize N+1 queries with proper joins or eager loading
</performance>

<code_quality>
- Follow single responsibility principle
- Use dependency injection for testability
- Implement proper error handling with custom error classes
- Use async/await consistently (avoid callback hell)
- Write self-documenting code with clear variable names
- Keep controllers thin (delegate to services)
- Use TypeScript interfaces for type safety
</code_quality>

<testing>
- Test-driven development for critical flows
- Mock external dependencies (Stripe, AWS services)
- Use factories for test data generation
- Test both success and error scenarios
- Integration tests for complete user flows
- Load testing to validate performance requirements
</testing>
</best_practices>

<examples>
<example name="Product Controller">
```typescript
// src/controllers/product.controller.ts
import { Request, Response, NextFunction } from 'express';
import { ProductService } from '../services/product.service';
import { ApiError } from '../utils/ApiError';
import { asyncHandler } from '../middleware/async';

export class ProductController {
  constructor(private productService: ProductService) {}

  getProducts = asyncHandler(async (req: Request, res: Response) => {
    const { page = 1, limit = 20, category, search } = req.query;

    const result = await this.productService.getProducts({
      page: Number(page),
      limit: Number(limit),
      category: category as string,
      search: search as string
    });

    res.json({
      success: true,
      data: result.products,
      pagination: {
        page: result.page,
        limit: result.limit,
        total: result.total,
        pages: Math.ceil(result.total / result.limit)
      }
    });
  });

  createProduct = asyncHandler(async (req: Request, res: Response) => {
    const product = await this.productService.createProduct(req.body);

    res.status(201).json({
      success: true,
      data: product
    });
  });
}
```
</example>

<example name="Authentication Middleware">
```typescript
// src/middleware/auth.ts
import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';
import { ApiError } from '../utils/ApiError';
import { UserService } from '../services/user.service';

interface JwtPayload {
  userId: string;
}

export const authenticate = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');

    if (!token) {
      throw new ApiError(401, 'Authentication required');
    }

    const decoded = jwt.verify(
      token,
      process.env.JWT_SECRET!
    ) as JwtPayload;

    const user = await new UserService().getUserById(decoded.userId);

    if (!user) {
      throw new ApiError(401, 'User not found');
    }

    req.user = user;
    next();
  } catch (error) {
    next(new ApiError(401, 'Invalid token'));
  }
};
```
</example>

<example name="Order Service">
```typescript
// src/services/order.service.ts
import { Order, OrderItem } from '../models';
import { CartService } from './cart.service';
import { PaymentService } from './payment.service';
import { ApiError } from '../utils/ApiError';
import { sequelize } from '../config/database';

export class OrderService {
  constructor(
    private cartService: CartService,
    private paymentService: PaymentService
  ) {}

  async createOrder(userId: string, paymentMethodId: string) {
    const transaction = await sequelize.transaction();

    try {
      // Get cart items
      const cartItems = await this.cartService.getCartItems(userId);

      if (cartItems.length === 0) {
        throw new ApiError(400, 'Cart is empty');
      }

      // Calculate total
      const total = cartItems.reduce((sum, item) =>
        sum + (item.price * item.quantity), 0
      );

      // Process payment
      const payment = await this.paymentService.processPayment({
        amount: total,
        paymentMethodId,
        userId
      });

      // Create order
      const order = await Order.create({
        userId,
        total,
        status: 'pending',
        paymentId: payment.id
      }, { transaction });

      // Create order items
      await OrderItem.bulkCreate(
        cartItems.map(item => ({
          orderId: order.id,
          productId: item.productId,
          quantity: item.quantity,
          price: item.price
        })),
        { transaction }
      );

      // Clear cart
      await this.cartService.clearCart(userId, { transaction });

      await transaction.commit();

      return order;
    } catch (error) {
      await transaction.rollback();
      throw error;
    }
  }
}
```
</example>
</examples>

<success_criteria>
✅ All API endpoints respond within 200ms (p95)
✅ Test coverage exceeds 80%
✅ OpenAPI documentation is complete and accurate
✅ Security best practices implemented (JWT, rate limiting, input validation)
✅ Successfully handles 10,000 concurrent users in load tests
✅ Docker containerization works locally and in production
✅ CI/CD pipeline deploys successfully to AWS
✅ Payment processing works end-to-end with Stripe
✅ Error handling provides clear, actionable messages
✅ Database queries are optimized with proper indexes
</success_criteria>

<validation_checklist>
Before considering this API complete, verify:
- [ ] All endpoints documented in OpenAPI spec
- [ ] Authentication and authorization work correctly
- [ ] Input validation prevents invalid data
- [ ] Error responses follow consistent format
- [ ] Database transactions handle failures properly
- [ ] Redis caching reduces database load
- [ ] Rate limiting prevents abuse
- [ ] Logging captures important events
- [ ] Environment variables are documented
- [ ] README includes complete setup instructions
- [ ] Load tests meet performance requirements
- [ ] Security scan (npm audit) shows no critical issues
</validation_checklist>
```

## Why This Example Works

**Comprehensiveness:** Covers architecture, implementation, testing, and deployment in one prompt.

**Actionable:** Provides specific code examples and step-by-step workflow.

**Quality Gates:** Includes success criteria and validation checklist.

**Best Practices:** Integrates security, performance, and code quality standards contextually.

**Production-Ready:** Focuses on real-world constraints (performance, scalability, budget).

## Estimated Output
- **Token Count:** ~4,200 tokens (Core mode)
- **Implementation Time:** 40-60 hours for complete implementation
- **Lines of Code:** ~5,000-7,000 LOC including tests
