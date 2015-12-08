# boolean True
while True:
# give x a value and print
    x = input("Enter a word: ")
# join all NON white spaces and split nothing
    x = ''.join(x.split())
# print backward
    print(x[::-1])
# if yes print palindrome
    if x == x[::-1]:
        print("It's a palindrome")
# if not NOT print palindrome
    else:
        print("It's NOT a palindrome")