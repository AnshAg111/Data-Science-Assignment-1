# Implement a function to calculate the Fibonacci sequence up to a given number of terms.

def fibonacci(n):
    a=1 
    b=1 
    print("fibonacci series upto",n,"terms is:")
    if(n>=1):
        print(a)
    if(n>=2):
        print(b)

    for i in range(3, n+1):
        c=a+b 
        print(c)
        a=b
        b=c
n=int(input("Enter the no. of terms\n")) 
fibonacci(n)