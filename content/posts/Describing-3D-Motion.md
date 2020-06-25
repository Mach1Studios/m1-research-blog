---
title: "Describing 3D Motion"
date: 2020-06-15T05:19:00-04:00
draft: true
---

## Describing 3D Motions & Rotations

In the years of developing and creating for immersive mediums, there are usually moments of confusion and trouble when discussing and describing rotations or motions 3D (or 2D) space. Depending on what the project entails can lead to the creator describing things from 1st or 3rd perspectives and depending on what platform it is being built upon (and what frameworks) we see complications between different rotation and translation standards. 

This results in a massive landmine to any creative process or endeavor. In this post we will outline the standards we have witness, how we typically handle these discussions internally and the standard we use that tends to be the easiest for anyone to understand via speech and diagrams.

Let's start with discovered standards and where we often find them used.

## Existing Standards

Before listing the existing standards we have come across, it is important to keep in mind the aspects that cause confusion. 

### Rotation Angle Conventions List of Concerns:
#### 1. Order of Yaw, Pitch, Roll (Defined as angle applied first, second and third).

*This is a major cause for issue, on development side misinterpretating input angle orders when describing rotations comepletely destroys the intended spatial audio mix (or intended rotation)*

#### 2. Direction of transform around each pole's positive movement (left or right rotation).

*Even when the input angles are used in the correct order from "source", misinterpretaing the direction an incrementing rotation describes causes many issues, especially breaking headtracking by inversing rotations. This tends to be common as many frameworks will use left-handed or right-handed standards and rely on developers and creators to RTFM.*

#### 3. Float/int range before rotation completes a full 360° (2*PI) rotation, incorrect parsing of rotation center.

*Describing the range expected to be parsed for a rotation tends to be tricky as well, whether the receiving framework can modolus values outside the intended range, or if the range has a center angle origin (think about using angles that have signed values such as -45° instead of 315° would likely expect 0° to be a default starting orientation on that axis without ever explaining what that might be). If these values are normalized we can face issues when a creator describes 0° elevation as one orientation and the developer things 0 represents the lowest angle in that range after normalization.*

### Observed Rotation Standards per Platform:
| Platform Used | Angle Order      | Convention   | Naming Used |
|--------------:|-----------------:|-------------:|------------:|
|               | (yaw-pitch-roll) | Left handed  |             |
|               | (yaw-pitch-roll) | Right handed |             |
| Unity         | (pitch-roll-yaw) | Left handed  | x-y-z       |
| Unreal Engine |                  | Right handed | z-y-x       |
|               | (yaw-roll-pitch) | Left handed  |             |
|               | (yaw-roll-pitch) | Right handed |             |

### Ideal Euler Rotation Descriptions

| Order          | airplane      | telescope | symbol    | angular velocity |
| --------------:| -------------:| ---------:| ---------:| ----------------:| 
| applied first  | heading       | azimuth   | θ (theta) | yaw              |
| applied second | attitude      | elevation | φ (phi)   | pitch            |
| applied last   | bank          | tilt      | ψ (psi)   | roll             |

### Origin Story for Different X-Y-Z Descriptions

We were curious why different engines/frameworks might have a different description for X-Y-Z translations in space. There was a common story we were able to trace for two patterns: 

- **X,Y,Z where Z represents up/down height depth:** Typically from more modern engines or software relating to CAD or architecture, the idea is the common 2D view is a top-down view so that X and Y represent left/right, front/back respectivaly. Z being added on to describe more "height" or "layers of height" above, specifically easier to imagine when thinking about architecture CAD software where Z represents floors of a building.

- **X,Y,Z where Z represents front/back depth:** Typically derived from older game enginers, where we imagine looking at a 2D screen in front of you, X represents left/right and Y represents up/down. As the game engine or framework evolved from 2D to 3D; Z was added to represent "depth" for front/back as X and Y are already spoken for.

## Mach1 Standards

As mentioned before, we decided to cherrypick and clarify how we think and describe rotations & translations in space, focused more to unify creators and developers and derived more from a first person perspective. After long deliberation on using various existing standards, they had places where they worked and places where they didn't, they also were not very "humanized" and in an effort to fix this, we follow these guidelines:

### Coordinate / Angle / Rotation Description Expectations:

* Rotations can be individually explained per axis with signed rotations
* Rotations are explained from a center perspective point of view (FPV - First Person View)

### Mach1 YPR Polar Expectation of Describing Orientation:

#### Common use: Mach1Decode API, Mach1DecodePositional API
* Yaw   (left -> right | where rotating left is negative)
* Pitch (down -> up | where rotating down is negative)
* Roll  (top-pointing-left -> top-pointing-right | where rotating top of object left is negative)

### Mach1 AED Expectation of Describing Polar Points:

#### Common use: Mach1Encode API
* Azimuth   (left -> right | where rotating left is negative)
* Elevation (down -> up | where rotating down is negative)
* Diverge   (backward -> forward | where behind origin of Azimuth/Elevation is negative)

### Mach1 XYZ Coordinate Expectation of Vector Points:
* X (left -> right | where -X is left)
* Y (front -> back | where -Y is back)
* Z (top -> bottom | where -Z is bottom)

#### Positional 3D Coords
* X+ = strafe right
* X- = strafe left
* Y+ = up
* Y- = down
* Z+ = forward
* Z- = backward

#### Orientation Euler
* Yaw[0]+ = rotate right [Range: 0->360 | -180->180]
* Yaw[0]- = rotate left [Range: 0->360 | -180->180]
* Pitch[1]+ = rotate up [Range: -90->90]
* Pitch[1]- = rotate down [Range: -90->90]
* Roll[2]+ = tilt right [Range: -90->90]
* Roll[2]- = tilt left [Range: -90->90]