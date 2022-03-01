
# TBA

from distutils.log import debug

import time as systime

version = "a2.0"

dev_mode = 2
lighting_mode = 0

grid_mode = 0
toggle_music = 0

if dev_mode >= 1:
    gen_sea = 0
    run_intro = False
else:
    gen_sea = 1
    run_intro = True

if run_intro == True:
    from intro import *
else:
    player_class_string = "1"
    player_name_string = "dev character"

########### import modules ##############

import random

#import subprocess
import sys #TODO disbel tkinter dev menu when using mac

##########--3RD PARTY MODULES--###############

from tkinter import *

from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

import pygame
import pygame.gfxdraw
pygame.mixer.pre_init() #44100, 16, 2, 4096
pygame.init()
pygame.font.init() # you have to call this at the start if you want to use fonts
myfont = pygame.font.Font('fonts/VT323-Regular.ttf',19,) # you have to call this at the start if you want to use fonts
gridfont = pygame.font.SysFont('MS Comic Sans', 16) # you have to call this at the start if you want to use fonts

pygame.key.set_repeat(300,200) # held key repeat timer (300,200)


from pytmx.util_pygame import load_pygame

#################--IMPORT_GAME_MODULES--####################

from scene_module import *
from npc_module import *

#import item_module as items_module
from item_module import *

from equipment_module import *
from spell_module import *

from enemy_module import *
from party_member_module import *

from colours_modules import *

import menu_module as menus
###########################----GLOBAL_VARIABLES-----####################

clock = pygame.time.Clock() #global clock

tick_delay_time = 0 #obsolete 

music_playing = 0

has_moved = False
check_for_combat = True
if dev_mode >= 2:
    check_for_combat = False
restock_shops = False
restock_ticks = 0

steps_x = 11
steps_y = 11
steps_z = 0

player_direction = 2

###########################################
current_menu = None
frames = 0
current_anim_index = 0
anim_index_max = 2

step_counter = 8
step_counter2 = 5

step_counter_max = 10

prev_x = 6
prev_y = 0
prev_z = 0

npc_fight = False
npc_enemy_fname = "0"
npc_enemy_lname = "0"

nearby_npc_list = [] 

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
in_submenu_questlog = False

in_submenu_talk = False
in_submenu_talk2 = False

in_submenu_buy3 = False

in_submenu_sell3 = False
in_submenu_sell4 = False

in_submenu_use = False
in_submenu_make = False
in_submenu_action = False
in_submenu_cook2 = False

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

raining = 1
weather = 0
season = 3 # value from 0,3 that determines season

time = 0
time2 = 0
days = 19
months = 4
years = 1567

time_latch = False

default_drop_table_items = []
default_drop_table_weapons = []
default_drop_table_armor = []

combat_option_list = []
input_option_list = []

quest_list = []

#blit globals

menu_cursor_pos = 1
combat_cursor_pos = 1

def func_reset_cursor_pos():
    global menu_cursor_pos
    global combat_cursor_pos
    menu_cursor_pos = 1
    combat_cursor_pos = 1

def func_close_all_menus():
    global in_submenu
    global in_menu
    global in_submenu2
    global in_submenu3
    global in_submenu4

    global in_submenu_equip
    global in_submenu_equip2

    global in_submenu_cast
    global in_submenu_drop
    global in_submenu_drop2
    global in_submenu_pickup
    global in_submenu_questlog

    global in_submenu_talk
    global in_submenu_talk2

    global in_submenu_buy3

    global in_submenu_sell3
    global in_submenu_sell4

    global in_submenu_use
    global in_submenu_make
    global in_submenu_action
    global in_submenu_cook2

    global in_submenu_use_combat
    global in_submenu_cast_combat
    global in_submenu_target_combat2
    global in_submenu_spell_target_combat2

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
    in_submenu_questlog = False

    in_submenu_talk = False
    in_submenu_talk2 = False

    in_submenu_buy3 = False

    in_submenu_sell3 = False
    in_submenu_sell4 = False

    in_submenu_use = False
    in_submenu_make = False
    in_submenu_action = False
    in_submenu_cook2 = False

    in_submenu_use_combat = False
    in_submenu_cast_combat = False
    in_submenu_target_combat2 = False
    in_submenu_spell_target_combat2 = False

blit_player_damage_amount = 0

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

##################################--PLAYER--############################################

class player_stats:
    def __init__(self, name):
        self.name = name
        
        self.level = 1
        self.xp = 1
        self.hp = 1 # current mana points
        self.mp = 1 # current hit points
        self.gp = 1

        self.magic = 1 #base stats
        self.strength = 1
        self.attack = 1
        self.defence = 1

        self.maxhp = 1 # hit points maximum value
        self.nobonus_maxhp = 1 #  hit points max without gear bonus

        self.maxmp = 1 # mana points maximum value
        self.nobonus_maxmp = 1 #  mana points max without gear bonus
        
        self.strength_xp = 1 #expereince
        self.attack_xp = 1
        self.magic_xp = 1
        self.defence_xp = 1

        self.status_effect = 1 #not used

        self.magic_bonus = 1 #equipment bonuses
        self.strength_bonus = 1
        self.attack_bonus = 1
        self.defence_bonus = 1
        self.maxhp_bonus = 1
        self.maxmp_bonus = 1

        self.status_effect_list = []

        self.status_effect_magic_bonus = 0 # status effect bonuses
        self.status_effect_strength_bonus = 0
        self.status_effect_attack_bonus = 0
        self.status_effect_defence_bonus = 0

        self.total_magic = 0 # base + equipment bonus + status effect bonuses
        self.total_strength = 0
        self.total_attack = 0
        self.total_defence = 0

        self.weakness = "nothing"
        self.attribute = "nothing"

    def calculate_total_bonuses(self):
        self.total_magic = self.status_effect_magic_bonus + self.magic_bonus + self.magic
        self.total_strength = self.status_effect_strength_bonus + self.strength_bonus + self.strength
        self.total_attack = self.status_effect_attack_bonus + self.attack_bonus + self.attack
        self.total_defence = self.status_effect_defence_bonus + self.defence_bonus + self.defence

    
    def check_dead(self):
        if self.hp <= 0:
            dead_timer = 10
            while dead_timer > 0:
                dead_timer -= 1
                print("\nYOU ARE DEAD... not big suprise")
            game_start = 0
            exit()
            #TODO  GO TO MAIN MENU WHEN DEAD


    def heal(self,amount):
        self.hp += amount
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        print("\n" + self.name + " heals for: " + Fore.GREEN + Style.BRIGHT + str(amount))

    def take_damage(self,damage,attribute,attacker_name):

        #deals damage to the player and returns the amount of damage dealt afterwards

        if attribute == self.attribute:
            damage = damage // 2
            print("it's not very effective")
        if attribute == self.weakness:
            damage = damage*2
            print("it's super effective")

        if damage > self.hp:
            damage = self.hp

        print("\n" + attacker_name + " hit you for " + self.name + " for " + Fore.RED + Style.BRIGHT + str(damage) + " " + colour_attribute + attribute + " " + "damage!")
        self.hp -= damage
        self.check_dead()
        return damage


player1 = player_stats(player_name_string)

class player_skills:
    def __init__(self, fishing, fishing_xp, thieving, thieving_xp, alchemy, alchemy_xp, cooking, cooking_xp):
        self.fishing = fishing
        self.fishing_xp = fishing_xp
        self.thieving = thieving
        self.thieving_xp = thieving_xp
        self.alchemy = alchemy
        self.alchemy_xp = alchemy_xp
        self.cooking = cooking
        self.cooking_xp = cooking_xp

player1_skills = player_skills(1,0,1,0,1,0,1,0)


class combat_option:
    def __init__(self, name):
        self.name = name

combat_option_hit = combat_option("hit")
combat_option_spell = combat_option("spell")
combat_option_item = combat_option("item")
combat_option_run = combat_option("run")

############################################--NPCS/DIALOUGE/QUESTS--#########################################

class quest:
    def __init__(self, name, quest_desc, xp, gp, reward_list, quest_collect_item, quest_item_name, quest_item_amount, quest_kill_enemy, quest_enemy_name, quest_kill_amount, quest_talk_npc, quest_npc_fname, quest_npc_lname):
        self.name = name
        self.quest_desc = quest_desc
        self.xp = xp
        self.gp = gp
        self.reward_list = reward_list
        self.quest_collect_item = quest_collect_item
        self.quest_item_name = quest_item_name
        self.quest_item_amount = quest_item_amount
        self.quest_kill_enemy = quest_kill_enemy
        self.quest_enemy_name = quest_enemy_name
        self.quest_kill_amount = quest_kill_amount
        self.quest_talk_npc = quest_talk_npc
        self.quest_npc_fname = quest_npc_fname
        self.quest_npc_lname = quest_npc_lname
        self.player_item_count = 0
        self.player_kill_count = 0
        self.started = False
        self.finished = False
        self.finished_message_displayed = False
        self.reward_collected = False
        self.quest_info = ""
        if quest_collect_item == True and quest_item_amount > 1:
            self.quest_info += "\nyou must find " + str(quest_item_amount) + " x " + quest_item_name
        if quest_collect_item == True and quest_item_amount == 1:
            self.quest_info += "\nyou must find " + quest_item_name


        if quest_kill_enemy == True and quest_kill_amount > 1:
            self.quest_info += "\nYou must kill " + str(quest_kill_amount) + " x " + quest_enemy_name
        if quest_kill_enemy == True and quest_kill_amount == 1:
            self.quest_info += "\nYou must kill " + quest_enemy_name

        if quest_talk_npc == True:
            self.quest_info += "\nYou must talk to " + quest_npc_fname + " " + quest_npc_lname


        quest_list.append(self)

quest_1 = quest("Cow Elite Killer","Prove your combat ability.", xp = 50, gp = 80, reward_list = [], quest_collect_item = False, quest_item_name = "0", quest_item_amount = 0, quest_kill_enemy = True, quest_enemy_name = "cow", quest_kill_amount = 1, quest_talk_npc = False, quest_npc_fname = "0", quest_npc_lname = "0")
quest_2 = quest("The Bandit Menace","Eliminate the local bandit population.", xp = 200, gp = 200, reward_list = [], quest_collect_item = False, quest_item_name = "0", quest_item_amount = 0, quest_kill_enemy = True, quest_enemy_name = "bandit", quest_kill_amount = 3, quest_talk_npc = False, quest_npc_fname = "0", quest_npc_lname = "0")
quest_3 = quest("Talk to Shmurlitz","Talk to Shmurlitz Durlitz, the town doctor.", xp = 50, gp = 10, reward_list = [], quest_collect_item = False, quest_item_name = "0", quest_item_amount = 0, quest_kill_enemy = False, quest_enemy_name = "", quest_kill_amount = 0, quest_talk_npc = True, quest_npc_fname = "Shmurlitz", quest_npc_lname = "Durlitz")
quest_4 = quest("Travel to Sorrlund","Travel down the high road to Sorrlund.", xp = 50, gp = 10, reward_list = [], quest_collect_item = False, quest_item_name = "0", quest_item_amount = 0, quest_kill_enemy = False, quest_enemy_name = "", quest_kill_amount = 0, quest_talk_npc = True, quest_npc_fname = "Jim", quest_npc_lname = "Greenmichs")
quest_5 = quest("Chop Wood","Cut down some trees for Jim.", xp = 50, gp = 120, reward_list = [certificate_of_passage], quest_collect_item = True, quest_item_name = "wood", quest_item_amount = 10, quest_kill_enemy = False, quest_enemy_name = "", quest_kill_amount = 0, quest_talk_npc = False, quest_npc_fname = "0", quest_npc_lname = "0")


#####################################################

def func_basic_droptables():
    del weapons_drop_table[:]
    del armor_drop_table[:]
    del helmets_drop_table[:]
    del shields_drop_table[:]
    del items_drop_table[:]

    lvl_min = 20 + random.randint(0,10)
    lvl_max = 5 + random.randint(0,5)

    for weapon in all_game_weapons:
        if weapon.level >= (player1.level - lvl_min) and weapon.level <= (player1.level + lvl_max):
            weapons_drop_table.append(weapon)
            random.shuffle(weapons_drop_table)

    for armor in all_game_armor:
        if armor.level >= (player1.level - lvl_min) and armor.level <= (player1.level + lvl_max):
            armor_drop_table.append(armor)
            random.shuffle(armor_drop_table)

    for helmet in all_game_helmets:
        if helmet.level >= (player1.level - lvl_min) and helmet.level <= (player1.level + lvl_max):
            helmets_drop_table.append(helmet)
            random.shuffle(helmets_drop_table)

    for shield in all_game_shields:
        if shield.level >= (player1.level - lvl_min) and shield.level <= (player1.level + lvl_max):
            shields_drop_table.append(shield)
            random.shuffle(shields_drop_table)


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

func_basic_droptables()

# place npcs in the world
def game_init():

    # dismurth_gates.npc_list.append(npc_town_guard)
    # tavern_interior_2.npc_list.append(npc_jenkins)
    # tavern_interior_1.npc_list.append(npc_jane_doe)
    # tavern_interior_3.npc_list.append(npc_doctor)
    # tower_interior_4.npc_list.append(npc_wizard_traenus)
    # tower_interior_7.npc_list.append(npc_wizard_marbles)
    # smith_interior_1.npc_list.append(npc_dismurth_smith)
    # smith_interior_3.npc_list.append(npc_john_doe)


    # cabin_interior_1.npc_list.append(npc_wizard_jim)
    # cabin_interior_3.npc_list.append(npc_wizard_tilly)


    # grassland_2.npc_list.append(npc_sheep)
    # dungeon_floor_7_entrance_6.npc_list.append(npc_cow)

    ################################

    # give npc dialouge options

    npc_town_guard.dialouge_options_list.append(dialouge_talk)
    npc_town_guard.dialouge_options_list.append(dialouge_gf)
    npc_town_guard.dialouge_options_list.append(dialouge_quest3)

    npc_jenkins.dialouge_options_list.append(dialouge_talk)
    npc_jenkins.dialouge_options_list.append(dialouge_gf)
    npc_jenkins.dialouge_options_list.append(dialouge_give)
    npc_jenkins.dialouge_options_list.append(dialouge_quest1)
    npc_jenkins.dialouge_options_list.append(dialouge_sell)

    npc_john_doe.dialouge_options_list.append(dialouge_talk)
    npc_john_doe.dialouge_options_list.append(dialouge_buy_weapon)
    npc_john_doe.dialouge_options_list.append(dialouge_buy_armor)
    npc_john_doe.dialouge_options_list.append(dialouge_buy_helmet)
    npc_john_doe.dialouge_options_list.append(dialouge_buy_shield)

    npc_jane_doe.dialouge_options_list.append(dialouge_talk)
    npc_jane_doe.dialouge_options_list.append(dialouge_buy_item)
    npc_jane_doe.dialouge_options_list.append(dialouge_quest2)

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
    npc_wizard_jim.dialouge_options_list.append(dialouge_quest5)

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
    npc_doctor.dialouge_options_list.append(dialouge_quest4)

    ####################-NPC COMBAT ENCOUNTERS--#########################

    npc_jenkins.combat_enemy_list.append(imp1)
    npc_town_guard.combat_enemy_list.append(imp1)
    npc_jenkins.combat_enemy_list.append(imp1)
    npc_jenkins.combat_enemy_list.append(imp1)
    npc_cow.combat_enemy_list.append(imp1)
    npc_cow.combat_enemy_list.append(imp1)

    npc_sheep.combat_enemy_list.append(imp1)
    npc_sheep.combat_enemy_list.append(imp2)
    # npc_sheep.combat_enemy_list.append(imp1)

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

    # hobgoblin.spellbook.append(earthblast)
    # hobgoblin.spellbook.append(hydroblast)
    # hobgoblin.spellbook.append(poison)
    # hobgoblin.spellbook.append(snare)
    # hobgoblin.spellbook.append(super_heal)

    # wolf.spellbook.append(str_up_heal_aoe)
    # wolf.spellbook.append(str_up_heal_aoe)

    # ice_wolf.spellbook.append(str_up_aoe)
    # ice_wolf.spellbook.append(str_up_aoe)
    # ice_wolf.spellbook.append(str_up_heal_aoe)
    # ice_wolf.spellbook.append(str_up_heal_aoe)

    # goblin.spellbook.append(prayer)
    # goblin.spellbook.append(burn)

    # giant_moth.spellbook.append(poison)
    # giant_moth.spellbook.append(poison)

    # giant_spider.spellbook.append(poison)
    # giant_spider.spellbook.append(poison)

    # giant_snail.spellbook.append(slime)

    # bandit.spellbook.append(prayer)

    # bandit_warlock.spellbook.append(snare)
    # bandit_warlock.spellbook.append(prayer)
    # bandit_warlock.spellbook.append(earthblast)
    # bandit_warlock.spellbook.append(earthblast)
    # bandit_warlock.spellbook.append(necroblast)

    # bandit_henchman.spellbook.append(burn)
    # bandit_henchman.spellbook.append(fireblast)
    # bandit_henchman.spellbook.append(prayer)

    # legion_soldier.spellbook.append(prayer)

    # legion_spearman.spellbook.append(super_heal)

    # legion_archer.spellbook.append(prayer)
    # legion_archer.spellbook.append(fire_arrow)
    # legion_archer.spellbook.append(fire_arrow)
    # legion_archer.spellbook.append(ice_arrow)
    # legion_archer.spellbook.append(ice_arrow)

    # legion_battle_mage.spellbook.append(holyblast)
    # legion_battle_mage.spellbook.append(holyblast)
    # legion_battle_mage.spellbook.append(prayer)
    # legion_battle_mage.spellbook.append(holyblast)
    # legion_battle_mage.spellbook.append(prayer)
    # legion_battle_mage.spellbook.append(holyblast)
    # legion_battle_mage.spellbook.append(holy_surge)
    # legion_battle_mage.spellbook.append(super_heal)
    # legion_battle_mage.spellbook.append(holy_surge)
    # legion_battle_mage.spellbook.append(super_heal)
    # legion_battle_mage.spellbook.append(holy_surge)
    # legion_battle_mage.spellbook.append(super_heal)
    # legion_battle_mage.spellbook.append(holy_surge)

    # fire_elemental.spellbook.append(fireblast)
    # fire_elemental.spellbook.append(fireblast)
    # fire_elemental.spellbook.append(fireblast)
    # fire_elemental.spellbook.append(burn)
    # fire_elemental.spellbook.append(fireblast)
    # fire_elemental.spellbook.append(fireblast)
    # fire_elemental.spellbook.append(burn)

    # water_elemental.spellbook.append(hydroblast)
    # water_elemental.spellbook.append(hydroblast)
    # water_elemental.spellbook.append(hydroblast)
    # water_elemental.spellbook.append(hydroblast)
    # water_elemental.spellbook.append(hydroblast)
    # water_elemental.spellbook.append(hydroblast)
    # water_elemental.spellbook.append(hydroblast)

    # earth_elemental.spellbook.append(earthblast)
    # earth_elemental.spellbook.append(earthblast)
    # earth_elemental.spellbook.append(earthblast)
    # earth_elemental.spellbook.append(earthblast)
    # earth_elemental.spellbook.append(earthblast)
    # earth_elemental.spellbook.append(earthblast)
    # earth_elemental.spellbook.append(earthblast)
    # earth_elemental.spellbook.append(earthblast)

    # air_elemental.spellbook.append(windblast)
    # air_elemental.spellbook.append(windblast)
    # air_elemental.spellbook.append(windblast)
    # air_elemental.spellbook.append(windblast)
    # air_elemental.spellbook.append(windblast)
    # air_elemental.spellbook.append(windblast)
    # air_elemental.spellbook.append(windblast)
    # air_elemental.spellbook.append(windblast)

    # skeleton_mage.spellbook.append(fireblast)
    # skeleton_mage.spellbook.append(burn)
    # skeleton_mage.spellbook.append(fireball)
    # skeleton_mage.spellbook.append(life_drain)
    # skeleton_mage.spellbook.append(fireball)
    # skeleton_mage.spellbook.append(life_drain)
    # skeleton_mage.spellbook.append(fireball)
    # skeleton_mage.spellbook.append(life_drain)

    # skeleton_warrior.spellbook.append(life_drain)
    # skeleton_warrior.spellbook.append(life_drain)

    # big_slug.spellbook.append(slime)
    # big_slug.spellbook.append(slime)
    # big_slug.spellbook.append(slime)
    # big_slug.spellbook.append(slime)
    # big_slug.spellbook.append(slime)
    # big_slug.spellbook.append(slime)
    # big_slug.spellbook.append(slime)
    # big_slug.spellbook.append(slime)
    # big_slug.spellbook.append(slime)
    # big_slug.spellbook.append(slime)
    # big_slug.spellbook.append(slime)

    for enemy_stats in all_game_enemies:
        for spell in all_game_spells:
            if spell.level >= enemy_stats.level // 2  and spell.level <= enemy_stats.level * 2:
                spell_equip_chance = random.randint(1,2)
                if spell_equip_chance == 1:
                    enemy_stats.spellbook.append(spell)
                    random.shuffle(enemy_stats.spellbook)
        if dev_mode >= 3:
            print("\n\n" + enemy_stats.print_name + " :\n")
            for spell in enemy_stats.spellbook:
                print(spell.print_name + " " + spell.print_attribute)

game_init()
  
#################################------PLACE GROUND_ITEMS IN WORLD------#######################################

#forest_1.scene_inventory.append(ground_oak_key)

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
dead_enemies = []
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

##########--PYGAME--############

sfx_cursor_move = pygame.mixer.Sound('sound/sfx_cursor_move16.wav')
sfx_cursor_select = pygame.mixer.Sound('sound/sfx_cursor_select16.wav')

sfx_player_move = sfx_cursor_move
sfx_player_select = sfx_cursor_select

 ######################

txt_1 = myfont.render('1', True, (0, 0, 0))
txt_2 = myfont.render('2', True, (0, 0, 0))
txt_3 = myfont.render('3', True, (0, 0, 0))
txt_4 = myfont.render('4', True, (0, 0, 0))
txt_5 = myfont.render('5', True, (0, 0, 0))
txt_6 = myfont.render('6', True, (0, 0, 0))
txt_7 = myfont.render('7', True, (0, 0, 0))
txt_8 = myfont.render('8', True, (0, 0, 0))
txt_9 = myfont.render('9', True, (0, 0, 0))
txt_10 = myfont.render('10', True, (0, 0, 0))
txt_11 = myfont.render('11', True, (0, 0, 0))
txt_12 = myfont.render('12', True, (0, 0, 0))
txt_13 = myfont.render('13', True, (0, 0, 0))
txt_14 = myfont.render('14', True, (0, 0, 0))

txt_talk = myfont.render('talk', True, (0, 0, 0))
txt_search = myfont.render('search', True, (0, 0, 0))
txt_inv = myfont.render('inv', True, (0, 0, 0))
txt_items = myfont.render('items', True, (0, 0, 0))
txt_skills = myfont.render('skills', True, (0, 0, 0))
txt_stats = myfont.render('stats', True, (0, 0, 0))
txt_gear = myfont.render('gear', True, (0, 0, 0))
txt_spellbook = myfont.render('spellbook', True, (0, 0, 0))
txt_cast = myfont.render('cast', True, (0, 0, 0))
txt_actions = myfont.render('actions', True, (0, 0, 0))
txt_pickup = myfont.render('pickup', True, (0, 0, 0))
txt_pickupall = myfont.render('pickupall', True, (0, 0, 0))
txt_camp = myfont.render('camp', True, (0, 0, 0))
txt_wait = myfont.render('wait', True, (0, 0, 0))
txt_quit = myfont.render('quit', True, (0, 0, 0))
txt_help = myfont.render('dev menu', True, (0, 0, 0))
txt_drop = myfont.render('drop', True, (0, 0, 0))
txt_quests = myfont.render('quests', True, (0, 0, 0))


txt_items = myfont.render('items', True, (0, 0, 0))
txt_weapons = myfont.render('weapons', True, (0, 0, 0))
txt_armor = myfont.render('armor', True, (0, 0, 0))
txt_helmets = myfont.render('helmets', True, (0, 0, 0))
txt_shields = myfont.render('shields', True, (0, 0, 0))
txt_spells = myfont.render('spells', True, (0, 0, 0))

txt_steal = myfont.render('steal', True, (0, 0, 0))
txt_craft = myfont.render('alchemy', True, (0, 0, 0))
txt_cook = myfont.render('cook', True, (0, 0, 0))
txt_fish = myfont.render('fish', True, (0, 0, 0))
txt_search = myfont.render('search', True, (0, 0, 0))


###################### SPRITES ##############################

spr_player_n = pygame.image.load("sprites/character.png")
spr_player_e = pygame.image.load("sprites/character.png")
spr_player_s = pygame.image.load("sprites/character.png")
spr_player_w = pygame.image.load("sprites/character.png")

spr_player = spr_player_s

spr_chest = None

################################################################

win_map = pygame.display.set_mode((1024,768))

pygame.display.set_caption("Map Screen")

anim_tiles = [] 

grid_x = 0
grid_y = 0

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

##############################--MUSIC / SOUND FUNCTIONS--#################################

def func_choose_music():
    if dev_mode == 0:
        global in_fight
        global music_playing

        music_playing = pygame.mixer.music.get_busy()

        if in_fight == True and music_playing == 0:
            music_battle1 = pygame.mixer.music.load('sound/music_mystical1.wav')

        elif in_fight == False and music_playing == 0:
            music_ow1 = pygame.mixer.music.load('sound/music_overworld1.wav')

        music_playing = pygame.mixer.music.get_busy()

        if music_playing == 0 and toggle_music == 1:
            pygame.mixer.music.play(-1)

##############################--GUI / GRAPHICS FUNCTIONS--#################################

def func_blit_enemy_list(gui_val):
    list_object_number = 0
    for enemy_stats in current_enemies:
        list_object_number += 1
        blit_text = myfont.render(enemy_stats.print_name, True, (0, 0, 0))
        win_map.blit(blit_text,(32+((gui_val-1)*200),(list_object_number*16)))

def func_blit_list(blitted_list,gui_val,is_stackable):
    list_object_number = 0
    for list_object in blitted_list:
        list_object_number += 1
        if is_stackable == True: #if is stackable check for amount
            blit_text = myfont.render(list_object.name + " x " + str(list_object.amount), True, (0, 0, 0))
        else:
            
            blit_text = myfont.render(list_object.name, True, (0, 0, 0))

        win_map.blit(blit_text,(32+((gui_val-1)*200),(list_object_number*16)))

def func_blit_item_list(gui_val):
    list_object_number = 0
    for item in inventory:
        list_object_number += 1

        blit_text = myfont.render(item.name + " x " + str(item.amount), True, (0, 0, 0))

        win_map.blit(blit_text,(32+((gui_val-1)*200),(list_object_number*16)))

def func_blit_npc_item_list(gui_val):
    for npc in current_npc:
        list_object_number = 0
        for item in npc.npc_inventory:
            list_object_number += 1

            blit_text = myfont.render(item.name, True, (0, 0, 0))

            win_map.blit(blit_text,(32+((gui_val-1)*200),(list_object_number*16)))

def func_blit_npc_list(gui_val):
    global nearby_npc_list
    list_object_number = 0
    for npc in nearby_npc_list:
        list_object_number += 1
        blit_text = myfont.render(npc.first_name + " " + npc.last_name, True, (0, 0, 0))
        win_map.blit(blit_text,(32+((gui_val-1)*200),(list_object_number*16)))

def func_blit_dialouge_list(list_object,list,gui_val):
    list_object_number = 0
    for list_object in list:
        list_object_number += 1
        blit_text = myfont.render(list_object.text, True, (0, 0, 0))
        win_map.blit(blit_text,(32+((gui_val-1)*200),(list_object_number*16)))

def func_blit_menu_cursor(gui_val):
    pygame.draw.rect(win_map, (247,255,0), (((14+((gui_val-1)*200), ((menu_cursor_pos)*16)+8, cursor_width, cursor_height))))

def func_blit_tip_text(text):
    text = f" > {text}"
    blit_info = myfont.render(text, True, (0, 0, 0))
    #TODO draw a box around the tool tip text
    win_map.blit(blit_info,(32+((0)*200),(46*16)))

def func_blit_combat_cursor(gui_val):
    pygame.draw.rect(win_map, (247,255,0), (((14+((gui_val-1)*200), ((combat_cursor_pos)*16)+8, cursor_width, cursor_height))))

def func_blit_HUD(hud_val):
    status_list = []
    for status_condition in player1.status_effect_list:
        status_list.append(status_condition.name)
    blit_HUD_name = myfont.render(player1.name, True, (0, 0, 0))
    blit_HUD_lvl = myfont.render("Lvl: " + str(player1.level), True, (0, 0, 0))
    for armor in equiped_armor:
        blit_HUD_att = myfont.render("Att: " + armor.attribute, True, (0, 0, 0))
    blit_HUD_hp = myfont.render("HP: " + str(player1.hp) + "/" + str(player1.maxhp), True, (0, 0, 0))
    blit_HUD_mp = myfont.render("MP: " + str(player1.mp) + "/" + str(player1.maxmp), True, (0, 0, 0))
    blit_HUD_xp = myfont.render("XP: " + str(player1.xp), True, (0, 0, 0))
    blit_HUD_gp = myfont.render("GP: " + str(player1.gp), True, (0, 0, 0))
    if len(player1.status_effect_list) != 0:
        blit_HUD_status = myfont.render("Status: " + str(status_list), True, (0, 0, 0))
    else:
        blit_HUD_status = myfont.render("Status: ['N0NE']", True, (0, 0, 0))

    win_map.blit(blit_HUD_name,(32+((hud_val-1)*200),(33*16)))
    win_map.blit(blit_HUD_lvl,(32+((hud_val-1)*200),(34*16)))
    win_map.blit(blit_HUD_att,(32+((hud_val-1)*200),(35*16)))
    win_map.blit(blit_HUD_hp,(32+((hud_val-1)*200),(36*16)))
    win_map.blit(blit_HUD_mp,(32+((hud_val-1)*200),(37*16)))
    win_map.blit(blit_HUD_status,(32+((hud_val-1)*200),(38*16)))
    win_map.blit(blit_HUD_xp,(32+((hud_val-1)*200),(39*16)))
    win_map.blit(blit_HUD_gp,(32+((hud_val-1)*200),(40*16)))

def func_blit_player_stats(hud_val):

    global days
    global months
    global years
    global season
    menu_season = "0"

    if season == 0:
        menu_season = "Summer"
    if season == 1:
        menu_season = "Autumn"
    if season == 2:
        menu_season = "Winter"
    if season == 3:
        menu_season = "Spring"

    blit_menu_name = myfont.render(player1.name, True, (0, 0, 0))
    blit_menu_lvl = myfont.render("Lvl: " + str(player1.level), True, (0, 0, 0))
    for armor in equiped_armor:
        blit_menu_att = myfont.render("Att: " + armor.attribute, True, (0, 0, 0))
    blit_menu_hp = myfont.render("Hp: " + str(player1.hp) + "/" + str(player1.maxhp), True, (0, 0, 0))
    blit_menu_mp = myfont.render("Mp: " + str(player1.mp) + "/" + str(player1.maxmp), True, (0, 0, 0))
    blit_menu_xp = myfont.render("Xp: " + str(player1.xp), True, (0, 0, 0))
    blit_menu_gp = myfont.render("Gp: " + str(player1.gp), True, (0, 0, 0))

    blit_menu_attack = myfont.render("Atk: " + str(player1.attack), True, (0, 0, 0))
    blit_menu_defence = myfont.render("Def: " + str(player1.defence), True, (0, 0, 0))
    blit_menu_strength = myfont.render("Str: " + str(player1.strength), True, (0, 0, 0))
    blit_menu_magic = myfont.render("Mgk: " + str(player1.magic), True, (0, 0, 0))

    blit_menu_thieving = myfont.render("Thieving: " + str(player1_skills.thieving), True, (0, 0, 0))
    blit_menu_fishing = myfont.render("Fishing: " + str(player1_skills.fishing), True, (0, 0, 0))
    blit_menu_cooking = myfont.render("Cooking: " + str(player1_skills.cooking), True, (0, 0, 0))
    blit_menu_alchemy = myfont.render("Alchemy: " + str(player1_skills.alchemy), True, (0, 0, 0))

    blit_menu_date = myfont.render("date:  " + str(days) + "." + str(months) + "." + str(years), True, (0, 0, 0))
    blit_menu_season = myfont.render(menu_season, True, (0, 0, 0))


    win_map.blit(blit_menu_name,(32+((hud_val-1)*200),(1*16)))
    win_map.blit(blit_menu_lvl,(32+((hud_val-1)*200),(2*16)))
    win_map.blit(blit_menu_att,(32+((hud_val-1)*200),(3*16)))
    win_map.blit(blit_menu_hp,(32+((hud_val-1)*200),(4*16)))
    win_map.blit(blit_menu_mp,(32+((hud_val-1)*200),(5*16)))
    win_map.blit(blit_menu_xp,(32+((hud_val-1)*200),(6*16)))
    win_map.blit(blit_menu_gp,(32+((hud_val-1)*200),(7*16)))

    win_map.blit(blit_menu_attack,(32+((hud_val-1)*200),(9*16)))
    win_map.blit(blit_menu_defence,(32+((hud_val-1)*200),(10*16)))
    win_map.blit(blit_menu_strength,(32+((hud_val-1)*200),(11*16)))
    win_map.blit(blit_menu_magic,(32+((hud_val-1)*200),(12*16)))

    win_map.blit(blit_menu_thieving,(32+((hud_val-1)*200),(14*16)))
    win_map.blit(blit_menu_fishing,(32+((hud_val-1)*200),(15*16)))
    win_map.blit(blit_menu_cooking,(32+((hud_val-1)*200),(16*16)))
    win_map.blit(blit_menu_alchemy,(32+((hud_val-1)*200),(17*16)))

    win_map.blit(blit_menu_date,(32+((hud_val-1)*200),(20*16)))
    win_map.blit(blit_menu_season,(32+((hud_val-1)*200),(21*16)))

def func_blit_player_gear(hud_val):

    if len(equiped_weapon) != 0:
        for weapon in equiped_weapon:
            blit_weapon_name = myfont.render(weapon.name, True, (0, 0, 0))
            blit_weapon_lvl = myfont.render("Lvl: " + str(weapon.level), True, (0, 0, 0))
            blit_weapon_type = myfont.render("Type: " + str(weapon.type), True, (0, 0, 0))
            blit_weapon_attribute = myfont.render("Att. ", True, (0, 0, 0))

            blit_weapon_attack = myfont.render("Atk: " + str(weapon.attack_bonus), True, (0, 0, 0))
            blit_weapon_defence = myfont.render("Def: " + str(weapon.defence_bonus), True, (0, 0, 0))
            blit_weapon_strength = myfont.render("Str: " + str(weapon.strength_bonus), True, (0, 0, 0))
            blit_weapon_magic = myfont.render("Mgk: " + str(weapon.magic_bonus), True, (0, 0, 0))
            blit_weapon_hp = myfont.render("Hp: " + str(weapon.maxhp_bonus), True, (0, 0, 0))

        win_map.blit(blit_weapon_name,(32+((hud_val-1)*200),(1*16)))
        win_map.blit(blit_weapon_lvl,(32+((hud_val-1)*200),(2*16)))
        win_map.blit(blit_weapon_type,(32+((hud_val-1)*200),(3*16)))
        win_map.blit(blit_weapon_attribute,(32+((hud_val-1)*200),(4*16)))
        win_map.blit(weapon.attribute_sprite, ( (68+((hud_val-1)*200),(4*16)+4)) )

        win_map.blit(blit_weapon_attack,(32+((hud_val-1)*200),(5*16)))
        win_map.blit(blit_weapon_defence,(32+((hud_val-1)*200),(6*16)))
        win_map.blit(blit_weapon_strength,(32+((hud_val-1)*200),(7*16)))
        win_map.blit(blit_weapon_magic,(32+((hud_val-1)*200),(8*16)))
        win_map.blit(blit_weapon_hp,(32+((hud_val-1)*200),(9*16)))
    else:
            blit_weapon_none = myfont.render("[ no weapon ]", True, (0, 0, 0))
            win_map.blit(blit_weapon_none,(32+((hud_val-1)*200),(1*16)))

    if len(equiped_armor) != 0:
        for armor in equiped_armor:
            blit_armor_name = myfont.render(armor.name, True, (0, 0, 0))
            blit_armor_lvl = myfont.render("Lvl: " + str(armor.level), True, (0, 0, 0))
            blit_armor_type = myfont.render("Type: " + str(armor.type), True, (0, 0, 0))
            blit_armor_attribute = myfont.render("Att. ", True, (0, 0, 0))


            blit_armor_attack = myfont.render("Atk: " + str(armor.attack_bonus), True, (0, 0, 0))
            blit_armor_defence = myfont.render("Def: " + str(armor.defence_bonus), True, (0, 0, 0))
            blit_armor_strength = myfont.render("Str: " + str(armor.strength_bonus), True, (0, 0, 0))
            blit_armor_magic = myfont.render("Mgk: " + str(armor.magic_bonus), True, (0, 0, 0))
            blit_armor_hp = myfont.render("Hp: " + str(armor.maxhp_bonus), True, (0, 0, 0))

        win_map.blit(blit_armor_name,(32+((hud_val-1)*200),(11*16)))
        win_map.blit(blit_armor_lvl,(32+((hud_val-1)*200),(12*16)))
        win_map.blit(blit_armor_type,(32+((hud_val-1)*200),(13*16)))
        win_map.blit(blit_armor_attribute,(32+((hud_val-1)*200),(14*16)))
        win_map.blit(armor.attribute_sprite, ( (68+((hud_val-1)*200),(14*16)+4)) )

        win_map.blit(blit_armor_attack,(32+((hud_val-1)*200),(15*16)))
        win_map.blit(blit_armor_defence,(32+((hud_val-1)*200),(16*16)))
        win_map.blit(blit_armor_strength,(32+((hud_val-1)*200),(17*16)))
        win_map.blit(blit_armor_magic,(32+((hud_val-1)*200),(18*16)))
        win_map.blit(blit_armor_hp,(32+((hud_val-1)*200),(19*16)))
    else:
            blit_armor_none = myfont.render("[ no armor ]", True, (0, 0, 0))
            win_map.blit(blit_armor_none,(32+((hud_val-1)*200),(11*16)))

def func_blit_player_gear2(hud_val):

    if len(equiped_helmet) != 0:
        for helmet in equiped_helmet:
            blit_helmet_name = myfont.render(helmet.name, True, (0, 0, 0))
            blit_helmet_lvl = myfont.render("Lvl: " + str(helmet.level), True, (0, 0, 0))
            blit_helmet_type = myfont.render("Type: " + str(helmet.type), True, (0, 0, 0))
            blit_helmet_attribute = myfont.render("Att. ", True, (0, 0, 0))

            blit_helmet_attack = myfont.render("Atk: " + str(helmet.attack_bonus), True, (0, 0, 0))
            blit_helmet_defence = myfont.render("Def: " + str(helmet.defence_bonus), True, (0, 0, 0))
            blit_helmet_strength = myfont.render("Str: " + str(helmet.strength_bonus), True, (0, 0, 0))
            blit_helmet_magic = myfont.render("Mgk: " + str(helmet.magic_bonus), True, (0, 0, 0))
            blit_helmet_hp = myfont.render("Hp: " + str(helmet.maxhp_bonus), True, (0, 0, 0))

        win_map.blit(blit_helmet_name,(32+((hud_val-1)*200),(1*16)))
        win_map.blit(blit_helmet_lvl,(32+((hud_val-1)*200),(2*16)))
        win_map.blit(blit_helmet_type,(32+((hud_val-1)*200),(3*16)))
        win_map.blit(blit_helmet_attribute,(32+((hud_val-1)*200),(4*16)))
        win_map.blit(helmet.attribute_sprite, ( (68+((hud_val-1)*200),(4*16)+4)) )

        win_map.blit(blit_helmet_attack,(32+((hud_val-1)*200),(5*16)))
        win_map.blit(blit_helmet_defence,(32+((hud_val-1)*200),(6*16)))
        win_map.blit(blit_helmet_strength,(32+((hud_val-1)*200),(7*16)))
        win_map.blit(blit_helmet_magic,(32+((hud_val-1)*200),(8*16)))
        win_map.blit(blit_helmet_hp,(32+((hud_val-1)*200),(9*16)))
    else:
            blit_helmet_none = myfont.render("[ no helmet ]", True, (0, 0, 0))
            win_map.blit(blit_helmet_none,(32+((hud_val-1)*200),(1*16)))

    if len(equiped_shield) != 0:
        for shield in equiped_shield:
            blit_shield_name = myfont.render(shield.name, True, (0, 0, 0))
            blit_shield_lvl = myfont.render("Lvl: " + str(shield.level), True, (0, 0, 0))
            blit_shield_type = myfont.render("Type: " + str(shield.type), True, (0, 0, 0))
            blit_shield_attribute = myfont.render("Att. ", True, (0, 0, 0))
            win_map.blit(shield.attribute_sprite, ( (68+((hud_val-1)*200),(14*16)+4)) )

            blit_shield_attack = myfont.render("Atk: " + str(shield.attack_bonus), True, (0, 0, 0))
            blit_shield_defence = myfont.render("Def: " + str(shield.defence_bonus), True, (0, 0, 0))
            blit_shield_strength = myfont.render("Str: " + str(shield.strength_bonus), True, (0, 0, 0))
            blit_shield_magic = myfont.render("Mgk: " + str(shield.magic_bonus), True, (0, 0, 0))
            blit_shield_hp = myfont.render("Hp: " + str(shield.maxhp_bonus), True, (0, 0, 0))

        win_map.blit(blit_shield_name,(32+((hud_val-1)*200),(11*16)))
        win_map.blit(blit_shield_lvl,(32+((hud_val-1)*200),(12*16)))
        win_map.blit(blit_shield_type,(32+((hud_val-1)*200),(13*16)))
        win_map.blit(blit_shield_attribute,(32+((hud_val-1)*200),(14*16)))

        win_map.blit(blit_shield_attack,(32+((hud_val-1)*200),(15*16)))
        win_map.blit(blit_shield_defence,(32+((hud_val-1)*200),(16*16)))
        win_map.blit(blit_shield_strength,(32+((hud_val-1)*200),(17*16)))
        win_map.blit(blit_shield_magic,(32+((hud_val-1)*200),(18*16)))
        win_map.blit(blit_shield_hp,(32+((hud_val-1)*200),(19*16)))
    else:
            blit_shield_none = myfont.render("[ no shield ]", False, (0, 0, 0))
            win_map.blit(blit_shield_none,(32+((hud_val-1)*200),(11*16)))

def func_blit_player_damage(hud_val,hud_val_damage,damage):
    blit_player_damage = myfont.render(str(damage), True, (244, 0, 0))
    if blit_player_damage_amount > 0:
        win_map.blit(blit_player_damage,(32+((hud_val-1)*200),(hud_val_damage*16)))

def func_blit_enemy_HUD(hud_val):
    enemy_number = 0
    for enemy_stats in current_enemies:
        enemy_number += 1
        status_list = []
        for status_condition in enemy_stats.status_effect_list:
            status_list.append(status_condition.name)

        blit_HUD_active = myfont.render("ACTIVE", True, (150, 50, 0))
        blit_HUD_inactive = myfont.render("ACTIVE", True, (10, 10, 10))
        blit_HUD_name = myfont.render(enemy_stats.print_name, True, (0, 0, 0))
        blit_HUD_lvl = myfont.render("Lvl: " + str(enemy_stats.level), True, (0, 0, 0))
        blit_HUD_att = myfont.render("Att: " + enemy_stats.attribute, True, (0, 0, 0))
        blit_HUD_hp = myfont.render("HP: " + str(enemy_stats.hp) + "/" + str(enemy_stats.maxhp), True, (0, 0, 0))
        blit_HUD_mp = myfont.render("MP: " + str(enemy_stats.mp) + "/" + str(enemy_stats.maxmp), True, (0, 0, 0))
        if len(enemy_stats.status_effect_list) != 0:
            blit_HUD_status = myfont.render("Status: " + str(status_list), True, (0, 0, 0))
        else:
            blit_HUD_status = myfont.render("Status: ['N0NE']", True, (0, 0, 0))

        win_map.blit(blit_HUD_name,(32+((hud_val+enemy_number-1)*200),(33*16)))
        win_map.blit(blit_HUD_lvl,(32+((hud_val+enemy_number-1)*200),(34*16)))
        win_map.blit(blit_HUD_att,(32+((hud_val+enemy_number-1)*200),(35*16)))
        win_map.blit(blit_HUD_hp,(32+((hud_val+enemy_number-1)*200),(36*16)))
        win_map.blit(blit_HUD_mp,(32+((hud_val+enemy_number-1)*200),(37*16)))
        win_map.blit(blit_HUD_status,(32+((hud_val+enemy_number-1)*200),(38*16)))
        win_map.blit(enemy_stats.enemy_sprite, ( ((cx-256) + ((enemy_number+1)*128)), ((cy) + ((1)*32)) ) )
        if enemy_stats.is_active == True:

            win_map.blit(blit_HUD_active,(32+((hud_val+enemy_number-1)*200),(32*16)))
            pygame.draw.rect(win_map, (125,100,0), ( ((cx-256) + ((enemy_number+1)*128)),((cy-100) + ((1)*32)), 16, 16 ) )
        if enemy_stats.is_active == False:
            win_map.blit(blit_HUD_inactive,(32+((hud_val+enemy_number-1)*200),(32*16)))
            pygame.draw.rect(win_map, (100,100,100), ( ((cx-256) + ((enemy_number+1)*128)),((cy-100) + ((1)*32)), 16, 16 ) )

        if in_submenu_target_combat2 == True and enemy_number == combat_cursor_pos:
            pygame.draw.rect(win_map, (255,0,0), ( ((cx-256) + ((enemy_number+1)*128)),((cy-100) + ((1)*32)), 16, 16 ) )

def func_blit_title(title_string,gui_val):
    blit_title = myfont.render(title_string, True, (0, 0, 0))
    pygame.draw.rect(win_map, (100,100,100), (32+((gui_val-1)*200), 0, 136, 16))
    win_map.blit(blit_title,(32+((gui_val-1)*200),0))

def func_blit_grid_coords():
    global grid_x
    global grid_y
    global grid_mode
    if grid_mode >= 1:
        grid_x = -30
        grid_y = -30
        while grid_x < 30 and grid_y < 30:
            if grid_x < 30:
                c1 = 100+(grid_x*5)
                if c1 >= 255:
                    c1 = 255
                if c1 <= 1:
                    c1 = 1
                c2 = 100+(grid_y*5)
                if c2 >= 255:
                    c2 = 255
                if c2 <= 1:
                    c2 = 1
                c3 = 61 + grid_x + grid_y
                if c3 >= 255:
                    c3 = 255
                if c3 <= 1:
                    c3 = 1

                grid_rgb = ( c1, c2, c3)
                pygame.draw.rect(win_map, grid_rgb, ( ((cx-16) + ((grid_x - steps_x)*(32))), ((cy-16) + ((grid_y - steps_y)*(32))), map_tile_width, (map_tile_height//2) - 3))
                blit_grid_coords = gridfont.render(str(grid_x) + "," + str(grid_y), True, (0, 0, 0))
                win_map.blit(blit_grid_coords, ( ((cx-16) + ((grid_x - steps_x)*(32))), ((cy-16) + ((grid_y - steps_y)*(32))) )  )
                grid_x += 1
            if grid_x == 30:
                grid_x = -30
                grid_y +=1
                if grid_y >= 30:
                    break

##############################--MAIN GRAPHICS FUNCTION--################################
########################################################################################

def func_check_tile_anims():

    #needs to be called whenever tilemap changes

    for layer in tmx_data: #blit the map from the tmx file
        #[0] = x pos of tile, [1] y pos of tile, [2] = tile image
        for x,y,tile in layer.tiles(): # for every tile
            for gid, props in tmx_data.tile_properties.items(): 
                try:
                    if tile == tmx_data.get_tile_image_by_gid(props['frames'][0].gid): 
                    #if props['frames'] and (gid,props) not in anim_tiles:
                        anim_tiles.append((gid,props))
                except:
                    pass

    if dev_mode >= 3:         
        for x in anim_tiles:
            print(x)

def func_refresh_pygame(battle_intro, animation):
    global current_anim_index
    global frames

    func_choose_music()

    battle_intro_ticks = 0
    if dev_mode >= 6:
        print("\nrefreshing pygame window // \n")

    if steps_z <= 0:
        win_map.fill((77,101,180)) #blue if on surface
    else:
        win_map.fill((15,15,15)) #black if underground

    layercount = 0
    for layer in tmx_data: #blit the map from the tmx file
        layercount +=1
        if layercount == 6:#???? tiled counts deleted layers think? 
            win_map.blit(spr_player,(cx-16, cy-16-32,))
            #tile is a list
            #[0] = x pos of tile, [1] y pos of tile, [2] = tile image
        for x,y,tile in layer.tiles(): #tile is a pygame surface
            view_distance_v,view_distance_h = 17,9 #16,8 
            if (x < steps_x + view_distance_v and  x > steps_x - view_distance_v) and (y < steps_y + view_distance_h and  y > steps_y - view_distance_h):
                if layercount >= 4: #if on layers which contain animations
                    for gid, props in anim_tiles:
                        if tile == tmx_data.get_tile_image_by_gid(props['frames'][0].gid): 
                            tile = tmx_data.get_tile_image_by_gid(props['frames'][current_anim_index].gid)
                            win_map.blit(tile, ( ((cx-16) + ((x - steps_x)*32)), ((cy-16) + ((y- steps_y)*32)) )  )
                        else:
                            win_map.blit(tile, ( ((cx-16) + ((x - steps_x)*32)), ((cy-16) + ((y- steps_y)*32)) )  )
 
                else:                
                    win_map.blit(tile, ( ((cx-16) + ((x - steps_x)*32)), ((cy-16) + ((y- steps_y)*32)) )  )                            
                        
    func_blit_grid_coords()

    if battle_intro == True:
        pygame.mixer.music.stop()
        battle_intro_ticks = 0

    while battle_intro == True:
        pygame.mixer.music.stop()
        pygame.time.delay(tick_delay_time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
                battle_intro = False
                break

        while battle_intro_ticks < 18:
            pygame.time.delay(tick_delay_time)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_start = 0
                    battle_intro_ticks = 18
                    break
            for scene_type in all_scene_types:
                if scene_type.zpos == steps_z:
                    tile_r = 100
                    tile_g = 100
                    tile_b = 100

                    pygame.draw.rect(win_map, (tile_r,tile_g,tile_b), ( ((cx-16) + ((scene_type.xpos - steps_x)*32*random.randint(1,3))), ((cy-16) + ((scene_type.ypos - steps_y)*(32*random.randint(1,3)))), map_tile_width, map_tile_height))

            battle_intro_ticks += 1
            pygame.display.update()
            print("ENTERING COMBAT")

        if battle_intro_ticks >= 18:
            battle_intro = False
            break

    
    #draws bottom hud box
    pygame.draw.rect(win_map, (100,100,100), (0, 512, 1024, 256))
    pygame.draw.rect(win_map, (125,125,125), (10,522, 1004, 236))

    func_blit_HUD(1)
    func_blit_enemy_HUD(1)

    if in_fight == True:

        win_map.fill((20,20,20))
        pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
        pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

        func_blit_list(combat_option_list,1,False)
        func_blit_combat_cursor(1)
        func_blit_title("Battle:",1)


        if in_submenu_cast_combat == True:

            pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

            func_blit_list(equiped_spells,1,False)

            func_blit_combat_cursor(1)
            func_blit_title("Cast:",1)


        if in_submenu_use_combat == True:

            pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

            func_blit_list(inventory,1,True)

            func_blit_combat_cursor(1)
            func_blit_title("Use item:",1)

        if in_submenu_target_combat2 == True:

            pygame.draw.rect(win_map, (100,100,100), (0, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (10,10, 180, 480))

            func_blit_list(combat_option_list,1,False)
            func_blit_title("Battle:",1)

            pygame.draw.rect(win_map, (100,100,100), (200, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (210,10, 180, 480))


            func_blit_enemy_list(2)

            func_blit_combat_cursor(2)
            func_blit_title("Target:",2)

        #draws bottom hud box
        pygame.draw.rect(win_map, (100,100,100), (0, 512, 1024, 256))
        pygame.draw.rect(win_map, (125,125,125), (10,522, 1004, 236))
        func_blit_HUD(1)
        func_blit_enemy_HUD(1)

    if current_menu:
        #bg
        pygame.draw.rect(win_map, (80,100,100), (0, 0, 1024, 512))

        #panel 1
        pygame.draw.rect(win_map, (100,100,100), (14, 0, 200, 500))
        pygame.draw.rect(win_map, (125,125,125), (24, 10, 180, 480))
        
        #panel 2
        pygame.draw.rect(win_map, (100,100,100), (214, 0, 200, 500))
        pygame.draw.rect(win_map, (125,125,125), (224,10, 180, 480))
        
        #panel 3
        pygame.draw.rect(win_map, (100,100,100), (414, 0, 200, 500))
        pygame.draw.rect(win_map, (125,125,125), (424,10, 180, 480))

        #panel 4
        pygame.draw.rect(win_map, (100,100,100), (614, 0, 200, 500))
        pygame.draw.rect(win_map, (125,125,125), (624,10, 180, 480))

        #panel 5
        pygame.draw.rect(win_map, (100,100,100), (814, 0, 200, 500))
        pygame.draw.rect(win_map, (125,125,125), (824,10, 180, 480))

        func_blit_player_stats(2)
        func_blit_player_gear(3)
        func_blit_player_gear2(4)
        func_blit_list(equiped_spells,5,False)

        func_blit_menu_cursor(1) 

        if current_menu.children:# if menu is a node print children
            func_blit_list(current_menu.children,1,False) 
        else:# if menu is a leaf print leaf data
            if current_menu.stackable_data:
                func_blit_list(current_menu.data,1,True)
            else:
                func_blit_list(current_menu.data,1,False)

    if in_menu == True and in_submenu == False and False:

        pygame.draw.rect(win_map, (80,100,100), (0, 0, 1024, 512))

        win_map.blit(txt_skills,(32,(1*16)))
        win_map.blit(txt_items,(32,(2*16)))
        win_map.blit(txt_cast,(32,(3*16)))
        win_map.blit(txt_equip,(32,(4*16)))
        win_map.blit(txt_spellbook,(32,(5*16))) #useless now that info is displayed in menu
        win_map.blit(txt_quests,(32,(6*16)))
        win_map.blit(txt_drop,(32,(7*16)))

        win_map.blit(txt_quit,(32,(18*16)))

        func_blit_menu_cursor(1)

        if menu_cursor_pos == 1:
            func_blit_tip_text("perform actions using your skills")
        elif menu_cursor_pos == 2:
            func_blit_tip_text("use your items")
        elif menu_cursor_pos == 3:
            func_blit_tip_text("cast a spell")
        elif menu_cursor_pos == 4:
            func_blit_tip_text("equip spells, weapons and other equipment")
        elif menu_cursor_pos == 5:
            func_blit_tip_text("check you current spellbook")
        elif menu_cursor_pos == 6:
            func_blit_tip_text("view quests")
        elif menu_cursor_pos == 7:
            func_blit_tip_text("drop an item from your inventory")
        elif menu_cursor_pos == 12:
            func_blit_tip_text("quit the game")
        else:
            func_blit_tip_text("menu")

    if in_menu == True and in_submenu == True and False:

        pygame.draw.rect(win_map, (80,100,100), (0, 0, 1024, 512))

        if in_submenu_action == True:

            pygame.draw.rect(win_map, (100,100,100), (14, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (24, 10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (214, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (224,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (414, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (424,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (614, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (624,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (814, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (824,10, 180, 480))

            win_map.blit(txt_steal,(32,(1*16)))
            win_map.blit(txt_fish,(32,(2*16)))
            win_map.blit(txt_cook,(32,(3*16)))
            win_map.blit(txt_craft,(32,(4*16)))
            win_map.blit(txt_search,(32,(5*16)))

            func_blit_menu_cursor(1)
            func_blit_title("Action:",1)

            if menu_cursor_pos == 1:
                func_blit_tip_text("steal an item")
            elif menu_cursor_pos == 2:
                func_blit_tip_text("fish for something")
            elif menu_cursor_pos == 3:
                func_blit_tip_text("cook raw food")
            elif menu_cursor_pos == 4:
                func_blit_tip_text("craft an item")
            elif menu_cursor_pos == 5:
                func_blit_tip_text("search the area for valuables")

            if in_submenu_cook2 == True:

                pygame.draw.rect(win_map, (100,100,100), (14, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (24, 10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (214, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (224,10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (414, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (424,10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (614, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (624,10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (814, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (824,10, 180, 480))

                func_blit_list(inventory,2,True)

                func_blit_menu_cursor(2)
                func_blit_title("Cook:",2)

        if in_submenu_use == True:

            pygame.draw.rect(win_map, (100,100,100), (14, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (24, 10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (214, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (224,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (414, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (424,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (614, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (624,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (814, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (824,10, 180, 480))

            func_blit_item_list(1)
            
            func_blit_tip_text(inventory[menu_cursor_pos-1].item_desc)
            

            func_blit_menu_cursor(1)
            func_blit_title("Use:",1)

        if in_submenu_questlog == True:

            pygame.draw.rect(win_map, (100,100,100), (14, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (24, 10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (214, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (224,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (414, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (424,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (614, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (624,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (814, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (824,10, 180, 480))

            func_blit_list(quest_list,1,False)
            func_blit_menu_cursor(1)
            func_blit_title("Quests:",1)

            func_blit_tip_text(quest_list[menu_cursor_pos-1].quest_desc)

        if in_submenu_cast == True:

            pygame.draw.rect(win_map, (100,100,100), (14, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (24, 10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (214, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (224,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (414, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (424,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (614, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (624,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (814, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (824,10, 180, 480))

            func_blit_list(equiped_spells,1,False)
            func_blit_menu_cursor(1)
            func_blit_tip_text(equiped_spells[menu_cursor_pos-1].spell_desc)

        if in_submenu_equip == True:

            pygame.draw.rect(win_map, (100,100,100), (14, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (24, 10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (214, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (224,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (414, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (424,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (614, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (624,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (814, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (824,10, 180, 480))

            win_map.blit(txt_weapons,(32,(1*16)))
            win_map.blit(txt_armor,(32,(2*16)))
            win_map.blit(txt_helmets,(32,(3*16)))
            win_map.blit(txt_shields,(32,(4*16)))
            win_map.blit(txt_spells,(32,(5*16)))

            func_blit_menu_cursor(1)
            func_blit_title("Equip:",1)

            if in_submenu_equip2 == False:
                if menu_cursor_pos == 1:
                    func_blit_tip_text("Equip a weapon from your inventory.")
                elif menu_cursor_pos == 2:
                    func_blit_tip_text("Equip some armor from your inventory.")
                elif menu_cursor_pos == 3:
                    func_blit_tip_text("Equip a helmet from your inventory.")
                elif menu_cursor_pos == 4:
                    func_blit_tip_text("Equip a shield from your inventory.")
                elif menu_cursor_pos == 5:
                    func_blit_tip_text("Equip spells from scrolls in your inventory.")

            if in_submenu_equip2 == True:
            
                pygame.draw.rect(win_map, (100,100,100), (14, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (24, 10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (214, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (224,10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (414, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (424,10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (614, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (624,10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (814, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (824,10, 180, 480))

                if in_menu_weapon == True:
                    if weapon_inventory:
                        func_blit_list(weapon_inventory,2,True)
                        tool_tip_item = weapon_inventory[menu_cursor_pos-1]
                        func_blit_tip_text(f"{tool_tip_item.name} - lvl. {tool_tip_item.level} - {tool_tip_item.attribute} | ATK:{tool_tip_item.attack_bonus} STR: {tool_tip_item.strength_bonus} DEF: {tool_tip_item.defence_bonus} MGK:{tool_tip_item.magic_bonus} HP: {tool_tip_item.maxhp_bonus}")
                
                if in_menu_armor == True:
                    if armor_inventory:
                        func_blit_list(armor_inventory,2,True)
                        tool_tip_item = armor_inventory[menu_cursor_pos-1]
                        func_blit_tip_text(f"{tool_tip_item.name} - lvl. {tool_tip_item.level} - {tool_tip_item.attribute} | ATK:{tool_tip_item.attack_bonus} STR: {tool_tip_item.strength_bonus} DEF: {tool_tip_item.defence_bonus} MGK:{tool_tip_item.magic_bonus} HP: {tool_tip_item.maxhp_bonus}")
                
                if in_menu_helmet == True:
                    if helmet_inventory:
                        func_blit_list(helmet_inventory,2,True)
                        tool_tip_item = helmet_inventory[menu_cursor_pos-1]
                        func_blit_tip_text(f"{tool_tip_item.name} - lvl. {tool_tip_item.level} - {tool_tip_item.attribute} | ATK:{tool_tip_item.attack_bonus} STR: {tool_tip_item.strength_bonus} DEF: {tool_tip_item.defence_bonus} MGK:{tool_tip_item.magic_bonus} HP: {tool_tip_item.maxhp_bonus}")
                
                if in_menu_shield == True:
                    #print(shield_inventory)
                    if shield_inventory:
                        func_blit_list(shield_inventory,2,True)
                        print(menu_cursor_pos)
                        tool_tip_item = shield_inventory[menu_cursor_pos-1]
                        func_blit_tip_text(f"{tool_tip_item.name} - lvl. {tool_tip_item.level} - {tool_tip_item.attribute} | ATK:{tool_tip_item.attack_bonus} STR: {tool_tip_item.strength_bonus} DEF: {tool_tip_item.defence_bonus} MGK:{tool_tip_item.magic_bonus} HP: {tool_tip_item.maxhp_bonus}")
                
                if in_menu_spell == True:
                    if spell_inventory:
                        func_blit_list(spell_inventory,2,True)
                        tool_tip_item = spell_inventory[menu_cursor_pos-1]
                        func_blit_tip_text(f"{tool_tip_item.name} - lvl. {tool_tip_item.level} - {tool_tip_item.attribute} | {tool_tip_item.spell_desc}")
                

                func_blit_menu_cursor(2)
                func_blit_title("Equip:",2)

        if in_submenu_talk == True:

            pygame.draw.rect(win_map, (100,100,100), (14, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (24, 10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (214, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (224,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (414, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (424,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (614, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (624,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (814, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (824,10, 180, 480))


            func_blit_npc_list(1)




            func_blit_menu_cursor(1)
            func_blit_title("Talk:",1)

            if in_submenu_talk2 == True:

                pygame.draw.rect(win_map, (100,100,100), (14, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (24, 10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (214, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (224,10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (414, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (424,10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (614, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (624,10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (814, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (824,10, 180, 480))
                for npc in current_npc:
                    func_blit_dialouge_list(dialouge_option,npc.dialouge_options_list,2)

                func_blit_menu_cursor(2)
                func_blit_title("Talk:",2)

                if in_submenu_sell3 == True:

                    pygame.draw.rect(win_map, (100,100,100), (14, 0, 200, 500))
                    pygame.draw.rect(win_map, (125,125,125), (24, 10, 180, 480))

                    pygame.draw.rect(win_map, (100,100,100), (214, 0, 200, 500))
                    pygame.draw.rect(win_map, (125,125,125), (224,10, 180, 480))

                    pygame.draw.rect(win_map, (100,100,100), (414, 0, 200, 500))
                    pygame.draw.rect(win_map, (125,125,125), (424,10, 180, 480))

                    pygame.draw.rect(win_map, (100,100,100), (614, 0, 200, 500))
                    pygame.draw.rect(win_map, (125,125,125), (624,10, 180, 480))

                    pygame.draw.rect(win_map, (100,100,100), (814, 0, 200, 500))
                    pygame.draw.rect(win_map, (125,125,125), (824,10, 180, 480))

                    win_map.blit(txt_items,(432,(1*16)))
                    win_map.blit(txt_weapons,(432,(2*16)))
                    win_map.blit(txt_armor,(432,(3*16)))
                    win_map.blit(txt_helmets,(432,(4*16)))
                    win_map.blit(txt_shields,(432,(5*16)))
                    win_map.blit(txt_spells,(432,(6*16)))


                    func_blit_menu_cursor(3)
                    func_blit_title("Sell 3:",3)

                    if in_submenu_sell4== True:

                        pygame.draw.rect(win_map, (100,100,100), (14, 0, 200, 500))
                        pygame.draw.rect(win_map, (125,125,125), (24, 10, 180, 480))

                        pygame.draw.rect(win_map, (100,100,100), (214, 0, 200, 500))
                        pygame.draw.rect(win_map, (125,125,125), (224,10, 180, 480))

                        pygame.draw.rect(win_map, (100,100,100), (414, 0, 200, 500))
                        pygame.draw.rect(win_map, (125,125,125), (424,10, 180, 480))

                        pygame.draw.rect(win_map, (100,100,100), (614, 0, 200, 500))
                        pygame.draw.rect(win_map, (125,125,125), (624,10, 180, 480))

                        pygame.draw.rect(win_map, (100,100,100), (814, 0, 200, 500))
                        pygame.draw.rect(win_map, (125,125,125), (824,10, 180, 480))
                        if in_menu_item == True:
                            if len(inventory) != 0:
                                func_blit_list(inventory,4,True)
                        if in_menu_weapon == True:
                            func_blit_list(weapon_inventory,4,True)
                        if in_menu_armor == True:
                            func_blit_list(armor_inventory,4,True)
                        if in_menu_helmet == True:
                            func_blit_list(helmet_inventory,4,True)
                        if in_menu_shield == True:
                            func_blit_list(shield_inventory,4,True)
                        if in_menu_spell == True:
                            func_blit_list(spell_inventory,4,True)

                        func_blit_menu_cursor(4)
                        func_blit_title("Sell 4:",4)

                if in_submenu_buy3 == True:

                    pygame.draw.rect(win_map, (100,100,100), (14, 0, 200, 500))
                    pygame.draw.rect(win_map, (125,125,125), (24, 10, 180, 480))

                    pygame.draw.rect(win_map, (100,100,100), (214, 0, 200, 500))
                    pygame.draw.rect(win_map, (125,125,125), (224,10, 180, 480))

                    pygame.draw.rect(win_map, (100,100,100), (414, 0, 200, 500))
                    pygame.draw.rect(win_map, (125,125,125), (424,10, 180, 480))

                    pygame.draw.rect(win_map, (100,100,100), (614, 0, 200, 500))
                    pygame.draw.rect(win_map, (125,125,125), (624,10, 180, 480))

                    pygame.draw.rect(win_map, (100,100,100), (814, 0, 200, 500))
                    pygame.draw.rect(win_map, (125,125,125), (824,10, 180, 480))

                    for npc in current_npc:
                        if in_menu_item == True:
                            func_blit_npc_item_list(3)
                        if in_menu_weapon == True:
                            func_blit_list(npc.npc_weapon_inventory,3,False)
                        if in_menu_armor == True:
                            func_blit_list(npc.npc_armor_inventory,3,False)
                        if in_menu_helmet == True:
                            func_blit_list(npc.npc_helmet_inventory,3,False)
                        if in_menu_shield == True:
                            func_blit_list(npc.npc_shield_inventory,3,False)
                        if in_menu_spell == True:
                            func_blit_list(npc.npc_spell_inventory,3,False)

                    func_blit_menu_cursor(3)
                    func_blit_title("Buy 3:",3)
        
        if in_submenu_drop == True:

            pygame.draw.rect(win_map, (100,100,100), (14, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (24, 10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (214, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (224,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (414, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (424,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (614, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (624,10, 180, 480))

            pygame.draw.rect(win_map, (100,100,100), (814, 0, 200, 500))
            pygame.draw.rect(win_map, (125,125,125), (824,10, 180, 480))

            win_map.blit(txt_items,(32,(1*16)))
            win_map.blit(txt_weapons,(32,(2*16)))
            win_map.blit(txt_armor,(32,(3*16)))
            win_map.blit(txt_helmets,(32,(4*16)))
            win_map.blit(txt_shields,(32,(5*16)))
            win_map.blit(txt_spells,(32,(6*16)))


            func_blit_menu_cursor(1)
            func_blit_title("Drop:",1)

            if in_submenu_drop2 == True:

                pygame.draw.rect(win_map, (100,100,100), (14, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (24, 10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (214, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (224,10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (414, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (424,10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (614, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (624,10, 180, 480))

                pygame.draw.rect(win_map, (100,100,100), (814, 0, 200, 500))
                pygame.draw.rect(win_map, (125,125,125), (824,10, 180, 480))

                if in_menu_item == True:
                    if len(inventory) != 0:
                        func_blit_list(inventory,2,True)
                if in_menu_weapon == True:
                    if len(weapon_inventory) != 0:
                        func_blit_list(weapon_inventory,2,True)
                if in_menu_armor == True:
                    if len(armor_inventory) != 0:
                        func_blit_list(armor_inventory,2,True)
                if in_menu_helmet == True:
                    if len(helmet_inventory) != 0:
                        func_blit_list(helmet_inventory,2,True)
                if in_menu_shield == True:
                    if len(shield_inventory) != 0:
                        func_blit_list(shield_inventory,2,True)
                if in_menu_spell == True:
                    if len(spell_inventory) != 0:
                        func_blit_list(spell_inventory,2,True)

                func_blit_menu_cursor(2)
                func_blit_title("Drop 2:",2)

    # func_blit_player_damage(1,32,blit_player_damage_amount)

    if animation != 0:
        frame_count = 1
        while frame_count < 5:
            #pygame.time.delay(tick_delay_time)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_start = 0
                    battle_intro = False
                    break

            if animation == 1:
                for enemy_stats in current_enemies:
                    enemy_pos = current_enemies.index(enemy_stats) + 1
                    if enemy_stats.is_active == True:
                        if dev_mode >= 4:
                            print(str(frame_count))
                        win_map.blit(enemy_stats.cast_sprite[frame_count], ( ((cx-256) + ((enemy_pos+1)*128)), ((cy) + ((1)*32)) ) )
                        frame_count += 1


            pygame.display.update()
            clock.tick(30) 

    pygame.display.update()
    clock.tick(40)#fps limit
    frames += 1
    if frames >= 8:
        frames = 0
        current_anim_index += 1
        if current_anim_index > anim_index_max:
            current_anim_index = 0
           
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

def func_player_mp_change(amount,is_add): #this needs to be a method on the player class
    if is_add == True:
        player1.mp += amount
        if player1.mp > player1.max_mp:
            player1.mp = player1.max_mp
    if is_add == False:
        player1.mp -= amount
        if player1.mp < 0:
            player1.mp = 0

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
                break
                
        scene_level = player1.level
        if dev_mode >= 1:
            print("looking for enemy level " + str(scene_level) + " +/- 3")
        for enemy_stats in all_game_enemies:
            if dev_mode >= 2:
                print("\ndifficulty: " + str(scene_level - 1) + "  - " + str(scene_level + 5))
                print(enemy_stats.print_name + ", lvl: " + str(enemy_stats.level))
            if enemy_stats.level <= scene_level + 5 and enemy_stats.level >= scene_level - 1 and enemy_stats.is_npc == False:
                compatible_enemies_found = True

        if compatible_enemies_found == True:
            for enemy_stats in all_game_enemies:
                encounter_chance = 0
                encounter_chance = random.randint(1,10)
                if encounter_chance == 1 and enemy_stats not in current_enemies and len(current_enemies) < enemy_count and enemy_stats.level <= scene_level + 5 and enemy_stats.level >= scene_level - 1 and enemy_stats.is_npc == False:
                    current_enemies.append(enemy_stats)

        if compatible_enemies_found == False:
            print("not enough compatitible enemies found for difficulty level of scene!")
            in_fight = False
            break

def func_drop_loot(dead_enemy,drop_table_always,drop_table,inv_type):
    
    #drop_table_always = item,weapon,helmet,armor etc.
    #drop_table = item,weapon,helmet,armor etc.

    #all_ground_game_type = the ground variant of the dropped item/gear
    #inv_type = the scene_inventory variant of the dropped item/gear

    #TODO: shuffle drop tables when they are built
    

    always_drop = True
    loot_modifier = 10 # the higher this number the lower the chance of loot

    if len(drop_table_always) != 0:
        for item in drop_table_always:

            if item not in inv_type:
                inv_type.append(item)
                print(dead_enemy.print_name + " dropped " + item.print_name + " \n")

            elif item in inv_type:
                for inv_item in inv_type:
                    if item.name == inv_item.name:
                        inv_item.amount += 1
                print(dead_enemy.print_name + " dropped " + item.print_name)


    if random.randint(0,2) == 1 or always_drop == True:
        if len(drop_table) != 0:
            for item in drop_table:
                loot_chance_item = random.randint(0,loot_modifier)
                if loot_chance_item == 1:
                    for item in drop_table_always:

                        if item not in inv_type:
                            inv_type.append(item)
                            print(dead_enemy.print_name + " dropped " + item.print_name + " \n")

                        elif item in inv_type:
                            for inv_item in inv_type:
                                if item.name == inv_item.name:
                                    inv_item.amount += 1
                            print(dead_enemy.print_name + " dropped " + item.print_name)

def func_enemy_dead(enemy_stats):

            print("\n// " + enemy_stats.print_name.upper() + " IS DEAD! // \n")

            player1.gp = player1.gp + enemy_stats.gp
            player1.xp = player1.xp + enemy_stats.xp
            print(enemy_stats.gp)
            print("gold obtained \n")
            print(enemy_stats.xp)
            print("xp obtained \n")

            for quest in quest_list:
                if quest.quest_kill_enemy == True and quest.quest_enemy_name == enemy_stats.print_name:
                    quest.player_kill_count += 1
                    if quest.player_kill_count == quest.quest_kill_amount:
                        quest.finished = True
                        print(quest.name + " is ready to turn in!")
                    if quest.player_kill_count > quest.quest_kill_amount:
                        quest.player_kill_count = quest.quest_kill_amount

            func_drop_loot(
                enemy_stats,
                enemy_stats.drop_table_items_always,
                enemy_stats.drop_table_items,
                inventory)

            func_drop_loot(
                enemy_stats,
                enemy_stats.drop_table_weapons_always,
                enemy_stats.drop_table_weapons,
                weapon_inventory)

            func_drop_loot(
                enemy_stats,
                enemy_stats.drop_table_armor_always,
                enemy_stats.drop_table_armor,
                armor_inventory)

            func_drop_loot(
                enemy_stats,
                enemy_stats.drop_table_helmets_always,
                enemy_stats.drop_table_helmets,
                helmet_inventory)

            func_drop_loot(
                enemy_stats,
                enemy_stats.drop_table_shields_always,
                enemy_stats.drop_table_shields,
                shield_inventory)

def func_get_target():
    #
    # Opens a menu for player to decide who to target, defaults to single enemy if there is only one enemy available
    #
    global combat_cursor_pos
    global in_submenu2
    global in_submenu_target_combat2

    target = "0"
    if len(current_enemies) > 0:
        if dev_mode >=2:
            print("")
            for enemy_stats in current_enemies:
                print("|| " + str((current_enemies.index(enemy_stats)+1)) + " || LVL: " + str(enemy_stats.level) + " || " + enemy_stats.print_name + " || ATR: " + enemy_stats.print_attribute)
            print("\nWho will you attack? \n")

        in_submenu2 = True
        in_submenu_target_combat2 = True
        while in_submenu_target_combat2 == True:

            #pygame.time.delay(tick_delay_time)

            func_refresh_pygame(False,0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_start = 0
                    in_fight = False
                    in_submenu2 = False
                    in_submenu_target_combat2 = False
                    in_menu = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        func_move_combat_cursor(True)
                    if event.key == pygame.K_s:
                        func_move_combat_cursor(False)
                    if event.key == pygame.K_q:
                        func_reset_cursor_pos()
                        in_submenu2 = False
                        in_submenu_target_combat2 = False

                    if event.key == pygame.K_e:
                        sfx_cursor_select.play()
                        val_target_input = combat_cursor_pos
                        val_enemy = val_target_input - 1
                        for enemy_stats in current_enemies:
                            if val_enemy == current_enemies.index(enemy_stats):
                                target = enemy_stats.name
                        in_submenu2 = False
                        in_submenu_target_combat2 = False
                        break

    return target

def func_player_melee(): #add spell bonus, status effect buffs to melee attacks
    global player_turns
    target = func_get_target()
    for enemy_stats in current_enemies:
        enemy_stats.calculate_total_bonuses()
        if enemy_stats.name == target:

            #get stats of equipped weapon
            if equiped_weapon:
                player_weapon_level = weapon.level
            else:
                player_weapon_level = 1

            player_hit_chance = random.randint(0,enemy_stats.total_defence) + (player1.total_attack + player_weapon_level)
            player_crit_chance = random.randint(0,100) + ((player1.total_attack + player_weapon_level) // 10)
            
            player_damage =  player1.total_attack + player1.total_strength +  (random.randint(1,player1.level) * (player1.level // 2))

            player_crit_damage = player_damage * 2
            
            if player_hit_chance >= enemy_stats.total_defence:
                if player_crit_chance >= 100:
                    #crit damage
                    print(Fore.RED + Style.BRIGHT + "\nCRITICAL HIT!" + Style.RESET_ALL)
                    dealt_damage = enemy_stats.take_damage(player_crit_damage,"physical")
                else:
                    #normal damage
                    dealt_damage = enemy_stats.take_damage(player_damage,"physical")
                  
                #calculate skill xp from attacking
                player1.attack_xp += (player1.attack * (dealt_damage))
                player1.strength_xp += (player1.strength * (dealt_damage + player1.strength))
            
            else:
                print("Your attack missed the " + enemy_stats.print_name)
            

            break

def func_player_spell():

    status_mgk = player1.status_effect_magic_bonus

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
                    # spell effect 0 does damage, spell effect 1 does damage and heals caster for some amount
                    print("you cast " + spell.print_name)
                    if spell.aoe_scale == 0:
                        target = func_get_target()
                        for enemy_stats in current_enemies:
                            if enemy_stats.name == target:
                                for fx in spell.status_effects:
                                    if fx not in enemy_stats.status_effect_list:
                                        enemy_stats.status_effect_list.append(fx)
                                        print("\nyou " + fx.text + " the " + enemy_stats.print_name)
                                if spell.damage:
                                    player_damage = (player1.level + spell.damage) * player1.total_magic     
                                    enemy_stats.take_damage(player_damage,spell.attribute)
                                    if spell.effect == 1:
                                        player1.heal(player_damage // 2)
                                            

                    if spell.aoe_scale == 1: #all enemies
                        for enemy_stats in current_enemies:
                            for fx in spell.status_effects:
                                if fx not in enemy_stats.status_effect_list:
                                    enemy_stats.status_effect_list.append(fx)
                                    print("\nyou " + fx.text + " the " + enemy_stats.print_name)
                            if spell.damage:
                                player_damage = (player1.level + spell.damage) * player1.total_magic     
                                enemy_stats.take_damage(player_damage,spell.attribute)
                                if spell.effect == 1:
                                    player1.heal(player_damage // 2)
                                        


                    if spell.aoe_scale == 2: #random, inaccurate
                        for enemy_stats in current_enemies:
                            if random.randint(0,7) == 1:
                                for fx in spell.status_effects:
                                    if fx not in enemy_stats.status_effect_list:
                                        enemy_stats.status_effect_list.append(fx)
                                        print("\nyou " + fx.text + " the " + enemy_stats.print_name)
                                if spell.damage:
                                    player_damage = (player1.level + spell.damage) * player1.total_magic     
                                    enemy_stats.take_damage(player_damage,spell.attribute)
                                    if spell.effect == 1:
                                        player1.heal(player_damage // 2)


                    if spell.aoe_scale == 3: #random, accurate
                        for enemy_stats in current_enemies:
                            if random.randint(0,1) == 1:
                                for fx in spell.status_effects:
                                    if fx not in enemy_stats.status_effect_list:
                                        enemy_stats.status_effect_list.append(fx)
                                        print("\nyou " + fx.text + " the " + enemy_stats.print_name)
                                if spell.damage:
                                    player_damage = (player1.level + spell.damage) * player1.total_magic     
                                    enemy_stats.take_damage(player_damage,spell.attribute)
                                    if spell.effect == 1:
                                        player1.heal(player_damage // 2)



                    player1.magic_xp += (player1.magic^2 + spell.xp)

                    break


                if spell.effect == 2: 
                    # spell effect 10 applies buffs and can heal if spell has damage
                    print("you cast " + spell.print_name)
                    if spell.aoe_scale == 0: # targets only the caster
                        if spell.status_effects: #if spell has status effects
                            for fx in spell.status_effects:
                                if fx not in player1.status_effect_list:
                                    player1.status_effect_list.append(fx)
                                    print(player1.name + " " + fx.text + " itself")

                        if spell.damage: #if spell does damage/healing
                            player_healing = (player1.level + spell.damage) * player1.total_magic     
                            player1.heal(player_healing)
                else:
                    print("  PLAYER CANNOT CAST AOE HEALING/BUFFING SPELLS - PLEASE IMPLEMENT  ")

            else:
                print(Fore.RED + "\nNOT ENOUGH MANA!\n")
                break

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

def func_calculate_buffs(character):
    if len(character.status_effect_list) != 0:
        for status_condition in character.status_effect_list:
            #stats up
            if status_condition.is_str_up == True:
                character.status_effect_strength_bonus = (character.strength // 4) + (2 * status_condition.scalar)

            if status_condition.is_atk_up == True:
                character.status_effect_attack_bonus = (character.attack // 4) + (2 * status_condition.scalar)

            if status_condition.is_mgk_up == True:
                character.status_effect_magic_bonus = (character.magic // 4) + (2 * status_condition.scalar)

            if status_condition.is_def_up == True:
                character.status_effect_defence_bonus = (character.defence // 4) + (2 * status_condition.scalar)

            #stats down
            if status_condition.is_str_down == True:
                character.status_effect_strength_bonus = -1 * ((character.defence // 4) + (2 * status_condition.scalar))

            if status_condition.is_atk_down == True:
                character.status_effect_attack_bonus = -1 * ((character.attack // 4) + (2 * status_condition.scalar))

            if status_condition.is_mgk_down == True:
                character.status_effect_magic_bonus = -1 * ((character.magic // 4) + (2 * status_condition.scalar))

            if status_condition.is_def_down == True:
                character.status_effect_defence_bonus = -1 * ((enemy_stats.defence // 4) + (2 * status_condition.scalar))
    
    character.calculate_total_bonuses()

def func_player_status_check(is_attack_type_hit,force_no_attack):

    for player_stats in players:

        func_calculate_buffs(player_stats)

        player_can_attack = False
        if len(player_stats.status_effect_list) == 0:
            player_can_attack = True
        else:
            for status_condition in player_stats.status_effect_list:
                
                # these neeed to be caclculated at the start of each turn

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
                        player_stats.check_dead()
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
                        player_stats.check_dead()
                        player_can_attack = True
                    else:
                        print("\n" + player_stats.name + " is no longer burning")
                        player_stats.status_effect_list.remove(status_condition)
                        player_can_attack = True

        if force_no_attack == True:
            player_can_attack = False

        if player_can_attack == True:

            if is_attack_type_hit == False:
                func_player_spell()
            if is_attack_type_hit == True:
                func_player_melee()

def func_enemy_status_check():
    # iterates through all current enemies and performs their turn
    for enemy_stats in current_enemies:
        
        enemy_can_attack = False

        enemy_stats.is_active = True
        print("\n" + enemy_stats.print_name + " is active")

        func_calculate_buffs(enemy_stats)

        if len(enemy_stats.status_effect_list) == 0:
            enemy_can_attack = True
            
        else:
            for status_condition in enemy_stats.status_effect_list:
                if status_condition.is_freeze == True:
                    freeze_chance = 0
                    freeze_chance = random.randint(1,6)
                    if freeze_chance != 1:
                        print(enemy_stats.print_name + " is frozen and cannot attack!\n")
                        enemy_can_attack = False
                    else:
                        print(enemy_stats.print_name + " broke free from the ice!\n")
                        enemy_stats.status_effect_list.remove(status_condition)
                        enemy_can_attack = True

                if status_condition.is_poisoned == True:
                    poison_chance = 0
                    poison_chance = random.randint(1,5)
                    if poison_chance != 1:
                        enemy_poison_damage = (enemy_stats.hp // 100) + (status_condition.scalar * 10)
                        enemy_stats.hp -= enemy_poison_damage
                        print(enemy_stats.print_name + " takes " + str(enemy_poison_damage) + " poison damage!\n")
                        func_check_enemy_dead()
                        enemy_can_attack = True
                    else:
                        print(enemy_stats.print_name + " is no longer poisoned\n")
                        enemy_stats.status_effect_list.remove(status_condition)
                        enemy_can_attack = True

                if status_condition.is_burning == True:
                    burn_chance = 0
                    burn_chance = random.randint(1,11)
                    if burn_chance != 1:
                        enemy_burn_damage = (enemy_stats.hp // 100) + (status_condition.scalar * 10)
                        enemy_stats.hp -= enemy_burn_damage
                        print(enemy_stats.print_name + " is on fire and takes " + str(enemy_burn_damage)+ " damage!\n")
                        func_check_enemy_dead()
                        enemy_can_attack = True
                    else:
                        print(enemy_stats.print_name + " is no longer burning\n")
                        enemy_stats.status_effect_list.remove(status_condition)
                        enemy_can_attack = True

        if enemy_can_attack:
            func_enemy_attack(enemy_stats)

def func_check_enemy_dead():
    global npc_enemy_fname
    global npc_enemy_lname
    global in_fight
    global npc_fight
    for enemy_stats in current_enemies:
        if enemy_stats.hp <= 0:
            dead_enemies.append(enemy_stats)
            current_enemies.remove(enemy_stats)

    if len(current_enemies) == 0:
        in_fight = False
        pygame.mixer.music.stop()
        for scene_type in location:
            for npc in scene_type.npc_list:
                if npc_enemy_fname == npc.first_name and npc_enemy_lname == npc.last_name:
                    print("\n" + npc.first_name + "" + npc.last_name + " is dead...")
                    scene_type.npc_list.remove(npc)
                    npc_fight = False

def func_enemy_attack(enemy_stats):

    global blit_player_damage_amount

    if (not enemy_stats.spellbook):
        func_enemy_melee(enemy_stats)
    else:
        for spell in enemy_stats.spellbook:
            
            print(enemy_stats.print_name + " is preparing a spell")
            spellchance = 1

            if spellchance == 1:
                enemy_stats.mp -= spell.mp_cost
                if enemy_stats.mp < 0:
                    enemy_stats.mp = 0

                if spell.effect == 0 or spell.effect == 1:
                    print(enemy_stats.print_name + " casts " + spell.print_name)
                    if spell.status_effects:
                        for fx in spell.status_effects:
                            if fx not in player1.status_effect_list:
                                player1.status_effect_list.append(fx)
                                print(enemy_stats.print_name + " " + fx.text + " you")
                                
                    if spell.damage:
                        enemy_damage = (enemy_stats.level + spell.damage) * enemy_stats.total_magic     
                        damage_dealt = player1.take_damage(enemy_damage,spell.attribute,enemy_stats.print_name)
                        if spell.effect == 1:
                            enemy_stats.heal(damage_dealt // 2)


                if spell.effect == 2: 
                    # spell effect 10 applies buffs and can heal if spell has damage
                    print(enemy_stats.print_name + " casts " + spell.print_name)
                    if spell.aoe_scale == 0: # targets only the caster
                        if spell.status_effects: #if spell has status effects
                            for fx in spell.status_effects:
                                if fx not in enemy_stats.status_effect_list:
                                    enemy_stats.status_effect_list.append(fx)
                                    print(enemy_stats.print_name + " " + fx.text + " itself")

                        if spell.damage: #if spell does damage/healing
                            enemy_healing = (enemy_stats.level + spell.damage) * enemy_stats.total_magic     
                            enemy_stats.heal(enemy_healing)     

                    if spell.aoe_scale == 1: # target all allies
                        for enemy_stats_other in current_enemies:
                            for fx in spell.status_effects:
                                if fx not in enemy_stats.status_effect_list:
                                    enemy_stats_other.status_effect_list.append(fx)
                                    print(enemy_stats.print_name + " " + fx.text + " the " + enemy_stats_other.name)

                            if spell.damage:
                                enemy_healing = (enemy_stats.level + spell.damage) * enemy_stats.total_magic     
                                enemy_stats_other.heal(enemy_healing)

                    #TODO: add spells which heal/buff with random accuracy? 
                                                  
                    
                enemy_stats.is_active = False

                break
            else:
                func_enemy_melee(enemy_stats)
                break

def func_enemy_melee(enemy_stats):
    global blit_player_damage_amount
    print(enemy_stats.print_name + "is preparing to attack")
    for player_stats in players: 
        enemy_damage = 0

        enemy_hit_chance = random.randint(0,player_stats.total_defence) + (enemy_stats.total_attack)
        
        if enemy_hit_chance >= player_stats.total_defence:
            
            enemy_damage = (enemy_stats.total_attack + enemy_stats.total_strength + (random.randint(1,5) * (enemy_stats.level // 2)))
            enemy_crit_chance = random.randint(0,100) + ((enemy_stats.total_attack) // 10)
            
            if enemy_crit_chance >= 100:
                enemy_damage = enemy_damage * 2
                print(Fore.RED + Style.BRIGHT + "\nCRITICAL HIT!" + Style.RESET_ALL)
                player_stats.take_damage(enemy_damage,"physical",enemy_stats.print_name)
                blit_player_damage_amount = enemy_damage      

            else:
                player_stats.take_damage(enemy_damage,"physical",enemy_stats.print_name)
                blit_player_damage_amount = enemy_damage        
        
        else:
            print(enemy_stats.print_name + "'s attack missed!")

        enemy_stats.is_active = False

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

        #pygame.time.delay(tick_delay_time)

        
        func_refresh_pygame(False,0)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
                in_fight = False
                in_submenu = False
                in_submenu_use_combat = False
                in_menu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    func_move_combat_cursor(True)
                if event.key == pygame.K_s:
                    func_move_combat_cursor(False)
                if event.key == pygame.K_q:
                    func_reset_cursor_pos()
                    in_submenu = False
                    in_submenu_use_combat = False
                if event.key == pygame.K_e:
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
                        has_item_multiple = False
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
                                        player1.check_dead()


                                    if item.name == eaten_item and item.amount > 1:
                                        has_item_multiple = True
                                        item.amount -= 1
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

#############################--MENU FUNCTIONS--#######################

def check_quit(event):
    global game_start
    if event.type == pygame.QUIT:
        game_start = 0
        func_close_all_menus()

def check_cursor_moved(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            func_move_cursor(True)

        elif event.key == pygame.K_s:
            func_move_cursor(False)

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
        if True:
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

                #pygame.time.delay(tick_delay_time)

                func_check_level()
                func_refresh_pygame(False,0)


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_start = 0
                        in_fight = False
                        in_submenu3 = False
                        in_submenu_buy3 = False
                        in_menu = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            func_move_cursor(True)
                        if event.key == pygame.K_s:
                            func_move_cursor(False)
                        if event.key == pygame.K_q:
                            func_reset_cursor_pos()
                            in_submenu3 = False
                            in_submenu_buy3 = False
                            in_menu_weapon = False
                            in_menu_armor = False
                            in_menu_helmet = False
                            in_menu_shield = False
                            in_menu_spell = False

                        if event.key == pygame.K_e:
                            sfx_cursor_select.play()
                            val_bought_item = menu_cursor_pos
                            val_shop = val_bought_item - 1
                            for gear in npc_gear_inv:
                                if val_shop == npc_gear_inv.index(gear):
                                    target_gear = gear.name

                            has_item = False
                            has_item_multiple = False

                            has_weapon_multiple = False
                            has_armor_multiple = False
                            has_helmet_multiple = False
                            has_shield_multiple = False
                            has_spell_multiple = False

                            for gear in npc_gear_inv:
                                if target_gear == gear.name:
                                    has_item = True
                                    if player1.gp >= gear.value:
                                        player1.gp -= gear.value

                                        if gear in all_game_weapons:
                                            for weapon in weapon_inventory:
                                                if weapon.name == target_gear:
                                                    has_weapon_multiple = True
                                                    weapon.amount += 1
                                                    break
                                            if has_weapon_multiple == False:
                                                for weapon in all_game_weapons:
                                                    if weapon.name == target_gear:
                                                        weapon_inventory.append(weapon)
                                                        break

                                        if gear in all_game_armor:
                                            for armor in armor_inventory:
                                                if armor.name == target_gear:
                                                    has_armor_multiple = True
                                                    armor.amount += 1
                                                    break
                                            if has_armor_multiple == False:
                                                for armor in all_game_armor:
                                                    if armor.name == target_gear:
                                                        armor_inventory.append(armor)
                                                        break

                                        if gear in all_game_helmets:
                                            for helmet in helmet_inventory:
                                                if helmet.name == target_gear:
                                                    has_helmet_multiple = True
                                                    helmet.amount += 1
                                                    break
                                            if has_helmet_multiple == False:
                                                for helmet in all_game_helmets:
                                                    if helmet.name == target_gear:
                                                        helmet_inventory.append(helmet)
                                                        break

                                        if gear in all_game_shields:
                                            for shield in shield_inventory:
                                                if shield.name == target_gear:
                                                    has_shield_multiple = True
                                                    shield.amount += 1
                                                    break
                                            if has_shield_multiple == False:
                                                for shield in all_game_shields:
                                                    if shield.name == target_gear:
                                                        shield_inventory.append(shield)
                                                        break

                                        if gear in all_game_items:
                                            for item in inventory:
                                                if item.name == target_gear:
                                                    has_item_multiple = True
                                                    item.amount += 1
                                                    break
                                            if has_item_multiple == False:
                                                for item in all_game_items:
                                                    if item.name == target_gear:
                                                        inventory.append(item)
                                                        break

                                        if gear in all_game_spells:
                                            for spell in spell_inventory:
                                                if spell.name == target_gear:
                                                    has_spell_multiple = True
                                                    spell.amount += 1
                                                    print("\nadded " + gear.name + "\n")

                                                    break
                                            if has_spell_multiple == False:
                                                for spell in all_game_spells:
                                                    if spell.name == target_gear:
                                                        spell_inventory.append(spell)
                                                        print("\naquired " + gear.name + "\n")

                                                        break

                                        print("\nthanks, enjoy your " + gear.name + "\n")
                                        func_check_quest_items()
                                        # in_submenu3 = False
                                        # in_submenu_buy3 = False
                                        # in_menu_item = False
                                        # in_menu_weapon = False
                                        # in_menu_armor = False
                                        # in_menu_helmet = False
                                        # in_menu_shield = False
                                        # in_menu_spell = False

                                    else:
                                        print("You can't afford that!")
                                        # in_submenu3 = False
                                        # in_submenu_buy3 = False
                            # in_submenu3 = False
                            # in_submenu_buy3 = False


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

        #pygame.time.delay(tick_delay_time)

        func_check_level()
        func_refresh_pygame(False,0)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
                in_fight = False
                in_submenu4 = False
                in_submenu_sell4 = False
                in_menu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    func_move_cursor(True)
                if event.key == pygame.K_s:
                    func_move_cursor(False, limit = len(player_gear_inv))
                if event.key == pygame.K_q:
                    func_reset_cursor_pos()
                    in_submenu4 = False
                    in_submenu_sell4 = False
                    in_menu_item = False
                    in_menu_weapon = False
                    in_menu_armor = False
                    in_menu_helmet = False
                    in_menu_shield = False
                    in_menu_spell = False

                if event.key == pygame.K_e:
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
                            gear.amount -= 1
                            if gear.amount <= 0:
                                player_gear_inv.remove(gear)
                            # in_submenu4 = False
                            # in_submenu_sell4 = False
                            break

def func_use(player_gear_inv):
    global time
    global time2
    eaten_item = "0"
    if dev_mode >= 2:
        for gear in player_gear_inv:
                print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + str(gear.value) + " gp. " + " || " + str(gear.item_desc) + "... ")
    
    has_item = False
    val_use = menu_cursor_pos - 1
    for gear in player_gear_inv:
        if val_use == player_gear_inv.index(gear):
            eaten_item = gear.name

    for item in inventory:
        has_item = False
        can_use = False
        for item in inventory:
            if eaten_item == item.name:
                has_item = True
                if item.name == "woodcutting axe":
                    can_chop = False
                    can_use = True
                    has_item_multiple = False
                    for scene_type in location:
                        if scene_type.biome == "forest":
                            can_chop = True
                        else:
                            can_chop = False
                            print("there is no forest here!")
                    if can_chop == True:
                        print("You chop down some wood.")
                        for item in inventory:
                            if item.name == "wood" and item.amount >= 1:
                                has_item_multiple = True
                                item.amount += 1
                                print("+ 1 wood added")
                                can_chop = False

                    if can_chop == True:
                        if has_item_multiple == False:
                            for item in all_game_items:
                                if item.name == "wood":
                                    print("wood appended")
                                    inventory.append(item)
                                    break

                if item.name == "tent":
                    can_camp = False
                    can_use = True
                    for scene_type in location:
                        if scene_type.safe == True:
                            can_camp = True
                        else:
                            can_camp = False
                            print("It is too dangerous to camp here!")
                    if can_camp == True:
                        print("You camp untill the next morning, your hp and mp have been restored.")
                        time += 24
                        for player_stats in players:
                            player_stats.hp = player_stats.maxhp
                            player_stats.mp = player_stats.maxmp

                if item.name == "rope":
                    can_climb = False
                    can_use = True
                    for scene_type in location:
                        if scene_type.zpos < 0:
                            can_climb = True
                        else:
                            can_climb = False
                            print("\nyou can't use that here!")
                    if can_climb == True:
                        print("\nyou return to the surface... ")
                        func_tp(6,0,0)
                        func_close_all_menus()
                    break

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

                        player1.check_dead()

                    if item.name == eaten_item:
                        item.amount -= 1
                        if item.amount <= 0:
                            inventory.remove(item)

                    
                    break

                if can_use == False:
                    "you try to use " + item.print_name + ", but nothing interesting happens"
                func_check_quest_items()
        break

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

        #pygame.time.delay(tick_delay_time)

        func_check_level()
        func_refresh_pygame(False,0)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
                in_submenu = False
                in_submenu_cast = False
                in_menu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    func_move_cursor(True)
                if event.key == pygame.K_s:
                    func_move_cursor(False, limit = len(player_gear_inv))
                if event.key == pygame.K_q:
                    func_reset_cursor_pos()
                    in_submenu = False
                    in_submenu_cast = False

                if event.key == pygame.K_e:
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

def func_choose_equip_menu():
    global game_start

    global menu_cursor_pos

    global in_menu
    global in_submenu
    global in_submenu_equip
    
    global in_submenu2
    global in_submenu_equip2
    global in_menu_item
    global in_menu_spell
    global in_menu_weapon
    global in_menu_armor
    global in_menu_helmet
    global in_menu_shield
    

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
        #func_check_level()
        func_refresh_pygame(False,0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
                func_close_all_menus()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:
                    func_move_cursor(True)

                if event.key == pygame.K_s:
                    func_move_cursor(False)

                if event.key == pygame.K_q:
                    func_reset_cursor_pos()
                    in_submenu_equip = False
                    in_submenu = False
                    print("equip menu quit")
                    break # break the in_submenu_equip while loop

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

#############################----SCENE_FUNCTIONS----#########################

def func_tp(coordinates :tuple):
    global steps_x
    global steps_y
    global steps_z

    global tmx_data
    global tmx_list

    old_z = steps_z

    x = coordinates[0]
    y = coordinates[1]
    z = coordinates[2]

    steps_x = x
    steps_y = y
    steps_z = z

    if z != old_z:
        #load new tmx
        tmx_data = tmx_list[z]

    if dev_mode >= 1:
        print("you teleported to: ",x,y,z)

    location_desc()

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
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || x " + str(gear.amount) + " || " + str(gear.value * gear.amount) + " gp. " )
        if gear in all_game_spells:
            in_menu_spell = True
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + str(gear.value) + " gp. ")

    print("\nwhat do you want to drop\n")
    in_submenu2 = True
    in_submenu_drop2 = True
    while in_submenu_drop2 == True:

        #pygame.time.delay(tick_delay_time)

        func_check_level()
        func_refresh_pygame(False,0)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_menu_item = False
                in_menu_weapon = False
                in_menu_armor = False
                in_menu_helmet = False
                in_menu_shield = False
                in_menu_spell = False
                in_submenu2 = False
                in_submenu_drop2 = False
                in_menu = False
                game_start = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    func_move_cursor(True)
                if event.key == pygame.K_s:
                    func_move_cursor(False, limit = len(player_gear_inv))
                if event.key == pygame.K_q:
                    func_reset_cursor_pos()
                    in_submenu2 = False
                    in_submenu_drop2 = False
                    in_menu_item = False
                    in_menu_weapon = False
                    in_menu_armor = False
                    in_menu_helmet = False
                    in_menu_shield = False
                    in_menu_spell = False
                if event.key == pygame.K_e:
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
                                    if item.name == target_gear and item.amount > 1:
                                        has_item_multiple = True
                                        item.amount -= 1
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
                                    if end_drop == False and ground_item.name == target_gear and ground_item.amount >= 1:
                                        ground_has_item_multiple = True
                                        ground_item.amount += 1
                                        end_drop = True
                                        break

                                if end_drop == False and ground_has_item_multiple == False:
                                    for ground_item in all_ground_game_items:
                                        if ground_item.name == target_gear:
                                            scene_type.scene_inventory.append(ground_item)
                                    for ground_item in scene_type.scene_inventory:
                                        if ground_item.name == target_gear:
                                            ground_item.amount = 1
                                    end_drop = True

                            if gear in all_game_weapons:
                                pass # WEAPONS AND ARMOR WILL BE REMOVED FROM INVENTORY, BUT WILL NOT APPEAR ON THE GROUND
                            if gear in all_game_armor:
                                pass # WEAPONS AND ARMOR WILL BE REMOVED FROM INVENTORY, BUT WILL NOT APPEAR ON THE GROUND
                            if gear in all_game_helmets:
                                pass # WEAPONS AND ARMOR WILL BE REMOVED FROM INVENTORY, BUT WILL NOT APPEAR ON THE GROUND
                            if gear in all_game_shields:
                                pass # WEAPONS AND ARMOR WILL BE REMOVED FROM INVENTORY, BUT WILL NOT APPEAR ON THE GROUND

                    break

def func_search_treasure(location):
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
                                    print("you found " + item.print_name + "")
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
            for scene_type in location:
                scene_type.passable = True

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

def func_move_cursor(is_up,limit = 18):

    global menu_cursor_pos
    if is_up == True:
        if menu_cursor_pos <= 1:
            menu_cursor_pos == 1
        else:
            sfx_cursor_move.play()
            menu_cursor_pos -= 1
        if dev_mode >= 4:
            print(menu_cursor_pos)

    elif is_up == False:
        if menu_cursor_pos >= limit:
            menu_cursor_pos == limit
        else:
            sfx_cursor_move.play()
            menu_cursor_pos += 1
        if dev_mode >= 4:
            print(menu_cursor_pos)

def func_move_combat_cursor(is_up,limit = 18):
    global combat_cursor_pos
    if is_up == True:
        if combat_cursor_pos <= 1:
            combat_cursor_pos == 1
        else:
            sfx_cursor_move.play()
            combat_cursor_pos -= 1
        if dev_mode >= 4:
            print(combat_cursor_pos)

    if is_up == False:
        if combat_cursor_pos >= limit:
            combat_cursor_pos == limit
        else:
            sfx_cursor_move.play()
            combat_cursor_pos += 1
        if dev_mode >= 4:
            print(combat_cursor_pos)

def func_cook(gear,player_gear_inv):
    global menu_cursor_pos
    global in_submenu2
    global in_submenu_cook2
    eaten_item = "0"
    for gear in player_gear_inv:
        if gear in all_game_items:
            print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + str(gear.value) + " gp. " + " || " + str(gear.item_desc) + "... ")

    in_submenu2 = True
    in_submenu_cook2 = True
    while in_submenu_cook2 == True:

        #pygame.time.delay(tick_delay_time)

        func_check_level()
        func_refresh_pygame(False,0)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
                in_fight = False
                in_submenu2 = False
                in_submenu_cook2 = False
                in_menu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    func_move_cursor(True)
                if event.key == pygame.K_s:
                    func_move_cursor(False, limit = len(player_gear_inv))
                if event.key == pygame.K_q:
                    func_reset_cursor_pos()
                    in_submenu2 = False
                    in_submenu_cook2 = False

                if event.key == pygame.K_e:
                    sfx_cursor_select.play()
                    has_item = False
                    val_cooked_item = menu_cursor_pos
                    val_cook = val_cooked_item - 1
                    for gear in player_gear_inv:
                        if val_cook == player_gear_inv.index(gear):
                            cooked_item = gear.name

                    for item in inventory:
                        if item.name == cooked_item:
                            if item.is_raw == True:
                                print("you cook a " + item.print_name)
                                player1_skills.cooking_xp += item.value
                                func_check_level()
                                item.amount -= 1
                                if item.amount <= 0:
                                    inventory.remove(item)
                                #remove 1x item from inventory

                                for item in all_game_items:
                                    if item.ingredient_name == cooked_item:
                                        new_item = item.name
                                        #get name of new item

                                has_item = False

                                for item in inventory:
                                    if item.name == new_item:
                                        has_item = True
                                        item.amount += 1

                                if has_item == False:
                                    for item in all_game_items:
                                        if item.name == new_item:
                                            inventory.append(item)

                            else:
                                print("you cannot cook " + item.print_name)

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

def func_equip(player_gear_inv,equip_slot):
    '''
    player_gear_inv = the list to equip from,
    equip_slot = the list to equip to

    '''
 
    # for gear in player_gear_inv: #def. list to print in gui
    #     print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || " + gear.type + " || lvl: " + str(gear.level) + " || ATK: " + str(gear.attack_bonus) + " || STR: " + str(gear.strength_bonus) + " || MGK: " + str(gear.magic_bonus) + " || DEF: " + str(gear.defence_bonus) + " || HP: " + str(gear.maxhp_bonus) + " || " + str(gear.value) + " gp. ")
        
    #     if gear in all_game_spells:
    #         in_menu_spell = True
    #         print("|| " + str((player_gear_inv.index(gear)+1)) + " || " + gear.print_name + " || " + gear.print_attribute + " || lvl: " + str(gear.level) + " || PWR: " + str(gear.damage) + " || " + str(gear.value) + " gp. ")
    #         print(gear.spell_desc + "\n")

    # print("\nwhat do you want to equip\n")

    if len(player_gear_inv) > menu_cursor_pos - 1:
        
        unequiped_gear = None
        equiped_gear = player_gear_inv[menu_cursor_pos - 1]

        if not isinstance(equiped_gear,spell):
            #if equiped gear is not a spell
            if equiped_gear.level <= player1.level:
                if equip_slot:
                    unequiped_gear = equip_slot[0]

                    if unequiped_gear not in player_gear_inv:
                        unequiped_gear.amount = 1
                        player_gear_inv.append(unequiped_gear)
                    else:
                        for gear in player_gear_inv:
                            if gear.name == unequiped_gear.name:
                                gear.amount += 1

                    del equip_slot[:]
                
                #Remove gear from inventory
                equiped_gear.amount -= 1
                if equiped_gear.amount <= 0:
                    player_gear_inv.remove(equiped_gear)

                equip_slot.append(equiped_gear)

            else:
                print(f"not high enough level to equip {equiped_gear.name}")
        else:
            #if equiped gear is a spell
            if equiped_gear.level <= player1.level:
                if equiped_gear not in equip_slot: #equip_slot is the spellbook in this case
                    equiped_gear.amount -= 1
                    if equiped_gear.amount <= 0:
                        player_gear_inv.remove(equiped_gear)

                    equip_slot.append(equiped_gear)
                else:
                    print(f"You already have {equiped_gear.name} in your spellbook")
                    #add spell to equiped spells, remove from inventory
            else:
                print(f"You are not a high enough level to learn {equiped_gear.name}")


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

        if player_stats.xp >= (player_stats.level ** 3):
            player_stats.level += 1
            print("\nLEVELED UP \nyou are now level: ", player_stats.level)
            func_basic_droptables()
            func_check_level()

        player_stats.nobonus_maxhp = (player_stats.level * 100) + (player_stats.defence * 25) + (player_stats.strength * 10) + (player_stats.attack * 10) + (player_stats.magic * 10)

        player_stats.nobonus_maxmp = (player_stats.level * 72) + (player_stats.magic * 125)

        player_stats.maxhp = (player_stats.nobonus_maxhp + player_stats.maxhp_bonus)

        player_stats.maxmp = (player_stats.nobonus_maxmp + player_stats.maxmp_bonus)

    for player_skills in players_skills:
        if player_skills.thieving_xp >= (player_skills.thieving ** 4):
            player_skills.thieving += 1
            print("\nyour thieving level is now: ", player_skills.thieving)
            func_check_level()

        if player_skills.fishing_xp >= (player_skills.fishing ** 4):
            player_skills.fishing += 1
            print("\nyour fishing level is now: ", player_skills.fishing)
            func_check_level()

        if player_skills.alchemy_xp >= (player_skills.alchemy ** 4):
            player_skills.alchemy += 1
            print("\nyour alchemy level is now: ", player_skills.alchemy)
            func_check_level()

        if player_skills.cooking_xp >= (player_skills.cooking ** 4):
            player_skills.cooking += 1
            print("\nyour cooking level is now: ", player_skills.cooking)
            func_check_level()

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
                    
#######################---PLAYER LOCATION---#######################

def check_collision(position:tuple) -> bool:
    can_move = True
    for i in range(3,len(tmx_data.layers)):
        #checks all tiles on all layers for collisions 
        tile_properties = tmx_data.get_tile_properties(steps_x+position[0], steps_y+position[1], i)
        if tile_properties:
            if dev_mode >= 2:
                print(tile_properties)
            if tile_properties["solid"] == 1:
                can_move = False
                break
    return can_move

def check_player_direction():
    global spr_player
    global player_direction
    global spr_player_n
    global spr_player_e
    global spr_player_s
    global spr_player_w

    if player_direction == 0:
        spr_player = spr_player_n
    if player_direction == 1:
        spr_player = spr_player_e
    if player_direction == 2:
        spr_player = spr_player_s
    if player_direction == 3:
        spr_player = spr_player_w

def player_north_check() -> Interactive_Tile:
    for interactable in interactive_tiles:
        if steps_y-1 == interactable.ypos and steps_x == interactable.xpos and steps_z == interactable.zpos:
            return interactable

def player_south_check() -> Interactive_Tile:
    for interactable in interactive_tiles:
        if steps_y+1 == interactable.ypos and steps_x == interactable.xpos and steps_z == interactable.zpos:
            return interactable

def player_east_check() -> Interactive_Tile:
    for interactable in interactive_tiles:
        if steps_y == interactable.ypos and steps_x+1 == interactable.xpos and steps_z == interactable.zpos:
            return interactable

def player_west_check() -> Interactive_Tile:
    for interactable in interactive_tiles:
        if steps_y == interactable.ypos and steps_x-1 == interactable.xpos and steps_z == interactable.zpos:
            return interactable

def location_desc():
    func_check_season()
    func_check_weather()
    func_check_light()
    if dev_mode >= 1:
        print("\n///   DEV MODE " + str(dev_mode) +"!  ///\n")
        if dev_mode >= 2:
 
            if dev_mode >= 3:
                print("in_fight: ", in_fight)
                print("time", time)
                print("season", season)
                print("rain status", raining)
                print("date: ", days, months, years)
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

            # print("restock_ticks " + str(restock_ticks))

            if dev_mode >= 3:
                for scene_type in location:
                    print("scene temp desc. string: ", scene_type.temp)
                    print("scene light desc. string: ", scene_type.light)
                    print("scene_biome: ", scene_type.biome)
                    print("scene_encounter_difficulty: ", scene_type.difficulty)
                    print("can_fish: ", scene_type.can_fish)
                    print("scene_treasure: ", scene_type.treasure)
                    print("scene_has_tp: ", scene_type.has_tp)

                


    for scene_type in location:
        scene_npc_count = 0
        scene_animal_count = 0
        print(Fore.YELLOW + Style.BRIGHT + "\n///////////// ///////////// ////////////\n")
        print("you are in " + scene_type.name + "\n")

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
            
        if  len(scene_type.scene_inventory) != 0 or len(scene_type.scene_weapon_inventory) != 0 or len(scene_type.scene_armor_inventory) != 0 or len(scene_type.scene_helmet_inventory) != 0 or len(scene_type.scene_shield_inventory) != 0:
            print("on the ground is:")
            
        else:
            print("there is nothing on the ground.")
            

        for ground_item in scene_type.scene_inventory:
            print(ground_item.print_name + " x " + str(ground_item.amount))
            
        for ground_weapon in scene_type.scene_weapon_inventory:
            print(ground_weapon.print_name + " x " + str(ground_weapon.amount))
            
        for ground_armor in scene_type.scene_armor_inventory:
            print(ground_armor.print_name + " x " + str(ground_armor.amount))
            
        for ground_helmet in scene_type.scene_helmet_inventory:
            print(ground_helmet.print_name + " x " + str(ground_helmet.amount))
            
        for ground_shield in scene_type.scene_shield_inventory:
            print(ground_shield.print_name + " x " + str(ground_shield.amount))
            


        if scene_type.safe == False:
            print("\nit is dangerous here... \n")

        if dev_mode >= 2:
            
            print("x: ", steps_x)
            print("y: ", steps_y)
            print("z: ", steps_z)
            print("last x: ", prev_x)
            print("last y: ", prev_y)
            print("last z: ", prev_z)

    func_rain()
            
#######################--- QUESTS ---#######################

def func_check_quest_items():
    for quest in quest_list:
        if quest.started == True and quest.quest_collect_item == True:
            for item in inventory:
                if item.name == quest.quest_item_name:
                    if item.amount >= quest.quest_item_amount:
                        quest.finished = True
                        if quest.finished_message_displayed == False:
                            print("you have collected the " + quest.quest_item_name + ", " + quest.name + " is ready to turn in!")
                            quest.finished_message_displayed = True

##########--pre game stat calcutions--#########

def func_gen_class_stats(player_class_string):
    if player_class_string == "1":
        for player_stats in players:
            player_stats.level = 1
            player_stats.xp = 40
            player_stats.strength = 1
            player_stats.attack = 1
            player_stats.magic = 1
            player_stats.defence = 1
            player_stats.strength_xp = 100
            player_stats.attack_xp = 10
            player_stats.magic_xp = 10
            player_stats.defence_xp = 200
    elif player_class_string == "2":
        for player_stats in players:
            player_stats.level = 1
            player_stats.xp = 35
            player_stats.strength = 1
            player_stats.attack = 1
            player_stats.magic = 1
            player_stats.defence = 1
            player_stats.strength_xp = 200
            player_stats.attack_xp = 100
            player_stats.magic_xp = 10
            player_stats.defence_xp = 10
    elif player_class_string == "3":
        for player_stats in players:
            player_stats.level = 1
            player_stats.xp = 50
            player_stats.strength = 1
            player_stats.attack = 1
            player_stats.magic = 1
            player_stats.defence = 1
            player_stats.strength_xp = 10
            player_stats.attack_xp = 10
            player_stats.magic_xp = 200
            player_stats.defence_xp = 10


    ####################################################################

    #dev loadout
    if dev_mode >= 2:
 
        equiped_helmet.append(leather_cap)
        equiped_shield.append(wooden_round_shield)
        equiped_weapon.append(iron_sword)
        equiped_armor.append(iron_chain_mail)

        spell_inventory.append(fireblast)
        spell_inventory.append(necro_surge)

        spell_inventory.append(snare)
        spell_inventory.append(fire_bolt)
        spell_inventory.append(earthblast)


        weapon_inventory.append(super_bird_sword)
        weapon_inventory.append(gladius)
        weapon_inventory.append(iron_axe)
        weapon_inventory.append(iron_dagger)
        weapon_inventory.append(iron_knife)

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
            item.amount = 10

        inventory.append(tent)
        inventory.append(rope)
        inventory.append(torch)


        equiped_spells.append(atk_down)
        equiped_spells.append(str_up)
        equiped_spells.append(fire_bolt)
        equiped_spells.append(ice_bolt)
        equiped_spells.append(atk_down_damage_aoe)
        equiped_spells.append(def_down_aoe)
        equiped_spells.append(mgk_down_damage)
        equiped_spells.append(life_siphon)
        equiped_spells.append(burn)
        equiped_spells.append(mega_burn)
        equiped_spells.append(cone_of_cold)

        
    else:
        if player_class_string == "1":
            equiped_shield.append(wooden_round_shield)
            equiped_weapon.append(iron_sword)
            equiped_armor.append(cloth_armor)

            equiped_spells.append(str_up)
        elif player_class_string == "2":
            equiped_weapon.append(short_dagger)
            equiped_armor.append(cloth_armor)

            equiped_spells.append(atk_down)
        elif player_class_string == "3":

            equiped_weapon.append(wooden_staff)
            equiped_armor.append(rags)

            equiped_spells.append(fire_bolt)
            equiped_spells.append(ice_bolt)


        inventory.append(pendant)
        inventory.append(hp_potion)
        inventory.append(meat)

        for item in inventory:
            item.amount = 1

#####################################

tmx_list = [
    load_pygame("tmx_maps/overworld_1.tmx"),
    load_pygame("tmx_maps/small_cave.tmx")]

tmx_data = tmx_list[0]

func_gen_class_stats(player_class_string)
func_check_stat_bonus()
func_check_level()

player1.hp = player1.maxhp # has to be last as max hp is calculated from all other stats
player1.mp = player1.maxmp

if dev_mode >= 2:
    player1.gp = 999999
    player1.xp = 999999

for tile in interactive_tiles:
    tile.enforce_tile_attributes()


########## GAME START #########
game_start = 1


print(Fore.RED + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to the land of Tonbale! \n")

print("\nversion: " + version + " \n")
print("\n  Controls:\n  W,A,S,D: Move \n  SPACE: Menu\n  E: Select/Use/Pickup\n  R: Talk/Interact \n  Q: Back")
print("\n  Function Keys:\n  F1: Dev Window (WINDOWS ONLY DO NOT OPEN ON MAC OS) \n  F2: player stats\n  F3: equipment\n  F4: dev_mode value + 1 (default = 0) \n  F5: Toggle grid_mode \n  F6: Toggle lighting_mode")

print("\npress any key to start! \n")

active_tiles = []
for tile in interactive_tiles:
    if tile.zpos == steps_z:
        active_tiles.append(tile)

func_check_tile_anims()

while game_start == 1:

    #grab data for use in menus
    menus.items.data = inventory
    menus.equip_spell.data = spell_inventory
    menus.equip_weapon.data = weapon_inventory
    menus.equip_armor.data = armor_inventory
    menus.equip_helmet.data = helmet_inventory
    menus.equip_shield.data = shield_inventory
    menus.quests.data = quest_list

    func_check_quest_items()
    func_shop_restock()
    func_check_stat_bonus()
    func_check_level() #checks surrounding objects for interactive tiles

    player1.hp = player1.maxhp #???
    player1.mp = player1.maxmp #???

    func_refresh_pygame(False,0)

    if has_moved == True or in_fight == True:
        step_counter += 1
        if step_counter >= step_counter_max:
            step_counter = 1
            step_counter2 += 1
            step_counter_max = 12
            if step_counter2 >= 12:
                step_counter_max = 15 + random.randint(1,5)
                step_counter2 = 1


        if npc_fight == False and check_for_combat == True:
            for scene_type in location:
                if scene_type.safe == False:
                    if in_fight == False:
                        if time >= 1200 and steps_z >= - 1000:
                            combat_chance = random.randint(0,50)
                        if time < 1200 or steps_z <= - 1000:
                            combat_chance = random.randint(0,100)

                        if dev_mode >= 3:
                            combat_chance = 50

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
                    del enemy_stats.drop_table_items[:]
                    del enemy_stats.drop_table_weapons[:]
                    del enemy_stats.drop_table_armor[:]
                    del enemy_stats.drop_table_helmets[:]
                    del enemy_stats.drop_table_shields[:]

                for item in enemy_stats.drop_table_items_always:
                    item.amount = 1
                    enemy_stats.drop_table_items.append(item)

                for item in all_game_items:
                    add_to_table = random.randint(0,20)
                    if add_to_table == 20 and item not in enemy_stats.drop_table_items and item.value >= (enemy_stats.level * 2) and item.value <= (enemy_stats.level * 100):
                        enemy_stats.drop_table_items.append(item)
                        random.shuffle(enemy_stats.drop_table_items)
                if dev_mode >= 1:
                    for item in enemy_stats.drop_table_items:
                        print(item.print_name)

                for weapon in enemy_stats.drop_table_weapons_always:
                    weapon.amount = 1
                    enemy_stats.drop_table_weapons.append(weapon)
                for weapon in all_game_weapons:
                    if weapon not in enemy_stats.drop_table_weapons:
                        if weapon.level <= (enemy_stats.level + 10) and weapon.level >= (enemy_stats.level - 30) and enemy_stats.attribute == weapon.attribute:
                            enemy_stats.drop_table_weapons.append(weapon)
                            random.shuffle(enemy_stats.drop_table_weapons)
                if dev_mode >= 1:
                    for weapon in enemy_stats.drop_table_weapons:
                        print(weapon.print_name)

                for armor in enemy_stats.drop_table_armor_always:
                    armor.amount = 1
                    enemy_stats.drop_table_armor.append(armor)
                for armor in all_game_armor:
                    if armor not in enemy_stats.drop_table_armor:
                        if armor.level <= (enemy_stats.level + 10) and armor.level >= (enemy_stats.level - 30) and enemy_stats.attribute == armor.attribute:
                            enemy_stats.drop_table_armor.append(armor)
                            random.shuffle(enemy_stats.drop_table_armor)
                if dev_mode >= 1:
                    for armor in enemy_stats.drop_table_armor:
                        print(armor.print_name)

                for helmet in enemy_stats.drop_table_helmets_always:
                    helmet.amount = 1
                    enemy_stats.drop_table_helmets.append(helmet)
                for helmet in all_game_helmets:
                    if helmet not in enemy_stats.drop_table_helmets:
                        if helmet.level <= (enemy_stats.level + 10)and helmet.level >= (enemy_stats.level - 30) and enemy_stats.attribute == helmet.attribute:
                            enemy_stats.drop_table_helmets.append(helmet)
                            random.shuffle(enemy_stats.drop_table_helmets)
                if dev_mode >= 1:
                    for helmet in enemy_stats.drop_table_helmets:
                        print(helmet.print_name)

                for shield in enemy_stats.drop_table_shields_always:
                    shield.amount = 1
                    enemy_stats.drop_table_shields.append(shield)
                for shield in all_game_shields:
                    if shield not in enemy_stats.drop_table_shields:
                        if shield.level <= (enemy_stats.level + 10) and shield.level >= (enemy_stats.level - 30) and enemy_stats.attribute == shield.attribute:
                            enemy_stats.drop_table_shields.append(shield)
                            random.shuffle(enemy_stats.drop_table_shields)
                if dev_mode >= 1:
                    for shield in enemy_stats.drop_table_shields:
                        print(shield.print_name)

                if dev_mode >= 1:
                    print("modifying enemy stats")
                enemy_stats.maxhp += (random.randint(20,100) * enemy_stats.level)
                enemy_stats.hp = (0 + enemy_stats.maxhp)
                enemy_stats.gp += ((random.randint(0,10) * enemy_stats.maxhp) // 1000) * enemy_stats.level
                enemy_stats.xp = random.randint((enemy_stats.level // 2),(enemy_stats.level * 3)) + (enemy_stats.maxhp // 100)
                if dev_mode >= 1:
                    print("enemy stats have been calculated")

            player_turns = 3
            if dev_mode >= 1:
                print("playing battle intro")
            if npc_fight == False:
                func_refresh_pygame(True,0)
            else:
                func_refresh_pygame(False,0)
            npc_fight = False
            if dev_mode >= 1:
                print("battle intro finished")
            print(Fore.RED + "\n//////////// YOU ARE NOW IN COMBAT //////////// \n")

    
            print("\nturns left: " + str(player_turns))

            if dev_mode >= 2:
                print("\nEnemy stats:")
                for enemy_stats in current_enemies:
                    status_list = []
                    for status_condition in enemy_stats.status_effect_list:
                        status_list.append(status_condition.name)
                    print("Name: " + enemy_stats.print_name)
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

                #pygame.time.delay(tick_delay_time)

                func_refresh_pygame(False,0)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_start = 0
                        in_fight = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            func_move_combat_cursor(True)
                        if event.key == pygame.K_s:
                            func_move_combat_cursor(False)
                        if event.key == pygame.K_e:
                            sfx_cursor_select.play()
                            if combat_cursor_pos == 4: #run option
                                run_chance = random.randint(1,len(current_enemies)+1)
                                if run_chance == 1:
                                    in_fight = False
                                    pygame.mixer.music.stop()
                                    print(Fore.GREEN + Style.BRIGHT + "\nyou ran away! \n" + Style.RESET_ALL)
                                    del current_enemies[:]
                                    location_desc()
                                else:
                                    print(Fore.RED + Style.BRIGHT + "\nyou couldn't escape!\n" + Style.RESET_ALL)
                                    func_player_status_check(False,True)
                                    player_turns -= 1

                            elif combat_cursor_pos == 1: #hit option
                                func_player_status_check(True,False)
                                func_check_enemy_dead()
                                player_turns -= 1

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

                                    #pygame.time.delay(tick_delay_time)

                                    func_refresh_pygame(False,0)


                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            game_start = 0
                                            in_fight = False
                                            in_submenu = False
                                            in_submenu_cast_combat = False

                                        elif event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_w:
                                                func_move_combat_cursor(True)
                                            if event.key == pygame.K_s:
                                                func_move_combat_cursor(False)
                                            if event.key == pygame.K_q:
                                                func_reset_cursor_pos()
                                                in_submenu = False
                                                in_submenu_cast_combat = False
                                            if event.key == pygame.K_e:
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
                                                

                                                in_submenu = False
                                                in_submenu_cast_combat = False
                                                break



                            elif combat_cursor_pos == 3: #use option
                                func_player_status_check(False,True)
                                func_use_combat(item,inventory)
                                func_check_enemy_dead()

                            elif combat_cursor_pos == 6:
                                if dev_mode >= 1:
                                    player_turns = 0
                                    player1.hp = player1.maxhp


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


        if in_fight == False: #end of combat
            
            #get loot and xp from enemies
            for enemy_stats in dead_enemies:
                func_enemy_dead(enemy_stats)

            dead_enemies.clear()
            #update player's level
            func_check_level()

            location_desc()
            if dev_mode >=3:
                func_HUD()

        has_moved = False

    player1.status_effect_list.clear()# potentially do not want to do this in order for items that remove status fx to have a use
    
    func_check_stat_bonus()
    func_check_level()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_start = 0
            pygame.quit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_F1:
                if dev_mode >= 0:
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
                        func_tp((int(tpx_entry.get()),int(tpy_entry.get()),int(tpz_entry.get())))


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
                                        item.amount += 1
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
                                        weapon.amount += 1
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
                                        armor.amount += 1
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
                                        helmet.amount += 1
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
                                        shield.amount += 1
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

            if event.key == pygame.K_F2:
                for player1 in players:
                    print("|| Stats: \n")
                    print("|| Name: " + player1.name)
                    print("|| Level: " + str(player1.level))
                    print("|| xp: " + str(player1.xp))
                    print("|| gold: " + str(player1.gp))
                    print("|| hp: " + str(player1.hp) + " / " + str(player1.nobonus_maxhp) + " || + " + str(player1.maxhp_bonus))
                    print("|| mp: " + str(player1.mp) + " / " + str(player1.nobonus_maxmp) + " || + " + str(player1.maxmp_bonus))

                    print("|| Magic: " + str(player1.magic) + " || + " + str(player1.magic_bonus) + " || xp: " + str(player1.magic_xp))
                    print("|| Strength: " + str(player1.strength) + " || + " + str(player1.strength_bonus) + " || xp: " + str(player1.strength_xp))
                    print("|| Attack: " + str(player1.attack) + " || + " + str(player1.attack_bonus) + " || xp: " + str(player1.attack_xp))
                    print("|| Defence: " + str(player1.defence) + " || + " + str(player1.defence_bonus) + " || xp: " + str(player1.defence_xp))

                    print("|| Skills: \n")
                    print("|| Fishing: " + str(player1_skills.fishing) + " || xp: " + str(player1_skills.fishing_xp))
                    print("|| Theiving: " + str(player1_skills.thieving) + " || xp: " + str(player1_skills.thieving_xp))
                    print("|| Alchemy: " + str(player1_skills.alchemy) + " || xp: " + str(player1_skills.alchemy_xp))
                    print("|| Cooking: " + str(player1_skills.cooking) + " || xp: " + str(player1_skills.cooking_xp))

            if event.key == pygame.K_F3:
                if dev_mode >= 0:
                    if dev_mode >= 0:
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
                    print("\nInventory: \n")

                    if len(inventory) != 0:
                        for item in inventory:

                            print("|| " + item.print_name + " x " + str(item.amount))

                    if len(spell_inventory) != 0:
                        for spell in spell_inventory:

                            print("|| " + spell.print_name + " || " + spell.print_attribute + " || lvl: " + str(spell.level))

                    if len(helmet_inventory) != 0:
                        for helmet in helmet_inventory:

                            print("|| " + helmet.print_name + " x " + str(helmet.amount) + " || attribute: " + helmet.print_attribute + " || type: " + helmet.type + " || lvl: " + str(helmet.level))

                    if len(armor_inventory) != 0:
                        for armor in armor_inventory:

                            print("|| " + armor.print_name + " x " + str(armor.amount) + " || attribute: " + armor.print_attribute + " || type: " + armor.type + " || lvl: " + str(armor.level))

                    if len(shield_inventory) != 0:
                        for shield in shield_inventory:

                            print("|| " + shield.print_name + " x " + str(shield.amount) + " || attribute: " + shield.print_attribute + " || type: " + shield.type + " || lvl: " + str(shield.level))

                    if len(weapon_inventory) != 0:
                        for weapon in weapon_inventory:

                            print("|| " + weapon.print_name + " x " + str(weapon.amount) + " || attribute: " + weapon.print_attribute + " || type: " + weapon.type + " || lvl: " + str(weapon.level))

                    print("")

            if event.key == pygame.K_F4:
                dev_mode += 1
                if dev_mode > 6:
                    dev_mode = 0
                print("dev mode " + str(dev_mode))

            if event.key == pygame.K_F5:
                in_fight = True

            if event.key == pygame.K_w:
                sfx_player_move.play()
                if player_direction == 0 and check_collision((0,-1)):
                        has_moved = True
                        steps_y -= 1
                        prev_y = steps_y
                        prev_y += 1

                player_direction = 0
                check_player_direction()

            if event.key == pygame.K_s:
                sfx_player_move.play()

                if player_direction == 2 and check_collision((0,1)):
                    has_moved = True
                    steps_y += 1
                    prev_y = steps_y
                    prev_y -= 1

                player_direction = 2
                check_player_direction()

            if event.key == pygame.K_d:
                sfx_player_move.play()

                if player_direction == 1 and check_collision((1,0)):
                    has_moved = True
                    steps_x += 1
                    prev_x = steps_x
                    prev_x -= 1


                player_direction = 1
                check_player_direction()

            if event.key == pygame.K_a:
                sfx_player_move.play()

                if player_direction == 3 and check_collision((-1,0)):
                    has_moved = True
                    steps_x -= 1
                    prev_x = steps_x
                    prev_x += 1

                player_direction = 3
                check_player_direction()

            if event.key == pygame.K_x:
                print(f"fps: {clock.get_fps()}")

            if event.key == pygame.K_e:
                sfx_player_select.play()
                check_player_direction()

                interacted_tile = None
                if player_direction == 0:
                    interacted_tile = player_north_check()

                if player_direction == 2:
                    interacted_tile = player_south_check()

                if player_direction == 1:
                    interacted_tile = player_east_check()

                if player_direction == 3:
                    interacted_tile = player_west_check()

                if interacted_tile: # if interated tile has a telport location, tp the player to that location
                    if interacted_tile.has_tp:
                        func_tp(interacted_tile.tp_location)

                del nearby_npc_list [:]

                if interacted_tile: #if you interacted with something
                    if interacted_tile.npc_list:
                            in_menu = True
                            if True:
                                target_npc = "0"
                                for npc in interacted_tile.npc_list:
                                    print("|| " + npc.first_name + " " + npc.last_name + ", " + npc.title + " || " + npc.npc_desc)

                                print("\nWho will you talk too? \n")

                                in_submenu = True
                                in_submenu_talk = True
                                npc_found = False
                                while in_submenu_talk == True:

                                    func_check_level()
                                    func_refresh_pygame(False,0)


                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            game_start = 0
                                            func_close_all_menus()
                                        elif event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_w:
                                                func_move_cursor(True)
                                            if event.key == pygame.K_s:
                                                func_move_cursor(False)
                                            if event.key == pygame.K_q:
                                                func_reset_cursor_pos()
                                                func_close_all_menus()

                                            if event.key == pygame.K_e:
                                                sfx_cursor_select.play()
                                                val_dropped_item = menu_cursor_pos
                                                val_drop = val_dropped_item - 1
                                                for npc in nearby_npc_list:
                                                    if val_drop == nearby_npc_list.index(npc):
                                                        target_npc = npc.first_name
                                                        npc_found = True

                                                        for npc in nearby_npc_list:
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

                                                                    #pygame.time.delay(tick_delay_time)

                                                                    func_check_level()
                                                                    func_refresh_pygame(False,0)



                                                                    for event in pygame.event.get():
                                                                        if event.type == pygame.QUIT:
                                                                            game_start = 0
                                                                            in_fight = False
                                                                            in_submenu2 = False
                                                                            in_submenu_talk2 = False
                                                                            in_menu = False
                                                                        elif event.type == pygame.KEYDOWN:
                                                                            if event.key == pygame.K_w:
                                                                                func_move_cursor(True)
                                                                            if event.key == pygame.K_s:
                                                                                func_move_cursor(False)
                                                                            if event.key == pygame.K_q:
                                                                                func_reset_cursor_pos()
                                                                                in_submenu2 = False
                                                                                in_submenu_talk2 = False

                                                                            if event.key == pygame.K_e:
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
                                                                                                        # in_submenu2 = False
                                                                                                        # in_submenu_talk2 = False
                                                                                                        break
                                                                                                    if dialouge_option.is_buy_armor == True:
                                                                                                        func_shop(armor,npc.npc_armor_inventory)
                                                                                                        # in_submenu2 = False
                                                                                                        # in_submenu_talk2 = False
                                                                                                        break
                                                                                                    if dialouge_option.is_buy_helmet == True:
                                                                                                        func_shop(helmet,npc.npc_helmet_inventory)
                                                                                                        # in_submenu2 = False
                                                                                                        # in_submenu_talk2 = False
                                                                                                        break
                                                                                                    if dialouge_option.is_buy_shield == True:
                                                                                                        func_shop(armor,npc.npc_shield_inventory)
                                                                                                        # in_submenu2 = False
                                                                                                        # in_submenu_talk2 = False
                                                                                                        break

                                                                                                    if dialouge_option.is_buy_item == True:
                                                                                                        func_shop(item,npc.npc_inventory)
                                                                                                        # in_submenu2 = False
                                                                                                        # in_submenu_talk2 = False
                                                                                                        # break
                                                                                                    if dialouge_option.is_buy_spell == True:
                                                                                                        func_shop(spell,npc.npc_spell_inventory)
                                                                                                        # in_submenu2 = False
                                                                                                        # in_submenu_talk2 = False
                                                                                                        break

                                                                                                    if dialouge_option.is_talk == True:
                                                                                                        if npc.is_animal == True:
                                                                                                            print("You cannot speak with animals")
                                                                                                        if npc.is_animal == False:
                                                                                                            print(npc.talk_text)
                                                                                                            for quest in quest_list:
                                                                                                                if quest.started == True and quest.quest_talk_npc == True:
                                                                                                                    if quest.quest_npc_fname == target_npc:
                                                                                                                        quest.finished = True
                                                                                                                        print(quest.name + " is ready to turn in!")


                                                                                                    if dialouge_option.is_sell == True:
                                                                                                        if dev_mode >= 2:
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

                                                                                                            #pygame.time.delay(tick_delay_time)

                                                                                                            func_check_level()
                                                                                                            func_refresh_pygame(False,0)



                                                                                                            for event in pygame.event.get():
                                                                                                                if event.type == pygame.QUIT:
                                                                                                                    game_start = 0
                                                                                                                    in_fight = False
                                                                                                                    in_submenu3 = False
                                                                                                                    in_submenu_sell3 = False
                                                                                                                    in_menu = False
                                                                                                                if event.type == pygame.KEYDOWN:
                                                                                                                    if event.key == pygame.K_w:
                                                                                                                        func_move_cursor(True)
                                                                                                                    if event.key == pygame.K_s:
                                                                                                                        func_move_cursor(False)
                                                                                                                    if event.key == pygame.K_q:
                                                                                                                        func_reset_cursor_pos()
                                                                                                                        in_submenu3 = False
                                                                                                                        in_submenu_sell3 = False
                                                                                                                    if event.key == pygame.K_e:
                                                                                                                        sfx_cursor_select.play()
                                                                                                                        if menu_cursor_pos == 1:
                                                                                                                            func_sell(item,inventory)
                                                                                                                            func_check_quest_items()
                                                                                                                            # in_submenu3 = False
                                                                                                                            # in_submenu_sell3 = False
                                                                                                                            # # break
                                                                                                                        if menu_cursor_pos == 2:
                                                                                                                            func_sell(weapon,weapon_inventory)
                                                                                                                            # in_submenu3 = False
                                                                                                                            # in_submenu_sell3 = False
                                                                                                                            # break
                                                                                                                        if menu_cursor_pos == 3:
                                                                                                                            func_sell(armor,armor_inventory)
                                                                                                                            # in_submenu3 = False
                                                                                                                            # in_submenu_sell3 = False
                                                                                                                            # break
                                                                                                                        if menu_cursor_pos == 4:
                                                                                                                            func_sell(helmet,helmet_inventory)
                                                                                                                            # in_submenu3 = False
                                                                                                                            # in_submenu_sell3 = False
                                                                                                                            # break
                                                                                                                        if menu_cursor_pos == 5:
                                                                                                                            func_sell(shield,shield_inventory)
                                                                                                                            # in_submenu3 = False
                                                                                                                            # in_submenu_sell3 = False
                                                                                                                            # break
                                                                                                                        if menu_cursor_pos == 6:
                                                                                                                            func_sell(spell,spell_inventory)

                                                                                                    if dialouge_option.is_assault == True:
                                                                                                        print(npc.assault_dialouge)
                                                                                                        current_enemies.extend(npc.combat_enemy_list)
                                                                                                        npc_enemy_fname = npc.first_name
                                                                                                        npc_enemy_lname = npc.last_name

                                                                                                        is_talking = False
                                                                                                        in_submenu2 = False
                                                                                                        in_submenu_talk2 = False
                                                                                                        in_menu = False

                                                                                                        in_fight = True
                                                                                                        npc_fight = True

                                                                                                        break

                                                                                                    if dialouge_option.is_give == True:
                                                                                                        print("execute func_give_item")
                                                                                                        # in_submenu2 = False
                                                                                                        # in_submenu_talk2 = False
                                                                                                        # break

                                                                                                    if dialouge_option.is_quest == True:
                                                                                                        for quest in quest_list:
                                                                                                            if quest.name == dialouge_option.quest_name and quest.started == False:
                                                                                                                print("starting " + dialouge_option.quest_name)
                                                                                                                quest.started = True
                                                                                                                break

                                                                                                            if quest.name == dialouge_option.quest_name and quest.started == True and quest.finished == False:
                                                                                                                print("you have already started! " + dialouge_option.quest_name)
                                                                                                                break

                                                                                                            if quest.name == dialouge_option.quest_name and quest.finished == True and quest.reward_collected == True:
                                                                                                                print("you have already finished! " + dialouge_option.quest_name)
                                                                                                                break

                                                                                                            if quest.name == dialouge_option.quest_name and quest.finished == True and quest.reward_collected == False:
                                                                                                                if quest.quest_collect_item == True:
                                                                                                                    for item in inventory:
                                                                                                                        if item.name == quest.quest_item_name:
                                                                                                                            item.amount -= quest.quest_item_amount
                                                                                                                            if item.amount <= 0:
                                                                                                                                inventory.remove(item)

                                                                                                                print(dialouge_option.quest_name + " completed!")
                                                                                                                print("Thankyou, " + player1.name + " here is your reward ")

                                                                                                                if len(quest.reward_list) != 0:
                                                                                                                    for item in quest.reward_list:
                                                                                                                        inventory.append(item)
                                                                                                                        print("\nYou received a " + item.name)

                                                                                                                print("\nGained " + str(quest.xp) + " xp and " + str(quest.gp) + " gp.")
                                                                                                                quest.reward_collected = True
                                                                                                                player1.xp += quest.xp
                                                                                                                player1.gp += quest.gp

                                                                                                                break


                                                                                                        break

                                                                                                    if dialouge_option.is_heal == True:
                                                                                                        print("\nHealed by the doctor!\n")
                                                                                                        player1.hp = player1.maxhp

                                                                                                        break

                                                                                                    # break

                                                                                # in_submenu2 = False
                                                                                # in_submenu_talk2 = False
                                                                                # break



                                                                current_npc.remove(npc)

                                                in_submenu = False
                                                in_submenu_talk = False
                                                break
                    
                    
                    
                    
                    
                    
                    
                    else:
                        pass

                in_menu = False
                break

            if event.key == pygame.K_SPACE:
                sfx_player_select.play()
                func_reset_cursor_pos()
                current_menu = menus.root
                in_menu = True
                while in_menu == True:
                    func_check_level()
                    func_refresh_pygame(False,0)
  
                    for event in pygame.event.get():

                        check_quit(event)
                        check_cursor_moved(event)
 
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                func_reset_cursor_pos()
                                if current_menu.parent == None:
                                    in_menu = False
                                    print(f"top menu quit")
                                    current_menu = None
                                else:
                                    old_menu = current_menu
                                    print(f"{current_menu.name} menu quit")
                                    current_menu = current_menu.parent
                                    menu_cursor_pos = current_menu.children.index(old_menu)+1

                                break

                            if event.key == pygame.K_e:
                                sfx_cursor_select.play()
                                #equip 
                                if current_menu.children:
                                    if len(current_menu.children) > menu_cursor_pos - 1:
                                        current_menu = current_menu.children[menu_cursor_pos-1]
                                        func_reset_cursor_pos()
                                        print(f'menu: {current_menu.name}')
                                    
                                else: 
                                    print(f'leaf menu: {current_menu.name}')
                                    #if leaf node is currently active
                                    if current_menu.data:
                                        #checking that the list is not empty before referencing it prevents error

                                        #inventory menu
                                        if isinstance(current_menu.data[0],item):
                                            #intereract with the object stored in the list  
                                            func_use(inventory)

                                        #equip menus
                                        elif isinstance(current_menu.data[0],weapon):
                                            #intereract with the object stored in the list
                                            func_equip(weapon_inventory,equiped_weapon)

                                        elif isinstance(current_menu.data[0],armor):
                                            #intereract with the object stored in the list
                                            func_equip(armor_inventory,equiped_armor)

                                        elif isinstance(current_menu.data[0],helmet):
                                            #intereract with the object stored in the list
                                            func_equip(equiped_helmet,equiped_helmet)

                                        elif isinstance(current_menu.data[0],shield):
                                            #intereract with the object stored in the list
                                            func_equip(shield_inventory,equiped_shield)
                                            
                                        elif isinstance(current_menu.data[0],spell):
                                            #intereract with the object stored in the list
                                            func_equip(spell_inventory,equiped_spells)
                                    else:
                                        print(f'leaf menu: {current_menu.name} - no data in leaf object')
                                    

                                continue
                                if menu_cursor_pos == 4:
                                    func_choose_equip_menu()
                                    
                                #quest log
                                elif menu_cursor_pos == 6:
                                    in_submenu = True
                                    in_submenu_questlog = True
                                    while in_submenu_questlog == True:

                                        #pygame.time.delay(tick_delay_time)

                                        func_check_level()
                                        func_refresh_pygame(False,0)

                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                game_start = 0
                                                in_fight = False
                                                in_submenu = False
                                                in_submenu_questlog = False
                                                in_menu = False
                                            elif event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_w:
                                                    func_move_cursor(True)

                                                if event.key == pygame.K_s:
                                                    func_move_cursor(False)

                                                if event.key == pygame.K_q:
                                                    func_reset_cursor_pos()
                                                    in_submenu = False
                                                    in_submenu_questlog = False

                                                if event.key == pygame.K_e:

                                                    val_selected_quest = menu_cursor_pos
                                                    val_quest = val_selected_quest - 1
                                                    for quest in quest_list:
                                                        if val_quest == quest_list.index(quest):
                                                            selected_quest = quest.name

                                                    for quest in quest_list:
                                                        if quest.name == selected_quest:
                                                            print("\n" + quest.name)
                                                            print("\n" + quest.quest_desc)
                                                            print(quest.quest_info)

                                #drop
                                elif menu_cursor_pos == 7:
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

                                        #pygame.time.delay(tick_delay_time)

                                        func_check_level()
                                        func_refresh_pygame(False,0)




                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                game_start = 0
                                                in_fight = False
                                                in_submenu = False
                                                in_submenu_drop = False
                                                in_menu = False
                                            elif event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_w:
                                                    func_move_cursor(True)
                                                if event.key == pygame.K_s:
                                                    func_move_cursor(False)
                                                if event.key == pygame.K_q:
                                                    func_reset_cursor_pos()
                                                    in_submenu = False
                                                    in_submenu_drop = False

                                                if event.key == pygame.K_e:
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
                               
                                #use
                                elif menu_cursor_pos == 2:
                                    func_use(item,inventory)
                                #skills
                                elif menu_cursor_pos == 1:

                                    in_submenu = True
                                    in_submenu_action = True
                                    while in_submenu_action == True:

                                        #pygame.time.delay(tick_delay_time)

                                        func_check_level()
                                        func_refresh_pygame(False,0)

                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                game_start = 0
                                                in_fight = False
                                                in_submenu = False
                                                in_submenu_action = False
                                                in_menu = False
                                            elif event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_w:
                                                    func_move_cursor(True)
                                                if event.key == pygame.K_s:
                                                    func_move_cursor(False)

                                                if event.key == pygame.K_q:
                                                    func_reset_cursor_pos()
                                                    in_submenu = False
                                                    in_submenu_action = False

                                                if event.key == pygame.K_e:
                                                    sfx_cursor_select.play()

                                                    if menu_cursor_pos == 1:
                                                        stolen_item = "0"
                                                        for scene_type in location:
                                                            if scene_type.can_steal == True:
                                                                for item in all_game_items:
                                                                    steal_chance = random.randint(0,10)
                                                                    if steal_chance == 10:
                                                                        print("you steal " + item.name)
                                                                        player1_skills.thieving_xp += item.value
                                                                        func_check_level()
                                                                        stolen_item = item.name
                                                                        break

                                                                has_item_multiple = False

                                                                for item in inventory:
                                                                    if item.name == stolen_item:
                                                                        has_item_multiple = True
                                                                        item.amount += 1
                                                                        break
                                                                if has_item_multiple == False:
                                                                    for item in all_game_items:
                                                                        if item.name == stolen_item:
                                                                            inventory.append(item)
                                                                            break

                                                            else:
                                                                print("You cannot steal from here")

                                                    if menu_cursor_pos == 2:
                                                        fish_caught = "0"
                                                        has_rod = False
                                                        for scene_type in location:
                                                            if scene_type.can_fish == True:
                                                                for item in inventory:
                                                                    if item.name == "fishing rod":
                                                                        has_rod = True

                                                                if has_rod == True:
                                                                    for item in all_game_items:
                                                                        if item.is_fish == True:
                                                                            fish_chance = random.randint(0,10)
                                                                            if fish_chance == 10:
                                                                                print("you catch a " + item.name)
                                                                                player1_skills.fishing_xp += item.value
                                                                                func_check_level()
                                                                                fish_caught = item.name
                                                                                break
                                                                else:
                                                                    print("you do not have a fishing rod!")

                                                                has_item_multiple = False

                                                                for item in inventory:
                                                                    if item.name == fish_caught:
                                                                        has_item_multiple = True
                                                                        item.amount += 1
                                                                        break
                                                                if has_item_multiple == False:
                                                                    for item in all_game_items:
                                                                        if item.name == fish_caught:
                                                                            inventory.append(item)
                                                                            break

                                                            else:
                                                                print("You cannot fish here")

                                                    if menu_cursor_pos == 3:
                                                        func_cook(item,inventory)

                                                    if menu_cursor_pos == 4:
                                                        print("func_alchemy")

                                                    if menu_cursor_pos == 5:
                                                        for scene_type in location:
                                                            if scene_type.treasure == True:
                                                                func_search_treasure(location)
                                                                scene_type.treasure = False
                                                            else:
                                                                print("there is nothing here...\n")

                            ################################################

                                #cast
                                elif menu_cursor_pos == 3:
                                    func_cast(spell,equiped_spells)
                                #spellbook
                                elif menu_cursor_pos == 5:
                                    print("\nequiped spells:")
                                    for spell in equiped_spells:
                                        print("|| " + spell.print_name + " || " + spell.print_attribute + " || " + spell.spell_desc)
                                    print("")
                                    print("spell scrolls:")
                                    for spell in spell_inventory:
                                        print("|| " + spell.print_name + " || " + spell.print_attribute + " || " + spell.spell_desc)
                                    print("")


                            ################################################

                                elif menu_cursor_pos == 18:
                                    game_start = 0
                                    break

                                else:
                                    print("invalid command\n")


#######################################################################################

    if dev_mode >= 2:
        time_var = 100
    else:
        time_var = 10

    if time_latch == False:
        time += time_var
        time2 += time_var

    if time_latch == True:
        time -= time_var
        time2 -= time_var

    if time >= 2400:
        time_latch = True
        #print("\nit is midday...\n")

    if time <= 0:
        time_latch = False

        #print("\nit is midnight...\n")

        days += 1

        #print("\nIt is the " + str(days) + " - " + str(months) +" - " + str(years))

        if days >= 30:
            days = 1
            months += 1
            print(f"\nThe month is now: {months}")
            if months >= 13:
                months = 1
                years += 1
                print(f"\nThe year is now: {years}")
                

    if game_start == 0:
        break

#end of script
pygame.quit()
