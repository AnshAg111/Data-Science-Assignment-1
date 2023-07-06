#  Write a program to find the greatest common divisor (GCD) of two numbers.

# using euclid's division algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter first no.: "))
num2 = int(input("Enter second no.: "))
print("Greatest Common Divisor:", gcd(num1, num2))
