# Write a Python program to check the validity of password input by users.
# Validation :
# a. At least 1 letter between [a-z] and 1 letter between [A-Z].
# b. At least 1 number between [0-9].
# c. At least 1 character from [$#@].
# d. Minimum length 6 characters.
# e. Maximum length 16 characters
import re
pas=input("Enter password")
for i in pas:
    if (len(pas)<6 or len(pas)>12):
        break
    elif not re.search("[a-z]",pas):
        break
    elif not re.search("[0-9]",pas):
        break
    elif not re.search("[A-Z]",pas):
        break
    elif not re.search("[$#@]",pas):
        break
    elif re.search("\s",pas):
        break
    else:
        print("Valid Password")
        x=False
        break
    