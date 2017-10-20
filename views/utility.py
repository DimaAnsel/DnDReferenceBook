################################
# utility.py
# Noah Ansel
# 2017-09-27
# ------------------------------
# Generic utility functions for cleaning up Tkinter code.
################################

from tkinter import *
from PIL import Image, ImageTk
from base_view import BaseView

########
# Replaces text in a static view
def update_text(widget, value):
  widget.config(state = NORMAL)
  widget.delete(1.0, END)
  widget.insert(END, value)
  widget.config(state = DISABLED)

def update_img(widget, filepath, maxSize = 300):
  tkImg = get_img(filepath, maxSize)
  widget.config(image = tkImg)
  widget.photo = tkImg

def get_img(filepath, maxSize = 300):
  img = None
  try:
    img = Image.open(filepath)
  except Exception:
    img = Image.open(BaseView.DEFAULT_IMG)
  newSize = list(img.size)
  if newSize[0] > maxSize:
    ratio = newSize[0] / maxSize 
    newSize[0] = maxSize
    newSize[1] = int(newSize[1] / ratio)
  if newSize[1] > maxSize:
    ratio = newSize[1] / maxSize
    newSize[1] = maxSize
    newSize[0] = int(newSize[0] / ratio)
  if newSize[0] != img.size[0]:
    img = img.resize(tuple(newSize))
  return ImageTk.PhotoImage(img)


def update_combobox(widget, values):
  widget.config(state = NORMAL)
  widget.delete(0, END)
  widget.config(values = values)
  widget.config(state = "readonly")
  if len(values) > 0:
    widget.current(0)
