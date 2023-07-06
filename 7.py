# Write a program to calculate the factorial of a given number.

def factorial(num):
    fact=1
    for i in range(1, num+1):
        fact=fact*i 
    return fact 
n=int(input("Enter a no.\n"))
print("factorial of",n,"is",factorial(n))