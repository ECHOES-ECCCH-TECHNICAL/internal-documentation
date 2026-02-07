# DC & DCTERMS

Dublin Core is a lightweight metadata standard based on a small set of generic elements (title, creator, subject, date, and similar).
**DCMI Terms (DCTERMS)** extends and refines the original element set and is widely used in RDF contexts.

Dublin Core often acts as the lowest common denominator for cross‑domain interoperability.
Many systems can export it, which makes it a pragmatic baseline for discovery and onboarding.

This page provides practical, non‑normative guidance for using Dublin Core in CH Cloud contexts.

## What Dublin Core is good for

Use Dublin Core when you need:

- a minimal discovery record for initial registration and onboarding
- a common mapping target for heterogeneous legacy exports
- a lightweight metadata layer for cross‑domain search
- compatibility with repository tooling and harvesting interfaces, often via OAI‑PMH

In practice, Dublin Core works best as:

- a baseline minimum profile, or
- a fallback export, with mapping to richer models where needed

## When Dublin Core is not sufficient

Avoid using Dublin Core as the sole model when you need:

- rich cultural heritage semantics (events, actors, provenance chains)
- complex temporal structures and relationships
- ontology‑driven interoperability and reasoning (CIDOC CRM, EDM, domain ontologies are better fits)

A common pattern is DC for discovery and a richer model for deep semantics.

## DCMES vs DCTERMS

Practical distinction:

- DCMES (Dublin Core Metadata Element Set) provides 15 classic elements (for example `dc:title`, `dc:creator`)
- DCTERMS provides refined properties and better modelling options (for example `dcterms:created`, `dcterms:issued`, `dcterms:license`, `dcterms:spatial`)

Recommendation:
When you have a choice, prefer DCTERMS, especially in RDF and JSON‑LD environments, because it supports clearer typing and richer constraints.

## Serialisations and transport

Dublin Core is commonly encountered as:

- XML, especially via OAI‑PMH exports
- RDF, often with DCTERMS refinements
- JSON‑LD for web APIs, when mapped into linked data patterns

## Validation and application profiles

Dublin Core is intentionally flexible.
Interoperability improves when you adopt a constrained profile:

- define which properties are mandatory versus optional
- define expected datatypes (string, date, URI)
- define controlled vocabularies where relevant (subjects, resource types)
- validate exports using:

    - XSD for XML profiles
    - SHACL for RDF profiles
    - JSON Schema for JSON and JSON‑LD representations

## Recommended baseline fields

A practical discovery‑oriented baseline profile should include:

- identifier (stable where possible)
- title
- description
- creator or publisher
- date (created, issued, modified where available)
- rights and licence (prefer URI)
- type
- subject and keywords
- language where relevant
- contact point, or equivalent owner and steward metadata in the catalogue layer

## Common pitfalls

| Pitfall | Why it causes problems | Better pattern |
|---|---|---|
| Free‑text dates such as “circa 1900” in system date fields | Hard to compare and filter | Use ISO dates for system fields; keep human‑readable notes separately |
| Licence missing or free‑text only | Reuse cannot be automated | Use a licence URI (`dcterms:license`) |
| Uncontrolled keywords blob | Inconsistent discovery | Use arrays and controlled terms where possible |
| Using DC for complex CH semantics | Loss of meaning | Map DC into richer models for deep interoperability |

## References

- DCMES (Dublin Core elements): https://www.dublincore.org/specifications/dublin-core/dces/
- DCTERMS (DCMI Terms): https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
- Application profile guidelines: https://www.dublincore.org/specifications/dublin-core/profile-guidelines/
