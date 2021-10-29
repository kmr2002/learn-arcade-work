# Chapter 16: Classes

name = "Link"
outfit = "Green"
max_hit_points = 50
current_hit_points = 50
armor_amount = 6
max_speed = 10


def display_character(name, outfit, max_hit_points, current_hit_points, armor, max_speed):
    print(name, outfit, max_hit_points, current_hit_points)


# capitalize the class name
class Character:
    """
    This is a class that represents the player character.
    """
    def __init__(self):
        """ This is a method, function in a class that sets up the variable in the object. """
        # self = "mine"
        x = 0
        self.name = ""
        self.outfit = ""
        self.max_hit_points = 0
        self.current_hit_points = 0
        self.armor_amount = 0
        self.max_speed = 0


# US Mailing address example
class Address:
    """ Hold all the fields for a mailing address. """
    def __init(self):
        """ Set up the address fields. """
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""


def main():
    # the () after Address creates an instance
    # can have class with no instances
    home_address = Address()
    home_address.name = "John Smith"
    home_address.line1 = "701 N. C Street"
    home_address.line2 = "Carver Science Center"
    home_address.city = "Indianola"
    home_address.state = "IA"
    home_address.zip = "50125"


    # Create another address
    # the () after Address ARE IMPORTANT!!!
    vacation_home_address = Address()
    # Set the fields in the address
    vacation_home_address.name = "John Smith"
    vacation_home_address.line1 = "1122 Main Street"
    vacation_home_address.line2 = ""
    vacation_home_address.city = "Panama City Beach"
    vacation_home_address.state = "FL"
    vacation_home_address.zip = "32407"

    print("The client's main home is in " + home_address.city)
    print("His vacation home is in " + vacation_home_address.city)
main()


# Customizing the Constructor
class Dog():
    def __init__(self, name):
        """ Constructor """
        # self.name and name are completely different
        self.name = name
        print("A dog has been born")

def main():
    # This creates the dog
    my_dog = Dog("Scout")
    print(f"The dog's name is: {my_dog.name}")

    # This creates another dog
    my_other_dog = Dog("Xander")
    print(f"The dog's name is: {my_other_dog.name}")
main()


# Address class with Init Parameters
class Address():
    def __init__(self, line1, line2, city, state, zip, country):
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country


def main():
    # This creates the address
    my_address = Address("701 N. C Street",
                         "Carver Science Building",
                         "Indianola",
                         "IA",
                         "50125",
                          "USA")
main()


# Typing attributes
class Person:
    def __init(self):
        self.name: str = "A"

mary = Person()
mary.name = 22


@dataclass
class Address:
    name: str = ""
    line1: str = ""
    line2: str = ""
    city: str = ""
    state: str = ""
    zip_code: str = ""
