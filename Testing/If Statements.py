# Write a function that takes three numbers
# and returns the average

def average_three(x, y, z):
    result = (x + y + z) / 3
    return result


# Print result of 10, 20, 30
my_result = average_three(10, 20, 30)
print(my_result)


# "If" Statement
# "conditional logic"

a = 4
b = 5
if a < b:
    print("a is less than b")

if a > b:
    print("a is greater than b")

print("done")


# Flowcharts
# if statements in diamonds and have two possible paths out of them
# regular statements (everything else) goes in rectangles, they only have one exit path

# Has to be exactly like this or it won't work:
if a <= b:
    print("a is less than or equal to b")

if a >= b:
    print("a is greater than or equal to b")


# Equal
# If you are asking two ==, if you are telling one =
if a == b:
    print("a is equal to b")

# Not equal
if a !=b:
    print("a and b are not equal")



if a == 1:
    print("If a is one, this will print.")
    print("So will this.")
    print("And this.")

print("This will always print because it is not indented.")


# Using And/Or
# And
c = 6
if a < b and a < c:
    print("a is less than b and c")

# Non-exclusive Or
if a < b or a < c:
    print("a is less than either b or c (or both)")


# Boolean data type. This is illegal!
a = True
if a:
    print("a is true")


# How to use the not function
if not a:
    print("a is false")


a = True
b = False

if a and b:
    print("a and b are both true")


a = 3
b = 3

# This next line is strange-looking, but legal
# c will be true or false, depending if
# a and b are equal
c = a == b

# Prints value of c, in this case true
print(c)


# Zero means False. Everything else is True


if 1:
    print("1")

if "A":
    print("A")

# The code below will not print out anything because the value in the if statement is zero.
# The value zero is treated as False
if 0:
    print("Zero")

# an empty string will also come out as False
if "":
    print("1")



# The imput function
# Get input from the user
temperature = input("What is the temperature in Fahrenheit? ")

# Convert the input to an integer
temperature = int(temperature)

print(f"You said the temperature was {temperature}.")

# Do our comparison
if temperature > 90:
    print("It is hot outside.")


# Does the same thing with less typing:
# Get input from the user
temperature = int(input("What is the temperature in Fahrenheit? "))

# Do our comparison
if temperature > 90:
    print("It is hot outside.")


# Else and Else if Statements
# Else statements line up with the If statements
temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
else:
    print("It is not hot outside")
print("Done")


# if/elif/else statement
temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is not hot outside")
print("Done")


# ORDER PROPERLY!!! the 110 is the biggest so it has to be the first(if) statement
temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 110:
    print("Oh man, you could fry eggs on the pavement!")
elif temperature > 90:
    print("It is hot outside")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is ok outside")
print("Done")