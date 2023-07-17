# actions.py

def make_coffee(player):
    print("You make some coffee. It's good.")

def sleep(player):
    print("You sleep. It's good.")

def leave(player):
    player['location'] = 'space_hub'

def gorp_tentacles(player):
    print("You buy some Gorp Tentacles. They have the right number of suction cups, 73. You consume the tentacles. They're good.")
    player['location'] = 'space_hub'

def take_off(player): 
    print(f"You attempt to take off in {player['ship_name'] if player['ship_name'] else 'your good ship, a really good ship.'}")
    print("You immediately lose control of your ship and crash into the space port. You are dead.")
    print("Game Over")
    exit()

def name_ship(player):
    print("What would you like to name your new ship?")
    player['ship_name'] = input()
    print("You name your new ship " + player['ship_name'] + ". It's a good name, a really good name.")
    player['location'] = 'space_port'

def buy_ship(player):
    print("You buy a ship. It's a good ship, a really good ship.")
    player['ship_purchased'] = True
    player['location'] = 'space_port'
    

def go_to_space_market(player):
    player['location'] = 'space_market'

def go_to_space_port(player):
    if player['ship_purchased']:
        player['location'] = 'space_port'
    else:
        player['location'] = 'space_port_no_ship'

def go_to_space_apartment(player):
    player['location'] = 'space_apartment'

def go_to_space_hub(player):
    player['location'] = 'space_hub'


actions_dispatcher = {
    'make coffee': make_coffee,
    'sleep': sleep,
    'leave': leave,
    'gorp tentacles': gorp_tentacles,
    'take off': take_off,
    'name ship': name_ship,
    'buy ship': buy_ship,
    'market': go_to_space_market,
    'port': go_to_space_port,
    'apartment': go_to_space_apartment,
    'hub': go_to_space_hub
}