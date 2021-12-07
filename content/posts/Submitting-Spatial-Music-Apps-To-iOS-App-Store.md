---
title: "Submitting Spatial Music Apps to iOS App Store"
date: 2021-11-22T10:10:05-04:00
---

_Last Updated: 2021-11-29_

## Introduction 
At the time of writing this post ["spatial audio"]({{< relref "posts/spatial-audio-defined-by-different-companies" >}}) seems to be a term that has many varying meanings in the market. However we know the common expectation for spatial audio should include perceivable audio interactivity from a listener's headtracking or motion of some kind, otherwise we are just making more methods of distributing stereo mixes to listeners with more complex forms of run time processing to fit the "binaural stereo" category. Ultimately if you are an artist or label that wants to retain control how your spatial music soundfields are handled and played to the end user, currently the best method would be making your own app and leveraging 3rd party IMU/motion APIs (such as CMHeadphoneMotionManager/CMMotionManager from Apple, or BoseAR from Bose, or even a custom API, etc.) and applying that motion data to your preferred end target spatial audio "format". For the sake of this post we will only be referring to using Mach1 Spatial SDK and simple vector based panned or SPS soundfields as that preferred spatial audio framework. However this would also apply to other use cases such as: ambisonic player, headtracking augmented Dolby Atmos player, Mach1 Spatial SDK being used for both the aforementioned players, etc.

We want to go over our experience of submitting an app to handle a use case of spatial audio not supported by any conventional audio distribution pipeline currently offered by Apple. We hope we can save the next developers some time with this post!

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
    <p class="etxt">Resubmitted app with improvements</p>
  </div>
  <div class="event">
    <strong class="edate">06 Dec 2021</strong>
    <p class="etxt">Rejection: No Reason <br>(Apple representative to schedule a call to explain rejection)</p>
  </div>
    <div class="event">
    <strong class="edate">08 Dec 2021</strong>
    <p class="etxt"></p>
  </div>
</div>

## Summary of Issues
 1. App Store Review will reject "music" in the app and recommend distributing via iTunes
 2. iOS SDK currently does not support background audio/music with processing requirements
 3. Juggling motion managers
 4. App Store Review will require various App Privacy Descriptions

### Common Rejections seen when distributing a spatial music or spatial audio iOS app

#### `4. 2 Design: Minimum Functionality` Music Distribution Conflict
Apple seems to by default reject music packaged in an app, stating that you should instead distribute the music via iTunes under `4. 2 Design: Minimum Functionality`

##### Solutions
Simply just reply to the rejection and even appeal if needed with a message saying that iTunes does not distribute or playback spatial music as intended by the artist and label and until it does making an app is the only way to distribute the spatial music or spatial audio playback as intended and mixed.

_(We are currently in the process of appeal for this rejection reason, we will keep this thread updated as the results and best options for solutions.)_

#### `4. 2 Design: Minimum Functionality` Audio Player UX
Apple expects some minimum UX when it comes to an audio player like UI for their users, you will likely face rejections unless you have some of the following functional UX/UI for your spatial audio player:
 - Play / Stop controls
 - Playhead controls and seek controls
 - Next/Previous mix controls

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