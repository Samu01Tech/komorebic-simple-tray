import pystray
import subprocess
from PIL import Image, ImageDraw
import sys
import os

def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class KomorebiTray:
    def __init__(self):
        self.is_running = False
        self.icon = None
        
    def create_icon(self):
        """Load icon from PNG file and gray it out if not running"""
        try:
            # Try to load your PNG icon file
            icon_path = get_resource_path("icon.png")
            image = Image.open(icon_path)
           
            # Resize to appropriate size if needed
            image = image.resize((32, 32), Image.Resampling.LANCZOS)
            
            # Convert to RGBA if not already
            if image.mode != 'RGBA':
                image = image.convert('RGBA')
            
            # Gray out the icon if Komorebi is not running
            if not self.is_running:
                # Convert to grayscale while preserving alpha channel
                grayscale = image.convert('L')  # Convert to grayscale
                grayscale_rgba = Image.new('RGBA', image.size)
                
                # Copy grayscale data to RGB channels, keep original alpha
                pixels = []
                gray_pixels = list(grayscale.getdata())
                alpha_pixels = [pixel[3] if len(pixel) > 3 else 255 for pixel in image.getdata()]
                
                for i, gray_value in enumerate(gray_pixels):
                    # Make it even more muted by reducing contrast
                    muted_gray = int(gray_value * 0.6 + 128 * 0.4)  # Blend with middle gray
                    pixels.append((muted_gray, muted_gray, muted_gray, alpha_pixels[i]))
                
                grayscale_rgba.putdata(pixels)
                image = grayscale_rgba
           
            return image
        except FileNotFoundError:
            print(f"Icon file not found, using default icon")
            # Fallback: create a simple icon
            image = Image.new('RGBA', (32, 32), color=(255, 255, 255, 0))
            draw = ImageDraw.Draw(image)
            
            # Different colors based on state
            if self.is_running:
                color = (0, 200, 0, 255)  # Green if running
            else:
                color = (128, 128, 128, 255)  # Gray if stopped
            draw.ellipse([4, 4, 28, 28], fill=color)
           
            return image

    def start_komorebi(self):
        """Function to start Komorebi"""
        try:
            command = ["komorebic.exe", "start", "--whkd"]
            result = subprocess.run(command, check=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
            self.is_running = True
            self.update_icon()
            print("Komorebi started successfully")
        except subprocess.CalledProcessError as e:
            print(f"Error starting Komorebi: {e}")
        except FileNotFoundError:
            print("komorebic.exe not found")

    def stop_komorebi(self):
        """Function to stop Komorebi"""
        try:
            command = ["komorebic.exe", "stop", "--whkd"]
            result = subprocess.run(command, check=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
            self.is_running = False
            self.update_icon()
            print("Komorebi stopped successfully")
        except subprocess.CalledProcessError as e:
            print(f"Error stopping Komorebi: {e}")
        except FileNotFoundError:
            print("komorebic.exe not found")

    def toggle_komorebi(self):
        """Toggle Komorebi on/off"""
        if self.is_running:
            self.stop_komorebi()
        else:
            self.start_komorebi()

    def update_icon(self):
        """Update the tray icon to reflect current state"""
        if self.icon:
            new_image = self.create_icon()
            self.icon.icon = new_image
            # Update tooltip to show current state
            status = "Running" if self.is_running else "Stopped"
            self.icon.title = f"Komorebi Tray Icon - {status}"

    def update_menu(self):
        """Update menu based on current state"""
        if self.is_running:
            action_text = "Stop Komorebi"
            action_func = lambda: self.stop_komorebi()
        else:
            action_text = "Start Komorebi"
            action_func = lambda: self.start_komorebi()
        
        menu = pystray.Menu(
            pystray.MenuItem(action_text, action_func),
            pystray.MenuItem("-"),  # Separator
            pystray.MenuItem("Toggle Komorebi", lambda: self.toggle_komorebi()),
            pystray.MenuItem("Quit", self.quit_app)
        )
        
        if self.icon:
            self.icon.menu = menu

    def quit_app(self, icon, item):
        """Quit the application"""
        icon.stop()

    def check_initial_state(self):
        """Check if Komorebi is already running on startup"""
        try:
            # Try to get Komorebi state - this is a simple check
            result = subprocess.run(["komorebic.exe", "state"], 
                                  capture_output=True, text=True, timeout=5)
            # If the command succeeds and returns data, Komorebi is likely running
            self.is_running = result.returncode == 0 and len(result.stdout.strip()) > 0
        except:
            # If any error occurs, assume it's not running
            self.is_running = False

    def run(self):
        # Check initial state
        self.check_initial_state()
        
        # Create the icon
        icon_image = self.create_icon()
        
        # Create initial menu
        menu = pystray.Menu(
            pystray.MenuItem("Start Komorebi" if not self.is_running else "Stop Komorebi", 
                           lambda: self.toggle_komorebi(), default=True),
            pystray.MenuItem("Quit", self.quit_app)
        )
        
        # Create the tray icon
        self.icon = pystray.Icon(
            "Komorebi Tray Icon",
            icon_image,
            f"Komorebi Tray Icon - {'Running' if self.is_running else 'Stopped'}",
            menu
        )
                
        # Run the icon (this blocks)
        self.icon.run()

def main():
    app = KomorebiTray()
    app.run()

if __name__ == "__main__":
    main()

# To install required dependencies:
# pip install pystray pillow