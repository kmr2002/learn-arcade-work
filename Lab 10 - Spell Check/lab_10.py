"""
Lab 10 = Spell Check
"""

import re


# This function take sin a line of text and returns
# a list of words in the line
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    # Reading into an array
    my_file = open("dictionary.txt")
    dictionary_list = []
    for line in my_file:
        line = line.strip()
        dictionary_list.append(line)
    my_file.close()
    print("There were", len(dictionary_list), "names in the file.")

    # linear search
    i = 0
    while i < len(dictionary_list) and dictionary_list[i] == "Key":
        i += 1

    if i == len(dictionary_list):
        print("The name was not in the list")
    else:
        print("The name is at position", i)

    # Open Alice in Wonderland file
    my_file = open("AliceInWonderLand200.txt")
    for line in my_file:
        line = line.strip()
        split_line(line)
    my_file.close()


main()
