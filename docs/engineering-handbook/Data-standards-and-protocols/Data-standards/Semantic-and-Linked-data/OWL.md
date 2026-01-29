# OWL (Web Ontology Language)

OWL is a W3C standard for creating **formal ontologies**: conceptual models that define classes, properties, and logical relationships in a machine-interpretable way. OWL is more expressive than SKOS and can capture complex domain semantics and constraints.

Cultural heritage data frequently involves:
- events located in time and space,
- objects created through processes involving multiple actors,
- materials and techniques,
- detailed provenance and ownership chains.

OWL enables precise modelling of these relationships and supports **automated reasoning** (inferring new facts from existing assertions).



## When to use OWL

Use OWL when formal semantics and reuse across systems are required:

- Schema-level alignment is needed (e.g., mapping to or extending CIDOC CRM).
- You need to express complex constraints (e.g., “a production event must have at least one actor”).
- Automated reasoning provides value (e.g., inferring indirect relationships, class membership, property chains).
- You are building ontologies intended to be shared, extended, and reused across projects.
- Integration requires nuanced semantic distinctions beyond taxonomies.

## When not to use OWL

OWL may be unnecessary or impractical in these cases:

- Only simple metadata lists or flat taxonomies are needed (e.g., Dublin Core may suffice).
- Systems will not run ontology-aware tooling (no reasoning, no semantic infrastructure) and no conversion pathway is planned.
- Performance constraints make reasoning overhead unacceptable.
- The data and use cases do not benefit from formal semantics.


## Relevance to Cultural Heritage (CH Cloud)

- Highly relevant for **advanced interoperability (Level 3)** and work involving **Heritage Digital Twins (HDTs)** and semantic modelling.
- **CIDOC CRM**, a primary cultural heritage ontology referenced in the project, is expressed using **OWL/RDFS** patterns.
- Partners defining CH Cloud semantic models and profiles typically rely on OWL as a representation language.


## Technical considerations

### OWL 2 profiles

OWL 2 defines profiles with different expressiveness/performance trade-offs:

| Profile | Typical strength | Typical use |
|---|---|---|
| **EL** | Efficient reasoning over large class hierarchies | Biomedical-style ontologies; scalable classification |
| **QL** | Query answering over large datasets | Ontology-based data access (OBDA) patterns |
| **RL** | Rule-friendly subset | Rule engines; scalable reasoning with forward-chaining |

### Core constructs

| Construct | Meaning | Example use |
|---|---|---|
| `owl:Class` | Types of things | `crm:E22_Human-Made_Object` |
| `owl:ObjectProperty` | Relationships between things | production → produced object |
| `owl:DatatypeProperty` | Attributes with literal values | titles, dates, identifiers |
| `owl:equivalentClass` | Class alignment across ontologies | mapping two class definitions |
| Restrictions | Constraints (cardinality, values, etc.) | “at least 1 actor” |

### Reasoning

Reasoners can infer implicit relationships and classifications. Common tools include:
- HermiT
- Pellet
- ELK

### Validation

OWL alone is not always sufficient for operational validation. In practice:
- OWL is often combined with **SHACL** (constraint validation), and/or
- custom rules for domain-specific checks.

### Learning curve

OWL has a steeper learning curve than SKOS/RDF and typically requires familiarity with description logics and ontology engineering patterns.



## Example: CIDOC CRM in OWL/RDFS style 
A simplified example of defining a production event and its relationship to produced objects:

```turtle
@prefix crm:  <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

crm:E12_Production rdf:type owl:Class ;
  rdfs:subClassOf crm:E11_Modification ;
  rdfs:label "Production"@en ;
  rdfs:comment "This class comprises activities that bring into existence new physical objects."@en .

crm:P108_has_produced rdf:type owl:ObjectProperty ;
  rdfs:domain crm:E12_Production ;
  rdfs:range crm:E24_Physical_Human-Made_Thing .
```

From such schema-level definitions (and additional axioms, where present), reasoning engines can infer class membership and relationship implications, supporting richer interoperability across datasets.


## References (informative)

- OWL 2 Web Ontology Language Document Overview (W3C): https://www.w3.org/TR/owl2-overview/
- OWL 2 Profiles (W3C): https://www.w3.org/TR/owl2-profiles/
- RDFS (W3C): https://www.w3.org/TR/rdf-schema/
- SHACL (W3C): https://www.w3.org/TR/shacl/
- CIDOC CRM: https://www.cidoc-crm.org/
