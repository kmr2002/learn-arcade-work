"""
Chapter 21 - Sprites and Collisions
"""

# sprite: built in hardware to support things that move on the screen
# now its pretty much everything you put on the screen

# .bmp: every dot stored separately, very large
# .gif: specifically for line art, not photographs (long runs of white/black), can do animation
# .png: similar to .gif, free of patents
# .jpg: photographs, do not use for sprites
# .svg: holds all original drawing commands used to create the drawing, do not use for sprites

""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

    def on_draw(self):
        arcade.start_render()


def main():
    """ Main method """
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
