# Tooling and CI patterns (Living Documentation)

This page is intentionally tool-agnostic: list the tools you actually adopt in the repository (scripts, containers, CI jobs), and keep them updated here.

## Recommended repository layout
- /validation/
    - scripts/
    - schemas/
    - shacl/
    - openapi/
    - examples/
    - reports/

## CI integration patterns
- run static checks on PR (metadata/schema/openapi lint)
- run dynamic checks on staging deployments (smoke + contract probes)
- publish validation reports as CI artifacts
- keep a baseline for drift detection (esp. semantic assets)


