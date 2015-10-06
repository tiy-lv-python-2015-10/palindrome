##Cesar Marroquin
##Assignment 2 | Palindrome Test
#This program asks the user for one or more sentences and then lets the user know if it is a palindrome.

#steps
#1. Ask the user for input
    #ask for input and store it in a variable for future use
        #convert all text to same case to avoid comparison errors
        #remove all spaces and extra punctuation

#2. Perform palindrome test
    #check that string forwards is equivalent to string backwards
    #if string is the same, make variable ispalindrome True
    #else if the string is not the same make variable ispalindrome True

#3. Tell user wether or not given step is a palindrome
    #print a message that says input "is a palindrome" or input "is not a palindrome"
import re
user_input = str(input("Please enter some text to check if it is a palindrome: ")).lower()
print(user_input)

remove_space = re.compile( r'[^A-Za-z]')
print(remove_space.sub('', user_input))









"""
print(p.match("a"))
m = p.match("a")
print(m.group())
"""
