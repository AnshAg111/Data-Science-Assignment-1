#  Implement a function to check if a given number is a perfect number.

def isPerfect(n):
    sumOfFactors=0
    for i in range(1,n):
        if n%i==0:
            sumOfFactors+=i 
    if sumOfFactors==n:
        return True
    return False
    
num=int(input("Enter a number\n"))
if isPerfect(num):
    print(num, "is a perfect number")
else:
    print(num, "num is not a perfect number")