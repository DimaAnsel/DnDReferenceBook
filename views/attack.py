################################
# attack.py
# Noah Ansel
# 2017-10-16
# ------------------------------
# Tkinter view for the Attack object as presented by the DatabaseManager.
################################

from tkinter import *
from base_view import BaseView
import utility

################
# Tkinter representation of full attack object, used as separate page.
class AttackView(BaseView):
  pass
# AttackView
################

################
# Tkinter representation of simple attack object, used for previews.
class SimpleAttackView(BaseView):

  def _create_widgets(self):
    self._imgLabel = Label(self)
    self._nameLabel = Label(self, text = "Name")
    self._spellLabel = Label(self)

    self._imgLabel.grid(  row = 0, column = 0, sticky = N+W+E+S)
    self._spellLabel.grid(row = 0, column = 1, sticky = N+W+E+S)
    self._nameLabel.grid( row = 0, column = 2, sticky = W)

  def populate(self, data):
    name = ""
    for k, v in data.items():
      if k == "name":
        name = v
      elif k == "img":
        if v == None:
          v = BaseView.DEFAULT_IMG
        utility.update_img(self._imgLabel, v, maxSize = 30)
      elif k == "isSpell":
        if v == None:
          v = False
        utility.update_img(self._spellLabel, BaseView.WAND_IMG[v], maxSize = 30)
    self._nameLabel.config(text = name)


  def set_defaults(self):
    utility.update_img(self._imgLabel, BaseView.DEFAULT_IMG, maxSize = 30)
    utility.update_img(self._spellLabel, BaseView.WAND_IMG[False], maxSize = 30)
    self._nameLabel.config(text = "Name")
# SimpleAttackView
################

########
# Test code
if __name__ == "__main__":
  from DnDReferenceBook.src.dbase_manager import DatabaseManager

  root = Tk()

  dbm = DatabaseManager("../data/dnd_ref_book.db")
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
  sav = SimpleAttackView(top)
  sav.grid(row = 0, column = 0, sticky = W+E)
  sav2 = SimpleAttackView(top, dbm.get_simple_attack(0))
  sav2.grid(row = 1, column = 0, sticky = W+E)
  sav3 = SimpleAttackView(top, dbm.get_simple_attack(1))
  sav3.grid(row = 2, column = 0, sticky = W+E)
  sav4 = SimpleAttackView(top, dbm.get_simple_attack(2))
  sav4.grid(row = 3, column = 0, sticky = W+E)

  root.mainloop()
