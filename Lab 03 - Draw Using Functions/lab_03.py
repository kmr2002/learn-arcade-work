"""
Drawing with Functions
"""
# Import "arcade" library
import arcade

# Open up a window.
arcade.open_window(800, 600, "Lab 2")

# Set background color
arcade.set_background_color(arcade.color.MIDNIGHT_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the ground
arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.DARK_GREEN)

def draw_window(x, y):
    arcade.draw_rectangle_filled(x, y, 25, 25, arcade.csscolor.BLACK)

def draw_pumpkin(x, y):
    arcade.draw_ellipse_filled(x - 15, y, 30, 40, arcade.csscolor.ORANGE_RED)
    arcade.draw_ellipse_filled(x, y, 30, 40, arcade.csscolor.ORANGE_RED)
    arcade.draw_ellipse_filled(x + 15, y, 30, 40, arcade.csscolor.ORANGE_RED)
    arcade.draw_rectangle_filled(x, y + 25, 5, 20, arcade.csscolor.SADDLE_BROWN)

def draw_witch_hat(x, y):
    arcade.draw_arc_filled(x, y, 30, 80, arcade.csscolor.BLACK, 0, 180)
    arcade.draw_ellipse_filled(x, y - 3, 50, 15, arcade.csscolor.BLACK)

def draw_star(x, y):
    arcade.draw_circle_filled(x, y, 7, arcade.csscolor.BEIGE)

def draw_cloud(x, y):
    arcade.draw_ellipse_filled(x, y, 80, 40, arcade.csscolor.GAINSBORO, num_segments=32)
    arcade.draw_circle_filled(x - 40, y + 5, 15, arcade.csscolor.GAINSBORO, num_segments=32)
    arcade.draw_circle_filled(x - 20, y + 15, 15, arcade.csscolor.GAINSBORO, num_segments=32)
    arcade.draw_circle_filled(x, y + 19, 15, arcade.csscolor.GAINSBORO, num_segments=32)
    arcade.draw_circle_filled(x + 20, y + 15, 15, arcade.csscolor.GAINSBORO, num_segments=32)
    arcade.draw_circle_filled(x + 40, y + 5, 15, arcade.csscolor.GAINSBORO, num_segments=32)
    arcade.draw_circle_filled(x + 25, y - 5, 15, arcade.csscolor.GAINSBORO, num_segments=32)
    arcade.draw_circle_filled(x - 25, y - 5, 15, arcade.csscolor.GAINSBORO, num_segments=32)

def main():
    # Moon
    arcade.draw_circle_filled(400, 300, 200, arcade.csscolor.BEIGE)

    draw_cloud(50, 400)
    draw_cloud(300, 525)
    draw_cloud(175, 200)
    draw_cloud(650, 550)
    draw_cloud(775, 275)

    draw_star(100, 400)
    draw_star(500, 550)
    draw_star(150, 500)
    draw_star(75, 580)
    draw_star(50, 200)
    draw_star(250, 565)
    draw_star(550, 500)
    draw_star(675, 450)
    draw_star(700, 230)
    draw_star(780, 300)
    draw_star(745, 555)

    draw_pumpkin(100, 100)
    draw_pumpkin(50, 50)
    draw_pumpkin(725, 75)

    draw_witch_hat(50, 75)
    draw_witch_hat(275, 255)
    draw_witch_hat(750, 50)

    # --- Draw the castle ---
    # Castle base
    arcade.draw_rectangle_filled(400, 150, 500, 200, arcade.csscolor.DIM_GREY)

    # Castle Door
    arcade.draw_arc_filled(400, 50, 200, 300, arcade.csscolor.SADDLE_BROWN, 0, 180)

    # Middle tower
    arcade.draw_rectangle_filled(400, 300, 200, 100, arcade.csscolor.DIM_GREY)

    # Windows on Middle tower
    draw_window(325, 275)
    draw_window(475, 275)

    # Door on Middle tower
    arcade.draw_rectangle_filled(400, 275, 50, 50, arcade.csscolor.SADDLE_BROWN)

    # Door handles
    arcade.draw_circle_filled(395, 275, 3, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(405, 275, 3, arcade.csscolor.BLACK)

    # Top of Middle tower
    arcade.draw_triangle_filled(275, 325, 525, 325, 400, 550, arcade.csscolor.DARK_GREY)

    # Flag on middle tower
    arcade.draw_triangle_filled(400, 600, 400, 570, 440, 585, arcade.csscolor.DARK_RED)

    # Flag pole on middle tower
    arcade.draw_line(400, 550, 400, 600, arcade.csscolor.BLACK, 2)

    # Left Side tower
    # tower
    arcade.draw_rectangle_filled(200, 275, 100, 50, arcade.csscolor.DIM_GREY)

    draw_window(200, 275)

    # Top of tower
    arcade.draw_triangle_filled(125, 300, 275, 300, 200, 425, arcade.csscolor.DARK_GREY)

    # Flag on tower
    arcade.draw_triangle_filled(200, 475, 200, 445, 240, 460, arcade.csscolor.DARK_RED)

    # Flag pole on left tower
    arcade.draw_line(200, 425, 200, 475, arcade.csscolor.BLACK, 2)

    # Right side tower
    # tower
    arcade.draw_rectangle_filled(600, 275, 100, 50, arcade.csscolor.DIM_GREY)

    # window
    draw_window(600, 275)

    # Top of Right Tower
    arcade.draw_triangle_filled(525, 300, 675, 300, 600, 425, arcade.csscolor.DARK_GREY)

    # Flag on Right tower
    arcade.draw_triangle_filled(600, 475, 600, 445, 640, 460, arcade.csscolor.DARK_RED)

    # Flag pole on right tower
    arcade.draw_line(600, 425, 600, 475, arcade.csscolor.BLACK, 2)

    # Finish drawing
    arcade.finish_render()

    # Keep the window up until someone closes it
    arcade.run()

# Call the main function to get the program started
main()