---
title: "Observations and Limitations of Apple Spatial Playback Implementation"
date: 2021-09-22T10:10:00-04:00
lastmod: 2021-10-20T10:10:00-04:00
draft: false
---
---
## Introduction

This post is to discuss our internal observations and limitations we found when transcoding to a ingestible 5.1 mix format and container that Apple will apply dynamic headtracking spatial playback for. We have done these tests from a source Mach1 Spatial file and used M1-Transcoder.app to correctly setup a 5.1 file, we have also done the same tests from the Dolby Atmos pipeline and can conclude that the same resulting file could be made from either workflow approach, knowing this we find it much easier to use anything and correctly transcode as needed via M1-Transcoder.app to avoid all the complications and complexities when using Dolby Atmos Master files to create a simple 5.1 file. 

- [Read more on preparing 5.1 mixes for Apple Spatial playback here]({{< relref "tutorials/previewing-spatial-audio-on-apple" >}})
- [Read more on the limitations seen when using Dolby Atmos for spatial mixing here]({{< relref "posts/observations-and-limitations-of-dolby-atmos-for-spatial-mixing" >}})

## Reduced Soundfield Resolution

Some major quality issues are introduced by Apple in an attempt to add headtracking to the resulting 5.1 mix via an object audio implementation, in this section we will go over how the soundfield quality is reduced by poor implementation that could easily be avoided with different technical approaches. 

### Removal of Elevation in Soundfield

This one should be obvious since the mix has been transformed to a flattened 5.1 mix before Apple can use it for headtracking spatial playback. All sources with elevation panning in the mix are flattened to the center plane, the anecdote we want to point out is "why even partner & use Dolby Atmos as the recommended workflow" if at the end all of this will be stripped away. On that note, we want to remind anyone reading how even [Dolby Atmos has extremely limited panning space for "elevation"]({{< relref "posts/observations-and-limitations-of-dolby-atmos-for-spatial-mixing" >}}) despite marketing toward this feature. Anecdotes aside it should be noted that all headtracking related sonic changes from pitching your head up or down while listening to Apple Spatial playback, are not intended by the mix engineer and are an additional processing effect coloring and degrading sound quality of the mix instead of utilizing the mix information available from the audio professional's source material.

<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/observations-limiations-of-apple-spatial/applespatial-panning-1.png" alt="" style="width:50%;display:block;margin-left:auto;margin-right:auto;">

### Shrunken Soundfield Image

Apple's implementation of adding headtracking to playback 5.1 mixes seems to be done by constructing an object-based implementation of the 6 channels with positions of each channel placed as an object around you similar to how it would be in real life with 6 loudspeakers. By doing this they have inherently shrunken the soundfield even further as an object-based system has no divergence, when doing tests (and we plan on adding them to this post) you can hear how the soundfield shrinks when transcoding from source to 5.1, but how it shrinks again when comparing to a virtual (or physical) 5.1 setup when processing through Apple Spatial playback. This is a major hit on quality, and one that no audio professional has any control over or method of mixing for.

<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/observations-limiations-of-apple-spatial/applespatial-panning-2.png" alt="" style="width:50%;display:block;margin-left:auto;margin-right:auto;">

## Added Coloring Processing Effects

Apple's implementation also adds room modeling and HRTF filter processing to help the object-based channels simulate directionality while changing your head orientation. This process discolors the mix on a frequency domain and completely destroys sound quality to help achieve effects like "looking up" _even though we know there is no longer any sources panned with elevation due to the 5.1 transcoding step_. This process is completely unnecessary, any effect of spatial processing gained by this method is largely outweighed by the sound quality no longer having a full frequency range and in general filtered, phasy and tinny artifacts added to it. There is no question that listening to the Dolby Atmos -> 5.1 -> Apple HRTF/Room modeling version of Outkast - Ms. Jackson sounds tremendously worse than the original mix (even when looking forward in both), **and it does not have to be this way at all!**. We can have highly immersive and creative headtracking spatial mixes wihtout any additional processing effects added, in fact that is what [Mach1 Spatial SDK](https://github.com/Mach1Studios/m1-sdk) is for.

An analogy we like to give, is that this seems similar to the early days of 3D movies where we had to wear glasses to view the added "layer" of red blue to the movie to help add a fake sense of "depth" to the screen. While the effect works we all agree that achieving the effect without the glasses is better for quality and for the consumers. So we ask why do the same with added HRTF & modeling processes added on top of the artst or mix engineers work without their disgression? 

## Hardware Issues

### Tilt Sensor Data Issue

We have discussed this in depth (link below) but just want to point out we still hear it in the current implementation.

[Feedback on Apple's Spatial Audio Implementation]({{< relref "posts/feedback-on-apple-spatial-audio" >}})

## What did Apple Do Right?

The point of this post isn't to bash away at missed technical oppurtunity but to ensure anyone can read and learn more about expectations for proper spatial and multichannel audio handling. There are a few things we do want to acknowledge Apple for doing well and more importantly early on.

### Exposing Device Orientation Data via SDK

While this is early on and limited to only the iOS SDK, it is still a great step forward and one that all other companies who manufacture IMU enabled wearable devices NEED to follow. No one company, including Apple, can build or even predict all the use cases of how "headtracking" or "motion tracking" can be used creatively, in fact they shouldn't do so at all (as we see with how Apple Music Spatial Headtracking was implemented). However, exposing how their devices can be used to developers and creative technologists alike allows us all to build these new mediums of spatial audio together and correctly. We really hope to see this `CMHeadphoneMotionManager` API be accessible in macOS and other SDKs to really ensure a proper ecosystem for content creation and for consumers to start properly participating without proprietary roadblocks. 

### Continously Working on Introducing "Spatial Audio" to Consumers

We are happy to see progress made in teaching consumers what spatial audio could be used for as a medium or with other mediums. This is highly encouraging and we hope Apple can look beyond the highly proprietary and technically and creatively limited use of Dolby Atmos they are currently using as their strategy to see how they can engage a much larger audience by not assuming "spatial audio" only means adding "natural sound processing" to a mix. We often see this in first creative uses of "spatial audio" in any form, however we often see that as artists, creatives, users explore "spatial audio" they do not tend to only associate it with "how things can sound more natural" but also start exploring "how to creatively use motion or headtracking to create new forms of media". 
