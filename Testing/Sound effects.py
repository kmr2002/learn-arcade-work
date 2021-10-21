"""
Chapter 20 - Sound Effects
"""

import arcade


# Triggering Sounds
class MyApplication(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Trigger Sound with Key")
        self.laser_sound = arcade.load_sound(":resources:sounds/fall2.wav")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            arcade.play_sound(self.laser_sound)


def main():
    window = MyApplication(300, 300)
    arcade.run()


main()
