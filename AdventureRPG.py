import random

# Global variable list
DEBUG = False

# Naming scheme for inventory goes as follows:
# ID, amount, name, sell price, buy price, shop to be bought from

inventory = {
    "gold": [0, "Gold", 1, -1, -1],
    "potion_health_small": [0,"Potion of Minor Health", 5, 10, 1],
    "potion_health_medium": [0, "Potion of Health", 10, 20, 1],
    "potion_health_large": [0, "Potion of Major Health", 20, 40, 1],
    "potion_mana_small": [0,"Potion of Minor Arcana", 5, 10, 1],
    "potion_mana_medium": [0, "Potion of Arcana", 10, 20, 1],
    "potion_mana_large": [0, "Potion of Major Arcana", 20, 40, 1],
    "drop_slimeball": [0, "Slimeball", 0, 5, 2],
    "drop_guts": [0, "Monster Guts", 0, 2, 2],
    "held_amulet1": [0, "Amulet of Fugur'knum", 10000, -1, -1],
    "held_amulet2": [0, "Amulet of Bvarken-ra", 10000, -1, -1],
    "held_amulet3": [0, "Amulet of X//A3//I2", 10000, -1, -1],
    "resource_glass": [0, "Glass", 5, 10, 3],
    "resource_clearwater":[0, "Vial of Clear Water", 15, 30, 1],
    "resource_wood_ash": [0, "Ash Lumber", 45, 90, 3],
    "resource_wood_oak": [0, "Oak Lumber", 10, 20, 3],
    "resource_wood_rowan": [0, "Rowan Lumber", 35, 70, 3],
    "forage_berry_red": [0, "Branch of Red Berries", 2, -1, "forage"],
    "forage_berry_blue": [0, "Branch of Blue Berries", 2, -1, "forage"],
    "forage_berry_green": [0, "Branch of Green Berries", 2, -1, "forage"],
    "forage_berry_black": [0, "Branch of Black Berries", 2, -1, "forage"],
    "forage_berry_white": [0, "Branch of White Berries", 2, -1, "forage"],
    "crafted_glassvial": [0, "Glass Vial", 40, -1, -1],
    "crafted_alchemicalpaste": [0, "Alchemical Paste", 20, -1, -1]
}

held_item_ids = {
    [None, 0],
    ["held_amulet1", 1],
    ["held_amulet2", 2],
    ["held_amulet3", 3]
}

currency = next(iter(inventory))
