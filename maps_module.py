#maps

all_maps = []

class Map:
    def __init__(self,z,map):
        self.z = z
        self.map = map
    
        all_maps.append(self)

# KEY:
# X = Wall
# . = Floor
# $ = Chest
# W = Water
# D = Door


dungeon_lvl1 = Map(-1000,[
"XXXXXXXXXX",
"X...X$..XX",
"X.......XX",
"X..XXXX.XX",
"X..XXX..XX",
"X..XXX..XX",
"X..XXXX.XX",
"X.......XX",
"X.D.XXXXXX",
"XXXXXXXXXX"
])

dungeon_lvl2 = Map(-1001,[
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
])