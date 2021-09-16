# Expressions
x = 5
x += x + 1
print(x)

# Review


def print_hello():
    """This function prints hello."""
    print("hello")


def goodbye():
    print("Goodbye!")


def main():
    print_hello()
    goodbye()


# the main code, calling the function
print_hello()
print_hello()
goodbye()
main()


def print_number(my_number):
    print(my_number)


print_number(5)
print_number(6)
print_number(22)


# Add two numbers and return the results
def sum_two_numbers(a, b):
    result = a + b
    return result
# theres no print statement here
sum_two_numbers(5, 6)

my_result = sum_two_numbers(5, 6)
print(my_result)

def volume_cylinder(radius, height):
    pi = 3.141592653
    volume = pi * radius ** 2 * height
    return volume

# volume of a six pack:
my_volume = volume_cylinder(2.5, 5) * 6
print(my_volume)

# This function will print the result
def sum_print(a, b):
    result = a + b
    print(result)


# This function will return the result
def sum_return(a, b):
    result = a + b
    return result


# This code prints the sum of 4+4, because the function has a print
sum_print(4, 4)

# This code prints nothing, because the function returns, and doesn't print
sum_return(4, 4)

# This code will not set x1 to the sum.
# The sum_print function does not have a return statement, so it returns
# nothing!
# x1 actually gets a value of 'None' because nothing was returned
x1 = sum_print(4, 4)
print("x1 =", x1)

# This will set x2 to the sum and print it properly.
x2 = sum_return(4, 4)
print("x2 =", x2)

# none is the keyword for nothing



def calculate_average(a, b):
    """ Calculate an average of two numbers """
    result = (a + b) / 2
    return result


# Pretend you have some code here
x = 45
y = 56

# Wait how do I print the result of this?
average = calculate_average(x, y)
print(average)

# Define a simple function that sets x equal to 22
def f():
    x = 22

# Call the function
f()
# This fails, x only exists in f()
print(x)


# Create the x variable and set to 44
x = 44

# Define a simple function that prints x
def f():
    print(x)

# Call the function
f()



# Create the x variable and set to 44
x = 44

# Define a simple function that prints x
def f(x):
    x += 1
    print(x)

# Call the function
f(x)

# Define a simple function that prints x
def f(x):
    x += 1
    print(x)

# Set x
x = 10
# Call the function
f(x)
# Print x to see if it changed
print(x)

# Example 1
# start line 168, 153, 154, 159, 160, 165, 161, 155
def a():
    print("A start")
    b()
    print("A end")


def b():
    print("B start")
    c()
    print("B end")


def c():
    print("C start and end")

a()



# Example 2
def a(x):
    print("A start, x =", x)
    b(x + 1)
    print("A end, x =", x)


def b(x):
    print("B start, x =", x)
    c(x + 1)
    print("B end, x =", x)


def c(x):
    print("C start and end, x =", x)

a(5)


# Example 3
def a(x):
    x = x + 1

x = 3
a(x)

print(x)


# Example 4
def a(x):
    x = x + 1
    return x

x = 3
x = a(x)

print(x)


# Example 9
def a(x, y):
    x = x + 1
    y = y + 1
    print(x, y)


x = 10
y = 20
a(y, x)

