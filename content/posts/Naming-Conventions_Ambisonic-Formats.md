---
title: "Naming Conventions: Ambisonic Channel Formats"
date: 2023-11-28T10:10:05-04:00
lastmod: 2023-11-28T10:10:05-04:00
---

## Introduction
This post explores publically described ambisonic nomenclature and dives into the terms proposed meaning and afterwards we share our opinion on these terms and how they may be more harmful than helpful to helping the community at large understand spatial audio.

Within the ambisonic nomenclature there is scattered usage of various terms named [n]-format; they tend to try to describe nuances and differences in how the multichannel arrangement describes a fully spherical soundfield; however in our opinion we find that often these terms describe non-ambisonic concepts and create an issue where many users cannot differentiate ambisonic spherical harmonic content and more innate channel-bed or multichannel content. We will try to explain each of these terms we have discovered and give an opinion on how often we find users using the terms correctly or not as well as our suggestions on potentially better terminology, however we hope to open the floor in regards to the most succinct terminology and invite others to contribute to our evolving [/glossary]({{< ref "/glossary" >}} "Glossary").

## Terms

#### [A-Format]({{< ref "/glossary/technical-terms#a-format" >}} "A-Format")
This term seems to be largely focused on multi-mic arrays where the mics are typically spaced equally around a central point to be best used for capturing an equal multi-directional soundscape from a single point of origin. This term is largely used in the audio engineering and marketing worlds to signal a multi-mic array designed for encoding into B-Format ambisonics domain. We have seen a lot of confusion around this term as it misleads the user to believe the mics are directly in the ambisonic domain and can make "encoding/decoding" to and from ambisonics hard to understand.

[**Is not ambisonics**: multichannel source]

#### [B-Format]({{< ref "/glossary/existing-formats#ambisonics" >}} "B-Format")
This is a catch all term for when any audio input is encoded into the spherical harmonic ambisonic container, this is simply a synonym for the common usage of "ambisonic".

[**Is ambisonics**: ambisonic encoded source]

#### [T-Format]({{< ref "/glossary/technical-terms#t-format" >}} "T-Format")
This is a suggested format that generally tends to describe multichannel arrangements when each is represented as equidistant from its neighbor channels, typically platonic solids and various 3D shapes having their vertices or faces represented by channels. Commonly also refers to a channel-bed vector based format such as Mach1 Spatial or SPS.

[**Is not ambisonics**: multichannel source]

#### [P-Format]({{< ref "/glossary/technical-terms#p-format" >}} "P-Format")
This is a suggested term for a multi-array multichannel format where each channel represents a location of audio represented in a cardioid or other microphone pickup pattern, we have seen this term describing more complex multi-mic arrays such as the EigenMike which contains 32 channels. This seems largely synonymous with A-Format but typically is describing a mic that is more than 4 channels.

[**Is not ambisonics**: multichannel source]

##### Other mentioned "Formats"
These formats are mentioned or lightly documented but for the most part are deprecated and not used or even referred to in the spatial audio communities.

#### [C-Format]({{< ref "/glossary/technical-terms#c-format" >}} "C-Format")
A proposed and largely not used format which decodes stereo mixes from an ambisonic source and combines them with ambisonic channels for further decoding if the playback method supports it. Essentially hybrid-ambisonics ensuring the first two channels are traditional stereo for safer support.

[**Is partially ambisonics**: 2x channels are decoded from ambisonics the rest of the channels replicate ambisonic domain concepts to replicate the source ambisonic material]

#### [D-Format]({{< ref "/glossary/technical-terms#d-format" >}} "D-Format")
A proposed format for decoding from an ambisonic source.

[**Is not ambisonics**: multichannel decoding from an ambisonic source]

#### [E-Format]({{< ref "/glossary/technical-terms#e-format" >}} "E-Format")
A proposed format for decoding from an ambisonic source, not really documented at all.

[**Is not ambisonics**: multichannel decoding from an ambisonic source]

#### [G-Format]({{< ref "/glossary/technical-terms#g-format" >}} "G-Format")

[**Is not ambisonics**: 5.1 multichannel decoding from an ambisonic source]

##### Suggestion
We think these terms have caused harm and misinformation to the spatial audio community by making it unclear when something is or is not actually within the ambisonic domain and also misleading creators and recordists to think their mic arrays are limited to the ambisonic domain when in fact all these mic arrays can be used in many other ways and methods. When we ask around our community about A-Format and B-Format terminology we find that most audio professionals believe they are both strictly ambisonics and are not aware of the nuances behind the terms which causes technical issues and limits creative usage.

**We suggest reducing the usage of these terms to help audio professionals and developers understand that any multi-mic or multichannel audio file needs to be "encoded" into the ambisonic spherical domain before it is referred to as ambisonics.**

## Sources

- [ambisonic.info channel formats page](https://ambisonic.info/ambisonics/channels.html)
- [blueripplesound notes page](https://www.blueripplesound.com/notes/bformat)
- [ambisonic wikipedia page](https://en.wikipedia.org/wiki/Ambisonics)