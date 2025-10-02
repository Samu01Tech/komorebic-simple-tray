# Komorebi Simple Tray

A simple Windows system tray application for managing [Komorebi](https://github.com/LGUG2Z/komorebi), a tiling window manager for Windows.

## Features

- 🎯 **Simple Control**: Start and stop Komorebi directly from the system tray
- 🔄 **Visual Status**: Icon changes appearance based on Komorebi's running state
- ⚡ **Auto-detection**: Automatically detects if Komorebi is already running on startup
- 🚀 **Autostart Support**: Easy setup for automatic startup with Windows
- 🎨 **Custom Icon**: Uses a custom PNG icon that grays out when Komorebi is stopped

## Requirements

- Windows 10/11
- [Komorebi](https://github.com/LGUG2Z/komorebi) installed and `komorebic.exe` in PATH
- Python 3.7+ (for development)

## Installation

### Option 1: Download Pre-built Executable (Recommended)

1. Download the latest `KomorebiTrayIcon.exe` from the [Releases](../../releases) page
2. Place it in a permanent location (e.g., `%USERPROFILE%\AppData\Local\KomorebiTrayIcon\`)
3. Run `add_to_autostart.bat` to add it to Windows startup (optional)

### Option 2: Build from Source

1. Clone this repository:
   ```cmd
   git clone https://github.com/yourusername/komorebic-simple-tray.git
   cd komorebic-simple-tray
   ```

2. Install Python dependencies:
   ```cmd
   pip install pystray pillow pyinstaller
   ```

3. Build the executable:
   ```cmd
   build_executable.bat
   ```

4. The executable will be created in the `dist/` folder

## Usage

### Running the Tray Icon

Simply run `KomorebiTrayIcon.exe` or double-click it. The icon will appear in your system tray.

### System Tray Menu

Right-click the tray icon to access:
- **Start/Stop Komorebi**: Toggle Komorebi on or off
- **Toggle Komorebi**: Alternative toggle option
- **Quit**: Exit the tray application

### Autostart Setup

To automatically start the tray icon with Windows:

1. Run `add_to_autostart.bat` as administrator
2. The application will now start automatically when Windows boots

To remove from autostart:
- Run `remove_from_autostart.bat`

## Icon Behavior

- **Colored Icon**: Komorebi is running
- **Grayed Out Icon**: Komorebi is stopped
- **Tooltip**: Shows current status ("Running" or "Stopped")

## Project Structure

```
komorebic-simple-tray/
├── main.py                    # Main application code
├── icon.png                   # Tray icon image
├── build_executable.bat       # Build script for creating executable
├── add_to_autostart.bat      # Add to Windows autostart
├── remove_from_autostart.bat # Remove from Windows autostart
├── KomorebiTrayIcon.spec     # PyInstaller configuration
├── build/                    # Build artifacts (gitignored)
└── dist/                     # Final executable output (gitignored)
```

## Development

### Dependencies

- `pystray`: System tray functionality
- `PIL` (Pillow): Image processing for icon manipulation
- `subprocess`: Running Komorebi commands

### Building

The project uses PyInstaller to create a standalone executable:

```cmd
pyinstaller --onefile --windowed --add-data "icon.png;." --name "KomorebiTrayIcon" main.py
```

### Code Structure

- `KomorebiTray`: Main application class
- `create_icon()`: Handles icon creation and state visualization
- `start_komorebi()` / `stop_komorebi()`: Komorebi control functions
- `check_initial_state()`: Detects if Komorebi is already running

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Komorebi](https://github.com/LGUG2Z/komorebi) - The excellent tiling window manager this tool controls
- [pystray](https://github.com/moses-palmer/pystray) - For system tray functionality
- [Pillow](https://pillow.readthedocs.io/) - For image processing

## Troubleshooting

### Common Issues

**Tray icon doesn't appear:**
- Ensure the application is running and check Windows system tray settings
- Make sure `icon.png` is in the same directory as the executable

**"komorebic.exe not found" error:**
- Ensure Komorebi is installed and `komorebic.exe` is in your system PATH
- Try running `komorebic.exe --help` in Command Prompt to verify installation

**Autostart doesn't work:**
- Run `add_to_autostart.bat` as administrator
- Check Windows Task Manager > Startup tab to verify the entry was added

### Getting Help

If you encounter issues:
1. Check the [Issues](../../issues) page for existing solutions
2. Create a new issue with detailed information about your problem
3. Include your Windows version and Komorebi version