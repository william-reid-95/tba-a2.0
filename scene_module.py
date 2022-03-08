import random

import npc_module as npc

from colorama import init
from colorama import Fore, Back, Style

all_scene_types = []

interactive_tiles = []

'''
scene types are interactive objects in the game world
including:

doors and teleporters 
treasure chests and objects with inventories
containers for npcs

'''

class InteractiveTile:
    def __init__(self, xpos, ypos, zpos, treasure = False, has_tp = False, tp_location = None, npc_list = []):
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos
        self.treasure = treasure #has a chest
        self.has_tp = has_tp
        self.tp_location = tp_location # tuple (x,y,z)
        self.npc_list = npc_list

        self.can_fish = False
        self.can_cook = False
        self.can_craft = False
        self.can_steal = False

        self.scene_inventory = []
        self.scene_weapon_inventory = []
        self.scene_armor_inventory = []
        self.scene_helmet_inventory = []
        self.scene_shield_inventory = []
        
        self.tile_sprite = None
        self.deco_sprite = None

        interactive_tiles.append(self)

    def enforce_tile_attributes(self):

        if len(self.npc_list) != 0:
            self.passable = False
        if self.treasure == True:
            self.passable = False
               


def func_place_deco(x,y,z,sprite,solid = False, size = (1,1)):
    for tile in all_scene_types:
        if tile.xpos == x and tile.ypos == y and tile.zpos == z:
            tile.deco_sprite = sprite
            if solid:
                tile.passable = False
                if size[0] > 1 or size [1] > 1:
                    for other_tile in all_scene_types:
                        for i in range(1,size[0]):
                            if other_tile.xpos == x + i and other_tile.ypos == y and other_tile.zpos == z:
                                other_tile.passable = False
                        for i in range(1,size[1]):
                            if other_tile.xpos == x and other_tile.ypos == y + i and other_tile.zpos == z:
                                other_tile.passable = False

def get_interactive_tile_from_xyz(x :int,y :int,z :int) -> InteractiveTile:
    for i in interactive_tiles:
        if i.x == x and i.y == y and i.z == z:
            return i

small_cave_entrance = InteractiveTile(28, 9, 0, has_tp = True, tp_location = (3,3,1))
small_cave_exit = InteractiveTile(3, 2, 1, has_tp = True, tp_location = (28,10,0))

dungeon1_entrance = InteractiveTile(44, 4, 0, has_tp = True, tp_location = (3,3,1))
dungeon1_exit = InteractiveTile(3, 45, 2, has_tp = True, tp_location = (28,10,0))

npc_1 = InteractiveTile(10, 11, 0, npc_list = [npc.npc_cow])


