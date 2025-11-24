#!/usr/bin/env python3
"""
Click-Through Overlay Example

This example demonstrates creating a click-through overlay that doesn't
capture mouse events, allowing interaction with windows below it.
"""

from AppKit import (
    NSApplication, 
    NSObject, 
    NSApplicationActivationPolicyAccessory,
    NSColor,
    NSTextField,
    NSFont,
    NSMakeRect,
)
from overai.overlay import Overlay


class ClickThroughDelegate(NSObject):
    """Application delegate for click-through overlay example."""
    
    def applicationDidFinishLaunching_(self, notification):
        # Create a click-through overlay
        self.overlay = Overlay(
            x=200,
            y=300,
            width=400,
            height=200,
            transparency=0.7,
            corner_radius=15.0,
            click_through=True,  # This makes it click-through!
            always_on_top=True,
            border_width=2,
        )
        
        # Set border color to red for visibility
        self.overlay.border_color = NSColor.redColor()
        
        # Create the window
        self.overlay.create_window()
        
        # Add a text label to show it's click-through
        label = NSTextField.alloc().initWithFrame_(NSMakeRect(50, 75, 300, 50))
        label.setStringValue_("Click-Through Overlay\nYou can click through this!")
        label.setBezeled_(False)
        label.setDrawsBackground_(False)
        label.setEditable_(False)
        label.setSelectable_(False)
        label.setFont_(NSFont.boldSystemFontOfSize_(18))
        label.setTextColor_(NSColor.whiteColor())
        
        # Set background to semi-transparent blue
        self.overlay.content_view.layer().setBackgroundColor_(
            NSColor.colorWithCalibratedRed_green_blue_alpha_(0.2, 0.4, 0.8, 0.5).CGColor()
        )
        
        self.overlay.add_custom_view(label)
        
        # Show the overlay
        self.overlay.show()
        
        print("Click-through overlay created!")
        print("Try clicking on windows behind it - your clicks will pass through!")


def main():
    """Run the click-through overlay example."""
    app = NSApplication.sharedApplication()
    app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)
    
    delegate = ClickThroughDelegate.alloc().init()
    app.setDelegate_(delegate)
    
    app.run()


if __name__ == "__main__":
    main()
