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
  # Selects specific columns from specific rows from a given table. More generic
  # than SELECT_FILT_ROWS_COLS
  SELECT_FILT_ROWS_COLS_SPECIAL = "SELECT {} FROM {} WHERE {}"
  # Equals filter.
  FILT_EQUALS = "{} == {}"
  # And filter used in join commands.
  FILT_AND = " AND "

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
  # Fields present in equipment field of full creature object.
  CREATURE_EQUIPS_FIELDS = ("item",
                            "equipChance",
                            "notes")
  # Fields present in drops field of full creature object.
  CREATURE_DROPS_FIELDS = ("item",
                           "dropChance",
                           "notes")
  # Fields present in inhabits field of full creature object.
  CREATURE_INHABITS_FIELDS = ("location",
                              "notes")


  # Item type value marking consumables.
  ITEM_TYPE_CONSUMABLE = 1
  # Item type value marking armor.
  ITEM_TYPE_ARMOR = 2
  # Item type value marking weapons.
  ITEM_TYPE_WEAPON = 3
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
  # Fields present in equippedBy field of full item object.
  ITEM_EQUIPS_FIELDS = ("creature",
                        "equipChance",
                        "notes")
  # Fields present in droppedBy field of full item object.
  ITEM_DROPS_FIELDS = ("creature",
                       "dropChance",
                       "notes")
  # Fields present in spellCost field of full item object.
  ITEM_CASTINGCOST_FIELDS = ("spellId",
                             "qty")
  # Fields present in soldAt field of full item object.
  ITEM_SELLS_FIELDS = ("store",
                       "location",
                       "qty",
                       "stockDays",
                       "price")
  # Extra fields for the armor item object.
  ARMOR_FIELDS = ("ac",
                  "slot")
  # Extra fields for the weapon item object.
  WEAPON_FIELDS = ("dmg",
                   "crit",
                   "ammo",
                   "range",
                   "slot")
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
  # Fields present in the costs field of the spell attack object.
  SPELL_CASTINGCOST_FIELDS = ("item",
                              "qty")


  # Fields present in the simple location object.
  SIMPLE_LOCATION_FIELDS = ("name",
                            "img")
  # Fields present in the full location object.
  FULL_LOCATION_FIELDS = ("name",
                          "img",
                          "description",
                          "notes")
  # Fields present in the creatures field of the full location object.
  LOCATION_INHABITS_FIELDS = ("creature",
                              "notes")


  # Fields present in the simple store object.
  SIMPLE_STORE_FIELDS = ("name",
                         "location",
                         "img")
  # Fields present in the full store object.
  FULL_STORE_FIELDS = ("name",
                       "img",
                       "location",
                       "description",
                       "notes")
  # Fields present in the sells field of the full store object.
  STORE_SELLS_FIELDS = ("item",
                        "qty",
                        "stockDays",
                        "price")

  ########
  # Initializes the manager and opens the connection to the database.
  #
  # @param[in] dbase File name/path this manager will query and modify.
  # @param[in] filepathPrefix Filepath to prepend to returned filenames (images).
  #                           Allows initializing from separate directories.
  def __init__(self, dbase = "dnd_ref_book.db", filepathPrefix = ""):
    self._dbase = dbase
    self._book = sqlite3.connect(dbase)
    self._filepathPrefix = filepathPrefix

  ########
  # Wipes the saved database and starts from fresh run of tables and
  # initial SQL files.
  # 
  # @warning This will delete all saved data. Make a backup if necessary beforehand.
  def reset(self, tables = "tables.sql", initial = None):
    self._book.close()

    # in case screwed up, reset
    f = open(self._dbase, "w")
    f.close()
    self._book = sqlite3.connect(self._dbase)
    cursor = self._book.cursor()

    f = open(tables)
    s = f.read()
    f.close()
    cursor.executescript(s)

    if initial != None:
      f = open(initial)
      s = f.read()
      f.close()
      cursor.executescript(s)

    self.commit()

  ########
  # Commits all changes to the database. This must be called before closing the
  # manager or ending the program in order to preserve changes.
  def commit(self):
    self._book.commit()

  ########
  # Closes the connection to the database. Should only be called during cleanup.
  def close(self):
    self._book.close()

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
    if toRet["img"] != None:
      toRet["img"] = self._filepathPrefix + toRet["img"]
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

    # Equips
    toRet["equips"] = []
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.CREATURE_EQUIPS_FIELDS),
      "Equips",
      "creature",
      DatabaseManager.QUOTED.format(name)))
    for item in rawData:
      temp = {"item": self.get_simple_item(item[0])}
      for i in range(1, len(DatabaseManager.CREATURE_EQUIPS_FIELDS)):
        temp[DatabaseManager.CREATURE_EQUIPS_FIELDS[i]] = item[i]
      toRet["equips"].append(temp)

    # Drops
    toRet["drops"] = []
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.CREATURE_DROPS_FIELDS),
      "Drops",
      "creature",
      DatabaseManager.QUOTED.format(name)))
    for item in rawData:
      temp = {"item": self.get_simple_item(item[0])}
      for i in range(1, len(DatabaseManager.CREATURE_DROPS_FIELDS)):
        temp[DatabaseManager.CREATURE_DROPS_FIELDS[i]] = item[i]
      toRet["drops"].append(temp)

    # Attacks
    toRet["attacks"] = []
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      "attackId",
      "CreatureAttacks",
      "creature",
      DatabaseManager.QUOTED.format(name)))
    for item in rawData:
      toRet["attacks"].append(self.get_simple_attack(item[0]))
      
    # Inhabits
    toRet["inhabits"] = []
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.CREATURE_INHABITS_FIELDS),
      "Inhabits",
      "creature",
      DatabaseManager.QUOTED.format(name)))
    for item in rawData:
      temp = {"location": self.get_simple_location(item[0])}
      for i in range(1, len(DatabaseManager.CREATURE_INHABITS_FIELDS)):
        temp[DatabaseManager.CREATURE_INHABITS_FIELDS[i]] = item[i]
      toRet["inhabits"].append(temp)

    if toRet["img"] != None:
      toRet["img"] = self._filepathPrefix + toRet["img"]
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

    if toRet["img"] != None:
      toRet["img"] = self._filepathPrefix + toRet["img"]
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

    # Consumable type
    if toRet["type"] == DatabaseManager.ITEM_TYPE_CONSUMABLE:
      rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
        ",".join(DatabaseManager.CONSUMABLE_FIELDS),
        "Consumables",
        "name",
        DatabaseManager.QUOTED.format(name)))
      for i in range(len(DatabaseManager.CONSUMABLE_FIELDS)):
        toRet[DatabaseManager.CONSUMABLE_FIELDS[i]] = rawData[0][i]

    # Armor type
    elif toRet["type"] == DatabaseManager.ITEM_TYPE_ARMOR:
      rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
        ",".join(DatabaseManager.ARMOR_FIELDS),
        "Armor",
        "name",
        DatabaseManager.QUOTED.format(name)))
      for i in range(len(DatabaseManager.ARMOR_FIELDS)):
        toRet[DatabaseManager.ARMOR_FIELDS[i]] = rawData[0][i]

    # Weapon type
    elif toRet["type"] == DatabaseManager.ITEM_TYPE_WEAPON:
      rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
        ",".join(DatabaseManager.WEAPON_FIELDS),
        "Weapons",
        "name",
        DatabaseManager.QUOTED.format(name)))
      for i in range(len(DatabaseManager.WEAPON_FIELDS)):
        toRet[DatabaseManager.WEAPON_FIELDS[i]] = rawData[0][i]
      # Ammunition
      if toRet["ammo"] != None:
        toRet["ammo"] = self.get_simple_item(toRet["ammo"])
      # Attacks
      toRet["attacks"] = []
      rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
        "attackId",
        "WeaponAttacks",
        "item",
        DatabaseManager.QUOTED.format(name)))
      for item in rawData:
        toRet["attacks"].append(self.get_simple_attack(item[0]))

    # Equips
    toRet["equippedBy"] = []
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.ITEM_EQUIPS_FIELDS),
      "Equips",
      "item",
      DatabaseManager.QUOTED.format(name)))
    for item in rawData:
      temp = {"creature": self.get_simple_creature(item[0])}
      for i in range(1, len(DatabaseManager.ITEM_EQUIPS_FIELDS)):
        temp[DatabaseManager.ITEM_EQUIPS_FIELDS[i]] = item[i]
      toRet["equippedBy"].append(temp)

    # Drops
    toRet["droppedBy"] = []
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.ITEM_DROPS_FIELDS),
      "Drops",
      "item",
      DatabaseManager.QUOTED.format(name)))
    for item in rawData:
      temp = {"creature": self.get_simple_creature(item[0])}
      for i in range(1, len(DatabaseManager.ITEM_DROPS_FIELDS)):
        temp[DatabaseManager.ITEM_DROPS_FIELDS[i]] = item[i]
      toRet["droppedBy"].append(temp)

    # Ammo
    toRet["ammoFor"] = []
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      "name",
      "Weapons",
      "ammo",
      DatabaseManager.QUOTED.format(name)))
    for item in rawData:
      toRet["ammoFor"].append(self.get_simple_item(item[0]))

    # Spells
    toRet["spellCost"] = []
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.ITEM_CASTINGCOST_FIELDS),
      "CastingCosts",
      "item",
      DatabaseManager.QUOTED.format(name)))
    for item in rawData:
      temp = {"spell": self.get_simple_attack(item[0])}
      for i in range(1, len(DatabaseManager.ITEM_CASTINGCOST_FIELDS)):
        temp[DatabaseManager.ITEM_CASTINGCOST_FIELDS[i]] = item[i]
      toRet["spellCost"].append(temp)

    # Stores
    toRet["soldAt"] = []
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.ITEM_SELLS_FIELDS),
      "Sells",
      "item",
      DatabaseManager.QUOTED.format(name)))
    for item in rawData:
      temp = {"store": self.get_simple_store(item[0], item[1])}
      for i in range(2, len(DatabaseManager.ITEM_SELLS_FIELDS)):
        temp[DatabaseManager.ITEM_SELLS_FIELDS[i]] = item[i]
      toRet["soldAt"].append(temp)

    if toRet["img"] != None:
      toRet["img"] = self._filepathPrefix + toRet["img"]
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
      idNum))
    if len(rawData) < 1: # no results
      raise IndexError("'{}' does not match any entries in '{}'.".format(idNum, self._dbase))
    
    toRet = {}
    for i in range(len(DatabaseManager.SIMPLE_ATTACK_FIELDS)):
      toRet[DatabaseManager.SIMPLE_ATTACK_FIELDS[i]] = rawData[0][i]

    if toRet["img"] != None:
      toRet["img"] = self._filepathPrefix + toRet["img"]
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
      idNum))
    if len(rawData) < 1: # no results
      raise IndexError("'{}' does not match any entries in '{}'.".format(idNum, self._dbase))
    
    toRet = {}
    for i in range(len(DatabaseManager.FULL_ATTACK_FIELDS)):
      toRet[DatabaseManager.FULL_ATTACK_FIELDS[i]] = rawData[0][i]

    if toRet["isSpell"] == 1:
      rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
        ",".join(DatabaseManager.SPELL_FIELDS),
        "Spells",
        "id",
        idNum))

      for i in range(len(DatabaseManager.SPELL_FIELDS)):
        toRet[DatabaseManager.SPELL_FIELDS[i]] = rawData[0][i]
      # Costs
      toRet["costs"] = []
      rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
        ",".join(DatabaseManager.SPELL_CASTINGCOST_FIELDS),
        "CastingCosts",
        "spellId",
        idNum))
      for item in rawData:
        temp = {"item": self.get_simple_item(item[0])}
        for i in range(1, len(DatabaseManager.SPELL_CASTINGCOST_FIELDS)):
          temp[DatabaseManager.SPELL_CASTINGCOST_FIELDS[i]] = item[i]
        toRet["costs"].append(temp)

    # Creatures
    toRet["creatures"] = []
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      "creature",
      "CreatureAttacks",
      "attackId",
      idNum))
    for item in rawData:
      toRet["creatures"].append(self.get_simple_creature(item[0]))

    # Weapons
    toRet["weapons"] = []
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      "item",
      "WeaponAttacks",
      "attackId",
      idNum))
    for item in rawData:
      toRet["weapons"].append(self.get_simple_item(item[0]))

    if toRet["img"] != None:
      toRet["img"] = self._filepathPrefix + toRet["img"]
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

    if toRet["img"] != None:
      toRet["img"] = self._filepathPrefix + toRet["img"]
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

    # Creatures
    toRet["creatures"] = []
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      ",".join(DatabaseManager.LOCATION_INHABITS_FIELDS),
      "Inhabits",
      "location",
      DatabaseManager.QUOTED.format(name)))
    for item in rawData:
      temp = {"creature": self.get_simple_creature(item[0])}
      for i in range(1, len(DatabaseManager.LOCATION_INHABITS_FIELDS)):
        temp[DatabaseManager.LOCATION_INHABITS_FIELDS[i]] = item[i]
      toRet["creatures"].append(temp)

    # Stores
    toRet["stores"] = []
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS.format(
      "name",
      "Stores",
      "location",
      DatabaseManager.QUOTED.format(name)))
    for item in rawData:
      toRet["stores"].append(self.get_simple_store(item[0], name))

    if toRet["img"] != None:
      toRet["img"] = self._filepathPrefix + toRet["img"]
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
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS_SPECIAL.format(
      ",".join(DatabaseManager.SIMPLE_STORE_FIELDS),
      "Stores",
      DatabaseManager.FILT_AND.join([
        DatabaseManager.FILT_EQUALS.format(
          "name", DatabaseManager.QUOTED.format(name)),
        DatabaseManager.FILT_EQUALS.format(
          "location", DatabaseManager.QUOTED.format(location))])))
    if len(rawData) < 1: # no results
      raise IndexError("'{}' does not match any entries in '{}'.".format(name, self._dbase))

    toRet = {}
    for i in range(len(DatabaseManager.SIMPLE_STORE_FIELDS)):
      toRet[DatabaseManager.SIMPLE_STORE_FIELDS[i]] = rawData[0][i]

    if toRet["img"] != None:
      toRet["img"] = self._filepathPrefix + toRet["img"]
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
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS_SPECIAL.format(
      ",".join(DatabaseManager.FULL_STORE_FIELDS),
      "Stores",
      DatabaseManager.FILT_AND.join([
        DatabaseManager.FILT_EQUALS.format(
          "name", DatabaseManager.QUOTED.format(name)),
        DatabaseManager.FILT_EQUALS.format(
          "location", DatabaseManager.QUOTED.format(location))])))
    if len(rawData) < 1: # no results
      raise IndexError("'{}' does not match any entries in '{}'.".format(name, self._dbase))
    
    toRet = {}
    for i in range(len(DatabaseManager.FULL_STORE_FIELDS)):
      toRet[DatabaseManager.FULL_STORE_FIELDS[i]] = rawData[0][i]
    
    toRet["location"] = self.get_simple_location(toRet["location"])

    # Sells
    toRet["sells"] = []
    rawData = self._fetch_raw(DatabaseManager.SELECT_FILT_ROWS_COLS_SPECIAL.format(
      ",".join(DatabaseManager.STORE_SELLS_FIELDS),
      "Sells",
      DatabaseManager.FILT_AND.join([
        DatabaseManager.FILT_EQUALS.format(
          "store", DatabaseManager.QUOTED.format(name)),
        DatabaseManager.FILT_EQUALS.format(
          "location", DatabaseManager.QUOTED.format(location))])))
    for item in rawData:
      temp = {"item": self.get_simple_item(item[0])}
      for i in range(1, len(DatabaseManager.STORE_SELLS_FIELDS)):
        temp[DatabaseManager.STORE_SELLS_FIELDS[i]] = item[i]
      toRet["sells"].append(temp)

    if toRet["img"] != None:
      toRet["img"] = self._filepathPrefix + toRet["img"]
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
  dbm.reset(initial = "real.sql")
  allCreatures = dbm.get_creature_list()

  # print("Creatures:")
  # print(json.dumps(allCreatures, indent=2, sort_keys=True))
  print("Full creature:")
  print(json.dumps(dbm.get_creature(allCreatures[0]["name"]), indent=2, sort_keys=True))

  # print("\n\n\nItems:")
  # allItems = dbm.get_item_list()
  # print(json.dumps(allItems, indent=2, sort_keys=True))
  # for item in allItems:
  #   print("Full item:")
  #   print(json.dumps(dbm.get_item(item["name"]), indent=2, sort_keys=True))

  # print("\n\n\nAttacks:")
  # allAttacks = dbm.get_attack_list()
  # print(json.dumps(allAttacks, indent=2, sort_keys=True))
  # for attack in allAttacks:
  #   print("Full attack:")
  #   print(json.dumps(dbm.get_attack(attack["id"]), indent=2, sort_keys=True))

  dbm._book.close()