import random
import time
# Global variable list
DEBUG = False
TEXT_SPEED = 0.1

# Naming scheme for inventory goes as follows:
# ID, amount, name, sell price, buy price, shop to be bought from

def animate_text(text):
    number_of_characters=1
    while True:
        print(text[0:number_of_characters],end='\r')
        if number_of_characters > len(text):
            print('\n')
            break
        else:
            number_of_characters += 1
        time.sleep(0.05)

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

def detect_held_item(value:int):
    item_found = False
    for item in held_item_ids:
        if value == item[1]:
            item_found = True
            held_item_name = item[0]
        if item_found == True:
            if DEBUG:
                print(f"DEBUG: Item ID detected. Item is {held_item_name}.")
            return True
        else:
            if DEBUG:
                print(f"DEBUG: Item ID is invalid. Current id is {value}.")
            return False

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

def detect_rarity(rarity):
    if rarity == None or rarity == 0:
        return ""
    elif rarity == 1:
        return " (☆)"
    elif rarity == 2:
        return " (☆☆)"
    elif rarity == 3:
        return " (☆☆☆)"
    elif rarity == 4:
        return " (☆☆☆☆)"
    elif rarity == 5:
        return " (☆☆☆☆☆)"
    else:
        if DEBUG:
            print("DEBUG: Rarity invalid.")
        return " (???)"

race_list = ["human", "demonkin", "elf", "orc"]
class Adventurer:
    def __init__(self, race:str, name:str = None, attack:int = None, max_health:int = None, health:int = None, max_mana:int = None, mana:int = None, speed:int = None, held_item:int = None, rarity:int = None):
        if name == None or name == "":
            if DEBUG:
                print("DEBUG: No name detected. Randomizing...")
            name = get_random_name()
            if DEBUG:
                print(f"DEBUG: Name randomized. Chosen name is {name}.")
        if race == None:
            if DEBUG:
                print("DEBUG: No race detected. Randomizing...")
            pickrace = random.randint(0,len(race_list)-1)
            race = race_list[pickrace]
            if DEBUG:
                print(f"DEBUG: Race randomized. Chosen race is {race}.")
        if attack == None:
            if race == "human" or race == "demonkin":
                attack = random.randint(3,5)
            elif race == "elf":
                attack = random.randint(2,4)
            elif race == "orc":
                attack = random.randint(4,6)
            else:
                if DEBUG:
                    if race not in race_list:
                        print("DEBUG: Race not in race list. Defaulting to human")
                    else:
                        print("DEBUG: Unknown error. Defaulting to human.")
                race = "human"
                attack = random.randint(3,5)
        if max_health == None:
            if race == "human" or race == "demonkin":
                max_health == random.randint(20,30)
            elif race == "elf":
                max_health == random.randint(15,25)
            elif race == "orc":
                max_health == random.randint(22,35)
            else:
                if DEBUG:
                    print("DEBUG: Unknown error has occurred. Max health is 15.")
                max_health = 15
        if health == None:
            health = max_health
        if max_mana == None:
            if race == "human" or race == "orc":
                max_mana = random.randint(0,5)
            elif race == "demonkin" or race == "elf":
                max_mana = random.randint(3,8)
            else:
                if DEBUG:
                    print("DEBUG: Unknown error has occurred. Max mana is 0.")
                max_mana = 0
        if mana == None:
            mana = max_mana
        if speed == None:
            if race == "orc":
                speed = random.randint(12,25)
            elif race == "human":
                speed = random.randint(19,34)
            elif race == "demonkin":
                speed = random.randint(18,29)
            elif race == "elf":
                speed = random.randint(20,40)
            else:
                if DEBUG:
                    print("DEBUG: Unknown error has occurred. Speed is 20.")
                speed = 20
        if held_item == None or detect_held_item(held_item) == False:
            held_item = 0
        if rarity == None:
            rarity = 0
        self.race = race
        self.name = name
        self.attack = attack
        self.max_health = max_health
        self.health = health
        self.max_mana = max_mana
        self.mana = mana
        self.speed = speed
        self.held_item = held_item
        self.rarity = detect_rarity(rarity)
    def __str__(self):
        return f"{self.name}{self.rarity}- {self.race.upper()} ({self.health}/{self.max_health}) HP|({self.mana}/{self.max_mana}) MP|{self.attack} ATK|{self.speed} SPD"
