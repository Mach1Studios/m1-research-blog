---
title: "Submitting Spatial Music Apps to iOS App Store"
date: 2021-11-22T10:10:05-04:00
lastmod: 2022-01-21T10:10:05-04:00
draft: false
---

## Status
- Minimum Features for Single Artist Music App: **TBD**
  - Play controls and common audio player UI/UX
  - Additional media *(not confirmed)*
  - Fan interaction features
  - Documentation to the App Review Board explaining your use of "spatial audio"
<br>
- Minimum Features for Music Distribution Platform (multiple artists): **Not Confirmed**
  - Play controls and common audio player UI/UX

## Introduction

At the time of writing this post ["spatial audio"]({{< relref "posts/spatial-audio-defined-by-different-companies" >}}) seems to be a term that has many varying meanings in the market. However we know the common expectation for spatial audio should include perceivable audio interactivity from a listener's headtracking or motion of some kind, otherwise we are just making more methods of distributing stereo mixes to listeners with more complex forms of run time processing to fit the "binaural stereo" category. Ultimately if you are an artist or label that wants to retain control how your spatial music soundfields are handled and played to the end user, currently the best method would be making your own app and leveraging 3rd party IMU/motion APIs (such as CMHeadphoneMotionManager/CMMotionManager from Apple, or BoseAR from Bose, or even a custom API, etc.) and applying that motion data to your preferred end target spatial audio "format". For the sake of this post we will only be referring to using Mach1 Spatial SDK and simple vector based panned or SPS soundfields as that preferred spatial audio framework. However this would also apply to other use cases such as: ambisonic player, headtracking augmented Dolby Atmos player, Mach1 Spatial SDK being used for both the aforementioned players, etc.

We want to go over our experience of submitting an app to handle a use case of spatial audio not supported by any conventional audio distribution pipeline currently offered by Apple. **The goal is to track the bare minimum for distributing a spatial music app via App Store Review until iTunes and other pipelines support spatial audio formats.** We hope we can save the next developer, musician or artist some time with this post!

## Submission Tracking Timeline
This section will track our progress of submitting and handling common issues we saw when trying to distribute a spatial audio app on the iOS App Store.

<div class="vtl">
  <div class="event">
    <strong class="edate">15 Nov 2021</strong>
    <p class="etxt">App development started forking:<br><a href="https://github.com/Mach1Studios/Pod-Mach1SpatialAPI/tree/master/Examples/mach1-encode-example">SDK example</a></p>
  </div>
  <div class="event">
    <strong class="edate">17 Nov 2021</strong>
    <p class="etxt">Rejection: Improve UI/UX for minimal audio playback controls <br><b>[4.2 Design: Minimum Functionality]</b></p>
  </div>
  <div class="event">
    <strong class="edate">21 Nov 2021</strong>
    <p class="etxt">Resubmitted app with requested improvements</p>
  </div>
  <div class="event">
    <strong class="edate">21 Nov 2021 - 06 Dec 2021</strong>
    <p class="etxt">Waiting for Apple's manual review</p>
  </div>
  <div class="event">
    <strong class="edate">06 Dec 2021</strong>
    <p class="etxt">Rejection: No Reason <br>(Apple representative asks to schedule a call to explain rejection)</p>
  </div>
    <div class="event">
    <strong class="edate">06 Dec 2021 - 08 Dec 2021</strong>
    <p class="etxt">Waiting for Apple's explanation</p>
  </div>
  <div class="event">
    <strong class="edate">08 Dec 2021</strong>
    <p class="etxt">Apple call explanation<br>No recommendations given</p>
  </div>
  <div class="event">
    <strong class="edate">08 Dec 2021</strong>
    <p class="etxt">Appeal to App Review Board submitted<br>Recommendation: add more supplemental content such as video</p>
  </div>
  <div class="event">
    <strong class="edate">08 Dec 2021</strong>
    <p class="etxt">Development of additional video content features to explore "minimum required features"</p>
  </div>
  <div class="event">
    <strong class="edate">10 Dec 2021</strong>
    <p class="etxt">Submitted a new minimum designed app that includes accompanying video to test App Store Review acceptance</p>
  </div>
  <div class="event">
    <strong class="edate">02 Jan 2022</strong>
    <p class="etxt">Apple rejects app<br>Apple confirms single artist/album spatial music distribution is not allowed as an app</p>
  </div>
  <div class="event">
    <strong class="edate">05 Jan 2022</strong>
    <p class="etxt">Apple Review Board appeal call<br>Apple acknowledges difference between spatial audio as a format vs how iTunes supports spatial playback as a processing effect<br>Apple recommends adding <b>more</b> fan interaction</p>
  </div>
  <div class="event">
    <strong class="edate">06 Jan 2022</strong>
    <p class="etxt">Resubmitted app with <b>more</b> fan interaction UI/UX</p>
  </div>
  <div class="event">
    <strong class="edate">07 Jan 2022</strong>
    <p class="etxt">Apple rejects app<br>Reviewer inadequetly reviewed app<br>Claims 2.5.1 guideline<br>Claims the same 4.2 guideline regarding music distribution</p>
  </div>
  <div class="event">
    <strong class="edate">19 Jan 2022</strong>
    <p class="etxt">Apple calls from appeal board<br>rejection upheld<br>no recommendation<br>Apple states they will call in a week with more information</p>
  </div>
</div>

## Summary of Issues
 1. App Store Review will reject "music" in the app and recommend distributing via iTunes
 2. iOS SDK currently does not support background audio/music with processing requirements
 3. Juggling motion managers
 4. App Store Review will require various App Privacy Descriptions

### Common Rejections seen when distributing a spatial music or spatial audio iOS app

#### `Guideline 4.2 - Design - Minimum Functionality` Music Distribution Conflict
Apple seems to by default reject music packaged in an app, stating that you should instead distribute the music via iTunes under `4.2 Design: Minimum Functionality`

##### Example Response from Apple:
```
Your app seems to be primarily a single song album and is therefore not appropriate for the App Store.

Next Steps:
Songs and movies should be submitted to the iTunes Store. If you wish to distribute your content as an app, please review your app concept and incorporate different content and features that are in compliance with the App Store Review Guidelines.
```

Unfortunetly, the above error from Apple may mean that you are stuck. They deem that single instances of spatial music should only be distributed via iTunes despite iTunes not supporting spatial audio. **This is a deadend and a serious roadblock created by Apple due to their poor judgement and lack of understanding spatial audio as a medium instead of only as a processing or playback effect.**

The interesting thing about this response is this line: `If you wish to distribute your content as an app, please review your app concept and incorporate different content and features that are in compliance with the App Store Review Guidelines.` After many attempts (adding video content and various graphical content components) it was confirmed by Apple's Review Board representatives that this is a red herring and that nothing would be accepted until it was not a piece of spatial music any more. 

Rejection responses describe that they believe this is just an enhancement of traditional stereo audio instead of recognizing how this is a new format or medium entirely and not just a gimmicky playback feature. It is a shame that Apple's App Store Review Board does not understand what spatial audio is as a format and that there is no possible route for distributing spatial music via iTunes as they deem "spatal audio" to be limited to a processing effect as we hear it used via their implementation with AirPods, and not a mixing format as used by many to create spatial soundfields to create new experiences.

Additional appeals failed despite following the Review Board's advice for adding more multimedia content. We have been carefully reviewing [the referenced guideline](https://developer.apple.com/app-store/review/guidelines/#minimum-functionality) and are appealing the decision by explaining that a spatial music app is "unique" and "app-like" since there is **NO OTHER WAY FOR AN ARTIST TO DISTRIBUTE SPATIAL MIXES THEY CREATED AND LEVERAGE [CMHEADPHONEMOTIONMANAGER](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager) API**

##### Update
Apple has acknowledged the difference and distinction between spatial audio as a rendered soundfield mix and "spatial audio" as a processing playback effect. In a call with the App Review Board they challenged our claim that iTunes does not support "spatial audio" saying we should ask the artist to use the dedicated ["Apple Spatial Audio"]({{< relref "posts/observations-and-limitations-of-apple-spatial-playback-implementation" >}}) playback on iTunes. We discussed with the review board the difference between spatial audio soundfield mixes created by an artist or engineer via a multichannel format (whether Mach1 Spatial, ambisonics or an object based format) compared to what iTunes does not which is adding a "spatial playback effect" to specific Dolby or Sony based formats without disgression from the artist. They thankfully seemed to acknowledge this difference and recommend adding more fan interaction (merchandise purchase link or event ticket links) to the app to make it more of an interactive experience. They also asked to include notes on documentation of this distinction as well as any feedback from the artist/musicians involved endorsing the app.

**We will follow this advice and report back on what the minimum required development is for an artist or label to distribute their own spatial soundfields via an app.**

##### Update
Using the appeal board lead to the same conclusion, they acknowledged that we went beyond the intended UX of the app by adding everything Apple recommended us to add despite us disagreeing with the additions. They also acknowledged that there is no alternative form of distribution suitable for the spatial music content in the app, however they still upheld the rejection providing no additional real feedback or recommendations. They did say they will review all the content and this specific usecase and setup a follow up call since they were unable to provide next steps.

During the call they were suggesting we create a spatial music platform for multiple artists, which we said was not at all our attention, Apple then recommended making an app that is more encompassing for the artist, "adding more content about the artist would improve the return rate for users to the app", however we explained we are only responsible for creating an interactive audio experience for this single piece of content and are not responsible for making a content management app for the artist. After this exchange Apple seems to acknowledge our use case and intended UX and we are hoping they review with more scrutiny. Apple seems to be receptive to interactive spatial music content in an app as a side feature or bonus content, but not when the app is centered around spatial music or spatial content as the focus of the app.

#### `Guideline 4.2 - Design - Minimum Functionality` Audio Player UX
Apple expects some minimum UX when it comes to an audio player like UI for their users, you will likely face rejections unless you have some of the following functional UX/UI for your spatial audio player:
 - Play / Stop controls
 - Playhead controls and seek controls
 - Next/Previous mix controls

#### `Guideline 2.5.1 - Performance - Software Requirements`
Apple might give a rejection with a response along the lines of:
```
During review, we were prompted to provide consent to access the Motion & Fitness Activity information. However, we were not able to locate any features in your app that use the Motion & Fitness Activity information.
```
This should be an easy one to respond to since its clear the reviewer didn't spend too much time reviewing the app if they did not understand that motion data was used for playing back the spatial soundfield of the audio mix. Just remind them in a response that you use the motion data for audio related reasons to make the audio mix interactively to the user via CMHeadphoneMotionManager API and/or CMMotionManager API.

### Motion Management
In any case that your spatial music or audio app requiring orientation to properly decode a binauralized stereo listening experience you will have to design a management system for handling all the possible input orientation data from different IMU sources.

We will update our examples and this post with UX best practices we discover however this should be designed on a case by case instance.

#### Handling default native onboard IMU (the iPhone/iPad IMU) 
We have found that this is a great IMU source to capture by default as not everyone will have IMU enabled headphones or 3rd party peripherals, in our design we think of this as the lowest common denominator of motion input. We also like to disable pitch and roll when using a native device IMU so that we can focus on yaw and treat it more like a compass that correctly outputs no matter how the device is being held or interacted with. This ensures safe usage since we cannot easily predict how the user is holding the device. All of that said we think the best UX is one that has some instruction to a user before the listening experience to improve correct orientation usage. 

#### Handling Apple supported Headphones with IMUs
Thankfully there is a nicely [consolidated API for handling all Apple supported IMU enabled headphones](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager), the only downside is it currently is limited to the iOS SDK at the time of writing this post. Currently we have had sucess with starting the native device IMU `CMMotionManager.startDeviceUpdates()` as one thread and the `CMHeadphoneMotionManager.startDeviceUpdates()` as another async thread and using a logic to only update global orientaion variables with the correctly intended motion manager as needed. 

[Example thread for `CMMotionManager`](https://github.com/Mach1Studios/Pod-Mach1SpatialAPI/blob/master/Examples/mach1-decode-example/mach1-decode-example/ViewController.swift#L180-L221) \
[Example thread for `CMHeadphoneMotionManager`](https://github.com/Mach1Studios/Pod-Mach1SpatialAPI/blob/master/Examples/mach1-decode-example/mach1-decode-example/ViewController.swift#L223-L264)

#### BoseAR Motion Support
Currently the BoseAR SDK is not publically available, we are hoping this changes in the near future in which case we will promptly update our examples and this post on the some ideal best practices for handing the UX and motion managers along with others.

#### 3rd Party IMU
Supporting other IMUs via OSC or via bluetooth directly is also possible, we hope others will contribute here with examples of best practices.

### Background Motion and Audio Handling
Allowing spatial music and audio play as intended with updating orientation and binauralized spatial playback enters a new challenge when developing an app that enters background mode (or is terminated). 

We are currently investigating the best ways to allow spatial audio processing and playback in background mode with orientation still updating. So far we are looking into using the Location Services to allow background processing as this seems to be the only background thread safe API available. We will update this post with recomended solutions as they become available. 

<style>
/* (A) "SET" THE TIMELINE CONTAINER */
.vtl {
  /* (A1) RELATIVE POSITION NECESSARY TO PROPERLY POSITION TIMELINE LATER */
  position: relative;
  /* (A2) RESERVE MORE SPACE TO THE LEFT FOR THE TIMELINE */
  padding: 10px 10px 10px 50px;
  /* (A3) OPTIONAL WIDTH RESTRICTION */
  max-width: 400px;
}

/* (B) DRAW TIMELINE USING ::BEFORE */
.vtl::before {
  /* (B1) DRAW THE TIMELINE */
  content: '';
  width: 5px;
  background-color: #808080;
  /* (B2) POSITION IT TO THE LEFT */
  position: absolute;
  top: 0;
  bottom: 0;
  left: 15px;
}

/* (C) STYLES FOR THE EVENTS */
div.event {
  padding: 20px 30px;
  background-color: #929292;
  position: relative;
  border-radius: 6px;
  margin-bottom: 10px;
}

/* (D) STYLES FOR THE DATE & TEXT */
strong.edate {
  font-size: 1.1em;
  font-weight: bold;
  color: #202020;
}
p.etxt {
  margin: 10px 0 0 0;
  color: #404040;
}

/* (E) ADD "SPEECH BUBBLE TRIANGLE" TO THE EVENTS */
div.event::before {
  content: '';
  border: 10px solid transparent;
  border-right-color: #929292;
  border-left: 0;
  position: absolute;
  top: 20%;
  left: -10px;
}

/* (F) ADD A CIRCLE ON THE TIMELINE TO INDICATE AN EVENT */
div.event::after {
  content: '';
  background: #fff;
  border: 4px solid #808080;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  position: absolute;
  top: 20%;
  left: -41px;
}

/* (X) DOES NOT MATTER */
html, body { font-family: arial, sans-serif; }
</style>