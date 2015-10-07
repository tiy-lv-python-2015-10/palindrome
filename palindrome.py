##Cesar Marroquin
##Assignment 2 | Palindrome Test
#This program asks the user for one or more sentences and then lets the user know if it is a palindrome.

#steps
#1. Ask the user for input
    #ask for input and store it in a variable for future use
        #convert all text to same case to avoid comparison errors
        #remove all spaces and extra punctuation

#2. Perform palindrome test
    #reverse order of string
    #check that string forwards is equivalent to string backwards
    #if string is the same, make variable ispalindrome True
    #else if the string is not the same make variable ispalindrome True

#3. Tell user wether or not given step is a palindrome
    #print a message that says input "is a palindrome" or input "is not a palindrome"
import re
user_input = str(input("Please enter some text to check if it is a palindrome: ")).lower()
user_input = re.sub( r'[^A-Za-z]', '', user_input)#this removes the spaces and other characters

user_input_length = len(user_input)#creates a variable with the length of the string
#print("the lenght of the string is ",user_input_length)#prints the lenght of the string
#print(remove_space.sub('', user_input))

counter = 0
user_input_reverse = ""
while counter >= user_input_length*-1:
    #print("it works!", counter)
    if counter == 0:
        print(user_input[-1:],counter)
        user_input_reverse = user_input_reverse+user_input[-1:]
        print(user_input_reverse)
        counter = counter - 1
    elif counter == -1:
        counter = counter - 1
    else:
        print(user_input[counter: counter+1],counter)
        user_input_reverse = user_input_reverse+user_input[counter: counter+1]
        print(user_input_reverse)
        counter = counter - 1

#print(user_input_reverse)

#sprint(re.match(str(user_input), str(user_input_reverse)))

input_match = re.match(str(user_input), str(user_input_reverse))
str_input_match = str(input_match)
#print(str_input_match[24:34], ")")
y = str_input_match[24:34]
print(y)
y = str(y)
print(y)
x = (y + " )")
print(x ,"this is x")

q = str(user_input_length)

print("span=(0,",str(user_input_length),")")
z = ("span=(0, "+q+" )")
print(z)
math_match = re.match(z, x)#str_input_match[24:35])
#"span=(0,\",user_input,\")"

print(input_match, "this is the returned math object")
print(z)
print(x)

print(math_match, "this is the returned math object checked to see if it matches")

print(z==x)

if z==x:
    print("thats a palindrome!")
else:
    print("nope that is not a palindrome!")
