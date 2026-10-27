#!/usr/bin/env python3
"""Recheck selected HDTO relationship/type constraints on the example RDF.
This is NOT a general-purpose SHACL engine or conformance certification.
"""
from pathlib import Path
import json
from rdflib import Graph, URIRef, RDF, Namespace
ROOT = Path(__file__).resolve().parent
rdf = Graph().parse(ROOT / 'data.ttl', format='turtle')
shape = Graph().parse(ROOT / 'shapes.ttl', format='turtle')
h = URIRef('https://example.org/echoes/examples/heritage-twin/hdt/703')
H = Namespace('http://isl.ics.forth.gr/ontology/echoes/')
d1 = URIRef('http://www.cidoc-crm.org/extensions/crmdig/D1_Digital_Object')
objects = list(rdf.objects(h, H.HP29_has_digital_object_part))
sets = list(rdf.objects(h, H.HP33_contains))
checks = {
    'HDT explicitly typed HC2': (h, RDF.type, H.HC2_Heritage_Digital_Twin) in rdf,
    'HP29 values are D1 IRIs': all(isinstance(o, URIRef) and (o, RDF.type, d1) in rdf for o in objects),
    'HP33 minimum one': len(sets) >= 1,
    'HP33 values are HC16 IRIs': all(isinstance(o, URIRef) and (o, RDF.type, H.HC16_Heritage_Proposition_Set) in rdf for o in sets),
}
print(json.dumps({'result':'pass' if all(checks.values()) else 'fail', 'rdf_triples':len(rdf), 'shape_triples':len(shape), 'digital_objects':len(set(objects)), 'proposition_sets':len(set(sets)), 'checks':checks}, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
