print("Welcome to Treasure Island. Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
selectedWay = input('Type "left" or "right"\n')

if selectedWay == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    selectedAction = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n')

    if selectedAction == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        doorColor = input("One red, one yellow and one blue. Which colour do you choose?\n")

        if doorColor == "red":
            print("Burned by fire. Game Over.")
        elif doorColor == "blue":
            print("Eaten by beasts. Game Over.")
        elif doorColor == "yellow":
            print("You Win!")
        else:
            print("Game Over")

    else:
        print("Attacked by trout. Game over.")
else:
    print("Fall into a hole. Game Over.")