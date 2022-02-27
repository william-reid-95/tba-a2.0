

class MenuNode:
    def __init__ (self, name, data = [], stackable_data = False):
        self.name = name
        self.data = data
        self.stackable_data = stackable_data #is the object in the data list stackable
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

#def build_menu_tree():

root = MenuNode("Menu")

skills = MenuNode("Skills")
items = MenuNode("Items", stackable_data = True)
cast = MenuNode("Cast")
equip = MenuNode("Equip")
quests = MenuNode("Quests")
drop = MenuNode("Drop")

equip_spell = MenuNode("Equip Spell",stackable_data = True)
equip_weapon = MenuNode("Equip Weapon",stackable_data = True)
equip_armor = MenuNode("Equip Armor",stackable_data = True)
equip_helmet = MenuNode("Equip Helmet",stackable_data = True)
equip_shield = MenuNode("Equip Shield",stackable_data = True)

equip.add_child(equip_spell)
equip.add_child(equip_weapon)
equip.add_child(equip_armor)
equip.add_child(equip_helmet)
equip.add_child(equip_shield)

root.add_child(skills)
root.add_child(items)
root.add_child(cast)
root.add_child(equip)
root.add_child(quests)
root.add_child(drop)

    #return root


#menu = build_menu_tree()