import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

all_game_spells = []
all_game_status_conditions = []

class spell:
    def __init__(self, name, level, mp_cost, value, utility, damage, attribute, xp, effect, aoe_scale, spell_desc,):
        self.name = name
        self.level = level
        self.mp_cost = mp_cost
        self.value = value
        self.utility = utility
        self.damage = damage
        self.attribute = attribute
        self.xp = xp
        self.effect = effect
        self.amount = 1
        self.aoe_scale = aoe_scale
        self.spell_desc = spell_desc

        self.print_name = (Fore.BLACK + Back.WHITE + Style.NORMAL + name + Style.RESET_ALL)

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

        all_game_spells.append(self)

############--COMBAT SPELLS--#############

#### status 0 spells DAMAGE - combat spells, also used for turns where enemy does nothing by doing 0 damage.
slime = spell("slime",5,5,5,True,0,"slime",0,0,0,"slurms mackenzie")

#low level damage spells
fire_bolt = spell("fire bolt",4,25,50,False,80,"fire",100,0,0,"fire damage")
ice_bolt = spell("ice bolt",4,25,50,False,80,"ice",100,0,0,"ice damage")

# arrow spells
fire_arrow = spell("fire arrow",18,50,500,False,80,"fire",100,0,0,"fire damage")
ice_arrow = spell("ice arrow",18,50,500,False,80,"ice",100,0,0,"ice damage")

# tier 1 damage spells
fireball = spell("fireball",30,75,5,False,1000,"fire",200,0,0,"heavy fire damage")
hydro_barrage = spell("hydro barrage",30,75,1000,False,100,"water",200,0,0,"heavy water damage")
holy_surge = spell("holy surge",30,75,1000,False,100,"holy",200,0,0,"heavy holy damage")
necro_surge = spell("necro surge",30,75,1000,False,100,"undead",200,0,0,"heavy undead damage")

# tier 2 damage spells
hydroblast = spell("hydroblast",8,25,250,False,60,"water",100,0,0,"light water damage")
fireblast = spell("fireblast",8,25,250,False,60,"fire",100,0,0,"light fire damage")
windblast = spell("windblast",8,25,250,False,60,"air",100,0,0,"light air damage")
earthblast = spell("earthblast",8,25,250,False,60,"earth",100,0,0,"light earth damage")
necroblast = spell("necroblast",8,25,250,False,60,"undead",100,0,0,"light undead damage")
holyblast = spell("holyblast",8,25,250,False,60,"holy",100,0,0,"light holy damage")

#### status 1 spells HEAL AND DAMAGE
life_drain = spell("life drain",5,5,5,True,100,"undead",50,1,0,"a life draining spell which heals the user")

##################--standard STATUS EFFECTS--##############################

#### status 2 spells FREEZE
snare = spell("snare",5,5,500,True,5,"ice",70,2,0,"snares the enemy in ice")
blizzard = spell("blizzard",5,5,500,False,150,"ice",150,2,0,"freezes the enemy and does lots of damage")
cone_of_cold = spell("cone of cold",5,5,500,False,50,"ice",50,2,0,"freezes the enemy and does damage")

#### status 3 spells POISON
poison = spell("poison",5,5,50,True,5,"earth",70,3,0,"poisons the enemy")

#### status 4 spells BURN
burn = spell("burn",5,5,50,True,5,"fire",70,4,0,"burns the enemy")
mega_burn = spell("mega burn",30,5,5000,False,500,"fire",70,4,0,"MFB")

#### status 5 spells SLEEP
hypnosis = spell("hypnosis",50,5,50,True,5,"water",70,5,0,"puts the enemy to sleep")

#### status 6 spells BADLY POISON
toxic = spell("toxic",22,5,500,True,5,"earth",70,6,0,"badly poisons the enemy")

##############//BUFFS//#########

#### status 10 spells STR UP
str_up = spell("STR UP",5,5,50,True,5,"fire",70,10,0,"STR UP")
str_up_aoe = spell("STR UP aoe",5,5,50,True,5,"fire",70,10,1,"STR UP aoe")
str_up_heal = spell("STR UP and heal",5,5,50,False,5,"fire",70,10,0,"STR UP and heal")
str_up_heal_aoe = spell("STR UP and heal aoe",5,5,50,False,5,"fire",70,10,1,"STR UP and heal aoe")
#### status 11 spells ATK UP
atk_up = spell("ATK UP",5,5,50,True,5,"fire",70,10,0,"ATK UP")
atk_up_aoe = spell("ATK UP aoe",5,5,50,True,5,"fire",70,10,1,"ATK UP aoe")
atk_up_heal = spell("ATK UP and heal",5,5,50,False,5,"fire",70,11,0,"ATK UP and heal")
atk_up_heal_aoe = spell("ATK UP and heal aoe",5,5,50,False,5,"fire",70,11,1,"ATK UP and heal aoe")

#### status 12 spells MGK UP
mgk_up = spell("MGK UP",5,5,50,True,5,"fire",70,10,0,"MGK UP")
mgk_up_aoe = spell("MGK UP aoe",5,5,50,True,5,"fire",70,10,1,"MGK UP aoe")
mgk_up_heal = spell("MGK UP and heal",5,5,50,False,5,"fire",70,12,0,"MGK UP and heal")
mgk_up_heal_aoe = spell("MGK UP and heal aoe",5,5,50,False,5,"fire",70,12,1,"MGK UP and heal aoe")

#### status 13 spells DEF UP
def_up = spell("DEF UP",5,5,50,True,5,"fire",70,10,0,"DEF UP")
def_up_aoe = spell("DEF UP aoe",5,5,50,True,5,"fire",70,10,1,"DEF UP aoe")
def_up_heal = spell("DEF UP and heal",5,5,50,False,5,"fire",70,13,0,"DEF UP and heal")
def_up_heal_aoe = spell("DEF UP and heal aoe",5,5,50,False,5,"fire",70,13,1,"DEF UP and heal aoe")

##############//DE-BUFFS//###################

#### status 20 spells STR down 1
str_down = spell("STR down",5,5,50,True,5,"fire",70,20,0,"STR down")
str_down_aoe = spell("STR down aoe",5,5,50,True,5,"fire",70,20,1,"STR down aoe")
str_down_damage = spell("STR down and damage",5,5,50,False,5,"fire",70,20,0,"STR down and damage")
str_down_damage_aoe = spell("STR down and damage aoe",5,5,50,False,5,"fire",70,20,1,"STR down and damage aoe")

#### status 21 spells ATK down 1
atk_down = spell("ATK down",5,5,50,True,5,"fire",70,10,0,"ATK down")
atk_down_damage = spell("ATK down aoe",5,5,50,True,5,"fire",70,21,0,"ATK down aoe")
atk_down_damage = spell("ATK down and damage",5,5,50,False,5,"fire",70,21,0,"ATK down and damage")
atk_down_damage_aoe = spell("ATK down and damage aoe",5,5,50,False,5,"fire",70,21,1,"ATK down and damage aoe")
#### status 22 spells MGK down 1
mgk_down = spell("MGK down",5,5,50,True,5,"fire",70,10,0,"MGK down")
mgk_down_damage = spell("MGK down aoe",5,5,50,True,5,"fire",70,22,0,"MGK down aoe")
mgk_down_damage = spell("MGK down and damage",5,5,50,False,5,"fire",70,22,0,"MGK down and damage")
mgk_down_damage_aoe = spell("MGK down and damage aoe",5,5,50,False,5,"fire",70,22,1,"MGK down and damage aoe")
#### status 23 spells DEF down 1
def_down = spell("DEF down",5,5,50,True,5,"fire",70,10,0,"DEF down")
def_down_damage = spell("DEF down aoe",5,5,50,True,5,"fire",70,23,0,"DEF down aoe")
def_down_damage = spell("DEF down and damage",5,5,50,False,5,"fire",70,23,0,"DEF down and damage")
def_down_damage_aoe = spell("DEF down and damage aoe",5,5,50,False,5,"fire",70,23,1,"DEF down and damage aoe")

##################--BUFF/HEALING SPELLS--##############################

#### status 100 spells HEAL
mega_heal = spell("mega heal",15,5,1000,True,250,"holy",50,100,0,"a mega healing spell")

super_heal = spell("super heal",5,5,500,True,100,"holy",50,100,0,"a super healing spell")

prayer = spell("prayer",1,50,250,True,50,"holy",50,100,0,"a light healing spell")

class status_condition:
    def __init__(self, name, scalar, is_freeze, is_asleep, is_poisoned, is_poisoned_bad, is_burning, is_str_up, is_atk_up, is_mgk_up, is_def_up, is_str_down, is_atk_down, is_mgk_down, is_def_down):
        self.name = name
        self.scalar = scalar
        self.is_freeze = is_freeze
        self.is_asleep = is_asleep
        self.is_poisoned = is_poisoned
        self.is_poisoned_bad = is_poisoned_bad
        self.is_burning = is_burning

        self.is_str_up = is_str_up
        self.is_atk_up = is_atk_up
        self.is_mgk_up = is_mgk_up
        self.is_def_up = is_def_up

        self.is_str_down = is_str_down
        self.is_atk_down = is_atk_down
        self.is_mgk_down = is_mgk_down
        self.is_def_down = is_def_down


        all_game_status_conditions.append(self)

frozen = status_condition("Frozen",1,True,False,False,False,False,False,False,False,False,False,False,False,False)
asleep = status_condition("Asleep",1,False,True,False,False,False,False,False,False,False,False,False,False,False)
poisoned = status_condition("Poisoned",1,False,False,True,False,False,False,False,False,False,False,False,False,False)
poisoned_bad = status_condition("Badly Poisoned",1,False,False,False,True,False,False,False,False,False,False,False,False,False)
burning = status_condition("Burning",1,False,False,False,False,True,False,False,False,False,False,False,False,False)

str_up_lvl_1 = status_condition("STR UP",1,False,False,False,False,False,True,False,False,False,False,False,False,False)
atk_up_lvl_1 = status_condition("ATK UP",1,False,False,False,False,False,False,True,False,False,False,False,False,False)
mgk_up_lvl_1 = status_condition("MGK UP",1,False,False,False,False,False,False,False,True,False,False,False,False,False)
def_up_lvl_1 = status_condition("DEF UP",1,False,False,False,False,False,False,False,False,True,False,False,False,False)

str_down_lvl_1 = status_condition("STR DOWN",1,False,False,False,False,False,False,False,False,False,True,False,False,False)
atk_down_lvl_1 = status_condition("ATK DOWN",1,False,False,False,False,False,False,False,False,False,False,True,False,False)
mgk_down_lvl_1 = status_condition("MGK DOWN",1,False,False,False,False,False,False,False,False,False,False,False,True,False)
def_down_lvl_1 = status_condition("DEF DOWN",1,False,False,False,False,False,False,False,False,False,False,False,False,True)

knocked_out = status_condition("KO'd",1,False,False,False,False,False,False,False,False,False,False,False,False,False)
