/***************
 *
 * Objects
 *
 **************/

INSERT INTO Creatures(name, img, description, notes, rarity, hd, hp, ac, xp, basicAttack)
  VALUES ("creature 1", "creature 1.jpg", "creature 1 description", "creature 1 notes", 1, 4, "15 + [1d6]", 7, 80, "Punch: [1d8]"),
         ("creature 2", "creature 2.png", "creature 2 description", "creature 2 notes", 2, 5, "20 + [1d6]", 8, 120, "Punch: [1d4 + 1]"),
         ("creature 3", "creature 3.gif", "creature 3 description", "creature 3 notes", 3, 2, "5 + [1d6]", 9, 40, "Lick: [1d2]"),
         ("creature 4", NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO Items(name, img, type, value, description, notes, rarity)
  VALUES ("item 1", "item 1.tiff", 0, "10g,4s", "item 1 description", "item 1 notes", 4),
         ("item 2", "item 2.jpg", 1, "100p", "item 2 description", "item 2 notes", 2),
         ("item 3", "item 3.png", 3, "3c", "item 3 description", "item 3 notes", 1),
         ("item 4", "item 4.jpg", 2, "5g,5s,5c", "item 4 description", "item 4 notes", 3),
         ("item 5", NULL, 0, NULL, NULL, NULL, NULL),
         ("item 6", NULL, 1, NULL, NULL, NULL, NULL),
         ("item 7", NULL, 2, NULL, NULL, NULL, NULL),
         ("item 8", NULL, 3, NULL, NULL, NULL, NULL);

INSERT INTO Consumables(name, effect)
  VALUES ("item 2", "item 2 effect"),
         ("item 6", NULL);

INSERT INTO Armor(name, ac, slot)
  VALUES ("item 4", 3, "helmet"),
         ("item 7", NULL, NULL);

INSERT INTO Weapons(name, dmg, crit, ammo, range, slot)
  VALUES ("item 3", "[1d12]", "x3", "item 1", 30, "one-handed"),
         ("item 8", NULL, NULL, NULL, NULL, NULL);


INSERT INTO SpecialAttacks(id, name, img, description, notes, dmg, isSpell)
  VALUES (0, "attack 1", "attack 1_a.gif", "attack 1 description", "attack 1 notes", "[1d2] + 4", 0),
         (1, "attack 1", "attack 1_b.png", "attack 1_b description", "attack 1_b notes", "[1d4] + 4", 1),
         (2, "attack 2", NULL, "attack 2 description", "attack 2 notes", "[4d20]", 1),
         (3, "attack 3", NULL, NULL, NULL, NULL, 1),
         (4, "attack 4", NULL, NULL, NULL, NULL, 0);

INSERT INTO Spells(id, channel)
  VALUES (1, 4),
         (2, NULL),
         (3, 0);

INSERT INTO Locations(name, img, description, notes)
  VALUES ("location 1", "location 1.png", "location 1 description", "location 1 notes"),
         ("location 2", "location 2.gif", "location 2 description", "location 2 notes"),
         ("location 3", NULL, NULL, NULL);

INSERT INTO Stores(name, location, img, description, notes)
  VALUES ("store 1", "location 2", "store 1.gif", "store 1 description", "store 1 notes"),
         ("store 1", "location 1", NULL, "store 1 description_b", "store 1 notes_b"),
         ("store 2", "location 2", NULL, NULL, NULL),
         ("store 2", "location 3", NULL, NULL, NULL);

/***************
 *
 * Relations
 *
 **************/

INSERT INTO Equips(creature, item, equipChance, notes)
  VALUES ("creature 2", "item 3", "[10+] on [1d20]", "equipment 1 notes"),
         ("creature 1", "item 3", "[2+] on [1d8]", "equipment 2 notes"),
         ("creature 2", "item 4", NULL, NULL);

INSERT INTO Drops(item, creature, dropChance, notes)
  VALUES ("item 1", "creature 3", "[19+] on [1d20]", "drop 1 notes"),
         ("item 2", "creature 3", NULL, NULL),
         ("item 2", "creature 2", "[2+] on [1d10]", "drop 2 notes"),
         ("item 6", "creature 4", NULL, NULL);

INSERT INTO CreatureAttacks(creature, attackId)
  VALUES ("creature 1", 1),
         ("creature 1", 3),
         ("creature 1", 4),
         ("creature 2", 0);

INSERT INTO Inhabits(creature, location, notes)
  VALUES ("creature 1", "location 1", "inhabit 1 notes"),
         ("creature 1", "location 2", NULL),
         ("creature 2", "location 3", "inhabit 2 notes"),
         ("creature 3", "location 2", "inhabit 3 notes");

INSERT INTO WeaponAttacks(item, attackId)
  VALUES ("item 3", 0),
         ("item 3", 3);

INSERT INTO CastingCosts(item, spellId, qty)
  VALUES ("item 1", 3, 1),
         ("item 2", 6, NULL);

INSERT INTO Sells(item, store, location, qty, stockDays, price)
  VALUES ("item 1", "store 1", "location 2", 2, "[4] on [1d4]", "8g2s1c"),
         ("item 2", "store 1", "location 2", NULL, NULL, NULL),
         ("item 1", "store 1", "location 1", 100, "[1] on [1d4]", "2g"),
         ("item 3", "store 2", "location 3", NULL, NULL, NULL),
         ("item 7", "store 2", "location 3", NULL, NULL, NULL),
         ("item 8", "store 2", "location 2", NULL, NULL, NULL);
