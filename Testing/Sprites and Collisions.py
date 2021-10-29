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

        # variables that will hold sprites
        self.play_list = None
        self.coin_list = None

        # set up player into
        self.play_sprite = None
        self.score = 0

        # don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables """
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # score
        self.score = 0

        # set up the player
        # character image from kenney.nl
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # create the coin:
        for i in range(COIN_COUNT):
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()

        # Draw the sprites list here. typically sprites are divided into
        # different groups. other game engines might call these "sprite layers"
        # or "sprite groups." Sprites that don't move should be drawn in their
        # own group for the best performance, as Arcade can tell the graphics
        # card to just redraw them at the same spot.
        # try to avoid drawing sprites on their own, use a SpriteList
        # because there are many performance improvements in that code
        self.player_list.draw()
        self.coin_list.draw()

        # put score on the screen
        output = "Score:" + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 28)

    def on_mouse_motion(self, x, y, dx, dy):
        # move the center of the player sprite to match mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        # call update on all sprites
        self.coin_list.update()
        # generate a list of all sprites that collided with the player
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        # loop through each colliding sprite, remove it and add to the score
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

def main():
    """ Main method """
    # create the window
    window = MyGame()
    # call setup
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
