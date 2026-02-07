# Audio Formats

Audio assets in cultural heritage contexts commonly include oral histories, interviews, music recordings, and sound archives.

A typical interoperability pattern is:

- keep a **preservation master** in a lossless format (WAV/FLAC), and
- publish **access derivatives** in efficient delivery formats (MP3/AAC).

This page provides **practical, non-normative** guidance for CH Cloud workflows.

## When to use WAV, FLAC, MP3, AAC

### Preservation masters

- **WAV**: uncompressed PCM; broadly supported; large files.
- **FLAC**: lossless compression; reduces storage while preserving fidelity.

### Access delivery

- **MP3**: very broad compatibility; suitable for web playback.
- **AAC**: strong quality/bitrate trade-off; common in MP4/M4A ecosystems.

## When not to use them

- Avoid MP3/AAC as the *only* long-term master when high-fidelity preservation is required.
- Avoid distributing WAV/FLAC directly for web streaming at scale unless your delivery infrastructure supports large transfers efficiently.

## Interoperability considerations

### Metadata and rights

Capture and publish (at least):

- creator
- date
- rights/licence (prefer URIs)
- source
- language (for spoken-word content)
- duration
- technical metadata: codec, sample rate, bit depth, channels

If embedded tags exist (e.g., ID3, Vorbis comments), extract and preserve them in repository records and/or the metadata store you expose for exchange.

### Accessibility

For spoken-word content, consider transcripts and/or captions where feasible to support:

- accessibility
- discovery (search)
- downstream NLP workflows

## Validation checks

- File readability and codec identification.
- Duration and sample rate checks (sanity vs. expected).
- Rights/licence present in the metadata record.
- If derivatives exist: confirm mapping to the master version and record conversion parameters.

