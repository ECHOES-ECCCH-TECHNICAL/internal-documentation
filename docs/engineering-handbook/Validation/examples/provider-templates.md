# Provider Evidence Templates

These templates cover the main information needed to describe a resource and document its interoperability checks. Select the relevant files using the requirements catalogue and the applicability matrix for the resource type. Adapt the example values to the actual service or dataset.

## Templates

| Artefact | Main content | Download |
|---|---|---|
| Resource metadata | Identifier, provider contact, licence, version and access conditions | [resource-metadata.jsonld](assets/provider/templates/resource-metadata.jsonld) |
| API contract | OpenAPI 3.x operations, bearer authentication, errors and health endpoints | [api.openapi.yaml](assets/provider/templates/api.openapi.yaml) |
| Deployment | Runtime configuration, image reference and readiness checks | [deployment.yaml](assets/provider/templates/deployment.yaml) |
| Security | Endpoint classification, token handling and access-control tests | [security.yaml](assets/provider/templates/security.yaml) |
| Monitoring | Availability, logging, incident contacts and evidence references | [monitoring.yaml](assets/provider/templates/monitoring.yaml) |
| Provenance | Source data, processing steps and output relationships | [provenance.json](assets/provider/templates/provenance.json) |

The metadata template has a corresponding [JSON Schema](assets/provider/templates/resource-metadata.schema.json) and an [invalid sample](assets/provider/examples/resource-metadata-invalid.jsonld) for negative testing. Identifiers, access policies and licences in completed records must reflect the actual resource.

## Checking the examples

The [validator](assets/provider/scripts/validate_demo.py) checks sample metadata against the schema, parses JSON-LD and inspects selected fields in the OpenAPI YAML. It does not contact an API or test the running service.

Download the `provider/` files, keeping their directory structure, and run:

```bash
python3 -m pip install 'jsonschema>=4,<5' 'PyYAML>=6,<7' 'rdflib>=7,<8'
python3 scripts/validate_demo.py
```

The result is written to [`reports/demo-results.json`](assets/provider/reports/demo-results.json). It includes a valid metadata case, an intentionally invalid case, a negative check for the required provider contact and a basic API structure check. Review the individual outcomes and their scope. Passing these checks does not verify rights-holder approval, the long-term stability of identifiers or runtime API behaviour.

For RDF validation, see the [HDT SHACL example](hdt-semantic-validation.md). A small [dataset metadata shape](assets/provider/shapes/dataset-example.ttl) provides a separate example of SHACL property constraints.

## Recording the evidence

For each assessed resource, link the requirement to the method, result and supporting files. For example:

| Field | Example |
|---|---|
| Resource and release | `https://example.org/resources/collection-001`, version `1.0.0` |
| Requirement | `REQ-META-002` |
| Method | Static schema check |
| Evidence | Metadata record, schema revision, validator output |
| Result | Pass, Fail or justified Not applicable |
| Follow-up | Corrective action and retest, where needed |

Runtime and security assessments also require observed HTTP responses, test environments and relevant logs. The [VTL working assessment](assets/provider/reports/vtl-application-l1-working-assessment.csv), [TLS and logging observations](assets/provider/reports/vtl-route-and-logging-evidence-2026-10-25.md) and [endpoint classification summary](assets/provider/reports/vtl-sec03-classification-2026-10-25.md) show how provider observations can be recorded for review. They contain redacted summaries and do not assign a formal interoperability level.

Static checks can be included in a provider's normal development workflow. Contract and security tests against a running service require an approved environment and appropriately scoped credentials.

See [Validation Workflow](../workflow.md) for reporting and reassessment, and [Validation Artefacts](../artefacts.md) for evidence expectations.
