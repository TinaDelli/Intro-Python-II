from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


item1 = Item("sword", "strong, shiny, useful")
item2 = Item("torch", "lights the way")
item3 = Item("shield", "protects from danger")
item4 = Item("potion", "restores health")

room['outside'].items.append(item1)
room['outside'].items.append(item2)
room['foyer'].items.append(item3)
room['foyer'].items.append(item4)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p1 = Player(input("Please enter your name: -> ").capitalize(), room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


print("Welcome to my Text Based Adventure Game")
print(f"Your name is {p1.name} and you are currently in the {p1.room.name}") 
print(room['outside'].description)
print(f'{p1.room.get_rooms_string()}')
print("Your choices matter here so choose wisely")

choices = ["n", "s", "e", "w"]
acquire = ["get", "take"]
relinquish = ["drop"]

while True:
    cmd = input(f'Please choose {choices[0]} for North, {choices[1]} for South, {choices[2]} for East, or {choices[3]} for West to proceed.. If you have finished your adventure press q to quit ->').lower()
    first_word = cmd.split()[0]
    if cmd in choices:
        p1.move(cmd)  
        p1.room.get_rooms_string()
        print(f'{p1.room.get_rooms_string()}')
    elif first_word in acquire:
        second_word = cmd.split()[1]
        if p1.room.get_items().__contains__(second_word):
            p1.room.remove_item(f"{cmd.split()[1]}")
            p1.on_take(cmd.split()[1])
            print(f'This room now contains: {p1.room.get_items_string()}')
    elif first_word in relinquish:
        second_word = cmd.split()[1]
        print(f'You sly dog you did it yo, you got {cmd}')        
    elif cmd == "q":
        print("Thanks for adventuring please quest again")
        break #or exit()
    else:
        print(f"That is not an option, please choose from {choices} to proceed")
        
