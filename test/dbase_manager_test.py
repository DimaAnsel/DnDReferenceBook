################################
# dbase_manager_test.py
# Noah Ansel
# 2017-09-24
# ------------------------------
# Tests functionality of DatabaseManager against formats defined in formats.md.
################################

import unittest
from DnDReferenceBook.src.dbase_manager import DatabaseManager

class TestDatabaseManagerMethods(unittest.TestCase):
  
  def setUp(self):
    self._dbm = DatabaseManager("test.db")

  def tearDown(self):
    self._dbm.close()

  ########
  # Verifies functionality of get_simple_creature with non-null values.
  def test_simple_creature_non_null(self):
    res = self._dbm.get_simple_creature("creature 1")
    self.assertEqual(3, len(res.keys()))
    self.assertEqual(res["name"], "creature 1")
    self.assertEqual(res["img"], "creature 1.jpg")
    self.assertEqual(res["hd"], 4)

  ########
  # Verifies functionality of get_simple_creature with null valeus.
  def test_simple_creature_null(self):
    res = self._dbm.get_simple_creature("creature 4")
    self.assertEqual(3, len(res.keys()))
    self.assertEqual(res["name"], "creature 4")
    self.assertEqual(res["img"], None)
    self.assertEqual(res["hd"], None)

  ########
  # Verifies functionality of get_simple_item with non-null values.
  def test_simple_item_non_null(self):
    res = self._dbm.get_simple_item("item 1")
    self.assertEqual(4, len(res.keys()))
    self.assertEqual(res["name"], "item 1")
    self.assertEqual(res["img"], "item 1.tiff")
    self.assertEqual(res["type"], 0)
    self.assertEqual(res["value"], "10g,4s")

  ########
  # Verifies functionality of get_simple_item with null values.
  def test_simple_item_null(self):
    res = self._dbm.get_simple_item("item 7")
    self.assertEqual(4, len(res.keys()))
    self.assertEqual(res["name"], "item 7")
    self.assertEqual(res["img"], None)
    self.assertEqual(res["type"], 2)
    self.assertEqual(res["value"], None)

  ########
  # Verifies functionality of get_simple_attack with non-null values.
  def test_simple_attack_non_null(self):
    res = self._dbm.get_simple_attack(0)
    self.assertEqual(4, len(res.keys()))
    self.assertEqual(res["id"], 0)
    self.assertEqual(res["name"], "attack 1")
    self.assertEqual(res["img"], "attack 1_a.gif")
    self.assertEqual(res["isSpell"], 0)

    res = self._dbm.get_simple_attack(1)
    self.assertEqual(4, len(res.keys()))
    self.assertEqual(res["id"], 1)
    self.assertEqual(res["name"], "attack 1")
    self.assertEqual(res["img"], "attack 1_b.png")
    self.assertEqual(res["isSpell"], 1)

  ########
  # Verifies functionality of get_simple_attack with null values.
  def test_simple_attack_null(self):
    res = self._dbm.get_simple_attack(3)
    self.assertEqual(4, len(res.keys()))
    self.assertEqual(res["id"], 3)
    self.assertEqual(res["name"], "attack 3")
    self.assertEqual(res["img"], None)
    self.assertEqual(res["isSpell"], 1)

    res = self._dbm.get_simple_attack(4)
    self.assertEqual(4, len(res.keys()))
    self.assertEqual(res["id"], 4)
    self.assertEqual(res["name"], "attack 4")
    self.assertEqual(res["img"], None)
    self.assertEqual(res["isSpell"], 0)

  ########
  # Verifies functionality of get_simple_location with non-null values.
  def test_simple_location_non_null(self):
    res = self._dbm.get_simple_location("location 2")
    self.assertEqual(2, len(res.keys()))
    self.assertEqual(res["name"], "location 2")
    self.assertEqual(res["img"], "location 2.gif")

  ########
  # Verifies functionality of get_simple_location with null valeus.
  def test_simple_location_null(self):
    res = self._dbm.get_simple_location("location 3")
    self.assertEqual(2, len(res.keys()))
    self.assertEqual(res["name"], "location 3")
    self.assertEqual(res["img"], None)

  ########
  # Verifies functionality of get_simple_store with non-null values.
  def test_simple_store_non_null(self):
    res = self._dbm.get_simple_store("store 1", "location 2")
    self.assertEqual(3, len(res.keys()))
    self.assertEqual(res["name"], "store 1")
    self.assertEqual(res["location"], "location 2")
    self.assertEqual(res["img"], "store 1.gif")

    res = self._dbm.get_simple_store("store 1", "location 1")
    self.assertEqual(3, len(res.keys()))
    self.assertEqual(res["name"], "store 1")
    self.assertEqual(res["location"], "location 1")
    self.assertEqual(res["img"], None)

  ########
  # Verifies functionality of get_simple_store with null values.
  def test_simple_store_null(self):
    res = self._dbm.get_simple_store("store 2", "location 2")
    self.assertEqual(3, len(res.keys()))
    self.assertEqual(res["name"], "store 2")
    self.assertEqual(res["location"], "location 2")
    self.assertEqual(res["img"], None)

    res = self._dbm.get_simple_store("store 2", "location 3")
    self.assertEqual(3, len(res.keys()))
    self.assertEqual(res["name"], "store 2")
    self.assertEqual(res["location"], "location 3")
    self.assertEqual(res["img"], None)

  ########
  # Verifies functionality of get_creature with non-null values.
  def test_full_creature_non_null(self):
    # main values
    res = self._dbm.get_creature("creature 1")
    self.assertEqual(len(DatabaseManager.FULL_CREATURE_FIELDS) + 4, len(res.keys()))
    self.assertEqual(res["name"], "creature 1")
    self.assertEqual(res["img"], "creature 1.jpg")
    self.assertEqual(res["description"], "creature 1 description")
    self.assertEqual(res["notes"], "creature 1 notes")
    self.assertEqual(res["rarity"], 1)
    self.assertEqual(res["hd"], 4)
    self.assertEqual(res["hp"], "15 + [1d6]")
    self.assertEqual(res["ac"], 7)
    self.assertEqual(res["xp"], 80)
    self.assertEqual(res["basicAttack"], "Punch: [1d8]")

    # equips values
    self.assertEqual(1, len(res["equips"]))
    self.assertEqual(3, len(res["equips"][0].keys()))
    self.assertEqual(res["equips"][0]["item"]["name"], "item 3")
    self.assertEqual(res["equips"][0]["equipChance"], "[2+] on [1d8]")
    self.assertEqual(res["equips"][0]["notes"], "equipment 2 notes")

    self.assertEqual(0, len(res["drops"]))
    self.assertEqual(3, len(res["attacks"]))
    self.assertEqual(4, len(res["attacks"][0].keys()))
    self.assertEqual(2, len(res["inhabits"]))
    self.assertEqual(2, len(res["inhabits"][0].keys()))

    # drops values
    res = self._dbm.get_creature("creature 2")
    self.assertEqual(1, len(res["drops"]))
    self.assertEqual(3, len(res["drops"][0].keys()))
    self.assertEqual(res["drops"][0]["item"]["name"], "item 2")
    self.assertEqual(res["drops"][0]["dropChance"], "[2+] on [1d10]")
    self.assertEqual(res["drops"][0]["notes"], "drop 2 notes")

    # attacks values
    self.assertEqual(1, len(res["attacks"]))
    self.assertEqual(res["attacks"][0]["id"], 0)

    # inhabits values
    self.assertEqual(1, len(res["inhabits"]))
    self.assertEqual(2, len(res["inhabits"][0].keys()))
    self.assertEqual(res["inhabits"][0]["location"]["name"], "location 3")
    self.assertEqual(res["inhabits"][0]["notes"], "inhabit 2 notes")

  ########
  # Verifies functionality of get_creature with null values.
  def test_full_creature_null(self):
    res = self._dbm.get_creature("creature 4")
    self.assertEqual(len(DatabaseManager.FULL_CREATURE_FIELDS) + 4, len(res.keys()))
    self.assertEqual(res["name"], "creature 4")
    self.assertEqual(res["img"], None)
    self.assertEqual(res["description"], None)
    self.assertEqual(res["notes"], None)
    self.assertEqual(res["rarity"], None)
    self.assertEqual(res["hd"], None)
    self.assertEqual(res["hp"], None)
    self.assertEqual(res["ac"], None)
    self.assertEqual(res["xp"], None)
    self.assertEqual(res["basicAttack"], None)

    self.assertEqual(0, len(res["equips"]))
    self.assertEqual(1, len(res["drops"]))
    self.assertEqual(3, len(res["drops"][0].keys()))
    self.assertEqual(res["drops"][0]["item"]["name"], "item 6")
    self.assertEqual(res["drops"][0]["dropChance"], None)
    self.assertEqual(res["drops"][0]["notes"], None)  
    self.assertEqual(0, len(res["attacks"]))
    self.assertEqual(0, len(res["inhabits"]))

  ########
  # Verifies functionality of get_item with non-null values.
  def test_full_item_non_null(self):
    res = self._dbm.get_item("item 1")
    self.assertEqual(len(DatabaseManager.FULL_ITEM_FIELDS) + 5, len(res.keys()))
    self.assertEqual(res["name"], "item 1")
    self.assertEqual(res["img"], "item 1.tiff")
    self.assertEqual(res["type"], 0)
    self.assertEqual(res["value"], "10g,4s")
    self.assertEqual(res["description"], "item 1 description")
    self.assertEqual(res["notes"], "item 1 notes")
    self.assertEqual(res["rarity"], 4)

    self.assertEqual(1, len(res["equippedBy"]))
    self.assertEqual(3, len(res["equippedBy"][0].keys()))
    self.assertEqual(res["equippedBy"][0]["creature"]["name"], "creature 2")
    self.assertEqual(res["equippedBy"][0]["equipChance"], "[3+] on [1d4]")
    self.assertEqual(res["equippedBy"][0]["notes"], "equipment 3 notes")

    self.assertEqual(1, len(res["droppedBy"]))
    self.assertEqual(3, len(res["droppedBy"][0].keys()))
    self.assertEqual(res["droppedBy"][0]["creature"]["name"], "creature 3")
    self.assertEqual(res["droppedBy"][0]["dropChance"], "[19+] on [1d20]")
    self.assertEqual(res["droppedBy"][0]["notes"], "drop 1 notes")

    self.assertEqual(1, len(res["ammoFor"]))
    self.assertEqual(4, len(res["ammoFor"][0]))
    self.assertEqual(res["ammoFor"][0]["name"], "item 3")

    self.assertEqual(2, len(res["spellCost"]))
    self.assertEqual(2, len(res["spellCost"][0].keys()))
    self.assertEqual(2, len(res["soldAt"]))
    self.assertEqual(4, len(res["soldAt"][0].keys()))

    res = self._dbm.get_item("item 2")
    self.assertEqual(len(DatabaseManager.FULL_ITEM_FIELDS) + 6, len(res.keys()))
    self.assertEqual(res["effect"], "item 2 effect")
    self.assertEqual(1, len(res["spellCost"]))
    self.assertEqual(2, len(res["spellCost"][0]))
    self.assertEqual(res["spellCost"][0]["spell"]["id"], 2)
    self.assertEqual(res["spellCost"][0]["qty"], 2)

    res = self._dbm.get_item("item 3")
    self.assertEqual(len(DatabaseManager.FULL_ITEM_FIELDS) + len(DatabaseManager.WEAPON_FIELDS) + 6, len(res.keys()))
    self.assertEqual(res["dmg"], "[1d12]")
    self.assertEqual(res["crit"], "x3")
    self.assertEqual(res["ammo"]["name"], "item 1")
    self.assertEqual(res["range"], 30)
    self.assertEqual(res["slot"], "one-handed")
    self.assertEqual(1, len(res["attacks"]))
    self.assertEqual(res["attacks"][0]["id"], 0)

    self.assertEqual(1, len(res["soldAt"]))
    self.assertEqual(4, len(res["soldAt"][0].keys()))
    self.assertEqual(res["soldAt"][0]["store"]["name"], "store 2")
    self.assertEqual(res["soldAt"][0]["store"]["location"], "location 3")
    self.assertEqual(res["soldAt"][0]["qty"], 3)
    self.assertEqual(res["soldAt"][0]["stockDays"], "[2] on [1d4]")
    self.assertEqual(res["soldAt"][0]["price"], "3c")

    res = self._dbm.get_item("item 4")
    self.assertEqual(len(DatabaseManager.FULL_ITEM_FIELDS) + len(DatabaseManager.ARMOR_FIELDS) + 5, len(res.keys()))
    self.assertEqual(res["ac"], 3)
    self.assertEqual(res["slot"], "helmet")

  ########
  # Verifies functionality of get_item with null values.
  def test_full_item_null(self):
    res = self._dbm.get_item("item 5")
    self.assertEqual(len(DatabaseManager.FULL_ITEM_FIELDS) + 5, len(res.keys()))
    self.assertEqual(res["name"], "item 5")
    self.assertEqual(res["img"], None)
    self.assertEqual(res["type"], 0)
    self.assertEqual(res["value"], None)
    self.assertEqual(res["description"], None)
    self.assertEqual(res["notes"], None)
    self.assertEqual(res["rarity"], None)
    self.assertEqual(0, len(res["equippedBy"]))
    self.assertEqual(0, len(res["droppedBy"]))
    self.assertEqual(0, len(res["ammoFor"]))
    self.assertEqual(0, len(res["spellCost"]))
    self.assertEqual(0, len(res["soldAt"]))

    res = self._dbm.get_item("item 6")
    self.assertEqual(len(DatabaseManager.FULL_ITEM_FIELDS) + 6, len(res.keys()))
    self.assertEqual(res["effect"], None)
    self.assertEqual(1, len(res["droppedBy"]))
    self.assertEqual(3, len(res["droppedBy"][0].keys()))
    self.assertEqual(res["droppedBy"][0]["creature"]["name"], "creature 4")
    self.assertEqual(res["droppedBy"][0]["dropChance"], None)
    self.assertEqual(res["droppedBy"][0]["notes"], None)

    res = self._dbm.get_item("item 7")
    self.assertEqual(len(DatabaseManager.FULL_ITEM_FIELDS) + len(DatabaseManager.ARMOR_FIELDS) + 5, len(res.keys()))
    self.assertEqual(res["ac"], None)
    self.assertEqual(res["slot"], None)

    self.assertEqual(1, len(res["soldAt"]))
    self.assertEqual(4, len(res["soldAt"][0].keys()))
    self.assertEqual(res["soldAt"][0]["store"]["name"], "store 2")
    self.assertEqual(res["soldAt"][0]["store"]["location"], "location 3")
    self.assertEqual(res["soldAt"][0]["qty"], None)
    self.assertEqual(res["soldAt"][0]["stockDays"], None)
    self.assertEqual(res["soldAt"][0]["price"], None)

    res = self._dbm.get_item("item 8")
    self.assertEqual(len(DatabaseManager.FULL_ITEM_FIELDS) + len(DatabaseManager.WEAPON_FIELDS) + 6, len(res.keys()))
    self.assertEqual(res["dmg"], None)
    self.assertEqual(res["crit"], None)
    self.assertEqual(res["ammo"], None)
    self.assertEqual(res["range"], None)
    self.assertEqual(res["slot"], None)
    self.assertEqual(0, len(res["attacks"]))

  ########
  # Verifies functionality of get_attack with non-null values.
  def test_full_attack_non_null(self):
    res = self._dbm.get_attack(0)
    self.assertEqual(len(DatabaseManager.FULL_ATTACK_FIELDS) + 2, len(res.keys()))
    self.assertEqual(res["id"], 0)
    self.assertEqual(res["name"], "attack 1")
    self.assertEqual(res["img"], "attack 1_a.gif")
    self.assertEqual(res["description"], "attack 1 description")
    self.assertEqual(res["notes"], "attack 1 notes")
    self.assertEqual(res["dmg"], "[1d2] + 4")
    self.assertEqual(res["isSpell"], 0)

    self.assertEqual(1, len(res["creatures"]))
    self.assertEqual(res["creatures"][0]["name"], "creature 2")

    self.assertEqual(1, len(res["weapons"]))
    self.assertEqual(res["weapons"][0]["name"], "item 3")

    res = self._dbm.get_attack(1)
    self.assertEqual(len(DatabaseManager.FULL_ATTACK_FIELDS) + len(DatabaseManager.SPELL_FIELDS) + 3, len(res.keys()))
    self.assertEqual(res["id"], 1)
    self.assertEqual(res["name"], "attack 1")
    self.assertEqual(res["img"], "attack 1_b.png")
    self.assertEqual(res["isSpell"], 1)
    self.assertEqual(res["channel"], 4)
    self.assertEqual(1, len(res["costs"]))
    self.assertEqual(2, len(res["costs"][0].keys()))
    self.assertEqual(res["costs"][0]["item"]["name"], "item 1")
    self.assertEqual(res["costs"][0]["qty"], 1)

  ########
  # Verifies functionality of get_attack with null values.
  def test_full_attack_null(self):
    res = self._dbm.get_attack(4)
    self.assertEqual(len(DatabaseManager.FULL_ATTACK_FIELDS) + 2, len(res.keys()))
    self.assertEqual(res["id"], 4)
    self.assertEqual(res["name"], "attack 4")
    self.assertEqual(res["img"], None)
    self.assertEqual(res["description"], None)
    self.assertEqual(res["notes"], None)
    self.assertEqual(res["dmg"], None)
    self.assertEqual(res["isSpell"], 0)

    self.assertEqual(1, len(res["creatures"]))
    self.assertEqual(res["creatures"][0]["name"], "creature 1")

    self.assertEqual(0, len(res["weapons"]))

    res = self._dbm.get_attack(3)
    self.assertEqual(len(DatabaseManager.FULL_ATTACK_FIELDS) + len(DatabaseManager.SPELL_FIELDS) + 3, len(res.keys()))
    self.assertEqual(res["isSpell"], 1)
    self.assertEqual(res["channel"], None)
    self.assertEqual(1, len(res["costs"]))
    self.assertEqual(2, len(res["costs"][0].keys()))
    self.assertEqual(res["costs"][0]["item"]["name"], "item 4")
    self.assertEqual(res["costs"][0]["qty"], None)

  ########
  # Verifies functionality of get_location with non-null values.
  def test_full_location_non_null(self):
    res = self._dbm.get_location("location 1")
    self.assertEqual(len(DatabaseManager.FULL_LOCATION_FIELDS) + 2, len(res.keys()))
    self.assertEqual(res["name"], "location 1")
    self.assertEqual(res["img"], "location 1.png")
    self.assertEqual(res["description"], "location 1 description")
    self.assertEqual(res["notes"], "location 1 notes")

    self.assertEqual(1, len(res["creatures"]))
    self.assertEqual(2, len(res["creatures"][0].keys()))
    self.assertEqual(res["creatures"][0]["creature"]["name"], "creature 1")
    self.assertEqual(res["creatures"][0]["notes"], "inhabit 1 notes")

    self.assertEqual(1, len(res["stores"]))
    self.assertEqual(res["stores"][0]["name"], "store 1")
    self.assertEqual(res["stores"][0]["location"], "location 1")

  ########
  # Verifies functionality of get_location with null values.
  def test_full_location_null(self):
    res = self._dbm.get_location("location 3")
    self.assertEqual(len(DatabaseManager.FULL_LOCATION_FIELDS) + 2, len(res.keys()))
    self.assertEqual(res["name"], "location 3")
    self.assertEqual(res["img"], None)
    self.assertEqual(res["description"], None)
    self.assertEqual(res["notes"], None)
    self.assertEqual(1, len(res["creatures"]))
    self.assertEqual(res["creatures"][0]["creature"]["name"], "creature 2")

    self.assertEqual(1, len(res["stores"]))
    self.assertEqual(res["stores"][0]["name"], "store 2")
    self.assertEqual(res["stores"][0]["img"], None)

    res = self._dbm.get_location("location 2")
    self.assertEqual(1, len(res["creatures"]))
    self.assertEqual(res["creatures"][0]["creature"]["name"], "creature 1")
    self.assertEqual(res["creatures"][0]["notes"], None)

  ########
  # Verifies functionality of get_store with non=null values.
  def test_full_store_non_null(self):
    res = self._dbm.get_store("store 1", "location 2")
    self.assertEqual(len(DatabaseManager.FULL_STORE_FIELDS) + 1, len(res.keys()))
    self.assertEqual(res["name"], "store 1")
    self.assertEqual(res["location"]["name"], "location 2")
    self.assertEqual(res["img"], "store 1.gif")
    self.assertEqual(res["description"], "store 1 description")
    self.assertEqual(res["notes"], "store 1 notes")

    self.assertEqual(2, len(res["sells"]))

    res = self._dbm.get_store("store 1", "location 1")
    self.assertEqual(1, len(res["sells"]))
    self.assertEqual(4, len(res["sells"][0].keys()))
    self.assertEqual(res["sells"][0]["item"]["name"], "item 1")
    self.assertEqual(res["sells"][0]["qty"], 100)
    self.assertEqual(res["sells"][0]["stockDays"], "[1] on [1d4]")
    self.assertEqual(res["sells"][0]["price"], "2g")

  ########
  # Verifies functionality of get_store with null values.
  def test_full_store_null(self):
    res = self._dbm.get_store("store 2", "location 2")
    self.assertEqual(len(DatabaseManager.FULL_STORE_FIELDS) + 1, len(res.keys()))
    self.assertEqual(res["name"], "store 2")
    self.assertEqual(res["location"]["name"], "location 2")
    self.assertEqual(res["img"], None)
    self.assertEqual(res["description"], None)
    self.assertEqual(res["notes"], None)

    self.assertEqual(1, len(res["sells"]))
    self.assertEqual(res["sells"][0]["item"]["name"], "item 8")
    self.assertEqual(res["sells"][0]["qty"], None)
    self.assertEqual(res["sells"][0]["stockDays"], None)
    self.assertEqual(res["sells"][0]["price"], None)

if __name__ == "__main__":
  print("Setup")
  temp_dbm = DatabaseManager("test.db")
  temp_dbm.reset("../src/tables.sql", "test.sql")
  temp_dbm.commit()
  temp_dbm.close()
  del temp_dbm

  print("Test")
  unittest.main()
