################################
# item.py
# Noah Ansel
# 2017-10-16
# ------------------------------
# Tkinter view for the Item object as presented by the DatabaseManager.
################################

from tkinter import *
import utility

################
# Tkinter representation of full item object, used as separate page.
class ItemView(Frame):

  DEFAULT = "??"
  DEFAULT_IMG = "default_img.png"

  # Coins by Ben Iconator from the Noun Project
  VALUE_IMG = "coins.png"

  TYPE_MAP = ("Item",
              "Consumable",
              "Armor",
              "Weapon")
# ItemView
################

################
# Tkinter representation of simple item object, used for previews.
class SimpleItemView(Frame):

  NAME_FORMAT = "{} ({})"

  def __init__(self, master, data = None):
    super().__init__(master)
    self._create_widgets()
    if data != None:
      self.populate(data)
    else:
      self.set_defaults()

  def _create_widgets(self):
    self._imgLabel = Label(self)
    self._nameLabel = Label(self, text = SimpleItemView.NAME_FORMAT.format("Name", ItemView.DEFAULT))
    self._valueImg = Label(self)
    utility.update_img(self._valueImg, ItemView.VALUE_IMG, maxSize = 30)
    self._valueLabel = Label(self)

    self._imgLabel.grid(  row = 0, column = 0, sticky = N+W+E+S)
    self._nameLabel.grid( row = 0, column = 1, sticky = W)
    self._valueImg.grid(  row = 0, column = 2, sticky = N+W+E+S)
    self._valueLabel.grid(row = 0, column = 3, sticky = W)

  def populate(self, data):
    name = ""
    itemType = 0
    for k, v in data.items():
      if k == "name":
        name = v
      elif k == "img":
        if v == None:
          v = ItemView.DEFAULT_IMG
        utility.update_img(self._imgLabel, v, maxSize = 30)
      elif k == "type":
        if v != None:
          itemType = v
      elif k == "value":
        if v == None:
          v = ItemView.DEFAULT
        self._valueLabel.config(text = v)
    self._nameLabel.config(text = SimpleItemView.NAME_FORMAT.format(name, ItemView.TYPE_MAP[itemType]))


  def set_defaults(self):
    utility.update_img(self._imgLabel, ItemView.DEFAULT_IMG, maxSize = 30)
    self._nameLabel.config(text = SimpleItemView.NAME_FORMAT.format("Name", ItemView.DEFAULT))
    self._valueLabel.config(text = ItemView.DEFAULT)
# SimpleItemView
################

########
# Test code
if __name__ == "__main__":
  from DnDReferenceBook.src.dbase_manager import DatabaseManager

  root = Tk()

  dbm = DatabaseManager("../data/dnd_ref_book.db", "../data/img/")
  dbm.reset("../src/tables.sql", "../src/real.sql")
  # cv = CreatureView(root)
  # cv.grid(row = 0, column = 0, sticky = N+W)
  # cv2 = CreatureView(root, dbm.get_attack("Flame Wisp"))
  # cv2.grid(row = 0, column = 1, sticky = N+W)
  # cv3 = CreatureView(root, dbm.get_attack("Apprentice Rock Elementalist"))
  # cv3.grid(row = 1, column = 0, sticky = N+W)
  # cv4 = CreatureView(root, dbm.get_attack("Crystalline Serpent"))
  # cv4.grid(row = 1, column = 1, sticky = N+W)

  top = Toplevel(root)
  sav = SimpleItemView(top)
  sav.grid(row = 0, column = 0, sticky = W+E)
  sav2 = SimpleItemView(top, dbm.get_simple_item("Animating Crystal"))
  sav2.grid(row = 1, column = 0, sticky = W+E)
  sav3 = SimpleItemView(top, dbm.get_simple_item("Volatile Crystal"))
  sav3.grid(row = 2, column = 0, sticky = W+E)
  sav4 = SimpleItemView(top, dbm.get_simple_item("Rock Staff"))
  sav4.grid(row = 3, column = 0, sticky = W+E)

  root.mainloop()
