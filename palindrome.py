users_pally = input("test subject:")
import re
users_pally = users_pally.lower()
users_pally = re.sub("[^A-Za-z]", "", users_pally)
def users(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    else:
        return users(word[1:-1])

users(users_pally)
def answer(a, b):
    if users(b):
        print("is a palindrome")
    else:
        print("is not a palindrome")

answer(users, users_pally)
