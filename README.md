# tba-a2.0
RPG by William Reid

package dependancies(pip install):
pygame
colorama
pickle
pytmx

=================================================================================

Details:

An rpg engine developed in python, designed to be extendable/modular
with a simple 3 game areas to start:
- starting island
- town
- cave (combat area)

Features:
- character with stats system
- modular item system, with consumables
- modular equipment system
- shops - buy and sell items, equipmenta and spells
- modular spell system, with buffs, debuffs, status effects, healing and damage
- turn based trpg combat style
- modular enemy system
- simple quest system

create and customise tilemaps using the .tmx extension (reccomend using tiled to do so) 

=================================================================================

Getting started:

run main.py to play

W,A,S,D to move
E to interact, select in menus
Q to go back in menus
SPACE to open menu

combat occurs in the cave
user water fountains to teleport to other locations with "e"
objects with a red square can be interacted with

Config varaible at top of main.py:

dev_mode# prints debug information and shows interactive objects

toggle_music # toggle music

lighting_mode #obsolete

grid_mode #obsolete
