# MP4 Video Delivery

MP4 is a widely supported container format for digital video and is compatible with major browsers and media players.
For CH collections (interviews, documentaries, digitised films), MP4 is commonly used for dissemination and portal integration.

The codec used inside the MP4 container (for example H.264/AVC or H.265/HEVC) impacts quality, compatibility, and file size.

## When to use MP4

- web delivery and streaming use cases
- embedding videos in web‑based CH tools and exhibitions
- publishing interoperable access derivatives derived from preservation masters

## When not to use MP4

- uncompressed preservation masters (use preservation workflows, codecs, and archival packaging as appropriate)
- high‑resolution film scanning masters where preservation‑specific standards are required

## Interoperability considerations

### Codec choice

- H.264 generally provides the widest compatibility across browsers and devices
- H.265 can reduce file size for similar quality but may have more limited support depending on platform

### Accessibility

Provide captions or transcripts when available:

- captions commonly via WebVTT
- transcripts for discovery and accessibility where captions are not feasible

### Rights and metadata

- ensure rights and licence information is present in the repository record
- if distributing derivatives, record the master source identifier and conversion parameters

## Validation checks

- playback in a reference browser and player (smoke test)
- verify audio presence, sync, and duration
- confirm captions load correctly when provided
- record checksums for published files

## References

- ISO Base Media File Format (basis for MP4): https://www.iso.org/standard/68960.html
- ITU‑T H.264: https://www.itu.int/rec/T-REC-H.264
- ITU‑T H.265: https://www.itu.int/rec/T-REC-H.265
- WebVTT (W3C): https://www.w3.org/TR/webvtt1/
