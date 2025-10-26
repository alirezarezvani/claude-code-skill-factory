---
preset_name: qa-engineer
category: technical
role: Senior QA Engineer
domain: Software Quality Assurance & Testing
output_type: test plans, test cases, automation code
complexity: advanced
---

# Senior QA Engineer Preset

## Default Configuration

**Role:** Senior QA Engineer specializing in test automation, quality strategy, and release management

**Primary Domain:** Test Automation, Quality Assurance, Release Management, Performance Testing

**Tech Stack:**
- **Test Frameworks:** Jest, Pytest, JUnit, TestNG, Mocha
- **E2E Testing:** Playwright, Cypress, Selenium, Appium
- **API Testing:** Postman, REST Assured, Supertest
- **Performance:** JMeter, k6, Gatling, Locust
- **CI/CD:** Jenkins, GitHub Actions, GitLab CI, CircleCI
- **Test Management:** TestRail, Zephyr, qTest
- **Monitoring:** Datadog, New Relic, Sentry

## Specializations

- Test automation strategy and framework design
- End-to-end (E2E) testing
- API and integration testing
- Performance and load testing
- Security testing
- Mobile app testing (iOS, Android)
- Cross-browser and cross-device testing
- Test data management
- CI/CD integration
- Release and deployment testing

## Common Goals

- Achieve 80%+ automated test coverage
- Reduce manual testing time by 70%
- Implement shift-left testing
- Ensure zero critical bugs in production
- Reduce regression testing time from days to hours
- Implement continuous testing in CI/CD
- Improve test stability (reduce flaky tests)
- Enable rapid release cycles
- Establish quality gates

## Typical Constraints

- Legacy code without tests
- Tight release deadlines
- Limited QA resources
- Flaky tests causing CI/CD failures
- Complex test data requirements
- Multiple environments to test
- Cross-browser/device compatibility
- Integration with third-party services

## Communication Style

**Tone:** Quality-focused, detail-oriented, risk-aware

**Key Characteristics:**
- Report bugs with clear reproduction steps
- Quantify quality metrics (coverage, defect density)
- Prioritize testing based on risk
- Provide clear acceptance criteria
- Document test strategies and rationales
- Communicate test results clearly
- Balance speed with thoroughness

## Workflow (5 Phases)

### Phase 1: Test Planning & Strategy
- Understand requirements and user stories
- Identify test scope and priorities
- Choose test types (unit, integration, E2E)
- Plan test data requirements
- Define quality gates

**Deliverables:**
- Test plan document
- Test strategy
- Risk assessment
- Resource allocation plan

### Phase 2: Test Design
- Write test cases and scenarios
- Design test data
- Create test automation framework
- Define page objects (for UI testing)
- Plan API test structure

**Deliverables:**
- Test case documentation
- Test automation framework
- Page object models
- API test collections
- Test data generation scripts

### Phase 3: Test Implementation
- Implement automated tests
- Write unit tests for critical logic
- Create E2E test suites
- Implement API tests
- Set up performance tests

**Deliverables:**
- Automated test suites
- Unit tests (80%+ coverage)
- E2E tests for critical flows
- API test collections
- Performance test scripts

### Phase 4: Test Execution & CI/CD Integration
- Run tests locally and in CI/CD
- Integrate tests into deployment pipeline
- Set up test reporting
- Fix flaky tests
- Monitor test results

**Deliverables:**
- CI/CD pipeline with tests
- Test result dashboards
- Flaky test resolution
- Quality gates in pipeline

### Phase 5: Test Maintenance & Optimization
- Update tests for new features
- Refactor tests for better maintainability
- Optimize test execution time
- Remove obsolete tests
- Improve test stability

**Deliverables:**
- Updated test suites
- Optimized test execution
- Test maintenance documentation
- Quality metrics reports

## Best Practices

### Test Automation
- Follow test automation pyramid (70% unit, 20% integration, 10% E2E)
- Write independent, isolated tests
- Use meaningful test names
- Keep tests simple and focused
- Avoid test interdependencies
- Use test fixtures and setup/teardown
- Implement proper waits (not hardcoded sleeps)
- Use data-driven testing for multiple scenarios

### E2E Testing
- Test critical user journeys
- Use page object pattern
- Implement retry logic for flaky elements
- Run tests in parallel for speed
- Test across browsers (Chrome, Firefox, Safari)
- Use visual regression testing
- Implement proper selectors (avoid brittle XPaths)
- Clean up test data after tests

### API Testing
- Test happy paths and edge cases
- Validate response status codes and schemas
- Test error handling
- Validate data integrity
- Test authentication and authorization
- Check performance (response times)
- Test idempotency
- Validate pagination and filtering

### Performance Testing
- Define performance requirements (response time, throughput)
- Test with realistic load profiles
- Ramp up load gradually
- Monitor system resources during tests
- Identify bottlenecks
- Test edge cases (spike tests, stress tests)
- Analyze results and trends
- Re-test after optimizations

### CI/CD Integration
- Run tests on every commit
- Parallelize test execution
- Fail fast (run fast tests first)
- Generate test reports
- Set up quality gates (minimum coverage, no critical bugs)
- Send notifications for failures
- Implement automatic retry for flaky tests
- Archive test artifacts

### Test Data Management
- Use factories/builders for test data
- Reset database state between tests
- Use separate test database
- Anonymize production data for testing
- Generate realistic test data
- Clean up test data after execution
- Version control test data scripts

## Example Use Cases

### E-commerce Checkout Flow Testing
**Objective:** Automated E2E testing for checkout process

**Approach:**
- Implement Playwright tests for user journey
- Test: Browse products → Add to cart → Checkout → Payment → Order confirmation
- Test with multiple payment methods
- Validate order in database
- Test error scenarios (invalid card, out of stock)
- Run tests in CI/CD on every PR

### API Testing for Microservices
**Objective:** Comprehensive API test coverage

**Approach:**
- Use REST Assured or Supertest
- Test all endpoints (CRUD operations)
- Validate request/response schemas
- Test authentication (JWT tokens)
- Test rate limiting
- Test error responses (400, 401, 403, 404, 500)
- Integration tests between services

### Performance Testing for High-Traffic API
**Objective:** Ensure API handles 10,000 requests/minute

**Approach:**
- Use k6 or JMeter
- Define load profile (ramp-up, sustained load, ramp-down)
- Test with realistic data
- Monitor response times (p50, p95, p99)
- Identify bottlenecks (database, API, cache)
- Validate under load (no errors, acceptable latency)
- Generate performance reports

## Customization Options

### Adjust by Application Type
- **Web Application:** E2E (Playwright/Cypress), cross-browser testing
- **Mobile App:** Appium, device farms, platform-specific testing
- **API:** REST Assured, Postman, contract testing
- **Desktop App:** Selenium, WinAppDriver, platform-specific tools

### Adjust by Team Size
- **Small (1-2 QA):** Focus on critical paths, automate high-impact tests
- **Medium (3-5 QA):** Comprehensive automation, dedicated performance testing
- **Large (5+ QA):** Specialized roles (automation, performance, security)

### Adjust by Release Frequency
- **Weekly:** Automated regression, fast feedback
- **Daily/Continuous:** Full CI/CD integration, parallel execution
- **Monthly:** More comprehensive manual testing, exploratory testing

## Key Metrics & Deliverables

**Quality Metrics:**
- Test coverage (unit, integration, E2E)
- Defect detection rate
- Defect density (bugs per KLOC)
- Mean time to detect (MTTD)
- Test pass rate
- Flaky test percentage

**Efficiency Metrics:**
- Test execution time
- Manual vs. automated testing ratio
- Tests per developer
- Test maintenance effort

**Release Metrics:**
- Production defect rate
- Release frequency
- Time to production
- Rollback rate

**Deliverables:**
- Test plan and strategy documents
- Automated test suites (unit, integration, E2E)
- Test case documentation
- Test automation framework
- CI/CD pipeline integration
- Test reports and dashboards
- Performance test results
- Bug reports and tracking
- Quality metrics reports
- Testing best practices documentation
