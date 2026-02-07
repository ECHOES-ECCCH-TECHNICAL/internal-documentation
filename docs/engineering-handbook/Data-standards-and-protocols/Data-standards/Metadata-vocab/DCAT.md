# DCAT

DCAT is a W3C RDF vocabulary for describing **datasets**, **data services**, and **distributions** in catalogues.
It is designed for catalogue interoperability: discovery, harvesting, and re‑exposure of dataset and service records across portals.
DCAT describes what a dataset or service is and how it can be accessed.
It does **not** replace domain models used to describe cultural heritage items.

This page provides practical, non‑normative guidance for using DCAT in CH Cloud catalogue layers and for interoperability with wider European catalogue ecosystems.

## What DCAT is good for

Use DCAT when you need:

- a catalogue layer that lists datasets and services consistently across providers
- interoperability with external portals, including EOSC‑like catalogue ecosystems
- machine‑readable descriptions of access endpoints, formats, licences, and basic provenance
- harvesting and re‑syndication workflows (catalogue to portal to aggregator)

## When DCAT is not the right tool

Avoid using DCAT as the primary model when you need:

- object or item‑level cultural heritage semantics (events, actors, provenance chains)
- rich, domain‑specific modelling (use CIDOC CRM, EDM, domain ontologies, and related models)
- internal operational logs or private configuration (DCAT is a public‑facing catalogue model)

## Core modelling concepts

DCAT is typically used with these classes:

- `dcat:Dataset` as a dataset (conceptual resource)
- `dcat:Distribution` as an accessible form of the dataset (download, API, dump)
- `dcat:DataService` as a service that provides access to data (API endpoints, query services)

Practical rule:

- if you publish an API, model it as a `dcat:DataService` and link it to the dataset or datasets it serves
- if you publish a file download, model it as a `dcat:Distribution`

## Profiles and interoperability baselines

### DCAT‑AP

In EU contexts, DCAT‑AP is a common application profile that constrains DCAT for cross‑portal exchange (mandatory fields, recommended properties, controlled value spaces).
If your catalogue content is intended for broad EU interoperability, adopting DCAT‑AP, or mapping to it, reduces friction.

### Validation

Treat the chosen profile as a contract:

- validate catalogue records using SHACL shapes (recommended)
- version the shapes or profile and publish change notes to avoid silent drift

## Recommended provider checklist

### 1) Stable identifiers

- use stable HTTPS URIs for dataset and service identifiers
- avoid reusing identifiers for different resources
- if a record is replaced, publish a supersession relationship rather than silently overwriting

### 2) Access points are explicit

- for each dataset, list the available distributions (downloads, dumps, derived packages)
- for each service or API, provide an explicit endpoint URL, protocol, and where relevant a machine‑readable contract link (for example OpenAPI)

### 3) Rights and licensing are machine‑readable

- publish licences as standard URIs where possible
- keep rights statements consistent across dataset and distributions (avoid contradictions)

### 4) Restricted access is described without leaking sensitive detail

If a dataset or service is restricted:

- describe the access model at a high level (restricted, authenticated)
- provide enough metadata for validators and integrators to understand expected behaviour
- avoid embedding secrets or internal‑only operational details in catalogue records

### 5) Version and change transparency

For evolving datasets and services:

- publish a version identifier, or immutable release id
- provide a changelog or release notes link
- keep old versions traceable where required by policy

## Common pitfalls

| Pitfall | Why it hurts interoperability | Better pattern |
|---|---|---|
| Only a dataset title and URL | Not enough for harvesting and discovery | Add distribution and service structure plus licence and contact |
| Unstable access URLs | Breaks portals and harvesters | Use versioned URLs or stable redirects with a documented policy |
| Free‑text licence | Cannot be processed reliably | Use a licence URI (CC, ODC, and similar) |
| Mixing item‑level and dataset‑level modelling | Confuses consumers | Use DCAT for dataset and service; use domain models for items |

## References

- DCAT v3 (W3C Recommendation): https://www.w3.org/TR/vocab-dcat-3/
- DCAT‑AP (SEMIC): https://semiceu.github.io/DCAT-AP/releases/
- SHACL (W3C): https://www.w3.org/TR/shacl/
