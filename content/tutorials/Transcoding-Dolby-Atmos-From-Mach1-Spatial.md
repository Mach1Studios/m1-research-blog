---
title: "Transcoding Dolby Atmos From Mach1 Spatial"
date: 2021-10-20T03:10:00-04:00
---

---
To help encourage more agnostic mixing options for all kinds of multichannel and spatial audio formats and not encourage users to start their mixing process in a limiting format such as Dolby Atmos. We have been working on the best practices for conversion to/from Dolby Atmos and ADM metadata based formaats. 

This tutorial is to help as a starting point for anyone to test out converting to Dolby Atmos, the tutorial will focus on conversion from Mach1 Spatial, however you can safely convert to the Mach1 Spatial vector container easily from any other format transparently via the commandline tools and Mach1 Spatial SDK & Mach1 Spatial System in various ways.

While this is currently a new emerging multichannel deliverable format that we all should be prepared for, we have outlined the issues of pain points of using Dolby Atmos for non-theatre mixing and as a spatial audio pipeline in the following posts: 

- [Read more on the limitations seen when using Dolby Atmos for spatial mixing here]({{< relref "posts/observations-and-limitations-of-dolby-atmos-for-spatial-mixing" >}})
- [Read more on the limitations of Apple Spatial Playback Implemetation here]({{< relref "posts/observations-and-limitations-of-apple-spatial-playback-implementation" >}})
- [Read more on preparing 5.1 mixes for Apple Spatial playback here]({{< relref "tutorials/previewing-spatial-audio-on-apple" >}})
- [Read more on Initial Feedback on Apple Spatial Audio]({{< relref "posts/feedback-on-apple-spatial-audio" >}})

#### Using M1-Transcoder GUI App to Transcode from Mach1 Spatial to Dolby Atmos (7.1.2 ADM Channel-Bed)

- Open [M1-Transcoder](https://www.mach1.tech/spatial-system#transcoder)
- Input your Mach1 Spatial Mix as the `INPUT SPATIAL AUDIO` 
- Select `7.1.2 ADM / Dolby Atmos Channel-Bed (L, R, C, LFE, Lss, Rss, Lrs, Rrs, Lts, Rts)` as the `OUTPUT SPATIAL FORMAT`
- Name and render the output file _(result will be a single .wav with injected ADM metadata)_

<img src="https://mach1-research-public.s3.amazonaws.com/tutorials/resources/input-mach1spatial.gif" alt="" style="width:50%;display:block;margin-left:auto;margin-right:auto;">

#### Use Dolby Atmos Conversion Tool to Convert ADM .wav to .atmos files

- Open [Dolby Atmos Conversion Tool](https://developer.dolby.com/forms/dolby-atmos-conversion-tool/)
- Drag and Drop in the .wav ADM output from M1-Transcoder
- Select `.atmos` File Format and any other relevant settings
- Convert _(output will be 3 or 4 files that must be kept together)_

<img src="https://mach1-research-public.s3.amazonaws.com/tutorials/resources/convert-from-adm-to-atmos.gif" alt="" style="width:50%;display:block;margin-left:auto;margin-right:auto;">

#### Use Dolby Atmos Renderer for Playback Previewing

- Open [Dolby Atmos Renderer](https://professional.dolby.com/product/dolby-atmos-content-creation/dolby-atmos-renderer/)
- File>Open Master File
- Select `.atmos` file output from the Dolby Atmos Conversion Tool _(all .atmos files from the Conversion Tool need to be in the same folder to open the Master files)_
- Press Play

<img src="https://mach1-research-public.s3.amazonaws.com/tutorials/resources/atmos-playback-test.gif" alt="" style="width:50%;display:block;margin-left:auto;margin-right:auto;">
