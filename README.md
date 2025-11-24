# 🎨 macOS Overlay Library

**A flexible, customizable overlay window library for macOS** that provides transparency support, click-through mode, auto-hide, borders, and more using PyObjC.

Originally based on OverAI, this library allows you to create various types of overlays for macOS applications with minimal code.

> **Local-first. Lightweight. Powerful overlay creation made simple.**

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/pc-style/overplay-mac.git
cd overplay-mac

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

### Basic Usage (Library)

```python
from AppKit import NSApplication, NSObject, NSApplicationActivationPolicyAccessory
from overai.overlay import Overlay

class MyDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        # Create a customizable overlay
        overlay = Overlay(
            x=100, y=100,
            width=500, height=400,
            transparency=0.9,
            corner_radius=20.0,
            always_on_top=True,
        )
        
        # Create and configure the window
        overlay.create_window()
        overlay.add_drag_area(height=40)  # Add draggable area
        overlay.add_webview(url="https://example.com")  # Add content
        
        # Show the overlay
        overlay.show()

# Run the application
app = NSApplication.sharedApplication()
app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)
delegate = MyDelegate.alloc().init()
app.setDelegate_(delegate)
app.run()
```

### Run the Original OverAI App

```bash
python OverAI.py
```

---

## ✨ Features

### Library Features

| Feature                    | Description                                       |
| -------------------------- | ------------------------------------------------- |
| 🎨 Transparency Control    | Set opacity from 0.0 to 1.0 dynamically          |
| 🖱️ Click-Through Mode     | Make overlays that don't capture mouse events    |
| ⏱️ Auto-Hide              | Show overlays for a set duration, then hide      |
| 🎯 Always On Top           | Keep overlays above all other windows            |
| 🔲 Custom Borders          | Add borders with custom width and color         |
| 🎪 Rounded Corners         | Configurable corner radius                       |
| 🖐️ Draggable Areas        | Add areas that allow window dragging             |
| 🌐 WebView Support         | Embed web content easily                         |
| 🎭 Hide from Recordings    | Make overlays invisible in screen recordings     |
| 🖥️ Multi-Space Support    | Show in all virtual desktops                     |

### Original OverAI App Features

| Feature                    | Description                                       |
| -------------------------- | ------------------------------------------------- |
| 🪟 Frameless Overlay       | Stays always on top, clean and distraction-free   |
| 🧠 Multi-AI Support        | Easily switch between ChatGPT, Grok, Claude, etc. |
| 🎙️ Voice & Text Input     | Speak or type your prompt directly                |
| 🎛️ Transparency Control   | Adjust overlay opacity to your preference         |
| 🎹 Hotkey Toggle           | `⌘+G` or any custom key combo to toggle overlay   |
| 🕵️ Hidden from Recordings | Invisible in screen sharing and screen recordings |
| 🖥️ Lightweight + Local    | No lag, no cloud storage, no external servers     |

---

## 📚 Examples

Check out the `examples/` directory for complete working examples:

- **simple_overlay.py** - Basic overlay with web view
- **clickthrough_overlay.py** - Click-through overlay example
- **autohide_overlay.py** - Auto-hiding overlay
- **transparency_control.py** - Dynamic transparency control

Run any example:
```bash
python examples/simple_overlay.py
```

---

## 🛠 Overlay API

### Creating an Overlay

```python
from overai.overlay import Overlay

overlay = Overlay(
    x=500,                      # X position
    y=200,                      # Y position
    width=550,                  # Width
    height=580,                 # Height
    transparency=1.0,           # 0.0 (transparent) to 1.0 (opaque)
    corner_radius=15.0,         # Corner radius in pixels
    click_through=False,        # Enable click-through mode
    draggable=True,             # Enable dragging
    always_on_top=True,         # Stay on top of other windows
    show_in_all_spaces=True,    # Show in all virtual desktops
    hide_from_recordings=True,  # Hide from screen recordings
    border_width=0,             # Border width in pixels
    border_color=None,          # NSColor for border
)
```

### Methods

```python
# Window management
overlay.create_window()                    # Create the overlay window
overlay.show()                             # Show the overlay
overlay.hide()                             # Hide the overlay
overlay.show_for_duration(5.0)            # Show for 5 seconds then hide

# Transparency
overlay.set_transparency(0.8)              # Set transparency (0.0-1.0)
overlay.increase_transparency(0.1)         # Increase by amount
overlay.decrease_transparency(0.1)         # Decrease by amount

# Position and size
overlay.set_position(100, 100)             # Set window position
overlay.set_size(600, 400)                 # Set window size

# Content
overlay.add_drag_area(height=30)           # Add draggable area at top
overlay.add_webview(url="https://...")     # Add a web view
overlay.add_custom_view(my_nsview)         # Add custom NSView
```

---

## 🔐 Permissions Required (for OverAI App)

When you launch OverAI for the first time, macOS will request:

- 🎙️ **Microphone Access** — to capture voice commands
- ⌨️ **Accessibility Access** — to enable the global hotkey (⌘+G)

You can manage these anytime from: **System Settings → Privacy & Security**

---

## 💻 Tech Stack

- Python 3.10+
- PyObjC
- AppKit
- Quartz
- WebKit

---

## 🤝 Contributing

Contributions welcome!

- Fork the repo
- Create a feature branch
- Submit a pull request

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.

---

## ⭐ Like it?

If this project helped you, **please star the repo 🌟** — it really helps!


