import re
def main_program():
    user_input = re.sub( r'[^A-Za-z]', '', str(input("Please enter some text to check if it is a palindrome: ")))
    user_input_length = len(user_input)
    user_input_reverse = ""
    for counter in range(0, (user_input_length*-1)-1,-1):
        if counter == 0:
            user_input_reverse += user_input[-1:]
        elif counter == -1:
            continue
        else:
            user_input_reverse += user_input[counter: counter+1]
    theoretical_math_piece = ((str(str(re.match(str(user_input), str(user_input_reverse)))[24:34])) + " )")#the match reg ex function is applied to both the actual text and the reversed text and it compares the two and returns a math object based off of the result# after i recieve the math object i take out the span part of the object which looks similar to this <_sre.SRE_Match object; span=(4, 11), match='message'>
    actual_math_piece = ("span=(0, "+str(user_input_length)+" )")#this is the span part that should be generated if text is palandromic
    print("thats a palindrome!") if actual_math_piece == theoretical_math_piece else print("nope that is not a palindrome!")
main_program()
