################################
# dbase_manager_test.py
# Noah Ansel
# 2017-09-24
# ------------------------------
# Tests functionality of DatabaseManager against formats defined in formats.md.
################################

import unittest
from dbase_manager import DatabaseManager

class TestDatabaseManagerMethods(unittest.TestCase):
  
  def setUp(self):
    self._dbm = DatabaseManager("test/test.db")

  def tearDown(self):
    # do not commit, just close
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

if __name__ == "__main__":
  print("Setup")
  temp_dbm = DatabaseManager("test/test.db")
  temp_dbm.reset("tables.sql", "test/test.sql")
  temp_dbm.commit()
  temp_dbm.close()
  del temp_dbm

  print("Test")
  unittest.main()
