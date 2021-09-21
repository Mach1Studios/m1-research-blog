---
title: "Custom Formats with Mach1Transcode"
date: 2020-06-15T03:15:37-04:00
draft: true
---

The Mach1Transcode API and CommandLine executable `m1-transcode` can be supplied with a description of a custom multichannel format/configuration to be used as either an input desciption of a soundfield or an output soundfield.  

Developed originally to explore mixes on custom multichannel configurations often seen in various LBE or multimedia projects, however we found a lot of use cases for exploring custom pipelines between normally blackbox multichannel media handlers and serving them as needed to any other format/configuration. This allowed exploration of bridging between formats, tools and formats and enabled us to great creative with all available tools for mixing multimedia projects more easily. 

This post will cover how to describe a custom format/configuration and two current methods for transcoding them locally. We are building out tools to make this process more inline and even some GUI tools to avoid describing formats over JSON text, progress will be provided as new posts.

## Describing Custom Multichannel Format

The format for describing your custom format/configuration in JSON can be done via the following template:
```
{
    "points": [
        {
            "x": -1.0,
            "y": 1.0,
            "z": 0.0,
            "azimuth": -45.0,
            "elevation": 0.0,
            "diverge": 1.0,
            "usePolar": false,
            "name": "Speaker 1",
            "children": []
        }
    ]
}
```
For example; this would describe a format of a single channel.

`X`, `Y`, `Z` : Describe channel position by cartesian

```
Mach1 XYZ Coordinate Expectation of Vector Points:

* X (left -> right | where -X is left)
* Y (front -> back | where -Y is back)
* Z (top -> bottom | where -Z is bottom)
```

`Azimuth`, `Elevation`, `Diverge` : Describe channel position by polar 
_(note this is the same standard used in Mach1Encode API and M1-Panner plugins)_

```
Mach1 AED Expectation of Describing Polar Points:

* Azimuth   (left -> right | where rotating left is negative)
* Elevation (down -> up | where rotating down is negative)
* Diverge   (backward -> forward | where behind origin of Azimuth/Elevation is negative)
```

`usePolar` :
- When false the `X`, `Y`, `Z` values will be used; ignoring `Azimuth`, `Elevation`, `Diverge`
- When true the `Azimuth`, `Elevation`, `Diverge` values will be used; ignoring `X`, `Y`, `Z`

`name` : Adds a tag or name for the channel (string)

`children` : An array for adding sub-channels *(EXPERIMENTAL, please avoid use)*

## Using Custom Multichannel via CommandLine

You can grab the platformed commandline `m1-transcode` here: [Mach1 Spatial SDK Github](https://github.com/Mach1Studios/m1-sdk/tree/master/binaries/executables)
This commandline binary is also used by M1-Transcoder.app/exe and can be found in your `User Data/Mach1 Spatial System/` directory of your computer if you installed [Mach1 Spatial System](https://www.mach1.tech/spatial-system).

#### Example command
`./m1-transcode fmtconv -in-file /path/to/16channel.wav -in-fmt TTPoints -in-json /path/to/16ChannelDescription.json -out-file /path/to/output-m1spatial.wav -out-fmt M1Spatial -out-file-chans 0`

Input JSON description of the surround/spatial soundfield setup per your design and input it with the -in-json arguement for any custom input or output transcoding.

The `-in-fmt` or `-out-fmt` as `TTPoints` can be used to set a custom json format.

You can also find an example custom `.json` file here: [references/Custom16Channel.json](https://github.com/Mach1Studios/m1-sdk/tree/master/binaries/executables/reference)


## Using Custom Multichannel via M1-Transcoder

The [M1-Transcoder](https://www.mach1.tech/spatial-system#transcoder) application from the [Mach1 Spatial System](https://www.mach1.tech/spatial-system) can also support custom JSON formats/configurations for Mach1Spatial->Custom transcodings.

![ExampleCustomTranscodeGIF](references/Mach1Spatial-CustomOutput.gif)

#### Steps
- Drag or load in your created JSON description to the `INPUT JSON` field
- Drag or load in your Mach1 Spatial 8 channel audio mix
- Render

The output will transcode based on your described multichannel format/configuration from the JSON file. 

## Format Requests
Please raise an issue via github or email [whatsup@mach1.tech](mailto:whatsup@mach1.tech) to submit a description of a multichannel format you wish to be included. Please include a reference JSON file as well as: 

* Name of Format
* Number of channels
* Order of channels
* Description of channels (using our conventions below)