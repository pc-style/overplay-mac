"""
OverAI - A macOS overlay library and app.

This library provides a simple, flexible way to create customizable overlay
windows on macOS with transparency support, click-through mode, auto-hide,
borders, and more using PyObjC.

The library can be used in two ways:
1. As a library to create custom overlays in your own applications
2. As the original OverAI application for AI assistance

-- Sai Praveen 
"""

import os

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
ABOUT_DIR = os.path.join(DIRECTORY, "about")

def _read_about_file(fname, default=""):
    try:
        with open(os.path.join(ABOUT_DIR, fname)) as f:
            return f.read().strip()
    except Exception:
        return default

__version__ = _read_about_file("version.txt", "0.0.1")
__author__ = _read_about_file("author.txt", "Sai Praveen")

# Export main for backwards compatibility with the original app
__all__ = ["main", "Overlay", "OverlayWindow", "DragArea"]

from .main import main
from .overlay import Overlay, OverlayWindow, DragArea