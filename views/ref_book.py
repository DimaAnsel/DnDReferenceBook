################################
# ref_book.py
# Noah Ansel
# 2017-10-25
# ------------------------------
# Home page of ref book.
################################

from tkinter import *
import utility
from DnDReferenceBook.src.dbase_manager import DatabaseManager
from tkinter.ttk import Notebook, Treeview
from base_view import BaseView
from simple_item import SimpleItemView
from simple_store import SimpleStoreView
from simple_attack import SimpleAttackView
from simple_creature import SimpleCreatureView
from simple_location import SimpleLocationView
from item import ItemView
from store import StoreView
from attack import AttackView
from creature import CreatureView
from location import LocationView

################
# Tkinter representation of full reference book, used as parent for child frames.
class RefBook(Frame):

  ########
  # Opens database from provided arguments and creates and populates widgets.
  def __init__(self, master, *args, **kwargs):
    super().__init__(master)

    self._dbm = DatabaseManager(*args, **kwargs)
    self._openItems = {}
    self._openStores = {}
    self._openAttacks = {}
    self._openCreatures = {}
    self._openLocations = {}

    self._create_widgets()
    self._populate_items()
    self._populate_stores()
    self._populate_attacks()
    self._populate_creatures()
    self._populate_locations()

  ########
  # Initializes and places all GUI elements.
  def _create_widgets(self):
    self._nb = Notebook(self)

    # items
    self._itemTab   = Frame(self._nb)
    self._itemTree  = Treeview(self._itemTab,
                               columns = ["type", "value"],
                               selectmode = "browse",
                               height = 25)
    self._itemTree.heading("#0",    text = "Item",  anchor = N+W)
    self._itemTree.column( "#0",    width = 300,    anchor = N+W, stretch = True)
    self._itemTree.heading("type",  text = "Type",  anchor = N+W)
    self._itemTree.column( "type",  width = 100,    anchor = N+W)
    self._itemTree.heading("value", text = "Value", anchor = N+W)
    self._itemTree.column( "value", width = 60,     anchor = N+W)
    self._itemScroll = Scrollbar(self._itemTab,
                                command = self._itemTree.yview)
    self._itemTree.config(yscrollcommand = self._itemScroll.set)

    self._itemTree.grid(row = 0, column = 0, sticky = N+W+S+E)
    self._itemScroll.grid(row = 0, column = 1, sticky = N+S)
    self._nb.add(self._itemTab, text = "Items")

    # stores
    self._storeTab  = Frame(self._nb)
    self._storeTree = Treeview(self._storeTab,
                               columns = ["location"],
                               selectmode = "browse",
                               height = 25)
    self._storeTree.heading("#0",       text = "Store",     anchor = N+W)
    self._storeTree.column( "#0",       width = 330,        anchor = N+W, stretch = True)
    self._storeTree.heading("location", text = "Location",  anchor = N+W)
    self._storeTree.column( "location", width = 130,        anchor = N+W)
    self._storeScroll = Scrollbar(self._storeTab,
                                  command = self._storeTree.yview)
    self._storeTree.config(yscrollcommand = self._storeScroll.set)

    self._storeTree.grid(row = 0, column = 0, sticky = N+W+S+E)
    self._storeScroll.grid(row = 0, column = 1, sticky = N+S)
    self._nb.add(self._storeTab, text = "Stores")

    # attacks
    self._attackTab  = Frame(self._nb)
    self._attackTree = Treeview(self._attackTab,
                               columns = ["id", "spell"],
                               selectmode = "browse",
                               height = 25)
    self._attackTree.heading("#0",    text = "Attacks", anchor = N+W)
    self._attackTree.column( "#0",    width = 370,      anchor = N+W, stretch = True)
    self._attackTree.heading("id",    text = "ID",      anchor = N+W)
    self._attackTree.column( "id",    width = 40,       anchor = N+E)
    self._attackTree.heading("spell", text = "Spell",   anchor = N+W)
    self._attackTree.column( "spell", width = 50,       anchor = CENTER)
    self._attackScroll = Scrollbar(self._attackTab,
                                   command = self._attackTree.yview)
    self._attackTree.config(yscrollcommand = self._attackScroll.set)

    self._attackTree.grid(row = 0, column = 0, sticky = N+W+S+E)
    self._attackScroll.grid(row = 0, column = 1, sticky = N+S)
    self._nb.add(self._attackTab, text = "Attacks")

    # creatures
    self._creatureTab  = Frame(self._nb)
    self._creatureTree = Treeview(self._creatureTab,
                               columns = ["hd"],
                               selectmode = "browse",
                               height = 25)
    self._creatureTree.heading("#0",    text = "Creatures", anchor = N+W)
    self._creatureTree.column( "#0",    width = 420,      anchor = N+W, stretch = True)
    self._creatureTree.heading("hd",    text = "HD",      anchor = N+W)
    self._creatureTree.column( "hd",    width = 40,       anchor = N+E)
    self._creatureScroll = Scrollbar(self._creatureTab,
                                   command = self._creatureTree.yview)
    self._creatureTree.config(yscrollcommand = self._creatureScroll.set)

    self._creatureTree.grid(row = 0, column = 0, sticky = N+W+S+E)
    self._creatureScroll.grid(row = 0, column = 1, sticky = N+S)
    self._nb.add(self._creatureTab, text = "Creatures")

    # locations
    self._locationTab  = Frame(self._nb)
    self._locationTree = Treeview(self._locationTab,
                                  selectmode = "browse",
                                  height = 25)
    self._locationTree.heading("#0", text = "Locations",  anchor = N+W)
    self._locationTree.column( "#0", width = 460,         anchor = N+W, stretch = True)
    self._locationScroll = Scrollbar(self._locationTab,
                                     command = self._locationTree.yview)
    self._locationTree.config(yscrollcommand = self._locationScroll.set)

    self._locationTree.grid(row = 0, column = 0, sticky = N+W+S+E)
    self._locationScroll.grid(row = 0, column = 1, sticky = N+S)
    self._nb.add(self._locationTab, text = "Locations")

    self._nb.grid(row = 0, column = 0, sticky = N+W+S+E)

    # bindings
    self._itemTree.bind("<Double-Button-1>", self._item_on_double_click)
    self._storeTree.bind("<Double-Button-1>", self._store_on_double_click)
    self._attackTree.bind("<Double-Button-1>", self._attack_on_double_click)
    self._creatureTree.bind("<Double-Button-1>", self._creature_on_double_click)
    self._locationTree.bind("<Double-Button-1>", self._location_on_double_click)

  ########
  # Populates item list.
  def _populate_items(self):
    self._itemList = self._dbm.get_item_list()

    allItems = self._itemTree.get_children()
    for item in allItems:
      self._itemTree.delete(item)
    self._itemImgs = []
    if self._dbm == None:
      return
    for entry in self._itemList:
      img = entry["img"]
      if img == None:
        img = BaseView.DEFAULT_IMG
      img = utility.get_img(img, maxSize = 20)
      name = entry["name"]
      fields = [BaseView.TYPE_MAP[entry["type"]],
                entry["value"]]
      for i in range(len(fields)):
        if fields[i] == None:
          fields[i] = BaseView.EMPTY_STR
      self._itemImgs.append(img)
      self._itemTree.insert("", END, image = img, text = name, values = fields)

  ########
  # Populates store list.
  def _populate_stores(self):
    self._storeList = self._dbm.get_store_list()

    allStores = self._storeTree.get_children()
    for store in allStores:
      self._storeTree.delete(store)
    self._storeImgs = []
    if self._dbm == None:
      return
    for entry in self._storeList:
      img = entry["img"]
      if img == None:
        img = BaseView.DEFAULT_IMG
      img = utility.get_img(img, maxSize = 20)
      name = entry["name"]
      fields = [entry["location"]]
      for i in range(len(fields)):
        if fields[i] == None:
          fields[i] = BaseView.EMPTY_STR
      self._storeImgs.append(img)
      self._storeTree.insert("", END, image = img, text = name, values = fields)

  ########
  # Populates attack list.
  def _populate_attacks(self):
    self._attackList = self._dbm.get_attack_list()

    allAttacks = self._attackTree.get_children()
    for attack in allAttacks:
      self._attackTree.delete(attack)
    self._attackImgs = []
    if self._dbm == None:
      return
    for entry in self._attackList:
      img = entry["img"]
      if img == None:
        img = BaseView.DEFAULT_IMG
      img = utility.get_img(img, maxSize = 20)
      name = entry["name"]
      fields = [entry["id"],
                "✔" if entry["isSpell"] else ""]
      for i in range(len(fields)):
        if fields[i] == None:
          fields[i] = BaseView.EMPTY_STR
      self._attackImgs.append(img)
      self._attackTree.insert("", END, image = img, text = name, values = fields)

  ########
  # Populates creature list.
  def _populate_creatures(self):
    self._creatureList = self._dbm.get_creature_list()

    allCreatures = self._creatureTree.get_children()
    for creature in allCreatures:
      self._creatureTree.delete(creature)
    self._creatureImgs = []
    if self._dbm == None:
      return
    for entry in self._creatureList:
      img = entry["img"]
      if img == None:
        img = BaseView.DEFAULT_IMG
      img = utility.get_img(img, maxSize = 20)
      name = entry["name"]
      fields = [str(entry["hd"])]
      for i in range(len(fields)):
        if fields[i] == None:
          fields[i] = BaseView.EMPTY_STR
      self._creatureImgs.append(img)
      self._creatureTree.insert("", END, image = img, text = name, values = fields)

  ########
  # Populates location list.
  def _populate_locations(self):
    self._locationList = self._dbm.get_location_list()

    allLocations = self._locationTree.get_children()
    for location in allLocations:
      self._locationTree.delete(location)
    self._locationImgs = []
    if self._dbm == None:
      return
    for entry in self._locationList:
      img = entry["img"]
      if img == None:
        img = BaseView.DEFAULT_IMG
      img = utility.get_img(img, maxSize = 20)
      name = entry["name"]
      self._locationImgs.append(img)
      self._locationTree.insert("", END, image = img, text = name)

  ########
  # Callback for double clicking in item treeview.
  def _item_on_double_click(self, *args, **kwargs):
    if len(self._itemTree.selection()) == 0:
      return
    self.show_item(self._itemList[self._itemTree.index(self._itemTree.selection())]["name"])

  ########
  # Callback for double clicking in store treeview.
  def _store_on_double_click(self, *args, **kwargs):
    if len(self._storeTree.selection()) == 0:
      return
    curr = self._storeList[self._storeTree.index(self._itemTree.selection())]
    self.show_store(curr["name"], curr["location"])

  ########
  # Callback for double clicking in attack treeview.
  def _attack_on_double_click(self, *args, **kwargs):
    if len(self._attackTree.selection()) == 0:
      return
    self.show_attack(self._attackList[self._attackTree.index(self._attackTree.selection())]["id"])

  ########
  # Callback for double clicking in creature treeview.
  def _creature_on_double_click(self, *args, **kwargs):
    if len(self._creatureTree.selection()) == 0:
      return
    self.show_creature(self._creatureList[self._creatureTree.index(self._creatureTree.selection())]["name"])

  ########
  # Callback for double clicking in location treeview.
  def _location_on_double_click(self, *args, **kwargs):
    if len(self._locationTree.selection()) == 0:
      return
    self.show_location(self._locationList[self._locationTree.index(self._locationTree.selection())]["name"])

  ########
  # Shows a full item in a new window.
  def show_item(self, name):
    if name in self._openItems.keys():
      # TODO: make this cleaner
      try:
        self._openItems[name].lift()
        return
      except TclError:
        pass # fallthrough to make new window
    newWindow = Toplevel(self)
    itemView = ItemView(newWindow, self._dbm.get_item(name))
    itemView.grid(row = 0, column = 0, sticky = N+W+E+S)
    newWindow.title(name)
    newWindow.lift()
    self._openItems[name] = newWindow

  ########
  # Shows a full store in a new window.
  def show_store(self, name, location):
    key = (name, location)
    if key in self._openStores.keys():
      # TODO: make this cleaner
      try:
        self._openStores[key].lift()
        return
      except TclError:
        pass # fallthrough to make new window
    newWindow = Toplevel(self)
    storeView = StoreView(newWindow, self._dbm.get_store(name, location))
    storeView.grid(row = 0, column = 0, sticky = N+W+E+S)
    newWindow.title(name)
    newWindow.lift()
    self._openStores[key] = newWindow

  ########
  # Shows a full attack in a new window.
  def show_attack(self, attackId):
    if attackId in self._openAttacks.keys():
      # TODO: make this cleaner
      try:
        self._openAttacks[attackId].lift()
        return
      except TclError:
        pass # fallthrough to make new window
    attack = self._dbm.get_attack(attackId)
    newWindow = Toplevel(self)
    attackView = AttackView(newWindow, self._dbm.get_attack(attackId))
    attackView.grid(row = 0, column = 0, sticky = N+W+E+S)
    newWindow.title("{} ({})".format(attack["name"], attack["id"]))
    newWindow.lift()
    self._openAttacks[attackId] = newWindow

  ########
  # Shows a full creature in a new window.
  def show_creature(self, name):
    if name in self._openCreatures.keys():
      # TODO: make this cleaner
      try:
        self._openCreatures[name].lift()
        return
      except TclError:
        pass # fallthrough to make new window
    newWindow = Toplevel(self)
    creatureView = CreatureView(newWindow, self._dbm.get_creature(name))
    creatureView.grid(row = 0, column = 0, sticky = N+W+E+S)
    newWindow.title(name)
    newWindow.lift()
    self._openCreatures[name] = newWindow

  ########
  # Shows a full location in a new window.
  def show_location(self, name):
    if name in self._openLocations.keys():
      # TODO: make this cleaner
      try:
        self._openLocations[name].lift()
        return
      except TclError:
        pass # fallthrough to make new window
    newWindow = Toplevel(self)
    locationView = LocationView(newWindow, self._dbm.get_location(name))
    locationView.grid(row = 0, column = 0, sticky = N+W+E+S)
    newWindow.title(name)
    newWindow.lift()
    self._openLocations[name] = newWindow

# RefBook
################


########
# Test code
if __name__ == "__main__":

  root = Tk()
  root.title("DnD Reference Book")
  refBook = RefBook(root, "../data/dnd_ref_book.db", "../data/img/")
  refBook.grid(row = 0, column = 0, sticky = N+W+S+E)

  root.mainloop()
