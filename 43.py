# Write a program to find the number of occurrences of a given element in a list.

def frequency(num, lst):
    c=0 
    for i in lst:
        if i==num:
            c+=1
    return c 

my_list=[3,5,6,7,8,3,2,5]
n=int(input("Enter the number: "))
print("The no. of occurrences of", n,"is",frequency(n, my_list))