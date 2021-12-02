"""
Lab 12: Final Lab

Artwork from:
(grinch) *find a new one*
(present) https://nookipedia.com/wiki/Present
(santa) https://iconscout.com/icon/surprised-santa-2123294
 """

import random
import arcade
GRINCH_SPRITE_SCALING = 0.3
PRESENT_SPRITE_SCALING = 0.2
SANTA_SPRITE_SCALING = 0.4

PRESENT_COUNT = 30
SANTA_COUNT = 5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# how many pixels between the character and edge of the screen
VIEWPORT_MARGIN = 220
# how fast the camera pans to the player
CAMERA_SPEED = 0.1
# how fast the character moves
GRINCH_MOVEMENT_SPEED = 7


class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, resizable=True)

        # Sprite lists
        self.grinch_list = None
        self.present_list = None
        self.santa_list = None

        # set up the player
        self.grinch_sprite = None
        self.score = 0

        self.santa_sprite = None

        # physics engine
        self.physics_engine = None

        # Create the cameras: GUI and sprites
        # we scroll the sprite world but not the GUI
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        # Sprite lists
        self.grinch_list = arcade.SpriteList()
        self.present_list = arcade.SpriteList()
        self.santa_list = arcade.SpriteList()

        # set up the player
        self.grinch_sprite = arcade.Sprite("grinch.png", GRINCH_SPRITE_SCALING)
        self.grinch_sprite.center_x = 256
        self.grinch_sprite.center_y = 512
        self.grinch_list.append(self.grinch_sprite)

        for x in range(PRESENT_COUNT):
            present = arcade.Sprite("present.png", PRESENT_SPRITE_SCALING)
            present.center_x = random.randrange(SCREEN_WIDTH)
            present.center_y = random.randrange(SCREEN_HEIGHT)
            self.present_list.append(present)

        self.santa_sprite = arcade.Sprite("santa.png", SANTA_SPRITE_SCALING)
        self.santa_sprite.center_x = random.randrange(SCREEN_WIDTH)
        self.santa_sprite.center_x = random.randrange(SCREEN_HEIGHT)
        self.santa_list.append(self.santa_sprite)

        arcade.set_background_color(arcade.color.DARK_SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        # select the camera we'll use to draw the sprites
        self.camera_sprites.use()
        # draw the sprites
        self.grinch_list.draw()
        self.present_list.draw()
        self.santa_list.draw()

        # select the unscrolled camera for our GUI
        self.camera_gui.use()

        # ground: WHITE or ALMOND
        arcade.draw_rectangle_filled(self.width // 2, 20, self.width, 40, arcade.color.WHITE)
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 10, arcade.color.BLACK, 20)

        if self.score == 20 or self.score > 20:
            arcade.draw_text("YOU WIN!", 350, 10, arcade.color.BLUE_SAPPHIRE, 20)

    def on_update(self, delta_time):
        # scroll screen to player
        self.scroll_to_grinch()

        self.present_list.update()
        present_hit_list = arcade.check_for_collision_with_list(self.grinch_sprite, self.present_list)
        for present in present_hit_list:
            present.remove_from_sprite_lists()
            self.score += 1

    def on_key_press(self, key, modifiers):
        # move up and down
        if key == arcade.key.UP:
            self.grinch_sprite.change_y = GRINCH_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.grinch_sprite.change_y = -GRINCH_MOVEMENT_SPEED
        # move left to right
        elif key == arcade.key.LEFT:
            self.grinch_sprite.change_x = -GRINCH_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.grinch_sprite.change_x = GRINCH_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.grinch_sprite.change_x = 0

    def scroll_to_grinch(self):
        pos = self.grinch_sprite.center_x - self.width / 2, \
                   self.grinch_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(pos, CAMERA_SPEED)

    def on_resize(self, width, height):
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
