################################
# store.py
# Noah Ansel
# 2017-10-16
# ------------------------------
# Tkinter view for the Store object as presented by the DatabaseManager.
################################

from tkinter import *
from base_view import BaseView
import utility
from tkinter.ttk import Treeview, Separator
from simple_location import SimpleLocationView

################
# Tkinter representation of full store object, used as separate page.
class StoreView(BaseView):

  ########
  # Initializes and places all GUI elements.  
  def _create_widgets(self):
    # left frame
    self._leftFrame    = Frame(self)
    self._imgLabel     = Label(self._leftFrame)
    self._locLabel     = Label(self._leftFrame,
                               text = "Location:",
                               font = BaseView.NORMAL_FONT)
    self._locPreview   = SimpleLocationView(self._leftFrame)

    # right frame
    self._rightFrame    = Frame(self)
    self._nameLabel     = Label(self._rightFrame,
                                compound = LEFT,
                                text = "Name",
                                font = BaseView.LARGE_FONT)
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

    # bottom
    self._sep1          = Separator(self, orient = "horizontal")
    self._invLabel      = Label(self,
                                text = "Inventory:",
                                font = BaseView.NORMAL_FONT)
    self._invFrame      = Frame(self)
    self._inventory     = Treeview(self._invFrame,
                                   columns = ["type", "price", "qty", "stockDays"],
                                   selectmode = "browse",
                                   height = 15)
    self._inventory.heading("#0",         text = "Item",        anchor = N+W)
    self._inventory.column( "#0",         width = 300,          anchor = N+W, stretch = True)
    self._inventory.heading("type",       text = "Type",        anchor = N+W)
    self._inventory.column( "type",       width = 100,           anchor = N+W)
    self._inventory.heading("price",      text = "Price",       anchor = N+W)
    self._inventory.column( "price",      width = 60,          anchor = N+W)
    self._inventory.heading("qty",        text = "Qty",         anchor = N+W)
    self._inventory.column( "qty",        width = 40,           anchor = N+W)
    self._inventory.heading("stockDays",  text = "Stock Days",  anchor = N+W)
    self._inventory.column( "stockDays",  width = 200,          anchor = N+W, stretch = True)
    self._invScroll = Scrollbar(self._invFrame,
                                command = self._inventory.yview)
    self._inventory.config(yscrollcommand = self._invScroll.set)

    # placement: scrollbars
    self._descText.grid(            row = 0, column = 0, sticky = N+W+E+S)
    self._descScroll.grid(          row = 0, column = 1, sticky = N+S)
    self._notesText.grid(           row = 0, column = 0, sticky = N+W+E+S)
    self._notesScroll.grid(         row = 0, column = 1, sticky = N+S)
    self._inventory.grid(           row = 0, column = 0, sticky = N+W+E+S)
    self._invScroll.grid(           row = 0, column = 1, sticky = N+S)

    # placement: left frame
    self._imgLabel.grid(        row = 0, column = 0,                 sticky = N+W+E+S)
    self._locLabel.grid(        row = 1, column = 0,                 sticky = N+W)
    self._locPreview.grid(      row = 2, column = 0,                 sticky = W+E)

    # placement: right frame
    self._nameLabel.grid(     row = 0, column = 0,                 sticky = W)
    self._descLabel.grid(     row = 1, column = 0,                 sticky = W)
    self._descFrame.grid(     row = 2, column = 0,                 sticky = W)
    self._notesLabel.grid(    row = 3, column = 0,                 sticky = W)
    self._notesFrame.grid(    row = 4, column = 0,                 sticky = W)

    # bottom
    self._sep1.grid(          row = 1, column = 0, columnspan = 2, sticky = W+E)
    self._invLabel.grid(      row = 2, column = 0, columnspan = 2, sticky = N+W)
    self._invFrame.grid(      row = 3, column = 0, columnspan = 2, sticky = W+E)

    self._leftFrame.grid(    row = 0, column = 0,                 sticky = N+W)
    self._rightFrame.grid(   row = 0, column = 1,                 sticky = N+W)

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
      elif k == "location":
        # non-null
        self._locPreview.populate(v)
      elif k == "description":
        if v == None: # null check
          v = BaseView.EMPTY_STR
        utility.update_text(self._descText, v)
      elif k == "notes":
        if v == None: # null check
          v = BaseView.EMPTY_STR
        utility.update_text(self._notesText, v)
      elif k == "sells":
        self._update_inventory()

  ########
  # Resets GUI elements to default values.
  def set_defaults(self):
    utility.update_img(self._imgLabel, BaseView.DEFAULT_IMG, maxSize = 300)
    utility.update_text(self._descText, BaseView.EMPTY_STR)
    utility.update_text(self._notesText, BaseView.EMPTY_STR)

  ########
  # Populates inventory with correct values
  def _update_inventory(self):
    allItems = self._inventory.get_children()
    for item in allItems:
      self._inventory.delete(item)
    self._imgs = []
    if self._data == None:
      return
    for entry in self._data["sells"]:
      img = entry["item"]["img"]
      if img == None:
        img = BaseView.DEFAULT_IMG
      img = utility.get_img(img, maxSize = 20)
      name = entry["item"]["name"]
      fields = [BaseView.TYPE_MAP[entry["item"]["type"]],
                entry["price"],
                entry["qty"],
                entry["stockDays"]]
      for i in range(len(fields)):
        if fields[i] == None:
          fields[i] = BaseView.EMPTY_STR
      self._imgs.append(img)
      self._inventory.insert("", END, image = img, text = name, values = fields)
# StoreView
################

########
# Test code
if __name__ == "__main__":
  from DnDReferenceBook.src.dbase_manager import DatabaseManager
  from tkinter.ttk import Notebook
  from simple_store import SimpleStoreView

  root = Tk()

  dbm = DatabaseManager("../data/dnd_ref_book.db")
  # dbm.reset("../src/tables.sql", "../src/real.sql")
  storeList = dbm.get_store_list()

  nb = Notebook(root)
  sv = StoreView(root)
  nb.add(sv, text = "Default")
  for store in storeList:
    temp = StoreView(nb, dbm.get_store(store["name"], store["location"]))
    nb.add(temp, text = "{} ({})".format(store["name"], store["location"]))
  nb.grid(row = 0, column = 0)

  top = Toplevel(root)
  ssv = SimpleStoreView(top)
  ssv.grid(row = 0, column = 0, sticky = W+E)
  for i in range(len(storeList)):
    temp = SimpleStoreView(top, storeList[i])
    temp.grid(row = i + 1, column = 0, sticky = W+E)

  root.mainloop()
