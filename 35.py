# Write a program to check if a given number is a perfect square.

import math
def isPerfectSquare(num):
    return math.sqrt(num)==int(math.sqrt(num))

n=int(input("Enter a number: "))
if(isPerfectSquare(n)):
    print(n,"is perfect square")
else:
    print(n, "is not a perfect square")