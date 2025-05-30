---
title: "Multichannel Codec Support"
date: 2021-07-09T03:57:53-04:00
lastmod: 2021-07-09T03:57:53-04:00
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

#### filter_complex
You can get different channel orders by using different techniques to interleave multichannel streams in FFmpeg: 
 - `amerge`
 - `join` 

Using `amerge` tends to avoid channel_layout issues such as automatically processing and filtering `LFE` channels, however this could lead to issues later when other audio libraries or media handles assume your audio is something it is not. 

Using `join` if possible should use `octoganal` (for 8 channel) or any channel_layout that tends to treat all channels more discretely (to avoid issues with channel order and filtering LFE channels when unintended). Not every codec can support all channel_layouts and not every codec has a nice way to indicate "LEAVE MY CHANNELS ALONE!".

#### Channel Ordering
The following is an example of making a discretely handled 8 channel audio file.

#### `amerge`
```bash
ffmpeg -i 000.wav -i 001.wav -i 002.wav -i 003.wav -i 004.wav -i 005.wav -i 006.wav -i 007.wav -filter_complex "[0:a][1:a][2:a][3:a][4:a][5:a][6:a][7:a]amerge=inputs=8[aout]" -map "[aout]" output.wav
```
```bash
ffmpeg -i MERGED-amerge.wav -c:a libopus -mapping_family:a 255 -application:a audio -b:a 384K MERGED-amerge.opus 
```

#### `join`
```bash
ffmpeg -i 002.wav -i 000.wav -i 001.wav -i 003.wav -i 004.wav -i 005.wav -i 006.wav -i 007.wav -filter_complex "[0:a][1:a][2:a][3:a][4:a][5:a][6:a][7:a]join=inputs=8:channel_layout=octagonal[a]" -map "[a]" output.wav
```
```bash
ffmpeg -i output.wav -c:a libopus -mapping_family:a 255 -application:a audio output.opus
```

### vorbis (OGG)

#### Channel Ordering
The following is an example of making a discretely handled 8 channel audio file.

#### `amerge`
```bash
ffmpeg -i 000.wav -i 002.wav -i 001.wav -i 007.wav -i 005.wav -i 006.wav -i 003.wav -i 004.wav -filter_complex "[0:a][1:a][2:a][3:a][4:a][5:a][6:a][7:a]amerge=inputs=8[aout]" -map "[aout]" MERGED.wav
```
```bash
ffmpeg -i MERGED.wav -c:a libvorbis -q:a 10 output.ogg
```

### aac (AAC/M4A)

#### Channel Ordering
The following is an example of making a discretely handled 8 channel audio file.

#### `join`		
```bash
ffmpeg -i 006.wav -i 000.wav -i 001.wav -i 007.wav -i 004.wav -i 005.wav -i 002.wav -i 003.wav -filter_complex "[0:a][1:a][2:a][3:a][4:a][5:a][6:a][7:a]join=inputs=8:channel_layout=octagonal[a]" -map "[a]" output.wav
```
```bash
ffmpeg -i output.wav -c:a aac -b:a 1024k -q:a 10 output.aac 
```

### fdk-aac (AAC/M4A)

