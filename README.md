# Driving in Mumbai's western express highway

## Context

Self driving cars are less than 10 years away from becoming quotidian. Yet India seems to be at least 30-40 years away (if at all) given the state of infrastructure. This data set pertains to city only and contains a .mp4 files captured while driving on Mumbai's western express highway at midnight. The data set is aimed at building an understanding about India's driving conditions and how self driving cars can be programmed to tackle the challenges that Indian roads throw at them.

This data set is also aimed at answering a critical question. 

*Do we program self driving cars to fit Indian driving conditions already or wait for the infrastructure to match suitable conditions for safe operation of self driving vehicles?*

*#### Note
I'm using Python here to detect lanes, curbs and other objects. Being an interpreted language, it is grossly inefficient, but the detection itself isn't being used for any kind of production purposes, so it's all cool for now.*

## Example: using Canny edge detector
<img src="https://github.com/deveshdatwani/self-driving-cars-India/blob/master/data/screenshot1.png" width="500">
<img src="https://github.com/deveshdatwani/self-driving-cars-India/blob/master/data/screenshotdetect.png" width="500">
<img src="https://github.com/deveshdatwani/self-driving-cars-India/blob/master/data/lane-detect.png" width="500">


## Neural Networks for lane detection
