# What will this print
# x is a variable, = is an operator
x = 5
print(x)

# using "temperature" instead of "x"
temperature = 5
print(temperature)

PI = 3.14159
radius = 3

m = 294
g = 10.5
m2 = m / g
print(m2)

# Calculate mpg using good variable names
miles_driven = 294
gallons_used = 10.5
mpg = miles_driven / gallons_used
print(mpg)

# What will this print
# addition
x = 5 + 10
print(x)

# subtraction
x = 15 - 10
print(x)

# use * not x for multiplication
x = 15 * 10
print(x)

# this (^) doesn't raise it to the power, does something else
x = 15 ^ 10
print(x)

# use ** to exponentiation, raise something to the power
x = 15 ** 10
print(x)

# integer division, rounds down, never get a decimal
x = 15 // 10
print(x)

# Modulus, gives remainder of division
x = 300 % 200
print(x)

# juxtaposition doesn't work for multiplication, needs the multiplication sign
# this code will work, but it won't print anything
x = 3
y = 2 * x
z = x * (3 + x)
print(z)

# variable goes on left and by itself, expression goes on right
# otherwise it won't work

# works its way through the code, storing the previous answer in x
x = 4
print(x)
x = x + 1
print(x)

# will print 6
x = 4
print(x)
x = x + 1
x = x + 1
print(x)

# will print 5
x = 4
print(x)
print(x + 1)
print(x + 1)

# will print 5
x = 4
print(x + 1)

# divides x by 2
x = 4
x /= 2
print(x)

average = (90 + 86 + 71 + 100 + 98) / 5
print(average)

answer = "bananas"
print(answer)

answer = "bananas"
print("The answer is", answer, "which are great.")

answer = "bananas"
print("The answer is" + answer + "which is great")

answer = 42
print("The answer is" + str(answer) + "32")

answer = 42
print("The answer is 32")

answer = 42
print(f"The answer is {answer}.")