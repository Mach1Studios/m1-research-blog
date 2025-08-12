---
title: "Mach1 Spatial and Eclipsa Audio: Open-Format Interoperability"
date: 2024-01-15T10:00:00-05:00
lastmod: 2024-01-15T10:00:00-05:00
draft: false
---

## Introduction

Both Mach1 and Eclipsa share a philosophy of open, platform-agnostic spatial audio, and they complement each other in the production/distribution chain. Mach1 provides a creator-friendly and developer-friendly working framework and a robust SDK for manipulation, while Eclipsa provides a standardized delivery framework for the metadata and codec support. 

By combining Eclipsa/IAMF support with a Mach1 Spatial enabled production pipeline, we unlock powerful workflows that bridge creation and distribution seamlessly. This post explores the potential for integrating these two open-format spatial audio systems to create an *end-to-end* pipeline that maintains quality while providing maximum flexibility.

## Mach1 as an Intermediate Mix Format

Content creators can use Mach1 Spatial System to produce a multichannel spatial mix that is *independent of the final delivery codec*. Mach1's format is ideal as a "master" spatial audio container because it carries the fully mixed 3D audio scene with *no lossy processing* and can be converted later without altering the mix.

Integrating Eclipsa (IAMF) as one of these target formats via an output .iamf with associated metadata would mean you could take a Mach1 mix and transcode it directly to an Eclipsa Audio file for distribution if this deliverable becomes more adopted in end-points.

**Why this matters for creators:** This workflow lets you treat `Mach1Spatial-8` as your *RAW audio format* — keeping every detail until the very last moment, so *no creative compromises* are made in early production.

## Eclipsa as an Import/Export Option

Currently, Mach1Transcode supports a wide range of spatial audio formats – from channel-based surrounds (5.1, 7.1, 7.1.4, etc.), to ambisonics (ACN/SN3D first order, third order, etc.), to various microphone array layouts. It even allows *custom configurations* defined via JSON files.

By adding IAMF/Eclipsa to the supported format list, Mach1 would allow developers to ingest an Eclipsa file and convert it to Mach1 Spatial, or conversely take a Mach1 Spatial soundfield and produce an Eclipsa encoded bitstream. 

### Example API Usage

```
m1Transcode(inFile="mix.wav", inFmt="Mach1Spatial-8", outFmt="IAMF", outFile="immersive.mp4")
```

Under the hood, Mach1 would package the 8-channel Mach1 mix into the IAMF structure inside an MP4 container.

The reverse would also be hugely beneficial:

```
m1Transcode(inFile="spatial.mp4", inFmt="IAMF", outFmt="Mach1Spatial-8", outFile="mix.wav")
```

This would extract the audio into Mach1's working format for further editing or real-time decoding. This kind of two-way interoperability would bridge content from the open distribution format (Eclipsa) into the production/workflow format (Mach1) seamlessly.

## How They Differ but Complement Each Other

<style>
/* Scoped table styles for this post only */
.comparison-table { margin: 1.25rem 0; }
.comparison-table table { width: 100%; border-collapse: collapse; border: 1px solid var(--line); }
.comparison-table thead th { background: var(--background-darker); font-weight: 600; }
.comparison-table th, .comparison-table td { padding: 0.6rem 0.9rem; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }
/* Add vertical column separators */
.comparison-table th:not(:last-child), .comparison-table td:not(:last-child) { border-right: 1px solid var(--line); }
.comparison-table tbody tr:nth-child(odd) { background: rgba(255,255,255,0.02); }
.comparison-table tbody tr:hover { background: rgba(255,255,255,0.04); }
@media (max-width: 768px){ .comparison-table table { display: block; overflow-x: auto; white-space: nowrap; } }
</style>

<div class="comparison-table">

| Feature        | Mach1 SDK (Production)              | Eclipsa/IAMF (Distribution)       |
|:---------------|:------------------------------------|:----------------------------------|
| Primary role   | Intermediate “master” format        | consumer playback format option    |
| Focus          | Creator workflow, editing, routing, development & decode control  | Standardized packaging, compatibility |
| Audio data     | Uncompressed or custom-encoded      | Codec-based (Opus, AAC, PCM)      |
| Openness       | SDK + open documentation            | Public spec + reference implementation |
| Metadata       | Flexible channel mapping, amplitude panning | Structured IAMF metadata for spatial elements |

</div>

## Open Standards Enable Easier Integration

The IAMF spec is public and a reference implementation is available. This openness is similar to Mach1's own openness (*Mach1's methods are published and the SDK is on GitHub*).

The result is that a Mach1-Eclipsa integration is an example of covering "all of it" – the entire end-to-end chain in open source:
- **Authoring tools**
- **Intermediate format** 
- **Final consumer format**

Mach1's amplitude-pan approach could even simplify some aspects of Eclipsa authoring. For instance, the Mach1 Spatial channels could be mapped directly to Eclipsa's channel-based elements or used to derive object trajectories. Since Mach1 is *codec-agnostic*, it can carry uncompressed or compressed audio which Eclipsa could encode using Opus, AAC, or PCM inside the MP4 (IAMF supports multiple codecs, with Opus being a likely choice for delivery).

```mermaid
%%{init: {'theme': 'dark', 'flowchart': {'curve': 'basis'}} }%%
flowchart LR
  subgraph Prod["Production (Mach1)"]
    A(Capture)
    B(Mix in Mach1Spatial)
    C(Master in Mach1Spatial-8)
    A --> B --> C
  end

  subgraph Dist["Distribution (Eclipsa / IAMF)"]
    D(Transcode to IAMF)
    C --> D
  end

  subgraph Playback["Playback"]
    E(Mach1Decode API Playback)
    F(IAMF Decode Playback)
    D --> E
    D --> F
  end

  classDef m1 fill:#0f172a,stroke:#60a5fa,stroke-width:2px,color:#e5e7eb;
  classDef iamf fill:#111827,stroke:#34d399,stroke-width:2px,color:#e5e7eb;
  class A,B,C,E m1;
  class D,F iamf;
  ```

## Conclusion

In short, Mach1 Spatial and Eclipsa Audio together enable an open, end-to-end pipeline: Mach1 covers the creation and intermediary workflow and supportive development pipeline, and Eclipsa covers the codec deliverable and final streaming endpoint. This integration would provide content creators with unprecedented flexibility while maintaining the quality and openness that both platforms champion.

The combination of these technologies represents a great example in creating truly *platform-agnostic* spatial & multichannel audio workflows that can adapt to any distribution pipeline while *preserving the creative intent* of the original mix. 

## Future Research Directions

We see huge potential here, but also recognize there’s work to do. In upcoming research, we aim to:

- Test IAMF encoding pipelines as soon as their tools resolve current implementation issues.
- Investigate whether Eclipsa’s renderer has processing options that could be useful for creators.
- Evaluate whether IAMF can faithfully render a `Mach1Spatial-8` mix without losing detail.
- Publish listening examples comparing Mach1 masters with IAMF renders for the community.