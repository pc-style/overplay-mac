# macOS Overlay Library Examples

This directory contains example scripts demonstrating various features of the macOS overlay library.

## Examples

### 1. Simple Overlay (`simple_overlay.py`)
A basic example showing how to create a simple overlay with a web view.

**Features:**
- Transparent overlay window
- Rounded corners
- Draggable area
- Web view content
- Always on top

**Run:**
```bash
python examples/simple_overlay.py
```

### 2. Click-Through Overlay (`clickthrough_overlay.py`)
Demonstrates creating an overlay that doesn't capture mouse events.

**Features:**
- Click-through mode (mouse events pass through)
- Custom border with color
- Text content
- Semi-transparent background

**Run:**
```bash
python examples/clickthrough_overlay.py
```

### 3. Auto-Hide Overlay (`autohide_overlay.py`)
Shows how to create an overlay that automatically hides after a set duration.

**Features:**
- Auto-hide after specified duration
- Button to show again
- Draggable area
- Custom content

**Run:**
```bash
python examples/autohide_overlay.py
```

### 4. Transparency Control (`transparency_control.py`)
Demonstrates dynamic transparency control with interactive buttons.

**Features:**
- Real-time transparency adjustment
- Interactive buttons
- Status display
- Custom styling with borders

**Run:**
```bash
python examples/transparency_control.py
```

## Requirements

All examples require the overlay library to be installed:

```bash
pip install -e .
```

Or ensure you're running from the repository root with the virtual environment activated.

## Creating Your Own Overlay

Here's a minimal example:

```python
from AppKit import NSApplication, NSObject, NSApplicationActivationPolicyAccessory
from overai.overlay import Overlay

class MyDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        # Create overlay
        overlay = Overlay(
            x=100, y=100,
            width=400, height=300,
            transparency=0.9,
            corner_radius=15.0,
        )
        
        # Create and show window
        overlay.create_window()
        overlay.show()

# Run app
app = NSApplication.sharedApplication()
app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)
delegate = MyDelegate.alloc().init()
app.setDelegate_(delegate)
app.run()
```

## Tips

- **macOS Permissions**: Some features may require Accessibility permissions
- **Always on Top**: Use `always_on_top=True` to keep overlay above other windows
- **Click-Through**: Use `click_through=True` to allow interactions with windows below
- **Auto-Hide**: Use `overlay.show_for_duration(seconds)` for temporary overlays
- **Transparency**: Adjust with `overlay.set_transparency(0.0-1.0)` or use increase/decrease methods
