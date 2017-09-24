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
    f = open("test.db", "w")
    f.close()
    self._dbm = DatabaseManager("test.db")
    self._dbm.reset("../tables.sql", "test.sql")

  def tearDown(self):
    self._dbm.close()

  def test_simple_creature_non_null(self):
    res = self._dbm.get_simple_creature("creature 1")
    self.assertEqual(3, len(res.keys()))
    self.assertEqual(res["name"], "creature 1")
    self.assertEqual(res["img"], "creature 1.jpg")
    self.assertEqual(res["hd"], 4)

  def test_simple_creature_null(self):
    res = self._dbm.get_simple_creature("creature 4")
    self.assertEqual(3, len(res.keys()))
    self.assertEqual(res["name"], "creature 4")
    self.assertEqual(res["img"], None)
    self.assertEqual(res["hd"], None)

  def test_simple_item_non_null(self):
    res = self._dbm.get_simple_item("item 1")
    self.assertEqual(4, len(res.keys()))
    self.assertEqual(res["name"], "item 1")
    self.assertEqual(res["img"], "item 1.tiff")
    self.assertEqual(res["type"], 0)
    self.assertEqual(res["value"], "10g,4s")

  def test_simple_item_null(self):
    res = self._dbm.get_simple_item("item 7")
    self.assertEqual(4, len(res.keys()))
    self.assertEqual(res["name"], "item 7")
    self.assertEqual(res["img"], None)
    self.assertEqual(res["type"], 2)
    self.assertEqual(res["value"], None)


if __name__ == "__main__":
  unittest.main()
