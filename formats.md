# Database Manager Formats

All returns from the `DatabaseManager` object found in _dbase\_manager.py_ are formatted as dictionary objects as described below. The formatting `<a:b>` signifies an value of type `b` that represents the word or phrase described by `a`. If the type is preceded by an exclamation point (Ex: `!<a:b>`), it can be null. All lists can be empty, but no list will contain null entries.

## Creature

### Simple

    {
      "name": <name:string>,
      "img":  !<img_link:string>,
      "hd":   !<hit_dice:int>
    }

### Full

    {
      "name":   <name:string>,
      "img":    !<img_link:string>,
      "description": !<description:string>,
      "notes":  !<notes:string>,
      "rarity": !<rarity:int>,
      "hd":     !<hit_dice:int>,
      "hp":     !<health_points:string>,
      "ac":     !<armor_class:int>,
      "xp":     !<experience:int>,
      "basicAttack": !<basic_attack:string>,
      "equips": [
        {
          "item":   <item:simple_item>,
          "equipChance": !<equip_chance:string>,
          "notes":  !<notes:string>
        },
        ...
      ],
      "drops": [
        {
          "item":   <item:simple_item>,
          "dropChance": !<drop_chance:string>,
          "notes":  !<notes:string>
        },
        ...
      ],
      "creatureAttacks": [
        <attack:simple_attack>,
        ...
      ],
      "inhabits": [
        {
          "location": <location:simple_location>,
          "notes":    !<notes:string>
        },
        ...
      ]
    }

## Item

### Simple

    {
      "name":   <name:string>,
      "img":    !<img_link:string>,
      "type":   <type:int>,
      "value":  !<value:string>
    }

### Full

    {
      "name":   <name:string>,
      "img":    !<img_link:string>,
      "type":   <type:int>,
      "value":  !<value:string>,
      "description": !<description:string>,
      "notes":  !<notes:string>,
      "rarity": !<rarity:int>,
    }

If `type` is armor, also has:

    "ac":   !<armor_class:int>,
    "slot": !<armor_slot:string>

If `type` is weapon, also has:

    "dmg":    !<damage:string>,
    "crit":   !<critical_strike:string>,
    "ammo":   !<item:simple_item>,
    "range":  !<range:int>,
    "slot":   !<weapon_slot:string>,
    "weaponAttacks": [
      <attack:simple_attack>,
      ...
    ]

If `type` is consumable, also has:

    "effect": !<effect:string>

## Attack

### Simple

    {
      "id":       <attack_id:int>,
      "name":     <name:string>,
      "img":      !<img_link:string>,
      "isSpell":  !<is_spell:bool>
    }

### Full

    {
      "id":       <attack_id:int>,
      "name":     <name:string>,
      "img":      !<img_link:string>,
      "description": !<description:string>,
      "notes":    !<notes:string>,
      "dmg":      !<damage:string>,
      "isSpell":  <is_spell:bool>
    }

If `isSpell` is true, also has:

    "channel": !<channel_duration:int>,
    "cost": {
      <casting_cost:simple_item>,
      ...
    }

## Location

### Simple

    {
      "name": <name:string>,
      "img":  !<img_link:string>
    }

### Full

    {
      "name":   <name:string>,
      "img":    !<img_link:string>,
      "description": !<description:string>,
      "notes":  !<notes:string>,
      "creatures": [
        {
          <creature:simple_creature>,
          "notes": !<notes:string>
        },
        ...
      ],
      "stores": [
        <store:simple_store>,
        ...
      ]
    }

## Store

### Simple

    {
      "name":     <name:string>,
      "location": <location:string>,
      "img":      !<img_link:string>
    }

### Full

    {
      "name":     <name:string>,
      "img":      !<img_link:string>,
      "location": <location:simple_location>,
      "description": !<description:string>,
      "notes":    !<notes:string>,
      "sells": [
        {
          "item":   <item:simple_item>,
          "qty":    !<quantity:int>,
          "stockDays": !<stock_days:string>,
          "price":  !<price:string>
        },
        ...
      ]
    }
