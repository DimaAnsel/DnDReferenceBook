################################
# utility.py
# Noah Ansel
# 2017-09-27
# ------------------------------
# Generic utility functions for cleaning up Tkinter code.
################################

from tkinter import *

########
# Replaces text in a static view
def update_text(widget, value):
  widget.config(state = NORMAL)
  widget.delete(1.0, END)
  widget.insert(END, value)
  widget.config(state = DISABLED)