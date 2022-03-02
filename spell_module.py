import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

all_game_spells = []
all_game_status_conditions = []


class Status_condition:
    def __init__(self, name, scalar, is_freeze, is_asleep, is_poisoned, is_poisoned_bad, is_burning, is_str_up, is_atk_up, is_mgk_up, is_def_up, is_str_down, is_atk_down, is_mgk_down, is_def_down,text):
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
        self.text = text


        all_game_status_conditions.append(self)

frozen = Status_condition("Frozen",1,True,False,False,False,False,False,False,False,False,False,False,False,False,"froze")
asleep = Status_condition("Asleep",1,False,True,False,False,False,False,False,False,False,False,False,False,False,"hypnotised")
poisoned = Status_condition("Poisoned",1,False,False,True,False,False,False,False,False,False,False,False,False,False,"poisoned")
poisoned_bad = Status_condition("Badly Poisoned",1,False,False,False,True,False,False,False,False,False,False,False,False,False,"badly poisoned")
burning = Status_condition("Burning",1,False,False,False,False,True,False,False,False,False,False,False,False,False,"burnt")

str_up_lvl_1 = Status_condition("STR UP",1,False,False,False,False,False,True,False,False,False,False,False,False,False,"boosted")
atk_up_lvl_1 = Status_condition("ATK UP",1,False,False,False,False,False,False,True,False,False,False,False,False,False,"boosted")
mgk_up_lvl_1 = Status_condition("MGK UP",1,False,False,False,False,False,False,False,True,False,False,False,False,False,"boosted")
def_up_lvl_1 = Status_condition("DEF UP",1,False,False,False,False,False,False,False,False,True,False,False,False,False,"boosted")

str_down_lvl_1 = Status_condition("STR DOWN",1,False,False,False,False,False,False,False,False,False,True,False,False,False,"weakend")
atk_down_lvl_1 = Status_condition("ATK DOWN",1,False,False,False,False,False,False,False,False,False,False,True,False,False,"weakend")
mgk_down_lvl_1 = Status_condition("MGK DOWN",1,False,False,False,False,False,False,False,False,False,False,False,True,False,"weakend")
def_down_lvl_1 = Status_condition("DEF DOWN",1,False,False,False,False,False,False,False,False,False,False,False,False,True,"weakend")

knocked_out = Status_condition("KO'd",1,False,False,False,False,False,False,False,False,False,False,False,False,False,"knocked out")

class Spell:
    def __init__(self, name, level, mp_cost, value, damage, attribute, xp, effect, aoe_scale, spell_desc,status_effects):
        self.name = name
        self.level = level
        self.mp_cost = mp_cost
        self.value = value
        self.damage = damage
        self.attribute = attribute
        self.xp = xp

        self.effect = effect #making this redudandant

        self.aoe_scale = aoe_scale # TODO: target one enemy, all enemies or random enemies
        self.spell_desc = spell_desc
        self.status_effects = status_effects
        self.amount = 1
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

#utility spells do not damage

############--COMBAT SPELLS--#############

# status 0 does damage and applies status effects - targets enemys
# status 1 does the same, but also leeches life - targets enemys

# status 2 heals and applies status effects - targets allies
# damage/healing can = 0 if you just want to apply status effects


mega = Spell("Mega",1,1,5,999999,"holy",0,1,1,"mega spells",[])
omni = Spell("Omni",1,1,5,999999,"undead",0,1,1,"mega spells",[])


#### nothing
slime = Spell("slime",1,5,5,0,"slime",0,0,0,"slurms mackenzie",[])
splash = Spell("splash",1,5,5,0,"water",0,0,0,"splashes water",[])

#low level damage spells
fire_bolt = Spell("fire bolt",4,25,50,80,"fire",100,0,0,"fire damage",[])
ice_bolt = Spell("ice bolt",4,25,50,80,"ice",100,0,0,"ice damage",[])

# arrow spells
fire_arrow = Spell("fire arrow",18,50,500,80,"fire",100,0,0,"fire damage",[])
ice_arrow = Spell("ice arrow",18,50,500,80,"ice",100,0,0,"ice damage",[])

# tier 1 damage spells
fireball = Spell("fireball",30,75,5,1000,"fire",200,0,0,"heavy fire damage",[])
hydro_barrage = Spell("hydro barrage",30,75,1000,100,"water",200,0,0,"heavy water damage",[])
holy_surge = Spell("holy surge",30,75,1000,100,"holy",200,0,0,"heavy holy damage",[])
necro_surge = Spell("necro surge",30,75,1000,100,"undead",200,0,0,"heavy undead damage",[])

# tier 2 damage spells
hydroblast = Spell("hydroblast",8,25,250,60,"water",100,0,0,"light water damage",[])
fireblast = Spell("fireblast",8,25,250,60,"fire",100,0,0,"light fire damage",[])
windblast = Spell("windblast",8,25,250,60,"air",100,0,0,"light air damage",[])
earthblast = Spell("earthblast",8,25,250,60,"earth",100,0,0,"light earth damage",[])
necroblast = Spell("necroblast",8,25,250,60,"undead",100,0,0,"light undead damage",[])
holyblast = Spell("holyblast",8,25,250,60,"holy",100,0,0,"light holy damage",[])

##################-- DRAIN SPELLS --##############################

life_siphon= Spell("life siphon",5,5,5,50,"undead",50,1,0,"a life draining spell which heals the user",[])
life_drain = Spell("life drain",5,5,5,100,"undead",50,1,0,"a powerful life draining spell which heals the user",[])


##################--STATUS EFFECT SPELLS--##############################

snare = Spell("snare",5,5,500,5,"ice",70,0,0,"snares the enemy in ice",[frozen])
blizzard = Spell("blizzard",5,5,500,150,"ice",150,0,0,"freezes the enemy and does lots of damage",[frozen])
cone_of_cold = Spell("cone of cold",5,5,500,50,"ice",50,0,1,"freezes the enemy and does damage",[frozen])


poison = Spell("poison",5,5,50,5,"earth",70,0,0,"poisons the enemy",[poisoned])


burn = Spell("burn",5,5,50,5,"fire",70,0,2,"burns the enemy",[burning])
mega_burn = Spell("mega burn",30,5,5000,500,"fire",70,0,3,"MFB",[burning])


hypnosis = Spell("hypnosis",50,5,50,5,"water",70,0,0,"puts the enemy to sleep",[asleep])  

toxic = Spell("toxic",22,5,500,5,"earth",70,0,0,"badly poisons the enemy",[poisoned_bad])

##############//BUFFS//#########

#### STR UP
str_up = Spell("Meba",5,5,50,5,"fire",70,2,0,"STR UP",[str_up_lvl_1])
str_up_aoe = Spell("Mebana",10,5,50,5,"fire",70,2,1,"STR UP aoe",[str_up_lvl_1])
str_up_heal = Spell("Mebapo",15,5,50,5,"fire",70,2,0,"STR UP and heal",[str_up_lvl_1])
str_up_heal_aoe = Spell("Mebanapo",25,5,50,5,"fire",70,2,1,"STR UP and heal aoe",[str_up_lvl_1])
#### ATK UP
atk_up = Spell("Meda",5,5,50,5,"fire",70,0,0,"ATK UP",[atk_up_lvl_1])
atk_up_aoe = Spell("Medana",10,5,50,5,"fire",70,2,1,"ATK UP aoe",[atk_up_lvl_1])
atk_up_heal = Spell("Medapo",15,5,50,5,"fire",70,2,0,"ATK UP and heal",[atk_up_lvl_1])
atk_up_heal_aoe = Spell("Medanapo",25,5,50,5,"fire",70,2,1,"ATK UP and heal aoe",[atk_up_lvl_1])

#### MGK UP
mgk_up = Spell("Mera",5,5,50,5,"fire",70,2,0,"MGK UP",[mgk_up_lvl_1])
mgk_up_aoe = Spell("Merana",10,5,50,5,"fire",70,2,1,"MGK UP aoe",[mgk_up_lvl_1])
mgk_up_heal = Spell("Merapo",15,5,50,5,"fire",70,2,0,"MGK UP and heal",[mgk_up_lvl_1])
mgk_up_heal_aoe = Spell("Meranapo",25,5,50,5,"fire",70,2,1,"MGK UP and heal aoe",[mgk_up_lvl_1])

#### DEF UP
def_up = Spell("Meza",5,5,50,5,"fire",70,2,0,"DEF UP",[def_up_lvl_1])
def_up_aoe = Spell("Mezana",10,5,50,5,"fire",70,2,1,"DEF UP aoe",[def_up_lvl_1])
def_up_heal = Spell("Mezapo",15,5,50,5,"fire",70,2,0,"DEF UP and heal",[def_up_lvl_1])
def_up_heal_aoe = Spell("Mezanapo",25,5,50,5,"fire",70,2,1,"DEF UP and heal aoe",[def_up_lvl_1])

##############//DE-BUFFS//###################

#fire

#### sSTR down 1
str_down = Spell("Koba",5,5,50,5,"fire",70,0,0,"STR down",[str_down_lvl_1])
str_down_aoe = Spell("Kobana",10,5,50,5,"fire",70,0,1,"STR down aoe",[str_down_lvl_1])
str_down_damage = Spell("Kobajo",15,5,50,5,"fire",70,0,0,"STR down and damage",[str_down_lvl_1])
str_down_damage_aoe = Spell("Kobanajo",25,5,50,5,"fire",70,0,1,"STR down and damage aoe",[str_down_lvl_1])

####  ATK down 1
atk_down = Spell("Koda",5,5,50,5,"fire",70,0,0,"ATK down",[atk_down_lvl_1])
atk_down_aoe = Spell("Kodana",10,5,50,5,"fire",70,0,1,"ATK down aoe",[atk_down_lvl_1])
atk_down_damage = Spell("Kodajo",15,5,50,5,"fire",70,0,0,"ATK down and damage",[atk_down_lvl_1])
atk_down_damage_aoe = Spell("Kodanajo",25,5,50,5,"fire",70,0,1,"ATK down and damage aoe",[atk_down_lvl_1])
#### MGK down 1
mgk_down = Spell("Kora",5,5,50,5,"fire",70,0,0,"MGK down",[mgk_down_lvl_1])
mgk_down_aoe = Spell("Korana",10,5,50,5,"fire",70,0,1,"MGK down aoe",[mgk_down_lvl_1])
mgk_down_damage = Spell("Korajo",15,5,50,5,"fire",70,0,0,"MGK down and damage",[mgk_down_lvl_1])
mgk_down_damage_aoe = Spell("Koranajo",25,5,50,5,"fire",70,0,1,"MGK down and damage aoe",[mgk_down_lvl_1])
####  DEF down 1
def_down = Spell("Koza",5,5,50,5,"fire",70,0,0,"DEF down",[def_down_lvl_1])
def_down_aoe = Spell("Kozana",10,5,50,5,"fire",70,0,1,"DEF down aoe",[def_down_lvl_1])
def_down_damage = Spell("Kozajo",15,5,50,5,"fire",70,0,0,"DEF down and damage",[def_down_lvl_1])
def_down_damage_aoe = Spell("Kozanajo",25,5,50,5,"fire",70,0,1,"DEF down and damage aoe",[def_down_lvl_1])

##################--BUFF/HEALING SPELLS--##############################

#### status 100 spells HEAL
mega_heal = Spell("mega heal",15,5,1000,250,"holy",50,2,0,"a mega healing spell",[])

super_heal = Spell("super heal",5,5,500,100,"holy",50,2,0,"a super healing spell",[])

prayer = Spell("prayer",1,50,250,50,"holy",50,2,0,"a light healing spell",[])


