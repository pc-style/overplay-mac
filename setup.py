# setup.py
from setuptools import setup, find_packages
import os
import sys

# Read version
def read_about_file(fname, default=""):
    try:
        about_dir = os.path.join("overai", "about")
        with open(os.path.join(about_dir, fname)) as f:
            return f.read().strip()
    except (FileNotFoundError, IOError, OSError):
        return default

version = read_about_file("version.txt", "0.1.0")

# Read long description from README
try:
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()
except (FileNotFoundError, IOError):
    long_description = "A flexible, customizable overlay window library for macOS"

# Library setup
setup(
    name="overai",
    version=version,
    author="Sai Praveen",
    description="A flexible, customizable overlay window library for macOS with transparency, click-through, and more",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pc-style/overplay-mac",
    packages=find_packages(),
    package_data={
        "overai": [
            "logo/*.png",
            "logo/*.icns",
            "about/*.txt",
        ],
    },
    install_requires=[
        "pyobjc>=9.0",
        "pyobjc-framework-Quartz>=9.0",
        "pyobjc-framework-WebKit>=9.0",
    ],
    entry_points={
        "console_scripts": [
            "overai=overai.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Desktop Environment",
    ],
    python_requires=">=3.10",
)

# py2app configuration for building the standalone app
APP = ["OverAI.py"]
DATA_FILES = []
OPTIONS = {
    # Bundle your package directory so imports "just work"
    "packages": ["overai"],
    "includes": [],
    # GUI app (no console window)
    "argv_emulation": False,
    # Optional: your .icns icon
    "iconfile": "overai/logo/icon.icns",
    # Allow microphone & Accessibility prompts by embedding Info.plist keys:
    "plist": {
        "NSMicrophoneUsageDescription": "OverAI needs your mic for voice input.",
        "NSAppleEventsUsageDescription": "OverAI needs accessibility permission for hotkeys."
    },
}

# Only configure py2app if it's being used
if "py2app" in sys.argv:
    setup(
        app=APP,
        data_files=DATA_FILES,
        options={"py2app": OPTIONS},
        setup_requires=["py2app"],
    )
