################################
# creature.py
# Noah Ansel
# 2017-09-26
# ------------------------------
# Tkinter view for the Creature object as presented by the DatabaseManager.
################################

from tkinter import *
from tkinter.ttk import Separator, Combobox
from base_view import BaseView
from item import SimpleItemView
from attack import SimpleAttackView
from location import SimpleLocationView
import utility

################
# Tkinter representation of full creature object, used as separate page.
class CreatureView(BaseView):

  XP_FMT = "XP: {}"
  HD_FMT = "HD: {}"
  AC_FMT = "AC: {}"
  HP_FMT = "HP: {}"
  EQUIP_CHANCE = "Eqiup Chance: {}"
  DROP_CHANCE = "Drop Chance: {}"
  BASIC_ATTACK = "Basic Attack: {}"

  def _create_widgets(self):
    # left frame
    self._leftFrame    = Frame(self)
    self._imgLabel     = Label(self._leftFrame)
    self._equipLabel   = Label(self._leftFrame,
                               text = "Equipment",
                               font = BaseView.NORMAL_FONT)
    self._equipVar     = StringVar(self)
    self._equipCombo   = Combobox(self._leftFrame,
                                  state = "readonly",
                                  textvariable = self._equipVar)
    self._equipPreview = SimpleItemView(self._leftFrame)
    self._equipChance  = Label(self._leftFrame,
                               text = CreatureView.EQUIP_CHANCE.format(BaseView.DEFAULT),
                               font = BaseView.NORMAL_FONT)
    self._equipNotesLabel = Label(self._leftFrame,
                                  text = "Notes:",
                                  font = BaseView.NORMAL_FONT)
    self._equipNotesFrame = Frame(self._leftFrame)
    self._equipNotes   = Text(self._equipNotesFrame,
                              width = 30,
                              height = 2,
                              state = DISABLED,
                              wrap = WORD,
                              font = BaseView.NORMAL_FONT)
    self._equipNotesScroll  = Scrollbar(self._equipNotesFrame,
                                        command = self._equipNotes.yview)
    self._equipNotes.config(yscrollcommand = self._equipNotesScroll.set)
    self._leftSep1     = Separator(self._leftFrame, orient = "horizontal")
    self._dropLabel    = Label(self._leftFrame,
                            text = "Extra Drops:",
                            font = BaseView.NORMAL_FONT)
    self._dropVar      = StringVar(self)
    self._dropCombo    = Combobox(self._leftFrame,
                                  state = "readonly",
                                  textvariable = self._equipVar)
    self._dropPreview  = SimpleItemView(self._leftFrame)
    self._dropChance   = Label(self._leftFrame,
                               text = CreatureView.DROP_CHANCE.format(BaseView.DEFAULT),
                               font = BaseView.NORMAL_FONT)
    self._dropNotesFrame = Frame(self._leftFrame)
    self._dropNotesLabel = Label(self._leftFrame,
                                 text = "Notes:",
                                 font = BaseView.NORMAL_FONT)
    self._dropNotes    = Text(self._dropNotesFrame,
                              width = 30,
                              height = 2,
                              state = DISABLED,
                              wrap = WORD,
                              font = BaseView.NORMAL_FONT)
    self._dropNotesScroll  = Scrollbar(self._dropNotesFrame,
                                       command = self._dropNotes.yview)
    self._dropNotes.config(yscrollcommand = self._dropNotesScroll.set)

    # right frame
    self._rightFrame    = Frame(self)
    self._nameLabel     = Label(self._rightFrame,
                                compound = LEFT,
                                text = "Name",
                                font = BaseView.LARGE_FONT)
    self._rightSep1     = Separator(self._rightFrame, orient = "vertical")
    self._xpLabel       = Label(self._rightFrame,
                                text = CreatureView.XP_FMT.format(BaseView.DEFAULT),
                                font = BaseView.BOLD_FONT)
    self._descLabel     = Label(self._rightFrame,
                                text = "Description:",
                                font = BaseView.NORMAL_FONT)
    self._descFrame     = Frame(self._rightFrame)
    self._descText      = Text(self._descFrame,
                               width = 50,
                               height = 5,
                               state = DISABLED,
                               wrap = WORD,
                               font = BaseView.NORMAL_FONT)
    self._descScroll    = Scrollbar(self._descFrame,
                                    command = self._descText.yview)
    self._descText.config(yscrollcommand = self._descScroll.set)
    self._notesLabel    = Label(self._rightFrame,
                                text = "Notes:",
                                font = BaseView.NORMAL_FONT)
    self._notesFrame    = Frame(self._rightFrame)
    self._notesText     = Text(self._notesFrame,
                               width = 50,
                               height = 5,
                               state = DISABLED,
                               wrap = WORD,
                               font = BaseView.NORMAL_FONT)
    self._notesScroll   = Scrollbar(self._notesFrame,
                                    command = self._notesText.yview)
    self._notesText.config(yscrollcommand = self._notesScroll.set)
    self._basicAttack   = Label(self._rightFrame,
                                text = CreatureView.BASIC_ATTACK.format(BaseView.DEFAULT),
                                font = BaseView.NORMAL_FONT)
    self._hdLabel       = Label(self._rightFrame,
                                text = CreatureView.HD_FMT.format(BaseView.DEFAULT),
                                font = BaseView.BOLD_FONT)
    self._rightSep2     = Separator(self._rightFrame, orient = "vertical")
    self._acLabel       = Label(self._rightFrame,
                                text = CreatureView.AC_FMT.format(BaseView.DEFAULT),
                                font = BaseView.BOLD_FONT)
    self._rightSep3     = Separator(self._rightFrame, orient = "vertical")
    self._hpLabel       = Label(self._rightFrame,
                                text = CreatureView.HP_FMT.format(BaseView.DEFAULT),
                                font = BaseView.BOLD_FONT)
    self._rightSep4     = Separator(self._rightFrame, orient = "horizontal")
    self._rightBotFrame = Frame(self._rightFrame)
    self._attacksLabel  = Label(self._rightBotFrame,
                                text = "Special Attacks:",
                                font = BaseView.NORMAL_FONT)
    self._attacksVal    = StringVar(self)
    self._attacksCombo  = Combobox(self._rightBotFrame,
                                   state = "readonly",
                                   textvariable = self._attacksVal)
    self._attackPreview = SimpleAttackView(self._rightBotFrame)
    self._rightSep5     = Separator(self._rightBotFrame, orient = "horizontal")
    self._inhabitsLabel = Label(self._rightBotFrame,
                                text = "Inhabits:",
                                font = BaseView.NORMAL_FONT)
    self._inhabitsVal   = StringVar(self)
    self._inhabitsCombo = Combobox(self._rightBotFrame,
                                   state = "readonly",
                                   textvariable = self._inhabitsVal)
    self._inhabitsPreview    = SimpleLocationView(self._rightBotFrame)
    self._inhabitsNotesLabel = Label(self._rightBotFrame,
                                     text = "Notes:",
                                     font = BaseView.NORMAL_FONT)
    self._inhabitsNotesFrame = Frame(self._rightBotFrame)
    self._inhabitsNotes      = Text(self._inhabitsNotesFrame,
                                    width = 50,
                                    height = 3,
                                    state = DISABLED,
                                    wrap = WORD,
                                    font = BaseView.NORMAL_FONT)
    self._inhabitsNotesScroll = Scrollbar(self._inhabitsNotesFrame,
                                          command = self._inhabitsNotes.yview)
    self._inhabitsNotes.config(yscrollcommand = self._inhabitsNotesScroll.set)

    # placement: scrollbars
    self._equipNotes.grid(          row = 0, column = 0, sticky = N+W+E+S)
    self._equipNotesScroll.grid(    row = 0, column = 1, sticky = N+S)
    self._dropNotes.grid(           row = 0, column = 0, sticky = N+W+E+S)
    self._dropNotesScroll.grid(     row = 0, column = 1, sticky = N+S)
    self._descText.grid(            row = 0, column = 0, sticky = N+W+E+S)
    self._descScroll.grid(          row = 0, column = 1, sticky = N+S)
    self._notesText.grid(           row = 0, column = 0, sticky = N+W+E+S)
    self._notesScroll.grid(         row = 0, column = 1, sticky = N+S)
    self._inhabitsNotes.grid(       row = 0, column = 0, sticky = N+W+E+S)
    self._inhabitsNotesScroll.grid( row = 0, column = 1, sticky = N+S)

    # placement: left frame
    self._imgLabel.grid(        row =  0, column = 0, columnspan = 2, sticky = N+W+E+S)
    self._equipLabel.grid(      row =  1, column = 0,                 sticky = N+W)
    self._equipCombo.grid(      row =  1, column = 1,                 sticky = E)
    self._equipPreview.grid(    row =  2, column = 0, columnspan = 2, sticky = W+E)
    self._equipChance.grid(     row =  3, column = 0, columnspan = 2, sticky = N+W)
    self._equipNotesLabel.grid( row =  4, column = 0, columnspan = 2, sticky = N+W)
    self._equipNotesFrame.grid( row =  5, column = 0, columnspan = 2, sticky = N+W+E)
    self._leftSep1.grid(        row =  6, column = 0, columnspan = 2, sticky = W+E)
    self._dropLabel.grid(       row =  7, column = 0,                 sticky = N+W)
    self._dropCombo.grid(       row =  7, column = 1,                 sticky = E)
    self._dropPreview.grid(     row =  8, column = 0, columnspan = 2, sticky = W+E)
    self._dropChance.grid(      row =  9, column = 0, columnspan = 2, sticky = N+W)
    self._dropNotesLabel.grid(  row = 10, column = 0, columnspan = 2, sticky = N+W)
    self._dropNotesFrame.grid(  row = 11, column = 0, columnspan = 2, sticky = N+W+E)

    # placement: right frame
    self._nameLabel.grid(     row = 0, column = 0, columnspan = 3, sticky = W)
    self._rightSep1.grid(     row = 0, column = 3,                 sticky = N+E+S)
    self._xpLabel.grid(       row = 0, column = 4,                 sticky = E)
    self._descLabel.grid(     row = 1, column = 0, columnspan = 5, sticky = W)
    self._descFrame.grid(     row = 2, column = 0, columnspan = 5, sticky = W)
    self._notesLabel.grid(    row = 3, column = 0, columnspan = 5, sticky = W)
    self._notesFrame.grid(    row = 4, column = 0, columnspan = 5, sticky = W)
    self._hdLabel.grid(       row = 5, column = 0,                 sticky = W)
    self._rightSep2.grid(     row = 5, column = 1,                 sticky = N+E+S)
    self._acLabel.grid(       row = 5, column = 2,                 sticky = W+E)
    self._rightSep3.grid(     row = 5, column = 3,                 sticky = N+E+S)
    self._hpLabel.grid(       row = 5, column = 4,                 sticky = E)
    self._basicAttack.grid(   row = 6, column = 0, columnspan = 5, sticky = N+W)
    self._rightSep4.grid(     row = 7, column = 0, columnspan = 5, sticky = W+E)
    self._rightBotFrame.grid( row = 8, column = 0, columnspan = 5, sticky = N+W+E)
    
    # placement: bottom right frame
    self._attacksLabel.grid(      row = 0, column = 0,                 sticky = N+W)
    self._attacksCombo.grid(      row = 0, column = 1,                 sticky = E)
    self._attackPreview.grid(     row = 1, column = 0, columnspan = 2, sticky = W+E)
    self._rightSep5.grid(         row = 2, column = 0, columnspan = 2, sticky = W+E)
    self._inhabitsLabel.grid(     row = 3, column = 0,                 sticky = N+W)
    self._inhabitsCombo.grid(     row = 3, column = 1,                 sticky = E)
    self._inhabitsPreview.grid(   row = 4, column = 0, columnspan = 2, sticky = W+E)
    self._inhabitsNotesLabel.grid(row = 5, column = 0, columnspan = 2, sticky = N+W)
    self._inhabitsNotesFrame.grid(row = 6, column = 0, columnspan = 2, sticky = N+W+E)

    self._leftFrame.grid(    row = 0, column = 0,                 sticky = N+W)
    self._rightFrame.grid(   row = 0, column = 1,                 sticky = N+W)

  def populate(self, creature):
    for k, v in creature.items():
      if k == "img":
        if v == None: # null check
          v = BaseView.DEFAULT_IMG
        utility.update_img(self._imgLabel, v, maxSize = 300)
      elif k == "rarity":
        # null accepted
        utility.update_img(self._nameLabel, BaseView.RARITY_IMG[v], maxSize = 30) 
      elif k == "name":
        # non-null
        self._nameLabel.config(text = v)
      elif k == "description":
        if v == None: # null check
          v = ""
        utility.update_text(self._descText, v)
      elif k == "notes":
        if v == None: # null check
          v = ""
        utility.update_text(self._notesText, v)
      elif k == "hd":
        if v == None: # null check
          v = BaseView.DEFAULT
        self._hdLabel.config(text = CreatureView.HD_FMT.format(v))
      elif k == "hp":
        if v == None: # null check
          v = BaseView.DEFAULT
        self._hpLabel.config(text = CreatureView.HP_FMT.format(v))
      elif k == "ac":
        if v == None: # null check
          v = BaseView.DEFAULT
        self._acLabel.config(text = CreatureView.AC_FMT.format(v))
      elif k == "xp":
        if v == None: # null check
          v = BaseView.DEFAULT
        self._xpLabel.config(text = CreatureView.XP_FMT.format(v))
      elif k == "basicAttack":
        if v == None: # null check
          v = BaseView.DEFAULT
        self._basicAttack.config(text = CreatureView.BASIC_ATTACK.format(v))
      # TODO: handle other cases
      elif k == "equips":
        pass
      elif k == "drops":
        pass
      elif k == "attacks":
        pass
      elif k == "inhabits":
        pass

  def set_defaults(self):
    utility.update_img(self._imgLabel, BaseView.DEFAULT_IMG, maxSize = 300)
    utility.update_img(self._nameLabel, BaseView.RARITY_IMG[None], maxSize = 30)
    utility.update_text(self._descText, BaseView.DEFAULT)
    utility.update_text(self._notesText, BaseView.DEFAULT)
# CreatureView
################

################
# Tkinter representation of simple creature object, used for previews.
class SimpleCreatureView(BaseView):

  NAME_FORMAT = "{} ({})"

  def _create_widgets(self):
    self._imgLabel = Label(self)
    self._nameLabel = Label(self, text = SimpleCreatureView.NAME_FORMAT.format("Name", BaseView.DEFAULT))

    self._imgLabel.grid(  row = 0, column = 0, sticky = N+W+E+S)
    self._nameLabel.grid( row = 0, column = 1, sticky = W)

  def populate(self, data):
    name = ""
    hd = BaseView.DEFAULT
    for k, v in data.items():
      if k == "name":
        name = v
      elif k == "img":
        if v == None:
          v = BaseView.DEFAULT_IMG
        utility.update_img(self._imgLabel, v, maxSize = 30)
      elif k == "hd":
        if v != None:
          hd = v
    self._nameLabel.config(text = SimpleCreatureView.NAME_FORMAT.format(name, hd))

  def set_defaults(self):
    utility.update_img(self._imgLabel, BaseView.DEFAULT_IMG, maxSize = 30)
    self._nameLabel.config(text = SimpleCreatureView.NAME_FORMAT.format("Name", BaseView.DEFAULT))
# SimpleCreatureView
################

########
# Test code
if __name__ == "__main__":
  from DnDReferenceBook.src.dbase_manager import DatabaseManager
  from tkinter.ttk import Notebook

  root = Tk()

  dbm = DatabaseManager("../data/dnd_ref_book.db", "../data/img/")
  dbm.reset("../src/tables.sql", "../src/real.sql")
  nb = Notebook(root)
  cv = CreatureView(nb)
  nb.add(cv, text = "Default")
  cv2 = CreatureView(nb, dbm.get_creature("Flame Wisp"))
  nb.add(cv2, text = "Flame Wisp")
  cv3 = CreatureView(nb, dbm.get_creature("Apprentice Rock Elementalist"))
  nb.add(cv3, text = "Apprentice Rock Elementalist")
  cv4 = CreatureView(nb, dbm.get_creature("Crystalline Serpent"))
  nb.add(cv4, text = "Crystalline Serpent")
  cv5 = CreatureView(nb, dbm.get_creature("Rock Elemental"))
  nb.add(cv5, text = "Rock Elemental")
  nb.grid(row = 0, column = 0)

  top = Toplevel(root)
  scv = SimpleCreatureView(top)
  scv.grid(row = 0, column = 0, sticky = W+E)
  scv2 = SimpleCreatureView(top, dbm.get_creature("Flame Wisp"))
  scv2.grid(row = 1, column = 0, sticky = W+E)
  scv3 = SimpleCreatureView(top, dbm.get_creature("Apprentice Rock Elementalist"))
  scv3.grid(row = 2, column = 0, sticky = W+E)
  scv4 = SimpleCreatureView(top, dbm.get_creature("Crystalline Serpent"))
  scv4.grid(row = 3, column = 0, sticky = W+E)
  scv5 = SimpleCreatureView(top, dbm.get_creature("Rock Elemental"))
  scv5.grid(row = 4, column = 0, sticky = W+E)

  root.mainloop()
