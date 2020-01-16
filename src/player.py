# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.room = current_room 
        self.inventory = []
    def move(self, direction):
        next_room = self.room.get_room_in_direction(direction)
        if next_room is not None:
            self.room = next_room
            print(self.room)
        else:
            print("There is no path this way, if you continue you will surely die, go back at once")   