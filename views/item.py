################################
# item.py
# Noah Ansel
# 2017-10-16
# ------------------------------
# Tkinter view for the Item object as presented by the DatabaseManager.
################################

from tkinter import *
from base_view import BaseView
import utility

################
# Tkinter representation of full item object, used as separate page.
class ItemView(BaseView):

  def _create_widgets(self):
    self._imgLabel     = Label(self)

    self._infoFrame    = Frame(self)
    self._nameLabel    = Label(self._infoFrame, text = "Name")
    self._valLabel      = Label(self._infoFrame, compound = LEFT, text = BaseView.DEFAULT)
    utility.update_img(self._valLabel, BaseView.VALUE_IMG, 30)
    self._descLabel    = Label(self._infoFrame, text = "Description:")
    self._descFrame    = Frame(self._infoFrame)
    self._descText     = Text(self._descFrame,
                              width = 50,
                              height = 5,
                              state = DISABLED,
                              wrap = WORD,
                              font = ("Calibri", 10))
    self._descScroll   = Scrollbar(self._descFrame,
                                   command = self._descText.yview)
    self._descText.config(yscrollcommand = self._descScroll.set)
    self._attacksLabel = Label(self._infoFrame, text = "Attacks:")
    self._attacksText  = Label(self._infoFrame, text = BaseView.DEFAULT)
    self._notesLabel   = Label(self._infoFrame, text = "Notes:")
    self._notesFrame   = Frame(self._infoFrame)
    self._notesText    = Text(self._notesFrame,
                              width = 50,
                              height = 5,
                              state = DISABLED,
                              wrap = WORD,
                              font = ("Calibri", 10))
    self._notesScroll  = Scrollbar(self._notesFrame,
                                   command = self._notesText.yview)
    self._notesText.config(yscrollcommand = self._notesScroll.set)


    self._imgLabel.grid(    row = 0, column = 0,                 sticky = N+W+E+S)

    self._nameLabel.grid(   row = 0, column = 0, columnspan = 2, sticky = W)
    self._valLabel.grid(    row = 0, column = 2,                 sticky = E)
    self._descLabel.grid(   row = 1, column = 0, columnspan = 3, sticky = W)
    self._descText.grid(    row = 0, column = 0,                 sticky = N+W+E+S)
    self._descScroll.grid(  row = 0, column = 1,                 sticky = N+S)
    self._descFrame.grid(   row = 2, column = 0, columnspan = 3, sticky = W)
    if self._omniscient:
      self._attacksLabel.grid(row = 4, column = 0, columnspan = 3, sticky = W)
      self._attacksText.grid( row = 5, column = 0, columnspan = 3, sticky = W)
      self._notesLabel.grid(  row = 6, column = 0, columnspan = 3, sticky = W)
      self._notesText.grid(   row = 0, column = 0,                 sticky = N+W+E+S)
      self._notesScroll.grid( row = 0, column = 1,                 sticky = N+S)
      self._notesFrame.grid(  row = 7, column = 0, columnspan = 3, sticky = W)
    self._infoFrame.grid(   row = 0, column = 1,                 sticky = N+S)

  def populate(self, creature):
    for k, v in creature.items():
      if k == "img":
        if v == None:
          v = BaseView.DEFAULT_IMG
        utility.update_img(self._imgLabel, v, maxSize = 300)
      if k == "name":
        self._nameLabel.config(text = v)
      elif k == "description":
        if v == None:
          v = ""
        utility.update_text(self._descText, v)
      elif k == "notes":
        if v == None:
          v = ""
        utility.update_text(self._notesText, v)
      # elif k == "hd":
      #   if v == None:
      #     v = BaseView.DEFAULT
      #   self._hdLabel.config(text = CreatureView.HD_FMT.format(v))
      # elif k == "hp":
      #   if v == None:
      #     v = BaseView.DEFAULT
      #   self._hpLabel.config(text = CreatureView.HP_FMT.format(v))
      # elif k == "ac":
      #   if v == None:
      #     v = BaseView.DEFAULT
      #   self._acLabel.config(text = CreatureView.AC_FMT.format(v))
      # elif k == "xp":
      #   if v == None:
      #     v = BaseView.DEFAULT
      #   self._xpLabel.config(text = CreatureView.XP_FMT.format(v))
      # TODO: handle other cases

  def set_defaults(self):
    utility.update_img(self._imgLabel, BaseView.DEFAULT_IMG, maxSize = 300)
    utility.update_text(self._descText, BaseView.DEFAULT)
    utility.update_text(self._notesText, BaseView.DEFAULT)
# ItemView
################

################
# Tkinter representation of simple item object, used for previews.
class SimpleItemView(BaseView):

  NAME_FORMAT = "{} ({})"

  def _create_widgets(self):
    self._imgLabel = Label(self)
    self._nameLabel = Label(self, text = SimpleItemView.NAME_FORMAT.format("Name", BaseView.DEFAULT))
    self._valueLabel = Label(self, compound = LEFT)
    utility.update_img(self._valueLabel, BaseView.VALUE_IMG, maxSize = 30)

    self._imgLabel.grid(  row = 0, column = 0, sticky = N+W+E+S)
    self._nameLabel.grid( row = 0, column = 1, sticky = W)
    if self._omniscient:
      self._valueLabel.grid(row = 0, column = 2, sticky = W)

  def populate(self, data):
    name = ""
    itemType = 0
    for k, v in data.items():
      if k == "name":
        name = v
      elif k == "img":
        if v == None:
          v = BaseView.DEFAULT_IMG
        utility.update_img(self._imgLabel, v, maxSize = 30)
      elif k == "type":
        if v != None:
          itemType = v
      elif k == "value":
        if v == None:
          v = BaseView.DEFAULT
        self._valueLabel.config(text = v)
    self._nameLabel.config(text = SimpleItemView.NAME_FORMAT.format(name, BaseView.TYPE_MAP[itemType]))


  def set_defaults(self):
    utility.update_img(self._imgLabel, BaseView.DEFAULT_IMG, maxSize = 30)
    self._nameLabel.config(text = SimpleItemView.NAME_FORMAT.format("Name", BaseView.DEFAULT))
    self._valueLabel.config(text = BaseView.DEFAULT)
# SimpleItemView
################

########
# Test code
if __name__ == "__main__":
  from DnDReferenceBook.src.dbase_manager import DatabaseManager

  root = Tk()

  dbm = DatabaseManager("../data/dnd_ref_book.db", "../data/img/")
  dbm.reset("../src/tables.sql", "../src/real.sql")
  av = ItemView(root)
  av.grid(row = 0, column = 0, sticky = N+S+W+E)
  av2 = ItemView(root, dbm.get_item("Animating Crystal"))
  av2.grid(row = 0, column = 1, sticky = N+S+W+E)
  av3 = ItemView(root, dbm.get_item("Volatile Crystal"))
  av3.grid(row = 1, column = 0, sticky = N+S+W+E)
  av4 = ItemView(root, dbm.get_item("Rock Staff"))
  av4.grid(row = 1, column = 1, sticky = N+S+W+E)

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
