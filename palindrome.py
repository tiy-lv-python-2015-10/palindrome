import re


user_sentence = input("Please enter your sentence > ")

stripped_sentence = re.sub('[^A-Za-z]', '', user_sentence).lower()

backwards = []
count = 0
count_back = -1

while count < len(stripped_sentence):
    backwards.append(stripped_sentence[count_back])
    count_back -= 1
    count += 1

backwards_sentence = "".join(backwards)

if stripped_sentence == backwards_sentence:
    print("Yes it is a palindrome!")
else:
    print("No it is not a palindrome!")
