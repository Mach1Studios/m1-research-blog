---
title: "4. Existing Systems, methods, and formats of Spatial Audio"
---

## Pre-rendered Spatial Audio Formats

### [Mach1 Spatial](../existing-formats#mach1-spatial)
Mach1 spatial audio is an effect-process free and transparent container that introduces interactivity to unlock creative freedom for audio professionals and developers for scalable and customizable soundfield pipelines. This framework allows all the other flavors of “spatial audio” to be safely added on top of a simplified and modular spatial audio framework, and ensures that traditional post-production pipelines are preserved as new mediums are invented.

Mach1 is a VVBP system (Virtual Vector based panning system). VVBP is a useful method because it does not use effects that produce damaging artifacts in an artistic mix. There is no timbral effect on the mix, meaning the frequencies do not change and the quality of audio isn't altered in any way. Mach1 was born to meet the criteria for the preservation of professional audio standards and best practices in a medium where quality of sound is critical for maintaining immersion. The system is contained into a single multichannel deliverable through already existing audio containers and codecs. The system supports both head-tracked 3DOF spatial audi as well as 6DOF when integrated into a 3D Game Engine. It does not require any audio library or media engine and can function fully on top of any existing audio system/engine. The Mach1 system takes all traditional post-production practices and allows them to be deployed for interactive mediums such as VR, AR, MR and installations. 

Mach1 Spatial is a "universal delivery format" because it handles multiple multichannel and spatial audio formats and configurations, as well as conversions between them and stereo conversions both with and without head-tracking. This system allows for full down mix and up mix control without any abstract layers of ''encoders'' and ''decoders'' (data conversion processes). The framework simplifies spatial/multichannel audio to allow the development of custom multichannel configurations allowing backend development control to speaker configurations. The control over custom audio pipelines creates a futureproof solution as new mediums emerge. 
---

### [Ambisonics](../existing-formats#ambisonics)

Scene-based spatialisation represents an audio scene from a first-person perspective. The most common example of scene-based spatialisation is #Ambisonics, a technology that was developed in the 1970s and has since been used as one of the dominant spatialisation techniques. It's popularity stems from its use within academia rather than from its quality and ease of use from an industry perspective.

Scene-based spatialisation usually entails placing a listener at the center of a sphere or comparable 3D shape. Ambisonics are created using spherical harmonics and complex mathematics. They are referred to in 'orders', which means how many channels are output, corresponding to the "resolution" of the spatial image. 

While every system we have detailed has drawbacks, ambisonics are particularly tricky when it comes to playback in a real, physical space. It  can only be properly experienced within a few inches of a centerpoint and if not calibrated correctly will be perceived incorrectly. It is quite costly to render ambisonics with a high resolution for this reason. High resolution ambisonics, or HOA (High Order Ambisonics), begins at the 3rd order (16 channels). 

While ambisonics may be useful for some, such as those in academia with higher-order systems available, we ultimately do not recommend ambisonics as a spatialisation method. It can be great when used intelligently as a technique used to achieve something specific, such as a naturalistic soundscape, however it is not an approach to spatial audio that fits most forms of content. 

Once again, with ambisonics, we encounter the issue of whether the content was recorded using a spatial or ambisonic microphone or not. 
Using an ambisonic microphone is great if you want to have a quality ambisonic mix, however most ambisonic microphones are expensive and low in resolution and become limiting when used for creative mixing. 
When converting another kind of recording to ambisonics, we end up losing a lot of the frequency information (the mix essentially gets destroyed), and often we lose a lot of directional information as well (blurry sense of localisation, or confusions). 

For industry creators, ambisonics lack the creative freedom and dramatic flair required of entertainment mediums. Formats invented with content creators in mind, such as Mach 1, offer solutions that overcome many of the problems found in scene-based systems. 

---

### [Game Engine Object Audio](../existing-formats#game-engine-object-audio)

Object-based audio is a good example of a spatialisation method that *lends itself* to interactive content, or head-tracked spatial audio.

**Object-based audio refers to a system that sums together audio-objects at runtime/playtime.** This is a commonly used format that is growing in popularity due to its ability to assemble mixes for different configurations in real time, rather than having to create a new mix for each configuration, as seen in [[1. Channel-based]]. We see this approach used all the time in game audio (game engines function using object-based audio), as well as proprietary systems such as Dolby Atmos #DolbyAtmos. Wave-field synthesis (WFS) is also a type of object-based spatialisation, but not one commonly used in the industry.

**In object-based audio, metadata from your audio format tells your rendering system where objects are and when they play, depending on the audio delivery system you are using.** Object-based audio is easily made interactive, which may sound great (and it is!), but it has inherent tradeoffs.

Because object-based audio is a runtime solution (you program rules and it plays by the rules when a user uses it), it can sound different depending on what the user does and how well the rules were designed. However, there is never a complete post-production pipeline, which can remove some essential elements from a mix, and make it difficult to control your listener's experience.

---

### [Apple Spatial Audio](../existing-formats#apple-spatial-audio)

While Apple is developing their own spatial audio formats and engines, as well as production tools, they currently offer a version of head-tracked and head-locked Dolby Atmos as "spatial audio".
Apple's spatial audio is currently highly feature and use-case driven. The process used for spatialisation differs between these applications. For example, the head-tracked Dolby Atmos output from Apple TV undergoes a different process than Apple Music spatialisation to a certain extent. Apple Music spatial audio tracks have all had to be "re-engineered" using Dolby Atmos. On one hand, this has the benefit of ensuring that the spatial mix that is released is more closely related to what the producer intended you to hear. On the other hand, it creates the problem wherein it has become common for people to think that Apple Music Dolby Atmos is the be-all and end-all of spatial audio.
Dolby Atmos is not spatial audio. Dolby Atmos is an object-based method of audio rendering, making it a useful tool for spatial audio. It would be unexpected for Apple to continue using Dolby Atmos, especially as Apple must add an extra layer of processing and filtering in order to create the binaural effect. It will certainly not be used for all applications, as it would not be necessary to use their Dolby Atmos license for spatialised calls and notifications, and related auxiliary functions. 

On the developer side, Apple has some spatial audio features such as #HRTFs and binaural room impulse responses, all of which are at odds with our vision of what spatial audio should be. Using developer tools, it is possible to develop spatial audio applications for Apple devices containing #IMU's.  The latest WWDC showed another audio engine called PHASE which can also be used for spatial and interactive audio. 
---

### [Facebook Spatial Audio](../existing-formats#facebook-spatial-audio)

Facebook's spatial audio is part of their 360 Spatial Workstation. The system was bought by Facebook from Two Big Ears. They feature production tools that can be encoded with platform-specific metadata. It's focus is on playback within a specific application. The framework places a listener at the center of a sphere and uses panning within that sphere. Early and late room reflections are also available. In this sense, Facebook 360 uses a room modelling based approach. This is consistent with the research produced by Facebook Reality Labs, as their agenda focuses on users having a sense of shared space. 
Like Mach1, the essence of the tools from a user perspective are controlled via plugins in a Digital Audio Workstation. Unlike Mach1, Facebook spatial audio not only relies on room modelling (a somewhat arbitrary method of spatialisation due to the assumptions built on room characteristics) but also on HRTFs and ambisonics. Ambisonic recordings are not a prerequisite to use the tools at all, but their workflow prioritizes an ambisonic approach to audio spatialisation.


---

### [Dolby Spatial Audio](../existing-formats#dolby-spatial-audio)

Dolby Atmos is a proprietary production software suite that follows the [[2. Object-based]] method of creating spatial audio ideal for a Dolby Atmos speaker configuration, but due to its object-based approach is configuration agnostic. One of the distinguishing factors when compared to other surround sound formats is its use of height information. Like MPEG-H, Dolby Atmos does not store its information in channels. It is rendered in real-time using metadata containing X, Y, and Z information. Dolby Atmos for headphones is another application available on certain hardware platforms, which will render Dolby Atmos with head-tracking (the audio is rendered in real-time according to your head position). Some people commute to work by train, others take the bus. Despite the coverage Dolby Atmos has received due to their partnership with Apple, it is not the only tool used by spatial audio creators. 
For more information on Dolby Atmos, refer to [[2. Object-based]] 

---

### [THX Spatial Audio](../existing-formats#thx-spatial-audio)
While Mach1 Spatial and Facebook 360 are focused on the creation of spatial audio, THX offers an entirely different perspective and should not be compared. THX is an end-user solution that is marketed to enhance a gaming experience. We haven't seen any head-tracked spatial audio coming from THX. Our best description of THX is a post-processing chain of binaural filters and equalisation designed for listening to specific parts of a gaming soundscape. THX falls into the "virtual surround sound" category, but with more expansive calibration. Besides EQ, the two main spatial audio features they offer are virtual rendering of 7.1 surround sound and binauralized up-mixed version of standard stereo content. 
At Mach1, we believe in preserving the high quality audio that sound designers, composers, and engineers worked expertly to create. While it is surely an entertaining feature, it is important to note that the methods THX use to spatialise audio are ultimately destructive to the creative mix.  

---

### [High Fidelity Spatial Audio](../existing-formats#high-fidelity-spatial-audio)
High Fidelity is a spatial audio company that evolved as a pivot from social VR. Early beta versions demonstrated High Fidelity as an online platform with a 2D top-down view that featured spatial audio for the purpose of hosting, for example, simultaneous DJ sets that you could move your 2D avatar around the 2D space to discover. So 2D visuals, 3D audio. Recently, High Fidelity has offered themselves as a spatial audio integration tool for networked environments. Their spatial audio processing is geared for WebRTC (Web real-time communication). That makes their tools great for real-time voice over IP solutions with low latency and effective spatialisation. While their tools are interesting, they are not made for creators to produce spatial audio content by any means. 

---