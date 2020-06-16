import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style
import pygame

pygame.init()
init(autoreset=True)

from item_module import *
from equipment_module import *
from spell_module import *

all_game_enemies = []

spr_no_sprite = pygame.image.load("sprites/enemy/no_sprite1.png")

spr_goblin = pygame.image.load("sprites/enemy/goblin1.png")
spr_goblin2 = pygame.image.load("sprites/enemy/goblin2.png")
spr_ghost = pygame.image.load("sprites/enemy/ghost1.png")
spr_imp = pygame.image.load("sprites/enemy/imp1.png")
spr_imp2 = pygame.image.load("sprites/enemy/imp2.png")
spr_wolf = pygame.image.load("sprites/enemy/wolf1.png")
spr_ice_wolf = pygame.image.load("sprites/enemy/ice_wolf1.png")

spr_cow = pygame.image.load("sprites/enemy/cow1.png")
spr_sheep = pygame.image.load("sprites/enemy/sheep1.png")

spr_fire_ele = pygame.image.load("sprites/enemy/fire_ele1.png")
spr_air_ele = pygame.image.load("sprites/enemy/air_ele1.png")
spr_water_ele = pygame.image.load("sprites/enemy/water_ele1.png")
spr_earth_ele = pygame.image.load("sprites/enemy/earth_ele1.png")

spr_cast1 = [pygame.image.load("sprites/combat_animations/spell_cast1.png"),pygame.image.load("sprites/combat_animations/spell_cast2.png"),pygame.image.load("sprites/combat_animations/spell_cast3.png"),pygame.image.load("sprites/combat_animations/spell_cast4.png"),pygame.image.load("sprites/combat_animations/spell_cast5.png"),]
spr_cast_fire1 = [pygame.image.load("sprites/combat_animations/fire1.png"),pygame.image.load("sprites/combat_animations/fire2.png"),pygame.image.load("sprites/combat_animations/fire3.png"),pygame.image.load("sprites/combat_animations/fire4.png"),pygame.image.load("sprites/combat_animations/fire5.png"),]



class enemy_stats:
    def __init__(self, is_npc, name, level, xp, hp, maxhp, mp, maxmp, magic, strength, attack, defence, gp, attribute, weakness, spellbook, drop_table_items_always, drop_table_weapons_always, drop_table_armor_always, drop_table_helmets_always, drop_table_shields_always, status_effect, sprite_variable):
        self.is_npc = is_npc
        self.name = name
        self.level = level
        self.xp = xp
        self.hp = hp
        self.maxhp = maxhp
        self.mp = mp
        self.maxmp = maxmp
        self.gp = gp
        self.magic = magic
        self.strength = strength
        self.attack = attack
        self.defence = defence
        self.gp = gp
        self.attribute = attribute
        self.weakness = weakness
        self.spellbook = spellbook
        self.drop_table_items_always = drop_table_items_always
        self.drop_table_weapons_always = drop_table_weapons_always
        self.drop_table_armor_always = drop_table_armor_always
        self.drop_table_helmets_always = drop_table_helmets_always
        self.drop_table_shields_always = drop_table_shields_always

        self.drop_table_items = []
        self.drop_table_weapons = []
        self.drop_table_armor = []
        self.drop_table_helmets = []
        self.drop_table_shields = []

        self.status_effect = status_effect
        self.sprite_variable = sprite_variable
        self.enemy_sprite = spr_no_sprite
        self.status_effect_list = []
        self.cast_sprite = spr_cast1

        self.is_active = False
        self.print_name = (Fore.RED + Style.DIM + self.name + Style.RESET_ALL)

        if self.attribute == "fire":
            self.print_attribute = (Fore.RED + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "water":
            self.print_attribute = (Fore.BLUE + Style.BRIGHT + attribute + Style.RESET_ALL)
        if self.attribute == "earth":
            self.print_attribute = (Fore.GREEN + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "air":
            self.print_attribute = (Fore.BLACK + Style.BRIGHT + attribute + Style.RESET_ALL)
        if self.attribute == "holy":
            self.print_attribute = (Fore.YELLOW + Style.NORMAL + attribute + Style.RESET_ALL)
        if self.attribute == "undead":
            self.print_attribute = (Fore.MAGENTA + Style.DIM + attribute + Style.RESET_ALL)
        if self.attribute == "slime":
            self.print_attribute = (Fore.GREEN + Style.BRIGHT + attribute + Style.RESET_ALL)
        if self.attribute == "ice":
            self.print_attribute = (Fore.CYAN + Style.BRIGHT + attribute + Style.RESET_ALL)

        if sprite_variable == "imp":
            self.enemy_sprite = spr_imp
        if sprite_variable == "imp2":
            self.enemy_sprite = spr_imp2
        if sprite_variable == "goblin":
            self.enemy_sprite = spr_goblin
        if sprite_variable == "goblin2":
            self.enemy_sprite = spr_goblin2
        if sprite_variable == "ghost":
            self.enemy_sprite = spr_ghost
        if sprite_variable == "cow":
            self.enemy_sprite = spr_cow
        if sprite_variable == "sheep":
            self.enemy_sprite = spr_sheep
        if sprite_variable == "fire_ele":
            self.enemy_sprite = spr_fire_ele
        if sprite_variable == "air_ele":
            self.enemy_sprite = spr_air_ele
        if sprite_variable == "water_ele":
            self.enemy_sprite = spr_water_ele
        if sprite_variable == "earth_ele":
            self.enemy_sprite = spr_earth_ele
        if sprite_variable == "wolf":
            self.enemy_sprite = spr_wolf
        if sprite_variable == "ice_wolf":
            self.enemy_sprite = spr_ice_wolf


        all_game_enemies.append(self)

# Attributes: name, level, xp, hp, maxhp, mp, maxmp, magic, strength, attack, defence, gp, attribute, weakness,
# Lists: spellbook, drop_table_items, drop_table_weapons, drop_table_armor, drop_table_helmets, drop_table_shields,
# Status: status_effect

imp = enemy_stats(False,"imp",2,2,400,400,100,100,1,16,16,1,1,"fire","holy",[],[bones],[],[],[],[],0,"imp")
goon = enemy_stats(False,"goon",2,3,300,300,100,100,1,16,14,8,4,"earth","fire",[],[bones],[],[],[],[],0,"imp")
big_rat = enemy_stats(False,"big rat",2,3,100,100,100,100,10,16,14,8,4,"water","fire",[],[meat,bones],[],[],[],[],0,"imp2")
hawk = enemy_stats(False,"hawk",3,3,50,50,100,100,10,26,24,1,4,"air","fire",[],[meat,bones],[],[],[],[],0,"imp2")

wolf = enemy_stats(False,"mangy wolf",4,4,150,150,100,100,1,17,16,8,8,"earth","water",[],[meat,bones],[],[],[],[],0,"wolf")
ice_wolf = enemy_stats(False,"ice wolf",5,4,200,200,100,100,1,17,16,8,100,"ice","fire",[],[meat,bones],[wooden_staff],[],[],[],0,"ice_wolf")

goblin = enemy_stats(False,"goblin",6,5,80,80,100,100,11,12,10,10,11,"earth","fire",[],[bones],[wooden_staff,tall_staff,staff_of_earth,iron_axe],[],[],[],0,"goblin")
hobgoblin = enemy_stats(False,"hobgoblin",7,12,100,100,100,100,8,10,5,10,12,"earth","fire",[],[bones],[wooden_staff,iron_knife,staff_of_earth,short_dagger],[],[],[],0,"goblin2")
hobgoblin_berzerker = enemy_stats(False,"hobgoblin berzerker",8,22,1000,1000,100,100,1,12,10,30,300,"earth","fire",[],[bones],[wooden_staff,tall_staff,staff_of_earth,iron_dagger],[],[],[],0,"goblin2")

bandit = enemy_stats(False,"bandit",9,10,2000,2000,1000,1000,1,12,6,18,100,"fire","earth",[],[bones],[iron_sword,iron_dagger],[],[],[],0,"")
bandit_warlock = enemy_stats(False,"bandit warlock",10,28,2000,2000,5000,5000,18,5,2,18,70,"fire","earth",[],[bones],[tall_staff],[],[],[],0,"")
bandit_henchman = enemy_stats(False,"bandit henchman",11,50,2000,2000,2200,2200,10,12,4,18,230,"fire","earth",[],[bones],[steel_sword,steel_axe],[],[],[],0,"")

legion_soldier = enemy_stats(False,"legion soldier",12,500,10000,10000,100,100,10,14,20,100,1000,"air","earth",[],[bones],[],[],[],[],0,"")
legion_spearman = enemy_stats(False,"legion spearman",13,500,10500,10500,100,100,10,16,10,100,1050,"air","earth",[],[bones],[],[],[],[],0,"")
legion_archer = enemy_stats(False,"legion archer",14,500,8700,8700,100,100,10,11,22,100,654,"air","earth",[],[bones],[],[],[],[],0,"")
legion_battle_mage = enemy_stats(False,"legion battle mage",15,500,12400,12400,1000,1000,45,5,6,100,2245,"air","earth",[],[bones],[],[],[],[],0,"")

elf_warrior = enemy_stats(False,"elf warrior",16,100,15000,15000,2000,2000,10,20,22,100,100,"earth","fire",[],[bones],[],[],[],[],0,"")
elf_mage = enemy_stats(False,"elf mage",17,500,18400,18400,10000,10000,65,5,6,100,3245,"earth","fire",[],[bones],[],[],[],[],0,"")
elf_thief = enemy_stats(False,"elf thief",18,500,18800,18800,1000,1000,5,50,60,100,3245,"earth","fire",[],[bones],[],[],[],[],0,"")

mossy_giant = enemy_stats(False,"mossy giant",19,1000,22400,22400,10000,10000,65,80,10,200,3245,"earth","fire",[],[bones],[],[],[],[],0,"")

giant_wasp = enemy_stats(False,"giant wasp",20,500,12800,12800,1000,1000,5,50,60,200,3245,"earth","fire",[],[bones],[],[],[],[],0,"")
fire_demon = enemy_stats(False,"fire demon",21,500,14800,14800,1000,1000,50,50,60,120,3245,"fire","water",[],[bones],[],[],[],[],0,"")

elf_ranger = enemy_stats(False,"elf ranger",22,500,18800,18800,1000,1000,50,52,63,100,3245,"earth","fire",[],[bones],[],[],[],[],0,"")
elf_necromancer = enemy_stats(False,"elf necromancer",23,500,16200,16200,1000,1000,60,22,33,100,3245,"earth","holy",[],[bones],[],[],[],[],0,"")

ice_golem = enemy_stats(False,"ice golem",24,800,11230,11230,100,100,0,52,22,500,2230,"ice","fire",[],[],[],[],[],[],0,"")
rock_golem = enemy_stats(False,"rock golem",25,800,10520,10520,100,100,0,55,18,500,20230,"earth","water",[],[],[],[],[],[],0,"")
mushroom_man = enemy_stats(False,"mushroom man",26,800,10230,10230,100,100,0,50,20,500,10230,"earth","fire",[],[],[],[],[],[],0,"")
magical_mushroom_man = enemy_stats(False,"magical mushroom man",27,800,10230,10230,100,100,45,20,20,538,10230,"earth","fire",[],[],[],[],[],[],0,"")

bird_warrior = enemy_stats(False,"bird warrior",28,100000,2408070,2408070,1000000,1000000,100,300,220,1000,1000,"air","water",[],[bones],[],[],[],[],0,"")#leg

fire_elemental = enemy_stats(False,"fire elemental",5,200,3200,3200,1000,1000,18,5,2,1,100,"fire","water",[],[],[],[],[],[],0,"fire_ele")
water_elemental = enemy_stats(False,"water elemental",6,200,3800,3800,1000,1000,18,5,2,1,100,"water","earth",[],[],[],[],[],[],0,"water_ele")
earth_elemental = enemy_stats(False,"earth elemental",7,100,3200,3200,1000,1000,13,5,2,1,100,"earth","water",[],[],[],[],[],[],0,"earth_ele")
air_elemental = enemy_stats(False,"air elemental",8,100,3000,3000,1000,1000,13,5,2,1,100,"air","earth",[],[],[],[],[],[],0,"air_ele")

giant_snail = enemy_stats(False,"giant snail",12,10,9300,9300,100,100,0,12,2,100,930,"earth","earth",[],[],[],[],[],[],0,"")
giant_spider = enemy_stats(False,"giant spider",20,64,23000,23000,100,100,0,50,2,70,2300,"earth","fire",[],[],[],[],[],[],0,"")
giant_moth = enemy_stats(False,"giant moth",33,5,13400,13400,100,100,0,10,20,40,100,"earth","air",[],[],[],[],[],[],0,"")

big_slug = enemy_stats(False,"big slug",28,500,1035000,1035000,100,100,0,0,0,1,0,"slime","salt",[],[],[],[],[],[],0,"")#legendary

skeleton_mage = enemy_stats(False,"skeleton mage",32,4202,60070,60070,100,100,53,30,22,600,100,"undead","holy",[],[bones],[],[],[],[],0,"")
skeleton_warrior = enemy_stats(False,"skeleton warrior",33,50922,92070,92070,100,100,0,63,42,700,100,"undead","holy",[],[bones],[],[],[],[],0,"")

## npc enemies

chicken = enemy_stats(True,"chicken",2,2,20,20,10,10,1,8,7,20,200,"fire","holy",[],[meat,bones],[],[],[],[],0,"cow")
cow = enemy_stats(True,"cow",2,2,200,200,100,100,1,8,7,1,100,"fire","holy",[],[meat,bones],[],[],[],[],0,"cow")
sheep = enemy_stats(True,"sheep",2,2,100,100,100,100,1,6,5,1,100,"fire","holy",[],[meat,bones],[],[],[],[],0,"sheep")
town_guard = enemy_stats(True,"town guard",20,20,8000,8000,100,100,1,60,40,10,100,"holy","fire",[],[bones],[],[],[],[],0,"")
