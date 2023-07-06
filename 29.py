# Write a Python program to check if a given string is a valid palindrome ignoring non-alphanumeric characters.

import re

def is_valid_palindrome(string):
    alphanumeric_string = re.sub('[^a-zA-Z0-9]', '', string).lower()
    return alphanumeric_string == alphanumeric_string[::-1]

input_string = input("Enter a string: ")
result = is_valid_palindrome(input_string)
if result:
    print("The string is a valid palindrome.")
else:
    print("The string is not a valid palindrome.")
