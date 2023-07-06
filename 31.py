# Write a program to find the sum of all even numbers in a list.

def sumOfEvenNumbers(l):
    sum=0 
    for i in l:
        if i%2==0:
            sum+=i 
    return sum 

lst=[2,4,5,7,4,2,6,8]
print("The sum of all even numbers is:",sumOfEvenNumbers(lst))