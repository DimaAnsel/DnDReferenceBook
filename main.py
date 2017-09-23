from tkinter import *
import sqlite3
from dbase_manager import *
from views import *




class ReferenceBook(Frame):

  def __init__(self, master, dbm):
    super().__init__(master)
    self._dbm = dbm

    self._create_widgets()

  def _create_widgets(self):
    self._modifyEntry = Text(self)
    self._queryEntry = Entry(self, text = "SELECT * FROM Creatures")
    self._queryRes = Text(self)
    self._modifyButton = Button(self, text = "Modify", command = self._modify_action)
    self._queryButton = Button(self, text = "Query", command = self._query_action)
    self._commitButton = Button(self, text = "Commit", command = self._commit_action)

    self._creatureList = Frame(self)
    self._creatureList.listbox = Listbox(self._creatureList,
                                         exportselection = 0)
    self._creatureList.scrollbar = Scrollbar(self._creatureList,
                                             command = self._creatureList.listbox.yview)
    self._creatureList.listbox.config(yscrollcommand = self._creatureList.listbox.scrollbar.set)
    self._creatureList.listbox.pack(side = "left", fill = BOTH)
    self._creatureList.scrollbar.pack(side = "left", fill = Y)
    self._creature = CreatureView(self)

    self._modifyEntry.grid(row = 0, column = 0, rowspan = 2, sticky = N + W + S + E)
    self._queryEntry.grid(row = 0, column = 1, sticky = W + E)
    self._queryRes.grid(row = 1, column = 1, sticky = N + W + S + E)
    self._modifyButton.grid(row = 2, column = 0, sticky = W + E)
    self._queryButton.grid(row = 2, column = 1, sticky = W + E)
    self._commitButton.grid(row = 3, column = 0, rowspan = 2, sticky = W + E)

    self._creatureList.grid(row = 0, column = 2, rowspan = 4, sticky = N+W+E+S)
    self._creature.grid(row = 0, column = 3, rowspan = 4, sticky = N+W+E+S)

  def _modify_action(self):
    self._dbm._cursor.execute(self._modifyEntry.get(0.0, END))
    self._query_action()

  def _query_action(self):
    self._dbm._cursor.execute(self._queryEntry.get())
    result = self._dbm._cursor.fetchall()
    self._queryRes.delete(0.0, END)
    for item in result:
      self._queryRes.insert(END, str(item) + "\n")

  def _commit_action(self):
    self._dbm.commit()


# def init_book():
#   entry = ""
#   while entry.lower() != "quit":
#     entry = input("[SQL] ('quit' to exit):")
#     if entry.lower() == "quit":
#       break
#     else:
#       cursor.execute(entry)
#   connection.commit()
#   connection.quit()

if __name__ == "__main__":
  root = Tk()

  dbm = DatabaseManager()

  app = ReferenceBook(root, dbm)
  app.pack()

  print(dbm.get_creature_list())
  print(dbm.get_item_list())
  print(dbm.get_creature("Apprentice Rock Elementalist"))

  root.mainloop()
  book.close()