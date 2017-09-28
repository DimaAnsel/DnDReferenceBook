################################
# creature.py
# Noah Ansel
# 2017-09-26
# ------------------------------
# Tkinter view for the Creature object as presented by the DatabaseManager.
################################

from tkinter import *
import utility

class CreatureView(Frame):

  XP_FMT = "XP: {}"
  HD_FMT = "HD: {}"
  AC_FMT = "AC: {}"
  HP_FMT = "HP: {}"

  DEFAULT = "??"

  def __init__(self, master, data = None):
    super().__init__(master)
    self._create_widgets()
    if data != None:
      self.populate(data)
    else:
      self.set_defaults()

  def _create_widgets(self):
    self._imgLabel     = Label(self)

    self._infoFrame    = Frame(self)
    self._nameLabel    = Label(self._infoFrame, text = "Name")
    self._xpLabel      = Label(self._infoFrame, text = CreatureView.XP_FMT.format(CreatureView.DEFAULT))
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
    self._hdLabel      = Label(self._infoFrame, text = CreatureView.HD_FMT.format(CreatureView.DEFAULT))
    self._acLabel      = Label(self._infoFrame, text = CreatureView.AC_FMT.format(CreatureView.DEFAULT))
    self._hpLabel      = Label(self._infoFrame, text = CreatureView.HP_FMT.format(CreatureView.DEFAULT))
    self._attacksLabel = Label(self._infoFrame, text = "Attacks:")
    self._attacksText  = Label(self._infoFrame, text = CreatureView.DEFAULT)
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


    self._imgLabel.grid(row = 0, column = 0, sticky = N+W+E+S)

    self._nameLabel.grid(   row = 0, column = 0, columnspan = 2, sticky = W)
    self._xpLabel.grid(     row = 0, column = 2,                 sticky = E)
    self._descLabel.grid(   row = 1, column = 0, columnspan = 3, sticky = W)
    self._descText.grid(    row = 0, column = 0,                 sticky = N+W+E+S)
    self._descScroll.grid(  row = 0, column = 1,                 sticky = N+S)
    self._descFrame.grid(   row = 2, column = 0, columnspan = 3, sticky = W)
    self._hdLabel.grid(     row = 3, column = 0,                 sticky = W)
    self._acLabel.grid(     row = 3, column = 1,                 sticky = W+E)
    self._hpLabel.grid(     row = 3, column = 2,                 sticky = E)
    self._attacksLabel.grid(row = 4, column = 0, columnspan = 3, sticky = W)
    self._attacksText.grid( row = 5, column = 0, columnspan = 3, sticky = W)
    self._notesLabel.grid(  row = 6, column = 0, columnspan = 3, sticky = W)
    self._notesText.grid(   row = 0, column = 0,                 sticky = N+W+E+S)
    self._notesScroll.grid( row = 0, column = 1,                 sticky = N+S)
    self._notesFrame.grid(  row = 7, column = 0, columnspan = 3, sticky = W)
    self._infoFrame.grid(   row = 0, column = 1,                 sticky = N+S)

  def populate(self, creature):
    for k, v in creature.items():
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
      elif k == "hd":
        self._hdLabel.config(text = CreatureView.HD_FMT.format(v))
      elif k == "hp":
        self._hpLabel.config(text = CreatureView.HP_FMT.format(v))
      elif k == "ac":
        self._acLabel.config(text = CreatureView.AC_FMT.format(v))
      elif k == "xp":
        self._xpLabel.config(text = CreatureView.XP_FMT.format(v))
      # TODO: handle other cases

  def set_defaults(self):
    utility.update_text(self._descText, CreatureView.DEFAULT)
    utility.update_text(self._notesText, CreatureView.DEFAULT)


if __name__ == "__main__":
  from DnDReferenceBook.src.dbase_manager import DatabaseManager

  root = Tk()

  dbm = DatabaseManager("../data/dnd_ref_book.db")
  cv = CreatureView(root)
  cv.grid(row = 0, column = 0, sticky = N+W)
  cv2 = CreatureView(root, dbm.get_creature("Flame Wisp"))
  cv2.grid(row = 0, column = 1, sticky = N+W)
  cv3 = CreatureView(root, dbm.get_creature("Apprentice Rock Elementalist"))
  cv3.grid(row = 1, column = 0, sticky = N+W)
  cv4 = CreatureView(root, dbm.get_creature("Crystalline Serpent"))
  cv4.grid(row = 1, column = 1, sticky = N+W)

  root.mainloop()
