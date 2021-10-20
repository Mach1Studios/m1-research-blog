---
title: "How is the term \"Spatial Audio\" used by different companies?"
date: 2021-08-11T03:10:05-04:00
---

## What do companies mean when they talk about spatial audio?

Currently this is a very broad question because spatial audio is a subject spanning across disciplines and industries. We could talk about different [flavors of audio spatialization]({{< relref "glossary/general-terms#spatial-audio" >}}), or about the history of spatial audio in academia. What we would like to focus on is the way the consumer electronics industry has most commonly employed the term in recent years, and share some points of clarification based on our years of experience both creating spatial audio experiences and the tools necessary to create them.
  
Sony, Dolby Atmos, and by extension Apple, are all object-based audio style formats and workflows that utilize metadata loosely based on ADM & MPEG-H standards, [more info on differences here]({{< relref "posts/observations-and-limitations-of-dolby-atmos-for-spatial-mixing" >}}). This means that the metadata encoded in each file format follows the similar principles. However, they each differ in syntax and can use proprietary codecs or file handling to decode the metadata in these files. That means that if you play a Sony 360 audio file without a compatible device, you won't be able to decode the metadata within it. We share more on [object-based]({{< relref "glossary/mixing-terms#object-based" >}}) audio [in our glossary.]({{< relref "glossary/mixing-terms#object-based" >}})

Many [object-based]({{< relref "glossary/mixing-terms#object-based" >}}) audio systems are *not* transparent about the [physical modeling or room modeling]({{< relref "glossary/mixing-terms#room-modeling" >}}) involved in the way they make what you're hearing sound like it's inside a space. By [physical modeling]({{< relref "glossary/mixing-terms#room-modeling" >}}), we mean the addition of arbitrary room acoustics. While sound in real life always exists in space and is therefore colored by the room it's in (or the lack thereof), we believe that the addition of such arbitrary room acoustics – whether or not they are customizable – goes against the artistic intention of the mix. As creators of spatial audio mixes, we were careful to develop a spatial audio framework wherein *the technical mix is the creative mix*, more on this can be found in the [Mach1 Spatial SDK](https://www.mach1.tech).

One creative usecase of spatial audio is to re-create the way we hear naturally. Unfortunately, many platforms deliver head-locked experiences and call it spatial audio. In real life, the way you hear something changes as you move your head, so if any company is using the term spatial audio without using headtracking, take it as a sign to look deeper into what's *actually* going on, because it's not really spatial audio. Usually what those companies mean when they refer something as "spatial audio" is a binauralised stereo downmix of a mix that has been created using spatial characteristics or processing.

## [Mach1 Spatial Audio](#mach1-spatial)
We wanted to begin by explaining more clearly what we mean by [spatial audio]({{< relref "glossary/general-terms#spatial-audio" >}}). In our terms, spatial audio refers to audio that is extended in dimension for playback either by leveraging playback of multichannel audiofiles in a space of loudspeakers to create 3D soundfield playback or doing so virtually to headphones by introducing interactivity via orientation or positional data to "adjust" the correct stereo playback of that 3D soundfield. There are many approaches for prerendering spatial soundfields as well as approaches that utilize runtime only spatial soundfield processing. With that in mind we focus on making sure that all these approaches can be used together safely by focusing on tooling for multichannel audio creation and playback create an aggregated framework for all flavors of "spatial audio".

## [Apple Spatial Audio](#apple-spatial)

Currently Apple does not utilize its own spatial audio workflow or format, instead it expects a user to convert any piece of content of any spatial audio flavor into a specific 5.1 mix file type and combined within a video container. On iOS devices if the correct conditions are met the user can utilize orientation data from their AirPods Pro or AirPods Max devices to add headtracking spatial audio playback of the 5.1. This implementation is one of the earliest we have seen on a consumer level for true interactive spatial audio playback, however it is extremely poor in quality and limited in creative use. 

It should be noted that this seems to work for: 
- sideloading 5.1 mixes within specific video containers (as described above)
- several video streaming services such as: "TV, Hulu, Netflix, etc."

However Apple does not yet provide interactive spatial audio for its music streaming services over headphones. While this may change in the future, the essence remains that the music service sends a headlocked stereo binaural downmix of whatever Atmos mix is playing. It appears that use of "spatial audio" within Apple differs from product to product and team to team pretty drastically, we don't want to make any false predictions on unreleased products, but Apple's spatial audio speakers will likely use object-based audio for custom speaker configurations more akin to what we see with the audio object handling in ARKit. Spatial audio for headphones and for speakers are very different sides of the same coin. Though the intended effect is the same, the methods that are used are different.

### Is Apple Spatial Audio spatial audio?

When Apple makes use of head-tracking as an input to their audio spatialization, we can call it spatial audio. If you quantify spatial audio as how we hear naturally then headlocked binaural stereo cannot be considered spatial audio, it is just spatial processing effects. Despite Apple's success at creating a "theater-like" experience with interactive spatial audio, there are some significant drawbacks, such as a lack of compatibility with external IMUs and inability to decode other spatial file formats without creating the custom ability to do so via a third-party API (even with third-party APIs this is highly controlled and limited within iOS SDK and the AVFoundation API). We've created the [Mach1 Spatial SDK](https://www.mach1.tech/developers) to help overcome these problems.

Even if all of Apple's spatial audio were interactive, we would still need to see an end to the use of generic HRTFs to truly obtain interactive spatial audio. The binaural effect output by Apple's spatial audio system is created using head-related transfer functions. This means that Apple's spatial audio system colors the sound with filters representing the way that someone else's ears would hear in some kind of room. Spatial audio should be agnostic to ear shape and size. Of course, in addition to artifacts that damage the sound quality and intended mix, it also means that we won't all hear it as well and that it won't work for everyone. Spatial audio should be democratic to everyone. Hopefully, Apple can open their system just enough to allow spatial audio solutions that preserve the creative mix to benefit from headtracking in their own or other devices with IMUs.

For more on Apple's spatial audio, we have outlined how to sideload and review Apple's spatial audio implementation here: [Previewing Spatial Audio on Apple AirPods]({{< relref "tutorials/previewing-spatial-audio-on-apple" >}})

We have also reviewed the implementation and use of Apple's IMU enabled devices here:
[Feedback on Apple's Spatial Audio Implementation]({{< relref "posts/feedback-on-apple-spatial-audio" >}})

## [Dolby Spatial Audio](dolby-spatial-audio)

Like Sony 360 Reality, Dolby Atmos is not just a format, it is also a production tool. Dolby Atmos is not a codec. It does not itself encode or decode its format. Other Dolby codecs are used to decode the Dolby Atmos format. The Dolby Atmos format uses MPEG-H style of metadata however it does have its own parsed version of this metadata. This means that the Dolby Atmos format is a *container* holding both the file format as well as the object-based metadata.

Dolby Atmos' object-based production allows you to create audio "beds" that are more akin to channels, or larger sound fields. However, you are also able to make discrete "objects" that have their own independent behaviour. Though Dolby Atmos touts the never-done-before ability to pan towards height channels, this is not true. Almost every other spatial audio production suite can do this. Additionally the panning space available within Dolby Atmos is highly limited as discussed here: [Observations and Limitations of Dolby Atmos for Spatial Mixing]({{< relref "posts/observations-and-limitations-of-dolby-atmos-for-spatial-mixing" >}})

Dolby Atmos for physical speaker configurations is interesting but is not an entirely new concept. It's a standard surround sound system but with height information. The cool part is that the "beds" and "objects" can be played no matter what your configuration is – you don't need the traditional setup. However, if you don't have a decent configuration from the get-go, getting something that sounds good might be challenging. One thing to note is that the spatial audio we are talking about with headphones is usually really different from spatial audio for speakers. Spatial audio for speakers cannot have the kind of processing that mimics the way your ears hear within a space because your ears are already doing that!

### Is Dolby Atmos Spatial Audio?

As with everything we've looked at, it depends on the interaction involved. You definitely don't need Dolby Atmos to create spatial audio. When Dolby Atmos uses listener head position or speaker configuration to interactively bring the object-based mix to life, it is spatial audio. Otherwise, we're getting closer but not quite there yet.

Despite Dolby Atmos being an object-based supported audio format it does not include any features for interactive spatial audio of any kind, including typical headtracking binauralized playback. All cases of Dolby Atmos mixes playing back with headtracking headphones spatially, including Apple's implementation of playing back Dolby Atmos on AirPods Pro/Max, are 3rd party playback implementation without any standardization. To put it in other terms, if you are listening to a Dolby Atmos mix with headtracking that was done by some made up way outside of Dolby's approval (and not reviewable by Dolby Atmos Renderer) meaning each time we get a new case of this feature it will sound different from app to app resulting in a completely broken mixing landscape for artists and audio professionals alike. 
  
## [Sony Spatial Audio](sony-spatial-audio)

Sony, like Dolby Atmos, is both a production tool as well as a format using MPEG-H as a standard for encoding object-based metadata. With the Sony Headphones Connect app and a Sony 360 Reality compatible premium streaming service, you can playback 360 Reality content on any device. 

Although the Sony 360 Reality creative software suite is used to create an object-based format where the listener is at the center of a sphere, the end-user ultimately gets a headlocked binaural stereo playback. As we have said time and time again, without interaction (headtracking), you are not experiencing spatial audio. You are instead experiencing a post-production spatial effect.

In the Sony Headphones Connect App, you must take pictures of your ears as well as chose the product you are using. This indicates that Sony uses generic [head-related transfer functions or HRTFs]({{< relref "glossary/general-terms#hrtf" >}}). On top of the inevitably generic HRTFs, Sony will personalize a certain tuning of the spatial effect they are creating. 

When Sony writes that they create a personalized soundfield, you should have a big asterisk going off in your head. Unless you went to get your HRTF specifically measured, it is not your true HRTF. However, it may be better than a completely standard one. The fact that you choose your product also suggests that Sony adds what is called an inverse transfer function which will compensate for the way each type of headphone will uniquely color the sound.  

### Is Sony 360 Reality spatial audio?

While these methods are interesting, they contradict our philosophy on agnostic interactive spatial audio that preserves the creative mix. Until Sony 360 Reality includes interactive headtracking, it is not spatial audio. The only aspects inching their system closer to spatial audio are their inclusion of artists in the creation of an object-based mix, and the use of object-based mixes for custom potentially non-standard speaker configurations.
