"""
Lab 6: Text Adventure
"""


class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    room = Room("You are in the hallway, there is a door to your North and East.", 3, 1, None, None)
    room_list.append(room)
    room = Room("You are in the dining room, there are doors in all directions.", 4, 2, 7, 0)
    room_list.append(room)
    room = Room("You are in the kitchen, there is a door to the North and West.", 5, None, None, 1)
    room_list.append(room)
    room = Room("You are in the bathroom, there is a door to the South and East.", None, 4, 0, None)
    room_list.append(room)
    room = Room("You ar in the living room, there are doors in all directions.", 6, 5, 1, 3)
    room_list.append(room)
    room = Room("You are in the bedroom, there is a door to the South and West.", None, None, 2, 4)
    room_list.append(room)
    room = Room("You are in the library, there is on a door to the South.", None, None, 4, None)
    room_list.append(room)
    room = Room("You are in the office, there is a door to the North.", 1, None, None, None)
    room_list.append(room)
    current_room = 0

    # Moving
    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        user_choice = input("? ")

        # North
        if user_choice.lower() == "n" or user_choice.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can not go this way.")
            else:
                current_room = next_room

        # East
        elif user_choice.lower() == "e" or user_choice.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can not go this way.")
            else:
                current_room = next_room

        # South
        elif user_choice.lower() == "s" or user_choice.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can not go this way.")
            else:
                current_room = next_room

        # West
        elif user_choice.lower() == "w" or user_choice.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can not go this way")
            else:
                current_room = next_room

        # Quit
        elif user_choice.lower() == "q" or user_choice.lower() == "quit":
            print("You have quit the game.")
            break

        # "I do not understand"
        else:
            print("I do not understand")


main()
