---
title: "1. General Terms"
---

### [Spatial Audio](../general-terms#spatial-audio)
The term spatial audio has been thrown around a lot lately, especially as companies such as Apple tout it as a new feature – but *what is spatial audio*? What does it mean when you're listening to something with spatial audio? 

Spatial audio is a concept that has been used and defined in several ways. You could say that any audio expressed with more than one channel is spatial audio. The advent of stereo technology or surround sound systems can be considered spatial, but are not spatial audio as we define it today. You could also say that spatial audio is any kind of sound that interacts with space or spatial effects. We use spatial effects all the time in music. Reverberation, for example, is a spatial effect that represents the physical phenomenon of a sound wave bouncing off different materials in the real world, the way light bounces off a mirror. In a way, any sound that replicates the way we hear naturally in real life is spatial audio.

If we had to pick, then here are four main elements that could define spatial audio. Spatial audio tends to make use of sound [externalisation](../general-terms#externalisation), [direction](../general-terms#direction), [distance](../general-terms#distance), and [presence](../general-terms#presence).

##### Synonyms : 3D Audio, [Diegetic Audio](../general-terms#diegetic)
##### Related Terms : 

---

### [HRTF](../general-terms#hrtf)

HRTF is an abbrieviation for head-related-transfer-function. 

*A transfer function is an algorithm that describes how to go from one thing to another*. If we had a basket of apples, but we wanted an apple pie, then the apple-pie-related-transfer-function would describe how to slice the apples, decorate them on the tart, and what temperature to bake it at.

A head-related transfer function (HRTF) then describes the difference between the way a sound in space and the way we hear the sound. This concept is important and widely used in acoustics because each person has a completely unique set of features that contribute to their unique HRTF. 

Until recently, it was computationally costly to update a HRTF in real-time, because a HRTF is not one monolithic thing, even when it is personalised. Each angle/position at which you might be looking will require a new HRTF (if you are working with head-tracked spatial audio). That's a lot of math for a small device to handle. These days, however, it's more than doable. 

A quick google search on spatial audio will tell you that HRTFs are fundamental for good spatial audio, but that's not always the case. If you have a standard HRTF – a HRTF that was *not* indivualised specifically for you – you'll get mediocre results for your spatial audio experience. They simply don't work for everyone. They work well enough for the most part, but they are far from a perfect solution and are not the only way to describe the way your ears perceive distance. If there are other elements along your chain of audio spatialisation that are less than ideal (such as low-order [[7. Ambisonics]], using HRTFs will likely amplify perceivable issues. 

So what goes into an HRTF or other psychoacoustic algorithm? **The main attributes necessary to create spatial audio effects are inter-aural time difference (ITD) and inter-aural level difference (ILD)**. #ITD is the difference in the time it takes for a sound to reach your left ear vs. your right ear. The #ILD is the difference in loudness between the two ears. ITD and ILD are dependent on your head-size and shape, but despite those variables, ITD and ILD are somewhat more straightforward to model.
There are other attributes that may contribute to the creation of an HRTF, such as timbral filters – a 'tuning' of the frequencies (pitches) your device responds to, much like tuning an instrument. You can easily hear why this is necessary by cupping your ear in any direction – you will hear a change in what frequencies you are hearing. So, if a very loud fly came by your ear and then flew up, you would detect three main changes, which impact each ear differently: time, level, and frequency.

When you are discussing loudspeakers rather than headphones, you may also encounter filters to compensate for the spatialisation. Our ears naturally spatialise audio, so we need filters such as inter-aural cross-correlation cancellation so that the audio isn't spatialised twice. 

##### Synonyms : [Head Related Transfer Functions](../general-terms#hrtf), [Head Related Transfer Filters](../mixing-terms#hrtf)
##### Related Terms :

---

### [Binaural](../general-terms#binaural)
Binaural is a term that is used in a wide variety of contexts.

### *What does binaural really mean?*

The word binaural literally means 'two ears'. In audio technology, this term is used when the left ear and the right ear hears/receives something different.

There are two kinds of ways binaural is used: 
1) Recording
2) Filtering
3) Rendering

Let's start from the beginning. We established that binaural means that each of your ears hears something different, but for the most part, this isn't what people refer to when they say binaural. Here we discuss binaural recording, binaural filtering, and binaural rendering. That said, many people say binaural instead of spatial audio. Whether binaural is the best word to use depends on the context, however, since it can refer to many things, it is better to be more precise.

### Binaural Recording 
When you make a **binaural recording**, you put one microphone into each ear of a dummy head, thereby recording from a first-person perspective. Remember that this means the perspective you are recording will be 'colored' by the dimensions of the dummy head and ears.  

Alternatively, you can pop a microphone in each of your own ears and record with your own head size and ear shape. But the same concept applies to this method – if you pass on your recording to someone else, they will be listening from the perspective of _your_ ears. It might be pretty different from their own ears, which could degrade the quality of the spatial experience.

Binaural recording is used most often for ASMR, for testing in audio technology, and for art and entertainment experiences. 

### Binaural Filtering and Rendering 

When you hear any kind of ''spatial audio'' in your headphones, it is always a binaural mixdown, unless your headphones are over your ears and have multiple drivers (there are experimental versions of this but nothing of the sort is available for consumers, so we'll ignore experimental headsets for now). 

If your recording was not made *binaurally*, the second and third way in which the term binaural is used is for **filtering and rendering**. 

You could take a sound source such as a recording you took on your phone of your daughter playing violin, and bring it into a DAW. Then, you could apply some kind of binaural filter using a #plugin. 

 Or you could use a different kind of spatial audio plugin and then export it as a binaural file (two-channels but from a first-person perspective), or a multichannel binaural mix. The number of channels you are able to play back depend on the system you are using. If you have a multichannel file that can't be played on your system, you will have zero spatial audio. The way to overcome this is to create a binaural mixdown – an intermediary step that takes your multichannel file, and accurately mixes it down to two channels. However, if you do this, pay attention, because you might lose the ability to have head-tracking. **fact check with Dylan that this makes sense**
 
 These methods sound similar but are doing different things. If you slap on a binaural filter early on, you're stuck with it. 



##### Synonyms : 
##### Related Terms : 

---

## [Perception Terms](../general-terms#perception-terms)

---

### [Diegetic](../general-terms#diegetic)
_Refers to a sound placed or panned in the scene or soundfield around the listener._
##### Synonyms : Scene-locked, Spatialized, [Panned](../general-terms#panning)
##### Related Terms :

---

### [Non-Diegetic](../general-terms#non-diegetic)
_Refers to a sound locked to stereo instead of placed in a scene around the listener._
##### Synonyms : [Headlocked](../general-terms#non-diegetic), Traditional Stereo, Static Stereo
##### Related Terms :

---

### [Presence](../general-terms#presence)
Presence might be the most crucial aspect of spatial sound because it adds to our ability to be moved by the content we consume. Presence is also closely related to engagement, and connection to ourselves and others. Needless to say, it's a powerful energy that spatial sound can create. Presence is the feeling of '_being there'_.
##### Synonyms : 
##### Related Terms : 

---

### [Direction](../general-terms#direction)

##### Synonyms : [Azimuth](../technical-terms#azimuth), [Elevation](../technical-terms#elevation), [Pan](../mixing-terms#panning), [Panning](../mixing-terms#panning)
##### Related Terms : 

---

### [Distance](../general-terms#distance)
_Distance refers to how far away we precieve the intended sound source. Distance can and has been achieved creatively in post-production and recording techniques via various methods that alter the sound source in gain, filtering, reverberance and delay process effects or design._
_In some spatial audio systems such as spherical based systems like ambisonics or object based systems such as game audio distance is a pre-described process effect from toolset to toolset._

##### Synonyms : 
##### Related Terms : [Diverge](../mixing-terms#diverge)

---

### [Localisation](../general-terms#localisation)
_Localisation often refers to how well a listener or user is able to perceive the direction of a sound source in a spatial or multichannel surround field._

##### Synonyms : 
##### Related Terms : 

---

### [Externalization](../general-terms#externalization)
_Externalization refers to how well a listener or user perceives the sound emitting [Dietgetically](../general-terms#diegetic) or from the space around the listener or user. This can be achieved from utilizing ILD, ITD and additional room modeling, reverberance, delay and HRTF processing to enhance the sound to be perceived externally._

##### Synonyms : 
##### Related Terms : 

---
