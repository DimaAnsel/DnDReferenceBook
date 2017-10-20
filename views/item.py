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
from simple_creature import SimpleCreatureView
from simple_item import SimpleItemView
from simple_store import SimpleStoreView
from simple_attack import SimpleAttackView
from tkinter.ttk import Combobox, Separator

################
# Tkinter representation of full item object, used as separate page.
class ItemView(BaseView):

  EQUIP_CHANCE = "Equip Chance:"
  DROP_CHANCE = "Drop Chance:"

  PRICE = "Price: {}"
  QTY = "Qty: {}"
  STOCK_DAYS = "Stock Days: {}"
  SLOT = "Slot: {}"
  DMG = "Dmg: {}"
  RANGE = "Range: {}"
  CRIT = "Crit: {}"
  AC = "AC: {}"
  PRICE = "Price: {}"
  STOCK_DAYS = "Stock Days: {}"

  ########
  # Initializes and places all GUI elements.
  def _create_widgets(self):
    # left frame
    self._leftFrame    = Frame(self)
    self._imgLabel     = Label(self._leftFrame)
    self._equipLabel   = Label(self._leftFrame,
                               text = "Equipped by",
                               font = BaseView.NORMAL_FONT)
    self._equipVar     = StringVar(self)
    self._equipCombo   = Combobox(self._leftFrame,
                                  state = "readonly",
                                  textvariable = self._equipVar)
    self._equipPreview = SimpleCreatureView(self._leftFrame)
    self._equipChance  = Label(self._leftFrame,
                               text = ItemView.EQUIP_CHANCE.format(BaseView.DEFAULT),
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
                            text = "Dropped by:",
                            font = BaseView.NORMAL_FONT)
    self._dropVar      = StringVar(self)
    self._dropCombo    = Combobox(self._leftFrame,
                                  state = "readonly",
                                  textvariable = self._dropVar)
    self._dropPreview  = SimpleCreatureView(self._leftFrame)
    self._dropChance   = Label(self._leftFrame,
                               text = ItemView.DROP_CHANCE.format(BaseView.DEFAULT),
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
    self._leftSep2      = Separator(self._leftFrame, orient = "horizontal")
    self._ammoLabel     = Label(self._leftFrame,
                                text = "Ammo for:",
                                font = BaseView.NORMAL_FONT)
    self._ammoVar       = StringVar(self)
    self._ammoCombo     = Combobox(self._leftFrame,
                                   state = "readonly",
                                   textvariable = self._ammoVar)
    self._ammoPreview   = SimpleItemView(self._leftFrame)

    # right frame
    self._rightFrame    = Frame(self)
    self._nameLabel     = Label(self._rightFrame,
                                compound = LEFT,
                                text = "Name",
                                font = BaseView.LARGE_FONT)
    self._rightSep1     = Separator(self._rightFrame, orient = "vertical")
    self._valLabel      = Label(self._rightFrame,
                                compound = LEFT,
                                text = BaseView.DEFAULT,
                                font = BaseView.BOLD_FONT)
    utility.update_img(self._valLabel, BaseView.VALUE_IMG, maxSize = 30)
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
    self._rightSep2     = Separator(self._rightFrame, orient = "horizontal")
    self._soldAtLabel   = Label(self._rightFrame,
                                text = "Sold at:",
                                font = BaseView.NORMAL_FONT)
    self._soldAtVar     = StringVar(self)
    self._soldAtCombo   = Combobox(self._rightFrame,
                                   state = "readonly",
                                   textvariable = self._soldAtVar)
    self._soldAtPreview = SimpleStoreView(self._rightFrame)
    self._soldAtPrice   = Label(self._rightFrame,
                                text = ItemView.PRICE.format(BaseView.DEFAULT),
                                font = BaseView.NORMAL_FONT)
    self._rightSep3     = Separator(self._rightFrame, orient = "vertical")
    self._soldAtQty     = Label(self._rightFrame,
                                text = ItemView.QTY.format(BaseView.DEFAULT),
                                font = BaseView.NORMAL_FONT)
    self._rightSep4     = Separator(self._rightFrame, orient = "vertical")
    self._stockDays     = Label(self._rightFrame,
                                text = ItemView.STOCK_DAYS.format(BaseView.DEFAULT),
                                font = BaseView.NORMAL_FONT)
    self._rightSep5     = Separator(self._rightFrame, orient = "horizontal")
    self._spellLabel    = Label(self._rightFrame,
                                text = "Used in Spell:")
    self._spellVar      = StringVar(self)
    self._spellCombo    = Combobox(self._rightFrame,
                                   state = "readonly",
                                   textvariable = self._spellVar)
    self._spellPreview  = SimpleAttackView(self._rightFrame)
    self._spellQty      = Label(self._rightFrame,
                                text = ItemView.QTY.format(BaseView.DEFAULT),
                                font = BaseView.NORMAL_FONT)

    # weapon frame
    self._weaponFrame       = Frame(self._rightFrame)
    self._weaponSlot        = Label(self._weaponFrame,
                                    text = ItemView.SLOT.format(BaseView.DEFAULT),
                                    font = BaseView.NORMAL_FONT)
    self._weaponRange       = Label(self._weaponFrame,
                                    text = ItemView.RANGE.format(BaseView.DEFAULT),
                                    font = BaseView.NORMAL_FONT)
    self._weaponAmmoLabel   = Label(self._weaponFrame,
                                    text = "Ammo:",
                                    font = BaseView.NORMAL_FONT)
    self._weaponAmmoPreview = SimpleItemView(self._weaponFrame)
    self._weaponSep1        = Separator(self._weaponFrame, orient = "vertical")
    self._weaponDmg         = Label(self._weaponFrame,
                                    text = ItemView.DMG.format(BaseView.DEFAULT),
                                    font = BaseView.NORMAL_FONT)
    self._weaponCrit        = Label(self._weaponFrame,
                                    text = ItemView.CRIT.format(BaseView.DEFAULT),
                                    font = BaseView.NORMAL_FONT)
    self._weaponAttackLabel = Label(self._weaponFrame,
                                    text = "Attacks:",
                                    font = BaseView.NORMAL_FONT)
    self._weaponAttackVar   = StringVar(self)
    self._weaponAttackCombo = Combobox(self._weaponFrame,
                                       state = "readonly",
                                       textvariable = self._weaponAttackVar)
    self._weaponAttackPreview = SimpleAttackView(self._weaponFrame)
    self._weaponSep2        = Separator(self._weaponFrame, orient = "horizontal")

    # armor frame
    self._armorFrame = Frame(self._rightFrame)
    self._acLabel    = Label(self._armorFrame,
                             text = ItemView.AC.format(BaseView.DEFAULT),
                             font = BaseView.NORMAL_FONT)
    self._armorSep1  = Separator(self._armorFrame, orient = "vertical")
    self._armorSlot  = Label(self._armorFrame,
                             text = ItemView.SLOT.format(BaseView.DEFAULT),
                             font = BaseView.NORMAL_FONT)
    self._armorSep2  = Separator(self._armorFrame, orient = "horizontal")

    # consumable frame
    self._consumableFrame = Frame(self._rightFrame)
    self._effectLabel     = Label(self._consumableFrame,
                                  text = "Effect:",
                                  font = BaseView.NORMAL_FONT)
    self._effectText      = Text(self._consumableFrame,
                                 width = 50,
                                 height = 3,
                                 state = DISABLED,
                                 wrap = WORD,
                                 font = BaseView.NORMAL_FONT)
    self._effectScroll    = Scrollbar(self._consumableFrame,
                                      command = self._effectText.yview)
    self._effectText.config(yscrollcommand = self._effectScroll.set)
    self._consumableSep1  = Separator(self._consumableFrame, orient = "horizontal")


    # placement: scrollbars
    self._equipNotes.grid(          row = 0, column = 0, sticky = N+W+E+S)
    self._equipNotesScroll.grid(    row = 0, column = 1, sticky = N+S)
    self._dropNotes.grid(           row = 0, column = 0, sticky = N+W+E+S)
    self._dropNotesScroll.grid(     row = 0, column = 1, sticky = N+S)
    self._descText.grid(            row = 0, column = 0, sticky = N+W+E+S)
    self._descScroll.grid(          row = 0, column = 1, sticky = N+S)
    self._notesText.grid(           row = 0, column = 0, sticky = N+W+E+S)
    self._notesScroll.grid(         row = 0, column = 1, sticky = N+S)

    # placement: weapon frame
    self._weaponSlot.grid(          row = 0, column = 0,                 sticky = N+W)
    self._weaponRange.grid(         row = 1, column = 0,                 sticky = N+W)
    self._weaponAmmoLabel.grid(     row = 2, column = 0,                 sticky = N+W)
    self._weaponAmmoPreview.grid(   row = 3, column = 0,                 sticky = W+E)
    self._weaponDmg.grid(           row = 0, column = 2, columnspan = 2, sticky = N+W)
    self._weaponCrit.grid(          row = 1, column = 2, columnspan = 2, sticky = N+W)
    self._weaponAttackLabel.grid(   row = 2, column = 2,                 sticky = N+W)
    self._weaponAttackCombo.grid(   row = 2, column = 3,                 sticky = E)
    self._weaponAttackPreview.grid( row = 3, column = 2, columnspan = 2, sticky = W+E)
    self._weaponSep1.grid(          row = 0, column = 1, rowspan = 4,    sticky = N+S)
    self._weaponSep2.grid(          row = 4, column = 0, columnspan = 4, sticky = W+E)

    # placement: armor frame
    self._acLabel.grid(   row = 0, column = 0,                 sticky = N+W)
    self._armorSep1.grid( row = 0, column = 1,                 sticky = N+E+S)
    self._armorSlot.grid( row = 0, column = 2,                 sticky = E)
    self._armorSep2.grid( row = 1, column = 0, columnspan = 3, sticky = W+E)

    # placement: consumable frame
    self._effectLabel.grid(   row = 0, column = 0, columnspan = 2, sticky = N+W)
    self._effectText.grid(    row = 1, column = 0,                 sticky = N+W+E+S)
    self._effectScroll.grid(  row = 1, column = 1,                 sticky = N+S)
    self._consumableSep1.grid(row = 2, column = 0, columnspan = 2, sticky = W+E)

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
    self._leftSep2.grid(        row = 12, column = 0, columnspan = 2, sticky = W+E)
    self._ammoLabel.grid(       row = 13, column = 0,                 sticky = N+W)
    self._ammoCombo.grid(       row = 13, column = 1,                 sticky = E)
    self._ammoPreview.grid(     row = 14, column = 0, columnspan = 2, sticky = W+E)

    # placement: right frame
    self._nameLabel.grid(     row =  0, column = 0, columnspan = 3, sticky = W)
    self._rightSep1.grid(     row =  0, column = 3,                 sticky = N+E+S)
    self._valLabel.grid(      row =  0, column = 4,                 sticky = E)
    self._descLabel.grid(     row =  1, column = 0, columnspan = 5, sticky = W)
    self._descFrame.grid(     row =  2, column = 0, columnspan = 5, sticky = W)
    self._notesLabel.grid(    row =  3, column = 0, columnspan = 5, sticky = W)
    self._notesFrame.grid(    row =  4, column = 0, columnspan = 5, sticky = W)
    self._rightSep2.grid(     row =  5, column = 0, columnspan = 5, sticky = W+E)
    # empty row for special frames
    self._soldAtLabel.grid(   row =  7, column = 0, columnspan = 2, sticky = N+W)
    self._soldAtCombo.grid(   row =  7, column = 2, columnspan = 3, sticky = E)
    self._soldAtPreview.grid( row =  8, column = 0, columnspan = 5, sticky = W+E)
    self._soldAtPrice.grid(   row =  9, column = 0,                 sticky = N+W)
    self._rightSep3.grid(     row =  9, column = 1,                 sticky = N+E+S)
    self._soldAtQty.grid(     row =  9, column = 2,                 sticky = N+W)
    self._rightSep4.grid(     row =  9, column = 3,                 sticky = N+E+S)
    self._stockDays.grid(     row =  9, column = 4,                 sticky = N+E)
    self._rightSep5.grid(     row = 10, column = 0, columnspan = 5, sticky = W+E)
    self._spellLabel.grid(    row = 11, column = 0, columnspan = 2, sticky = N+W)
    self._spellCombo.grid(    row = 11, column = 2, columnspan = 3, sticky = E)
    self._spellPreview.grid(  row = 12, column = 0, columnspan = 5, sticky = W+E)
    self._spellQty.grid(      row = 13, column = 0, columnspan = 5, sticky = N+W)

    self._leftFrame.grid(    row = 0, column = 0,                 sticky = N+W)
    self._rightFrame.grid(   row = 0, column = 1,                 sticky = N+W)

    # bindings
    self._equipVar.trace('w', self._preview_equip)
    self._dropVar.trace('w', self._preview_drop)
    self._ammoVar.trace('w', self._preview_ammo)
    self._spellVar.trace('w', self._preview_spell)
    self._soldAtVar.trace('w', self._preview_sold_at)
    self._weaponAttackVar.trace('w', self._preview_weapon_attack)

  ########
  # Populates all GUI elements with new data.
  def populate(self, data):
    self._data = data
    if data == None: # null check
      self.set_defaults()
      return
    # forget conditional fields
    self._weaponFrame.grid_forget()
    self._armorFrame.grid_forget()
    self._consumableFrame.grid_forget()
    for k, v in data.items():
      if k == "name":
        # non-null
        self._nameLabel.config(text = v)
      elif k == "img":
        if v == None: # null check
          v = BaseView.DEFAULT_IMG
        utility.update_img(self._imgLabel, v, maxSize = 300)
      elif k == "rarity":
        # null accepted
        utility.update_img(self._nameLabel, BaseView.RARITY_IMG[v], maxSize = 30) 
      elif k == "description":
        if v == None: # null check
          v = BaseView.EMPTY_STR
        utility.update_text(self._descText, v)
      elif k == "notes":
        if v == None: # null check
          v = BaseView.EMPTY_STR
        utility.update_text(self._notesText, v)
      elif k == "type":
        # non-null
        if v == 1:
          self._consumableFrame.grid(row = 6, column = 0, columnspan = 5, sticky = W+E)
        elif v == 2:
          self._armorFrame.grid(     row = 6, column = 0, columnspan = 5, sticky = W+E)
        elif v == 3:
          self._weaponFrame.grid(    row = 6, column = 0, columnspan = 5, sticky = W+E)
      elif k == "value":
        if v == None: # null check
          v = BaseView.DEFAULT
        self._valLabel.config(text = v)
      elif k == "ac":
        if v == None: # null check
          v = BaseView.DEFAULT
        self._acLabel.config(text = ItemView.AC.format(v))
      elif k == "slot":
        if v == None: # null check
          v = BaseView.DEFAULT
        self._armorSlot.config(text = ItemView.SLOT.format(v))
        self._weaponSlot.config(text = ItemView.SLOT.format(v))
      elif k == "dmg":
        if v == None: # null check
          v = BaseView.DEFAULT
        self._weaponDmg.config(text = ItemView.DMG.format(v))
      elif k == "crit":
        if v == None: # null check
          v = BaseView.DEFAULT
        self._weaponCrit.config(text = ItemView.CRIT.format(v))
      elif k == "ammo":
        # null accepted
        self._weaponAmmoPreview.populate(v)
      elif k == "range":
        if v == None: # null check
          v = BaseView.DEFAULT
        self._weaponRange.config(text = ItemView.RANGE.format(v))
      elif k == "effect":
        if v == None: # null check
          v = BaseView.EMPTY_STR
        utility.update_text(self._effectText, v)
      elif k == "equippedBy":
        # non-null
        utility.update_combobox(self._equipCombo, [creature["creature"]["name"] for creature in v])
      elif k == "droppedBy":
        # non-null
        utility.update_combobox(self._dropCombo, [creature["creature"]["name"] for creature in v])
      elif k == "ammoFor":
        # non-null
        utility.update_combobox(self._ammoCombo, [item["name"] for item in v])
      elif k == "spellCost":
        # non-null
        utility.update_combobox(self._spellCombo, [spell["spell"]["name"] for spell in v])
      elif k == "soldAt":
        # non-null
        utility.update_combobox(self._soldAtCombo, ["{} ({})".format(store["store"]["name"], store["store"]["location"]) for store in v])
      elif k == "attacks":
        # non-null
        utility.update_combobox(self._weaponAttackCombo, [attack["name"] for attack in v])

  ########
  # Resets GUI elements to default values.
  def set_defaults(self):
    utility.update_img(self._imgLabel, BaseView.DEFAULT_IMG, maxSize = 300)
    utility.update_text(self._descText, BaseView.EMPTY_STR)
    utility.update_text(self._notesText, BaseView.EMPTY_STR)

  ########
  # Updates equipped by preveiw.
  def _preview_equip(self, *args, **kwargs):
    # first reset all
    self._equipPreview.set_defaults()
    self._equipChance.config(text = ItemView.EQUIP_CHANCE.format(BaseView.DEFAULT))
    utility.update_text(self._equipNotes, BaseView.EMPTY_STR)
    # update with new values
    if self._data == None or self._equipCombo.current() == -1:
      return
    newEquip = self._data["equippedBy"][self._equipCombo.current()]
    if newEquip != None:
      self._equipPreview.populate(newEquip["creature"])
      if newEquip["equipChance"] != None:
        self._equipChance.config(text = ItemView.EQUIP_CHANCE.format(newEquip["equipChance"]))
      if newEquip["notes"] != None:
        utility.update_text(self._equipNotes, newEquip["notes"])

  ########
  # Updates dropped by preview.
  def _preview_drop(self, *args, **kwargs):
    # first reset all
    self._dropPreview.set_defaults()
    self._dropChance.config(text = ItemView.DROP_CHANCE.format(BaseView.DEFAULT))
    utility.update_text(self._dropNotes, BaseView.EMPTY_STR)
    # update with new values
    if self._data == None or self._dropCombo.current() == -1:
      return
    newDrop = self._data["droppedBy"][self._dropCombo.current()]
    if newDrop != None:
      self._dropPreview.populate(newDrop["creature"])
      if newDrop["dropChance"] != None:
        self._dropChance.config(text = ItemView.DROP_CHANCE.format(newDrop["equipChance"]))
      if newDrop["notes"] != None:
        utility.update_text(self._dropNotes, newDrop["notes"])

  ########
  # Updates ammo for preview.
  def _preview_ammo(self, *args, **kwargs):
    # first reset all
    self._ammoPreview.set_defaults()
    # update with new values
    if self._data == None or self._ammoCombo.current() == -1:
      return
    newAmmo = self._data["ammoFor"][self._ammoCombo.current()]
    if newAmmo != None:
      self._ammoPreview.populate(newAmmo)

  ########
  # Updates casting cost preview.
  def _preview_spell(self, *args, **kwargs):
    # first reset all
    self._spellPreview.set_defaults()
    self._spellQty.config(text = ItemView.QTY.format(BaseView.DEFAULT))
    # update with new values
    if self._data == None or self._spellCombo.current() == -1:
      return
    newSpell = self._data["spellCost"][self._spellCombo.current()]
    if newSpell != None:
      self._spellPreview.populate(newSpell["spell"])
      if newSpell["qty"] != None:
        self._spellQty.config(text = ItemView.QTY.format(newSpell["qty"]))

  ########
  # Updates store preview.
  def _preview_sold_at(self, *args, **kwargs):
    # first reset all
    self._soldAtPreview.set_defaults()
    self._soldAtPrice.config(text = ItemView.PRICE.format(BaseView.DEFAULT))
    self._soldAtQty.config(text = ItemView.QTY.format(BaseView.DEFAULT))
    self._stockDays.config(text = ItemView.STOCK_DAYS.format(BaseView.DEFAULT))
    # update with new values
    if self._data == None or self._soldAtCombo.current() == -1:
      return
    newSoldAt = self._data["soldAt"][self._soldAtCombo.current()]
    if newSoldAt != None:
      self._soldAtPreview.populate(newSoldAt["store"])
      self._soldAtPrice.config(text = ItemView.PRICE.format(newSoldAt["price"]))
      self._soldAtQty.config(text = ItemView.QTY.format(newSoldAt["qty"]))
      self._stockDays.config(text = ItemView.STOCK_DAYS.format(newSoldAt["stockDays"]))

  ########
  # Updates weapon attack preview.
  def _preview_weapon_attack(self, *args, **kwargs):
    # first reset all
    self._weaponAttackPreview.set_defaults()
    # update with new values
    if self._data == None or self._weaponAttackCombo.current() == -1:
      return
    newAttack = self._data["attacks"][self._weaponAttackCombo.current()]
    if newAttack != None:
      self._weaponAttackPreview.populate(newAttack)
# ItemView
################

########
# Test code
if __name__ == "__main__":
  from DnDReferenceBook.src.dbase_manager import DatabaseManager
  from tkinter.ttk import Notebook

  root = Tk()

  dbm = DatabaseManager("../data/dnd_ref_book.db", "../data/img/")
  # dbm.reset("../src/tables.sql", "../src/real.sql")
  itemList = dbm.get_item_list()

  nb = Notebook(root)
  av = ItemView(nb)
  nb.add(av, text = "Default")
  for item in itemList:
    temp = ItemView(nb, dbm.get_item(item["name"]))
    nb.add(temp, text = item["name"])
  nb.grid(row = 0, column = 0)

  top = Toplevel(root)
  sav = SimpleItemView(top)
  sav.grid(row = 0, column = 0, sticky = W+E)
  for i in range(len(itemList)):
    temp = SimpleItemView(top, dbm.get_simple_item(itemList[i]["name"]))
    temp.grid(row = i + 1, column = 0, sticky = W+E)

  root.mainloop()
