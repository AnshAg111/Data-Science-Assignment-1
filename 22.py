#  Implement a function to find the first non-repeating character in a string.

def first_non_repeating(string):
    char_count = {}
    for i in string:
        char_count[i] = char_count.get(i, 0) + 1
    for i in string:
        if char_count[i] == 1:
            return i
    return None

s = input("Enter any string: ")
result=first_non_repeating(s)
if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found.")
