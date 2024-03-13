---
title: "Microphone Arrays and Vector Based Soundfields"
date: 2024-03-12T15:10:05-04:00
lastmod: 2024-03-12T15:10:05-04:00
---

## Introduction
This post is an account of multi-mic arrays commonly used for ambisonics and what was discovered when encoding them into a vector based or channel-based multichannel configuration such as Mach1 Spatial (14ch or 8ch).

## Challenges

### Capsule Layout Description
Finding, discovering or measuring the capsule arrangement and ordering precisely since most of the time we will be skipping over the manufacturers conversion software as they tend to only target ambisonic encoding/decoding.

Some manufacturers will nicely describe the layout and by using a visual tool to reference it we only have to confirm the angle descriptions (left handed/right handed polar, or order and meaning of Euler X Y Z).

### Divergence and Ideal Encoding Settings

Currently we are doing tests to figure out what are the ideal ways to encode a multi-mic array directly into a vector based or channel-based spatial audio container while avoiding ambisonics.

Explorations are staged between fully diverged calculations and partially divereged calculations as [seen here](https://github.com/Mach1Studios/m1-sdk/commit/f2681562dc937557babe65d1129833906657976f). 

#### Method

Currently we are using [this commandline tool](https://github.com/Mach1Studios/m1-sdk/tree/master/examples/mach1spatial-c/commandline/spatial-encode-example) to calculate each capsules encode coefficients. 

#### Results

TBD

## Examples

#### Zylia ZM-1
Provides nice [documentation](https://www.zylia.co/white-paper.html), we used the Spherical (or commonly known as Polar) coordinates which is right handed (inversed azimuth values when inputting to the M1-SDK).

<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/micarrays/zylia_zm-1.png" alt="Zylia ZM-1" style="width:75%;">

#### Core Sound OctoMic
Had less documentation on the ordering and position of the capsules, a user has shared unofficial mapping and 3D rendering of the placement (special thanks to @Sam Hocking).

<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/micarrays/coresound_octomic.png" alt="CoreSound OctoMic" style="width:75%;">
