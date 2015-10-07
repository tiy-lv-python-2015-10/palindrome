import re

word_to_your_mom = input("enter your word: ")

def palindrome_or_not(word_to_your_mom):
    if len(word_to_your_mom) < 2:
        return True
    elif word_to_your_mom[0] != word_to_your_mom[-1]:
        return False
    else:
        return palindrome_or_not(word_to_your_mom[1:-1])

if palindrome_or_not(word_to_your_mom):
    print("is a palindrome")
else:
    print("is not a palindrome")




palindrome_or_not(word_to_your_mom)
