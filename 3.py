# Write a program to find the largest element in a given list.

def find_largest(l):
    if not l:
        return None
    largest=l[0]
    for i in l:
        if i>largest:
            largest=i 
    return largest 

lst=[5, 7, 4, 6, 3, 2]
print("The largest no. in the list is:", find_largest(lst))