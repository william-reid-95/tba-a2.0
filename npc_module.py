import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style
import pygame

pygame.init()
init(autoreset=True)



spr_npc = pygame.image.load("sprites/character.png")


class dialouge_option:
    def __init__(self, text, is_quit, is_buy_item, is_buy_weapon, is_buy_armor, is_buy_helmet, is_buy_shield, is_buy_spell, is_sell, is_talk, is_assault, is_give, is_quest, quest_name, is_heal):
        self.text = text #text displayed for dialouge option
        self.is_quit = is_quit #option to allow user to leave dialouge
        self.is_buy_item = is_buy_item #interprets dialouge option as player wanting to make a purchase
        self.is_buy_weapon = is_buy_weapon #interprets dialouge option as player wanting to make a purchase
        self.is_buy_armor = is_buy_armor #interprets dialouge option as player wanting to make a purchase
        self.is_buy_helmet = is_buy_helmet #interprets dialouge option as player wanting to make a purchase
        self.is_buy_shield = is_buy_shield #interprets dialouge option as player wanting to make a purchase
        self.is_buy_spell = is_buy_spell #interprets dialouge option as player wanting to make a purchase
        self.is_sell = is_sell #interprets dialouge option as player wanting to sell something
        self.is_talk = is_talk #interprets dialouge option as player wanting to talk
        self.is_assault = is_assault #interprets dialouge option as player wanting to attack the npc
        self.is_give = is_give #interprets dialouge option as a trigger to give the player an item
        self.is_quest = is_quest #interprets dialouge option as player wanting a quest
        self.quest_name = quest_name
        self.is_heal = is_heal #etc...


dialouge_buy_item = dialouge_option("buy item",False,True,False,False,False,False,False,False,False,False,False,False,"0",False)
dialouge_buy_weapon = dialouge_option("buy weapons",False,False,True,False,False,False,False,False,False,False,False,False,"0",False)
dialouge_buy_armor = dialouge_option("buy armor",False,False,False,True,False,False,False,False,False,False,False,False,"0",False)
dialouge_buy_helmet = dialouge_option("buy helmets",False,False,False,False,True,False,False,False,False,False,False,False,"0",False)
dialouge_buy_shield = dialouge_option("buy shields",False,False,False,False,False,True,False,False,False,False,False,False,"0",False)
dialouge_buy_spell = dialouge_option("buy spells",False,False,False,False,False,False,True,False,False,False,False,False,"0",False)

dialouge_heal = dialouge_option("ask for healing",False,False,False,False,False,False,False,False,False,False,False,False,"0",True)

dialouge_sell = dialouge_option("can I sell",False,False,False,False,False,False,False,True,False,False,False,False,"0",False)
dialouge_talk = dialouge_option("heard any news?",False,False,False,False,False,False,False,False,True,False,False,False,"0",False)
dialouge_gf = dialouge_option("prepare to die!",False,False,False,False,False,False,False,False,False,True,False,False,"0",False)
dialouge_attack = dialouge_option("attack",False,False,False,False,False,False,False,False,False,True,False,False,"0",False)
dialouge_give = dialouge_option("give me something!",False,False,False,False,False,False,False,False,False,False,True,False,"0",False)
dialouge_quest1 = dialouge_option("quests",False,False,False,False,False,False,False,False,False,False,False,True,"Cow Elite Killer",False)
dialouge_quest2 = dialouge_option("do you have a quest?",False,False,False,False,False,False,False,False,False,False,False,True,"The Bandit Menace",False)
dialouge_quest3 = dialouge_option("do you have a quest?",False,False,False,False,False,False,False,False,False,False,False,True,"Talk to Shmurlitz",False)
dialouge_quest4 = dialouge_option("do you have a quest?",False,False,False,False,False,False,False,False,False,False,False,True,"Travel to Sorrlund",False)
dialouge_quest5 = dialouge_option("do you have a quest?",False,False,False,False,False,False,False,False,False,False,False,True,"Chop Wood",False)



dialouge_quit= dialouge_option("Goodbye",True,False,False,False,False,False,False,False,False,False,False,False,"0",False)

all_npcs = []

class npc:
    def __init__(self, first_name, last_name, title, npc_desc, greeting, is_animal, race, gender, faction, attire, assault_dialouge,talk_text,sprite_val):
        self.first_name = first_name
        self.last_name = last_name
        self.npc_desc = npc_desc
        self.title = title
        self.greeting = greeting
        self.is_animal = is_animal
        self.race = race
        self.gender = gender
        self.faction = faction
        self.attire = attire
        self.assault_dialouge = assault_dialouge
        self.talk_text = talk_text

        self.dialouge_options_list = []
        # self.dialouge_options_list.append(dialouge_quit)
        self.combat_enemy_list = []
        self.quest_list = []

        self.npc_inventory = []
        self.npc_spell_inventory = []
        self.npc_weapon_inventory = []
        self.npc_armor_inventory = []
        self.npc_helmet_inventory = []
        self.npc_shield_inventory = []

        self.sprite_val = sprite_val
        self.npc_sprite = spr_npc
        if self.sprite_val == "m1":
            self.npc_sprite = spr_npc
        if self.sprite_val == "m2":
            self.npc_sprite = spr_npc
        if self.sprite_val == "g1":
            self.npc_sprite = spr_npc
        if self.sprite_val == "cow":
            self.npc_sprite = spr_npc
        if self.sprite_val == "sheep":
            self.npc_sprite = spr_npc


        self.is_dead = False

        all_npcs.append(self)


#########   TWO NPCS CANNOT HAVE THE SAME FIRST NAME !!!!   #############

npc_doctor = npc("Shmurlitz","Durlitz","Doctor","Healing professional","Hello, I am a Dr. Durlitz, I can tend to your wounds if you get injured in battle.",False,"human","man","0","cloth clothes","0","The wizard Greenmichs lives in the forest south-west of here.\nIf he deems you worthy, he will teach you powerful spells!","m1")

npc_jenkins = npc("old man","jenkins","Seer","Good for a chat!","hello",False,"human","man","0","cloth clothes","*the old man transforms into a goblin*","If you can identify an enemy's weakness, you should use magic to exploit it!","m2")
npc_john_doe = npc("John","Dough","Merchant","weapons merchant...","hello",False,"human","man","0","cloth clothes","oof","I wonder if Haney solved her bandit problem?","g1")
npc_jane_doe = npc("Haney","Dunorf","Peasant","runs an item shop...","'ello",False,"human","woman","0","cloth clothes","oof","If you recover items from monsters, sell them to old man jenkins","m1")
npc_wizard_traenus = npc("Neil","Traenus","Head Wizard","a man of magic...","hello",False,"human","man","0","blue wizard robes","oof","I can train you in magic, but you must serve the arts well...","m1")
npc_wizard_marbles = npc("Marbles","the dog","canine magic specialist","a dog of magic...","woof!",True,"dog","cute","0","0","WOOF!","Woof!","m1")
npc_dismurth_smith = npc("George","Smith","Blacksmith","good at making horseshoes...","G'day",False,"dwarf","man","dwavern guild","cloth clothes","oof","My steel will aid you well my friend!","m1")

npc_wizard_jim = npc("Jim","Greenmichs","Wizard","appreciates a fine brew...","yo",False,"human","man","0","blue wizard robes","oof","Would you like a brew?","m1")
npc_wizard_tilly = npc("Tilly","the dog","Wizard","an apprentice wizard puppy...","woof!",True,"dog","puppy","0","cloth clothes","oof","Woof!","m1")


npc_merchant_ollie = npc("Lyo","Zeddecks","Travelling Merchant","an exotic trader...","G'day",False,"human","man","0","fine clothes","oof","","m1")
npc_merchant_dech = npc("Dechyn","Kneepa","Extractor","creative concoctions are his specialty...","G'day",False,"human","man","0","fine clothes","oof","","m1")

npc_wizard_will = npc("William","the wanderer","Traveller","Travels to far away lands","hello",False,"human","man","0","travellers robes","oof","","m2")
npc_wizard_laika = npc("Laika","the dog","Traveller","a travelling hound","woof!",True,"dog","female","0","cloth clothes","oof","","m1")

npc_wizard_pete = npc("Peter","Quicktounge","Poet","a rhyming genius","G'day",False,"human","man","0","cloth clothes","oof","","m1")

npc_lib = npc("Lord","Quas","The mad","a man of many names","G'day",False,"human","man","0","fine clothes","oof","","m1")
npc_king = npc("Daniel","Geedorah","King","known as the crown ruler...","G'day",False,"human","man","0","royal clothes","oof","","m1")
npc_chris_cornwell = npc("Chris","Cornwell","Farmer","has a beautiful garden...","G'day",False,"human","man","0","farmer's clothes","oof","","m1")
npc_dante = npc("Dante","","From the Devil May Cry series","","G'day",False,"human","man","0","Red Jacket","oof","","m1")


npc_cow = npc("cow","","","","moo",True,"cow","large","0","0","Moo!","","cow")
npc_sheep = npc("sheep","","","","baaaa",True,"sheep","wooley","0","0","Baa!","","sheep")

npc_town_guard = npc("Joneses","Keeneye","Town Guard","Keeps an eye on the gate...","hello",False,"human","man","0","chain mail","Prepare to die, invader!","","g1")
