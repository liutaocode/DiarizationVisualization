# Visualization Tools for Diarization
## Introduction

There lacks a diarization visualization tool that is essential for analyzing dataset or algorithm results. In this repo, we provide convenient ways to visualize speaker diarization results. One criterion for choosing this visualization software is to support interactive operation. Although those visualization tools could be better, we can not find a better replacement.



## Audio-only tutorials

### Step 1: Run:

```
python audio_visualized.py -rttm audio_cases/afjiv.rttm -audio_path audio_cases/afjiv.wav -praat_result audio_cases/afjiv.txt
```

* ``rttm`` --- the reference or system rttm 
* ``audio_path`` --- the audio path
* ``praat_result`` --- visualized result for praat software

(Example is from [URL](https://github.com/joonson/voxconverse))

### Step 2: import ``praat_result`` into Praat:
- Install Praat [Mac](https://www.fon.hum.uva.nl/praat/download_mac.html) or [Windows](https://www.fon.hum.uva.nl/praat/download_win.html)
- import ``praat_result`` into Praat 
    - Open ``praat_result`` and ``audio``
    - <img src='imgs/praat_import.png' width=50% />
    - Select them all
    - Click ``View & Edit``

### Step3: Overview

![](imgs/praat_overview.png)

You can slide with horizontal scroll. Speaker labels are shown in each timeline (e.g., ``spk00``, ``spk01`` ...).

Some usefull shortcuts:

- ``CMD + A``: Show all utterances in one screen.
- ``CMD + N``: Dive into selected areas.

## Audio-visual tutorials

**TODO**

We will update soon.

![](imgs/via_example.png)
