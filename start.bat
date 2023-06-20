@echo off
chcp 65001 > nul
cls
pip install -r requirements.txt
py main.py
echo.
pause >nul
exit 0