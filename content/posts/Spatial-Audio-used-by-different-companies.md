---
title: "How is the term \"Spatial Audio\" used by different companies?"
date: 2021-08-11T03:10:05-04:00
---

## What do companies mean when they talk about spatial audio?

Currently this is a very broad question because spatial audio is a subject spanning across disciplines and industries. We could talk about different [flavors of audio spatialization]({{< relref "glossary/general-terms#spatial-audio" >}}), or about the history of spatial audio in academia. What we would like to focus on is the way the consumer electronics industry has most commonly employed the term in recent years, and share some points of clarification based on our years of experience both creating spatial audio experiences and the tools necessary to create them.
  
Sony, Dolby Atmos, and by extension Apple, are all object-based audio style formats that utilize metadata loosely based on ADM & MPEG-H standards, [more info on differences here]({{< relref "posts/observations-and-limitations-of-dolby-atmos-for-spatial-mixing" >}}). This means that the metadata encoded in each file format follows the same standard. However, they each require proprietary codecs to decode the metadata in these files. That means that if you play a Sony 360 audio file without a compatible device, you won't be able to decode the metadata within it. You will hear *something*, but it will be a [channel-based]({{< relref "glossary/mixing-terms#channel-based" >}}) mix unable to scale in the modular way the object-based mix was intended to do.
We share more on [object-based]({{< relref "glossary/mixing-terms#object-based" >}}) audio [in our glossary.]({{< relref "glossary/mixing-terms#object-based" >}})

Many object-based audio systems are *not* transparent about the physical modeling involved in the way they make what you're hearing sound like it's inside a space. By physical modeling, we mean the addition of arbitrary room acoustics. While sound in real life always exists in space and is therefore colored by the room it's in (or the lack thereof), we believe that the addition of such arbitrary room acoustics – whether or not they are customizable – goes against the artistic intention of the mix. As creators of spatial audio mixes, we've developed a spatial audio workflow wherein *the technical mix is the creative mix*.

The whole purpose of spatial audio is the re-create the way we hear naturally. Unfortunately, many platforms deliver head-locked experiences and call it spatial audio. In real life, the way you hear something changes as you move your head, so if any company is using the term spatial audio without using head-tracking, take it as a sign to look deeper into what's *actually* going on, because it's not really spatial audio. Usually what companies mean when they say spatial audio is a binauralised stereo downmix of a mix that has been created using spatial characteristics.

## [Apple Spatial Audio](../posts#apple-spatial-audio)

In order to send two channels via bluetooth (bluetooth currently only supports two audio channels), Apple pre-processes a multichannel audio stream (for example five virtual speakers) using a binaural room impulse response.

### For Apple TV and headphones:

#IMU data from Apple headphones or earbuds are used to make interactive spatial audio from a Dolby Atmos mix. The Dolby Atmos metadata is mixed into five virtual speakers, and updated in real-time according to your head position.

The way Apple spatializes audio for their Apple TV services is as close to true spatial audio as we currently see from them. By true spatial audio, we mean interactive spatial audio.

### Apple Spatial Audio for Apple Music and headphones:

Apple does not yet provide interactive spatial audio for its music streaming services over headphones. While this may change in the future, the essence remains that the music service sends a head-locked stereo binaural down-mix of whatever Atmos mix is playing.

Hypothetically, Apple could do this with literally any content, and there is nothing ground-breaking about it. The Dolby Atmos mix is also much less impressive over a head-locked system because object-based spatial audio's strong suit lies in its ability to adjust to changing parameters such as head-tracking.

### Apple Spatial Audio for speakers:

We don't want to make any false predictions on unreleased products, but Apple's spatial audio speakers will likely use object-based audio for custom speaker configurations. Spatial audio for headphones and for speakers are very different sides of the same coin. Though the intended effect is the same, the methods that are used are different.

### Apple Spatial Audio for AR:

Spatial audio for augmented reality is similar to any object-based spatial audio system. The spatial audio APIs that Apple use for Augmented Reality development are closely related to game-audio workflows, in that a sound is mapped to a location in a 3D space. Because of that, mono audio creates a better spatial effect as you move relative to the audio object.
  
### Is Apple Spatial Audio *actually* spatial audio?

When Apple makes use of head-tracking as an input to their audio spatialization, we can call it spatial audio. Because spatial audio is how we hear naturally, head-locked binaural stereo cannot be considered spatial audio, it is just spatial processing effects. Despite Apple's success at creating a "theater-like" experience with interactive spatial audio, there are some significant drawbacks, such as lack of compatibility with external IMUs and inability to decode other spatial file formats without creating the custom ability to do so via a third-party API. We've created the Mach1 Spatial API to overcome this problem. https://github.com/Mach1Studios/Pod-Mach1SpatialAPI

Even if all of Apple's spatial audio were interactive, we would still need to see an end to the use of generic HRTFs to truly obtain interactive spatial audio. The binaural effect output by Apple's spatial audio system is created using head-related transfer functions. This means that Apple's spatial audio system colors the sound with filters representing the way that someone else's ears would hear in some kind of room. Spatial audio should be agnostic to ear shape and size. Of course, in addition to artifacts that damage the sound quality and intended mix, it also means that we won't all hear it as well and that it won't work for everyone. Spatial audio should be democratic to everyone. Alternative solutions, such as Mach1 Spatial, are totally agnostic to your ear type and head shape. Hopefully, Apple can open their system just enough to allow spatial audio algorithms that preserve the creative mix to benefit from head-tracking in their own or other devices with IMUs.

For more on Apple's spatial audio, we provided some feedback which you can find below.

[https://github.com/Mach1Studios/m1-research-blog/blob/master/content/posts/Feedback-On-Apple-Spatial-Audio.md](https://github.com/Mach1Studios/m1-research-blog/blob/master/content/posts/Feedback-On-Apple-Spatial-Audio.md)

## [Dolby Spatial Audio](../posts#dolby-spatial-audio)

Like Sony 360 Reality, Dolby Atmos is not just a format, it is also a production tool. Artists mix or re-mix parts of their recording to the Dolby Atmos format by using their digital audio workstation plugins. Dolby is not a codec. It does not itself encode or decode its format. Other Dolby codecs are used to decode the Dolby Atmos format. The Dolby Atmos format uses the MPEG-H standard of containing metadata. This means that the Dolby Atmos format is a *container* holding both the file format as well as the object-based metadata.

### Dolby Atmos Production and mixing

Dolby Atmos' object-based production allows you to create audio "beds" that are more akin to channels, or larger sound fields. However, you are also able to make discrete "objects" that have their own independent behaviour. Though Dolby Atmos touts the never-done-before ability to pan towards height channels, this is not true. Almost every other spatial audio production suite can do this.

### Dolby Atmos for headphones

Dolby Atmos can be enabled on headphones by purchasing their app. This doesn't involve interactive spatial audio (head-tracking). When using Apple Airpods Pro or Max, you can also experience Dolby Atmos but only Dolby Atmos on Apple TV takes advantage of interactive spatial audio. The Dolby renderer will surely be used by more embedded devices in the future, however, it is unclear how head-tracking dependent information will become a part of their licensing.

### Dolby Atmos for speakers

Dolby Atmos for physical configurations is interesting but is not an entirely new concept. It's a standard surround sound system but with height information. The cool part is that the "beds" and "objects" can be played no matter what your configuration is – you don't need the traditional setup. However, if you don't have a decent configuration from the get-go, getting something that sounds good might be challenging. One thing to note is that the spatial audio we are talking about with headphones is usually really different from spatial audio for speakers. Spatial audio for speakers cannot have the kind of processing that mimics the way your ears hear within a space because your ears are already doing that!

### Dolby Atmos for cars

Dolby Atmos is also increasing in popularity in its application for vehicle sound systems. This isn't dissimilar from Dolby Atmos for speakers, but in order to outfit a sound system for cars, a lot of other parties are involved. In the example of Lucid Motors, Dolby discusses their partnership with DSP Concepts, a digital signal processing program widely used in audio consumer electronics. Audio sound systems for cars have to be carefully tuned to compensate for the many interfering sounds we have on the road, as well as the fact that there are usually at least five different listener locations.

### Is Dolby Atmos spatial audio?

As with everything we've looked at, it depends on the interaction involved. You definitely don't need Dolby Atmos to create spatial audio. When Dolby Atmos uses listener head position or speaker configuration to interactively bring the object-based mix to life, it is spatial audio. Otherwise, we're getting closer but not quite there yet.
  
## [Sony Spatial Audio](../posts#sony-spatial-audio)

Sony, like Dolby Atmos, is both a production tool as well as a format using MPEG-H as a standard for encoding object-based metadata.
With the Sony Headphones Connect app and a Sony 360 Reality compatible premium streaming service, you can playback 360 Reality content on any device. 

### Creative tools
Although the Sony 360 Reality creative software suite is used to create an object-based format where the listener is at the center of a sphere, the end-user ultimately gets a head-locked binaural stereo playback. As we have said time and time again, without interaction (head-tracking), you are not experiencing spatial audio. You are instead experiencing a post-production spatial effect.

### Headphones 
In the Sony Headphones Connect App, you must take pictures of your ears as well as chose the product you are using. This indicates that Sony uses generic head-related transfer functions (you can read more on these in our glossary entry on [[Mach 1 Spatial Audio Glossary 2/2. HRTFs]]). On top of the inevitably generic HRTFs, Sony will personalize a certain tuning of the spatial effect they are creating. 

When Sony writes that they create a personalized sound field, you should have a big asterisk going off in your head. Unless you went to get your HRTF specifically measured, it is not your true HRTF. However, it may be better than a completely standard one. The fact that you choose your product also suggests that Sony adds what is called an inverse transfer function which will compensate for the way each type of headphone will uniquely color the sound.  

### Is Sony 360 Reality spatial audio?

While these methods are interesting, they contradict our philosophy on agnostic interactive spatial audio that preserves the creative mix. Until Sony 360 Reality includes interactive head-tracking, it is not spatial audio. The only aspects inching their system closer to spatial audio are their inclusion of artists in the creation of an object-based mix, and the use of object-based mixes for custom potentially non-standard speaker configurations.
