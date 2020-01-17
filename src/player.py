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
    def get_inventory(self):
        inventory_list = []
        for i in self.inventory:
            inventory_list.append(i) 
        return inventory_list 
    def on_take(self, new_item):
        self.inventory.append(new_item)
        print(f'You just picked up: {self.get_inventory()}')