# Implement a function to count the occurrence of each element in a list.

def count(l):
    occurence={}
    for i in l:
        if i in occurence:
            occurence[i]+=1
        else:
            occurence[i]=1
    return occurence

lst=[3,5,7,4,2,6,8,6,5,4,3]
print(count(lst))