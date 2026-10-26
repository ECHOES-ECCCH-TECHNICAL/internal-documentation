# Provider Validation Examples

These pages provide templates and worked examples for interoperability checks. The [validation workflow](../workflow.md) describes the assessment process, while [validation artefacts](../artefacts.md) and [semantic validation](../semantics.md) cover the supporting evidence.

| Example | Contents | Relevant requirements |
|---|---|---|
| [Provider Evidence Templates](provider-templates.md) | Metadata, API, deployment, security, monitoring and provenance templates, with sample checks | REQ-META, REQ-API, SEC, REQ-DEP, REQ-MON, REQ-PROV |
| [Heritage Digital Twin RDF and SHACL Validation](hdt-semantic-validation.md) | Example HDTO graph, SHACL shapes, SPARQL query and validation procedure | REQ-SEM-004/005, related provenance checks |
| [Deployment and Release Evidence](deployment-evidence.md) | Image builds, release identifiers, Kustomize, Argo CD, Helm and operational checks | REQ-API-002/003, relevant REQ-DEP and REQ-MON |

## Using the examples

1. Identify the resource, assessed release and applicable requirements. Applications, APIs and datasets can have different obligations.
2. Download the relevant files from the pages above and adapt them to the resource and environment.
3. Run the checks and record the inputs, versions, observations and results.
4. Retain the reports and evidence references for the conformance assessment.

The files are available individually from each page. Examples use demonstration identifiers and configuration values. When citing evidence in a conformance report, link to the repository revision used for the assessment so the cited files remain identifiable after subsequent changes.
