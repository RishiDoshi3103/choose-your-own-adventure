def river_choice():
    answer = input("You come to a river. Do you want to build a raft or swim across? Type 'raft' to build a raft and 'swim' to swim across: ").lower()

    if answer == "raft":
        print("You build a sturdy raft and sail across the river. You discover a hidden treasure chest. Congratulations, You WIN!")
    elif answer == "swim":
        print("You swim across but encounter a school of piranhas. You barely escape. Game Over!")
    else:
        print('Not a valid option. Game Over!')

def bridge_choice():
    answer = input("You reach a bridge guarded by a troll. Offer a gift or outsmart the troll (gift/outsmart)? ").lower()

    if answer == "gift":
        print("You offer the troll a gift, and it lets you pass. You find a magical land. Congratulations, You WIN!")
    elif answer == "outsmart":
        print("You outsmart the troll with riddles and pass the bridge. You encounter a mystical forest. You WIN!")
    else:
        print('Not a valid option. Game Over!')

def cave_choice():
    answer = input("You stumble upon a dark cave. Enter or ignore (enter/ignore)? ").lower()

    if answer == "enter":
        print("You cautiously enter the cave and find an ancient treasure. Congratulations, You WIN!")
    elif answer == "ignore":
        print("You decide to ignore the cave and find a shortcut. You reach the destination. You WIN!")
    else:
        print('Not a valid option. Game Over!')

def start_adventure():
    name = input("Welcome to the Epic Adventure! What's your name? ")
    print("Greetings,", name, "! Get ready for an incredible journey!")

    answer = input("You stand at a crossroad. Left, right, or straight ahead? ").lower()

    if answer == "left":
        river_choice()
    elif answer == "right":
        bridge_choice()
    elif answer == "straight":
        cave_choice()
    else:
        print('Not a valid option. Game Over!')

    print("Thanks for playing,", name, "!")

start_adventure()
