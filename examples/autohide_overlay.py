#!/usr/bin/env python3
"""
Auto-Hide Overlay Example

This example demonstrates creating an overlay that automatically hides
after a specified duration.
"""

from AppKit import (
    NSApplication,
    NSObject,
    NSApplicationActivationPolicyAccessory,
    NSColor,
    NSTextField,
    NSFont,
    NSMakeRect,
    NSButton,
    NSRoundedBezelStyle,
)
from overai.overlay import Overlay


class AutoHideDelegate(NSObject):
    """Application delegate for auto-hide overlay example."""
    
    def applicationDidFinishLaunching_(self, notification):
        # Create an overlay that will auto-hide
        self.overlay = Overlay(
            x=300,
            y=400,
            width=500,
            height=300,
            transparency=0.9,
            corner_radius=25.0,
            always_on_top=True,
        )
        
        # Create the window
        self.overlay.create_window()
        
        # Add a draggable area
        self.overlay.add_drag_area(height=50)
        
        # Add a label
        label = NSTextField.alloc().initWithFrame_(NSMakeRect(50, 150, 400, 40))
        label.setStringValue_("This overlay will hide in 5 seconds...")
        label.setBezeled_(False)
        label.setDrawsBackground_(False)
        label.setEditable_(False)
        label.setSelectable_(False)
        label.setFont_(NSFont.boldSystemFontOfSize_(20))
        label.setAlignment_(1)  # Center alignment
        
        # Add a button to show again
        button = NSButton.alloc().initWithFrame_(NSMakeRect(175, 80, 150, 40))
        button.setTitle_("Show for 5s Again")
        button.setBezelStyle_(NSRoundedBezelStyle)
        button.setTarget_(self)
        button.setAction_("showAgain:")
        
        self.overlay.add_custom_view(label)
        self.overlay.add_custom_view(button)
        
        # Show for 5 seconds
        self.overlay.show_for_duration(5.0)
        
        print("Auto-hide overlay created!")
        print("The overlay will automatically hide after 5 seconds")
        print("Click the button to show it again for another 5 seconds")
    
    def showAgain_(self, sender):
        """Show the overlay again for 5 seconds."""
        print("Showing overlay for another 5 seconds...")
        self.overlay.show_for_duration(5.0)


def main():
    """Run the auto-hide overlay example."""
    app = NSApplication.sharedApplication()
    app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)
    
    delegate = AutoHideDelegate.alloc().init()
    app.setDelegate_(delegate)
    
    app.run()


if __name__ == "__main__":
    main()
