---
title: "Observations and Limitations of Dolby Atmos for Spatial Mixing"
date: 2021-08-24T10:10:00-04:00
---

## Introduction
This post is to discuss our internal observations and limitations we found when using Dolby Atmos for a creative spatial audio project. Using Dolby Atmos for front facing projected style content should be discussed separately from this post, we want to only focus on pain points we found when using and comparing Dolby Atmos for full spatial audio mixing and post-production when every direction is important from a first person perspective, not just the front.

## Panning Space
Dolby Atmos contains two components, a channel-based bed component and an object-based bed component. These mix together in the final deliver, we find that most audio content seems to direct the mixes toward the channel-based bed and most decoders tend to futher downmix into different proprietary channel-bed configurations. 

### Half Elevation Vector Space
Something to make note of when using Dolby Atmos is that out of the box for both the object-bed and the channel-bed there is a limited vector space, specifically there is from the "floor" to the "ceiling" since this is originally designed for theater based mixing. That means that when translated to a virtual setting (expectations we would have for `spatial audio` mixing) we face our first observed limitation, we are missing 50% of the virtual mixing space.
<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/observations-limitations-of-atmos-for-spatial/atmos-panningspace-1.png" alt="" style="width:50%;display:block;margin-left:auto;margin-right:auto;">

### Reduced Elevation Spatial Resolution
Further exploration of the designated 2x channels for elevation in the channel-bed Dolby Atmos workflows shows that we have even less of the virtual vector space available for `spatial audio` mixing. Any input sources panned with `>0` elevation starts distributing signal to those 2x elevation channels, meaning there is very little directional isolation for any elevated sources. This seems to really derive from the fact that this system is intended for distributed loudspeaker soundsystems (in theaters), but when we use this for virtual `spatial audio` mixing this is a huge limitation, especially for headphone targeted content.
<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/observations-limitations-of-atmos-for-spatial/atmos-panningspace-2.png" alt="" style="width:50%;display:block;margin-left:auto;margin-right:auto;">

### Channel-Bed Panning and Object-Bed Panning
Having a split system multichannel format might have some advantages, however Dolby Atmos's implementation of this seems to cause more harm than good, we find a lot of user confusion on the panning spaces of the object-bed vs the channel-bed, the UI for tools focused around Dolby Atmos tends to lead a user to believe they are different, but they seem to have the same end effect after runtime playback. We also find that having this split causes a ton of issues for developers building interpretations of playback, the fact that it is left open ended around a proprietary and unforgiving channel-bed shape, combined with an object-bed that should be more straightforward but is not, and in fact requires proprietary runtime room modeling processes; will cause a fractured playback landscape for just Dolby Atmos content.

### UI Issues
We have seen some confusion from audio professionals using Dolby Atmos and their own developed UI, these might be minor but have cause massive loss of confidence during mixing and producing stages.

Some examples: 
- The Dolby Atmos Renderer UI has a larger distance in front/back display than the panners or Music Panner, this has cause confusion while mixing, expecting alterations in front to back sound panning relationships when it is just a mistake in the UI draw (yet another holdback from the theater workflow). 
- The non-theater UI in the Dolby Atmos Renderer shows a negative elevation space whne there in fact Dolby Atmos does not support this in panning.

## Distribution

### Proprietary Metadata
Another UX pain point we found was that while Dolby Atmos tends to follow the recommended structure of the opensource [ADM](https://adm.ebu.io/) but has its own written metadata that requires developers to build multiple parsers or interpreters. [ADM](https://adm.ebu.io/) or [Audio Definition Model](https://adm.ebu.io/) is a standardised metadata model for audio, ideally for any format or custom implementation that needs to further describe what each channel of audio represents (for example object audio formats). We have been working on conversion tools for all object audio formats and find this to be an unnecessary pain point by having a proprietary metadata style within the `.atmos` and `.atmos.metadata` files.

### File Size
All said and done a user can expect to deliver a Dolby Atmos Master file that includes double to triple digits of audio channels, even when only a few of those channels actually contain audio data. We have found that just any object layer will require the format to zero out the entire length of the project an empty audio channel, this is a *tremendous* increase in file size for no benefit at all. There can be a ton of optimizations made in this field, but even if all those were applied we are still discussing a channel-based multichannel format that has more channels and less directional soundfield resolution than any other pre-rendered `spatial audio` format existing.

We plan on expanding on this post with file size examples compared to spatial soundfield resolution.