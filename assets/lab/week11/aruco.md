---
layout: page
title: aruco
description: aruco, written by Siyuan Wang.
nav_exclude: true
---


[← Back](https://rpai-lab.github.io/EE211-24Fall/calendar/)

<br>

# "aruco code": Bridging 2D Image with 3D Coordinate 
> **For 2024Fall EE211 Course Project**
>
> **Last Update:** 2024-11-16

<br>

## What is aruco code?
> Aruco code is a type of 2D barcode used primarily in computer vision for object tracking. These square markers contain a unique binary pattern that can be detected and decoded by cameras. Each code corresponds to a specific identifier, enabling the system to recognize and interact with multiple markers simultaneously. Aruco codes facilitate precise positioning and orientation estimation in real-time, making them useful in robotics, gaming, and various augmented reality scenarios.

 

*"In your project, you use aruco to get the position(orientation) of the target object, so that the arm could reach and grasp"* 



<br>
<br>

## Using aruco with ROS2
> Since there are many many open-sourced project that provide aruco functionality with ROS2. Here is a revised one, and justified for your project.
>
> Please refer to [ros2_aruco_realsense](https://github.com/SeaHI-Robot/ros2_aruco_realsense)
<br>

See the detailed usage in the [README](https://github.com/SeaHI-Robot/ros2_aruco_realsense) of this repository

<br>
<br>

## Supplementary

Camera provides 2d informations, while a physical point has 3D information. 

Between a 2d point (in a camera image) and a 3d point (corresponding point in Cartasian space), a transformation (a Matrix, in the terminology linear algebra) should bridge them. 

This transformation consists of several parameters about the camera, which illusrates the camera's intrinsic properties. 

Realsense ros package has already provided this for you, that's why you never done any operations related with the camera's intrinsic parameters. As the realsense camera is launched, these camera intrinsic parameters are loaded into a `/camera_info` topic.

<br>

Check this link for detailed expanation:
- https://ksimek.github.io/2013/08/13/intrinsic/

<br>
<br>

