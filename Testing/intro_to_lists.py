# Chapter 15: Introduction to Lists

# 3 is an integer <int>
# 3.241 is a floating point (decimal) <float>
# "text" is string data <str>
# True is boolean data <bool>

# With () its a tuple
# With [] its a list
# Without anything is a tuple
x = (2, 3, 4, 5)
print(x)
x = [2, 3, 4, 5]
print(x)
x = 2, 3, 4, 5
print(x)


x = [10, 20]
print(x)

# functions use (), lists use [] only
# computers start at 0, not 1 (so if you want to print 10 use 0, print 20 use 1)
x = [10, 20]
print(x[0])

# print the 8
# print(list name[index - position])
x = [3, 8, 7, 0, 5, 5, 2, 1]
print(x[1])

# Start at the end of the list
x = [3, 8, 7, 0, 5, 5, 2, 1]
print(x[-1])


# replaces the 7 with 22
x = [3, 8, 7, 0, 5, 5, 2, 1]
print(x)

x[2] = 22
print(x)


# you can create a list with nothing in it
x = []
print(x)

# len = length
x = [3, 7, 3]
size = len(x)
print(size)

# iterating through a list, we do not have a range
my_list = [101, 20, 10, 50, 60]
for item in my_list:
    print(item)

# Can store strings in lists too
my_list = ["spoon", "fork", "knife"]
for item in my_list:
    print(item)


# lists can contain other lists
my_list = [[2, 3], [4, 3], [6, 7]]
for item in my_list:
    print(item)

# print(list name[index][position within first index])
# this will print 4
my_list = [[2, 3], [4, 3], [6, 7]]
print(my_list[2][0])


# this also works to print the list
my_list = [2, 3, 6, 5, 8, 10]
for i in range(6):
    print(my_list[i])


my_list = [101, 20, 10, 50, 60]
for index in range(len(my_list)):
    print(my_list[index])


# looping with both an index and element
my_list = [2, 3, 6, 5, 8, 10, 31]
for index, value in enumerate(my_list):
    print(index, value)


# Adding to a list, adds 9 to the list
my_list = [2, 4, 5, 6]
print(my_list)
# append command
my_list.append(9)
print(my_list)

# creating a list of numbers from user input
my_list = []
for i in range(5):
    user_input = input("Enter an integer: ")
    user_input = int(user_input)
    my_list.append(user_input)
    print(my_list)


# Creating an array with 100 zeros
my_list = [0] * 100
print(my_list)


# summing the values in a list
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]
# initial sum should be zero
list_total = 0
# loop from 0 up the the number of elements in the array:
for index in range(len(my_list)):
    # add element 0, next 1, then 2, etc.
    list_total += my_list[index]
print(list_total)

# this also sums the values in a list
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]
# Initial sum should be zero
list_total = 0
# Loop through array, copying each item in the array into the variable named item
for item in my_list:
    # Add each item
    list_total += item
print(list_total)


my_list = [3, 4, 5]
print(my_list)
my_list[0] = 2
# lists you can change, tuples you can not change
# tuples you can work with faster -> which is why you would want to use them


# Copy of array to modify
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]
for item in my_list:
    item = item * 2
print(my_list)

# my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]
for i in range(len(my_list)):
    my_list[i] *= 2
print(my_list)


# Accessing a string as a list
x = "This is a sample string"
# x = "0123456789"
print("x=", x)
# Accessing the first character ("T")
print("x[0]=", x[0])
# Accessing the second character ("h")
print("x[1]=", x[1])
# Accessing from the right side ("g")
print("x[-1]=", x[-1])
# Access 0-5 ("This i")
print("x[:6]=", x[:6])
# Access 6 to the end ("s a sample string")
print("x[6:]=", x[6:])
# Access 6-8 ("s a")
print("x[6:9]=", x[6:9])


# Adding and multiplying strings
a = "Hi"
b = "There"
c = "!"
print(a + b)
print(a + b + c)
print(3 * a)
print(a * 3)
print((a * 2) + (b * 2))


# Getting the length of a string or list
a = "Hi There"
print(len(a))

b = [3, 4, 5, 6, 76, 4, 3, 3]
print(len(b))


for character in "This is a test.":
    print(character)


months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))
month = months[(n - 1) * 3:(n - 1) * 3 + 3]
print(month)


# Caesar Cipher
plain_text = "This is a test. ABC abc"
for c in plain_text:
    print(c, end=" ")

plain_text = "This is a test. ABC abc"
for c in plain_text:
    # taking the letter and finding out what the number is (ordinate value)
    x = ord(c)
    # take the same numbers and make them bigger
    x = x + 1
    # takes the number and makes it into a letter (character value)
    c2 = chr(x)
    print(c2, end="")

print()

# print the encrypted message:
# encrypted_text = ""
# for c in encrypted_text:
# (indent) x = ord(c)
# (indent) x = x - 1
# (indent) c2 = chr(x)
# (indent) print(c2, end="")

my_list = [-4, -2, -56, -2, -0]
biggest_number = my_list[0]
for item in my_list:
    if item > biggest_number:
        biggest_number = item
print(biggest_number)

my_list = [-4, -2, -56, -2, -0]
positive_outlook_list = []
for item in my_list:
    if item > 0:
        positive_outlook_list.append(item)
print(positive_outlook_list)
