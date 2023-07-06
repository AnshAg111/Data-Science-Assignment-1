#  Implement a function to remove duplicate elements from a list.

def remove_duplicates(l):
    return list(set(l))

lst=[2,4,6,43,7,5,3,2]
print("unique list:", remove_duplicates(lst))