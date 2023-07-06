# Implement a function to calculate the power of a number using recursion.

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

base=int(input("Enter a number: "))
exponent=int(input("Enter its power: "))
print(base, "raised to the power of", exponent, "is:", power(base, exponent))
