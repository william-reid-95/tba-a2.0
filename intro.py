
name_chosen = False
class_chosen = False


print("What is your name?")
player_name_string = input("\n")
print("your name is " + player_name_string + "?")
name_chosen = True
print("\nPlease choose your class: \n")
print("1) Warrior")
print("2) Rouge")
print("3) Mage")

while class_chosen == False:
    player_class_string = input("\n")

    if player_class_string == "1":
        class_chosen = True
    elif player_class_string == "2":
        class_chosen = True
    elif player_class_string == "3":
        class_chosen = True
    else:
        print("\ninvalid selection!\n")
