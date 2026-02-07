# Validation and Conformance Testing

This section provides **living documentation** that supports the normative validation approach defined in the **D6.2 deliverable**.
Use these pages for operational guidance, templates, examples, CI integration patterns, and troubleshooting.

The key principle is **evidence-based validation**: every PASS result must be backed by reproducible artefacts and logs.


## Contents

- **Workflow:** how validation runs are executed, what inputs are required, and what outputs are produced  
- **Validation artefacts:** what evidence is collected and how it is checked  
- **APIs and services:** contracts, runtime checks, restricted endpoints 
- **Datasets:** metadata, schema/profile conformance, provenance 
- **Semantics:** vocabularies, contexts, mappings, RDF/SHACL, drift signals  
- **Tooling and CI:** recommended repository layout and CI patterns 


## Validation classes

- **Static validation:** inspect artefacts (metadata, contracts, schemas, shapes).
- **Dynamic validation:** probe runtime endpoints and verify behaviour.
- **Operational validation:** assess monitorability, resilience signals, and drift detection outputs.
- **Supervised/manual validation:** used only when human confirmation is required (e.g., UI flows).


## Inputs and outputs 

### Submission inputs (evidence package)
A minimal submission includes:

- resource identifier + version
- declared interoperability level
- machine-readable metadata record location
- required artefacts (OpenAPI/schema/SHACL/etc., as applicable)
- runtime endpoints (if applicable)
- owner/steward contact and escalation route

### Validation outputs
Every run should produce:

- a conformance report (requirement-by-requirement)
- raw validator outputs (lint logs, validation reports, probe results)
- pointers to stored evidence (with timestamps/checksums where possible)


## Continuous evaluation and observability

Where required by the interoperability level/type, validation may also cover:

- **feedback capture integration** for applications (visible trigger, consent, pseudonymous/anonymous handling, proof of submission)
- **telemetry accessibility** for services/applications (queryable observability interface or delegated access to existing telemetry streams)

These checks are implemented as operational validations and must be supported by archived evidence.
