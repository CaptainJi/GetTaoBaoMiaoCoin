@echo off
if "%1"=="" echo,请拖入需获取package与launchable-activity的apk至本文件上&pause&exit /b
aapt dump badging %1 |findstr "package launchable-activity"
pause
