# Continuous Monitoring and Feedback Loops

Once software is deployed, continuous monitoring ensures it remains healthy, performs well, and meets user needs. In the CH Cloud, monitoring also supports **federation readiness**: validators and evaluation teams need consistent signals across providers.

This page covers observability (logs/metrics/traces), operational feedback loops, and evaluation integration patterns that align with the consortium’s monitoring and evaluation approach.


## Observability baseline (logs, metrics, traces)

Observability relies on three complementary pillars:

| Pillar | Purpose | What it provides |
|---|---|---|
| Logs | event records | debugging context |
| Metrics | numeric time series | trends and alerting |
| Traces | request flows | cross-service latency and root cause |

Recommended practice:
- use **structured logging** (JSON) with standard fields
- define a minimum metrics set (latency, errors, throughput, uptime)
- adopt distributed tracing where systems are distributed or highly integrated


## Standard fields (recommended)

### Logs
Include (as applicable):
- timestamp, severity, service name, environment
- request/correlation id
- operation name (endpoint, job id, workflow step)
- outcome (success/failure + error code)

Avoid logging personal data; prefer pseudonymous identifiers when needed.

### Metrics
Prefer consistent naming and semantics across services (helps federation-level dashboards). Typical baseline metrics:
- response time (p95)
- throughput
- error rate (4xx/5xx split)
- uptime/availability
- auth success rate (for protected services)

### Traces
- propagate correlation/trace IDs across service boundaries
- sample errors at 100%; sample normal requests at an agreed rate

OpenTelemetry is a common standard approach; when supported, expose telemetry in OTLP or an agreed format.


## Evaluation readiness (feedback + analytics integration)

For tools and applications that participate in user-facing evaluation, implement **two complementary mechanisms**:

### 1) In-app feedback trigger (user feedback mechanism)
Recommended pattern:
- visible UI entry point (e.g., “Feedback”, “Rate this tool”)
- modular interaction: quick review (e.g., 5-star) → optional deeper questionnaire
- informed consent notice before capture (purpose, retention, pseudonymous identifiers)

Identity handling:
- authenticated users: pass OIDC `sub` (pseudonymous subject identifier)
- guest users: submissions are anonymous

### 2) Passive telemetry access (observability endpoint / query access)
Provide a standardized way for authorised analytics collectors to retrieve:
- logs/metrics/traces or the agreed subset required for ecosystem monitoring
- mandatory baseline signals (performance, reliability, adoption/usage, security/governance)

If telemetry is already exposed via an agreed standard interface (e.g., OpenTelemetry), it is typically sufficient to grant query access rather than duplicating streams.


## Alerting and incident feedback loops

Use alerting rules that map to user impact:
- elevated 5xx rates
- increased latency (p95/p99)
- auth failures spikes
- dependency failures (DB/queue/storage)

Operational feedback loop:
1. detect (alert)
2. triage (logs/traces)
3. mitigate (rollback / feature flag / capacity)
4. remediate (fix + release)
5. learn (post-incident note; update monitors/tests)


## Deployment feedback mechanisms (recommended)

### Canary releases
- deploy to a small traffic segment
- monitor error/latency signals
- expand gradually or rollback quickly

### Feature flags
Use flags to decouple deployment from activation and enable fast rollback of features without redeploying.


## Evidence artefacts (what to keep)

- dashboards or metric snapshots (baseline)
- alert definitions and escalation path
- example logs/trace correlation showing cross-service debugging
- evaluation integration evidence (feedback trigger + telemetry query access) where applicable


## Related pages
- [Testing](testing.md)
- [CI/CD](CICD.md)
- [Security](security.md)
- [KPIs](kpis.md)
