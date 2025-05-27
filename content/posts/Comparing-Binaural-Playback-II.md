---
title: "Comparing Binaural Playback/Decoders (Part II)"
date: 2021-10-01T03:10:05-04:00
lastmod: 2021-10-01T03:10:05-04:00
draft: false
---

## Introduction 
This post is a continuation of an exploration that prompted the development of an agnostic and process free multichannel/spatial audio framework that became the Mach1 Spatial SDK. In an effort to help showcase the sonic differences and usability of the current spatial audio market we are rendering various different format tests to sonically compare them without use of additional hardware, making A/B comparisons a little more accessible. It is recommended to create your own local tests and compare mixes played back in different means with headtracking active to further expose limitations. 

These tests are focusing only on headtracking implementation, for comparisons that also compare coloration from HRTF or room modeling related processing please listen to the comparisons from [Comparing Binaural Decoders]({{< relref "posts/comparing-binaural-decoders" >}}).

## Comparisons

### Test Case #1: Front Facing Rendered Playback
The following includes a spatial audio mix conformed to the required "format" per app/player and recorded as the binaural playback is facing forward only.

<p>
    <h4>Mach1 Spatial - Front Facing</h4>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/Mach1Spatial-Forward-Render.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/Mach1Spatial-Forward-Render.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>
<p>
    <h4>Facebook360 - Front Facing</h4>
      <p><i></p></i>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/FB360-Forward-Render.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/FB360-Forward-Render.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>
<p>
    <h4>YouTube360 - Front Facing</h4>
      <p><i></p></i>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/YT360-Forward-Render.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/YT360-Forward-Render.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>
<p>
    <h4>Apple Spatial - Front Facing</h4>
      <p><i></p></i>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/AppleSpatial-Forward-Render.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/AppleSpatial-Forward-Render.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>

### Test Case #2: Front / Back Soundfield Comparison
The following illustrate how an intended soundfield mix is altered (or not) to accomondate headtracking. It also serves as a way to compare headtracking results sonically and note on the limitations added to introduce headtracking by some poorly implemented vendors.

_Both of these "Right Facing" examples were taking by listening to the spatial mix with headtracking enabled headphones and turning +90 degrees to the right to hear the front side of the mix in the left ear and the rear side of the mix in the right ear._

 <p>
    <h4>Mach1 Spatial - Right Facing</h4>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/Mach1Spatial-RightFacing-Render.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/Mach1Spatial-RightFacing-Render.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>

The Above is the intended spatial mix, with specifically designed reflections in the rear which could be heard in the right ear, while the Apple Spatial playback of Dolby Atmos version of this mix has shrunken the soundfield and reduced the difference of front to back in the soundfield because it is designed to support only forward facing use cases and alters any mix inputted without bias. 

<p>
    <h4>Apple Spatial - Right Facing</h4>
      <p><i></p></i>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/AppleSpatial-RightFacing-Render.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/AppleSpatial-RightFacing-Render.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>

We recommend comparing the results of headtracking on your own, please download the source mix files below and follow the steps to setup a comparison locally.

<a href="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/downloads/M1-Orchestra_Mach1Spatial.wav" download>Download Mach1 Spatial audio file</a>
[Test Mach1 Spatial audio file here](https://demos.mach1.tech/#Music-Orchestra)

<a href="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/downloads/M1-Orchestra_YT360.mp4" download>Download Youtube360 uploadable file</a>

<a href="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/downloads/M1-Orchestra_FB360_3D.mp4" download>Download Facebook360 uploadable file</a>

<a href="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-playback-ii/downloads/M1-Orchestra_Atmos-to-Apple51.mp4" download>Download Sideloadable Apple Spatial file from Dolby Atmos</a>
[File]