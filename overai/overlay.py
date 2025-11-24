"""
overlay.py

A flexible, customizable overlay window library for macOS using PyObjC.
Supports transparency, click-through, borders, auto-hide, and more.
"""

import objc
from AppKit import *
from WebKit import *
from Quartz import *
from Foundation import NSObject, NSURL, NSURLRequest


class OverlayWindow(NSWindow):
    """Custom overlay window with configurable properties."""
    
    def __init__(self, click_through=False):
        """Initialize the overlay window.
        
        Args:
            click_through: If True, mouse events pass through the window
        """
        self._click_through = click_through
        super(OverlayWindow, self).__init__()
    
    def canBecomeKeyWindow(self):
        """Allow window to become key window unless click-through is enabled."""
        return not self._click_through
    
    def ignoresMouseEvents(self):
        """Return whether the window ignores mouse events (click-through)."""
        return self._click_through


class Overlay:
    """
    A customizable overlay window for macOS.
    
    This class provides a simple API to create transparent, always-on-top
    overlay windows with various customization options including:
    - Transparency control
    - Click-through mode
    - Custom borders and corner radius
    - Auto-hide after duration
    - Drag-to-move capability
    - Custom content (WebView or custom NSView)
    """
    
    def __init__(
        self,
        x=500,
        y=200,
        width=550,
        height=580,
        transparency=1.0,
        corner_radius=15.0,
        click_through=False,
        draggable=True,
        always_on_top=True,
        show_in_all_spaces=True,
        hide_from_recordings=True,
        border_width=0,
        border_color=None,
    ):
        """
        Initialize an overlay window.
        
        Args:
            x: X position of the window
            y: Y position of the window
            width: Width of the window
            height: Height of the window
            transparency: Alpha value (0.0 to 1.0), where 1.0 is fully opaque
            corner_radius: Corner radius for rounded corners (0 for square)
            click_through: If True, mouse clicks pass through the window
            draggable: If True, window can be dragged (requires a drag area)
            always_on_top: If True, window stays on top of other windows
            show_in_all_spaces: If True, window appears in all virtual desktops
            hide_from_recordings: If True, window is invisible in screen recordings
            border_width: Width of the border (0 for no border)
            border_color: NSColor for the border (defaults to clear if None)
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.transparency = max(0.0, min(1.0, transparency))
        self.corner_radius = corner_radius
        self.click_through = click_through
        self.draggable = draggable
        self.always_on_top = always_on_top
        self.show_in_all_spaces = show_in_all_spaces
        self.hide_from_recordings = hide_from_recordings
        self.border_width = border_width
        self.border_color = border_color or NSColor.clearColor()
        
        self.window = None
        self.content_view = None
        self.drag_area = None
        self.auto_hide_timer = None
        
    def create_window(self):
        """Create and configure the overlay window."""
        # Create borderless, optionally resizable window
        style_mask = NSBorderlessWindowMask
        if not self.click_through:
            style_mask |= NSResizableWindowMask
            
        self.window = OverlayWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            NSMakeRect(self.x, self.y, self.width, self.height),
            style_mask,
            NSBackingStoreBuffered,
            False
        )
        
        # Configure window level
        if self.always_on_top:
            self.window.setLevel_(NSFloatingWindowLevel)
        
        # Configure window behavior
        collection_behavior = 0
        if self.show_in_all_spaces:
            collection_behavior |= NSWindowCollectionBehaviorCanJoinAllSpaces
            collection_behavior |= NSWindowCollectionBehaviorStationary
        if collection_behavior:
            self.window.setCollectionBehavior_(collection_behavior)
        
        # Set transparency
        self.window.setOpaque_(False)
        self.window.setBackgroundColor_(NSColor.clearColor())
        self.window.setAlphaValue_(self.transparency)
        
        # Hide from screen recordings if requested
        if self.hide_from_recordings:
            self.window.setSharingType_(NSWindowSharingNone)
        
        # Set up content view with rounded corners and border
        content_view = NSView.alloc().initWithFrame_(self.window.contentView().bounds())
        content_view.setWantsLayer_(True)
        content_view.layer().setCornerRadius_(self.corner_radius)
        content_view.layer().setBackgroundColor_(NSColor.whiteColor().CGColor())
        
        # Add border if requested
        if self.border_width > 0:
            content_view.layer().setBorderWidth_(self.border_width)
            content_view.layer().setBorderColor_(self.border_color.CGColor())
        
        self.window.setContentView_(content_view)
        self.content_view = content_view
        
        # Set click-through behavior
        if self.click_through:
            self.window.setIgnoresMouseEvents_(True)
        
        return self.window
    
    def add_drag_area(self, height=30, background_color=None):
        """
        Add a draggable area at the top of the window.
        
        Args:
            height: Height of the drag area in pixels
            background_color: NSColor for the drag area background
        
        Returns:
            The drag area NSView
        """
        if not self.draggable or self.click_through:
            return None
            
        bounds = self.content_view.bounds()
        drag_area = DragArea.alloc().initWithFrame_(
            NSMakeRect(0, bounds.size.height - height, bounds.size.width, height)
        )
        
        if background_color:
            drag_area.setBackgroundColor_(background_color)
        
        self.content_view.addSubview_(drag_area)
        self.drag_area = drag_area
        return drag_area
    
    def set_transparency(self, alpha):
        """
        Set window transparency.
        
        Args:
            alpha: Alpha value from 0.0 (fully transparent) to 1.0 (fully opaque)
        """
        self.transparency = max(0.0, min(1.0, alpha))
        if self.window:
            self.window.setAlphaValue_(self.transparency)
    
    def increase_transparency(self, amount=0.1):
        """Increase transparency (make more opaque) by the specified amount."""
        self.set_transparency(self.transparency + amount)
    
    def decrease_transparency(self, amount=0.1):
        """Decrease transparency (make more transparent) by the specified amount."""
        self.set_transparency(self.transparency - amount)
    
    def show(self):
        """Show the overlay window."""
        if self.window:
            self.window.orderFront_(None)
            if not self.click_through:
                self.window.makeKeyAndOrderFront_(None)
    
    def hide(self):
        """Hide the overlay window."""
        if self.window:
            self.window.orderOut_(None)
    
    def show_for_duration(self, duration):
        """
        Show the overlay for a specified duration, then hide it.
        
        Args:
            duration: Duration in seconds to show the overlay
        """
        self.show()
        
        # Cancel any existing timer
        if self.auto_hide_timer:
            self.auto_hide_timer.invalidate()
        
        # Create a new timer to hide the window
        self.auto_hide_timer = NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
            duration,
            self,
            "hideWindow:",
            None,
            False
        )
    
    def hideWindow_(self, timer):
        """Timer callback to hide the window."""
        self.hide()
    
    def set_position(self, x, y):
        """Set the window position."""
        if self.window:
            self.window.setFrameOrigin_(NSPoint(x, y))
    
    def set_size(self, width, height):
        """Set the window size."""
        if self.window:
            frame = self.window.frame()
            frame.size = NSSize(width, height)
            self.window.setFrame_display_(frame, True)
    
    def add_webview(self, url=None, user_agent=None):
        """
        Add a WebView to the overlay.
        
        Args:
            url: URL to load in the WebView
            user_agent: Custom user agent string
        
        Returns:
            The WKWebView instance
        """
        config = WKWebViewConfiguration.alloc().init()
        config.preferences().setJavaScriptCanOpenWindowsAutomatically_(True)
        
        # Calculate frame (below drag area if it exists)
        bounds = self.content_view.bounds()
        if self.drag_area:
            drag_height = self.drag_area.frame().size.height
            webview_frame = NSMakeRect(0, 0, bounds.size.width, bounds.size.height - drag_height)
        else:
            webview_frame = bounds
        
        webview = WKWebView.alloc().initWithFrame_configuration_(webview_frame, config)
        webview.setAutoresizingMask_(NSViewWidthSizable | NSViewHeightSizable)
        
        if user_agent:
            webview.setCustomUserAgent_(user_agent)
        
        self.content_view.addSubview_(webview)
        
        if url:
            nsurl = NSURL.URLWithString_(url)
            request = NSURLRequest.requestWithURL_(nsurl)
            webview.loadRequest_(request)
        
        return webview
    
    def add_custom_view(self, view):
        """
        Add a custom NSView to the overlay.
        
        Args:
            view: NSView instance to add
        
        Returns:
            The added view
        """
        if self.content_view:
            self.content_view.addSubview_(view)
        return view


class DragArea(NSView):
    """A view that allows dragging the window."""
    
    def initWithFrame_(self, frame):
        objc.super(DragArea, self).initWithFrame_(frame)
        self.setWantsLayer_(True)
        return self
    
    def setBackgroundColor_(self, color):
        """Set the background color of the drag area."""
        self.layer().setBackgroundColor_(color.CGColor())
    
    def mouseDown_(self, event):
        """Handle mouse down to initiate window dragging."""
        self.window().performWindowDragWithEvent_(event)
