################################
# simple_store.py
# Noah Ansel
# 2017-10-19
# ------------------------------
# Tkinter view for the simple Store object as presented by the DatabaseManager.
################################

from tkinter import *
from base_view import BaseView
import utility

################
# Tkinter representation of simple store object, used for previews.
class SimpleStoreView(BaseView):

  NAME_FORMAT = "{} ({})"

  def _create_widgets(self):
    self._imgLabel = Label(self)
    self._nameLabel = Label(self, text = SimpleStoreView.NAME_FORMAT.format("Name", BaseView.DEFAULT))

    self._imgLabel.grid(  row = 0, column = 0, sticky = N+W+E+S)
    self._nameLabel.grid( row = 0, column = 1, sticky = W)

  def populate(self, data):
    self._data = data
    if data == None:
      self.set_defaults()
      return
    name = ""
    location = ""
    for k, v in data.items():
      if k == "name":
        # non-null
        name = v
      elif k == "location":
        # non-null
        if isinstance(v, str): # from simple store
          location = v
        else: # from full store
          location = v["name"]
      elif k == "img":
        if v == None: # null check
          v = BaseView.DEFAULT_IMG
        utility.update_img(self._imgLabel, v, maxSize = 30)
    self._nameLabel.config(text = SimpleStoreView.NAME_FORMAT.format(name, location))

  def set_defaults(self):
    utility.update_img(self._imgLabel, BaseView.DEFAULT_IMG, maxSize = 30)
    self._nameLabel.config(text = SimpleStoreView.NAME_FORMAT.format("Name", BaseView.DEFAULT))
# SimpleStoreView
################
