# GetMiaoCoin
淘宝2020活动 618列车喵币自动领取
==
使用python+appium编写
## 如何使用
1.安装jdk并配置jdk环境变量<br>
2.安装sdk并配置sdk环境变量<br>
3.安装Node.js<br>
4.安装python3<br>
5.下载淘宝app并放置在app目录中<br>
6.使用记事本打开config目录中的capability.yaml文件，在“appname: ”后填入刚下载好的淘宝app的文件名，如：“appname: 701483.apk” 注意：“appname:”后要留有一个空格。<br>
7.capability.yaml中的“platformVersion: ”也需要修改为自己手机系统的版本<br>
8.手机使用usb连接电脑<br>
9.打开cmd <br>
输入 pip install selenium<br>
输入 pip install appium<br>
输入 pip install pyyaml<br>
9.打开cmd 进入到脚本目录，输入python run.py<br>
环境配置可查看此连接：[Appium环境配置](https://github.com/CaptainJi/Appium-AutoTest/blob/master/Appium%20MD%E6%95%99%E7%A8%8B/Appium%E5%9F%BA%E7%A1%80/3.Appium%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE.md)

注意：手机中的淘宝首次打开需要手动登录，登录后要关闭首页弹出广告和弹窗，才可以正常使用。淘宝人生中的喵币需要手动点击领取、菜地的喵币需要手动点击领取（懒了嫌麻烦，先不写这部分了）

本来可以编译成exe执行，但是appium环境配置还是少不了，也不差安装python3这一步了，所以还是直接用源代码吧。
