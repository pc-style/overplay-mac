# Installation and Testing Guide

This guide explains how to install and test the macOS Overlay Library.

## System Requirements

⚠️ **IMPORTANT**: This library only works on macOS (10.15 Catalina or later) as it uses PyObjC to interface with Apple's native frameworks.

- **Operating System**: macOS 10.15+ (Catalina, Big Sur, Monterey, Ventura, Sonoma)
- **Python Version**: 3.10 or later
- **Required Frameworks**: AppKit, Quartz, WebKit (bundled with macOS)

## Installation

### Option 1: From Source (Recommended for Development)

```bash
# Clone the repository
git clone https://github.com/pc-style/overplay-mac.git
cd overplay-mac

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install in development mode
pip install -e .
```

### Option 2: From Source (Standard Install)

```bash
# Clone the repository
git clone https://github.com/pc-style/overplay-mac.git
cd overplay-mac

# Install
pip install .
```

### Option 3: Direct Install from Git (Future)

```bash
pip install git+https://github.com/pc-style/overplay-mac.git
```

## Verifying Installation

After installation, verify the library is available:

```bash
python3 -c "from overai.overlay import Overlay; print('✓ Library installed successfully')"
```

You should see: `✓ Library installed successfully`

## Testing the Library

### Running Examples

The `examples/` directory contains four test scripts:

```bash
# Test basic overlay
python3 examples/simple_overlay.py

# Test click-through functionality
python3 examples/clickthrough_overlay.py

# Test auto-hide feature
python3 examples/autohide_overlay.py

# Test transparency controls
python3 examples/transparency_control.py
```

### What to Expect

When running examples, you should see:

1. **Initial Console Output**: Each example prints information about what it's doing
2. **Overlay Window**: A floating window appears on your screen with the configured properties
3. **Interactive Elements**: Depending on the example, buttons, drag areas, or web content

### Permissions

Some examples may trigger macOS permission dialogs:

- **Accessibility**: For global keyboard shortcuts (original OverAI app only)
- **Microphone**: For voice features (original OverAI app only)
- **Screen Recording**: Generally not needed for the library itself

Grant these permissions in **System Settings → Privacy & Security** if needed.

## Running the Original OverAI App

The original OverAI application is still available:

```bash
# Run directly
python3 OverAI.py

# Or via command line (if installed)
overai
```

### OverAI Command Line Options

```bash
# Install OverAI to run at login
overai --install-startup

# Uninstall from login items
overai --uninstall-startup

# Check accessibility permissions
overai --check-permissions
```

## Building a Standalone App (Advanced)

To create a standalone .app bundle:

```bash
# Install py2app
pip install py2app

# Build the app
python setup.py py2app

# The app will be in dist/OverAI.app
```

## Troubleshooting

### Import Error: No module named 'Quartz'

**Problem**: PyObjC frameworks not installed or not on macOS.

**Solution**:
```bash
pip install pyobjc pyobjc-framework-Quartz pyobjc-framework-WebKit
```

If this fails, ensure you're on macOS. The library will not work on Linux or Windows.

### Window Not Appearing

**Checklist**:
1. Did you call `overlay.create_window()` before `show()`?
2. Is transparency set to 0.0 (fully transparent)?
3. Is the window positioned off-screen?
4. Is your Python script running the app event loop (`app.run()`)?

**Example Fix**:
```python
overlay = Overlay(x=100, y=100, width=400, height=300)
overlay.create_window()  # Don't forget this!
overlay.show()
```

### Click-Through Not Working

**Problem**: Window still captures mouse events.

**Solution**: Ensure `click_through=True` in the constructor:
```python
overlay = Overlay(click_through=True, ...)
```

### Auto-Hide Not Working

**Problem**: Overlay doesn't hide automatically.

**Solution**: Ensure the app is running in the main event loop:
```python
# At the end of your script
app.run()  # This must be called for timers to work
```

### Permission Denied Errors

**Problem**: macOS blocking certain operations.

**Solution**: Grant necessary permissions in System Settings:
- **Accessibility**: System Settings → Privacy & Security → Accessibility
- **Microphone**: System Settings → Privacy & Security → Microphone

## Development Workflow

### Making Changes to the Library

1. Install in development mode: `pip install -e .`
2. Make changes to `overai/overlay.py`
3. Test immediately without reinstalling: `python3 examples/simple_overlay.py`
4. Changes are reflected immediately in development mode

### Adding New Examples

1. Create a new file in `examples/`
2. Follow the pattern from existing examples
3. Document the example in `examples/README.md`

### Code Style

- Follow PEP 8 conventions
- Use descriptive variable names
- Add docstrings to public methods
- Keep methods focused and single-purpose

## Testing Checklist

Before submitting changes, verify:

- [ ] All examples run without errors
- [ ] No syntax errors: `python3 -m py_compile overai/overlay.py`
- [ ] Documentation updated if API changed
- [ ] New features have example usage
- [ ] README.md reflects any new capabilities

## Getting Help

- **Documentation**: See [USAGE.md](USAGE.md) for API reference
- **Examples**: Check `examples/` directory
- **Issues**: https://github.com/pc-style/overplay-mac/issues

## Next Steps

After successful installation:

1. **Explore Examples**: Run all four examples to see capabilities
2. **Read USAGE.md**: Learn the complete API
3. **Create Your Overlay**: Use examples as templates
4. **Share Your Creation**: Contribute back to the project

Happy coding! 🎨
