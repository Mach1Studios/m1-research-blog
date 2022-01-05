---
title: "Multichannel Order from Codec to Codec"
date: 2018-06-15T05:19:00-04:00
lastmod: 2018-06-15T05:19:00-04:00
draft: false
---
---
## Introduction
Another common pitfall when dealing with multichannel content or developing handling multichannel content is various hardcoded channel orderings that happen from leftover surround formats development focused around broadcasting. This now plagues more modern developments with various issues when attempting to bridge between solutions or development media pipelines specific to your project or a new application. Various commonly used media handlers know will read a multichannel of `x` channels and assume a specific legacy multichannel surround format, depending on the codec during handling the channels may be tagged, re-ordered and even filtered. This can be completely destructive when using multichannel audio for anything outside the intended legacy surround design, commonly seen in AR,VR,MR,XR,LBE and custom media application and projects we know all work on today.

Below are some examples of this, we will take a simple 8 channel audio file from Pro Tools and see how it changes depending on what codec you export from Pro Tools and what a common input media handler might do upon ingest (such as FFmpeg).

## Results

#### SOURCE REFERENCE
<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/codec-channel-ordering/ProToolsAudioOrder.png" alt="" style="width:75%;">

#### AIF FROM PRO TOOLS HD/ULTIMATE
<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/codec-channel-ordering/PT_Exported_Aif_Order.png" alt="" style="width:75%;">

#### AIF TO M4A
<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/codec-channel-ordering/PT_Exported_aif-to-m4a_Order.png" alt="" style="width:75%;">

#### AIF TO OGG
<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/codec-channel-ordering/PT_Exported_aif-to-ogg_Order.png" alt="" style="width:75%;">

#### MP4 TO AIF
<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/codec-channel-ordering/PT_Exported_mp4-from-aif_Order.png" alt="" style="width:75%;">

#### WAV FROM PRO TOOLS HD/ULTIMATE
<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/codec-channel-ordering/PT_Exported_Wav_Order.png" alt="" style="width:75%;">

#### WAV TO M4A
<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/codec-channel-ordering/PT_Exported_wav-to-m4a_Order.png" alt="" style="width:75%;">

#### WAV TO OGG
<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/codec-channel-ordering/PT_Exported_wav-to-ogg_Order.png" alt="" style="width:75%;">

## Notes

- AIF tends to be safer to use due to the lack of metadata support, meaning cases of the wav file containing estaimted channel metadata tags are avoided when converting to other codecs.