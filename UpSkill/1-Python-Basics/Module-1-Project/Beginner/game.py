ship_name = None

# Actions
def space_apartment():
    print("You are in your apartment. You have a bed, a desk, and a door.")
    print("But this is an alpha, so only objects are doors, beds, and the coffeepot are interactive for some reason.")
    def make_coffee():
        print("You make some coffee. It's good.")
        space_apartment()
    def sleep():
        print("You sleep. It's good.")
        space_apartment()
    def leave():
      print("You leave your apartment.")
      space_hub()
    options = [make_coffee, sleep, leave]
    options[int(input("What do you want to do?\n 1. Make coffee\n 2. Sleep\n 3. Leave\n"))-1]()
    
def space_hub():
    print("You are in the space hub. You can ride the train to the market, space_port, or return to your apartment.")
    print("What would you like to do?\n 1. Go to the market\n 2. Go to the space_port\n 3. Return to your apartment")
    options = [space_market, space_port, space_apartment]
    options[int(input())-1]()

def space_market():
    print("You are in the market. You can buy Gorp Tentacles, or return to the space_hub.")
    print("What would you like to do?\n 1. Buy Gorp Tentacles\n 2. Return to the space_hub")
    def gorp_tentacles():
        print("You buy some Gorp Tentacles. They have the right number of suction cups, 73. You consume the tentacles. They're good.")
        space_hub()
    options = [gorp_tentacles, space_hub]
    options[int(input())-1]()


# Locations
def space_port():
    print("You are in the space port. You can buy a ship, or return to the space_hub.")
    print("What would you like to do?\n 1. Buy a ship\n 2. Return to the space_hub")
    def buy_ship():
        print("You buy a ship. It'sa good ship, a really good ship.")
        print("You are in the space port and now with a really good ship. You can attempt to take off in your new ship, name your new ship, or return to the space_hub.")
        print("What would you like to do?\n 1. Take off in your new ship\n 2. Name your new ship\n 3. Return to the space_hub")
        def take_off(): 
            print(f"You attempt to take off in {ship_name if ship_name else ''} your good ship, a really good ship.")
            print("You immediately lose control of your ship and crash into the space port. You are dead.")
            print("Game Over")
            exit()
        def name_ship():
            print("What would you like to name your new ship?")
            ship_name = input()
            print("You name your new ship " + ship_name + ". It's a good name, a really good name.")
            print("You are in the space port and now with a really good ship named " + ship_name + ". You can attempt to take off in your new ship, name your new ship, or return to the space_hub.")
            print("What would you like to do?\n 1. Take off in your new ship\n 2. Name your new ship\n 3. Return to the space_hub")
            options = [take_off, name_ship, space_hub]
            options[int(input())-1]()
        options = [take_off, name_ship, space_hub]
        options[int(input())-1]()
    options = [buy_ship, space_hub]
    options[int(input())-1]()


space_apartment()