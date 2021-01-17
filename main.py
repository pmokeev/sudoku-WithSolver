from playerFile import gamePlayer
from computerFile import gameComputer

def printHello():
    print("Select the game mode:")
    print("1 - Game mode for user")
    print("2 - Computer game mode")
    print("3 - exit")
    print("Input key")

printHello()

while True:
    try:
        keyGame = int(input())

    except:
        print("Something went wrong! Let's try again.")
        continue

    if keyGame == 1 or keyGame == 2 or keyGame == 3:
        break

    else:
        print("Try again!")

if keyGame == 1:
    gamePlayer()

elif keyGame == 2:
    gameComputer()

else:
    print("Have a nice day!")