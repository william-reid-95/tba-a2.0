import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

all_game_party_members = []

class party_member_stats:
    def __init__(self, name, level, xp, hp, maxhp, mp, maxmp, magic, strength, attack, gp, attribute, weakness, spellbook, drop_table_items, drop_table_weapons, drop_table_armor, drop_table_helmets, drop_table_shields, status_effect):
        self.name =  name
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
        self.gp = gp
        self.attribute = attribute
        self.weakness = weakness
        self.spellbook = spellbook
        self.drop_table_items = drop_table_items
        self.equiped_weapon = drop_table_weapons
        self.equiped_armor = drop_table_armor
        self.equiped_helmet = drop_table_helmets
        self.equiped_shield = drop_table_shields
        self.status_effect = status_effect
        self.status_effect_list = []

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

        all_game_party_members.append(self)

# Attributes: name, level, xp, hp, maxhp, mp, maxmp, magic, strength, attack, gp, attribute, weakness,
# LIsts: spellbook, drop_table_items, drop_table_weapons, drop_table_armor, drop_table_helmets, drop_table_shields,
# Status: status_effect
party_goblin = party_member_stats("goblin",2,5,1000,1000,100,100,1,8,4,100,"earth","fire",[],[],[],[],[],[],0)
# hobgoblin = party_member_stats("hobgoblin",3,12,5000,5000,100,100,8,10,5,300,"earth","fire",[],[],[],[],[],[],0)
# hobgoblin_berzerker = party_member_stats("hobgoblin berzerker",6,22,5000,5000,100,100,1,12,10,300,"earth","fire",[],[],[],[],[],[],0)
# bandit = party_member_stats("bandit",5,10,2000,2000,1000,1000,1,12,6,100,"fire","earth",[],[],[],[],[],[],0)
# bandit_warlock = party_member_stats("bandit warlock",8,28,2000,2000,5000,5000,18,5,2,70,"fire","earth",[],[],[],[],[],[],0)
# bandit_henchman = party_member_stats("bandit henchman",12,50,2000,2000,2200,2200,10,12,4,230,"fire","earth",[],[],[],[],[],[],0)
#
# legion_soldier = party_member_stats("legion soldier",28,500,10000,10000,100,100,10,14,20,1000,"air","earth",[],[],[],[],[],[],0)
# legion_spearman = party_member_stats("legion spearman",25,500,10500,10500,100,100,10,16,10,1050,"air","earth",[],[],[],[],[],[],0)
# legion_archer = party_member_stats("legion archer",23,500,8700,8700,100,100,10,11,22,654,"air","earth",[],[],[],[],[],[],0)
# legion_battle_mage = party_member_stats("legion battle mage",29,500,12400,12400,100,100,45,5,6,2245,"air","earth",[],[],[],[],[],[],0)
#
# rock_golem = party_member_stats("rock golem",62,800,10230,10230,100,100,0,55,18,20230,"earth","water",[],[],[],[],[],[],0)
# mushroom_man = party_member_stats("mushroom man",67,800,10230,10230,100,100,0,50,20,10230,"earth","fire",[],[],[],[],[],[],0)
#
# bird_warrior = party_member_stats("bird warrior",191,100000,2408070,2408070,1000000,1000000,100,300,220,1000,"air","water",[],[],[],[],[],[],0)#leg
#
# fire_elemental = party_member_stats("fire elemental",8,200,3200,3200,1000,1000,8,5,2,100,"fire","water",[],[],[],[],[],[],0)
# water_elemental = party_member_stats("water elemental",8,200,3800,3800,1000,1000,8,5,2,100,"water","earth",[],[],[],[],[],[],0)
# earth_elemental = party_member_stats("earth elemental",8,100,3200,3200,1000,1000,3,5,2,100,"earth","water",[],[],[],[],[],[],0)
# air_elemental = party_member_stats("air elemental",8,100,3000,3000,1000,1000,3,5,2,100,"air","earth",[],[],[],[],[],[],0)
#
# giant_snail = party_member_stats("giant snail",14,10,9300,9300,100,100,0,12,2,930,"earth","earth",[],[],[],[],[],[],0)
# giant_spider = party_member_stats("giant spider",33,64,23000,23000,100,100,0,50,2,2300,"earth","fire",[],[],[],[],[],[],0)
# giant_moth = party_member_stats("giant moth",18,5,13400,13400,100,100,0,10,20,100,"earth","air",[],[],[],[],[],[],0)
#
# big_slug = party_member_stats("big slug",1,500,103000,103000,100,100,0,0,0,0,"slime","salt",[],[],[],[],[],[],0)#legendary
#
# skeleton_mage = party_member_stats("skeleton mage",101,4202,60070,60070,100,100,53,30,22,100,"undead","holy",[],[],[],[],[],[],0)
# skeleton_warrior = enemy_stats("skeleton warrior",101,50922,92070,92070,100,100,0,63,42,100,"undead","holy",[],[],[],[],[],[],0)

## npc enemies
