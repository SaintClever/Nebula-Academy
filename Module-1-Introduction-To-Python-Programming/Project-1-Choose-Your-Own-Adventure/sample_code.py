# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def finalRoom():
    directions = ["N"]
    print("You find a hatch to exit to the (E)ast")
    userInput = ""
    while userInput not in directions:
        print("Options: (W)est and (E)ast")
        userInput = input()
        if userInput == "W":
            firstRoom()
        elif userInput == "E":
            print("You escaped!")
            break
        else:
            print("Please enter a valid option for the adventure game.")


def firstRoom():
    directions = ["S", "E"]
    print(
        "You enter a room full of cobwebs and a canyon to the (N)orth and a room to the (E)ast"
    )
    userInput = ""
    while userInput not in directions:
        print("Options: (N)orth or (S)outh or (E)ast")
        userInput = input()
        if userInput == "S":
            introScene()
        elif userInput == "N":
            print("There is a cliff, you cannot go further.")
        elif userInput == "E":
            finalRoom()
        else:
            print("Please enter a valid option for the adventure game.")


def introScene():
    directions = ["N"]
    print("You enter the catacombs, you can go North or South")
    userInput = ""
    while userInput not in directions:
        print("Options: (N)orth or (S)outh")
        userInput = input()
        if userInput == "N":
            firstRoom()
        elif userInput == "S":
            print("This is where you came from, there's no turning back.")
        else:
            print("Please enter a valid option for the adventure game.")


while True:
    print("Welcome to the Adventure Game!")
    print("As an avid traveler, you have decided to visit the Catacombs of Paris.")
    print("However, during your exploration, you find yourself lost.")
    print("You can choose to walk in multiple directions to find a way out.")
    print("Let's startwith your name: ")
    name = input()
    print("Good luck, " + name + ".")
    introScene()
    break
