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
# Tkinter representation of simple attack object, used for previews.
class SimpleAttackView(BaseView):

  def _create_widgets(self):
    self._imgLabel = Label(self)
    self._nameLabel = Label(self, text = "Name")
    self._spellLabel = Label(self)

    self._imgLabel.grid(  row = 0, column = 0, sticky = N+W+E+S)
    self._spellLabel.grid(row = 0, column = 1, sticky = N+W+E+S)
    self._nameLabel.grid( row = 0, column = 2, sticky = W)

  def populate(self, data):
    self._data = data
    if data == None:
      self.set_defaults()
      return
    name = ""
    for k, v in data.items():
      if k == "name":
        name = v
      elif k == "img":
        if v == None:
          v = BaseView.DEFAULT_IMG
        utility.update_img(self._imgLabel, v, maxSize = 30)
      elif k == "isSpell":
        if v == None:
          v = False
        utility.update_img(self._spellLabel, BaseView.WAND_IMG[v], maxSize = 30)
    self._nameLabel.config(text = name)


  def set_defaults(self):
    utility.update_img(self._imgLabel, BaseView.DEFAULT_IMG, maxSize = 30)
    utility.update_img(self._spellLabel, BaseView.WAND_IMG[False], maxSize = 30)
    self._nameLabel.config(text = "Name")
# SimpleAttackView
################
