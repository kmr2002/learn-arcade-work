"""
Work for Lab 07 - User Control
"""

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3
smash = arcade.load_sound("impactsplat01.mp3.wav")
magic = arcade.load_sound("magical_1.wav")

# Moves with key movement
class Pumpkin:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_ellipse_filled(self.position_x - 15, self.position_y, 30, 40, arcade.csscolor.ORANGE_RED)
        arcade.draw_ellipse_filled(self.position_x, self.position_y, 30, 40, arcade.csscolor.ORANGE_RED)
        arcade.draw_ellipse_filled(self.position_x + 15, self.position_y, 30, 40, arcade.csscolor.ORANGE_RED)
        arcade.draw_rectangle_filled(self.position_x, self.position_y + 25, 5, 20, arcade.csscolor.SADDLE_BROWN)

    def update(self):
        # Move the pumpkin
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < self.radius:
            self.position_x = self.radius
            arcade.play_sound(smash)
        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(smash)
        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(smash)
        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(smash)


# Moves with mouse movements
class Hat:
    def __init__(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_arc_filled(self.position_x, self.position_y, 30, 80, arcade.csscolor.BLACK, 0, 180)
        arcade.draw_ellipse_filled(self.position_x, self.position_y - 3, 50, 15, arcade.csscolor.BLACK)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        # see object not pointer
        self.set_mouse_visible(False)
        # background color
        arcade.set_background_color(arcade.color.MIDNIGHT_BLUE)
        # create the pumpkin
        self.pumpkin = Pumpkin(50, 50, 0, 0, 15, arcade.color.ORANGE_RED)
        # create the ball
        self.hat = Hat(100, 100, 15, arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        # Background, code from Lab 02
        arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.DARK_GREEN)
        arcade.draw_circle_filled(400, 300, 200, arcade.csscolor.BEIGE)
        # Draw the Castle Code:
        arcade.draw_rectangle_filled(400, 150, 500, 200, arcade.csscolor.DIM_GREY)
        arcade.draw_arc_filled(400, 50, 200, 300, arcade.csscolor.SADDLE_BROWN, 0, 180)
        arcade.draw_rectangle_filled(400, 300, 200, 100, arcade.csscolor.DIM_GREY)
        arcade.draw_rectangle_filled(325, 275, 25, 25, arcade.csscolor.BLACK)
        arcade.draw_rectangle_filled(475, 275, 25, 25, arcade.csscolor.BLACK)
        arcade.draw_rectangle_filled(400, 275, 50, 50, arcade.csscolor.SADDLE_BROWN)
        arcade.draw_circle_filled(395, 275, 3, arcade.csscolor.BLACK)
        arcade.draw_circle_filled(405, 275, 3, arcade.csscolor.BLACK)
        arcade.draw_triangle_filled(275, 325, 525, 325, 400, 550, arcade.csscolor.DARK_GREY)
        arcade.draw_triangle_filled(400, 600, 400, 570, 440, 585, arcade.csscolor.DARK_RED)
        arcade.draw_line(400, 550, 400, 600, arcade.csscolor.BLACK, 2)
        arcade.draw_rectangle_filled(200, 275, 100, 50, arcade.csscolor.DIM_GREY)
        arcade.draw_rectangle_filled(200, 275, 25, 25, arcade.csscolor.BLACK)
        arcade.draw_triangle_filled(125, 300, 275, 300, 200, 425, arcade.csscolor.DARK_GREY)
        arcade.draw_triangle_filled(200, 475, 200, 445, 240, 460, arcade.csscolor.DARK_RED)
        arcade.draw_line(200, 425, 200, 475, arcade.csscolor.BLACK, 2)
        arcade.draw_rectangle_filled(600, 275, 100, 50, arcade.csscolor.DIM_GREY)
        arcade.draw_rectangle_filled(600, 275, 25, 25, arcade.csscolor.BLACK)
        arcade.draw_triangle_filled(525, 300, 675, 300, 600, 425, arcade.csscolor.DARK_GREY)
        arcade.draw_triangle_filled(600, 475, 600, 445, 640, 460, arcade.csscolor.DARK_RED)
        arcade.draw_line(600, 425, 600, 475, arcade.csscolor.BLACK, 2)

        self.pumpkin.draw()
        self.hat.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.hat.position_x = x
        self.hat.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(magic)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(magic)

    def update(self, delta_time):
        self.pumpkin.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.pumpkin.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.pumpkin.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.pumpkin.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.pumpkin.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.pumpkin.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.pumpkin.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()
