#  Write a program to remove all vowels from a given string.

def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in string if char not in vowels)

s = input("Enter a string: ")
print("String without vowels:", remove_vowels(s))
