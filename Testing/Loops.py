"""
Loops
"""

# 'for loops' - when you know how many times to loop
# 'while loop' - loop until a condition

# for loop
# Indentation matters!
for i in range(5):
    print("I will not chew gun in class.")
    print("But I can drink water.")


# can use a variable for how many times to loop
repetitions = int(input("How many times?"))
for i in range(repetitions):
    print("I will not chew gun in class.")
    print("But I can drink water.")


def print_about_gum(repetitions):
    for i in range(repetitions):
        print("I will not chew gum in class.")
        print("But I can drink water.")

repetitions = int(input("How many times?"))
print_about_gum(repetitions)


# computers start counting at 0
for i in range(10):
    print(i)


# print the numbers 1 to 10
for star_count in range(1, 11):
    print(star_count)

for star_count in range(10):
    # add 1 to star_count before printing
    print(star_count + 1)


# Counting by numbers other than 1
# 10 to 0
for i in range(10, -1, -1):
    print(i)

# Printing even numbers
for i in range(2, 12, 2):
    print(i)

for i in range(5):
    print((i + 1) * 2)


# Print numbers out of a list
for item in [2, 6, 4, 2, 4, 6, 7, 4]:
    print(item)


# Nesting loops
for i in range(3):
    print("a")
for j in range(3):
    print("b")

for i in range(3):
    print("a")
    for j in range(3):
        print("b")

print("Done")


# loop from 1:00 to 12:59
for hour in range(1, 13):
    for minute in range(60):
        print(hour, minute)


# Keep a running total
# Make sure the variables (total = 0) aren't inside the loop (needs to be before the "for" line)
total = 0
for i in range(5):
    new_number = int(input("Enter a number: " ))
    # total = total + new_number, this and the next line are the same
    total += new_number
print("The total is: ", total)


# Sum all numbers 1 to 100
total = 0
for i in range(1, 101):
    total = total + i
print(total)

# Take 5 numbers from the user
# Count the number of times the user enters a 0
total = 0
for i in range(5):
    new_number = int(input( "Enter a number: "))
    if new_number == 0:
        total = total + 1
print("You entered a total of", total, "zeros.")


# Review
for i in range(5):
    print("hello")
print("there")


a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)


# While loop
# these two are equivalent:
for i in range(10):
    print(i)

i = 0    # sentinel variable: the variable being watched
while i < 10:
    print(i)
    i += 1


# Print a while loop starting at 10 going down to 0, including zero
i = 10
while i > -1:
    print(i)
    i -= 1


# Do not mix quit.upper() and quit.lower() - only use one in each loop
quit = "n"
while quit.lower() == "n" or quit.lower() == "no":
    quit = input("Do you want to quit?1")


done = False
while not done:
    quit = input("Do you want to quit?2")
    if quit.lower() == "y":
        done = True
        print("Bye!")

    attack = input("Do you want to attack the dragon?")
    if attack.lower() == "y":
        done = True
        print("Bad choice, you died.")


done = False
while not done:
    quit = input("Do you want to quit?3")
    if quit.lower() == "y":
        done = True
        print("Bye!")

    if not done:
        attack = input("Do you want to attack the dragon?")
        if attack.lower() == "y":
            done = True
            print("Bad choice, you died.")


done = False
while not done:
    quit = input("Do you want to quit?4")
    if quit.lower() == "y":
        done = True
        print("Bye!")
        # break out of that loop
        break

    attack = input("Do you want to attack the dragon?")
    if attack.lower() == "y":
        done = True
        print("Bad choice, you died.")


# inclusive function: meaning type both the 5 and 10 in this case
def count_up(start, end):
    for i in range(start, end + 1):
        print(i)
count_up(5, 10)


import random

# random number from 0 to 49
my_number = random.randrange(50)
print(my_number)

# random number from 100 to 200
my_number = random.randrange(100, 201)
print(my_number)

# Random Chance of something happening
for i in range(20):
    my_number = random.randrange(5)
    print(my_number)

for i in range(20):
    my_number = random.randrange(1, 6)
    print(my_number)


# line below "rolls the dice" 20 times, if the range is ever 1 then you are doing something wrong
for i in range(20):
    # the line below will roll a random number 0-4
    # if we roll a zero the print that we encountered a dragon, 1 in 20 chance
    if random.randrange(5) == 0:
        print("DRAGON!")
    else:
        print("No dragon.")


# random floating point from 0 to 1
my_number = random.random()
print(my_number)

# random number from 0 to 10
my_number = random.random() * 10
print(my_number)

# random number from 1 to 10
my_number = random.random() * 9 + 1
print(my_number)