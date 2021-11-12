"""
Artwork from:
 (cat) https://iconarchive.com/show/noto-emoji-animals-nature-icons-by-google/22221-cat-icon.html
 (mouse) https://www.shareicon.net/animal-kingdom-mouse-pet-animals-mammal-rodent-wildlife-813901
 (question block) https://gamebanana.com/sprays/17539
 (brick block) https://villagerdb.com/item/red-brick-flooring
 """
import random
import arcade
SPRITE_SCALING_BOX = 0.3
SPRITE_SCALING_BRICK = 0.5
SPRITE_SCALING_PLAYER = 0.4
SPRITE_SCALING_MOUSE = 0.2

MOUSE_COUNT = 25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# how many pixels between the character and edge of the screen
VIEWPORT_MARGIN = 220
# how fast the camera pans to the player
CAMERA_SPEED = 0.1
# how fast the character moves
PLAYER_MOVEMENT_SPEED = 7

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, resizable=True)

        # Sprite lists
        self.player_list = None
        self.mouse_list = None
        self.wall_list = None

        # set up the player
        self.player_sprite = None
        self.score = 0

        # physics engine
        self.physics_engine = None

        # Create the cameras: GUI and sprites
        # we scroll the sprite world but not the GUI
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.mouse_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.score = 0

        # set up the player
        self.player_sprite = arcade.Sprite("cat-icon.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        for x in range(MOUSE_COUNT):
            mouse = arcade.Sprite("mouse_512x512.png", SPRITE_SCALING_MOUSE)
            mouse.center_x = random.randrange(SCREEN_WIDTH)
            mouse.center_y = random.randrange(SCREEN_HEIGHT)
            self.mouse_list.append(mouse)

        # Corners
        wall = arcade.Sprite("question_block_preview.png", SPRITE_SCALING_BOX)
        wall.center_x = 128
        wall.center_y = 349
        self.wall_list.append(wall)

        wall = arcade.Sprite("question_block_preview.png", SPRITE_SCALING_BOX)
        wall.center_x = 840
        wall.center_y = 500
        self.wall_list.append(wall)

        wall = arcade.Sprite("question_block_preview.png", SPRITE_SCALING_BOX)
        wall.center_x = 305
        wall.center_y = 100
        self.wall_list.append(wall)

        wall = arcade.Sprite("question_block_preview.png", SPRITE_SCALING_BOX)
        wall.center_x = 25
        wall.center_y = 25
        self.wall_list.append(wall)

        # Horizontal brick walls
        for x in range(173, 650, 44):
            wall = arcade.Sprite("red-brick-flooring.d527e76.png", SPRITE_SCALING_BRICK)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        for x in range(350, 700, 44):
            wall = arcade.Sprite("red-brick-flooring.d527e76.png", SPRITE_SCALING_BRICK)
            wall.center_x = x
            wall.center_y = 100
            self.wall_list.append(wall)

        for x in range(0, 173, 44):
            wall = arcade.Sprite("red-brick-flooring.d527e76.png", SPRITE_SCALING_BRICK)
            wall.center_x = x
            wall.center_y = 600
            self.wall_list.append(wall)

        for x in range(400, 800, 44):
            wall = arcade.Sprite("red-brick-flooring.d527e76.png", SPRITE_SCALING_BRICK)
            wall.center_x = x
            wall.center_y = 500
            self.wall_list.append(wall)

        for x in range(70, 150, 44):
            wall = arcade.Sprite("red-brick-flooring.d527e76.png", SPRITE_SCALING_BRICK)
            wall.center_x = x
            wall.center_y = 25
            self.wall_list.append(wall)

        # Vertical brick walls
        for y in range(394, 450, 44):
            wall = arcade.Sprite("red-brick-flooring.d527e76.png", SPRITE_SCALING_BRICK)
            wall.center_x = 128
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(235, 480, 44):
            wall = arcade.Sprite("red-brick-flooring.d527e76.png", SPRITE_SCALING_BRICK)
            wall.center_x = 840
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(-32, 100, 44):
            wall = arcade.Sprite("red-brick-flooring.d527e76.png", SPRITE_SCALING_BRICK)
            wall.center_x = 305
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(70, 180, 44):
            wall = arcade.Sprite("red-brick-flooring.d527e76.png", SPRITE_SCALING_BRICK)
            wall.center_x = 25
            wall.center_y = y
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()
        # select the camera we'll use to draw the sprites
        self.camera_sprites.use()
        # draw the sprites
        self.wall_list.draw()
        self.mouse_list.draw()
        self.player_list.draw()

        # select the unscrolled camera for our GUI
        self.camera_gui.use()

        # draw the gui
        arcade.draw_rectangle_filled(self.width // 2, 20, self.width, 40, arcade.color.ALMOND)
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 10, arcade.color.BLACK, 20)

        if self.score == 20 or self.score > 20:
            arcade.draw_text("YOU WIN!", 350, 10, arcade.color.BLUE_SAPPHIRE, 20)

    def on_update(self, delta_time):
        # call all sprites
        self.physics_engine.update()
        # scroll screen to player
        self.scroll_to_player()

        self.mouse_list.update()
        mouse_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.mouse_list)
        for mouse in mouse_hit_list:
            mouse.remove_from_sprite_lists()
            self.score += 1

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def scroll_to_player(self):
        pos = self.player_sprite.center_x - self.width / 2, \
                   self.player_sprite.center_y -self.height / 2
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
