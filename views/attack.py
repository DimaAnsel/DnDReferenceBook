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
from simple_creature import SimpleCreatureView
from simple_item import SimpleItemView
from tkinter.ttk import Combobox, Separator

################
# Tkinter representation of full attack object, used as separate page.
class AttackView(BaseView):
  
  CHANNEL = "Channel: {}"
  DMG = "Damage: {}"
  QTY = "Qty: {}"

  ########
  # Initializes and places all GUI elements.
  def _create_widgets(self):
    # left frame
    self._leftFrame       = Frame(self)
    self._imgLabel        = Label(self._leftFrame)
    self._creatureLabel   = Label(self._leftFrame,
                               text = "Used by Creature",
                               font = BaseView.NORMAL_FONT)
    self._creatureVar     = StringVar(self)
    self._creatureCombo   = Combobox(self._leftFrame,
                                  state = "readonly",
                                  textvariable = self._creatureVar)
    self._creaturePreview = SimpleCreatureView(self._leftFrame)
    self._leftSep1        = Separator(self._leftFrame, orient = "horizontal")
    self._weaponLabel     = Label(self._leftFrame,
                                  text = "Used by Weapon:",
                                  font = BaseView.NORMAL_FONT)
    self._weaponVar       = StringVar(self)
    self._weaponCombo     = Combobox(self._leftFrame,
                                     state = "readonly",
                                     textvariable = self._weaponVar)
    self._weaponPreview   = SimpleItemView(self._leftFrame)

    # right frame
    self._rightFrame    = Frame(self)
    self._nameLabel     = Label(self._rightFrame,
                                compound = LEFT,
                                text = "Name",
                                font = BaseView.LARGE_FONT)
    utility.update_img(self._nameLabel, BaseView.WAND_IMG[False], maxSize = 30)
    self._rightSep1     = Separator(self._rightFrame, orient = "vertical")
    self._channelLabel  = Label(self._rightFrame,
                                text = AttackView.CHANNEL.format(BaseView.DEFAULT),
                                font = BaseView.BOLD_FONT)
    self._descLabel     = Label(self._rightFrame,
                                text = "Description:",
                                font = BaseView.NORMAL_FONT)
    self._descFrame     = Frame(self._rightFrame)
    self._descText      = Text(self._descFrame,
                               width = 50,
                               height = 4,
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
                               height = 4,
                               state = DISABLED,
                               wrap = WORD,
                               font = BaseView.NORMAL_FONT)
    self._notesScroll   = Scrollbar(self._notesFrame,
                                    command = self._notesText.yview)
    self._notesText.config(yscrollcommand = self._notesScroll.set)
    self._dmgLabel      = Label(self._rightFrame,
                                text = AttackView.DMG.format(BaseView.DEFAULT),
                                font = BaseView.BOLD_FONT)
    self._rightSep2     = Separator(self._rightFrame, orient = "horizontal")
    self._costLabel     = Label(self._rightFrame,
                                text = "Casting Cost:",
                                font = BaseView.NORMAL_FONT)
    self._costVar       = StringVar(self)
    self._costCombo     = Combobox(self._rightFrame,
                                   state = "readonly",
                                   textvariable = self._costVar)
    self._costPreview   = SimpleItemView(self._rightFrame)
    self._costQtyLabel  = Label(self._rightFrame,
                                text = AttackView.QTY.format(BaseView.DEFAULT),
                                font = BaseView.NORMAL_FONT)


    # placement: scrollbars
    self._descText.grid(            row = 0, column = 0, sticky = N+W+E+S)
    self._descScroll.grid(          row = 0, column = 1, sticky = N+S)
    self._notesText.grid(           row = 0, column = 0, sticky = N+W+E+S)
    self._notesScroll.grid(         row = 0, column = 1, sticky = N+S)

    # placement: left frame
    self._imgLabel.grid(        row = 0, column = 0, columnspan = 2, sticky = N+W+E+S)
    self._creatureLabel.grid(   row = 1, column = 0,                 sticky = N+W)
    self._creatureCombo.grid(   row = 1, column = 1,                 sticky = E)
    self._creaturePreview.grid( row = 2, column = 0, columnspan = 2, sticky = W+E)
    self._weaponLabel.grid(     row = 3, column = 0,                 sticky = N+W)
    self._weaponCombo.grid(     row = 3, column = 1,                 sticky = E)
    self._weaponPreview.grid(   row = 4, column = 0, columnspan = 2, sticky = W+E)

    # placement: right frame
    self._nameLabel.grid(     row = 0, column = 0,                 sticky = W)
    self._descLabel.grid(     row = 1, column = 0, columnspan = 3, sticky = W)
    self._descFrame.grid(     row = 2, column = 0, columnspan = 3, sticky = W)
    self._notesLabel.grid(    row = 3, column = 0, columnspan = 3, sticky = W)
    self._notesFrame.grid(    row = 4, column = 0, columnspan = 3, sticky = W)
    self._dmgLabel.grid(      row = 5, column = 0, columnspan = 3, sticky = N+W)
    self._show_spell_fields(False)

    self._leftFrame.grid(    row = 0, column = 0,                 sticky = N+W)
    self._rightFrame.grid(   row = 0, column = 1,                 sticky = N+W)

    # bindings
    self._creatureVar.trace('w', self._preview_creature)
    self._weaponVar.trace('w', self._preview_weapon)
    self._costVar.trace('w', self._preview_cost)

  ########
  # Populates all GUI elements with new data.
  def populate(self, data):
    self._data = data
    if data == None: # null check
      self.set_defaults()
      return
    for k, v in data.items():
      if k == "name":
        # non-null
        self._nameLabel.config(text = v)
      elif k == "img":
        if v == None: # null check
          v = BaseView.DEFAULT_IMG
        utility.update_img(self._imgLabel, v, maxSize = 300)
      elif k == "isSpell":
        # non-null
        utility.update_img(self._nameLabel, BaseView.WAND_IMG[v], maxSize = 30)
        self._show_spell_fields(v)
      elif k == "description":
        if v == None: # null check
          v = BaseView.EMPTY_STR
        utility.update_text(self._descText, v)
      elif k == "notes":
        if v == None: # null check
          v = BaseView.EMPTY_STR
        utility.update_text(self._notesText, v)
      elif k == "dmg":
        if v == None: # null check
          v = BaseView.DEFAULT
        self._dmgLabel.config(text = AttackView.DMG.format(v))
      elif k == "channel":
        if v == None: # null check
          v = BaseView.DEFAULT
        self._channelLabel.config(text = AttackView.CHANNEL.format(v))
      elif k == "creatures":
        # non-null
        utility.update_combobox(self._creatureCombo, [creature["name"] for creature in v])
      elif k == "weapons":
        # non-null
        utility.update_combobox(self._weaponCombo, [item["name"] for item in v])
      elif k == "costs":
        # non-null
        utility.update_combobox(self._costCombo, [cost["item"]["name"] for cost in v])

  ########
  # Reveals GUI elements containing spell fields.
  def _show_spell_fields(self, show = True):
    if show:
      self._rightSep1.grid(     row = 0, column = 1,                 sticky = N+S+E)
      self._channelLabel.grid(  row = 0, column = 2,                 sticky = E)
      self._rightSep2.grid(     row = 6, column = 0, columnspan = 3, sticky = W+E)
      self._costLabel.grid(     row = 7, column = 0,                 sticky = N+W)
      self._costCombo.grid(     row = 7, column = 1, columnspan = 2, sticky = E)
      self._costPreview.grid(   row = 8, column = 0, columnspan = 3, sticky = W+E)
      self._costQtyLabel.grid(  row = 9, column = 0, columnspan = 3, sticky = N+W)
    else:
      self._rightSep1.grid_forget()
      self._channelLabel.grid_forget()
      self._rightSep2.grid_forget()
      self._costLabel.grid_forget()
      self._costCombo.grid_forget()
      self._costPreview.grid_forget()
      self._costQtyLabel.grid_forget()

  ########
  # Resets GUI elements to default values.
  def set_defaults(self):
    utility.update_img(self._imgLabel, BaseView.DEFAULT_IMG, maxSize = 300)
    utility.update_text(self._descText, BaseView.EMPTY_STR)
    utility.update_text(self._notesText, BaseView.EMPTY_STR)
    utility.update_combobox(self._creatureCombo, [])
    utility.update_combobox(self._weaponCombo, [])

  ########
  # Updates creature preview.
  def _preview_creature(self, *args, **kwargs):
    # first reset all
    self._creaturePreview.set_defaults()
    # update with new values
    if self._data == None or self._creatureCombo.current() == -1:
      return
    newCreature = self._data["creatures"][self._creatureCombo.current()]
    if newCreature != None:
      self._creaturePreview.populate(newCreature)

  ########
  # Updates weapon preview.
  def _preview_weapon(self, *args, **kwargs):
    # first reset all
    self._weaponPreview.set_defaults()
    # update with new values
    if self._data == None or self._weaponCombo.current() == -1:
      return
    newWeapon = self._data["weapons"][self._weaponCombo.current()]
    if newWeapon != None:
      self._weaponPreview.populate(newWeapon)

  ########
  # Updates casting cost preview.
  def _preview_cost(self, *args, **kwargs):
    # first reset all
    self._costPreview.set_defaults()
    self._costQtyLabel.config(text = AttackView.QTY.format(BaseView.DEFAULT))
    # update with new values
    if self._data == None or self._costCombo.current() == -1:
      return
    newCost = self._data["costs"][self._costCombo.current()]
    if newCost != None:
      self._costPreview.populate(newCost["item"])
      if newCost["qty"] != None:
        self._costQtyLabel.config(text = AttackView.QTY.format(newCost["qty"]))
# AttackView
################

########
# Test code
if __name__ == "__main__":
  from DnDReferenceBook.src.dbase_manager import DatabaseManager
  from simple_attack import SimpleAttackView
  from tkinter.ttk import Notebook

  root = Tk()

  dbm = DatabaseManager("../data/dnd_ref_book.db")
  # dbm.reset("../src/tables.sql", "../src/real.sql")
  attackList = dbm.get_attack_list()

  nb = Notebook(root)
  av = AttackView(nb)
  nb.add(av, text = "Default")
  for attack in attackList:
    temp = AttackView(nb, dbm.get_attack(attack["id"]))
    nb.add(temp, text = attack["name"])
  nb.grid(row = 0, column = 0)

  top = Toplevel(root)
  sav = SimpleAttackView(top)
  sav.grid(row = 0, column = 0, sticky = W+E)
  for i in range(len(attackList)):
    temp = SimpleAttackView(top, dbm.get_simple_attack(i))
    temp.grid(row = i + 1, column = 0, sticky = W+E)

  root.mainloop()
