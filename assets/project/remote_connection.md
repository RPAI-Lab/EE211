---
layout: page
title: Three Ways of Remote Connection to the robot
description: Robot Connection, written by Siyuan Wang.
nav_exclude: true
---

[← Back](https://rpai-lab.github.io/EE211-24Fall/HW_and_Project/)

<br>

# Three Ways of Remote Connection to the robot

> **For 2024Fall EE211 Course Project**
>
> **Last Update:** 2024-10-15

<br>

## 0. 开机

- 按下电源键
- 给机器人上的小nuc开机

## 1. 配置NoMachine

- 在你的电脑上安装NoMachine

```bash
sudo apt install ./<pkg_name>.deb
# or
sudo dpkg -i ./<pkg_name>.deb
```

- 确保你的PC和小车上的nuc处在同一局域网下，然后打开终端，检查是否能ping通：

```bash
ping <remote_ip>
# e.g. ping 192.168.1.1
```

- 如果能ping通，进入NoMachine连接，确保ip和用户名输对


- 如果能ping通，但NoMachine远程桌面能进入但黑屏，新开一个终端ssh连接小车，执行一下命令，然后重新尝试连接NoMachine:

```bash
sudo /etc/NX/nxserver --restart
```

## 2. ssh连接
> NoMachine只能连接一台客户端机器，因此一个组同时只有一个人可以使用远程桌面；但ssh支持多客户端。

```bash
ssh <usr_name>@<ip>
# e.g. ssh tony@192.168.1.1
```

## 3. vscode - Remote SSH Plugin
> 安装vsode Remote SSH插件，体验和在本地一样的远端代码编辑体验
