@echo off
if "%1"=="" echo,���������ȡpackage��launchable-activity��apk�����ļ���&pause&exit /b
aapt dump badging %1 |findstr "package launchable-activity"
pause
