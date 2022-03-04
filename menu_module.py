

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

##dialouge

dialouge_root = MenuNode("Dialouge Menu")

#dialouge options with children
dialouge_shop_buy = MenuNode("Buy") # purchase items/spells/gear
dialouge_shop_sell = MenuNode("Sell") # sell items/spells/gear

#leaves with data
dialouge_quests = MenuNode("Quests") # start/finish quests
dialouge_talk = MenuNode("Talk") # get informaiton about npc/world classic dialouge menu

#leaves with no data - actions
dialouge_attack = MenuNode("Fight")#init combat with npc
dialouge_heal = MenuNode("Heal")#heal the player and/or restore mana of party (SHOULD COST GOLD?)
dialouge_give = MenuNode("Give")#have npc give player an item


#item lists / inventories

buy_item = MenuNode("Buy Items", stackable_data = True)
buy_spell = MenuNode("Buy Spell", stackable_data = True)
buy_weapon = MenuNode("Buy Weapon", stackable_data = True)
buy_armor = MenuNode("Buy Armor", stackable_data = True)
buy_helmet = MenuNode("Buy Helmet", stackable_data = True)
buy_shield = MenuNode("Buy Shield", stackable_data = True)

sell_item = MenuNode("Sell Items", stackable_data = True)
sell_spell = MenuNode("Sell Spell", stackable_data = True)
sell_weapon = MenuNode("Sell Weapon", stackable_data = True)
sell_armor = MenuNode("Sell Armor", stackable_data = True)
sell_helmet = MenuNode("Sell Helmet", stackable_data = True)
sell_shield = MenuNode("Sell Shield", stackable_data = True)

dialouge_shop_buy.add_child(buy_item)
dialouge_shop_buy.add_child(buy_spell)
dialouge_shop_buy.add_child(buy_weapon)
dialouge_shop_buy.add_child(buy_armor)
dialouge_shop_buy.add_child(buy_helmet)
dialouge_shop_buy.add_child(buy_shield)

dialouge_shop_sell.add_child(sell_item)
dialouge_shop_sell.add_child(sell_spell)
dialouge_shop_sell.add_child(sell_weapon)
dialouge_shop_sell.add_child(sell_armor)
dialouge_shop_sell.add_child(sell_helmet)
dialouge_shop_sell.add_child(sell_shield)

dialouge_root.add_child(dialouge_shop_buy)
dialouge_root.add_child(dialouge_shop_sell)

dialouge_root.add_child(dialouge_quests)
dialouge_root.add_child(dialouge_talk)
dialouge_root.add_child(dialouge_attack)
dialouge_root.add_child(dialouge_heal)
dialouge_root.add_child(dialouge_give)
