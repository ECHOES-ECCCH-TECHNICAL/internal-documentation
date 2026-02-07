# Web Annotation Data Model 

The **Web Annotation Data Model** is a W3C standard for representing annotations about web resources (images, text, audio, video, and 3D).
It is commonly serialized as **JSON-LD** and is a widely used interoperability format for annotation exchange, especially in cultural heritage and **IIIF** ecosystems.

This page provides **practical, non-normative** guidance for adopting Web Annotation in CH Cloud tools and services.


## When to use Web Annotation

Use Web Annotation when you need to:
- exchange annotations across tools, services, or institutions,
- attach comments, tags, or scholarly statements to specific resources,
- target fragments (regions, ranges, time segments) via selectors,
- integrate annotation workflows with IIIF canvases, images, and manifests,
- support crowdsourcing or expert annotation with consistent portability.


## When Web Annotation is not enough

Web Annotation is usually not the right *primary* mechanism for:
- **ontology-level knowledge modelling** (use RDF/OWL/domain ontologies; link to them from annotations),
- **complex editorial workflows** with rich state machines (use an application workflow model; use Web Annotation for exchange),
- **unstable or missing identifiers** (address identifier governance first).

A common pattern is:
- Web Annotation for **portable annotation exchange**, and
- domain ontologies for **deep semantic assertions**, referenced from the annotation body.


## Key concepts

| Concept | Practical meaning |
|---|---|
| Annotation | The container resource (itself has an identifier) |
| Target | What is being annotated (a resource or fragment) |
| Body | The annotation content (text comment, tag, semantic URI, etc.) |
| Selector | How a fragment is addressed (region in image, quoted text, time segment) |
| Motivation | Why the annotation exists (commenting, tagging, describing, etc.) |


## Interoperability checklist (recommended)

### 1) Use stable target identifiers
Targets **SHOULD** be stable HTTP(S) URIs. This enables:
- long-term reuse of annotations,
- portability across services,
- federation and reconciliation.

If you use IIIF, prefer targeting:
- a IIIF **Canvas** (page-level targets), and/or
- a IIIF **Image** service with region selectors (image fragments).

### 2) Choose selectors that match media and intent
Pick selectors based on both media type and interoperability needs:
- **Images:** Media Fragments (`xywh`) or SVG selectors for regions
- **Text:** Quote selectors and/or text position selectors
- **Audio/Video:** Time selectors (start/end)
- **3D:** Document the selector convention you adopt (Web Annotation does not mandate a single approach)

### 3) Handle rights, privacy, and visibility explicitly
Annotations may include personal data (names, opinions) or sensitive context. Recommended rules:
- minimize personal data; use pseudonymous identities where appropriate,
- do not expose private annotations by default,
- document retention and visibility rules,
- if users submit annotations, provide a clear consent/privacy notice.

### 4) Plan for change: edits, moderation, and target drift
Annotations often need edits (typos, moderation, redaction). Recommended patterns:
- keep annotation identifiers stable; use `modified` timestamps and a documented moderation policy,
- avoid silent deletion; publish tombstones or clear redaction behavior,
- if targets move, maintain redirects and avoid frequent target churn.


## Minimal JSON-LD example

```json
{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "id": "https://annotations.example.org/anno/1",
  "type": "Annotation",
  "motivation": "commenting",
  "body": {
    "type": "TextualBody",
    "value": "Damage visible on the lower edge.",
    "format": "text/plain",
    "language": "en"
  },
  "target": {
    "source": "https://museum.example.org/iiif/image/123/full/full/0/default.jpg",
    "selector": {
      "type": "FragmentSelector",
      "conformsTo": "http://www.w3.org/TR/media-frags/",
      "value": "xywh=120,340,560,220"
    }
  }
}
```


## Validation checks (recommended)

- Annotation documents are valid JSON-LD (when JSON-LD is used).
- Targets resolve (or redirect predictably) when dereferenceability is expected.
- Selectors conform to documented selector conventions.
- Access control is enforced for private/restricted annotations.
- Rights statements for annotation content are clear (especially for crowdsourcing outputs).



## References (primary sources)
- Web Annotation Data Model (W3C): https://www.w3.org/TR/annotation-model/
- Web Annotation Vocabulary (W3C): https://www.w3.org/TR/annotation-vocab/
- IIIF and Web Annotation (annex): https://iiif.io/api/annex/services/
