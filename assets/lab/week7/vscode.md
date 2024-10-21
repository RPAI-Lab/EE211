---
title: "Setup VSCode for ROS Developing"
author: [Siyuan Wang]
date: "2024-10-21"
---



# Setup VSCode for ROS Developing



## 1. 添加ros包的IncludePath：

- `ctrl+shift+p` 打开vscode的控制面板，点击`C/C++: Edit Configurations (JSON)`

<img src="./imgs/pic1.png" alt="pic1" style="zoom:30%;" /> 

​	之后在当前目录下会生成`.vscode`文件夹

- 打开`.vscode/c_cpp_properties.json`，在`includePath`中添加ros的路径:

<img src="./imgs/pic2.png" alt="pic2" style="zoom:45%;" /> 

之后再编写C++的ROS相关代码时候，就可以使用代码补全功能。




## 2. 安装一些插件辅助编程：

对于ROS编程，有很多重复的代码片段，安装一个代码片段插件会提高代码书写效率。可以在插件市场安装`High ROS2 Snippets`，替补代码片段补全功能:

<img src="./imgs/pic3.png" alt="pic4" style="zoom:65%;" /> 

​	之后便可以使用代码片段补全功能，如:

<img src="./imgs/pic4.png" alt="pic4" style="zoom:30%;" /> <img src="./imgs/pic5.png" alt="pic5" style="zoom:30%;" /> 

