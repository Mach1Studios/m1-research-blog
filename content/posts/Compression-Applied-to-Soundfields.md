---
title: "Compression Applied to Soundfields"
date: 2019-09-05T03:11:53-04:00
lastmod: 2019-09-05T03:11:53-04:00
draft: false
---
---
## Targets of Testing
To determine the value of compression in terms of file reduction compared to the quality of retaining the compression across the whole soundfield evenly. Also with discussion of the comparison of typical value of file reduction compared to the quality of resulting decompressed audio files. Also exploring if VBR compression types are safe to use on channel dependent soundfield material.

### Codecs Tested
- OPUS via libopus
- VORBIS via libvorbis
- MP3 via LAME
- AAC via FFMPEG Native AAC

#### Codecs To Test
- AAC via FDKAAC
- AAC via apple

## Test Material
- Test 1: Wideband noise material in 90 degree offset combined into a soundfield with a narrowband saw wave @ 2kHz in the front direction and a sine tone panned 90 degree to the left.

## Methodology
  For this test, we used ffpmeg to convert the original wave files to the targeted codec format, and decompress them back to the wave files. The goal of this process was to compare the decompressed waves with the original and build procedures to fundamentally compare their quality and analyze which codec format would be the closest to the original file. The chosen codec format were as follows:

| Codec      | Bitrate/Quality | Bitrate Mode |
|:---------- |:------------| --- |
| AAC        | 16             | Constant        |
| AAC        | 48             | Constant        |
| AAC        | 320            | Constant        |
| AAC        | 0.1            | Variable        |
| AAC        | 2              | Variable        |
| AAC        | 10             | Variable        |
| VORBIS     | 0              | Variable        |
| VORBIS     | 10             | Variable        |
| VORBIS     | 0              | Variable        |
| OPUS       | 16             | Constant        |
| OPUS       | 32             | Constant        |
| OPUS       | 96             | Constant        |
| OPUS       | 8              | Variable        |
| OPUS       | 32             | Variable        |
| MP3        | 320            | Constant        |
| MP3        | 30             | Variable        |
| MP3        | 260            | Variable        |

## First Test Case
To proceed, a mean over the total time of the Magnitude Squared Coherence Estimate was taken between the source PCM audio and the codec's decompressed PCM of each compression and quality to get the `Correlation Percent`.
  
The `Time Difference` was calculated by comparing the number of samples in the source PCM audio file to the number of samples in the decompressed PCM of each compression and quality. 
  
Figure below, depicts the accumulated results:

## Results of File Size
| Codec         | Filesize after Compression  | Correlation Percent\*  | Time Difference\*\* | Multichannel Support | 
| ------------- |:-------------:| ---  | ---    | --- | --- |
| Source WAV    | 7.1MB         |  --100%--   | --     | Yes                         
| VORBIS Q0     | 476KB         | 45.85% | 0.0054% | Yes
| VORBIS Q3     | 696KB         | 66.16% | 0.0054% | Yes
| VORBIS Q7     | 1.1MB         | 88.28% | 0.0054% | Yes
| VORBIS Q10    | 2.2MB         | 98.81% | 0.0054% | Yes
| OPUS C16      | 168KB         |  22.71% | 0.065%  | Yes
| OPUS C32      | 328MB         | 37.78% | 0.065%  | Yes
| OPUS C96      | 969KB         |  81.41%  | 0.065%  | Yes
| OPUS V8       | 63KB          |  16.86%  | 0.065%  | Yes
| OPUS V16      | 166KB         |  23.09%    | 0.065%  | Yes
| OPUS V32      | 478KB         | 51.66% | 0.065%  | Yes
| AAC C16       | 189KB         | 21.21% | 0.31%   | Yes
| AAC C48       | 511KB         | 46.01% | 0.31%   | Yes
| AAC C320      | 2.4MB         | 98.89% | 0.31%   | Yes
| AAC V0        | 437KB         |   51.78%   | 0.31%   | Yes
| AAC V0.1      |  45KB         |    12.44%\*\*\*  | 0.31%   | Yes
| AAC V2        | 1.3MB         |   91.00%   | 0.31%   | Yes
| AAC V10       | 2.1MB         |   99.67%   | 0.31%   | Yes
| MP3 C320      | 3.2MB         |   91.73%   |       | No
| MP3 V30       | 323KB         |   29.61%   |       | No
| MP3 V260      | 2.68MB        |   91.64%   |     | No

\*  _Only for showing decoded signal difference without compensating for time domain changes due to codec_ _(not conclusive, see \#Limitations section for more information)_

\*\* _Calculated after decoding back to PCM and comparing number of samples_

\*\*\* Possible exploit issue in command of compression settings, not definitive

## Observations for the First Test Case

- AAC: This compression consistently changes the time domain which may be less safe/ideal for soundfield audio (multichannel). aac native lib of ffmpeg also did not seem to be the best version of AAC tested so far.
- Vorbis: This was the most consistent codec in terms of de-compressing back the results closest to source, even when material was noise/wideband related
- Opus: This codec did a fair job and maintaining consistency on harmonic material (might be better for music related material) but did not perform as well on wideband sound material (maybe less ideal for some content and most sound design content)

It is important to mention that many of the codecs introduce extra samples at the beginning and end of the rendered files which make our test method faulty as it is depends only on the time alignment, therefore a high quality rendering might be considered low, only because it is not in phase with the original. For instance, VORBIS proves to be the closest to the original uncompressed files, it may not necessarily indicate the actual higher quality.Therefore, it is important for us to think of more comprehensive methods to analyze the quality of the codecs more objectively.

## Second Test Case

In order to check for the actual quality of the decompressed files regardless of their time differences, for the second round of our test, we time aligned all the stems, flipped their phase and listened to all of them again. We were looking for the highest cancellation to check for the amount of similarity with the original. The top five percieved quality ranking were as follows:

As the next step, we calculated the magnitude squared coherence estimate to quantitaviely meassure the similarity of the decompressed files with the original wav files. It is calculated by taking the average over time domian of the two signals:

```
Correlation Percent = Mean(Magnitude Squared Coherence Estimate) 
Magnitude Squared Coherence Estimate = absolute(power spectral density [source * compressed decoded])^2 / (power spectral density of source * power spectral density of compressed decoded)
```

### Spatial Decode Listening Results:
The Spatialially decoded results are available here.
_Both the source multichannel audio and decompressed codec multichannel audio are being decoded in as Mach1Spatial 8 channel (YPR) at the same settings, the codec test material are then subtracted from the source so we can audibly listen to the remainder which would be the "difference" of signals due to the compression process._

#### Source Spatially Decoded:
**SOURCE WAV** [PCM]: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/ORIGINAL_Y0.wav"></source></audio>

#### Decoded Difference:
_Note: This test is to audibly hear the difference, the less heard the more successful the codec at this quality setting was at recreating the source after decompressing._
**AAC C16** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/AAC_C16_SUM.wav"></source></audio>

**AAC C48** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/AAC_C48_SUM.wav"></source></audio>

**AAC C320** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/AAC_C320_SUM.wav"></source></audio>

**AAC V0** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/AAC_V0_SUM.wav"></source></audio>

**AAC V2** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/AAC_V2_SUM.wav"></source></audio>

**AAC V10** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/AAC_V10_SUM.wav"></source></audio>

**MP3 C320** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/MP3_C320_SUM.wav"></source></audio>

**MP3 V30** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/MP3_V30_SUM.wav"></source></audio>

**MP3 V260** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/MP3_V260_SUM.wav"></source></audio>

**OPUS C16** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/OPUS_C16_SUM.wav"></source></audio>

**OPUS C32** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/OPUS_C32_SUM.wav"></source></audio>

**OPUS C96** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/OPUS_C96_SUM.wav"></source></audio>

**OPUS V8** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/OPUS_V8_SUM.wav"></source></audio>

**OPUS V16** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/OPUS_V16_SUM.wav"></source></audio>

**OPUS V32** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/OPUS_V32_SUM.wav"></source></audio>

**VORBIS Q0** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/VORBIS_Q0_SUM.wav"></source></audio>

**VORBIS Q3** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/VORBIS_Q3_SUM.wav"></source></audio>

**VORBIS Q7** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/VORBIS_Q7_SUM.wav"></source></audio>

**VORBIS Q10** Phase Cancelled: <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/VORBIS_Q10_SUM.wav"></source></audio>

#### Decoded Codecs:
_Note: This is to hear the audio after compression->decompression to hear how it alters from the source in a subjective comparison._

**AAC C16** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/AAC_C16.wav"></source></audio>

**AAC C48** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/AAC_C48.wav"></source></audio>

**AAC C320** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/AAC_C320.wav"></source></audio>

**AAC V0** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/AAC_V0.wav"></source></audio>

**AAC V2** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/AAC_V2.wav"></source></audio>

**AAC V10** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/AAC_V10.wav"></source></audio>

**MP3 C320** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/MP3_C320.wav"></source></audio>

**MP3 V30** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/MP3_V30.wav"></source></audio>

**MP3 V260** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/MP3_V260.wav"></source></audio>

**OPUS C16** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/OPUS_C16.wav"></source></audio>

**OPUS C32** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/OPUS_C32.wav"></source></audio>

**OPUS C96** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/OPUS_C96.wav"></source></audio>

**OPUS V8** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/OPUS_V8.wav"></source></audio>

**OPUS V16** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/OPUS_V16.wav"></source></audio>

**OPUS V32** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/OPUS_V32.wav"></source></audio>

**VORBIS Q0** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/VORBIS_Q0.wav"></source></audio>

**VORBIS Q3** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/VORBIS_Q3.wav"></source></audio>

**VORBIS Q7** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/VORBIS_Q7.wav"></source></audio>

**VORBIS Q10** <audio controls="controls"><source type="audio/wav" src="https://mach1-research-public.s3.amazonaws.com/posts/resources/soundfield-compression/audio/VORBIS_Q10.wav"></source></audio>

## Limitations and Future Works

Although these tests are analyzing different codecs and how they are affecting the files, they do not necessarily study how they might affect the spatial image of the multichannel files. One might argue that any changes in the sample numbers, amplitude and the frequency domain will inevitably affect the spatial image, but it is crucial to come up with methods to analyze this in further details.

More importantly, it is important to consider that our test methods are ultimately based on our subjective judgment of the decompression quality. Therefore, we might need to establish a more solid testing methodologies in future to increase the validity of our results. Further testing on spherical harmonic spatial audio formats should be conducted for soundfield changes to correlated multichannel audio formats. Testing on VBAP/VVBP/SPS formats would likely not yield different results from stereo field testing as the channels are uncorrelated already. As is with stereo soundfields being altered due to compression quality being too low to support containing the unique differences of channels, all spatial audio will be subject to the same effect. 
