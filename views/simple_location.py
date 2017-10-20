################################
# simple_location.py
# Noah Ansel
# 2017-10-16
# ------------------------------
# Tkinter view for the simple Location object as presented by the DatabaseManager.
################################

from tkinter import *
from base_view import BaseView
import utility

################
# Tkinter representation of simple location object, used for previews.
class SimpleLocationView(BaseView):

  def _create_widgets(self):
    self._imgLabel = Label(self)
    self._nameLabel = Label(self, text = "Name")

    self._imgLabel.grid(  row = 0, column = 0, sticky = N+W+E+S)
    self._nameLabel.grid( row = 0, column = 1, sticky = W)

  def populate(self, data):
    for k, v in data.items():
      if k == "name":
        # non-null
        self._nameLabel.config(text = v)
      elif k == "img":
        if v == None: # null check
          v = BaseView.DEFAULT_IMG
        utility.update_img(self._imgLabel, v, maxSize = 30)


  def set_defaults(self):
    utility.update_img(self._imgLabel, BaseView.DEFAULT_IMG, maxSize = 30)
    self._nameLabel.config(text = "Name")
# SimpleLocationView
################
