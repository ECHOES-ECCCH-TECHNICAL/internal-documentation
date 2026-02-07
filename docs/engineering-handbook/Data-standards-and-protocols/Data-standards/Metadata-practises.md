# Metadata Practices

This page provides **practical, non‑normative** guidance and examples for producing metadata that is:

- consistent (predictable fields and types),
- discoverable (usable in search and indexing),
- interoperable (portable across tools and institutions),
- auditable (clear provenance, ownership, and reuse conditions).

It complements the project’s interoperability documentation by focusing on implementation quality rather than normative wording.

Scope: machine‑readable metadata exposed by providers for datasets, services and APIs, applications, semantic artefacts, and workflows.

## 1) Minimum metadata set

Even when providers use different internal schemas, the following fields should be available, directly or via mapping, for federation and discovery.

### Identity and classification

- stable identifier, prefer a dereferenceable HTTPS URI
- resource type, dataset, service, application, workflow, semantic artefact
- title or name, human‑readable
- short description, human‑readable

### Ownership and contact

- provider organisation, name plus URL
- owner or steward, role name or team
- contact point, email and or support URL

### Reuse and access

- licence or reuse conditions as a standard URI where possible
- access model, open, restricted, embargoed, and if restricted a high‑level access policy statement

### Currency and change

- version, if the resource evolves
- creation and modification dates, ISO 8601 where possible
- changelog or release notes link for services and evolving datasets, recommended

### Discovery fields

- keywords or subjects, array, preferably controlled terms
- spatial and temporal coverage, structured where possible
- language, where relevant

## 2) Good practices

### 2.1 Identifiers and URIs

- use stable HTTPS URIs as identifiers, avoid local IDs as the primary identifier
- ensure identifiers are:

  - globally unique
  - stable across versions, do not reuse identifiers for different things
  - consistent across metadata, APIs, and documentation

- if identifiers are intended to be dereferenceable, ensure they resolve to a representation, HTML and or machine‑readable

Recommended: document the URI pattern, what segments mean, whether IDs are opaque, and the versioning policy.

### 2.2 Licences and reuse

- use standard licence URIs, Creative Commons, Open Data Commons, and similar
- if reuse is restricted, express that in structured form, not free text only
- include:

  - rights holder, where applicable
  - attribution requirements
  - constraints, for example non‑commercial, share‑alike, embargo

Avoid ambiguous statements like “free to use” that cannot be interpreted consistently.

### 2.3 Titles, descriptions, and discoverability

- use descriptive titles, avoid placeholders like “Collection”
- provide a concise description that answers what, who, where and when, why it exists, and how it can be reused
- use keyword arrays, not comma‑separated strings
- use controlled vocabularies where possible, subjects, object types, techniques

### 2.4 Multilingual metadata

If you provide multilingual labels:

- use a consistent strategy:

  - language‑tagged strings, JSON‑LD and RDF, or
  - separate fields per language, and document the mapping

- avoid mixing languages in the same field without tags

### 2.5 Schema and profile declaration

- declare which schema or profile is used and where it is defined
- version schemas explicitly and communicate breaking changes
- prefer deterministic, schema‑governed structures over ad hoc and free‑form fields

Where appropriate, publish:

- JSON Schema, XSD, and or SHACL artefacts
- example records validated against the artefacts

### 2.6 Semantics, where applicable, L2+ and L3 style

- use JSON‑LD where semantic interoperability is needed or already adopted
- keep `@context`:

  - stable
  - documented
  - versioned

- link to authoritative vocabularies and authority files where applicable, for example Getty AAT, Wikidata, VIAF
- avoid silent semantic changes, term remapping without a version bump

### 2.7 Provenance and transformation transparency

If your metadata is produced by pipelines or enrichment:

- record the source system and export date
- distinguish source versus derived or enriched fields
- document transformation steps and version the transformation rules

This matters for trust and reproducibility, especially for aggregated catalogues.

## 3) Common anti‑patterns and why they fail

| Anti‑pattern | Example | Why it is a problem | Better alternative |
|---|---|---|---|
| Non‑global identifier | `"id": "12345"` | Not globally unique or dereferenceable | Use a stable HTTPS URI, for example `"@id": "https://…/resource/12345"` |
| Vague title | `"title": "Collection"` | Not meaningful for discovery | Use a descriptive title, scope, place, time, collection name |
| Non‑machine‑readable licence | `"license": "Free to use"` | Cannot be processed consistently | Use a licence URI, for example a CC BY URI |
| Missing ownership or contact | none | No escalation route, hard to reuse responsibly | Add owner or steward plus contact point |
| Ambiguous date | `"date": "last year"` | Not standard, not comparable | Use ISO 8601, for example `"dateModified": "2026-01-29"` |
| Free‑text keywords blob | `"keywords": "medieval, manuscripts"` | Hard to parse, inconsistent | Use an array, for example `"keywords": ["medieval", "manuscripts"]` |
| Mixed‑language string | `"description": "… (EN) … (FR)"` | Not indexable per language | Use language tags or separate fields |
| Undocumented context | `"@context": "http://my-context/v1"` | Friction, hard to validate | Publish a documented, versioned context and keep it stable |
| Silent schema drift | removing fields without notice | Breaks consumers and validators | Version schemas and announce breaking changes |
| Inconsistent types | `"dateCreated": 20260129` | Breaks validation and indexing | Use consistent types, ISO date strings |

## 4) Example: non‑compliant vs improved metadata

### 4.1 Non‑compliant example

```json
{
  "id": "12345",
  "title": "Collection",
  "license": "Free to use",
  "date": "last year",
  "@context": "http://my-custom-context.example.org/v1",
  "keywords": "medieval, manuscripts, religion"
}
```

### 4.2 Improved example

```json
{
  "@context": "https://schema.org",
  "@id": "https://example.org/resource/collection/12345",
  "@type": "Dataset",
  "name": "Medieval Manuscripts Collection (Provider X)",
  "description": "Digitised manuscript descriptions and selected images from Provider X, curated for discovery and reuse.",
  "provider": {
    "@type": "Organization",
    "name": "Provider X",
    "url": "https://example.org"
  },
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "dateCreated": "2024-06-15",
  "dateModified": "2026-01-29",
  "keywords": ["medieval", "manuscripts", "religion"],
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "mailto:contact@example.org"
  }
}
```

Why this is better:

- uses a dereferenceable identifier, `@id`
- uses a standard vocabulary, Schema.org, and predictable structure
- uses ISO 8601 dates and a licence URI
- uses arrays for keywords and structured provider and contact metadata


## References

- Schema.org, JSON‑LD vocabulary: https://schema.org/
- JSON‑LD 1.1 (W3C): https://www.w3.org/TR/json-ld11/
- ISO 8601 dates overview: https://www.iso.org/iso-8601-date-and-time-format.html
- Creative Commons licences: https://creativecommons.org/licenses/
