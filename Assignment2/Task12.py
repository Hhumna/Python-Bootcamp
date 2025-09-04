print("You are at a Death and Life game. You have 2 doors to choose from.")
print("Type 'death' for death door or 'live' for live door.")

choice = input("Which door do you choose? ")
choice = choice.lower()

if choice == "death":
    print("You chose the death door. Game over.")

elif choice == "live":
    print("\nYou are at the HEARTS GAME.")
    print("Game starts now.")
    print("Kill everyone in the game to save yourself or die.")
    
    choice1 = input("\nType 'death' to sacrifice yourself or 'live' to kill others: ")
    choice1 = choice1.lower()

    if choice1 == "death":
        print("\nYou hesitated. coward huh.")
        print("You sacrificed yourself. Game Over.")

    elif choice1 == "live":
        print("\nYour hands are stained with blood.")
        print("But you survive. You cleared the HEARTS GAME. You Win!")

    else:
        print("\nInvalid choice. Game Over.")

else:
    print("\nInvalid choice. Game Over.")



print("\nHEARTS GAME is a game which plays with your hearts.")
