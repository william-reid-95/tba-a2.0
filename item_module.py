import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

all_game_items = []
all_ground_game_items = []

class Item:
    def __init__(self, id, name, value, edible, poisonous, is_fish, is_raw, is_herb, hp, item_desc, ingredient_name):
        self.id = id
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + name + Style.RESET_ALL)
        self.value = value
        self.edible = edible
        self.poisonous = poisonous

        self.is_fish = is_fish
        self.is_raw = is_raw
        self.is_herb = is_herb
        self.hp = hp
        self.item_desc = item_desc

        self.ingredient_name = ingredient_name

        self.amount = 1
        self.item_weight = 1 * self.amount
        
#ITEM IDS SERVE NO PURPOSE!

#unique items:

    #rope is unique item used to travel down and up on the z axis below 0
rope = Item(109,"rope",120,False,False,False,False,False,0,"","")
all_game_items.append(rope)
    #tent allows player to use "camp" command to heal fully, late game item.
tent = Item(108,"tent",200,False,False,False,False,False,8,"","")
all_game_items.append(tent)
    #torch changes description text in dark enviroments, need to implement encounter rate change at night and in dark areas
torch = Item(110,"torch",80,False,False,False,False,False,0,"","")
all_game_items.append(torch)

woodcutting_axe = Item(110,"woodcutting axe",80,False,False,False,False,False,0,"","")
all_game_items.append(woodcutting_axe)

fishing_rod = Item(110,"fishing rod",80,False,False,False,False,False,0,"","")
all_game_items.append(fishing_rod)

wood = Item(110,"wood",2,False,False,False,False,False,0,"","")
all_game_items.append(wood)

tinder_box = Item(110,"tinder box",2,False,False,False,False,False,0,"","")
all_game_items.append(tinder_box)
#########################################

#edible poisonous items
apple = Item(100,"apple",5,True,True,False,False,False,1000,"","")
all_game_items.append(apple)
rotten_food = Item(100,"rotten food",1,True,True,False,False,False,100,"","")
all_game_items.append(rotten_food)

#edible healing items
pear = Item(101,"pear",20,True,False,False,False,False,300,"","")
all_game_items.append(pear)
cabbage = Item(101,"cabbage",2,True,False,False,False,False,10,"","")
all_game_items.append(cabbage)
turnip = Item(101,"turnip",5,True,False,False,False,False,50,"","")
all_game_items.append(turnip)
banana = Item(101,"banana",15,True,False,False,False,False,150,"","")
all_game_items.append(banana)
pineapple = Item(101,"pineapple",18,True,False,False,False,False,300,"","")
all_game_items.append(pineapple)
mushroom = Item(101,"mushroom",2,True,True,False,False,False,500,"","")
all_game_items.append(mushroom)
magic_mushroom = Item(101,"magic mushroom",50,True,False,False,False,False,1000,"","")
all_game_items.append(magic_mushroom)

mushroom_tea = Item(108,"cup of mushroom tea",20,True,False,False,False,False,800,"","")
all_game_items.append(mushroom_tea)
mushroom_brew = Item(108,"mushroom brew",28,True,False,False,False,False,8250,"","")
all_game_items.append(mushroom_brew)
cup = Item(104,"cup",12,False,False,False,False,False,0,"","")
all_game_items.append(cup)
mug = Item(104,"mug",12,False,False,False,False,False,0,"","")
all_game_items.append(mug)
tea_bag = Item(107,"tea bag",1,False,False,False,False,False,0,"","")
all_game_items.append(tea_bag)
cup_of_tea = Item(108,"cup of tea",5,True,False,False,False,False,800,"","")
all_game_items.append(cup_of_tea)


meat = Item(111,"meat",5,True,False,False,False,False,500,"a piece of cooked meat","")
all_game_items.append(meat)

hp_potion = Item(111,"hp potion",20,True,False,False,False,False,1000,"","")
all_game_items.append(hp_potion)
super_hp_potion = Item(111,"super hp potion",200,True,False,False,False,False,10000,"","")
all_game_items.append(super_hp_potion)

#fish

raw_fish_salmon = Item(111,"raw salmon",2000,False,False,True,True,False,10000,"","")
all_game_items.append(raw_fish_salmon)
raw_fish_trout = Item(111,"raw trout",1200,False,False,True,True,False,2200,"","")
all_game_items.append(raw_fish_trout)
raw_fish_herring = Item(111,"raw herring",200,False,False,True,True,False,1000,"","")
all_game_items.append(raw_fish_herring)
raw_fish_baron_maryan = Item(111,"raw baron maryan",50000,False,False,True,True,False,150000,"","")
all_game_items.append(raw_fish_baron_maryan)


fish_salmon = Item(111,"salmon",2000,True,False,False,False,False,10000,"","raw salmon")
all_game_items.append(fish_salmon)
fish_trout = Item(111,"trout",1200,True,False,False,False,False,2200,"","raw trout")
all_game_items.append(fish_trout)
fish_herring = Item(111,"herring",200,True,False,False,False,False,1000,"","raw herring")
all_game_items.append(fish_herring)
fish_baron_maryan = Item(111,"baron maryan",50000,True,False,False,False,False,150000,"","raw baron maryan")
all_game_items.append(fish_baron_maryan)

#??? items:
fire_orb = Item(106,"fire orb",1000,False,False,False,False,False,0,"","")
all_game_items.append(fire_orb)
water_orb = Item(106,"water orb",900,False,False,False,False,False,0,"","")
all_game_items.append(water_orb)
earth_orb = Item(106,"earth orb",800,False,False,False,False,False,0,"","")
all_game_items.append(earth_orb)
air_orb = Item(106,"air orb",700,False,False,False,False,False,0,"","")
all_game_items.append(air_orb)

bones = Item(112,"bones",2,False,False,False,False,False,0,"","")
all_game_items.append(bones)
worms = Item(102,"worms",500,False,False,False,False,False,0,"","")
all_game_items.append(worms)

#key items:
beak_polish = Item(103,"beak polish",10,False,False,False,False,False,0,"","")
all_game_items.append(beak_polish)
pendant = Item(105,"pendant",80,False,False,False,False,False,0,"","")
all_game_items.append(pendant)
legion_seal = Item(106,"legion seal",7,False,False,False,False,False,0,"","")
all_game_items.append(legion_seal)
oak_key = Item(106,"oak key",7,False,False,False,False,False,0,"","")
all_game_items.append(oak_key)
jail_key = Item(106,"jail key",7,False,False,False,False,False,0,"","")
all_game_items.append(jail_key)
certificate_of_passage = Item(106,"certificate of passage",100,False,False,False,False,False,0,"","")
all_game_items.append(certificate_of_passage)
