@echo off
echo Removing MyTrayApp from Windows autostart...

REM Remove from registry
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "KomorebiTrayIcon" /f

echo.
echo MyTrayApp removed from autostart
pause