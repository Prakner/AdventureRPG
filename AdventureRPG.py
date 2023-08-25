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

handcrafting_recipes = {
    "Glass Vial": ["crafted_glassvial", [5, "resource_glass"]],
    "Alchemical Paste": ["crafted_alchemicalpaste", [1, "resource_clearwater"], [3, "drop_guts"], [1, "drop_slimeball"]]
}

alchemical_recipes = {
    "Potion of Minor Health": ["potion_health_small", [1, "crafted_glassvial"], [1, "crafted_alchemicalpaste"], [5, "forage_berry_red"]],
    "Potion of Health": ["potion_health", [1, "potion_health_small"], [3, "crafted_alchemicalpaste"], [5, "forage_berry_red"]],
    "Potion of Minor Arcana": ["potion_mana_small", [1, "crafted_glassvial"], [1, "crafted_alchemicalpaste"], [5, "forage_berry_blue"]],
    "Potion of Arcana": ["potion_mana", [1, "potion_mana_small"], [3, "crafted_alchemicalpaste"], [5, "forage_berry_blue"]]
}

def get_random_name():
    name1 = ["Arc", "Mai", "Shen", "Meg", "Gre", "Pre", "Ur", "Ar", "Est", "Anc", "Redd", "Mu", "Br", "Pet", "Lo", "Stew", "Mar", "Dar", "Claud", "Ja", "Sky", "Jenn", "Ash", "Nata", "Dw", "Bill", "Will", "Bai", "Sebas", "Hero", "Aca", "Pik", "Lay", "Fe", "Tex", "El", "Men", "Le", "Al", "Had", "Prak", "No", "Mid", "Be", "Sanc", "Oop", "Dough", "Do", "Pep", "Shake", "Jo", "Sa", "Tr", "Hol", "Mo", "Yo", "Ba", "Har", "Valen", "Vic", "Theo", "Per", "Cy", "Anna", "Ta", "Ea", "Ca", "Ka", "Pi", "Calyp", "Cha", "Sli", "Ly", "Zip", "Po", "A", "E", "I", "O", "U", "Scr", "Fo", "Fi", "Fee", "Bar", "Wo", "Dump", "Gu", "Ran", "Dom", "Bul", "Ch", "Go", "Rai", "Cap", "Tain", "Amer", "Icar", "Grem", "Krak"]
    name2 = ["man", "shen", "an", "ian", "ast", "shu", "ho", "gry", "it", "hovy", "atron", "er", "is", "ie", "io", "izabeth", "ette", "ron", "son", "lyn", "ley", "leigh", "ey", "lie", "ight", "iam", "tian", "brine", "cia", "min", "oli", "ton", "lix", "as", "on", "den", "tos", "bron", "bert", "die", "ner", "ah", "night", "egz", "tus", "sie", "nut", "vah", "per", "speare", "jo", "lem", "ash", "nopoly", "rty", "ney", "ry", "tina", "tine", "tor", "toria", "cy", "rus", "beth", "ble", "rl", "a", "i", "zza", "so", "se", "my", "ser", "co", "ol", "mp", "truck", "sin", "us", "ite", "lin", "in", "borb", "birb", "berb", "barb", "burb", "bon", "bie", "gy", "bread", "drop", "slurp", "goo", "bow", "kou", "ken", "hen", "zgy", "qry"]
    name = random.choice(name1) + random.choice(name2)
    return name

