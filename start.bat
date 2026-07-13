@echo off
cd /d "%~dp0"

echo.
echo === Hanzi Stroke Demo ===
echo.
echo Online (any device): https://icer2020.github.io/haizi-stroke/
echo.
echo Open on mobile (same WiFi):
for /f %%i in ('powershell -noprofile -command "$a=(Get-NetIPAddress -AddressFamily IPv4^|Where-Object PrefixOrigin -eq Dhcp^|Select-Object -First 1).IPAddress;Write-Host $a"') do (
  echo   http://%%i:8899/
  goto :found
)
:found
echo.
echo Local: http://localhost:8899/
echo.
echo Tip: Chrome can add to home screen for offline use
echo.
start http://localhost:8899/
python -m http.server 8899 --bind 0.0.0.0
