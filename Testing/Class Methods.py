"""
Chapter 17: Class Methods
"""

# use classes to group data together
# attributes = variables that are part of the class, "has-a"
# object is an instance of a class, class = dog, object = fluffy, spot
# methods = functions inside a class
# period = dot operator

# Static Variables, use when you need common data shared between all objects

# Defines a class:
class Dog:
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    # A function in a class is called a method:
    def bark(self):
        if self.weight < 10:
            print("Yip says", self.name)
        else:
            print("Woof says", self.name)


def main():
    # Creates a class:
    my_dog = Dog()
    my_dog.name = "Scout"
    my_dog.weight = 20
    my_dog.age = 3

    my_other_dog = Dog()
    my_other_dog.name = "Xander"
    my_other_dog.weight = 20
    my_other_dog.age = 3

    my_dog.bark()
    my_other_dog.bark()


main()
# encapsulate all data for it in the class, simplifies code outside of it significantly


# References
class Person:
    # 1 Method
    def __init__(self):
        # 2 Attributes
        self.name = ""
        self.money = 0


def main():
    # Person points to the class, bob points to person instance
    # References = Pointers, where in memory the stuff is
    bob = Person()
    bob.name = "Bob"
    bob.money = 100

    # nancy = bob would make them the same person, only printing 1 person(Person() - 1)
    nancy = Person()
    nancy.name = "Nancy"

    print(bob.name, "has", bob.money, "dollars.")
    print(nancy.name, "has", nancy.money, "dollars.")


main()


# Functions and References
# Uses class Person(): from above
# Give bob money
def give_money1(person):
    person.money += 100


def main():
    bob = Person()
    bob.name = "Bob"
    bob.money = 100

    give_money1(bob)
    print(bob.money)


main()


# Class definition for a boat
class Boat:
    def __init__(self):
        self.tonnage = 0
        self.name = ""
        self.is_docked = True

    def dock(self):
        if self.is_docked:
            print("You are already docked.")
        else:
            self.is_docked = True
            print("Docking")

    def undock(self):
        if not self.is_docked:
            print("You aren't docked.")
        else:
            self.is_docked = False
            print("Undocking")


# Now make a submarine
# Boat = parent class, Submarine = child class -> child classes inherit all parent class stuff
class Submarine(Boat):
    def submerge(self):
        print("Submerge!")


# Person, Employee, Customer Classes
# class Person(): -> class Employee(Person): -> class Customer(Person):

# Overriding Constructors
# Refers back to the parent not override(create new):
# def __init__(self): -> super().__init__()
# only override if you want to do a completely different report, otherwise above

"""
Is-A
Has-A

kitchen "is-a" room, kitchen "has-a" stove
more generic one on top in parent class, more specific in child class
"""
