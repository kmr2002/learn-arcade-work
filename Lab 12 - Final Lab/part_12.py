"""
Lab 12: Final Lab
"""

import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

ELF_SPRITE_SCALING = 0.2
SNOWFLAKE_SPRITE_SCALING = 0.075
PRESENT_SPRITE_SCALING = 0.25
WALL_SPRITE_SCALING = 0.175

SNOWFLAKE_SPEED = 0.25
ELF_MOVEMENT_SPEED = 3

PRESENT_COUNT = 25


class Present(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the ornament
        self.center_y -= 2
        # See if it reaches the bottom
        if self.top < 0:
            self.reset_pos()


class Walls(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()


class Snowflake(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def follow_sprite(self, elf_sprite):
        if self.center_y < elf_sprite.center_y:
            self.center_y += min(SNOWFLAKE_SPEED, elf_sprite.center_y - self.center_y)
        elif self.center_y > elf_sprite.center_y:
            self.center_y -= min(SNOWFLAKE_SPEED, self.center_y - elf_sprite.center_y)

        if self.center_x < elf_sprite.center_x:
            self.center_x += min(SNOWFLAKE_SPEED, elf_sprite.center_x - self.center_x)
        elif self.center_x > elf_sprite.center_x:
            self.center_x -= min(SNOWFLAKE_SPEED, self.center_x - elf_sprite.center_x)


class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        # Variables to hold the Sprite lists
        self.elf_list = None
        self.snowflake_list = None
        self.present_list = None
        self.wall_list = None

        # Set up the player
        self.elf_sprite = None
        self.score = 0
        self.snowflake_count = 25

        self.snowflake_sprite = None
        self.present_sprite = None
        self.wall_sprite = None

        # Don't show mouse cursor
        self.set_mouse_visible(False)

        # Background music
        # "Deck the Halls - Christmas Song", OpenGameArt
        # https://opengameart.org/content/deck-the-halls-christmas-song-203
        self.background_music = arcade.load_sound("Deck the Halls.wav")
        arcade.play_sound(self.background_music)

        self.wind = arcade.load_sound("whoosh1.wav")
        self.crash = arcade.load_sound("qubodup-crash.wav")

        # Set background color
        arcade.set_background_color(arcade.color.DARK_SKY_BLUE)

    def setup(self):
        # Sprite lists
        self.elf_list = arcade.SpriteList()
        self.snowflake_list = arcade.SpriteList()
        self.present_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.score = 0
        self.snowflake_count = 25

        # Set up the player
        # "Naughty Elf Clipart - 24 Elf On The Shelf Ideas Clipart", Pinclipart
        # https://www.pinclipart.com/maxpin/xbowTR/
        self.elf_sprite = arcade.Sprite("elf.png", ELF_SPRITE_SCALING)
        self.elf_sprite.center_x = 50
        self.elf_sprite.center_y = 115
        self.elf_list.append(self.elf_sprite)

        # Create the ornaments
        for i in range(PRESENT_COUNT):
            # create ornament instance
            # "Icon of a Present in Animal Crossing: New Horizons", Nookipedia
            # https://nookipedia.com/wiki/Present
            present = Present("present.png", PRESENT_SPRITE_SCALING)
            # position the ornament
            present.center_x = random.randrange(SCREEN_WIDTH)
            present.center_y = random.randrange(SCREEN_HEIGHT)
            # add ornament to the lists
            self.present_list.append(present)

        # Set up Snowflakes
        for i in range(10):
            # "Thick Snowflake Sticker", Car Stickers
            # https://www.carstickers.com/products/stickers/holiday-and-special-occasions-stickers/
            # christmas-car-stickers-decals/details/thick-snowflake-sticker-13261/
            snowflake = Snowflake("snowflake.png", SNOWFLAKE_SPRITE_SCALING)
            snowflake.center_x = random.randrange(SCREEN_WIDTH)
            snowflake.center_y = random.randrange(SCREEN_HEIGHT)
            self.snowflake_list.append(snowflake)

        # Create the walls
        for i in range(3):
        # "Chimney with Snow Clip Art", clker
        # http://www.clker.com/clipart-chimney-with-snow.html
            wall = Walls("wall.png", WALL_SPRITE_SCALING)
            wall.center_x = random.randrange(SCREEN_WIDTH)
            wall.center_y = random.randrange(SCREEN_HEIGHT)
            self.wall_list.append(wall)

    def on_draw(self):
        arcade.start_render()

        # Draw the sprites
        self.elf_list.draw()
        self.present_list.draw()
        if self.score >= 50:
            self.snowflake_list.draw()
        if self.score >= 100:
            self.wall_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if self.score <= 50:
            arcade.draw_text("Collect presents", 450, 20, arcade.color.WHITE, 25)
        if self.score > 50 and self.score < 100:
            arcade.draw_text("Avoid the snowflakes", 450, 20, arcade.color.WHITE, 25)
        if self.score > 100:
            arcade.draw_text("Don't run into the walls", 450, 20, arcade.color.WHITE, 25)

        if self.snowflake_count == 0:
            arcade.draw_rectangle_filled(400, 300, 800, 600, arcade.color.DARK_SKY_BLUE)
            arcade.draw_text("You lost, your score: ", self.score, 350, 300, arcade.color.WHITE, 25)
            self.score = 0

        if self.score > 250:
            arcade.draw_rectangle_filled(400, 300, 800, 600, arcade.color.DARK_SKY_BLUE)
            arcade.draw_text("You saved Christmas!", 250, 300, arcade.color.WHITE, 25)

    def on_mouse_motion(self, x, y, dx, dy):
        # Move the center of the player sprite to match mouse x
        self.elf_sprite.center_x = x
        self.elf_sprite.center_y = y

    def on_update(self, delta_time):
        self.snowflake_list.update()
        self.present_list.update()
        self.wall_list.update()

        # ornament scoring
        present_hit_list = arcade.check_for_collision_with_list(self.elf_sprite,
                                                                self.present_list)
        for present in present_hit_list:
            present.reset_pos()
            self.score += 1

        if self.score >= 50:
            for snowflake in self.snowflake_list:
                snowflake.follow_sprite(self.elf_sprite)
            snowflake_hit_list = arcade.check_for_collision_with_list(self.elf_sprite,
                                                                      self.snowflake_list)
            for snowflake in snowflake_hit_list:
                # "Whoosh 1", OpenGameArt
                # https://opengameart.org/content/whoosh-1
                arcade.play_sound(self.wind)
                snowflake.reset_pos()
                self.score -= 2
                self.snowflake_count -= 1

        if self.score >= 100:
            wall_hit_list = arcade.check_for_collision_with_list(self.elf_sprite,
                                                                 self.wall_list)
            for wall in wall_hit_list:
                # "Crash Collision", OpenGameArt
                # https://opengameart.org/content/crash-collision
                arcade.play_sound(self.crash)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
