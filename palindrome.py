import re


#reverses a string
def backwards(statement):
    backwards = ""

    for count in range(len(statement)):
        backwards = backwards + statement[-1 - count]
    return backwards

#checks to see if a string is a palindrome
def is_palindrome(statement):
    if len(statement) <= 1:
        return True
    elif statement[0] == statement[-1]:
        is_palindrome(statement[1:-1])
        return True
    else:
        return False

#takes user input and strips it of all numbers, special chars, and whitespace
user_input = input("Please enter your word or sentence > ")
stripped = re.sub('[^A-Za-z]', '', user_input).lower()

#checks to see if it's a palindrome twice
if is_palindrome(stripped) and stripped == backwards(stripped):
    print("Yes it is a palindrome!")
else:
    print("No it is not a palindrome!")
