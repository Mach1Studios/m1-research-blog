---
title: "Multichannel Codec Support"
date: 2021-07-09T03:57:53-04:00
draft: false
---

While working with spatial and multichannel audio across different target platform; what codec is available is not always what is preferred. This post is to keep tabs on the different expectations of each codec and how it handles multichannel audio streams/files.

## FFmpeg
The following are FFmpeg's handling of the codecs below.

### libopus (OPUS)
We highly recommend using `-c:a libopus` instead of `-c:a opus` for proper multichannel handling from FFmpeg due to the following reason:

#### mapping_family
A very handy feature and addition to OPUS codec is the `mapping_family` argument. By using `-mapping_family:a 255` you can safely encode into opus with multichannel streams up to 255 channels.
 - `default` default behavior is `-1` which basically is `0` if input is mono/stereo and automatically `1` if input is greater than 2 channels but equal to or less than 8 _(2 < channels < 9)_
 - `0` for mono/stereo
 - `1` for adding LFE filtering to multichannel inputs
 - `255` for discrete channel handling or to unspecify the channel_layout (thank you!!!)

### VORBIS (OGG)

### aac (AAC/M4A)

### fdk-aac (AAC/M4A)

