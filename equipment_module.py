import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style
import pygame

init(autoreset=True)

all_game_weapons = []
all_ground_game_weapons = []
all_game_armor = []
all_ground_game_armor = []
all_game_helmets = []
all_ground_game_helmets = []
all_game_shields = []
all_ground_game_shields = []

#ITEM IDS SERVE NO PURPOSE!

spr_att_fire = pygame.image.load("sprites/icons/icon_fire1.png")
spr_att_water = pygame.image.load("sprites/icons/icon_water1.png")
spr_att_air = pygame.image.load("sprites/icons/icon_air1.png")
spr_att_earth = pygame.image.load("sprites/icons/icon_earth1.png")

spr_att_undead = pygame.image.load("sprites/icons/icon_fire1.png")
spr_att_holy = pygame.image.load("sprites/icons/icon_water1.png")
spr_att_slime = pygame.image.load("sprites/icons/icon_air1.png")
spr_att_ice = pygame.image.load("sprites/icons/icon_earth1.png")

class Weapon:
    def __init__(self, id, name, value, type, level, attribute, magic_bonus, strength_bonus, attack_bonus, defence_bonus, maxhp_bonus):
        self.id = id
        self.name = name

        self.value = value
        self.type = type
        self.level = level
        self.attribute = attribute
        self.magic_bonus = magic_bonus
        self.strength_bonus = strength_bonus
        self.attack_bonus = attack_bonus
        self.defence_bonus = defence_bonus
        self.maxhp_bonus = maxhp_bonus
        self.amount = 1
        self.print_attribute = ""
        self.attribute_sprite = spr_att_fire

        if self.attribute == "fire":
            self.print_attribute = (Fore.RED + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_fire
        if self.attribute == "water":
            self.print_attribute = (Fore.BLUE + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_water
        if self.attribute == "earth":
            self.print_attribute = (Fore.GREEN + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_earth
        if self.attribute == "air":
            self.print_attribute = (Fore.BLACK + Style.BRIGHT + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_air
        if self.attribute == "holy":
            self.print_attribute = (Fore.YELLOW + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_holy
        if self.attribute == "undead":
            self.print_attribute = (Fore.MAGENTA + Style.DIM + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_undead
        if self.attribute == "slime":
            self.print_attribute = (Fore.GREEN + Style.BRIGHT + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_slime
        if self.attribute == "ice":
            self.print_attribute = (Fore.CYAN + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_ice

        self.print_name = (Fore.BLACK + Style.BRIGHT + name + Style.RESET_ALL)

        all_game_weapons.append(self)

bird_sword = Weapon(201,"bird sword",3,"sword",5,"air",5,9,15,12,1000)
super_bird_sword = Weapon(202,"super bird sword",180,"sword",50,"air",0,500,500,500,1000)

wooden_staff = Weapon(204,"wooden staff",80,"staff",3,"earth",10,2,2,20,0)
tall_staff = Weapon(204,"tall staff",80,"staff",5,"fire",22,4,4,25,100)
iron_knife = Weapon(203,"iron knife",1,"sword",2,"water",0,8,8,1,1)
iron_spear = Weapon(203,"iron spear",2,"spear",2,"earth",0,14,2,12,1)
iron_dagger = Weapon(203,"iron dagger",2,"dagger",2,"air",0,8,18,2,1)

long_spear = Weapon(203,"long spear",2,"spear",2,"water",0,14,2,12,1)
short_dagger = Weapon(203,"short dagger",2,"dagger",2,"fire",0,8,18,2,1)
staff_of_air = Weapon(204,"staff of air",80,"staff",5,"air",20,2,2,20,0)
staff_of_fire = Weapon(204,"staff of fire",80,"staff",5,"fire",20,2,2,20,0)
staff_of_earth = Weapon(204,"staff of earth",80,"staff",5,"earth",20,2,2,20,0)
staff_of_ice = Weapon(204,"staff of ice",80,"staff",5,"ice",20,2,2,20,0)

steel_spear = Weapon(204,"steel spear",80,"spear",10,"earth",0,18,24,28,0)

iron_sword = Weapon(203,"iron sword",2,"sword",2,"earth",0,10,10,10,1)
steel_sword = Weapon(204,"steel sword",80,"sword",10,"earth",0,20,20,20,0)
mithril_sword = Weapon(204,"mithril sword",80,"sword",15,"water",0,30,30,30,0)
adamantite_sword = Weapon(204,"adamantite sword",80,"sword",20,"earth",0,40,40,40,0)
rune_sword = Weapon(204,"rune sword",80,"sword",25,"holy",0,50,50,50,0)

iron_axe = Weapon(205,"iron axe",8,"axe",5,"earth",0,10,10,10,0)
steel_axe = Weapon(206,"steel axe",80,"axe",10,"earth",0,20,20,20,0)
mithril_axe = Weapon(206,"mithril axe",80,"axe",15,"water",0,30,30,30,0)
adamantite_axe = Weapon(206,"adamantite axe",80,"axe",20,"earth",0,40,40,40,0)
rune_axe = Weapon(206,"rune axe",80,"axe",25,"holy",0,50,50,50,0)

greatsword = Weapon(207,"greatsword",800,"large sword",32,"water",0,40,40,40,0)
ultra_greatsword = Weapon(208,"ultra greatsword",8000,"large sword",54,"water",0,60,60,60,0)
war_spear = Weapon(209,"war spear",80,"spear",16,"fire",70,20,20,20,0)
lance = Weapon(210,"lance",80,"spear",28,"air",100,30,30,30,0)

bone_scimitar = Weapon(211,"bone scimitar",80000,"sword",320,"undead",10,100,200,0,0)
gladius = Weapon(212,"gladius",8000,"sword",120,"holy",5,50,50,200,0)
battle_axe = Weapon(213,"battle axe",6000,"axe",160,"fire",0,220,120,50,0)
warhammer = Weapon(214,"warhammer",5600,"hammer",280,"earth",0,250,60,22,0)


class Armor:
    def __init__(self, id, name, value, type, level, attribute, magic_bonus, strength_bonus, attack_bonus, defence_bonus, maxhp_bonus):
        self.id = id
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)
        self.value = value
        self.type = type
        self.level = level
        self.attribute = attribute
        self.magic_bonus = magic_bonus
        self.strength_bonus = strength_bonus
        self.attack_bonus = attack_bonus
        self.defence_bonus = defence_bonus
        self.maxhp_bonus = maxhp_bonus
        self.amount = 1

        self.print_attribute = ""
        self.attribute_sprite = spr_att_fire

        if self.attribute == "fire":
            self.print_attribute = (Fore.RED + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_fire
        if self.attribute == "water":
            self.print_attribute = (Fore.BLUE + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_water
        if self.attribute == "earth":
            self.print_attribute = (Fore.GREEN + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_earth
        if self.attribute == "air":
            self.print_attribute = (Fore.BLACK + Style.BRIGHT + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_air
        if self.attribute == "holy":
            self.print_attribute = (Fore.YELLOW + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_holy
        if self.attribute == "undead":
            self.print_attribute = (Fore.MAGENTA + Style.DIM + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_undead
        if self.attribute == "slime":
            self.print_attribute = (Fore.GREEN + Style.BRIGHT + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_slime
        if self.attribute == "ice":
            self.print_attribute = (Fore.CYAN + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_ice


        all_game_armor.append(self)

birdshirt = Armor(301,"bird t shirt",100,"light",99,"air",100,240,220,400,11000)

cloth_armor = Armor(302,"cloth armor",10,"light",4,"water",0,0,0,4,20)
bronze_armor = Armor(302,"bronze plate armor",50,"heavy",5,"earth",0,8,8,12,100)
dusty_robes = Armor(302,"dusty robes",50,"mage",8,"water",10,0,0,5,50)
cloth_robes = Armor(309,"cloth robes",100,"mage",12,"water",24,0,0,8,50)
heavy_robes = Armor(309,"heavy robes",100,"mage",13,"earth",20,0,0,15,100)

leather_armor = Armor(302,"leather armor",50,"light",9,"water",2,4,4,5,40)
hard_leather_armor = Armor(303,"hard leather armor",90,"light",10,"water",2,5,20,10,50)

iron_chain_mail = Armor(304,"iron chain mail",40,"heavy",12,"earth",0,7,14,17,50)
iron_plate_armor = Armor(305,"iron plate armor",100,"heavy",15,"earth",0,11,9,22,500)

steel_chain_mail = Armor(306,"steel chain mail",400,"heavy",14,"earth",0,13,18,25,100)
steel_plate_armor = Armor(307,"steel plate armor",1000,"heavy",22,"earth",0,16,15,28,1000)

rags = Armor(308,"rags",1,"light",1,"fire",15,1,1,1,1)

mage_robes = Armor(309,"mage robes",1000,"mage",20,"air",50,0,0,20,1000)
necro_robes = Armor(309,"necromancer robes",1000,"mage",44,"air",55,0,0,50,2000)


class Helmet:
    def __init__(self, id, name, value, type, level, attribute, magic_bonus, strength_bonus, attack_bonus, defence_bonus, maxhp_bonus):
        self.id = id
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)
        self.value = value
        self.type = type
        self.level = level
        self.attribute = attribute
        self.magic_bonus = magic_bonus
        self.strength_bonus = strength_bonus
        self.attack_bonus = attack_bonus
        self.defence_bonus = defence_bonus
        self.maxhp_bonus = maxhp_bonus
        self.amount = 1

        self.print_attribute = ""
        self.attribute_sprite = spr_att_fire

        if self.attribute == "fire":
            self.print_attribute = (Fore.RED + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_fire
        if self.attribute == "water":
            self.print_attribute = (Fore.BLUE + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_water
        if self.attribute == "earth":
            self.print_attribute = (Fore.GREEN + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_earth
        if self.attribute == "air":
            self.print_attribute = (Fore.BLACK + Style.BRIGHT + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_air
        if self.attribute == "holy":
            self.print_attribute = (Fore.YELLOW + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_holy
        if self.attribute == "undead":
            self.print_attribute = (Fore.MAGENTA + Style.DIM + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_undead
        if self.attribute == "slime":
            self.print_attribute = (Fore.GREEN + Style.BRIGHT + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_slime
        if self.attribute == "ice":
            self.print_attribute = (Fore.CYAN + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_ice


        all_game_helmets.append(self)

bird_hat = Helmet(301,"bird hat",100,"light",99,"air",10,24,22,40,1100)

wizard_hat = Helmet(301,"wizard hat",60,"mage",6,"air",10,0,0,1,0)
leather_cap = Helmet(301,"leather cap",100,"light",6,"earth",0,0,0,5,20)
bronze_helmet = Helmet(301,"bronze helmet",60,"heavy",8,"earth",0,0,0,8,50)

iron_helmet = Helmet(301,"iron helmet",100,"heavy",9,"air",1,2,2,10,100)
steel_helmet = Helmet(301,"steel helmet",100,"heavy",18,"air",1,4,2,20,500)
mage_hood = Helmet(301,"mage hood",100,"mage",70,"air",100,0,0,40,1000)


class Shield:
    def __init__(self, id, name, value, type, level, attribute, magic_bonus, strength_bonus, attack_bonus, defence_bonus, maxhp_bonus):
        self.id = id
        self.name = name
        self.print_name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)
        self.value = value
        self.type = type
        self.level = level
        self.attribute = attribute
        self.magic_bonus = magic_bonus
        self.strength_bonus = strength_bonus
        self.attack_bonus = attack_bonus
        self.defence_bonus = defence_bonus
        self.maxhp_bonus = maxhp_bonus
        self.amount = 1

        self.print_attribute = ""
        self.attribute_sprite = spr_att_fire

        if self.attribute == "fire":
            self.print_attribute = (Fore.RED + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_fire
        if self.attribute == "water":
            self.print_attribute = (Fore.BLUE + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_water
        if self.attribute == "earth":
            self.print_attribute = (Fore.GREEN + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_earth
        if self.attribute == "air":
            self.print_attribute = (Fore.BLACK + Style.BRIGHT + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_air
        if self.attribute == "holy":
            self.print_attribute = (Fore.YELLOW + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_holy
        if self.attribute == "undead":
            self.print_attribute = (Fore.MAGENTA + Style.DIM + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_undead
        if self.attribute == "slime":
            self.print_attribute = (Fore.GREEN + Style.BRIGHT + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_slime
        if self.attribute == "ice":
            self.print_attribute = (Fore.CYAN + Style.NORMAL + attribute + Style.RESET_ALL)
            self.attribute_sprite = spr_att_ice


        all_game_shields.append(self)

bird_shield = Shield(301,"bird shield",100,"light",99,"air",10,24,22,40,1100)
iron_square_shield = Shield(301,"iron square shield",100,"heavy",9,"air",1,2,2,10,200)
steel_square_shield = Shield(301,"steel square shield",100,"heavy",18,"air",1,4,2,20,500)
mage_book = Shield(301,"mage book",100,"light",99,"air",100,0,0,40,1000)

wooden_round_shield = Shield(301,"wooden round shield",100,"light",1,"air",0,0,0,5,50)
magic_orb = Shield(301,"magic orb",100,"light",1,"air",30,0,0,0,0)

buckler = Shield(301,"buckler",500,"light",5,"air",0,0,0,10,100)
red_magic_gem = Shield(301,"red magic gem",1000,"light",5,"fire",50,40,0,0,0)
green_magic_gem = Shield(301,"green magic gem",1000,"light",5,"earth",40,10,10,10,0)
blue_magic_gem = Shield(301,"blue magic gem",1000,"light",5,"water",40,0,0,40,1000)
