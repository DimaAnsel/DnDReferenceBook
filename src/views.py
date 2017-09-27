from tkinter import *

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

  def _create_widgets(self):
    self._imgLabel     = Label(self)

    self._infoFrame    = Frame(self)
    self._nameLabel    = Label(self._infoFrame, text = "Name")
    self._xpLabel      = Label(self._infoFrame, text = CreatureView.XP_FMT.format(CreatureView.DEFAULT))
    self._descLabel    = Label(self._infoFrame, text = "Description:")
    self._descValue    = Label(self._infoFrame, text = CreatureView.DEFAULT)
    self._hdLabel      = Label(self._infoFrame, text = CreatureView.HD_FMT.format(CreatureView.DEFAULT))
    self._acLabel      = Label(self._infoFrame, text = CreatureView.AC_FMT.format(CreatureView.DEFAULT))
    self._hpLabel      = Label(self._infoFrame, text = CreatureView.HP_FMT.format(CreatureView.DEFAULT))
    self._attacksLabel = Label(self._infoFrame, text = "Attacks:")
    self._attacksValue = Label(self._infoFrame, text = CreatureView.DEFAULT)
    self._notesLabel   = Label(self._infoFrame, text = "Notes:")
    self._notesValue   = Label(self._infoFrame, text = CreatureView.DEFAULT)


    self._imgLabel.grid(row = 0, column = 0, sticky = N+W+E+S)

    self._nameLabel.grid(   row = 0, column = 0, columnspan = 2, sticky = W)
    self._xpLabel.grid(     row = 0, column = 2,                 sticky = E)
    self._descLabel.grid(   row = 1, column = 0, columnspan = 3, sticky = W)
    self._descValue.grid(   row = 2, column = 0, columnspan = 3, sticky = W)
    self._hdLabel.grid(     row = 3, column = 0,                 sticky = W)
    self._acLabel.grid(     row = 3, column = 1,                 sticky = W+E)
    self._hpLabel.grid(     row = 3, column = 2,                 sticky = E)
    self._attacksLabel.grid(row = 4, column = 0, columnspan = 3, sticky = W)
    self._attacksValue.grid(row = 5, column = 0, columnspan = 3, sticky = W)
    self._notesLabel.grid(  row = 6, column = 0, columnspan = 3, sticky = W)
    self._notesValue.grid(  row = 7, column = 0, columnspan = 3, sticky = W)
    self._infoFrame.grid(   row = 0, column = 1, sticky = N+S)


  def populate(self, creature):
    # #TODO: use SQL -> JSON converter
    # self._nameLabel.config(text = creature[0])
    # self._descValue.config(text = creature[1])
    # self._notesValue.config(text = creature[2])
    # #TODO: img & rarity
    # self._hdLabel.config(text = CreatureView.HD_FMT.format(creature[5]))
    # self._hpLabel.config(text = CreatureView.HP_FMT.format(creature[6]))
    # self._acLabel.config(text = CreatureView.AC_FMT.format(creature[7]))
    # self._xpLabel.config(text = CreatureView.XP_FMT.format(creature[8]))

    for k, v in creature.items():
      if k == "name":
        self._nameLabel.config(text = v)
      elif k == "description":
        self._descValue.config(text = v)
      elif k == "notes":
        self._notesValue.config(text = v)
      elif k == "hd":
        self._hdLabel.config(text = CreatureView.HD_FMT.format(v))
      elif k == "hp":
        self._hpLabel.config(text = CreatureView.HP_FMT.format(v))
      elif k == "ac":
        self._acLabel.config(text = CreatureView.AC_FMT.format(v))
      elif k == "xp":
        self._xpLabel.config(text = CreatureView.XP_FMT.format(v))
      # TODO: handle other cases