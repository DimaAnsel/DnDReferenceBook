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
from simple_store import SimpleStoreView
from simple_creature import SimpleCreatureView
from tkinter.ttk import Combobox, Separator

################
# Tkinter representation of full location object, used as separate page.
class LocationView(BaseView):

  ########
  # Initializes and places all GUI elements.
  def _create_widgets(self):
    # left frame
    self._leftFrame         = Frame(self)
    self._imgLabel          = Label(self._leftFrame)
    self._storeLabel        = Label(self._leftFrame,
                                    text = "Stores",
                                    font = BaseView.NORMAL_FONT)
    self._storeVar          = StringVar(self)
    self._storeCombo        = Combobox(self._leftFrame,
                                       state = "readonly",
                                       textvariable = self._storeVar)
    self._storePreview      = SimpleStoreView(self._leftFrame)
    self._leftSep1          = Separator(self._leftFrame, orient = "horizontal")
    self._inhabitantLabel   = Label(self._leftFrame,
                                    text = "Inhabitants:",
                                    font = BaseView.NORMAL_FONT)
    self._inhabitantVar     = StringVar(self)
    self._inhabitantCombo   = Combobox(self._leftFrame,
                                       state = "readonly",
                                       textvariable = self._inhabitantVar)
    self._inhabitantPreview = SimpleCreatureView(self._leftFrame)
    self._inhabitantNotesFrame = Frame(self._leftFrame)
    self._inhabitantNotesLabel = Label(self._leftFrame,
                                       text = "Notes:",
                                       font = BaseView.NORMAL_FONT)
    self._inhabitantNotes   = Text(self._inhabitantNotesFrame,
                                   width = 30,
                                   height = 2,
                                   state = DISABLED,
                                   wrap = WORD,
                                   font = BaseView.NORMAL_FONT)
    self._inhabitantNotesScroll = Scrollbar(self._inhabitantNotesFrame,
                                       command = self._inhabitantNotes.yview)
    self._inhabitantNotes.config(yscrollcommand = self._inhabitantNotesScroll.set)

    # right frame
    self._rightFrame    = Frame(self)
    self._nameLabel     = Label(self._rightFrame,
                                text = "Name",
                                font = BaseView.LARGE_FONT)
    self._descLabel     = Label(self._rightFrame,
                                text = "Description:",
                                font = BaseView.NORMAL_FONT)
    self._descFrame     = Frame(self._rightFrame)
    self._descText      = Text(self._descFrame,
                               width = 50,
                               height = 8,
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
                               height = 8,
                               state = DISABLED,
                               wrap = WORD,
                               font = BaseView.NORMAL_FONT)
    self._notesScroll   = Scrollbar(self._notesFrame,
                                    command = self._notesText.yview)
    self._notesText.config(yscrollcommand = self._notesScroll.set)

    # placement: scrollbars
    self._inhabitantNotes.grid(       row = 0, column = 0, sticky = N+W+E+S)
    self._inhabitantNotesScroll.grid( row = 0, column = 1, sticky = N+S)
    self._descText.grid(              row = 0, column = 0, sticky = N+W+E+S)
    self._descScroll.grid(            row = 0, column = 1, sticky = N+S)
    self._notesText.grid(             row = 0, column = 0, sticky = N+W+E+S)
    self._notesScroll.grid(           row = 0, column = 1, sticky = N+S)

    # placement: left frame
    self._imgLabel.grid(              row = 0, column = 0, columnspan = 2, sticky = N+W+E+S)
    self._storeLabel.grid(            row = 1, column = 0,                 sticky = N+W)
    self._storeCombo.grid(            row = 1, column = 1,                 sticky = E)
    self._storePreview.grid(          row = 2, column = 0, columnspan = 2, sticky = W+E)
    self._leftSep1.grid(              row = 3, column = 0, columnspan = 2, sticky = W+E)
    self._inhabitantLabel.grid(       row = 4, column = 0,                 sticky = N+W)
    self._inhabitantCombo.grid(       row = 4, column = 1,                 sticky = E)
    self._inhabitantPreview.grid(     row = 5, column = 0, columnspan = 2, sticky = W+E)
    self._inhabitantNotesLabel.grid(  row = 6, column = 0, columnspan = 2, sticky = N+W)
    self._inhabitantNotesFrame.grid(  row = 7, column = 0, columnspan = 2, sticky = N+W+E)

    # placement: right frame
    self._nameLabel.grid(   row = 0, column = 0,                 sticky = W)
    self._descLabel.grid(   row = 1, column = 0,                 sticky = W)
    self._descFrame.grid(   row = 2, column = 0,                 sticky = W)
    self._notesLabel.grid(  row = 3, column = 0,                 sticky = W)
    self._notesFrame.grid(  row = 4, column = 0,                 sticky = W)

    self._leftFrame.grid(    row = 0, column = 0,                 sticky = N+W)
    self._rightFrame.grid(   row = 0, column = 1,                 sticky = N+W)


  ########
  # Add callbacks for all GUI element events and Tkinter variables.
  def _bind_widgets(self):
    self._storeVar.trace('w', self._preview_store)
    self._inhabitantVar.trace('w', self._preview_inhabitant)

    self._storePreview.bind(      "<Double-Button-1>", self._open_store)
    self._inhabitantPreview.bind( "<Double-Button-1>", self._open_inhabitant)

  ########
  # Populates all GUI elements with new data.
  def populate(self, data):
    self._data = data
    if data == None: # null check
      self.set_defaults()
      return
    for k, v in data.items():
      if k == "img":
        if v == None: # null check
          v = BaseView.DEFAULT_IMG
        utility.update_img(self._imgLabel, v, maxSize = 300)
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
      elif k == "stores":
        if v == None: # null check
          v = []
        utility.update_combobox(self._storeCombo, [store["name"] for store in v])
      elif k == "creatures":
        if v == None: # null check
          v = []
        utility.update_combobox(self._inhabitantCombo, [creature["creature"]["name"] for creature in v])

  ########
  # Resets GUI elements to default values.
  def set_defaults(self):
    utility.update_img(self._imgLabel, BaseView.DEFAULT_IMG, maxSize = 300)
    utility.update_text(self._descText, BaseView.EMPTY_STR)
    utility.update_text(self._notesText, BaseView.EMPTY_STR)
    utility.update_combobox(self._storeCombo, [])
    utility.update_combobox(self._inhabitantCombo, [])


  ########
  # Updates equipment preview.
  def _preview_store(self, *args, **kwargs):
    # first reset all
    self._storePreview.set_defaults()
    # update with new values
    if self._data == None or self._storeCombo.current() == -1:
      return
    newStore = self._data["stores"][self._storeCombo.current()]
    if newStore != None:
      self._storePreview.populate(newStore)

  ########
  # Updates drop preview.
  def _preview_inhabitant(self, *args, **kwargs):
    # first reset all
    self._inhabitantPreview.set_defaults()
    utility.update_text(self._inhabitantNotes, BaseView.EMPTY_STR)
    # update with new values
    if self._data == None or self._inhabitantCombo.current() == -1:
      return
    newInhabitant = self._data["creatures"][self._inhabitantCombo.current()]
    if newInhabitant != None:
      self._inhabitantPreview.populate(newInhabitant["creature"])
      if newInhabitant["notes"] != None:
        utility.update_text(self._inhabitantNotes, newInhabitant["notes"])

  ########
  # Opens store view through refBook.
  def _open_store(self, *args, **kwargs):
    idx = self._storeCombo.current()
    if self._refBook == None or self._data == None or idx == -1 or len(self._data["stores"]) == 0:
      return
    self._refBook.show_store(self._data["stores"][idx]["name"], self._data["name"])

  ########
  # Opens creature view through refBook.
  def _open_inhabitant(self, *args, **kwargs):
    idx = self._inhabitantCombo.current()
    if self._refBook == None or self._data == None or idx == -1 or len(self._data["creatures"]) == 0:
      return
    self._refBook.show_creature(self._data["creatures"][idx]["creature"]["name"])
# LocationView
################

########
# Test code
if __name__ == "__main__":
  from DnDReferenceBook.src.dbase_manager import DatabaseManager
  from simple_location import SimpleLocationView
  from tkinter.ttk import Notebook

  root = Tk()

  dbm = DatabaseManager("../data/dnd_ref_book.db")
  dbm.reset("../src/tables.sql", "../src/real.sql")
  locList = dbm.get_location_list()

  nb = Notebook(root)
  lv = LocationView(nb)
  nb.add(lv, text = "Default")
  for location in locList:
    temp = LocationView(nb, dbm.get_location(location["name"]))
    nb.add(temp, text = location["name"])
  nb.grid(row = 0, column = 0, sticky = N+W+E+S)

  top = Toplevel(root)
  slv = SimpleLocationView(top)
  slv.grid(row = 0, column = 0, sticky = W+E)
  for i in range(len(locList)):
    temp = SimpleLocationView(top, dbm.get_simple_location(locList[i]["name"]))
    temp.grid(row = i + 1, column = 0, sticky = W+E)

  root.mainloop()
