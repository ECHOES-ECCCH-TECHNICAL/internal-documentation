# Governance and roles

This page summarises the governance functions and decision rights that keep the CH Cloud interoperability framework stable, enforceable, and continuously maintainable.
It also defines the core obligations around change control, compliance, and communication.


## Governance structure

The interoperability framework SHALL be governed through the following functions.
Roles may be implemented by one or more project bodies, depending on project organisation.

### Interoperability Governance Board, IGB

Owns the interoperability framework and publishes authoritative versions of:

- interoperability levels
- requirements catalogue, REQ, SEC, NODE
- validation process
- node and federation requirements

### Technical Validation Team, TVT

Executes conformance testing and produces conformance reports.
Maintains test suites and validation tooling.

### Operational Federation Team, OFT

Operates federation wide control plane components where applicable, coordinates cross site operational processes, and ensures monitoring and revalidation triggers are applied consistently across nodes.

### Change Control Secretariat, CCS

Manages change requests, decision records, version publication, and communication to providers and operators.

## Decision rights

Governance SHALL establish decision rights for each area as follows.

| Area | Accountable | Admin | Consulted | Informed |
|---|---|---|---|---|
| Requirements catalogue, REQ, SEC, NODE | IGB | CCS | TVT, OFT | Providers and Operators |
| Validation rules and tooling | TVT | CCS | OFT | IGB, Providers and Operators |
| Node and federation operational requirements | OFT | CCS | TVT | IGB, Providers and Operators |
| Documentation templates | CCS | CCS | TVT, OFT | Providers and Operators |

## Charter and review cadence

Decision rights MUST be documented in a governance charter and reviewed at least annually.
Changes to decision rights MUST be recorded as governance decisions.

## Linked operational policies

- Change control, versioning, deprecation: see `change-control.md`.
- Compliance audits, onboarding, exceptions, record keeping: see `compliance.md`.

Governance SHALL ensure these policies are applied consistently across resource providers and node operators.
