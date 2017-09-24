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

  # Selects specific columns from ALL rows from a given table.
  SELECT_ALL_ROWS_FILT_COLS = "SELECT {} FROM {}"
  # Selects ALL columns from specific rows from a given table.
  SELECT_FILT_ROWS_ALL_COLS = "SELECT * FROM {} WHERE {} == {}"
  # Selects specific columns from specific rows from a given table.
  SELECT_FILT_ROWS_COLS = "SELECT {} FROM {} WHERE {} == {}"

  # Format string for text surrounded by quotes (").
  QUOTED = "\"{}\""

  # Fields present in simple creature object.
  SIMPLE_CREATURE_FIELDS = ("name",
                            "img",
                            "hd")
  # Fields present in full creature object.
  FULL_CREATURE_FIELDS = ("name",
                          "img",
                          "description",
                          "notes",
                          "rarity",
                          "hd",
                          "hp",
                          "ac",
                          "xp",
                          "basicAttack")
  # References present in full creature object.
  FULL_CREATURE_REFS = {"Equips": ("equips",
                                   ("equipChance",
                                    "notes")),
                        "Drops": ("drops",
                                  ("dropChance",
                                   "notes")),
                        "CreatureAttacks": ("creatureAttacks")}

  # Fields present in the simple item object.
  SIMPLE_ITEM_FIELDS = ("name",
                        "img",
                        "type",
                        "value")
  # Fields present in the full item object.
  FULL_ITEM_FIELDS = ("name",
                      "img",
                      "type",
                      "value",
                      "description",
                      "notes",
                      "rarity")
  # Extra fields for the armor item object.
  ARMOR_FIELDS = ("ac",
                  "slot")
  # Extra fields for the weapon item object.
  WEAPON_FIELDS = ("dmg",
                   "crit",
                   "ammo",
                   "range",
                   "slot")
  # References present in the weapon item object.
  WEAPON_REFS = {"WeaponAttacks": "weaponAttacks"}
  # Extra fields for the consumable item object.
  CONSUMABLE_FIELDS = tuple(["effect"])

  # Fields present in the simple attack object.
  SIMPLE_ATTACK_FIELDS = ("id",
                          "name",
                          "img",
                          "isSpell")
  # Fields present in the full attack object.
  FULL_ATTACK_FIELDS = ("id",
                        "name",
                        "img",
                        "description",
                        "notes",
                        "dmg",
                        "isSpell")
  # Extra fields for the spell attack object.
  SPELL_FIELDS = tuple(["channel"])
  # References present in the spell attack object.
  SPELL_REFS = {"CastingCosts": "cost"}

  # Fields present in the simple location object.
  SIMPLE_LOCATION_FIELDS = ("name",
                            "img")
  # Fields present in the full location object.
  FULL_LOCATION_FIELDS = ("name",
                          "img",
                          "location",
                          "description",
                          "notes")
  # References present in the full location object.
  FULL_LOCATION_REFS = {"Inhabits": ("creatures",
                                     tuple(["notes"])),
                        "Stores": "stores"}

  # Fields present in the simple store object.
  SIMPLE_STORE_FIELDS = ("name",
                         "img")
  # Fields present in the full store object.
  FULL_STORE_FIELDS = ("name",
                       "img",
                       "location",
                       "description",
                       "notes")
  # References present in the full store object.
  FULL_STORE_REFS = {"Sells", ("sells",
                               ("qty",
                                "stockDays",
                                "price"))}

  def __init__(self, dbase = "dnd_ref_book.db"):
    self._dbase = dbase
    self._book = sqlite3.connect(dbase)

  ########
  # Wipes the saved database and starts from fresh run of `tables.sql`.
  # 
  # @warning This will delete all saved data. Make a backup if necessary beforehand.
  def reset(self):
    self._book.close()

    # in case screwed up, reset
    f = open(self._dbase, "w")
    f.close()
    self._book = sqlite3.connect(self._dbase)
    cursor = self._book.cursor()

    f = open("tables.sql")
    s = f.read()
    f.close()
    cursor.executescript(s)
    self.commit()

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
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.SIMPLE_CREATURE_FIELDS),
      "Creatures",
      "name",
      DatabaseManager.QUOTED.format(name)))
    if len(rawData) < 1: # no results
      raise IndexError("'{}' does not match any entries in '{}'.".format(name, self._dbase))
    
    toRet = {}
    for i in range(len(DatabaseManager.SIMPLE_CREATURE_FIELDS)):
      toRet[DatabaseManager.SIMPLE_CREATURE_FIELDS[i]] = rawData[0][i]
    return toRet

  ########
  # Obtains a full creature from the database, including references to other
  # objects.
  #
  # @param[in] name Name of the creature to be fetched.
  #
  # @return Full representation of creature.
  def get_creature(self, name):
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.FULL_CREATURE_FIELDS),
      "Creatures",
      "name",
      DatabaseManager.QUOTED.format(name)))
    if len(rawData) < 1: # no results
      raise IndexError("'{}' does not match any entries in '{}'.".format(name, self._dbase))
    
    toRet = {}
    for i in range(len(DatabaseManager.FULL_CREATURE_FIELDS)):
      toRet[DatabaseManager.FULL_CREATURE_FIELDS[i]] = rawData[0][i]

    # TODO: relation lookups

    return toRet

  ########
  # Obtains a list of all creatures in the database.
  #
  # @return List of simple creatures.
  def get_creature_list(self):
    rawData = self._fetch_raw(DatabaseManager.SELECT_ALL_ROWS_FILT_COLS.format(
      "name",
      "Creatures"))
    toRet = []
    for item in rawData:
      temp = self.get_simple_creature(item[0])
      toRet.append(temp)
    return toRet

  ########
  # Fetches a simple item from the database.
  #
  # @param[in] name Name of the item to be fetched.
  #
  # @return Simple representation of item.
  def get_simple_item(self, name):
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.SIMPLE_ITEM_FIELDS),
      "Items",
      "name",
      DatabaseManager.QUOTED.format(name)))
    if len(rawData) < 1: # no results
      raise IndexError("'{}' does not match any entries in '{}'.".format(name, self._dbase))
    
    toRet = {}
    for i in range(len(DatabaseManager.SIMPLE_ITEM_FIELDS)):
      toRet[DatabaseManager.SIMPLE_ITEM_FIELDS[i]] = rawData[0][i]
    return toRet

  ########
  # Obtains a full item from the database, including references to other
  # objects.
  #
  # @param[in] name Name of the item to be fetched.
  #
  # @return Full representation of item.
  def get_item(self, name):
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.FULL_ITEM_FIELDS),
      "Items",
      "name",
      DatabaseManager.QUOTED.format(name)))
    if len(rawData) < 1: # no results
      raise IndexError("'{}' does not match any entries in '{}'.".format(name, self._dbase))
    
    toRet = {}
    for i in range(len(DatabaseManager.FULL_ITEM_FIELDS)):
      toRet[DatabaseManager.FULL_ITEM_FIELDS[i]] = rawData[0][i]

    # TODO: relation lookups

    return toRet

  ########
  # Obtains a list of all items in the database.
  #
  # @return List of simple items.
  def get_item_list(self):
    rawData = self._fetch_raw(DatabaseManager.SELECT_ALL_ROWS_FILT_COLS.format(
      "name",
      "Items"))
    toRet = []
    for item in rawData:
      temp = self.get_simple_item(item[0])
      toRet.append(temp)
    return toRet

  ########
  # Fetches a simple attack from the database.
  #
  # @param[in] idNum ID of the attack to be fetched.
  #
  # @return Simple representation of attack.
  def get_simple_attack(self, idNum):
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.SIMPLE_ATTACK_FIELDS),
      "SpecialAttacks",
      "id",
      DatabaseManager.QUOTED.format(idNum)))
    if len(rawData) < 1: # no results
      raise IndexError("'{}' does not match any entries in '{}'.".format(idNum, self._dbase))
    
    toRet = {}
    for i in range(len(DatabaseManager.SIMPLE_ATTACK_FIELDS)):
      toRet[DatabaseManager.SIMPLE_ATTACK_FIELDS[i]] = rawData[0][i]
    return toRet

  ########
  # Obtains a full attack from the database, including references to other
  # objects.
  #
  # @param[in] idNum ID of the attack to be fetched.
  #
  # @return Full representation of attack.
  def get_attack(self, idNum):
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.FULL_ATTACK_FIELDS),
      "SpecialAttacks",
      "id",
      DatabaseManager.QUOTED.format(idNum)))
    if len(rawData) < 1: # no results
      raise IndexError("'{}' does not match any entries in '{}'.".format(name, self._dbase))
    
    toRet = {}
    for i in range(len(DatabaseManager.FULL_ATTACK_FIELDS)):
      toRet[DatabaseManager.FULL_ATTACK_FIELDS[i]] = rawData[0][i]

    # TODO: relation lookups

    return toRet

  ########
  # Obtains a list of all attacks in the database.
  #
  # @return List of simple attacks.
  def get_attack_list(self):
    rawData = self._fetch_raw(DatabaseManager.SELECT_ALL_ROWS_FILT_COLS.format(
      "id",
      "SpecialAttacks"))
    toRet = []
    for item in rawData:
      temp = self.get_simple_attack(item[0])
      toRet.append(temp)
    return toRet

  ########
  # Fetches a simple location from the database.
  #
  # @param[in] name Name of the location to be fetched.
  #
  # @return Simple representation of location.
  def get_simple_location(self, name):
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.SIMPLE_LOCATION_FIELDS),
      "Locations",
      "name",
      DatabaseManager.QUOTED.format(name)))
    if len(rawData) < 1: # no results
      raise IndexError("'{}' does not match any entries in '{}'.".format(name, self._dbase))
    
    toRet = {}
    for i in range(len(DatabaseManager.SIMPLE_LOCATION_FIELDS)):
      toRet[DatabaseManager.SIMPLE_LOCATION_FIELDS[i]] = rawData[0][i]
    return toRet

  ########
  # Obtains a full location from the database, including references to other
  # objects.
  #
  # @param[in] name Name of the location to be fetched.
  #
  # @return Full representation of location.
  def get_location(self, name):
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.FULL_LOCATION_FIELDS),
      "Locations",
      "name",
      DatabaseManager.QUOTED.format(name)))
    if len(rawData) < 1: # no results
      raise IndexError("'{}' does not match any entries in '{}'.".format(name, self._dbase))
    
    toRet = {}
    for i in range(len(DatabaseManager.FULL_LOCATION_FIELDS)):
      toRet[DatabaseManager.FULL_LOCATION_FIELDS[i]] = rawData[0][i]

    # TODO: relation lookups

    return toRet

  ########
  # Obtains a list of all locations in the database.
  #
  # @return List of simple locations.
  def get_location_list(self):
    rawData = self._fetch_raw(DatabaseManager.SELECT_ALL_ROWS_FILT_COLS.format(
      "name",
      "Locations"))
    toRet = []
    for item in rawData:
      temp = self.get_simple_location(item[0])
      toRet.append(temp)
    return toRet

  ########
  # Fetches a simple store from the database.
  #
  # @param[in] name Name of the store to be fetched.
  # @param[in] location Location of the store to be fetched.
  #
  # @return Simple representation of store.
  def get_simple_store(self, name, location):
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.SIMPLE_STORE_FIELDS),
      "Stores",
      "(name,location)",
      "({},{})".format(
        DatabaseManager.QUOTED.format(name),
        DatabaseManager.QUOTED.format(location))))
    if len(rawData) < 1: # no results
      raise IndexError("'{}' does not match any entries in '{}'.".format(name, self._dbase))

    toRet = {}
    for i in range(len(DatabaseManager.SIMPLE_STORE_FIELDS)):
      toRet[DatabaseManager.SIMPLE_STORE_FIELDS[i]] = rawData[0][i]
    return toRet

  ########
  # Obtains a full store from the database, including references to other
  # objects.
  #
  # @param[in] name Name of the store to be fetched.
  # @param[in] location Location of the store to be fetched
  #
  # @return Full representation of store.
  def get_store(self, name, location):
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.FULL_STORE_FIELDS),
      "Stores",
      "(name,location)",
      "({},{})".format(
        DatabaseManager.QUOTED.format(name),
        DatabaseManager.QUOTED.format(location))))
    if len(rawData) < 1: # no results
      raise IndexError("'{}' does not match any entries in '{}'.".format(name, self._dbase))
    
    toRet = {}
    for i in range(len(DatabaseManager.FULL_STORE_FIELDS)):
      toRet[DatabaseManager.FULL_STORE_FIELDS[i]] = rawData[0][i]

    # TODO: relation lookups

    return toRet

  ########
  # Obtains a list of all stores in the database.
  #
  # @return List of simple stores.
  def get_store_list(self):
    rawData = self._fetch_raw(DatabaseManager.SELECT_ALL_ROWS_FILT_COLS.format(
      "(name,location)",
      "Stores"))
    toRet = []
    for item in rawData:
      temp = self.get_simple_store(item[0], item[1])
      toRet.append(temp)
    return toRet

#######################
if __name__ == "__main__":
  import json

  dbm = DatabaseManager()
  dbm.reset()
  allCreatures = dbm.get_creature_list()

  print("Creatures:")
  print(json.dumps(allCreatures, indent=2, sort_keys=True))
  print("Full creature:")
  print(json.dumps(dbm.get_creature(allCreatures[0]["name"]), indent=2, sort_keys=True))

  print("\n\n\nItems:")
  allItems = dbm.get_item_list()
  print(json.dumps(allItems, indent=2, sort_keys=True))
  print("Full item:")
  print(json.dumps(dbm.get_item(allItems[0]["name"]), indent=2, sort_keys=True))

  print("\n\n\nAttacks:")
  allAttacks = dbm.get_attack_list()
  print(json.dumps(allAttacks, indent=2, sort_keys=True))
  print("Full attack:")
  print(json.dumps(dbm.get_attack(allAttacks[0]["id"]), indent=2, sort_keys=True))

  dbm._book.close()