---
title: "IMU Enabled Devices"
date: 2020-06-05T03:10:05-04:00
draft: true
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
 - Apple AirPod Pro (`TBD`)
 - [Audeze Mobius](#audeze-mobius) (`semi-open-use`)
 - JBL Quantum One (`closed/inaccessible`)

### Attachable IMU Trackers
 - EDTracker Pro (`open-use`)
 - WitMotion (`open-use`)
 - Waves NX (`closed/inaccessible`)
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
 - Spark AR: Face Tracker

## Device Specific Instructions

#### Audeze Mobius
The Link Mode checkbox in the HQ app is a beta feature in our latest HQ App & Firmware that allows apps using Zeroconf (such as FaceBook360's OSC protocol) to access the head tracking data provided by Mobius. If you have software that's compatible with that protocol, the data should transmit to it when you check the box in HQ as follows:
<img src="https://mach1-research-public.s3.amazonaws.com/posts/resources/imu-enabled-devices/inline-149321904.png" alt="" style="width:75%;">
