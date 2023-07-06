# Implement a function to find the sum of all numbers in a list.

def sum_of_list(l):
    n=len(l)
    if n==0:
        return 0
    sum=0 
    for i in range(0, n):
        sum+=l[i]
    return sum 

lst=[3,5,6,78,3,22,5,7]
print("The sum of all elements of the list is:", sum_of_list(lst))