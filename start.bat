@echo off
REM
REM @File          :   start.bat
REM @LastModified  :   2026/07/13 10:30:00
REM @Author        :   ICer
REM @Contact       :   i_chip_backend@163.com
REM @WebSite       :   https://blog.csdn.net/i_chip_backend
REM @License       :   (C)Copyright 2018-2026, ICerDev
REM @Description   :   一键启动 HTTP 服务器（含局域网地址）
REM

cd /d "%~dp0"
echo.
echo === 汉字笔画演示 ===
echo.
echo 手机在同 WiFi 下访问:
for /f "skip=1 delims={}, " %%A in ('wmic nicconfig where "IPEnabled=True and not Description like '*Virtual*'" get IPAddress 2^>nul') do for %%B in (%%~A) do (
  echo %%B | findstr /r "^[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*$" >nul && echo   http://%%B:8899/
)
echo.
echo 本机访问: http://localhost:8899/
echo.
echo 首次访问后，Chrome 可"添加到主屏幕"离线使用
echo.
start http://localhost:8899/
python -m http.server 8899
