# 概述

基于Python的西北农林科技大学校园网自动登录程序。开发基于MIT授权协议的北京理工大学深澜校园网（@coffeehat）

# 环境依赖
python 3.8

# 目录结构描述
```bash
NWAFU_wifi_login_script
│  always_online.py // 在线监测脚本，如果监测到掉线则自动重连
│  AutoLoad.py // 采用selenium库实现的校园网自动登录（一般不必使用，仅展示一种方式）
│  demo.py // 登录示例脚本
│  README.md
│
└─NWAFU_WIFI_login
    │  LoginManager.py
    │  _decorators.py
    │  __init__.py
    │
    ├─encryption
    │  │  srun_base64.py
    │  │  srun_md5.py
    │  │  srun_sha1.py
    │  │  srun_xencode.py
    │  │  __init__.py
    │  └─
    └─
```
always_online.py可采用`nohup`命令挂在后台：
``` bash
nohup python always_online.py &
```
---
# Makefile使用说明

使用本项目的`Makefile`可以由`loginScript.py`构建可执行程序以实现自动登录。同时，在`systemd`文件夹中提供了相关的`service`和`timer`以实现自动运行。

以下是构建步骤：

1. 使用`make confVenv`来构建虚拟环境，之后运行`source ./buildEnv/bin/activate`来激活它
2. `make buildBinary`会在`dist`文件夹中构建可执行文件
3. 使用`make install`来安装可执行文件和`systemd`相关任务。别忘了修改相应的`service`文件来修改用户名和密码

# AutoLoad.py使用说明（shrrr提供）
此脚本独立于登录程序。一个基于selenium库的实现方案，不建议使用！！！！！

``` bash
ps aux | grep python
kill <PID>
```
