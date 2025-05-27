---
title: "State of Affairs: Spatial Audio"
date: 2022-03-18T10:10:05-04:00
lastmod: 2022-03-23T10:10:05-04:00
---

Over the last year there has been a lot of growth and interest into concepts surrounding spatial and multichannel audio in various different use cases and examples across many markets. We wanted to collect our observations and criticisms into a single post in an effort to help everyone researching to learn from our experiences and encourage better practices at large. When it comes to spatial audio we want to encourage growth as a medium and let different use cases define what spatial audio means in each instance while still catering to a creative production pipeline that enables more creative and technical growth at large, in human words: we want less proprietary approaches or tools and more open or cross-compatible growth.

## Key Points for the Industry to Encourage Growth
In our view its clear that there are a few key ingredients we need to encourage a healthy new "spatial audio" medium and landscape for all: 

### *Hardware / Consumer Audio Wearable Manufacturers*: 
If you are including IMUs into products that can be used for detecting motion/headtracking/position-tracking, please do not try to make that a proprietary process and expose it for developers and creators a like with simple and easy to use APIs that return orientation/position tracking data. _*Let the development community build to your device instead of you trying to predict what the community and consumers at large might want!*_

### *Software Audio Distribution Services & Streamers*: 
Instead of building your own interpretation of "spatial audio" please provide support to ingest more open practices and existing pipelines or formats _(this is why we prepared the [Mach1 Spatial SDK](https://github.com/Mach1Studios/m1-sdk), to aggregate handling playback of the ever growing list of formats to keep things flexible and avoid introducing new "sounding" solutions that add more blockers to the creative production pipeline)_. Introduction of proprietary room modeling or proprietary spatial headtracking processing effects might have short term consumer reaction and excitement it ultimately encourages less growth for creators and audio engineers lose time and confidence due to the loss of creative control as well as the amount of additional effort it takes to make content deliverable to more platforms. In the long run; the more ways to distribute and ingest spatial audio mixes the better for consumer interest and for creative experimentation which will lead "spatial audio" going from an end-point processing effect for consumers to become a new medium that artists and creators can use broadly to reach larger audiences and attract more IMU enabled hardware growth.

### *Creators and Audio Engineers*
Hang in there, understand that there will always be an excitement for consumers who listen to a mix with any form of audio interactivity but after that is more expected in consumers they will start to be less intrigued by "it can be spatial?" and more intrigued by "why is this spatial?". As soon as we have more ways to distribute to consumers a spatial soundfield that is defined from creation and not defined by the tools used to make it; there will be a surge in creative exploration to improve creative ability for "spatial audio" in production and turning it into a medium we can all be excited about!

## Observations and Critism Examples
This section will look at the large scale deployments of "spatial audio" in 2021 -> 2022. While it is exciting to see such large scale engagement we wanted to repeat our observations of what is working and what isn't to transparently offer support that would encourage more growth for everyone interested and involved in spatial and multichannel audio.

### Apple Spatial
The Apple team has gotten some things right and some things very wrong, we will try to explain it all here as succintly as we can. However you can read more about our observations and feedback here regarding [Apple Spatial's playback processing effect]({{< relref "posts/observations-and-limitations-of-apple-spatial-playback-implementation" >}}) or [Apple's IMU implementation]({{< relref "posts/feedback-on-apple-spatial-audio" >}}).

##### Pros
 - Introducing large scale headtracking concepts.
 - [API for developers](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager) to access motion/orientation data from supported devices.

##### Cons
- Introducing "Spatial Audio" as a proprietary processing effect on playback for end-users instead of introducing already existing spatial audio mixing practices (and ideally all of them) to encourage content growth.
- Partnering tightly with Dolby to retrofit a cinema mixing pipeline as a spatial audio pipeline and blocking out the majority of quality spatial audio mixing approaches and already existing content.
- [Not allowing spatial music to exist in app form more loosely]({{< relref "posts/submitting-spatial-music-apps-to-ios-app-store" >}}) while common streaming distribution services do not have implmented solutions yet.

### Dolby Atmos
The explosion of remixed Dolby Atmos mixes has caused some strain and issues for creators, developers and consumers. We want to start by saying Dolby Atmos used for theatre based production pipelines makes sense and is a great solution that solves a lot of pain points seen in that use case previously. _In no way are our observations about the usage of Dolby Atmos for theatre surround mixing_. What we can critique is the usage of Dolby Atmos to remix stereo content to become "spatial audio", introducing a close pipeline for mixers to turn content that in some cases should never be anything else but the intended stereo mix it was, but also limiting the mixing experience to a front facing, non-headtracking based pipeline that introduces proprietary room modeling to simulate "spatial audio" completely defeats the purpose of spatial audio and has been harming market and consumer confidence in spatial audio in its entirety. It may be an extreme and biased thing to claim but there is no benefit of using Dolby Atmos for spatial mixing for audio AR, or headtracking intended audio mixes and we strongly recommend against this usage as long as it remains so controlled and proprietary and not accessible to creators or developers to redefine based on their needs.  

Feel free to read more on our [observations and feedback of Dolby Atmos used for spatial audio mixing]({{< relref "posts/observations-and-limitations-of-dolby-atmos-for-spatial-mixing" >}})).
