# Gesture-Controlled Scrolling

A Python based computer vision project that lets you control system scrolling using hand gestures instead of a mouse or trackpad.

The project uses MediaPipe to detect hand landmarks, OpenCV to process the webcam feed, and PyAutoGUI to control system scrolling.

## Why?

While reading articles on a laptop, reaching for the mouse just to scroll can interrupt the reading flow—especially when sitting back or when your hands are occupied.

This project provides a simple hands-free alternative.

## Features

1. ☝️ Index Finger up = Scroll up
2. ✌️ Peace sign = Scroll down
3. 🖐️ Open palm = Stop
4. Real time hand tracking through the webcam
5. Safety control to enable/disable scrolling
6. Gesture cooldown to prevent excessive scrolling

The gesture detector identifies finger states from MediaPipe hand landmarks and maps them to scrolling actions.

## Tech Stack

Python
OpenCV
MediaPipe
PyAutoGUI
The hand tracker processes the webcam frame and extracts the pixel coordinates of the detected hand landmarks.




## Safety Control

The scrolling system includes an enable/disable control.
E - Toggle scrolling ON/OFF
Q - Quit

This allows the camera to continue running without accidentally triggering scrolling when the user does not want it.
