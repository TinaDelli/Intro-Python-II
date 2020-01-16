from room import Room
from player import Player

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p1 = Player("Charlie", room['outside'])

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

def direction_choices(current_position="none", cmd="none"):
    if current_position == "none" and cmd == "none":
        available_directions = p1.room.change_direction()
        
        for el in available_directions:
            if el !=None:
                print(f"From here you have a choice: You can go to the {el}..")
        
    
    

def player_choices(player_choice):
    if player_choice == "n" and room['outside']:
        p1.room = p1.room.n_to
        print(f"You are now in {p1.room.name}. {p1.room.description}")
        direction_choices()
        # print(f"From here you have a few choices you can go to the {p1.room.n_to.name}")



print("Welcome to my Text Based Adventure Game")
print(f"Your name is {p1.name} and you are currently in the {p1.room.name}") #can we make this more dynamic?
print(room['outside'].description)
direction_choices()
print("Your choices matter here so choose wisely")

choices = ["n", "s", "e", "w"]
# directions = [n.to, s_to, e_to, w_to]

while True:
    cmd = input(f'Please choose {choices[0]} for North, {choices[1]} for South, {choices[2]} for East, or {choices[3]} for West to proceed.. If you have finished your adventure press q to quit ->')
    if cmd in choices:
        # print(f"You chose {cmd} ")
        if cmd == "n" and p1.room == room['outside']:
            p1.room = p1.room.n_to
            print(f"You are now in {p1.room.name}. {p1.room.description}")
            direction_choices()
            # print(f"From here you have a few choices you can go to the {p1.room.n_to.name}, the {p1.room.s_to} or the {p1.room.e_to}..")
        
    elif cmd == "q":
        print("Thanks for adventuring please quest again")
        break
    else:
        print(f"That is not an option, please choose from {choices} to proceed")