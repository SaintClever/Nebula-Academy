# game.py

from locations import locations
from actions import actions_dispatcher

# Global player state
player = {
    'ship_name': None,
    'location': 'space_apartment',  # the starting location of the player
    'ship_purchased': False
}

# Game functions
def describe_location(location):
    """Prints the description of the current location."""
    print(locations[location]['description'])

def get_player_choice():
    """Asks the player for their choice of action."""
    choice = input('What do you want to do? ')
    return choice

def handle_choice(choice):
    """Handles the player's choice of action."""
    if choice == 'help':
        print_help()
    elif choice == 'actions':
        list_actions()
    elif choice in locations[player['location']]['actions']:
        actions_dispatcher[choice](player)  # call the function from the dispatcher
    else:
        print("You can't do that! Input 'actions' to see what you can do. Input 'help' to see the help message.")

def print_help():
    """Prints the available commands."""
    print('Commands:')
    print('  help: show this help message')
    print('  actions: see possible actions in your current location')
    print('  [action]: perform an action')

def list_actions():
    """Lists the available actions in the current location."""
    print('You can do the following actions:')
    for action in locations[player['location']]['actions']:
        print('  ' + action)

def game_loop():
    """Main game loop."""
    while True:
        describe_location(player['location'])
        choice = get_player_choice()
        handle_choice(choice)

# Start the game
game_loop()
