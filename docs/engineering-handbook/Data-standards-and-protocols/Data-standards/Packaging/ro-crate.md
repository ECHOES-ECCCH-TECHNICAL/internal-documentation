# RO‑Crate

RO‑Crate is a lightweight, machine‑actionable packaging format that uses **JSON‑LD** to describe files, metadata, provenance, workflows, and relationships.
RO‑Crate metadata is stored in `ro-crate-metadata.json` as JSON‑LD.

This page provides practical, non‑normative guidance for adopting RO‑Crate in CH Cloud ingestion and exchange workflows.

## What RO‑Crate is good for

Use RO‑Crate when you need:

- datasets accompanied by rich metadata (structure, description, rights, contacts)
- provenance and processing context (digitisation, derivation, enrichment workflows)
- reproducible packaging for research and validation (inputs, tools, outputs)
- an exchange format that can be validated and versioned with clear semantics

## When RO‑Crate is not the best choice

RO‑Crate may be unnecessary when:

- you only need fixity for a file transfer with minimal metadata (BagIt may be simpler)
- the dataset is extremely large and you do not benefit from packaging relationships and provenance (consider catalogue‑level metadata plus checksums)
- your workflow cannot maintain stable identifiers and versioning for crate contents (stabilise those foundations first)

## Core components

A crate is typically a folder or archive that includes:

- payload files (data, media, documentation)
- `ro-crate-metadata.json` as the canonical metadata entry point
- optional profile indicators and additional documentation

RO‑Crate profiles allow communities to constrain expected fields and entity patterns.

## Recommended minimum crate metadata

At minimum, a crate should provide:

- crate name or title and description
- stable identifier or identifiers where applicable
- publisher or organisation and contact point
- licence or rights statement (prefer standard URIs)
- date created and modified or a release version
- explicit listing of payload files that matter for reuse
- checksums or file sizes where practical (helps integrity checks even without BagIt)

If the crate includes derived outputs:

- link derived files to their sources (provenance)
- record the transformation process (tool name and version plus parameters), where feasible

## Minimal illustrative ro-crate-metadata.json

```json
{
  "@context": "https://w3id.org/ro/crate/1.1/context",
  "@graph": [
    {
      "@id": "ro-crate-metadata.json",
      "@type": "CreativeWork",
      "conformsTo": { "@id": "https://w3id.org/ro/crate/1.1" },
      "about": { "@id": "./" }
    },
    {
      "@id": "./",
      "@type": "Dataset",
      "name": "Example CH dataset package",
      "description": "Digitised images with JSON-LD metadata sidecars for onboarding validation.",
      "license": "https://creativecommons.org/licenses/by/4.0/",
      "publisher": { "@id": "#org" }
    },
    {
      "@id": "#org",
      "@type": "Organization",
      "name": "Example Provider",
      "url": "https://example.org"
    },
    {
      "@id": "data/images/obj-12345_access.jpg",
      "@type": "File",
      "encodingFormat": "image/jpeg"
    },
    {
      "@id": "data/metadata/obj-12345.jsonld",
      "@type": "File",
      "encodingFormat": "application/ld+json"
    }
  ]
}
```

## Validation

A RO‑Crate validation run commonly confirms:

- `ro-crate-metadata.json` parses as JSON‑LD
- required entities and fields exist for the adopted profile, if any
- files referenced in the crate exist (no dangling references)
- licences and ownership or contact metadata are present and consistent
- provenance relationships are coherent when declared

For reproducibility, store:

- the crate version (tag or commit hash)
- validator tool version
- validation outputs (pass or fail plus error list)

## Profiles and community constraints

If the CH Cloud adopts or defines a community profile:

- publish the profile as versioned documentation
- supply SHACL (or equivalent) validation rules where possible
- provide worked examples (good crates) and counter‑examples (common mistakes)

Profiles make RO‑Crate more interoperable by reducing ambiguity.

## RO‑Crate vs BagIt

| Need | Prefer |
|---|---|
| Integrity and fixity during transfer | BagIt |
| Rich metadata and relationships | RO‑Crate |
| Provenance and workflow description | RO‑Crate |
| Offline transfer plus rich metadata | BagIt with RO‑Crate inside |
| Minimal packaging with very low overhead | BagIt (or none) |

## References

- RO‑Crate specification: https://www.researchobject.org/ro-crate/
- RO‑Crate 1.1: https://www.researchobject.org/ro-crate/1.1/
- JSON‑LD 1.1 (W3C): https://www.w3.org/TR/json-ld11/
