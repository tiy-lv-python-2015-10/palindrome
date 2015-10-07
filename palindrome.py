import re
user_input = str(input("Please enter some text to check if it is a palindrome: ")).lower()
re.sub( r'[^A-Za-z]', '', user_input)
user_input_length = len(user_input)
counter = 0
user_input_reverse = ""

while counter >= user_input_length*-1:
    if counter == 0:
        user_input_reverse = user_input_reverse+user_input[-1:]
        counter = counter - 1
    elif counter == -1:
        counter = counter - 1
    else:
        user_input_reverse = user_input_reverse+user_input[counter: counter+1]
        counter = counter - 1

input_match = re.match(str(user_input), str(user_input_reverse))
reg_ex_match = str(input_match)
y = reg_ex_match[24:34]
y = str(y)
x = (y + " )")
q = str(user_input_length)
z = ("span=(0, "+q+" )")
if z==x:
    print("thats a palindrome!")
else:
    print("nope that is not a palindrome!")
