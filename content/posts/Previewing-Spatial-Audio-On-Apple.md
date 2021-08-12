---
title: "Previewing Spatial Audio on Apple AirPods"
date: 2021-08-12T03:10:00-04:00
---

While investigating how Apple applies their own HRTF and headtracking implementation on top of Dolby Atmos it became appearent that there are a few glaring issues and limitations. It also became clear that we can transcode all formats to playback on Apple devices without use of Dolby Atmos at all, making a much cleaner and direct pipeline if your target is only for headtracking as defined by Apple.

Apple seems to simply expect a video file with an `EAC3` encoded audio track configured as `5.1(side)` and with a specific bitrate and other simple to implement codec settings.

It should be known that the `5.1(side)` then undergoes an arbritrary and frankly sloppy and low quality HRTF process by Apple that drastically shrinks the soundfield range, limits your divergence in the soundfield and results in a low quality and hard to mix for soundfield. Going into further detail about the soundfield limitations: 

#### Limitations & Issues with Apple's Spatial Implementation
_These limitations are based on the date of this written post_
 - 5.1(side) = Left, Right, Center, LFE, Side-Left, Side-Right (L,R,C,LFE,SL,SR)
 - The HRTF process force blends front/back aspects of the soundfield, if you turn around you will still hear the front bleed to 180 yaw orientation, also you will hear the rear bleed into the front. It seems Apple only wants to target a simulated "theatre" instead of opening this up to be applicable to many spatial audio concepts such as Spatial Music, Interactive Spatial Podcasts or any concept that doesn't want the listener to pretend they are in a front-facing theatre (which is nearly all concepts using headtracking spatial audio)
 - The HRTF process heavily colors the intended mix, adding an additional filtering and room modeling process on top of the intended mix also drastically limiting the usage of this technology
 - The headtracking implementation has some glaring issues, tilting head rotates the yaw angle of the mix which is another limitation and technical mistake

Read more about early feedback on [Apple Spatial Implementation here]({{< relref "posts/feedback-on-apple-spatial-audio" >}})

#### How To Listen to Any Spatial Audio Format via Apple's Spatial Implementation

As of version [1.5.10 of Mach1 Spatial System](https://www.mach1.tech/downloads) we have implementated a new `output type` on the `M1-Transcoder.app` it uses our [`m1-transcode`](https://github.com/Mach1Studios/m1-sdk/tree/master/binaries/executables) commandline to transcode to `5.1(side)` and then nicely generates or applies to video and transcodes the codec for direct AirDrop review on your Spatial-supported iOS device.

<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/previewing-spatial-audio-on-apple/applespatialoutput.gif" alt="" style="width:50%;display:block;margin-left:auto;margin-right:auto;">

##### If you are starting with a Mach1 Spatial mix
 - Open `M1-Transcode.app`
 - Input the Mach1 Spatial multichannel wav file
 - Select `Apple Spatial 5.1-side (L,R,C,LFE,SL,SR)` `Output Spatial Format`
 - [optional] Input a video file if you want (otherwise the app will auto-generate a video)
 - Render
 - Airdrop the output .mp4 file to your iOS device and play it natively with AirPod Pro or AirPod Max headphones connected

##### If you are starting with a different spatial audio format mix
 - Use `m1-transcode` commandline tool to transcode from your input format to your `Mach1 Spatial`
 - Open `M1-Transcode.app`
 - Input the Mach1 Spatial multichannel wav file
 - Select `Apple Spatial 5.1-side (L,R,C,LFE,SL,SR)` `Output Spatial Format`
 - [optional] Input a video file if you want (otherwise the app will auto-generate a video)
 - Render
 - Airdrop the output .mp4 file to your iOS device and play it natively with AirPod Pro or AirPod Max headphones connected