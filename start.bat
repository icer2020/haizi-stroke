@echo off
REM
REM @File          :   start.bat
REM @LastModified  :   2026/07/13 10:30:00
REM @Author        :   ICer
REM @Contact       :   i_chip_backend@163.com
REM @WebSite       :   https://blog.csdn.net/i_chip_backend
REM @License       :   (C)Copyright 2018-2026, ICerDev
REM @Description   :   一键启动 HTTP 服务器
REM

cd /d "%~dp0"
start http://localhost:8899/
python -m http.server 8899
