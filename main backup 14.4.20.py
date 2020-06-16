
import random # default python module
from time import sleep # default python module

##########--3RD PARTY MODULES--###############
from tkinter import *

from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)

import pygame
pygame.mixer.pre_init() #44100, 16, 2, 4096
pygame.init()
pygame.font.init() # you have to call this at the start if you want to use fonts
myfont = pygame.font.SysFont('MS Comic Sans', 21) # you have to call this at the start if you want to use fonts

pygame.key.set_repeat(0,1) # held key repeat timer

#################--IMPORT_GAME_MODULES--####################

from scene_module import *
from npc_module import *

from item_module import *
from equipment_module import *
from spell_module import *

from enemy_module import *
from party_member_module import *

###########################----GLOBAL_VARIABLES-----####################

version = "1.8.4"

dev_mode = 1

has_moved = False
check_for_combat = True
restock_shops = False
restock_ticks = 0

steps_x = 0
steps_y = 0
steps_z = 0

###########################################

prev_x = 0
prev_y = 0
prev_z = 0

npc_fight = False
npc_enemy_fname = "0"
npc_enemy_lname = "0"

player_turns = 0

in_fight = False
in_menu = False
in_submenu = False
in_submenu2 = False
in_submenu3 = False
in_submenu4 = False

in_submenu_equip = False
in_submenu_equip2 = False

in_submenu_cast = False
in_submenu_drop = False
in_submenu_drop2 = False
in_submenu_pickup = False

in_submenu_talk = False
in_submenu_talk2 = False

in_submenu_buy3 = False

in_submenu_sell3 = False
in_submenu_sell4 = False

in_submenu_use = False
in_submenu_make = False

in_submenu_use_combat = False
in_submenu_cast_combat = False
in_submenu_target_combat2 = False
in_submenu_spell_target_combat2 = False

in_menu_item = False
in_menu_weapon = False
in_menu_armor = False
in_menu_helmet = False
in_menu_shield = False
in_menu_spell = False


val = 999 #spell selection value
val_npc = 999 #selection value
val_enemy = 999 #selection value
val_dialouge = 999 #selection value
val_shop = 999 #selection value
val_drop = 999 #selection value
val_sell = 999 #selection value
val_combat_input = 999 #selection value
combat_cast_spell = "0"
recipe_found = False

sleep_time = 0
sleep_time_fast = 0
sleep_time_slow = 0

raining = 1
weather = 0
season = 3 # value from 0,3 that determines season

time = 0
time2 = 0
days = 19
months = 4
years = 1567

default_drop_table_items = []
default_drop_table_weapons = []
default_drop_table_armor = []

combat_option_list = []
input_option_list = []

#blit globals

menu_cursor_pos = 1
combat_cursor_pos = 1

blit_player_damage_amount = 0

###########################------COLOUR_VARIABLES-------#############################

colour_reset = (Style.RESET_ALL) # resest colour

colour_scene_name = (Fore.GREEN + Style.DIM) # text colours for scene variables

colour_scene_temp = (Fore.MAGENTA + Style.DIM)

colour_scene_light_day = (Fore.BLUE + Style.BRIGHT)
colour_scene_light_night = (Fore.BLUE + Style.DIM)

colour_item_name = (Fore.BLACK + Style.BRIGHT) # text colour for all item names

colour_gear_name = (Fore.CYAN + Style.DIM) # text colour for all gear names

colour_spell_name = (Fore.CYAN + Style.NORMAL) # text colour

colour_enemy_name = (Fore.RED + Style.DIM) # text colour

colour_misc_name = (Fore.BLACK + Style.BRIGHT) # misc. text colour

colour_attribute = (Fore.BLACK + Style.BRIGHT) # misc. text colour

############################----DROP_TABLES-###########################

## default drop tables

weapons_drop_table = []
large_weapons_drop_table = []
magic_weapons_drop_table = []

armor_drop_table = []
magic_armor_drop_table = []

helmets_drop_table = []

shields_drop_table = []

healing_drop_table = []
super_healing_drop_table = []
items_drop_table = []

## default shop tables

weapons_shop_table = []
armor_shop_table = []
helmets_shop_table = []
shields_shop_table = []

spells_shop_table = []

items_shop_table = []

weapons_shop_table.extend(weapons_drop_table)
weapons_shop_table.extend(large_weapons_drop_table)
weapons_shop_table.extend(magic_weapons_drop_table)

armor_shop_table.extend(armor_drop_table)
armor_shop_table.extend(magic_armor_drop_table)

helmets_shop_table.extend(helmets_drop_table)

shields_shop_table.extend(shields_drop_table)

items_shop_table.extend(items_drop_table)
items_shop_table.extend(healing_drop_table)

#####################################################

weapons_drop_table.append(iron_sword)
weapons_drop_table.append(iron_axe)
weapons_drop_table.append(steel_sword)
weapons_drop_table.append(steel_axe)
weapons_drop_table.append(mithril_sword)
weapons_drop_table.append(mithril_axe)
weapons_drop_table.append(adamantite_sword)
weapons_drop_table.append(adamantite_axe)
weapons_drop_table.append(rune_sword)
weapons_drop_table.append(rune_axe)

large_weapons_drop_table.append(war_spear)
large_weapons_drop_table.append(greatsword)
large_weapons_drop_table.append(lance)
large_weapons_drop_table.append(ultra_greatsword)

magic_weapons_drop_table.append(gladius)
magic_weapons_drop_table.append(gladius)
magic_weapons_drop_table.append(bone_scimitar)

#####################################################

armor_drop_table.append(leather_armor)
armor_drop_table.append(hard_leather_armor)
armor_drop_table.append(iron_chain_mail)
armor_drop_table.append(iron_plate_armor)
armor_drop_table.append(steel_chain_mail)
armor_drop_table.append(steel_plate_armor)

magic_armor_drop_table.append(mage_robes)
magic_armor_drop_table.append(mage_robes)
magic_armor_drop_table.append(necro_robes)

#######################################################

helmets_drop_table.append(iron_helmet)
helmets_drop_table.append(steel_helmet)
helmets_drop_table.append(mage_hood)

#####################################################

shields_drop_table.append(mage_book)
shields_drop_table.append(iron_square_shield)
shields_drop_table.append(steel_square_shield)

#####################################################

healing_drop_table.append(apple)
healing_drop_table.append(pear)
healing_drop_table.append(hp_potion)
healing_drop_table.append(hp_potion)

super_healing_drop_table.append(hp_potion)
super_healing_drop_table.append(hp_potion)
super_healing_drop_table.append(super_hp_potion)

for item in all_game_items:
    items_drop_table.append(item)

##################################--PLAYER--############################################

class player_stats:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 1
        self.hp = 1 # current mana points
        self.mp = 1 # current hit points
        self.gp = 1
        self.magic = 1
        self.strength = 1
        self.attack = 1
        self.defence = 1
        self.maxhp = 1 # hit points maximum value
        self.nobonus_maxhp = 1 #  hit points max without gear bonus
        self.maxmp = 1 # mana points maximum value
        self.nobonus_maxmp = 1 #  mana points max without gear bonus
        self.strength_xp = 1
        self.attack_xp = 1
        self.magic_xp = 1
        self.defence_xp = 1
        self.status_effect = 1
        self.magic_bonus = 1
        self.strength_bonus = 1
        self.attack_bonus = 1
        self.defence_bonus = 1
        self.maxhp_bonus = 1
        self.maxmp_bonus = 1

        self.status_effect_list = []

player1 = player_stats("The Hero")

class player_skills:
    def __init__(self, fishing, fishing_xp, thieving, thieving_xp, crafting, crafting_xp, cooking, cooking_xp):
        self.fishing = fishing
        self.fishing_xp = fishing_xp
        self.thieving = thieving
        self.thieving_xp = thieving_xp
        self.crafting = crafting
        self.crafting_xp = crafting_xp
        self.cooking = cooking
        self.cooking_xp = cooking_xp

player1_skills = player_skills(1,0,1,0,1,0,1,0)

class input_option:
    def __init__(self, name, hotkey, is_default_option, print_in_main):
        self.name = name
        self.hotkey = hotkey
        self.is_default_option = is_default_option
        self.print_in_main = print_in_main
        if is_default_option == True:
            input_option_list.append(self)

        # input_option_talk = input_option("talk","t",True,True)
        # input_option_equip = input_option("equip","e",True,True)
        # input_option_gear = input_option("gear","w",True,True)
        # input_option_stats = input_option("stats","q",True,True)
        # input_option_skills = input_option("skills","Q",True,True)
        # input_option_search = input_option("search","j",True,True)
        # input_option_drop = input_option("drop","l",True,True)
        # input_option_pickup = input_option("pickup","p",True,True)
        # input_option_pickupall = input_option("pickupall","P",True,True)
        # input_option_consume = input_option("consume","k",True,True)
        # input_option_inv = input_option("inv","i",True,True)
        # input_option_spellbook = input_option("spellbook","b",True,True)
        # input_option_cast = input_option("cast","c",True,True)
        # input_option_wait = input_option("wait","W",True,True)
        #
        # input_option_help = input_option("help","H",True,True)
        # input_option_quit = input_option("quit","Z",True,True)
        # input_option_camp = input_option("camp","u",False,True)
        #
        # input_option_dev = input_option("dev","dv",True,False)
        # input_option_dev_xp = input_option("/xp","/xp",True,False)
        # input_option_dev_tp = input_option("/tp","/tp",True,False)
        # input_option_dev_gp = input_option("/gp","/gp",True,False)


class combat_option:
    def __init__(self, name):
        self.name = name

combat_option_hit = combat_option("hit")
combat_option_spell = combat_option("spell")
combat_option_item = combat_option("item")
combat_option_run = combat_option("run")

############################################--NPCS/DIALOUGE/QUESTS--#########################################

class quest:
    def __init__(self, name, quest_desc, xp, gp, reward_list, quest_collect_items, item_amount, quest_kill_enemies, kill_amount):
        self.name = name
        self.quest_desc = quest_desc
        self.xp = xp
        self.gp = gp
        self.reward_list = reward_list
        self.quest_collect_items = quest_collect_items
        self.item_amount = item_amount
        self.quest_kill_enemies = quest_kill_enemies
        self.kill_amount = kill_amount

quest_1 = quest("The Bandit Menace","eliminate the local bandit population",200,80,[],False,0,True,10)

# place npcs in the world
dismurth_gates.npc_list.append(npc_town_guard)
dismurth_square.npc_list.append(npc_jenkins)
dismurth_market.npc_list.append(npc_john_doe)
dismurth_market.npc_list.append(npc_jane_doe)
dismurth_market.npc_list.append(npc_doctor)
dismurth_tower_1f.npc_list.append(npc_wizard_traenus)
dismurth_tower_gf.npc_list.append(npc_wizard_marbles)
dismurth_smith.npc_list.append(npc_dismurth_smith)

forest_cabin.npc_list.append(npc_wizard_jim)
forest_cabin.npc_list.append(npc_wizard_tilly)

grassland_2.npc_list.append(npc_cow)
grassland_2.npc_list.append(npc_sheep)
grassland_4.npc_list.append(npc_sheep)
grassland_5.npc_list.append(npc_cow)
grassland_8.npc_list.append(npc_cow)

################################

# give npc dialouge options

npc_town_guard.dialouge_options_list.append(dialouge_talk)
npc_town_guard.dialouge_options_list.append(dialouge_gf)

npc_jenkins.dialouge_options_list.append(dialouge_talk)
npc_jenkins.dialouge_options_list.append(dialouge_gf)
npc_jenkins.dialouge_options_list.append(dialouge_give)
npc_jenkins.dialouge_options_list.append(dialouge_quest)
npc_jenkins.dialouge_options_list.append(dialouge_sell)

npc_john_doe.dialouge_options_list.append(dialouge_talk)
npc_john_doe.dialouge_options_list.append(dialouge_buy_weapon)
npc_john_doe.dialouge_options_list.append(dialouge_buy_armor)
npc_john_doe.dialouge_options_list.append(dialouge_buy_helmet)
npc_john_doe.dialouge_options_list.append(dialouge_buy_shield)

npc_jane_doe.dialouge_options_list.append(dialouge_talk)
npc_jane_doe.dialouge_options_list.append(dialouge_buy_item)

npc_wizard_traenus.dialouge_options_list.append(dialouge_talk)
npc_wizard_traenus.dialouge_options_list.append(dialouge_buy_spell)
npc_wizard_traenus.dialouge_options_list.append(dialouge_buy_item)

npc_wizard_marbles.dialouge_options_list.append(dialouge_talk)
npc_wizard_marbles.dialouge_options_list.append(dialouge_buy_spell)

npc_dismurth_smith.dialouge_options_list.append(dialouge_talk)
npc_dismurth_smith.dialouge_options_list.append(dialouge_buy_weapon)
npc_dismurth_smith.dialouge_options_list.append(dialouge_buy_armor)
npc_dismurth_smith.dialouge_options_list.append(dialouge_buy_helmet)
npc_dismurth_smith.dialouge_options_list.append(dialouge_buy_shield)

npc_wizard_jim.dialouge_options_list.append(dialouge_talk)
npc_wizard_jim.dialouge_options_list.append(dialouge_buy_spell)

npc_wizard_tilly.dialouge_options_list.append(dialouge_talk)
npc_wizard_tilly.dialouge_options_list.append(dialouge_buy_weapon)
npc_wizard_tilly.dialouge_options_list.append(dialouge_buy_helmet)
npc_wizard_tilly.dialouge_options_list.append(dialouge_buy_shield)

npc_cow.dialouge_options_list.append(dialouge_talk)
npc_cow.dialouge_options_list.append(dialouge_attack)

npc_sheep.dialouge_options_list.append(dialouge_talk)
npc_sheep.dialouge_options_list.append(dialouge_attack)

npc_doctor.dialouge_options_list.append(dialouge_talk)
npc_doctor.dialouge_options_list.append(dialouge_heal)

####################-NPC COMBAT ENCOUNTERS--#########################

npc_jenkins.combat_enemy_list.append(hobgoblin)
npc_town_guard.combat_enemy_list.append(town_guard)
npc_jenkins.combat_enemy_list.append(cow)
npc_jenkins.combat_enemy_list.append(sheep)
npc_cow.combat_enemy_list.append(cow)
npc_sheep.combat_enemy_list.append(sheep)

#######################--SHOP INVENTORIES--############################

npc_dismurth_smith.npc_armor_inventory.append(leather_armor)
npc_dismurth_smith.npc_armor_inventory.append(hard_leather_armor)
npc_dismurth_smith.npc_armor_inventory.append(iron_chain_mail)
npc_dismurth_smith.npc_armor_inventory.append(iron_plate_armor)
npc_dismurth_smith.npc_armor_inventory.append(steel_chain_mail)


npc_john_doe.npc_weapon_inventory.append(steel_spear)
npc_john_doe.npc_weapon_inventory.append(iron_sword)
npc_john_doe.npc_weapon_inventory.append(iron_spear)
npc_john_doe.npc_weapon_inventory.append(steel_sword)
npc_john_doe.npc_weapon_inventory.append(steel_axe)
npc_john_doe.npc_weapon_inventory.append(greatsword)
npc_john_doe.npc_weapon_inventory.append(wooden_staff)
npc_john_doe.npc_weapon_inventory.append(tall_staff)
npc_john_doe.npc_weapon_inventory.append(battle_axe)
npc_john_doe.npc_weapon_inventory.append(warhammer)
npc_john_doe.npc_weapon_inventory.append(war_spear)

npc_john_doe.npc_armor_inventory.append(leather_armor)

npc_john_doe.npc_helmet_inventory.append(steel_helmet)
npc_john_doe.npc_helmet_inventory.append(iron_helmet)

npc_john_doe.npc_shield_inventory.append(iron_square_shield)
npc_john_doe.npc_shield_inventory.append(wooden_round_shield)
npc_john_doe.npc_shield_inventory.append(magic_orb)


########################################################

npc_wizard_traenus.npc_spell_inventory.append(fire_arrow)
npc_wizard_traenus.npc_spell_inventory.append(ice_arrow)
npc_wizard_traenus.npc_spell_inventory.append(hydroblast)
npc_wizard_traenus.npc_spell_inventory.append(fireblast)
npc_wizard_traenus.npc_spell_inventory.append(windblast)
npc_wizard_traenus.npc_spell_inventory.append(earthblast)
npc_wizard_traenus.npc_spell_inventory.append(necroblast)
npc_wizard_traenus.npc_spell_inventory.append(holyblast)
npc_wizard_traenus.npc_spell_inventory.append(snare)
npc_wizard_traenus.npc_spell_inventory.append(poison)
npc_wizard_traenus.npc_spell_inventory.append(burn)

npc_wizard_marbles.npc_spell_inventory.append(mega_heal)
npc_wizard_marbles.npc_spell_inventory.append(super_heal)
npc_wizard_marbles.npc_spell_inventory.append(prayer)

npc_jane_doe.npc_inventory.append(torch)
npc_jane_doe.npc_inventory.append(rope)
npc_jane_doe.npc_inventory.append(tent)
npc_jane_doe.npc_inventory.append(hp_potion)
npc_jane_doe.npc_inventory.append(super_hp_potion)
npc_jane_doe.npc_inventory.append(cup_of_tea)
npc_jane_doe.npc_inventory.append(tea_bag)

npc_wizard_jim.npc_spell_inventory.append(fire_bolt)
npc_wizard_jim.npc_spell_inventory.append(ice_bolt)
npc_wizard_jim.npc_spell_inventory.append(fire_arrow)
npc_wizard_jim.npc_spell_inventory.append(fireball)
npc_wizard_jim.npc_spell_inventory.append(hydro_barrage)
npc_wizard_jim.npc_spell_inventory.append(holy_surge)
npc_wizard_jim.npc_spell_inventory.append(necro_surge)
npc_wizard_jim.npc_spell_inventory.append(life_drain)

npc_wizard_jim.npc_inventory.append(hp_potion)
npc_wizard_jim.npc_inventory.append(super_hp_potion)

npc_wizard_tilly.npc_weapon_inventory.append(bird_sword)
npc_wizard_tilly.npc_weapon_inventory.append(adamantite_axe)
npc_wizard_tilly.npc_weapon_inventory.append(adamantite_sword)
npc_wizard_tilly.npc_weapon_inventory.append(gladius)

npc_wizard_tilly.npc_helmet_inventory.append(mage_hood)

npc_wizard_tilly.npc_shield_inventory.append(mage_book)


######################------ENEMY_SPELLBOOKS------########################

hobgoblin.spellbook.append(earthblast)
hobgoblin.spellbook.append(hydroblast)
hobgoblin.spellbook.append(poison)
hobgoblin.spellbook.append(snare)
hobgoblin.spellbook.append(super_heal)

goblin.spellbook.append(prayer)
goblin.spellbook.append(burn)

giant_moth.spellbook.append(poison)
giant_moth.spellbook.append(poison)

giant_spider.spellbook.append(poison)
giant_spider.spellbook.append(poison)

giant_snail.spellbook.append(slime)


bandit.spellbook.append(prayer)

bandit_warlock.spellbook.append(snare)
bandit_warlock.spellbook.append(prayer)
bandit_warlock.spellbook.append(earthblast)
bandit_warlock.spellbook.append(earthblast)
bandit_warlock.spellbook.append(necroblast)

bandit_henchman.spellbook.append(burn)
bandit_henchman.spellbook.append(fireblast)
bandit_henchman.spellbook.append(prayer)

legion_soldier.spellbook.append(prayer)

legion_spearman.spellbook.append(super_heal)

legion_archer.spellbook.append(prayer)
legion_archer.spellbook.append(fire_arrow)
legion_archer.spellbook.append(fire_arrow)
legion_archer.spellbook.append(ice_arrow)
legion_archer.spellbook.append(ice_arrow)

legion_battle_mage.spellbook.append(holyblast)
legion_battle_mage.spellbook.append(holyblast)
legion_battle_mage.spellbook.append(prayer)
legion_battle_mage.spellbook.append(holyblast)
legion_battle_mage.spellbook.append(prayer)
legion_battle_mage.spellbook.append(holyblast)
legion_battle_mage.spellbook.append(holy_surge)
legion_battle_mage.spellbook.append(super_heal)
legion_battle_mage.spellbook.append(holy_surge)
legion_battle_mage.spellbook.append(super_heal)
legion_battle_mage.spellbook.append(holy_surge)
legion_battle_mage.spellbook.append(super_heal)
legion_battle_mage.spellbook.append(holy_surge)

fire_elemental.spellbook.append(fireblast)
fire_elemental.spellbook.append(fireblast)
fire_elemental.spellbook.append(fireblast)
fire_elemental.spellbook.append(burn)
fire_elemental.spellbook.append(fireblast)
fire_elemental.spellbook.append(fireblast)
fire_elemental.spellbook.append(burn)

water_elemental.spellbook.append(hydroblast)
water_elemental.spellbook.append(hydroblast)
water_elemental.spellbook.append(hydroblast)
water_elemental.spellbook.append(hydroblast)
water_elemental.spellbook.append(hydroblast)
water_elemental.spellbook.append(hydroblast)
water_elemental.spellbook.append(hydroblast)

earth_elemental.spellbook.append(earthblast)
earth_elemental.spellbook.append(earthblast)
earth_elemental.spellbook.append(earthblast)
earth_elemental.spellbook.append(earthblast)
earth_elemental.spellbook.append(earthblast)
earth_elemental.spellbook.append(earthblast)
earth_elemental.spellbook.append(earthblast)
earth_elemental.spellbook.append(earthblast)

air_elemental.spellbook.append(windblast)
air_elemental.spellbook.append(windblast)
air_elemental.spellbook.append(windblast)
air_elemental.spellbook.append(windblast)
air_elemental.spellbook.append(windblast)
air_elemental.spellbook.append(windblast)
air_elemental.spellbook.append(windblast)
air_elemental.spellbook.append(windblast)

skeleton_mage.spellbook.append(fireblast)
skeleton_mage.spellbook.append(burn)
skeleton_mage.spellbook.append(fireball)
skeleton_mage.spellbook.append(life_drain)
skeleton_mage.spellbook.append(fireball)
skeleton_mage.spellbook.append(life_drain)
skeleton_mage.spellbook.append(fireball)
skeleton_mage.spellbook.append(life_drain)

skeleton_warrior.spellbook.append(life_drain)
skeleton_warrior.spellbook.append(life_drain)

big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)
big_slug.spellbook.append(slime)

#################################------PLACE GROUND_ITEMS IN WORLD------#######################################

forest_1.scene_inventory.append(ground_oak_key)

fortress.scene_inventory.append(ground_certificate_of_passage)

########################################------LISTS------###############################################

players = []
players_skills = []

players.append(player1)
players_skills.append(player1_skills)

location = []
location_north = []
location_east = []
location_south = []
location_west = []
location_down = []
location_up = []

current_enemies = []
current_npc = []

combat_option_list.append(combat_option_hit)
combat_option_list.append(combat_option_spell)
combat_option_list.append(combat_option_item)
combat_option_list.append(combat_option_run)

##############

inventory = []
inventory2 = []
weapon_inventory = []
armor_inventory = []
helmet_inventory = []
shield_inventory = []
spell_inventory = []

####################################################################

equiped_armor = []
equiped_weapon = []
equiped_helmet = []
equiped_shield = []
equiped_spells = []

####################################################################

if dev_mode >= 1:

    equiped_helmet.append(bird_hat)
    equiped_shield.append(bird_shield)
    equiped_weapon.append(super_bird_sword)
    equiped_armor.append(birdshirt)

    equiped_spells.append(mega_heal)
    equiped_spells.append(fireblast)
    equiped_spells.append(hydroblast)
    equiped_spells.append(earthblast)
    equiped_spells.append(windblast)
    equiped_spells.append(blizzard)
    equiped_spells.append(poison)
    equiped_spells.append(mega_burn)

    spell_inventory.append(fireblast)
    spell_inventory.append(snare)

    weapon_inventory.append(super_bird_sword)
    weapon_inventory.append(gladius)

    armor_inventory.append(iron_chain_mail)
    armor_inventory.append(steel_chain_mail)

    helmet_inventory.append(iron_helmet)
    helmet_inventory.append(steel_helmet)

    shield_inventory.append(iron_square_shield)
    shield_inventory.append(steel_square_shield)

    inventory.append(super_hp_potion)
    inventory.append(hp_potion)
    inventory.append(meat)

    for item in inventory:
        item.item_amount = 10

    inventory.append(tent)
    inventory.append(rope)
    inventory.append(torch)

else:
    equiped_armor.append(rags)

##########--PYGAME--############

sfx_cursor_move = pygame.mixer.Sound('sfx_cursor_move16.wav')
sfx_cursor_select = pygame.mixer.Sound('sfx_cursor_select16.wav')

txt_1 = myfont.render('1', False, (0, 0, 0))
txt_2 = myfont.render('2', False, (0, 0, 0))
txt_3 = myfont.render('3', False, (0, 0, 0))
txt_4 = myfont.render('4', False, (0, 0, 0))
txt_5 = myfont.render('5', False, (0, 0, 0))
txt_6 = myfont.render('6', False, (0, 0, 0))
txt_7 = myfont.render('7', False, (0, 0, 0))
txt_8 = myfont.render('8', False, (0, 0, 0))
txt_9 = myfont.render('9', False, (0, 0, 0))
txt_10 = myfont.render('10', False, (0, 0, 0))
txt_11 = myfont.render('11', False, (0, 0, 0))
txt_12 = myfont.render('12', False, (0, 0, 0))
txt_13 = myfont.render('13', False, (0, 0, 0))
txt_14 = myfont.render('14', False, (0, 0, 0))


 # search (j)  equip (e)  stats (q)  skills (Q)
 # drop (l)  pickup (p)  pickupall (P)  consume (k)  inv (i)  spellbook (b)  cast (c)  wait (W)  camp (u)  quit ")

txt_talk = myfont.render('talk', False, (0, 0, 0))
txt_search = myfont.render('search', False, (0, 0, 0))
txt_inv = myfont.render('inv', False, (0, 0, 0))
txt_equip = myfont.render('equip', False, (0, 0, 0))
txt_consume = myfont.render('consume', False, (0, 0, 0))
txt_skills = myfont.render('skills', False, (0, 0, 0))
txt_stats = myfont.render('stats', False, (0, 0, 0))
txt_gear = myfont.render('gear', False, (0, 0, 0))
txt_spellbook = myfont.render('spellbook', False, (0, 0, 0))
txt_cast = myfont.render('cast', False, (0, 0, 0))
txt_make = myfont.render('make', False, (0, 0, 0))
txt_pickup = myfont.render('pickup', False, (0, 0, 0))
txt_pickupall = myfont.render('pickupall', False, (0, 0, 0))
txt_camp = myfont.render('camp', False, (0, 0, 0))
txt_wait = myfont.render('wait', False, (0, 0, 0))
txt_quit = myfont.render('quit', False, (0, 0, 0))
txt_help = myfont.render('dev menu', False, (0, 0, 0))
txt_drop = myfont.render('drop', False, (0, 0, 0))

txt_items = myfont.render('items', False, (0, 0, 0))
txt_weapons = myfont.render('weapons', False, (0, 0, 0))
txt_armor = myfont.render('armor', False, (0, 0, 0))
txt_helmets = myfont.render('helmets', False, (0, 0, 0))
txt_shields = myfont.render('shields', False, (0, 0, 0))
txt_spells = myfont.render('spells', False, (0, 0, 0))

spr_house = pygame.image.load("house1.png")
spr_player = pygame.image.load("player1.png")

win_map = pygame.display.set_mode((1024,768))

pygame.display.set_caption("Map Screen")

x = 128
y = 128

cx = 512
cy = 256

cursor_width = 16
cursor_height = 8

map_tile_width = 32
map_tile_height = 32

char_width = 10
char_height = 10

enemy_width = 32
enemy_height = 32

vel = 16

##############################--GUI / GRAPHICS FUNCTIONS--#################################

def func_blit_list(list_object,list,gui_val):
    list_object_number = 0
    for list_object in list:
        list_object_number += 1
        blit_text = myfont.render(list_object.name + " x " + list_object.amount, False, (0, 0, 0))
        win_map.blit(blit_text,(32+((gui_val-1)*200),(list_object_number*16)))

def func_blit_npc_list(list_object,list,gui_val):
    list_object_number = 0
    for list_object in list:
        list_object_number += 1
        blit_text = myfont.render(list_object.first_name + " " + list_object.last_name, False, (0, 0, 0))
        win_map.blit(blit_text,(32+((gui_val-1)*200),(list_object_number*16)))

def func_blit_dialouge_list(list_object,list,gui_val):
    list_object_number = 0
    for list_object in list:
        list_object_number += 1
        blit_text = myfont.render(list_object.text, False, (0, 0, 0))
        win_map.blit(blit_text,(32+((gui_val-1)*200),(list_object_number*16)))

def func_blit_menu_cursor(gui_val):
    pygame.draw.rect(win_map, (247,255,0), (((14+((gui_val-1)*200), ((menu_cursor_pos)*16)+8, cursor_width, cursor_height))))

def func_blit_combat_cursor(gui_val):
    pygame.draw.rect(win_map, (247,255,0), (((14+((gui_val-1)*200), ((combat_cursor_pos)*16)+8, cursor_width, cursor_height))))

def func_blit_HUD(hud_val):
    status_list = []
    for status_condition in player1.status_effect_list:
        status_list.append(status_condition.name)
    blit_HUD_name = myfont.render(player1.name, False, (0, 0, 0))
    blit_HUD_lvl = myfont.render("Lvl: " + str(player1.level), False, (0, 0, 0))
    for armor in equiped_armor:
        blit_HUD_att = myfont.render("Att: " + armor.attribute, False, (0, 0, 0))
    blit_HUD_hp = myfont.render("HP: " + str(player1.hp) + "/" + str(player1.maxhp), False, (0, 0, 0))
    blit_HUD_mp = myfont.render("MP: " + str(player1.mp) + "/" + str(player1.maxmp), False, (0, 0, 0))
    blit_HUD_xp = myfont.render("XP: " + str(player1.xp), False, (0, 0, 0))
    blit_HUD_gp = myfont.render("GP: " + str(player1.gp), False, (0, 0, 0))
    if len(player1.status_effect_list) != 0:
        blit_HUD_status = myfont.render("Status: " + str(status_list), False, (0, 0, 0))
    else:
        blit_HUD_status = myfont.render("Status: ['N0NE']", False, (0, 0, 0))

    win_map.blit(blit_HUD_name,(32+((hud_val-1)*200),(33*16)))
    win_map.blit(blit_HUD_lvl,(32+((hud_val-1)*200),(34*16)))
    win_map.blit(blit_HUD_att,(32+((hud_val-1)*200),(35*16)))
    win_map.blit(blit_HUD_hp,(32+((hud_val-1)*200),(36*16)))
    win_map.blit(blit_HUD_mp,(32+((hud_val-1)*200),(37*16)))
    win_map.blit(blit_HUD_status,(32+((hud_val-1)*200),(38*16)))
    win_map.blit(blit_HUD_xp,(32+((hud_val-1)*200),(39*16)))
    win_map.blit(blit_HUD_gp,(32+((hud_val-1)*200),(40*16)))

def func_blit_player_damage(hud_val,hud_val_damage,damage):
    blit_player_damage = myfont.render(str(damage), False, (244, 0, 0))
    if blit_player_damage_amount > 0:
        win_map.blit(blit_player_damage,(32+((hud_val-1)*200),(hud_val_damage*16)))

def func_blit_enemy_HUD(hud_val):
    enemy_number = 0
    for enemy_stats in current_enemies:
        enemy_number += 1
        status_list = []
        for status_condition in enemy_stats.status_effect_list:
            status_list.append(status_condition.name)
        blit_HUD_name = myfont.render(enemy_stats.name, False, (0, 0, 0))
        blit_HUD_lvl = myfont.render("Lvl: " + str(enemy_stats.level), False, (0, 0, 0))
        blit_HUD_att = myfont.render("Att: " + enemy_stats.attribute, False, (0, 0, 0))
        blit_HUD_hp = myfont.render("HP: " + str(enemy_stats.hp) + "/" + str(enemy_stats.maxhp), False, (0, 0, 0))
        blit_HUD_mp = myfont.render("MP: " + str(enemy_stats.mp) + "/" + str(enemy_stats.maxmp), False, (0, 0, 0))
        if len(enemy_stats.status_effect_list) != 0:
            blit_HUD_status = myfont.render("Status: " + str(status_list), False, (0, 0, 0))
        else:
            blit_HUD_status = myfont.render("Status: ['N0NE']", False, (0, 0, 0))

        win_map.blit(blit_HUD_name,(32+((hud_val+enemy_number-1)*200),(33*16)))
        win_map.blit(blit_HUD_lvl,(32+((hud_val+enemy_number-1)*200),(34*16)))
        win_map.blit(blit_HUD_att,(32+((hud_val+enemy_number-1)*200),(35*16)))
        win_map.blit(blit_HUD_hp,(32+((hud_val+enemy_number-1)*200),(36*16)))
        win_map.blit(blit_HUD_mp,(32+((hud_val+enemy_number-1)*200),(37*16)))
        win_map.blit(blit_HUD_status,(32+((hud_val+enemy_number-1)*200),(38*16)))
        win_map.blit(enemy_stats.enemy_sprite, ( ((cx-256) + ((enemy_number+1)*128)), ((cy) + ((1)*32)) )  )
        # win_map.blit(enemy_stats.enemy_sprite,(32+(18(hud_val+enemy_number-1)*200),(18*16)))

def func_blit_title(title_string,gui_val):
    blit_title = myfont.render(title_string, False, (0, 0, 0))
    pygame.draw.rect(win_map, (100,100,100), (32+((gui_val-1)*200), 0, 136, 16))
    win_map.blit(blit_title,(32+((gui_val-1)*200),0))

##############################--MAIN GRAPHICS FUNCTION--################################
#########################################################################################

def func_refresh_pygame(battle_intro):
    battle_intro_ticks = 0
    if dev_mode >= 2:
        print("\nrefreshing pygame window//\n")

    if steps_z >= 0:
        win_map.fill((0,14,214))
    else:
        win_map.fill((100,100,100))


    for scene_type in all_scene_types:
        if scene_type.zpos == steps_z:
            if time != -1:
                if time < 600:
                    tile_r = scene_type.tile_r + (time2/10)
                    tile_g = scene_type.tile_g + (time2/10)
                    tile_b = scene_type.tile_b + (time2/10)
                if time >= 600 and time < 1200:
                    tile_r = (scene_type.tile_r + 60) - (time2/10)
                    tile_g = (scene_type.tile_g + 60) - (time2/10)
                    tile_b = (scene_type.tile_b + 60) - (time2/10)
                if time >= 1200 and time < 1800:
                    tile_r = scene_type.tile_r - (time2/10)
                    tile_g = scene_type.tile_g - (time2/10)
                    tile_b = scene_type.tile_b - (time2/10)
                if time >= 1800:
                    tile_r = (scene_type.tile_r - 60) + (time2/10)
                    tile_g = (scene_type.tile_g - 60) + (time2/10)
                    tile_b = (scene_type.tile_b - 60) + (time2/10)

                if tile_r >= 255:
                    tile_r = 255
                if tile_g >= 255:
                    tile_g = 255
                if tile_b >= 255:
                    tile_b = 255
                if tile_r < 0:
                    tile_r = 0
                if tile_g < 0:
                    tile_g = 0
                if tile_b < 0:
                    tile_b = 0

                tile_r_2 = tile_r - 20
                tile_g_2 = tile_g - 20
                tile_b_2 = tile_b - 20

                if tile_r_2 >= 255:
                    tile_r_2 = 255
                if tile_g_2 >= 255:
                    tile_g_2 = 255
                if tile_b_2 >= 255:
                    tile_b_2 = 255
                if tile_r_2 < 0:
                    tile_r_2 = 0
                if tile_g_2 < 0:
                    tile_g_2 = 0
                if tile_b_2 < 0:
                    tile_b_2 = 0

            win_map.blit(scene_type.tile_sprite, ( ((cx-16) + ((scene_type.xpos - steps_x)*32)), ((cy-16) + ((scene_type.ypos - steps_y)*32)) )  )

            #pygame.draw.rect(win_map, (tile_r,tile_g,tile_b), ( ((cx-16) + ((scene_type.xpos - steps_x)*32)), ((cy-16) + ((scene_type.ypos - steps_y)*32)), map_tile_width, map_tile_height))

            if scene_type.indoors == True:
                win_map.blit(spr_house, ( ((cx-14) + ((scene_type.xpos - steps_x)*32)), ((cy-14) + ((scene_type.ypos - steps_y)*32)) )  )

                #pygame.draw.rect(win_map, (tile_r_2,tile_g_2,tile_b_2), ( ((cx-14) + ((scene_type.xpos - steps_x)*32)), ((cy-14) + ((scene_type.ypos - steps_y)*32)), map_tile_width-4, map_tile_height-12))
            if len(scene_type.npc_list) == 1:
                pygame.draw.rect(win_map, (204,0,0), ( ((cx-12) + ((scene_type.xpos - steps_x)*32)), ((cy-4) + ((scene_type.ypos - steps_y)*32)), map_tile_width-24, map_tile_height-24))
            if len(scene_type.npc_list) > 1:
                pygame.draw.rect(win_map, (182,0,0), ( ((cx+6) + ((scene_type.xpos - steps_x)*32)), ((cy+6) + ((scene_type.ypos - steps_y)*32)), map_tile_width-24, map_tile_height-24))
                pygame.draw.rect(win_map, (204,0,0), ( ((cx-12) + ((scene_type.xpos - steps_x)*32)), ((cy-12) + ((scene_type.ypos - steps_y)*32)), map_tile_width-24, map_tile_height-24))


    # pygame.draw.rect(win_map, (255,0,0), (cx-5, cy-5, char_width, char_height))
    win_map.blit(spr_player,(cx-16, cy-16,))

    if battle_intro == True:
        battle_intro_ticks = 0
    while battle_intro == True:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
                battle_intro = False
                break

        while battle_intro_ticks < 18:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_start = 0
                    battle_intro_ticks = 18
                    break
            for scene_type in all_scene_types:
                if scene_type.zpos == steps_z:
                    if time < 600:
                        tile_r = scene_type.tile_r + (time2/10)
                        tile_g = scene_type.tile_g + (time2/10)
                        tile_b = scene_type.tile_b + (time2/10)
                    if time >= 600 and time < 1200:
                        tile_r = (scene_type.tile_r + 60) - (time2/10)
                        tile_g = (scene_type.tile_g + 60) - (time2/10)
                        tile_b = (scene_type.tile_b + 60) - (time2/10)
                    if time >= 1200 and time < 1800:
                        tile_r = scene_type.tile_r - (time2/10)
                        tile_g = scene_type.tile_g - (time2/10)
                        tile_b = scene_type.tile_b - (time2/10)
                    if time >= 1800:
                        tile_r = (scene_type.tile_r - 60) + (time2/10)
                        tile_g = (scene_type.tile_g - 60) + (time2/10)
                        tile_b = (scene_type.tile_b - 60) + (time2/10)

                    if tile_r >= 255:
                        tile_r = 255
                    if tile_g >= 255:
                        tile_g = 255
                    if tile_b >= 255:
                        tile_b = 255
                    if tile_r < 0:
                        tile_r = 0
                    if tile_g < 0:
                        tile_g = 0
                    if tile_b < 0:
                        tile_b = 0

                    tile_r_2 = tile_r - 20
                    tile_g_2 = tile_g - 20
                    tile_b_2 = tile_b - 20

                    if tile_r_2 >= 255:
                        tile_r_2 = 255
                    if tile_g_2 >= 255:
                        tile_g_2 = 255
                    if tile_b_2 >= 255:
                        tile_b_2 = 255
                    if tile_r_2 < 0:
                        tile_r_2 = 0
                    if tile_g_2 < 0:
                        tile_g_2 = 0
                    if tile_b_2 < 0:
                        tile_b_2 = 0

                    pygame.draw.rect(win_map, (tile_r,tile_g,tile_b), ( ((cx-16) + ((scene_type.xpos - steps_x)*32*random.randint(1,3))), ((cy-16) + ((scene_type.ypos - steps_y)*(32*random.randint(1,3)))), map_tile_width, map_tile_height))

            battle_intro_ticks += 1
            pygame.display.update()
            print("/")

        if battle_intro_ticks >= 18:
            battle_intro = False
            break


    if in_fight == True:

        win_map.fill((20,20,20))
        pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
        pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

        func_blit_list(combat_option,combat_option_list,1)
        func_blit_combat_cursor(1)
        func_blit_title("Battle:",1)



        if in_submenu_cast_combat == True:

            pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

            func_blit_list(spell,equiped_spells,1)

            func_blit_combat_cursor(1)
            func_blit_title("Cast:",1)


        if in_submenu_use_combat == True:

            pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

            func_blit_list(item,inventory,1)

            func_blit_combat_cursor(1)
            func_blit_title("Use item:",1)

        if in_submenu_target_combat2 == True:

            pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

            func_blit_list(combat_option,combat_option_list,1)
            func_blit_title("Battle:",1)

            pygame.draw.rect(win_map, (100,100,100), (200, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (210,10, 180, 480))

            func_blit_list(enemy_stats,current_enemies,2)

            func_blit_combat_cursor(2)
            func_blit_title("Target:",2)

    if in_menu == True and in_submenu == False:

        pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
        pygame.draw.rect(win_map, (125,125,125), (10, 10, 180, 480))

        win_map.blit(txt_talk,(32,(1*16)))
        win_map.blit(txt_cast,(32,(2*16)))
        win_map.blit(txt_equip,(32,(3*16)))
        win_map.blit(txt_gear,(32,(4*16)))
        win_map.blit(txt_spellbook,(32,(5*16)))
        win_map.blit(txt_camp,(32,(6*16)))
        win_map.blit(txt_inv,(32,(7*16)))
        win_map.blit(txt_consume,(32,(8*16)))
        win_map.blit(txt_make,(32,(9*16)))
        win_map.blit(txt_pickup,(32,(10*16)))
        win_map.blit(txt_pickupall,(32,(11*16)))
        win_map.blit(txt_drop,(32,(12*16)))
        win_map.blit(txt_search,(32,(13*16)))
        win_map.blit(txt_skills,(32,(14*16)))
        win_map.blit(txt_stats,(32,(15*16)))
        win_map.blit(txt_wait,(32,(16*16)))
        win_map.blit(txt_help,(32,(17*16)))
        win_map.blit(txt_quit,(32,(18*16)))

        func_blit_menu_cursor(1)

    if in_menu == True and in_submenu == True:

        if in_submenu_use == True:

            pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

            func_blit_list(item,inventory,1)
            func_blit_menu_cursor(1)


        if in_submenu_cast == True:

            pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

            func_blit_list(spell,equiped_spells,1)
            func_blit_menu_cursor(1)


        if in_submenu_equip == True:

            pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

            win_map.blit(txt_weapons,(32,(1*16)))
            win_map.blit(txt_armor,(32,(2*16)))
            win_map.blit(txt_helmets,(32,(3*16)))
            win_map.blit(txt_shields,(32,(4*16)))
            win_map.blit(txt_spells,(32,(5*16)))


            func_blit_menu_cursor(1)
            func_blit_title("Equip:",1)

            if in_submenu_equip2 == True:

                pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (200, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (210,10, 180, 480))

                if in_menu_weapon == True:
                    func_blit_list(weapon,weapon_inventory,2)
                if in_menu_armor == True:
                    func_blit_list(armor,armor_inventory,2)
                if in_menu_helmet == True:
                    func_blit_list(helmet,helmet_inventory,2)
                if in_menu_shield == True:
                    func_blit_list(shield,shield_inventory,2)
                if in_menu_spell == True:
                    func_blit_list(spell,spell_inventory,2)

                func_blit_menu_cursor(2)
                func_blit_title("Equip 2:",2)

        if in_submenu_talk == True:

            pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

            for scene_type in location:
                for npc in scene_type.npc_list:
                    func_blit_npc_list(npc,scene_type.npc_list,1)
                    break


            func_blit_menu_cursor(1)
            func_blit_title("Talk:",1)

            if in_submenu_talk2 == True:

                pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (200, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (210,10, 180, 480))
                for npc in current_npc:
                    func_blit_dialouge_list(dialouge_option,npc.dialouge_options_list,2)

                func_blit_menu_cursor(2)
                func_blit_title("Talk 2:",2)

                if in_submenu_sell3 == True:

                    pygame.draw.rect(win_map, (100,100,100), (200, 0, 200, 500))
                    pygame.draw.rect(win_map, (125,125,125), (210,10, 180, 480))


                    pygame.draw.rect(win_map, (100,100,100), (400, 0, 200, 500))
                    pygame.draw.rect(win_map, (125,125,125), (410, 10, 180, 480))

                    win_map.blit(txt_items,(432,(1*16)))
                    win_map.blit(txt_weapons,(432,(2*16)))
                    win_map.blit(txt_armor,(432,(3*16)))
                    win_map.blit(txt_helmets,(432,(4*16)))
                    win_map.blit(txt_shields,(432,(5*16)))
                    win_map.blit(txt_spells,(432,(6*16)))


                    func_blit_menu_cursor(3)
                    func_blit_title("Sell 3:",3)

                    if in_submenu_sell4== True:

                        pygame.draw.rect(win_map, (100,100,100), (400, 0, 200, 500))
                        pygame.draw.rect(win_map, (125,125,125), (410, 10, 180, 480))


                        pygame.draw.rect(win_map, (100,100,100), (600, 0, 200, 500))
                        pygame.draw.rect(win_map, (125,125,125), (610,10, 180, 480))

                        if in_menu_item == True:
                            func_blit_list(item,inventory,4)
                        if in_menu_weapon == True:
                            func_blit_list(weapon,weapon_inventory,4)
                        if in_menu_armor == True:
                            func_blit_list(armor,armor_inventory,4)
                        if in_menu_helmet == True:
                            func_blit_list(helmet,helmet_inventory,4)
                        if in_menu_shield == True:
                            func_blit_list(shield,shield_inventory,4)
                        if in_menu_spell == True:
                            func_blit_list(spell,spell_inventory,4)

                        func_blit_menu_cursor(4)
                        func_blit_title("Sell 4:",4)

                if in_submenu_buy3 == True:

                    pygame.draw.rect(win_map, (100,100,100), (200, 0, 200, 500))
                    pygame.draw.rect(win_map, (125,125,125), (210,10, 180, 480))

                    pygame.draw.rect(win_map, (100,100,100), (400, 0, 200, 500))
                    pygame.draw.rect(win_map, (125,125,125), (410, 10, 180, 480))

                    for npc in current_npc:
                        if in_menu_item == True:
                            func_blit_list(item,npc.npc_inventory,3)
                        if in_menu_weapon == True:
                            func_blit_list(weapon,npc.npc_weapon_inventory,3)
                        if in_menu_armor == True:
                            func_blit_list(armor,npc.npc_armor_inventory,3)
                        if in_menu_helmet == True:
                            func_blit_list(helmet,npc.npc_helmet_inventory,3)
                        if in_menu_shield == True:
                            func_blit_list(shield,npc.npc_shield_inventory,3)
                        if in_menu_spell == True:
                            func_blit_list(spell,npc.npc_spell_inventory,3)

                    func_blit_menu_cursor(3)
                    func_blit_title("Buy 3:",3)
        if in_submenu_drop == True:

            pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

            win_map.blit(txt_items,(32,(1*16)))
            win_map.blit(txt_weapons,(32,(2*16)))
            win_map.blit(txt_armor,(32,(3*16)))
            win_map.blit(txt_helmets,(32,(4*16)))
            win_map.blit(txt_shields,(32,(5*16)))
            win_map.blit(txt_spells,(32,(6*16)))


            func_blit_menu_cursor(1)
            func_blit_title("Drop:",1)

            if in_submenu_drop2 == True:

                pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (200, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (210,10, 180, 480))

                if in_menu_item == True:
                    func_blit_list(item,inventory,2)
                if in_menu_weapon == True:
                    func_blit_list(weapon,weapon_inventory,2)
                if in_menu_armor == True:
                    func_blit_list(armor,armor_inventory,2)
                if in_menu_helmet == True:
                    func_blit_list(helmet,helmet_inventory,2)
                if in_menu_shield == True:
                    func_blit_list(shield,shield_inventory,2)
                if in_menu_spell == True:
                    func_blit_list(spell,spell_inventory,2)

                func_blit_menu_cursor(2)
                func_blit_title("Drop 2:",2)


    pygame.draw.rect(win_map, (100,100,100), (0, 512, 1024, 256))
    pygame.draw.rect(win_map, (125,125,125), (10,522, 1004, 236))

    func_blit_HUD(1)
    func_blit_enemy_HUD(1)
    func_blit_player_damage(1,32,blit_player_damage_amount)
    pygame.display.update()

#########################################################################################
##############################--SHOP INVENTORY FUNCTIONS--##############################

def func_shop_restock():
    chance = 1
    item_chance = 1
    global restock_ticks #int
    global restock_shops #bool
    restock_ticks += 1
    if restock_ticks < 0:
        restock_ticks = 0
        if restock_shops == True:
            print("\n////////////////////////////   shops restocked!   //////////////////////////////\n")
            for npc in all_npcs:
                for item in npc.npc_inventory:
                    # chance = random.randint(0,1)
                    if chance == 1:
                        npc.npc_inventory.remove(item)
                        print(item.name + " removed from " + npc.first_name + npc.last_name)
                for item in items_shop_table:
                    # item_chance = random.randint(0,1)
                    if item_chance == 1:
                        npc.npc_inventory.append(item)
                        print(item.name + " appended to " + npc.first_name + npc.last_name)

#############################----COMBAT FUNCTIONS----#########################

def func_player_mp_change(amount,is_add):
    if is_add == True:
        player1.mp += amount
        if player1.mp > player1.max_mp:
            player1.mp = player1.max_mp
    if is_add == False:
        player1.mp -= amount
        if player1.mp < 0:
            player1.mp = 0

def func_choose_combat_option():
    target_combat_option = "0"
    selected_combat_option = "0"
    for combat_option in combat_option_list:
        print("|| " + str((combat_option_list.index(combat_option)+1)) + " || " + combat_option.name )

    combat_option_input = input("\nwhat do you want to do?\n")
    has_option = False
    if combat_option_input.isdigit():
        val_combat_option_input = int(combat_option_input)
        val_combat_input = val_combat_option_input - 1
        for combat_option in combat_option_list:
            if val_combat_input == combat_option_list.index(combat_option):
                target_combat_option = combat_option.name
    else:
        for combat_option in combat_option_list:
            if combat_option.name == combat_option_input:
                target_combat_option = combat_option.name

    for combat_option in combat_option_list:
        if target_combat_option == combat_option.name:
            has_option = True
            print("you selected " + combat_option.name + "\n")
            selected_combat_option = target_combat_option
            break
    return selected_combat_option

def func_choose_enemy():
    global in_fight
    #rolls for which enemies to fight
    compatible_enemies_found = False
    enemy_count = 0
    enemy_count = random.randint(1,4)
    while len(current_enemies) < enemy_count:
        if dev_mode >= 1:
            print("looking for " + str(enemy_count) + " enemies")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
        for scene_type in location:
            scene_level = scene_type.difficulty
            for enemy_stats in all_game_enemies:
                if enemy_stats.level <= scene_level + 5 and enemy_stats.level >= scene_level - 15:
                    compatible_enemies_found = True
        if compatible_enemies_found == True:
            for enemy_stats in all_game_enemies:
                encounter_chance = 0
                encounter_chance = random.randint(1,10)
                if encounter_chance == 1 and enemy_stats not in current_enemies and len(current_enemies) < enemy_count and enemy_stats.level <= scene_level and enemy_stats.level >= scene_level - 10:
                    current_enemies.append(enemy_stats)
        if compatible_enemies_found == False:
            print("no compatitible enemies found for difficulty level of scene!")
            in_fight = False

def func_enemy_dead(enemy_stats):

            print("\n// " + enemy_stats.name.upper() + " IS DEAD! // \n")
            sleep(sleep_time)
            player1.gp = player1.gp + enemy_stats.gp
            player1.xp = player1.xp + enemy_stats.xp
            print(enemy_stats.gp)
            print("gold obtained \n")
            sleep(sleep_time)
            print(enemy_stats.xp)
            print("xp obtained \n")
            sleep(sleep_time)

            loot_spawn_chance_item = 0
            loot_chance_item = 0
            loot_amount_item = 0
            loot_spawn_chance_weapon = 0
            loot_chance_weapon = 0
            loot_amount_weapon = 0

            loot_spawn_chance_armor = 0
            loot_chance_armor = 0
            loot_amount_armor = 0

            loot_spawn_chance_helmet = 0
            loot_chance_helmet = 0
            loot_amount_helmet = 0

            loot_spawn_chance_shield = 0
            loot_chance_shield = 0
            loot_amount_shield = 0

            loot_quality = 0

            loot_spawn_chance_item = 1
            loot_spawn_chance_weapon = random.randint(0,1)
            loot_spawn_chance_armor = random.randint(0,1)
            loot_spawn_chance_helmet = random.randint(0,1)
            loot_spawn_chance_shield = random.randint(0,1)

            if len(enemy_stats.drop_table_items_always) != 0:
                for item in enemy_stats.drop_table_items_always:
                    loot_chance_item = 1
                    if loot_chance_item == 1:
                        for ground_item in all_ground_game_items:
                            item_dropped = False
                            if item_dropped == False and ground_item.name == item.name and ground_item not in scene_type.scene_inventory:
                                scene_type.scene_inventory.append(ground_item)
                                print(enemy_stats.name + " dropped " + item.print_name + " \n")
                                item_dropped = True

                            if item_dropped == False and ground_item.name == item.name and ground_item in scene_type.scene_inventory:
                                for ground_item in scene_type.scene_inventory:
                                    if ground_item.name == item.name:
                                        ground_item.item_amount += 1
                                print(item.name + ' is already on the ground!')
                                item_dropped = True

                        loot_amount_item = random.randint(0,10)
                        if loot_amount_item == 10:
                            break

            if loot_spawn_chance_item == 1:
                if len(enemy_stats.drop_table_items) != 0:
                    for item in enemy_stats.drop_table_items:
                        loot_chance_item = random.randint(0,1)
                        if loot_chance_item == 1:
                            for ground_item in all_ground_game_items:
                                item_dropped = False
                                if item_dropped == False and ground_item.name == item.name and ground_item not in scene_type.scene_inventory:
                                    scene_type.scene_inventory.append(ground_item)
                                    print(enemy_stats.name + " dropped " + item.print_name)
                                    item_dropped = True

                                if item_dropped == False and ground_item.name == item.name and ground_item in scene_type.scene_inventory:
                                    for ground_item in scene_type.scene_inventory:
                                        if ground_item.name == item.name:
                                            ground_item.item_amount += 1
                                    print(item.name + ' is already on the ground!')
                                    item_dropped = True

                            loot_amount_item = random.randint(0,10)
                            if loot_amount_item == 10:
                                break

            if len(enemy_stats.drop_table_weapons_always) != 0:
                for weapon in enemy_stats.drop_table_weapons_always:
                    loot_chance_weapon = 1
                    if loot_chance_weapon == 1:
                        for ground_weapon in all_ground_game_weapons:
                            if ground_weapon.name == weapon.name:
                                scene_type.scene_weapon_inventory.append(ground_weapon)
                                print(enemy_stats.name + " dropped " + weapon.print_name + " \n" )
                                sleep(sleep_time_fast)
                        loot_amount_weapon = random.randint(0,1)
                        if loot_amount_weapon != 1:
                            break

            if loot_spawn_chance_weapon == 1:
                if len(enemy_stats.drop_table_weapons) != 0:
                    for weapon in enemy_stats.drop_table_weapons:
                        loot_chance_weapon = random.randint(0,1)
                        if loot_chance_weapon == 1:
                            for ground_weapon in all_ground_game_weapons:
                                if ground_weapon.name == weapon.name:
                                    scene_type.scene_weapon_inventory.append(ground_weapon)
                                    print(enemy_stats.name + " dropped " + weapon.print_name + " \n" )
                                    sleep(sleep_time_fast)
                            loot_amount_weapon = random.randint(0,10)
                            if loot_amount_weapon != 10:
                                break

            if len(enemy_stats.drop_table_armor_always) != 0:
                for armor in enemy_stats.drop_table_armor_always:
                    loot_chance_armor = random.randint(0,1)
                    if loot_chance_armor == 1:
                        for ground_armor in all_ground_game_armor:
                            if ground_armor.name == armor.name:
                                scene_type.scene_armor_inventory.append(ground_armor)
                                print(enemy_stats.name + " dropped " + armor.print_name + " \n" )
                                sleep(sleep_time_fast)
                        loot_amount_armor = random.randint(0,1)
                        if loot_amount_armor != 1:
                            break

            if loot_spawn_chance_armor == 1:
                if len(enemy_stats.drop_table_armor) != 0:
                    for armor in enemy_stats.drop_table_armor:
                        loot_chance_armor = random.randint(0,1)
                        if loot_chance_armor == 1:
                            for ground_armor in all_ground_game_armor:
                                if ground_armor.name == armor.name:
                                    scene_type.scene_armor_inventory.append(ground_armor)
                                    print(enemy_stats.name + " dropped " + armor.print_name + " \n" )
                                    sleep(sleep_time_fast)
                            loot_amount_armor = random.randint(0,10)
                            if loot_amount_armor != 10:
                                break

            if len(enemy_stats.drop_table_helmets_always) != 0:
                for helmet in enemy_stats.drop_table_helmets_always:
                    loot_chance_helmet = random.randint(0,1)
                    if loot_chance_helmet == 1:
                        for ground_helmet in all_ground_game_helmets:
                            if ground_helmet.name == helmet.name:
                                scene_type.scene_helmet_inventory.append(ground_helmet)
                                print(enemy_stats.name + " dropped " + helmet.print_name + " \n" )
                                sleep(sleep_time_fast)
                        loot_amount_helmet = random.randint(0,1)
                        if loot_amount_helmet != 1:
                            break

            if loot_spawn_chance_helmet == 1:
                if len(enemy_stats.drop_table_helmets) != 0:
                    for helmet in enemy_stats.drop_table_helmets:
                        loot_chance_helmet = random.randint(0,1)
                        if loot_chance_helmet == 1:
                            for ground_helmet in all_ground_game_helmets:
                                if ground_helmet.name == helmet.name:
                                    scene_type.scene_helmet_inventory.append(ground_helmet)
                                    print(enemy_stats.name + " dropped " + helmet.print_name + " \n" )
                                    sleep(sleep_time_fast)
                            loot_amount_helmet = random.randint(0,10)
                            if loot_amount_helmet != 10:
                                break

            if len(enemy_stats.drop_table_shields_always) != 0:
                for shield in enemy_stats.drop_table_shields_always:
                    loot_chance_shield = random.randint(0,1)
                    if loot_chance_shield == 1:
                        for ground_shield in all_ground_game_shields:
                            if ground_shield.name == shield.name:
                                scene_type.scene_shield_inventory.append(ground_shield)
                                print(enemy_stats.name + " dropped " + shield.print_name + " \n" )
                                sleep(sleep_time_fast)
                        loot_amount_shield = random.randint(0,1)
                        if loot_amount_shield != 1:
                            break

            if loot_spawn_chance_shield == 1:
                if len(enemy_stats.drop_table_shields) != 0:
                    for shield in enemy_stats.drop_table_shields:
                        loot_chance_shield = random.randint(0,1)
                        if loot_chance_shield == 1:
                            for ground_shield in all_ground_game_shields:
                                if ground_shield.name == shield.name:
                                    scene_type.scene_shield_inventory.append(ground_shield)
                                    print(enemy_stats.name + " dropped " + shield.print_name + " \n" )
                                    sleep(sleep_time_fast)
                            loot_amount_shield = random.randint(0,10)
                            if loot_amount_shield != 10:
                                break

            func_check_level()

def func_get_target():
    global combat_cursor_pos
    global in_submenu2
    global in_submenu_target_combat2

    target = "0"
    if len(current_enemies) > 0:
        if dev_mode >=2:
            print("")
            for enemy_stats in current_enemies:
                print("|| " + str((current_enemies.index(enemy_stats)+1)) + " || LVL: " + str(enemy_stats.level) + " || " + enemy_stats.name + " || ATR: " + enemy_stats.print_attribute)
            print("\nWho will you attack? \n")

        in_submenu2 = True
        in_submenu_target_combat2 = True
        while in_submenu_target_combat2 == True:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_start = 0
                    in_fight = False
                    in_submenu2 = False
                    in_submenu_target_combat2 = False
                    in_menu = False

            func_check_level()
            func_refresh_pygame(False)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_q]:
                in_submenu2 = False
                in_submenu_target_combat2 = False

            if keys[pygame.K_w]:
                if combat_cursor_pos <= 1:
                    combat_cursor_pos == 1
                else:
                    sfx_cursor_move.play()
                    combat_cursor_pos -= 1
                if dev_mode >= 2:
                    print(combat_cursor_pos)

            if keys[pygame.K_s]:
                if combat_cursor_pos >= 18:
                    combat_cursor_pos == 18
                else:
                    sfx_cursor_move.play()
                    combat_cursor_pos += 1
                if dev_mode >= 2:
                    print(combat_cursor_pos)


            if keys[pygame.K_e]:
                sfx_cursor_select.play()
                val_target_input = combat_cursor_pos
                val_enemy = val_target_input - 1
                for enemy_stats in current_enemies:
                    if val_enemy == current_enemies.index(enemy_stats):
                        target = enemy_stats.name
                in_submenu2 = False
                in_submenu_target_combat2 = False
                break
    # else:
    #     for enemy_stats in current_enemies:
    #         target = enemy_stats.name
    return target

def func_player_melee(status_str,status_atk):
    global player_turns
    target = func_get_target()

    for enemy_stats in current_enemies:
        if enemy_stats.name == target:
            player_turns -= 1
            player_weapon_level = 0
            for weapon in equiped_weapon:
                player_weapon_level = weapon.level
            player_damage = (player1.attack + player1.attack_bonus + status_atk + player_weapon_level) + (player1.strength + status_str + player1.strength_bonus + player_weapon_level) + (random.randint(1,player1.level) * (player1.level // 2))
            if player_damage > (enemy_stats.hp):
                player_damage = (enemy_stats.hp)
            enemy_stats.hp = enemy_stats.hp - player_damage
            print("\nyou hit " + enemy_stats.name + " for: " + Fore.RED + Style.BRIGHT + str(player_damage) + Style.RESET_ALL + " melee damage!")
            sleep(sleep_time)
            player1.attack_xp += (player1.attack * (player_damage))
            player1.strength_xp += (player1.strength * (player_damage + player1.strength))
            break

def func_player_spell(status_mgk):
    global val
    global combat_cast_spell
    global menu_cursor_pos
    global combat_cursor_pos
    global in_submenu2
    global in_submenu_spell_target_combat2
    global in_submenu
    global in_submenu_cast_combat
    spell_damage = 0
    for spell in equiped_spells:
        spell_found = False

        if val == equiped_spells.index(spell):
            spell_found = True

        if spell_found == True:
            if player1.mp >= spell.mp_cost:
                func_player_mp_change(spell.mp_cost,False)
                if spell.effect == 0 or spell.effect == 1:
                    target = func_get_target()
                    for enemy_stats in current_enemies:
                        if enemy_stats.name == target:
                            spell_damage = spell.damage
                            print("\nyou cast " + spell.print_name)
                            sleep(sleep_time)
                            for enemy_stats in current_enemies:
                                if enemy_stats.name == target:
                                    player_damage = (player1.level + spell_damage) * (player1.magic + player1.magic_bonus + status_mgk)
                                    if spell.attribute == enemy_stats.weakness or spell.attribute == enemy_stats.attribute:
                                        if spell.attribute == enemy_stats.weakness:
                                            print("it's super effective")
                                            sleep(sleep_time)
                                            player_damage = player_damage * 2
                                        if spell.attribute == enemy_stats.attribute:
                                            print("it's not very effective")
                                            sleep(sleep_time)
                                            player_damage = player_damage // 2
                                    if player_damage > (enemy_stats.hp):
                                        player_damage = (enemy_stats.hp)
                                    enemy_stats.hp = enemy_stats.hp - player_damage
                                    print("\nyou hit " + enemy_stats.name + " for " + Fore.RED + Style.BRIGHT + str(player_damage) + " " + spell.print_attribute + " " + "damage!")
                                    if spell.effect == 1:
                                        player_healing = player_spell_damage // 2
                                        player_stats.hp = player_stats.hp + player_healing
                                        if player_stats.hp > player_stats.maxhp:
                                            player_stats.hp = player_stats.maxhp
                                        print("\n" + player_stats.name + " heals for: " + Fore.GREEN + Style.BRIGHT + str(player_healing))
                                    sleep(sleep_time)
                                    player1.magic_xp += (player1.magic + spell.xp + spell.damage + (player_damage // 100))
                    break
                if spell.effect == 100:
                    spell_healing = spell.damage
                    print("you cast " + spell.print_name)
                    player1.magic_xp += (player1.magic + spell.xp + spell.damage)
                    sleep(sleep_time)
                    player_healing = (player1.level + spell_healing) * (player1.magic + player1.magic_bonus + status_mgk)
                    player_stats.hp = player_stats.hp + player_healing
                    if player_stats.hp > player_stats.maxhp:
                        player_stats.hp = player_stats.maxhp
                    print("\nyou heal for:" + Fore.GREEN + Style.BRIGHT + str(player_healing))
                    sleep(sleep_time)
                    player1.magic_xp += (player1.magic + spell.xp + spell.damage)
                    break
                if spell.effect == 2:
                    target = func_get_target()
                    for enemy_stats in current_enemies:
                        if enemy_stats.name == target:
                            print("you cast " + spell.print_name)
                            if frozen not in enemy_stats.status_effect_list:
                                enemy_stats.status_effect_list.append(frozen)
                                print("you freeze the " + enemy_stats.name)
                            if spell.utility == False:
                                for enemy_stats in current_enemies:
                                    if enemy_stats.name == target:
                                        player_damage = (player1.level + spell_damage) * (player1.magic + player1.magic_bonus + status_mgk)
                                        if spell.attribute == enemy_stats.weakness or spell.attribute == enemy_stats.attribute:
                                            if spell.attribute == enemy_stats.weakness:
                                                print("it's super effective")
                                                sleep(sleep_time)
                                                player_damage = player_damage * 2
                                            if spell.attribute == enemy_stats.attribute:
                                                print("it's not very effective")
                                                sleep(sleep_time)
                                                player_damage = player_damage // 2
                                        if player_damage > (enemy_stats.hp):
                                            player_damage = (enemy_stats.hp)
                                        enemy_stats.hp = enemy_stats.hp - player_damage
                                        print("\nyou hit " + enemy_stats.name + " for " + Fore.RED + Style.BRIGHT + str(player_damage) + " " + spell.print_attribute + " " + "damage!")
                                        if spell.effect == 1:
                                            player_healing = player_spell_damage // 2
                                            player_stats.hp = player_stats.hp + player_healing
                                            if player_stats.hp > player_stats.maxhp:
                                                player_stats.hp = player_stats.maxhp
                                            print("\n" + player_stats.name + " heals for: " + Fore.GREEN + Style.BRIGHT + str(player_healing))
                                        sleep(sleep_time)

                            sleep(sleep_time)
                    break
                if spell.effect == 3:
                    target = func_get_target()
                    for enemy_stats in current_enemies:
                        if enemy_stats.name == target:
                            print("you cast " + spell.print_name)
                            player1.magic_xp += (player1.magic + spell.xp + spell.damage)
                            if poisoned not in enemy_stats.status_effect_list:
                                enemy_stats.status_effect_list.append(poisoned)
                                print("you poison the " + enemy_stats.name)
                            if spell.utility == False:
                                for enemy_stats in current_enemies:
                                    if enemy_stats.name == target:
                                        player_damage = (player1.level + spell_damage) * (player1.magic + player1.magic_bonus + status_mgk)
                                        if spell.attribute == enemy_stats.weakness or spell.attribute == enemy_stats.attribute:
                                            if spell.attribute == enemy_stats.weakness:
                                                print("it's super effective")
                                                sleep(sleep_time)
                                                player_damage = player_damage * 2
                                            if spell.attribute == enemy_stats.attribute:
                                                print("it's not very effective")
                                                sleep(sleep_time)
                                                player_damage = player_damage // 2
                                        if player_damage > (enemy_stats.hp):
                                            player_damage = (enemy_stats.hp)
                                        enemy_stats.hp = enemy_stats.hp - player_damage
                                        print("\nyou hit " + enemy_stats.name + " for " + Fore.RED + Style.BRIGHT + str(player_damage) + " " + spell.print_attribute + " " + "damage!")
                                        if spell.effect == 1:
                                            player_healing = player_spell_damage // 2
                                            player_stats.hp = player_stats.hp + player_healing
                                            if player_stats.hp > player_stats.maxhp:
                                                player_stats.hp = player_stats.maxhp
                                            print("\n" + player_stats.name + " heals for: " + Fore.GREEN + Style.BRIGHT + str(player_healing))
                                        sleep(sleep_time)
                            sleep(sleep_time)
                    break
                if spell.effect == 4:
                    target = func_get_target()
                    for enemy_stats in current_enemies:
                        if enemy_stats.name == target:
                            print("you cast " + spell.print_name)
                            player1.magic_xp += (player1.magic + spell.xp + spell.damage)
                            if burning not in enemy_stats.status_effect_list:
                                enemy_stats.status_effect_list.append(burning)
                                print("you burn the " + enemy_stats.name)
                            if spell.utility == False:
                                for enemy_stats in current_enemies:
                                    if enemy_stats.name == target:
                                        player_damage = (player1.level + spell_damage) * (player1.magic + player1.magic_bonus + status_mgk)
                                        if spell.attribute == enemy_stats.weakness or spell.attribute == enemy_stats.attribute:
                                            if spell.attribute == enemy_stats.weakness:
                                                print("it's super effective")
                                                sleep(sleep_time)
                                                player_damage = player_damage * 2
                                            if spell.attribute == enemy_stats.attribute:
                                                print("it's not very effective")
                                                sleep(sleep_time)
                                                player_damage = player_damage // 2
                                        if player_damage > (enemy_stats.hp):
                                            player_damage = (enemy_stats.hp)
                                        enemy_stats.hp = enemy_stats.hp - player_damage
                                        print("\nyou hit " + enemy_stats.name + " for " + Fore.RED + Style.BRIGHT + str(player_damage) + " " + spell.print_attribute + " " + "damage!")
                                        if spell.effect == 1:
                                            player_healing = player_spell_damage // 2
                                            player_stats.hp = player_stats.hp + player_healing
                                            if player_stats.hp > player_stats.maxhp:
                                                player_stats.hp = player_stats.maxhp
                                            print("\n" + player_stats.name + " heals for: " + Fore.GREEN + Style.BRIGHT + str(player_healing))
                                        sleep(sleep_time)

                            sleep(sleep_time)
                    break
            else:
                print(Fore.RED + "\nNOT ENOUGH MANA!\n")
                break
    func_check_level()
    in_submenu = False
    in_submenu_cast_combat = False
    in_submenu2 = False
    in_submenu_spell_target_combat2 = False

def func_player_spell_non_combat(cast_spell):
    for spell in equiped_spells:
        if spell.name == cast_spell:
            if spell.effect == 0:

                print("\nyou are not in combat...")

            if spell.effect == 100:
                spell_healing = spell.damage
                print("you cast " + spell.print_name)
                player_healing = (player1.level + spell_healing) * (player1.magic + player1.magic_bonus)
                player_stats.hp = player_stats.hp + player_healing
                if player_stats.hp > player_stats.maxhp:
                    player_stats.hp = player_stats.maxhp
                print("\nspell healing: ")
                print(spell_healing)
                print("\nyou heal for:")
                print(player_healing)
                player1.magic_xp += (player_healing)

def func_player_status_check(is_attack_type_hit,force_no_attack):

    for player_stats in players:
        status_str_bonus = 1
        status_atk_bonus = 1
        status_mgk_bonus = 1
        status_def_bonus = 1
        player_can_attack = False
        if len(player_stats.status_effect_list) == 0:
            player_can_attack = True
        else:
            for status_condition in player_stats.status_effect_list:
                if status_condition.is_freeze == True:
                    freeze_chance = 0
                    freeze_chance = random.randint(1,6)
                    if freeze_chance != 1:
                        print("\n" + player_stats.name + " is frozen and cannot attack!")
                        player_can_attack = False
                    else:
                        print("\n" + player_stats.name + " broke free from the ice!")
                        player_stats.status_effect_list.remove(status_condition)
                        player_can_attack = True

                if status_condition.is_poisoned == True:
                    poison_chance = 0
                    poison_chance = random.randint(1,5)
                    if poison_chance != 1:
                        player_poison_damage = (player_stats.hp // 100) + (status_condition.scalar * 10)
                        player_stats.hp -= player_poison_damage
                        print("\n" + player_stats.name + " takes " + str(player_poison_damage) + " poison damage!")
                        func_check_player_dead()
                        player_can_attack = True
                    else:
                        print("\n" + player_stats.name + " is no longer poisoned")
                        player_stats.status_effect_list.remove(status_condition)
                        player_can_attack = True

                if status_condition.is_burning == True:
                    burn_chance = 0
                    burn_chance = random.randint(1,11)
                    if burn_chance != 1:
                        player_burn_damage = (player_stats.hp // 100) + (status_condition.scalar * 10)
                        player_stats.hp -= player_burn_damage
                        print("\n" + player_stats.name + " is on fire and takes " + str(player_burn_damage)+ " damage!")
                        func_check_player_dead()
                        player_can_attack = True
                    else:
                        print("\n" + player_stats.name + " is no longer burning")
                        player_stats.status_effect_list.remove(status_condition)
                        player_can_attack = True

                if status_condition.is_str_up == True:
                    status_str_bonus = (player_stats.strength // 4) + (2 * status_condition.scalar)
                    player_can_attack = True

                if status_condition.is_atk_up == True:
                    status_atk_bonus = (player_stats.attack // 4) + (2 * status_condition.scalar)
                    player_can_attack = True

                if status_condition.is_mgk_up == True:
                    status_mgk_bonus = (player_stats.magic // 4) + (2 * status_condition.scalar)
                    player_can_attack = True

                if status_condition.is_def_up == True:
                    status_def_bonus = (player_stats.defence // 4) + (2 * status_condition.scalar)
                    player_can_attack = True

        if force_no_attack == True:
            player_can_attack = False

        if player_can_attack == True:
            if is_attack_type_hit == False:
                func_player_spell(status_mgk_bonus)
            if is_attack_type_hit == True:
                func_player_melee(status_str_bonus,status_atk_bonus)

def func_check_player_dead():
    if player1.hp <= 0:
        in_fight = False
        del current_enemies[:]
        dead_timer = 10
        while dead_timer > 0:
            dead_timer -= 1
            print("YOU ARE DEAD!")
        game_start = 0
        exit()

def func_enemy_status_check():

    for enemy_stats in current_enemies:
        status_str_bonus = 1
        status_atk_bonus = 1
        status_mgk_bonus = 1
        status_def_bonus = 1
        enemy_can_attack = False
        if len(enemy_stats.status_effect_list) == 0:
            enemy_can_attack = True
        else:
            for status_condition in enemy_stats.status_effect_list:
                if status_condition.is_freeze == True:
                    freeze_chance = 0
                    freeze_chance = random.randint(1,6)
                    if freeze_chance != 1:
                        print(enemy_stats.name + " is frozen and cannot attack!\n")
                        enemy_can_attack = False
                    else:
                        print(enemy_stats.name + " broke free from the ice!\n")
                        enemy_stats.status_effect_list.remove(status_condition)
                        enemy_can_attack = True

                if status_condition.is_poisoned == True:
                    poison_chance = 0
                    poison_chance = random.randint(1,5)
                    if poison_chance != 1:
                        enemy_poison_damage = (enemy_stats.hp // 100) + (status_condition.scalar * 10)
                        enemy_stats.hp -= enemy_poison_damage
                        print(enemy_stats.name + " takes " + str(enemy_poison_damage) + " poison damage!\n")
                        func_check_enemy_dead()
                        enemy_can_attack = True
                    else:
                        print(enemy_stats.name + " is no longer poisoned\n")
                        enemy_stats.status_effect_list.remove(status_condition)
                        enemy_can_attack = True

                if status_condition.is_burning == True:
                    burn_chance = 0
                    burn_chance = random.randint(1,11)
                    if burn_chance != 1:
                        enemy_burn_damage = (enemy_stats.hp // 100) + (status_condition.scalar * 10)
                        enemy_stats.hp -= enemy_burn_damage
                        print(enemy_stats.name + " is on fire and takes " + str(enemy_burn_damage)+ " damage!\n")
                        func_check_enemy_dead()
                        enemy_can_attack = True
                    else:
                        print(enemy_stats.name + " is no longer burning\n")
                        enemy_stats.status_effect_list.remove(status_condition)
                        enemy_can_attack = True

                if status_condition.is_str_up == True:
                    status_str_bonus = (enemy_stats.strength // 4) + (2 * status_condition.scalar)
                    enemy_can_attack = True

                if status_condition.is_atk_up == True:
                    status_atk_bonus = (enemy_stats.attack // 4) + (2 * status_condition.scalar)
                    enemy_can_attack = True

                if status_condition.is_mgk_up == True:
                    status_mgk_bonus = (enemy_stats.magic // 4) + (2 * status_condition.scalar)
                    enemy_can_attack = True

                if status_condition.is_def_up == True:
                    status_def_bonus = (enemy_stats.defence // 4) + (2 * status_condition.scalar)
                    enemy_can_attack = True

        if enemy_can_attack == True:
            func_enemy_attack(enemy_stats,status_str_bonus,status_atk_bonus,status_mgk_bonus,status_def_bonus)

def func_check_enemy_dead():
    global npc_enemy_fname
    global npc_enemy_lname
    global in_fight
    global npc_fight
    for enemy_stats in current_enemies:
        if enemy_stats.hp <= 0:
            current_enemies.remove(enemy_stats)
            func_enemy_dead(enemy_stats)

    if len(current_enemies) == 0:
        in_fight = False
        for scene_type in location:
            for npc in scene_type.npc_list:
                if npc_enemy_fname == npc.first_name and npc_enemy_lname == npc.last_name:
                    print("\n" + npc.first_name + "" + npc.last_name + " is dead...")
                    scene_type.npc_list.remove(npc)
                    npc_fight = False

def func_enemy_attack(enemy_stats,status_str,status_atk,status_mgk,status_def):

    global blit_player_damage_amount

    if (not enemy_stats.spellbook):
        func_enemy_melee(enemy_stats)
    else:
        player_magic_level = 0
        player_defence_level = 0
        enemy_spell_damage = 0
        spell_damage = 0

        player_magic_level = player1.magic
        player_defence_level = player1.defence
        for spell in enemy_stats.spellbook:
            spellchance = random.randint(0,1)
            if spell.effect >= 2 and spell.effect == player1.status_effect:
                spellchance = 0
            if spellchance == 1:
                if spell.effect == 0 or spell.effect == 1:
                    print("\n" + enemy_stats.name + " casts:")
                    print(spell.print_name)
                    sleep(sleep_time)
                    spell_damage = spell.damage
                    enemy_spell_damage = (enemy_stats.level + spell_damage) * (enemy_stats.magic + status_mgk)
                    enemy_spell_damage = enemy_spell_damage // (player1.magic + player1.defence + player1.defence_bonus // 10)
                    player1.hp = player1.hp - (enemy_spell_damage)
                    print("\n" + enemy_stats.name + " hit you for " + Fore.RED + Style.BRIGHT + str(enemy_spell_damage) + Style.RESET_ALL + " " + spell.print_attribute + " " + "damage!\n")
                    if spell.effect == 1:
                        enemy_healing = enemy_spell_damage // 2
                        enemy_stats.hp = enemy_stats.hp + enemy_healing
                        if enemy_stats.hp > enemy_stats.maxhp:
                            enemy_stats.hp = enemy_stats.maxhp
                        print("\n" + enemy_stats.name + " heals for: " + Fore.GREEN + Style.BRIGHT + str(enemy_healing))
                    blit_player_damage_amount = enemy_spell_damage
                    func_check_player_dead()
                    break
                if spell.effect == 100:
                    spell_healing = spell.damage
                    print("\n" + enemy_stats.name + " casts :")
                    print(spell.print_name)
                    sleep(sleep_time)
                    enemy_healing = (enemy_stats.level + spell_healing) * enemy_stats.magic
                    enemy_stats.hp = enemy_stats.hp + enemy_healing
                    if enemy_stats.hp > enemy_stats.maxhp:
                        enemy_stats.hp = enemy_stats.maxhp
                    print("\n" + enemy_stats.name + " heals for: " + Fore.GREEN + Style.BRIGHT + str(enemy_healing))
                    sleep(sleep_time)
                    break
                if spell.effect == 2:
                    print("\n" + enemy_stats.name + " casts :")
                    print(spell.print_name)
                    sleep(sleep_time)
                    for player_stats in players:
                        if frozen not in player_stats.status_effect_list:
                            player_stats.status_effect_list.append(frozen)
                            print("you were frozen by the " + enemy_stats.name)
                        if spell.utility == False:
                            spell_damage = spell.damage
                            enemy_spell_damage = (enemy_stats.level + spell_damage) * (enemy_stats.magic + status_mgk)
                            enemy_spell_damage = enemy_spell_damage // (player1.magic + player1.defence + player1.defence_bonus // 10)
                            player1.hp = player1.hp - (enemy_spell_damage)
                            print("\n" + enemy_stats.name + " hit you for " + Fore.RED + Style.BRIGHT + str(enemy_spell_damage) + Style.RESET_ALL + " " + spell.print_attribute + " " + "damage!")
                            func_check_player_dead()
                    sleep(sleep_time)
                    break
                if spell.effect == 3:
                    print("\n" + enemy_stats.name + " casts :")
                    print(spell.print_name)
                    sleep(sleep_time)
                    for player_stats in players:
                        if poisoned not in player_stats.status_effect_list:
                            player_stats.status_effect_list.append(poisoned)
                            print("you were poisoned by the " + enemy_stats.name)
                        if spell.utility == False:
                            spell_damage = spell.damage
                            enemy_spell_damage = (enemy_stats.level + spell_damage) * (enemy_stats.magic + status_mgk)
                            enemy_spell_damage = enemy_spell_damage // (player1.magic + player1.defence + player1.defence_bonus // 10)
                            player1.hp = player1.hp - (enemy_spell_damage)
                            print("\n" + enemy_stats.name + " hit you for " + Fore.RED + Style.BRIGHT + str(enemy_spell_damage) + Style.RESET_ALL + " " + spell.print_attribute + " " + "damage!")
                            func_check_player_dead()
                    sleep(sleep_time)
                    break
                if spell.effect == 4:
                    print("\n" + enemy_stats.name + " casts :")
                    print(spell.print_name)
                    sleep(sleep_time)
                    for player_stats in players:
                        if burning not in player_stats.status_effect_list:
                            player_stats.status_effect_list.append(burning)
                            print("you were burnt by the " + enemy_stats.name)
                        if spell.utility == False:
                            spell_damage = spell.damage
                            enemy_spell_damage = (enemy_stats.level + spell_damage) * (enemy_stats.magic + status_mgk)
                            enemy_spell_damage = enemy_spell_damage // (player1.magic + player1.defence + player1.defence_bonus // 10)
                            player1.hp = player1.hp - (enemy_spell_damage)
                            print("\n" + enemy_stats.name + " hit you for " + Fore.RED + Style.BRIGHT + str(enemy_spell_damage) + Style.RESET_ALL + " " + spell.print_attribute + " " + "damage!")
                            func_check_player_dead()
                    sleep(sleep_time)
                    break
                break
            else:
                func_enemy_melee(enemy_stats)
                break

def func_enemy_melee(enemy_stats):
    global blit_player_damage_amount
    for player_stats in players:
        player_armor_level = 0
        enemy_damage = 0
        for armor in equiped_armor:
            player_armor_level = armor.level
        enemy_damage = (enemy_stats.attack + enemy_stats.strength + (random.randint(1,5) * (enemy_stats.level // 2)))
        enemy_damage = (enemy_damage * enemy_damage)//(player_armor_level + player1.defence + player1.defence_bonus)
        player_stats.hp = player_stats.hp - enemy_damage
        print("\n" + enemy_stats.name + " hit you for " + Fore.RED + Style.BRIGHT + str(enemy_damage) + Style.RESET_ALL + " melee damage!" )
        blit_player_damage_amount = enemy_damage
        player1.defence_xp += (player1.defence * (enemy_damage))
        func_check_player_dead()

def func_use_combat(gear,player_gear_inv):
    global combat_cursor_pos
    global in_submenu
    global in_submenu_use_combat
    global player_turns

    eaten_item = "0"
    for gear in player_gear_inv:
        if gear in all_game_items:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + str(gear.value) + " gp. " + " || " + str(gear.item_desc) + "... ")

    in_submenu = True
    in_submenu_use_combat = True
    while in_submenu_use_combat == True:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
                in_fight = False
                in_submenu = False
                in_submenu_use_combat = False
                in_menu = False

        func_check_level()
        func_refresh_pygame(False)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            in_submenu = False
            in_submenu_use_combat = False

        if keys[pygame.K_w]:
            if combat_cursor_pos <= 1:
                combat_cursor_pos == 1
            else:
                sfx_cursor_move.play()
                combat_cursor_pos -= 1
            if dev_mode >= 2:
                print(combat_cursor_pos)

        if keys[pygame.K_s]:
            if combat_cursor_pos >= 18:
                combat_cursor_pos == 18
            else:
                sfx_cursor_move.play()
                combat_cursor_pos += 1
            if dev_mode >= 2:
                print(combat_cursor_pos)


        if keys[pygame.K_e]:
            sfx_cursor_select.play()
            has_item = False
            val_used_item = combat_cursor_pos
            val_use = val_used_item - 1
            for gear in player_gear_inv:
                if val_use == player_gear_inv.index(gear):
                    eaten_item = gear.name

            for item in inventory:
                has_item = False
                can_use = False
                for item in inventory:
                    if eaten_item == item.name:
                        has_item = True
                        player_turns -= 1
                        if item.edible == True:
                            if item.poisonous == False:
                                print("you consume " + item.print_name)
                                can_use = True
                                player1.hp = player1.hp + item.hp
                                if player1.hp > player1.maxhp:
                                    player1.hp = player1.maxhp
                            else:
                                print("\nyou consume " + item.print_name + " !\n")
                                can_use = True
                                player1.hp = player1.hp - item.hp
                                print("you feel sick...")

                                if player1.hp <= 0:
                                    print("\nYOU ARE DEAD \n")
                                    game_start = 0

                            if item.name == eaten_item and item.item_amount > 1:
                                has_item_multiple = True
                                item.item_amount -= 1
                            if has_item_multiple == False:
                                for item in inventory:
                                    if item.name == eaten_item:
                                        inventory.remove(item)
                            break

                        if can_use == False:
                            print("you try to use " + item.print_name + ", but nothing interesting happens")

                break

            # if has_item == False:
            #     print("you don't have " + eaten_item)


            in_submenu = False
            in_submenu_use_combat = False

#############################--DIALOUGE FUNCTIONS--#######################

def func_shop(gear,npc_gear_inv):
    global menu_cursor_pos
    global in_submenu3
    global in_submenu_buy3
    global game_start
    global in_menu_item
    global in_menu_weapon
    global in_menu_armor
    global in_menu_helmet
    global in_menu_shield
    global in_menu_spell

    target_gear = "0"
    if player1.gp != -1:
        if game_start == 1:
            print("gold: ", player1.gp)
            print("shop inventory:\n")
            for gear in npc_gear_inv:
                if gear in all_game_weapons:
                    in_menu_weapon = True
                    print("|| " + str((npc_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
                if gear in all_game_armor:
                    in_menu_armor = True
                    print("|| " + str((npc_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
                if gear in all_game_helmets:
                    in_menu_helmet = True
                    print("|| " + str((npc_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
                if gear in all_game_shields:
                    in_menu_shield = True
                    print("|| " + str((npc_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
                if gear in all_game_items:
                    in_menu_item = True
                    print("|| " + str((npc_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + str(gear.value) + " gp. ")
                if gear in all_game_spells:
                    in_menu_spell = True
                    print("|| " + str((npc_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + str(gear.value) + " gp. ")

            in_submenu3 = True
            in_submenu_buy3 = True
            while in_submenu_buy3 == True:
                pygame.time.delay(100)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_start = 0
                        in_fight = False
                        in_submenu3 = False
                        in_submenu_buy3 = False
                        in_menu = False

                func_check_level()
                func_refresh_pygame(False)

                keys = pygame.key.get_pressed()

                if keys[pygame.K_q]:
                    in_submenu3 = False
                    in_submenu_buy3 = False


                if keys[pygame.K_w]:
                    if menu_cursor_pos <= 1:
                        menu_cursor_pos == 1
                    else:
                        sfx_cursor_move.play()
                        menu_cursor_pos -= 1
                    if dev_mode >= 2:
                        print(menu_cursor_pos)

                if keys[pygame.K_s]:
                    if menu_cursor_pos >= 18:
                        menu_cursor_pos == 18
                    else:
                        sfx_cursor_move.play()
                        menu_cursor_pos += 1
                    if dev_mode >= 2:
                        print(menu_cursor_pos)



                if keys[pygame.K_e]:
                    sfx_cursor_select.play()
                    val_bought_item = menu_cursor_pos
                    val_shop = val_bought_item - 1
                    for gear in npc_gear_inv:
                        if val_shop == npc_gear_inv.index(gear):
                            target_gear = gear.name

                    has_item = False
                    has_item_multiple = False
                    for gear in npc_gear_inv:
                        if target_gear == gear.name:
                            has_item = True
                            if player1.gp >= gear.value:
                                player1.gp -= gear.value
                                if gear in all_game_weapons:
                                    weapon_inventory.append(gear)
                                    break
                                if gear in all_game_armor:
                                    armor_inventory.append(gear)
                                    break
                                if gear in all_game_helmets:
                                    helmet_inventory.append(gear)
                                    break
                                if gear in all_game_shields:
                                    shield_inventory.append(gear)
                                    break
                                if gear in all_game_items:
                                    for item in inventory:
                                        if item.name == target_gear:
                                            has_item_multiple = True
                                            item.item_amount += 1
                                            break
                                    if has_item_multiple == False:
                                        for item in all_game_items:
                                            if item.name == target_gear:
                                                inventory.append(item)
                                                break
                                if gear in all_game_spells:
                                    spell_inventory.append(gear)
                                print("\nthanks, enjoy your " + gear.name + "\n")
                                in_submenu3 = False
                                in_submenu_buy3 = False
                                in_menu_item = False
                                in_menu_weapon = False
                                in_menu_armor = False
                                in_menu_helmet = False
                                in_menu_shield = False
                                in_menu_spell = False

                            else:
                                print("You can't afford that!")
                                in_submenu3 = False
                                in_submenu_buy3 = False
                    in_submenu3 = False
                    in_submenu_buy3 = False

        else:
            print("game_start = 0 func_shop aborted")
            in_submenu3 = False
            in_submenu_buy3 = False
    else:
        print("gp = -1, func_shop aborted")
        in_submenu3 = False
        in_submenu_buy3 = False

def func_sell(gear,player_gear_inv):
    global in_menu_item
    global in_menu_weapon
    global in_menu_armor
    global in_menu_helmet
    global in_menu_shield
    global in_menu_spell
    global menu_cursor_pos
    global in_submenu4
    global in_submenu_sell4
    target_gear = "0"
    for gear in player_gear_inv:
        if gear in all_game_weapons:
            in_menu_weapon = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_armor:
            in_menu_armor = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_helmets:
            in_menu_helmet = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_shields:
            in_menu_shield = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_items:
            in_menu_item = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + str(gear.value) + " gp. ")
        if gear in all_game_spells:
            in_menu_spell = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + str(gear.value) + " gp. ")

    in_submenu4 = True
    in_submenu_sell4 = True
    while in_submenu_sell4 == True:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
                in_fight = False
                in_submenu4 = False
                in_submenu_sell4 = False
                in_menu = False

        func_check_level()
        func_refresh_pygame(False)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            in_submenu4 = False
            in_submenu_sell4 = False


        if keys[pygame.K_w]:
            if menu_cursor_pos <= 1:
                menu_cursor_pos == 1
            else:
                sfx_cursor_move.play()
                menu_cursor_pos -= 1
            if dev_mode >= 2:
                print(menu_cursor_pos)

        if keys[pygame.K_s]:
            if menu_cursor_pos >= 18:
                menu_cursor_pos == 18
            else:
                sfx_cursor_move.play()
                menu_cursor_pos += 1
            if dev_mode >= 2:
                print(menu_cursor_pos)


        if keys[pygame.K_e]:
            sfx_cursor_select.play()
            has_item = False
            val_sold_item = menu_cursor_pos
            val_sell = val_sold_item - 1
            for gear in player_gear_inv:
                if val_sell == player_gear_inv.index(gear):
                    target_gear = gear.name

            for gear in player_gear_inv:
                if target_gear == gear.name:
                    has_item = True
                    print("you sold " + gear.print_name + " for " + str(gear.value) + " gp.\n")
                    player1.gp += gear.value
                    player_gear_inv.remove(gear)
                    in_submenu4 = False
                    in_submenu_sell4 = False
                    break
            in_submenu4 = False
            in_submenu_sell4 = False
            in_menu_item = False
            in_menu_weapon = False
            in_menu_armor = False
            in_menu_helmet = False
            in_menu_shield = False
            in_menu_spell = False
            break

def func_use(gear,player_gear_inv):
    global menu_cursor_pos
    global in_submenu
    global in_submenu_use
    eaten_item = "0"
    for gear in player_gear_inv:
        if gear in all_game_items:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + str(gear.value) + " gp. " + " || " + str(gear.item_desc) + "... ")

    in_submenu = True
    in_submenu_use = True
    while in_submenu_use == True:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
                in_fight = False
                in_submenu = False
                in_submenu_use = False
                in_menu = False

        func_check_level()
        func_refresh_pygame(False)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            in_submenu = False
            in_submenu_use = False

        if keys[pygame.K_w]:
            if menu_cursor_pos <= 1:
                menu_cursor_pos == 1
            else:
                sfx_cursor_move.play()
                menu_cursor_pos -= 1
            if dev_mode >= 2:
                print(menu_cursor_pos)

        if keys[pygame.K_s]:
            if menu_cursor_pos >= 18:
                menu_cursor_pos == 18
            else:
                sfx_cursor_move.play()
                menu_cursor_pos += 1
            if dev_mode >= 2:
                print(menu_cursor_pos)


        if keys[pygame.K_e]:
            sfx_cursor_select.play()
            has_item = False
            val_used_item = menu_cursor_pos
            val_use = val_used_item - 1
            for gear in player_gear_inv:
                if val_use == player_gear_inv.index(gear):
                    eaten_item = gear.name

            for item in inventory:
                has_item = False
                can_use = False
                for item in inventory:
                    if eaten_item == item.name:
                        has_item = True
                        if item.edible == True:
                            if item.poisonous == False:
                                print("you consume " + item.print_name)
                                can_use = True
                                player1.hp = player1.hp + item.hp
                                if player1.hp > player1.maxhp:
                                    player1.hp = player1.maxhp
                            else:
                                print("\nyou consume " + item.print_name + " !\n")
                                can_use = True
                                player1.hp = player1.hp - item.hp
                                print("you feel sick...")

                                if player1.hp <= 0:
                                    print("\nYOU ARE DEAD \n")
                                    game_start = 0

                            if item.name == eaten_item and item.item_amount > 1:
                                has_item_multiple = True
                                item.item_amount -= 1
                            if has_item_multiple == False:
                                for item in inventory:
                                    if item.name == eaten_item:
                                        inventory.remove(item)
                            break
                        if can_use == False:
                            "you try to use " + item.print_name + ", but nothing interesting happens"

                break

            # if has_item == False:
            #     print("you don't have " + eaten_item)


            in_submenu = False
            in_submenu_use = False

def func_cast(gear,player_gear_inv):
    global menu_cursor_pos
    global in_submenu
    global in_submenu_cast
    cast_spell = "0"
    if dev_mode >= 2:
        for gear in player_gear_inv:
            if gear in all_game_spells:
                print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + str(gear.value) + " gp. ")

    in_submenu = True
    in_submenu_cast = True
    while in_submenu_cast == True:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
                in_fight = False
                in_submenu = False
                in_submenu_cast = False
                in_menu = False

        func_check_level()
        func_refresh_pygame(False)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            in_submenu = False
            in_submenu_cast = False

        if keys[pygame.K_w]:
            if menu_cursor_pos <= 1:
                menu_cursor_pos == 1
            else:
                sfx_cursor_move.play()
                menu_cursor_pos -= 1
            if dev_mode >= 2:
                print(menu_cursor_pos)

        if keys[pygame.K_s]:
            if menu_cursor_pos >= 18:
                menu_cursor_pos == 18
            else:
                sfx_cursor_move.play()
                menu_cursor_pos += 1
            if dev_mode >= 2:
                print(menu_cursor_pos)


        if keys[pygame.K_e]:
            sfx_cursor_select.play()
            has_item = False
            val_used_item = menu_cursor_pos
            val_use = val_used_item - 1
            for gear in player_gear_inv:
                if val_use == player_gear_inv.index(gear):
                    cast_spell = gear.name

            has_spell = 0
            for spell in equiped_spells:
                if spell.name == cast_spell:
                    has_spell = 1
                    if spell.effect == 100:
                        func_player_spell_non_combat(cast_spell)
                        break
                    else:
                        print("you have no use for that spell right now")
            if has_spell == 0:
                print("Invalid spell!")

            in_submenu = False
            in_submenu_cast = False

#############################----SCENE_FUNCTIONS----#########################

def func_tp(x,y,z):
    global steps_x
    global steps_y
    global steps_z

    steps_x = x
    steps_y = y
    steps_z = z

    if dev_mode >= 1:
        print("you teleported to: ",x,y,z)

def func_drop(gear,player_gear_inv):
    global in_menu_item
    global in_menu_weapon
    global in_menu_armor
    global in_menu_helmet
    global in_menu_shield
    global in_menu_spell
    global menu_cursor_pos
    global in_submenu2
    global in_submenu_drop2
    target_gear = "0"
    for gear in player_gear_inv:
        if gear in all_game_weapons:
            in_menu_weapon = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_armor:
            in_menu_armor = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_helmets:
            in_menu_helmet = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_shields:
            in_menu_shield = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_items:
            in_menu_item = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || x " + str(gear.item_amount) + " || " + str(gear.value * gear.item_amount) + " gp. " )
        if gear in all_game_spells:
            in_menu_spell = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + str(gear.value) + " gp. ")

    print("\nwhat do you want to drop\n")
    in_submenu2 = True
    in_submenu_drop2 = True
    while in_submenu_drop2 == True:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
                in_fight = False
                in_submenu2 = False
                in_submenu_drop2 = False
                in_menu = False

        func_check_level()
        func_refresh_pygame(False)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            in_submenu2 = False
            in_submenu_drop2 = False

        if keys[pygame.K_w]:
            if menu_cursor_pos <= 1:
                menu_cursor_pos == 1
            else:
                sfx_cursor_move.play()
                menu_cursor_pos -= 1
            if dev_mode >= 2:
                print(menu_cursor_pos)

        if keys[pygame.K_s]:
            if menu_cursor_pos >= 18:
                menu_cursor_pos == 18
            else:
                sfx_cursor_move.play()
                menu_cursor_pos += 1
            if dev_mode >= 2:
                print(menu_cursor_pos)


        if keys[pygame.K_e]:
            sfx_cursor_select.play()

            has_item = False
            has_item_multiple = False
            ground_has_item_multiple = False

            val_dropped_item = menu_cursor_pos
            val_drop = val_dropped_item - 1
            for gear in player_gear_inv:
                if val_drop == player_gear_inv.index(gear):
                    target_gear = gear.name

            for gear in player_gear_inv:
                if target_gear == gear.name:
                    has_item = True

                    if gear in all_game_items:
                        print("you drop " + gear.print_name + " x 1" + "\n")
                        for item in inventory:
                            if item.name == target_gear and item.item_amount > 1:
                                has_item_multiple = True
                                item.item_amount -= 1
                        if has_item_multiple == False:
                            for item in inventory:
                                if item.name == target_gear:
                                    inventory.remove(item)
                    else:
                        print("was not an item " + gear.print_name + "\n")
                        player_gear_inv.remove(gear)
                    break
            if has_item == True:
                for scene_type in location:
                    if gear in all_game_items:
                        end_drop = False
                        for ground_item in scene_type.scene_inventory:
                            if end_drop == False and ground_item.name == target_gear and ground_item.item_amount >= 1:
                                ground_has_item_multiple = True
                                ground_item.item_amount += 1
                                end_drop = True
                                break

                        if end_drop == False and ground_has_item_multiple == False:
                            for ground_item in all_ground_game_items:
                                if ground_item.name == target_gear:
                                    scene_type.scene_inventory.append(ground_item)
                            for ground_item in scene_type.scene_inventory:
                                if ground_item.name == target_gear:
                                    ground_item.item_amount = 1
                            end_drop = True

                    if gear in all_game_weapons:
                        pass # WEAPONS AND ARMOR WILL BE REMOVED FROM INVENTORY, BUT WILL NOT APPEAR ON THE GROUND
                    if gear in all_game_armor:
                        pass # WEAPONS AND ARMOR WILL BE REMOVED FROM INVENTORY, BUT WILL NOT APPEAR ON THE GROUND
                    if gear in all_game_helmets:
                        pass # WEAPONS AND ARMOR WILL BE REMOVED FROM INVENTORY, BUT WILL NOT APPEAR ON THE GROUND
                    if gear in all_game_shields:
                        pass # WEAPONS AND ARMOR WILL BE REMOVED FROM INVENTORY, BUT WILL NOT APPEAR ON THE GROUND
            in_submenu2 = False
            in_submenu_drop2 = False
            in_menu_item = False
            in_menu_weapon = False
            in_menu_armor = False
            in_menu_helmet = False
            in_menu_shield = False
            in_menu_spell = False
            break

def func_search_treasure():
            scene_difficulty = 0
            for scene_type in location:
                scene_difficulty = scene_type.difficulty

            loot_spawn_chance_item = 0
            loot_chance_item = 0
            loot_amount_item = 0
            loot_spawn_chance_weapon = 0
            loot_chance_weapon = 0
            loot_amount_weapon = 0

            loot_spawn_chance_armor = 0
            loot_chance_armor = 0
            loot_amount_armor = 0

            loot_spawn_chance_helmet = 0
            loot_chance_helmet = 0
            loot_amount_helmet = 0

            loot_spawn_chance_shield = 0
            loot_chance_shield = 0
            loot_amount_shield = 0

            loot_spawn_chance_gp = 0
            loot_amount_gp = 0

            loot_quality = 0

            loot_spawn_chance_item = random.randint(0,1)
            loot_spawn_chance_weapon = random.randint(0,1)
            loot_spawn_chance_armor = random.randint(0,1)
            loot_spawn_chance_helmet = random.randint(0,1)
            loot_spawn_chance_shield = random.randint(0,1)
            loot_spawn_chance_gp = random.randint(0,1)

            noloot = True

            if loot_spawn_chance_item != 1 and loot_spawn_chance_armor != 1 and loot_spawn_chance_helmet != 1 and loot_spawn_chance_shield != 1 and loot_spawn_chance_weapon != 1:
                noloot = True
            else:
                noloot = False

            if loot_spawn_chance_gp == 1 or noloot == True:
                loot_amount_gp = random.randint(1,100) * random.randint(1,10)
                player1.gp = player1.gp + loot_amount_gp
                print(loot_amount_gp)
                print("gold obtained \n")

            if loot_spawn_chance_item == 1:
                if len(items_drop_table) != 0:
                    for item in items_drop_table:
                        loot_chance_item = random.randint(0,1)
                        if loot_chance_item == 1:
                            for ground_item in all_ground_game_items:
                                if ground_item.name == item.name:
                                    scene_type.scene_inventory.append(ground_item)
                                    print("you found " + item.print_name + " \n")
                            loot_amount_item = random.randint(0,1)
                            if loot_amount_item == 1:
                                break

            if loot_spawn_chance_weapon == 1:
                if len(weapons_drop_table) != 0:
                    for weapon in weapons_drop_table:
                        loot_chance_weapon = random.randint(0,1)
                        if loot_chance_weapon == 1:
                            for ground_weapon in all_ground_game_weapons:
                                if ground_weapon.name == weapon.name:
                                    scene_type.scene_weapon_inventory.append(ground_weapon)
                                    print("you found " + weapon.print_name + " \n" )
                            loot_amount_weapon = random.randint(0,1)
                            if loot_amount_weapon == 1:
                                break


            if loot_spawn_chance_armor == 1:
                if len(armor_drop_table) != 0:
                    for armor in armor_drop_table:
                        loot_chance_armor = random.randint(0,1)
                        if loot_chance_armor == 1:
                            for ground_armor in all_ground_game_armor:
                                if ground_armor.name == armor.name:
                                    scene_type.scene_armor_inventory.append(ground_armor)
                                    print("you found " + armor.print_name + " \n" )
                            loot_amount_armor = random.randint(0,1)
                            if loot_amount_armor == 1:
                                break


            if loot_spawn_chance_helmet == 1:
                if len(helmets_drop_table) != 0:
                    for helmet in helmets_drop_table:
                        loot_chance_helmet = random.randint(0,1)
                        if loot_chance_helmet == 1:
                            for ground_helmet in all_ground_game_helmets:
                                if ground_helmet.name == helmet.name:
                                    scene_type.scene_helmet_inventory.append(ground_helmet)
                                    print("you found " + helmet.print_name + " \n" )
                            loot_amount_helmet = random.randint(0,1)
                            if loot_amount_helmet == 1:
                                break


            if loot_spawn_chance_shield == 1:
                if len(shields_drop_table) != 0:
                    for shield in shields_drop_table:
                        loot_chance_shield = random.randint(0,1)
                        if loot_chance_shield == 1:
                            for ground_shield in all_ground_game_shields:
                                if ground_shield.name == shield.name:
                                    scene_type.scene_shield_inventory.append(ground_shield)
                                    print("you found " + shield.print_name + " \n" )
                            loot_amount_shield = random.randint(0,1)
                            if loot_amount_shield == 1:
                                break
            if noloot == True:
                print("\nthere was no equipment here, but at least I found some gold...")
            func_check_level()

def func_rain():
    global raining
    raining += random.randint(-1,1)
    if raining < 0:
        raining = 0
    if raining >= 10:
        raining = 1

def func_check_weather():
    for scene_type in location:
        if season == 0:
            scene_type.temp = (Fore.YELLOW + "hot" + Style.RESET_ALL)
        if season == 1:
            scene_type.temp = (Fore.CYAN + Style.DIM + "chilly" + Style.RESET_ALL)
        if season == 2:
            scene_type.temp = (Fore.CYAN + "very cold" + Style.RESET_ALL)
        if season == 3:
            scene_type.temp = (Fore.GREEN + "temperate" + Style.RESET_ALL)

def func_check_season():
    if months >= 4:
        season = 0
    if months >= 1 and months <= 3:
        season = 0
    if months >= 4 and months <= 6:
        season = 1
    if months >= 7 and months <= 9:
        season = 2
    if months >= 9 and months <= 12:
        season = 3

def func_check_light():
    has_torch = False
    for scene_type in location:
        if steps_z <= -1:
            for item in inventory:
                if item.name == "torch":
                    has_torch = True
                    scene_type.light = (Fore.YELLOW + Style.DIM + " and very dark, but slightly illuminated by your torch" + Style.RESET_ALL)
                else:
                    scene_type.light = (Fore.BLACK + Style.BRIGHT + " and very dark" + Style.RESET_ALL)

        else:
            is_night = False
            if time >= 12:
                is_night = True
            if is_night == True:
                for item in inventory:
                    if item.name == "torch":
                        has_torch = True
                if has_torch == True:
                    if raining == 1 and steps_z >= 0:
                        scene_type.light = (Fore.BLACK + Style.BRIGHT + ", very dark and lightly raining, your torch illuminates the area" + Style.RESET_ALL)
                    if raining >= 2 and steps_z >= 0:
                        scene_type.light = (Fore.BLACK + Style.BRIGHT + ", very dark and raining heavily, your torch illuminates the area" + Style.RESET_ALL)
                    if raining == 0 and steps_z >= 0:
                        scene_type.light = (Fore.YELLOW + Style.DIM + " and very dark, but slightly illuminated by your torch" + Style.RESET_ALL)
                else:
                    if raining == 1 and steps_z >= 0:
                        scene_type.light = (Fore.BLUE + Style.DIM + ", very dark and lightly raining" + Style.RESET_ALL)
                    if raining >= 2 and steps_z >= 0:
                        scene_type.light = (Fore.BLUE + Style.DIM + ", very dark and raining heavily" + Style.RESET_ALL)
                    if raining == 0 and steps_z >= 0:
                        scene_type.light = (Fore.BLACK + Style.BRIGHT + " and very dark" + Style.RESET_ALL)
            if is_night == False and season == 3:
                if raining == 1 and steps_z >= 0:
                    scene_type.light = (Fore.CYAN + Style.DIM + " and lightly raining" + Style.RESET_ALL)
                if raining >= 2 and steps_z >= 0:
                    scene_type.light = (Fore.BLUE + Style.NORMAL + " and raining heavily" + Style.RESET_ALL)
                if raining == 0 and steps_z >= 0:
                    scene_type.light = (Fore.CYAN + Style.DIM + " and very overcast" + Style.RESET_ALL)
            if is_night == False and season != 3:
                if raining == 1 and steps_z >= 0:
                    scene_type.light = (Fore.CYAN + Style.NORMAL + " and lightly raining" + Style.RESET_ALL)
                if raining >= 2 and steps_z >= 0:
                    scene_type.light = (Fore.BLUE + Style.NORMAL + " and raining heavily" + Style.RESET_ALL)
                if raining == 0 and steps_z >= 0:
                    scene_type.light = (Fore.YELLOW + Style.BRIGHT + " and very sunny" + Style.RESET_ALL)

###########################---PLAYER STATS/SKILLS/INVENTORY----############################

def func_cook():
    target_gear = "0"
    ingredient = "0"

    for item in inventory:
        print("|| " + str((inventory.index(item)+1)) + " || " + item.print_name + " || " + str(item.value) + " gp. ")

    dropped_item = input("\nwhat do you want to cook with?\n")
    has_item = False
    if dropped_item.isdigit():
        val_dropped_item = int(dropped_item)
        val_drop = val_dropped_item - 1
        for item in inventory:
            if val_drop == inventory.index(item):
                target_gear = item.name
    else:
        for item in inventory:
            if item.name == dropped_item:
                target_gear = item.name

    for item in inventory:
        if target_gear == item.name:
            has_item = True
            print("you selected " + item.print_name + "\n")
            ingredient = target_gear
            break
    return ingredient

def func_create_item(ing1_name,ing2_name,ingreq_1,ingreq_2,skill_lvl_req,made_item):
    global recipe_found
    if ing1_name == ingreq_1.name and ing2_name == ingreq_2.name:
        recipe_found == True
        if player1_skills.cooking >= skill_lvl_req:
            has_cooked = True
            for item in all_game_items:
                if item.name == made_item.name:
                    inventory.append(item)
                    print("you made " + item.name)
                    for item in inventory:
                        if item.name == ing1_name:
                            inventory.remove(item)
                    for item in inventory:
                        if item.name == ing2_name:
                            inventory.remove(item)
        else:
            print("your cooking level is not high enough to make that!")
            has_cooked = False

    elif ing2_name == ingreq_1.name and ing1_name == ingreq_2.name:
        recipe_found == True
        if player1_skills.cooking >= skill_lvl_req:
            has_cooked = True
            for item in all_game_items:
                if item.name == made_item.name:
                    inventory.append(item)
                    print("you made " + item.name)
                    for item in inventory:
                        if item.name == ing1_name:
                            inventory.remove(item)
                    for item in inventory:
                        if item.name == ing2_name:
                            inventory.remove(item)
        else:
            print("your cooking level is not high enough to make that!")
            has_cooked = False


    else:
        has_cooked = False

def func_equip(gear,player_gear_inv,current_gear):
    global menu_cursor_pos
    global in_submenu2
    global in_submenu
    global in_submenu_equip
    global in_submenu_equip2
    global in_menu_item
    global in_menu_weapon
    global in_menu_armor
    global in_menu_helmet
    global in_menu_shield
    global in_menu_spell
    target_gear = "0"
    has_level = False
    has_space = False

    for gear in player_gear_inv: #def. list to print in gui
        if gear in all_game_weapons:
            in_menu_weapon = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_armor:
            in_menu_armor = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_helmets:
            in_menu_helmet = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_shields:
            in_menu_shield = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_spells:
            in_menu_spell = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")

    print("\nwhat do you want to equip\n")

    in_submenu2 = True
    in_submenu_equip2 = True

    while in_submenu_equip2 == True:

        pygame.time.delay(100)

        keys = pygame.key.get_pressed()

        func_check_level()
        func_refresh_pygame(False)

        if keys[pygame.K_w]:
            if menu_cursor_pos <= 1:
                menu_cursor_pos == 1
            else:
                sfx_cursor_move.play()
                menu_cursor_pos -= 1
            if dev_mode >= 2:
                print(menu_cursor_pos)

        if keys[pygame.K_s]:
            if menu_cursor_pos >= 18:
                menu_cursor_pos == 18
            else:
                sfx_cursor_move.play()
                menu_cursor_pos += 1
            if dev_mode >= 2:
                print(menu_cursor_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
                in_fight = False
                in_menu_item = False
                in_menu_weapon = False
                in_menu_armor = False
                in_menu_helmet = False
                in_menu_shield = False
                in_menu_spell = False
                in_submenu2 = False
                in_submenu_equip2 == False
                in_submenu = False
                in_submenu_equip == False
                in_menu = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    in_menu_item = False
                    in_menu_weapon = False
                    in_menu_armor = False
                    in_menu_helmet = False
                    in_menu_shield = False
                    in_menu_spell = False
                    in_submenu_equip2 = False
                    in_submenu2 = False
                    print("equip2 menu quit")
                    break

                if event.key == pygame.K_e:
                    sfx_cursor_select.play()

                    has_gear = False

                    val_dropped_item = menu_cursor_pos
                    val_drop = val_dropped_item - 1
                    for gear in player_gear_inv:
                        if val_drop == player_gear_inv.index(gear):
                            target_gear = gear.name

                    for gear in player_gear_inv:
                        if player_gear_inv.index(gear) == (menu_cursor_pos - 1):
                            has_gear = True #player has the selected gear in their inv

                            if player1.level < gear.level:
                                print("You are not high enough level to equip " + gear.print_name + " ...")
                                has_level = False
                            else:
                                has_level = True

                            if gear in equiped_spells:
                                has_space = False
                            else:
                                has_space = True

                            if has_level == True and has_space == True:
                                if gear in all_game_weapons:
                                    gear.weapon_amount -= 1
                                    if gear.weapon_amount == 0:
                                        weapon_inventory.remove(gear)
                                if gear in all_game_armor:
                                    gear.armor_amount -= 1
                                    if gear.armor_amount == 0:
                                        armor_inventory.remove(gear)
                                if gear in all_game_helmets:
                                    gear.helmet_amount -= 1
                                    if gear.helmet_amount == 0:
                                        helmet_inventory.remove(gear)
                                if gear in all_game_shields:
                                    gear.shield_amount -= 1
                                    if gear.shield_amount == 0:
                                        shield_inventory.remove(gear)
                                if gear in all_game_spells:
                                    spell_inventory.remove(gear)

                                if gear in all_game_weapons:
                                    del equiped_weapon[:]
                                if gear in all_game_armor:
                                    del equiped_armor[:]
                                if gear in all_game_helmets:
                                    del equiped_helmet[:]
                                if gear in all_game_shields:
                                    del equiped_shield[:]

                                if gear in all_game_weapons:
                                    equiped_weapon.append(gear)
                                if gear in all_game_armor:
                                    equiped_armor.append(gear)
                                if gear in all_game_helmets:
                                    equiped_helmet.append(gear)
                                if gear in all_game_shields:
                                    equiped_shield.append(gear)
                                if gear in all_game_spells:
                                    equiped_spells.append(gear)

                                print(gear.name + " equipped!")

                                if current_gear != "0":
                                    if gear in all_game_weapons:
                                        for weapon in all_game_weapons:
                                            if weapon.name == current_gear:
                                                if weapon not in weapon_inventory:
                                                    weapon_inventory.append(weapon)
                                                else:
                                                    for weapon in weapon_inventory:
                                                        if weapon.name == current_gear:
                                                            weapon.weapon_amount += 1
                                                break

                                    if gear in all_game_armor:
                                        for armor in all_game_armor:
                                            if armor.name == current_gear:
                                                if armor not in armor_inventory:
                                                    armor_inventory.append(armor)
                                                else:
                                                    for armor in armor_inventory:
                                                        if armor.name == current_gear:
                                                            armor.armor_amount += 1
                                                break

                                    if gear in all_game_helmets:
                                        for helmet in all_game_helmets:
                                            if helmet.name == current_gear:
                                                if helmet not in helmet_inventory:
                                                    helmet_inventory.append(helmet)
                                                else:
                                                    for helmet in helmet_inventory:
                                                        if helmet.name == current_gear:
                                                            helmet.helmet_amount += 1
                                                break

                                    if gear in all_game_shields:
                                        for shield in all_game_shields:
                                            if shield.name == current_gear:
                                                if shield not in shield_inventory:
                                                    shield_inventory.append(shield)
                                                else:
                                                    for shield in shield_inventory:
                                                        if shield.name == current_gear:
                                                            shield.shield_amount += 1
                                                break


                                current_gear = gear.name

                            if has_level == True and has_space == False:
                                print("\nYou already have this spell in your spellbook!\n")
                            if has_level == False and has_space == False:
                                # print("\nYou are not high enough level to equip this!\n")
                                pass
                            if has_level == False and has_space == True:
                                # print("\nYou are not high enough level to equip this!\n")
                                pass
                            break

def func_inv(gear,player_gear_inv):
    target_gear = "0"
    for gear in player_gear_inv:
        if gear in all_game_weapons:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_armor:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_helmets:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")
        if gear in all_game_shields:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || " + str(gear.value) + " gp. ")

        if gear in all_game_spells:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + str(gear.value) + " gp. ")

        if gear in all_game_items:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + str(gear.value) + " gp. ")

def func_check_stat_bonus():
    for player_stats in players:

        weapon_magic_bonus = 0
        weapon_strength_bonus = 0
        weapon_attack_bonus = 0
        weapon_defence_bonus = 0
        weapon_maxhp_bonus = 0

        armor_magic_bonus = 0
        armor_strength_bonus = 0
        armor_attack_bonus = 0
        armor_defence_bonus = 0
        armor_maxhp_bonus = 0

        helmet_magic_bonus = 0
        helmet_strength_bonus = 0
        helmet_attack_bonus = 0
        helmet_defence_bonus = 0
        helmet_maxhp_bonus = 0

        shield_magic_bonus = 0
        shield_strength_bonus = 0
        shield_attack_bonus = 0
        shield_defence_bonus = 0
        shield_maxhp_bonus = 0

        for weapon in equiped_weapon:
            weapon_magic_bonus = weapon.magic_bonus
            weapon_strength_bonus = weapon.strength_bonus
            weapon_attack_bonus = weapon.attack_bonus
            weapon_defence_bonus = weapon.defence_bonus
            weapon_maxhp_bonus = weapon.maxhp_bonus

        for armor in equiped_armor:
            armor_magic_bonus = armor.magic_bonus
            armor_strength_bonus = armor.strength_bonus
            armor_attack_bonus = armor.attack_bonus
            armor_defence_bonus = armor.defence_bonus
            armor_maxhp_bonus = armor.maxhp_bonus

        for helmet in equiped_helmet:
            helmet_magic_bonus = helmet.magic_bonus
            helmet_strength_bonus = helmet.strength_bonus
            helmet_attack_bonus = helmet.attack_bonus
            helmet_defence_bonus = helmet.defence_bonus
            helmet_maxhp_bonus = helmet.maxhp_bonus

        for shield in equiped_shield:
            shield_magic_bonus = shield.magic_bonus
            shield_strength_bonus = shield.strength_bonus
            shield_attack_bonus = shield.attack_bonus
            shield_defence_bonus = shield.defence_bonus
            shield_maxhp_bonus = shield.maxhp_bonus

        total_magic_bonus = weapon_magic_bonus + armor_magic_bonus + helmet_magic_bonus + shield_magic_bonus
        total_strength_bonus = weapon_strength_bonus + armor_strength_bonus + helmet_strength_bonus + shield_strength_bonus
        total_attack_bonus = weapon_attack_bonus + armor_attack_bonus + helmet_attack_bonus + shield_attack_bonus
        total_defence_bonus = weapon_defence_bonus + armor_defence_bonus + helmet_defence_bonus + shield_defence_bonus
        total_maxhp_bonus = weapon_maxhp_bonus + armor_maxhp_bonus + helmet_maxhp_bonus + shield_maxhp_bonus

        player_stats.magic_bonus = total_magic_bonus
        player_stats.strength_bonus = total_strength_bonus
        player_stats.attack_bonus = total_attack_bonus
        player_stats.defence_bonus = total_defence_bonus
        player_stats.maxhp_bonus = total_maxhp_bonus

def func_check_level():
    sleep(sleep_time_fast)
    for player_stats in players:
        if player_stats.magic_xp >= (player_stats.magic ** 4):
            player_stats.magic += 1
            print("\nyour magic level is now: ", player_stats.magic)
            func_check_level()

        if player_stats.strength_xp >= (player_stats.strength ** 4):
            player_stats.strength += 1
            print("\nyour strength level is now: ", player_stats.strength)
            func_check_level()

        if player_stats.attack_xp >= (player_stats.attack ** 4):
            player_stats.attack += 1
            print("\nyour attack level is now: ", player_stats.attack)
            func_check_level()

        if player_stats.defence_xp >= (player_stats.defence ** 4):
            player_stats.defence += 1
            print("\nyour defence level is now: ", player_stats.defence)
            func_check_level()

        if player_stats.xp >= (player_stats.level ** 2):
            player_stats.level += 1
            print("\nLEVELED UP \nyou are now level: ", player_stats.level)
            func_check_level()

        player_stats.nobonus_maxhp = (player_stats.level * 100) + (player_stats.defence * 25) + (player_stats.strength * 10) + (player_stats.attack * 10) + (player_stats.magic * 10)

        player_stats.nobonus_maxmp = (player_stats.level * 72) + (player_stats.magic * 125)

        player_stats.maxhp = (player_stats.nobonus_maxhp + player_stats.maxhp_bonus)

        player_stats.maxmp = (player_stats.nobonus_maxmp + player_stats.maxmp_bonus)

def func_HUD():
    status_list = []
    for status_condition in player1.status_effect_list:
        status_list.append(status_condition.name)
    print("\nName: " + Fore.YELLOW + Style.BRIGHT + player1.name)
    print("LVL: " + Fore.YELLOW + str(player1.level))
    for armor in equiped_armor:
        print("ATT.: " + armor.print_attribute)
    print("HP:" + Fore.RED + str(player1.hp) + Style.RESET_ALL + "/" + Fore.RED + str(player1.maxhp) + Style.RESET_ALL)
    print("MP:" + Fore.BLUE + Style.BRIGHT + str(player1.mp) + Style.RESET_ALL + "/" + Fore.BLUE + Style.BRIGHT  + str(player1.maxmp) + Style.RESET_ALL)
    if len(player1.status_effect_list) != 0:
        print("Status: " + str(status_list) + " \n")
    else:
        print("Status: ['N0NE'] \n")

def player_keys_check():
    if len(inventory) == 0: #locks all doors if inventory is empty, tile which are passable by default would be unlocked if the player never picks up an item
        large_tree_cave_door.passable = False
        dismurth_bridge.passable = False
    else:
        for item in inventory:
            if item.name == "oak key":
                large_tree_cave_door.passable = True
                break
            else:
                for item.name in large_tree_cave_door.scene_inventory:
                    if item.name == "oak key":
                        large_tree_cave_door.passable = True
                else:
                    large_tree_cave_door.passable = False

        for item in inventory:
            if item.name == "certificate of passage":
                dismurth_bridge.passable = True
                break
            else:
                for item.name in dismurth_bridge.scene_inventory:
                    if item.name == "certificate of passage":
                        dismurth_bridge.passable = True
                else:
                    dismurth_bridge.passable = False

def func_choose_input_option():
    target_input_option = "0"
    selected_input_option = "0"
    for input_option in input_option_list:
        if input_option.print_in_main == True:
            print("|| " + str((input_option_list.index(input_option)+1)) + " || " + input_option.name )

    input_option_input = input("\nwhat do you want to do?\n")
    has_option = False
    if input_option_input.isdigit():
        val_input_option_input = int(input_option_input)
        val_input_input = val_input_option_input - 1
        for input_option in input_option_list:
            if val_input_input == input_option_list.index(input_option):
                target_input_option = input_option.name
    else:
        for input_option in input_option_list:
            if input_option.name == input_option_input or input_option.hotkey == input_option_input:
                target_input_option = input_option.name

    for input_option in input_option_list:
        if target_input_option == input_option.name:
            has_option = True
            print("you selected " + input_option.name + "\n")
            selected_input_option = target_input_option
            break
    return selected_input_option

#######################---PLAYER LOCATION---#######################

def player_position_check():
    location_found = False
    for scene_type in all_scene_types:
        if steps_y == scene_type.ypos and steps_x == scene_type.xpos and steps_z == scene_type.zpos:
            location_found = True
            del location[:]
            location.append(scene_type)
            break
    if location_found == False:
        if steps_z == 0:
            del location[:]
            location.append(ocean)
        if steps_z <= -1:
            del location[:]
            location.append(solid_cave_wall)

def player_north_check():
    location_found = False
    for scene_type in all_scene_types:
        if steps_y-1 == scene_type.ypos and steps_x == scene_type.xpos and steps_z == scene_type.zpos:
            location_found = True
            del location_north[:]
            location_north.append(scene_type)
            break
    if location_found == False:
        if steps_z == 0:
            del location_north[:]
            location_north.append(ocean)
        if steps_z <= -1 and steps_z >= -3:
            del location_north[:]
            location_north.append(solid_cave_wall)
        if steps_z <= -4 and steps_z >= -6:
            del location_north[:]
            location_north.append(solid_dungeon_wall)
        if steps_z <= -7 and steps_z >= -9:
            del location_north[:]
            location_north.append(solid_dungeon_wall)
        if steps_z <= -10 and steps_z >= -12:
            del location_north[:]
            location_north.append(solid_dungeon_wall)
        if steps_z >= 1:
            del location_north[:]
            location_north.append(sky)

def player_south_check():
    location_found = False
    for scene_type in all_scene_types:
        if steps_y+1 == scene_type.ypos and steps_x == scene_type.xpos and steps_z == scene_type.zpos:
            location_found = True
            del location_south[:]
            location_south.append(scene_type)
            break
    if location_found == False:
        if steps_z == 0:
            del location_south[:]
            location_south.append(ocean)
        if steps_z <= -1 and steps_z >= -3:
            del location_south[:]
            location_south.append(solid_cave_wall)
        if steps_z <= -4 and steps_z >= -6:
            del location_south[:]
            location_south.append(solid_dungeon_wall)
        if steps_z <= -7 and steps_z >= -9:
            del location_south[:]
            location_south.append(solid_dungeon_wall)
        if steps_z <= -10 and steps_z >= -12:
            del location_south[:]
            location_south.append(solid_dungeon_wall)
        if steps_z >= 1:
            del location_south[:]
            location_south.append(sky)

def player_east_check():
    location_found = False
    for scene_type in all_scene_types:
        if steps_y == scene_type.ypos and steps_x+1 == scene_type.xpos and steps_z == scene_type.zpos:
            location_found = True
            del location_east[:]
            location_east.append(scene_type)
            break

    if location_found == False:
        if steps_z == 0:
            del location_east[:]
            location_east.append(ocean)
        if steps_z <= -1 and steps_z >= -3:
            del location_east[:]
            location_east.append(solid_cave_wall)
        if steps_z <= -4 and steps_z >= -6:
            del location_east[:]
            location_east.append(solid_dungeon_wall)
        if steps_z <= -7 and steps_z >= -9:
            del location_east[:]
            location_east.append(solid_dungeon_wall)
        if steps_z <= -10 and steps_z >= -12:
            del location_east[:]
            location_east.append(solid_dungeon_wall)
        if steps_z >= 1:
            del location_east[:]
            location_east.append(sky)

def player_west_check():
    location_found = False
    for scene_type in all_scene_types:
        if steps_y == scene_type.ypos and steps_x-1 == scene_type.xpos and steps_z == scene_type.zpos:
            location_found = True
            del location_west[:]
            location_west.append(scene_type)
            break
    if location_found == False:
        if steps_z == 0:
            del location_west[:]
            location_west.append(ocean)
        if steps_z <= -1 and steps_z >= -3:
            del location_west[:]
            location_west.append(solid_cave_wall)
        if steps_z <= -4 and steps_z >= -6:
            del location_west[:]
            location_west.append(solid_dungeon_wall)
        if steps_z <= -7 and steps_z >= -9:
            del location_west[:]
            location_west.append(solid_dungeon_wall)
        if steps_z <= -10 and steps_z >= -12:
            del location_west[:]
            location_west.append(solid_dungeon_wall)
        if steps_z >= 1:
            del location_west[:]
            location_west.append(sky)

def player_down_check():
    location_found = False
    for scene_type in all_scene_types:
        if steps_y == scene_type.ypos and steps_x == scene_type.xpos and steps_z-1 == scene_type.zpos:
            location_found = True
            del location_down[:]
            location_down.append(scene_type)
            break
    if location_found == False:
        if steps_z == 0:
            del location_down[:]
            location_down.append(ground)
        if steps_z <= -1 and steps_z >= -3:
            del location_down[:]
            location_down.append(solid_cave_ground)
        if steps_z <= -4 and steps_z >= -6:
            del location_down[:]
            location_down.append(solid_dungeon_ground)
        if steps_z <= -7 and steps_z >= -9:
            del location_down[:]
            location_down.append(solid_dungeon_ground)
        if steps_z <= -10 and steps_z >= -12:
            del location_down[:]
            location_down.append(solid_dungeon_ground)
        if steps_z >= 1:
            del location_down[:]
            location_up.append(sky)

def player_up_check():
    location_found = False
    for scene_type in all_scene_types:
        if steps_y == scene_type.ypos and steps_x == scene_type.xpos and steps_z+1 == scene_type.zpos:
            location_found = True
            del location_up[:]
            location_up.append(scene_type)
            break
    if location_found == False:
        if steps_z <= -1 and steps_z >= -3:
            del location_up[:]
            location_up.append(solid_cave_ground)
        if steps_z <= -4 and steps_z >= -6:
            del location_up[:]
            location_up.append(solid_dungeon_ground)
        if steps_z <= -7 and steps_z >= -9:
            del location_up[:]
            location_up.append(solid_dungeon_ground)
        if steps_z <= -10 and steps_z >= -12:
            del location_up[:]
            location_up.append(solid_dungeon_ground)


        if steps_z == 0:
            del location_up[:]
            location_up.append(sky)
        if steps_z >= 1:
            del location_up[:]
            location_up.append(sky)

def location_desc():
    player_position_check()
    player_north_check()
    player_south_check()
    player_east_check()
    player_west_check()
    player_down_check()
    player_up_check()
    func_check_season()
    func_check_weather()
    func_check_light()
    if dev_mode >= 1:
        print("\n///   DEV MODE " + str(dev_mode) +"!  ///\n")
        if dev_mode >= 2:
            # for player_stats in players:
            #     print("status effect: ", player_stats.status_effect)
            print("\ninv:")
            for item in inventory:
                print(item.print_name)
            for spell in spell_inventory:
                print(spell.print_name)
            for armor in armor_inventory:
                print(armor.print_name)
            for weapon in weapon_inventory:
                print(weapon.print_name)
            for helmet in helmet_inventory:
                print(helmet.print_name)
            for shield in shield_inventory:
                print(shield.print_name)
            print("")

            print("restock_ticks " + str(restock_ticks))

            if dev_mode >= 3:
                for scene_type in location:
                    print("scene temp desc. string: ", scene_type.temp)
                    print("scene light desc. string: ", scene_type.light)
                    print("scene_biome: ", scene_type.biome)
                    print("scene_encounter_difficulty: ", scene_type.difficulty)
                    print("can_fish: ", scene_type.can_fish)
                    print("scene_treasure: ", scene_type.treasure)
                print("in_fight: ", in_fight)
                print("x: ", steps_x)
                print("y: ", steps_y)
                print("z: ", steps_z)
                print("last x: ", prev_x)
                print("last y: ", prev_y)
                print("last z: ", prev_z)
                print("time", time)
                print("season", season)
                print("rain status", raining)
                print("date: ", days, months, years)

                if dev_mode >= 4:
                    for scene_type in all_scene_types:
                        print(scene_type.name, scene_type.xpos, scene_type.ypos, scene_type.zpos)

    for scene_type in location:
        scene_npc_count = 0
        scene_animal_count = 0
        print(Fore.YELLOW + Style.BRIGHT + "\n///////////// ///////////// ////////////\n")
        print("you are in " + scene_type.name + "\n")
        sleep(sleep_time_fast)
        print("it is " + scene_type.temp + "" + scene_type.light + ".\n")
        sleep(sleep_time_fast)
        print("\"" + scene_type.flavour + "\" \n")
        sleep(sleep_time_fast)

        if scene_type.indoors == True:
            if scene_type.can_fish == True:
                print("looks like I can somehow fish in here ...")
            if scene_type.can_craft == True:
                print("there is a worksbench in here ...")
            if scene_type.can_cook == True:
                print("there is a cooking range here, it is nice and hot...")
            if scene_type.can_steal == True:
                print("I could steal from here...")
            if len(scene_type.npc_list) >= 1:
                if len(scene_type.npc_list) == 1:
                    print("\nthere is someone in here. \n")
            if len(scene_type.npc_list) > 1:
                print("\nthere are " + str(len(scene_type.npc_list)) + " people in here. \n")
        else:
            if scene_type.can_fish == True:
                print("looks like I can fish off here ...")
            if scene_type.can_craft == True:
                print("there is a workbench out here ...")
            if scene_type.can_cook == True:
                print("there is a fire here, it is nice and hot...")
            if scene_type.can_steal == True:
                print("I could steal from here...")

        if len(scene_type.npc_list) >= 1:
            for npc in scene_type.npc_list:
                if npc.is_animal == True:
                    scene_animal_count += 1
                if npc.is_animal == False:
                    scene_npc_count += 1

        if scene_npc_count == 1:
            print("\nthere is someone here. \n")
            sleep(sleep_time_fast)
        if scene_npc_count > 1:
            print("\nthere are " + str(scene_npc_count) + " people here. \n")
            sleep(sleep_time_fast)
        if scene_animal_count == 1:
            print("\nthere is a creature here. \n")
            sleep(sleep_time_fast)
        if scene_animal_count > 1:
            print("\nthere are " + str(scene_animal_count) + " creatures here. \n")
            sleep(sleep_time_fast)

        scene_npc_count = 0
        scene_animal_count = 0

        if scene_type.treasure == True:
            print("\nthere is treasure here. \n")
            sleep(sleep_time_fast)
        if  len(scene_type.scene_inventory) != 0 or len(scene_type.scene_weapon_inventory) != 0 or len(scene_type.scene_armor_inventory) != 0 or len(scene_type.scene_helmet_inventory) != 0 or len(scene_type.scene_shield_inventory) != 0:
            print("on the ground is:")
            sleep(sleep_time_fast)
        else:
            print("there is nothing on the ground.")
            sleep(sleep_time_fast)

        for ground_item in scene_type.scene_inventory:
            print(ground_item.print_name + " x " + str(ground_item.item_amount))
            sleep(sleep_time_fast)
        for ground_weapon in scene_type.scene_weapon_inventory:
            print(ground_weapon.print_name)
            sleep(sleep_time_fast)
        for ground_armor in scene_type.scene_armor_inventory:
            print(ground_armor.print_name)
            sleep(sleep_time_fast)
        for ground_helmet in scene_type.scene_helmet_inventory:
            print(ground_helmet.print_name)
            sleep(sleep_time_fast)
        for ground_shield in scene_type.scene_shield_inventory:
            print(ground_shield.print_name)
            sleep(sleep_time_fast)


        if scene_type.safe == False:
            print("\nit is dangerous here... \n")

    func_rain()

    for scene_type in location_north:
        print("\nto your north is " + scene_type.name + "")
        sleep(sleep_time_fast)
    for scene_type in location_south:
        print("to your south is " + scene_type.name + "")
        sleep(sleep_time_fast)
    for scene_type in location_east:
        print("to your east is " + scene_type.name + "")
        sleep(sleep_time_fast)
    for scene_type in location_west:
        print("to your west is " + scene_type.name + "")
        sleep(sleep_time_fast)
    for scene_type in location_down:
        print("below you is " + scene_type.name + "")
        sleep(sleep_time_fast)
    for scene_type in location_up:
        print("above you is " + scene_type.name + "")
        sleep(sleep_time_fast)

##########--pre game stat calcutions--#########

for player_stats in players:
    player_stats.level = 1
    player_stats.xp = 100
    player_stats.strength = 1
    player_stats.attack = 1
    player_stats.magic = 1
    player_stats.strength_xp = 100
    player_stats.attack_xp = 100
    player_stats.magic_xp = 100

func_check_stat_bonus()
func_check_level()
player_keys_check()

player1.hp = player1.maxhp # has to be last as max hp is calculated from all other stats
player1.mp = player1.maxmp

if dev_mode >= 1:
    player1.gp = 10000

########## GAME START #########
game_start = 1



print(Fore.RED + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to the land of Tonbale! \n")

print("\nversion: " + version + " \n")

print("\n  Controls:\n  W,A,S,D: Move \n  SPACE: Menu\n  E: Select \n  Q: Back")

print("\npress the D key to start! \n")
# if dev_mode == 0:
#     name = input("Please enter your name: \n")
#     for player_stats in players:
#         player_stats.name = name

while game_start == 1:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_start = 0

    func_shop_restock()
    player_keys_check()
    func_check_stat_bonus()
    func_check_level()
    player_position_check()

    func_refresh_pygame(False)

    keys = pygame.key.get_pressed()

    if has_moved == True or in_fight == True:
        if npc_fight == False and check_for_combat == True:
            for scene_type in location:
                if scene_type.safe == False:
                    if in_fight == False:
                        if time >= 12:
                            combat_chance = random.randint(0,50)
                        if time < 12:
                            combat_chance = random.randint(0,100)
                        if combat_chance > 5:
                            in_fight = False
                        if combat_chance <= 5:
                            in_fight = True
        if in_fight == True: #init combat
            if npc_fight == False:
                if dev_mode >= 1:
                    print("choosing enemies")
                func_choose_enemy()
                if dev_mode >= 1:
                    print("enemies chosen")

            for enemy_stats in current_enemies: #build drop tables
                if dev_mode >= 1:
                    print("building drop tables")

                for item in enemy_stats.drop_table_items:
                    enemy_stats.drop_table_items_always.append(item)
                for item in all_game_items:
                    if item not in enemy_stats.drop_table_items and item.value >= (enemy_stats.level * 5) and item.value <= (enemy_stats.level * 20):
                        enemy_stats.drop_table_items.append(item)
                if dev_mode >= 1:
                    for item in enemy_stats.drop_table_items:
                        print(item.print_name)

                for weapon in enemy_stats.drop_table_weapons:
                    enemy_stats.drop_table_weapons_always.append(weapon)
                for weapon in all_game_weapons:
                    if weapon not in enemy_stats.drop_table_weapons:
                        if weapon.level <= (enemy_stats.level + 2) and weapon.level >= (enemy_stats.level - 6) and enemy_stats.attribute == weapon.attribute:
                            enemy_stats.drop_table_weapons.append(weapon)

                for armor in enemy_stats.drop_table_armor:
                    enemy_stats.drop_table_armor_always.append(armor)
                for armor in all_game_armor:
                    if armor not in enemy_stats.drop_table_armor:
                        if armor.level <= (enemy_stats.level + 2) and armor.level >= (enemy_stats.level - 6) and enemy_stats.attribute == armor.attribute:
                            enemy_stats.drop_table_armor.append(armor)

                for helmet in enemy_stats.drop_table_helmets:
                    enemy_stats.drop_table_helmets_always.append(helmet)
                for helmet in all_game_helmets:
                    if helmet not in enemy_stats.drop_table_helmets:
                        if helmet.level <= (enemy_stats.level + 2)and helmet.level >= (enemy_stats.level - 6) and enemy_stats.attribute == helmet.attribute:
                            enemy_stats.drop_table_helmets.append(helmet)

                for shield in enemy_stats.drop_table_shields:
                    enemy_stats.drop_table_shields_always.append(shield)
                for shield in all_game_shields:
                    if shield not in enemy_stats.drop_table_shields:
                        if shield.level <= (enemy_stats.level + 2) and shield.level >= (enemy_stats.level - 6) and enemy_stats.attribute == shield.attribute:
                            enemy_stats.drop_table_shields.append(shield)

                if dev_mode >= 1:
                    print("modifying enemy stats")
                enemy_stats.maxhp += (random.randint(0,50) * enemy_stats.level)
                enemy_stats.hp = (0 + enemy_stats.maxhp)
                enemy_stats.gp += ((random.randint(0,10) * enemy_stats.maxhp) // 1000) * enemy_stats.level
                enemy_stats.xp += ((random.randint(0,10) * enemy_stats.xp) // 10) * enemy_stats.level
                if dev_mode >= 1:
                    print("enemy stats have been calculated")

            player_turns = 3
            if dev_mode >= 1:
                print("playing battle intro")
            if npc_fight == False:
                func_refresh_pygame(True)
            else:
                func_refresh_pygame(False)
            npc_fight = False
            if dev_mode >= 1:
                print("battle intro finished")
            print(Fore.RED + "\n//////////// YOU ARE NOW IN COMBAT //////////// \n")
            print("\nLocation: " + scene_type.name)

            print("\nturns left: " + str(player_turns))

            if dev_mode >= 2:
                print("\nEnemy stats:")
                for enemy_stats in current_enemies:
                    status_list = []
                    for status_condition in enemy_stats.status_effect_list:
                        status_list.append(status_condition.name)
                    print("Name: " + enemy_stats.name)
                    print("LVL: " + str(enemy_stats.level))
                    print("ATT.: " + enemy_stats.print_attribute)
                    print("HP:" + Fore.RED + str(enemy_stats.hp) + Style.RESET_ALL + "/" + Fore.RED + str(enemy_stats.maxhp))
                    print("MP:" + Fore.BLUE + Style.BRIGHT + str(enemy_stats.mp) + Style.RESET_ALL + "/" + Fore.BLUE + Style.BRIGHT + str(enemy_stats.maxmp))
                    if len(enemy_stats.status_effect_list) != 0:
                        print("Status: " + str(status_list) + " \n")
                    else:
                        print("Status: ['N0NE'] \n")

                    func_HUD()

            while in_fight == True:
                pygame.time.delay(100)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_start = 0
                        in_fight = False

                func_check_level()
                func_refresh_pygame(False)
                keys = pygame.key.get_pressed()

                if keys[pygame.K_w]:
                    if combat_cursor_pos <= 1:
                        combat_cursor_pos == 1
                    else:
                        sfx_cursor_move.play()
                        combat_cursor_pos -= 1
                    if dev_mode >= 2:
                        print(combat_cursor_pos)

                if keys[pygame.K_s]:
                    if combat_cursor_pos >= 18:
                        combat_cursor_pos == 18
                    else:
                        sfx_cursor_move.play()
                        combat_cursor_pos += 1
                    if dev_mode >= 2:
                        print(combat_cursor_pos)

                if keys[pygame.K_e]:
                    sfx_cursor_select.play()
                    if combat_cursor_pos == 4: #run option
                        in_fight = False
                        print("you ran away! \n")
                        del current_enemies[:]
                        location_desc()
                    elif combat_cursor_pos == 1: #hit option
                        func_player_status_check(True,False)
                        func_check_enemy_dead()
                        func_check_level()
                        # func_enemy_status_check()
                        # func_check_enemy_dead()
                    elif combat_cursor_pos == 2: #spell option

                        if dev_mode >= 2:
                            print("\nYour equipped spells: \n")
                            for spell in equiped_spells:
                                print(str((equiped_spells.index(spell) + 1)) + " || " + spell.print_name + " || " + spell.print_attribute)
                            print("")
                            print("which spell will you cast? \n")

                        in_submenu = True
                        in_submenu_cast_combat = True
                        while in_submenu_cast_combat == True:
                            pygame.time.delay(100)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    game_start = 0
                                    in_fight = False
                                    in_submenu = False
                                    in_submenu_cast_combat = False

                            func_check_level()
                            func_refresh_pygame(False)

                            keys = pygame.key.get_pressed()

                            if keys[pygame.K_q]:
                                in_submenu = False
                                in_submenu_cast_combat = False

                            if keys[pygame.K_w]:
                                if combat_cursor_pos <= 1:
                                    combat_cursor_pos == 1
                                else:
                                    sfx_cursor_move.play()
                                    combat_cursor_pos -= 1
                                if dev_mode >= 2:
                                    print(combat_cursor_pos)

                            if keys[pygame.K_s]:
                                if combat_cursor_pos >= 18:
                                    combat_cursor_pos == 18
                                else:
                                    sfx_cursor_move.play()
                                    combat_cursor_pos += 1
                                if dev_mode >= 2:
                                    print(combat_cursor_pos)

                            if keys[pygame.K_e]:
                                sfx_cursor_select.play()

                                val_combat_spell = combat_cursor_pos
                                val = val_combat_spell - 1
                                for spell in spell_inventory:
                                    if val == spell_inventory.index(spell):
                                        combat_cast_spell = spell.name

                                has_spell = 0

                                for spell in equiped_spells:
                                    if spell.name == combat_cast_spell:
                                        has_spell = 1

                                player_turns -= 1
                                func_player_status_check(False,False)
                                func_check_enemy_dead()
                                func_check_level()
                                # func_enemy_status_check()
                                # func_check_enemy_dead()
                                in_submenu = False
                                in_submenu_cast_combat = False
                                break

                    elif combat_cursor_pos == 3: #use option
                        func_player_status_check(False,True)
                        func_use_combat(item,inventory)
                        func_check_enemy_dead()
                        func_check_level()
                        # func_enemy_status_check()
                        # func_check_enemy_dead()

                    elif combat_cursor_pos == 5:
                        in_fight = False
                        game_start = 0

                    elif combat_cursor_pos == 10:
                        in_fight = False
                        game_start = 0

                    else:
                        print("invalid combat command \n")

                    print("turns left: " + str(player_turns))
                    if player_turns == 0:

                        print("\n///////////////////////////////  end of player turn  ///////////////////////////\n")
                        func_enemy_status_check()
                        func_check_enemy_dead()
                        print("\n///////////////////////////////  end of enemy turn  ///////////////////////////\n")

                        player_turns = 3
                        print("\nturns left: " + str(player_turns))

        if in_fight == False:
            location_desc()
            if dev_mode >=2:
                func_HUD()

        has_moved = False

    player1.status_effect_list.clear()
    func_check_stat_bonus()
    func_check_level()
    func_refresh_pygame(False)

    if keys[pygame.K_w]:
        has_moved = True
        for scene_type in location_north:
            if scene_type.passable == True:
                steps_y -= 1
                prev_y = steps_y
                prev_y += 1
            else:
                print(scene_type.impass_msg + ", you have not moved.")

    if keys[pygame.K_s]:
        has_moved = True
        for scene_type in location_south:
            if scene_type.passable == True:
                steps_y += 1
                prev_y = steps_y
                prev_y -= 1
            else:
                print(scene_type.impass_msg + ", you have not moved")

    if keys[pygame.K_d]:
        has_moved = True
        for scene_type in location_east:
            if scene_type.passable == True:
                steps_x += 1
                prev_x = steps_x
                prev_x -= 1
            else:
                print(scene_type.impass_msg + ", you have not moved")

    if keys[pygame.K_a]:
        has_moved = True
        for scene_type in location_west:
            if scene_type.passable == True:
                steps_x -= 1
                prev_x = steps_x
                prev_x += 1
            else:
                print(scene_type.impass_msg + ", you have not moved")

    if keys[pygame.K_r]:
        has_moved = True
        has_rope = False
        has_stairs = False
        can_climb = False
        for item in inventory:
            if item.name == "rope":
                has_rope = True
                can_climb = True
        for scene_type in location:
            if scene_type.has_stairs == True:
                can_climb = True
                has_stairs = True
        if can_climb == True:
            for scene_type in location_up:
                if scene_type.passable == True and scene_type.has_stairs == True:
                    steps_z += 1
                    prev_z = steps_z
                    prev_z -= 1
                else:
                    print(scene_type.impass_msg + ", you have not moved.")
        if has_rope == False and has_stairs == False:
            print("you need a rope to climb up.")

    if keys[pygame.K_f]:
        has_moved = True
        has_rope = False
        has_stairs = False
        can_climb = False
        for item in inventory:
            if item.name == "rope":
                has_rope = True
                can_climb = True
        for scene_type in location:
            if scene_type.has_stairs == True:
                can_climb = True
                has_stairs = True
        if can_climb == True:
            for scene_type in location_down:
                if scene_type.passable == True and scene_type.has_stairs == True:
                    steps_z -= 1
                    prev_z = steps_z
                    prev_z += 1
                else:
                    print(scene_type.impass_msg + ", you have not moved")
        if has_rope == False:
            print("you need a rope to climb down.")

    if keys[pygame.K_SPACE]:
        in_menu = True

        while in_menu == True:

            pygame.time.delay(100)

            func_check_level()
            func_refresh_pygame(False)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                if menu_cursor_pos <= 1:
                    menu_cursor_pos == 1
                else:
                    sfx_cursor_move.play()
                    menu_cursor_pos -= 1
                if dev_mode >= 2:
                    print(menu_cursor_pos)

            if keys[pygame.K_s]:
                if menu_cursor_pos >= 24:
                    menu_cursor_pos == 24
                else:
                    sfx_cursor_move.play()
                    menu_cursor_pos += 1
                if dev_mode >= 2:
                    print(menu_cursor_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_start = 0
                    in_fight = False
                    in_menu = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        in_menu = False
                        print("menu quit")
                        break

                    if event.key == pygame.K_e:
                        sfx_cursor_select.play()
                        #search
                        if menu_cursor_pos == 13:
                            for scene_type in location:
                                if scene_type.treasure == True:
                                    func_search_treasure()
                                    scene_type.treasure = False
                                else:
                                    print("there is nothing here...\n")

                        #equip
                        elif menu_cursor_pos == 3:
                            if len(equiped_weapon) != 0:
                                for weapon in equiped_weapon:
                                    current_weapon = weapon.name
                            else:
                                current_weapon = "0"

                            if len(equiped_armor) != 0:
                                for armor in equiped_armor:
                                    current_armor = armor.name
                            else:
                                current_armor = "0"

                            if len(equiped_helmet) != 0:
                                for helmet in equiped_helmet:
                                    current_helmet = helmet.name
                            else:
                                current_helmet = "0"

                            if len(equiped_shield) != 0:
                                for shield in equiped_shield:
                                    current_shield = shield.name
                            else:
                                current_shield = "0"

                            current_spell = "0"

                            in_submenu = True
                            in_submenu_equip = True

                            while in_submenu_equip == True:

                                pygame.time.delay(100)

                                func_check_level()
                                func_refresh_pygame(False)

                                keys = pygame.key.get_pressed()

                                if keys[pygame.K_w]:
                                    if menu_cursor_pos <= 1:
                                        menu_cursor_pos == 1
                                    else:
                                        sfx_cursor_move.play()
                                        menu_cursor_pos -= 1
                                    if dev_mode >= 2:
                                        print(menu_cursor_pos)

                                if keys[pygame.K_s]:
                                    if menu_cursor_pos >= 18:
                                        menu_cursor_pos == 18
                                    else:
                                        sfx_cursor_move.play()
                                        menu_cursor_pos += 1
                                    if dev_mode >= 2:
                                        print(menu_cursor_pos)

                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        game_start = 0
                                        in_fight = False
                                        in_submenu = False
                                        in_submenu_equip == False
                                        in_menu = False

                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_q:
                                            in_submenu_equip = False
                                            in_submenu = False
                                            print("equip menu quit")
                                            break

                                        if event.key == pygame.K_e:
                                            sfx_cursor_select.play()
                                            if menu_cursor_pos == 1:
                                                if len(weapon_inventory) != 0:
                                                    func_equip(weapon,weapon_inventory,current_weapon)
                                                else:
                                                    print("you have no weapons in your inventory...")
                                            elif menu_cursor_pos == 2:
                                                if len(armor_inventory) != 0:
                                                    func_equip(armor,armor_inventory,current_armor)
                                                else:
                                                    print("you have no armor in your inventory...")
                                            elif menu_cursor_pos == 3:
                                                if len(helmet_inventory) != 0:
                                                    func_equip(helmet,helmet_inventory,current_helmet)
                                                else:
                                                    print("you have no helmets in your inventory...")
                                            elif menu_cursor_pos == 4:
                                                if len(shield_inventory) != 0:
                                                    func_equip(shield,shield_inventory,current_shield)
                                                else:
                                                    print("you have no shields in your inventory...")
                                            elif menu_cursor_pos == 5:
                                                if len(spell_inventory) != 0:
                                                    func_equip(spell,spell_inventory,current_spell)
                                                else:
                                                    print("you have no spell scrolls in your inventory...")
                                            else:
                                                print("\ninvalid choice!\n")

                                            func_check_stat_bonus()
                                            # in_submenu = False
                                            # in_submenu_equip = False
                                            in_submenu2 = False
                                            in_submenu_equip2 = False
                                            in_menu_item = False
                                            in_menu_spell = False
                                            in_menu_weapon = False
                                            in_menu_armor = False
                                            in_menu_helmet = False
                                            in_menu_shield = False

                        elif menu_cursor_pos == 15:
                            for player1 in players:
                                print("|| Stats: \n")
                                print("|| name: " + player1.name)
                                print("|| level: " + str(player1.level))
                                print("|| xp: " + str(player1.xp))
                                print("|| gold: " + str(player1.gp))
                                print("|| hp: " + str(player1.hp) + " / " + str(player1.nobonus_maxhp) + " || + " + str(player1.maxhp_bonus))
                                print("|| mp: " + str(player1.mp) + " / " + str(player1.nobonus_maxmp) + " || + " + str(player1.maxmp_bonus))

                                print("|| magic: " + str(player1.magic) + " || + " + str(player1.magic_bonus) + " || xp: " + str(player1.magic_xp))
                                print("|| strength: " + str(player1.strength) + " || + " + str(player1.strength_bonus) + " || xp: " + str(player1.strength_xp))
                                print("|| attack: " + str(player1.attack) + " || + " + str(player1.attack_bonus) + " || xp: " + str(player1.attack_xp))
                                print("|| defence: " + str(player1.defence) + " || + " + str(player1.defence_bonus) + " || xp: " + str(player1.defence_xp))

                        elif menu_cursor_pos == 14:
                            for player1_skills in players_skills:
                                print("|| Skills: \n")
                                print("|| fishing: " + str(player1_skills.fishing) + " || xp: " + str(player1_skills.fishing_xp))
                                print("|| theiving: " + str(player1_skills.thieving) + " || xp: " + str(player1_skills.thieving_xp))
                                print("|| crafting: " + str(player1_skills.crafting) + " || xp: " + str(player1_skills.crafting_xp))
                                print("|| cooking: " + str(player1_skills.cooking) + " || xp: " + str(player1_skills.cooking_xp))

                        elif menu_cursor_pos == 4:
                            for player1 in players:

                                print("gear: \n")

                                if len(equiped_helmet) != 0:
                                    for helmet in equiped_helmet:
                                        print("|| Helmet: \n")
                                        print("|| level: ", helmet.level)
                                        print("|| name: " + helmet.print_name + " || attribute: " + helmet.print_attribute + " || type: " + helmet.type)
                                        print("|| magic: " + str(helmet.magic_bonus) + " || strength: " + str(helmet.strength_bonus) + " || attack: " + str(helmet.attack_bonus))
                                        print("|| hp bonus: " + str(helmet.maxhp_bonus) + " || defence: " + str(helmet.defence_bonus))


                                    print("")
                                else:
                                    print("you have no helmet... \n")

                                if len(equiped_armor) != 0:
                                    for armor in equiped_armor:
                                        print("|| Armor: \n")
                                        print("|| level: ", armor.level)
                                        print("|| name: " + armor.print_name + " || attribute: " + armor.print_attribute + " || type: " + armor.type)
                                        print("|| magic: " + str(armor.magic_bonus) + " || strength: " + str(armor.strength_bonus) + " || attack: " + str(armor.attack_bonus))
                                        print("|| hp bonus: " + str(armor.maxhp_bonus) + " || defence: " + str(armor.defence_bonus))

                                    print("")
                                else:
                                    print("you have no armor... \n")

                                if len(equiped_shield) != 0:
                                    for shield in equiped_shield:
                                        print("|| Shield: \n")
                                        print("|| level: ", shield.level)
                                        print("|| name: " + shield.print_name + " || attribute: " + shield.print_attribute + " || type: " + shield.type)
                                        print("|| magic: " + str(shield.magic_bonus) + " || strength: " + str(shield.strength_bonus) + " || attack: " + str(shield.attack_bonus))
                                        print("|| hp bonus: " + str(shield.maxhp_bonus) + " || defence: " + str(shield.defence_bonus))

                                    print("")
                                else:
                                    print("you have no shield... \n")

                                if len(equiped_weapon) != 0:
                                    for weapon in equiped_weapon:
                                        print("|| Weapon: \n")
                                        print("|| level: ", weapon.level)
                                        print("|| name: " + weapon.print_name + " || attribute: " + weapon.print_attribute + " || type: " + weapon.type)
                                        print("|| magic: " + str(weapon.magic_bonus) + " || strength: " + str(weapon.strength_bonus) + " || attack: " + str(weapon.attack_bonus))
                                        print("|| hp bonus: " + str(weapon.maxhp_bonus) + " || defence: " + str(weapon.defence_bonus))
                                    print("")
                                else:
                                    print("you have no weapon... \n")

                        elif menu_cursor_pos == 12:
                            print("")
                            if dev_mode >= 2:
                                print("|| 1 || Items")
                                print("|| 2 || Weapons")
                                print("|| 3 || Armor")
                                print("|| 4 || Helmets")
                                print("|| 5 || Shields")
                                print("|| 6 || Spells")
                                print("\nwhich bag to drop from?\n")
                            in_submenu = True
                            in_submenu_drop = True
                            while in_submenu_drop == True:
                                pygame.time.delay(100)
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        game_start = 0
                                        in_fight = False
                                        in_submenu = False
                                        in_submenu_drop = False
                                        in_menu = False

                                func_check_level()
                                func_refresh_pygame(False)

                                keys = pygame.key.get_pressed()

                                if keys[pygame.K_q]:
                                    in_submenu = False
                                    in_submenu_drop = False

                                if keys[pygame.K_w]:
                                    if menu_cursor_pos <= 1:
                                        menu_cursor_pos == 1
                                    else:
                                        sfx_cursor_move.play()
                                        menu_cursor_pos -= 1
                                    if dev_mode >= 2:
                                        print(menu_cursor_pos)

                                if keys[pygame.K_s]:
                                    if menu_cursor_pos >= 18:
                                        menu_cursor_pos == 18
                                    else:
                                        sfx_cursor_move.play()
                                        menu_cursor_pos += 1
                                    if dev_mode >= 2:
                                        print(menu_cursor_pos)


                                if keys[pygame.K_e]:
                                    sfx_cursor_select.play()
                                    if menu_cursor_pos == 1:
                                        if len(inventory) != 0:
                                            func_drop(item,inventory)
                                        else:
                                            print("you have no items in your inventory...")
                                    elif menu_cursor_pos == 2:
                                        if len(weapon_inventory) != 0:
                                            func_drop(weapon,weapon_inventory)
                                        else:
                                            print("you have no weapons in your inventory...")
                                    elif menu_cursor_pos == 3:
                                        if len(armor_inventory) != 0:
                                            func_drop(armor,armor_inventory)
                                        else:
                                            print("you have no armor in your inventory...")
                                    elif menu_cursor_pos == 4:
                                        if len(helmet_inventory) != 0:
                                            func_drop(helmet,helmet_inventory)
                                        else:
                                            print("you have no helmets in your inventory...")
                                    elif menu_cursor_pos == 5:
                                        if len(shield_inventory) != 0:
                                            func_drop(shield,shield_inventory)
                                        else:
                                            print("you have no shields in your inventory...")
                                    elif menu_cursor_pos == 6:
                                        if len(spell_inventory) != 0:
                                            func_drop(spell,spell_inventory)
                                        else:
                                            print("you have no spell scrolls in your inventory...")
                                    else:
                                        print("\ninvalid choice!\n")
                                    in_submenu = False
                                    in_submenu_drop = False
                                    break

                        elif menu_cursor_pos == 10:
                            print("Which item do you want to pickup? NON FUNCTIONAL COMMAND\n")
                            pickedup_item = "0"
                            has_item = False
                            has_item_multiple = False
                            if has_item == False:
                                for scene_type in location:
                                    for ground_item in scene_type.scene_inventory:
                                        if ground_item.name == pickedup_item:
                                            has_item = True
                                            print("you pickup " + ground_item.print_name + " x " + str(ground_item.item_amount) + "\n")
                                            sleep(sleep_time_fast)

                                            for item in inventory:
                                                if item.name == pickedup_item:
                                                    has_item_multiple = True
                                                    item.item_amount += ground_item.item_amount
                                            if has_item_multiple == False:
                                                for item in all_game_items:
                                                    if item.name == pickedup_item:
                                                        inventory.append(item)
                                                        break
                                            scene_type.scene_inventory.remove(ground_item)

                                            break

                                    for ground_weapon in scene_type.scene_weapon_inventory:
                                        if ground_weapon.name == pickedup_item:
                                            has_item = True
                                            print("you pickup " + ground_weapon.print_name + "\n")
                                            sleep(sleep_time_fast)
                                            scene_type.scene_weapon_inventory.remove(ground_weapon)
                                            for weapon in all_game_weapons:
                                                if weapon.name == pickedup_item:
                                                    weapon_inventory.append(weapon)
                                                    break
                                            break

                                    for ground_armor in scene_type.scene_armor_inventory:
                                        if ground_armor.name == pickedup_item:
                                            has_item = True
                                            print("you pickup " + ground_armor.print_name + "\n")
                                            sleep(sleep_time_fast)
                                            scene_type.scene_armor_inventory.remove(ground_armor)
                                            for armor in all_game_armor:
                                                if armor.name == pickedup_item:
                                                    armor_inventory.append(armor)
                                                    break
                                            break

                                    for ground_helmet in scene_type.scene_helmet_inventory:
                                        if ground_helmet.name == pickedup_item:
                                            has_item = True
                                            print("you pickup " + ground_helmet.print_name + "\n")
                                            sleep(sleep_time_fast)
                                            scene_type.scene_helmet_inventory.remove(ground_helmet)
                                            for helmet in all_game_helmets:
                                                if helmet.name == pickedup_item:
                                                    helmet_inventory.append(helmet)
                                                    break
                                            break

                                    for ground_shield in scene_type.scene_shield_inventory:
                                        if ground_shield.name == pickedup_item:
                                            has_item = True
                                            print("you pickup " + ground_shield.print_name + "\n")
                                            sleep(sleep_time_fast)
                                            scene_type.scene_shield_inventory.remove(ground_shield)
                                            for shield in all_game_shields:
                                                if shield.name == pickedup_item:
                                                    shield_inventory.append(shield)
                                                    break
                                            break

                                    if has_item == False:
                                        print("that is not on the ground.\n")
                                        sleep(sleep_time_fast)
                                        break

                        elif menu_cursor_pos == 11:
                            print("")
                            while len(scene_type.scene_inventory) != 0 or len(scene_type.scene_weapon_inventory) != 0 or len(scene_type.scene_armor_inventory) != 0 or len(scene_type.scene_helmet_inventory) != 0 or len(scene_type.scene_shield_inventory) != 0:
                                has_item = False
                                has_item_multiple = False
                                while has_item == False:
                                    for scene_type in location:
                                        for ground_item in scene_type.scene_inventory:
                                            pickedup_item_amount = ground_item.item_amount
                                            pickedup_item = "0"
                                            pickedup_item = ground_item.name
                                            has_item = True
                                            print("you pickup " + ground_item.print_name + " x " + str(ground_item.item_amount))
                                            sleep(sleep_time_fast)
                                            for item in inventory:
                                                if item.name == pickedup_item:
                                                    has_item_multiple = True
                                                    item.item_amount += pickedup_item_amount

                                            if has_item_multiple == False:
                                                for item in all_game_items:
                                                    if item.name == pickedup_item:
                                                        inventory.append(item)
                                                        for item in inventory:
                                                            if item.name == pickedup_item:
                                                                item.item_amount = pickedup_item_amount
                                                        break
                                            scene_type.scene_inventory.remove(ground_item)
                                            break

                                        for ground_weapon in scene_type.scene_weapon_inventory:
                                            pickedup_item = "0"
                                            pickedup_item = ground_weapon.name
                                            has_item = True
                                            print("you pickup " + ground_weapon.print_name)
                                            sleep(sleep_time_fast)
                                            scene_type.scene_weapon_inventory.remove(ground_weapon)
                                            for weapon in all_game_weapons:
                                                if weapon.name == pickedup_item:
                                                    weapon_inventory.append(weapon)
                                                    break
                                            break

                                        for ground_armor in scene_type.scene_armor_inventory:
                                            pickedup_item = "0"
                                            pickedup_item = ground_armor.name
                                            has_item = True
                                            print("you pickup " + ground_armor.print_name)
                                            sleep(sleep_time_fast)
                                            scene_type.scene_armor_inventory.remove(ground_armor)
                                            for armor in all_game_armor:
                                                if armor.name == pickedup_item:
                                                    armor_inventory.append(armor)
                                                    break
                                            break

                                        for ground_helmet in scene_type.scene_helmet_inventory:
                                            pickedup_item = "0"
                                            pickedup_item = ground_helmet.name
                                            has_item = True
                                            print("you pickup " + ground_helmet.print_name)
                                            sleep(sleep_time_fast)
                                            scene_type.scene_helmet_inventory.remove(ground_helmet)
                                            for helmet in all_game_helmets:
                                                if helmet.name == pickedup_item:
                                                    helmet_inventory.append(helmet)
                                                    break
                                            break

                                        for ground_shield in scene_type.scene_shield_inventory:
                                            pickedup_item = "0"
                                            pickedup_item = ground_shield.name
                                            has_item = True
                                            print("you pickup " + ground_shield.print_name)
                                            sleep(sleep_time_fast)
                                            scene_type.scene_shield_inventory.remove(ground_shield)
                                            for shield in all_game_shields:
                                                if shield.name == pickedup_item:
                                                    shield_inventory.append(shield)
                                                    break
                                            break

                                        if has_item == False:
                                            print("\npicked up all items.\n")
                                            sleep(sleep_time_fast)
                                            break

                        elif menu_cursor_pos == 8:
                            func_use(item,inventory)

                    ################################################

                        elif menu_cursor_pos == 7:

                                print("\nInventory: \n")

                                if len(inventory) != 0:
                                    for item in inventory:

                                        print("|| " + item.print_name + " x " + str(item.item_amount))

                                if len(spell_inventory) != 0:
                                    for spell in spell_inventory:

                                        print("|| " + spell.print_name + " || " + spell.print_attribute + " || lvl: " + str(spell.level))

                                if len(helmet_inventory) != 0:
                                    for helmet in helmet_inventory:

                                        print("|| " + helmet.print_name + " x " + str(helmet.helmet_amount) + " || attribute: " + helmet.print_attribute + " || type: " + helmet.type + " || lvl: " + str(helmet.level))

                                if len(armor_inventory) != 0:
                                    for armor in armor_inventory:

                                        print("|| " + armor.print_name + " x " + str(armor.armor_amount) + " || attribute: " + armor.print_attribute + " || type: " + armor.type + " || lvl: " + str(armor.level))

                                if len(shield_inventory) != 0:
                                    for shield in shield_inventory:

                                        print("|| " + shield.print_name + " x " + str(shield.shield_amount) + " || attribute: " + shield.print_attribute + " || type: " + shield.type + " || lvl: " + str(shield.level))

                                if len(weapon_inventory) != 0:
                                    for weapon in weapon_inventory:

                                        print("|| " + weapon.print_name + " x " + str(weapon.weapon_amount) + " || attribute: " + weapon.print_attribute + " || type: " + weapon.type + " || lvl: " + str(weapon.level))

                                print("")

                        elif menu_cursor_pos == 16:
                            for scene_type in location:
                                print("you wait in " + scene_type.name + " ...\n")
                            location_desc()

                        elif menu_cursor_pos == 6:
                            can_camp = False
                            for item in inventory:
                                if item.name == "tent":
                                    has_tent = True
                                    for scene_type in location:
                                        if scene_type.safe == True:
                                            can_camp = True
                                    print("You camp untill the next morning, your hp has been restored.")
                                    time += 24
                                    for player_stats in players:
                                        player_stats.hp = player_stats.maxhp
                                        player_stats.mp = player_stats.maxmp
                                else:
                                    can_camp = False

                        elif menu_cursor_pos == 2:
                            func_cast(spell,equiped_spells)

                        elif menu_cursor_pos == 5:
                            print("\nequiped spells:")
                            for spell in equiped_spells:
                                print("|| " + spell.print_name + " || " + spell.print_attribute + " || " + spell.spell_desc)
                            print("")
                            print("spell scrolls:")
                            for spell in spell_inventory:
                                print("|| " + spell.print_name + " || " + spell.print_attribute + " || " + spell.spell_desc)
                            print("")

                    #################----DIALOGUE----###############

                        elif menu_cursor_pos == 1:
                            for scene_type in location:
                                if len(scene_type.npc_list) >= 1:
                                    for scene_type in location:
                                        if len(scene_type.npc_list) >= 1:
                                            print("")
                                            target_npc = "0"
                                            for npc in scene_type.npc_list:
                                                print("|| " + str((scene_type.npc_list.index(npc)+1)) + " || " + npc.first_name + " " + npc.last_name + ", " + npc.title + " || " + npc.npc_desc)

                                            print("\nWho will you talk too? \n")

                                            in_submenu = True
                                            in_submenu_talk = True
                                            npc_found = False
                                            while in_submenu_talk == True:
                                                pygame.time.delay(100)
                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        game_start = 0
                                                        in_fight = False
                                                        in_submenu = False
                                                        in_submenu_talk = False
                                                        in_menu = False

                                                func_check_level()
                                                func_refresh_pygame(False)

                                                keys = pygame.key.get_pressed()

                                                if keys[pygame.K_q]:
                                                    in_submenu = False
                                                    in_submenu_talk = False
                                                    in_menu = False


                                                if keys[pygame.K_w]:
                                                    if menu_cursor_pos <= 1:
                                                        menu_cursor_pos == 1
                                                    else:
                                                        sfx_cursor_move.play()
                                                        menu_cursor_pos -= 1
                                                    if dev_mode >= 2:
                                                        print(menu_cursor_pos)

                                                if keys[pygame.K_s]:
                                                    if menu_cursor_pos >= 18:
                                                        menu_cursor_pos == 18
                                                    else:
                                                        sfx_cursor_move.play()
                                                        menu_cursor_pos += 1
                                                    if dev_mode >= 2:
                                                        print(menu_cursor_pos)


                                                if keys[pygame.K_e]:
                                                    sfx_cursor_select.play()
                                                    val_dropped_item = menu_cursor_pos
                                                    val_drop = val_dropped_item - 1
                                                    for npc in scene_type.npc_list:
                                                        if val_drop == scene_type.npc_list.index(npc):
                                                            target_npc = npc.first_name
                                                            npc_found = True

                                                            for npc in scene_type.npc_list:
                                                                if npc.first_name == target_npc:
                                                                    current_npc.append(npc)
                                                                    if npc.is_animal == True:
                                                                        print("in front of you is a " + npc.gender + " " + npc.race + "\n")

                                                                    else:
                                                                        print("in front of you is a " + npc.race + " " + npc.gender + " in " + npc.attire + "\n")

                                                                        if npc.faction != "0":
                                                                            print(npc.greeting + ", I am " + npc.first_name + " " + npc.last_name + ", the " + npc.title + " of the " + npc.faction + "\n")
                                                                        else:
                                                                            print(npc.greeting + ", I am " + npc.first_name + " " + npc.last_name + ", the " + npc.title + "\n")

                                                                    print(npc.npc_desc)

                                                                    if len(npc.dialouge_options_list) > 1:
                                                                        print("")
                                                                        target_dialouge = "0"
                                                                        for dialouge_option in npc.dialouge_options_list:
                                                                            print("|| " + str((npc.dialouge_options_list.index(dialouge_option)+1)) + " || " + dialouge_option.text)
                                                                    print("\nWhat will you say? \n")
                                                                    in_submenu2 = True
                                                                    in_submenu_talk2 = True
                                                                    while in_submenu_talk2 == True:
                                                                        pygame.time.delay(100)
                                                                        for event in pygame.event.get():
                                                                            if event.type == pygame.QUIT:
                                                                                game_start = 0
                                                                                in_fight = False
                                                                                in_submenu2 = False
                                                                                in_submenu_talk2 = False
                                                                                in_menu = False


                                                                        func_check_level()
                                                                        func_refresh_pygame(False)

                                                                        keys = pygame.key.get_pressed()

                                                                        if keys[pygame.K_q]:
                                                                            in_submenu2 = False
                                                                            in_submenu_talk2 = False



                                                                        if keys[pygame.K_w]:
                                                                            if menu_cursor_pos <= 1:
                                                                                menu_cursor_pos == 1
                                                                            else:
                                                                                sfx_cursor_move.play()
                                                                                menu_cursor_pos -= 1
                                                                            if dev_mode >= 2:
                                                                                print(menu_cursor_pos)

                                                                        if keys[pygame.K_s]:
                                                                            if menu_cursor_pos >= 18:
                                                                                menu_cursor_pos == 18
                                                                            else:
                                                                                sfx_cursor_move.play()
                                                                                menu_cursor_pos += 1
                                                                            if dev_mode >= 2:
                                                                                print(menu_cursor_pos)


                                                                        if keys[pygame.K_e]:
                                                                            sfx_cursor_select.play()
                                                                            if len(npc.dialouge_options_list) > 1:
                                                                                val_target_input = menu_cursor_pos
                                                                                val_dialouge = val_target_input - 1
                                                                                for dialouge_option in npc.dialouge_options_list:
                                                                                    if val_dialouge == npc.dialouge_options_list.index(dialouge_option):
                                                                                        target_dialouge = dialouge_option.text

                                                                                        for dialouge_option in npc.dialouge_options_list:
                                                                                            if dialouge_option.text == target_dialouge:

                                                                                                if dialouge_option.is_quit == True:
                                                                                                    print("Goodbye!")
                                                                                                    in_submenu2 = False
                                                                                                    in_submenu_talk2 = False
                                                                                                    break

                                                                                                if dialouge_option.is_buy_weapon == True:
                                                                                                    func_shop(weapon,npc.npc_weapon_inventory)
                                                                                                    in_submenu2 = False
                                                                                                    in_submenu_talk2 = False
                                                                                                    break
                                                                                                if dialouge_option.is_buy_armor == True:
                                                                                                    func_shop(armor,npc.npc_armor_inventory)
                                                                                                    in_submenu2 = False
                                                                                                    in_submenu_talk2 = False
                                                                                                    break
                                                                                                if dialouge_option.is_buy_helmet == True:
                                                                                                    func_shop(helmet,npc.npc_helmet_inventory)
                                                                                                    in_submenu2 = False
                                                                                                    in_submenu_talk2 = False
                                                                                                    break
                                                                                                if dialouge_option.is_buy_shield == True:
                                                                                                    func_shop(armor,npc.npc_shield_inventory)
                                                                                                    in_submenu2 = False
                                                                                                    in_submenu_talk2 = False
                                                                                                    break

                                                                                                if dialouge_option.is_buy_item == True:
                                                                                                    func_shop(item,npc.npc_inventory)
                                                                                                    in_submenu2 = False
                                                                                                    in_submenu_talk2 = False
                                                                                                    break
                                                                                                if dialouge_option.is_buy_spell == True:
                                                                                                    func_shop(spell,npc.npc_spell_inventory)
                                                                                                    in_submenu2 = False
                                                                                                    in_submenu_talk2 = False
                                                                                                    break

                                                                                                if dialouge_option.is_talk == True:
                                                                                                    if npc.is_animal == True:
                                                                                                        print("You cannot speak with animals")
                                                                                                    else:
                                                                                                        print(npc.talk_text)
                                                                                                    in_submenu2 = False
                                                                                                    in_submenu_talk2 = False
                                                                                                    break

                                                                                                if dialouge_option.is_sell == True:
                                                                                                    print("")
                                                                                                    print("|| 1 || Items")
                                                                                                    print("|| 2 || Weapons")
                                                                                                    print("|| 3 || Armor")
                                                                                                    print("|| 4 || Helmets")
                                                                                                    print("|| 5 || Shields")
                                                                                                    print("|| 6 || Spells")
                                                                                                    in_submenu3 = True
                                                                                                    in_submenu_sell3 = True
                                                                                                    while in_submenu_sell3 == True:
                                                                                                        pygame.time.delay(100)
                                                                                                        for event in pygame.event.get():
                                                                                                            if event.type == pygame.QUIT:
                                                                                                                game_start = 0
                                                                                                                in_fight = False
                                                                                                                in_submenu3 = False
                                                                                                                in_submenu_sell3 = False
                                                                                                                in_menu = False

                                                                                                        func_check_level()
                                                                                                        func_refresh_pygame(False)

                                                                                                        keys = pygame.key.get_pressed()

                                                                                                        if keys[pygame.K_q]:
                                                                                                            in_submenu3 = False
                                                                                                            in_submenu_sell3 = False


                                                                                                        if keys[pygame.K_w]:
                                                                                                            if menu_cursor_pos <= 1:
                                                                                                                menu_cursor_pos == 1
                                                                                                            else:
                                                                                                                sfx_cursor_move.play()
                                                                                                                menu_cursor_pos -= 1
                                                                                                            if dev_mode >= 2:
                                                                                                                print(menu_cursor_pos)

                                                                                                        if keys[pygame.K_s]:
                                                                                                            if menu_cursor_pos >= 18:
                                                                                                                menu_cursor_pos == 18
                                                                                                            else:
                                                                                                                sfx_cursor_move.play()
                                                                                                                menu_cursor_pos += 1
                                                                                                            if dev_mode >= 2:
                                                                                                                print(menu_cursor_pos)


                                                                                                        if keys[pygame.K_e]:
                                                                                                            sfx_cursor_select.play()
                                                                                                            if menu_cursor_pos == 1:
                                                                                                                func_sell(item,inventory)
                                                                                                                in_submenu3 = False
                                                                                                                in_submenu_sell3 = False
                                                                                                                break
                                                                                                            if menu_cursor_pos == 2:
                                                                                                                func_sell(weapon,weapon_inventory)
                                                                                                                in_submenu3 = False
                                                                                                                in_submenu_sell3 = False
                                                                                                                break
                                                                                                            if menu_cursor_pos == 3:
                                                                                                                func_sell(armor,armor_inventory)
                                                                                                                in_submenu3 = False
                                                                                                                in_submenu_sell3 = False
                                                                                                                break
                                                                                                            if menu_cursor_pos == 4:
                                                                                                                func_sell(helmet,helmet_inventory)
                                                                                                                in_submenu3 = False
                                                                                                                in_submenu_sell3 = False
                                                                                                                break
                                                                                                            if menu_cursor_pos == 5:
                                                                                                                func_sell(shield,shield_inventory)
                                                                                                                in_submenu3 = False
                                                                                                                in_submenu_sell3 = False
                                                                                                                break
                                                                                                            if menu_cursor_pos == 6:
                                                                                                                func_sell(spell,spell_inventory)
                                                                                                                in_submenu3 = False
                                                                                                                in_submenu_sell3 = False
                                                                                                                break
                                                                                                            in_submenu3 = False
                                                                                                            in_submenu_sell3 = False
                                                                                                            break
                                                                                                if dialouge_option.is_assault == True:
                                                                                                    print(npc.assault_dialouge)
                                                                                                    current_enemies.extend(npc.combat_enemy_list)
                                                                                                    npc_enemy_fname = npc.first_name
                                                                                                    npc_enemy_lname = npc.last_name
                                                                                                    in_fight = True
                                                                                                    npc_fight = True
                                                                                                    is_talking = False
                                                                                                    in_submenu2 = False
                                                                                                    in_submenu_talk2 = False
                                                                                                    in_menu = False
                                                                                                    break

                                                                                                if dialouge_option.is_give == True:
                                                                                                    print("execute func_give_item")
                                                                                                    in_submenu2 = False
                                                                                                    in_submenu_talk2 = False
                                                                                                    break

                                                                                                if dialouge_option.is_quest == True:
                                                                                                    print("execute func_quest")
                                                                                                    in_submenu2 = False
                                                                                                    in_submenu_talk2 = False
                                                                                                    break
                                                                                                if dialouge_option.is_heal == True:
                                                                                                    print("\nHealed by the doctor!\n")
                                                                                                    player1.hp = player1.maxhp
                                                                                                    in_submenu2 = False
                                                                                                    in_submenu_talk2 = False
                                                                                                    break

                                                                                                break

                                                                            in_submenu2 = False
                                                                            in_submenu_talk2 = False
                                                                            break
                                                                    current_npc.remove(npc)

                                                    in_submenu = False
                                                    in_submenu_talk = False
                                                    break
                                else:
                                    print("there is nobody to talk to\n")

                    ################################################

                        elif menu_cursor_pos == 90000:
                            ing_1 = "0"
                            ing_2 = "0"
                            ing_1_index = 0
                            ing_2_index = 0
                            has_cooked = False
                            for scene_type in location:
                                if player1_skills.crafting != 0:

                                    ing_1 = func_cook() # func_cook returns the name of the item the player selects as string
                                    for item in inventory:
                                        if item.name == ing_1:
                                            ing_1_index = inventory.index(item)
                                            inventory.remove(item)
                                            break

                                    ing_2 = func_cook()
                                    for item in inventory:
                                        if item.name == ing_2:
                                            ing_2_index = inventory.index(item)
                                            inventory.remove(item)
                                            break

                                    if ing_1 != ing_2:
                                        while recipe_found == False:
                                            #iterates thorugh all recipes untill it finds a match for both ingredients
                                            #breaks when it minds a match prints lvl status and item created
                                            func_create_item(ing_1,ing_2,cup,mushroom,1,mushroom_tea)
                                            if recipe_found == True:
                                                break
                                            func_create_item(ing_1,ing_2,mug,mushroom,1,mushroom_tea)
                                            if recipe_found == True:
                                                break
                                            func_create_item(ing_1,ing_2,cup,tea_bag,1,cup_of_tea)
                                            if recipe_found == True:
                                                break
                                            func_create_item(ing_1,ing_2,cup,magic_mushroom,1,mushroom_tea)
                                            if recipe_found == True:
                                                break
                                            func_create_item(ing_1,ing_2,mug,magic_mushroom,1,mushroom_tea)
                                            if recipe_found == True:
                                                break
                                            func_create_item(ing_1,ing_2,mushroom_tea,mushroom,1,mushroom_brew)
                                            if recipe_found == True:
                                                break
                                            func_create_item(ing_1,ing_2,mushroom_tea,magic_mushroom,1,mushroom_brew)
                                            if recipe_found == True:
                                                break
                                            #break loop if no match is found
                                            break
                                        if has_cooked == False:
                                            if ing_2_index > ing_1_index:
                                                ing_2_index += 1
                                            if ing_1_index > ing_2_index:
                                                ing_1_index += 1
                                            print("nothing interesting happens...\n")
                                            for item in all_game_items:
                                                if item.name == ing_1:
                                                    inventory.insert(ing_1_index,item)
                                                if item.name == ing_2:
                                                    inventory.insert(ing_2_index,item)

                    ################################################

                        elif menu_cursor_pos == 17:
                            if dev_mode >= 1:
                                print("dev menu open")

                                root = Tk()

                                dw_p1_xp = IntVar()
                                dw_p1_xp.set(player1.xp)

                                dw_player_xp = Label(root, textvariable=dw_p1_xp)
                                dw_player_xp.grid(row=0, column=1)
                                xp_label = Label(root, text="xp:")
                                xp_label.grid(row=0, column=0)

                                dw_p1_gp = IntVar()
                                dw_p1_gp.set(player1.gp)

                                dw_player_gp = Label(root, textvariable=dw_p1_gp)


                                #####################################

                                def func_click_xp():
                                    player1.xp += int(xp_entry.get())
                                    dw_p1_xp.set(player1.xp)
                                    xp_entry.delete(0, 'end')


                                xp_entry = Entry(root, width = 10)
                                xp_entry.grid(row=1, column=0, columnspan=2)

                                xp_button = Button(root, text=" + xp", command=func_click_xp)
                                xp_button.grid(row=2, column=0, columnspan=2)

                                #####################################

                                dw_player_gp.grid(row=0, column=3)
                                gp_label = Label(root, text="gp:")
                                gp_label.grid(row=0, column=2)

                                def func_click_gp():
                                    player1.gp += int(gp_entry.get())
                                    dw_p1_gp.set(player1.gp)
                                    gp_entry.delete(0, 'end')


                                gp_entry = Entry(root, width = 10)
                                gp_entry.grid(row=1, column=2, columnspan=2)

                                gp_button = Button(root, text=" + gp", command=func_click_gp)
                                gp_button.grid(row=2, column=2, columnspan=2)

                                #####################################
                                def func_click_tp():
                                    func_tp(int(tpx_entry.get()),int(tpy_entry.get()),int(tpz_entry.get()))



                                tpx_entry = Entry(root, width = 10)
                                tpx_entry.grid(row=3, column=0)
                                tpx_entry.insert(0,"0")

                                tpy_entry = Entry(root, width = 10)
                                tpy_entry.grid(row=4, column=0)
                                tpy_entry.insert(0,"0")

                                tpz_entry = Entry(root, width = 10)
                                tpz_entry.grid(row=5, column=0)
                                tpz_entry.insert(0,"0")

                                tp_button = Button(root, text="teleport", command=func_click_tp)
                                tp_button.grid(row=3, column=1)

                                #####################################

                                item_name_list = []
                                dev_item = StringVar()

                                name_string = "0"


                                def func_click_item():
                                    has_item_multiple = False
                                    for item in all_game_items:
                                        if item.name == dev_item.get():
                                            for item in inventory:
                                                if item.name == dev_item.get():
                                                    has_item_multiple = True
                                                    item.item_amount += 1
                                                    break
                                            if has_item_multiple == False:
                                                for item in all_game_items:
                                                    if item.name == dev_item.get():
                                                        inventory.append(item)
                                                        break
                                            # break

                                for item in all_game_items:
                                    name_string = item.name
                                    item_name_list.append(name_string)

                                dev_item.set(item_name_list[0])

                                item_choice = OptionMenu(root, dev_item, *item_name_list)
                                item_choice.grid(row=0, column=4, columnspan=2)
                                item_button = Button(root, text=" + item", command=func_click_item)
                                item_button.grid(row=0, column=6, columnspan=1)

                                #####################################

                                weapon_name_list = []
                                dev_weapon = StringVar()

                                weapon_name_string = "0"

                                def func_click_weapon():
                                    has_weapon_multiple = False
                                    for weapon in all_game_weapons:
                                        if weapon.name == dev_weapon.get():
                                            for weapon in weapon_inventory:
                                                if weapon.name == dev_weapon.get():
                                                    has_weapon_multiple = True
                                                    weapon.weapon_amount += 1
                                                    break
                                            if has_weapon_multiple == False:
                                                for weapon in all_game_weapons:
                                                    if weapon.name == dev_weapon.get():
                                                        weapon_inventory.append(weapon)
                                                        break
                                            # break

                                for weapon in all_game_weapons:
                                    weapon_name_string = weapon.name
                                    weapon_name_list.append(weapon_name_string)

                                dev_weapon.set(weapon_name_list[0])

                                weapon_choice = OptionMenu(root, dev_weapon, *weapon_name_list)
                                weapon_choice.grid(row=2, column=4, columnspan=2)
                                weapon_button = Button(root, text=" + weapon", command=func_click_weapon)
                                weapon_button.grid(row=2, column=6, columnspan=1)

                                #####################################

                                armor_name_list = []
                                dev_armor = StringVar()

                                armor_name_string = "0"

                                def func_click_armor():
                                    has_armor_multiple = False
                                    for armor in all_game_armor:
                                        if armor.name == dev_armor.get():
                                            for armor in armor_inventory:
                                                if armor.name == dev_armor.get():
                                                    has_armor_multiple = True
                                                    armor.armor_amount += 1
                                                    break
                                            if has_armor_multiple == False:
                                                for armor in all_game_armor:
                                                    if armor.name == dev_armor.get():
                                                        armor_inventory.append(armor)
                                                        break

                                for armor in all_game_armor:
                                    armor_name_string = armor.name
                                    armor_name_list.append(armor_name_string)

                                dev_armor.set(armor_name_list[0])

                                armor_choice = OptionMenu(root, dev_armor, *armor_name_list)
                                armor_choice.grid(row=3, column=4, columnspan=2)
                                armor_button = Button(root, text=" + armor", command=func_click_armor)
                                armor_button.grid(row=3, column=6, columnspan=1)


                                #####################################

                                helmet_name_list = []
                                dev_helmet = StringVar()

                                helmet_name_string = "0"

                                def func_click_helmet():
                                    has_helmet_multiple = False
                                    for helmet in all_game_helmets:
                                        if helmet.name == dev_helmet.get():
                                            for helmet in helmet_inventory:
                                                if helmet.name == dev_helmet.get():
                                                    has_helmet_multiple = True
                                                    helmet.helmet_amount += 1
                                                    break
                                            if has_helmet_multiple == False:
                                                for helmet in all_game_helmets:
                                                    if helmet.name == dev_helmet.get():
                                                        helmet_inventory.append(helmet)
                                                        break

                                for helmet in all_game_helmets:
                                    helmet_name_string = helmet.name
                                    helmet_name_list.append(helmet_name_string)

                                dev_helmet.set(helmet_name_list[0])

                                helmet_choice = OptionMenu(root, dev_helmet, *helmet_name_list)
                                helmet_choice.grid(row=4, column=4, columnspan=2)
                                helmet_button = Button(root, text=" + helmet", command=func_click_helmet)
                                helmet_button.grid(row=4, column=6, columnspan=1)

                                #####################################
                                shield_name_list = []
                                dev_shield = StringVar()

                                shield_name_string = "0"

                                def func_click_shield():
                                    has_shield_multiple = False
                                    for shield in all_game_shields:
                                        if shield.name == dev_shield.get():
                                            for shield in shield_inventory:
                                                if shield.name == dev_shield.get():
                                                    has_shield_multiple = True
                                                    shield.shield_amount += 1
                                                    break
                                            if has_shield_multiple == False:
                                                for shield in all_game_shields:
                                                    if shield.name == dev_shield.get():
                                                        shield_inventory.append(shield)
                                                        break

                                for shield in all_game_shields:
                                    shield_name_string = shield.name
                                    shield_name_list.append(shield_name_string)

                                dev_shield.set(shield_name_list[0])

                                shield_choice = OptionMenu(root, dev_shield, *shield_name_list)
                                shield_choice.grid(row=5, column=4, columnspan=2)
                                shield_button = Button(root, text=" + shield", command=func_click_shield)
                                shield_button.grid(row=5, column=6, columnspan=1)

                                #####################################

                                spell_name_list = []
                                dev_spell = StringVar()

                                name_string = "0"

                                def func_click_spell():
                                    for spell in all_game_spells:
                                        if spell.name == dev_spell.get():
                                            spell_inventory.append(spell)
                                            break

                                for spell in all_game_spells:
                                    spell_name_string = spell.name
                                    spell_name_list.append(spell_name_string)

                                dev_spell.set(spell_name_list[0])

                                spell_choice = OptionMenu(root, dev_spell, *spell_name_list)
                                spell_choice.grid(row=1, column=4, columnspan=2)
                                spell_button = Button(root, text=" + spell", command=func_click_spell)
                                spell_button.grid(row=1, column=6, columnspan=1)

                                #####################################


                                root.mainloop()


                        elif menu_cursor_pos == 18:
                            game_start = 0
                            break

                    ################################################

                        elif menu_cursor_pos == 19:
                            dev_mode += 1
                            if dev_mode >= 6:
                                dev_mode = 0

                        elif menu_cursor_pos == 20:
                            if dev_mode >= 1:
                                pass

                        elif menu_cursor_pos == 21:
                            if dev_mode >= 1:
                                pass

                        else:
                            print("invalid command\n")



#######################################################################################


    time += 1
    time2 += 1

    if time2 >= 600:
        time2 = 0

    if time >= 2400:
        time = 0
        print("\nthe sun has risen...\n")
        sleep(sleep_time_fast)
        days += 1
        if days >= 30:
            days = 1
            months += 1
            if months >= 13:
                months = 1
                years += 1
                print("\nHappy new year " + player1.name + "! \nThe year is now:")
                print(years)
                sleep(sleep_time_fast)

    if time == 1200:
        print("\nthe sun has gone down...\n")
        sleep(sleep_time_fast)

    if game_start == 0:
        break

#end of script
pygame.quit()
