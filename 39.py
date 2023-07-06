#  Write a program to find the sum of digits of a given number.

def sumOfDigits(n):
    if n<0:
        n=abs(n)
    sum=0
    while(n!=0):
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum 

num=int(input("Enter a number\n"))

print("sum of digits of",num,"is",sumOfDigits(num))