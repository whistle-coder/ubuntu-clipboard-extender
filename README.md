# Nautilus Clipboard Extender: Ultimate Clipboard History for Ubuntu File Manager

If you're a Linux user who frequently works with files in Nautilus (the default file manager in Ubuntu), you already know how cumbersome it can be to copy multiple file names one at a time. What if you could maintain a clipboard history of every file you copy, making it effortless to paste any previously copied filename? Enter the **Nautilus Clipboard Extender** — a Python-based Nautilus extension that transforms your file management workflow.

## What is Nautilus Clipboard Extender?

[Nautilus Clipboard Extender](https://github.com/whistle-coder/ubuntu-clipboard-extender) is an open-source extension for the GNOME Files application (Nautilus) that adds powerful clipboard history functionality. Every time you copy a filename from Nautilus, it's automatically saved to a history file that persists between sessions.

### Key Features

- **Automatic History Tracking** — Files you copy are automatically added to your clipboard history
- **Persistent Storage** — History is saved to `~/.clipboard_history` and survives restarts
- **Quick Access** — Easily paste any previously copied filename
- **Simple Installation** — No complex setup required
- **Open Source** — Free to use and modify

## Installation

Getting started with Nautilus Clipboard Extender takes just a few minutes:

```bash
# Install xclip (if not already installed)
sudo apt install xclip

# Create extension directory
mkdir -p ~/.local/share/nautilus-python/extensions

# Clone or copy the extension
git clone https://github.com/whistle-coder/clipboard-extender.git
cp clipboard-extender/nautilus-clipboard_extender.py ~/.local/share/nautilus-python/extensions/

# Restart Nautilus to activate the extension
nautilus -q
```

## How It Works

The extension integrates directly into Nautilus's context menu. When you select one or more files and choose "Copy: filename" from the right-click menu:

1. The filename is copied to your system clipboard using xclip
2. The filename is automatically added to `~/.clipboard_history`
3. You can access your full history anytime

To view your clipboard history, simply open the history file:

```bash
cat ~/.clipboard_history
```

## Why Do You Need Clipboard History?

Consider these everyday scenarios:

- **Web Development** — Copy multiple image files (logo.png, hero.jpg, icon.svg) and paste them one by one into your HTML
- **Server Management** — Copy log filenames and switch between them quickly
- **Document Organization** — Keep track of recently used filenames across different folders
- **Batch Operations** — Build a library of commonly used filenames

## Requirements

- Ubuntu or GNOME-based Linux distribution
- Python 3
- Nautilus file manager
- xclip package

## Source Code

The complete source code is available on GitHub:

**[https://github.com/whistle-coder/clipboard-extender](https://github.com/whistle-coder/clipboard-extender)**

Feel free to fork the repository, report issues, or contribute improvements!

## Conclusion

The Nautilus Clipboard Extender is a simple yet powerful tool that significantly improves productivity for Linux users who work with files regularly. By maintaining a persistent history of every filename you copy, it eliminates the frustration of losing clipboard content or needing to navigate back to a file just to copy its name again.

Try it today and experience a smoother file management workflow on Ubuntu!

---

**Tags:** #Ubuntu #Nautilus #Linux #Clipboard #Productivity #GNOME #OpenSource

see also [https://ubuntubase.com/software/nautilus-clipboard-extender-ultimate-clipboard-history-for-ubuntu-file-manager/](https://ubuntubase.com/software/nautilus-clipboard-extender-ultimate-clipboard-history-for-ubuntu-file-manager/)
