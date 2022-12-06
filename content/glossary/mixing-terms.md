---
title: "2. Mixing Terms"
---

---
## [Common Workflow Terms](../mixing-terms#workflow-terms)
---

### [Panning](../mixing-terms#panning)
_Refers to panning a source sound or track into a spatial soundfield multichannel configuration or format. It is completely synonymous with [Encode](../technical-terms#encode)_
##### Synonyms : [Pan](../mixing-terms#panning), [Encode](../technical-terms#encode), Input to Spatial Soundfield
##### Related Terms :

---

### [Monitoring](../mixing-terms#monitoring)
_Refers to the binaural downmix based on the current listening "orientation" as a method of monitoring or live listening to a spatial soundfield via stereo binuaralized headpones or speakers. It is completely synonymous with [Decode](../technical-terms#decode)_
##### Synonyms : [Monitor](../mixing-terms#monitoring), [Decode](../technical-terms#decode), [Listening](../mixing-terms#monitoring), Stereo Playback, [Binauralized](../mixing-terms#binaural)
##### Related Terms : [Binaural](../mixing-terms#binaural)

---

### [Divergence](../mixing-terms#diverge)
_Divergence describes the amount of concentration of a panned or encoded input sound source to a specific [azimuth](../technical-terms#azimuth) or [elevation](../technical-terms#elevation). For example the higher the diverge the less this signal will exist in the opposite direction, the lower the diverge the more the signal will exist in all directions (until eventually becoming mono during [monitoring](../mixing-terms#monitoring) or [decoding](../technical-terms#decode))._
_This is unique to a vector based spatial or multichannel audio system and is different from sperhical based audio systems [distance](../general-terms#distance) which is less about signal distribution within a soundfield._
##### Synonyms : Focus, Directional Isolation
##### Related Terms : [Distance](../general-terms#distance)

---
## [Processing Effect Terms](../mixing-terms#processing-terms)
---

### [HRTF](../mixing-terms#hrtf)
##### Synonyms : [Head Related Transfer Functions](../general-terms#hrtf)
##### Related Terms : 

---

### [Room Modeling](../mixing-terms#room-modeling)
_Room modeling is a catch all term for various [reverberance](../mixing-terms#reverb), delay and even filter digital signal processes (DSP) that can be applied to the audio content. This can be used as a tool to add more externalization preception ability to any audio content but comes at the cost of altering the signal to do so. This effect is highly dependent on the use case and how this is being utilized to be more effective than destructive._
##### Synonyms : [Reverb](../mixing-terms#reverb), [Reverberance](../mixing-terms#reverb), Physical Modeling
##### Related Terms : [Externalization](../general-terms#externalization)

---

### [Binaural Filtering](../mixing-terms#binaural-filtering)

##### Synonyms : 
##### Related Terms : [Binaural Recording](../mixing-terms#binaural-recording)
When you hear any kind of ''spatial audio'' in your headphones, it is always a binaural mixdown, unless your headphones are over your ears and have multiple drivers (there are experimental versions of this but nothing of the sort is available for consumers, so we'll ignore experimental headsets for now). 

If your recording was not made *binaurally*, another way in which the term binaural is used is for **filtering and rendering**. 

You could take a sound source such as a recording you took on your phone of your daughter playing violin, and bring it into a DAW. Then, you could apply some kind of binaural filter using a #plugin. 

Or you could use a different kind of spatial audio plugin and then export it as a binaural file (two-channels but from a first-person perspective), or a multichannel binaural mix. The number of channels you are able to play back depend on the system you are using. If you have a multichannel file that can't be played on your system, you will have zero spatial audio. The way to overcome this is to create a binaural mixdown – an intermediary step that takes your multichannel file, and accurately mixes it down to two channels. However, if you do this, pay attention, because you might lose the ability to have head-tracking.
 
These methods sound similar but are doing different things. If you slap on a binaural filter early on, you're stuck with it. 

---

### [Binaural Recording](../mixing-terms#binaural-recording)
When you make a **binaural recording**, you put one microphone into each ear of a dummy head, thereby recording from a first-person perspective. Remember that this means the perspective you are recording will be 'colored' by the dimensions of the dummy head and ears.  

Alternatively, you can pop a microphone in each of your own ears and record with your own head size and ear shape. But the same concept applies to this method – if you pass on your recording to someone else, they will be listening from the perspective of _your_ ears. It might be pretty different from their own ears, which could degrade the quality of the spatial experience.

Binaural recording is used most often for ASMR, for testing in audio technology, and for art and entertainment experiences.
##### Synonyms : 
##### Related Terms : [Binaural Filtering](../mixing-terms#binaural-filtering)
---
## [Spatial Mix Dimensions](../mixing-terms#spatial-dimensions)
---

### [3DOF](../mixing-terms#3dof)
_3DOF stands for 3 Degrees of Freedom:_
 - _Rotating head left and right (shaking head as "no")_
 - _Rotating head up and down (shaking head as "yes")_
 - _Tilting head from left to right (tilting head so left ear approaches left shoulder or right ear approaches right shoulder)_
_Typically if you refer to a spatial mix as a 3DOF mix then you are implying it is only a headtracking or orientation only mix, instead of the mix being intended for head rotations as well as walking around._
##### Synonyms : 360-Mix, Orientational
##### Related Terms : [3DOF (sensor)](../technical-terms#3dof)

---

### [6DOF](../mixing-terms#6dof)
_6DOF stands for 6 degrees of Freedom:_
 - _Rotating head left and right (shaking head as "no")_
 - _Rotating head up and down (shaking head as "yes")_
 - _Tilting head from left to right (tilting head so left ear approaches left shoulder or right ear approaches right shoulder)_
 - _Walking forward or back_
 - _Strafing left or right (side-stepping to your left or right)_
 - _Climbing up or down (in level or floors)_

Typically this is referred to as [roomscale](../technical-terms#roomscale) or orientational & positional movements and rotations.
##### Synonyms : [Roomscale](../technical-terms#roomscale), Orientational & Positional
##### Related Terms : [6DOF (sensor)](../technical-terms#6dof)

---
## [Spatial Mixing Types](../mixing-terms#mix-types)
---

### [Channel-Based](../mixing-terms#channel-based)

Channel-based spatialisation is a process by which an audio engineer has created a multichannel mix of 'where the sounds go', typically for a standard surround sound format such as 5.1, 7.1, etc.

We've heard of mono (1-channel), stereo (2-channel), and surround sound. In stereo, the standard approach is that the 1st channel goes to the left speaker, and the 2nd channel goes to the right speaker. Surround sound is actually a channel-based spatialisation approach, with each channel number corresponding to a part of a speaker configuration.

Imagine you went to the recording studio with your choir and recorded each singer individually. Now, instead of hearing all the singers on all the speakers, let's say you want each singer's voice to be coming out of one speaker only. (There is a piece that does this. It's called *40 part motet*, by artist Janet Cardiff). This might be one approach to channel-based spatialisation, but it isn't a very practical one.

Alternatively, let's say you're back at the recording studio, and instead of having each singer go through one channel each, you want to group sections of the choir into 5 speakers. To do this, you would have to go into your Digital Audio Workstation (any audio production software), and create a multichannel mix specifically for that layout.

All audio is ultimately delivered via a given number of channels. The main difference with channel-based spatialisation is that there is *no way to change it*. **Whatever was mixed in the studio is what you're going to get**. Your system is pre-rendered for a fixed system.

There are some exceptions to this, however. Formats such as #Mach1,  unify the handling of multichannel and spatial audio formats/configurations and conversions between them. They allow for the development of custom multichannel configurations allowing backend development control to speaker configurations. While many virtual spatializers will use damaging effects to spatialise a channel-based mix, Mach1 Spatial's system is contained into a single multichannel deliverable through already existing audio containers and codecs.

Channel-based spatialisation is not set to disappear anytime soon. For all the discussion on the versatility of [Object-Based](../mixing-terms#object-based) audio, channel-based spatialisation may have its own advantages depending on the experience that needs to be created and the system it's created for.

##### Synonyms : [Surround](../existing-formats#surround)
##### Related Terms : [Mach1 Spatial](../existing-formats#mach1-spatial), [Dolby Atmos](../existing-formats#dolby-atmos)

---

### [Object-Based](../mixing-terms#object-based)

Object-based audio is a good example of a spatialisation method that *lends itself* to interactive content, or head-tracked spatial audio.

**Object-based audio refers to a system that sums together audio-objects at runtime/playtime.** This is a commonly used format that is growing in popularity due to its ability to assemble mixes for different configurations in real time, rather than having to create a new mix for each configuration, as seen in [Channel-Based](../mixing-terms#channel-based). We see this approach used all the time in game audio (game engines function using object-based audio), as well as proprietary systems such as Dolby Atmos #DolbyAtmos. Wave-field synthesis (WFS) is also a type of object-based spatialisation, but not one commonly used in the industry.

**In object-based audio, metadata from your audio format tells your rendering system where objects are and when they play, depending on the audio delivery system you are using.** Object-based audio is easily made interactive, which may sound great (and it is!), but it has inherent tradeoffs.

Because object-based audio is a runtime solution (you program rules and it plays by the rules when a user uses it), it can sound different depending on what the user does and how well the rules were designed. However, there is never a complete post-production pipeline, which can remove some essential elements from a mix, and make it difficult to control your listener's experience.

##### Synonyms : 
##### Related Terms : [Dolby Atmos](../existing-formats#dolby-atmos), [Sony 360](../existing-formats#sony-360)

---

### [Scene-Based](../mixing-terms#scene-based)

Scene-based spatialisation represents an audio scene from a first-person perspective. The most common example of scene-based spatialisation is #Ambisonics, a technology that was developed in the 1970s and has since been used as one of the dominant spatialisation techniques. It's popularity stems from its use within academia rather than from its quality and ease of use from an industry perspective.

Scene-based spatialisation usually entails placing a listener at the center of a sphere or comparable 3D shape. Ambisonics are created using spherical harmonics and complex mathematics. They are referred to in 'orders', which means how many channels are output, corresponding to the "resolution" of the spatial image. 

While every system we have detailed has drawbacks, ambisonics are particularly tricky when it comes to playback in a real, physical space. It  can only be properly experienced within a few inches of a centerpoint and if not calibrated correctly will be perceived incorrectly. It is quite costly to render ambisonics with a high resolution for this reason. High resolution ambisonics, or HOA (High Order Ambisonics), begins at the 3rd order (16 channels). 

While ambisonics may be useful for some, such as those in academia with higher-order systems available, we ultimately do not recommend ambisonics as a spatialisation method. It can be great when used intelligently as a technique used to achieve something specific, such as a naturalistic soundscape, however it is not an approach to spatial audio that fits most forms of content. 

Once again, with ambisonics, we encounter the issue of whether the content was recorded using a spatial or ambisonic microphone or not. 
Using an ambisonic microphone is great if you want to have a quality ambisonic mix, however most ambisonic microphones are expensive and low in resolution and become limiting when used for creative mixing. 
When converting another kind of recording to ambisonics, we end up losing a lot of the frequency information (the mix essentially gets destroyed), and often we lose a lot of directional information as well (blurry sense of localisation, or confusions). 

For industry creators, ambisonics lack the creative freedom and dramatic flair required of entertainment mediums. Formats invented with content creators in mind, such as Mach 1, offer solutions that overcome many of the problems found in scene-based systems. 

##### Synonyms : [Ambisonics](../existing-formats#ambisonics)
##### Related Terms : 
