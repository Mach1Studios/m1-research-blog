---
title: "1. General Terms"
---

### [Spatial Audio](../general-terms#spatial-audio)
The term spatial audio has been thrown around a lot lately, especially as companies such as Apple tout it as a new feature - but *what is spatial audio*? What does it mean when you're listening to something with spatial audio? 

Spatial audio is a concept that has been used and defined in several ways in our current audio landscape and marketplace. You could say that any audio expressed with more than one channel is spatial audio. The advent of stereo technology or surround sound systems can be considered spatial, but are not spatial audio as we define it today. You could also say that spatial audio is any kind of sound that interacts with space or spatial effects. We use spatial effects all the time in music. Reverberation, for example, is a spatial effect that represents the physical phenomenon of a sound wave bouncing off different materials in the real world, the way light bounces off a mirror. In a way, any sound that replicates the way we hear naturally in real life is spatial audio. This seems to be logic of how it is currently used as a term in upcoming technologies, just as loosely defined and differs drastically in press release to press release. We are trying to work out a common langauge that can be agreed upon so we can prepare consumers and creatives a like to have the correct expectations as these mediums are developed and used to share experiences.

If we had to pick, then here are four main elements that could define spatial audio. Spatial audio tends to make use of sound [direction](../general-terms#direction), [distance](../general-terms#distance), [externalisation](../general-terms#externalisation) and [presence](../general-terms#presence). These are typical quality traits we can discuss when listening to anything that is `spatial audio`. However there are also some technical traits we need to outline to make sure when two parties discuss something about `spatial audio` they are in fact referring to the same thing. From our experience the easiest starting point when discussing `spatial audio` is whether it is interactive and involves headtracking or position tracking of any kind (updates with interactivity or movement and rotation), or if we are referring to processing effects applied to traditional stereo with no interactivity aka "[headlocked](../general-terms#headlocked) spatial audio".

#### Headtracked vs. Headlocked
As mentioned above, we find it easier to boil down the usage of `spatial audio` to whether its [headtracking](../general-terms#headtracked) or roomscale interactive or headlocked for room modeling and HRTF processing simulation. From there it becomes clearer to narrow down expectations for all parties involved.

A quick way to feel the difference between headtracked and headlocked spatial audio is to stick your left arm out and make a ball with your hand. Pretend the ball is the sound source. Now, keep your arm still (don't move it), and rotate your head to the right, like you're trying to see something over your right shoulder. See how the distance and angle between the ball and you head has changed? Those changes are what would be applied to the audio while listening to headtracked `spatial audio`. 

If that exercise wasn't too cumbersome, try it again. This time, when you rotate your ear to the right, bring your arm around with you, so that your arm and your head/torse are moving together. That's headlocked spatial audio. Headlocked stereo audio is what we have been listening to in headphones since the advent of stereo an unnatural phenomon that has be taught to us all. 

The majority of spatial audio experiences are headlocked. This is truly a shame, because while headlocked spatial audio processing can be used creatively and effectively it has always existed via traditional stereo audio listening experiences, **headtracking spatial audio is *far* more interesting and even magical**. If spatial audio is defined as a way to replicate the way we hear naturally, then headtracking spatial audio *is* `spatial audio`. 

Spatial audio with headtracking has many other advantages, including but not limited to: 
- Helping the user adapt to non-individualised HRTFs 
- Interactive and helpful for gameplay
- Essential mechanism for VR,AR,XR
- Keeping realism/suspension of disbelief
- Superior user experience
- Providing audio cues to guide a user
- Being used creatively and not just to spatially place sounds around a user

The difference between head-tracked and head-locked spatial audio is really important. Spatial audio experiences and technology should include headtracking to be truly considered as such. You can find more about [headtracked](../general-terms#headtracked) vs. [headlocked](../general-terms#headlocked) spatial audio and the methods used to create spatial audio such as in our section on [headtracking](../general-terms#headtracked), as well as in [HRTFs](../general-terms#hrtf).

##### Synonyms : [3D Audio](../misc-terms#3daudio), [Diegetic Audio](../general-terms#diegetic)
##### Related Terms : 

---

### [Headtracking](../general-terms#headtracked)
Headtracked spatial audio is anchored in absolute space, which can be detected as the listener rotates their head or in some cases [moves within a space](../mixing-terms#6dof).

We recommend that the term `spatial audio` refers to audio that is updated in real-time according the your head orientation and/or position. It means that the spatial audio is headtracking (as opposed to [headlocked](../general-terms#headlocked)). However until this term is more commonly understood in the marketplace it is best to over explain what you are referring to what using terms like `spatial audio`.

There are several ways to introduce orientation data to act as a form of "headtracking" input, commonly a sensor technology is used known as an [IMU](../technical-terms#imu), or [Inertial Motion Unit](../technical-terms#imu). You can also read more about [IMUs](../technical-terms#imu). Other methods can be more passive such as a [camera to detect face/head changes](https://github.com/Mach1Studios/m1-web-spatialaudioplayer#facetracking), or even just other devices around the user.

##### Synonyms : Headtracking
##### Related Terms : [Headlocked](../general-terms#headlocked)

---

### [Headlocked](../general-terms#headlocked)
Head-locked spatial audio is anchored at a point relative to the listener. Technically equivelent to just stereo audio playback, however we have seen rise to the usage of spatial audio processing effects such as HRTFs, room modeling, reverbs and binaural filters being applied to headlocked stereo audio and earning the right to be called "spatial audio", we are very weary of this as it causes confusion in expectations for creators, developers and consumers alike.

It should be noted that there is no effect process that happens in headlocked spatial audio processes that couldn't be applied to `spatial audio` with headtracking to make it even more effective.

##### Synonyms : 
##### Related Terms : [Headtracked](../general-terms#headtracking)

---

### [HRTF](../general-terms#hrtf)
*A transfer function is an algorithm that describes how to go from one thing to another*. If we had a basket of apples, but we wanted an apple pie, then the apple-pie-related-transfer-function would describe how to slice the apples, decorate them on the tart, and what temperature to bake it at.

A head related transfer function (HRTF) then describes the difference between the way a sound in space and the way we hear the sound. This concept is important and widely used in acoustics because each person has a completely unique set of features that contribute to their unique HRTF. 

Until recently, it was computationally costly to update a HRTF in real-time, because a HRTF is not one monolithic thing, even when it is personalised. Each angle/position at which you might be looking will require a new HRTF (if you are working with headtracked spatial audio). That's a lot of math for a small device to handle. These days, however, it's more than doable. 

A quick google search on spatial audio will tell you that HRTFs are fundamental for good spatial audio, but that's not always the case. If you have a standard HRTF – a HRTF that was *not* indivualised specifically for you – you'll get mediocre results for your spatial audio experience. They simply don't work for everyone. They work well enough for the most part, but they are far from a perfect solution and are not the only way to describe the way your ears perceive distance. If there are other elements along your chain of audio spatialisation that are less than ideal (such as low-order [ambisonics](../mixing-terms#scene-based), using HRTFs will likely amplify perceivable issues. However one of the greatest issues with them is that they add an additional processing layer to an audio mix that is out of control of the creator or audio engineer, this adds a further gap between an intended artistic mix and ways we can play it back as intended.

So what goes into an HRTF or other psychoacoustic algorithm? **The main attributes necessary to create spatial audio effects are interaural time difference ([ITD](../general-terms#itd)) and interaural level difference ([ILD](../general-terms#ild))**. [ITD](../general-terms#itd) is the difference in the time it takes for a sound to reach your left ear vs. your right ear. The [ILD](../general-terms#ild) is the difference in loudness between the two ears. [ITD](../general-terms#itd) and [ILD](../general-terms#ild) are dependent on your head-size and shape, but despite those variables, [ITD](../general-terms#itd) and [ILD](../general-terms#ild) are somewhat more straightforward to model.
There are other attributes that may contribute to the creation of an HRTF, such as timbral filters – a 'tuning' of the frequencies (pitches) your device responds to, much like tuning an instrument. You can easily hear why this is necessary by cupping your ear in any direction – you will hear a change in what frequencies you are hearing. So, if a very loud fly came by your ear and then flew up, you would detect three main changes, which impact each ear differently: time, level, and frequency.

When you are discussing loudspeakers rather than headphones, you may also encounter filters to compensate for the spatialisation. Our ears naturally spatialise audio, so we need filters such as interaural cross-correlation cancellation so that the audio isn't spatialised twice. 

##### Synonyms : [Head Related Transfer Functions](../general-terms#hrtf), [Head Related Transfer Filters](../mixing-terms#hrtf)
##### Related Terms :

---

### [Binaural](../general-terms#binaural)
Binaural is a term that is used in a wide variety of contexts.

The word binaural literally means 'two ears'. In audio technology, this term is used when the left ear and the right ear hears/receives something different.

There are two kinds of ways binaural is used: 
1) Recording
2) Filtering
3) Rendering

Let's start from the beginning. We established that binaural means that each of your ears hears something different, but for the most part, this isn't what people refer to when they say binaural. Here we discuss binaural recording, binaural filtering, and binaural rendering. That said, many people say binaural instead of spatial audio. Whether binaural is the best word to use depends on the context, however, since it can refer to many things, it is better to be more precise.

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

### [Direction](../general-terms#direction)
_Refers to the original angle the source of a sound is perceived to come from compared to the listener._

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

Spatial audio tends to incorporate a sense of direction and distance. There are many other factors that can heighten the sense of sound coming from a specific location, but when we say localisation, we usually mean direction and distance. So if you are looking straight ahead, you can hear sound from every direction around you.  But it's not enough to hear the direction of a sound source. We hypothetically also want to be able to tell how far away our zombie enemy is from our character in a RPG game. While it turns out that humans are not great at detecting distance with precision, that doesn't mean that the sense of distance isn't important. Keep in mind that relaying the sense of distance towards the front of the listener's head is more challenging than to the sides. Similarly, if you are using [HRTFs](../general-terms#hrtf), you may encounter front-back confusion. The good news is that when you use [headtracking](../general-terms#headtracked), you can often mitigate some of these issues.

There are also contextual factors that play into our perception of direction and distance. For example, if your spatial sound effect is accompanied by a visual image, let's say you see someone playing the violin and you hear violin music, you will have a much easier time believing that the violin music is coming from the violin player, even if without the visuals you would not have been able to locate the direction of the violin music. On the other hand, if your violin music isn't spatialised, you will be less immersed and engaged in the suspension of disbelief. 

There are some ways you can exploit localisation phenomena. One way is by using the **Ventriloquist Effect** that we discussed above. Another way is by using content to relay spatial information. You will perceive the sound of someone whispering as much closer to you than the sound of someone shouting at you to "come over this way!". Spatial sound designers can also play around with timbre and timing to make something sound spatial even in a non-spatial context. You may have experienced listening to a show with your headphones, and suddenly taking them off because you thought there was someone knocking at your door, when it was actually coming from the show. 

##### Synonyms : 
##### Related Terms : 

---

### [Externalization](../general-terms#externalization)
_Externalization refers to how well a listener or user perceives the sound emitting [Dietgetically](../general-terms#diegetic) or from the space around the listener or user. This can be achieved from utilizing ILD, ITD and additional room modeling, reverberance, delay and HRTF processing to enhance the sound to be perceived externally._

Externalisation is the phenomenon of perceiving that what you hear is outside your head. It's exactly how we hear every day in normal life – when you hear a car coming up behind you as you walk to the coffee shop, you know where the car is, roughly how close it is, and how fast it is approaching you. An airplane sounds like it's above your head, obviously not inside your skull. 

But when we put on a pair of headphones and listen to **stereo** content, something called in-head localisation occurs. In-head localisation just means that you hear the 'soundstage' on a line behind your eyes and between your two ears. So, instead of hearing Joni Mitchell crooning to you on stage, she's right in the center of your head. The in-head localisation effect has pros and cons. On one hand, lots of new music is produced for headphones. They fully take advantage of stereo phenomena (this speaks to how important it is to have your end-point rendering system in mind when you are producing), as well as the considerations of retroactively spatialising a stereo mix. On the other hand, a lot of artists love the creative that freedom spatial audio offers them. In addition, it can be really exhausting for your brain. Cognitively speaking, stereo listening over headphones is unnatural for your brain. When paired with immersive visual content, it is important to have spatial audio externalisation in order to really drive home your experience.

##### Synonyms : 
##### Related Terms : 

---

### [Presence](../general-terms#presence)
Presence might be the most crucial aspect of spatial sound because it adds to our ability to be moved by the content we consume. Presence is also closely related to engagement, and connection to ourselves and others. Needless to say, it's a powerful energy that spatial sound can create. Presence is the feeling of '_being there'_.

##### Synonyms : 
##### Related Terms : 

---

### [ILD](../general-terms#ild)

##### Synonyms : 
##### Related Terms : 

---

### [ITD](../general-terms#itd)

##### Synonyms : 
##### Related Terms : 

---