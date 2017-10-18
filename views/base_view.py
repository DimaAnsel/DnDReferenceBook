################################
# view.py
# Noah Ansel
# 2017-10-17
# ------------------------------
# Abstract class for all views of the DnD reference book.
################################

from tkinter import *


class BaseView(Frame):

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

  def __init__(self, master, data = None, omniscient = True):
    super().__init__(master)
    self._omniscient = omniscient
    self._create_widgets()
    if data != None:
      self.populate(data)
    else:
      self.set_defaults()

  def _create_widgets(self):
    pass

  def populate(self, data):
    pass

  def set_defaults(self):
    pass
