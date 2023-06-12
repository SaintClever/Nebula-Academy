# Global player state
player = {
  'hp': 100,
  'level': 1,
  'gold': 0,
  'location': 'town'  # the starting location of the player
}

# Define areas
areas = {
  'town': {
    'description': 'You are in a peaceful town.',
    'paths': ['forest'],
  },
  'forest': {
    'description': 'You are in a dark forest. There are wild animals around.',
    'paths': ['town', 'mountain'],
  },
  'mountain': {
    'description': 'You are on a mountain. It is cold and windy.',
    'paths': ['forest'],
  }
}

# Game functions

def describe_location(location):
  # Prints the description of the current location.
  print(areas[location]['description'])

def get_player_choice():
  # Asks the player for their choice of action.
  choice = input('What do you want to do? ')
  return choice

def handle_choice(choice):
  # Handle the player's choice of action
  if choice == 'help':
    print_help()
  elif choice == 'look':
    print_paths()
  elif choice in areas[player['location']]['paths']:
    player['location'] = choice
  else:
    print("You can't do that!")

def print_help():
  # Prints the available commands.
  print('Commands:')
  print('  look: see possible paths from your current location')
  print('  help: show this help message')
  print('  [location]: move to a new location')

def print_paths():
  # Prints the possible paths from the current location.
  print('You can go to the following locations:')
  for path in areas[player['location']]['paths']:
      print('  ' + path)

def game_loop():
# Main game loop.
  while True:
    # Describe the current location
    describe_location(player['location'])

    # Get the player's choice of action
    choice = get_player_choice()

    # Handle the player's choice
    handle_choice(choice)

# Start the game
game_loop()
