# Write a Python program to merge two sorted lists into a single sorted list.

def merge(l1, l2):
    n=len(l1)
    m=len(l2)
    i=0 
    j=0 
    l=[]
    while i<n and j<m:
        if l1[i]<=l2[j]:
            l.append(l1[i])
            i+=1
        else:
            l.append(l2[j])
            j+=1
    while(i<n):
        l.append(l1[i])
        i+=1
    while(j<m):
        l.append(l2[j])
        j+=1
    return l 

l1=[1,2,4,6,8]
l2=[2,3,5,7,9]
print("Lists after merging:", merge(l1, l2))