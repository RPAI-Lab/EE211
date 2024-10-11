#!/usr/bin/bash

##### You may find this script helpful when configura your developing environment on your robot #####


sudo apt update
sudo apt dist-upgrade

sudo apt remove brltty

# https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
# https://mirrors.bfsu.edu.cn/help/ros2/

sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt install curl gnupg2
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] https://mirrors.bfsu.edu.cn/ros2/ubuntu jammy main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt install ros-humble-desktop ros-dev-tools

sudo apt install python3-pip
pip config set global.index-url https://mirrors.bfsu.edu.cn/pypi/web/simple
python -m pip install --upgrade pip
python3 -m pip install setuptools==58.2.0

# https://mirrors.bfsu.edu.cn/help/rosdistro/
# 手动模拟 rosdep init
sudo mkdir -p /etc/ros/rosdep/sources.list.d/
sudo curl -o /etc/ros/rosdep/sources.list.d/20-default.list https://mirrors.bfsu.edu.cn/github-raw/ros/rosdistro/master/rosdep/sources.list.d/20-default.list
echo 'export ROSDISTRO_INDEX_URL=https://mirrors.bfsu.edu.cn/rosdistro/index-v4.yaml' >> ~/.bashrc


# https://github.com/IntelRealSense/realsense-ros
# https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md#installing-the-packages
sudo mkdir -p /etc/apt/keyrings
curl -sSf https://librealsense.intel.com/Debian/librealsense.pgp | sudo tee /etc/apt/keyrings/librealsense.pgp > /dev/null
echo "deb [signed-by=/etc/apt/keyrings/librealsense.pgp] https://librealsense.intel.com/Debian/apt-repo `lsb_release -cs` main" | \
sudo tee /etc/apt/sources.list.d/librealsense.list
sudo apt update
sudo apt install librealsense2-dkms librealsense2-utils librealsense2-dev
sudo apt install ros-humble-realsense2-camera ros-humble-realsense2-description


# https://github.com/Slamtec/sllidar_ros2
git clone https://github.com/Slamtec/sllidar_ros2.git
colcon build --symlink-install

https://iroboteducation.github.io/create3_docs/setup/ubuntu2204/
sudo apt install -y ros-humble-irobot-create-msgs

# https://github.com/ElettraSciComp/witmotion_IMU_ros/tree/ros2
sudo apt install libqt5serialport5-dev
cd ros2_ws/src
git clone -b ros2 --recursive https://github.com/ElettraSciComp/witmotion_IMU_ros.git witmotion_ros
colcon build --symlink-install
source install/setup.bash

# arm
# https://docs.trossenrobotics.com/interbotix_xsarms_docs/ros_interface/ros2/software_setup.html
....
rosdep install --from-paths src -y --ignore-src
colcon build --symlink-install
