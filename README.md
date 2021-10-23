# 概述

基于Python的西北农林科技大学校园网自动登录程序。开发基于MIT授权协议的北京理工大学深澜校园网（@coffeehat）

# 环境依赖
python 3.8

# 目录结构描述
```bash
NWAFU_wifi_login_script
│  always_online.py // 在线监测脚本，如果监测到掉线则自动重连
│  AutoLoad.py // 采用selenium库实现的校园网自动登录
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
# AutoLoad.py使用说明（shrrr提供）
此脚本独立于登录程序。

考虑到深澜校园网登录已经增加了一系列加密处理机制，抓包分析相对复杂，所以本脚本基于selenium库实现了校园网的自动登录

由于selenium库本质上是一个浏览器自动控制工具，所以本脚本需要预先安装Chrome或Firefox浏览器及其相应的驱动，配置教程可以参考[Windows](https://www.cnblogs.com/xyztank/articles/13457260.html)、[Ubuntu、Mac](https://cloud.tencent.com/developer/article/1514874),也正因如此，脚本虽然修改应用比较简单，但在openwrt最终平台上运行可能会存在一些问题...，大家有什么好的想法也可以继续 ~~ o(*￣▽￣*)ブ

为了降低大家在公共服务器上部署AutoLoad.py文件时泄露账号密码的风险，建议大家在使用时新建tmux窗口运行，输入账号密码确认运行起来以后可以直接kill掉tmux 

如需要解除此python文件部署时可以使用以下命令查找任务ID并关闭任务

``` bash
ps aux | grep python
kill <PID>
```