---
title: "IMU Enabled Devices"
date: 2020-06-05T03:10:05-04:00
lastmod: 2022-08-15T03:10:05-04:00
draft: false
---
---
## Introduction
As more and more devices become available on the market for headtracking and positional tracking we can expect more oppurtunity for growth of spatial audio and other creative uses for multichannel/spatial audio. Here we will try to track and list known devices, focused more on the consumer side as the DIY side could be endless (however we will still list some here for anyone starting to research DIY solutions).

Additionally we are excited to which of these devices will be easy for 3rd party developers to use for their use cases, instead of just having access to the tethered software of each device, we will list the ones that support open use (`open-use`) as well as those that do not (via `closed/inaccessible`)

## Development Tracking
- (`TBD`) - Orientation is not accessible, public SDK in progress
- (`open-use`) - Orientation data is accessible, full public SDK available
- (`semi-open-use`) - Orientation data is limited, no official public SDK available
- (`closed/inaccessible`) - Orientation data is not accessible or is proprietary

### Headphones / Earphones
 - Bose NC 700  (`semi-open-use`)
 - Bose QC35 II (`semi-open-use`)
 - Bose Frames Alto (`semi-open-use`)
 - Bose Frames Rondo (`semi-open-use`)
 - Apple AirPods Pro (`open-use`)
 - Apple AirPods Max (`open-use`)
 - Apple AirPods [3rd generation] (`open-use`)
 - Beats Fit Pro (`open-use`)
 - [Audeze Mobius](#audeze-mobius) (`semi-open-use`)
 - JBL Quantum One (`closed/inaccessible`)

### Attachable IMU Trackers
 - [mBient Lab MetaMotion](https://mbientlab.com/metamotions) (`open-use`)
 - [Supperware](https://supperware.co.uk/) (`open-use`)
 - [WitMotion](#witmotion) (`open-use`)
 - [nvsonic](https://github.com/trsonic/nvsonic-head-tracker) (`open-use`)
 - EDTracker Pro (`open-use`)
 - Waves NX (`closed/inaccessible`)(`semi-open-use`)
 - BBC micro:bit (`open-use`)

### AR/MR Glasses
 - MagicLeap: Lightwear
 - [Nreal](https://www.nreal.ai/)
 - LeapMotion: North Star
 - Shadow Creator: Action One
 - Rokid: Glass
 - Kopin: Golden-I Infinity
 - Rokid: Project Aurora
 - Vuzix: M300
 - ThirdEye Gen: X2

### Alternatives Headtracking Sensors
 - TrackIr
 - [OpenTrack](https://github.com/opentrack/opentrack)
 - FaceTrackerNoIR
 - PointTracker
 - Intel RealSense 3D cameras (via OpenTrack)
 - Razer Hydra
 - [Aruco](https://github.com/opentrack/opentrack/wiki/Aruco-tracker)
 - Wiimote
 - Consolidated DIY IMU: [BNO055](https://www.adafruit.com/product/2472)
 - Consolidated DIY IMU: [L3GD20H + LSM303](https://www.adafruit.com/product/1714)
 - Consolidated DIY IMU: [ICM-20948](https://www.sparkfun.com/products/15335)
 - Consolidated DIY IMU: [MPU-9250](https://www.sparkfun.com/products/13762)
 - Consolidated DIY IMU: [BNO080](https://www.sparkfun.com/products/14686)

#### Web Facetrackers
 - MediaPipe BlazeFace
 - jeelizFaceFilter
 - FaceTracker.net
 - tracking.js

#### Opensource Facetrackers
 - Mediapipe FaceDetection/FaceTracker
 - Spark AR: Face Tracker

## Device Specific Instructions

#### AirPods Pro, AirPods Max, AirPods (3rd gen) & Beats Fit Pro
As of Xcode 12 Beta Preview 6 or newer (Xcode 12) along with iOS 14+ the [CMHeadphoneMotionManager](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager) API is available and with minimal effort we can expose the orientation data of the AirPod Pro. 
View our demo implementation of this via an iOS app that outputs the orientation data via OSC here: https://github.com/Mach1Studios/M1-AirPodOSC

#### Supperware
We recommend usage of [Supperware](https://supperware.co.uk/) tethered IMU for studio environments. The IMU and associated connection tools are very maturely designed and further supports an opensource API for bridge connection to be natively written into production software.

#### MetaMotion
We have been using MetaMotion MMRL & MMS devices for custom 3rd party headtracking added nicely to any pair of headphones with great performance. We have even contributed to a prototyping cross-platform OpenFrameworks addon to help others use these devices as well: https://github.com/Mach1Studios/ofxMetaMotion

#### WitMotion
In an attempt to make the WitMotion controller accessible we have developed a cross-platform OpenFrameworks addon and example: https://github.com/Mach1Studios/ofxWitMotion

#### Waves NX : NXOSC (audiooo.com)
The WavesNX are now usable for macOS to custom OSC output addresses via Katsuhiro Chiba's little middleman sniffer hacker application: https://audiooo.com/nxosc

#### Audeze Mobius
The Link Mode checkbox in the [Audeze HQ](https://www.audeze.com/pages/audeze-hq-software) application contains a beta feature with Audeze's latest Firmware that allows apps using Zeroconf (OSC protocol) to access the headtracking data provided by [Audeze Mobius](https://www.audeze.com/products/mobius). If you have software that's compatible with that protocol, the data should transmit to it when you check the box in HQ as follows:

<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/imu-enabled-devices/inline-149321904.png" alt="" style="width:75%;">
