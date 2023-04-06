#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
# Python Ver:    3.11.1
#
# Author:   Mitchal Larson
#
# Purpose:  Basic app to input and view student information
#
# Tested OS:    This code was written and tested to work with Windows 10

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

# Importing our other modules
import students_gui
import students_func


# Defining master Tkinter frame class
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define master frame configuration
        self.master = master
        self.master.minsize(500,350)
        self.master.maxsize(500,350)
        # CenterWindow method will center app on users screen
        students_func.center_window(self,500,350)
        self.master.title("Student Tracker")
        self.master.configure(bg="#F0F0F0")
        # Protocol method to catch if user clicks on upper corner "X"
        self.master.protocol("WM_DELETE_WINDOW", lambda: students_func.ask_quit(self))
        arg = self.master

        # Load in GUI widgets from seperate module
        students_gui.load_gui(self)

        # Instantiate Tkinter menu dropdown object
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: students_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About this phonebook demo")
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar, borderwidth='1')





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
