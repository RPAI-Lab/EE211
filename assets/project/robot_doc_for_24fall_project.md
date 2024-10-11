---
layout: page
title: Manual for the robot we use 
description: Robot Manual, written by Jielin Wu.
nav_exclude: true
---

[← Back](https://rpai-lab.github.io/EE211/HW_and_Project/)

<br>

# 机器人使用规范

> **For 2024Fall EE211 Course Project**
>
> **Last Update:** 2024-10-11

<br>

## 机器人配置
本次项目使用的机器人为TurtleBot4改装小车，已加装激光雷达、云台和深度相机等配件，以满足项目需求。

## 管理与维护
- 每组将分配一个改装小车，直至项目结束，各组需负责保管和维护。
- 非特殊情况下，不得交换使用。
- 未经许可，不得将小车带离120实验室。
- 如有损坏，需根据损坏情况确定赔偿责任（正常使用耗损除外）。

## 充电与使用
- 小车配备底盘充电器（充电桩）和NUC电池充电器（普通适配器）。
- 上下位机需分开充电。
- 机器人充电时间较长，请每日使用完毕后及时充电。
- 充电位置位于机器人摆放处，已配备足够充电口。

## 开机与调试
- 开机顺序：上位机开机时，先打开底盘上的按压按钮，再打开上位机nuc的电源；下位机开机需要把机器人底盘放到充电桩上等待语音提示开机（灯光变为白色，具体查看厂家guidance，并且伴随音乐表示底盘启动）。
- 机器人启动后，可进入NUC系统进行直接调试，或使用NoMachine进行远程调试（推荐）。
- 调试过程中请注意安全。

<span style="color: red; font-size: 18px">
    <strong>
<i>
 **安全提示**
</i>
    </strong>
</span> 

> 在开始调试前，请确保周围环境空旷，并已熟悉Ubuntu和ROS2的基本指令。否则，可能导致机器人硬件和软件的重复维修。

## 文档与支持
具体使用细节和机器人相关文档如下，如遇问题，请先查阅文档。若问题无法解决，请携带日志寻求助教帮助。

- 机器人厂家指导手册：[https://doc.iqr-robot.com/turtlebot4_user_manual/software/software.html](https://doc.iqr-robot.com/turtlebot4_user_manual/software/software.html)
- 底盘文档：[https://iroboteducation.github.io/create3_docs](https://iroboteducation.github.io/create3_docs)
- 深度相机：
  - [https://github.com/IntelRealSense/realsense-ros](https://github.com/IntelRealSense/realsense-ros)
  - [https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md#installing-the-packages](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md#installing-the-packages)
- TurtleBot4教程（请使用Humble版本）：[https://turtlebot.github.io/turtlebot4-user-manual/overview/](https://turtlebot.github.io/turtlebot4-user-manual/overview/)
- 机械臂：[https://docs.trossenrobotics.com/interbotix_xsarms_docs/ros_interface/ros2/software_setup.html](https://docs.trossenrobotics.com/interbotix_xsarms_docs/ros_interface/ros2/software_setup.html)
- 陀螺仪：[https://github.com/ElettraSciComp/witmotion_IMU_ros/tree/ros2](https://github.com/ElettraSciComp/witmotion_IMU_ros/tree/ros2)
- 激光雷达：[https://github.com/Slamtec/sllidar_ros2](https://github.com/Slamtec/sllidar_ros2)
