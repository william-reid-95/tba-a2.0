#maps

all_maps = []

class Map:
    def __init__(self,z,name,biome,map,teleports = []):
        self.z = z
        self.name = name
        self.biome = biome
        self.map = map
        self.teleports = teleports # list of tuples, tuple shoudl contain x,y,z coords for teleport

        
    
        all_maps.append(self)

'''
# KEY:
# █ = Wall

# ▒ = stone floor | ░ = stone floor 2 
# . = cobble      | , = cobble 2
# @ = swirl,      | & = swirl 2
# G = grass floor | g = grass floor 2

# $ = Chest
# W = Water
# 0,1,2,3, 9 = teleport
# <space> or # = Nothing

'''

dungeon1 = Map(-1001,"dungeon lvl. 1","dungeon",[
" ████████████████████       ████████████                              ",
" ████████████████████       ████████████                                 ",
" ....GG...,.,...,,.,,       ,...........                              ",
" ...gGgGG........,,.,███████,...........                             ",
" ..g...░░░░g░░...,.,,███████..,,......$.                               ",
" ..G...░g░gGg░.g.,.,,,,,,,,,...,........   ███.████████                                      ",
" .,.,..░gGg░g░.GG...,            .         ███.████████                             ",
" ....G.░ggGgg░g......       █████.██████   ............                               ",
" ..g...░░░G░░░.,.gg..       █████.██████   ........$...                               ",
" ....................       .,..........   ............                             ",
"                            .,..........███......                       ",
"                            .,.$........███......                ",
"                            .,...................                            ",
"                                          ",
],teleports = [(0,0,0)])


overworld = Map(0,"overworld","grassy",[
"gggggggggggggggggggg",
"gggggggggggggggggggg",
"gggggggggggggggggggg",
"gggggggggggggggggggg",
"gggggggggggggggggggg",
"gggggggggggggggggggg",
"gggggggggggggggggggg",
"gggggggggggggggggggg",
"gggggggggggggggggggg",
"gggggggggggggggggggg"
],teleports = [(0,0,0)])


dungeon_lvl2 = Map(-1002,"dungeon lvl. 2","dungeon",[
"XXXXXXXXXX",
"X...X$..XX",
"X.......XX",
"XXXXXXX.XX",
"X..XXX..XX",
"X.......XX",
"X..XXXX.XX",
"X.......XX",
"X.D.XXXXXX",
"XXXXXXXXXX"
],teleports = [(0,0,0)])