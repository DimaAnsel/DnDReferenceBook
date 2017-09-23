################################
# dbase_manager.py
# Noah Ansel
# 2017-09-23
# ------------------------------
# Python class that handles querying and modifying the database.
# Queries are returned packaged into the formats specified in formats.md.
################################

import sqlite3

class DatabaseManager:

  SELECT_ALL_ROWS_FILT_COLS = "SELECT {} FROM {}"
  SELECT_FILT_ROWS_ALL_COLS = "SELECT * FROM {} WHERE {} == {}"

  SELECT_FILT_ROWS_COLS = "SELECT {} FROM {} WHERE {} == {}"

  CREATURE_MAP = ("name", "description", "notes", "img", "rarity", "hd", "hp", "ac", "xp", "basicAttack")
  CREATURE_REFS = {"Equips":"equips", "Drops":"drops", "CreatureAttacks":"creatureAttacks"}

  ITEM_MAP = ("name", "description", "notes", "img", "rarity")

  def __init__(self, dbase = "dnd_ref_book.db"):
    self._dbase = dbase
    self._book = sqlite3.connect(dbase)

  def reset(self):
    self._book.close()

    # in case screwed up, reset
    f = open(self._dbase, "w")
    f.close()
    self._book = sqlite3.connect(self._dbase)
    self._cursor = book.cursor()

    f = open("tables.sql")
    s = f.read()
    f.close()
    self._cursor.executescript(s)
    self._book.commit()

  def commit(self):
    self._book.commit()

  ########
  # Helper function to get results for a database query.
  # 
  # @param[in] command SELECT command to be executed
  #
  # @return Raw results of the command as an N-tuple of N-tuples
  def _fetch_raw(self, command):
    cursor = self._book.cursor()
    cursor.execute(command)
    toRet = cursor.fetchall()
    return toRet

  ########
  # Fetches a simple creature from the database.
  #
  # @param[in] name Name of the creature to be fetched.
  #
  # @return Simple representation of creature.
  def get_simple_creature(self, name):
    pass

  ########
  # Obtains a full creature from the database, including references to other
  # objects.
  #
  # @param[in] name Name of the creature to be fetched.
  #
  # @return Full representation of creature.
  def get_creature(self, name):
    pass

  ########
  # Obtains a list of all creatures in the database.
  #
  # @return List of simple creatures.
  def get_creature_list(self):
    pass

  ########
  # Fetches a simple item from the database.
  #
  # @param[in] name Name of the item to be fetched.
  #
  # @return Simple representation of item.
  def get_simple_item(self, name):
    pass

  ########
  # Obtains a full item from the database, including references to other
  # objects.
  #
  # @param[in] name Name of the item to be fetched.
  #
  # @return Full representation of item.
  def get_item(self, name):
    pass

  ########
  # Obtains a list of all items in the database.
  #
  # @return List of simple items.
  def get_item_list(self):
    pass

  ########
  # Fetches a simple attack from the database.
  #
  # @param[in] id ID of the attack to be fetched.
  #
  # @return Simple representation of attack.
  def get_simple_attack(self, id):
    pass

  ########
  # Obtains a full attack from the database, including references to other
  # objects.
  #
  # @param[in] id ID of the attack to be fetched.
  #
  # @return Full representation of attack.
  def get_attack(self, id):
    pass

  ########
  # Obtains a list of all attacks in the database.
  #
  # @return List of simple attacks.
  def get_attack_list(self):
    pass

  ########
  # Fetches a simple location from the database.
  #
  # @param[in] name Name of the location to be fetched.
  #
  # @return Simple representation of location.
  def get_simple_location(self, name):
    pass

  ########
  # Obtains a full location from the database, including references to other
  # objects.
  #
  # @param[in] name Name of the location to be fetched.
  #
  # @return Full representation of location.
  def get_location(self, name):
    pass

  ########
  # Obtains a list of all locations in the database.
  #
  # @return List of simple locations.
  def get_location_list(self):
    pass

  ########
  # Fetches a simple store from the database.
  #
  # @param[in] name Name of the store to be fetched.
  #
  # @return Simple representation of store.
  def get_simple_store(self, name):
    pass

  ########
  # Obtains a full store from the database, including references to other
  # objects.
  #
  # @param[in] name Name of the store to be fetched.
  #
  # @return Full representation of store.
  def get_store(self, name):
    pass

  ########
  # Obtains a list of all stores in the database.
  #
  # @return List of simple stores.
  def get_store_list(self):
    pass