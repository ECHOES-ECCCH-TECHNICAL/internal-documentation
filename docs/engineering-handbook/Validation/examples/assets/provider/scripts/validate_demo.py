#!/usr/bin/env python3
"""Demonstration-only static checks. No ECCCH conformance level is assigned."""
import json
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from rdflib import Graph
BASE=Path(__file__).resolve().parents[1]
REPORT=BASE/'reports/demo-results.json'

def check_metadata(path, schema):
    doc=json.loads(path.read_text(encoding='utf-8'))
    errors=sorted(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(doc),key=lambda e:list(map(str,e.path)))
    syntax_ok=False
    try:
        Graph().parse(data=json.dumps(doc),format='json-ld')
        syntax_ok=True
    except Exception:
        pass
    return len(errors)==0 and syntax_ok, [e.message for e in errors], syntax_ok

def main():
    schema=json.loads((BASE/'templates/resource-metadata.schema.json').read_text())
    ok,errors,parsed=check_metadata(BASE/'templates/resource-metadata.jsonld',schema)
    bad, bad_errors,bad_parsed=check_metadata(BASE/'examples/resource-metadata-invalid.jsonld',schema)
    api=yaml.safe_load((BASE/'templates/api.openapi.yaml').read_text())
    api_structure=(api.get('openapi','').startswith('3.') and
        all(path in api.get('paths',{}) for path in ['/health','/ready','/v1/resources/{resourceId}']) and
        'Error' in api.get('components',{}).get('schemas',{}))
    report={
      'scope':'Synthetic static checks. No conformance level is assigned.',
      'checks':[
        {'id':'metadata_schema_positive','status':'Pass' if ok else 'Fail','requirement_ids':['REQ-META-001','REQ-META-002'], 'notes':'Checks the schema and JSON-LD syntax. Rights, identifier permanence and runtime behaviour require separate checks.'},
        {'id':'metadata_schema_negative','status':'Pass' if not bad else 'Fail','requirement_ids':['REQ-META-002'], 'notes':'Expected rejection of deliberately incomplete record.','errors':bad_errors},
        {'id':'openapi_parse_structure','status':'Pass' if api_structure else 'Fail','requirement_ids':['REQ-API-002'], 'notes':'Checks selected YAML fields. Full OpenAPI lint and runtime contract testing are separate.'},
        {'id':'semantic_context_versioning','status':'Not run','requirement_ids':['REQ-SEM-009'], 'notes':'Uses an illustrative inline context. An external versioned context has not been checked.'},
        {'id':'shacl','status':'Not run','requirement_ids':['REQ-SEM-005'], 'notes':'Run pySHACL separately when SHACL validation applies.'},
        {'id':'dynamic_api_contract','status':'Not run','requirement_ids':['REQ-API-003','REQ-API-007'], 'notes':'Requires a deployed endpoint, credentials and recorded observed responses.'}
      ],'level_assignment':'Not assessed'}
    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not (ok and not bad and api_structure):
        raise SystemExit(1)
if __name__=='__main__': main()
