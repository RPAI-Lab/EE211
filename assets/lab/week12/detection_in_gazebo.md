---
layout: page
title: detection in gazebo
description: detection in gazebo, written by Siyuan Wang.
nav_exclude: true
---


[← Back](https://rpai-lab.github.io/EE211-24Fall/calendar/)

<br>

# A Gazebo Simulation Environment aiming Quick Data Collection for Object Detection

> **For 2024Fall EE211 Course Project**
>
> **Last Update:** 2024-11-25

[Download](https://raw.githubusercontent.com/RPAI-Lab/EE211-24Fall/refs/heads/24fall/assets/lab/week12/detection_in_gazebo.zip)

<br>

## Usage

- [**Download wall_with_pic**](https://raw.githubusercontent.com/RPAI-Lab/EE211-24Fall/refs/heads/24fall/assets/lab/week12/wall_with_pic.zip), extract it then copy `wall_with_pic` folder to `/usr/share/gazebo-11/models/`


- `ros2 launch detection_in_gazebo gazebo.launch.py`: Launch Gazebo Environment, then you can publish to topic `cmd_vel` to control the robot, subscribe `/camera/image_raw` to obtain the camera image

<img src="https://rpai-lab.github.io/EE211-24Fall/assets/lab/week12/imgs/pic0.png" alt="pic0" style="zoom:50%;" /> 

- An Useful script for image collection: 

  cd to `<path_to_detection_in_gazebo>/detection_in_gazebo/`, run `python3 image_capture.py`, which will gives you an UI interface, press `s` to save current image, `q` to quit. 

- For a quick check for the camera image, run `ros2 run rqt_image_view rqt_image_view`.

<img src="https://rpai-lab.github.io/EE211-24Fall/assets/lab/week12/imgs/pic1.png" alt="pic1" style="zoom:90%;" /> 

<br>
<br>

