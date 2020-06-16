if len(scene_type.npc_list) == 9999: #this condition will never be met, it just hides a bunch of code i want to keep
    for scene_type in location:
        if scene_type == birds_nest:

            if (not equiped_weapon):
                print("\nHello you look as though you could do with some supplies skwark!")
                print("Here you go!\n")
                inventory.append(worms)
                equiped_weapon.append(bird_sword)
                print("The bird hands you some worms and a sword\n")
                response = input("bird expects a response...\n")
                if response == "skwark!":
                    print("\n I like you skwark!\n")
                else:
                    inventory.remove(worms)
                    print("*the bird snatches your worms and scowls*\n")
            else:
                print("hello welcome to the bird armory skwark!\n")
                response2 = input("would you like to purchase any armor skwark!?\n")
                if response2 == "yes":
                    print("bird shop armory:\n")
                    print("gold: ", player1.gp)
                    for armor in bird_store_armor:
                        print(armor.name + " ----- ", armor.value, " gp. ")
                    bought_item = input("\nplease choose some armor to buy skwark!\n")
                    has_item = False
                    for armor in bird_store_armor:
                        if bought_item == armor.name:
                            has_item = True
                            if player1.gp >= armor.value:
                                player1.gp -= armor.value
                                armor_inventory.append(armor)
                                print("\nthanks, enjoy your " + armor.name + " skwark!\n")
                            else:
                                print("You can't afford that skwark!")
                        if has_item == False:
                            print("\nI don't have " + bought_item + " skwark!\n")

                else:
                    print("okay seeya! skwark!\n")

    for scene_type in location:
        if scene_type == large_tree:

                for item in inventory:
                    if item.name == "worms":
                        has_worms = True

                if has_worms == True:
                    print ("could I please have your worms, I will give you 100 gold!")


                else:
                    print("hello welcome to the bird shop for birds skwark!\n")
                    response = input("would you like to purchase any items?\n")
                    if response == "yes":
                        print("bird shop inventory:\n")
                        print("gold: ", player1.gp)
                        for item in bird_store_inventory:
                            print(item.name + " ----- ", item.value, " gp. ")
                        bought_item = input("please choose an item to buy skwark!\n")
                        has_item = False
                        for item in bird_store_inventory:
                            if bought_item == item.name:
                                has_item = True
                                if player1.gp >= item.value:
                                    player1.gp -= item.value
                                    inventory.append(item)
                                    print("\nthanks, enjoy your " + item.name + " skwark!\n")
                                else:
                                    print("You can't afford that skwark!")
                        if has_item == False:
                            print("I don't have " + bought_item + " skwark!\n")

                        else:

                            print("pardon!? skwark!\n")
                    else:

                        print("okay seeya! skwark!\n")

    for scene_type in location:
        if scene_type == hills:
                print("\nhello I am an old man, I have travelled very far")
                response = input("I found this pendant *cough*, would you like it?\n")
                if response == "yes":
                    if pendant in old_man_inventory:
                        inventory.append(pendant)
                        old_man_inventory.remove(pendant)
                        print("here you are. \n")
                    else:
                        print("it's gone! erhm... *cough* damn theives!\n")
                else:
                    print("erm... herm.. what?\n")

    for scene_type in location:
        if scene_type == forest_cabin:
                print("\nwhat are you doing in my cabin?")
                response = input("do you wish to learn the magic I have created?\n")
                if response == "yes":
                    for player_stats in players:
                        if player_stats.magic >= 10:
                            equiped_spells.append(hydro_barrage)
                            equiped_spells.append(fireball)
                            print("you feel more powerful.. \n")
                        else:
                            print("you are too weak to learn this. Come back when you're stronger!\n")
                if response == "no":
                    print("\nThen what are you doing in my cabin?")

                if response != "yes" and response != "no":
                    print("what?")

    for scene_type in location:
        if scene_type == dismurth_gates:
                print("\nwe are the town guard")
                response = input("Before you can pass, you must answer this question, What is the meaning of life?\n")
                if response == "fat doinks":
                    print("\nYou may enter, for you understand true path of righteousness \n")
                else:
                    print("\njust kidding haha \n")

    for scene_type in location:
        if scene_type == dismurth_square:
                print("\nhello")
                response = input("my name is Sir Kobious, I am from the glorious legion, do you support the legion!?\n")
                if response == "yes":
                    if legion_seal in sir_kobious_inventory:
                        inventory.append(legion_seal)
                        sir_kobious_inventory.remove(legion_seal)
                        print("\nGLORY TO THE LEGION! \n")
                    else:
                        print("\nGLORY TO THE LEGION! \n")
                else:
                    print("Blasphemy I say!\n")

    for scene_type in location:
        if scene_type == dismurth_smith:
                print("\n*the blacksmith is working hard*")
                response = input("I am the blacksmith, would you like to purchase anything?\n")
                if response == "yes":
                    print("gold: ", player1.gp)
                    print("blacksmith inventory:\n")
                    for armor in blacksmith_inventory:
                        print(armor.name + " ----- ", armor.value, " gp. ")
                    bought_item = input("please, choose an item to buy\n")
                    has_item = False
                    for armor in blacksmith_inventory:
                        if bought_item == armor.name:
                            has_item = True
                            if player1.gp >= armor.value:
                                player1.gp -= armor.value
                                armor_inventory.append(armor)
                                print("\nthanks, enjoy your " + armor.name + "\n")
                            else:
                                print("You can't afford that!")

                    if has_item == False:
                        print("I don't have " + bought_item + " i'm sorry.\n")
                else:
                    print("Goodbye.\n")

    for scene_type in location:
        if scene_type == dismurth_barracks:
                print("\n *There are two soliders aruging, one wearing an eagle helmet, \nanother wearing a red and yellow insignia of a mallet and a small curved cutting tool.*")
                print("WHAT DID YOU SAY!?")
                print("*one soldier grabs the other*")
                print("*a third solider appears*")
                print("Gentlemen, you cannot fight here, this is the war room!")

    for scene_type in location:
        if scene_type == dismurth_farm:
                print("\n*the farmer and his wife look visibly upset*")
                response = input("Those damn bandits keep raiding our stores, you look like you can handle a fight, would you help us?\n")
                if response == "yes":
                    print("\nthank you, their fortress is south of here, you might find them there, be careful! \n")

                else:
                    print("Goodbye.\n")

    for scene_type in location:
        if scene_type == dismurth_tower:
                print("\nthe wizard appears to be in deep thought...")
                response = input("I am the town mage, would you like to learn any spells?\n")
                if response == "yes":
                    print("gold: ", player1.gp)
                    print("wizard's spellbook:\n")
                    for spell in wizard_inventory:
                        print(spell.print_name + " || " + spell.print_attribute + " || " + str(spell.damage) + " gp. ")
                    bought_item = input("please, choose a spell to learn\n")
                    has_item = False
                    for spell in wizard_inventory:
                        if bought_item == spell.name:
                            has_item = True
                            if player1.gp >= spell.damage:
                                player1.gp -= spell.damage
                                spell_inventory.append(spell)
                                print("\nthanks, enjoy your " + spell.print_name + "\n")
                            else:
                                print("You can't afford that!")

                    if has_item == False:
                        print("I don't have " + bought_item + " i'm sorry.\n")
                else:
                    print("Goodbye.\n")

    for scene_type in location:
        if scene_type == south_road_a:
                print("*there is a guard blocking the bridge*")
                print("\n You may not cross the bridge without a certificate of passage")
