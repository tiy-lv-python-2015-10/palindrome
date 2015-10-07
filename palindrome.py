import re
phrase = input("Enter text here: ")

def space_remover(phrase):
    """ Removes the spaces from the string"""
    return re.sub(r'[^A-Za-z]', "", phrase)


def palindrome_test(phrase):
    """ Goes through and reads the string to see if it is read the same way forwards and back"""
    print("Reading front to back...")
    counter = 0
    for letter in phrase:
        first_letter = 0
        last_letter = -1
        print("Adding a counter")
        counter += 1
        print("Checking each letter")
        if phrase[first_letter] == phrase[last_letter]:
            first_letter = first_letter + 1
            last_letter = last_letter - 1
        else:
            counter += 1
    if counter == len(phrase):
        print("it is a palindrome!")
    else:
        print("it is not a palindrome...")
test = space_remover(phrase.lower())
palindrome_test(test)


def easy_way(phrase):
    """flips the string backwards and compares it to the original"""
    if phrase == phrase[::-1]:
        print("it is a palindrome!")
    else:
        print("it is not a palindrom...")
easy_way(test)
