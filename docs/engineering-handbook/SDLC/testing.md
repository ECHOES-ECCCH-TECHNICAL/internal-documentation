## Unit, Integration, and End-to-End Testing

Automated testing helps catch issues early and enables safer changes over time. Testing provides confidence that code works as intended, reduces regression bugs, and serves as living documentation of system behavior. The ECHOES project recommends three complementary tiers of tests: unit, integration, and end-to-end (E2E).

All tests should run automatically in the CI/CD pipeline where feasible, with results reported in an accessible way (e.g., CI summaries, dashboards, or reporting tools such as ReportPortal). This automation ensures consistent quality checks without requiring manual intervention.

### Test Tiers Overview

Each tier of testing serves a distinct purpose and has different characteristics:

| Tier | Purpose | Typical Scope | Environment | Typical Tools |
|------|---------|---------------|-------------|---------------|
| **Unit** | Validate small, isolated logic units | Functions, classes, modules | Local development + CI | pytest (Python), JUnit (Java), Jest (JavaScript) |
| **Integration** | Verify component interactions and interfaces | APIs, databases, message queues, file I/O | CI + ephemeral environments | pytest + Docker, Robot Framework, contract tests, Testcontainers |
| **E2E** | Validate complete user workflows end-to-end | UI + backend + integrations | Staging or near-production environment | Playwright, Cypress, Robot Framework, Selenium |

### Recommended Expectations Per Tier
Understanding what each tier should and shouldn't do helps maintain an effective test suite:

| Tier | Should Be | Should Avoid | Key Checks |
|------|-----------|--------------|------------|
| **Unit** | Fast (milliseconds), deterministic, isolated; uses mocking/stubbing for dependencies | External dependencies (database, network, filesystem); complex test setup | Normal and edge cases; clear naming; stable assertions; boundary conditions |
| **Integration** | Covers interfaces and configuration; uses realistic dependencies (often containerized) | Excessive UI coverage; flakiness without stabilization; overly broad scope | API contracts, database migrations, authentication flows, configuration correctness, data persistence |
| **E2E** | Focused on critical user journeys; runs against a deployed system; validates cross-component behavior | Large, brittle test suites; duplicating unit/integration assertions; testing every edge case | Workflow success, cross-component behavior, basic UI accessibility, critical business processes |

### Test Strategy Details

#### Unit Tests

Unit tests form the foundation of your testing strategy. They should:

- **Run fast** (milliseconds per test) to provide immediate feedback during development
- **Be deterministic** with no random failures or dependencies on external state
- **Test one thing** at a time with clear focus on specific functionality
- **Use mocks and stubs** to isolate the code under test from dependencies
- **Cover edge cases** including error conditions, boundary values, and null inputs

**Good unit test characteristics:**
- Clear test names that describe what is being tested and expected outcome
- Arrange-Act-Assert structure for readability
- No side effects or shared state between tests
- Fast execution (entire suite runs in seconds, not minutes)

#### Integration Tests

Integration tests verify that components work together correctly. They should:

- **Test real integrations** with databases, message queues, APIs, and file systems
- **Use containerization** (e.g., Docker, Testcontainers) for reproducible test environments
- **Validate contracts** between services and APIs
- **Check configuration** to ensure components are wired correctly
- **Test data flow** across boundaries and layers

**Good integration test characteristics:**
- Isolated test environments that don't interfere with each other
- Realistic data scenarios that mirror production usage
- Clear setup and teardown to ensure clean state
- Focused scope (not full E2E workflows)

#### End-to-End Tests

E2E tests validate complete user workflows from the user interface through the full stack. They should:

- **Focus on critical paths** that represent core business value
- **Run against deployed systems** in staging or production-like environments
- **Test cross-component behavior** that can't be validated at lower levels
- **Include accessibility checks** for basic usability requirements
- **Be maintainable** with clear page objects or similar abstractions

**Good E2E test characteristics:**
- Small, focused test suite (10-50 tests for most systems)
- Explicit waits and retry logic to handle timing issues
- Screenshots and videos on failure for debugging
- Clear separation from unit and integration test concerns

### CI/CD Execution and Reporting

Automated test execution ensures consistent quality without manual intervention:

| Area | Guideline |
|------|-----------|
| **Automation** | Run unit tests on every PR to provide fast feedback; run integration tests on PR and/or merge to catch interface issues; run E2E tests on merge to main and scheduled (nightly) where appropriate to validate full workflows |
| **Quality gates** | Treat test failures as release blockers for critical services to maintain quality standards; prioritize fixing flaky tests to keep trust in CI and prevent "test blindness" |
| **Reporting** | Provide a short CI summary (what failed + links to details) in PR comments or status checks; expose detailed reports, logs, and screenshots via artifacts or dashboards (e.g., ReportPortal, Allure) for non-technical stakeholders to understand quality trends |
| **Tooling** | Prefer standard frameworks that integrate well with CI tooling (e.g., pytest, Robot Framework, Playwright, k6 for performance testing) to reduce maintenance burden and leverage community support |
| **Performance** | Keep unit test suites fast (under 5 minutes ideally) to maintain developer productivity; parallelize slower integration and E2E tests where possible |

### Test Pyramid Principle

Follow the test pyramid principle:
many fast unit tests at the base (70-80%), fewer integration tests in the middle (15-20%), and a small number of E2E tests at the top (5-10%). This ensures quick feedback while maintaining comprehensive coverage and keeping test execution time reasonable.

This distribution provides the best balance of:
- **Speed**: Unit tests provide instant feedback
- **Confidence**: Integration and E2E tests catch real-world issues
- **Maintainability**: Most tests are simple units that are easy to update
- **Cost**: Fast tests can run frequently without infrastructure overhead

---

## Using Test Frameworks

Different testing needs require different tools. Choose frameworks based on what you are testing (API vs. UI vs. performance), team skills, and CI/CD integration requirements. Prefer widely adopted tools with strong community support and good reporting.

### Framework selection guide

| Framework | Type | Best for | Key strengths |
|---|---|---|---|
| **Robot Framework** | Keyword-driven acceptance testing | Acceptance tests, API tests readable by non-developers, mixed-skill teams | Human-readable tests, large library ecosystem, rich HTML reports |
| **k6** | Load / performance testing | Performance validation, scalability checks, capacity planning | JavaScript-based scripting, CI-friendly, realistic load models, strong metrics |
| **Playwright** | End-to-end (E2E) UI testing | Web UI workflows, cross-browser validation | Reliable automation, auto-waiting, cross-browser, trace viewer |
| **pytest** | Unit / integration (Python) | Python services and libraries | Fixtures, parametrization, plugin ecosystem |
| **JUnit** | Unit / integration (Java) | Java services and libraries | Industry standard, excellent IDE support, mature tooling |
| **Jest** | Unit / integration (JS/TS) | Node/web components | Fast execution, snapshot testing, built-in mocking |

### Robot Framework (acceptance and API testing)

**When to use**
- Acceptance tests that domain experts and non-developers need to review.
- API testing with explicit, documented test cases.
- Teams with mixed technical backgrounds.

**Characteristics**
- Keyword-driven syntax that is easy to read.
- Extensive libraries for web/API/database testing.
- Generates detailed HTML reports.
- Suitable for “specification by example” workflows.

**Practical example (scenario)**
A metadata API is validated using Robot Framework test cases that curators can review: “Given an object exists, when I query by identifier, then I receive expected fields and licence URI”.

### k6 (load and performance testing)

**When to use**
- Validating performance under load and identifying bottlenecks.
- Testing scalability before production deployment.
- Establishing and tracking performance regressions across releases.

**Characteristics**
- JavaScript-based scripting (low barrier for many teams).
- Supports realistic load models (ramp-up, spike, soak).
- Produces detailed metrics and integrates with CI/CD.
- Enables threshold-based quality gates (e.g., p95 latency, error rate).

**Practical example (scenario)**
Simulate 1,000 concurrent users searching the CH Cloud metadata catalogue and assert p95 response time remains within an agreed threshold; fail the pipeline if thresholds are exceeded.

### Playwright (E2E web UI testing)

**When to use**
- Testing critical user workflows end-to-end through the browser.
- Verifying cross-browser compatibility.
- Reducing flakiness compared to legacy UI automation approaches.

**Characteristics**
- Auto-waiting for UI elements reduces timing-related flakes.
- Supports Chromium, Firefox, and WebKit.
- Trace viewer and debugging tooling for failures.
- Works well with screenshots/videos as CI artifacts.

**Practical example (scenario)**
Verify that curators can log in, search for objects, open details, and add annotations through the web interface, using a staging environment with test identities.

### Language-specific unit/integration frameworks

Use ecosystem-native frameworks for unit and integration testing:

- **pytest (Python)**: strong fixtures and parametrization; good for API and service tests.
- **JUnit (Java)**: standardised approach with strong IDE/tooling support.
- **Jest (JavaScript/TypeScript)**: fast and convenient, especially for frontend and Node services.

### Tooling placement across test tiers

| Tier | Recommended tools (examples) | Notes |
|---|---|---|
| Unit | pytest, JUnit, Jest | Keep fast and deterministic; avoid network and real services |
| Integration | pytest + Docker/Testcontainers, Robot Framework, contract tests | Prefer containerised dependencies; validate schemas/contracts |
| E2E | Playwright, Robot Framework, (Selenium if legacy) | Keep small and focused; treat failures as high-signal |
| Performance | k6 | Run regularly (nightly) and before major releases; use thresholds |

### Reporting and evidence

Regardless of framework, tests should produce actionable evidence:

- Machine-readable results (e.g., JUnit XML) for CI dashboards.
- Human-readable reports (e.g., HTML) for stakeholders.
- Failure artifacts (logs, screenshots, traces) for rapid debugging.
- Trend visibility (flaky tests, performance regression) where possible.
