# Write a Python program to check if two strings are anagrams of each other.

def is_anagram(s1, s2):
    return sorted(s1)==sorted(s2)

str1=input("Enter the first string:")
str2=input("Enter the second string:")
if(is_anagram(str1, str2)):
    print(str2, "is anagram of ", str1)
else:
    print(str2, "is not a anagram of", str1)