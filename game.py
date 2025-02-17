rooms = {
    'start': {
        'description': 'You are standing in a dark forest. There is a path leading north.',
        'north': 'cabin',
        'south': 'lake',
    },
    'cabin': {
        'description': 'You are in a cozy cabin. There is a door to the south.',
        'south': 'start',
    },
    'lake': {
        'description': 'You are in a beautiful lake. There is a locked chest here.',
        'north': 'start',
    },
}

# Add items to the room
rooms['cabin']['item'] = 'key'

inventory = []

def collect_item(room):
    """Allows the player to collect an item if present in the room."""
    if 'item' in rooms[room]:
        inventory.append(rooms[room]['item'])
        print(f"You collected {rooms[room]['item']}")
        del rooms[room]['item']
    else:
        print("There is nothing to collect here.")

def describe_room(room):
    """Describes the current room the player is in."""
    print("\n" + rooms[room]['description'])

def player_move(current_room, direction):
    """Handles the player's movement and checks if the direction is valid."""
    if direction in rooms[current_room]:
        return rooms[current_room][direction]
    else:
        print("You can't go that way.")
        return current_room

def play_game():
    """Main game loop."""
    current_room = 'start'

    while True:
        describe_room(current_room)

        # Collect items automatically if present in the room
        if 'item' in rooms.get(current_room, {}):
            collect_item(current_room)

        command = input("\nWhat do you want to do? (go north, go south, quit, collect): ").lower().strip()

        if command == 'quit':
            print("Thanks for playing!")
            break
        elif command.startswith('go'):
            direction = command.split()[1] if len(command.split()) > 1 else None
            if direction:
                current_room = player_move(current_room, direction)
            else:
                print("Please specify a direction (north/south).")
        elif command == "collect":
            collect_item(current_room)
        else:
            print("I don't understand that command.")

play_game()

