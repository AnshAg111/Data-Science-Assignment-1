# Write a Python program to find the second largest number in a list.
import sys 
def second_largest(l):
    if len(l)<2:
        return None
    largest1=float('-inf')
    largest2=float('-inf')
    for i in l:
        if i>largest1:
            largest2=largest1
            largest1=i 
        elif i>largest2 and i!=largest1:
            largest2=i 
    return largest2

lst=[4,35,63,24,64]
print("Second largest number in the list is:", second_largest(lst))