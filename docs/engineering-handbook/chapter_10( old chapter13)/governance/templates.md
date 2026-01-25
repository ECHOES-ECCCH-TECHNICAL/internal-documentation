# Templates (evidence packages) (D6.2 Chapter 10)

This page lists the required onboarding/validation templates and provides a compact “starter” structure for each. Treat these as versioned artefacts.

---

## Required templates

### 1) Resource metadata template
Required:
- id (persistent)
- title, description
- provider/owner + contact
- licence/rights
- version (or immutable release id)
- access classification
- created/updated timestamps  
  Optional:
- provenance links
- schema/profile references
- vocabulary references/mappings

### 2) API documentation template
Required:
- service id + base URL(s)
- endpoint inventory (public vs restricted)
- OpenAPI location (if applicable)
- error model summary
- versioning + deprecation policy
- health/readiness endpoints  
  Optional:
- synthetic test list
- release notes/changelog link

### 3) Deployment template
Required:
- runtime model (Kubernetes/VM/hybrid)
- dependencies
- configuration model
- health/readiness behaviour
- rollback approach  
  Optional:
- capacity assumptions
- maintenance windows

### 4) Security template
Required:
- endpoint classification
- auth model (AAI integration if restricted)
- token validation behaviour
- secrets handling approach
- logging/redaction rules  
  Optional:
- compensating controls (if any)
- security scanning evidence

### 5) Monitoring template
Required:
- signals monitored (availability, error rate, latency, auth failures where applicable)
- alert rules summary
- escalation contact  
  Optional:
- dashboards links
- periodic drift checks (semantic, contract)

### 6) Provenance template
Required (where applicable):
- lineage: inputs → processing → outputs
- tools/versions/parameters
- release links and version identifiers  
  Optional:
- reproducibility notes
- environment identifiers for compute-heavy workflows
