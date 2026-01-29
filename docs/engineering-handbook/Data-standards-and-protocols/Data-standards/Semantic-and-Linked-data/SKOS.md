# SKOS (Simple Knowledge Organization System)

SKOS is a W3C standard for representing **controlled vocabularies**, thesauri, taxonomies, and classification schemes as linked data. It provides a simple, consistent way to publish terminology systems on the web and link them across institutions.

Cultural heritage institutions rely on controlled vocabularies for:
- subjects,
- object types,
- materials,
- techniques,
- periods, etc.

SKOS makes these vocabularies shareable and interoperable: terms can be linked across languages, mapped between vocabulary systems, and reused consistently in metadata. For example, concepts in the Getty Art & Architecture Thesaurus (AAT) can be mapped to equivalent concepts in national or institutional vocabularies.


## When to use SKOS

Use SKOS when you need to publish, consume, or align **terminology systems**:

- Publishing or consuming controlled vocabularies and thesauri.
- Providing subject classifications, material terms, or technique terms.
- Enabling multilingual access (SKOS supports multiple labels per concept).
- Mapping between different terminology systems (crosswalks).
- Supporting faceted search and browse interfaces.

## When not to use SKOS

SKOS may not be the right tool in these cases:

- Complex logical constraints or automated inference are required.
- Full ontological modelling is needed with rich domain semantics (use OWL/domain ontologies).
- Frequently changing internal lists are not yet curated and stable.
- Modelling data instances (actual objects/events) — use RDF with domain ontologies (e.g., CIDOC CRM) for instances; SKOS is for *concept schemes*.


## Relevance to Cultural Heritage (CH Cloud)

- Critical for **Level 2** semantic alignment.
- Enables terminology unification and multilingual discovery across CH providers.
- Many CH actors already publish SKOS vocabularies (e.g., Getty AAT, Iconclass, national subject headings).


## Technical considerations

### Core classes and properties

| Term | Meaning |
|---|---|
| `skos:Concept` | A concept (term) in a controlled vocabulary |
| `skos:ConceptScheme` | A vocabulary or classification scheme |
| `skos:prefLabel` | Preferred label (typically one per language) |
| `skos:altLabel` | Alternative labels and synonyms |
| `skos:broader` / `skos:narrower` | Hierarchical relations |
| `skos:related` | Associative relation (non-hierarchical) |
| `skos:exactMatch` / `skos:closeMatch` | Cross-vocabulary mappings |

### Best practices

- Assign each concept a **stable, dereferenceable URI**.
- Maintain **one `skos:prefLabel` per language** per concept.
- Use `skos:altLabel` for synonyms, spelling variants, and near-equivalent labels.
- Document the vocabulary scope, versioning, and governance (who maintains it, update policy).

### Validation

Validate SKOS consistency using:
- SKOS integrity constraints, and/or
- SHACL shapes (e.g., enforce “max one `skos:prefLabel` per language”).

### Publishing options

SKOS vocabularies can be published:
- via SPARQL endpoints,
- as RDF dumps (Turtle / RDF/XML / JSON-LD),
- as downloadable files with documentation and version tags.


## Example: Concept with multilingual labels and hierarchy

The Getty AAT contains a concept for “watercolor painting”:

```turtle
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix aat:  <http://vocab.getty.edu/aat/> .

aat:300078925 a skos:Concept ;
  skos:prefLabel "watercolor painting"@en ;
  skos:prefLabel "Aquarellmalerei"@de ;
  skos:prefLabel "aquarelle"@fr ;
  skos:broader aat:300054216 ;   # painting (image making)
  skos:narrower aat:300404620 .  # botanical watercolors
```

A Polish archive could link its local concept “akwarela” to the AAT concept using `skos:exactMatch`, enabling cross-collection search using shared semantics:

```turtle
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://archive.example.org/vocab/materials/akwarela> a skos:Concept ;
  skos:prefLabel "akwarela"@pl ;
  skos:exactMatch <http://vocab.getty.edu/aat/300078925> .
```

## References (informative)

- SKOS Reference (W3C): https://www.w3.org/TR/skos-reference/
- SKOS Primer (W3C): https://www.w3.org/TR/skos-primer/
- Getty AAT (vocabulary): https://www.getty.edu/research/tools/vocabularies/aat/
