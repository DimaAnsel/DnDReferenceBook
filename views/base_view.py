################################
# view.py
# Noah Ansel
# 2017-10-17
# ------------------------------
# Abstract class for all views of the DnD reference book.
################################

from tkinter import *


class BaseView(Frame):

  EMPTY_STR = ""
  DEFAULT = "??"
  DEFAULT_IMG = "assets/default_img.png"

  # Magic Wand by useiconic.com from the Noun Project
  WAND_IMG = {True:  "assets/is_spell.png",
              False: "assets/not_spell.png"}

  # Coins by Ben Iconator from the Noun Project
  VALUE_IMG = "assets/coins.png"

  TYPE_MAP = ("Item",
              "Consumable",
              "Armor",
              "Weapon")

  RARITY_IMG = {None: "assets/unknown_rarity.png",
                0:    "assets/common.png",
                1:    "assets/uncommon.png",
                2:    "assets/rare.png",
                3:    "assets/legendary.png"}

  LARGE_FONT  = ("Calibri", 16, "bold")
  NORMAL_FONT = ("Calibri", 10)
  BOLD_FONT   = ("Calibri", 10, "bold")

  ########
  # Creates widgets and, if given data, populates them.
  def __init__(self, master, data = None, refBook = None, omniscient = True):
    super().__init__(master)
    self._refBook = refBook
    self._data = data
    self._omniscient = omniscient
    self._create_widgets()
    self._bind_widgets()
    if data != None:
      self.populate(data)
    else:
      self.set_defaults()

  ########
  # Initializes and places all GUI elements.
  def _create_widgets(self):
    pass

  ########
  # Add callbacks for all GUI element events and Tkinter variables.
  def _bind_widgets(self):
    pass

  ########
  # Populates all GUI elements with new data.
  def populate(self, data):
    self._data = data
    pass

  ########
  # Resets GUI elements to default values.
  def set_defaults(self):
    pass
