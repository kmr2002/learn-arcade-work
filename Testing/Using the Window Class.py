"""
Chapter 18: Using the Window Class
"""

import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Ball:
    """ This class manages a ball bouncing on the screen. """
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        """ Constructor. """
        # Take the parameters of the init function above, and create instance variables out of them
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.change_x, self.change_y,
                                  self.radius, self.color)

    def update(self):
        """ Code to control the ball's movement. """
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # see if the ball hit the edge of the screen. if so, change the direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ My window class. """
    def __init__(self, width, height, title):
        """ Constructor. """

        # Call the parent class's init function
        super().__init__(width, height, title)
        # Set the background color
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create the ball
        self.ball = Ball(50, 50, 3, 3, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whatever we need to draw on the window. """
        # Clear the screen
        arcade.start_render()
        self.ball.draw()

    # on_update = update, same thing and both work
    # delta_time = 1/60 (seconds)
    def update(self, delta_time):
        """ Called to update our objects. Happens app. 60 times/second. """
        self.ball.update()


def main():

    window = MyGame(640, 480, "Drawing Example")

    # starts a loop, keeps the window open until someone tells it to do something else
    arcade.run()


main()
