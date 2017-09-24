/*******************************
 * tables.sql
 * Noah Ansel
 * 2017-09-24
 * -----------------------------
 * Initializes all tables and relations in the database.
 ******************************/


/***************
 *
 * Tables
 *
 **************/

/*
 * Basic values for a creature. Does not include relations. Does not include
 * relations.
 */
CREATE TABLE Creatures (
  name CHAR(255) PRIMARY KEY,
  img CHAR(255),
  description TEXT(1023),
  notes TEXT(1023),
  rarity INTEGER,
  hd INTEGER,
  hp CHAR(127),
  ac INTEGER,
  xp INTEGER,
  basicAttack CHAR(255)
);

/*
 * Basic values for an item, and `type` value indicating type of item:
 *  0: Item (no extra fields)
 *  1: Consumable
 *  2: Armor
 *  3: Weapon
 * Does not include relations.
 */
CREATE TABLE Items (
  name CHAR(255) PRIMARY KEY,
  img CHAR(255),
  type INTEGER NOT NULL,
  value CHAR(127),
  description TEXT(1023),
  notes TEXT(1023),
  rarity INTEGER
);

/*
 * Child of Items containing extra fields for a consumable item.
 */
CREATE TABLE Consumables (
  name CHAR(255) PRIMARY KEY REFERENCES Items ON DELETE CASCADE,
  effect CHAR(1023)
);

/*
 * Child of Items containing extra fields for an armor item.
 */
CREATE TABLE Armor (
  name CHAR(255) PRIMARY KEY REFERENCES Items ON DELETE CASCADE,
  ac INTEGER,
  slot CHAR(63)
);

/*
 * Child of Items containing extra fields for a weapon item. Includes ammo
 * relation.
 */
CREATE TABLE Weapons (
  name CHAR(255) PRIMARY KEY REFERENCES Items ON DELETE CASCADE,
  dmg CHAR(127),
  crit CHAR(127),
  ammo CHAR(255),
  range INTEGER,
  slot CHAR(63),
  FOREIGN KEY (ammo) REFERENCES Items(name)
);

/*
 * Basic values for a spell, and `isSpell` field indicating whether entry is a
 * spell. Does not include relations.
 */
CREATE TABLE SpecialAttacks (
  id INTEGER PRIMARY KEY,
  name CHAR(255) NOT NULL,
  img CHAR(255),
  description TEXT(1023),
  notes TEXT(1023),
  dmg CHAR(127),
  isSpell BOOLEAN NOT NULL
);

/*
 * Child of SpecialAttacks containing extra fields for a spell item. Does not
 * include relations.
 */
CREATE TABLE Spells (
  id INTEGER PRIMARY KEY REFERENCES SpecialAttacks,
  channel INTEGER
);

/*
 * Basic values for a location. Does not include relations.
 */
CREATE TABLE Locations (
  name CHAR(255) PRIMARY KEY,
  img CHAR(255),
  description TEXT(1023),
  notes TEXT(1023)
);

/*
 * Basic values for a store. Includes store-location relation.
 */
CREATE TABLE Stores (
  name CHAR(255) NOT NULL,
  location CHAR(255) REFERENCES Locations,
  img CHAR(255),
  description TEXT(1023),
  notes TEXT(1023),
  FOREIGN KEY (location) REFERENCES Locations ON UPDATE CASCADE,
  PRIMARY KEY (name, location)
);




/***************
 *
 * Relations
 *
 **************/

/*
 * Equip relation: Creatures -> Items
 */
CREATE TABLE Equips (
  creatureName CHAR(255) NOT NULL,
  itemName CHAR(255) NOT NULL,
  equipChance CHAR(127),
  notes TEXT(1023),
  FOREIGN KEY (itemName) REFERENCES Items(name) ON UPDATE CASCADE,
  FOREIGN KEY (creatureName) REFERENCES Creatures(name) ON DELETE CASCADE ON UPDATE CASCADE,
  PRIMARY KEY (itemName, creatureName)
);

/*
 * Drop relation: Creatures -> Items
 */
CREATE TABLE Drops (
  itemName CHAR(255) NOT NULL,
  creatureName CHAR(255) NOT NULL,
  dropChance CHAR(127),
  notes TEXT(1023),
  FOREIGN KEY (itemName) REFERENCES Items(name) ON UPDATE CASCADE,
  FOREIGN KEY (creatureName) REFERENCES Creatures(name) ON DELETE CASCADE ON UPDATE CASCADE,
  PRIMARY KEY (itemName, creatureName)
);

/*
 * CreatureAttack relation: Creatures -> SpecialAttacks
 */
CREATE TABLE CreatureAttacks (
  creatureName CHAR(255) NOT NULL,
  attackId INTEGER NOT NULL,
  FOREIGN KEY (creatureName) REFERENCES Creatures(name) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (attackId) REFERENCES SpecialAttacks(id) ON UPDATE CASCADE,
  PRIMARY KEY (creatureName, attackId)
);

/*
 * Inhabit relation: Creatures <-> Locations
 */
CREATE TABLE Inhabits (
  creatureName CHAR(255) NOT NULL,
  locationName CHAR(255) NOT NULL,
  FOREIGN KEY (creatureName) REFERENCES Creatures(name) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (locationName) REFERENCES Locations(name) ON DELETE CASCADE ON UPDATE CASCADE,
  PRIMARY KEY (creatureName, locationName)
);

/*
 * WeaponAttack relation: Weapons -> SpecialAttacks
 */
CREATE TABLE WeaponAttacks (
  itemName CHAR(255) NOT NULL,
  attackId INTEGER NOT NULL,
  FOREIGN KEY (itemName) REFERENCES Items(name) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (attackId) REFERENCES SpecialAttacks(id) ON UPDATE CASCADE,
  PRIMARY KEY (itemName, attackId)
);

/*
 * CastingCost relation: Spells -> Items
 */
CREATE TABLE CastingCosts (
  itemName CHAR(255) NOT NULL,
  spellId INTEGER NOT NULL,
  FOREIGN KEY (itemName) REFERENCES Items(name) ON UPDATE CASCADE,
  FOREIGN KEY (spellId) REFERENCES SpecialAttacks(id) ON DELETE CASCADE ON UPDATE CASCADE,
  PRIMARY KEY (itemName, spellId)
);

/*
 * Sell relation: Stores -> Items
 */
CREATE TABLE Sells (
  itemName CHAR(255) NOT NULL,
  storeName CHAR(255) NOT NULL,
  locationName CHAR(255) NOT NULL,
  qty INTEGER,
  stockDays CHAR(127),
  price CHAR(127),
  FOREIGN KEY (itemName) REFERENCES Items(name) ON UPDATE CASCADE,
  FOREIGN KEY (storeName, locationName) REFERENCES Stores(name, location) ON DELETE CASCADE ON UPDATE CASCADE,
  PRIMARY KEY (itemName, storeName, locationName)
);