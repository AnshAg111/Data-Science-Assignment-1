#  Write a Python program to sort a list of integers in ascending order.

def sort(l):
    n=len(l)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if l[j]<l[i]:
                l[j], l[i]=l[i], l[j]
    return l

lst=[4,5,6,7,43,2,65,8]
print("The sorted list is",sort(lst))