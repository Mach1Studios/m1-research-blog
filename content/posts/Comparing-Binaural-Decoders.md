---
title: "Comparing Binaural Decoders"
date: 2017-06-05T03:10:05-04:00
lastmod: 2017-06-05T03:10:05-04:00
draft: false
---

## Introduction 

In this post we will decode implemented spatial audio decoders and associated binaural filters and other HRTF effect processes. At the time of this testing we are selecting available ambisonic players and plugins as well as the Mach1 Spatial VVBP approach. 

The following are comparison of audio encoded into the following formats and decoded back to stereo in an effort to hear and compare audio processed in different spatial audio formats. Note that this comparison is only looking into fixed decoded positions to compare audio degradation and stereo imagery on decoding, a large portion of spatial audio format comparisons should also derive on the effect of orientation/directional audio, which will be the proceeding test subject (results were decoded .wav, if on IE you will be hearing an .mp3 conversion).

All audio comes from the same source, and are decoded as if the user/player was orientated looking forward with Euler angles: yaw, pitch, roll. All audio is gain matched to make comparisons easier, it should be noted that some of these decoding formats have less dynamic gain range which this comparison demonstration does not illustrate and is another major feature to M1 Spatial which supports a fuller dynamic range than any ambisonic related spatial audio format.

## Comparisons

<p>
    <h4>Source Stereo</h4>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/wav/WhiteNoise_CleanStereo.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/mp3/WhiteNoise_CleanStereo.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>
<p>
    <h4>Mach1 Spatial</h4>
      <p><i></p></i>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/wav/WhiteNoise_M1_Spatial.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/mp3/WhiteNoise_M1_Spatial.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>
<p>
    <h4>Ambisonic ACNSN3D AmbiX Youtube HRTF</h4>
      <p><i>Notes: stereo image altered, binaural filter colors mix, less dynamic range)</p></i>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/wav/WhiteNoise_ENC_AmbiX_AmbiPan_DEC_Ambihead_YoutubeHRTF.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/mp3/WhiteNoise_ENC_AmbiX_AmbiPan_DEC_Ambihead_YoutubeHRTF.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>
<p>
    <h4>Ambisonic FuMa SurroundZone Decoded</h4>
      <p><i>Notes: stereo image altered, less dynamic range)</p></i>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/wav/WhiteNoise_ENC_AmbiPan_Fuma_DEC_SurroundZone.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/mp3/WhiteNoise_ENC_AmbiPan_Fuma_DEC_SurroundZone.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>
<p>
    <h4>Ambisonic AmbiX Noisemaker HRTF</h4>
      <p><i>To compare different filtering schemes applied to mix.</p></i>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/wav/WhiteNoise_ENC_AmbiPan_AmbiX_DEC_Ambihead_NoisemakersHRTF.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/mp3/WhiteNoise_ENC_AmbiPan_AmbiX_DEC_Ambihead_NoisemakersHRTF.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>
<p>
    <h4>FB360</h4>
      <p><i>Notes: not using attenuation or room settings, mix sources clipping due to sum</p></i>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/wav/WhiteNoise_FB360.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/mp3/WhiteNoise_FB360.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
    <br>
</p>
<!-- <p>
    <h4>Source Stereo (Warning: Loudest Sample)</h4>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/wav/stereosource.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/mp3/stereosource.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>
<p>
    <h4>Ambisonic AmbiX FOA (Youtube ACNSN3D)</h4>
      <p><i>Notes: stereo image drastically altered, binaural filter colors mix, slight gain reduction, less dynamic range)</p></i>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/wav/ambix_forward.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/mp3/ambix_forward.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>
<p>
    <h4>Ambisonic ACNSN3D Decoding without Binaural Filters</h4>
      <p><i>Notes: stereo image drastically altered, slight gain reduction, less dynamic range)</p></i>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/wav/*.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/mp3/*.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>
<p>
    <h4>Mach1 Spatial</h4>
      <p><i>Notes: slight gain reduction</p></i>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/wav/m1spatial_forward.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/mp3/m1spatial_forward.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>
<p>
	<h4>FB360</h4>
      <p><i>Notes: not using attenuation or room settings, mix sources clipping due to sum</p></i>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/wav/fb360_forward.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/mp3/fb360_forward.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br> 
</p> -->

## Additional Ambisonic AmbiX FOA (Youtube ACNSN3D)
<p>
      <p>To compare different filtering schemes applied to mix.</p>
      <h4>Decoded Facing Upward</h4>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/wav/ambix_up.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/mp3/ambix_up.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>
<p>    
    <h4>Decoded Facing Downward</h4>
      <audio controls="controls">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/wav/ambix_down.wav" type="audio/wav">
      <source src="https://mach1-research-public.s3.amazonaws.com/posts/resources/compare-binaural-decode/audio/mp3/ambix_down.mp3" type="audio/mp3">
      Your browser does not support the audio element.</audio>
    <br>
</p>

<p></p>

*Notes: M1Spatial does not add additional filter processing during decoding/playback, directionality deteremined by audio engineer supplying pre-rendered filters/delays in traditional mix workflow. Due to this it is redundant to show dry converted comparisons to M1Spatial without mix engineer creative additions.*