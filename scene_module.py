import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style
import pygame

pygame.init()
init(autoreset=True)

from maps_module import *
from map_sprites_module import *

all_scene_types = []

class scene_type:
    def __init__(self, xpos, ypos, zpos, name, biome, safe, passable, wall = False, treasure = False, indoors = True, has_tp = False, tp_location = None, tile_type = None):
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos
        self.name = name
        self.biome = biome
        self.safe = safe
        self.passable = passable
        self.wall = wall
        self.treasure = treasure #has a chest
        self.indoors = indoors # dictates weather to use map icon or player spirte
        self.has_tp = has_tp
        self.tp_location = tp_location
        self.tile_type = tile_type

        self.can_fish = False
        self.can_cook = False
        self.can_craft = False
        self.can_steal = False

        self.npc_list = []

        self.scene_inventory = []
        self.scene_weapon_inventory = []
        self.scene_armor_inventory = []
        self.scene_helmet_inventory = []
        self.scene_shield_inventory = []
        
        self.tile_sprite = spr_town
        self.deco_sprite = None

        self.rare_item_chance = random.randint(1,10)

        self.difficulty = 1
        if self.zpos <= -1000:
            self.difficulty = ((self.zpos * - 1) -1000) * 3

        self.difficulty += 1

        all_scene_types.append(self)

        self.tile_r = 0
        self.tile_g = 255
        self.tile_b = 229

    def generate_sprite_positions(self):

        if len(self.npc_list) != 0:
            self.passable = False
        if self.treasure == True:
            self.passable = False

        if self.zpos >= -10:
            self.safe = True

        if self.biome == "water":
            self.can_fish = True
        else:
            self.can_fish = False

        if self.wall:
            self.tile_sprite = spr_river

        if self.passable or self.treasure:
            if self.tile_type: #if tile was passed a floor type in gernation
                
                '''
                # ▒ = stone floor | ░ = stone floor 2 
                # . = cobble      | , = cobble 2
                # @ = swirl,      | & = swirl 2
                # G = grass floor | g = grass floor 2
                '''

                if self.tile_type == "▒":
                    self.tile_sprite = spr_dungeon_floor
                if self.tile_type == "░":
                    self.tile_sprite = spr_dungeon_floor2
               
                if self.tile_type == ",":
                    self.tile_sprite = spr_dungeon_cobble
                if self.tile_type == ".":
                    self.tile_sprite = spr_dungeon_cobble2
               
                if self.tile_type == "@":
                    self.tile_sprite = spr_dungeon_swirl
                if self.tile_type == "&":
                    self.tile_sprite = spr_dungeon_swirl2
               
                if self.tile_type == "G":
                    self.tile_sprite = spr_dungeon_grass
                if self.tile_type == "g":
                    self.tile_sprite = spr_dungeon_grass2

            else: 
                self.tile_sprite = spr_dungeon_floor2 #default floor tile

        if self.biome == "seaside":
            self.name = (Fore.CYAN + Style.NORMAL + self.name + Style.RESET_ALL)

        elif self.biome == "water":
            self.name = (Fore.BLUE + Style.NORMAL + self.name + Style.RESET_ALL)

        elif self.biome == "forest":
            self.name = (Fore.GREEN + Style.NORMAL + self.name + Style.RESET_ALL)

        elif self.biome == "town":
            self.name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)

        elif self.biome == "desert":
            self.name = (Fore.YELLOW + Style.NORMAL + self.name + Style.RESET_ALL)

        elif self.biome == "grassy":
            self.name = (Fore.GREEN + Style.DIM + self.name + Style.RESET_ALL)

        elif self.biome == "cave":
            self.name = (Fore.MAGENTA + Style.DIM + self.name + Style.RESET_ALL)

        elif self.biome == "house":
            self.name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)
           
        elif self.biome == "dungeon":
            self.name = (Fore.BLACK + Style.BRIGHT + self.name + Style.RESET_ALL)

        else:
            self.name = (Fore.RED + Style.DIM + self.name + Style.RESET_ALL)
            self.tile_r = 255
            self.tile_g = 0
            self.tile_b = 0

    def auto_tile(self,local_tiles):
        if self.zpos <= -1000:
            if self.passable == False and self.wall == True:

                self.wall_N = False
                self.wall_E = False
                self.wall_S = False
                self.wall_W = False

                self.floor_N = False
                self.floor_E = False
                self.floor_S = False
                self.floor_W = False

                for tile in local_tiles:
                    if tile.zpos == self.zpos:
                        if tile.wall == True and tile.passable == False:

                            #north
                            if tile.ypos == self.ypos - 1 and tile.xpos == self.xpos:
                                self.wall_N = True
                            #east
                            if tile.xpos == self.xpos + 1 and tile.ypos == self.ypos:
                                self.wall_E = True
                            #south
                            if tile.ypos == self.ypos + 1 and tile.xpos == self.xpos:
                                self.wall_S = True
                            #west
                            if tile.xpos == self.xpos - 1 and tile.ypos == self.ypos:
                                self.wall_W = True

                        if tile.wall == False and tile.passable == True:

                            if tile.ypos == self.ypos - 1 and tile.xpos == self.xpos:
                                self.floor_N = True
                            #east
                            if tile.xpos == self.xpos + 1 and tile.ypos == self.ypos:
                                self.floor_E = True
                            #south
                            if tile.ypos == self.ypos + 1 and tile.xpos == self.xpos:
                                self.floor_S = True
                            #west
                            if tile.xpos == self.xpos - 1 and tile.ypos == self.ypos:
                                self.floor_W = True
                            

                if self.floor_S:
                    #bottom
                    if self.wall_E and self.wall_W:
                        self.tile_sprite = spr_dungeon_wall_BM
                    if not self.wall_E and self.wall_W:
                        self.tile_sprite = spr_dungeon_wall_BR
                        self.deco_sprite = spr_dungeon_pillar_BR

                    if self.wall_E and not self.wall_W:
                        self.tile_sprite = spr_dungeon_wall_BL
                        self.deco_sprite = spr_dungeon_pillar_BL
                    if not self.wall_E and not self.wall_W:
                        self.tile_sprite = spr_dungeon_wall_B_single


                elif self.wall_S:
                    #top
                    if self.wall_E and self.wall_W:
                        self.tile_sprite = spr_dungeon_wall_TM
                        self.deco_sprite = spr_dungeon_trim
                    
                    if not self.wall_E and self.wall_W:
                        self.tile_sprite = spr_dungeon_wall_TR
                        self.deco_sprite = spr_dungeon_pillar_TR

                    if self.wall_E and not self.wall_W:
                        self.tile_sprite = spr_dungeon_wall_TL
                        self.deco_sprite = spr_dungeon_pillar_TL
                   
                    if not self.wall_E and not self.wall_W:
                        self.tile_sprite = spr_dungeon_wall_T_single
               
               
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

                    #TODO: make tiles in area not passable

                    

def func_overwrite_tile_sprite(x,y,z,sprite):
    for tile in all_scene_types:
        if tile.xpos == x and tile.ypos == y and tile.zpos == z:
            tile.tile_sprite = sprite


def func_map_tiles(generated_map):

    floors = [".",",","▒","░","@","&","G","g"]
    #takes a map object and places tiles in the world
    relative_ypos = 0
    for y in generated_map.map:
        relative_xpos = 0
        for x in y:

            scene_type.ypos = relative_ypos
            scene_type.xpos = relative_xpos

            if x in floors:

                # ▓ = stone floor  ▒ = cobble floor ░ = cobble floor 2 @ = swirl, & = swirl 2
                #G = grass floor, g = grass floor 2
                #floors
                tile = scene_type(relative_xpos,relative_ypos,generated_map.z,
                name = generated_map.name,
                biome = generated_map.biome,
                safe = False,
                passable = True,
                tile_type = x )

            
            if x == "█":
                
                #walls
                tile = scene_type(relative_xpos,relative_ypos,generated_map.z,
                name = generated_map.name,
                biome = generated_map.biome,
                safe = False,
                passable = False,
                wall = True)
                

            if x == "$":
                tile = scene_type(relative_xpos,relative_ypos,generated_map.z,
                name = generated_map.name,
                biome = generated_map.biome,
                safe = False,
                passable = False,
                treasure = True)

            if x == " " or "#":
                pass
            
            if x == "0":
                #door
                tile = scene_type(relative_xpos,relative_ypos,generated_map.z,
                name = generated_map.name,
                biome = generated_map.biome,
                safe = True,
                passable = True,
                has_tp = True,
                tp_location = generated_map.teleports[0])

            if x == "1":
                #door
                tile = scene_type(relative_xpos,relative_ypos,generated_map.z,
                name = generated_map.name,
                biome = generated_map.biome,
                safe = True,
                passable = True,
                has_tp = True,
                tp_location = generated_map.teleports[1])
                
                #add more teleports 

            relative_xpos += 1
        relative_ypos += 1

