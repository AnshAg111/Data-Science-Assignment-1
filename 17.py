# Write a Python program to find the intersection of two lists.

def intersection(l1, l2):
    res=[]
    for i in l1:
        if i in l2 and i not in res:
            res.append(i)
    return res 

l1=[4,6,7,8,4]
l2=[2,4,5,6,7,8]
print("Intersection of two lists contains:", intersection(l1, l2))

