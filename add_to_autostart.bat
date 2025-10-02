@echo off
echo Adding Komorebi Tray Icon to Windows autostart...

REM Method 1: Registry (Current User)
set APP_PATH=%USERPROFILE%\AppData\Local\KomorebiTrayIcon\KomorebiTrayIcon.exe
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "KomorebiTrayIcon" /t REG_SZ /d "%APP_PATH%" /f

echo.
echo KomorebiTrayIcon added to autostart (current user only)
echo Location: %APP_PATH%
echo.
echo The app will start automatically on next boot.
echo To remove from autostart, run: remove_from_autostart.bat
pause