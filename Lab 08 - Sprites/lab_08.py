"""
Lab 8: Sprites
"""
import arcade
import random

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.4
SPRITE_SCALING_COIN = 0.2

COIN_COUNT = 50

SPRITE_SCALING_FIRE = 0.2
FIRE_COUNT = 10
SPRITE_SPEED = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_WIDTH + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()


class Fire(arcade.Sprite):
    def follow_sprite(self, player_sprite):
        if self.center_y < player_sprite.center_y:
            self.center_y += min(SPRITE_SPEED, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(SPRITE_SPEED, self.center_y - player_sprite.center_y)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(SPRITE_SPEED, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(SPRITE_SPEED, self.center_x - player_sprite.center_x)


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.fire_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 50

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # load the sounds
        self.jellyfish_sting = arcade.sound.load_sound("bzzzt.wav")
        self.meow = arcade.sound.load_sound("Meow.wav")

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.fire_list = arcade.SpriteList()

        # Score
        self.score = 50

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("cat.ico", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin("fish.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        for i in range(FIRE_COUNT):
            fire = Fire("jellyfish.png", SPRITE_SCALING_FIRE)

            fire.center_x = random.randrange(SCREEN_WIDTH)
            fire.center_y = random.randrange(SCREEN_HEIGHT)

            self.fire_list.append(fire)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.fire_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if self.score == 0 or self.score < 0:
            output = "Game Over"
            arcade.draw_text(output, 250, 300, arcade.color.BLACK, 50)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        # Move the center of the player sprite to match the mouse x, y
        if self.score > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y
        else:
            self.player_sprite.center_x = 50
            self.player_sprite.center_y = 50

    def update(self, delta_time):
        """ Movement and game logic """
        self.coin_list.update()
        self.fire_list.update()
        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            if self.score > 0:
                arcade.play_sound(self.meow)
                coin.reset_pos()
                self.score -= 1
            else:
                self.score = 0

        for fire in self.fire_list:
            fire.follow_sprite(self.player_sprite)
        fire_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.fire_list)
        for fire in fire_hit_list:
            if self.score > 0:
                arcade.play_sound(self.jellyfish_sting)
                fire.remove_from_sprite_lists()
                self.score += 3
            else:
                fire.remove_from_sprite_lists()
                self.score = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
