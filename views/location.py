################################
# location.py
# Noah Ansel
# 2017-10-16
# ------------------------------
# Tkinter view for the Location object as presented by the DatabaseManager.
################################

from tkinter import *
from base_view import BaseView
import utility

################
# Tkinter representation of full location object, used as separate page.
class LocationView(BaseView):
  pass
# LocationView
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
  sav = SimpleLocationView(top)
  sav.grid(row = 0, column = 0, sticky = W+E)
  sav2 = SimpleLocationView(top, dbm.get_simple_item("Animating Crystal"))
  sav2.grid(row = 1, column = 0, sticky = W+E)
  sav3 = SimpleLocationView(top, dbm.get_simple_item("Volatile Crystal"))
  sav3.grid(row = 2, column = 0, sticky = W+E)
  sav4 = SimpleLocationView(top, dbm.get_simple_item("Rock Staff"))
  sav4.grid(row = 3, column = 0, sticky = W+E)

  root.mainloop()
