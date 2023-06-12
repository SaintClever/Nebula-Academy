# locations.py

locations = {
    'space_apartment': {
        'description': 'You are in your apartment. You can make coffee, sleep, or leave.',
        'actions': ['make coffee', 'sleep', 'leave'],
    },
    'space_hub': {
        'description': 'You are in the space hub. You can ride the train to the market, port, or return to your apartment. Type the name of the location to go there.',
        'actions': ['market', 'port', 'apartment'],
    },
    'space_market': {
        'description': 'You are in the market. You can buy Gorp Tentacles, or return to the hub.',
        'actions': ['gorp tentacles', 'hub'],
    },
    'space_port_no_ship': {
        'description': 'You are in the space port. You can buy a ship or return to the space hub.',
        'actions': ['buy ship', 'hub'],
    },
    'space_port': {
        'description': 'You are in the space port. You can name your ship, take off, or return to the hub.',
        'actions': ['name ship', 'take off', 'hub'],
    }
}
