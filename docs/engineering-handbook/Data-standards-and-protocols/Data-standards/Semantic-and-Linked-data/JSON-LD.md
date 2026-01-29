# JSON-LD (JSON for Linking Data)

JSON-LD is a JSON-based format for expressing **Linked Data**. It introduces an `@context` that maps JSON keys to RDF IRIs, making ordinary JSON **semantically meaningful**.

JSON is the dominant payload format for web APIs and applications, but traditional JSON has no built-in semantics. JSON-LD bridges this gap:

- Developers work with familiar JSON.
- Systems can interpret the same payload as RDF / Linked Data.


## When to use JSON-LD

- APIs exchanging structured metadata or object descriptions.
- Integration with modern web applications and JavaScript frameworks.
- Teams more comfortable with JSON than RDF syntax.
- Lightweight semantic integration without running a full RDF stack.
- Ecosystems where JSON is already the preferred interchange format.

## When not to use JSON-LD

- Ontology engineering and complex ontology authoring where Turtle/RDF/XML may be more practical.
- Pipelines where all tools already operate on RDF syntaxes directly and JSON provides no advantage.
- Cases where raw human readability for ontology specialists is the primary requirement.


## Relevance to Cultural Heritage (CH Cloud)

- Highly relevant for **Level 1 and Level 2** interoperability at the API layer.
- Used by IIIF, Schema.org, and newer CH APIs, making it a natural choice for modern CH Cloud services exposing or consuming Linked Data.


## Technical considerations

### `@context`
Maps compact terms to full URIs/IRIs. Contexts may be inline or referenced externally. Context stability and versioning matter.

### Expansion / compaction
JSON-LD can be programmatically:
- **expanded** into full RDF form,
- **compacted** into a more developer-friendly form using a context.

### Framing
**Framing** reshapes JSON-LD into a structure that matches application needs while preserving RDF semantics.

### Validation
- Use **JSON Schema** for structural checks (required fields, types).
- Use **SHACL** for semantic constraints on the RDF graph (cardinality, class membership, property constraints).

### Tooling
- JavaScript: `jsonld.js`
- Python: `PyLD`
- JSON-LD Playground
- RDF toolchains that support JSON-LD import/export


## Example 
A museum API returns object metadata as JSON-LD:

```json
{
  "@context": "https://linked.art/ns/v1/linked-art.json",
  "@type": "HumanMadeObject",
  "id": "https://museum.example.org/object/12345",
  "identified_by": [
    {
      "@type": "Name",
      "content": "Portrait of a Woman",
      "language": "en"
    }
  ],
  "produced_by": {
    "@type": "Production",
    "carried_out_by": {
      "@type": "Person",
      "id": "https://vocab.getty.edu/ulan/500011051",
      "identified_by": [
        {
          "@type": "Name",
          "content": "Rembrandt van Rijn"
        }
      ]
    },
    "timespan": {
      "@type": "TimeSpan",
      "begin_of_the_begin": "1632-01-01",
      "end_of_the_end": "1632-12-31"
    }
  }
}
```

A web application can treat this as normal JSON, while semantic tools can interpret it as RDF and integrate it into a larger knowledge graph.


## References (informative)

- JSON-LD 1.1 (W3C Recommendation): https://www.w3.org/TR/json-ld11/
- JSON-LD 1.1 API (W3C): https://www.w3.org/TR/json-ld11-api/
- JSON-LD Playground: https://json-ld.org/playground/
- SHACL (W3C Recommendation): https://www.w3.org/TR/shacl/
- JSON Schema: https://json-schema.org/
