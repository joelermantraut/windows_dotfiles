#!/usr/bin/env python

"""
This script runs Gopass, gets the output, and
writes it using pyautogui module.
"""

import subprocess
import tkinter as tk
from pathlib import Path
import os
import pyautogui
import screeninfo

the_password = None

class Selector:
    def __init__(self, pass_list):
        self.pass_list = pass_list
        self.init()

    def init(self):
        """
        Init method.
        """
        self.master = tk.Tk()
        self.master.title("Password Manager")
        self.master.overrideredirect(True)

        self.master.bind("<Escape>", self.destroy)

        monitor = screeninfo.get_monitors()[0]
        width = 500
        height = 600
        x = int(monitor.width / 2 - width / 2)
        y = int(monitor.height / 2 - height / 2) - 20
        self.master.geometry(f"{width}x{height}+{x}+{y}")
        # All this to set width, height, and center
        self.generate_gui()
        self.input.focus()

        self.master.mainloop()

    def fill_listbox(self, string=""):
        """
        Fills listbox with pass_list. If a string
        is passed, filter using it.
        """
        for item_index in range(len(self.pass_list)):
            item = self.pass_list[item_index]
            if string.lower() in item.lower():
                # Takes both lower and upper
                self.listbox.insert(item_index, self.pass_list[item_index])

    def press_keys(self, event):
        """
        When any key is pressed in input element.
        """
        keycode = event.keycode
        string = self.input_content.get()

        if keycode == 13:
            self.double_click_event(None)
        else:
            self.listbox.delete(0, tk.END)
            self.fill_listbox(string)

    def generate_gui(self):
        """
        Generates a GUI to select a password.
        """
        self.input_content = tk.StringVar()
        self.input = tk.Entry(
            self.master,
            textvariable = self.input_content,
            font = ("Arial", 12),
            bg = "#4E0DDE",
            fg = "#FFFFFF"
        )
        self.input.bind("<KeyRelease>", self.press_keys)
        self.input.pack(fill = tk.BOTH)

        self.listbox = tk.Listbox(
            self.master,
            bg = "#4E0DDE",
            fg = "#FFFFFF",
            font = ("Arial", 12),
            borderwidth=0,
            highlightthickness=0
        )
        self.fill_listbox()
        self.listbox.bind('<Double-Button-1>', self.double_click_event)
        self.listbox.pack(fill = tk.BOTH, expand = tk.YES)

    def double_click_event(self, event):
        """
        Listbox double click handler.
        """
        global the_password

        selected = self.listbox.curselection()

        if not selected:
            selection = self.listbox.get(0)
        else:
            selection = self.listbox.get(selected)

        the_password = selection
        self.destroy()

    def destroy(self, event=None):
        """
        Destroys window.
        """
        self.master.destroy()

def get_cmd_output(cmd):
    """
    Runs a cmd and returns its output.
    """
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, _) = p.communicate()
    result = output.decode()
    return result

def get_passwords_list(folder_path):
    """
    Gets list of paths.
    """
    pathlist = list()
    for path in Path(folder_path).rglob("*.gpg"):
        name = path.name.split(".")
        name.pop()
        name = ".".join(name)
        # Gets name without .gpg
        last_parent = path.parent.__str__().split("\\")[-1]
        # Gets last parent's name
        if last_parent in ["branches", "hooks", "info", "objects", "refs"]:
            continue
            # Special folders
        elif last_parent != "password":
            pathlist.append("{}({})".format(name, last_parent))
        else:
            pathlist.append(name)

    pathlist.sort()
    # Alphabetic sort
    return pathlist

def get_pass(name):
    """
    Get the pass with gopass utility.
    """
    if "(" in name:
        name = name.split("(")
        basename = name[0]
        parent = name[1][:-1]
        name = "{}/{}".format(parent, basename)

    password = get_cmd_output("gopass show {}".format(name))
    return password

def write_pass(password):
    """
    Writes the password passed with pyautogui.
    """
    pyautogui.write(password)
    pyautogui.press("enter")

def main():
    PASSWORD_PATH = r"D:\\Documentos\\password"

    pass_list = get_passwords_list(PASSWORD_PATH)
    selector = Selector(pass_list)

    if the_password:
        write_pass(get_pass(the_password))
    # Maybe window is closed without selection

if __name__ == "__main__":
    main()