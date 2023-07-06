# Write a program to find the common elements between two lists.

def common_elements(l1, l2):
    return list(set(l1) & set(l2))  

list1=[33,46,235,76,33,6,34]
list2=[33,55,65,32,64,3,45,46]
print(f"common elements are {common_elements(list1, list2)}")