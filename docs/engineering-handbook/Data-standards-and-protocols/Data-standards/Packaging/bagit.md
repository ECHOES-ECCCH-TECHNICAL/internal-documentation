# BagIt

BagIt is a packaging format designed to support **fixity and integrity** during transfer and archival ingestion.
A BagIt “bag” contains payload files plus manifests (checksums) and optional metadata, enabling receivers to validate that a transfer is complete and unmodified.

This page provides practical, non‑normative guidance for using BagIt in CH Cloud ingestion and exchange workflows.

## What BagIt is good for

Use BagIt when you need:

- bulk transfer of collections between institutions or systems
- offline exchange (air‑gapped or limited connectivity)
- ingestion packages where integrity verification is required
- a simple, tool‑agnostic way to ensure “what arrived is exactly what was sent”

## When BagIt is not the best choice

BagIt is usually not ideal for:

- dynamic datasets requiring frequent partial updates (bags are snapshot‑oriented)
- interactive or API‑first delivery where files are retrieved on demand
- scenarios where you also need rich machine‑readable relationships, provenance, and workflow semantics (consider RO‑Crate)

## How a bag is structured

A BagIt package is a directory containing:

- `data/` for payload files
- `manifest-<algo>.txt` for checksums of payload files
- `tagmanifest-<algo>.txt` for checksums of tag files (optional but recommended)
- `bagit.txt` and `bag-info.txt` for format metadata and optional descriptive fields

Illustrative layout:

```text
my-bag/
  bagit.txt
  bag-info.txt
  manifest-sha256.txt
  tagmanifest-sha256.txt
  data/
    images/
      obj-12345_master.tif
    metadata/
      obj-12345.jsonld
```

Practical rule: treat the bag as a transfer and ingestion unit.
Your repository or catalogue should still store stable identifiers, licences, and ownership metadata at the record level.

## Recommended practices

### 1) Choose a checksum algorithm

Use a modern algorithm aligned with organisational policy.
SHA‑256 is a common baseline.
Avoid mixing algorithms within the same validation pipeline unless you have a clear reason.

### 2) Include tag manifests

Include `tagmanifest-*.txt` so the receiver can validate that tag files (bag metadata and manifest files) were not altered during transfer.

### 3) Record provenance for the package

In `bag-info.txt` or an additional sidecar metadata file, capture:

- package creator (organisation)
- creation date
- source system or export job identifier
- version or release identifier of the exported dataset
- licence and access notes at a high level

Avoid embedding secrets or personal data in `bag-info.txt`.
Treat it as potentially shareable.

### 4) Use deterministic paths and naming

- keep stable naming conventions and directory structure
- avoid OS‑specific paths, spaces, or ambiguous encodings
- use UTF‑8 consistently

### 5) Don’t silently overwrite bags

If you regenerate a bag for the same dataset:

- publish it as a new release (new bag identifier or version)
- retain a supersession relation (old → new) in your catalogue or repository metadata

## Validation

A BagIt validation run commonly confirms:

- the bag is structurally valid (required files present)
- all payload checksums match the manifests
- tag manifests match, if used
- expected metadata artefacts exist (for example a catalogue record or sidecar metadata)
- the package can be mapped to a stable dataset or resource identifier and version

## Combining BagIt with RO‑Crate

BagIt and RO‑Crate solve complementary problems:

- BagIt answers: files arrived intact (fixity and completeness)
- RO‑Crate answers: files mean something (metadata, relationships, provenance)

A common pattern is:

- produce an RO‑Crate describing the dataset and workflow
- place the RO‑Crate inside `data/` in a BagIt package
- validate fixity with BagIt and validate semantics with RO‑Crate tooling

## References

- BagIt File Packaging Format (IETF RFC 8493): https://www.rfc-editor.org/rfc/rfc8493
