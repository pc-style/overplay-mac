#!/usr/bin/env python3
"""
Transparency Control Example

This example demonstrates dynamic transparency control with buttons
to increase and decrease the overlay transparency.
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


class TransparencyDelegate(NSObject):
    """Application delegate for transparency control example."""
    
    def applicationDidFinishLaunching_(self, notification):
        # Create an overlay with medium transparency
        self.overlay = Overlay(
            x=250,
            y=250,
            width=450,
            height=350,
            transparency=0.7,
            corner_radius=20.0,
            always_on_top=True,
            border_width=3,
        )
        
        self.overlay.border_color = NSColor.blueColor()
        
        # Create the window
        self.overlay.create_window()
        
        # Add a draggable area
        self.overlay.add_drag_area(height=50)
        
        # Add status label
        self.status_label = NSTextField.alloc().initWithFrame_(NSMakeRect(50, 200, 350, 40))
        self.status_label.setStringValue_(f"Transparency: {int(self.overlay.transparency * 100)}%")
        self.status_label.setBezeled_(False)
        self.status_label.setDrawsBackground_(False)
        self.status_label.setEditable_(False)
        self.status_label.setSelectable_(False)
        self.status_label.setFont_(NSFont.boldSystemFontOfSize_(24))
        self.status_label.setAlignment_(1)  # Center
        
        # Add increase button
        increase_btn = NSButton.alloc().initWithFrame_(NSMakeRect(250, 120, 150, 40))
        increase_btn.setTitle_("More Opaque (+)")
        increase_btn.setBezelStyle_(NSRoundedBezelStyle)
        increase_btn.setTarget_(self)
        increase_btn.setAction_("increaseTransparency:")
        
        # Add decrease button
        decrease_btn = NSButton.alloc().initWithFrame_(NSMakeRect(50, 120, 150, 40))
        decrease_btn.setTitle_("More Transparent (-)")
        decrease_btn.setBezelStyle_(NSRoundedBezelStyle)
        decrease_btn.setTarget_(self)
        decrease_btn.setAction_("decreaseTransparency:")
        
        # Add instruction label
        instruction = NSTextField.alloc().initWithFrame_(NSMakeRect(50, 50, 350, 40))
        instruction.setStringValue_("Use buttons to adjust transparency")
        instruction.setBezeled_(False)
        instruction.setDrawsBackground_(False)
        instruction.setEditable_(False)
        instruction.setSelectable_(False)
        instruction.setFont_(NSFont.systemFontOfSize_(14))
        instruction.setAlignment_(1)
        
        self.overlay.add_custom_view(self.status_label)
        self.overlay.add_custom_view(increase_btn)
        self.overlay.add_custom_view(decrease_btn)
        self.overlay.add_custom_view(instruction)
        
        # Set a nice gradient background
        self.overlay.content_view.layer().setBackgroundColor_(
            NSColor.colorWithCalibratedRed_green_blue_alpha_(0.9, 0.9, 0.95, 1.0).CGColor()
        )
        
        # Show the overlay
        self.overlay.show()
        
        print("Transparency control overlay created!")
        print("Use the buttons to adjust transparency")
    
    def increaseTransparency_(self, sender):
        """Make the overlay more opaque."""
        self.overlay.increase_transparency(0.1)
        self.updateStatusLabel()
        print(f"Transparency increased to {int(self.overlay.transparency * 100)}%")
    
    def decreaseTransparency_(self, sender):
        """Make the overlay more transparent."""
        self.overlay.decrease_transparency(0.1)
        self.updateStatusLabel()
        print(f"Transparency decreased to {int(self.overlay.transparency * 100)}%")
    
    def updateStatusLabel(self):
        """Update the status label with current transparency."""
        self.status_label.setStringValue_(f"Transparency: {int(self.overlay.transparency * 100)}%")


def main():
    """Run the transparency control example."""
    app = NSApplication.sharedApplication()
    app.setActivationPolicy_(NSApplicationActivationPolicyAccessory)
    
    delegate = TransparencyDelegate.alloc().init()
    app.setDelegate_(delegate)
    
    app.run()


if __name__ == "__main__":
    main()
