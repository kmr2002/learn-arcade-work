"""
Drawing a Picture
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

# Moon
arcade.draw_circle_filled(400, 300, 200, arcade.csscolor.BEIGE)

# --- Draw the castle ---
# Castle base
arcade.draw_rectangle_filled(400, 150, 500, 200, arcade.csscolor.DIM_GREY)

# Castle Door
arcade.draw_arc_filled(400, 50, 200, 300, arcade.csscolor.SADDLE_BROWN, 0, 180)

# Middle tower
arcade.draw_rectangle_filled(400, 300, 200, 100, arcade.csscolor.DIM_GREY)

# Windows on Middle tower
# left window
arcade.draw_rectangle_filled(325, 275, 25, 25, arcade.csscolor.BLACK)
# Right Window
arcade.draw_rectangle_filled(475, 275, 25, 25, arcade.csscolor.BLACK)

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

# Left tower
arcade.draw_rectangle_filled(200, 275, 100, 50, arcade.csscolor.DIM_GREY)

# Window on Left Tower
arcade.draw_rectangle_filled(200, 275, 25, 25, arcade.csscolor.BLACK)

# Top of Left tower
arcade.draw_triangle_filled(125, 300, 275, 300, 200, 425, arcade.csscolor.DARK_GREY)

# Flag on left tower
arcade.draw_triangle_filled(200, 475, 200, 445, 240, 460, arcade.csscolor.DARK_RED)

# Flag pole on left tower
arcade.draw_line(200, 425, 200, 475, arcade.csscolor.BLACK, 2)

# Right tower
arcade.draw_rectangle_filled(600, 275, 100, 50, arcade.csscolor.DIM_GREY)

# Window on Right Tower
arcade.draw_rectangle_filled(600, 275, 25, 25, arcade.csscolor.BLACK)

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
