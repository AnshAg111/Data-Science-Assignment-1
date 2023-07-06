# Write a Python program to remove all duplicates from a string.

def remove_duplicates(string):
    seen = set()
    result = ""

    for char in string:
        if char not in seen:
            result += char
            seen.add(char)

    return result

input_string = input("Enter a string: ")
print("String after removing duplicates:", remove_duplicates(input_string))
