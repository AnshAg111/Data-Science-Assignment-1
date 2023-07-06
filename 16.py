# Implement a function to check if a given list is sorted in non-decreasing order.

def isIncreasing(l):
    n=len(l)
    for i in range(1, n):
        if l[i]<l[i-1]:
            return False
    return True

lst=[3,4,5,6,7,8,3]
if(isIncreasing(lst)):
    print("The given list is sorted in non-decreasing order")
else:
    print("The given list is not sorted")