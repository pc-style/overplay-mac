# Overlay Library Usage Guide

This guide provides comprehensive documentation for using the macOS Overlay Library.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Concepts](#core-concepts)
- [API Reference](#api-reference)
- [Advanced Usage](#advanced-usage)
- [Examples](#examples)

## Installation

### From Source

```bash
git clone https://github.com/pc-style/overplay-mac.git
cd overplay-mac
pip install -e .
```

### Requirements

- macOS 10.15+ (Catalina or later)
- Python 3.10 or later
- PyObjC framework

## Quick Start

Here's a minimal example to create your first overlay:

```python
from AppKit import NSApplication, NSObject, NSApplicationActivationPolicyAccessory
from overai.overlay import Overlay

class SimpleDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        # Create overlay
        overlay = Overlay(x=100, y=100, width=400, height=300)
        overlay.create_window()
        overlay.show()

# Run
app = NSApplication.sharedApplication()
app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)
delegate = SimpleDelegate.alloc().init()
app.setDelegate_(delegate)
app.run()
```

## Core Concepts

### The Overlay Class

The `Overlay` class is the main component of the library. It handles:

- Window creation and management
- Transparency control
- Click-through behavior
- Content management
- Position and sizing

### Window Lifecycle

1. **Create** - Initialize the `Overlay` object with desired properties
2. **Configure** - Call `create_window()` to create the actual window
3. **Populate** - Add content (webview, custom views, drag area)
4. **Display** - Call `show()` to make the overlay visible
5. **Manage** - Control visibility, transparency, position dynamically

## API Reference

### Overlay Constructor

```python
Overlay(
    x=500,                      # int: X position
    y=200,                      # int: Y position
    width=550,                  # int: Window width
    height=580,                 # int: Window height
    transparency=1.0,           # float: 0.0-1.0 (0=invisible, 1=opaque)
    corner_radius=15.0,         # float: Corner radius in pixels
    click_through=False,        # bool: Allow clicks to pass through
    draggable=True,             # bool: Enable window dragging
    always_on_top=True,         # bool: Keep above other windows
    show_in_all_spaces=True,    # bool: Show in all virtual desktops
    hide_from_recordings=True,  # bool: Hide from screen recordings
    border_width=0,             # int: Border width in pixels
    border_color=None,          # NSColor: Border color
)
```

### Window Management Methods

#### `create_window()`
Creates and configures the overlay window. Must be called before showing.

```python
overlay = Overlay(x=100, y=100, width=400, height=300)
overlay.create_window()
```

#### `show()`
Makes the overlay visible and brings it to front.

```python
overlay.show()
```

#### `hide()`
Hides the overlay window.

```python
overlay.hide()
```

#### `show_for_duration(duration)`
Shows the overlay for a specified number of seconds, then automatically hides it.

```python
overlay.show_for_duration(5.0)  # Show for 5 seconds
```

### Transparency Methods

#### `set_transparency(alpha)`
Set the window transparency level.

```python
overlay.set_transparency(0.8)  # 80% opaque
```

#### `increase_transparency(amount=0.1)`
Make the overlay more opaque.

```python
overlay.increase_transparency(0.1)  # Increase by 10%
```

#### `decrease_transparency(amount=0.1)`
Make the overlay more transparent.

```python
overlay.decrease_transparency(0.1)  # Decrease by 10%
```

### Position and Size Methods

#### `set_position(x, y)`
Move the overlay to a new position.

```python
overlay.set_position(200, 300)
```

#### `set_size(width, height)`
Resize the overlay window.

```python
overlay.set_size(600, 400)
```

### Content Methods

#### `add_drag_area(height=30, background_color=None)`
Add a draggable area at the top of the window.

```python
from AppKit import NSColor

drag_area = overlay.add_drag_area(
    height=40, 
    background_color=NSColor.grayColor()
)
```

#### `add_webview(url=None, user_agent=None)`
Add a WebKit web view to display web content.

```python
webview = overlay.add_webview(
    url="https://example.com",
    user_agent="Custom User Agent String"
)
```

#### `add_custom_view(view)`
Add any custom NSView to the overlay.

```python
from AppKit import NSTextField, NSMakeRect

label = NSTextField.alloc().initWithFrame_(NSMakeRect(10, 10, 200, 30))
label.setStringValue_("Hello, World!")
overlay.add_custom_view(label)
```

## Advanced Usage

### Click-Through Overlays

Create an overlay that doesn't capture mouse events:

```python
overlay = Overlay(
    x=100, y=100, width=400, height=300,
    click_through=True,  # Enable click-through
    always_on_top=True,
)
overlay.create_window()
overlay.show()
```

### Custom Borders

Add a custom border with color:

```python
from AppKit import NSColor

overlay = Overlay(
    x=100, y=100, width=400, height=300,
    border_width=3,
    border_color=NSColor.redColor(),
)
overlay.create_window()
overlay.show()
```

### Auto-Hide Notifications

Create a notification-style overlay that auto-hides:

```python
class NotificationDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        overlay = Overlay(
            x=100, y=100, width=300, height=100,
            transparency=0.95,
            corner_radius=10,
        )
        overlay.create_window()
        
        # Add content
        from AppKit import NSTextField, NSMakeRect
        label = NSTextField.alloc().initWithFrame_(NSMakeRect(10, 30, 280, 40))
        label.setStringValue_("This is a notification!")
        label.setBezeled_(False)
        label.setDrawsBackground_(False)
        overlay.add_custom_view(label)
        
        # Show for 3 seconds
        overlay.show_for_duration(3.0)
```

### Multiple Overlays

You can create and manage multiple overlays:

```python
class MultiOverlayDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        # Create first overlay
        self.overlay1 = Overlay(x=100, y=100, width=300, height=200)
        self.overlay1.create_window()
        self.overlay1.show()
        
        # Create second overlay
        self.overlay2 = Overlay(x=450, y=100, width=300, height=200)
        self.overlay2.create_window()
        self.overlay2.show()
```

### Dynamic Transparency Control

Add buttons to control transparency:

```python
from AppKit import NSButton, NSRoundedBezelStyle, NSMakeRect

class TransparencyDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        self.overlay = Overlay(x=100, y=100, width=400, height=300)
        self.overlay.create_window()
        
        # Add increase button
        btn_up = NSButton.alloc().initWithFrame_(NSMakeRect(100, 50, 80, 30))
        btn_up.setTitle_("Opaque +")
        btn_up.setBezelStyle_(NSRoundedBezelStyle)
        btn_up.setTarget_(self)
        btn_up.setAction_("increaseOpacity:")
        self.overlay.add_custom_view(btn_up)
        
        # Add decrease button
        btn_down = NSButton.alloc().initWithFrame_(NSMakeRect(220, 50, 80, 30))
        btn_down.setTitle_("Transparent -")
        btn_down.setBezelStyle_(NSRoundedBezelStyle)
        btn_down.setTarget_(self)
        btn_down.setAction_("decreaseOpacity:")
        self.overlay.add_custom_view(btn_down)
        
        self.overlay.show()
    
    def increaseOpacity_(self, sender):
        self.overlay.increase_transparency(0.1)
    
    def decreaseOpacity_(self, sender):
        self.overlay.decrease_transparency(0.1)
```

## Examples

See the `examples/` directory for complete working examples:

- `simple_overlay.py` - Basic overlay with web view
- `clickthrough_overlay.py` - Click-through overlay
- `autohide_overlay.py` - Auto-hiding overlay  
- `transparency_control.py` - Dynamic transparency

## Tips and Best Practices

1. **Always create window before showing**: Call `create_window()` before `show()`
2. **Use NSApplicationActivationPolicyAccessory**: For overlays without dock icon
3. **Manage memory**: Keep references to overlays to prevent garbage collection
4. **Test permissions**: Some features require macOS permissions
5. **Use auto-hide for notifications**: Better UX for temporary messages
6. **Add drag areas**: Makes overlays more user-friendly
7. **Consider click-through**: For HUD-style overlays that shouldn't block interaction

## Troubleshooting

### Overlay not showing
- Ensure you called `create_window()` before `show()`
- Check transparency is not set to 0.0
- Verify window is not positioned off-screen

### Click-through not working
- Set `click_through=True` in constructor
- Note: Click-through windows can't become key window

### Auto-hide not working
- Ensure app is running in main loop
- Check timer is not being garbage collected

## Platform Requirements

- **macOS Version**: 10.15 (Catalina) or later
- **Python Version**: 3.10 or later
- **PyObjC Version**: 9.0 or later

## Support

For issues, questions, or contributions:
- GitHub: https://github.com/pc-style/overplay-mac
- Issues: https://github.com/pc-style/overplay-mac/issues
