# Web Annotation Data Model (W3C)

The Web Annotation Data Model is a W3C standard (commonly represented in JSON-LD) for expressing annotations that target digital objects such as images, texts, audio, and 3D resources.

In cultural heritage contexts, it supports:
- shared annotation tools across institutions,
- alignment with IIIF (targeting canvases, regions),
- crowdsourcing, scholarly notes, contextualization, and enrichment.


## When to use Web Annotation

- Associating comments, regions of interest, or scholarly observations with digital objects.
- Enabling annotation functionality in CH Cloud tools.
- Interoperable annotation exchange across systems.

## When not to use Web Annotation

- Storing complex semantic assertions that require ontology-level modelling (use RDF/OWL + domain ontologies, optionally linked from annotations).
- Targeting non-HTTP resources that lack stable identifiers.


## Relevance to Cultural Heritage (CH Cloud)

- Strong candidate for Level 2 or Level 3 annotations.
- Integrates naturally with IIIF.



## Technical considerations

- Requires stable canonical URIs for annotation targets (and selectors for fragments/regions).
- Commonly represented in JSON-LD; compatible with Linked Data workflows.
- Apply access control where needed; avoid broadcasting sensitive personal data.


## References (informative)

- Web Annotation Data Model (W3C Recommendation): https://www.w3.org/TR/annotation-model/
- Web Annotation Vocabulary (W3C): https://www.w3.org/TR/annotation-vocab/
- IIIF and Web Annotation: https://iiif.io/api/annex/services/
