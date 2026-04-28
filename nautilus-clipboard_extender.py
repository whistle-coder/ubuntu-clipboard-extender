#!/usr/bin/env python3
"""
Nautilus Clipboard Extender Extension
Adds "Copy to Clipboard" functionality and maintains history.
"""
import os
import subprocess
from gi import require_version
require_version('Nautilus', '3.0')
from gi.repository import Nautilus, Gtk, Gdk

HISTORY_FILE = os.path.expanduser("~/.clipboard_history")
MAX_ITEMS = 50

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r') as f:
                return [line.strip() for line in f.readlines() if line.strip()]
        except:
            return []
    return []

def save_history(history):
    try:
        with open(HISTORY_FILE, 'w') as f:
            f.write('\n'.join(history))
    except:
        pass

def copy_to_clipboard(text):
    proc = subprocess.Popen(
        ['xclip', '-selection', 'clipboard'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    proc.communicate(text.encode())

class ClipboardExtender(Nautilus.MenuProvider):
    def __init__(self):
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

    def copy_to_history(self, file_path):
        history = load_history()
        if file_path in history:
            history.remove(file_path)
        history.insert(0, file_path)
        history = history[:MAX_ITEMS]
        save_history(history)

    def copy_callback(self, menu, uri):
        file_path = uri.replace('file://', '')
        path = os.path.basename(file_path)
        copy_to_clipboard(path)
        self.copy_to_history(path)

    def get_file_items(self, window):
        files = window.get_selected_files()
        if not files:
            return []

        items = []
        for uri in files:
            basename = os.path.basename(uri)
            item = Nautilus.MenuItem(
                name=f"ClipboardExtender::Copy_{basename}",
                label=f"Copy: {basename}",
                tip=f"Copy '{basename}' to clipboard"
            )
            item.connect('activate', self.copy_callback, uri)
            items.append(item)

        return items

    def get_background_items(self, window):
        return []