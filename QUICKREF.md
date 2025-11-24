# Quick Reference Cheatsheet

## Basic Overlay Creation

```python
from AppKit import NSApplication, NSObject, NSApplicationActivationPolicyAccessory
from overai.overlay import Overlay

class MyDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        overlay = Overlay(x=100, y=100, width=400, height=300)
        overlay.create_window()
        overlay.show()

app = NSApplication.sharedApplication()
app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)
delegate = MyDelegate.alloc().init()
app.setDelegate_(delegate)
app.run()
```

## Common Configurations

### Transparent Overlay
```python
overlay = Overlay(transparency=0.8)  # 80% opaque
```

### Click-Through Overlay
```python
overlay = Overlay(click_through=True)  # Clicks pass through
```

### Overlay with Border
```python
from AppKit import NSColor
overlay = Overlay(
    border_width=3,
    border_color=NSColor.redColor()
)
```

### Auto-Hide Overlay
```python
overlay.show_for_duration(5.0)  # Show for 5 seconds
```

### Rounded Corners
```python
overlay = Overlay(corner_radius=20.0)  # 20px radius
```

## Common Methods

### Window Management
```python
overlay.create_window()           # Create window (required)
overlay.show()                    # Show window
overlay.hide()                    # Hide window
overlay.show_for_duration(3.0)    # Show then auto-hide
```

### Transparency Control
```python
overlay.set_transparency(0.9)     # Set to 90% opaque
overlay.increase_transparency()   # +10% opacity
overlay.decrease_transparency()   # -10% opacity
```

### Position & Size
```python
overlay.set_position(200, 300)    # Move to (200, 300)
overlay.set_size(600, 400)        # Resize to 600x400
```

### Adding Content

#### Web View
```python
overlay.add_webview(
    url="https://example.com",
    user_agent="Custom UA"
)
```

#### Drag Area
```python
from AppKit import NSColor
overlay.add_drag_area(
    height=40,
    background_color=NSColor.grayColor()
)
```

#### Custom View
```python
from AppKit import NSTextField, NSMakeRect

label = NSTextField.alloc().initWithFrame_(NSMakeRect(10, 10, 200, 30))
label.setStringValue_("Hello!")
overlay.add_custom_view(label)
```

## Constructor Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| x | int | 500 | X position |
| y | int | 200 | Y position |
| width | int | 550 | Window width |
| height | int | 580 | Window height |
| transparency | float | 1.0 | 0.0-1.0 (0=invisible) |
| corner_radius | float | 15.0 | Corner radius in pixels |
| click_through | bool | False | Pass clicks through |
| draggable | bool | True | Allow dragging |
| always_on_top | bool | True | Stay above windows |
| show_in_all_spaces | bool | True | All virtual desktops |
| hide_from_recordings | bool | True | Invisible in recordings |
| border_width | int | 0 | Border width |
| border_color | NSColor | None | Border color |

## Quick Examples

### Notification-Style Overlay
```python
overlay = Overlay(
    x=100, y=50, width=300, height=80,
    transparency=0.95,
    corner_radius=10,
    draggable=False
)
overlay.create_window()
overlay.show_for_duration(3.0)
```

### HUD-Style Click-Through
```python
overlay = Overlay(
    x=50, y=50, width=200, height=100,
    transparency=0.7,
    click_through=True,
    border_width=2,
    border_color=NSColor.greenColor()
)
overlay.create_window()
overlay.show()
```

### Web Browser Overlay
```python
overlay = Overlay(
    x=200, y=200, width=800, height=600,
    transparency=0.95,
    corner_radius=20
)
overlay.create_window()
overlay.add_drag_area(height=40)
overlay.add_webview(url="https://example.com")
overlay.show()
```

## Tips

✅ **DO**:
- Call `create_window()` before `show()`
- Keep references to overlays to prevent GC
- Use `NSApplicationActivationPolicyAccessory` for no dock icon
- Add drag areas for better UX

❌ **DON'T**:
- Forget to call `create_window()`
- Set transparency to 0.0 and wonder why nothing shows
- Use click-through for interactive overlays
- Position windows off-screen (negative coords)

## Common Imports

```python
from AppKit import (
    NSApplication,
    NSObject,
    NSApplicationActivationPolicyAccessory,
    NSColor,
    NSTextField,
    NSButton,
    NSMakeRect,
    NSFont,
    NSRoundedBezelStyle,
)
from overai.overlay import Overlay
```

## See Also

- Full API: [USAGE.md](USAGE.md)
- Examples: [examples/README.md](examples/README.md)
- Installation: [INSTALL.md](INSTALL.md)
