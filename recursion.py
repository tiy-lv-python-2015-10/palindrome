import re
def main_program():
    counter = 0
    user_input = re.sub( r'[^A-Za-z]', '', str(input("Please enter some text to check if it is a palindrome: ")))
    user_input_reverse = ""
    user_input_length = len(user_input)

    def reverse_string(counter2, user_input2, user_input_reverse2, user_input_length2):
        if counter2 == 0:
            user_input_reverse2 += user_input2[-1:]
        elif counter2 == -1:
            user_input_reverse2 = user_input_reverse2
        else:
            user_input_reverse2 = user_input_reverse2+user_input2[counter2: counter2+1]

        if counter2 >= ((user_input_length2*-1)+1):#BASE CASE
            reverse_string(counter2 - 1,user_input2, user_input_reverse2, user_input_length2)
        else:
            calculate_if_palindrome(counter2, user_input2, user_input_reverse2, user_input_length2)

    def calculate_if_palindrome(counter3, user_input3, user_input_reverse3, user_input_length3):
        theoretical_math_piece = ((str(str(re.match(str(user_input3), str(user_input_reverse3)))[24:34])) + " )")#the match reg ex function is applied to both the actual text and the reversed text and it compares the two and returns a math object based off of the result# after i recieve the math object i take out the span part of the object which looks similar to this <_sre.SRE_Match object; span=(4, 11), match='message'>
        actual_math_piece = ("span=(0, "+str(user_input_length3)+" )")#this is the span part that should be generated if text is palandromic
        print("thats a palindrome!") if actual_math_piece == theoretical_math_piece else print("nope that is not a palindrome!")

    reverse_string(counter, user_input, user_input_reverse, user_input_length)
main_program()
