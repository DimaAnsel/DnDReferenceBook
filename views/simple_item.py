################################
# simple_item.py
# Noah Ansel
# 2017-10-19
# ------------------------------
# Tkinter view for the simple Item object as presented by the DatabaseManager.
################################

from tkinter import *
from base_view import BaseView
import utility

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
    self._data = data
    if data == None:
      self.set_defaults()
      return
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
