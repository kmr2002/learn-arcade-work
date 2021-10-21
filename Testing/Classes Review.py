"""
class
    attributes - adjectives, variables that belong to a class, instance variables
    methods - verbs, functions that belong to a class, anything the class can do (dog can bark, window can open/close)


parent/child class relationships - inheritance
super-class is the parent
    parent class is more generic
    -- kitchen is a room, but room is not necessarily a kitchen --
        kitchen - child, room - parent
class -- child class of arcade.Window
Easiest way to control: Mouse
    on_mouse_motion
    on_mouse_press
    set_mouse_visible = False: to hide mouse

keyboard:
    need starting position
    need move speed
    need to stop when key is released
    on_key_press
    on_key_release

Game controller:
"""


def is_list_sorted(my_list):
    for item in my_list:
        if (my_list[item]) > (my_list[item - 1]):
            return True
        else:
            return False


# This is some code you can use to test:

# Example 1, should print False
my_list = [0, 3, -1, 8]
result = is_list_sorted(my_list)
print("Example 1:", result)

# Example 2, should print True
my_list = [-100, -80, 0, 20, 40, 99, 101]
result = is_list_sorted(my_list)
print("Example 2:", result)