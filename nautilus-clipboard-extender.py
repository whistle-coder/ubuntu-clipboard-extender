#!/usr/bin/env python3
import gi
gi.require_version('Nautilus', '3.0')
from gi import Nautilus
from gi.repository import Gtk, Gdk, Nautilus as NautilusCore
import os
import subprocess
import threading

HISTORY_FILE = os.path.expanduser("~/.clipboard_history")
MAX_ITEMS = 50

class ClipboardHistory:
    def __init__(self):
        self.history = self.load()

    def load(self):
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, 'r') as f:
                    return [line.strip() for line in f.readlines() if line.strip()]
            except:
                return []
        return []

    def save(self):
        try:
            with open(HISTORY_FILE, 'w') as f:
                f.write('\n'.join(self.history))
        except:
            pass

    def add(self, path):
        if path in self.history:
            self.history.remove(path)
        self.history.insert(0, path)
        self.history = self.history[:MAX_ITEMS]
        self.save()

    def get_all(self):
        return self.history.copy()

clipboard_history = ClipboardHistory()

def copy_to_clipboard(text):
    proc = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
    proc.communicate(text.encode())

class ClipboardMenuExtension(NautilusCore.MenuProvider):
    def __init__(self):
        pass

    def menu_activate_cb(self, menu, file_path):
        file_path = menu.add_attribute("file_path", "uri")
        if file_path:
            file_path = file_path.replace('file://', '')
            file_path = os.path.basename(file_path)
        clipboard_history.add(file_path)
        copy_to_clipboard(file_path)

    def get_file_items(self, window):
        files = window.get_selected_files()
        if not files:
            return []

        items = []
        for i, f in enumerate(files):
            item = NautilusCore.MenuItem(
                name=f"ClipboardExtender::Copy{i}",
                label=f"Copy '{os.path.basename(f)}'",
                tip="Copy filename to clipboard history"
            )
            item.connect('activate', self.menu_activate_cb, f)
            items.append(item)

        return items