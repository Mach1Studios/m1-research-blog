---
title: "4. Existing Systems, methods, and formats of Spatial Audio"
---

## Deliverable Spatial Audio Formats
---

### [Mach1 Spatial](../existing-formats#mach1-spatial)

##### Type: Channel-Based Audio

Mach1 Spatial acts as a universal delivery format by safely handling or ingesting all surround, multichannel and spatial audio formats and configurations, as well as conversions between them and stereo conversions both with and without head-tracking. This system allows for full down-mix and up-mix control without any proprietary steps or protected abstract layers allowing full control of the spatial or multichannel audio from end to end. The framework simplifies spatial and multichannel audio to encourage the development of custom multichannel configurations allowing backend development control to any target on any platform. Mach1 Spatial effect-process free framework can also be used to easily introduce interactivity and unlock creative freedom for audio professionals and developers for scalable, customizable and futureproofed soundfield pipelines. The goal of Mach1 Spatial is to allow all the other flavors of “spatial audio” to be safely added on top of a simplified and modular spatial audio framework, and ensures that traditional post-production pipelines are preserved as new mediums are invented.

Mach1 Spatial is a VVBP system (Virtual Vector based panning system). VVBP is a useful method because it does not use effects that can produce damaging artifacts in an artistic mix. There is no timbral effect on the mix, meaning the frequencies do not change and the quality of audio isn't altered in any way. Instead Mach1 Spatial acts as a framework for correctly assembling, translating and containing spatial soundfields with full transparency and ease of use. Mach1 Spatial was born to meet the criteria for the preservation of professional audio standards and best practices in a medium where quality of sound is critical for maintaining immersion. The system is contained into a single multichannel deliverable through already existing audio containers and codecs and does not require use of any additional metadata or complex processing, all of the spatial soundfield information is within the audio data. The system supports both head-tracked 3DOF spatial audi as well as 6DOF when integrated into a 3D engines. It does not require any proprietary audio library or media engine and can function fully on top of any existing audio system/engine.

Mach1 Spatial is a "universal delivery format" because it can safely handle or ingest all surround, multichannel and spatial audio audio formats and configurations, as well as conversions between them and stereo conversions both with and without head-tracking. This system allows for full down-mix and up-mix control without any private or protected abstract layers allowing full control of the spatial audio from end to end. The framework simplifies spatial/multichannel audio to allow the development of custom multichannel configurations allowing backend development control to speaker configurations. The control over custom audio pipelines creates a futureproof solution as new mediums emerge.

---

### [Ambisonics](../existing-formats#ambisonics)

##### Type: Ambisonics / Scene Audio

Scene-based spatialisation represents an audio scene from a first person perspective. The most common example of scene-based spatialisation is [ambisonics](../mixing-terms#scene-based), a technology that was developed in the 1970s and has since been used as one of the dominant spatialisation techniques. It's popularity stems from its use within academia rather than from its quality and ease of use from an industry perspective.

[Scene-based](../mixing-terms#scene-based) spatialisation usually entails placing a listener at the center of a sphere or comparable 3D shape. [Ambisonics](../mixing-terms#scene-based) are created using spherical harmonics to help summarize data from a specific direction, this process of summarizing data from a direction can be increased in quality and accuracy by increasing the number of associated channels to summarize from. This process of increasing the number of channels is referred to as increasing the 'order', which means how many channels are are used to correspond to the "resolution" of the spatial image. 

[Ambisonics](../mixing-terms#scene-based) are particularly tricky when it comes to playback in a real, physical space. It can only be properly experienced within a few inches of a centerpoint and if not calibrated correctly will be perceived incorrectly. It is quite costly to render ambisonics with a high resolution for this reason. High resolution ambisonics, or HOA (High Order Ambisonics), begins at the 3rd order (16 channels). 

While ambisonics may be useful for some, such as those with higher-order systems available, they inherently have some issues when compared to other means of pre-rendering spatial soundfields. [Ambisonics](../mixing-terms#scene-based) can be great when used intelligently as a technique used to achieve something specific, such as a naturalistic soundscape, however it is not an approach to spatial audio that fits most forms of content. 

- Abstract channel handling and metering and unintuitive for audio professionals
- Unable to "hard-pan" or isolate signal to one direction without bleeding to opposite direction channels
- Minimized stereo-width
- Minimized dynamic range
- Non standardized tooling; resulting in implementations that sonically differ
- Confusion with channel order for different variations of ambisonics
- Confusion with normalization for different variations of ambisonics

A usecase for ambisonics that is common is for field recordings using ambisonic related microphone arrangements. It should be noted however that the microphones themselves are vector point recordings that later get [encoded](../technical-terms#encode) into the ambisonic B-Format spherical harmonic standard, before this step they are akin to other multi-mic arrays where each capsule is attempting to capture a specific cardioid sound response & direction (typically referred to as A-Format ambisonics). With this in mind, and true with most spatial audio formats, any microphone arrangements could be succesfully used and [encoded](../technical-terms#encode).

---

### [Facebook 360 Audio](../existing-formats#fb360)

##### Type: Ambisonics / Scene Audio

Facebook's spatial audio is part of their 360 Spatial Workstation. The system was bought by Facebook from Two Big Ears. They feature production tools that can be encoded with platform-specific metadata. It's focus is on playback within a specific application. The framework places a listener at the center of a sphere and uses panning within that sphere. Early and late room reflections are also available. In this sense, Facebook 360 uses additional room modelling processing. This is consistent with the research produced by Facebook Reality Labs, as their agenda focuses on users having a sense of shared space. On a technical level the Facebook360 (aka .tbe) is a custom variation of a 2nd order ambisonic soundfield with additional HRTF and room modeling processing.

---

### [Dolby Atmos Audio](../existing-formats#dolby-atmos)

##### Type: Object Audio

Dolby Atmos is a proprietary production software suite that follows the [Object-Based](../mixing-terms#object-based) method of creating spatial audio ideal for a Dolby Atmos speaker configuration, but due to its object-based approach is configuration agnostic. One of the distinguishing factors when compared to other surround sound formats is its limited use of height information. Like ADM, Dolby Atmos does not store its information in channels. It is rendered in real-time using metadata assocaited to each channel to render its position and other processing effects during runtime.

Dolby Atmos Master files contain two components for the audio streams: 
- `channel-bed` : Submix that by default uses 7.1.2, additional proprietary surround configurations can be added
- `object-bed` : individual mono or stereo objects

The Dolby Atmos Master files are comprised of: 
- `.atmos` : the general metadata for both channel-bed and object-bed of the project
- `.atmos.audio` : a multichannel uncompressed audio file
- `.atmos.metadata` : the object-bed specific metadata

For a review of use of Dolby Atmos, refer to [Observations and Limitations of Dolby Atmos for Spatial Mixing]({{< relref "posts/observations-and-limitations-of-dolby-atmos-for-spatial-mixing" >}})\
For more information on Dolby Atmos, refer to [Object-Based](../mixing-terms#object-based) 

---

### [Sony 360 Audio](../existing-formats#sony-360)

##### Type: Object Audio

For more information on Sony 360, refer to [Object-Based](../mixing-terms#object-based) 

---
## Runtime Spatial Audio Implementations
---

### [Apple Spatial Audio](../existing-formats#apple-spatial-audio)

##### Type: Other / Channel-Based Audio

Apple's spatial audio is currently highly feature and use-case driven. The process used for spatialisation differs between these applications. For example, the headtracked Dolby Atmos output from Apple TV undergoes a different process than Apple Music spatialisation to a certain extent. Apple Music spatial audio tracks have all had to be "re-engineered" using Dolby Atmos. Ideally this would allow the benefit of ensuring that the spatial mix that is released is more closely related to what the producer intended you to hear, however Apple Spatial does not utilize any of the processing effects forced by Dolby Atmos and upon rendering for Apple Spatial from Dolby Atmos all of the soundfield's height, room modeling and HRTF processing are stripped away to create a resulting 5.1 mix. This 5.1 mix is then forced through another object style playback rendering with additional **new** room modeling and HRTF processing that cannot be edited or controlled, further degrading and shrinking the intended spatial soundfield for headtracked playback with IMU enabled AirPods. 

For more on Apple's spatial audio, we have outlined how to sideload and review Apple's spatial audio implementation here: [Previewing Spatial Audio on Apple AirPods]({{< relref "posts/previewing-spatial-audio-on-apple" >}})

We have also reviewed the implementation and use of Apple's IMU enabled devices here:
[Feedback on Apple's Spatial Audio Implementation]({{< relref "posts/feedback-on-apple-spatial-audio" >}})

---

### [Game Engine Object Audio](../existing-formats#game-engine-object-audio)

##### Type: Object Audio

Object-based audio is a good example of a spatialisation method that *lends itself* to interactive content, or head-tracked spatial audio.

**Object-based audio refers to a system that sums together audio-objects at runtime/playtime.** This is a commonly used format that is growing in popularity due to its ability to assemble mixes for different configurations in real time, rather than having to create a new mix for each configuration, as seen in [Channel-Based](../mixing-terms#channel-based). We see this approach used all the time in game audio (game engines function using object-based audio), as well as proprietary systems such as Dolby Atmos #DolbyAtmos. Wave-field synthesis (WFS) is also a type of object-based spatialisation, but not one commonly used in the industry.

**In object-based audio, metadata from your audio format tells your rendering system where objects are and when they play, depending on the audio delivery system you are using.** Object-based audio is easily made interactive, which may sound great (and it is!), but it has inherent tradeoffs.

Because object-based audio is a runtime solution (you program rules and it plays by the rules when a user uses it), it can sound different depending on what the user does and how well the rules were designed. However, there is never a complete post-production pipeline, which can remove some essential elements from a mix, and make it difficult to control your listener's experience.

---

### [High Fidelity Spatial Audio](../existing-formats#high-fidelity-spatial-audio)

##### Type: Object Audio

High Fidelity is a spatial audio company that evolved as a pivot from social VR. Early beta versions demonstrated High Fidelity as an online platform with a 2D top-down view that featured spatial audio for the purpose of hosting, for example, simultaneous DJ sets that you could move your 2D avatar around the 2D space to discover. So 2D visuals, 3D audio. Recently, High Fidelity has offered themselves as a spatial audio integration tool for networked environments. Their spatial audio processing is geared for WebRTC (Web real-time communication). That makes their tools great for real-time voice over IP solutions with low latency and effective spatialisation. While their tools are interesting, they are not made for creators to produce spatial audio content and are an extension of object audio implementation use for 3D engines (or game engine object audio). 

---
### [THX Spatial Audio]({{< relref "glossary/existing-formats#thx" >}})

##### Type: Other / HRTF

While Mach1 Spatial and Facebook 360 are focused on the creation of spatial audio, THX offers an entirely different perspective and should not be compared. THX is an end-user solution that is marketed to enhance a gaming experience. We haven't seen any head-tracked spatial audio coming from THX. Our best description of THX is a post-processing chain of binaural filters and equalisation designed for listening to specific parts of a gaming soundscape. THX falls into the "virtual surround sound" category, but with more expansive calibration. Besides EQ, the two main spatial audio features they offer are virtual rendering of 7.1 surround sound and binauralized up-mixed version of standard stereo content. 

At Mach1, we believe in preserving the high quality audio that sound designers, composers, and engineers worked expertly to create. While it is surely an entertaining feature, it is important to note that the methods THX use to spatialise audio are ultimately destructive to the creative mix.  

---

### [Codec vs. Format](../existing-formats#codec-vs-format)

A codec is a software that compresses your media content into a container. When discussing spatial audio, MPEG-H is often brought up as the future of spatial audio formats. While MPEG-H is a very helpful technology for spatial audio, this isn't entirely correct. 

MPEG-H is a modern codec and container to encourage support of large multichannel audio content/formats and metadata when needed. 
It isn't relevant to compare a spatial audio format to MPEG-H because they are entirely different components.

MPEG-H is the "container" and "codec" and "packaging" for multichannel/spatial/interactive audio content, whether it is Mach1 Spatial, ambisonics, surround sound, something custom made, or Dolby Atmos. All of these formats can be packaged in a codec and you can use MPEG-H as your preferred codec for that packaging. MPEG-H is suited to modernize and support the growing requirements of audio object solutions that require meta-data for processing. In short, it's a file container for audio that requires an audio engine with 3D math support to render that audio.

So on it's own, MPEG-H is just an empty container, which begs the question of how to fill that container with audio content. 

Mach1 Spatial offers a solution by focusing on how to fill that container with audio content that can be safely re-purposed or bridged to any and all other audio content formats. Mach1 Spatial's agnostic design and independence from proprietary codecs or containers makes it highly compatible with MPEG-H. The Mach1 Spatial format is a multichannel audio format that does not require any meta-data since the spatial audio is pre-rendered, and works easily with MPEG-H.

---