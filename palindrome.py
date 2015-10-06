import re


user_input = input("Please enter your word or sentence > ")
stripped = re.sub('[^A-Za-z]', '', user_input).lower()

backwards = ""

for count in range(len(stripped)):
    backwards = backwards + stripped[-1 - count]

if stripped == backwards:
    print("Yes it is a palindrome!")
else:
    print("No it is not a palindrome!")
