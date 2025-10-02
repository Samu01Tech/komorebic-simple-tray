@echo off
echo Building executable...

REM Build the executable with PyInstaller
REM --onefile: Creates a single executable file
REM --windowed: Runs without console window
REM --add-data: Include your PNG icon in the executable
REM Note: Use semicolon on Windows, colon on Linux/Mac

pyinstaller --onefile --windowed --add-data "icon.png;." --name "KomorebiTrayIcon" main.py

echo.
echo Executable created in dist/KomorebiTrayIcon.exe
echo.

REM Optional: Copy to a permanent location
set INSTALL_DIR=%USERPROFILE%\AppData\Local\KomorebiTrayIcon
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"
copy "dist\KomorebiTrayIcon.exe" "%INSTALL_DIR%\"

echo Installed to: %INSTALL_DIR%
echo.
echo To add to autostart, run: add_to_autostart.bat
pause