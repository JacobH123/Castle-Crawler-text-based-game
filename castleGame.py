import sys,time


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)


def rules():
    print_slow('--------------\n')
    print_slow('An evil fire breathing dragon has recently flown into the kings castle,forcing all residents to flee.\n')
    print_slow('You have been conscripted by the king of England to take back his castle from the dragon.\n')
    print_slow('In order to reach the dragon, you must first scour '
               'the castle and collect 5 keys and the holy sword Excalibur.\n')
    print_slow('The dragon is asleep in the throne room, which is locked by 4 unique keys.\n')
    print_slow('Although you may enter the throne room once you have obtained 4 keys, '
               'without the holy sword you will surely perish.\n')
    print_slow('The sword is behind the locked armory door, and you must use one of your keys to unlock it.\n')
    print_slow('Move through the rooms using the commands: "west", "south", "north", or "east".\n')
    print_slow('Some room may contain an item to pick up. If you encounter an item, use the command: "grab".\n')
    print_slow('If you lose track of the items in your inventory, you can use the command "Inventory".\n\n')
    while True:
        begin = input('Do you wish to defeat the dragon and achieve glory? Or flee and become a coward. \nBegin/Flee\n').lower().strip()
        if begin == 'begin':
            print("\nExcellent, continue inside")
            break
        elif begin == 'leave':
            print("You will forever be remembered as a coward!")
            quit()
        elif begin != 'begin' or 'leave':
            print("That wasn't an option")
            continue


# define command available for each room
rooms = {
    'Court Yard': {'north': 'Great Hall'},
    'Great Hall': {'north': 'Throne Room', 'south': 'Court Yard', 'east': 'Kitchen', 'west': 'Barracks', 'item': 'wooden key'},
    'Barracks': {'north': 'Armory', 'east': 'Great Hall', 'item': 'key ring'},
    'Armory': {'south': 'Barracks', 'item': 'sword'},
    'Throne Room': {'south': 'Great Hall'},
    'Kitchen': {'north': 'Kings Chambers', 'south': 'Cellar', 'west': 'Great Hall', 'item': 'skeleton key'},
    'Kings Chambers': {'south': 'Kitchen', 'item': 'heart key'},
    'Cellar': {'north': 'Kitchen', 'item': 'special key'}
}


def user_status():  # indicate room and inventory contents
    print('\n-------------------------')
    print('You are in the {}'.format(current_room))
    if 'item' in rooms[current_room]:
        print('In this room you see a {}'.format(rooms[current_room]['item']))
        print('Inventory:', inventory)
        print('-------------------------------')
    else:
        print("There's nothing here")
    print('The available paths are: {}'.format(availablepaths()))
    print('-------------------------')

def availablepaths():
    paths = []         #Sets paths as an empty list.
    for item in rooms[current_room]: #Checks current room dictionary for the item.
        if item in directions:   #Checks if the remaining items are also in the directions list.
            paths.append(item)   #adds the remaining items to the list path.
    return', '.join(paths)


def check_inventory():
    print('The items in your inventory are:', inventory)


def grab():
    item = input('What do you want to grab? ').lower().strip() #asks the user if they want to grab
    if item != rooms[current_room]['item']:  #Checks the current rooms dictionary for the item
        print('\n--------------')
        print("That item isn't here")
    elif item == rooms[current_room]['item']: #if item is in the dictionary it adds it to the list inventory
        inventory.append(item)
        print_slow('You picked up the: {}\n'.format(rooms[current_room]['item']))
        print('Inventory:',*inventory)
        rooms[current_room].pop('item')


def check_value_exist(inventory, *values):  #Checks if mulitple values exist within inventory
    return set(values).issubset(inventory)


def end_game():
    if 'sword' not in inventory:  # Checks for sword in inventory
        print('\n--------------')
        print_slow('You challenged the dragon and failed miserably.')
        time.sleep(5)
    else:
        print('\n--------------')
        print_slow('After an intense battle, you deal a fatal blow to the wretched  dragon.\n')
        print_slow('Having succeeded in your mission, you received a large fortune and were knighted by the king.\n')
        print_slow('Congratulations Warrior!')
        time.sleep(5)


rules()
directions = ['north', 'south', 'west', 'east']
inventory = []  # list begins empty
current_room = 'Court Yard'  # start in Court Yard
command = ''

while current_room != 'Throne Room':
    user_status()
    command = input('Enter your next move.\n').lower().strip()
    if current_room == 'Barracks' and command == 'north' and 'special key' not in inventory: #Checks if player has key to allow going north
        print('\n--------------')
        print_slow('The door ahead is locked, go find the correct key and return here.')
    elif current_room == 'Barracks' and command == 'north' and 'special key' in inventory:
        print_slow('You unlocked the door!\n')
        current_room = rooms[current_room][command]
    elif command == 'grab' and 'item' not in rooms[current_room]: #Checks if there exists in item in the current room
        print('\n--------------')
        print_slow("There's nothing here to grab!")
    elif command == 'inventory':
        print('\n--------------')
        check_inventory()
    elif current_room == 'Great Hall' and command == 'north' \
            and check_value_exist(inventory, 'special key', 'heart key', 'skeleton key', 'key ring', 'wooden key') == False:
        current_room = 'Great Hall' #Checks for all keys to enter the room
        print('\n--------------')
        print_slow('In order to enter the throne room, you must first collect all the keys.')
    elif (command in directions) and command not in rooms[current_room]:
        print('\n--------------')
        print_slow("You can't go that way.")
    elif command == 'grab':
        grab()
    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]
    else:
        print('\n--------------')
        print_slow('Invalid command.')
end_game()