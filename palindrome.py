users_pally = input("test subject:")
import re
users_pally = users_pally.lower()
users_pally = re.sub("[^A-Za-z]", "", users_pally)
rev_str = users_pally[::-1]
if list(users_pally) == list(rev_str):
    print("is a palindrome")
else:
    print("is not a palindrome")
