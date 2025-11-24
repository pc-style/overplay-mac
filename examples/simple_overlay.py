#!/usr/bin/env python3
"""
Simple Overlay Example

This example demonstrates creating a basic overlay window with transparency
and a web view.
"""

from AppKit import NSApplication, NSObject, NSApplicationActivationPolicyAccessory
from overai.overlay import Overlay


class SimpleOverlayDelegate(NSObject):
    """Simple application delegate for the overlay example."""
    
    def applicationDidFinishLaunching_(self, notification):
        # Create an overlay with custom settings
        self.overlay = Overlay(
            x=100,
            y=100,
            width=600,
            height=400,
            transparency=0.95,
            corner_radius=20.0,
            always_on_top=True,
            hide_from_recordings=True,
        )
        
        # Create the window
        self.overlay.create_window()
        
        # Add a draggable area at the top
        self.overlay.add_drag_area(height=40)
        
        # Add a web view
        self.overlay.add_webview(
            url="https://www.example.com",
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15"
        )
        
        # Show the overlay
        self.overlay.show()
        
        print("Simple overlay created!")
        print("- Position: (100, 100)")
        print("- Size: 600x400")
        print("- Transparency: 95%")
        print("- Corner radius: 20px")


def main():
    """Run the simple overlay example."""
    app = NSApplication.sharedApplication()
    app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)
    
    delegate = SimpleOverlayDelegate.alloc().init()
    app.setDelegate_(delegate)
    
    app.run()


if __name__ == "__main__":
    main()
