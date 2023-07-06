# Write a program to find the median of a list of numbers.

def median(l):
    sorted_list=sorted(l)
    n=len(sorted_list)
    if n%2==0:
        med=(sorted_list[n/2-1]+sorted_list[n/2])/2
    else:
        med=sorted_list[n//2]
    return med 

lst=[2,4,5,4,3,67,85,3,7,4,7]
print("The median of the given list is", median(lst))