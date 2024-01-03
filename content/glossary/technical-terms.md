---
title: "3. Technical Terms"
---

---
## [Degrees of Freedom (DOF)](../technical-terms#dof)
---

### [3DOF](../technical-terms#3dof)
_Typically refers to a single sensor (accelerometer or gyroscope) 3 axis output values_
##### Synonyms : 
##### Related Terms : [3DOF (Movement)](../mixing-terms#3dof)

---

### [6DOF](../technical-terms#6dof)
_Typically refers to the usage of two sensors (accelerometer and/or gyroscope and/or magnometer) 6 axis output values_
##### Synonyms : 
##### Related Terms : [6DOF (Movement)](../mixing-terms#6dof)

---

### [9DOF](../technical-terms#9dof)
_Typically refers to the usage of three sensors (accelerometer, gyroscope and magnometer) 9 axis output values_
##### Synonyms : 
##### Related Terms : 

---

### [10DOF (and greater)](../technical-terms#10dof)
_Typically refers to the usage and combination of sensors for 10 or more axis data output values_
##### Synonyms : 
##### Related Terms : 

---
## [Inputs & Outputs](../technical-terms#io)
---

### [Source](../technical-terms#source)
_Typically referring to a sound source or a single mono or stereo input sound/track_
##### Synonyms : Input
##### Related Terms : 

---

### [Listener](../technical-terms#listener)
_Typically referring to the listening object representing your first person perspective ears or the virtual microphone object or location for stereo capture and playback_
##### Synonyms : [Decode](../technical-terms#decode), [Monitor](../mixing-terms#monitoring), [Monitoring](../mixing-terms#monitoring), [Listening](../mixing-terms#monitoring), Stereo Playback, [Binauralized](../mixing-terms#binaural)
##### Related Terms : 

---

### [Encode](../technical-terms#encode)
_Having audio content input into a spatial or multichannel soundfield._
##### Synonyms : [Pan](../mixing-terms#panning), [Panning](../mixing-terms#panning), Input to Spatial Soundfield
##### Related Terms :

---

### [Decode](../technical-terms#decode)
_Having spatial or multichannel soundfield content output for an intended two ear or two channel playback._
##### Synonyms : [Monitor](../mixing-terms#monitoring), [Monitoring](../mixing-terms#monitoring), [Listening](../mixing-terms#monitoring), Stereo Playback, [Binauralized](../mixing-terms#binaural), [Listener](../technical-terms#listener)
##### Related Terms : [Binaural](../mixing-terms#binaural)

---
## [Describing Rotations](../technical-terms#describing-rotation)
---

### [Azimuth](../technical-terms#azimuth)
_Refers to the horizontal angle or direction or rotation. Typically when discussing spatial audio a common example of usage of azimuth would be the azimuth of a sound source [panned](../mixing-terms#panning) around you as the [listener](../technical-terms#listener)._
##### Synonyms : Yaw
##### Related Terms : [Heading](../technical-terms#heading) 

---

### [Elevation](../technical-terms#elevation)
_Refers to the angular distance of the source above or below the horizon._
##### Synonyms : Height, Pitch
##### Related Terms : [Heading](../technical-terms#heading)

---

### [Heading](../technical-terms#heading)
A direction or bearing, combining the above terms of [Azimuth](../technical-terms#azimuth) and [Elevation](../technical-terms#elevation).

##### Synonyms : 
##### Related Terms : [Azimuth](../technical-terms#azimuth), [Elevation](../technical-terms#elevation)

---

### [Euler](../technical-terms#euler)
Description of rotations comprised of 3 angles. Commonly using: 
 - Yaw
 - Pitch
 - Roll / Tilt

but sometimes referred to as `X, Y, Z` in some 3D systems _(be mindful of the order in which `X, Y, Z` can refer to `Yaw, Pitch, Roll`)_

[Read more on this here.](https://research.mach1.tech/posts/describing-3d-motion)

##### Synonyms : 
##### Related Terms : [Degrees](../technical-terms#degrees), [Radians](../technical-terms#radians), [Gimbal Lock](../technical-terms#gimbal-lock)

---

### [Quaternion](../technical-terms#quat)
Mathematical notation for representing spatial orientations and rotations of elements in three dimensional space. Useful for [avoiding common issues when describing 3D](https://research.mach1.tech/posts/describing-3d-motion) rotations in [Euler](../technical-terms#euler) such as [Gimbal Lock](../technical-terms#gimbal-lock)
##### Synonyms : [Quat](../technical-terms#quat)
##### Related Terms : 

---

### [Degrees](../technical-terms#degrees)
Used to describe rotation angles in which a full rotation is `360` degree units. 

##### Synonyms : 
##### Related Terms : [Euler](../technical-terms#euler)

---

### [Radians](../technical-terms#radians)
Used to describe rotation angles in which a full rotation is `2π` or `6.28318530718`.

##### Synonyms : 
##### Related Terms : [Euler](../technical-terms#euler)

---
## [Spatial Audio: Common Issues](../technical-terms#commonissues)
---

### [Gimbal Lock](../technical-terms#gimbal-lock)
Gimbal lock is a loss of a degree of freedom when two axes rotate in parralel, the output rotation becomes one less degree of freedom.

To explain this more simply; two or more axes line up in a way so that the applied Euler rotation cannot distiguish which of the two axes are rotating because they yield the same results. 

_Example: If you add 90 pitch upward in degrees to an object, rotating yaw or roll would yield the same result._

##### Synonyms : 
##### Related Terms : [Euler](../technical-terms#euler)
 
---

### [Latency](../technical-terms#latency)
Describes when something has a latent or delayed reaction. Typically in spatial audio world we can describe headtracking or 3D rotations as being latent when you can percieve a time delay from your real world motion to the interacted virtual motion. This can be a very destructive issue for any hardware that has motion based sensors in them when applied to audio for spatial audio perception.

When discussing latency in the audio world in general it can refer to the actual audio signal itself having a perceived delay.

##### Synonyms : 
##### Related Terms : 

---
## [Additional Technologies](../technical-terms#tech)
---

### [IMU](../technical-terms#imu)
Stands for *I*nertial *M*otion *U*nit, a series of sensors usually within a silicon chip that can typically include any number of the following sensor types:
- Accelerometer
- Gyroscope
- Magnometer

Each of these sensor outputs can have typically 3 data outputs so the IMU typically includes a process called [Sensor Fusion](../technical-terms#sensor-fusion) to combine the datasets of all sensors into one dataset for orientation and/or position.
##### Synonyms : 
##### Related Terms : [Sensor Fusion](../technical-terms#sensor-fusion)

--- 

### [Sensor Fusion](../technical-terms#sensor-fusion)
Sensor Fusion is a a mathematics for combining multiple datasets relating to motion or force into one dataset for predicting orientation, [heading](../technical-terms#heading) and/or position. The output data can be collected into different types such as [Radians](../technical-terms#radians) or [Degrees](../technical-terms#degrees) or [Quaternion](../technical-terms#quat).

##### Synonyms : 
##### Related Terms : 

---
## [Technical Descriptions](../technical-terms#techdesc)
---

### [Realtime](../technical-terms#realtime)
_Refers to a process or effect that can be applied in realtime, usually during playback but in general any process that can be computed faster than actual time._

##### Synonyms : 
##### Related Terms : 

---

### [Runtime](../technical-terms#runtime)
_Refers to all processes that happen during the playback of the sound content._

`Spatial audio` processes that are limited to runtime processes have to compensate for what processing power is available on that device, this limitation means that these processes have to be able to run faster than realtime and can sometimes be limited in quality.

##### Synonyms : 
##### Related Terms : 

---

### [Render](../technical-terms#render)
_Refers to a process of pre-determining all intended processes and effects to an output file usually to be faithfully replayed or reused without change._ 

`Spatial audio` content that has been pre-rendered or rendered has the added benefit of using more time expensive and higher quality processing effects that might not normally be too expensive to be processed in realtime, especially from device to device.

##### Synonyms : 
##### Related Terms : 

---

### [A-Format]({{< ref "/glossary/technical-terms#a-format" >}})
A often misused term describing multichannel soundfields or multi-mic arrays that **Is not ambisonics** but is sometimes used as to create a multichannel source that later can be encoded into ambisonics.

##### Synonyms : 
##### Related Terms : 

---

### [B-Format]({{< ref "/glossary/technical-terms#ambisonics" >}})
A synonym for an ambisonic encoded soundfield.

##### Synonyms : [Ambisonics]({{< ref "/glossary/technical-terms#p-format" >}})
##### Related Terms : 

---

### [T-Format]({{< ref "/glossary/technical-terms#t-format" >}})
A often misused term describing multichannel soundfields or multi-mic arrays that **Is not ambisonics** but is sometimes used as to create a multichannel source that later can be encoded into ambisonics.

##### Synonyms :
##### Related Terms : 

---

### [P-Format]({{< ref "/glossary/technical-terms#p-format" >}})
A often misused term describing multichannel soundfields or multi-mic arrays that **Is not ambisonics** but is sometimes used as to create a multichannel source that later can be encoded into ambisonics.

##### Synonyms : 
##### Related Terms : 

---

### [C-Format]({{< ref "/glossary/technical-terms#c-format" >}})
Describes a **partially ambisonics** multichannel file where 2 of the channels are decoded from ambisonics the rest of the channels replicate ambisonic domain concepts to replicate the source ambisonic material. Was suggested as a temporary means of distribution to ensure that the first two channels can be played back safely on all systems as they are decoded from ambisonics into traditional stereo.

##### Synonyms : 
##### Related Terms : 

---

### [D-Format]({{< ref "/glossary/technical-terms#d-format" >}})
**Is not ambisonics**: multichannel decoding from an ambisonic source

##### Synonyms : 
##### Related Terms : 

---

### [E-Format]({{< ref "/glossary/technical-terms#e-format" >}})
**Is not ambisonics**: multichannel decoding from an ambisonic source

##### Synonyms : 
##### Related Terms : 

---

### [G-Format]({{< ref "/glossary/technical-terms#g-format" >}})
**Is not ambisonics**: 5.1 multichannel decoding from an ambisonic source

##### Synonyms : 
##### Related Terms : 

---