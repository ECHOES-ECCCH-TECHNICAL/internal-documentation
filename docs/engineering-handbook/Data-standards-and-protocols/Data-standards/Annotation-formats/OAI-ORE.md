# OAI-ORE

OAI-ORE is a standard for describing **aggregations of related web resources** (compound digital objects) and their relationships. It's widely used in cultural heritage ecosystems (notably Europeana via EDM/OAI-ORE patterns) to represent objects with multiple files and representations.



## When to use OAI-ORE

**Use for:**
- Compound objects with multiple parts (pages, images, transcripts, derivatives)
- Machine-readable structure that says "these resources belong together"
- Europeana-style aggregation patterns
- Packaging multipart objects for exchange

**Don't use for:**
- General cultural heritage semantics (events, actors, provenance) ( use CIDOC CRM)
- Rich item-level description (use DC/EDM)
- Single-file objects with no parts

**Common pattern:** OAI-ORE for structure + DC/EDM/CIDOC CRM for description


## Key concepts

| Concept | Meaning |
|---------|---------|
| **Aggregation** | The compound object ("these resources belong together") |
| **Aggregated Resource** | A member resource (file, page, transcript) |
| **Resource Map** | The RDF document describing the aggregation |


## Quick start

1. **Identify** your compound object
2. **Assign stable URIs** to aggregation and each part
3. **Create** a Resource Map in Turtle, JSON-LD, or RDF/XML
4. **Publish** and maintain

### Minimal example

```turtle
@prefix ore: <http://www.openarchives.org/ore/terms/> .
@prefix dcterms: <http://purl.org/dc/terms/> .

<https://chcloud.example.org/aggregation/book-123>
  a ore:Aggregation ;
  dcterms:title "Medieval Manuscript 123"@en ;
  ore:aggregates <https://chcloud.example.org/file/book-123/page-001.jpg> ;
  ore:aggregates <https://chcloud.example.org/file/book-123/page-001-ocr.txt> .
```



## Best practices

### 1. Use stable identifiers
- Use persistent URIs (ARK, Handle, DOI, or stable HTTPS)
- Implement redirects if URIs change
- Pattern(example): `https://chcloud.example.org/aggregation/{collection}/{object}`

### 2. Distinguish parts vs representations
- **Parts:** conceptual divisions (pages, chapters)
- **Files:** actual bitstreams (TIFF, JPEG, OCR)
- **Derivatives:** thumbnails, tiles, alternates

Document what you include and how derivatives link to sources.

### 3. Handle rights explicitly
- Specify rights per resource when they differ
- Don't assume aggregation license covers all parts
- Enforce access control at retrieval time

```turtle
<https://chcloud.example.org/aggregation/diary-789>
  dcterms:rights <http://rightsstatements.org/vocab/InC/1.0/> ;
  ore:aggregates <https://chcloud.example.org/file/page-restricted.jpg> .

<https://chcloud.example.org/file/page-restricted.jpg>
  dcterms:accessRights "Institution access only"@en .
```

### 4. Version transparently
- Keep aggregation URI stable
- Use `dcterms:modified` on Resource Maps
- Document membership changes


## Tools

### Python

```python
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import DCTERMS, RDF

ORE = Namespace("http://www.openarchives.org/ore/terms/")
g = Graph()

agg = URIRef("https://chcloud.example.org/aggregation/book-123")
g.add((agg, RDF.type, ORE.Aggregation))
g.add((agg, DCTERMS.title, Literal("Book 123", lang="en")))

print(g.serialize(format="turtle"))
```


### SPARQL validation

```sparql
PREFIX ore: <http://www.openarchives.org/ore/terms/>
PREFIX dcterms: <http://purl.org/dc/terms/>

# Find aggregations without titles
SELECT ?agg WHERE {
  ?agg a ore:Aggregation .
  FILTER NOT EXISTS { ?agg dcterms:title ?title }
}
```

## Common pitfalls

- **Unstable URIs** — Use persistent identifiers from the start
- **Mixed concerns** — Don't overload ORE with descriptive metadata
- **Missing rights** — Make licenses explicit per resource
- **Silent updates** — Version Resource Maps when membership changes
- **Broken links** — Verify all aggregated URIs resolve


## References

- **OAI-ORE spec:** https://www.openarchives.org/ore/1.0/toc
- **Europeana EDM:** https://pro.europeana.eu/page/edm-documentation
- **rdflib docs:** https://rdflib.readthedocs.io/

