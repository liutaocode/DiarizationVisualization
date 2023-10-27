# Visualization Tools for Speaker Diarization
## Introduction

The current landscape lacks a robust tool for diarization visualization, which is critical for the analysis of datasets and algorithm outcomes. In this repository, we offer intuitive methods to illustrate speaker diarization results. A pivotal criterion for selecting this visualization software was its capacity for interactive operation. While these visualization tools have room for improvement, they are the best available options at present.

[Go to: Visualization tool for Audio-only datasets ](#anchor_ao) 

[Go to: Visualization tool for Audio-visual datasets ](#anchor_av) 


<p id="anchor_ao"></p>  

## Visualization for Audio-only datasets 

### Step 1: Generating praat format:

```
python audio_visualized.py -rttm audio_cases/afjiv.rttm -audio_path audio_cases/afjiv.wav -praat_result audio_cases/afjiv.txt
```

* ``rttm`` --- the reference or system rttm 
* ``audio_path`` --- the audio path
* ``praat_result`` --- visualized result for praat software

(Example is from [VoxConverse](https://github.com/joonson/voxconverse))

### Step 2: Import ``praat_result`` into Praat:
- Install Praat [Mac](https://www.fon.hum.uva.nl/praat/download_mac.html) or [Windows](https://www.fon.hum.uva.nl/praat/download_win.html)
- import ``praat_result`` into Praat 
    - Open ``praat_result`` and ``audio``
    - <img src='imgs/praat_import.png' width=50% />
    - Select them all
    - Click ``View & Edit``

### Step3: Overview

![](imgs/praat_overview.png)

You can slide with a horizontal scroll. Speaker labels are shown in each timeline (e.g., ``spk00``, ``spk01`` ...).

Some useful shortcuts:

- ``CMD + A``: Show all utterances in one screen.
- ``CMD + N``: Dive into selected areas.

<p id="anchor_av"></p> 

## Visualization for Audio-visual datasets

### Step 1: Generating VIA format

```
python audio_visual_visualized.py -rttm audio_visual_cases/00115.rttm -mp4_path audio_visual_cases/00115.rttm -via_json_result audio_visual_cases/00115.json
```

* ``rttm`` --- the reference or system rttm 
* ``mp4_path`` --- the mp4 path
* ``via_json_result`` --- visualized result for VIA software

(Example is from [MSDWild](https://github.com/X-LANCE/MSDWILD))

> If the video cannot be previewed or quickly previewed, please try to convert them to support the specific mp4 format of HTML5.
> ```
> ffmpeg -i original.mp4 -vcodec libx264 -acodec aac -preset fast -movflags +faststart  previewed.mp4
> ```

### Step 2: Import ``via_format.json`` into VIA tools

- Download ``via_video_annotator.html`` from [URL](https://www.robots.ox.ac.uk/~vgg/software/via/downloads/via3/via-3.0.11.zip) or directly use a [online demo](https://www.robots.ox.ac.uk/~vgg/software/via/demo/via_video_annotator.html). This website is an offline client, and we have tested on version ``via-3.0.11``(see file: ``via_video_annotator_3.0.11.html`` in this repo).
- Import JSON by clicking the ``folder button`` as follows:<img src='imgs/via_import.png' width=90% />
- You can also modify the script to support online URLs from OSS (Object Storage Service).

### Step3: Overview

![](imgs/via_example.png)

You can use the ``Space`` key to control ``Play/Pause Media.``

More keys can be found on:

 <img src='imgs/via_shortcut.png' width=20% />
 

References
=========
- https://www.fon.hum.uva.nl/praat/
- https://www.robots.ox.ac.uk/~vgg/software/via/
