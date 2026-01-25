# Semantic monitoring playbook (Living Documentation for D6.2 §7.3)

This page provides **non-binding** implementation guidance supporting the normative semantic monitoring requirements in **D6.2 §7.3**.
It includes recommended drift/quality checks and an illustrative monitoring workflow.

---

## Recommended drift and quality signals (informative)

These checks are recommended to strengthen early detection of semantic drift beyond the mandatory checks defined in D6.2 §7.3.3.

| Signal category | Recommended checks |
|---|---|
| Identifier & URI integrity | Detect 404/410; redirects that change identity; content negotiation failures (if supported) |
| JSON-LD context & serialization | Detect term remapping without versioning; mixed contexts without policy; undefined terms |
| Vocabulary integrity (SKOS) | Multilingual tagging consistency (BCP47); missing labels for supported languages; label hygiene checks |
| Mapping integrity | Conflicting mappings; mapping cycles; mapping coverage regressions |
| Ontology integrity | Reasoning consistency checks and unsatisfiable classes only where reasoning functionality is declared |
| SHACL integrity | Detect shape drift without version bump; inconsistent shape application; validation performance regressions |
| SPARQL integrity | Sentinel queries for counts/predicates/vocabulary usage; spikes/drops indicating ingestion errors (sentinels documented and versioned) |

---

## Illustrative semantic monitoring workflow (non-binding example)

This workflow is an example of how teams can satisfy the capability intent of D6.2 §7.3 (it does not mandate specific tools).

### Nightly baseline checks
- Validate JSON-LD context resolvability (all declared contexts).
- Expand representative JSON-LD payloads and compare expansion determinism against baseline.
- Validate mapping target resolvability (where mappings exist).
- Run SHACL validation for declared L3 RDF assets and record pass/fail trends.
- Run URI dereferenceability checks where dereferenceability is expected.

### After each release or semantic change
- Re-run the baseline suite.
- Compare results to the previous baseline and publish a drift report.
- Correlate detected regressions with release events, configuration changes, or dependency upgrades.

### On failure
- Open an incident ticket and notify the declared owner/governance contact.
- Classify severity using D6.2 §7.3.4 (Critical/Major/Minor).
- Require remediation, documented transition strategy (where applicable), or downgrade/re-evaluation where necessary.
