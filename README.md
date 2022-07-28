# tello-localization
DGMD S-17 Final Project, implemented with djitellopy and Python 3.10
## Monocular drone (Tello) localization
2022 DGMD S-17 Robotics, Autonomous Vehicles, Drones, and Artificial Intelligence @ Harvard University Extension School

**Team Members:** Daniel Lebedinsky, Yangsoo Song, John Ward, Claire Peters


Proposal
---
#### https://docs.google.com/document/d/1O5AGPdEM5yHExTr-1Uiikc-4K_LPvO8e1A04pVEgl_Y/edit

Videos
---
#### 

Presentation
---
#### 

Report
---
#### 

Getting Started
---
#### https://github.com/damiafuentes/DJITelloPy
To test this project on Fedora, clone this repository, run `chmod u+x dependencies.sh`, install the dependencies with `./dependencies.sh`, and run `python main.py`

# Technical Planning

main.py
---
####
The entry point for our project is at the bottom of this file, the main function. It creates the FrontEnd object and executes its method run().
Upon creation, FrontEnd opens a display for the live video from the tello drone, and creates a Tello object (which is used to control the drone motion)
The run method starts the tello object's video stream, and does the following continuously: 
"listens" for key press and release events to update the drone's movement, **gets each new frame from the Tello Camera to update the display**. 
Our first challenge is to run the detection and depth algorithms inside this loop, without creating excessive lag. I believe it may be necessary to run the key press listening and display updating in two separate threads. As a first step, we could define a new key to take pictures, and run detection and depth on each image.
If we have time, we can then find a way to make the drone move autonomously, in response to what it detects.

Take a picture of the scene
Take a picture further back
get 2 vectors of Midas and YOLO output, what do we do with the vectors?
"graph" is a chain which loops back, each node is orientation at a certain time, made up of midas and yolo output. Order is based on time, but lets say a current position looks like a much older position. This could indicate that you moved in a loop, and helps you build a map or deconstruct the environment.  
For the graph algorthim step, we can just put that as conclusion/next step, not the actual implementation for our project. 