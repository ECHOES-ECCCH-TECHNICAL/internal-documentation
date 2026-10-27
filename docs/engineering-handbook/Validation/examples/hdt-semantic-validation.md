# Heritage Digital Twin RDF and SHACL Validation

RDF queries establish that data is accessible. SHACL checks whether a graph meets specified constraints. This example shows both steps using the [Heritage Digital Twin Ontology (HDTO) v1.1](https://echoes-eccch.github.io/HDTO-Heritage-Digital-Twin-Ontology/html/HDT_v1.1.html). It supports practical checks relevant to **REQ-SEM-004** and **REQ-SEM-005**.

## Example graph

The [RDF data](assets/semantic/data.ttl) contains 56 triples representing a transcription-related HDT. Resource identifiers and labels have been replaced with demonstration values. The HDTO and CRMdig vocabulary IRIs are unchanged.

| RDF element | Content |
|---|---|
| `HC2_Heritage_Digital_Twin` | One typed HDT |
| `HP29_has_digital_object_part` | Three digital-object links |
| `crmdig:D1_Digital_Object` | All three linked objects have this type |
| `HP33_contains` | Six proposition-set links |
| `HC16_Heritage_Proposition_Set` | All six linked resources have this type |
| Maintenance and `HP30_added_content` | Present in the graph, outside the scope of these SHACL checks |

In HDTO v1.1, HP29 links a volatile digital object to a CRMdig digital object. `HC2_Heritage_Digital_Twin` is a subclass of the volatile digital object. HP29 is optional, so the example shape does not require a minimum number of HP29 links.

HP33 connects an HDT to heritage proposition sets. The example checks for at least one HP33 link and requires its target to have the `HC16_Heritage_Proposition_Set` type.

## SHACL checks

The [shapes file](assets/semantic/shapes.ttl) targets the example HDT and checks four conditions:

1. The HDT has type `HC2_Heritage_Digital_Twin`.
2. Every HP29 value is an IRI of type `crmdig:D1_Digital_Object`.
3. The HDT has at least one HP33 link.
4. Every HP33 value is an IRI of type `HC16_Heritage_Proposition_Set`.

The profile uses `sh:targetNode`, `sh:class`, `sh:path`, `sh:nodeKind` and `sh:minCount`. It covers these selected HDTO relationships. Other ontology constraints, mapping rules and provenance checks need their own assessment. The example graph contains explicit `rdf:type` statements for the resources checked by the shape.

## Run locally

Download [`data.ttl`](assets/semantic/data.ttl) and [`shapes.ttl`](assets/semantic/shapes.ttl) into the same directory.

```bash
python3 -m pip install 'pyshacl>=0.25,<1'
pyshacl -s shapes.ttl -sf turtle -df turtle -f human data.ttl
```

To save the SHACL report:

```bash
pyshacl -s shapes.ttl -sf turtle -df turtle -f turtle data.ttl > validation-report.ttl
```

The expected outcome for this sample is `sh:conforms true`. Retain the input graph, shapes, report, validation date and tool version with the evidence record. The [structural check script](assets/semantic/verify_demo.py) and its [summary](assets/semantic/independent-structural-crosscheck.json) provide an additional RDF-level check. They do not run SHACL. Generate a pySHACL report from the downloadable graph when recording an executed validation.

## SPARQL retrieval

The [SPARQL CONSTRUCT query](assets/semantic/query.rq) extracts the HDT's statements and those of resources linked through HP29 and HP33. Its example IRI is not a live Knowledge Base endpoint.

For graph-level provenance, query the named graphs containing the relevant statements and retain their identifiers. The Turtle graph used here does not preserve named-graph boundaries. Publication records and operation identifiers should be retained separately where provenance or lineage is assessed.

## Interpreting the result

A successful SHACL run confirms the four selected conditions for the input graph and shapes used. It does not establish full HDTO coverage or a conformance level. Formal assessment follows the applicable requirements and the [Validation Workflow](../workflow.md).
