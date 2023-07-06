# Implement a function to check if a given number is prime.

def isprime(num):
    for i in range(2, num):
        if num%i==0:
            return False
    return True 

n=int(input("Enter a no.\n"))
if isprime(n):
    print(n, "is prime")
else:
    print(n, "is not prime")