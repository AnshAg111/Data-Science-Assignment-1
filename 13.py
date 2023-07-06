# Write a Python program to generate all permutations of a given string.

def generate_permutations(s):
    permutations=[]
    if len(s)==0:
        return permutations
    if len(s)==1:
        return [s]
    for i in range(len(s)):
        chars=s[:i]+s[i+1:]
        list=generate_permutations(chars)
        for strs in list:
            permutations.append(s[i]+strs)
    return permutations

s=input("Enter a string:")
print("permutations of",s, "are",generate_permutations(s))