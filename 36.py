#  Implement a function to calculate the product of all elements in a list.

def product(l):
    if len(l)==0:
        return None
    p=1 
    for i in l:
        p*=i 
    return p 

lst=[3,5,7,3,7,8]
print("The product of all numbers is:",product(lst))
