# Metadata Good and Bad Practices

This page provides **practical, non-normative** examples to support the requirements in **D6.2 §4.2.1 (Metadata Structures and Serializations)**. It is intended to help providers produce metadata that is consistent, discoverable, and interoperable across the CH Cloud.

**Scope:** Examples apply to machine-readable metadata exposed by providers for datasets, services/APIs, applications, semantic artefacts, and workflows.


## Good Practices

### Identifiers and URIs
- Use **stable HTTPS URIs** as identifiers (avoid local IDs as the primary identifier).
- Ensure identifiers are:
    - **dereferenceable** (resolve to a representation),
    - **stable across versions** (do not reuse identifiers for different things),
    - **consistent** across metadata, APIs, and documentation.
- Apply **predictable and persistent URI patterns** (document them).

### Licences and reuse
- Use **standard licence URIs** (e.g., Creative Commons, Open Data Commons).
- Make reuse conditions explicit (rights holder, attribution requirements, restrictions).
- Prefer machine-readable licences over free text.

### Descriptions and discoverability
- Provide clear, meaningful titles and descriptions (avoid placeholders like “Collection”).
- Include provider and contact information (email or URL).
- Add keywords/tags as arrays (not comma-separated strings), using controlled vocabularies where possible.
- Provide multilingual labels where feasible (e.g., `name`/`description` with language tags in JSON-LD).

### Semantics (L2+/L3)
- Use **JSON-LD** for metadata exchange where required/available.
- Keep `@context` **stable, documented, and versioned**.
- Link to authoritative vocabularies and authority files where applicable (e.g., Getty AAT, Wikidata, VIAF).
- Document the ontology profile in use and version it.

### Schemas and governance
- Declare the schema/profile used (and where it is defined).
- Version schemas explicitly; communicate breaking changes.
- Prefer deterministic, schema-governed structures over ad hoc/free-form fields.



## Bad Practices and Why They Fail

The table below shows common metadata anti-patterns and why they break interoperability.

| Anti-pattern | Example | Why it is a problem | Better alternative |
|---|---|---|---|
| Non-global identifier | `"id": "12345"` | Not globally unique or dereferenceable | Use a stable HTTPS URI (e.g., `"@id": "https://…/resource/12345"`) |
| Vague title | `"title": "Collection"` | Not meaningful for discovery | Use a descriptive title (scope, place/time, collection name) |
| Non-machine-readable licence | `"license": "Free to use"` | Cannot be processed consistently | Use a licence URI (e.g., Creative Commons URI) |
| Ambiguous date | `"date": "last year"` | Not standard; not comparable | Use ISO 8601 (e.g., `"modified": "2026-01-29"`) |
| Non-machine temporal period | `"date": "medieval period"` | Not computable; unclear boundaries | Use structured temporal fields and/or link to a controlled concept |
| Unstable or undocumented context | `"@context": "http://my-custom-context.example.org/v1"` | Custom context without documentation/community adoption increases friction | Use a documented and versioned context, preferably based on standard vocabularies |
| Free-text keywords blob | `"keywords": "medieval, manuscripts, religion"` | Hard to parse; inconsistent | Use an array (e.g., `"keywords": ["medieval", "manuscripts", "religion"]`) |



## Example: Non-compliant vs. Improved Metadata

### Non-compliant 

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
### Improved
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

Notes:
- Uses **dereferenceable** identifier (`@id`).
- Uses a **standard vocabulary** (`schema.org`) and predictable structure.
- Uses **ISO 8601** dates and a **licence URI**.
- Uses arrays for keywords and structured provider/contact metadata.

