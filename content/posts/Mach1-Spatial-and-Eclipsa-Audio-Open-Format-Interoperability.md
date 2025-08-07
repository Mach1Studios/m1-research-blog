---
title: "Mach1 Spatial and Eclipsa Audio: Open-Format Interoperability"
date: 2024-01-15T10:00:00-05:00
lastmod: 2024-01-15T10:00:00-05:00
draft: false
---

## Introduction

Both Mach1 and Eclipsa share a philosophy of open, platform-agnostic spatial audio, and they complement each other in the production/distribution chain. Mach1 provides a creator-friendly and developer-friendly working framework and a robust SDK for manipulation, while Eclipsa provides a standardized delivery framework for the metadata and codec support. 

By adding Eclipsa/IAMF support from the Mach1 Spatial enabled production pipeline, we unlock powerful workflows that bridge creation and distribution seamlessly. This post explores the potential for integrating these two open-format spatial audio systems to create an end-to-end pipeline that maintains quality while providing maximum flexibility.

## Mach1 as an Intermediate Mix Format

Content creators can use Mach1 Spatial System to produce a multichannel spatial mix that is independent of the final delivery codec. Mach1's format is ideal as a "master" spatial audio container because it carries the fully mixed 3D audio scene with no lossy processing and can be converted later without altering the mix.

Integrating Eclipsa (IAMF) as one of these target formats via an output .iamf with associated metadata would mean you could take a Mach1 mix and transcode it directly to an Eclipsa Audio file for distribution if this deliverable becomes more adopted in end-points.

## Eclipsa as an Import/Export Option

Currently, Mach1Transcode supports a wide range of spatial audio formats – from channel-based surrounds (5.1, 7.1, 7.1.4, etc.), to ambisonics (ACN/SN3D first order, third order, etc.), to various microphone array layouts. It even allows custom configurations defined via JSON files.

By adding IAMF/Eclipsa to the supported format list, Mach1 would allow developers to ingest an Eclipsa file and convert it to Mach1, or conversely take a Mach1 mix and produce an Eclipsa bitstream. 

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

## Open Standards Enable Easier Integration

The IAMF spec is public and a reference implementation is available. This openness is similar to Mach1's own openness (Mach1's methods are published and the SDK is on GitHub).

The result is that a Mach1-Eclipsa integration could potentially cover "all of it" – the entire end-to-end chain in open source:
- **Authoring tools**
- **Intermediate format** 
- **Final consumer format**

Mach1's amplitude-pan approach could even simplify some aspects of Eclipsa authoring. For instance, Mach1's channels could be mapped directly to Eclipsa's channel-based elements or used to derive object trajectories. Since Mach1 is codec-agnostic, it can carry uncompressed or compressed audio which Eclipsa could encode using Opus, AAC, or PCM inside the MP4 (IAMF supports multiple codecs, with Opus being a likely choice for delivery).

## Conclusion

In short, Mach1 Spatial and Eclipsa Audio together enable an open, end-to-end pipeline: Mach1 covers the creation and intermediary workflow and supportive development pipeline, and Eclipsa covers the codec deliverable and final streaming endpoint. This integration would provide content creators with unprecedented flexibility while maintaining the quality and openness that both platforms champion.

The combination of these technologies represents a significant step forward in creating truly platform-agnostic spatial & multichannel audio workflows that can adapt to any distribution pipeline while preserving the creative intent of the original mix. 