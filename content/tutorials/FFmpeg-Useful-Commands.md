---
title: "FFmpeg: Useful Commands"
date: 2020-07-20T05:19:00-04:00
draft: false
---

## Flags
Some common audio/video related flags or arguments to FFmpeg commands and what they mean.

##### General:
`-i` = input

##### Audio/Video:
_NOTE: `a` || `v` are interchangeable_

`-an` or `-vn` = remove either audio or video

`-b:a` or` -b:v` = bitrate, great for reducing a HQ video to work on mobile (example: `-b:v 20m`)

`-r` = frame rate (video)

`-c:a` or `-c:v` = refers to a command relating to the codec, so if you want to copy one of those codecs you can write: `-c:v copy` which is passthrough for video

## Commands

#### Remove Audio:
`ffmpeg -i input.mp4 -c:v copy -an output.mp4`

#### Extract Audio (use preferred codec):
`ffmpeg -i video.mp4 -vn -c:a copy -acodec pcm_s16le output.wav`

#### Add Audio To Video:
`ffmpeg -i input.mp4 -i input.wav -c:v copy -c:a aac -b:a 320k output.mp4`
or
`ffmpeg -i input.mov -i input.wav -c:v copy output.mov`

#### Adjust the Volume (percentage or db works) :
`ffmpeg -i input.mp4 -vcodec copy -af "volume=-15dB" -b:a 320k output.mp4`

#### Adjust Length to the shortest audio or video:
`ffmpeg -i input.mp4 -i audio.aac -shortest -c:v copy -c:a copy output.mp4`

#### Scale a video for performance:
`ffmpeg -i input.mp4 -s 1920×960 output.mp4`
or
#### Scale a video by video filter for reducing size:
`ffmpeg -i input.mp4 -vf scale=iw*.5:ih*.5 output.mp4`

#### Convert to DNxHD for Pro Tools
`ffmpeg -i input.mp4 -c dnxhd -s 1280x720 -r 24000/1001 -pix_fmt yuv422p -b 90M OUTPUTNAME.mov`

### 360 Video Manipulation

#### Stereoscopic to Monoscopic:
##### Over-under (top-bottom):
`ffmpeg -i input.mp4 -vf crop=h=in_h/2:y=0 output.mp4`

##### Side-by-side (left-right):
`ffmpeg -i input.mp4 -vf crop=h=in_w/2:y=0 output.mp4`

#### 360 Video Rotation
Where `100` is the desired amount of vertical pixels you want to offset from right to left, shifting the image toward the right:
`ffmpeg -i /path/to/input.mov -filter_complex "[0:v][0:v]overlay=100:0[bg]; [bg][0:v]overlay=100-W,format=yuv420p[out]" -map "[out]" -an -codec:v libx264 -crf 23 -preset medium /path/to/output.mp4`

if you want to shift by an angle use the following:
`width_of_video / 360 = pixels_per_degree`
`pixels_per_degree * degrees_you_want_shifted = number_of_vertical_pixels_rounded`