---
layout: page
title: tf2 listener
description: tf2 listener, written by Siyuan Wang.
nav_exclude: true
---


[← Back](https://rpai-lab.github.io/EE211-24Fall/calendar/)

<br>

# TF2: Managing Your Transformations in ROS2

> **For 2024Fall EE211 Course Project**
>
> **Last Update:** 2024-11-13

<br>

## What is TF2?
> TF2 is a package in ROS2 that lets the user keep track of multiple coordinate frames over time. It maintains the relationship between coordinate frames in a tree structure buffered in time, and lets the user query for the transformation between any two frames at any point in time.

*"In our project, you can obtain the transformation between the target grasping object and the end-effector_link of the PX100 arm utilizing TF2. Then execute the result of the inverse kinematics to move the arm to the target pose to grasp the object."*





<br>

## An Example

<br>

***0. Install TF2***

```bash
sudo apt-get install ros-humble-tf2-ros
sudo apt-get install ros-humble-tf2
sudo apt-get install ros-humble-tf2-tools
```
<br>

***1. Connect to your robot, then run `ros2 launch interbotix_xsarm_descriptions xsarm_description.launch.py robot_model:=px100 use_joint_pub_gui:=true`***

After this, the tf2 tree will be built. 

- run `ros2 run tf2_tools view_frames` to visualize the tf2 tree, check the generated `.pdf` file.

- run `ros2 topic list`, you can find the topic `/tf` and `/tf_static` are published.

- run `ros2 topic echo /tf` to see the transformation information.

<br>

***2. Create a listener node to get the transformation between two frames***

Here is a one provided for you, which listens to the transformation between the `base_link` and `ee_gripper_link` of the PX100 arm.
```python
import rclpy
from rclpy.node import Node
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

class FrameListener(Node):

    def __init__(self):
        super().__init__('tf2_frame_listener')

        # Declare and acquire `target_frame` and `source_frame` parameter
        self.base_frame = self.declare_parameter('arm_base_frame', 'px100/base_link').get_parameter_value().string_value
        self.ee_frame = self.declare_parameter('arm_ee_frame', 'px100/ee_gripper_link').get_parameter_value().string_value

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        
        # Call on_timer function every second
        self.timer = self.create_timer(1.0, self.on_timer)

    def on_timer(self):
        t = self.tf_buffer.lookup_transform(
                self.base_frame,
                self.ee_frame,
                rclpy.time.Time())
        self.get_logger().info('translation: {} \nrotation: {}'.format(t.transform.translation, t.transform.rotation))

def main():
    rclpy.init()
    node = FrameListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()

if __name__ == "__main__":
    main()
```

Keep the shell that runs `ros2 launch interbotix_xsarm_descriptions xsarm_description.launch.py robot_model:=px100 use_joint_pub_gui:=true`, you can run the python script directly to see the results (Integrate the script into a package in your seperate ros2 colcon workspace is more recommended).

<br>
<br>



**Reference**
- [TF2: ros2 humble doc](https://docs.ros.org/en/humble/Tutorials/Intermediate/Tf2/Tf2-Main.html)

<br>
<br>

