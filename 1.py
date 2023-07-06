# Write a Python program to reverse a string without using any built-in string reversal functions.
def reverse_string(s):
    rev=""
    for i in range(len(s)-1, -1, -1):
        rev+=s[i]
    return rev 

s=input("Enter a string: ")
rev=reverse_string(s)
print("Reversed string: ", rev)