import random
import time


print(r"""  ___      _                 _                 ____________ _____         _____  __  
 / _ \    | |               | |                | ___ \ ___ \  __ \       |  _  |/  | 
/ /_\ \ __| |_   _____ _ __ | |_ _   _ _ __ ___| |_/ / |_/ / |  \/ __   _| |/' |`| | 
|  _  |/ _` \ \ / / _ \ '_ \| __| | | | '__/ _ \    /|  __/| | __  \ \ / /  /| | | | 
| | | | (_| |\ V /  __/ | | | |_| |_| | | |  __/ |\ \| |   | |_\ |  \ V /\ |_/ /_| |_
\_| |_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___\_| \_\_|   \_____/   \_/  \___(_)___/
      
      """)




# Global variable list
DEBUG = False
TEXT_SPEED = 0.001
base_exp = 500

party = []
adventurer_list = []

def fprint(text):
    number_of_characters=1
    while True:
        print(text[0:number_of_characters],end='\r')
        if number_of_characters > len(text):
            print('\n')
            break
        else:
            number_of_characters += 1
        time.sleep(TEXT_SPEED)

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
    "crafted_alchemicalpaste": [0, "Alchemical Paste", 20, -1, -1],
    "gatcha_ticket": [100, "Gatcha Ticket", -1, -1, -1]
}

held_item_ids = [
    [None, 0],
    ["held_amulet1", 1],
    ["held_amulet2", 2],
    ["held_amulet3", 3]
]

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
        return " (0 ✭ )"
    elif rarity == 1:
        return " (1 ✭ )"
    elif rarity == 2:
        return " (2 ✭ )"
    elif rarity == 3:
        return " (3 ✭ )"
    elif rarity == 4:
        return " (4 ✭ )"
    elif rarity == 5:
        return " (5 ✭ )"
    else:
        if DEBUG:
            print("DEBUG: Rarity invalid.")
        return " (???)"

# Naming scheme for equipment is as follows:
# ID: amount, name, sell price, buy price, tool type, rarity, attack boost, defense boost, mana boost, speed boost, crit boost, evasion chance, block chance

class Equipment:
    def __init__(self, name:str, buyprice:int, sellprice:int, tooltype:str, rarity:int, atk_boost:int, def_boost:int, mana_boost:int, spd_boost:int, crit_boost:float, evasion_chance:float, block_chance:float):
        self.name = name + detect_rarity(rarity)
        self.buyprice = buyprice
        self.sellprice = sellprice
        self.tooltype = tooltype
        self.rarity = rarity
        self.atk_boost = atk_boost
        self.def_boost = def_boost
        self.mana_boost = mana_boost
        self.spd_boost = spd_boost
        self.crit_boost = crit_boost
        self.evasion_chance = evasion_chance
        self.block_chance = block_chance
    def __str__(self):
        return self.name

equip_list = {
    "wooden_shield": [0, Equipment("Wooden Shield", 5, 10, "shield", 0, 0, 5, 0, 0, 0.0, 0.0, .005)],
    "copper_shield": [0, Equipment("Copper Shield", 10, 20, "shield", 0, 0, 7, 0, 0, 0.0, 0.0, .01)],
    "bronze_shield": [0, Equipment("Bronze Shield", 15, 30, "shield", 0, 0, 10, 0, 0, 0.0, 0.0, .01)],
    "iron_shield": [0, Equipment("Iron Shield", 30, 60, "shield", 1, 0, 13, 0, 0, 0.0, 0.0, .015)],
    "steel_shield": [0, Equipment("Steel Shield", 50, 100, "shield", 1, 0, 15, 0, 0, 0.0, 0.0, .015)],
    "manasteel_shield": [0, Equipment("Manasteel Shield", 5, 10, "shield", 2, 0, 5, 0, 0, 0.0, 0.0, .02)],
    "bone_shield": [0, Equipment("Bone Shield", 10, 20, "shield", 2, 0, 7, 0, 0, 0.0, 0.0, .025)],
    "necrotic_shield": [0, Equipment("Necrotic Shield", 15, 30, "shield", 3, 0, 10, 0, 0, 0.0, 0.0, .03)],
    "blessed_shield": [0, Equipment("Blessed Shield", 30, 60, "shield", 3, 0, 13, 0, 0, 0.0, 0.0, .04)],
    "gold_shield": [0, Equipment("Golden Shield", 50, 100, "shield", 4, 0, 15, 0, 0, 0.0, 0.0, .05)],
    "godly_shield": [0, Equipment("Godly Shield", 50, 100, "shield", 5, 0, 15, 0, 0, 0.0, 0.0, .075)],
}

race_list = ["human", "demonkin", "elf", "orc"]
class Adventurer:
    def __init__(self, race:str = None, name:str = None, strength:int = None, defense:int = None,max_health:int = None, health:int = None, max_mana:int = None, mana:int = None, speed:int = None, held_item:int = None, level:int = None, exp:int = None, main_character:bool = False):
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
        if strength == None:
            if race == "human" or race == "demonkin":
                strength = random.randint(3,5)
            elif race == "elf":
                strength = random.randint(2,4)
            elif race == "orc":
                strength = random.randint(4,6)
            else:
                if DEBUG:
                    if race not in race_list:
                        print("DEBUG: Race not in race list. Defaulting to human")
                    else:
                        print("DEBUG: Unknown error. Defaulting to human.")
                race = "human"
                strength = random.randint(3,5)
        if defense == None:
            defense = random.randint(10,15)
        if max_health == None:
            if race == "human" or race == "demonkin":
                max_health = random.randint(20,30)
            elif race == "elf":
                max_health = random.randint(15,25)
            elif race == "orc":
                max_health = random.randint(22,35)
            else:
                if DEBUG:
                    print("DEBUG: Unknown error has occurred. Max health is 15.")
                max_health = 15
        if max_mana == None:
            if race == "human" or race == "orc":
                max_mana = random.randint(0,5)
            elif race == "demonkin" or race == "elf":
                max_mana = random.randint(3,8)
            else:
                if DEBUG:
                    print("DEBUG: Unknown error has occurred. Max mana is 0.")
                max_mana = 0
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
        if health == None:
            health = max_health
        if mana == None:
            mana = max_mana
        if level == None:
            level = 1
        elif level < 100:
            level = 100
        if exp == None:
            exp = 0
        self.race = race
        self.name = name
        self.strength = strength
        self.defense = defense
        self.max_health = max_health
        self.health = health
        self.max_mana = max_mana
        self.mana = mana
        self.speed = speed
        self.held_item = held_item
        self.level = level
        self.exp = exp
        self.main_character = main_character
    def __str__(self):
        return f"{self.name}" + (f"" if self.main_character == False else "(You)") + f" - Lvl{self.level} {self.race.capitalize()} ({self.health}/{self.max_health}) HP|({self.mana}/{self.max_mana}) MP|{self.strength} ATK|{self.speed} SPD"

def adven_gen(race:str = None, name:str = None, strength:int = None, defense:int = None, max_health:int = None, max_mana:int = None, speed:int = None, held_item:int = None, level:int = None, exp = None):
    if DEBUG:
        print("DEBUG: Creating new Adventurer.")
    return Adventurer(race, name, strength, defense, max_health, None, max_mana, None, speed, held_item, level, exp)

def adven_list_append(adventurer:Adventurer):
    adventurer_list.append(adventurer)

# Gatcha
gatcha_list = []

def gatcha():
    if inventory["gatcha_ticket"][0] >= 10:
        inventory["gatcha_ticket"][0] -= 10
        fprint("It works!")
    else:
        fprint(f"You need 10 {inventory['gatcha_ticket'][1]}s to gamble. You only have {inventory['gatcha_ticket'][0]}")

# Level Up
def next_level_exp(level):
    return int(base_exp*(1.05**level))

def levelup(adven:Adventurer):
    if adven.exp >= next_level_exp(adven.level):
        adven.exp -= next_level_exp(adven.level)
        adven.level += 1
        if adven.race in race_list:
            if adven.race == "human":
                fprint(f"{adven.name} leveled up to Lvl {adven.level}! The following stats have improved:")
                # Strength increase
                new_strength = adven.strength + random.randint(1,2)
                print(f"Strength: {adven.strength} -> {new_strength}")
                adven.strength = new_strength
                # Defense increase
                new_defense = adven.defense + random.randint(1,2)
                print(f"Defense: {adven.defense} -> {new_defense}")
                adven.defense = new_defense
                # Health increase
                new_health = random.randint(3,5)
                print(f"Max Health: {adven.max_health} -> {adven.max_health + new_health}")
                adven.max_health += new_health
                adven.health += new_health
                # Mana increase
                new_mana = random.randint(1,3)
                print(f"Max Mana: {adven.max_mana} -> {adven.max_mana + new_mana}")
                adven.max_mana += new_mana
                adven.mana += new_mana
                # Speed increase
                new_speed = adven.speed + random.randint(2,4)
                print(f"Speed: {adven.speed} -> {new_speed}")
                adven.speed = new_speed
            elif adven.race == "demonkin":
                fprint(f"{adven.name} leveled up to Lvl {adven.level}! The following stats have improved:")
                # Strength increase
                new_strength = adven.strength + random.randint(1,2)
                print(f"Strength: {adven.strength} -> {new_strength}")
                adven.strength = new_strength
                # Defense increase
                new_defense = adven.defense + random.randint(1,2)
                print(f"Defense: {adven.defense} -> {new_defense}")
                adven.defense = new_defense
                # Health increase
                new_health = random.randint(2,4)
                print(f"Max Health: {adven.max_health} -> {adven.max_health + new_health}")
                adven.max_health += new_health
                adven.health += new_health
                # Mana increase
                new_mana = random.randint(2,4)
                print(f"Max Mana: {adven.max_mana} -> {adven.max_mana + new_mana}")
                adven.max_mana += new_mana
                adven.mana += new_mana
                # Speed increase
                new_speed = adven.speed + random.randint(2,4)
                print(f"Speed: {adven.speed} -> {new_speed}")
                adven.speed = new_speed
            elif adven.race == "elf":
                fprint(f"{adven.name} leveled up to Lvl {adven.level}! The following stats have improved:")
                # Strength increase
                new_strength = adven.strength + random.randint(0,1)
                print(f"Strength: {adven.strength} -> {new_strength}")
                adven.strength = new_strength
                # Defense increase
                new_defense = adven.defense + random.randint(1,2)
                print(f"Defense: {adven.defense} -> {new_defense}")
                adven.defense = new_defense
                # Health increase
                new_health = random.randint(2,4)
                print(f"Max Health: {adven.max_health} -> {adven.max_health + new_health}")
                adven.max_health += new_health
                adven.health += new_health
                # Mana increase
                new_mana = random.randint(3,5)
                print(f"Max Mana: {adven.max_mana} -> {adven.max_mana + new_mana}")
                adven.max_mana += new_mana
                adven.mana += new_mana
                # Speed increase
                new_speed = adven.speed + random.randint(2,5)
                print(f"Speed: {adven.speed} -> {new_speed}")
                adven.speed = new_speed
            elif adven.race == "orc":
                fprint(f"{adven.name} leveled up to Lvl {adven.level}! The following stats have improved:")
                # Strength increase
                new_strength = adven.strength + random.randint(1,3)
                print(f"Strength: {adven.strength} -> {new_strength}")
                adven.strength = new_strength
                # Defense increase
                new_defense = adven.defense + random.randint(1,2)
                print(f"Defense: {adven.defense} -> {new_defense}")
                adven.defense = new_defense
                # Health increase
                new_health = random.randint(5,8)
                print(f"Max Health: {adven.max_health} -> {adven.max_health + new_health}")
                adven.max_health += new_health
                adven.health += new_health
                # Mana increase
                new_mana = random.randint(0,2)
                print(f"Max Mana: {adven.max_mana} -> {adven.max_mana + new_mana}")
                adven.max_mana += new_mana
                adven.mana += new_mana
                # Speed increase
                new_speed = adven.speed + random.randint(0,2)
                print(f"Speed: {adven.speed} -> {new_speed}")
                adven.speed = new_speed
            print()
        else:
            if DEBUG:
                print("DEBUG: Race not detected. No stats improved.")
    else:
        fprint("Beegor")

x = adven_gen(None,None,None,None,None,None,None,None,None,5000000)
for i in range(1,10):
    levelup(x)

def crit_chance(char:Adventurer, crit_increase:float = None):
    if crit_increase == None:
        crit_increase = 0.0
    chance = (char.strength + char.speed)/10000 + .03 + crit_increase
    x = random.random()
    if DEBUG:
        print(f"DEBUG: crit chance is {chance} and result is {x}.")
    if x <= chance:
        return True
    else:
        return False

def battle_dmg(char:Adventurer, attack:int, defense:int, attack_modifier:float = None, defense_modifier:float = None, blessing:float = None):
    n = random.choice([-1,1])
    if attack_modifier == None:
        attack_modifier = 1.0
    if defense_modifier == None:
        defense_modifier = 1.0
    if blessing == None:
        blessing = 1.0
    crit = crit_chance(char)
    if crit == False:
        damage = int(blessing*(((attack_modifier)*(attack/2) - (defense_modifier)*(defense/4)) + n*(attack/2 - defense/4)/16))
        if damage < 1:
            damage = 1
        print(f"{char.name} hit the opponent for {damage} damage.")
    else:
        damage = int(blessing*((attack_modifier)*(attack) - (defense_modifier)*(defense/4)))
        if damage < 1:
            damage = 1
        print(f"Eureka! {char.name} struck a critical hit on the opponent for {damage} damage!")
    return damage

def equip_inv():
    empty_inv = True
    for item in equip_list:
        if equip_list[item][0] != 0:
            empty_inv = False
            print(equip_list[item][1])
    if empty_inv == True:
        print("You don't have any equipment.")
