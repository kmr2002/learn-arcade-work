"""

Lab 10 - Spell Check
"""

import re


# This functions takes in a line of text and returns
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
    print("---Linear Search---")

    # Linear Search
    i = 0
    with open("AliceInWonderLand200.txt") as my_text:
        for line in my_text:
            i += 1
            word_list = split_line(line)
            for word in word_list:
                key = word.upper()
                current_position = 0
                while current_position < len(dictionary_list) and dictionary_list[current_position] != key:
                    current_position += 1
                if current_position >= len(dictionary_list):
                    print("line", i, "possible misspelled word:", word)

    print("---binary search---")
    i = 0
    with open("AliceInWonderLand200.txt") as my_text:
        for line in my_text:
            i += 1
            word_list = split_line(line)
            for word in word_list:
                key = word.upper()
                lower_bound = 0
                upper_bound = len(dictionary_list) - 1
                found = False

                while lower_bound <= upper_bound and not found:
                    middle = (lower_bound + upper_bound) // 2
                    if dictionary_list[middle] < key:
                        lower_bound = middle + 1
                    elif dictionary_list[middle] > key:
                        upper_bound = middle - 1
                    else:
                        found = True

                if not found:
                    print("Line", i, "possible misspelled word:", word)

main()