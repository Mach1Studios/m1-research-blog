---
title: "Feedback on Apple's Spatial Audio Implementation"
date: 2021-03-08T03:10:00-04:00
lastmod: 2021-03-08T03:10:00-04:00
draft: false
---
---
The Mach1 Spatial team is adamant about sharing tools and info to help the community build mediums revolving around spatial audio and headtracking audio. We wanted to share some feedback we had regarding Apple's approaches and what the next steps could be for them. 
We have been tracking and collating tools for various headtracking and IMU enabled devices as we find them and [summarizing them here](https://research.mach1.tech/imu-enabled-devices).
This includes examples we make to evaluate headtracking hardware (and used for this post) such as: https://github.com/Mach1Studios/M1-AirPodOSC

## Issues and Feedback on Apple's Spatial Audio

In the initial implementations using [CMHeadphoneMotionManager](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager) we noticed a few things developers and Apple might want to resolve:
 
 - The orientation data from Pitch & Roll head rotations for 5.1 mixes break the playback completely, think about maybe blocking usage of Pitch or Roll rotations from the head if the audio content does not support "height" within the audio mix such as the surround mixes in distribution currently.

---

<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/feedback-on-apples-spatial-audio/roll-issue.gif" alt="" style="width:50%;display:block;margin-left:auto;margin-right:auto;">

_Tilting/Rolling your head left or right rotates the audio mix making it more apparent in left or right ear, something that is obviously not intended with a 5.1 mix off of Hulu!_

---

- The HRTF filter/room modeling is completely destructive to the audio mix, have you thought about using a simpler and transparent approach? 
We have a [framework to help developers](https://www.mach1.tech/developers) and [creators work with spatial audio](https://www.mach1.tech/spatial-system) in a completely transparent and intuitive way, we are very nervous about introducing early on HRTF filter/room modeling processes to mixes to induce spatialization effects, this can be a bad way to start educating consumers on spatial audio by having them get acquainted to mix altering and noisey effect processes so early on.

- On the similar topic, we would love to discuss expanding inputs to beyond just 5.1 and select Atmos support, and answering the common trouble points such as how all consumers or professionals can use your headtracking devices beyond just some hardcoded usage examples. Developers and creators should have limitless ways to utilize [CMHeadphoneMotionManager](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager).

## Feedback on SDK Implementation

- While looking at the [CMHeadphoneMotionManager](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager), it would be amazing to extend this beyond iOS SDK to all other SDKs (and more??!?).
We are sure this is already the plan but just wanted to express the request directly.

- When directly using the [CMHeadphoneMotionManager](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager), we can see that your two devices (AirPods Pro and AirPods Max) have different relative Euler orientation outputs, this is just an unnecessary pitfall to throw at developers proceeding forward, maybe also its important to have the hardware teams designing around the IMU sensors to keep in mind placement and keeping things as streamlined as possible to developers UX wise down the line. 

[Example video posted on Facebook](https://www.facebook.com/590732605/videos/10158158827442606/)

_Some other recommendations include returning some device description so Developers have a way to maintain rotation differences between AirPod Pro vs Air Pod Max (and other upcoming devices). If the APIs can also have ways to switch relative and absolute orientation usage to give developers more tools to calibrate or improve tracking themselves it could help with more options as well._

---

If you are interested in the growing new mediums using spatial audio feel free to explore our framework and exploration in headtracking while we wait for more consumer devices to have IMUs embedded.
We also have some spatial audio demos that can be listened to: https://demos.mach1.tech/ 
which is all built from https://github.com/Mach1Studios/m1-web-spatialaudioplayer