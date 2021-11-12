"""
Chapter 25: Sprites and Walls
"""

import arcade

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites With Walls Example")

        # Sprite Lists
        self.player_list = None
        self.wall_list = None
        # Set up the player
        self.player_sprite = None
        # This variable holds our simple "physics engine"
        self.physics_engine = None

    def setup(self):
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Create the player
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # Manually create and position a box at 300, 200
        wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)
        # Create another box
        wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 364
        wall.center_y = 200
        self.wall_list.append(wall)

        # Placing boxes inside a loop
        for i in range(10):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = i * 64 + 120
            wall.center_y = 400
            self.wall_list.append(wall)

        for x in range(100, 600, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 500
            self.wall_list.append(wall)

        # Placing walls with a list
        coordinate_list = [[500, 100], [570, 100], [500, 170], [570, 170]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_update(self, delta_time: float):
        self.physics_engine.update()

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_sprite.draw()

    # set the velocity:
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
