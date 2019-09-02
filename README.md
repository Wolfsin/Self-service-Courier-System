# Self-service-Courier-System
A courier barcode recognition and entry system using Raspberry Pi as a terminal, including a simple admin Web.   -- 一个使用树莓派作为终端机的快递条码识别、录入系统，附带一个简易Web后台。

- [Self-service-Courier-System](#self-service-courier-system)
    + [前言](#前言)
  * [快速开始](#快速开始)
- [English Version](#english-version)
    + [Before the start](#before-the-start)
  * [Quick start](#quick-start)


### 前言
这是我大学毕业时完成的一个毕业设计，是从学校现实出发的一个小项目，运用了很多开源的库、参考了很多前辈写的代码，说来惭愧，这个项目我所作的可能就只是整合了现有的东西。下面我将来详细说明怎么使用这个项目。

## 快速开始
1. 下载本项目到本地
2. 配置本地环境：
为了正常运行所有的项目，你需要准备一台 PC 和树莓派。
- 2.1树莓派环境： 
本项目使用的树莓配为 3B+，使用的摄像头为树莓派专用的 CSI 摄像头模块。树莓派运行的系统为官方的 raspberry。同时树莓派需要安装的 Python3 库有： pymysql、PyQt5、cv2、imutils、numpy、multiprocessing、pyzbar。
- 2.2 Web 端环境：
Web 端使用 SpringBoot 进行开发，JDK 版本为 8，项目使用 Maven 进行库文件管理，缺少的 JAR 包会自动下载。
3. 数据库：
数据库推荐 MySQL 5.7 版本，Sql 文件在 DB 文件夹下。
4. 修改数据库的配置文件：
Web 端配置文件在 `src/main/resources/application.properties `文件中；树莓派端配置文件在` Connect.py` 文件中。
    为了保证数据统一，请确保 Web 和树莓派链接的数据库为同一个！！
5. 运行代码


# English Version

### Before the start
This is a graduation project that I completed when I graduated from university. It is a small project based on the reality of the school. I use a lot of open source libraries and reference the code written by many seniors. After all, what I am doing is just integration. The existing things. Below I will explain in detail how to run this project.

## Quick start
1. Download this project to your local
2. Configuring the local environment：
In order to run all the projects properly, you need to prepare a PC and Raspberry Pi.
- 2.1 Raspberry Pi environment： 
The raspberry I used is raspberry 3B+ and the camera used is the CSI camera module dedicated to the Raspberry Pi. The Raspberry Pi running system is raspberry. The Python3 libraries that the Raspberry Pi needs to install are: pymysql, PyQt5, cv2, imutils, numpy, multiprocessing, pyzbar.
- 2.2 Web side environment：
The Web side uses SpringBoot for development. The JDK version is 8. The project uses Maven for library file management, and the missing JAR package is automatically downloaded.
3. database：
The database recommends MySQL version 5.7, and the Sql file is in the DB folder.
4. Modify the database configuration file：
The web side configuration file is in the ：
 `src/main/resources/application.properties` 
 the raspberry configuration file is in the ：
 `Connect.py`.
    To ensure data consistency, make sure that the web and the Raspberry Pi link database are the same!!
5. Run Code

