################################
# simple_creature.py
# Noah Ansel
# 2017-10-19
# ------------------------------
# Tkinter view for the simple Creature object as presented by the DatabaseManager.
################################

from tkinter import *
from base_view import BaseView
import utility

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
    self._data = data
    if data == None:
      self.set_defaults()
      return
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
