"""
Lab 04 - Camel
"""
import random


def main():
    print("Welcome to Space!")
    print("After landing on Saturn you find some alien rocket ships.")
    print("You steal one and the alien's find out. They are chasing you!")
    print("Make your way to safety by out flying the aliens.")

    miles_traveled = 0
    hunger = 0
    ship_gas = 0
    aliens_traveled = -20
    initial_meals = 3

    done = False
    while not done:
        print("A. Eat a meal.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the gas.")
        print("E. Status Check.")
        print("Q. Quit.")
        user_choice = input("What is your choice? ")

        if user_choice.upper() == "Q":
            print("You have quit this program.")
            done = True

        elif user_choice.upper() == "E":
            print("You have traveled", miles_traveled, "miles.")
            print("You have", initial_meals - hunger, "meals left.")
            print("The aliens are", miles_traveled - aliens_traveled, "miles behind you")

        elif user_choice.upper() == "D":
            print("Your ships tank is full.")
            my_number = random.randrange(7, 14)
            aliens_traveled += my_number

        elif user_choice.upper() == "C":
            my_number = random.randrange(10, 20)
            print("You just traveled", my_number, "miles.")
            hunger += 1
            my_number1 = random.randrange(1, 3)
            ship_gas += my_number1
            my_number2 = random.randrange(7, 14)
            aliens_traveled += my_number2

        elif user_choice.upper() == "B":
            my_number = random.randrange(5, 12)
            miles_traveled += my_number
            print("You just traveled", my_number, "miles.")
            hunger += 1
            ship_gas += 1
            my_number1 = random.randrange(7, 14)
            aliens_traveled += my_number1

        elif user_choice.upper() == "A":
            if initial_meals > 0:
                initial_meals -= 1
                hunger = 0
            elif initial_meals >= 4:
                print("There was an error, yoo don't have any meals left.")

        if hunger > 6:
            print("You died of hunger.")
            done = True

        if hunger > 4:
            print("You are hungry.")

        if ship_gas > 8:
            print("You ran out of gas.")

        if ship_gas > 5:
            print("You are low on gas.")

        if aliens_traveled >= miles_traveled:
            print("You have been caught by the aliens!")
            done = True

        if aliens_traveled >= miles_traveled - 15:
            print("The aliens are getting close!")

        if miles_traveled >= 200:
            print("You have won the game!")

        my_number = random.randrange(1, 20)
        if my_number == 10:
            print("You found a food supply and free gas!")
            initial_meals = 3
            hunger = 0
            ship_gas = 0

main()