print('''
+-------------------------------------------------------------------+
| _                                       _     _                 _ |
|| |_ _ __ ___  __ _ ___ _   _ _ __ ___  (_)___| | __ _ _ __   __| ||
|| __| '__/ _ \/ _` / __| | | | '__/ _ \ | / __| |/ _` | '_ \ / _` ||
|| |_| | |  __/ (_| \__ \ |_| | | |  __/ | \__ \ | (_| | | | | (_| ||
| \__|_|  \___|\__,_|___/\__,_|_|  \___| |_|___/_|\__,_|_| |_|\__,_||
+-------------------------------------------------------------------+
''')

print("Welcome to Treasure Island! \nYour mission is to find the treasure.")
direction = input("You're at a crossroad, where do you want to go? Type 'left' or 'right': ")
if direction.lower() == "left":
    action = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ")
    if action.lower() == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
        if door.lower() == "yellow":
            print("You found the treasure! You WIN!!!")
        elif door.lower() == "red":
            print("It's a room full of fire. Game Over.")
        elif door.lower() == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("Game Over.")